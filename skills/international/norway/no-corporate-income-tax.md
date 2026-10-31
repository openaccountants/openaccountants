---
name: no-corporate-income-tax
description: "Corporate income tax (skatt på alminnelig inntekt for selskaper) in Norway for income year 2026. Covers who is taxable (AS, ASA and other companies, resident by incorporation or effective management from 2026), the 22% rate and the 25% rate for companies that pay financial-sector tax on wages, the petroleum special tax and resource rent tax rates, the participation exemption (fritaksmetoden) with its 3% rule, the interest limitation rule, depreciation groups, loss carry-forward, group contributions, the 31 May return, advance tax on 15 February and 15 April, withholding tax on dividends, interest and royalties, company exit taxation, and penalties. Trigger phrases: Norway corporate tax, selskapsskatt, skattemelding for AS, fritaksmetoden, rentebegrensning, kildeskatt på utbytte, forskuddsskatt AS, Norwegian company tax return. Out of scope: transfer pricing (no-transfer-pricing), payroll and contributions (no-employer-payroll, no-social-contributions), shareholder tax (no-capital-gains, no-income-tax), VAT (norway-mva, no-vat-return)."
version: 0.2
jurisdiction: "NO"
category: international
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway corporate income tax (2026)

Norway taxes companies on ordinary income (alminnelig inntekt) at a flat state rate. The rules sit in the Tax Act (skatteloven, sktl., lov 1999-03-26-14). The yearly rates sit in the Storting's tax decision for 2026 (Stortingets skattevedtak 2026, ssv., FOR-2025-12-18-2747). Returns and penalties follow the Tax Administration Act (skatteforvaltningsloven, sktfvl.). Payment and interest follow the Tax Payment Act (skattebetalingsloven, sktbl.). The income year is the calendar year.

## Who this applies to

- **Taxable companies.** Companies resident in Norway pay tax: AS and ASA, savings banks and other self-owning finance undertakings, mutual insurers, cooperatives, other bodies whose owners' liability is limited to the capital, state enterprises, inter-municipal companies, foundations, and estates _(sktl. § 2-2 first paragraph)_.
- **Not taxpayers in their own right.** General partnerships (ANS, DA), limited partnerships (KS), internal partnerships and shipowning partnerships. Each partner is taxed on its share of the partnership's wealth and income _(sktl. § 2-2 second and third paragraphs)_.
- **Residence from 2026.** A company is resident if it is incorporated under Norwegian company law, or if it has its effective management in Norway. Effective management looks at where board-level and day-to-day management is carried out, and at the company's other circumstances. A company that a tax treaty makes resident in another state is not resident in Norway. This wording applies from 1 January 2026 _(sktl. § 2-2 seventh and eighth paragraphs, as amended by lov 10 April 2025 nr. 9)_.
- **Worldwide scope.** A resident company is taxed on all its wealth and income in Norway and abroad _(sktl. § 2-2 sixth paragraph)_.
- **Non-resident companies** are taxed on Norwegian-source items, for example business carried on in or managed from Norway, and dividends from Norwegian companies under the withholding rules _(sktl. § 2-3 first paragraph letters b and c)_. See Cross-border points.
- **Wealth tax.** AS and ASA, limited-liability bodies under § 2-2 first paragraph e and g, securities funds and state enterprises do not pay wealth tax _(sktl. § 2-36 first paragraph)_. Other companies and bodies under § 2-36 second paragraph that are not exempt pay state wealth tax at 0.3%, with wealth under NOK 10,000 tax-free _(ssv. § 2-2)_.
- **No local income tax.** Companies that are separate taxpayers do not pay income tax to the municipality or county _(sktl. § 2-36 second paragraph)_. The whole rate goes to the state.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tax on ordinary income, companies | 22% | 2026 | ssv. § 3-3 first paragraph; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Companies that pay financial-sector tax on wages (finansskatt, folketrygdloven § 23-2a) | 25% | 2026 | ssv. § 3-3 second paragraph |
| Group entities within the global minimum tax | Supplementary tax (suppleringsskatt) under the Supplementary Tax Act | 2026 | ssv. § 3-3 third paragraph |
| Petroleum: ordinary tax on petroleum income | 22% | 2026 | ssv. § 4-1 third paragraph |
| Petroleum: special tax (særskatt) | 71.8% | 2026 | ssv. § 4-2 |
| Resource rent tax, hydropower | 57.7% | 2026 | ssv. § 3-4 |
| Resource rent tax, wind power | 32.1% | 2026 | ssv. § 3-4 |
| Resource rent tax, aquaculture | 32.1%; base deduction of NOK 70 million can be claimed | 2026 | ssv. § 3-4 A |
| State wealth tax, companies and bodies not exempt (not AS or ASA) | 0.3%; wealth under NOK 10,000 tax-free | 2026 | ssv. § 2-2 |
| Participation exemption: taxable share of exempt dividends | 3% of the dividend (22% x 3% = 0.66% effective) | 2026 | sktl. § 2-38 sixth paragraph letter a; https://lovdata.no/lov/1999-03-26-14/§2-38 |
| Participation exemption: holding test for shares outside the EEA | At least 10% of capital and votes, held continuously for 2 years | 2026 | sktl. § 2-38 third paragraph letters b and d |
| Interest limitation: cap | Net interest above 25% of ordinary income plus interest costs and tax depreciation, less interest income | 2026 | sktl. § 6-41 third paragraph; https://lovdata.no/lov/1999-03-26-14/§6-41 |
| Interest limitation: threshold, group companies | NOK 25 million net interest, for the Norwegian part of the group together | 2026 | sktl. § 6-41 fourth paragraph |
| Interest limitation: threshold, companies not in a group | NOK 5 million net interest | 2026 | sktl. § 6-41 fourth paragraph |
| Interest limitation: related-party test | At least 50% ownership or control, direct or indirect | 2026 | sktl. § 6-41 fifth paragraph |
| Interest limitation: carry-forward of disallowed interest | Next 10 years | 2026 | sktl. § 6-41 tenth paragraph |
| Group contribution: ownership test | Parent owns more than nine tenths of the shares and votes at year end | 2026 | sktl. § 10-4 first paragraph; https://lovdata.no/lov/1999-03-26-14/§10-4 |
| Capitalisation threshold for depreciable assets | Cost of NOK 30,000 or more and useful life of at least 3 years | 2026 | sktl. § 14-40 first paragraph letter a; https://lovdata.no/lov/1999-03-26-14/§14-40 |
| Declining-balance depreciation, groups a / b / c / d | 30% / 20% / 24% / 20% | 2026 | sktl. § 14-43 first paragraph; https://lovdata.no/lov/1999-03-26-14/§14-43 |
| Declining-balance depreciation, groups e / f / g / h / i / j | 14% / 12% / 5% / 4% / 2% / 10% | 2026 | sktl. § 14-43 first paragraph |
| Withholding tax on dividends to foreign shareholders | 25%, or the lower treaty rate | 2026 | ssv. § 3-5 third paragraph; sktl. § 10-13 |
| Withholding tax on interest, royalties and certain lease payments to related companies in low-tax countries | 15%, or the lower treaty rate | 2026 | ssv. § 3-5 fifth paragraph; sktl. §§ 10-80, 10-81 |
| Low-tax country | Tax on the company's total profit is less than two thirds of the Norwegian tax | 2026 | sktl. § 10-63 |
| Tonnage tax, first 1,000 net tonnes | NOK 0.90 per day per 100 net tonnes | 2026 | ssv. § 5-1 |
| Late-payment interest | 12% from 1 January 2026; 12.25% from 1 July 2026 | 2026 | sktbl. § 11-1; Skatteetaten, Forsinkelsesrenter; https://www.skatteetaten.no/satser/forsinkelsesrenter/ |
| Court fee (rettsgebyr), the base for coercive fines | NOK 1,345 | 2026 | Brønnøysundregistrene, late filing penalty page; https://www.brreg.no/en/submission-of-annual-accounts/late-filing-penalty/how-much-is-the-late-filing-penalty/ |

## The taxable base

**Start from the accounts.** Ordinary income is the accounting result adjusted by the tax rules. The return carries a business specification (næringsspesifikasjon). The exemption from that specification for turnover up to NOK 50,000 does not apply to companies under sktl. § 2-2 first paragraph _(skatteforvaltningsforskriften § 8-2-1 second paragraph letter a)_.

**Participation exemption (fritaksmetoden).** Companies, securities funds and the other bodies listed in § 2-38 first paragraph are not taxed on dividends and gains from shares in companies, and cannot deduct losses on them _(sktl. § 2-38 first and second paragraphs)_. Exceptions:
- Shares in companies in low-tax countries outside the EEA. Shares in low-tax companies inside the EEA that are not really established there with real economic activity _(§ 2-38 third paragraph letter a)_.
- Shares in companies outside the EEA: gains and dividends are exempt only if the holder has owned at least 10% of capital and votes continuously for 2 years _(§ 2-38 third paragraph letters b and d)_.
- Dividends the paying company can deduct _(§ 2-38 third paragraph letter h)_.
- **3% rule.** 3% of exempt dividends is still taxable income _(§ 2-38 sixth paragraph letter a)_. The 3% rule does not apply to dividends within a group where the group-contribution conditions in § 10-4 first paragraph are met, that is more than nine tenths ownership _(§ 2-38 sixth paragraph letter c)_. At 22%, the 3% rule costs 0.66% of the dividend.
- The 3% rule applies only to dividends. Exempt share gains are not subject to it.

**Interest limitation (sktl. § 6-41).** Net interest costs are deductible only up to 25% of a base. The base is ordinary income (or the year's loss) before the limitation, plus interest costs and tax depreciation, less interest income _(third paragraph)_.
- The cut applies only if net interest exceeds the threshold: NOK 25 million for the Norwegian part of a group, NOK 5 million for a company not in a group _(fourth paragraph)_.
- In a group, the cut can hit interest on both related and unrelated debt. Outside a group, the cut is limited to net interest on debt to related parties _(third paragraph)_.
- Related means 50% or more ownership or control, direct or indirect, at any time in the year _(fifth paragraph)_. Debt to an unrelated lender counts as related debt where a related party has given security for it _(seventh paragraph)_.
- A group company can claim full deduction if its equity ratio, or the equity ratio of the Norwegian part of the group, is at least the group's equity ratio in the consolidated accounts for the previous year _(eighth paragraph)_. This escape does not protect net interest on debt to related parties outside the group _(ninth paragraph)_.
- Disallowed interest carries forward for the next 10 years, inside the cap of later years _(tenth paragraph)_.

**Depreciation.** Assets with a useful life of at least 3 years and a cost of NOK 30,000 or more go into declining-balance groups _(sktl. § 14-40 first paragraph letter a)_. The maximum rates are: a office machines 30%; b acquired goodwill 20%; c lorries, buses, vans, taxis 24%; d cars, machinery, fixtures 20%; e ships and rigs 14%; f aircraft and helicopters 12%; g power transmission plant 5%; h buildings and plant, hotels 4%; i commercial buildings 2%; j fixed technical installations in buildings 10% _(sktl. § 14-43 first paragraph)_. Buildings so simple that their life is 20 years or less can use 10% _(§ 14-43 second paragraph)_.

**Losses.** A loss is deducted against income of later years, oldest loss first _(sktl. § 14-6 first paragraph)_. The section sets no time limit. After a debt composition, the loss counts only beyond the debt forgiven _(§ 14-6 second paragraph)_. A loss covered by a received group contribution cannot be carried forward _(§ 14-6 fifth paragraph)_.

**Group contribution (konsernbidrag).** An AS or ASA may deduct a group contribution to the extent it fits within its otherwise taxable ordinary income and is lawful under company law _(sktl. § 10-2 first paragraph)_. Giver and recipient must be Norwegian companies in the same group, with the parent owning more than nine tenths of the shares and votes at year end _(sktl. § 10-4 first paragraph)_. There is no deduction against petroleum income _(§ 10-2 second paragraph)_.

**Anti-avoidance.** Where the main purpose of an arrangement was a tax advantage and an overall assessment says it cannot be accepted, tax is assessed as if the arrangement reflected its economic substance _(sktl. § 13-2)_. Related-party pricing is in [no-transfer-pricing](no-transfer-pricing.md).

## Deadlines and filing

- **Return (skattemelding for formues- og inntektsskatt).** Due by the end of May in the year after the income year for companies under sktl. § 2-2 first paragraph _(skatteforvaltningsforskriften § 8-2-3 first paragraph letter a)_. For 2026: 31 May 2027. A business must file the return electronically _(skatteforvaltningsforskriften § 8-1-2 second paragraph letter a)_. Partners in a partnership that files a partnership return have the same deadline as the partnership _(§ 8-2-3 third paragraph)_.
- **Who must file.** Anyone with wealth or income taxable in Norway must file, unless the only liability is under the withholding rules in sktl. §§ 10-80, 10-81 or 10-13 _(sktfvl. § 8-2 first paragraph letter a)_.
- **Auditor signature.** Where the company has an auditor, the signature-required business information and group-contribution information must be signed by the auditor _(skatteforvaltningsforskriften § 8-2-7)_.
- **Accounting year.** The return covers the previous calendar year's income and wealth at 1 January of the assessment year. A different accounting year is allowed only under an exemption in the Accounting Act § 1-7, and it cannot exceed 12 months _(skatteforvaltningsforskriften § 8-2-2)_.
- **Advance tax (forskuddsskatt).** For companies, advance tax falls due in two equal instalments on 15 February and 15 April of the year after the income year, but not earlier than three weeks after the notice was sent _(sktbl. § 10-20 third paragraph)_. For 2026: 15 February 2027 and 15 April 2027. If an instalment is not paid, the later one falls due at once _(§ 10-20 fourth paragraph)_.
- **Balance due (restskatt).** For companies, due three weeks after the tax settlement was sent _(sktbl. § 10-21 third paragraph)_.

## Penalties and interest

- **Coercive fine (tvangsmulkt)** for missing information, including a missing return: half a court fee per day _(skatteforvaltningsforskriften § 14-1-1 first paragraph)_, so NOK 672.50 a day at the NOK 1,345 court fee. The total cannot exceed 50 court fees _(sktfvl. § 14-1 second paragraph)_, so NOK 67,250.
- **Additional tax (tilleggsskatt):** 20% of the tax advantage that was or could have been obtained _(sktfvl. § 14-5 first paragraph)_.
- **Aggravated additional tax:** a further 20% or 40% where information was wrong or missing wilfully or with gross negligence _(sktfvl. § 14-6 first and third paragraphs)_.
- **Late-payment interest** runs from the due date until payment _(sktbl. § 11-1 first paragraph)_. The 2026 rate is 12% from 1 January and 12.25% from 1 July _(Skatteetaten, Forsinkelsesrenter)_.
- **Interest on later increases.** Tax increased by a change decision, or by the company's own correction, carries interest from the original due date _(sktbl. § 11-2 first and second paragraphs)_.
- **Change window.** The tax office can reopen an assessment for 5 years after the end of the income year, and for 10 years where aggravated additional tax is imposed _(sktfvl. § 12-6 first and second paragraphs)_.

## Cross-border points

- **Dividends paid abroad.** Dividends to foreign shareholders bear withholding tax at 25% unless a treaty gives a lower rate _(ssv. § 3-5 third paragraph; sktl. § 10-13 first paragraph)_. A foreign company that corresponds to a Norwegian company covered by the participation exemption is exempt, but only if it is really established and carries on real economic activity in an EEA state _(sktl. § 2-38 first paragraph letter i and fifth paragraph)_.
- **Interest and royalties.** Norway has no general withholding tax on interest or royalties. A related company resident in a low-tax country pays 15% (or the lower treaty rate) on interest, royalties and payments for ships, rigs, aircraft and helicopters received from a Norwegian payer _(sktl. §§ 10-80, 10-81 first paragraph; ssv. § 3-5 fifth paragraph)_. Recipients really established with real economic activity in an EEA state are exempt _(§§ 10-80, 10-81 second paragraph letter a)_.
- **Low-tax country** means a country where tax on the company's total profit is less than two thirds of the tax it would have paid if resident in Norway _(sktl. § 10-63)_. The same test drives the controlled foreign company (NOKUS) rules in sktl. §§ 10-60 to 10-68.
- **Exit of a company.** When a company stops being resident in Norway, its assets and liabilities are treated as realised at market value on the last day before. This applies only where it becomes resident outside the EEA, or in a low-tax EEA state without real establishment and activity _(sktl. § 10-71 first and second paragraphs)_.
- **Petroleum.** Dividends from a Norwegian AS or ASA taxed under the Petroleum Tax Act § 5 to a foreign company owning at least 25% directly are free of tax, for the part relating to special-tax income _(ssv. § 4-4)_.
- **Non-resident companies with a Norwegian business** also fall under the interest limitation. Their interest is split between related and unrelated debt by the average balances at 1 January and 31 December _(sktl. § 6-41 first paragraph letter d and sixth paragraph)_.
- **Individuals moving abroad** with shares: see [norway-to-switzerland-wealth-tax-exit](norway-to-switzerland-wealth-tax-exit.md) and [no-individual-residence](no-individual-residence.md).

## Worked examples

### Example 1: Holding and trading AS, ordinary year

An Oslo AS has 2026 accounting profit of NOK 2,000,000. This includes a NOK 300,000 dividend from a Norwegian AS in which it holds 40%, and a NOK 500,000 gain on selling shares in another Norwegian AS. It has a NOK 400,000 loss carried forward from 2024. It is not in a group with the dividend payer.

Both the dividend and the gain are exempt under the participation exemption, so take them out (sktl. § 2-38 first and second paragraphs). A 40% holding is not more than nine tenths, so 3% of the dividend, NOK 9,000, stays taxable (§ 2-38 sixth paragraph letter a). Income before losses is 2,000,000 - 300,000 - 500,000 + 9,000 = NOK 1,209,000. Deduct the 2024 loss (§ 14-6): NOK 809,000. Tax at 22% (ssv. § 3-3) is NOK 177,980. If the advance tax notice matches, it is paid on 15 February and 15 April 2027 (sktbl. § 10-20 third paragraph), NOK 88,990 each.

```oa-check
name: Norwegian AS 2026, participation exemption with 3% rule and loss carried forward
inputs:
  accounting_profit: 2000000
  dividend: 300000
  share_gain: 500000
  loss_brought_forward: 400000
steps:
  - taxable_dividend_share: dividend * 0.03
  - income_before_loss: accounting_profit - dividend - share_gain + taxable_dividend_share
  - loss_used: min(loss_brought_forward, income_before_loss)
  - taxable_income: income_before_loss - loss_used
  - tax: taxable_income * 0.22
  - instalment: tax / 2
expected:
  taxable_dividend_share: 9000
  income_before_loss: 1209000
  loss_used: 400000
  taxable_income: 809000
  tax: 177980
  instalment: 88990
```

### Example 2: AS outside a group, interest to its owner above the cap

A property AS is not part of a group. All its debt is a loan from its sole personal owner. In 2026 it pays NOK 8,000,000 interest to the owner and has no interest income. Tax depreciation is NOK 1,500,000. Ordinary income before any interest cut is NOK 2,000,000.

Net interest of NOK 8,000,000 is above the NOK 5,000,000 threshold for a company not in a group, so the rule applies (sktl. § 6-41 fourth paragraph). The base is 2,000,000 + 8,000,000 + 1,500,000 = NOK 11,500,000. 25% of that is NOK 2,875,000. Net interest above that is NOK 5,125,000 (third paragraph). The owner holds 100%, so all the interest is on related debt and the full excess is cut. Taxable income is NOK 7,125,000 and tax at 22% is NOK 1,567,500. The NOK 5,125,000 carries forward for 10 years (tenth paragraph).

```oa-check
name: Norwegian AS not in a group, 2026 interest limitation on related-party interest
inputs:
  income_before_cut: 2000000
  net_interest: 8000000
  tax_depreciation: 1500000
  related_net_interest: 8000000
steps:
  - base: income_before_cut + net_interest + tax_depreciation
  - cap: base * 0.25
  - excess: max(0, net_interest - cap)
  - disallowed: min(excess, related_net_interest)
  - taxable_income: income_before_cut + disallowed
  - tax: taxable_income * 0.22
expected:
  base: 11500000
  cap: 2875000
  excess: 5125000
  disallowed: 5125000
  taxable_income: 7125000
  tax: 1567500
```

## Ask the client first

1. Is the company in a group (consolidated line by line, or could it be under IFRS), and who owns or controls it with 50% or more? This decides the interest threshold and which interest can be cut.
2. Which companies does it hold shares in, in which countries, what percentage, and since when? This decides the participation exemption and the 3% rule.
3. Does it pay financial-sector tax on wages, or have petroleum, hydropower, wind or aquaculture income? Different rates apply.
4. Does it pay dividends, interest, royalties or lease payments to foreign related parties, and in which countries? This decides withholding tax.
5. Was it incorporated in Norway, and where do the board and daily management meet and decide? This decides residence from 2026.
6. What losses and disallowed interest are carried forward, and from which years?

## Sources

| Source | URL | Read on |
|---|---|---|
| Skatteloven (lov 1999-03-26-14) §§ 2-2, 2-3, 2-36, 2-38 | https://lovdata.no/lov/1999-03-26-14/§2-2 | 2026-10-30 |
| Skatteloven § 6-41 (interest limitation) | https://lovdata.no/lov/1999-03-26-14/§6-41 | 2026-10-30 |
| Skatteloven §§ 10-2, 10-4, 10-13, 10-63, 10-71, 10-80, 10-81 | https://lovdata.no/lov/1999-03-26-14/§10-4 | 2026-10-30 |
| Skatteloven § 13-2 (anti-avoidance) | https://lovdata.no/lov/1999-03-26-14/§13-2 | 2026-10-30 |
| Skatteloven §§ 14-6, 14-40, 14-43 | https://lovdata.no/lov/1999-03-26-14/§14-43 | 2026-10-30 |
| Stortingets skattevedtak 2026 (FOR-2025-12-18-2747, as amended by FOR-2026-06-19-1243) | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 | 2026-10-30 |
| Skatteforvaltningsloven §§ 8-2, 12-6, 14-1, 14-5, 14-6 | https://lovdata.no/lov/2016-05-27-14/§8-2 | 2026-10-30 |
| Skatteforvaltningsforskriften §§ 8-1-2, 8-2-1, 8-2-2, 8-2-3, 8-2-7, 14-1-1 | https://lovdata.no/forskrift/2016-11-23-1360/§8-2-3 | 2026-10-30 |
| Skattebetalingsloven §§ 10-20, 10-21, 11-1, 11-2 | https://lovdata.no/lov/2005-06-17-67/§10-20 | 2026-10-30 |
| Skatteetaten, Forskuddsutskrivingen 2026 | https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ | 2026-10-30 |
| Skatteetaten, Forsinkelsesrenter (2026) | https://www.skatteetaten.no/satser/forsinkelsesrenter/ | 2026-10-30 |
| Skatteetaten, Avskrivningssatser | https://www.skatteetaten.no/satser/avskrivningssatser/ | 2026-10-30 |
| Brønnøysundregistrene, how much is the late filing penalty (court fee NOK 1,345) | https://www.brreg.no/en/submission-of-annual-accounts/late-filing-penalty/how-much-is-the-late-filing-penalty/ | 2026-10-30 |

Not yet confirmed: the Petroleum Tax Act's own base rules (uplift, deductions) and the resource rent bases for hydropower, wind and aquaculture, which are given here only by rate; the Supplementary Tax Act (global minimum tax) scope and rate; the full CFC (NOKUS) computation; loss carry-back on cessation (sktl. § 14-7); the amendment to sktl. § 14-6 by lov 19 June 2026 nr. 48, which is not yet in force; how advance tax for companies is set; the 2026 rate of interest on restskatt.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
