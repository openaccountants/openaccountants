---
name: kazakhstan-vat
description: "Kazakhstan 2026 VAT: registration, current rates, supply classification, credit, imports, deadlines and evidence-based worked cases."
version: 2.1
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax

type: computation
category: international
---

# Kazakhstan VAT and quarterly return v2.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Registered Kazakhstan VAT/NDS payers preparing the ordinary quarterly VAT job. Load `vat-workflow-base` v0.1 or later. Importers and special-regime non-resident/import-VAT obligations require their own branch rather than an assumption that non-registration eliminates VAT. The ordinary return is Form 300.00; use the current official electronic form, not the old unsupported line-code table. Currency is KZT. KGD/Ministry of Finance administers the job; use the current taxpayer cabinet and IS ESF.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Ordinary domestic taxable turnover/imports | 16% in 2026; classification and turnover date matter (art. 503(1)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Specified medicines/devices and licensed medical services outside exemptions | 5% in 2026, 10% from 2027; statutory/government-list and licence conditions apply (art. 503(2)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Domestic periodical printed publications | 10% (art. 503(3)); not every printed product | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Qualifying chapter-47 turnover | 0% only with the specific export/international-transport/other statutory conditions and evidence (art. 503(4)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Ordinary VAT registration threshold | 10,000 МРП of 1 January, calendar-year cumulative test under arts. 99–101; special-regime taxpayers and other art. 99 exclusions cannot register | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| 2026 threshold, derived | KZT 43,250,000 = 10,000 × KZT 4,325; art. 101 specifies start date and pre-transaction/application rules | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru |
| Ordinary return period/window | Quarterly; no earlier than the 15th after the quarter and no later than the 15th of the second month after it (arts. 504–505) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Ordinary payment | 25th of the second month after the quarter, including ordinary non-resident VAT; customs/import and liquidation exceptions differ (art. 506) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Establish registration/transaction scope first. Arts. 99–101 exclude special-regime taxpayers from ordinary registration; threshold counting after a special-to-general transition begins on that transition date. Apply within 5 working days after excess, and before turnover on a transaction that itself exceeds the threshold. Below-threshold eligible general-regime taxpayers can elect registration; do not presume voluntary deregistration merely because subsequent turnover falls.

For each sale identify goods versus services, place of supply under art. 459 (or EAEU art. 515), turnover date and applicable exemption/rate. A foreign payer does not automatically make a service zero-rated. Outside-Kazakhstan place-of-supply services are non-taxable turnover under art. 450, whereas qualifying goods exports use art. 467 and their export evidence. The old generic “agricultural zero rate” and blanket financial/insurance/medical/education/residential/public-transport exemptions are not current classification instructions; test the actual article/list. Medical treatment changed in 2026.

Input credit requires the art. 480 conditions: registered payer, eligible acquired supplies used for taxable turnover, valid stated VAT/documentation, relevant import/payment evidence, and the IS ESF recognition/period requirements. Art. 482 denies credit for specified defects, non-taxable use and other listed cases. Credit is claimed once, not once per available document. Timing under art. 481 differs for domestic receipt, customs release, EAEU import payment and non-resident services. Mixed taxable/exempt use requires the statutory allocation method under arts. 487–489, outside automatic classification. Do not automatically credit a whole bank debit.

Non-resident services: art. 454 applies when the purchaser/supply meets its scope and Kazakhstan place-of-supply test. Check its exceptions, including an electronic service already including the foreign supplier’s VAT under the statutory foreign-company regime, services in customs/EAEU import value, listed exemptions and other specified cases. Reverse charge is not inferred from a SaaS brand alone and is not always immediately net zero. The self-invoice and payment/credit conditions are separate.

EAEU goods imports are distinct from non-EAEU customs imports. Establish actual dispatch/transaction facts, not just a counterparty’s bank country. Keep the import statement and indirect-tax payment, invoices/contracts and movement documents under art. 530; the ordinary import VAT payment is due by the 20th of the month following the import tax period (art. 530(5)), and the import statement is separately due by the 20th of that following month, with specialised leasing/price-change rules. A Form 328.00 reference is an import-statement identifier, not proof of the current electronic field map. Complex triangulation/tolling/processing routes to a specialist. Customs imports use customs value/tax/documentation and release-based credit timing.

Ask the actual industry/activity. For fuel or vehicle spending establish passenger car versus commercial use and business-use evidence; for large purchases ask whether a capital/fixed asset is involved; for rent establish commercial versus residential premises, supplier VAT status and actual invoice. These are evidence questions, not automatic blocks or exemptions.

Bank-description patterns are prompts for evidence, not legal decisions:

- HALYK BANK/HALYK, KASPI BANK/KASPI, FORTE BANK, JUSAN BANK, BANK CENTERCREDIT, OTBASY BANK, PROTSENTY/INTEREST and KREDIT/ZAIM: distinguish actual financial services, principal and taxable fees.
- KGD/SALYK/TAX COMMITTEE, TAMOZHNYA/CUSTOMS, SOCIAL FUND/GFSS and GOVERNMENT OF RK: separate taxes, duty, import VAT and contributions from purchases.
- SAMRUK-ENERGO/KEGOC/AREK, ALMATY SU/ASTANA SU, KAZAKHTELECOM/KCELL/BEELINE KZ/TELE2 KZ: examine actual utility supply and valid VAT invoice, not an unconditional brand rate/credit.
- EURASIA INSURANCE/KAZKOM STRAKHOVANIE, STRAKHOVANIE/INSURANCE: confirm insurance/exemption scope. MAGNUM/SMALL/RAMSTORE and RESTORAN/KAFE/BAR: hold personal/entertainment items pending business use and valid-document evidence, not an invented universal block.
- GOOGLE/MICROSOFT/ADOBE/META, SLACK/ZOOM/NOTION/AWS/ANTHROPIC/OPENAI: identify contracting/billing entity and tax charged before the non-resident analysis.
- NOTER/NOTARY, AUDITOR/BUKHGALTER, ADVOKAT/LAWYER: check supplier/status, service and business purpose. ZARPLATA/SALARY, DIVIDEND, VNUTRENNIY/INTERNAL and BANKOMAT/ATM: separate payroll/distributions/internal transfers and unresolved cash.

Preserve source statements and supplier documents in the `vat-workflow-base` working paper: transaction/date/counterparty/currency, source link, place/rate/exemption decision, base/output/input, evidence, unconfirmed assumptions and review status. Halyk/Kaspi exports may use semicolons/DD.MM.YYYY, JSON or spreadsheets; inspect the actual file. Keep original FX and the legally applicable official conversion basis; distinguish personal Kaspi Gold activity, own-account transfers and genuine business transactions. Confirm statement-period coverage and carried-forward credit. Unknown country, business use, rate, EAEU origin or SaaS entity is a gap to resolve, not permission to assume a legal treatment. Legacy internal triage settings (KZT 5,000,000 transaction; KZT 300,000 tax delta; concentration above 40%; more than 4 defaults; KZT 10,000,000 net position) are optional workflow review flags, not statutory tax thresholds or safe harbours.

## Deadlines and filing

Reconcile output, admissible input and prior excess/credits to the current Form 300.00. Select the taxpayer and quarter in the current cabinet, transfer reconciled amounts to the verified current field labels, run form validation, sign/submit through the authorised process, retain acceptance and payment reference, then verify allocation. Never reuse the old 300.00.001–.013 mapping without the 2026 form rules. Arts. 505–506 govern ordinary return/payment dates, not every import. For non-resident-service self-invoices, art. 493 requires issuance after payment and within 5 calendar days of payment (5 in words on the page). For imports use the current customs/EAEU branch and relevant statement/payment evidence. Do not call unaccepted or unreconciled work “filed”.

## Penalties and interest

Late/non-registration, unsupported credit and false zero-rating can have distinct consequences. Determine the current operative administrative provision, taxpayer category and dates before quantifying a sanction. The optional internal triage figures are not legal materiality or penalty amounts.

## Cross-border points

EAEU members include Russia, Belarus, Armenia and Kyrgyzstan alongside Kazakhstan; this file describes the Kazakhstan obligations, not separate coverage for those jurisdictions. EAEU goods, foreign services, exports and foreign-company electronic VAT are different branches. Refer complex EAEU triangulation/tolling, mixed exempt use, disputed place of supply and any unsourced exemption. Income tax is outside this VAT computation. Simplified/patent/fixed-regime requests route to `kz-simplified-regime` for current eligibility/transition, not the old tax regimes.

## Two worked examples that recompute

Case 1: preserved NOTION LABS INC service input of 03.04.2026, KZT 7,520 before any Kazakhstan VAT. If the verified art. 454 scope applies and no exception applies, output is KZT 1,203.20 at 16%. Input credit is conditional on payment, self-invoice, use and timing; it is not automatically simultaneous. The old KZT 902 at 12% was wrong for 2026.

```oa-check
name: Nonresident SaaS conditional output and credit
inputs:
  base: 7520
  rate: 0.16
steps:
  - output: base * rate
  - eligible_later_credit: output
  - net_if_fully_eligible: output - eligible_later_credit
expected:
  output: 1203.2
  net_if_fully_eligible: 0
```

Case 2: preserved KAZAKHTELECOM utility input of 10.04.2026, KZT 18,500 VAT-inclusive, assuming an ordinary taxable invoice and full eligibility. Derived net is KZT 15,948.28 and VAT KZT 2,551.72, subject to actual invoice rounding/evidence.

```oa-check
name: VAT inclusive utility
inputs:
  gross: 18500
  rate: 0.16
steps:
  - base: round(gross / (1 + rate), 2)
  - vat: gross - base
expected:
  base: 15948.28
  vat: 2551.72
```

Case 3: preserved RESTORAN ZHETI KAZYNA dinner on 15.04.2026, KZT 35,000: hold credit pending business-use/legal/document evidence. Do not label every restaurant expense legally blocked. Case 4: preserved TECHCORP GMBH IT-services receipt on 22.04.2026, KZT 2,850,000: establish actual service and art. 459/515 place of supply; a foreign customer is not proof of a zero-rated goods export. No final VAT amount is supplied without those facts.

Case 5: preserved OOO TECHNOPARK equipment input on 18.04.2026, KZT 1,500,000 verified ordinary taxable EAEU import base. At 16%, import VAT is KZT 240,000, with the import statement/payment and separate credit conditions.

```oa-check
name: Ordinary EAEU import
inputs:
  base: 1500000
  rate: 0.16
steps:
  - import_vat: base * rate
expected:
  import_vat: 240000
```

Case 6: preserved ASTANA MOTORS car-lease input on 28.04.2026, KZT 450,000: hold pending actual contract, supplier VAT, business use, document and art. 480–482 analysis. The bank description does not establish a blanket vehicle-credit prohibition.

## Ask the client first

- Entity/ИП, regime, BIN/IIN, actual registration status and quarter?
- Complete statements, ESF register, supply contracts and evidence of business use?
- Goods/services, customer location/status and actual supplier billing entity?
- Imports/EAEU/customs/foreign services and their payment/movement documents?
- Taxable/exempt use, actual prior credit and accepted prior returns?
- Actual current form labels, unresolved defaults and review evidence?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 99–101, 447–450, 454, 459, 467, 480–482, 487–489, 493, 503–506; art. 530 ordinary import-statement and document provisions | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for 2026 budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru | 2026-11-14 |

Not yet confirmed: Exact current Form 300.00.001–300.00.013 line mapping and 328.00 electronic fields; generic agricultural zero-rating; categorical bank/insurance/education/residential/public-transport exemptions; a universal passenger-vehicle/entertainment block; exact FX conversion for every VAT transaction; full complex EAEU procedure; numeric penalties. These old claims are not default usable guidance. Counterparty patterns and 6 historical cases are retained above with corrected conditional treatment.
