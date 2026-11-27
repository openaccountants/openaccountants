---
name: de-freelance-intake
description: "Intake for German full-year-resident freelancers and sole traders, tax year 2026: collect documents, test classification, registration, VAT and profit method, record unresolved points and hand off to de-return-assembly. Includes dated 2025 cases without rolling their inputs forward."
version: 0.5
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# German freelancer and sole trader tax intake

## Scope

Collect and reconcile the evidence for one full-year German-resident sole proprietor, then hand it to the relevant Guides and `de-return-assembly`. This is an intake, not filing clearance. The working year is 2026; keep 2025 documents and examples in their own year. A person with a German home or habitual abode is subject to unlimited income tax liability ([EStG § 1(1)](https://www.gesetze-im-internet.de/estg/__1.html)); full-year residence is this workflow's scope limit, not the definition of every resident taxpayer.

Stop the sole-business workflow for non-residents, part-year residents, a partnership as the business, a GmbH/UG, farming/forestry, balance-sheet filers or more than five employees. Five employees is a workflow limit. Payroll at any size goes to `de-payroll`. Keep a separable own business in scope where a partnership interest or other income also needs specialist work. Obtain Steuerberater review before filing.

## Ask the client first

Read the documents first. Ask only the missing questions, in short related batches; use an available structured-question tool, otherwise one numbered list. Do not infer a settled tax status from a bank description, invoice note or the client's job title.

- Year, residence dates, legal structure, marital status, children, state, home/business addresses, tax number and VAT ID; employees and any partnership interest.
- Actual activities, qualifications, staff supervision, customers, sales of goods, commissions, brokerage and bought-in work resold; start/move/closure dates and trade registration.
- Prior/current-year turnover, including foreign and exempt sales and fixed-asset sales separately; VAT waiver, invoice treatment, filed periods and extension notices.
- EÜR or accounts, voluntary books, any bookkeeping notice or whole-business takeover; prior assessments, prepayments and actual payments.
- Home-working days/room/months/area, rent/utilities, telephone/internet business share; cars, acquisition details, list price, logbook, business/private kilometres, commuting days and one-way distance.
- Teaching/coaching, nursing/child care, midwifery, art/publishing or registered crafts; one main customer, employees/Minijobs, pension/KSK notices, GKV/PKV and insurer's annual statement including sick-pay position.
- Employment, rent, investments, crypto, foreign income and church membership/changes. Preserve unknowns as unknowns.

## The method, step by step

1. Confirm the year and scope. Collect the available documents together: full-year bank statements, sales/purchase invoices, assessments and prepayment notices, filed VAT returns/extension letters, prior EÜR and asset schedule, insurer statements, tax-office correspondence, registration/questionnaire, pension/KSK notices and asset receipts. If records are partial, start with them and list the gaps. For missing records, search the bank, email, ELSTER, insurer portal, saved files and previous adviser.
2. Reconcile bank receipts with invoices, distinguishing candidate sales, transfers and other movements. Extract customer/supplier location and service, net/VAT/gross amounts, dates, assets, rent, software, memberships, insurance, telephone/internet, vehicle costs and restricted-expense candidates. Bank descriptions and VAT shown are evidence to test, not proof of deductibility or VAT status. Preserve original invoice totals until treatment is established.
3. Compare the work with the classification rules below. Record the client's description separately from the conclusion; escalate unsettled classification and mixed activities. Do not make the facts fit a preferred route.
4. Check registration, turnover/waiver, return rhythm, EÜR eligibility and notices below. Read any authority instruction before applying the ordinary rule. Send VAT to `germany-vat-return`, records to `germany-bookkeeping` and classification/deductions to `de-einkommensteuer-freelancer`; add `de-trade-tax` for the commercial route.
5. Reconcile assessed prepayments to bank payments, by tax and year. Send planning to `de-estimated-tax`; insurance to `de-social-contributions`; other income to `de-employee-income-tax`, `de-rental-income`, `de-capital-gains` or `de-crypto-tax` as appropriate.
6. Show one compact summary with document sources, discrepancies, missing facts and referrals. Obtain corrections, then pass the structured package to `de-return-assembly`: taxpayer/structure/year, documents, receipts, expenses/assets, VAT, insurance, prepayments, prior assessments/AfA, home office, private use, municipality/trade-tax status and `open_flags`. Keep classifications `unsettled` and unknown amounts/rates/booleans `null`; zero means an evidenced zero. Supply a filing calendar and reviewer brief; any working paper must retain formulas and source references. Do not claim a return is ready while a material flag remains.

### Classification

[EStG § 18(1) no. 1](https://www.gesetze-im-internet.de/estg/__18.html) covers self-employed scientific, artistic, literary, teaching or educational activities and the named or similar professions. The list includes Ärzte, Zahnärzte, Tierärzte, Rechtsanwälte, Notare, Patentanwälte, Vermessungsingenieure, Ingenieure, Architekten, Handelschemiker, Wirtschaftsprüfer, Steuerberater, beratende Volks- und Betriebswirte, vereidigte Buchprüfer, Steuerbevollmächtigte, Heilpraktiker, Dentisten, Krankengymnasten, Journalisten, Bildberichterstatter, Dolmetscher, Übersetzer and Lotsen. Qualified assistance is compatible with this rule if the professional acts with their own expertise, leadership and personal responsibility; temporary representation does not itself defeat it. Software/IT work, design, marketing and a generic “consultant” label do not establish a classification. Other self-employed categories under § 18 require their own assessment.

[EStG § 15(2)](https://www.gesetze-im-internet.de/estg/__15.html) defines a trade as an independent, sustained activity undertaken for profit and participation in general economic life, excluding farming/forestry, a liberal profession and other self-employed work. A tax saving is not that profit; profit can be an ancillary purpose. For uncertain similar professions, staff arrangements, mixed activities, possible retrospective reclassification or a binding ruling: **Check this point with one of our partner accountants.** Collect prior Anlage S/G, assessments and registrations; do not promise that previous treatment is final.

### Registration

For ordinary starts, [AO § 138(1), (1b), (4)](https://www.gesetze-im-internet.de/ao_1977/__138.html) requires a commercial-business notification to the municipality, which informs the tax office; where real-tax assessment has not been transferred to municipalities the specified tax office takes its place. Freelance starts are notified directly to the competent tax office. Moving/closing is also covered. The AO notifications and start-up tax information are due within one month of the event. Further start-up details use the prescribed electronic dataset; the office may permit the prescribed paper form on hardship application. Check any applicable official exception. This tax-notification period does not settle separate trade-registration/licensing duties: **Check this point with one of our partner accountants.**

[ELSTER's start-up page](https://www.elster.de/elsterweb/infoseite/unternehmensgruendung) identifies the Fragebogen zur steuerlichen Erfassung. Use the questionnaire appropriate to the individual business, send it electronically to the Finanzamt and retain the receipt; the office sends the tax number after checking it. Compare actual start, submission, anticipated turnover/profit and VAT election. Flag an omitted or late submission for prompt correction.

### VAT triage

For an entrepreneur established in Germany, [UStG § 19(1)](https://www.gesetze-im-internet.de/ustg_1980/__19.html) exempts the covered supplies if statutory Gesamtumsatz did not exceed EUR 25,000 in the prior year and does not exceed EUR 100,000 in the current year, provided no effective waiver applies. Equality is inside each limit. Intra-EU supplies of new vehicles are excluded from this exemption (§ 19(6)); overseas establishment or EU-wide small-business treatment needs a separate review.

Gesamtumsatz is receipts-based turnover under § 19(2), not all bank credits: subtract the exempt supplies specified there and omit fixed-asset sales. Establish the place of each foreign supply before deciding whether it belongs in the German test. **Check this point with one of our partner accountants.**

The [2026 EÜR instructions, line 12](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) apply EUR 25,000 in the start-up year. The receipt crossing the applicable current-year limit is already under normal VAT rules; earlier exempt receipts remain exempt. Normal rules can themselves include other exemptions: do not automatically add VAT to every later sale. Previously taxable supplies received after a switch into the small-business scheme remain subject to their earlier treatment. Escalate the transition before issuing or correcting invoices.

Under [§ 19(3)](https://www.gesetze-im-internet.de/ustg_1980/__19.html), an irrevocable waiver declaration can be made by the last day of February of the second calendar year after the tax year; it operates from that tax year's start and binds for at least five calendar years. Revocation takes effect only from the start of a subsequent calendar year after that binding period. Ask for the actual election history.

Small-business exemption ordinarily disapplies the advance and annual return duties in § 18(1)–(4), but an authority request and [§ 18(4a)](https://www.gesetze-im-internet.de/ustg_1980/__18.html) remain: actual VAT liability on EU acquisitions, recipient-liable supplies or triangular transactions can require both annual and affected-period returns. Buying a foreign service alone proves none of those conditions. Invoice requirements, VAT wrongly shown, input deductions, foreign services/goods, ZM, OSS and special schemes: **Check this point with one of our partner accountants.**

For ordinary normal-scheme advance returns, [UStG § 18(2)](https://www.gesetze-im-internet.de/ustg_1980/__18.html) sets quarters by default, months where prior-year VAT exceeds EUR 9,000, and discretionary tax-office release from advance filing/payment where it is at most EUR 2,000. This tests VAT, not turnover. A prior-year refund surplus above EUR 9,000 permits a year-binding monthly election by submitting January's return by 10 February (§ 18(2a)). Check the election and office notices.

For ordinary starts in 2021–2026, use expected current-year VAT or annualise actual prior-year VAT if the business operated for only part of that year (§ 18(2)); do not carry this temporary rule into 2027 without checking the then-applicable law. Shelf/shell entities and other special cases: **Check this point with one of our partner accountants.**

Returns and payment are ordinarily due on the tenth day after each period ([§ 18(1)](https://www.gesetze-im-internet.de/ustg_1980/__18.html)); prescribed electronic submission, with a discretionary hardship-paper exception. An approved Dauerfristverlängerung extends filing and payment by one month ([UStDV § 46](https://www.gesetze-im-internet.de/ustdv_1980/__46.html)); it is refused/revoked if the tax claim appears endangered. Monthly filers must pay a special prepayment of one eleventh of prior-year prepayments; annualise a partial prior year using whole started months, or use expected payments for a current-year start ([§ 47](https://www.gesetze-im-internet.de/ustdv_1980/__47.html)). Application, annual declaration and crediting details: **Check this point with one of our partner accountants.**

### Profit method and trade tax

[EStG § 4(3)](https://www.gesetze-im-internet.de/estg/__4.html) allows receipts less expenses only where there is no statutory duty to keep books and regular accounts and the taxpayer does not voluntarily keep them. Asset, depreciation and other EÜR-specific rules still need checking. Submit EÜR by prescribed electronic dataset; the office may permit a prescribed paper calculation on hardship application ([EStDV § 60(4)](https://www.gesetze-im-internet.de/estdv_1955/__60.html)).

Check merchant duties under [HGB § 238](https://www.gesetze-im-internet.de/hgb/__238.html), which also count for tax under [AO § 140](https://www.gesetze-im-internet.de/ao_1977/__140.html). Commercial-register entry alone does not settle the result: [HGB § 241a](https://www.gesetze-im-internet.de/hgb/__241a.html) releases sole merchants with no more than EUR 800,000 sales AND EUR 80,000 annual surplus at two consecutive closing dates; for a new business the first closing date suffices.

For a commercial business, [AO § 141](https://www.gesetze-im-internet.de/ao_1977/__141.html) can impose books/accounts if the authority finds statutory Gesamtumsatz above EUR 800,000 in the calendar year OR commercial profit above EUR 80,000 in the business year. The ordinary commencement is the business year after notification. A whole-business successor can inherit the duty without a new commencement notice. Do not infer eligibility for EÜR merely from absence of a notice: check other legal duties and voluntary accounts. Freiberufler are not within § 141's size test. Send balance-sheet work to `germany-bookkeeping` and a partner accountant.

For an ordinary individual commercial business, [GewStG § 11](https://www.gesetze-im-internet.de/gewstg/__11.html) rounds trade income down to full EUR 100, deducts the EUR 24,500 allowance up to that rounded income and applies the 3.5% base rate. The municipality's multiplier and any special-rate relief must be established before computing tax. The classification, IHK membership/fees, trade-tax liability, § 35 income-tax credit and its income/actual-tax ceilings need review: **Check this point with one of our partner accountants.**

For the individual commercial route, [GewStDV § 25(1)](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html) requires a trade return when trade income exceeds EUR 24,500, when prior-period carried-forward losses were separately determined, or when the office specifically requests one. Do not treat the allowance as a universal no-return exemption. Filing format and specialist exceptions: **Check this point with one of our partner accountants.**

### Filing calendar and prepayments

First establish which annual returns the client must file; profit alone is not proof that every person must file. Income-tax filing duty, electronic-return exceptions and exact Anlage S/G/Vorsorgeaufwand/form-line selection: **Check this point with one of our partner accountants.**

For required calendar-year annual returns, the ordinary deadline is seven months after year end ([AO § 149(2)](https://www.gesetze-im-internet.de/ao_1977/__149.html)). Covered adviser-prepared returns have the last day of February of the second following year, subject to an earlier authority request (§ 149(3)–(4)); this is not a general extension for a voluntary employee return. Check individual requests/extensions and shorter VAT tax periods before using these dates. Pandemic extensions covered 2020–2024, not 2025/2026 ([EGAO Art. 97 § 36](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)).

- **2025:** own required annual return ordinarily due 31 July 2026; covered adviser return due 1 March 2027 because 28 February is Sunday.
- **2026:** own required annual return due 2 August 2027 because 31 July is Saturday; covered adviser return due 29 February 2028.

A Saturday, Sunday or statutory-holiday deadline moves to the next working day ([AO § 108(3)](https://www.gesetze-im-internet.de/ao_1977/__108.html)). Recalculate the actual date for the relevant locality.

Ordinary income-tax prepayments are due 10 March, 10 June, 10 September and 10 December, set by Vorauszahlungsbescheid, generally using the previous assessment after withholding credits ([EStG § 37(1), (3)](https://www.gesetze-im-internet.de/estg/__37.html)). Initial amounts require at least EUR 400 per calendar year AND EUR 100 per due date (§ 37(5)). Reconcile notices and payments rather than infer a missing obligation from a bank statement. Adjustments, additional-payment dates and late-filing/payment sanctions: **Check this point with one of our partner accountants.**

## Worked cases

These preserve the original years and inputs. Added conditions are assumptions for illustration, not newly discovered client facts.

1. **Lena, software developer for three agencies.** No trade registration; she calls herself Freiberuflerin. Keep classification unsettled. If an ordinary individual trade-tax computation applies to trade income EUR 30,000, rounded income is EUR 30,000; less EUR 24,500 gives EUR 5,500; at 3.5% the base amount is EUR 192.50 ([§ 11](https://www.gesetze-im-internet.de/gewstg/__11.html)). The old EUR 770 figure is only 4 × EUR 192.50, not an established income-tax credit. Classification, IHK consequences, actual trade tax and the credit: **Check this point with one of our partner accountants.**
2. **Tom, translator.** Statutory Gesamtumsatz EUR 25,000 in 2025; EUR 60,000 expected in 2026. If German-established, with no effective waiver and only supplies eligible for § 19(1), the 2025 equality does not exclude exemption in 2026; actual 2026 receipts must remain within EUR 100,000. If actual 2026 statutory turnover is EUR 60,000, § 19(1) is unavailable from 1 January 2027 because prior-year turnover then exceeds EUR 25,000 ([§ 19](https://www.gesetze-im-internet.de/ustg_1980/__19.html)). A forecast is not actual turnover; normal VAT does not make every activity taxable. Route the switch for review.
3. **Aylin, business coaching started 15 October 2026.** Do not assume freelance classification or teaching-pension eligibility. The ordinary one-month AO notification/questionnaire deadline falls on Sunday 15 November, moving to Monday 16 November 2026 ([AO §§ 138](https://www.gesetze-im-internet.de/ao_1977/__138.html), [108](https://www.gesetze-im-internet.de/ao_1977/__108.html)). If the domestic small-business scheme otherwise applies, the start-up limit is EUR 25,000 actual 2026 turnover; apply the crossing rule above. Trade-registration timing, classification and social insurance: **Check this point with one of our partner accountants.**
4. **Max, normal-scheme commercial business.** Original 2025 VAT EUR 9,000. Assume this is the relevant full-year tax, with no monthly refund election or special instruction: it does not exceed the threshold, so 2026 periods are quarterly. Q3's 10 October 2026 is Saturday: due Monday 12 October. With an effective one-month extension, the underlying 10 October deadline becomes 10 November 2026, not 12 November ([§ 18](https://www.gesetze-im-internet.de/ustg_1980/__18.html), [UStDV § 46](https://www.gesetze-im-internet.de/ustdv_1980/__46.html), [AO § 108](https://www.gesetze-im-internet.de/ao_1977/__108.html)). Amounts paid alone do not prove assessed VAT.
5. **Sara, unfiled own 2025 annual returns.** If she was required to file and has no extension, the ordinary deadline was 31 July 2026. Arrange filing promptly. The old automatic-surcharge checkpoint was 14 months after year end, February 2027; it did not mean 14 months after the filing deadline. Its actual application, weekend/extension effects, exceptions and amount: **Check this point with one of our partner accountants.**
6. **Original 2025 intake illustration, Max Mustermann.** Keep these as historical inputs, not established tax findings: single, Berlin, described as software developer/Freiberufler; VAT ID DE123456789; net receipts EUR 85,000 split TechCorp GmbH EUR 48,000, StartupAG EUR 25,000, smaller clients EUR 12,000; separately described EU income EUR 8,000 and VAT EUR 16,150 at 19%. Costs: rent EUR 6,000, software EUR 2,400, liability insurance EUR 600, prior adviser EUR 1,200, telephone/internet EUR 960, fuel EUR 3,600, maintenance EUR 800, MacBook Pro EUR 2,200 net in April 2025, input VAT EUR 2,300. TK/GKV EUR 8,400, formerly split EUR 7,200 plus EUR 1,200; care EUR 1,800; no pension payment detected. ESt prepayments EUR 2,500 × 4 = EUR 10,000; recorded SolZ EUR 0, church status unclear. The 2024 assessment supplied ESt EUR 12,000, profit EUR 42,000 and continuing AfA EUR 733. January–November 2025 VAT returns were said to be filed, December outstanding; an extension/one-eleventh prepayment was said to exist. Old estimated profit: EUR 68,000. The later placeholder illustration described a translator instead; do not overwrite the earlier activity. Arithmetic: 48,000 + 25,000 + 12,000 = 85,000; 85,000 × 19% = 16,150; 7,200 + 1,200 = 8,400. The eight listed costs total EUR 17,760, so 85,000 − 17,760 = EUR 67,240 before resolving mixed use, assets, VAT, insurance or other adjustments; EUR 68,000 is not reconciled. The EUR 8,000 EU amount may overlap the receipts; establish that first. Classification, invoice/input VAT, three-year versus one-year computer treatment, insurance deduction, SolZ and final profit: **Check this point with one of our partner accountants.** No return result follows from this template.
7. **Original 2026 home-working calculation.** If 150 days qualify under [EStG § 4(5) no. 6c](https://www.gesetze-im-internet.de/estg/__4.html), EUR 6/day capped at EUR 1,260 gives EUR 900. Qualification ordinarily requires mainly working at home and no visit to an outside first workplace that day; the permanent-no-other-workplace exception also allows away/first-workplace days. There is one allowance across activities, with no overlap with the specified second-household accommodation or room deduction. Check actual days and overlapping claims.
8. **Original 2026 commuting calculation.** Preserve 20 km one way, 220 days, EUR 0.38 and EUR 4,500: min(20 × 220 × 0.38, 4,500) = EUR 1,672. This is the arithmetic checkpoint only. Whether these are qualifying journeys to business premises, which distance/cap applies, public-transport alternatives, private/business car treatment and the different 2025 rate: **Check this point with one of our partner accountants.** Do not use the checkpoint as a deduction.

```oa-check
name: DE ordinary trade-tax base, original Lena input
inputs:
  trade_income: 30000
steps:
  - rounded: floor(trade_income / 100) * 100
  - excess: max(rounded - 24500, 0)
  - base: excess * 0.035
  - historical_fourfold: base * 4
expected:
  base: 192.50
  historical_fourfold: 770.00
```

```oa-check
name: DE 2026, home office day rate under the yearly cap
inputs:
  days: 150
steps:
  - amount: min(days * 6, 1260)
expected:
  amount: 900.00
```

```oa-check
name: DE 2026, commuting to own premises, 20 km, 220 days
inputs:
  km: 20
  days: 220
steps:
  - amount: min(km * days * 0.38, 4500)
expected:
  amount: 1672.00
```

```oa-check
name: Historical 2025 intake, reconciliation only
inputs:
  receipts: 85000
steps:
  - client_total: 48000 + 25000 + 12000
  - historical_vat: receipts * 0.19
  - listed_costs: 6000 + 2400 + 600 + 1200 + 960 + 3600 + 800 + 2200
  - unreconciled_checkpoint: receipts - listed_costs
  - prepayments: 2500 * 4
  - insurance_total: 7200 + 1200
expected:
  client_total: 85000
  historical_vat: 16150
  listed_costs: 17760
  unreconciled_checkpoint: 67240
  prepayments: 10000
  insurance_total: 8400
```

## When to refuse or refer

Each row is a hold on the tax outcome: **Check this point with one of our partner accountants.** Retain the question, evidence and destination in `open_flags`; loading a companion Guide does not release the hold.

| Topic needing a decision | Destination |
|---|---|
| Part-year/non-resident facts, partnership returns/interests and taint rules, corporations, farming/forestry or profit determination in another tax-office district | Appropriately qualified Steuerberater; `de-partners-and-part-year`, `de-non-resident-tax`, `de-corporate-tax` |
| Unsettled professional/commercial classification, mixed work, staff responsibility, binding ruling and prior-year reassessment | `de-einkommensteuer-freelancer`, `de-trade-tax` |
| IHK membership/fee exemptions, actual trade tax and § 35 credit | `de-trade-tax` |
| Low-value assets, register requirements and Kleinunternehmer cost measurement | `germany-bookkeeping` |
| Pool election, eligible assets, year-wide consistency and release period | `germany-bookkeeping` |
| Computer/peripheral/software useful life and continuing AfA; investment deductions/special depreciation | `germany-bookkeeping`, `de-einkommensteuer-freelancer` |
| Gifts: recipient/year limits, net/gross measurement and separate records | `de-einkommensteuer-freelancer` |
| Entertainment: reasonable business cost, participants/purpose/receipt and separate records | `de-einkommensteuer-freelancer` |
| Home-office room: centre of all work, actual costs versus annual allowance, part-year months and separate records | `de-einkommensteuer-freelancer` |
| Cars: business/private split, logbook/list-price/cost method, electric/hybrid relief, commuting versus business mileage | `de-einkommensteuer-freelancer` |
| Pension duty: teachers/coaches, carers, midwives, crafts and lasting one-client work; insured staff/Minijob treatment and exceptions | `de-social-contributions`; Deutsche Rentenversicherung |
| KSK: artist/publicist status, earnings, duration, staffing, trainees/Minijobs and statutory exclusions | `de-social-contributions`; Künstlersozialkasse |
| Health/care: GKV/PKV, basic cover, Zusatzbeitrag, sick pay, annual certified deductible amounts | `de-social-contributions`, `de-einkommensteuer-freelancer` |
| VAT invoices/tax wrongly shown, input tax, exemptions/rates, foreign supplies/purchases, ZM, EU acquisitions, OSS and transitions | `germany-vat-return` |
| Bookkeeping/record retention, GoBD, e-invoice issue/receipt/format/transition and tills | `germany-bookkeeping`, `germany-einvoice` |
| Church-tax membership/state/rate/base/rounding, salary, rent, investments, crypto and foreign income | Relevant income Guide and Steuerberater |
| Filing-duty exceptions, form placement, extra prepayments/adjustments, late-filing surcharge/formula/cap, interest and late-payment consequences | `de-return-assembly`, `de-estimated-tax`; Steuerberater |

## Completion checklist

Confirm the year and scope; reconcile source documents; keep classification/VAT/profit method evidenced or explicitly unsettled; reconcile notices/payments; obtain missing facts once; keep every specialist hold visible; confirm the corrected summary; hand the package, calendar and reviewer brief to `de-return-assembly`. A referral is not a client fact or professional approval.


## Sources

Read dates refer to the provisions or instruction passages identified here, not a read of an entire code. Applicable exact 26 November reads from the completed German bookkeeping, VAT and employee proofs are reused for unchanged operative rules; business applicability of EÜR and the home-day provision is confirmed directly by EStG § 4. No employee commuting entitlement is imported into the business example.

| Source and scope read | URL | Read on |
|---|---|---|
| EStG § 1(1): residence; completed German employee proof, same natural-person rule | https://www.gesetze-im-internet.de/estg/__1.html | 2026-11-26 |
| EStG § 18(1): professional activities and qualified staff | https://www.gesetze-im-internet.de/estg/__18.html | 2026-11-26 |
| EStG § 15(2): trade definition and profit purpose | https://www.gesetze-im-internet.de/estg/__15.html | 2026-11-26 |
| AO § 138(1), (1b), (1c), (4): tax notices/information, exception power and period | https://www.gesetze-im-internet.de/ao_1977/__138.html | 2026-11-26 |
| ELSTER: business questionnaire, submission and tax number | https://www.elster.de/elsterweb/infoseite/unternehmensgruendung | 2026-11-26 |
| UStG § 19(1)–(6): domestic exemption, turnover, waiver and excluded new vehicles | https://www.gesetze-im-internet.de/ustg_1980/__19.html | 2026-11-26 |
| BMF EÜR 2026 instructions, line 12: start-up, crossing and transition receipts; saved official text | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 | 2026-11-26 |
| UStG § 18(1)–(4a): periods, deadlines and small-business exception; ordinary period/extension reads reused | https://www.gesetze-im-internet.de/ustg_1980/__18.html | 2026-11-26 |
| UStDV § 46: extension, tax-claim safeguard | https://www.gesetze-im-internet.de/ustdv_1980/__46.html | 2026-11-26 |
| UStDV § 47: monthly special prepayment and partial/new years | https://www.gesetze-im-internet.de/ustdv_1980/__47.html | 2026-11-26 |
| EStG § 4(3), (5) no. 6c: EÜR and home-day conditions; German bookkeeping proof reused | https://www.gesetze-im-internet.de/estg/__4.html | 2026-11-26 |
| EStDV § 60(4): electronic EÜR/hardship; German bookkeeping proof reused | https://www.gesetze-im-internet.de/estdv_1955/__60.html | 2026-11-26 |
| HGB § 238: merchant books; German bookkeeping proof reused | https://www.gesetze-im-internet.de/hgb/__238.html | 2026-11-26 |
| AO § 140: non-tax-law duties; German bookkeeping proof reused | https://www.gesetze-im-internet.de/ao_1977/__140.html | 2026-11-26 |
| HGB § 241a: sole-merchant release; German bookkeeping proof reused | https://www.gesetze-im-internet.de/hgb/__241a.html | 2026-11-26 |
| AO § 141: size tests, notice and successor; German bookkeeping proof reused | https://www.gesetze-im-internet.de/ao_1977/__141.html | 2026-11-26 |
| GewStG § 11: ordinary rounding, allowance, base rate and special-rate boundary | https://www.gesetze-im-internet.de/gewstg/__11.html | 2026-11-26 |
| GewStDV § 25(1): trade return including loss carryforward/request | https://www.gesetze-im-internet.de/gewstdv_1955/__25.html | 2026-11-26 |
| AO § 149(1)–(4): annual/adviser deadlines and requests; German employee proof reused | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-11-26 |
| EGAO Art. 97 § 36 opening: pandemic years only; German employee proof reused | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-11-26 |
| AO § 108(3): weekends/holidays; German VAT proof reused | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-11-26 |
| EStG § 37(1), (3), (5): ordinary prepayments and initial minimums | https://www.gesetze-im-internet.de/estg/__37.html | 2026-11-26 |

Not yet confirmed: no usable unverified tax outcome retained; the listed specialist points remain explicit partner-accountant holds.
