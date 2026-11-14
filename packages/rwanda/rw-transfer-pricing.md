---
name: rw-transfer-pricing
description: "Rwanda transfer pricing for the 2026 tax period under Article 32 of Law 027/2022 establishing taxes on income (as amended by Laws 051/2023 and 014/2025) and Ministerial Order 003/26/10/TC of 29/04/2026 on transfer pricing. Covers related persons (no percentage threshold in the Law), controlled transactions including deemed controlled dealings with beneficial tax regimes (15% test), the arm's length principle, the five methods and the tested party, the interquartile range with adjustment to the median, services and intangibles, the transfer pricing policy, local file and master file, the controlled transactions schedule, country-by-country report within 12 months, the FRW 600 million documentation waiver, advance pricing agreements (FRW 100 million, FRW 600 million, FRW 6 million fee, 3 years), corresponding adjustments, the 5% fine on controlled transaction information and the secondary dividend rule. Trigger on: Rwanda transfer pricing, RRA TP audit, related party Rwanda, local file master file Rwanda, APA Rwanda, arm's length Rwanda. Out of scope: treaty rates, mining."
version: 0.2
jurisdiction: RW
category: transfer-pricing
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - rw-corporate-income-tax
tier: 2
domain: transfer-pricing
type: situation-rules
---

# Rwanda transfer pricing: related persons, arm's length, documentation and APAs (2026) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The duty sits in Article 32 of Law 027/2022 of 20/10/2022 establishing taxes on income (the Income Tax Law, "ITL"): related persons in controlled transactions must hold documents showing their prices and profits follow the arm's length principle, and the Rwanda Revenue Authority (RRA) adjusts them if they do not. The detailed rules are in Chapter II (Articles 2 to 31) of Ministerial Order 003/26/10/TC of 29/04/2026, in force on its publication in the Official Gazette Special of 29/04/2026 (Order art 37). The Order has no repeal clause; the 2020 transfer pricing Order was made under the repealed 2018 Law, and orders under that Law stayed in force for no more than 12 months after Law 027/2022 was published (ITL art 70). The tax period is the calendar year (ITL art 8), so this skill covers the year to 31 December 2026. Corporate rates, the 2% fee cap and the 4x interest rule are owned by [rw-corporate-income-tax](rw-corporate-income-tax.md); withholding on payments abroad by [rw-cross-border](rw-cross-border.md).

## Who this applies to

- **Related persons (ITL art 3(1)).** Any person who acts, or is likely to act, in line with the directives, opinion or wishes of another person, whether or not these are communicated. In particular:
  - an individual, the spouse, direct ascendants and descendants, and collateral relatives to at least the 3rd degree;
  - a person who participates directly or indirectly in the management, control or capital of another person;
  - a third person who participates directly or indirectly in the management, control or capital of another person;
  - the persons above who participate in the management, control or capital of an enterprise;
  - a person under direct or indirect common control with another person.
  The Law sets no percentage. The RRA Tax Handbook gives 50% of voting rights as an example; the Law's test is wider, so follow the Law.
- **Controlled transaction (ITL art 3(7); Order art 3).** A transaction between related persons, or a deemed controlled transaction with an independent person resident in a place the RRA considers a beneficial tax regime. The Order applies when:
  - one party is in Rwanda and taxable here and the related party is in Rwanda or abroad (domestic dealings are covered too);
  - a non-resident deals with a related non-resident and the transaction relates to a permanent establishment of either;
  - a Rwandan resident deals with a person in a beneficial tax regime, related or not;
  - a person in a beneficial tax regime deals with a Rwandan permanent establishment of a non-resident, related or not.
- **Beneficial tax regime (Order art 2(a)).** A country or tax jurisdiction with any one of: no income tax or a maximum rate of 15%; tax breaks for non-residents; no substantial economic activity requirement; no tax on foreign income or a maximum of 15% on it; no access to information on corporate structure, ownership of assets or transactions.
- **Transactions covered (Order art 5).** Goods; tangible assets (sale, free transfer, lease); intangibles (including licences); services; financing (loans, guarantees, securities, advances, deferred payments, receivables); cost contribution arrangements; business restructurings; any other transaction that may affect profit or loss.

Not covered here: treaty mutual agreement procedure detail, treaty rates, mining and minerals tax.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Corporate income tax on an upward adjustment | 28% of taxable business profit, rounded down to FRW 1,000 (ITL art 48 as amended by Law 051/2023 art 2) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf |
| Related person test | No percentage; acting on another's directives, participation in management, control or capital, or common control (ITL art 3(1)) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |
| Secondary rule on an adjustment | The balance left after taxing the income from an RRA transfer pricing correction is dividend income (ITL art 40); dividends paid by a resident to a payee not registered with the RRA, or registered without a recent income tax declaration, bear 15% withholding (ITL art 60, item 1) | 2026 | same |
| Beneficial tax regime marker | Income tax, or tax on foreign income, of at most 15%, or other markers in Order art 2(a) | 2026 | https://www.rra.gov.rw/fileadmin/Folder_for_2025/Ministerial_Order_on_Simplified_Accounting_Method_April_2026.pdf |
| Arm's length range | Interquartile range where a statistical approach is used; no adjustment inside it; outside it, profit is reset to the median (Order art 16) | 2026 | same |
| Documentation waiver | Annual turnover below FRW 600,000,000 and controlled transactions below FRW 10,000,000 or an aggregate below FRW 100,000,000; the arm's length duty still applies (Order art 19) | 2026 | same |
| Documentation on request | Within 7 days of the written request (Order art 18(2)) | 2026 | same |
| Country-by-country report | Part of the documentation where the ultimate parent must prepare one; filed not later than 12 months after the last day of the group's reporting fiscal year (Order art 17(3)(a), (g)) | 2026 | same |
| APA eligibility | Controlled transactions of at least FRW 100,000,000 and annual turnover of at least FRW 600,000,000 (turnover test waived in the year of CIT registration) (Order art 28(1), (3)) | 2026 | same |
| APA processing fee | FRW 6,000,000, non-refundable (Order art 28(1)(d)) | 2026 | same |
| APA term | 3 years, renewable once; rollback to at most 2 prior years on request (Order arts 26(3), 30(1)) | 2026 | same |
| Fine for missing, incomplete, incorrect or misleading information on controlled transactions | 5% of the value of the controlled transaction (Law 020/2023 art 86) | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf |
| Failure to keep books and records of controlled transactions | The art 81 administrative fine is doubled (Law 020/2023 art 81) | 2026 | same |
| Late or missing information after an RRA request | FRW 500,000 (turnover up to FRW 20m); FRW 2,000,000 (over FRW 20m, under FRW 200m); FRW 3,000,000 (FRW 200m to under FRW 600m); FRW 5,000,000 (FRW 600m or more); doubled for a 2nd fault in 2 years, 4 times for a 3rd (Law 020/2023 art 81) | 2026 | same |
| Audit window | 5 years from 1 January after the tax period; 10 years where information was concealed to evade tax (Law 020/2023 art 35) | 2026 | same |
| Related-party fee and interest limits | 2% of turnover cap on management, technical and royalty fees to a non-resident related person; 4x paid-up equity on related-party interest and realised exchange loss (ITL art 25); figures owned by rw-corporate-income-tax | 2026 | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf |

## The base

**The duty and the adjustment (ITL art 32; Order art 8).**
- A person in a controlled transaction sets the price or margin so that it complies with the arm's length principle (Order art 8(1)).
- The arm's length principle means the conditions of the controlled transaction do not differ from those in comparable uncontrolled transactions in comparable circumstances (ITL art 3(8)).
- If the documents are not provided, or do not justify the price and profit, the RRA adjusts prices or profits under the general rules (ITL art 32).
- The RRA performs a dedicated transfer pricing audit on controlled transactions (Law 020/2023 art 46).
- The general anti-abuse rule also reaches arrangements that create rights or obligations not normally created at arm's length; the RRA may disregard, recharacterise, reallocate, or deem persons related (ITL art 68).

**Choosing the method (Order arts 8(2), 9 to 16).** The approved methods are:
- comparable uncontrolled price (art 9);
- resale price (art 10);
- cost plus (art 11);
- transactional net margin, against costs, sales or assets (art 12);
- transactional profit split, including the residual approach (art 13).

The most appropriate method weighs the methods' strengths and weaknesses, the functional analysis (functions, assets, risks), the reliable information available and the degree of comparability (art 8(2)). Another method is allowed only if the RRA is satisfied that none of the five can reasonably apply, or that the other method gives an arm's length result (art 14). For cost plus, resale price and TNMM a tested party must be selected, consistent with the functional analysis; if it is foreign, enough information on it must be held for the RRA to review (art 15).

**Comparability (Order arts 4, 6, 7, 20).**
- Factors: characteristics of the property or services; functions, assets and risks; contract terms; economic circumstances; business strategies (art 6(1)).
- Risk follows control: a party that contractually bears a risk but does not control it or lacks the financial capacity to bear it is not allocated the profit from it (art 6(2), (3)).
- A transaction that independent persons behaving rationally would not have entered may be disregarded (art 7).
- Comparables may be internal or external; foreign comparables are allowed case by case when none exist in Rwanda, adjusted for geographic differences (art 20). The RRA may not rely on external data the taxpayer cannot see, and the taxpayer may not rely on data it does not give the RRA (art 20(2), (3)).

**Services (Order art 21).** An intra-group service fee is treated as arm's length if the service was actually rendered, gave (or was expected to give) economic or commercial value, is one an independent party would pay for or perform itself, or its amount matches what independent parties would agree (the Order joins the last two tests with "or"; document all four). Shareholder activities are not chargeable: the parent's legal structure, shareholder and supervisory costs, parent reporting and consolidation, and raising funds to buy shares (unless the shares benefit the payer). Where services cannot be identified per recipient, the total is allocated by reasonable keys.

**Intangibles (Order art 22).** Returns follow the development, enhancement, maintenance, protection and exploitation functions, assets and risks, and who controls them, not only the contracts. Both the transferor's and the transferee's perspectives count. For hard-to-value intangibles the RRA may use actual outcomes as presumptive evidence of the original pricing.

**Corresponding adjustments (Order arts 23, 24).** For a domestic adjustment the RRA may adjust the other Rwandan party. For a foreign adjustment, a Rwandan resident may ask the RRA to examine it where the other country has a treaty with Rwanda aimed at relieving economic double taxation; if it is arm's length, the RRA reduces the Rwandan tax.

**Documentation (Order art 17).** Beyond the books the tax laws require, a person in controlled transactions must have:
- a transfer pricing policy;
- a local file and a master file;
- evidence that the year's controlled transactions are at arm's length.

The local file includes at least:
- the business overview and organisation;
- the legal and operational group structure;
- group business drivers, and the supply chain for the five largest products or services plus any above 5% of group turnover;
- strategy and restructurings, and key competitors in Rwanda;
- the controlled transactions, the functional analysis, the comparables search and its rejections, the method, tested party and financial indicator;
- financial data tied to the annual accounts, any foreign APAs, and a conclusion on arm's length.

The documentation also includes:
- the country-by-country report where the ultimate parent must prepare one;
- copies of intercompany agreements;
- third-party supplier contracts and invoices for supplies sourced through a related party;
- the controlled transactions schedule (Annex 1 model form);
- allocation keys and their rationale.

A person with annual turnover above FRW 20,000,000 keeps information on controlled transactions (Law 020/2023 art 14, item 5), for 10 years from 1 January after the year it relates to (art 15). For related party transactions the annual declaration is accompanied by the transfer pricing documentation (art 16).

**Advance pricing agreements (ITL art 32; Order arts 25 to 31, 35).**
- **Who and when.** A taxpayer may apply before entering into controlled transactions, or after (art 26(1), (2)). A pre-application meeting is possible (art 26(8)). The application goes through an RRA portal, which the Order required within three months of publication (arts 27, 35).
- **The proposal (art 28(2)).** It covers the activities, the transactions, the parties and permanent establishments involved, the method and critical assumptions, any other country to involve, and the art 17 documentation.
- **Process.** Missing information is due within 30 days, or the application is treated as withdrawn (art 26(4)). With a treaty partner the APA can be bilateral or multilateral (art 26(7)). The RRA accepts, modifies or disregards the proposal (art 28(4)) and drafts the agreement within 45 days after final engagement (art 28(5)). The taxpayer signs within 30 days of the invitation, or the application is treated as withdrawn (art 28(7)).
- **Refusal (art 29).** The RRA may disregard an application aimed at evading or avoiding tax, one that does not meet the requirements, or one filed while the transaction is under audit, investigation, appeal or court proceedings.
- **Compliance.** An annual compliance report is filed with each return in the term (art 30(2)).
- **Cancellation (art 31).** On a breach of terms or critical assumptions, a request from the treaty partner, a material change in law or conventions, tax evasion (immediate) or facts that deviate. It takes effect 30 days after notice.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Annual CIT declaration and payment for 2026 | 31 March 2027 (see rw-corporate-income-tax) | ITL art 9 as amended by Law 051/2023 art 1; ITL art 10 |
| Transfer pricing documentation for the period | prepared before the income tax declaration deadline and submitted to the RRA; the declaration for related party transactions is accompanied by it | Order art 18(1); Law 020/2023 art 16 |
| Controlled transactions schedule and the subsidiary's structure document | submitted with the tax declaration | Order art 18(1), (2) |
| Global legal structure of the group (all related persons, shareholdings, management) | with the first income tax declaration; updates with the declaration for the year of change | Order art 18(3), (4) |
| Documentation produced on request | within 7 days of receiving the written request | Order art 18(2) |
| Country-by-country report (where the ultimate parent must prepare one) | not later than 12 months after the last day of the reporting fiscal year | Order art 17(3)(g) |
| APA additional information; signature | within 30 days of the request; within 30 days of the invitation to sign | Order arts 26(4), 28(7) |
| APA annual compliance report | on the date the return is filed, each year of the term | Order art 30(2) |
| Extension of a declaration deadline | apply in writing at least 15 days before the deadline; interest still runs | Law 020/2023 art 20 |

**How it is filed.** In E-Tax (https://etax.rra.gov.rw), the Real Regime CIT or PIT annexures include a Related Party Transactions (transfer pricing) tab. The RRA Handbook says it must be completed and uploaded with every Real Regime declaration, with a single "None" row if there were no related-party transactions. Each row asks for:
- the related person, the nature of the relationship, and its countries of residence and incorporation;
- the transaction type;
- the aggregate inbound and outbound values in FRW;
- the percentage covered by transfer pricing documentation;
- the method and the key financial items.

The other filing steps are in rw-corporate-income-tax.

## Penalties and interest

- **Information on controlled transactions:** an administrative fine of 5% of the value of the controlled transaction if information is not provided, or is incomplete, incorrect or misleading (Law 020/2023 art 86), without prejudice to other sanctions.
- **Records:** failing to keep books and records of controlled transactions is a fixed-fine fault, and the applicable fine is doubled (art 81).
- **Information requests:** not answering an RRA request on time, or answering incompletely or misleadingly, costs FRW 500,000 to FRW 5,000,000 by turnover band, doubled for a second fault within 2 years and quadrupled for a third (art 81).
- **Understatement (art 83):** if an adjustment shows the declared tax was understated by 10% to 20% of the liability, the fine is 10% of the understatement; above 20% it doubles. No understatement fine applies if the taxpayer corrects and pays before notice of an audit, though late-payment fines then apply.
- **Late payment fines (art 82)** and **interest (art 80):** 0.5% a month for up to 6 months, 1% from 6 to 12 months, 1.5% after 12 months; simple, every started month counts, capped at 100% of the tax, payable even under appeal. Figures and bands: rw-corporate-income-tax.
- **Evasion:** a fine equal to the evaded tax plus criminal penalties (art 81); concealment extends the audit window to 10 years (art 35).

## Cross-border points

- **Foreign related parties:** cross-border dealings are in scope whenever one party is taxable in Rwanda (Order art 3(1)(a)). A Rwandan permanent establishment dealing with a related non-resident is also in scope (art 3(1)(b)).
- **Low-tax counterparties:** a transaction with any person in a beneficial tax regime is treated as controlled even if unrelated (ITL art 3(7); Order art 3(1)(c), (d), (2)).
- **Payments abroad:** management, technical and royalty fees to a non-resident related person above 2% of turnover are not deductible (ITL art 25). The gross payment also bears 15% withholding where the payee is not registered with the RRA or has no recent income tax declaration, unless a treaty reduces it (ITL art 60; see rw-cross-border).
- **Secondary adjustment:** after an adjustment, the balance left after tax is dividend income (ITL art 40). Dividends to a foreign parent that is not registered in Rwanda fall within the 15% dividend withholding (art 60, item 1); how the RRA collects it on a deemed dividend is not confirmed.
- **Double taxation relief:** corresponding adjustments for foreign adjustments are available only where a treaty provides for relief (Order art 24). Bilateral APAs need a treaty partner (art 26(7)).

## Two worked examples that recompute

### Example 1: under-remunerated distributor adjusted to the median

Kivu Distribution Ltd (Rwanda, calendar year) buys all its products from its Kenyan parent. In 2026 its sales are FRW 5,000,000,000 and its operating margin is 0.5%. A TNMM benchmark of independent distributors gives an interquartile range of 2.0% to 4.0%, median 3.0%.

- **Outside the range, so reset to the median (Order art 16(4)):** (3.0% - 0.5%) x 5,000,000,000 = FRW 125,000,000 of extra profit.
- **CIT at 28%:** FRW 35,000,000.
- **Secondary rule:** the balance of FRW 90,000,000 after tax is dividend income (ITL art 40). At 15% dividend withholding (ITL art 60, the parent not being registered in Rwanda), that is FRW 13,500,000, unless a treaty with Kenya reduces it.
- **Exposure if the file is missing:** the 5% fine under art 86 would be on the value of the controlled purchases, on top of the above.

```oa-check
name: Rwanda distributor TNMM adjustment to median, sales FRW 5bn (2026)
inputs:
  sales: 5000000000
  actual_margin: 0.005
  median_margin: 0.03
  cit_rate: 0.28
  dividend_wht: 0.15
steps:
  - adjustment: (median_margin - actual_margin) * sales
  - extra_cit: adjustment * cit_rate
  - deemed_dividend: adjustment - extra_cit
  - dividend_tax: deemed_dividend * dividend_wht
  - total_cost: extra_cit + dividend_tax
expected:
  adjustment: 125000000.00
  extra_cit: 35000000.00
  deemed_dividend: 90000000.00
  dividend_tax: 13500000.00
  total_cost: 48500000.00
```

### Example 2: decision, does the company need a local file and master file?

Two Rwandan companies each have 2026 turnover of FRW 550,000,000, below the FRW 600,000,000 waiver line (Order art 19).
- **Company A:** its largest controlled transaction is FRW 8,000,000 and the aggregate is FRW 95,000,000. It meets both the single-transaction and the aggregate limb, so it is waived from the art 17 file. It must still price at arm's length (art 19(3)) and complete the E-Tax related-party tab (Handbook).
- **Company B:** it pays a related-party royalty of FRW 60,000,000 and has an aggregate of FRW 120,000,000, failing both limbs. It needs the full policy, local file and master file before 31 March 2027. If it cannot produce the information, the art 86 fine is 5% x 120,000,000 = **FRW 6,000,000**.
- **APA:** Company B cannot yet apply. It meets the FRW 100,000,000 transaction test but not the FRW 600,000,000 turnover test (art 28(1)).

```oa-check
name: Rwanda documentation waiver decision and art 86 exposure (2026)
inputs:
  waiver_turnover: 600000000
  turnover: 550000000
  aggregate_limit: 100000000
  a_aggregate: 95000000
  b_aggregate: 120000000
  fine_rate: 0.05
steps:
  - turnover_headroom: waiver_turnover - turnover
  - a_headroom: aggregate_limit - a_aggregate
  - b_excess: b_aggregate - aggregate_limit
  - b_fine_exposure: b_aggregate * fine_rate
expected:
  turnover_headroom: 50000000.00
  a_headroom: 5000000.00
  b_excess: 20000000.00
  b_fine_exposure: 6000000.00
```

## Ask the client first

1. Who owns, manages or controls the Rwandan entity, and who it deals with: family links, participation in management, control or capital, and common control.
2. Every controlled transaction in 2026, domestic and cross-border, by type and FRW value, including dealings with unrelated parties in places with tax of 15% or less.
3. Annual turnover, the largest single controlled transaction and the aggregate value, against FRW 600 million, FRW 10 million and FRW 100 million.
4. Whether a policy, local file, master file, intercompany agreements and a benchmark exist, and their dates; whether the group files a country-by-country report and its fiscal year end.
5. Management, technical, royalty and interest payments to foreign related persons, against 2% of turnover and 4x paid-up equity.
6. Any APA, any foreign adjustment needing a corresponding adjustment, and any open audit.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 027/2022 establishing taxes on income, OG Special of 28/10/2022 (read for arts 3(1), 3(7) to 3(9), 8 to 10, 25, 32, 40, 47, 48, 60, 68, 70) | https://www.rra.gov.rw/fileadmin/user_upload/Income_Tax_law_of_2022.pdf | 2026-11-02 |
| Law 051/2023 amending the income tax law (read for arts 1 and 2: declarations and the 28% rate) | https://www.rra.gov.rw/fileadmin/user_upload/Law_amending_Income_Tax_Ok.pdf | 2026-11-02 |
| Official Gazette Special of 29/05/2025, Law 014/2025 amending the income tax law (read whole: arts 36, 37, 45, 50, 50 bis, 61 amended; no transfer pricing change) | https://www.minijust.gov.rw/index.php?eID=dumpFile&f=130496&t=f&token=4b9d4de9658212b7aaeeb5c8a42c823a7b879d7b | 2026-11-02 |
| Ministerial Order 003/26/10/TC of 29/04/2026 relating to transfer pricing, simplified accounting method and authorisation to carry forward loss for more than five tax periods, OG Special of 29/04/2026 (read for arts 1 to 31, 35 to 37 and Annex 1) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/Ministerial_Order_on_Simplified_Accounting_Method_April_2026.pdf | 2026-11-02 |
| Law 020/2023 on tax procedures (read for arts 9, 14 to 16, 20, 35, 46, 55, 80 to 83, 86) | https://www.rra.gov.rw/fileadmin/user_upload/OG_n___Special_ter_of_31.03.2023_Uburyo_bw_isoresha_Tax_procedures_01.pdf | 2026-11-02 |
| RRA Tax Handbook 2025 (read for the related persons page, the Related Party Transactions tab and audit types) | https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf | 2026-11-02 |
| RRA, Laws, policies and rulings page (read for the list of income tax laws and orders in force, including the 2020 transfer pricing Order still listed) | https://www.rra.gov.rw/en/laws-policies-and-rulings | 2026-11-02 |

Not yet confirmed: whether the full local file and master file are filed with the declaration (Law 020/2023 art 16 and Order art 18(1) say the documentation is submitted; Order art 18(2) names only the structure document and the schedule as filed with the declaration and the rest as produced within 7 days of a request); the declaration date for a company with an approved non-calendar tax period (ITL arts 9 and 10 as read give only 31 March; the 3-month rule in ITL art 45(2) as amended by Law 014/2025 art 3 is for exempt persons' statements); whether Order art 21(1) requires all four service tests or any one (its list ends with "or"); the reading of Order art 19(2), whose "or" between the FRW 10,000,000 and FRW 100,000,000 limbs could mean either limb suffices (the worked example uses facts that pass or fail both); whether the controlled transactions schedule is still required from a taxpayer waived under art 19 (the Handbook requires the E-Tax tab from all Real Regime filers); how the RRA collects withholding on the art 40 deemed dividend after an adjustment, and whether it applies when the counterparty is a resident company; whether a Rwandan-parented group must file a country-by-country report itself and at what group revenue threshold (the Order sets none); the fixed fine base for art 81 item 9 before doubling (art 81 excludes items 9 and 10 from the listed amounts); whether the RRA APA portal under art 35 is live; any Commissioner General directives on transfer pricing or on advance rulings (Law 020/2023 art 9); the list of treaties with a corresponding-adjustment or mutual agreement article.
