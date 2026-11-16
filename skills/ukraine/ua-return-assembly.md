---
name: ua-return-assembly
description: "Final orchestrator that assembles the complete Ukrainian ФОП (FOP) filing package for a Ukraine-resident sole proprietor: consumes the Ukraine content-skill outputs and produces one unified reviewer package with the correct declaration, schedules, filing-and-payment calendar, and pre-filing checklist. Computes nothing itself."
version: 0.2
jurisdiction: UA
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - ua-freelance-intake
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Ukraine FOP return assembly

**2026 review, read 15 November 2026.** Run this router **last**, after `ua-freelance-intake` and the applicable content skills. It selects forms, reconciles their outputs and builds a reviewer package; it does not calculate tax or authorize filing. This covers a confirmed Ukraine-resident individual FOP, ordinary Groups 1/2/3 or the general system. TOV/company, Group 4 farming, e-resident, disputed residence, tax-agent special cases and unresolved regime changes require specialist routing rather than a default answer.

## Start here: intake and required outputs

Reuse the validated intake scope. Do not re-ask FOP versus TOV, regime, group, VAT status or residence without a new conflict. A conflict is a reason to stop and repair the package, not to silently trust inconsistent numbers. Obtain the effective dates of registration, each regime/group change, VAT entry/exit and closure, plus the income/expense period, approved KVED codes, bank/PSP records, receipt-date NBU FX conversions and cap/barred-activity flags. The regime is exclusive for an effective subperiod; **both declarations can be needed in a year containing a transition**. [Tax Code 177.5.2](https://tax.gov.ua/nk/).

| Consume from | Required package, not a fresh tax computation here |
| --- | --- |
| `ua-freelance-intake` | Validated FOP/residence/regime timeline, group, VAT evidence, KVED, receipt ledger, exceptions and unresolved flags |
| `ua-single-tax` | Group/period/rate and cumulative single tax, affected income/excess and military levy separately; ordinary Group 3 rates **3% with separate VAT / 5% with VAT included in single tax**, ordinary Group 3 levy **1% of article 292 income**. Groups 1/2 have separate fixed levy obligations, not a levy included in single tax. E-resident/special relief requires its own route [293.3; XX.10.16-1](https://tax.gov.ua/nk/) |
| `ua-income-tax` | General-system net taxable business income, ordinary **18% PIT / 5% levy**, other declarable income, documented advances/credits and unresolved costs; do not copy a rate without its upstream eligibility [167.1,177; XX.10.16-1](https://tax.gov.ua/nk/) |
| `ua-social-contributions` | Own ЄСВ by month and quarter, base/minimum/maximum and payments; ordinary **22%** rate is only an upstream input. Record pension/disability, employer-paid-month, mobilization and other relief evidence. A main-job label alone is not exemption evidence; current employer-paid minimum test is monthly [DPS figures](https://tax.gov.ua/media-tsentr/novini/999526.html); [current employer-paid test](https://zir.tax.gov.ua/main/bz/view/?id=43912&src=ques) |
| `ukraine-vat` | Registered VAT return boxes, period, net payable/refundable and registration dates, separately reconciled to turnover. A nonregistered FOP's possible nonresident-service VAT obligation is a separate unresolved route, not proof that no VAT filing can ever arise [VAT 202-203](https://tax.gov.ua/nk/) |
| Tax-agent/payroll package if applicable | Accrued individual income, withholding and employer ЄСВ, reporting months and accepted prior reports. It is separate from own ЄСВ [176.2](https://tax.gov.ua/nk/) |

**Missing required output, conflicting residence/regime evidence, unexplained receipt difference or unverified relief: stop assembly and route back to its owner.** A blank is not a zero. Do not recompute tax from headline rates to fill the gap.

## The method, step by step

### Select the declaration and schedules

**Voluntary general-system closure is a separate final route:** 177.11 requires a final declaration reporting business income only, on the monthly-period filing deadline; the last base period ends on the last day of the closure month. Do not use the ordinary annual row for this return. Route its concrete final calendar, schedules and other personal-income obligations for separate review. [177.11](https://tax.gov.ua/nk/).

| Route | Declaration and schedules | Conditions that stay with it |
| --- | --- | --- |
| Ordinary Group 1/2 | **Декларація платника єдиного податку**, Order **578**, ordinary annual reporting; own **Додаток 1** where required | Annual treatment assumes no excess, upward group change or departure requiring quarterly reporting under **296.5.1**. The own-contribution schedule follows ЄСВ liability/reporting, not simply whether cash was paid. Check exemptions, closure and other special triggers [DPS forms instructions](https://rv.tax.gov.ua/media-ark/news-ark/print-972360.html) |
| Ordinary Group 3 FOP | Same declaration, quarterly **cumulative within the year**; own **Додаток 1 normally with the fourth-quarter/year return** | Do not attach the annual own-ЄСВ schedule as a universal quarterly obligation. E-residents excluded from this ordinary 296.3 route; special/closure schedules require current instructions. Separate VAT return for an eligible **3%** payer [296.3,296.7](https://tax.gov.ua/nk/); [DPS forms](https://rv.tax.gov.ua/media-ark/news-ark/print-972360.html) |
| General-system FOP | **Декларація про майновий стан і доходи**, Order **859**, annual; business-income **Ф2**, own **ЄСВ 1** where required, and other applicable income schedules | **Own ЄСВ is not the employer quarterly combined report.** Include other domestic/foreign income under 177.11. Annual reporting can apply to a year with a regime transition [DPS general-system guidance](https://kh.tax.gov.ua/media-ark/news-ark/print-982973.html); [own ЄСВ guidance](https://ck.tax.gov.ua/media-ark/news-ark/print-976727.html); [177.5.2](https://tax.gov.ua/nk/) |
| Registered ordinary VAT payer | **Податкова декларація з ПДВ**, separate monthly cycle | Registration/annulment can make first/last periods nonstandard under **202.1**. Do not fold VAT into the single-tax/income return or treat Group 1 as automatically eligible for separate VAT [202-203](https://tax.gov.ua/nk/) |
| FOP/self-employed tax agent | **Податковий розрахунок** for PIT, levy and employer ЄСВ, quarterly from **1 January 2026**, with month-by-month breakdown | Trigger is **accrual of the stated individual income**, including accrued unpaid wages, not only cash payment. Other tax agents, including ordinary legal entities, remain monthly. This does not replace annual own-ЄСВ schedules [176.2](https://tax.gov.ua/nk/); [DPS 2026 change](https://tax.gov.ua/media-tsentr/novini/984181.html) |

**Agricultural-land flag:** article 297-1.1 requires an annual minimum-tax-obligation appendix for the specified single-tax owners, lessees/other users (including emphyteusis) of agricultural land and heads of family farms, including qualifying family-member land used by the farm. For the single-tax return this is **Додаток 2**, distinct from own-ЄСВ Додаток 1. Separately, general-system **177.14** requires an annual minimum-tax appendix for the specified registered FOP agricultural-land owners, lessees/other users producing their own agricultural products, and qualifying family-farm heads including member land used by that farm. Route those general-system cases too; do not label their appendix as the single-tax Додаток 2. [General-system 177.14](https://tax.gov.ua/nk/). Route the computation to an agricultural specialist; do not silently omit the appendix. [DPS complete form/land conditions](https://rv.tax.gov.ua/media-ark/news-ark/print-972360.html).

**No-activity and closure exceptions:** zero receipts do not by themselves prove no return. General-system FOP with no business activity/income but other domestic/foreign income files the property/income return and **Ф2 with blank columns** in the cited explanation; with neither business activity/income nor other income, that explanation says no declaration/Ф2 obligation. Where a declaration is required from other grounds but no business income arose, the separate own-ЄСВ explanation says **ЄСВ 1 is not attached** in its stated nonclosure case. Do not conflate blank Ф2 and omitted ЄСВ 1. [18 February 2026 DPS](https://kh.tax.gov.ua/media-ark/news-ark/print-982973.html); [29 January 2026 DPS](https://ck.tax.gov.ua/media-ark/news-ark/print-976727.html).

For Group 3, the cited explanation allows no interim return where no income or other declarable objects arose in the first quarter/half-year/three quarters; earlier-year income must still appear cumulatively in the annual return without being taxed twice. Its closure nonfiling conclusion also requires no declarable indicators, the specified pension/disability/age-and-pension-or-social-assistance ЄСВ exemption and no minimum-tax obligation. Closure does not extinguish prior liabilities. Other closure, employee-paid or mobilization scenarios are not automatically covered by that conclusion. [7 September 2026 DPS, full conditions](https://ck.tax.gov.ua/media-ark/news-ark/print-1047346.html).

## Filing and payment calendar: separate period, obligation and due date

**The 2025-2026 filing cycle is not the same as the 2026 tax year.** The March/April/May 2026 annual dates below concern **2025** income. Record the tax period on every action. Filing and payment have separate weekend rules: **49.20** for filing, **57.1** for tax payment; own ЄСВ uses its contribution rule and Instruction **449**. Do not shift all dates by one generic rule or measure payment time from the actual day you choose to file. [Tax Code](https://tax.gov.ua/nk/); [own ЄСВ timing](https://zak.tax.gov.ua/media-ark/news-ark/981527.html).

| Obligation | Verified rule and dated example | Source |
| --- | --- | --- |
| Ordinary Group 1/2 annual single-tax return | **60 calendar days** after year-end, subject to quarterly exceptions above; **2025 return: 2 March 2026**, following weekend adjustment | [49.18.3](https://tax.gov.ua/nk/); [official dated reminder](https://if.tax.gov.ua/media-ark/news-ark/print-986361.html) |
| Group 3 cumulative return | **40 calendar days** after quarter-end; **Q1 2026: 11 May 2026**; **half-year: 10 August 2026**; **three quarters: 9 November 2026** | [May calendar](https://mk.tax.gov.ua/media-ark/news-ark/print-1006435.html); [August calendar](https://tr.tax.gov.ua/media-ark/news-ark/print-1038154.html); [October reminder](https://ck.tax.gov.ua/media-ark/local-news/print-1062092.html) |
| Group 3 single tax and separate levy | **10 calendar days after the statutory declaration deadline**, not ten days after actual submission. **Q1 2026 payment: 20 May 2026** even though filing shifted to 11 May. Do not infer 21 May. **Q2 2026 payment: 19 August 2026**, correcting the old 20 August date; the unshifted 40-day point is 9 August and the payment period ends 10 days later. Obtain the applicable official payment calendar for every remaining quarter | [295.3,XX.10.16-1](https://tax.gov.ua/nk/); [official May calendar](https://mk.tax.gov.ua/media-ark/news-ark/print-1006435.html); [official August payment calendar](https://tr.tax.gov.ua/media-ark/news-ark/print-1041192.html) |
| Groups 1/2 single tax and separate military levy | Ordinary monthly advance **no later than the 20th of the current month**, subject to independently verified relief and applicable payment-day rules. Separate liabilities/records, not a combined tax | [295.1; XX.10.16-1](https://tax.gov.ua/nk/); [May calendar](https://mk.tax.gov.ua/media-ark/news-ark/print-1006435.html) |
| General-system annual income return | **Before 1 May** of following year, subject to special cases/calendar rule. **2025 return: 30 April 2026**, not an instruction to file on 1 May | [49.18.4,177.5](https://tax.gov.ua/nk/); [2026 DPS explanation](https://kh.tax.gov.ua/media-ark/news-ark/print-982973.html) |
| General-system annual PIT and levy balance | Reconcile documented advances separately. **2025 business balance: 11 May 2026** in the official calendar under 57/177, correcting the old unadjusted 10 May. Do not substitute the ordinary individual's before-1-August rule for this FOP business balance | [57.1,177.5.3](https://tax.gov.ua/nk/); [official May calendar](https://mk.tax.gov.ua/media-ark/news-ark/print-1006435.html) |
| General-system PIT advances | Ordinary 177.5.1: **before the 20th** after the first, second and third quarters; **no fourth-quarter advance**, and no advance when that quarter's computed result is negative. Retail-fuel businesses have separate 177.5.1-1 rules and require specialist routing. Import amounts and applicable calendar dates from the content owner | [177.5.1-177.5.3](https://tax.gov.ua/nk/) |
| Own ЄСВ payment | Ordinary quarterly rule **before the 20th**, normally the **19th inclusive**, with next-working-day adjustment under Instruction 449. **Q1 2026: 20 April 2026** officially confirmed; **Q3: 19 October 2026** officially confirmed. Payment frequency does not determine annual schedule frequency | [general rule](https://zak.tax.gov.ua/media-ark/news-ark/981527.html); [April calendar](https://if.tax.gov.ua/media-ark/news-ark/print-1000911.html); [October deadline](https://ck.tax.gov.ua/media-ark/news-ark/print-1058715.html) |
| Tax-agent combined report | For FOP/self-employed tax agents, quarterly **40 calendar days**, month breakdown; **Q1 2026: 11 May 2026**, half-year report **10 August 2026**. Ordinary other tax agents' monthly cycle is **20 days**. Tax withholding/payment dates remain separate | [176.2](https://tax.gov.ua/nk/); [DPS change](https://tax.gov.ua/media-tsentr/novini/984181.html); [August calendar](https://tr.tax.gov.ua/media-ark/news-ark/print-1038154.html) |
| Ordinary registered VAT return/payment | File within **20 calendar days** after reporting month; pay within **10 calendar days** after the statutory 203.1 deadline, applying the relevant payment calendar. Not always the 30th; first/last registration periods differ. Special VAT routes remain outside this ordinary line | [202.1,203.1-203.2,49.20,57.1](https://tax.gov.ua/nk/) |

**Retained planning dates, not a verified future filing calendar:** the old Q4/2026 Group 3 date **9 February 2027** is the derived 40-day result from 31 December 2026; the old **19 February 2027** payment is the derived further 10-day result. The old Q2/2026 payment **20 August 2026** is corrected to the verified **19 August 2026** above. The Q3 payment **19 November 2026** is derived from the statutory periods; its separate official payment-calendar entry has not been opened here. Own ЄСВ **20 July 2026** is derived from 19 July being Sunday and the next-working-day rule; **19 January 2027** is the derived ordinary Q4 date. These items stay **Not yet confirmed for filing** until the accountant binds the applicable official calendar and any special extension to the package. Do not present the earlier approximate `~20/~19` dates as verified. Final 2026 annual forms and 2027 dates are not established by an older 2025 filing example.

## Submission through Електронний кабінет and electronic signature

This workflow uses [Електронний кабінет](https://cabinet.tax.gov.ua). It does not assert every FOP return can only be electronic: **49.3** allows personal/representative, prescribed postal or electronic routes unless a special rule applies; VAT returns are electronic under **49.4**. Current approved format/signature rules still apply. [Tax Code 48.5,49.3-49.5](https://tax.gov.ua/nk/).

1. Confirm taxpayer, reporting period, tax office, return type and effective regime; validate **КЕП** and signing authority. The cited Cabinet instructions use КЕП for private access. Order **557** also describes a qualified or qualifying advanced signature based on a qualified certificate; a seal applies **if present**. Do not treat an expired certificate as acceptable. [Cabinet instructions](https://rv.tax.gov.ua/media-ark/news-ark/print-972360.html); [Order 557 explained](https://cv.tax.gov.ua/media-ark/news-ark/print-1040075.html).
2. Use **«Введення звітності»**, select year/period, **«Створити»**, relevant form and **«Код ДПІ»**. The official January 2026 single-tax instructions use **«F01 Прибуток»**, annual **F0103407** or Group 3 quarterly **F0103309**. Their own-ЄСВ appendices are **F0134107/F0133109**, agricultural minimum-tax appendices **F0134207/F0133209** respectively. These are the dated published identifiers, not a promise that the final 2026/2027 schema is unchanged. [Official instructions](https://rv.tax.gov.ua/media-ark/news-ark/print-972360.html).
3. Select the relevant single-tax or property/income return, required **Додаток 1** or **ЄСВ 1/Ф2**, payroll combined report and separate VAT form as applicable. Confirm actual schedule obligations, not just whether a payment was made. The PIT forms portal labels its main form **introduced 1 January 2026**, and lists ЄСВ 1 and Ф2; only the portal metadata was read, not all downloadable form cells. The old **6 February 2026** effective-date claim remains unconfirmed. [Official PIT forms portal](https://tax.gov.ua/zakonodavstvo/elektronni-formi-dokumentiv/podatok-na-dohodi-fizichnih-osib/).
4. Check required fields, signature sequence and signing rights, sign and send in the current accepted format. File early enough to resolve errors; do not infer acceptance from a local successful-send message. [Order 557 explanation](https://cv.tax.gov.ua/media-ark/news-ark/print-1040075.html).
5. Retain **Квитанція №1**: automatic-check result, ordinarily within **2 hours** of receipt or the first **2 hours** of the next operating day in the specified case. A negative first result gives nonacceptance reasons and no second receipt; absent first receipt within the specified period, Order 557 treats the document as not received. **Квитанція №2** normally follows no later than the next working day after the first, unless another rule applies; it confirms acceptance/registration or rejection. Resolve rejection and send the correct replacement before the deadline where possible. [Order 557, II.8-II.10](https://cv.tax.gov.ua/media-ark/news-ark/print-1040075.html).
6. Obtain positive **Квитанція №2 «Прийнято»** for each return/schedule package and retain both receipts, submitted file, registration number and timestamps. **With a positive second receipt, the accepted timestamp is the first receipt's timestamp.** Correctly formed, accepted last predeadline submission is the original where several copies were sent; distinguish **«звітний новий»** before deadline from later correction procedures. Missing second receipt requires investigation, not an unconditional legal conclusion that the return was never filed: **49.9.2** also has deemed-acceptance rules, **conditional on compliance with articles 48 and 49**, where the authority fails to give a timely refusal. Electronic/posted refusal generally has **5 working days** under 49.11.1, distinct from the ordinary second-receipt timing. Escalate evidence and any appeal/correction rather than inventing acceptance. [Current receipt guidance](https://dp.tax.gov.ua/media-ark/news-ark/print-1054979.html); [49.9-49.16](https://tax.gov.ua/nk/).
7. Pay each verified balance separately by its payment deadline; check actual budget-credit records and account details, retain payment evidence and reconcile arrears/overpayments. Filing or acceptance does not prove payment. Keep source figures and returns provisional until qualified Ukrainian accountant review.

**Provider names retained as pointers only:** Вчасно, M.E.Doc, Соната and Taxer appeared in the old workflow. Their current service, accreditation, tariffs and schema support were not opened or confirmed here; no official endorsement or paid-provider requirement is asserted. Use the official Cabinet route above unless the reviewer verifies a chosen provider.

## Worked reconciliation cases: no tax calculated here

**Case A, cumulative return without paying twice.** Hypothetical upstream approved package for an ordinary Group 3 non-VAT FOP: Q1 cumulative single tax 15,000 and levy 3,000; half-year cumulative single tax 40,000 and levy 8,000. The quarter-only increments are 25,000 and 5,000, total 30,000. Actual previous declarations/payments and credits must be checked before a payment instruction. Carry annual own-ЄСВ detail to the correct year/Q4 schedule rather than adding it to the ordinary half-year tax-agent report. These supplied liabilities do not infer a tax rate or create an exemption.

```oa-check
name: Cumulative amounts are not a second full payment
inputs:
  q1_single_tax: 15000
  q1_levy: 3000
  half_year_single_tax: 40000
  half_year_levy: 8000
steps:
  current_single_tax_increment: half_year_single_tax - q1_single_tax
  current_levy_increment: half_year_levy - q1_levy
  current_increment_total: current_single_tax_increment + current_levy_increment
expected:
  current_single_tax_increment: 25000
  current_levy_increment: 5000
  current_increment_total: 30000
```

**Case B, failed reconciliation blocks filing.** Hypothetical received bank/PSP total 1,000,000 contains 50,000 documented nontaxable transfers already classified by intake and 950,000 taxable receipts. The single-tax owner instead supplies a 940,000 base: difference 10,000, so stop and repair that output. Do not fabricate a tax top-up. Separately the supplied approved annual PIT liability 36,000 less documented PIT advances 30,000 leaves a 6,000 PIT balance; the supplied levy liability 10,000 less its own advances 8,000 leaves 2,000, combined payment-list balance 8,000. These are imported liabilities from the appropriate separately dated regime subperiod, not two competing taxes on one base or an unrestricted cross-tax offset. Amounts, dates and registration changes need review before release.

```oa-check
name: Receipt mismatch and separate payment credits
inputs:
  bank_psp_receipts: 1000000
  classified_nontaxable_transfers: 50000
  owner_taxable_receipts: 940000
  annual_pit: 36000
  pit_advances: 30000
  annual_levy: 10000
  levy_advances: 8000
steps:
  classified_taxable_receipts: bank_psp_receipts - classified_nontaxable_transfers
  unresolved_difference: classified_taxable_receipts - owner_taxable_receipts
  pit_balance: annual_pit - pit_advances
  levy_balance: annual_levy - levy_advances
  payment_list_total: pit_balance + levy_balance
expected:
  classified_taxable_receipts: 950000
  unresolved_difference: 10000
  pit_balance: 6000
  levy_balance: 2000
  payment_list_total: 8000
```

## Final pre-filing checklist and reviewer deliverable

- [ ] Intake confirms FOP, residence and effective regime/group/VAT timeline; investigate only new conflicts. No blanket whole-year either/or where a transition occurred.
- [ ] Correct declaration and all required schedules selected for each effective subperiod; no general-system own-ЄСВ routed into the employer return.
- [ ] All applicable single-tax **or** general-income outputs per subperiod, own ЄСВ, VAT and tax-agent outputs present; missing owner output stops assembly.
- [ ] Receipt-date NBU FX values and receipt classifications reconcile to bank/PSP records; every difference has a documented owner resolution.
- [ ] Barred-activity screen includes excisable goods, FX exchange, financial services, gambling and mineral extraction, with actual article 291 exceptions; cap breaches are routed, not assumed absent.
- [ ] Own ЄСВ reviewed by **month and quarter**, with evidence for pension/disability, employer-paid-month, mobilization or other applicable relief; use a current deadline even if a sibling's calendar differs.
- [ ] Correct own-ЄСВ schedule attached when legally required, including unpaid liabilities; do not use a cash-paid-only trigger. Ф2/ЄСВ1 no-activity and closure distinctions checked.
- [ ] Single tax, PIT and **separate** levy agree to the correct group/period; cumulative liabilities and previously declared/paid sums not counted twice.
- [ ] Tax-agent quarterly combined report prepared for the actual accrued-income trigger, including unpaid accruals; other agents' monthly route not applied automatically to FOPs.
- [ ] VAT boxes/turnover/net payment or refund agree; registration dates and separate VAT/reverse-charge specialist flags resolved.
- [ ] Filing and payment action list has period, concrete confirmed date, separate amount, account, owner and source; derived/unconfirmed dates are blocked from release.
- [ ] Valid signature/certificate, authorized signer and Cabinet access confirmed; form/schema/date/tax office and appendix indicators checked.
- [ ] Submitted files and both receipts saved; positive acceptance, first-receipt timestamp and payment evidence reconciled. Missing/rejected receipts escalated with statutory exceptions preserved.
- [ ] Qualified Ukrainian accountant has reviewed and signed off **before filing**. Supply a single package: scope timeline, every content output/version, declaration/schedules, reconciliation, dated action list, unresolved items and subsequent filing/payment evidence.

## When to refuse or refer

The following unresolved branches block release of the affected return; send them to the qualified Ukrainian accountant or the content owner.

### Not yet confirmed: stop boundaries

- Exact future annual 2026 forms/schema/codes, 2027 official calendar, special extensions and the retained derived dates above; do not back-date a future form verification.
- Old claim of a PIT form effective **6 February 2026**; portal metadata instead labels the listed form introduced **1 January 2026**, without a full downloadable-form review here.
- Chosen private provider status/support, unusual electronic rejection/deemed-acceptance facts, postdeadline corrections/appeals, closure schedules beyond the cited case, employer/mobilization/territory relief not fully evidenced upstream.
- Residence conflict, company/farm/e-resident or special tax-agent route, unverified VAT nonresident-service obligation, actual tax/expense eligibility, current account details or any unexplained bank/return difference. Never turn a missing figure into zero or narrow a client's requested work to hide it.

## Sources

All read **2026-11-15**, official material. The consolidated Code was read for the listed operative provisions and neighboring exceptions, not its whole 26,507-line text. Main-form portal metadata is not a claim to have read every XLS cell.

| Official source | Actual scope | Read date |
| --- | --- | --- |
| [Tax Code, consolidated DPS publication](https://tax.gov.ua/nk/) | Read for 48.5,49.1-49.5,49.8-49.20,57.1,167.1,176.2,177.5.1-177.5.3/transition,177.10-177.14/closure and agricultural neighbors,202-203,291-296/298 ordinary route and XX.10.16-1 levy provisions; no general filing relief inferred| 2026-11-15 |
| [Single-tax forms and Cabinet instructions](https://rv.tax.gov.ua/media-ark/news-ark/print-972360.html) | Read for Full operative text: annual/quarterly exceptions, e-residents, annual own ЄСВ, agricultural appendix, dated identifiers and Cabinet steps| 2026-11-15 |
| [General FOP no-activity return](https://kh.tax.gov.ua/media-ark/news-ark/print-982973.html) | Read for Full explanation: other income, blank Ф2 versus no declaration/Ф2| 2026-11-15 |
| [Own ЄСВ1 with annual income return](https://ck.tax.gov.ua/media-ark/news-ark/print-976727.html) | Read for Full nonclosure explanation, zero-profit contribution choice, Order859 and no-business-income schedule exception| 2026-11-15 |
| [Single-tax closure/no indicators](https://ck.tax.gov.ua/media-ark/news-ark/print-1047346.html) | Read for Full explanation, cumulative interim/annual reporting, land, specific exemption and surviving liabilities| 2026-11-15 |
| [2026 tax-agent frequency change](https://tax.gov.ua/media-tsentr/novini/984181.html) | Read for Full operative body: quarterly/month breakdown, other agents monthly, Q1 date, then-pending form not treated as current schema approval| 2026-11-15 |
| [May 2026 official calendar](https://mk.tax.gov.ua/media-ark/news-ark/print-1006435.html) | Read for Full operative calendar, especially FOP annual balance 11 May, Group3 filing11/payment20 May and separate liabilities| 2026-11-15 |
| [2025 Group1/2 return reminder](https://if.tax.gov.ua/media-ark/news-ark/print-986361.html) | Read for Full text: 2 March2026 and weekend adjustment| 2026-11-15 |
| [August payment calendar](https://tr.tax.gov.ua/media-ark/news-ark/print-1041192.html) | Read for the full operative calendar: Group3 FOP/legal-person single tax and levy payment19 August2026, distinct from filing shift | 2026-11-15 |
| [August filing calendar](https://tr.tax.gov.ua/media-ark/news-ark/print-1038154.html) | Read for Full text: half-year Group3/FOP-agent reports due10 August2026| 2026-11-15 |
| [Three-quarter filing reminder](https://ck.tax.gov.ua/media-ark/local-news/print-1062092.html) | Read for Full text:9 November2026, register/records/payments/signature/receipt checks| 2026-11-15 |
| [Own ЄСВ payment rule](https://zak.tax.gov.ua/media-ark/news-ark/981527.html) | Read for Ordinary before20/19inclusive and Instruction449 next-working-day rule| 2026-11-15 |
| [April payment calendar](https://if.tax.gov.ua/media-ark/news-ark/print-1000911.html) | Read for Full text: own-ЄСВ Q1 due20 April2026, distinct employer report| 2026-11-15 |
| [October own ЄСВ date](https://ck.tax.gov.ua/media-ark/news-ark/print-1058715.html) | Read for Full operative text: Q3 deadline19 October2026| 2026-11-15 |
| [Order557 electronic receipt procedure](https://cv.tax.gov.ua/media-ark/news-ark/print-1040075.html) | Read for Full text: signatures/seal/automatic checks, first/second receipts, timings, negative/no-first receipt, accepted first timestamp and last accepted copy| 2026-11-15 |
| [Receipt acceptance date and replacement](https://dp.tax.gov.ua/media-ark/news-ark/print-1054979.html) | Read for Full text: second acceptance binds first timestamp; predeadline звітний новий| 2026-11-15 |
| [PIT forms portal](https://tax.gov.ua/zakonodavstvo/elektronni-formi-dokumentiv/podatok-na-dohodi-fizichnih-osib/) | Read for Operative listing only: main form introduced1 January2026, ЄСВ1 and Ф2 titles; no XLS-cell/schema review claimed| 2026-11-15 |
| [National 2026 ЄСВ figures](https://tax.gov.ua/media-tsentr/novini/999526.html) | Read for Ordinary22% and minimum/maximum background for upstream output| 2026-11-15 |
| [Current employer-paid ЄСВ answer](https://zir.tax.gov.ua/main/bz/view/?id=43912&src=ques) | Read for Full current answer: monthly employer-paid minimum threshold; not main-job-label-only| 2026-11-15 |

Not yet confirmed: final 2026/2027 forms and official calendar entries for the retained derived dates, 6 February form claim, private-provider status, exceptional relief/closure/receipt cases, actual account details and all unresolved upstream classifications; see refusal boundaries above.

## Disclaimer

This skill performs **orchestration only**: it selects the correct declaration, sequences the content skills, builds the calendar, and packages the result. It computes no tax. Every figure, schedule, and return assembled here is **provisional** and must be reviewed and signed off by a **qualified Ukrainian accountant or auditor** before it is filed with the State Tax Service. Deadlines and form references reflect rules as understood for tax year 2026 and must be re-verified against tax.gov.ua / dps.gov.ua at filing time. The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
