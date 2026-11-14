---
name: ls-transfer-pricing
description: "Lesotho transfer pricing for the 2026-27 year of assessment (1 April 2026 to 31 March 2027) under section 113 of the Income Tax Act 1993 as amended. Covers who is an associate (the directions or wishes test in section 3), the Commissioner General's power to distribute, apportion or allocate gross income, deductions and credits between associates, the commensurate-with-income rule for intangibles, recharacterisation of source and of revenue or capital, market value on non-arm's length disposals (s.61), disguised distributions taxed as dividends (s.88), the four-year window for amended assessments, records and additional tax, and Article 9 of the South Africa treaty. Lesotho has no transfer pricing regulations, documentation rule or advance pricing agreement in the law read. Trigger on: Lesotho transfer pricing, related party Lesotho, associates section 113, RSL TP adjustment, management fees to parent Lesotho, arm's length Lesotho. Out of scope: treaty mutual agreement procedure in depth, mining agreements."
version: 0.2
jurisdiction: LS
category: transfer-pricing
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-14
depends_on:
  - ls-corporate-income-tax
tier: 2
domain: transfer-pricing
type: situation-rules
---

# Lesotho transfer pricing: associates, section 113 adjustments and related rules (2026-27) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Lesotho's transfer pricing rule is one section: section 113 of the Income Tax Act 1993 (Act No. 9 of 1993, as amended), in Part XI (Anti-Avoidance) of Chapter II. Revenue Services Lesotho (RSL) administers it. The year of assessment runs from 1 April to 31 March (s.3, "year of assessment"), so this skill covers the 2026-27 year of assessment, 1 April 2026 to 31 March 2027. A company may have a different year allowed by the Commissioner General (s.49).

The text used is RSL's consolidated copy of the Act "Updated up to 1 April 2012". RSL's 2025-26 Integrated Annual Report says an Income Tax Amendment Bill was announced for tabling in FY2026/27, so the 1993 Act remains the base law; any amendment made after 2012 that RSL's copy does not show is on the "Not yet confirmed" line.

## Who this applies to

- **Associates (s.3(1)).** An associate of a person is any other person who acts, or is likely to act, in accordance with the directions, requests, suggestions or wishes of that person, whether or not they are communicated. There is no percentage ownership test in this definition. Whether a parent, subsidiary, sister company, family member or partner is an associate is a question of fact: who in practice follows whose wishes.
- **Transactions caught (s.113(1)).** Any transaction between taxpayers who are associates. The text does not limit it to cross-border dealings, so domestic dealings between associates are caught too.
- **Branches.** A Lesotho branch of a non-resident company is treated as a separate person which is a resident company (s.6(2)). Its dealings with head office are therefore dealings between separate persons, and fall under s.113 where the head office is also a taxpayer (for example, it receives Lesotho-source income) and the two are associates. Branch profits tax is in ls-cross-border.
- **Companies and members (s.88).** A loan, payment for property or services, disposal of an asset, provision of services or release of a liability by a company to or in favour of a member, or an associate of a member, that in substance is a distribution is treated as a dividend paid to the member.

Not covered here: thin capitalisation (no rule found in the Act read), treaty mutual agreement procedure in depth, and mining or Lesotho Highlands Water Project arrangements (Protocol V, s.112A).

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Company tax on an upward adjustment (ordinary income) | 25% | Third Schedule item 4; manufacturing income 10% (items 1 and 3; see ls-corporate-income-tax), never for a branch of a non-resident company (s.10(2)) | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Standard rate of tax | 25% | s.3 definition; non-residents (s.12) and s.107 withholding use it | same |
| Associate test | no percentage; acts in accordance with directions, requests, suggestions or wishes | s.3(1) | same |
| Time to amend an assessment | 4 years after service of the notice of assessment; any time for fraud or gross or wilful neglect | s.135(2) | same |
| Withholding on a management charge or royalty paid to a non-resident | 25% of the gross amount; 15% where solely for concessional manufacturing income | s.107(1), (3); full table in ls-cross-border | same |
| Additional tax (late payment, including tax found due after an adjustment) | specified rate, published by the Commissioner General from commercial lending rates | s.192, s.194 | same |
| Specified rate as RSL states it most recently | 3% a month, compounded monthly, from the due date | RSL Tax Guide on Provisional Tax, question 8 (file dated November 2023), stated for unpaid instalments under s.194; the older RSL Corporate Income Tax Guide (file dated May 2017, section 1.4) gave 22% per twelve months. No published s.192 rate notice was found | https://www.rsl.org.ls/sites/default/files/2024-05/Tax%20Guide%20on%20Provisional%20Tax%20%281%29.pdf |
| Poor records | additional tax of double the tax payable for the year | s.197 | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| False or misleading statement, knowingly or recklessly | additional tax of double the excess tax | s.198(1) | same |
| Lesotho and South Africa treaty: technical, managerial or consultancy fees to a South African resident beneficial owner | 7.5% of the gross amount | Treaty Article 13(2); RSL applies it from 27 June 2016; where a special relationship inflates the fee, the 7.5% cap covers only the arm's length amount and the excess stays taxable under domestic law (Article 13(6)) | https://www.rsl.org.ls/sites/default/files/2024-07/Guideline%20on%20Technical%20Services.pdf |

## The base

**The power (s.113(1)).** In any transaction between taxpayers who are associates, the Commissioner General may distribute, apportion or allocate gross income, deductions or credits between them as necessary to prevent the evasion of taxes or to clearly reflect their income. The Act does not use the words "arm's length price" in s.113; the measure is income that is clearly reflected.

**Intangibles (s.113(2)).** Income from a transfer or licence of intangible property between associates may be adjusted so that it is commensurate with the income attributable to the intangible.

**Recharacterisation (s.113(3)).** In making either adjustment, the Commissioner General may recharacterise the source of the income and the nature of a payment or loss as revenue, capital or otherwise. This matters for withholding: a payment recharacterised as Lesotho-source, or as a royalty or management charge, can attract s.107 withholding (see ls-cross-border).

**Instalment sales (s.113(4)).** Where property is sold for instalments and the sale gives no income apart from interest on the unpaid price, the Commissioner General may split the instalments into principal and interest, and the interest is income of the seller. This does not apply where the sale carries interest at an open market rate at the time of sale.

**General anti-avoidance (s.114).** Separately, the Commissioner General may recharacterise an element of a tax avoidance scheme, disregard a transaction without substantial economic effect, and recharacterise a transaction whose form does not reflect its substance.

**Asset disposals (s.61(2)).** Where an asset is disposed of in a non-arm's length transaction, the disposer is treated as receiving its fair market value at the date of disposal. For a gift, the greater of adjusted cost base and fair market value (s.61(3)).

**Methods and documentation.** The Act read sets no pricing methods, no comparability factors, no contemporaneous documentation duty and no advance pricing agreement procedure. The general record duty applies: a taxpayer keeps in Lesotho, in Sesotho or English, the records needed to determine the tax payable, for as long as they remain material (s.169). A deduction may be disallowed if the taxpayer cannot, without reasonable excuse, produce a record or evidence of the circumstances giving rise to it (s.169(2)). In practice, a file showing how each associate price was set is what answers a s.113 enquiry and a s.169(2) challenge.

**The burden of proof.** On objection or appeal, the taxpayer must prove that an assessment is excessive (s.141(1)).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Annual return of income (companies and individuals) | last day of the third month after the year end: 30 June 2027 for 2026-27 | ITA s.128(1) |
| Tax payable | on the date the return is due | ITA s.143(1) |
| Tax under an amended assessment (including a s.113 adjustment) | 30 days after service of the notice of assessment | ITA s.143(2) |
| Commissioner General may amend an assessment | within 4 years after service of the notice; any time for fraud or gross or wilful neglect | ITA s.135(2) |
| Objection to an amended assessment (for example a s.113 adjustment) | the later of 4 years after service of the original assessment and 60 days after service of the amended assessment; in writing, with detailed grounds | ITA s.137(2), (3) |
| Return of Lesotho-source interest, dividends, royalties, management fees and rent paid | within 28 days after the end of the year of assessment | ITA s.130 |

Tax under an assessment is payable even while an objection or appeal is pending (s.143(3)).

## Penalties and interest

- **Late payment.** Tax not paid by its due date, including tax under an amended assessment after a s.113 adjustment, carries additional tax at the specified rate on the deficiency from the due date (s.194(1)). The specified rate is the rate the Commissioner General publishes from normal commercial lending rates (s.192). RSL's most recent statement of it is 3% a month, compounded monthly (Tax Guide on Provisional Tax, question 8, file dated November 2023); an older RSL guide (Corporate Income Tax Guide, 1.4, file dated May 2017) gave 22% per twelve months. Confirm the current published rate before relying on either.
- **Records.** Failing to keep proper records: additional tax equal to double the tax payable for the year (s.197). This is not payable where the taxpayer has been convicted under s.176 for the same omission (s.199(4)).
- **False or misleading statements.** Knowingly or recklessly making a materially false or misleading statement: additional tax equal to double the excess tax (s.198).
- **Remission.** The Commissioner General may remit additional tax in whole or in part (s.199(2)).
- **Withholding.** Additional tax for not withholding on a management charge or royalty to a foreign associate is in ls-cross-border (s.196).

## Cross-border points

- **Treaties.** Article 9 (Associated Enterprises) of the Lesotho and South Africa agreement allows profits to be adjusted to what independent enterprises would have made where one enterprise participates directly or indirectly in the management, control or capital of the other, or the same persons participate in both. Article 9(2) requires the other State to make an appropriate corresponding adjustment, with the competent authorities consulting if necessary. Check the article in the treaty that applies; RSL lists treaties with South Africa, the United Kingdom, Mauritius, Botswana and Eswatini.
- **Payments to a foreign associate.** A management charge or royalty is subject to s.107 withholding (25%, or the treaty rate), and an amount above what clearly reflects income can also be reallocated under s.113. The South Africa agreement limits its reduced rates to the arm's length amount where a special relationship inflates interest, royalties or technical fees; the excess stays taxable under domestic law (Articles 11(6), 12(6) and 13(6)). A payment that in substance is a distribution to a member can be a dividend under s.88. See ls-cross-border for withholding rates and branch profits tax.
- **Tax havens (s.106).** Where a resident's transaction routes income through a non-resident company connected to a tax haven, the Commissioner General may adjust the resident's income and foreign tax credit. A country with which Lesotho has a double taxation agreement is not treated as a tax haven (s.106(3)).

## Two worked examples that recompute

### Example 1: under-remunerated Lesotho distributor

Maloti Distribution (Pty) Ltd (Lesotho, 31 March year end) buys all its stock from its South African parent, whose wishes it follows, so the two are associates. For the year to 31 March 2027 sales are M50,000,000 and its operating margin is 1%. Independent distributors earn a 4% operating margin.

- **Adjustment under s.113(1):** (4% - 1%) x 50,000,000 = M1,500,000 of extra chargeable income.
- **Extra tax at 25%:** M375,000.
- **If the adjusted tax is paid twelve months after it was due,** additional tax at RSL's most recently stated rate of 3% a month, compounded monthly, is 375,000 x (1.03^12 - 1) = M159,660.33 (s.194). At the older 22% per twelve months it would be M82,500. Confirm the rate RSL currently publishes.

```oa-check
name: Lesotho distributor s.113 adjustment, sales M50m, 1% vs 4% (2026-27)
inputs:
  sales: 50000000
  actual_margin: 0.01
  benchmark_margin: 0.04
  cit_rate: 0.25
  monthly_rate: 0.03
steps:
  - adjustment: (benchmark_margin - actual_margin) * sales
  - extra_tax: adjustment * cit_rate
  - f2: (1 + monthly_rate) * (1 + monthly_rate)
  - f4: f2 * f2
  - f12: f4 * f4 * f4
  - additional_tax_twelve_months: extra_tax * (f12 - 1)
expected:
  adjustment: 1500000.00
  extra_tax: 375000.00
  additional_tax_twelve_months: 159660.33
```

### Example 2, a decision: charge the parent's full management fee or the supportable amount?

Thaba Textiles (Pty) Ltd (Lesotho resident, ordinary 25% income) receives management services from its South African parent. The parent proposes a fee of M2,000,000; the evidence supports M1,200,000. The parent is the beneficial owner and is resident in South Africa, so the treaty caps withholding on technical, managerial or consultancy fees at 7.5% (RSL technical services guideline).

- **Option A, pay M2,000,000, and the M800,000 excess is found not to be arm's length:** under Article 13(6) the 7.5% cap covers only the M1,200,000 arm's length amount (M90,000); the M800,000 excess stays taxable under domestic law, so s.107 withholding at 25% applies to it (M200,000), and the agent that withheld only 7.5% is personally liable for the shortfall (s.165). If the Commissioner General also reallocates the excess deduction under s.113, extra company tax is 25% x 800,000 = M200,000. Lesotho tax cost: M490,000.
- **Option B, pay M1,200,000:** withholding 7.5% x 1,200,000 = M90,000, and nothing to adjust.
- **Difference:** M400,000 more Lesotho tax under Option A, before additional tax and before any s.88 deemed dividend treatment of the excess (which would bring the dividend article, not Article 13, into play).

```oa-check
name: Lesotho management fee to SA parent, M2.0m vs M1.2m (2026-27)
inputs:
  fee_a: 2000000
  fee_b: 1200000
  wht_treaty: 0.075
  wht_domestic: 0.25
  cit_rate: 0.25
steps:
  - excess: max(0, fee_a - fee_b)
  - wht_a: fee_b * wht_treaty + excess * wht_domestic
  - extra_cit_a: excess * cit_rate
  - cost_a: wht_a + extra_cit_a
  - cost_b: fee_b * wht_treaty
  - difference: cost_a - cost_b
expected:
  wht_a: 290000.00
  extra_cit_a: 200000.00
  cost_a: 490000.00
  cost_b: 90000.00
  difference: 400000.00
```

## Ask the client first

1. Who the Lesotho entity deals with, and who follows whose directions or wishes in practice (the s.3 associate test).
2. Every transaction with associates in the year, domestic and cross-border, by type and amount, including branch and head office dealings.
3. How each price was set, and what evidence was kept and where (s.169).
4. Management charges, royalties and interest paid to foreign associates, the withholding deducted, and the treaty claimed.
5. Whether the income is manufacturing (10%) or ordinary (25%) income, and the year end.
6. Any notice of amended assessment received, and when it was served.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 1993, RSL copy updated to 1 April 2012 (read for s.3 definitions of associate, standard rate and year of assessment, s.6, s.10, s.49, s.61, s.88, s.106, s.107, s.113, s.114, s.128, s.130, s.135, s.137, s.141, s.143, s.165, s.169, ss.192 to 199 and the Third Schedule) | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf | 2026-11-02 |
| RSL Corporate Income Tax Guide, file dated May 2017 (read for section 1.4, additional tax at 22% per twelve months, superseded by the newer guide below) | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf | 2026-11-02 |
| RSL Tax Guide on Provisional Tax, file dated November 2023 (read in full; question 8: additional tax at 3% compounded monthly) | https://www.rsl.org.ls/sites/default/files/2024-05/Tax%20Guide%20on%20Provisional%20Tax%20%281%29.pdf | 2026-11-02 |
| RSL internal guide on technical fees under Article 13 of the Lesotho and South Africa DTA (read in full: 7.5% from 27 June 2016, scope of managerial, technical and consultancy services) | https://www.rsl.org.ls/sites/default/files/2024-07/Guideline%20on%20Technical%20Services.pdf | 2026-11-02 |
| Agreement between Lesotho and South Africa on double taxation, RSL copy (read for Articles 5, 9, 10, 11(6), 12(6), 13 and Article 29 on entry into force) | https://www.rsl.org.ls/sites/default/files/2024-07/Agreement%20between%20Lesotho%20and%20Republic%20of%20South%20Africa.pdf | 2026-11-02 |
| RSL Tax Treaties page (read for the list of agreements) | https://www.rsl.org.ls/tax-treaties | 2026-11-02 |
| RSL 2025-2026 Integrated Annual Report (read for the legislative pipeline: Income Tax Amendment Bill for FY2026/27) | https://www.rsl.org.ls/sites/default/files/2026-10/2025%20-%202026%20Integrated%20Annual%20Report.pdf | 2026-11-02 |
| RSL Income Tax page (read for the list of published income tax laws and regulations; no transfer pricing regulations listed) | https://www.rsl.org.ls/income-tax | 2026-11-02 |

Not yet confirmed:
- Amendments to the Income Tax Act made after 1 April 2012 that RSL's consolidated copy does not show, and whether the Income Tax Amendment Bill announced for FY2026/27 has been enacted or changes s.113.
- Whether any transfer pricing regulations, practice note or documentation rule exist outside RSL's published list.
- Revenue Appeals Tribunal decisions on s.113 (for example X v Lesotho Revenue Authority, RAT 01/2017/18, [2022] LSRAT 1, and RAT/05/2019/20, [2022] LSRAT 5): LesLII's search index describes them as applying arm's length and OECD guidance under s.113, but the judgments could not be opened (bot check), so nothing from them is relied on.
- The currently published specified rate under s.192. RSL guides disagree: 3% a month compounded (Provisional Tax guide, November 2023, stated for instalments) against 22% per twelve months (Corporate Income Tax Guide, May 2017). The skill uses the newer figure; no rate notice was found.
- The date the renegotiated Lesotho and South Africa agreement entered into force (the text leaves it to notifications; RSL's guideline gives 27 June 2016 for the 7.5% rate).
- Whether a thin capitalisation or interest limitation rule exists in any later amendment.
