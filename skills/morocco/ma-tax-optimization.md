---
name: ma-tax-optimization
description: Use this skill whenever asked about legitimate tax optimization for a self-employed person, freelancer or sole trader in Morocco for tax year 2026, choosing the most efficient regime and using lawful levers without evasion. Trigger on phrases like "reduce tax Morocco", "optimiser mes impots Maroc", "auto-entrepreneur vs CPU", "tax planning Morocco freelancer", "quel regime fiscal Maroc", "lower my tax legally Morocco", "best status freelance Maroc", "كيف أقلل الضريبة". Covers the choice between auto-entrepreneur (0.5% or 1% of turnover), the Contribution Professionnelle Unique (CPU) and the simplified or real net result (RNS or RNR, net profit on the IR scale to 37%), worked both ways to the figure that decides; the MAD 80,000 single-client rule and disguised-employment risk; the cotisation minimale and its three-year start exemption; VAT exposure; and when to consider incorporating. Reply in the user's language (English, French or Darija). Legal planning only, never evasion. Cross-reference ma-auto-entrepreneur, ma-cpu, morocco-professional-income-tax.
version: 2.0
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-14
type: decision
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
---

# Morocco: legitimate tax optimization for the self-employed, tax year 2026 (optimisation fiscale legale)

## Scope

This skill helps a self-employed person in Morocco (a freelancer, sole trader or independent professional, travailleur independant) pay the least tax the law allows for 2026, by choosing the right regime and using lawful levers. It is planning, not evasion. Every figure is from the 2026 Code General des Impots (CGI), which includes Finance Law 50-25 for 2026, administered by the Direction Generale des Impots (DGI).

The decisive idea: the self-employed are taxed under the Impot sur le Revenu (IR), but the base depends on the regime. The same MAD 300,000 of turnover can produce very different tax depending on whether it is taxed as a flat percentage of turnover (auto-entrepreneur), turnover times a trade coefficient (CPU), or real net profit on the progressive scale (RNS or RNR). Optimization is mostly matching the regime to the turnover and the margin.

This skill sits above the regime skills and helps choose between them. For the mechanics defer to `ma-auto-entrepreneur` (the 0.5% and 1% regime and its CNSS and AMO cover), `ma-cpu` and `morocco-professional-income-tax` (the scale, RNS and RNR, deductions). Reply in the user's language and keep the native terms (auto-entrepreneur, CPU, RNS, RNR, IR, TVA, CNSS, cotisation minimale, DGI).

## Ask the client first

1. Activity: commercial, industrial or craft, or services? Name the trade (the CPU coefficient and the CPU exclusions depend on it).
2. Turnover collected in 2026 and in each of the last two years.
3. Real costs: what is the genuine net margin (profit divided by turnover)?
4. Clients: how many, and does any one pay more than MAD 80,000 a year for services? Is the work done under that client's direction?
5. When did the activity start (the cotisation minimale start exemption runs for three financial years)?
6. Are the clients VAT-registered businesses or consumers, and how much VAT is on the person's own purchases?

## The method, step by step

1. **Check what is open.** Turnover against each regime's limit, the CPU excluded professions (see `ma-cpu`), AMO membership for CPU, social security membership for auto-entrepreneur.
2. **Price each open regime** on the client's own turnover and margin: auto-entrepreneur turnover x rate; CPU turnover x coefficient x 10% plus the droit complementaire; RNS or RNR net profit on the scale, never below the cotisation minimale.
3. **Test the single-client rule and the employment substance** before recommending anything.
4. **Add the levers:** the three-year cotisation minimale exemption, VAT position, incorporation.
5. **Recommend the regime that survives audit,** not the one with the lowest headline number, and say what figure decides it.

### Rates, bands and thresholds

| Item | Rate or amount | Conditions | Year | Source URL |
|---|---|---|---|---|
| IR scale, exempt band | 0% to MAD 40,000 | Art. 73-I | 2026 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| IR scale bands | 10% (40,001 to 60,000), 20% (to 80,000), 30% (to 100,000), 34% (to 180,000) | Art. 73-I | 2026 | same |
| IR scale, top band | 37% above MAD 180,000 | Art. 73-I | 2026 | same |
| Auto-entrepreneur IR | 0.5% commercial, industrial, craft; 1% services, on turnover collected | Art. 73-III | 2026 | same |
| Auto-entrepreneur limits | MAD 500,000 commercial, industrial, craft; MAD 200,000 services | Art. 42 ter-II-A. Option stays valid until two consecutive years over (Art. 43-4°) | 2026 | same |
| Single-client rule, services | 30% withheld by the client on turnover above MAD 80,000 a year from that client | Art. 73-II-G-8° and 45 bis. Applies to auto-entrepreneurs and CPU payers | 2026 | same |
| CPU | Turnover x trade coefficient, then 10%, plus the droit complementaire (MAD 1,200 to 14,400 a year) | Art. 40-I, 73-II-B-6° | 2026 | same |
| CPU limits | MAD 2,000,000 commercial, industrial, craft; MAD 500,000 services | Art. 41-II-A | 2026 | same |
| RNS limits | MAD 2,000,000 commercial, industrial, craft; MAD 500,000 services, excluding VAT | Art. 39 | 2026 | same |
| Cotisation minimale, standard rate | 0.25% of turnover | Art. 144-I-D. RNS and RNR | 2026 | same |
| Cotisation minimale, listed liberal professions | 4% | Art. 144-I-D, professions at Art. 89-I-12° and 91-VI-1° taxed under IR | 2026 | same |
| Cotisation minimale, floor for RNS and RNR | MAD 1,500 a year, even with no turnover | Art. 144-I-D | 2026 | same |
| Cotisation minimale, start exemption | First three financial years after the activity starts | Art. 144-I-C-2°. Not again on restarting the same activity | 2026 | same |
| VAT rates | 20% standard, 10% reduced | Art. 99 | 2026 | same |
| VAT exemption for small makers and service providers | Turnover up to MAD 500,000, individuals | Art. 91-II-3°. Exemption without right to deduct | 2026 | same |
| Optional VAT registration | Binding for at least three consecutive years | Art. 90 | 2026 | same |

### The three options at a glance

| Regime | Tax base | Headline rate | Best when | Key limit |
| --- | --- | --- | --- | --- |
| Auto-entrepreneur (AE) | Turnover collected | 0.5% (goods) or 1% (services), final | Low costs, high margin, turnover within the limit | MAD 500,000 or 200,000; single-client MAD 80,000 rule |
| CPU | Turnover x trade coefficient | 10% on the coefficient base, plus droit complementaire | Turnover above AE limits, margin near the coefficient, no full accounts wanted | MAD 2,000,000 or 500,000; excluded professions |
| RNS or RNR (net profit) | Real net profit | Scale 0% to 37%, never below the cotisation minimale | High real costs, thin margin, or turnover above CPU limits | Books; cotisation minimale floor |

RNS (resultat net simplifie) and RNR (resultat net reel) both tax real net profit on the scale; RNR needs fuller accounting. See `morocco-professional-income-tax`.

### Break-even logic: turnover and margin decide

- **Auto-entrepreneur is hard to beat when margin is high and costs are low.** It taxes turnover at 0.5% or 1%. On MAD 200,000 of services, AE IR is MAD 2,000. No net-profit regime matches that for a freelancer with few costs.
- **Net profit (RNS or RNR) wins when margin is thin.** A trader reselling at a 10% margin pays AE or CPU on turnover the suppliers took; net profit deducts the cost of goods. The crossover is where net profit on the scale costs less than the turnover-based tax.
- **CPU sits between.** The coefficient approximates a margin for the trade, then 10% applies. CPU is not automatically cheaper: if the real margin is well below the coefficient, it can cost more (worked case 2).
- **Decision rule.** (1) Within the AE limit, high margin, no dominant client: AE. (2) Above the AE limit, within CPU, margin near the coefficient, trade not excluded: CPU. (3) Thin margin, turnover above CPU, or large real expenses (rent, salaries, equipment): RNS or RNR.
- **Margin sensitivity.** At a 20% net margin, 1% of turnover is 5% of profit, cheap. At a 5% margin it is 20% of profit, and a net-profit regime may now win. Always run the client's numbers.

### The MAD 80,000 single-client rule and disguised employment

**What the rule says.** When annual services turnover from one client passes MAD 80,000, the client withholds IR at 30% on the excess (Art. 73-II-G-8°, 45 bis). The flat rate applies only to the first MAD 80,000 from that client.

**Why it exists.** It targets disguised employment (salariat deguise): businesses replacing staff with auto-entrepreneurs to avoid payroll tax, CNSS and Labour Code duties.

**How to plan around it legitimately.** Never hide the relationship or split invoices across shell entities: that is evasion. The lawful options:
- Genuinely diversify clients, so no single one passes MAD 80,000.
- Accept the withholding and move to the right regime: re-run the break-even, CPU (if the trade is not excluded) or RNS or RNR may be lawful and cheaper.
- If the relationship is in substance employment, treat it as employment: a salaried contract with CNSS and wage withholding (see `morocco-payroll`).

**Red flags the DGI looks for.** One dominant client giving most or all income; subordination (fixed hours, the client's premises and equipment, direction and supervision); no business autonomy (no other clients, no own tools, no commercial risk, no right to refuse work); continuity like permanent employment. If several are present, warn the client: the DGI, the labour authorities and CNSS can requalify the relationship, with back taxes, contributions and penalties.

### Cotisation minimale, start years and VAT

- **Cotisation minimale.** Under RNS and RNR a low or no-profit year still owes the cotisation minimale on turnover: 0.25%, or 4% for the listed liberal professions, at least MAD 1,500 (Art. 144). It is a floor: a net-profit regime never costs less.
- **Start exemption.** IR taxpayers are exempt from the cotisation minimale for the first three financial years after the activity starts, once only for the same activity (Art. 144-I-C-2°). In early thin-margin years a net-profit regime gets more attractive; note when the window ends.
- **VAT.** Individual makers and service providers with turnover up to MAD 500,000 are exempt without the right to deduct (Art. 91-II-3°); details and the trader rules are in `morocco-vat`. Above that, VAT applies at 20% (10% for some items) with input VAT deductible. Optional registration can pay when clients are VAT-registered and the person carries input VAT, but it binds for at least three years (Art. 90): model it first.
- **Do not suppress turnover** to stay under a limit. Declining work is a business choice; concealing turnover is evasion.

### Incorporating, exports and Casablanca Finance City

Export reliefs and Casablanca Finance City (CFC) status are company (IS) matters, not for a bare sole trader. Mention them only as a "consider incorporating" prompt and route to `morocco-corporate-income-tax` and a specialist. Their 2026 terms are not confirmed in this skill.

## Boundary and exception table

| Situation | Risk or rule | What to do |
|---|---|---|
| One dominant client plus subordination | Requalification as employment | Flag; consider a salaried contract; never facilitate |
| Turnover split across relatives or sham entities to stay under limits or the MAD 80,000 rule | Abusive and illegal | Refuse |
| Turnover under-declared or off-book | Evasion | Refuse |
| AE turnover over the limit in one year | Option stays valid; two consecutive years over moves the person to RNR from 1 January of the next year unless RNS or CPU is chosen (Art. 43-4°) | Plan the move; do not hide it |
| CPU chosen with real margin far below the coefficient | CPU can cost more | Price RNS or RNR too |
| Net-profit regime modelled without the cotisation minimale | Understates the tax | Apply the floor |
| Optional VAT election | Three-year lock-in (Art. 90) | Model before opting |
| Trade on the CPU excluded list (consultants, IT services, medical, legal and others) | CPU closed at any turnover | AE or RNS or RNR only |

### Conservative defaults

- Default to the regime that survives audit, not the lowest headline number.
- Treat a single client above MAD 80,000 as a red flag until the relationship is shown to be genuinely independent.
- Assume VAT applies above the exemption limit unless an exemption is clearly established.
- Assume the standard cotisation minimale applies once the three-year window closes.
- State any figure on the Not yet confirmed line as provisional and send the user to the DGI or an expert-comptable.

## Worked cases

Illustrative clients; 2026 rates and limits from the table above.

**Case 1, a decision: Amine, freelance developer, services turnover MAD 180,000, several clients (none above MAD 80,000), real costs MAD 15,000.** AE: 180,000 x 1% = MAD 1,800, final, within the MAD 200,000 limit. RNS: net profit 165,000 on the scale, 165,000 x 34% less 22,000 = MAD 34,100 (above the cotisation minimale). AE saves MAD 32,300. CPU is closed: IT service providers are on the excluded list. Recommendation: auto-entrepreneur; keep clients diversified and watch the MAD 200,000 limit.

```oa-check
name: Amine, AE against RNS
inputs:
  turnover: 180000
  costs: 15000
steps:
  - ae: turnover * 0.01
  - profit: turnover - costs
  - rns: profit * 0.34 - 22000
  - saving: rns - ae
expected:
  ae: 1800
  rns: 34100
  saving: 32300
```

**Case 2, a decision: Younes, electronics reseller, turnover MAD 1,200,000, cost of goods and expenses MAD 1,080,000, net profit MAD 120,000.** AE is closed (above MAD 500,000). RNS: 120,000 x 34% less 22,000 = MAD 18,800; the cotisation minimale is 0.25% x 1,200,000 = MAD 3,000, below the IR, so IR stands at MAD 18,800. CPU: trade "Autres produits non alimentaires", coefficient 12%: base 144,000, IR 14,400, droit complementaire MAD 6,000 (band 10,001 to 25,000), total MAD 20,400. RNS is cheaper by MAD 1,600 and deducts the real cost of goods. If he is in his first three financial years, the cotisation minimale is switched off, which only matters in a loss year. VAT applies at this turnover as a reseller only on the rules in `morocco-vat`.

```oa-check
name: Younes, RNS against CPU
inputs:
  turnover: 1200000
  profit: 120000
  coefficient: 0.12
  droit: 6000
steps:
  - rns_ir: profit * 0.34 - 22000
  - cm: max(turnover * 0.0025, 1500)
  - rns: max(rns_ir, cm)
  - cpu: turnover * coefficient * 0.10 + droit
  - cpu_extra: cpu - rns
expected:
  rns_ir: 18800
  cm: 3000
  rns: 18800
  cpu: 20400
  cpu_extra: 1600
```

**Case 3: Khadija, consultant invoicing one company MAD 240,000 a year.** Naive view: "1% is MAD 2,400". Wrong: only the first MAD 80,000 from that client stays at 1% (MAD 800); the client withholds 30% on the MAD 160,000 excess (MAD 48,000). Turnover is also above the MAD 200,000 services limit; the option stays valid for this year, but a second consecutive year over moves her to RNR (Art. 43-4°). One client and likely subordination: high requalification risk. Recommendation: (a) if genuinely independent, price RNS (CPU is likely closed, as legal, tax and other consultants are excluded); (b) if in substance an employee, a salaried contract. Never split invoices or interpose entities.

## When to refuse or refer

This skill gives legal tax optimization only. It must never:
- advise, design or facilitate tax evasion: under-declaring or concealing turnover or income, cash off-book, falsified records;
- help structure or disguise an employment relationship as freelancing to dodge payroll tax, CNSS or Labour Code duties (salariat deguise); where the substance is employment, say so;
- suggest fragmenting turnover across several auto-entrepreneurs, relatives or sham entities to stay under limits or the MAD 80,000 rule;
- recommend artificial invoice-splitting, backdating or fictitious deductions;
- present an abusive arrangement that fails a substance test as "optimization";
- state an unconfirmed figure as certain.

When a request crosses into evasion or disguised employment, decline the unlawful part, explain why, and offer the lawful alternative. Refer incorporation, export, CFC and any regime change with past-year consequences to a Moroccan expert-comptable.

## Filing and payment

The filing calendar for each regime is in `ma-return-assembly`: auto-entrepreneur monthly or quarterly (Art. 82 bis), CPU before 1 April of the following year (Art. 82 quater), RNS or RNR before 1 May (Art. 82-I). An option for a regime is made in writing to the tax inspector within the deadlines of Art. 43 and 44 (see `ma-cpu` for the CPU option).

## Completion checklist

- Regimes actually open checked: limits, CPU exclusions, membership conditions.
- Each open regime priced on the client's own turnover and margin, with the cotisation minimale floor on net-profit regimes.
- Single-client rule and employment substance tested.
- Start-year exemption, VAT position and lock-in considered.
- Recommendation names the deciding figure and survives audit.
- Nothing suggests splitting, concealment or disguised employment.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code Général des Impôts 2026, DGI, French edition (includes Finance Law 50-25). Read for Art. 73-I scale, Art. 73-III auto-entrepreneur rates, Art. 42 ter and 43-4° limits and exit, Art. 73-II-G-8° and 45 bis single-client 30%, Art. 40-I coefficients and Art. 73-II-B-6° droit complementaire, Art. 39 and 41-II limits, Art. 144 cotisation minimale (0.25%, 4%, MAD 1,500, three-year start exemption), Art. 89, 90, 91-II-3° and 99 VAT | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-14 |

Not yet confirmed: 2026 terms of export reliefs and Casablanca Finance City status for companies (old file: multi-year IS exemption then a reduced 20% rate); whether a given consultant trade is on the CPU excluded list (decree 2-08-124, see `ma-cpu`).
