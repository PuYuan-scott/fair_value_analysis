# KO DCF：完整数据、假设与计算说明

完整、可直接作为报告正文使用的英文版本见 [`KO_DCF_Article_EN.md`](KO_DCF_Article_EN.md)。本文件保留为模型使用说明和快速计算摘要。

## 结论

估值日为 2026-08-19。Base Case 的模型结果为：

- Core fair value：约 **$74.22/股**；
- IRS 风险调整：约 **-$1.98/股**；
- Risk-adjusted fair value：约 **$72.24/股**；
- 2026 comparable EPS 中点：**$3.285/股**；
- 对应合理 forward P/E：core **22.59x**，risk-adjusted **21.99x**。

这不是精确价格预测。终值约占 EV 的 83%，所以 WACC、永续增长率和 terminal ROIC 是最重要的估值变量。

## 文件结构

| 文件 | 内容 |
|---|---|
| `data/facts.csv` | 财报事实、管理层指引、市场观察、日期和原始来源 |
| `data/assumptions.csv` | Base Case 假设、计算方法和选择理由 |
| `data/scenario_assumptions.csv` | Bear/Base/Bull 三套经营与估值假设 |
| `model.py` | 只使用 Python 标准库的完整计算脚本 |
| `outputs/derived_inputs.csv` | CCBA、WACC、forward EPS 等推导过程 |
| `outputs/forecast.csv` | 2027–2031 年逐项 FCFF |
| `outputs/valuation_summary.csv` | 终值、折现和企业价值 |
| `outputs/equity_bridge.csv` | EV 到股权价值及每股价值 |
| `outputs/irs_scenarios.csv` | IRS 胜诉概率为 50%、60%、70%时的结果 |
| `outputs/sensitivity.csv` | WACC × terminal growth 敏感性矩阵 |
| `outputs/scenario_forecast.csv` | 三种经营情景的逐年收入与 FCFF |
| `outputs/operating_scenarios.csv` | 三种综合情景的 EV、IRS 调整和每股价值 |
| `outputs/fair_value_summary.csv` | 最终 fair value 和合理 forward P/E |
| `outputs/validation_checks.csv` | 财报口径和模型加总的一致性检查 |

重新计算：

```bash
python3 model.py
```

所有输出 CSV 都会被重新生成。修改 Base 假设时编辑 `data/assumptions.csv`；修改三种情景时编辑 `data/scenario_assumptions.csv`。

## 一、事实、推导和假设必须分开

模型把数据分为三种：

1. **Reported fact**：例如 2025 revenue、2026 Q2 debt；
2. **Derived input**：例如推算 CCBA revenue、资本结构权重；
3. **Analyst assumption**：例如 2029 revenue growth、terminal ROIC。

公司 guidance 是事实，但 guidance 中的预测数字仍然不是已经实现的历史结果。模型不会把 management guidance 自动延伸到五年以后。

## 二、为什么先做 CCBA pro forma

2025 comparable revenue 为：

```text
$48.062B
```

公司披露 Bottling Investments 占 2025 revenue 的 12%，同时披露排除 CCBA 后 Bottling Investments 仅占约 4%。因此估算：

```text
CCBA revenue
= 2025 reported revenue × (Bottling share - Bottling ex-CCBA share)
= $47.941B × (12% - 4%)
= $3.835B
```

这不是公司直接披露的 CCBA revenue，而是由公司披露的收入占比推算。

```text
2025 pro forma comparable revenue ex-CCBA
= $48.062B - $3.835B
= $44.227B
```

2026 guidance 是 organic revenue 约 +5%、FX 约 +1%、M&A/divestiture 约 -2%至-3%。由于模型已经把 CCBA 从历史基数中完整删除，所以 2026 pro forma revenue 只应用 organic 和 FX：

```text
2026 pro forma revenue ex-CCBA
= $44.227B × (1 + 5% + 1%)
= $46.880B
```

不能再扣一次 -2.5% divestiture headwind，否则会重复计算 CCBA 出售。

## 三、Revenue growth 如何得到

采用的路径为：

| 年度 | Growth | 依据 |
|---|---:|---|
| 2026 pro forma | 6.0% | 5% organic guidance + 1% FX |
| 2027 | 4.7% | 去除一次性 FX 后，略低于当前 organic trend |
| 2028 | 4.4% | 向成熟增长回归 |
| 2029 | 4.1% | 向成熟增长回归 |
| 2030 | 3.8% | 接近长期水平 |
| 2031 | 3.5% | 接近但仍高于 terminal growth |
| Terminal | 3.0% | 全球成熟消费企业长期名义增长假设 |

计算公式：

```text
Revenue[t] = Revenue[t-1] × (1 + growth[t])
```

例如：

```text
2027 revenue = $46.880B × 1.047 = $49.084B
2028 revenue = $49.084B × 1.044 = $51.243B
```

这里没有假设当前 5% organic growth 永远持续；每年逐步回归 3% terminal growth。

## 四、Operating margin 如何得到

已知数据：

- 2025 comparable operating margin：31.24%；
- 2025 underlying operating margin：32.61%；
- 2026 H1 comparable operating margin：34.3%，但存在季度季节性；
- CCBA 属于低利润率、资本密集型瓶装业务，出售后公司组合更轻资产。

因此 Base Case 不直接使用 34.3%，而采用：

```text
33.7% → 33.8% → 33.9% → 34.0% → 34.1%
```

这相当于每年仅扩张 10bp。利润率改善已经进入 EBIT 和 FCFF，后面不会再因为“高利润率”人为提高 P/E，避免 double count。

```text
EBIT[t] = Revenue[t] × operating margin[t]
```

例如：

```text
2027 EBIT = $49.084B × 33.7% = $16.541B
```

## 五、Tax 和 NOPAT

管理层 2026 underlying effective tax rate guidance 为 19.9%。Base Case 四舍五入到 20.0%：

```text
NOPAT[t] = EBIT[t] × (1 - tax rate[t])
```

例如：

```text
2027 NOPAT = $16.541B × (1 - 20%) = $13.233B
```

20%税率不包含 IRS 诉讼败诉影响。IRS 风险在股权价值之后单独做概率加权，避免把诉讼风险同时放进税率和 bridge。

## 六、D&A、CapEx 和营运资本

2025 consolidated 数据：

```text
D&A / revenue = $1.050B / $47.941B = 2.19%
CapEx / revenue = $2.112B / $47.941B = 4.41%
```

CCBA 是资本密集型瓶装业务，相关 held-for-sale PP&E 占公司 PP&E 的较大部分。因此 post-CCBA 模型采用：

- D&A / revenue：1.7%；
- CapEx / revenue：从 3.6%逐步降至 3.2%；
- CapEx 始终高于 D&A，模型没有假设公司停止投资。

```text
D&A[t] = Revenue[t] × D&A ratio[t]
CapEx[t] = Revenue[t] × CapEx ratio[t]
```

营运资本采用零现金占用：

```text
ΔNWC[t] = 0
```

原因是 KO 长期拥有负营运资本，且 2024–2026 的 reported working-capital changes 被 fairlife payment、120天供应商账期和 supplier finance 明显扭曲。设为零意味着既不计现金释放，也不计额外现金消耗，是中性处理。

## 七、显式期 FCFF

显式期使用会计式 FCFF：

```text
FCFF[t]
= EBIT[t] × (1 - tax rate[t])
  + D&A[t]
  - CapEx[t]
  - ΔNWC[t]
```

以 2027 年为例：

```text
FCFF 2027
= $13.233B + $0.834B - $1.767B - $0
= $12.300B
```

公司 2026 guidance 的 $12.4B FCF 是 `CFO - CapEx`，已经扣除了利息，并可能包含权益法投资的股息，因此仅作为量级交叉检查，不直接作为 FCFF 输入。

显式期没有再使用 `NOPAT × (1-g/ROIC)`，否则会把 CapEx 和 ΔNWC 已经反映的再投资重复扣除。

## 八、WACC 的每一步

### 1. Cost of equity

```text
Risk-free rate = 4.5%
Raw beta = 0.35
Adjusted beta adopted = 0.60
ERP = 4.2%
```

beta 调整参考：

```text
Adjusted beta
= 2/3 × raw beta + 1/3 × 1.0
= 2/3 × 0.35 + 1/3
= 0.567 ≈ 0.60
```

```text
Cost of equity
= 4.5% + 0.60 × 4.2%
= 7.02%
```

### 2. Cost of debt

```text
Pretax cost of debt = 5.0%
After-tax cost of debt = 5.0% × (1 - 20%) = 4.0%
```

5.0%是当前再融资成本假设，不是历史利息费用除以债务。历史 coupon 不能代表未来融资成本。

### 3. Capital weights

总债务：

```text
$0.048B loans and notes
+ $6.494B current maturities
+ $37.001B long-term debt
= $43.543B
```

仅用于 WACC 权重的市场股权价值：

```text
$87.05 × 4.313B diluted shares = $375.447B
```

```text
E/V = 89.61%
D/V = 10.39%
```

```text
Calculated WACC
= 89.61% × 7.02% + 10.39% × 4.0%
= 6.706%
```

Base Case 采用四舍五入的 6.7%。市场价格只用于资本结构权重，未被用来决定 fair value。

## 九、折现期间

估值日在 2026-08-19，2027 是第一个完整预测年度。采用 mid-year convention：

| Cash flow | 折现年数 |
|---|---:|
| 2027 FCFF | 0.87 |
| 2028 FCFF | 1.87 |
| 2029 FCFF | 2.87 |
| 2030 FCFF | 3.87 |
| 2031 FCFF | 4.87 |
| 2031 year-end terminal value | 5.37 |

```text
PV(FCFF[t]) = FCFF[t] / (1 + WACC)^discount years
```

显式期 FCFF 现值合计约 $56.14B。

## 十、Terminal value

显式期采用会计式 FCFF，terminal period 使用 ROIC 检查永续增长需要的再投资：

```text
Terminal growth = 3.0%
Terminal ROIC = 25.0%
Terminal reinvestment rate
= terminal growth / terminal ROIC
= 3% / 25%
= 12%
```

```text
2032 terminal NOPAT
= 2031 NOPAT × 1.03
= $16.103B
```

```text
2032 terminal FCFF
= terminal NOPAT × (1 - 12%)
= $14.171B
```

```text
Terminal value at 2031 year-end
= $14.171B / (6.7% - 3.0%)
= $383.0B
```

折现后 terminal value 约 $270.35B。

```text
Fair EV
= PV(explicit FCFF) + PV(terminal value)
= $56.14B + $270.36B
= $326.50B
```

CSV 保留更多小数，以上展示值经过四舍五入。

## 十一、EV 到股权价值

```text
Fair EV                                      $326.50B
- Debt                                       (43.54B)
+ Cash and short-term investments             13.53B
+ Marketable securities                        2.84B
+ Equity-method investments                    20.78B
+ CCBA sale cash consideration                  1.30B
+ CCBA retained interest                        0.85B
- Noncontrolling interests                     (2.17B)
= Fair equity value before IRS                $320.10B
```

权益法收益在 income statement 中位于 operating income 以下。因此基于 EBIT 的 DCF 没有包含这些业务的现金流，对应的 equity-method investments 必须单独加回，否则会漏算。

Equity-method investments 采用账面价值而不是逐项市场价值；完整 NCI 均被扣除。两项处理整体偏保守。

```text
Core fair value per share
= $320.10B / 4.313B shares
= $74.22
```

## 十二、IRS 风险调整

Core DCF 既没有加入胜诉时可收回的 IRS deposit，也没有扣除败诉结果。

已披露数据：

```text
Refund if KO wins = $6.000B deposit + $0.514B interest = $6.514B
Remaining liability if KO loses = $14.9B
Potential future effective-tax-rate increase = 3.8 percentage points
```

未来年度税负估算：

```text
2026 pro forma EBIT
= $46.880B × 33.6%
= $15.752B
```

```text
Annual future tax drag
= $15.752B × 3.8%
= $0.599B
```

将其作为增长3%的长期税负估值：

```text
PV future tax drag if loss
= $0.599B / (6.7% - 3.0%)
= $16.18B
```

Base Case 主观胜诉概率为60%。这是分析假设，不是公司披露的概率。

```text
Expected IRS adjustment
= 60% × $6.514B
  - 40% × ($14.9B + $16.18B)
= -$8.52B
```

```text
Risk-adjusted fair value
= ($320.10B - $8.52B) / 4.313B
= $72.24/股
```

| 胜诉概率 | Fair value/股 |
|---:|---:|
| 50% | 约 $71.37 |
| 60% | 约 $72.24 |
| 70% | 约 $73.11 |

## 十三、敏感性

下表为 IRS 调整前的每股价值：

| WACC \ Terminal growth | 2.5% | 3.0% | 3.5% |
|---|---:|---:|---:|
| 6.2% | $77.13 | $86.04 | $98.22 |
| 6.7% | $67.74 | **$74.22** | $82.71 |
| 7.2% | $60.34 | $65.21 | $71.39 |
| 7.7% | $54.37 | $58.13 | $62.77 |

这个矩阵说明：`$74.22` 不是一个应当脱离假设使用的精确事实。对 KO 这类长久期公司，50bp 的 WACC 变化足以显著改变估值。

## 十三-A、综合经营情景

与只改变 WACC 和 terminal growth 的敏感性不同，综合情景同时改变收入增长、利润率、税率、CapEx、WACC、terminal growth、terminal ROIC 和 IRS 胜诉概率：

| 情景 | Core fair value/股 | Risk-adjusted fair value/股 |
|---|---:|---:|
| Bear | $52.32 | $49.87 |
| Base | $74.22 | $72.24 |
| Bull | $108.03 | $106.51 |

精确的逐年变量、相对 Base 的改变和形成理由见英文完整报告的 Sections 3 and 6 以及 Appendix B。综合情景用于检验成套假设下的边界，不代表统计置信区间，也没有被赋予发生概率。

## 十四、模型没有做什么

- 没有把 2026 H1 的 34.3% margin 永久化；
- 没有把管理层 5% organic growth 永久化；
- 没有把公司定义的 FCF 直接当成 FCFF；
- 没有在显式期同时使用 CapEx 法和 `g/ROIC` 法扣两次再投资；
- 没有把 IRS 风险同时放入税率和 equity bridge；
- 没有利用当前股价倒推结果，股价只影响 WACC 的资本权重。

## 十五、主要局限

1. CCBA revenue 是根据披露占比推算，不是单独审计数字；
2. Post-CCBA D&A 和 CapEx ratio 需要交易完成后的真实报表验证；
3. Equity-method investments 使用账面值，未逐项按市场价值估值；
4. 60% IRS 胜诉概率是主观假设；
5. 没有纳入分析师 consensus，只使用公司资料、市场参数和基本面回归路径；
6. 终值占比较高，因此必须结合敏感性区间使用。
