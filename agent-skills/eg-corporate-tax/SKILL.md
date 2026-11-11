---
name: eg-corporate-tax
description: "Use this skill whenever asked about Egyptian corporate income tax for tax year 2026 on resident companies, partnerships, branches and permanent establishments of foreign companies, to compute, review, or explain the tax on legal persons' profits, deductions, thin capitalisation, losses, depreciation, dividends, capital gains, advance payments and the annual return. Trigger on phrases like \"Egypt corporate tax\", \"Egypt CIT\", \"Egyptian company tax\", \"22.5% Egypt\", \"thin cap Egypt\", \"ضريبة أرباح الأشخاص الاعتبارية\", \"ضريبة دخل الشركات\", \"إقرار الشركات\", \"permanent establishment Egypt\", or any request to prepare or check an Egyptian company tax return. ALWAYS read this skill before touching any Egypt corporate tax work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eg-corporate-tax"
  jurisdiction: "EG"
  tax_year: "2026"
  last_updated: "2026-11-02"
---

# EG Corporate Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers the Egyptian tax on the profits of legal persons (الضريبة على أرباح الأشخاص الاعتبارية, Law 91 of 2005, Book Three) for tax year 2026. Reply in the user's language, English or Arabic. All amounts are in EGP. Tax year: the financial year of the company; returns run on the calendar year unless the company's financial year ends on another date. Law 151 of 2026 (Gazette 30 bis (a), 28 July 2026) took effect on 29 July 2026 and changed thin capitalisation, the participation exemption, listed share gains and dividend tax; where it matters the row says which period applies.

## Who this applies to

- **Taxed on worldwide profit** (Law 91 art. 47): legal persons resident in Egypt, on all profits made in Egypt or abroad, except the National Service Projects Organisation of the Ministry of Defence.
- **Taxed on Egyptian PE profit** (art. 47): non-resident legal persons, on profits made through a permanent establishment in Egypt. Art. 4 (as replaced by Law 30/2023) defines a PE (place of management, branch, office, factory, workshop, mine or well, building or installation site over 90 days in any 12 months, services through staff over 90 days, dependent agent); art. 4 bis lists what is not a PE (preparatory or auxiliary activity).
- **Legal persons** (art. 48): capital companies and partnerships whatever law governs them, and de facto partnerships; cooperatives and their unions; public bodies on taxable activity; banks, companies and foreign establishments with a branch in Egypt; local administration units on taxable activity. Civil companies are treated as partnerships for dividends (art. 56 bis).
- **Exempt bodies** (art. 50 as replaced by Law 30/2023): ministries and government agencies; NGOs within their purpose; non-profit social, scientific, sports or cultural bodies on non-commercial activity; private insurance funds under Law 54/1975; international organisations exempt by treaty; land reclamation companies and poultry, bee, livestock and fish farming companies for ten years from start. Several investment funds are exempt on conditions (art. 50 items 14 to 18).
- **Not here:** turnover up to EGP 20 million that opted into Law 6/2025 (`eg-sme-tax`); individuals and sole traders (`eg-income-tax`); withholding on payments the company makes (`eg-withholding-tax`); payroll (`eg-payroll`); VAT (`egypt-vat`); transfer pricing files (`eg-transfer-pricing`); residence, PE and treaty questions for foreign groups (`eg-cross-border`).

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Standard rate | 22.5% of net annual profit | Law 91 art. 49 first para., as replaced by Law 96/2015. Base rounded down to the nearest EGP 10 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.96-2015.pdf |
| Suez Canal Authority, Egyptian General Petroleum Corporation, Central Bank of Egypt | 40% | Art. 49 second para. (2005 text, not replaced by Law 96/2015) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Oil and gas exploration and production companies | 40.55% | Art. 49 second para. | 2026 | same |
| Thin capitalisation, statutory ratio | Interest on loans above 2 times average equity is not deductible | Art. 52 item 1 as replaced by Law 30/2023 (from 16 Jun 2023) and re-enacted by Law 151/2026 (from 29 Jul 2026). Not for banks, insurers, or finance companies named by ministerial decision | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Thin capitalisation, 2026 transitional ratio | Interest deductible on loans up to 3 times average equity | Law 30/2023 art. 5: 4:1 for 2023, 3:1 for tax years 2024 to 2027, 2:1 for 2028. Law 151/2026 did not repeal it | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| Thin capitalisation, national infrastructure projects | 4 times average equity | Projects named by Prime Minister decision; loans from unrelated lenders; the company's share at least 25% of its investments; ends when the term of the loans for carrying out the project's main works ends (art. 52 item 1 second para., Law 151/2026, as corrected by the Gazette erratum of 8 Aug 2026) | From 29 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Dividends received, participation exemption | Exempt | Parent or holding company holds at least 25% of capital or votes for two years, or undertakes to hold for two years; resident and non-resident subsidiaries (art. 50 item 10 as replaced by Law 151/2026). The Law 30/2023 text added 10% of the dividend to the base; the 2026 text does not | From 29 Jul 2026 | same |
| Dividends from another resident company | Excluded from the company's taxable base, with the related cost | Art. 56 bis as replaced by Law 151/2026 | 2026 | same |
| Gains on securities listed on the Egyptian Exchange | Exempt; losses not deductible | Art. 50 item 7 as replaced by Law 151/2026. Not exempt where the disposal causes the company's shares to be delisted. Art. 46 bis 5 (10% on listed gains) repealed by Law 151 art. 6 | From 29 Jul 2026 | same |
| Gains on unlisted securities and company interests | Taxed, made in Egypt or abroad; gain = price less acquisition cost and brokerage | Art. 46 bis 3 and 4 as replaced by Law 151/2026. Non-resident seller computes and pays within 60 days. At a fair value price, add the Central Bank rate for each year held if held at least three years; weighted average cost | From 29 Jul 2026 | same |
| Dividend tax on distributions | 10%; 5% if the securities are listed in Egypt | Art. 56 bis; no costs deducted; not on bonus shares. Detail and remittance in `eg-withholding-tax` | 2026 | same |
| PE profits | Deemed distributed 60 days after the PE's year end, so 10% dividend tax applies | Art. 56 bis | 2026 | same |
| Listing incentive | 15% off the tax due on the return for three years from the offering | Law 151/2026 art. 3: shares offered on the Egyptian Exchange under an FRA-approved prospectus; fair market value at the offering at least EGP 50 billion; at least 20% of shares offered or an offer of at least EGP 10 billion; once in the company's life; not combined with incentives under any other law; the Minister of Finance may extend it for a like period | From 29 Jul 2026 | same |
| Depreciation, buildings, installations, equipment, ships, aircraft | 5% of cost a year | Art. 25 item 1 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Depreciation, purchased intangibles including goodwill | 10% of cost a year | Art. 25 item 2 | 2026 | same |
| Depreciation pools, declining balance | Computers, systems, software, storage 50%; all other business assets 25% | Art. 25 item 3; pool basis per art. 26; a pool basis of EGP 10,000 or less is deducted in full | 2026 | same |
| Initial allowance | 30% of the cost of new or used production machinery, in the first period of use | Art. 27; regular books needed; depreciation then runs on cost less 30% | 2026 | same |
| Loss carry-forward | To the fifth following year, no carry-back | Art. 29, applied to companies by art. 51. Exception: a loss on completing a long-term contract is set against that contract's profits taxed in earlier periods and the tax refunded; any excess carries forward under art. 29 (art. 21, 2005 text) | 2026 | same |
| Donations | Deductible in full to the government, local units and public legal persons; up to 10% of annual net profit to registered Egyptian NGOs and foundations, science institutions and hospitals under government supervision, and Egyptian scientific research bodies | Art. 23 items 7 and 8 (2005 text) | 2026 | same |
| Other taxes and fees | Deductible, except the income tax itself | Art. 23 item 3 and art. 24 item 3 (2005 text) | 2026 | same |
| Comprehensive health insurance solidarity contribution | Deductible | Art. 23 item 10 added by Law 151/2026 art. 2 (contribution under Law 2/2018 art. 40 item 9) | From 29 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Head office charges of a PE | Capped at 7% of the PE's net taxable profit | Executive Regulations art. 74; no royalties, interest or commissions inside the cap; head office auditor's certificate | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.991-2005.pdf |
| Advance payment option | 60% of the last declared tax (or estimate), in three equal instalments | Arts. 61 to 63; replaces withholding under art. 59 (art. 60, which also requires regular records). Annual yield at the Central Bank rate (art. 63 fourth para. as replaced by Law 206/2020 issuing law art. 3; rate in ETA circular 1/2026), worked on the first and second instalments from payment to the period end (ETA Services Guide 8/1) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Delay charge | Central Bank rate on 1 January before the due date plus 2%: 20.50% + 2% = 22.50% a year for 2026 | Law 91 art. 110; part months and pounds dropped | 2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf |
| Delay charge ceiling | Delay charge or additional tax may not exceed 100% of the principal | Law 206/2020 art. 45 bis, added by Law 7/2025 | 2026 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |

## The base

1. **Start from net profit** under the commercial and industrial rules of Book Two, Part Three (art. 51), unless Book Three says otherwise. Costs must be real, needed for the activity and, from the e-invoice and e-receipt dates, backed by e-invoices or e-receipts (art. 22 item 2 as replaced by Law 30/2023).
2. **Add back non-deductible items** (art. 52): interest above the thin cap ratio; provisions of any kind, except 80% of loan provisions banks must form under Central Bank rules and insurers' technical provisions; dividends and profit shares and attendance fees paid to shareholders; board members' remuneration; employees' profit share; and the art. 24 items (2005 text): reserves and provisions of any kind; fines, financial penalties and damages imposed for a felony or intentional misdemeanour by the taxpayer or a subordinate; the income tax itself; interest on loans above twice the Central Bank rate at the start of the calendar year in which the period ends; interest paid to natural persons who are not taxable or are exempt. Donations over the art. 23 item 8 cap (10% of annual net profit) are added back.
3. **Thin capitalisation** (art. 52 item 1 and Executive Regulations arts. 58 and 59). Interest covers anything paid for loans, advances, bonds and any debt finance at fixed or variable return. Equity = paid-up capital plus reserves and carried profits less carried losses, excluding untaxed revaluation reserves; losses come off reserves and retained profit only, never below paid-up capital. Average equity = (opening + closing) / 2; average loans the same, leaving out interest-free loans, loans whose interest is not taxable, and loans with a grace period for paying interest (until that period ends). Ratio for 2026: 3:1 (Law 30/2023 art. 5).
4. **Bad debts** (art. 28 as replaced by Law 151/2026 for item 4): written off the books, with a report from an accountant on the register of accountants and auditors; regular books; debt linked to the activity; previously taken into income; serious collection steps and no recovery 12 months after due date (payment order, first-instance judgment, or claim in bankruptcy or composition). A debt up to EGP 10,000 needs no steps if total bad debts stay within 1% of debtor balances at year end. Recoveries are income in the year collected.
5. **Tax depreciation** replaces accounting depreciation: rates in the table, pool basis rules in art. 26. Land, works of art, antiques and jewellery are not depreciated.
6. **Exclude** exempt income: dividends under the participation exemption or from resident companies, listed share gains (from 29 Jul 2026), listed non-government bond interest (art. 50 item 7). An exemption may not create a loss to carry forward (art. 50 last para.).
7. **Deduct losses** brought forward within five years (art. 29). Losses lapse (art. 55, Executive Regulations art. 68) only if all three hold: ownership of capital or votes changes by more than 50%, the activity changes, and the shares are not listed (the listing test is for joint-stock companies and partnerships limited by shares); adding a related or complementary activity is not a change. If not all three hold, the losses carry forward provided the three do not all come together within the next three years (Executive Regulations art. 68). A change of form or ownership made to avoid tax is disregarded (art. 69).
8. **Change of legal form** (art. 53): merger, division, conversion, or a share or asset swap of 50% or more is tax-neutral if assets and liabilities keep their book values; otherwise revaluation gains are taxed (Executive Regulations art. 64).
9. **Foreign tax credit** (art. 54): foreign tax on foreign profit is credited, with documents, up to the Egyptian tax on that profit; foreign losses never reduce the Egyptian base; each country is computed separately (Executive Regulations art. 67).
10. **Round down** to EGP 10 and apply the rate. Credit tax withheld under art. 59, advance payments and their yield (Law 206/2020 art. 32).
11. **Related parties** (art. 30): ETA may reset prices to arm's length; detail in `eg-transfer-pricing`.
12. **Long-term contracts** (art. 21, 2005 text): profit on each contract running over more than one period is taxed by percentage of completion, measured by actual cost to the period end against total estimated cost, and settled on actual figures in the period the contract ends.

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Annual return | Before 1 May each year, or within four months after the end of the financial year | Law 206/2020 art. 31(c) |
| Accountant signature | The annual return of capital companies, cooperatives, individuals and partnerships whose turnover exceeds EGP 2 million a year must be signed by an accountant on the register of accountants and auditors | Law 206/2020 art. 31(d) last para. |
| Completeness | A return without all the form's tables is not a return; a return is due for exempt periods too | Law 206/2020 art. 31(c) |
| Filing channel and payment | Electronic filing with password and e-signature; tax shown is paid the same day, net of tax withheld, advance payments and their yield | Law 206/2020 art. 32 |
| Amended return | Within the year after the deadline; within 30 days of the deadline it counts as the original. The right is lost once evasion is discovered or an audit notice is served. Public sector banks and companies: final return within 30 days of the general assembly approving the accounts | Law 206/2020 art. 33 |
| Cessation | Return within 60 days of stopping; on a transfer of the business, a separate return within 60 days | Law 206/2020 art. 31(d) |
| Advance payments | Apply at least 60 days before the period on the form; ETA answers in 60 days (silence is refusal). Instalments by 30 June, 30 September and 31 December for a calendar year (the ETA guide: 6, 9 and 12 months from the period start). Renewal can be filed up to the end of the prior period | Law 91 arts. 62, 63; ETA Services Guide 8/1 |

**Steps:**
1. Log in to the ETA tax system (https://workspace.eta.gov.eg/workspace/dashboard for merged offices).
2. Prepare the return from audited accounts with all tables completed, signed by the registered accountant.
3. Submit before 1 May (or four months after a non-December year end), keep the confirmation, and pay the balance the same day through the e-payment channel.
4. If a mistake is found, file an amended return within the year after the deadline.

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Return and payment late by up to 60 days, or a wrong return showing more tax | Fine EGP 3,000 to 50,000 plus the tax; trebled on repeat | Law 206/2020 art. 69 |
| No return for over 60 days past the deadline | Fine EGP 5,000 to 200,000; doubled on repeat within three years | Law 206/2020 art. 70 |
| Breach of record-keeping articles | Fine EGP 20,000 to 100,000; up to EGP 50,000 for not keeping books for the required period | Law 206/2020 art. 71 |
| Evasion | Prison one to three years and fine EGP 50,000 to 250,000, or either; the partner, manager or board member in charge is liable if the breach was within their knowledge | Law 206/2020 arts. 72, 73 |
| Late payment | Delay charge 22.50% a year for 2026, capped at 100% of the principal | Law 91 art. 110; ETA circular 1/2026; Law 206/2020 art. 45 bis |
| Settlement | Before prosecution 100% of the tax due; after, 150% before judgment and 175% after final judgment; crimes with no tax at stake, half to twice the minimum fine | Law 206/2020 art. 75; art. 75 bis (Law 7/2025) |

## Cross-border points

- Non-resident companies pay only on PE profit (art. 47); the PE definition is art. 4 and 4 bis. PE profit is deemed distributed 60 days after year end, so 10% dividend tax applies on top of 22.5%.
- Payments abroad for interest, royalties, services and dividends carry withholding: `eg-withholding-tax`.
- Foreign tax credit: art. 54, per country, capped at the Egyptian tax.
- Residence, PE and treaty relief for foreign groups: `eg-cross-border`.

## Two worked examples that recompute

**Case 1. Trading company, calendar 2026.** Accounting profit 10,000,000. Add back a general provision of 500,000 and accounting depreciation of 800,000. Tax depreciation: 25% on an other-assets pool of 2,400,000 = 600,000. Taxable 10,700,000; tax 22.5% = 2,407,500. Less 150,000 withheld by customers under art. 59: payable 2,257,500 before 1 May 2027.

```oa-check
name: Company profit with provision and depreciation adjustments
inputs:
  profit: 10000000
  provision: 500000
  book_dep: 800000
  pool: 2400000
  withheld: 150000
steps:
  - tax_dep: pool * 0.25
  - taxable: floor((profit + provision + book_dep - tax_dep) / 10) * 10
  - tax: taxable * 0.225
  - payable: tax - withheld
expected:
  tax_dep: 600000.00
  taxable: 10700000.00
  tax: 2407500.00
  payable: 2257500.00
```

**Case 2. Decision: fund growth by shareholder loan or by equity.** Average equity 20,000,000; average loans 80,000,000 at 15%, interest 12,000,000. For 2026 the limit is 3 times equity, 60,000,000. Interest on the excess 20,000,000 (3,000,000) is not deductible, costing 675,000 of tax. If the shareholder had put the extra 20,000,000 in as equity, equity would be 40,000,000, the limit 120,000,000, and every pound of the remaining 60,000,000 loan interest deductible. In 2028 the ratio falls to 2:1 and the same loan structure would lose 6,000,000 of interest.

```oa-check
name: Thin capitalisation 2026 at 3 to 1
inputs:
  equity: 20000000
  loans: 80000000
  rate: 0.15
steps:
  - limit: equity * 3
  - disallowed: max(loans - limit, 0) * rate
  - extra_tax: disallowed * 0.225
  - disallowed_2028: max(loans - equity * 2, 0) * rate
expected:
  limit: 60000000.00
  disallowed: 3000000.00
  extra_tax: 675000.00
  disallowed_2028: 6000000.00
```

This assumes one interest rate across all loans; with mixed rates ask how ETA allocates the excess (see "Not yet confirmed").

## Ask the client first

1. Legal form, residence, and whether this is a branch or PE of a foreign company?
2. Financial year end, and turnover: up to EGP 20 million and in the Law 6/2025 regime? If yes, use `eg-sme-tax`.
3. Average equity and average loans for the year, and which lenders are related?
4. Holdings in other companies: percentage, how long held, listed or not, and any disposals in 2026 (before or after 29 July)?
5. Losses brought forward by year, and any ownership change over 50% with a change of activity?
6. Tax withheld by customers, advance payments made, and any foreign tax paid?

Do not help hide profit, invent costs or shift profit to related parties off arm's length. Do not present output as a filed return or a professional sign-off.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 91 of 2005, original Gazette text: arts. 21 to 31, 47 to 63 (page images read; 2005 text, used only where no later law replaced it) | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-02 |
| Executive Regulations, MoF decree 991 of 2005: arts. 57 to 60, 64 to 69, 74 to 84 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.991-2005.pdf | 2026-11-02 |
| Law 96 of 2015, art. 1 (art. 49 first para., 22.5%; art. 56 bis 2015 text; page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.96-2015.pdf | 2026-11-02 |
| Law 53 of 2014, art. 1 (art. 50 items 7 and 10, art. 59 first para., arts. 72, 73, 86, 135; page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf | 2026-11-02 |
| Law 30 of 2023, whole text (arts. 4, 4 bis, 22, 46 bis to 46 bis 7, 50, 52, 56, 56 bis, 58, 72 bis; transitional arts. 3 to 10; text layer read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | 2026-11-02 |
| Law 151 of 2026, whole text; Gazette 30 bis (a), 28 Jul 2026 (text layer read) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-02 |
| Unified Tax Procedures Law 206 of 2020: arts. 29 to 34, 50 to 56, 63 to 75 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-02 |
| Law 7 of 2025, whole text (arts. 45 bis, 75 bis, 75 bis 1 of Law 206) | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-02 |
| Law 5 of 2025, arts. 1 to 4 (settlement of past periods; read to check the old skill's citations) | https://eta.gov.eg/sites/default/files/2025-02/law_no.5.of_.2025.pdf | 2026-11-02 |
| ETA circular 1 of 2026 (Central Bank rates 2021 to 2026; page image read) | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | 2026-11-02 |
| ETA Services Guide, 2nd edition: service 8/1 advance payments (text layer read) | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-02 |
| Gazette erratum to Laws 149, 150 and 151 of 2026, Gazette 32 bis, 8 Aug 2026 (read for the correction to arts. 52 and 56 on infrastructure loans; via the independent review) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-02 |

Not yet confirmed: whether the Law 151/2026 changes (participation exemption without the 10% add-back, listed gains exemption, repeal of art. 46 bis 5) apply to the whole of tax year 2026 or only from 29 July 2026; Law 151 art. 7 gives only the start date. Whether Law 30/2023 art. 5 (3:1 for 2024 to 2027) is read by ETA as still running after Law 151 replaced art. 52 item 1. How the disallowed interest is allocated where loans carry different rates. Whether arts. 21, 23 (other than item 10), 24 and 25 to 27 were amended after 2005 by a law not read here (only the 2005 text was read, and no amendment was found in Laws 53/2014, 96/2015, 30/2023 or 151/2026). The old skill's 5% donations cap is wrong (art. 23 item 8 says 10%); its blanket fines add-back is narrower in the law (art. 24 item 2: felonies and intentional misdemeanours); its entertainment add-back, start-up costs over five years, R&D 150% and training 100% deductions had no official source and were not found. Whether the 40% and 40.55% rates in art. 49 second para. still stand unchanged (no later replacement was found in the laws read). Whether art. 46 bis 4's three-year fair value uplift applies to companies' gains, since it sits in the individuals' book. The meaning of the art. 56 bis exclusion of resident-company dividends from dividend tax (see `eg-withholding-tax`). Transfer pricing documentation thresholds (old skill: EGP 8 million, CbCR EGP 3 billion) belong to `eg-transfer-pricing`. Free zone and special economic zone regimes (Law 83/2002, Investment Law 72/2017), a non-calendar financial year approval, and the box numbers of the corporate return were not read.

> Originally contributed by Ahmed Hassan; rebuilt against the law by the OpenAccountants team.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-02. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eg-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eg-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
