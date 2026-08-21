# Coca-Cola (KO) Post-CCBA DCF Valuation

A fully reproducible free-cash-flow-to-the-firm valuation of The Coca-Cola Company, including:

- a reconstructed post-CCBA operating baseline;
- a five-year explicit FCFF forecast;
- Bear, Base, and Bull operating scenarios;
- WACC and terminal-growth sensitivity analysis;
- an enterprise-to-equity value bridge;
- a probability-weighted IRS litigation adjustment; and
- machine-readable assumptions, sources, outputs, and validation checks.

The full investment report is available in [`KO_DCF_Article_EN.md`](KO_DCF_Article_EN.md). This README is the technical guide to the repository and the model.

## Headline Results

The valuation date is August 19, 2026. Base Case results are:

| Metric | Result |
|---|---:|
| Core fair value | **$74.22 per share** |
| Expected IRS adjustment | **-$1.98 per share** |
| Risk-adjusted fair value | **$72.24 per share** |
| 2026 comparable EPS midpoint | **$3.285 per share** |
| Core justified forward P/E | **22.59×** |
| Risk-adjusted justified forward P/E | **21.99×** |

These values are conditional model outputs, not precise price predictions. The present value of the terminal value represents approximately 83% of Base Case enterprise value, making WACC, terminal growth, and terminal ROIC especially important.

The integrated scenarios produce the following results:

| Scenario | Core fair value per share | Risk-adjusted fair value per share |
|---|---:|---:|
| Bear | $52.32 | $49.87 |
| Base | $74.22 | $72.24 |
| Bull | $108.03 | $106.51 |

Bear and Bull are coherent analytical boundary cases rather than statistical confidence intervals. No occurrence probabilities are assigned to the three operating scenarios.

## Repository Structure

| File | Purpose |
|---|---|
| [`KO_DCF_Article_EN.md`](KO_DCF_Article_EN.md) | Full English investment report and technical appendix |
| [`data/facts.csv`](data/facts.csv) | Reported facts, management guidance, market observations, dates, classifications, and original sources |
| [`data/assumptions.csv`](data/assumptions.csv) | Base Case assumptions, formulas, methods, and rationale |
| [`data/scenario_assumptions.csv`](data/scenario_assumptions.csv) | Integrated Bear, Base, and Bull assumptions |
| [`model.py`](model.py) | Complete calculation engine using only the Python standard library |
| [`outputs/derived_inputs.csv`](outputs/derived_inputs.csv) | CCBA, capital structure, WACC, and forward EPS derivations |
| [`outputs/forecast.csv`](outputs/forecast.csv) | Base Case 2027–2031 FCFF forecast |
| [`outputs/scenario_forecast.csv`](outputs/scenario_forecast.csv) | Annual forecasts for Bear, Base, and Bull |
| [`outputs/operating_scenarios.csv`](outputs/operating_scenarios.csv) | Scenario EV, equity value, IRS adjustment, and per-share value |
| [`outputs/valuation_summary.csv`](outputs/valuation_summary.csv) | Explicit-period and terminal-value calculations |
| [`outputs/equity_bridge.csv`](outputs/equity_bridge.csv) | Enterprise-to-equity reconciliation |
| [`outputs/irs_scenarios.csv`](outputs/irs_scenarios.csv) | Single-factor IRS probability analysis |
| [`outputs/sensitivity.csv`](outputs/sensitivity.csv) | WACC and terminal-growth sensitivity matrix |
| [`outputs/fair_value_summary.csv`](outputs/fair_value_summary.csv) | Core and risk-adjusted fair value and justified P/E |
| [`outputs/validation_checks.csv`](outputs/validation_checks.csv) | Mechanical reconciliation and arithmetic checks |

## Reproducing the Model

The model requires Python 3 and no external packages.

```bash
python3 model.py
```

Running the script regenerates every CSV in `outputs/` and prints the headline valuation results:

```text
Core fair value: $74.22/share
Risk-adjusted fair value: $72.24/share
Calculated WACC: 6.706%; adopted: 6.7%
```

To update the model:

1. Replace or add reported information in `data/facts.csv`.
2. Update Base Case judgments in `data/assumptions.csv`.
3. Update integrated scenario definitions in `data/scenario_assumptions.csv`.
4. Run `python3 model.py`.
5. Review `outputs/validation_checks.csv` before using the results.

## Input Discipline

The model separates inputs into four categories:

| Classification | Meaning | Examples |
|---|---|---|
| Reported fact | Directly disclosed historical or balance-sheet information | 2025 revenue, Q2 2026 debt, diluted shares |
| Management guidance | A disclosed forecast, not a realized result | 2026 organic growth, tax rate, FCF guidance |
| Derived input | Calculated from disclosed facts | Estimated CCBA revenue, market-value capital weights |
| Analyst assumption | A judgment that cannot be mechanically obtained from a filing | 2029 revenue growth, terminal ROIC, IRS win probability |

Management guidance is treated as a disclosed statement, but its forecast values are not historical facts. The model does not automatically extend short-term guidance through the entire explicit period.

## Reconstructing the Post-CCBA Baseline

Coca-Cola reported 2025 revenue of $47.941 billion and comparable revenue of $48.062 billion. Bottling Investments represented approximately 12% of revenue, while Bottling Investments excluding CCBA represented approximately 4%.

Estimated CCBA revenue is therefore:

```text
Estimated 2025 CCBA revenue
= 2025 reported revenue × (12% - 4%)
= $47.941 billion × 8%
= $3.835 billion
```

This is a derived estimate based on disclosed revenue shares, not a separately audited CCBA revenue figure.

The post-CCBA comparable baseline is:

```text
2025 pro forma comparable revenue excluding CCBA
= $48.062 billion - $3.835 billion
= $44.227 billion
```

Management's 2026 guidance includes approximately 5% organic revenue growth, an approximately 1% favorable currency effect, and a 2%–3% acquisitions-and-divestitures headwind. Because the model has already removed a full year of estimated CCBA revenue from the historical base, it applies only organic growth and currency:

```text
2026 pro forma revenue excluding CCBA
= $44.227 billion × (1 + 5% + 1%)
= $46.880 billion
```

The divestiture headwind is not deducted again. Applying it to an already normalized historical base would double-count the CCBA disposal.

## Base Case Revenue Growth

The 2026 pro forma growth rate of 6.0% includes a 1.0% currency tailwind that is not treated as permanent. Base Case 2027 growth is constructed as follows:

```text
2027 revenue growth
= 2026 pro forma growth
  - 2026 currency contribution
  - normalization haircut
= 6.0% - 1.0% - 0.3%
= 4.7%
```

Growth then fades gradually toward the terminal rate:

| Year | Growth | Construction |
|---|---:|---|
| 2026 pro forma | 6.0% | 5.0% organic guidance plus 1.0% FX |
| 2027 | 4.7% | Remove 1.0% FX and apply a 0.3% normalization haircut |
| 2028 | 4.4% | Approximately 0.3 percentage points below 2027 |
| 2029 | 4.1% | Approximately 0.3 percentage points below 2028 |
| 2030 | 3.8% | Approximately 0.3 percentage points below 2029 |
| 2031 | 3.5% | Approximately 0.3 percentage points below 2030 |
| Terminal period | 3.0% | Mature long-run nominal growth assumption |

Revenue is calculated as:

```text
Revenue[t] = Revenue[t-1] × (1 + growth[t])

2027 revenue = $46.880 billion × 1.047 = $49.084 billion
2028 revenue = $49.084 billion × 1.044 = $51.243 billion
```

The growth rate is total post-CCBA revenue growth. It is not presented as unit-volume growth and is not separately decomposed into volume, price/mix, geography, and foreign exchange.

## Operating Margin, Tax, and Reinvestment

The operating-margin forecast is anchored to:

- 2025 comparable operating margin of 31.24%;
- 2025 underlying operating margin of 32.61%; and
- 2026 H1 comparable operating margin of 34.3%.

The first-half 2026 result is seasonal and is not treated as a permanent full-year margin. Base begins at 33.7% in 2027 and expands by only 10 basis points per year to 34.1% in 2031.

```text
EBIT[t] = Revenue[t] × operating margin[t]

2027 EBIT = $49.084 billion × 33.7% = $16.541 billion
```

The Base Case tax rate is 20.0%, rounded from management's 19.9% underlying effective tax-rate guidance. It excludes a possible adverse IRS outcome, which is valued separately.

```text
NOPAT[t] = EBIT[t] × (1 - tax rate[t])
```

In 2025, consolidated D&A represented approximately 2.19% of revenue and capital expenditure represented approximately 4.41%. CCBA is capital-intensive, so the post-CCBA Base Case uses:

- D&A equal to 1.7% of revenue;
- CapEx declining from 3.6% of revenue in 2027 to 3.2% in 2031; and
- normalized change in net working capital equal to zero.

CapEx remains above D&A throughout the explicit forecast. The model does not generate free cash flow by assuming that Coca-Cola stops reinvesting.

Normalized change in working capital is set to zero because Coca-Cola historically operates with negative working capital and recent reported changes were distorted by the fairlife payment, supplier terms, and supplier-finance arrangements. The assumption recognizes neither a continuing cash release nor an additional cash use.

## Explicit-Period FCFF

The model uses an accounting FCFF formulation:

```text
FCFF[t]
= EBIT[t] × (1 - tax rate[t])
  + D&A[t]
  - CapEx[t]
  - change in NWC[t]
```

For 2027:

```text
FCFF
= $16.541 billion × (1 - 20.0%)
  + $0.834 billion
  - $1.767 billion
  - $0
= $12.300 billion
```

Management's 2026 FCF guidance of $12.4 billion is operating cash flow less capital expenditure. It is measured after interest and may include dividends from equity-method investments, so it is used only as a scale check and not inserted directly as FCFF.

The explicit period does not also apply `NOPAT × (1 - g/ROIC)`. Doing so after directly deducting CapEx and working-capital investment would count reinvestment twice.

## WACC

Base Case cost of equity is:

```text
Risk-free rate = 4.5%
Raw beta = 0.35
Adjusted beta = 0.60
Mature-market ERP = 4.2%
```

The raw beta is adjusted toward one:

```text
Adjusted beta
= 2/3 × 0.35 + 1/3 × 1.0
= 0.567, rounded to 0.60
```

```text
Cost of equity
= 4.5% + 0.60 × 4.2%
= 7.02%
```

Pretax cost of debt is assumed to be 5.0%, producing an after-tax cost of 4.0% at a 20% tax rate. This is a forward refinancing-cost assumption rather than historical interest expense divided by debt.

Total debt is:

```text
$0.048 billion of loans and notes
+ $6.494 billion of current maturities
+ $37.001 billion of long-term debt
= $43.543 billion
```

Market equity used only for WACC weighting is:

```text
$87.05 reference market price × 4.313 billion diluted shares
= $375.447 billion
```

This produces an equity weight of 89.61% and a debt weight of 10.39%.

```text
Calculated WACC
= 89.61% × 7.02% + 10.39% × 4.0%
= 6.706%
```

The Base Case uses a rounded WACC of 6.7%. The reference market price affects only the capital weights and is not used to reverse-engineer fair value.

## Discount Timing and Terminal Value

The valuation date is August 19, 2026, and 2027 is the first complete forecast year. The model applies a mid-year convention:

| Cash flow | Discount period |
|---|---:|
| 2027 FCFF | 0.87 years |
| 2028 FCFF | 1.87 years |
| 2029 FCFF | 2.87 years |
| 2030 FCFF | 3.87 years |
| 2031 FCFF | 4.87 years |
| Year-end 2031 terminal value | 5.37 years |

Base Case present value of explicit FCFF is approximately $56.142 billion.

The terminal period uses a 3.0% growth rate and 25% terminal ROIC. This forces the model to recognize the reinvestment required to support perpetual growth:

```text
Terminal reinvestment rate
= terminal growth / terminal ROIC
= 3.0% / 25.0%
= 12.0%

2032 terminal NOPAT
= 2031 NOPAT × 1.03
= $16.103 billion

2032 terminal FCFF
= $16.103 billion × (1 - 12.0%)
= $14.171 billion

Terminal value at year-end 2031
= $14.171 billion / (6.7% - 3.0%)
= $382.991 billion

Present value of terminal value
= $382.991 billion / (1.067)^5.37
= $270.362 billion
```

Enterprise value is therefore:

```text
$56.142 billion + $270.362 billion
= $326.504 billion
```

## Enterprise-to-Equity Bridge

| Item | Amount |
|---|---:|
| Fair enterprise value | $326.504 billion |
| Less: debt | ($43.543 billion) |
| Add: cash and short-term investments | $13.529 billion |
| Add: marketable securities | $2.842 billion |
| Add: equity-method investments | $20.782 billion |
| Add: CCBA cash consideration | $1.300 billion |
| Add: retained 25% CCBA interest | $0.850 billion |
| Less: noncontrolling interests | ($2.165 billion) |
| **Fair equity value before IRS** | **$320.099 billion** |

Equity-method investments are added because their earnings are below operating income and are not included in the EBIT-based DCF. They are included at reported carrying value rather than valued individually. The full reported noncontrolling-interest balance is deducted.

```text
Core fair value per share
= $320.099 billion / 4.313 billion diluted shares
= $74.22
```

## IRS Litigation Adjustment

The core DCF excludes both the potential refund asset and adverse-case liabilities.

```text
Refund if Coca-Cola prevails
= $6.000 billion deposit + $0.514 billion accrued interest
= $6.514 billion

Remaining liability if Coca-Cola loses = $14.900 billion
Potential future effective-tax-rate increase = 3.8 percentage points
```

The annual future tax burden is estimated from 2026 pro forma EBIT:

```text
2026 pro forma EBIT
= $46.880 billion × 33.6%
= $15.752 billion

Annual future tax drag
= $15.752 billion × 3.8%
= $0.599 billion

Present value of future tax drag if Coca-Cola loses
= $0.599 billion / (6.7% - 3.0%)
= $16.178 billion
```

The Base Case assumes a 60% probability that Coca-Cola prevails. This is an analyst assumption rather than a company-disclosed probability.

```text
Expected IRS adjustment
= 60% × $6.514 billion
  - 40% × ($14.900 billion + $16.178 billion)
= -$8.523 billion

Risk-adjusted fair value
= ($320.099 billion - $8.523 billion) / 4.313 billion shares
= $72.24 per share
```

Holding all other Base assumptions constant:

| IRS win probability | Fair value per share |
|---:|---:|
| 50% | $71.37 |
| 60% | $72.24 |
| 70% | $73.11 |

## Scenario Analysis

The integrated scenarios change revenue growth, operating margin, tax rate, capital intensity, WACC, terminal growth, terminal ROIC, and IRS win probability together.

| Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| 2027–2031 revenue growth | 3.2% → 2.6% | 4.7% → 3.5% | 5.5% → 4.0% |
| 2027–2031 operating margin | 32.7% → 32.5% | 33.7% → 34.1% | 34.2% → 35.2% |
| Normal tax rate | 21.0% | 20.0% | 19.5% |
| 2027–2031 CapEx/revenue | 3.8% → 3.4% | 3.6% → 3.2% | 3.5% → 3.1% |
| WACC | 7.2% | 6.7% | 6.2% |
| Terminal growth | 2.5% | 3.0% | 3.5% |
| Terminal ROIC | 20.0% | 25.0% | 30.0% |
| IRS win probability | 50% | 60% | 70% |

Bear represents faster normalization in pricing and volume, margin pressure, higher capital intensity, and higher valuation risk premia. Bull requires durable brand pricing, resilient volume, sustained operating leverage, lower capital intensity, and stronger terminal economics.

The detailed annual variables, exact changes relative to Base, and case rationale are available in Sections 3 and 6 and Appendix B of the full report.

## WACC and Terminal-Growth Sensitivity

The following values are per share before the IRS adjustment and hold the Base operating forecast and terminal ROIC constant:

| WACC \ Terminal growth | 2.5% | 3.0% | 3.5% |
|---|---:|---:|---:|
| 6.2% | $77.13 | $86.04 | $98.22 |
| 6.7% | $67.74 | **$74.22** | $82.71 |
| 7.2% | $60.34 | $65.21 | $71.39 |
| 7.7% | $54.37 | $58.13 | $62.77 |

This sensitivity matrix changes only valuation parameters. It should not be confused with the integrated operating scenarios, which change several economically related assumptions together.

## Validation Checks

The model currently passes all eight mechanical checks:

| Check | Status |
|---|---|
| 2025 comparable operating margin reconciliation | Pass |
| 2025 adjusted FCF excluding fairlife | Pass |
| 2026 management FCF guidance | Pass |
| Enterprise value aggregation | Pass |
| Core equity value bridge | Pass |
| Risk-adjusted fair value | Pass |
| Integrated Base core fair value equals main Base model | Pass |
| Integrated Base risk-adjusted value equals main Base model | Pass |

These checks validate arithmetic and accounting reconciliation. They do not establish that the analyst assumptions are necessarily correct.

## Important Modeling Boundaries

The model does not:

- perpetuate the 34.3% first-half 2026 margin;
- perpetuate management's 5% organic growth guidance;
- treat company-defined FCF as FCFF;
- deduct reinvestment twice during the explicit period;
- include IRS exposure in both the operating tax rate and equity bridge;
- apply the CCBA divestiture headwind to a base from which CCBA has already been fully removed; or
- use the reference market price to reverse-engineer intrinsic value.

## Principal Limitations

1. Estimated CCBA revenue is derived from disclosed revenue shares rather than a separately audited figure.
2. Post-CCBA D&A and CapEx ratios require validation after the transaction closes.
3. Revenue growth is modeled top-down without a separate volume, price/mix, and currency forecast.
4. Equity-method investments are included at carrying value rather than valued individually.
5. Transaction taxes, costs, timing, and closing risk are not modeled separately.
6. The IRS win probability is subjective, and the timing of a final ruling is simplified.
7. WACC inputs are time-sensitive and should be updated with market conditions.
8. Terminal value represents a large share of enterprise value.
9. Bear, Base, and Bull have no assigned scenario probabilities.

## Disclaimer

This repository is an analytical and educational valuation model. It is not investment advice, a recommendation to buy or sell securities, or a guarantee of future results. Users should independently verify source data, assumptions, tax and legal developments, and market inputs before relying on the analysis.
