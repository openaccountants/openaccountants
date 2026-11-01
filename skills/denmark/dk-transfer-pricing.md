---
name: dk-transfer-pricing
description: "Danish transfer pricing for income year 2026: companies, permanent establishments and controlling shareholders that deal with related parties. Covers the arm's length rule in Ligningsloven § 2 (more than 50% control, group links, secondary and corresponding adjustments, § 2 B Amount B), reporting of controlled transactions in the corporate return (TastSelv Selskabsskat; form 05.021 only for hydrocarbon companies), the written documentation duty in Skattekontrolloven §§ 37-40 (master file and local file, the DKK 5m / DKK 50m exemption from 2025, the 250 employees / DKK 195m / DKK 391m small-group test, filing 60 days after the return deadline), the DKK 250,000 fine plus 10% of the adjustment, estimated assessments, the six-year assessment window, country-by-country reporting and APAs. Trigger on: transfer pricing Denmark, armslængde, kontrollerede transaktioner, TP-dokumentation, LL § 2, SKL § 39, master file, local file, land for land-rapport, APA. Out of scope: corporate rates, base and interest limits (dk-corporate-tax), individuals (dk-income-tax), VAT (denmark-vat-return)."
version: 0.2
jurisdiction: DK
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark: transfer pricing (armslængdeprincippet) v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific company's facts, transactions or filings. Do not rely on it to file, price a transaction or take a tax position without review by a qualified professional in Denmark.

Tax year: income year 2026 (indkomståret 2026). Currency: Danish kroner (DKK). Authority: Skattestyrelsen. Statutes: Ligningsloven (LL), LBK nr. 1500 of 24 November 2025; Skattekontrolloven (SKL), LBK nr. 12 of 8 January 2024, as amended by lov nr. 750 of 20 June 2025 (documentation relief) and lov nr. 16 of 14 January 2025 (skattetillæg rates); Skatteforvaltningsloven (SFL), LBK nr. 1228 of 13 October 2025; and the documentation order, BEK nr. 883 of 24 June 2025. See Sources.

**What changed from income year 2025.** Lov nr. 750 of 20 June 2025 (§ 3, nr. 2-11, in effect from income year 2025):
- A company whose documentation-relevant controlled transactions are under DKK 5m in the year, and whose controlled receivables and debt are under DKK 50m at year end, no longer prepares written documentation (SKL § 39, stk. 2, nr. 1). Intangibles and some non-EU counterparties are carved out.
- Cash dividends, contributions and similar one-way payments need no documentation (§ 39, stk. 2, nr. 2).
- The small-group test rose to DKK 195m balance sheet or DKK 391m revenue (§ 40, stk. 1).
- If the return deadline is extended under SKL § 14, the documentation deadline moves with it (§ 39, stk. 3).
- The power to order an auditor's statement on the documentation (old SKL §§ 43-45) was repealed.

The same law added LL § 2 B (Amount B, see Cross-border points).

See also: dk-corporate-tax (rates, base, interest limitation, return and payment), dk-income-tax (individuals), dk-capital-gains, denmark-vat-return.

## Who this applies to

**The arm's length rule (LL § 2, stk. 1).** A taxpayer must use arm's length prices and terms for commercial or economic transactions with these parties (controlled transactions), when it:
1. is controlled by a person or a legal entity;
2. controls a legal entity;
3. is in the same group as a legal entity;
4. has a permanent establishment abroad;
5. is a foreign person or company with a permanent establishment in Denmark; or
6. is a foreign person or company with hydrocarbon activity covered by kulbrinteskatteloven § 21, stk. 1 or 4.

**Control (LL § 2, stk. 2).** Control means owning more than 50% of the share capital, directly or indirectly, or holding more than 50% of the votes. These holdings are added together:
- holdings of group companies;
- holdings of personal shareholders and their close relatives (spouse, parents, grandparents, children, grandchildren and their spouses, or their estates; step and adoptive links count);
- holdings of foundations or trusts set up by any of them;
- holdings of other shareholders with whom the taxpayer has an agreement to exercise joint control.

**Group link (LL § 2, stk. 3).** Legal entities are in the same group when the same circle of shareholders controls them or they have common management. Transparent entities governed by company law or a partnership agreement count as legal entities (§ 2, stk. 1, last sentence).

**Individuals are in scope.** A person who controls a company falls under § 2. So does a Danish person with a foreign permanent establishment. Their transactions with the company (salary, rent, loans, asset sales) are controlled transactions. They report on form 04.021 by 1 July after the income year (Juridisk Vejledning C.D.11.12.2).

**Domestic transactions.** LL § 2 applies whether or not the other party is Danish. The written documentation duty is narrower: it applies only where SKL § 39, stk. 1 says so (see The taxable base, step 3).

**Out of scope here.** Corporate rates, the taxable base and the interest limitation rules (SEL §§ 11, 11 B and 11 C) are in dk-corporate-tax. Those rules apply on top of the arm's length test: an interest rate can be at arm's length and the deduction still be limited. Hydrocarbon and tonnage tax specifics are not covered.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Control threshold | More than 50% of share capital or votes, direct or indirect, with the aggregation rules above | 2026 | LL § 2, stk. 2; https://www.retsinformation.dk/eli/lta/2025/1500 |
| Corporate tax on an upward adjustment | 22% (see dk-corporate-tax for financial companies) | 2026 | SEL § 17; https://www.retsinformation.dk/eli/lta/2025/279 |
| Documentation exemption: total controlled transactions (excluding receivables and debt) | Under DKK 5,000,000 in the income year, counting only transactions inside the § 39, stk. 1 duty | From income year 2025 | SKL § 39, stk. 2, nr. 1, as amended by lov nr. 750/2025 § 3, nr. 4; https://www.retsinformation.dk/eli/lta/2025/750 |
| Documentation exemption: controlled receivables and debt | Under DKK 50,000,000 at the end of the income year (both tests must be met) | From income year 2025 | SKL § 39, stk. 2, nr. 1; https://www.retsinformation.dk/eli/lta/2025/750 |
| Carve-outs from the DKK 5m / 50m exemption | Transactions on intangibles (afskrivningsloven § 40); counterparties outside the EU/EEA that do not exchange tax information with Denmark | From income year 2025 | SKL § 39, stk. 2, nr. 1, 2. and 3. pkt.; https://www.retsinformation.dk/eli/lta/2025/750 |
| Small-group test (limited documentation) | Fewer than 250 employees, group-wide, AND either balance sheet under DKK 195,000,000 OR revenue under DKK 391,000,000 | From income year 2025 | SKL § 40, stk. 1, as amended by lov nr. 750/2025 § 3, nr. 7; https://www.retsinformation.dk/eli/lta/2025/750 |
| Documentation deadline | 60 days after the return (oplysningsskema) deadline; moves if the return deadline is extended | 2026 | SKL § 39, stk. 3; https://www.retsinformation.dk/eli/lta/2025/750 |
| Company return deadline | 6 months after the end of the income year (1 September where the year ends in March) | 2026 | SKL § 12; https://www.retsinformation.dk/eli/lta/2024/12 |
| Database search on request | At least 60 days; under the order, between 60 and 90 days | 2026 | SKL § 39, stk. 4; BEK 883/2025 § 7, stk. 4; https://www.retsinformation.dk/eli/lta/2025/883 |
| Documentation languages | Danish, Norwegian, Swedish or English | From income year 2025 | BEK 883/2025 § 2, stk. 3; https://www.retsinformation.dk/eli/lta/2025/883 |
| Fine for late or missing documentation (SKL § 84, nr. 5) | Base DKK 250,000 per income year, cut to DKK 125,000 if documentation of adequate quality is produced later, plus 10% of the income increase | 2026 practice | Juridisk Vejledning A.C.3.5.3.6 and C.D.11.13.1.3.3 (version 3.17, from 31 July 2026); https://info.skat.dk/data.aspx?oid=2090329 |
| Fine for wrong small-group information (SKL § 84, nr. 2) | Larger of a revenue scale (0.5% of revenue up to DKK 500m, +0.1% from DKK 500m to 1bn, +0.05% above) and a headcount scale (DKK 250,000 for 0-50 employees up to DKK 2m for 351+) | 2026 practice | Juridisk Vejledning A.C.3.5.3.8; https://info.skat.dk/data.aspx?oid=2090398 |
| Skattetillæg for late reporting of controlled transactions in the return | DKK 400 per day late, at most DKK 10,000 | From 15 January 2025 | SKL § 73, stk. 1, as amended by lov nr. 16/2025; https://www.retsinformation.dk/eli/lta/2025/16 |
| Assessment window for controlled transactions | Notice by 1 May and assessment by 1 August of the 6th year after the income year (4th year for other items) | 2026 | SFL § 26, stk. 1 and 5; https://www.retsinformation.dk/eli/lta/2025/1228 |
| Country-by-country report | Danish ultimate parent of a multinational group with consolidated revenue of at least DKK 5.6bn in the year before the reported year | 2026 | SKL § 48, stk. 1; https://www.retsinformation.dk/eli/lta/2024/12 |
| Amount B distributor test (LL § 2 B) | Operating expenses at least 3% and at most 20% of net revenue (up to 30% if the distributor's country uses a higher cap) | Income years from 1 January 2025 | LL § 2 B, stk. 2, nr. 2; https://www.retsinformation.dk/eli/lta/2025/1500 |

## The taxable base

1. **Find the controlled transactions.** List every transaction with the parties in LL § 2, stk. 1, nr. 1-6. Include goods, services, royalties, loans and guarantees, asset transfers, salary and dividends to controlling shareholders. Also include head office and permanent establishment dealings. For a permanent establishment, the functional and factual analysis decides which dealings exist (Juridisk Vejledning C.D.11.12.2).
2. **Report them in the return (SKL § 38).** Every taxpayer with controlled transactions reports their type and scope in the oplysningsskema. This applies even when no documentation is needed. Companies answer the controlled-transaction questions in TastSelv Selskabsskat (DIAS). The questions cover: whether the company belongs to the § 37 circle; the number of counterparties in the EU/EEA, in treaty states and in non-treaty states; the § 40 size test; and the SEL § 11 thin capitalisation test. Declared dividends, reported salary, contributions and capital increases must also be reported. Hydrocarbon companies that cannot use DIAS file form 05.021 (English version 05.022) with their hydrocarbon return. The form is an appendix to the return and has the same deadline (skat.dk, form 05.021; Juridisk Vejledning C.D.11.12.2).
3. **Decide whether written documentation is required (SKL § 39, stk. 1).** Documentation is needed only where at least one of these applies:
   - one party is a foreign person or company, or a permanent establishment abroad (§ 39, stk. 1, nr. 1). This does not apply where all parties are Danish permanent establishments of foreign companies or head offices of Danish companies;
   - one party is taxed under tonnageskatteloven or kulbrinteskatteloven, and not all parties are (nr. 2-3);
   - one party is a cooperative (SEL § 1, stk. 1, nr. 3) or a financial company (SEL § 17 A), and not all parties are (nr. 4-5);
   - one party falls under SEL § 1, stk. 1, nr. 6 or SEL § 3 (nr. 6-7);
   - income is computed under the arm's length attribution rules for permanent establishments (KSL § 2, stk. 8, SEL § 2, stk. 7, or SEL § 8, stk. 6) (nr. 8).

   Purely domestic dealings between ordinary Danish companies under the same tax regime are reported but not documented.
4. **Apply the exemptions (SKL § 39, stk. 2, from income year 2025).** No documentation is needed for:
   - all controlled transactions, where the documentation-relevant transactions total under DKK 5m in the year (receivables and debt left out) and controlled receivables and debt total under DKK 50m at year end. Intangible transactions and counterparties outside the EU/EEA that do not exchange information with Denmark stay in;
   - cash dividends, contributions and similar payments;
   - certain transactions in joint-control structures where the taxpayer and its group hold under 5% of the capital and votes;
   - certain transactions with participants taxed under SEL § 13 F or the pension return tax act;
   - other transactions that are insignificant in scope and frequency. These are one-off transactions of modest economic size (BEK 883/2025 § 3, stk. 3).

   If the taxpayer has only exempt transactions, it reports them under § 38 and prepares nothing (§ 39, stk. 1, 2. pkt.; BEK 883/2025 § 3, stk. 4).
5. **Apply the small-group test (SKL § 40).** A taxpayer that, together with its group companies, has fewer than 250 employees and either a balance sheet under DKK 195m or revenue under DKK 391m must prepare and file documentation only for controlled transactions with persons and permanent establishments in states that have no tax treaty with Denmark and are not in the EU/EEA. Group figures are counted under kursgevinstloven § 4, stk. 2. Intra-group debt, receivables and shareholdings are left out of the balance sheet, and intra-group sales are left out of revenue (§ 40, stk. 2).
6. **Prepare the documentation (BEK 883/2025 §§ 2, 4 and 5).** It has two parts:
   - a **master file** (fællesdokumentation) for the group: an organisation chart; a business description, including value drivers, the supply chain for the five largest products and any product over 5% of group revenue, main markets and a short functional analysis; intangibles; intra-group financing; the consolidated accounts; and a list of unilateral APAs and rulings;
   - a **local file** (landespecifik dokumentation) for each Danish taxpayer: management and organisation; business and strategy; main competitors; for each category of controlled transaction, the amounts by jurisdiction, the counterparties, copies of material agreements, a comparability and functional analysis, the chosen method and why, the tested party, the comparables and adjustments, and the conclusion; the annual accounts and a reconciliation of the transfer pricing data to them.

   The depth depends on the size and complexity of the group and its transactions (BEK 883/2025 § 2, stk. 2). A database (benchmark) study is required only when Skattestyrelsen asks for one during an audit (SKL § 39, stk. 4; BEK 883/2025 § 7). Documentation must be prepared for each year. Skattestyrelsen does not accept multi-year documentation or references to earlier years. If the current master file is not ready because the group prepares it to another country's deadline, the previous year's master file may be filed as a preliminary master file, provided it is at most one year old (counted from the filing deadline in that country). The filing must say when the final master file follows and describe any significant changes for the Danish taxpayer not shown in the local file. If that is not possible, ask for an extension (skat.dk, transfer pricing page; Juridisk Vejledning C.D.11.13.1.3.2).
7. **Primary adjustment (LL § 2, stk. 1).** Where the price or terms are not at arm's length, Skattestyrelsen adjusts the taxable income to the arm's length level. Tax is charged at the normal rate (22% for an ordinary company; see dk-corporate-tax).
8. **Secondary adjustments and payment correction (LL § 2, stk. 5).** After a primary adjustment the money has still moved on non-arm's length terms. Skattestyrelsen can tax that benefit as a secondary adjustment: as a dividend, a contribution, a loan or otherwise. No secondary adjustment is made where the transfer is a tax-free group contribution under SEL § 31 D (parent to controlled subsidiary, or between sister companies whose common parent can receive subsidiary dividends tax-free) (Juridisk Vejledning C.D.11.16.1). The taxpayer avoids the secondary adjustment by committing to pay in line with the arm's length price (betalingskorrektion). The conditions (LL § 2, stk. 5; Juridisk Vejledning C.D.11.16.2):
   - the commitment is made immediately after the adjustment; an appeal does not postpone it;
   - it is a real, unconditional legal obligation, not just a book entry; payment itself need not have been made;
   - it runs from the original transaction date, with arm's length interest, and its own terms are at arm's length;
   - LL § 16 E (loans to shareholders) does not cover it;
   - with a foreign counterparty, the foreign tax authority taxes on the arm's length prices (a corresponding adjustment).
9. **Downward adjustments (LL § 2, stk. 6).** Income can be reduced only if the other party's income is increased to match. With a foreign party, the matching income must be included in that country's tax computation.
10. **Estimated assessment (SKL § 46).** If documentation was not prepared and filed on time, Skattestyrelsen may estimate the income from the controlled transactions after the return deadline. It must do so in line with LL § 2, stk. 1. Documentation counts as on time only if it was prepared and filed by the § 39, stk. 3 deadline. Documentation so deficient that it gives no basis for testing the arm's length principle counts as missing (SKM2019.136.HR, SKM2021.251.HR, SKM2023.8.HR, cited in Juridisk Vejledning C.D.11.13.1.3.3). After an estimated assessment, the taxpayer must show that the estimate is clearly unreasonable or rests on a wrong basis (same section).

## Deadlines and filing

| What | Who | Deadline | Channel | Source |
|---|---|---|---|---|
| Controlled-transaction disclosure | Every taxpayer with controlled transactions | With the oplysningsskema: 6 months after year end; calendar year 2026 means 30 June 2027 | TastSelv Selskabsskat (DIAS); form 05.021 or 05.022 only for hydrocarbon companies that cannot use DIAS | SKL §§ 12, 38; https://skat.dk/hjaelp/blanketter/05-skat-selskabsskat-blanketter/kontrollerede-transaktioner-bilag-til-oplysningsskemaet |
| Controlled-transaction disclosure, individuals | Controlling shareholders, owners of a foreign permanent establishment | 1 July after the income year | Form 04.021 (digital) | SKL § 11; Juridisk Vejledning C.D.11.12.2 |
| Master file and local file | Taxpayers covered by § 39, stk. 1 and not exempt | 60 days after the return deadline. Calendar year 2026: 29 August 2027 (a Sunday, see Not yet confirmed) | Transfer pricing module in TastSelv Selskabsskat (DIAS), as readable files (PDF, DOCX, XLSX, CSV, TXT) | SKL § 39, stk. 3; https://skat.dk/en-us/businesses/companies-and-foundations/companies-and-foundations/transfer-pricing |
| Extension | On request where special circumstances justify it; automatically if the return deadline is extended under SKL § 14 | As granted | Request to Skattestyrelsen | SKL § 39, stk. 3, 2. and 3. pkt. |
| Database study | Any documenting taxpayer, on request during an audit | 60 to 90 days, as set in the request | As directed | SKL § 39, stk. 4; BEK 883/2025 § 7 |
| CbC notification | Danish ultimate or surrogate parent, or another Danish group company naming the filer | By the end of the income year reported on | Skattestyrelsen | SKL § 51 |
| CbC report | Danish ultimate parent at DKK 5.6bn or more, or a Danish group company in the § 49 cases | 12 months after the end of the income year reported on | Skattestyrelsen | SKL §§ 48, stk. 2, 49 |

For a company with a non-calendar income year, the deadlines run from the end of its own year (SKL § 12). The weekend rule in SKL § 13 is written for the return deadlines in §§ 10-12.

## Penalties and interest

- **Late or missing documentation (SKL § 84, nr. 5).** It is a criminal fine and requires intent or gross negligence. Fine practice comes from the bill's comments and is set out in Juridisk Vejledning A.C.3.5.3.6. The base is DKK 250,000 per income year. It falls to DKK 125,000 if documentation of adequate quality is produced later. It is increased by 10% of the income increase, and that 10% can be computed only once the assessment is final. Fines for several years can be added together. Court cases cited by Skattestyrelsen: SKM2017.216.BR (DKK 250,000 for deficient documentation), SKM2017.227.ØLR (late documentation; the High Court cut a DKK 500,000 fine to DKK 250,000), SKM2018.564.BR (DKK 625,000) and SKM2019.272.BR (DKK 500,000, documentation so deficient it counted as missing). In Skattestyrelsen's view, a company cannot avoid the fine by self-reporting after the 60-day deadline (A.C.3.5.3.6). A fine can be imposed even if no income adjustment is made (C.D.11.13.1.3.3).
- **Wrong small-group information (SKL § 84, nr. 2).** The fine is the larger of the revenue scale and the headcount scale in the Rates table. The headcount scale is in principle capped at DKK 2m per year (Juridisk Vejledning A.C.3.5.3.8).
- **Skattetillæg for late disclosure (SKL § 73, stk. 1).** Where the return information, including the § 38 disclosure, is late: DKK 400 per day, at most DKK 10,000. Skattestyrelsen can waive it in special cases (§ 73, stk. 4).
- **Daily coercive fines (SKL § 72, stk. 1).** These can be imposed when the § 39 documentation is not filed on time. A complaint does not suspend them unless the appeal body decides otherwise (Juridisk Vejledning C.D.11.13.1.3.3).
- **Estimated assessment (SKL § 46).** See The taxable base, step 10. This is the main civil consequence of missing documentation.
- **Interest and surcharges on the extra tax** follow the general corporate rules in dk-corporate-tax. This skill does not restate them.

## Cross-border points

- **Six-year window.** For taxpayers covered by SKL chapter 4, Skattestyrelsen can give notice of a change to controlled transactions until 1 May of the sixth year after the income year, with the assessment by 1 August of that year. The taxpayer's own request has the same 1 May limit (SFL § 26, stk. 1, 2 and 5). For income year 2026 that is 1 May 2032.
- **Corresponding adjustment after a foreign decision.** An assessment can be reopened outside the normal deadlines where a foreign tax authority has made a decision that affects the Danish taxpayer and Skattestyrelsen accepts it (SFL § 27, stk. 1, nr. 4). It can also be reopened where a mutual agreement case ended without a solution (nr. 9). The request must be made within 6 months of learning of the ground (SFL § 27, stk. 2). A downward adjustment needs the matching upward adjustment in the other country (LL § 2, stk. 6).
- **APAs.** Skattestyrelsen's competent authority concludes bilateral and multilateral APAs. These follow the mutual agreement article (OECD Model art. 25), so the other country must take part. There is no fixed programme. For intra-EU cases the aim is to finish within 18 months of a complete application. Skattestyrelsen says bilateral and multilateral APAs often take 2 to 3 years in practice. Renewals are faster. APAs are not published in Denmark (Juridisk Vejledning C.D.11.15.3.1 and C.D.11.15.3.3). The local file must include copies of APAs and rulings that relate to the documented transactions and to which the Danish competent authority is not a party (BEK 883/2025 § 5, stk. 2, nr. 14).
- **Amount B (LL § 2 B).** A price set under the OECD simplified approach for baseline distribution counts as arm's length when all of these hold:
  - the distributor's country is one of the 23 listed in § 2 B, stk. 3 (for example Brazil, Egypt, Malaysia, Mexico, South Africa, Thailand, Vietnam) and has chosen to allow the approach;
  - the transaction is wholesale distribution of tangible goods, or a sales agent or commissionaire supporting it;
  - the distributor's operating expenses are between 3% and 20% of its net revenue;
  - the conditions in § 2 B, stk. 2 are met.

  It does not apply to a Danish distributor.
- **Country-by-country reporting (SKL §§ 47-52).** A Danish ultimate parent files if group revenue in the year before the reported year was at least DKK 5.6bn. A Danish group company files instead where the parent's country does not require a report, has no competent authority agreement with Denmark for automatic exchange of the reports, or has a systemic failure that Skattestyrelsen has notified (§ 49). This does not apply if a surrogate parent files abroad under § 50. Every Danish group company tells Skattestyrelsen by the end of the income year who files (§ 51).
- **Interest limitation, thin capitalisation, withholding on interest and royalties, and exit tax** are in dk-corporate-tax. A transfer pricing adjustment to interest or royalties paid abroad can change the withholding position. Check it there.

## Worked examples

### Example 1: royalty above arm's length, primary adjustment

A Danish ApS, wholly owned by a Swiss parent, sells the group's products in Denmark. In 2026 its sales are DKK 80,000,000 and it pays the parent a trademark royalty of 6% of sales. The group is above the § 40 small-group test and the royalty concerns an intangible, so the DKK 5m / 50m exemption cannot apply (SKL § 39, stk. 2, nr. 1, 2. pkt.). The ApS files a local file. On audit, Skattestyrelsen finds an arm's length royalty of 4% of sales.

1. Royalty paid: 80,000,000 x 6% = DKK 4,800,000.
2. Arm's length royalty: 80,000,000 x 4% = DKK 3,200,000.
3. Upward adjustment under LL § 2, stk. 1: DKK 1,600,000.
4. Extra corporate tax at 22%: 1,600,000 x 22% = DKK 352,000.
5. The documentation was filed on time, so the SKL § 84, nr. 5 fine does not apply. Late payment interest and surcharges follow dk-corporate-tax.
6. To avoid a secondary adjustment, the ApS can commit, immediately after the adjustment, to recover the DKK 1,600,000 from the parent with arm's length interest from the original payment dates (LL § 2, stk. 5). This works only if Switzerland taxes the parent on the 4% royalty. Relief for double tax in Switzerland is sought under the Denmark-Switzerland treaty mutual agreement article.

```oa-check
name: Danish ApS, royalty 6% vs arm's length 4% on sales DKK 80m, income year 2026
inputs:
  sales: 80000000
  royalty_rate_paid: 0.06
  royalty_rate_arm: 0.04
  cit_rate: 0.22
steps:
  - royalty_paid: sales * royalty_rate_paid
  - royalty_arm: sales * royalty_rate_arm
  - adjustment: royalty_paid - royalty_arm
  - extra_tax: adjustment * cit_rate
expected:
  royalty_paid: 4800000
  royalty_arm: 3200000
  adjustment: 1600000
  extra_tax: 352000
```

### Example 2: documentation filed late, fine and estimated assessment

A Danish A/S with a calendar income year buys services from a related company in the United States. In 2026 it has documentation-relevant controlled transactions of DKK 12,000,000 and controlled debt of DKK 20,000,000. The transactions exceed DKK 5m, so the § 39, stk. 2, nr. 1 exemption fails, even though the debt is under DKK 50m. The group has 400 employees, so the § 40 small-group test fails as well.

The 2026 return is due on 30 June 2027. The documentation is due 60 days later, on 29 August 2027. The A/S files nothing until December 2027. Skattestyrelsen makes an estimated assessment under SKL § 46 and increases income by DKK 2,000,000. The assessment becomes final. The case is treated as grossly negligent. The A/S later files a local file of adequate quality.

1. Extra corporate tax: 2,000,000 x 22% = DKK 440,000.
2. Fine, full base: 250,000 + 2,000,000 x 10% = DKK 450,000.
3. Because adequate documentation was produced later, the base halves: 125,000 + 2,000,000 x 10% = DKK 325,000.
4. Total cost before interest: 440,000 + 325,000 = DKK 765,000.
5. If the case were only simple negligence, there would be no fine. The estimated assessment and the extra tax would still apply (Juridisk Vejledning C.D.11.13.1.3.3).

```oa-check
name: Danish A/S, late 2026 TP documentation, adjustment DKK 2m, fine with halved base
inputs:
  controlled_transactions: 12000000
  exemption_limit_transactions: 5000000
  adjustment: 2000000
  cit_rate: 0.22
  fine_base: 250000
  fine_base_reduced: 125000
  fine_pct_of_increase: 0.10
steps:
  - over_exemption_limit: controlled_transactions - exemption_limit_transactions
  - extra_tax: adjustment * cit_rate
  - fine_full: fine_base + adjustment * fine_pct_of_increase
  - fine_reduced: fine_base_reduced + adjustment * fine_pct_of_increase
  - total_cost: extra_tax + fine_reduced
expected:
  over_exemption_limit: 7000000
  extra_tax: 440000
  fine_full: 450000
  fine_reduced: 325000
  total_cost: 765000
```

## Ask the client first

1. **Who owns the company, and who do they act with?** Include holdings of close relatives, group companies, foundations and shareholder agreements. This decides whether the 50% control test in LL § 2, stk. 2 is met and who the controlled parties are.
2. **Which controlled transactions were there in 2026, with whom, in which countries, and for how much?** Include year-end intra-group receivables and debt. This decides whether documentation is needed under SKL § 39, stk. 1, and the DKK 5m / 50m exemption.
3. **Do any transactions involve intangibles, or a counterparty outside the EU/EEA?** For a non-EU/EEA counterparty, ask whether its country exchanges tax information with Denmark and has a tax treaty. These facts take transactions out of the exemption and decide the § 40 limited duty.
4. **What were the group's headcount, balance sheet and revenue?** Use group figures, with intra-group items removed. This decides the § 40 small-group test.
5. **What is the income year, and has the return deadline been extended?** This sets the 60-day documentation deadline.
6. **Are there any APAs, rulings, foreign audit adjustments or open mutual agreement cases on these flows?** These affect the local file, corresponding adjustments and the six-year window.

## Sources

| Source | URL | Read on |
|---|---|---|
| Ligningsloven, LBK nr. 1500 of 24 November 2025, §§ 2 and 2 B | https://www.retsinformation.dk/eli/lta/2025/1500 | 2026-10-23 |
| Skattekontrolloven, LBK nr. 12 of 8 January 2024, §§ 11-14, 37-52, 72-73, 84 | https://www.retsinformation.dk/eli/lta/2024/12 | 2026-10-23 |
| Lov nr. 750 of 20 June 2025 (§ 3: SKL §§ 39, 40, 43-46, 84 amendments; § 5: LL § 2 B; § 7: effective dates) | https://www.retsinformation.dk/eli/lta/2025/750 | 2026-10-23 |
| Lov nr. 16 of 14 January 2025 (§ 2: SKL § 73 skattetillæg DKK 400 per day, at most DKK 10,000) | https://www.retsinformation.dk/eli/lta/2025/16 | 2026-10-23 |
| Skatteforvaltningsloven, LBK nr. 1228 of 13 October 2025, §§ 26-27 | https://www.retsinformation.dk/eli/lta/2025/1228 | 2026-10-23 |
| BEK nr. 883 of 24 June 2025 on transfer pricing documentation | https://www.retsinformation.dk/eli/lta/2025/883 | 2026-10-23 |
| Selskabsskatteloven, LBK nr. 279 of 13 March 2025, § 17 | https://www.retsinformation.dk/eli/lta/2025/279 | 2026-10-22 (dk-corporate-tax) |
| Juridisk Vejledning C.D.11.13.1.3.2, Frist for at udarbejde og indgive transfer pricing-dokumentation (version 3.17) | https://info.skat.dk/data.aspx?oid=2232523 | 2026-10-23 |
| Juridisk Vejledning C.D.11.16.1, Sekundære justeringer, and C.D.11.16.2, Betalingskorrektion (version 3.17) | https://info.skat.dk/data.aspx?oid=2338674 and https://info.skat.dk/data.aspx?oid=2338676 | 2026-10-23 |
| Skattestyrelsen, Transfer pricing and documentation requirements | https://skat.dk/en-us/businesses/companies-and-foundations/companies-and-foundations/transfer-pricing | 2026-10-23 |
| Skattestyrelsen, form 05.021 Kontrollerede transaktioner, bilag til oplysningsskemaet | https://skat.dk/hjaelp/blanketter/05-skat-selskabsskat-blanketter/kontrollerede-transaktioner-bilag-til-oplysningsskemaet | 2026-10-23 |
| Juridisk Vejledning C.D.11.12.2, Hvilke transaktioner er oplysningspligtige (version 3.17) | https://info.skat.dk/data.aspx?oid=2232553 | 2026-10-23 |
| Juridisk Vejledning C.D.11.13.1.3.3, Sanktioner ved manglende eller mangelfuld TP-dokumentation (version 3.17) | https://info.skat.dk/data.aspx?oid=2232789 | 2026-10-23 |
| Juridisk Vejledning A.C.3.5.3.6, Bødeniveau, SKL § 84, nr. 5 (version 3.17) | https://info.skat.dk/data.aspx?oid=2090329 | 2026-10-23 |
| Juridisk Vejledning A.C.3.5.3.8, Bødeniveau, SKL § 84, nr. 2 (version 3.17) | https://info.skat.dk/data.aspx?oid=2090398 | 2026-10-23 |
| Juridisk Vejledning C.D.11.15.3.1, Hvad er en APA (version 3.17) | https://info.skat.dk/data.aspx?oid=2060566 | 2026-10-23 |
| Juridisk Vejledning C.D.11.15.3.3, Den typiske APA-proces (version 3.17) | https://info.skat.dk/data.aspx?oid=2060568 | 2026-10-23 |

Not yet confirmed: (1) whether the documentation deadline moves when the 60th day falls on a weekend. SKL § 39, stk. 3 counts the 60 days from the return deadline "jf. §§ 11-13", but the § 13 weekend rule itself covers only the return deadlines, and Juridisk Vejledning C.D.11.13.1.3.2 gives 29 August for calendar years without a weekend rule. For calendar year 2026, 29 August 2027 is a Sunday, so file by Friday 27 August 2027. (2) The rules for the EU Dispute Resolution Directive and the EU Arbitration Convention in Danish law, and any time limits in specific Danish treaties, were not read for this skill. (3) Whether Skattestyrelsen offers unilateral APAs, beyond binding rulings (bindende svar), was not confirmed. (4) Which characterisation applies to a given secondary adjustment (for example whether an overpayment by a Danish subsidiary to its foreign parent is a dividend with Danish withholding tax) was not researched.

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
