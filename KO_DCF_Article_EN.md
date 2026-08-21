# The Coca-Cola Company (KO): A Post-CCBA Intrinsic Value Assessment

**Valuation date: August 19, 2026**  
**Currency: U.S. dollars; all monetary amounts are in billions except per-share data**

## Executive Summary

This report estimates the intrinsic value of The Coca-Cola Company using a free-cash-flow-to-the-firm discounted cash flow model. The analysis is built around an important change in the perimeter of the business: the sale of a controlling interest in Coca-Cola Beverages Africa, or CCBA. Because CCBA is a relatively low-margin and capital-intensive bottling operation, its removal reduces consolidated revenue but should improve the margin and capital-intensity profile of the remaining company. A conventional forecast that simply grows reported 2025 revenue would therefore mix two different business perimeters and produce a misleading result. The model instead reconstructs a post-CCBA revenue base before forecasting 2027–2031 cash flows.

Under the Base Case, the model produces a core fair value of **$74.22 per share** before accounting for the IRS transfer-pricing dispute. Applying a 60% probability that Coca-Cola prevails, while also recognizing both the potential remaining liability and the present value of a possible 3.8-percentage-point increase in the future effective tax rate, reduces the risk-adjusted value to **$72.24 per share**. Relative to the $87.05 market price used only to calculate the market-value capital structure in WACC, the core and risk-adjusted estimates are approximately 14.7% and 17.0% lower, respectively.

The valuation range is intentionally wider than the Base Case point estimate. The Bear Case produces a risk-adjusted value of $49.87 per share, while the Bull Case produces $106.51. These are not statistical confidence bounds and they are not assigned probabilities. They are internally consistent operating and valuation cases designed to show what happens when revenue durability, operating leverage, reinvestment requirements, the discount rate, terminal economics, and litigation risk move together.

| Valuation output | Bear Case | Base Case | Bull Case |
|---|---:|---:|---:|
| Core fair value per share | $52.32 | $74.22 | $108.03 |
| Assumed IRS win probability | 50% | 60% | 70% |
| Risk-adjusted fair value per share | **$49.87** | **$72.24** | **$106.51** |
| Present value of terminal value as a share of EV | 78.5% | 82.8% | 87.2% |

The central conclusion is not that Coca-Cola is worth exactly $72.24. The more useful conclusion is that a value near the Base Case requires the company to grow post-CCBA revenue from 4.7% in 2027 toward 3.5% in 2031, expand operating margin gradually from 33.7% to 34.1%, and sustain a 25% terminal return on invested capital while the cost of capital remains around 6.7%. A value closer to the reference market price requires either more durable growth, stronger operating leverage, a lower discount rate, or some combination of the three. Because 82.8% of Base Case enterprise value comes from the terminal value, the result should always be read alongside the scenario and sensitivity analysis rather than as a stand-alone price target.

## 1. Investment Case and Valuation Architecture

### 1.1 Investment Thesis

Coca-Cola is an unusually durable consumer franchise, but franchise quality by itself does not determine investment value. The relevant question is whether the growth, margin, reinvestment, and capital-cost expectations embedded in the current market value are justified by the cash flows the company can reasonably generate. This distinction matters because a high-quality business can still be overvalued if its market price requires several favorable assumptions to occur at the same time.

Three characteristics support the company's intrinsic value. First, Coca-Cola owns a collection of global brands and a distribution system that have historically supported pricing power, repeat demand, and attractive returns on capital. Second, management's 2026 guidance for approximately 5% organic revenue growth indicates that the core system remains capable of generating mid-single-digit growth despite its scale. Third, the CCBA transaction should make the consolidated business more asset-light by removing a portion of capital-intensive bottling revenue. Although this mechanically lowers reported revenue, it can increase the quality of each remaining dollar of revenue through a better margin mix and lower capital expenditure requirements.

The principal valuation constraints are equally important. The 34.3% comparable operating margin reported for the first half of 2026 is a seasonal half-year figure and should not be treated as a permanent annual margin. The company's 5% organic growth guidance is also a near-term operating target rather than a perpetual growth rate. In addition, the IRS dispute is not merely a one-time balance-sheet exposure. An adverse outcome could create both a remaining tax and interest liability and a structurally higher future effective tax rate. Finally, Coca-Cola is a long-duration asset: most of its value lies beyond the explicit five-year forecast, making the valuation particularly sensitive to WACC, terminal growth, and terminal return on invested capital.

### 1.2 Valuation Scope and Input Framework

The model values the core operating business using FCFF derived from EBIT. That choice determines how non-operating assets must be treated. Earnings from equity-method investments are recorded below operating income, so the DCF does not include the cash flows associated with those investments. Their reported carrying value is therefore added separately in the enterprise-to-equity bridge. The expected CCBA sale consideration and the value of the retained 25% interest are also added separately because the operating forecast excludes CCBA revenue. Debt and noncontrolling interests are deducted, while cash, short-term investments, and marketable securities are added.

The analysis distinguishes rigorously between three kinds of inputs. A **reported fact** is a number disclosed in a filing or company release, such as 2025 revenue or Q2 2026 debt. A **derived input** is calculated from disclosed facts, such as estimated CCBA revenue or the market-value weights used in WACC. An **analyst assumption** cannot be mechanically obtained from a filing and requires judgment, such as 2029 revenue growth, terminal ROIC, or the probability of winning the IRS case. Management guidance is a reported statement, but the future amount in that guidance is not a realized historical fact, and any extension of the guidance beyond its stated period remains an analyst forecast.

This classification is central to the credibility of the model. It prevents forecast assumptions from being presented as if management had disclosed them, and it makes clear which variables should be updated when new information arrives. The exact source, date, status, and original URL for each factual input are recorded in the model's facts file, while Base Case and scenario judgments are maintained separately in the assumptions files.

## 2. Reconstructing the Post-CCBA Operating Baseline

### 2.1 Estimating the CCBA Revenue Base

The first analytical task is to create a comparable revenue base for the business that investors will own after the CCBA transaction. Coca-Cola reported 2025 revenue of $47.941 and comparable revenue of $48.062. The company also disclosed that Bottling Investments represented approximately 12% of revenue in 2025, while Bottling Investments excluding CCBA represented approximately 4%. The eight-percentage-point difference provides a reasonable estimate of CCBA's contribution to consolidated revenue:

```text
Estimated 2025 CCBA revenue
= 2025 reported revenue × (Bottling Investments share
  - Bottling Investments share excluding CCBA)
= $47.941 × (12% - 4%)
= $3.835
```

This $3.835 figure is not a separately audited CCBA revenue disclosure. It is a derived estimate based on company-reported revenue shares, and its precision should not be overstated. The estimate is deducted from 2025 comparable revenue so that the starting point and subsequent growth assumptions remain on a comparable operating basis:

```text
2025 pro forma comparable revenue excluding CCBA
= $48.062 - $3.835
= $44.227
```

### 2.2 Extending the Baseline to 2026 on a Consistent Perimeter

Management's 2026 guidance includes approximately 5% organic revenue growth, an approximately 1% favorable currency effect on comparable revenue, and a 2%–3% headwind from acquisitions and divestitures. The model has already removed a full year of estimated CCBA revenue from the historical base. It therefore applies only organic growth and currency to the pro forma base:

```text
2026 pro forma revenue excluding CCBA
= $44.227 × (1 + 5% organic growth + 1% FX)
= $46.880
```

The midpoint of the reported divestiture headwind, approximately negative 2.5%, is deliberately not deducted a second time. The management guidance describes the effect of transaction timing on reported year-over-year revenue. Once the model has fully removed CCBA from the prior-year base, subtracting the divestiture effect again would double-count the sale and understate the post-transaction revenue base.

The same perimeter discipline applies to profitability and reinvestment. In 2025, comparable operating margin was 31.24%, underlying operating margin was 32.61%, depreciation and amortization represented 2.19% of consolidated revenue, and capital expenditure represented 4.41%. Those consolidated ratios include the capital-intensive bottling operations being sold. The post-CCBA forecast should therefore not simply preserve the 2025 consolidated D&A and capital expenditure ratios. At the same time, the model should not assume that every dollar of bottling investment disappears or that the remaining business can grow without maintaining brands, digital capabilities, concentrate capacity, and supply-chain infrastructure.

The 2026 pro forma revenue estimate of $46.880 is used as the common starting point for all three scenarios. Historical facts, the Q2 balance sheet, diluted shares, and announced CCBA transaction values do not change across Bear, Base, and Bull. Only the forward operating, reinvestment, discount-rate, terminal, and litigation assumptions differ. This common starting point is important: if each scenario began from a different 2026 perimeter, part of the apparent valuation difference would reflect inconsistent accounting rather than a genuinely different view of future performance.

## 3. Forecast Assumptions and Scenario Construction

### 3.1 Constructing the Revenue Growth Path

Revenue growth is forecast on a top-down post-CCBA basis. The model does not claim to possess a precise five-year split among unit volume, price, product mix, geographic mix, and foreign exchange. Such a decomposition would require granular assumptions that are not supported by the current input set and could create false precision. Instead, the model begins with management's near-term organic growth and currency guidance, removes effects that should not be extrapolated, and then fades total revenue growth toward a defensible long-run nominal rate.

The Base Case begins with 2026 pro forma growth of 6.0%, consisting of approximately 5.0% organic growth and 1.0% currency tailwind. The 1.0% FX contribution is treated as a year-specific benefit rather than a permanent source of growth. A further 0.3-percentage-point normalization haircut is applied in 2027 to recognize that even the current organic trend should not automatically be extended in full:

```text
2027 Base Case revenue growth
= 2026 pro forma growth
  - 2026 currency contribution
  - normalization haircut
= 6.0% - 1.0% - 0.3%
= 4.7%
```

After 2027, growth is reduced by approximately 0.3 percentage points per year: 4.4% in 2028, 4.1% in 2029, 3.8% in 2030, and 3.5% in 2031. The terminal growth rate is 3.0%. This creates a gradual transition rather than an abrupt jump between the explicit forecast and perpetuity. It also avoids assuming that the current 5% organic growth rate can persist indefinitely for a company of Coca-Cola's scale.

| Year | Base Case growth | Construction |
|---|---:|---|
| 2026 pro forma | 6.0% | 5.0% organic guidance plus 1.0% FX |
| 2027 | 4.7% | Remove 1.0% FX and apply a 0.3% normalization haircut |
| 2028 | 4.4% | 2027 growth less approximately 0.3% |
| 2029 | 4.1% | 2028 growth less approximately 0.3% |
| 2030 | 3.8% | 2029 growth less approximately 0.3% |
| 2031 | 3.5% | 2030 growth less approximately 0.3% |
| Terminal period | 3.0% | Mature long-run nominal growth assumption |

Revenue is then compounded mechanically:

```text
Revenue[t] = Revenue[t-1] × (1 + revenue growth[t])

2027 revenue = $46.880 × 1.047 = $49.084
2028 revenue = $49.084 × 1.044 = $51.243
```

The 4.7% assumption should not be interpreted as 4.7% unit-volume growth. It is total post-CCBA revenue growth and implicitly captures the combined contribution of volume, price and product mix, geographic mix, and normalized currency effects. The model is intentionally transparent about this limitation. If future disclosures show that reported organic growth is being generated almost entirely by price while volume deteriorates, the durability of the growth path should be reconsidered even if the headline growth rate initially appears consistent with the forecast.

The Bear and Bull growth paths are constructed as explicit adjustments to the Base Case rather than unrelated forecasts. The Bear Case assumes that consumer resistance to pricing becomes more pronounced, volume recovery is weaker, and emerging-market or product-mix contributions are insufficient to sustain mid-single-digit growth. It starts 1.5 percentage points below Base in 2027, but the gap narrows over time because the Base Case itself is already converging toward mature growth. The Bear path is 3.2%, 3.0%, 2.8%, 2.7%, and 2.6% from 2027 through 2031, followed by 2.5% terminal growth.

The Bull Case assumes that brand pricing remains durable, emerging-market volume is resilient, and portfolio development allows mid-single-digit growth to persist longer. It begins 0.8 percentage points above Base in 2027–2029, with the premium narrowing to 0.7 percentage points in 2030 and 0.5 points in 2031. The Bull path is 5.5%, 5.2%, 4.9%, 4.5%, and 4.0%, followed by 3.5% terminal growth. Even the Bull Case fades: it does not assume that 5% or higher growth continues forever.

| Year | Bear growth | Base growth | Bull growth | Bear adjustment vs. Base | Bull adjustment vs. Base |
|---|---:|---:|---:|---:|---:|
| 2027 | 3.2% | 4.7% | 5.5% | -150bp | +80bp |
| 2028 | 3.0% | 4.4% | 5.2% | -140bp | +80bp |
| 2029 | 2.8% | 4.1% | 4.9% | -130bp | +80bp |
| 2030 | 2.7% | 3.8% | 4.5% | -110bp | +70bp |
| 2031 | 2.6% | 3.5% | 4.0% | -90bp | +50bp |
| Terminal period | 2.5% | 3.0% | 3.5% | -50bp | +50bp |

Compounding these paths from the same $46.880 starting point produces 2031 revenue of $53.978 in Bear, $57.309 in Base, and $59.318 in Bull. Relative to Base, the 2031 revenue difference is approximately negative 5.8% in Bear and positive 3.5% in Bull. These revenue differences are meaningful but not sufficient by themselves to explain the much wider valuation range. The full range arises because weaker growth is paired with weaker margin economics, higher reinvestment intensity, and a higher discount rate in Bear, while the opposite combination applies in Bull.

### 3.2 Margin, Tax, and Reinvestment Assumptions

Operating margin assumptions are anchored to three reported observations: 31.24% comparable operating margin in 2025, 32.61% underlying operating margin in 2025, and 34.3% comparable operating margin in the first half of 2026. The first-half figure benefits from seasonality and cannot safely be annualized. The Base Case therefore starts at 33.7% in 2027, below the 2026 H1 level but above the 2025 underlying margin, and expands by only 10 basis points per year to 34.1% in 2031. The 33.7% starting point is a triangulated analyst judgment reflecting historical underlying profitability, recent performance, and the expected mix benefit from removing CCBA; it is not a company-disclosed pro forma margin.

The Bear Case begins at 32.7% and declines slightly to 32.5%, implying that Coca-Cola gives back part of the expected post-CCBA mix benefit through weaker pricing, adverse product or geographic mix, or less operating leverage. The Bull Case starts at 34.2% and expands to 35.2%, requiring the asset-light mix and scale benefits to translate into sustained operating leverage. Because margin changes affect every dollar of revenue, they have a larger effect on NOPAT and FCFF than the modest absolute changes might initially suggest.

The normal tax rate is 20.0% in Base, rounded from management's 19.9% underlying effective tax-rate guidance. Bear uses 21.0% and Bull uses 19.5%. These rates exclude any adverse IRS outcome because the litigation is valued separately. Including the possible IRS methodology in both the operating tax rate and the equity bridge would count the same risk twice.

Post-CCBA D&A is held at 1.7% of revenue in every case. Base Case capital expenditure declines from 3.6% of revenue in 2027 to 3.2% in 2031. CapEx remains materially above D&A throughout the forecast, so the model does not create free cash flow by assuming the company stops reinvesting. Bear CapEx is 20 basis points above Base in each year, reflecting the possibility that investment requirements are partly fixed even when revenue growth weakens. Bull CapEx is 10 basis points below Base, reflecting stronger scale benefits and a more efficient asset-light mix.

Normalized change in net working capital is set to zero in all three cases. Coca-Cola has historically operated with negative working capital, while recent reported movements were distorted by the fairlife contingent-consideration payment, extended supplier terms, and supplier-finance arrangements. A zero assumption recognizes neither a continuing cash release nor an additional cash use. It is a neutral normalization, not a claim that working capital is economically irrelevant.

### 3.3 Integrated Bear, Base, and Bull Definitions

The integrated scenario assumptions are summarized below. They are designed to be economically coherent. Bear does not merely reduce growth while leaving every other variable favorable, and Bull does not merely add a premium to terminal growth. This coherence makes the scenarios useful as boundary cases, but it also means their differences are not additive and cannot be used to isolate the effect of a single variable.

| Assumption | Bear Case | Base Case | Bull Case |
|---|---:|---:|---:|
| 2027–2031 revenue growth | 3.2% → 2.6% | 4.7% → 3.5% | 5.5% → 4.0% |
| 2027–2031 operating margin | 32.7% → 32.5% | 33.7% → 34.1% | 34.2% → 35.2% |
| Normal tax rate | 21.0% | 20.0% | 19.5% |
| D&A as a percentage of revenue | 1.7% | 1.7% | 1.7% |
| 2027–2031 CapEx as a percentage of revenue | 3.8% → 3.4% | 3.6% → 3.2% | 3.5% → 3.1% |
| Normalized change in NWC as a percentage of revenue | 0.0% | 0.0% | 0.0% |
| WACC | 7.2% | 6.7% | 6.2% |
| Terminal growth | 2.5% | 3.0% | 3.5% |
| Terminal ROIC | 20.0% | 25.0% | 30.0% |
| IRS win probability | 50% | 60% | 70% |

## 4. Cash Flow Forecast, Cost of Capital, and Terminal Value

### 4.1 Explicit-Period FCFF Forecast

The explicit forecast uses an accounting FCFF formulation. EBIT is taxed at the normalized operating tax rate to produce NOPAT. D&A is added back because it is a non-cash charge, while capital expenditure and normalized investment in working capital are deducted:

```text
FCFF[t]
= EBIT[t] × (1 - tax rate[t])
  + D&A[t]
  - CapEx[t]
  - change in NWC[t]
```

The Base Case forecast is shown below. Revenue grows from $46.880 in 2026 pro forma to $57.309 in 2031. Operating margin expands modestly, allowing NOPAT to increase from $13.233 in 2027 to $15.634 in 2031. FCFF rises from $12.300 to $14.774 even though CapEx remains above D&A in every year.

| Year | Revenue | Growth | Operating margin | EBIT | NOPAT | D&A | CapEx | FCFF | Present value of FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 49.084 | 4.7% | 33.7% | 16.541 | 13.233 | 0.834 | 1.767 | 12.300 | 11.626 |
| 2028 | 51.243 | 4.4% | 33.8% | 17.320 | 13.856 | 0.871 | 1.794 | 12.934 | 11.457 |
| 2029 | 53.344 | 4.1% | 33.9% | 18.084 | 14.467 | 0.907 | 1.814 | 13.560 | 11.257 |
| 2030 | 55.371 | 3.8% | 34.0% | 18.826 | 15.061 | 0.941 | 1.827 | 14.175 | 11.029 |
| 2031 | 57.309 | 3.5% | 34.1% | 19.543 | 15.634 | 0.974 | 1.834 | 14.774 | 10.773 |

For example, 2027 FCFF is calculated as follows:

```text
2027 EBIT = $49.084 × 33.7% = $16.541
2027 NOPAT = $16.541 × (1 - 20.0%) = $13.233
2027 D&A = $49.084 × 1.7% = $0.834
2027 CapEx = $49.084 × 3.6% = $1.767

2027 FCFF
= $13.233 + $0.834 - $1.767 - $0
= $12.300
```

Management's 2026 free cash flow guidance of approximately $12.4 is useful as a scale check but is not inserted directly into the DCF. Company-defined FCF is operating cash flow less capital expenditure. It is measured after interest and may include dividends from equity-method investments, whereas FCFF is intended to represent cash flow available to all capital providers before financing costs. Treating management-defined FCF as FCFF would mix financing and operating concepts.

The explicit forecast uses D&A, CapEx, and change in working capital directly. The model therefore does not also apply `NOPAT × (1 - g/ROIC)` during 2027–2031. Doing so would deduct reinvestment twice. The `g/ROIC` relationship is reserved for the terminal period, where a normalized accounting reinvestment rate is required to make perpetual growth economically consistent.

### 4.2 Deriving the Cost of Capital

Base Case cost of equity is derived using a normalized 4.5% risk-free rate, a 0.60 adjusted beta, and a 4.2% mature-market equity risk premium. The observed five-year monthly raw beta of 0.35 is unusually low and is adjusted toward one:

```text
Adjusted beta
= 2/3 × raw beta + 1/3 × 1.0
= 2/3 × 0.35 + 1/3
= 0.567, rounded to 0.60

Cost of equity
= risk-free rate + adjusted beta × equity risk premium
= 4.5% + 0.60 × 4.2%
= 7.02%
```

The pretax cost of debt is assumed to be 5.0%, producing a 4.0% after-tax cost at the 20% Base Case tax rate. The 5.0% assumption represents a forward refinancing cost rather than historical interest expense divided by debt. Historical coupons were set in earlier rate environments and are not an appropriate measure of the marginal long-term cost of borrowing.

Total debt is $43.543, consisting of $0.048 of loans and notes payable, $6.494 of current maturities, and $37.001 of long-term debt. Market equity used for capital weighting is $375.447, calculated from the $87.05 reference price and 4.313 billion diluted shares. This produces an equity weight of 89.61% and a debt weight of 10.39%:

```text
Calculated WACC
= 89.61% × 7.02% + 10.39% × 4.0%
= 6.706%
```

The Base Case adopts a rounded WACC of 6.7%. The market price influences only the market-value capital weights; it is not used to reverse-engineer the fair value. Bear uses 7.2%, or 50 basis points above Base, while Bull uses 6.2%, or 50 basis points below Base. The movement is intended to capture a combination of changes in risk-free rates, risk premia, and perceived cash-flow risk rather than a forecast of any single market variable.

### 4.3 Discount Timing and Terminal Value

The valuation date is August 19, 2026, and 2027 is the first complete forecast year. The model applies a mid-year convention to operating cash flows. Discount periods for 2027–2031 FCFF are 0.87, 1.87, 2.87, 3.87, and 4.87 years. Terminal value is measured at year-end 2031 and discounted for 5.37 years. This timing avoids treating an entire year's cash flow as if it were received on the final day of the year.

Base Case present value of explicit FCFF is $56.142. Terminal value is estimated using a 3.0% growth rate and 25% terminal ROIC. The ROIC assumption forces the model to recognize that even a strong franchise must reinvest to grow:

```text
Terminal reinvestment rate
= terminal growth / terminal ROIC
= 3.0% / 25.0%
= 12.0%

2032 terminal NOPAT
= 2031 NOPAT × (1 + terminal growth)
= $15.634 × 1.03
= $16.103

2032 terminal FCFF
= $16.103 × (1 - 12.0%)
= $14.171

Terminal value at year-end 2031
= $14.171 / (6.7% - 3.0%)
= $382.991

Present value of terminal value
= $382.991 / (1.067)^5.37
= $270.362
```

Adding the present value of explicit FCFF and terminal value produces enterprise value of $326.504. The terminal value accounts for 82.8% of this amount. That high contribution is not unusual for a durable consumer franchise, but it materially limits the apparent precision of the result. Small changes in the spread between WACC and terminal growth can have a much larger valuation effect than small changes in a single explicit forecast year.

## 5. Enterprise-to-Equity Bridge and IRS Risk

### 5.1 Converting Enterprise Value into Common Equity Value

The DCF produces the value of the core operations before financing and non-operating assets. To reach common equity value, debt and noncontrolling interests are deducted, while cash, securities, equity-method investments, and CCBA transaction assets are added:

| Enterprise-to-equity bridge | Amount |
|---|---:|
| Fair enterprise value | 326.504 |
| Less: debt | (43.543) |
| Add: cash and short-term investments | 13.529 |
| Add: marketable securities | 2.842 |
| Add: equity-method investments | 20.782 |
| Add: CCBA cash consideration | 1.300 |
| Add: value of retained 25% CCBA interest | 0.850 |
| Less: noncontrolling interests | (2.165) |
| **Fair equity value before IRS** | **320.099** |

Equity-method investments are included at reported carrying value rather than being valued individually. This is a simplifying and generally conservative convention, but book value may differ from realizable market value. The retained CCBA interest is valued at 25% of the announced $3.4 implied total equity value, or $0.850. The full reported noncontrolling-interest balance is deducted. Transaction taxes, costs, timing, and closing risk are not separately modeled, which should be considered when interpreting the precision of the bridge.

Dividing pre-IRS equity value by 4.313 billion diluted shares produces core fair value:

```text
Core fair value per share
= $320.099 / 4.313 billion shares
= $74.22
```

### 5.2 Valuing the IRS Contingent Exposure

The IRS dispute is then treated as a separate contingent claim. The core DCF excludes both the potential refund asset in a successful outcome and the adverse liabilities in an unsuccessful outcome. If Coca-Cola prevails, the model assumes recovery of a $6.000 deposit plus $0.514 of accrued interest, for a total benefit of $6.514. If the company loses, it may face a remaining tax and interest liability of approximately $14.900. The disclosed methodology could also increase the future effective tax rate by approximately 3.8 percentage points.

The annual future tax burden is estimated using 2026 pro forma EBIT at a normalized 33.6% margin:

```text
2026 pro forma EBIT
= $46.880 × 33.6%
= $15.752

Annual future tax drag
= $15.752 × 3.8%
= $0.599
```

In Base, the ongoing tax burden is capitalized using the same 6.7% WACC and 3.0% long-run growth rate:

```text
Present value of future tax drag if Coca-Cola loses
= $0.599 / (6.7% - 3.0%)
= $16.178
```

The Base Case assumes a 60% probability that Coca-Cola prevails. This is an analyst assumption, not a probability disclosed by management. The company's statement that it is more likely than not to prevail does not mechanically establish a 60% probability. The assumption is simply a transparent central estimate between the 50% and 70% cases shown in the litigation sensitivity.

```text
Expected Base Case IRS adjustment
= 60% × $6.514
  - 40% × ($14.900 + $16.178)
= -$8.523

IRS adjustment per share
= -$8.523 / 4.313
= -$1.98

Risk-adjusted fair value per share
= $74.22 - $1.98
= $72.24
```

Holding all Base operating and valuation assumptions constant, values at IRS win probabilities of 50%, 60%, and 70% are $71.37, $72.24, and $73.11 per share. These single-factor results differ slightly from the integrated Bear and Bull litigation adjustments because the integrated scenarios also change the discount rate and terminal growth rate used to capitalize the possible future tax burden.

## 6. Scenario Outcomes and Sensitivity Analysis

### 6.1 Integrated Scenario Results

The integrated scenarios demonstrate how differences in growth can be amplified or offset by the economics that accompany them. In Bear, slower revenue growth is paired with margin pressure, a higher normal tax rate, greater capital intensity, a higher WACC, lower terminal growth, lower terminal ROIC, and a lower IRS win probability. In Bull, stronger revenue growth is paired with operating leverage, lower capital intensity, a lower discount rate, better terminal economics, and a higher probability of a favorable IRS outcome.

The resulting revenue and FCFF forecasts are shown below. By 2031, Bull revenue is only about $5.3 higher than Bear revenue, but Bull FCFF is approximately $3.0 higher because the margin, tax, and reinvestment assumptions also differ.

| Year | Bear revenue | Bear FCFF | Base revenue | Base FCFF | Bull revenue | Bull FCFF |
|---|---:|---:|---:|---:|---:|---:|
| 2027 | 48.380 | 11.482 | 49.084 | 12.300 | 49.459 | 12.726 |
| 2028 | 49.832 | 11.837 | 51.243 | 12.934 | 52.031 | 13.566 |
| 2029 | 51.227 | 12.179 | 53.344 | 13.560 | 54.580 | 14.417 |
| 2030 | 52.610 | 12.561 | 55.371 | 14.175 | 57.036 | 15.214 |
| 2031 | 53.978 | 12.941 | 57.309 | 14.774 | 59.318 | 15.978 |

| Valuation output | Bear Case | Base Case | Bull Case |
|---|---:|---:|---:|
| Present value of explicit FCFF | 50.000 | 56.142 | 60.306 |
| Present value of terminal value | 182.061 | 270.362 | 412.036 |
| Enterprise value | 232.061 | 326.504 | 472.341 |
| Core fair value per share | $52.32 | $74.22 | $108.03 |
| Expected IRS adjustment | (10.561) | (8.523) | (6.561) |
| Risk-adjusted fair value per share | **$49.87** | **$72.24** | **$106.51** |

The Bull Case increase is especially large because a lower WACC and higher terminal growth reduce the denominator of the perpetuity formula while stronger NOPAT increases its numerator. The Bull terminal-value share rises to 87.2% of enterprise value, making that case particularly sensitive to long-run assumptions. It should therefore be interpreted as an optimistic boundary that requires several favorable conditions to coexist, not as a minor extension of Base.

The Bear-to-Bull range should not be described as the range within which intrinsic value must fall. The scenarios are conditional statements: if the defined assumptions occur, the model produces the corresponding values. They are not historical-volatility bands, analyst-consensus percentiles, or probability-weighted targets. A formal probability-weighted valuation would require explicit and defensible probabilities for all three cases; none are assigned here.

### 6.2 Single-Factor Sensitivity and Multiple Cross-Check

To separate operating changes from valuation parameters, the following matrix holds the Base operating forecast, terminal ROIC, and enterprise-to-equity bridge constant and changes only WACC and terminal growth. Values are per share before the IRS adjustment:

| WACC \ Terminal growth | 2.5% | 3.0% | 3.5% |
|---|---:|---:|---:|
| 6.2% | $77.13 | $86.04 | $98.22 |
| 6.7% | $67.74 | **$74.22** | $82.71 |
| 7.2% | $60.34 | $65.21 | $71.39 |
| 7.7% | $54.37 | $58.13 | $62.77 |

This table answers a different question from the integrated cases. The sensitivity matrix asks what happens if only discount and terminal-growth assumptions change. The integrated scenarios ask what happens if operating performance, reinvestment, perceived risk, terminal economics, and litigation expectations move together. The two analyses are complementary and should not be substituted for one another.

A forward P/E cross-check provides an additional reasonableness test. Comparable EPS was $3.00 in 2025, and the midpoint of 2026 comparable EPS growth guidance is 9.5%, producing forward comparable EPS of $3.285:

```text
2026 comparable EPS midpoint
= $3.00 × (1 + 9.5%)
= $3.285

Core justified forward P/E
= $74.22 / $3.285
= 22.59×

Risk-adjusted justified forward P/E
= $72.24 / $3.285
= 21.99×
```

The multiple is an output and a cross-check, not an input to the DCF. Margin improvement is already reflected in EBIT and FCFF. Applying an additional premium multiple solely because margin is higher would count the same favorable economics twice.

## 7. What Matters Next and Final Assessment

### 7.1 Evidence That Would Confirm or Challenge the Model

The most important future evidence is not a short-term change in Coca-Cola's share price. It is whether reported results validate the assumptions that carry the largest amount of judgment. The first item to monitor is the post-CCBA operating perimeter. If future pro forma disclosure shows that the reconstructed 2025 revenue base of $44.227 is materially wrong, the entire revenue sequence should be rebuilt before adjusting downstream margins or cash flows.

The second item is full-year operating margin. A sustainable comparable margin above 33% would support the Base starting point, while a reversion toward 32.5% would move the operating profile closer to Bear. The third is capital intensity. If CapEx remains close to the 2025 consolidated level of 4.4% of revenue after CCBA exits the perimeter, the current FCFF forecast is too high. Conversely, a demonstrated decline toward the low-3% range without deterioration in brand investment or system growth would support the asset-light thesis.

Revenue quality matters as much as reported growth. Growth driven by balanced volume, price, and mix is more durable than growth produced almost entirely by repeated price increases against weakening unit demand. Geographic composition also matters because strong emerging-market growth can support the Bull path but may introduce additional currency and execution volatility. The model's top-down growth assumptions should therefore be revised when the underlying volume, price/mix, and geographic disclosures indicate a different quality of growth, even if the headline percentage remains near the forecast.

The IRS case is a distinct catalyst and risk. A favorable ruling could make the deposit and accrued interest recoverable. An adverse ruling could create both an immediate liability and a persistent reduction in after-tax cash flow. Any new disclosure should be incorporated in both dimensions. Updating only the one-time liability while ignoring the future tax-rate effect, or vice versa, would provide an incomplete valuation response.

Capital-market inputs also require ongoing review. The 4.5% normalized risk-free rate, 4.2% equity risk premium, 0.60 adjusted beta, 5.0% pretax borrowing cost, and market-value capital weights are all time-sensitive. They are not permanent characteristics of Coca-Cola. A change in Treasury yields, credit spreads, market risk premiums, or the company's observed risk profile can alter WACC even if the operating forecast is unchanged.

### 7.2 Final Valuation Assessment

Under the Base assumptions—revenue growth fading from 4.7% to 3.5%, operating margin rising gradually from 33.7% to 34.1%, WACC of 6.7%, terminal growth of 3.0%, and terminal ROIC of 25%—the core business is worth approximately $74.22 per share. The expected IRS adjustment reduces that value to $72.24 per share. The result is internally consistent and reproducible, but its apparent numerical precision should not be confused with certainty.

For a value near or above the $87 reference market price to be supported, Coca-Cola would need to deliver some combination of more persistent growth, stronger margins, lower capital intensity, or a lower long-run cost of capital than assumed in Base. A deterioration toward 32.5% operating margin combined with a 7.2% WACC would push the valuation meaningfully toward Bear. The appropriate interpretation of the report is therefore conditional: $72.24 is the output of a transparent set of assumptions, while the investment decision depends on whether the reader believes those assumptions are conservative, balanced, or still too optimistic.

---

# Appendix

## Appendix A: Sources and Input Classification

The complete machine-readable source register is available in [`data/facts.csv`](data/facts.csv). Each item includes its category, metric, value, unit, reporting period, as-of date, classification status, original URL, and a short source note. The principal sources are summarized below.

| Information | Principal source |
|---|---|
| 2025 financial statements, revenue, D&A, CapEx, and bottling revenue share | [Coca-Cola 2025 Form 10-K](https://investors.coca-colacompany.com/filings-reports/annual-filings-10-k/content/0001628280-26-010047/ko-20251231.htm) |
| 2025 comparable revenue, operating income, margin, and adjusted FCF | [Coca-Cola 2025 Q4 earnings release reconciliation](https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-006642/a2025q4earningsreleaseex-9.htm) |
| Q2 2026 balance sheet and IRS disclosures | [Coca-Cola Q2 2026 filing](https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-050503/ko-20260703.htm) |
| 2026 organic growth, FX, tax rate, cash flow, CapEx, FCF, and EPS guidance | [Coca-Cola Q2 2026 results and guidance](https://investors.coca-colacompany.com/news-events/press-releases/detail/1168/coca-cola-reports-second-quarter-2026-results-and-raises-full-year-guidance) |
| CCBA consideration, implied value, and retained interest | [Coca-Cola HBC transaction announcement](https://www.coca-colahellenic.com/en/media/news/corporate_news/2025/acquisition-of-coca-cola-beverages-africa-bringing-together-two-leading-bottlers-in-africa) |
| Raw beta and reference market price | [Yahoo Finance KO](https://finance.yahoo.com/quote/KO/) and [Stock Analysis KO history](https://stockanalysis.com/stocks/ko/history/) |

The online links provide the original source trail. The model itself reads the numerical observations recorded in the local CSV files. Market inputs are date-specific and should be updated when the valuation date changes.

| Classification | Meaning | Examples in this model |
|---|---|---|
| Reported fact | Directly disclosed historical or balance-sheet amount | 2025 revenue, Q2 debt, diluted shares |
| Reported management guidance | A disclosed forecast, not a realized result | 2026 organic growth, tax rate, FCF guidance |
| Derived input | Calculated from reported facts | CCBA revenue estimate, market-value capital weights |
| Analyst assumption | Judgment required; not directly disclosed | 2029 growth, terminal ROIC, IRS win probability |

## Appendix B: Assumption Ledger and Exact Scenario Changes

The full Base Case assumption file is [`data/assumptions.csv`](data/assumptions.csv), while integrated scenario assumptions are stored in [`data/scenario_assumptions.csv`](data/scenario_assumptions.csv).

| Category | Base Case assumption | Value or path | Basis |
|---|---|---:|---|
| Operating base | 2026 pro forma growth | 6.0% | 5% organic guidance plus 1% FX after fully removing CCBA |
| Revenue | 2027–2031 growth | 4.7%, 4.4%, 4.1%, 3.8%, 3.5% | Analyst fade toward mature growth |
| Profitability | 2027–2031 operating margin | 33.7%, 33.8%, 33.9%, 34.0%, 34.1% | Post-CCBA mix plus modest operating leverage |
| Tax | Normal tax rate | 20.0% | Rounded from 19.9% guidance; excludes IRS outcome |
| Reinvestment | D&A/revenue | 1.7% | Post-CCBA normalization |
| Reinvestment | 2027–2031 CapEx/revenue | 3.6%, 3.5%, 3.4%, 3.3%, 3.2% | Asset-light normalization; remains above D&A |
| Reinvestment | Change in NWC/revenue | 0.0% | Neutral normalized convention |
| WACC | Risk-free rate | 4.5% | Normalized market input |
| WACC | Adjusted beta | 0.60 | Raw 0.35 adjusted toward one and rounded |
| WACC | Mature-market ERP | 4.2% | Market input |
| WACC | Pretax cost of debt | 5.0% | Forward refinancing-cost assumption |
| WACC | Adopted WACC | 6.7% | Calculated 6.706% rounded to 10bp |
| Terminal | Growth | 3.0% | Mature long-run nominal growth assumption |
| Terminal | ROIC | 25.0% | Normalized franchise economics |
| Litigation | IRS win probability | 60% | Analyst assumption |

The exact Bear and Bull changes relative to Base are shown below. Basis points refer to hundredths of a percentage point; percentage points are used for larger absolute changes such as terminal ROIC.

| Variable | Bear relative to Base | Bull relative to Base |
|---|---|---|
| 2027–2031 revenue growth | -150, -140, -130, -110, -90bp | +80, +80, +80, +70, +50bp |
| 2027–2031 operating margin | -100, -120, -140, -150, -160bp | +50, +70, +90, +100, +110bp |
| Normal tax rate | +100bp | -50bp |
| D&A/revenue | No change | No change |
| 2027–2031 CapEx/revenue | +20bp in every year | -10bp in every year |
| Change in NWC/revenue | No change | No change |
| WACC | +50bp | -50bp |
| Terminal growth | -50bp | +50bp |
| Terminal ROIC | -5 percentage points | +5 percentage points |
| IRS win probability | -10 percentage points | +10 percentage points |

These adjustments define analytical cases rather than empirically estimated confidence intervals. Because WACC, terminal growth, and terminal ROIC change together, the integrated cases intentionally magnify differences in long-run value. The single-factor sensitivity matrix should be used when the objective is to isolate the marginal effect of discount and growth assumptions.

## Appendix C: Formula Set and Fully Worked 2027 Example

The model uses the following core formulas:

```text
Estimated CCBA revenue
= reported revenue × (Bottling Investments share
  - Bottling Investments share excluding CCBA)

Revenue[t]
= Revenue[t-1] × (1 + growth[t])

EBIT[t]
= Revenue[t] × operating margin[t]

NOPAT[t]
= EBIT[t] × (1 - tax rate[t])

D&A[t]
= Revenue[t] × D&A/revenue[t]

CapEx[t]
= Revenue[t] × CapEx/revenue[t]

Change in NWC[t]
= Revenue[t] × change in NWC/revenue[t]

FCFF[t]
= NOPAT[t] + D&A[t] - CapEx[t] - change in NWC[t]

Present value of FCFF[t]
= FCFF[t] / (1 + WACC)^discount period[t]

Terminal reinvestment rate
= terminal growth / terminal ROIC

Terminal FCFF
= prior-year NOPAT × (1 + terminal growth)
  × (1 - terminal reinvestment rate)

Terminal value
= Terminal FCFF / (WACC - terminal growth)

Enterprise value
= sum of present value of explicit FCFF
  + present value of terminal value

Equity value
= enterprise value - debt + cash + securities
  + equity-method investments + transaction assets - NCI

Expected IRS adjustment
= probability of win × refund if successful
  - probability of loss × (remaining liability + PV of future tax drag)

Fair value per share
= equity value / diluted shares
```

The complete 2027 Base Case calculation, retaining additional decimal precision, is:

```text
Step 1: Revenue
= $46.8803232 × (1 + 4.7%)
= $49.0836984

Step 2: EBIT
= $49.0836984 × 33.7%
= $16.5412064

Step 3: NOPAT
= $16.5412064 × (1 - 20.0%)
= $13.2329651

Step 4: D&A
= $49.0836984 × 1.7%
= $0.8344229

Step 5: CapEx
= $49.0836984 × 3.6%
= $1.7670131

Step 6: Change in NWC
= $49.0836984 × 0.0%
= $0

Step 7: FCFF
= $13.2329651 + $0.8344229 - $1.7670131 - $0
= $12.3003748

Step 8: Discount factor
= 1 / (1 + 6.7%)^0.87
= 0.9451418

Step 9: Present value of 2027 FCFF
= $12.3003748 × 0.9451418
= $11.6255980
```

The same sequence is used for 2028–2031, with only the applicable annual growth, margin, and capital expenditure ratios changing. Full-precision results are available in [`outputs/forecast.csv`](outputs/forecast.csv), and all three scenario forecasts are in [`outputs/scenario_forecast.csv`](outputs/scenario_forecast.csv).

## Appendix D: Validation, Limitations, and Non-Interchangeable Measures

The model performs mechanical reconciliation and arithmetic checks. All currently pass:

| Validation | Calculation | Expected result | Status |
|---|---:|---:|---|
| 2025 comparable operating margin | 15.013 / 48.062 = 31.2367% | 31.24% | Pass |
| 2025 adjusted FCF excluding fairlife | 7.408 - 2.112 + 6.069 = 11.365 | 11.365 | Pass |
| 2026 management FCF guidance | 14.6 - 2.2 = 12.4 | 12.4 | Pass |
| Enterprise value | PV of explicit FCFF plus PV of terminal value | 326.504 | Pass |
| Core equity value | Sum of enterprise-to-equity bridge | 320.099 | Pass |
| Risk-adjusted fair value | Core equity plus IRS adjustment | $72.24/share | Pass |
| Integrated Base core value | Scenario engine equals main Base model | $74.22/share | Pass |
| Integrated Base risk-adjusted value | Scenario engine equals main Base model | $72.24/share | Pass |

These checks demonstrate that the accounting reconciliations and arithmetic are internally consistent. They do not prove that growth, margin, WACC, terminal ROIC, or litigation probabilities are correct. Several measures must not be mixed:

- Company-defined FCF is not the same as FCFF.
- Comparable and underlying non-GAAP measures should not be mixed with reported GAAP measures without a stated purpose and reconciliation.
- Explicit CapEx and working-capital deductions should not be combined with a second `g/ROIC` reinvestment deduction in the same period.
- IRS risk should not be included in both the normalized operating tax rate and the equity adjustment.
- A historical base from which CCBA has already been fully removed should not receive a second divestiture haircut.
- A DCF based on EBIT excludes equity-method earnings, so the related investment value should not be omitted from the equity bridge.

The principal model limitations are as follows:

1. Estimated CCBA revenue is derived from disclosed revenue shares and is not a separately audited figure.
2. Post-CCBA D&A and CapEx ratios must be validated against financial statements after the transaction closes.
3. The 2027–2031 growth forecast is a top-down fade and does not separately model volume, price/mix, and currency.
4. Equity-method investments are included at carrying value rather than valued individually.
5. CCBA consideration is included before separately modeling transaction costs, taxes, timing differences, or closing risk.
6. The IRS win probability is subjective, and the simplified perpetuity for future tax drag does not explicitly model the timing of a final ruling.
7. WACC uses time-sensitive market inputs and should be updated with Treasury yields, ERP, beta, credit spreads, and capital weights.
8. Terminal value represents a large share of enterprise value, making the result highly sensitive to long-run assumptions.
9. No probabilities are assigned to Bear, Base, and Bull, so the model does not calculate a probability-weighted scenario target.

## Appendix E: Reproduction and File Map

The model is fully reproducible using only the Python standard library. Update reported facts first, then analytical assumptions, and rerun the model:

```bash
python3 model.py
```

| File | Purpose |
|---|---|
| [`data/facts.csv`](data/facts.csv) | Reported facts, guidance, market observations, dates, classifications, and original sources |
| [`data/assumptions.csv`](data/assumptions.csv) | Base Case assumptions, methods, and rationale |
| [`data/scenario_assumptions.csv`](data/scenario_assumptions.csv) | Bear, Base, and Bull operating and valuation assumptions |
| [`model.py`](model.py) | Complete reproducible calculation engine |
| [`outputs/derived_inputs.csv`](outputs/derived_inputs.csv) | CCBA, capital structure, WACC, and forward EPS derivations |
| [`outputs/forecast.csv`](outputs/forecast.csv) | Base Case 2027–2031 FCFF forecast |
| [`outputs/scenario_forecast.csv`](outputs/scenario_forecast.csv) | Annual forecast for all integrated scenarios |
| [`outputs/operating_scenarios.csv`](outputs/operating_scenarios.csv) | Scenario enterprise value, equity value, IRS adjustment, and per-share value |
| [`outputs/valuation_summary.csv`](outputs/valuation_summary.csv) | Explicit-period and terminal-value calculations |
| [`outputs/equity_bridge.csv`](outputs/equity_bridge.csv) | Enterprise-to-equity reconciliation |
| [`outputs/irs_scenarios.csv`](outputs/irs_scenarios.csv) | Single-factor IRS probability analysis |
| [`outputs/sensitivity.csv`](outputs/sensitivity.csv) | WACC and terminal-growth sensitivity matrix |
| [`outputs/fair_value_summary.csv`](outputs/fair_value_summary.csv) | Core and risk-adjusted fair value and justified P/E |
| [`outputs/validation_checks.csv`](outputs/validation_checks.csv) | Mechanical reconciliation and arithmetic checks |

Running the model regenerates every output file. This separation between source facts, analyst assumptions, scenario definitions, calculations, and published results makes each material conclusion traceable and allows a reader to replace any disputed assumption without reconstructing the entire valuation.
