---
name: ro-company-formation
description: "Company formation and entity choice in Romania for 2026. Covers SRL, SA, PFA and branches; the RON 500 new-SRL capital minimum, RON 5,000 floor above RON 400,000 prior-year net turnover, existing-company transition, paid-capital timing, net assets, ONRC registration, beneficial owners and first tax duties. Ordinary calendar-year accounts are due by 31 May; opted noncalendar financial years have a distinct 150-calendar-day rule. Trigger phrases: register a company in Romania, înființare SRL, capital social minim 2026, ONRC, Registrul Comerțului, PFA. Detailed company tax: ro-corporate-income-tax; VAT: ro-vat-return; payroll: ro-payroll-social; self-employed tax and contributions: ro-income-tax and ro-cas-cass; cross-border: ro-cross-border. Unverified current ancillary fees, live ONRC fields and representative-office procedures remain held under Sources."
version: 0.3
jurisdiction: RO
category: international
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: situation-rules
---

# Romania Company Formation & Entity Choice v0.3

## Scope

Use this skill to identify the legal form, compute subscribed and paid capital, assemble the statutory registration sequence and identify first-year duties in Romania for 2026. It covers the limited liability company (societate cu răspundere limitată, SRL), joint-stock company (societate pe acțiuni, SA), authorised natural person (persoană fizică autorizată, PFA) and branch (sucursală).

The National Trade Register Office (Oficiul Național al Registrului Comerțului, ONRC) administers registration under Law 265/2022, which repealed Law 26/1990: articles 24, 25 and 140. New SRLs have minimum subscribed capital of RON 500. The RON 5,000 floor above RON 400,000 prior-year reported net turnover has separate timing and transition conditions below. Subscribed capital, paid capital, registration expenses and operating funds are separate figures.

The first-tax recap preserves the topics of the earlier version. Load ro-corporate-income-tax, ro-vat-return, ro-payroll-social, ro-income-tax and ro-cas-cass for detailed computations and filing procedures; load ro-cross-border for international issues. This skill does not establish that a proposed activity is licensed or provide a verified live ONRC screen walkthrough.

## Ask the client first

1. Which legal form, activity and associates are proposed? Obtain ownership, control and foreign-entity details.
2. Is this a new company or existing SRL? Obtain registration date, current articles, subscribed capital and paid contributions.
3. What net turnover appears in the previous financial year's annual statements, and when was a higher turnover identified?
4. Are contributions cash or assets, when will operations begin, and is there a sole associate requiring expert valuation of an in-kind contribution?
5. What do approved annual and interim statements show for net assets, carried losses, reserves, dividends and shareholder/affiliate loans?
6. What are the registered office, financial year, employee plans, linked enterprises, VAT turnover and beneficial-owner changes or jurisdiction risks?

## The method, step by step

### 1. Select the legal form

**SRL.** Associates are liable only up to subscribed capital. There may be at most 50 associates. A sole associate has the general meeting's rights and obligations. Equal părți sociale cannot be represented by negotiable securities. These characteristics do not eliminate separate administrator liabilities. Law 31/1990 articles 3(3), 11, 12 and 13.

**SA.** The general rule is at least 2 associates unless the law provides otherwise; article 10(3) specifically requires at least 2 SA shareholders. The simultaneous-subscription payment rule below does not replace the separate public-subscription procedure. Law 31 articles 4, 9 and 10.

**PFA.** An economic enterprise without legal personality, organized by an individual principally using their own labour. Register before economic activity. OUG 44/2008 articles 1 and 2(i) distinguish liberal professions and activities organized by special laws; check special authorization separately. Law 265 article 87. Income tax and contributions belong in ro-income-tax and ro-cas-cass.

**Branch.** A subdivision without legal personality, registered before activity in the county where it will operate. A branch in the parent's county or locality still has a distinct registration. Other secondary establishments are recorded with the parent under article 43; do not describe them as separate subsidiaries. Law 31 article 43. A foreign representative office is a separate authorization job held under Sources.

### 2. Set capital and contribution dates

Law 239/2025 was published in Monitorul Oficial Part I no. 1160 on 15 December 2025. Article VI has no later commencement provision: Constitution article 78 gives commencement 3 days after publication, on 18 December 2025. Article XI(2) expressly starts articles II and III on 1 January 2026. These dates rest on the actually read official texts, rather than the inaccessible historical ONRC announcement.

| Capital item | Amount and conditions for 2026 | Act/article and official source |
|---|---|---|
| New SRL minimum | RON 500 subscribed capital for a newly formed SRL | Law 239 VI(2), [official text](https://legislatie.just.ro/Public/DetaliiDocument/307677) |
| Higher-turnover SRL | RON 5,000 where net turnover reported in the previous financial year's annual statements is **above RON 400,000** | Law 239 VI(1), [official text](https://legislatie.just.ro/Public/DetaliiDocument/307677) |
| Initial SRL payment | 30% of subscribed capital within 3 months after registration **and before operations in the company's name** | Law 31 article 9^1(2), [official text](https://legislatie.just.ro/Public/FormaPrintabila/00000G01M2T69J19PSR0XRYL4MCF6GLI) |
| SRL balance | Cash within 12 months after registration; in-kind within at most 2 years after registration | Law 31 article 9^1(2)(a)–(b), [official text](https://legislatie.just.ro/Public/FormaPrintabila/00000G01M2T69J19PSR0XRYL4MCF6GLI) |
| SA minimum | RON 90,000; government may adjust at most once every 2 years to maintain the RON equivalent of EUR 25,000 | Law 31 article 10(1), [official text](https://legislatie.just.ro/Public/FormaPrintabila/00000G01M2T69J19PSR0XRYL4MCF6GLI) |
| SA simultaneous subscription | At least 30% paid at formation if all signatories subscribe integrally and simultaneously; cash balance within 12 months, in-kind within at most 2 years after registration | Law 31 article 9(2), [official text](https://legislatie.just.ro/Public/FormaPrintabila/00000G01M2T69J19PSR0XRYL4MCF6GLI) |
| Existing-SRL transition | Increase capital set under VI(1) by amending the articles within 2 years after commencement; the low-turnover interpretation gap remains held below | Law 239 VI(6), [official text](https://legislatie.just.ro/Public/DetaliiDocument/307677) |
| Capital-increase publication reduction | 50% of the then-current Part IV tariff for an increase by 31 December 2026 under VI(1), **only if the amendment exclusively implements that capital increase** | Law 239 VI(7), [official text](https://legislatie.just.ro/Public/DetaliiDocument/307677) |

Apply all interacting SRL conditions:

- Increase the floor by the end of the financial year following the one in which the higher prior-year reported turnover is established: VI(3). Read this together with VI(6)'s existing-company transition; neither disregards the other.
- The capital floor set under VI(1) does not decrease when later reported turnover decreases: VI(4).
- Except conversion to another legal form, reduction below the minimum requires a simultaneous increase maintaining at least the legal minimum. Breach permits an interested person to seek dissolution: VI(5).
- If the VI(6) deadline is missed, the tribunal pronounces dissolution at an interested person's or ONRC's request. Reaching the legal minimum before the dissolution judgment becomes final prevents dissolution: VI(8)–(9).
- Do not infer an express existing-company RON 500 deadline from VI(2), which is worded for new SRLs. Keep the at-or-below-RON-400,000 interpretation gap under Sources.

Cash contributions are compulsory at formation. Work or services cannot form or increase capital. In-kind contributions must be economically measurable and effectively transferred/delivered; receivables are not admitted as SRL contributions. A sole associate's in-kind contribution requires a specialist expert valuation. Law 31 articles 13(3), 16. Apply these rules together with article 9^1: compulsory cash contribution does not mean all subscribed cash must already be paid at registration.

### 3. Assemble and submit the statutory ONRC application

This sequence is established by law. Current live field labels, the full operational checklist and ancillary tariffs are unverified; do not invent them.

1. **Reserve the name before drafting the articles.** ONRC checks availability and distinctiveness. An existing or reserved name cannot be reserved again; the proof lasts **1 month from issue**. Online reservation is permitted. Law 265 articles 48–50; Law 31 article 17(1). Present the proof for authentication where required or when giving the articles a date certain.
2. **Prepare articles and registered-office information.** ONRC must provide model articles for online constitution, Romanian forms and an English version for information. The application includes the reserved name, registered office, representative and correspondence details, date and signature. Attach documents prescribed for the form and any legally required pre-approvals. Law 265 articles 42 and 72. The model does not replace special licensing requirements.
3. **Apply the capital rules and identify beneficial owners.** Formation disclosure in the articles requires both identification details and control modalities to substitute for a separate initial UBO declaration: Law 129 article 56(7).
4. **Sign and lodge.** Normally file within **15 days after concluding the articles**, unless law provides otherwise. Filing is allowed at the counter, by post/courier or electronically; article 85 permits lodgment at any registry office. Electronic supporting documents require qualified electronic signatures or certification under article 84(3). Romanian-language, apostille/legalization and legalized translation requirements for foreign official documents depend on articles 75–76 and applicable exceptions. Law 265 articles 75–87. An unsigned upload is not proof of completed filing.
5. **Track decision and actual entry.** The normal documentary decision is within **1 working day** after filing. Identity doubts, foreign-register information or incomplete documentation can alter the process. Article 106 permits remedy/completion within at most **15 calendar days**; failure to comply leads to refusal. Actual entry is made within **24 hours** after the registrar orders it; legal personality starts at actual entry. The certificate contains the registry number, CUI fiscal code and EUID. Law 265 articles 105–110.
6. **Retain issued documents and publication evidence.** Electronic bulletin publication is due within **3 working days** after registration and is free to publish/consult. The registry transmits the required extract to Monitorul Oficial within **3 working days** after registration. That is a transmission deadline, not a guaranteed total incorporation period. Law 265 articles 15–16. No taxes or tariffs apply to registration and subsequent-entry operations in articles 41/43: article 44. This does not establish that all ancillary name services, assistance, translations or Part IV publication are free.

### 4. Test net assets before dividends or shareholder loans

Use approved annual statements for annual tests and approved interim statements for interim tests. Under Law 31 article 69^1(1), current-year profit distributions where accounting losses are carried forward require legal reserves, coverage of carried accounting losses and the required statutory reserves first.

If approved annual net assets are **below half of subscribed capital**, current-profit dividend distributions require restoration to the statutory minimum: article 69^1(2). Approved interim net assets below that level also bar interim current-profit dividends until restoration: 69^1(3). Article 69 separately requires reconstitution or reduction of subscribed capital before profit distribution where a net-asset loss is found; any reduction also respects minimum-capital rules.

Distinguish the two loan directions. A quarterly dividend distributor cannot **lend to** shareholders, associates or accounting-law affiliates before regularizing interim-distribution differences: article 67(2^3). A company with approved annual net assets below half of subscribed capital cannot **repay loans received from** those persons: article 67(2^4). Article 67(2^5) expressly provides joint liability for the company and the shareholder/associate beneficiary for outstanding centrally administered budget obligations, limited to the amount lent or repaid; do not extend that express liability rule to every affiliate covered by the loan bans. The separate article 153^24 capital-maintenance sanctions have their own timetable and exceptions; do not substitute them for these loan bans.

### 5. Complete UBO, payment-account and first tax duties

**UBO declaration.** File at formation and whenever the beneficial owner changes. Identification-detail changes must be declared within **15 days after the change**. Articles can meet the initial duty only if they contain both identification details and control modalities; later UBO updates do not alone require an articles amendment. Companies whose shareholding structures contain entities incorporated/registered and/or tax-resident in noncooperative tax jurisdictions, high-risk money-laundering/terrorism-financing jurisdictions or jurisdictions under relevant international monitoring file additionally each year within **15 days after approval of annual statements**. This is not a universal annual declaration. Law 129 article 56(1), (1^3), (3), (4), (7)–(8).

**Payment account.** From 1 January 2026, legal persons must hold a payment account in Romania or at the State Treasury. A new legal person opens it within **60 working days after formation** and maintains at least one throughout activity. Specified payment providers cannot refuse opening unless it would breach anti-money-laundering or international-sanctions law. Law 239 II and XI(2), amending Law 70/2015 article 1(1^2)–(1^4). This is distinct from paid-capital timing.

The CUI is the fiscal code; VAT registration is a separate test. The inherited first-tax figures below are scoped orientation; detailed computation belongs in the linked skills.

| First tax item | Rate or threshold and conditions for 2026 | Official source and detailed skill |
|---|---|---|
| Ordinary profit tax | 16% of taxable profit; special regimes may change the outcome | Fiscal Code article 17, [official text](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm); ro-corporate-income-tax |
| Micro-enterprise tax | Optional 1% of the statutory revenue base, only if eligible; EUR 100,000 ceiling with linked-enterprise aggregation | Articles 47–51, [official text](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm); ro-corporate-income-tax |
| New-company micro employee | Ownership conditions in 47(1)(d)/(h) at registration; employee condition within **90 days inclusive**. Failure means profit tax from the quarter after expiry | Article 48(3), [official text](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm); ro-corporate-income-tax |
| Resident-individual dividends | 16% final withholding for dividends distributed from 1 January 2026. Corporate-recipient exemptions, nonresident treaties and separate individual contributions need their own tests | Article 97(7), Law 141/2025 VII(1)(c), [official text](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm); ro-corporate-income-tax / ro-cross-border |
| Domestic small-business VAT exemption | RON 395,000 annual article 310 turnover ceiling; opt-in below it is possible. When exceeded, request registration by the crossing date and apply VAT starting with that transaction | Articles 310(1)/(2)/(6), 316(1), [official text](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm); ro-vat-return |

Micro conditions are cumulative: private rather than state/local-authority capital; no registered dissolution followed by liquidation; the employee condition; direct/indirect owners above **25%** designating a single eligible micro company; and annual statements filed on time. Check article 47(1^1)'s linked ownership/control and linked PFA rules. Article 47(3) excludes specified guarantee/compensation funds, transparent entities, banking, the specified insurance/capital-market businesses, gambling and oil/gas exploration/development/extraction, subject to its limited insurance-intermediary exception. Article 51(4) allows part-time contracts totaling a full-time equivalent, or a management/mandate contract remunerated at least at the national gross minimum, to satisfy the employee condition. For an existing company's 2026 micro option, article 48(2) specifically treats the statements condition as met if annual statements are filed by 31 March 2026 inclusive. Do not choose by comparing 1% with 16% alone.

## Boundary and exception table

| Situation | Treatment | Official source |
|---|---|---|
| Existing SRL at exactly RON 400,000 prior-year net turnover | VI(1) says above RON 400,000. The separate existing-company RON 500 deadline remains unresolved below | [Law 239 VI(1)/(2)/(6)](https://legislatie.just.ro/Public/DetaliiDocument/307677) |
| Turnover falls after the higher floor applies | The floor established under VI(1) remains unchanged | [Law 239 VI(4)](https://legislatie.just.ro/Public/DetaliiDocument/307677) |
| Capital amendment also changes another matter | The exclusive-purpose condition for the 50% Part IV reduction is not met | [Law 239 VI(7)](https://legislatie.just.ro/Public/DetaliiDocument/307677) |
| Incomplete application | Completion can change the normal one-working-day decision timeline; noncompliance can lead to refusal | [Law 265 articles 105–108](https://legislatie.just.ro/Public/DetaliiDocument/288036) |
| Never active since formation | Statutory inactivity declaration; a quiet later year is not that condition | [Law 82 article 36(2)](https://legislatie.just.ro/Public/DetaliiDocument/293379) |
| Foreign founder or official document | Apply the particular signature, translation, apostille/legalization and identification rules and their exceptions | [Law 265 articles 75–84](https://legislatie.just.ro/Public/DetaliiDocument/288036) |

## Worked cases

### New cash-only SRL

A new SRL is formed in 2026 with RON 500 subscribed cash capital. It starts operations before three months elapse. Initial payment is 500 × 30% = **RON 150**, due before operations and no later than three months after registration. The remaining **RON 350** cash is due within twelve months after registration. Fees and operating funds are excluded. Law 239 VI(2); Law 31 article 9^1(2).

```oa-check
name: New cash-only SRL capital payments
inputs:
  subscribed_capital: 500
  initial_fraction: 0.30
steps:
  - initial_payment: subscribed_capital * initial_fraction
  - remaining_cash: subscribed_capital - initial_payment
expected:
  initial_payment: 150
  remaining_cash: 350
```

### Decision: minimum cash capital for SRL or SA

Two eligible founders have RON 1,000 available for capital. Compare a new SRL with an SA formed by integral and simultaneous subscription, using cash-only contributions. Fees, licensing and commercial funding needs are excluded: this is only the statutory capital comparison.

An SRL requires RON 500 subscription: RON 150 initially under the before-operations/three-month rule and RON 350 remaining within twelve months. The SA requires RON 90,000 subscription: **RON 27,000 at formation** and RON 63,000 remaining cash within twelve months. Available cash covers the SRL minimum subscription. The SA has an **RON 89,000 total subscription-funding gap** and an **RON 26,000 initial formation-payment gap**. On this limited criterion the SRL fits; the SA requires additional capital. Law 239 VI(2); Law 31 articles 9(2), 9^1(2) and 10(1).

```oa-check
name: SRL versus SA minimum cash-capital funding
inputs:
  available_cash: 1000
  srl_capital: 500
  sa_capital: 90000
  initial_fraction: 0.30
steps:
  - srl_initial: srl_capital * initial_fraction
  - srl_balance: srl_capital - srl_initial
  - sa_initial: sa_capital * initial_fraction
  - sa_balance: sa_capital - sa_initial
  - sa_subscription_gap: max(0, sa_capital - available_cash)
  - sa_initial_gap: max(0, sa_initial - available_cash)
expected:
  srl_initial: 150
  srl_balance: 350
  sa_initial: 27000
  sa_balance: 63000
  sa_subscription_gap: 89000
  sa_initial_gap: 26000
```

## When to refuse or refer

Stop a completion claim if registered-office rights, signatures, special authorizations, owner/control evidence or actual registry entry are missing. Uploading documents is not proof the company exists.

Refer disputed existing-SRL capital transitions, threatened dissolution, net-asset restoration, shareholder loans, noncash valuation, public subscription and foreign representative-office authorization. Do not quote unverified ancillary fees, promise the earlier practical five-to-ten-business-day timeline or invent current ONRC buttons/fields. Held assertions below are outside usable guidance.

## Filing and payment

- **Annual accounts:** ordinary calendar-year Law 31 companies file with the competent ANAF fiscal body by **31 May of the following year**, or the next working day if nonworking. Opted noncalendar financial years generally have **150 calendar days** after close; the other-person class in 36(1)(b) instead has **120 calendar days**, with next-working-day treatment. Test the foreign-subunit EEA exception and other entity classes separately. Law 82 articles 35–37. The specified annual statements are transmitted electronically from financial year 2025: OUG 138/2024 XI(1). For an opted noncalendar financial year, that electronic-only rule starts with the statements for the first chosen financial year beginning after 1 January 2025: XI(2).
- **Never traded since formation:** the article 36(2) inactivity declaration is due within **60 days after financial-year-end**; a later inactive year does not satisfy this condition.
- **Profit tax:** ordinary calendar-year 2026 D101 and final payment are due **25 June 2027**. Ordinary quarterly declarations/payments for the first three quarters are due on the **25th of the month following each quarter**. Modified years and dissolution have separate deadlines. Fiscal Code articles 41(1), 42(1)–(2); ro-corporate-income-tax.
- **Payroll:** D112 is normally monthly by the **25th of the following month**. Article 147(4) requires quarterly submission of each month's declaration for article 80(2) payers, by the 25th after the quarter. These include nonprofits; profit-tax legal persons with preceding-year total revenue up to EUR 100,000 and average employees strictly below 3; micro companies with preceding-year average employees strictly below 3; and specified individual employers. Article 147(8) permits a monthly option; (10) governs qualifying new-company estimates. Under 147(11), medical leave or cessation of insured status accelerates the relevant quarterly payer's D112 deadline to the **25th of the following month**; declarations for the remaining part of the quarter retain the quarterly deadline. If insured status ends in the quarter's second month, both first- and second-month declarations are filed at the accelerated deadline. Use ro-payroll-social for the detailed mechanics.
- **VAT:** D300 is due by the **25th after the fiscal period**. Calendar month is the default. Quarterly eligibility uses article 322's preceding-year EUR 100,000 turnover test and absence of intra-EU goods acquisitions. New registrants have proportionate forecast/recalculation rules; a taxable intra-EU acquisition can switch the period. Fiscal Code articles 322–323; ro-vat-return.
- **Accounts late filing:** for the specific article 41(2)(e) offense, Law 82 article 42(1)(e) sets RON 300–1,000 for 1–15 working days late, RON 1,000–3,000 for 16–30 working days and RON 1,500–4,500 for more than 30 working days. Outright nonfiling and inactivity-declaration breaches are separate offenses; these bands are not universal accounting fines.
- **Loan bans:** Law 31 article 67(2^6) sets RON 10,000–200,000 for breach of 67(2^3)/(2^4). Law 239 XXV excludes the usual half-minimum payment option within fifteen days for this fine. Payment-account breaches have a distinct Law 70 article 12(4) sanction; do not reuse the loan-ban fine.

## Completion checklist

- Form, associates, activity and special-law requirements established.
- Correct capital floor, prior-year turnover, transition and contribution dates recorded; expert valuation obtained where needed.
- Name, articles, registered office, signatures, prescribed documents and UBO/control evidence assembled.
- Decision, actual registration, certificate, CUI/EUID and publication evidence retained.
- Account-opening, tax/VAT eligibility, payroll frequency and accounts duties assigned to named responsible people.
- Dividends and loans tested against approved annual/interim statements.
- Unresolved items remain held; filing, payment or incorporation completion is reported only from actual evidence.

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| Law 31/1990, official printable text containing amendments through 18 December 2025 | https://legislatie.just.ro/Public/FormaPrintabila/00000G01M2T69J19PSR0XRYL4MCF6GLI | Read for: Articles 1–17, 43, 67–69^1 and neighbors: forms, capital, contributions, branches, net assets and loans; latest listed amendment date checked | 2026-11-15 |
| Law 239/2025, selected 9 March 2026 consolidation | https://legislatie.just.ro/Public/DetaliiDocument/307677 | Read for: Publication; II–III, VI, XI, XXIV–XXV and neighbors: capital, account duties and company-law amendments | 2026-11-15 |
| OUG 43/2026, ANAF original | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_43_2026.pdf | Read for: XVIII–XXII: November repeal of Law 239 XXII parcel levy, with savings; does not amend formation VI/XXIV | 2026-11-15 |
| Constitution of Romania, Senate | https://www.senat.ro/pagini/constitutia/constitutia.htm | Read for: Articles 77–79, including 78 commencement | 2026-11-15 |
| Law 265/2022, selected 12 September 2024 consolidation | https://legislatie.just.ro/Public/DetaliiDocument/288036 | Read for: Articles 15–18, 24–27, 41–52, relevant 72–87, 104–110, 135–141: registration, documents, names, fees, cure, actual entry and certificate | 2026-11-15 |
| OUG 44/2008, selected 26 November 2022 consolidation | https://legislatie.just.ro/Public/DetaliiDocument/261165 | Read for: Articles 1–2 and neighbors: PFA definition, liberal-profession/special-law boundaries | 2026-11-15 |
| Law 129/2019, selected 19 December 2025 consolidation | https://legislatie.just.ro/Public/DetaliiDocument/305272 | Read for: Complete 56 and neighbors: UBO formation, change, articles alternative and annual risk-jurisdiction duties | 2026-11-15 |
| Law 82/1991, selected 4 February 2025 consolidation | https://legislatie.just.ro/Public/DetaliiDocument/293379 | Read for: Articles 34^1–37^2, 40–42: accounts deadlines, inactivity declaration and specific offenses/penalties | 2026-11-15 |
| OUG 138/2024, selected 6 December 2024 consolidation | https://legislatie.just.ro/Public/DetaliiDocumentAfis/292068 | Read for: IX–XI: accounting deadline amendment and electronic filing from financial year 2025 | 2026-11-15 |
| Fiscal Code, ANAF annotation, header latest Law 204/2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | Read for: 17, 41–42, 47–52, 80–81, 97(7), 147, 310, 316, 322–323 and neighbors: scoped tax recap, quarterly conditions, VAT and deadlines | 2026-11-15 |
| Law 223/2020, ANAF original | https://static.anaf.ro/static/10/Anaf/legislatie/L_223_2020.pdf | Read for: Entire original I–III: capital wording replaced without expressly enacting RON 1 | 2026-11-15 |

Not yet confirmed: (1) how ONRC/courts apply VI(6) to existing SRLs at or below RON 400,000 prior-year net turnover; VI(1) specifies RON 5,000 above it and VI(2)'s RON 500 is expressly for new companies, so no existing-company RON 500 deadline is asserted; (2) the earlier historical statutory RON 1 minimum claim for 2020–2025: the actually read Law 223 original removes numerical wording without stating RON 1; (3) current name-reservation fees, Part IV publication tariffs, live ONRC fields and complete operational checklist, because ONRC pages/DOCX returned Request Rejected challenge content; (4) current foreign-company representative-office authorization, distinct from a Law 31 branch; (5) the earlier practical 5–10 business-day timeline, which the statutory one-working-day decision does not prove; (6) the inaccessible ONRC announcement of 17 December 2025 that the previous version said confirmed commencement on 18 December 2025, the earlier description of SRL as the usual business vehicle (no official frequency evidence read), and the original ANAF Law 82 PDF's consolidation date. Alternative official reads above support the usable rules. The newest Law 239 consolidation dated 1 November 2026 could not be opened; its operative OUG 43 amendment was read separately. No blocked response counts as a legal read, and none of these held assertions is usable filing guidance.
