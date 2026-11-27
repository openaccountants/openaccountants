---
name: netherlands-transfer-pricing
description: Use this skill whenever asked about Netherlands transfer pricing rules, documentation requirements, or verrekenprijzen compliance. Trigger on phrases like "transfer pricing Netherlands", "Dutch TP documentation", "verrekenprijzen", "master file Netherlands", "local file Netherlands", "CbCR Netherlands", "APA Netherlands", "Article 8b DCITA", "DTA transfer pricing", "CbC fine Netherlands", "missing transfer pricing documentation Netherlands", "verrekenprijzen boete", or any question about intercompany pricing for Dutch entities.
version: 1.4
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: transfer-pricing
type: situation-rules
---

# Netherlands transfer pricing: pricing, documentation and reporting, 2026 v1.4

Tax year 2026: related-party pricing, mismatches, documentation, country-by-country (CbC) reporting and failures. First obtain entity, years, ownership, preceding-year revenue and transaction evidence. Examples do not establish market prices. Corporate tax computation: `nl-corporate-tax`.

## Who this applies to

- **Related bodies:** article 8b applies to direct or indirect participation in another body's management, supervision or capital, and where the same person participates in both. Apply independent-party conditions to profit. Domestic dealings are included. [Wet Vpb art. 8b(1)–(2)][law1].
- **Article 8b records:** every body within that relationship test keeps the pricing records; there is no revenue exemption. [Art. 8b(3)][law1].
- **Master/local files:** a Dutch-taxable entity of a multinational group meeting the preceding-reporting-year test below. Group entities include size/materiality consolidation exclusions and qualifying separately accounted PEs. A multinational group has different-state resident bodies or a taxable foreign PE. [Arts. 29b–29g][law1].
- **Confidential CbC:** a Dutch-resident ultimate parent reports for an in-scope multinational group. A Dutch non-parent reports under the local-filing conditions below. Every Dutch-resident entity of an in-scope group must be covered by the separate notification. [Arts. 29c–29d][law1].

| Boundary / exception | Action |
|---|---|
| Below the master/local threshold | Keep proportionate article 8b evidence; do not infer a pricing exemption. |
| Domestic-only related dealings | Article 8b still applies; the multinational master/local and CbC tests are separate. |
| Non-parent CbC filing, surrogate or incomplete parent information | Apply the conditions below; a parent's refusal is not permission to do nothing. |
| Debt, transparency, merger/split or historical mismatch transition | Non-usable specialist hold. Check this point with one of our partner accountants. |
| Minimum tax, interest limits, innovation box, withholding tax, fiscal unity, VAT or customs | Separate workstream; this Guide gives no entitlement or computation under those regimes. Check this point with one of our partner accountants. |

## Rates, bands and thresholds

| Item and operative condition | Amount | Period | Source URL |
|---|---|---|---|
| Master/local files: multinational group's consolidated revenue in the reporting year immediately before the return year | At least EUR 50,000,000 | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 29g(4)) |
| Confidential CbC: preceding reporting-year consolidated group revenue | At least EUR 750,000,000 | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 29c(5)) |
| Public CbC: Dutch ultimate-parent entities listed in art. 2(1)(a), or standalone bv/nv; subject to the exceptions below | More than EUR 750,000,000 on two consecutive balance-sheet dates; obligation ends after two consecutive dates no longer exceeding it | Financial years beginning on/after 22 June 2024 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0049420/2024-06-22_0/xml/BWBR0049420_2024-06-22_0.xml (arts. 1–2, 15) |
| Optional qualifying low-value services; eligible cost base, allocation and documentation conditions below | 5% markup | 2026 | https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html (§ 6.3) |
| Corporate tax, taxable amount through EUR 200,000 | 19% | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 22) |
| Corporate tax, taxable amount above EUR 200,000 | EUR 38,000 plus 25.8% of the excess | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 22) |
| Article 29h CbC failure through intent/gross negligence; maximum, not an automatic fine | Sixth category: EUR 1,100,000 | Offences on/after 1 January 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 29h); https://zoek.officielebekendmakingen.nl/stb-2025-401.html (arts. I–II) |
| Corporate-tax vergrijpboete under AWR 67d/67e; statutory base and culpability conditions below | Up to 100% of the statutory penalty base | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml (arts. 67d–67e) |
| Policy starting points: additional-assessment gross negligence/intent; subject to individual mitigation/aggravation | 25% gross negligence; 50% intent | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0038145/2026-08-08_0/xml/BWBR0038145_2026-08-08_0.xml (§§ 6–8, 25–27) |
| Corporate-tax interest; future periods need their own rate check | 5% a year from 1 January 2026, published | Read 27 November 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente |

A lower current-year revenue does not undo the preceding-year tests. Public CbC has its separate two-date test.

## The base

**1. Delineate the transaction.** Compare contracts with actual conduct. Document contractual terms, functions/assets/risks, goods/services characteristics, economic circumstances and business strategy, including both parties' realistically available alternatives. Analyse who controls risks and can bear their financial consequences; a contractual label alone does not allocate the return. [2022 decree §§ 2.2–2.4](https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html).

**2. Support a method.** The methods are comparable uncontrolled price (CUP), resale price, cost plus, transactional net margin (TNMM) and transactional profit split. Support comparables and material adjustments. A one-sided method normally tests the less complex party. Justify the method, tested party and measure; reconcile to segmented accounts, including relevant losses. The result must be arm's length; testing every method is unnecessary. Distinguish gross resale margins, gross cost markups, net margins and combined-profit splits. [Decree §§ 2–3](https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html).

**3. Services.** Establish the recipient's benefit; exclude shareholder activities and do not charge merely for duplicated work. Separate mixed shareholder/service activities. Optional low-value services must support noncore business, without using/creating unique valuable intangibles or assuming/controlling/creating significant risks. OECD 7.46–7.47 excludes: third-party comparable services, R&D outside the qualifying IT category, manufacturing, raw-material purchasing, sales/marketing/distribution, financial transactions, natural-resource activities, insurance/reinsurance and corporate senior management outside supervision of qualifying services. An invoice's small size is not eligibility. [Decree §§ 6.1–6.3](https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html), incorporating [OECD paragraphs 7.45–7.49](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf#page=329).

Keep documentation, benefit justification and allocation keys. Apply 5% to relevant direct/indirect costs and overhead; exclude shareholder/sole-beneficiary costs from the shared pool and exclude pass-through costs from the markup. Costs solely for one recipient are charged to that recipient. Support category benefits generally; the fixed markup needs no benchmark. [Decree § 6.3](https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html), incorporating OECD paragraphs 7.54–7.65.

**4. Financing and IP.** First establish debt character, repayment capacity, terms, credit risk, implicit group support and both parties' alternatives; then price the loan on the facts. Do not use a universal interest percentage. For guarantees, cash pools, IP transfers, hard-to-value intangibles, royalties, contract research/manufacturing and business restructurings: non-usable specialist hold. Check this point with one of our partner accountants. [Decree §§ 3.3, 5–9](https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html).

**5. Apply mismatch restrictions before claiming a Dutch benefit.** Ordinary non-transparent, non-debt cases, assuming no exception:

- **Article 8bb:** allow a downward adjustment (higher costs/lower income than the agreed terms) only to the extent corresponding upward profit-tax inclusion at the related body is made plausible.
- **Article 8bc:** for a non-debt asset acquired from a related body, recognise a step-up from agreed to arm's length price only to the extent the taxpayer makes plausible the higher transfer price is included in the seller's profit tax.
- **Article 8bd:** for a non-debt asset received by contribution, distribution, capital repayment, liquidation or comparable act, if market value exceeds the transferor's profit-tax inclusion value, use the latter; the taxpayer must substantiate it. This is not automatically the historical accounting basis.

Keep contractual amounts, arm's length values and taxable inclusion evidence separately. Transparent/disregarded entities, debts, mergers/splits and historic transitions are held for their statutory exceptions. Check this point with one of our partner accountants. [Arts. 8ba–8bd][law1].

**6. Prepare the records.** Article 8b records cover the five comparability factors, method choice and pricing/terms support, proportionate to the transactions. Meeting article 29g's content also meets article 8b for cross-border transactions; the decree extends that approval to domestic transactions where the same content is prepared for them. Adapt group studies to Dutch facts; do not assume a missing commercial database study alone makes proportionate evidence inadequate. The master file describes the business, overall TP policy and worldwide income/activity allocation. The local file supports foreign related-entity transactions and arm's length permanent-establishment profit allocation; Dutch or English is permitted. Retain both in the administration, not merely after the deadline. [Art. 29g][law1]; [decree § 10.2](https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html).

Review current functions, risks and financial data annually as a workpaper control. Do not treat three years as an automatic Dutch benchmark safe harbour. For reliance on a three-year search-refresh interval, the ministerial model annexes C–F, or the effect of the 2026 international-tax decree on PE allocation: non-usable hold. Check this point with one of our partner accountants.

## Deadlines and filing

| Obligation | Deadline / action | Source |
|---|---|---|
| Article 8b records | Keep in the administration; no assumed 4–6 week statutory grace period | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 8b(3)) |
| Master/local files | In the administration by the actual corporate return deadline for that year; record any extension actually granted | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 29g(1)) |
| CbC notification | By the last day of the group's reporting year | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 29d) |
| Confidential CbC report | Within twelve months after the last day of the reporting year | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 29c) |
| Corporate return, ordinary calendar year / broken year | Before 1 June of next year / within five months after year-end; short years need their specific rule | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen |
| Calendar-year online extension | Request before 1 June for extension to 1 November; longer/non-calendar extension uses the reasoned paper form | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/uitstel_aangifte_vennootschapsbelasting |
| Public CbC | Deposit with the trade register and publish online within twelve months after year-end; accessible online for at least five consecutive years | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0049420/2024-06-22_0/xml/BWBR0049420_2024-06-22_0.xml (art. 11) |

**Confidential CbC local filing:** article 29c(2) applies where the parent has no filing obligation, or the parent state has an information-exchange agreement but no operative CbC competent-authority agreement with the Netherlands by twelve months after year-end, or the inspector has notified systematic failure. An eligible EU-designated group entity may report for the EU entities under article 29c(3). A surrogate report within the deadline relieves local filing only under article 29c(4); a non-EU surrogate additionally needs the reporting law, exchange agreement, absence of notified systematic failure and both notifications specified there. Do not assume any parent/surrogate filing suffices. Where local filing applies, request the parent information; if it is not obtained, notify the inspector and file all information held by the deadline. [Arts. 29c–29d][law1].

**Separate submission routes:** use the [CbC notification portal](https://gegevensportaal.belastingdienst.nl/cbc/faq/nl/) for notification; one entity may notify for all Dutch-resident entities of the same group. Identify the reporting entity/residence, submit, validate through the emailed link and retain the completion confirmation and covered-entity list. Send the actual CbC report electronically through **Digipoort**, using the current [Belastingdienst technical specifications](https://odb.belastingdienst.nl/); it is not the notification upload. Resolve rejected submissions. The report contains per-state financial/tax/personnel/assets aggregates and the entities' residences/activities. It is for risk assessment, not a basis for a TP adjustment. [Arts. 29e–29f][law1].

## Penalties and interest

Distinguish pricing corrections, documentation gaps and CbC failures; none automatically establishes the others.

| Failure | Consequence and conditions | Source |
|---|---|---|
| CbC report/notification not made, late, incomplete or wrong through intent/gross negligence | Article 29h identifies liable entities. Power expires five years after the obligation-calendar-year end. Maximum sixth category above; policy amount is set with the formal-law coordinator, subject to mitigation/aggravation | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml (art. 29h); https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0038145/2026-08-08_0/xml/BWBR0038145_2026-08-08_0.xml (§ 28h) |
| Article 8b records clearly inadequate | The explanatory memorandum describes a shift to the taxpayer to make arm's length pricing plausible by any means. This is distinct from reversed/heavier proof after a final information decision | https://zoek.officielebekendmakingen.nl/kst-28034-3.html (art. 8b explanation); https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml (arts. 25(3), 27e) |
| Required records/master/local files not kept | Ordinary records obligations/offences can apply, including AWR 68(1)(d). The inspector can issue an information decision for qualifying failures | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml (arts. 52a, 68) |
| Required return not made, or relevant information decision final | In objection/appeal, assessment stands unless the taxpayer demonstrates that/how far it is wrong; reversal does not extend to a vergrijpboete | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml (arts. 25(3), 27e) |
| Incorrect/incomplete return through intent, initial assessment | AWR 67d: maximum 100% of its statutory penalty base; gross negligence alone does not suffice | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml (art. 67d) |
| Too-low assessment through intent/gross negligence, additional assessment | AWR 67e: maximum 100% of its statutory penalty base. Ordinary policy starting points 50% / 25%; individual circumstances can alter them. The base is the tax attributable to the culpable shortfall, with the statutory loss-offset adjustments, not automatically the TP correction itself | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml (art. 67e); https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0038145/2026-08-08_0/xml/BWBR0038145_2026-08-08_0.xml (§§ 6–8, 25, 27) |

An information decision is open to objection. It lapses if the relevant assessment is set before it becomes final. Corporate tax is levied by assessment; do not use self-assessed-payment penalty provisions to calculate this corporate-tax correction. [AWR art. 52a][law2]; [Wet Vpb art. 24][law1].

**Criminal exposure:** non-usable hold for AWR 68–69 offences, imprisonment, tax-based fines and corporate higher-category/turnover rules. The CbC provision disapplies the usual too-little-tax condition. Do not quantify exposure from category amounts alone. Check this point with one of our partner accountants. [Wet Vpb art. 29h(3)][law1]; [AWR arts. 68–69][law2].

**Interest:** AWR 30fc generally begins six months after the tax period ends and ends the day **before** the assessment becomes collectable. No interest for an assessment matching a return received before the sixth month starts. A matching later return caps the end at nineteen weeks after receipt; a requested additional assessment caps it at twelve weeks after receipt. Keep assessment dates/rate periods and apply the exception/cap. For an unconfirmed future rate or disputed interest computation: non-usable hold. Check this point with one of our partner accountants. [AWR art. 30fc(1)–(5)][law2].

## Cross-border points

- **Amount B:** the Dutch decree does not introduce it for Dutch routine marketing/distribution activities. Recognition of a correct foreign application requires a covered jurisdiction implementing it in the relevant year and an applicable treaty; this also concerns PE allocation. Do not use an unconfirmed foreign classification/return; check the relevant year's implementation. [Bedrag B decree §§ 2–3](https://zoek.officielebekendmakingen.nl/stcrt-2024-38369.html).
- **Public CbC:** separate from confidential reporting. The ordinary Dutch-parent/standalone test above excludes wholly Dutch-only operations and qualifying banks/investment firms publishing the specified capital-requirements information. Revenue follows the applicable accounting definition in article 1(2). For non-EU/EEA parent subsidiaries/branches, parent-publication relief, withheld information or publication-format details: non-usable hold. Check this point with one of our partner accountants. [Public-report decree arts. 1–6, 11, 15][law3].
- **Advance certainty:** APA eligibility, economic nexus, avoidance/low-tax/sanctions exclusions, unilateral/bilateral/multilateral route, duration, rollback, fees, processing times, annual compliance and renewal are held for case-specific confirmation. No fee, time or entitlement promise is usable here. Check this point with one of our partner accountants.
- **ICAP:** participation, assurance versus binding advance certainty are held for specialist confirmation. Check this point with one of our partner accountants.
- **Disputes:** retain the assessment, reasoning, dates and objection/MAP/EU-route documents; no suspension or deadline is assumed from informal talks. Eligibility, time limits and procedure remain non-usable holds. Check this point with one of our partner accountants.

## Two worked examples that recompute

### Example 1: low-value services recharge

A Dutch shared-service company provides payroll processing and IT helpdesk support. Eligible costs allocated to one recipient are EUR 200,000 after exclusions; assume all eligibility, benefit, documentation and allocation conditions above are met and there are no pass-through costs in that base. Markup = EUR 10,000; charge = EUR 210,000. Core manufacturing or product development does not qualify merely because the arithmetic works. [Decree § 6.3](https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html).

```oa-check
name: NL low-value services, cost base EUR 200,000 at 5% markup (2026)
inputs:
  eligible_costs: 200000
steps:
  - markup: eligible_costs * 0.05
  - charge: eligible_costs + markup
expected:
  markup: 10000.00
  charge: 210000.00
```

### Example 2: TP correction, reversed proof and a separately established fine

Calendar year 2026. Facts: Dutch distributor; preceding-year group revenue EUR 80,000,000; taxable amount EUR 1,000,000; local file missing by the actual return deadline; unanswered information request; relevant information decision final; additional-assessment TP correction EUR 300,000. Assume multinational-group scope, a legally sustainable additional assessment, no loss offsets or other tax adjustments, and that the whole extra tax is attributable to any culpability separately proved. The final information decision produces the heavier proof rule for the assessment, not for the fine. [Wet Vpb arts. 22, 29g][law1]; [AWR arts. 25(3), 27e, 67e][law2].

Tax before = EUR 244,400; after = EUR 321,800; extra = EUR 77,400. At the ordinary starting points, proven gross negligence gives EUR 19,350 and proven intent EUR 38,700; statutory maximum EUR 77,400 on these assumptions. These are alternative calculations before individual mitigation/aggravation, not fines automatically due. [BBBB §§ 6–8, 25, 27][law4].

```oa-check
name: NL TP correction of EUR 300,000 and vergrijpboete (2026)
inputs:
  taxable_before: 1000000
  correction: 300000
steps:
  - tax_before: min(taxable_before, 200000) * 0.19 + max(taxable_before - 200000, 0) * 0.258
  - taxable_after: taxable_before + correction
  - tax_after: min(taxable_after, 200000) * 0.19 + max(taxable_after - 200000, 0) * 0.258
  - extra_tax: tax_after - tax_before
  - fine_gross_negligence: extra_tax * 0.25
  - fine_intent: extra_tax * 0.50
  - fine_legal_max: extra_tax * 1.00
expected:
  tax_before: 244400.00
  extra_tax: 77400.00
  fine_gross_negligence: 19350.00
  fine_intent: 38700.00
  fine_legal_max: 77400.00
```

For that same calendar 2026 period, the ordinary interest start is 1 July 2027, subject to article 30fc's exceptions/caps. **The original 5% future-period assumption is held: do not calculate interest from it.** Check this point with one of our partner accountants. Alternative group revenue EUR 750,000,000: a Dutch parent's culpable CbC failure can separately attract article 29h, subject to offence-date/liability conditions. [AWR art. 30fc][law2]; [Wet Vpb art. 29h][law1].

Historical hypothetical cases, assuming ordinary rules and no exception:

- **A:** exactly EUR 50,000,000 preceding-year consolidated revenue meets article 29g; a current-year fall does not reverse it.
- **B:** calendar reporting year ending 31 December 2026: notification by 31 December 2026; required confidential report by 31 December 2027. [Arts. 29c–29g][law1].
- **C:** non-debt asset acquisition: agreed EUR 100,000; arm's length EUR 140,000; seller's included price only EUR 100,000. The EUR 40,000 step-up is denied; starting value EUR 100,000. [Art. 8bc(1)][law1].
- **D:** contractual service cost EUR 80,000; arm's length cost EUR 100,000; proposed extra deduction EUR 20,000; proven corresponding upward inclusion only EUR 12,000. Additional downward adjustment allowed EUR 12,000; cost EUR 92,000 before other restrictions; EUR 8,000 denied. [Art. 8bb][law1].
- **E:** EUR 200,000 eligible services at 5% = EUR 210,000; this is Example 1, with the same original inputs.
- **F:** non-debt asset contribution: market value EUR 140,000; proven transferor profit-tax inclusion value EUR 100,000; no exception. Starting value EUR 100,000; EUR 40,000 is not recognised. [Art. 8bd(1)][law1].
- **G:** Dutch ultimate-parent group revenue exactly EUR 750,000,000 in the preceding year meets confidential CbC. Exactly that amount on both balance-sheet dates does not meet the ordinary public test; check any separate subsidiary/branch route. [Art. 29c(5)][law1]; [public-report art. 2][law3].

## Ask the client first

- Obtain entity/PE, residence, years, ownership/control, consolidation perimeter and preceding-year revenue, including size/materiality exclusions.
- Obtain contracts, invoices, ledger/segmented accounts, functional interviews, decisions, financing terms and actual-conduct evidence for each transaction type.
- For downward adjustments/basis changes, obtain taxable inclusion evidence; identify transparent/disregarded bodies and exemptions.
- Obtain pricing records, master/local files, financial updates, CbC reporter/residence and exchange status, accepted filings/confirmations, rulings, actual deadlines/extensions and dated inspector letters.
- Reconcile adjustments to ledger/tax workpapers; keep allocation keys, exclusions and loss explanations. Confirm notification, report acceptance and entity coverage separately; escalate holds before acting.

## Sources

| Source and bounded scope read | URL | Read on |
|---|---|---|
| Wet Vpb, arts. 8b–8bd, 29b–29h; official 2026 XML. Arts. 22 rates and 24 assessment basis | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml | 2026-11-27 (listed articles; art. 22 completed proof reused and XML confirmed) |
| AWR, arts. 25, 27e, 30fc, 52a, 67d–67e, 68–69 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml | 2026-11-27 (listed clauses) |
| BBBB §§ 6–8, 25–27, 28h; November amendment changes other paragraphs | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0038145/2026-08-08_0/xml/BWBR0038145_2026-08-08_0.xml; https://zoek.officielebekendmakingen.nl/stcrt-2026-40596.html | 2026-11-27 (listed clauses and amendment scope) |
| Fine-category amounts and commencement, arts. I–II; not a determination of criminal exposure | https://zoek.officielebekendmakingen.nl/stb-2025-401.html | 2026-11-27 (operative amounts/date) |
| Transfer-pricing decree §§ 2–3, 5.1, 6.1–6.3, 9.1, 10.2 | https://zoek.officielebekendmakingen.nl/stcrt-2022-16685.html | 2026-11-27 (listed sections) |
| Article 8b explanatory memorandum, documentation/proof paragraph | https://zoek.officielebekendmakingen.nl/kst-28034-3.html | 2026-11-27 (article 8b explanation) |
| Public CbC arts. 1–6, 11–12, 15; operative threshold, exceptions and deadlines | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0049420/2024-06-22_0/xml/BWBR0049420_2024-06-22_0.xml; https://zoek.officielebekendmakingen.nl/stb-2024-43.html | 2026-11-27 (listed provisions) |
| Amount B decree §§ 2–4 | https://zoek.officielebekendmakingen.nl/stcrt-2024-38369.html | 2026-11-27 (domestic exclusion and foreign-recognition conditions) |
| Corporate-return filing dates and extensions, completed matching proof reused | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/uitstel_aangifte_vennootschapsbelasting | 2026-11-23 (completed read reused) |
| Belastingdienst, corporate-tax interest table | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-11-27 (corporate-tax rows) |
| Belastingdienst CbC FAQ, scope, reporting route, validation and confirmation | https://gegevensportaal.belastingdienst.nl/cbc/faq/nl/ | 2026-11-27 (named questions) |
| OECD Guidelines, paragraphs 7.45–7.49, 7.54–7.62; 5.37–5.38 read only to reject an automatic three-year safe harbour | https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf | 2026-11-27 (named paragraphs) |

Not yet confirmed: no usable conclusion is supplied for the explicit specialist holds above: future interest rates, criminal exposure, APA/ICAP, dispute procedures, benchmark-refresh reliance, ministerial model detail, PE-allocation policy changes, specialist mismatch cases and public-CbC subsidiary/branch/relief/format cases. Check this point with one of our partner accountants.

[law1]: https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml
[law2]: https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml
[law3]: https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0049420/2024-06-22_0/xml/BWBR0049420_2024-06-22_0.xml
[law4]: https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0038145/2026-08-08_0/xml/BWBR0038145_2026-08-08_0.xml
