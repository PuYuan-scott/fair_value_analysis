#!/usr/bin/env python3
"""Reproducible KO DCF using only the Python standard library.

Inputs:
    data/facts.csv
    data/assumptions.csv

Outputs:
    outputs/derived_inputs.csv
    outputs/forecast.csv
    outputs/valuation_summary.csv
    outputs/equity_bridge.csv
    outputs/irs_scenarios.csv
    outputs/sensitivity.csv
    outputs/fair_value_summary.csv
    outputs/validation_checks.csv
    outputs/scenario_forecast.csv
    outputs/operating_scenarios.csv
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"


def load_values(path: Path) -> dict[str, str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["id"]: row["value"] for row in csv.DictReader(handle)}


def write_csv(name: str, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    OUTPUTS.mkdir(exist_ok=True)
    with (OUTPUTS / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: (f"{value:.9f}".rstrip("0").rstrip(".") if isinstance(value, float) else value)
                    for key, value in row.items()
                }
            )


def f(values: dict[str, str], key: str) -> float:
    return float(values[key])


facts = load_values(DATA / "facts.csv")
assumptions = load_values(DATA / "assumptions.csv")

with (DATA / "scenario_assumptions.csv").open(newline="", encoding="utf-8") as handle:
    scenario_inputs = list(csv.DictReader(handle))

# 1) Normalize the operating base and remove CCBA for a clean post-sale forecast.
ccba_revenue = f(facts, "fy2025_reported_revenue") * (
    f(facts, "fy2025_bottling_revenue_share")
    - f(facts, "fy2025_bottling_ex_ccba_share")
)
proforma_2025_revenue = f(facts, "fy2025_comparable_revenue") - ccba_revenue
proforma_2026_revenue = proforma_2025_revenue * (
    1 + f(assumptions, "proforma_2026_growth")
)

# 2) Calculate WACC. Market price affects only debt/equity weights, not fair value.
debt = (
    f(facts, "q2_2026_loans_notes")
    + f(facts, "q2_2026_current_debt")
    + f(facts, "q2_2026_long_term_debt")
)
market_equity = (
    f(facts, "market_price_for_weights")
    * f(facts, "q2_2026_diluted_shares")
)
equity_weight = market_equity / (market_equity + debt)
debt_weight = 1 - equity_weight
cost_of_equity = f(assumptions, "risk_free_rate") + (
    f(assumptions, "adjusted_beta") * f(facts, "mature_market_erp")
)
after_tax_cost_of_debt = f(assumptions, "pretax_cost_of_debt") * (
    1 - f(assumptions, "tax_rate_2027")
)
calculated_wacc = (
    equity_weight * cost_of_equity + debt_weight * after_tax_cost_of_debt
)
wacc = f(assumptions, "wacc_adopted")

# 3) Explicit accounting FCFF forecast.
forecast_rows: list[dict[str, object]] = []
revenue = proforma_2026_revenue
first_discount = f(assumptions, "first_cash_flow_discount_years")
for index, year in enumerate(range(2027, 2032)):
    growth = f(assumptions, f"revenue_growth_{year}")
    margin = f(assumptions, f"operating_margin_{year}")
    tax_rate = f(assumptions, f"tax_rate_{year}")
    da_ratio = f(assumptions, f"da_revenue_{year}")
    capex_ratio = f(assumptions, f"capex_revenue_{year}")
    delta_nwc_ratio = f(assumptions, f"delta_nwc_revenue_{year}")

    revenue *= 1 + growth
    ebit = revenue * margin
    nopat = ebit * (1 - tax_rate)
    da = revenue * da_ratio
    capex = revenue * capex_ratio
    delta_nwc = revenue * delta_nwc_ratio
    fcff = nopat + da - capex - delta_nwc
    discount_years = first_discount + index
    discount_factor = 1 / ((1 + wacc) ** discount_years)
    pv_fcff = fcff * discount_factor
    forecast_rows.append(
        {
            "year": year,
            "revenue_usd_bn": revenue,
            "revenue_growth": growth,
            "operating_margin": margin,
            "ebit_usd_bn": ebit,
            "tax_rate": tax_rate,
            "nopat_usd_bn": nopat,
            "da_revenue_ratio": da_ratio,
            "da_usd_bn": da,
            "capex_revenue_ratio": capex_ratio,
            "capex_usd_bn": capex,
            "delta_nwc_revenue_ratio": delta_nwc_ratio,
            "delta_nwc_usd_bn": delta_nwc,
            "fcff_usd_bn": fcff,
            "discount_years": discount_years,
            "discount_factor": discount_factor,
            "pv_fcff_usd_bn": pv_fcff,
        }
    )

# 4) Terminal period uses ROIC to force growth-related reinvestment.
terminal_growth = f(assumptions, "terminal_growth")
terminal_roic = f(assumptions, "terminal_roic")
terminal_nopat = float(forecast_rows[-1]["nopat_usd_bn"]) * (1 + terminal_growth)
terminal_reinvestment_rate = terminal_growth / terminal_roic
terminal_fcff = terminal_nopat * (1 - terminal_reinvestment_rate)
terminal_value = terminal_fcff / (wacc - terminal_growth)
terminal_discount_years = f(assumptions, "terminal_discount_years")
terminal_discount_factor = 1 / ((1 + wacc) ** terminal_discount_years)
pv_terminal_value = terminal_value * terminal_discount_factor
pv_explicit_fcff = sum(float(row["pv_fcff_usd_bn"]) for row in forecast_rows)
enterprise_value = pv_explicit_fcff + pv_terminal_value

# 5) EV-to-equity bridge. Equity-method earnings are outside EBIT, so the
# corresponding investments are added separately at reported carrying value.
ccba_retained_value = (
    f(facts, "ccba_total_equity_value") * f(facts, "ccba_retained_stake")
)
bridge_rows = [
    ("Fair enterprise value", enterprise_value, "DCF output"),
    ("Debt", -debt, "Loans + current maturities + long-term debt"),
    (
        "Cash and short-term investments",
        f(facts, "q2_2026_cash_short_term_investments"),
        "Q2 2026 balance sheet",
    ),
    (
        "Marketable securities",
        f(facts, "q2_2026_marketable_securities"),
        "Q2 2026 balance sheet",
    ),
    (
        "Equity-method investments",
        f(facts, "q2_2026_equity_method_investments"),
        "Added because equity income is below operating income",
    ),
    (
        "CCBA sale cash consideration",
        f(facts, "ccba_sale_cash"),
        "Pending transaction consideration",
    ),
    (
        "CCBA retained 25% interest",
        ccba_retained_value,
        "25% x $3.4bn implied equity value",
    ),
    (
        "Noncontrolling interests",
        -f(facts, "q2_2026_nci"),
        "Full reported balance deducted conservatively",
    ),
]
equity_value_before_irs = sum(value for _, value, _ in bridge_rows)
shares = f(facts, "q2_2026_diluted_shares")
core_fair_value_per_share = equity_value_before_irs / shares

# 6) IRS litigation. Core DCF excludes both the refund asset and adverse case.
irs_refund = f(facts, "irs_deposit") + f(facts, "irs_deposit_interest")
irs_remaining = f(facts, "irs_remaining_liability")
proforma_2026_margin = 0.336  # midpoint consistent with first explicit margin
proforma_2026_ebit = proforma_2026_revenue * proforma_2026_margin
annual_future_tax_drag = proforma_2026_ebit * f(facts, "irs_future_tax_rate_increase")
pv_future_tax_drag = annual_future_tax_drag / (wacc - terminal_growth)

irs_rows: list[dict[str, object]] = []
for win_probability in (0.50, 0.60, 0.70):
    expected_adjustment = (
        win_probability * irs_refund
        - (1 - win_probability) * (irs_remaining + pv_future_tax_drag)
    )
    adjusted_equity_value = equity_value_before_irs + expected_adjustment
    irs_rows.append(
        {
            "win_probability": win_probability,
            "refund_if_win_usd_bn": irs_refund,
            "remaining_liability_if_loss_usd_bn": irs_remaining,
            "annual_future_tax_drag_usd_bn": annual_future_tax_drag,
            "pv_future_tax_drag_if_loss_usd_bn": pv_future_tax_drag,
            "expected_adjustment_usd_bn": expected_adjustment,
            "adjusted_equity_value_usd_bn": adjusted_equity_value,
            "adjusted_fair_value_per_share": adjusted_equity_value / shares,
        }
    )

base_win_probability = f(assumptions, "irs_base_win_probability")
base_irs = next(row for row in irs_rows if row["win_probability"] == base_win_probability)
risk_adjusted_fair_value = float(base_irs["adjusted_fair_value_per_share"])

# 6b) Integrated operating scenarios. Each case starts from the same 2026
# post-CCBA revenue base and changes a coherent set of operating, reinvestment,
# discount-rate, terminal, and litigation assumptions.
scenario_forecast_rows: list[dict[str, object]] = []
operating_scenario_rows: list[dict[str, object]] = []
non_ev_bridge = equity_value_before_irs - enterprise_value

for scenario in scenario_inputs:
    scenario_name = scenario["scenario"]
    scenario_label = scenario["label"]
    scenario_revenue = proforma_2026_revenue
    scenario_wacc = float(scenario["wacc"])
    scenario_tax = float(scenario["tax_rate"])
    scenario_da_ratio = float(scenario["da_revenue"])
    scenario_nwc_ratio = float(scenario["delta_nwc_revenue"])
    scenario_rows: list[dict[str, object]] = []

    for index, year in enumerate(range(2027, 2032)):
        scenario_growth = float(scenario[f"revenue_growth_{year}"])
        scenario_margin = float(scenario[f"operating_margin_{year}"])
        scenario_capex_ratio = float(scenario[f"capex_revenue_{year}"])
        scenario_revenue *= 1 + scenario_growth
        scenario_ebit = scenario_revenue * scenario_margin
        scenario_nopat = scenario_ebit * (1 - scenario_tax)
        scenario_da = scenario_revenue * scenario_da_ratio
        scenario_capex = scenario_revenue * scenario_capex_ratio
        scenario_delta_nwc = scenario_revenue * scenario_nwc_ratio
        scenario_fcff = (
            scenario_nopat + scenario_da - scenario_capex - scenario_delta_nwc
        )
        scenario_discount_years = first_discount + index
        scenario_pv_fcff = scenario_fcff / (
            (1 + scenario_wacc) ** scenario_discount_years
        )
        scenario_row = {
            "scenario": scenario_name,
            "label": scenario_label,
            "year": year,
            "revenue_usd_bn": scenario_revenue,
            "revenue_growth": scenario_growth,
            "operating_margin": scenario_margin,
            "tax_rate": scenario_tax,
            "nopat_usd_bn": scenario_nopat,
            "da_revenue_ratio": scenario_da_ratio,
            "capex_revenue_ratio": scenario_capex_ratio,
            "delta_nwc_revenue_ratio": scenario_nwc_ratio,
            "fcff_usd_bn": scenario_fcff,
            "discount_years": scenario_discount_years,
            "pv_fcff_usd_bn": scenario_pv_fcff,
        }
        scenario_rows.append(scenario_row)
        scenario_forecast_rows.append(scenario_row)

    scenario_terminal_growth = float(scenario["terminal_growth"])
    scenario_terminal_roic = float(scenario["terminal_roic"])
    scenario_terminal_nopat = float(scenario_rows[-1]["nopat_usd_bn"]) * (
        1 + scenario_terminal_growth
    )
    scenario_terminal_reinvestment = (
        scenario_terminal_growth / scenario_terminal_roic
    )
    scenario_terminal_fcff = scenario_terminal_nopat * (
        1 - scenario_terminal_reinvestment
    )
    scenario_terminal_value = scenario_terminal_fcff / (
        scenario_wacc - scenario_terminal_growth
    )
    scenario_pv_terminal = scenario_terminal_value / (
        (1 + scenario_wacc) ** terminal_discount_years
    )
    scenario_pv_explicit = sum(
        float(row["pv_fcff_usd_bn"]) for row in scenario_rows
    )
    scenario_ev = scenario_pv_explicit + scenario_pv_terminal
    scenario_core_equity = scenario_ev + non_ev_bridge
    scenario_core_per_share = scenario_core_equity / shares
    scenario_irs_probability = float(scenario["irs_win_probability"])
    scenario_pv_future_tax_drag = annual_future_tax_drag / (
        scenario_wacc - scenario_terminal_growth
    )
    scenario_irs_adjustment = (
        scenario_irs_probability * irs_refund
        - (1 - scenario_irs_probability)
        * (irs_remaining + scenario_pv_future_tax_drag)
    )
    scenario_risk_adjusted_equity = scenario_core_equity + scenario_irs_adjustment

    operating_scenario_rows.append(
        {
            "scenario": scenario_name,
            "label": scenario_label,
            "enterprise_value_usd_bn": scenario_ev,
            "pv_explicit_fcff_usd_bn": scenario_pv_explicit,
            "pv_terminal_value_usd_bn": scenario_pv_terminal,
            "terminal_value_share_of_ev": scenario_pv_terminal / scenario_ev,
            "core_equity_value_usd_bn": scenario_core_equity,
            "core_fair_value_per_share": scenario_core_per_share,
            "irs_win_probability": scenario_irs_probability,
            "pv_future_tax_drag_if_loss_usd_bn": scenario_pv_future_tax_drag,
            "irs_expected_adjustment_usd_bn": scenario_irs_adjustment,
            "risk_adjusted_equity_value_usd_bn": scenario_risk_adjusted_equity,
            "risk_adjusted_fair_value_per_share": scenario_risk_adjusted_equity / shares,
            "rationale": scenario["rationale"],
        }
    )

# 7) WACC / terminal-growth sensitivity before IRS risk adjustment.
sensitivity_rows: list[dict[str, object]] = []
for scenario_wacc in (0.062, 0.067, 0.072, 0.077):
    row: dict[str, object] = {"wacc": scenario_wacc}
    for scenario_growth in (0.025, 0.030, 0.035):
        scenario_terminal_nopat = float(forecast_rows[-1]["nopat_usd_bn"]) * (
            1 + scenario_growth
        )
        scenario_terminal_fcff = scenario_terminal_nopat * (
            1 - scenario_growth / terminal_roic
        )
        scenario_tv = scenario_terminal_fcff / (scenario_wacc - scenario_growth)
        scenario_pv_explicit = sum(
            float(item["fcff_usd_bn"])
            / ((1 + scenario_wacc) ** float(item["discount_years"]))
            for item in forecast_rows
        )
        scenario_pv_tv = scenario_tv / (
            (1 + scenario_wacc) ** terminal_discount_years
        )
        non_ev_bridge = equity_value_before_irs - enterprise_value
        scenario_equity = scenario_pv_explicit + scenario_pv_tv + non_ev_bridge
        row[f"terminal_growth_{scenario_growth:.3f}"] = scenario_equity / shares
    sensitivity_rows.append(row)

# 8) Forward multiple cross-check.
forward_eps = f(facts, "fy2025_comparable_eps") * (
    1 + f(facts, "fy2026_guidance_eps_growth_midpoint")
)

# Mechanical integrity checks. These validate reconciliation and arithmetic,
# not the analyst judgment embedded in assumptions.
validation_rows = [
    {
        "check": "2025 comparable operating margin",
        "calculated": f(facts, "fy2025_comparable_operating_income") / f(facts, "fy2025_comparable_revenue"),
        "reported_or_expected": f(facts, "fy2025_comparable_operating_margin"),
        "tolerance": 0.0001,
    },
    {
        "check": "2025 adjusted FCF excluding fairlife",
        "calculated": f(facts, "fy2025_ocf") - f(facts, "fy2025_capex") + f(facts, "fy2025_fairlife_payment"),
        "reported_or_expected": f(facts, "fy2025_adjusted_fcf"),
        "tolerance": 0.000001,
    },
    {
        "check": "2026 management FCF guidance",
        "calculated": f(facts, "fy2026_guidance_ocf") - f(facts, "fy2026_guidance_capex"),
        "reported_or_expected": f(facts, "fy2026_guidance_fcf"),
        "tolerance": 0.000001,
    },
    {
        "check": "Enterprise value",
        "calculated": pv_explicit_fcff + pv_terminal_value,
        "reported_or_expected": enterprise_value,
        "tolerance": 0.000001,
    },
    {
        "check": "Core equity value",
        "calculated": sum(value for _, value, _ in bridge_rows),
        "reported_or_expected": equity_value_before_irs,
        "tolerance": 0.000001,
    },
    {
        "check": "Risk-adjusted fair value",
        "calculated": (equity_value_before_irs + float(base_irs["expected_adjustment_usd_bn"])) / shares,
        "reported_or_expected": risk_adjusted_fair_value,
        "tolerance": 0.000001,
    },
    {
        "check": "Integrated Base scenario core fair value",
        "calculated": next(
            float(row["core_fair_value_per_share"])
            for row in operating_scenario_rows
            if row["scenario"] == "base"
        ),
        "reported_or_expected": core_fair_value_per_share,
        "tolerance": 0.000001,
    },
    {
        "check": "Integrated Base scenario risk-adjusted fair value",
        "calculated": next(
            float(row["risk_adjusted_fair_value_per_share"])
            for row in operating_scenario_rows
            if row["scenario"] == "base"
        ),
        "reported_or_expected": risk_adjusted_fair_value,
        "tolerance": 0.000001,
    },
]
for row in validation_rows:
    row["difference"] = float(row["calculated"]) - float(row["reported_or_expected"])
    row["passed"] = abs(float(row["difference"])) <= float(row["tolerance"])

derived_rows = [
    {"item": "Estimated 2025 CCBA revenue", "value": ccba_revenue, "unit": "USD bn", "formula": "2025 reported revenue x (12% Bottling share - 4% Bottling ex-CCBA share)"},
    {"item": "2025 pro forma comparable revenue ex-CCBA", "value": proforma_2025_revenue, "unit": "USD bn", "formula": "2025 comparable revenue - estimated CCBA revenue"},
    {"item": "2026 pro forma revenue ex-CCBA", "value": proforma_2026_revenue, "unit": "USD bn", "formula": "2025 pro forma revenue x (1 + 5% organic + 1% FX)"},
    {"item": "Total debt", "value": debt, "unit": "USD bn", "formula": "loans and notes + current maturities + long-term debt"},
    {"item": "Market equity used for WACC weights", "value": market_equity, "unit": "USD bn", "formula": "$87.05 market price x 4.313bn diluted shares"},
    {"item": "Equity weight", "value": equity_weight, "unit": "decimal", "formula": "market equity / (market equity + debt)"},
    {"item": "Debt weight", "value": debt_weight, "unit": "decimal", "formula": "debt / (market equity + debt)"},
    {"item": "Cost of equity", "value": cost_of_equity, "unit": "decimal", "formula": "4.5% risk-free + 0.60 adjusted beta x 4.2% ERP"},
    {"item": "After-tax cost of debt", "value": after_tax_cost_of_debt, "unit": "decimal", "formula": "5.0% pre-tax cost x (1 - 20% tax)"},
    {"item": "Calculated WACC", "value": calculated_wacc, "unit": "decimal", "formula": "E/V x cost of equity + D/V x after-tax cost of debt"},
    {"item": "Adopted WACC", "value": wacc, "unit": "decimal", "formula": "Calculated WACC rounded to nearest 10 bps"},
    {"item": "CCBA retained interest value", "value": ccba_retained_value, "unit": "USD bn", "formula": "$3.4bn total value x 25% retained stake"},
    {"item": "2026 comparable EPS midpoint", "value": forward_eps, "unit": "USD per share", "formula": "$3.00 x (1 + 9.5%)"},
]

valuation_rows = [
    {"item": "PV of explicit FCFF", "value_usd_bn": pv_explicit_fcff, "formula": "Sum of 2027-2031 FCFF present values"},
    {"item": "2032 terminal NOPAT", "value_usd_bn": terminal_nopat, "formula": "2031 NOPAT x (1 + terminal growth)"},
    {"item": "Terminal reinvestment rate", "value_usd_bn": terminal_reinvestment_rate, "formula": "terminal growth / terminal ROIC; value shown as decimal"},
    {"item": "2032 terminal FCFF", "value_usd_bn": terminal_fcff, "formula": "terminal NOPAT x (1 - terminal reinvestment rate)"},
    {"item": "Terminal value at 2031 year-end", "value_usd_bn": terminal_value, "formula": "terminal FCFF / (WACC - terminal growth)"},
    {"item": "PV of terminal value", "value_usd_bn": pv_terminal_value, "formula": "terminal value / (1 + WACC)^5.37"},
    {"item": "Fair enterprise value", "value_usd_bn": enterprise_value, "formula": "PV explicit FCFF + PV terminal value"},
    {"item": "Terminal value share of EV", "value_usd_bn": pv_terminal_value / enterprise_value, "formula": "PV terminal value / enterprise value; value shown as decimal"},
]

write_csv("derived_inputs.csv", ["item", "value", "unit", "formula"], derived_rows)
write_csv(
    "forecast.csv",
    list(forecast_rows[0].keys()),
    forecast_rows,
)
write_csv("valuation_summary.csv", ["item", "value_usd_bn", "formula"], valuation_rows)
write_csv(
    "equity_bridge.csv",
    ["item", "value_usd_bn", "formula_or_source"],
    [
        {"item": item, "value_usd_bn": value, "formula_or_source": note}
        for item, value, note in bridge_rows
    ]
    + [
        {"item": "Fair equity value before IRS", "value_usd_bn": equity_value_before_irs, "formula_or_source": "Sum of bridge"},
        {"item": "Diluted shares (bn)", "value_usd_bn": shares, "formula_or_source": "Q2 2026 diluted shares"},
        {"item": "Core fair value per share", "value_usd_bn": core_fair_value_per_share, "formula_or_source": "Fair equity value / diluted shares"},
    ],
)
write_csv("irs_scenarios.csv", list(irs_rows[0].keys()), irs_rows)
write_csv("sensitivity.csv", list(sensitivity_rows[0].keys()), sensitivity_rows)
write_csv(
    "fair_value_summary.csv",
    ["metric", "value", "unit", "formula"],
    [
        {"metric": "Core fair value", "value": core_fair_value_per_share, "unit": "USD per share", "formula": "Equity value before IRS / diluted shares"},
        {"metric": "Base IRS win probability", "value": base_win_probability, "unit": "decimal", "formula": "Analyst assumption"},
        {"metric": "IRS expected adjustment", "value": base_irs["expected_adjustment_usd_bn"], "unit": "USD bn", "formula": "P(win) x refund - P(loss) x (remaining liability + PV tax drag)"},
        {"metric": "Risk-adjusted fair value", "value": risk_adjusted_fair_value, "unit": "USD per share", "formula": "(Core equity value + IRS expected adjustment) / diluted shares"},
        {"metric": "2026 comparable EPS midpoint", "value": forward_eps, "unit": "USD per share", "formula": "$3.00 x 1.095"},
        {"metric": "Core justified forward PE", "value": core_fair_value_per_share / forward_eps, "unit": "x", "formula": "Core fair value / 2026 EPS midpoint"},
        {"metric": "Risk-adjusted justified forward PE", "value": risk_adjusted_fair_value / forward_eps, "unit": "x", "formula": "Risk-adjusted fair value / 2026 EPS midpoint"},
    ],
)
write_csv(
    "scenario_forecast.csv",
    list(scenario_forecast_rows[0].keys()),
    scenario_forecast_rows,
)
write_csv(
    "operating_scenarios.csv",
    list(operating_scenario_rows[0].keys()),
    operating_scenario_rows,
)
write_csv(
    "validation_checks.csv",
    ["check", "calculated", "reported_or_expected", "difference", "tolerance", "passed"],
    validation_rows,
)

print(f"Core fair value: ${core_fair_value_per_share:.2f}/share")
print(f"Risk-adjusted fair value: ${risk_adjusted_fair_value:.2f}/share")
print(f"Calculated WACC: {calculated_wacc:.3%}; adopted: {wacc:.1%}")
