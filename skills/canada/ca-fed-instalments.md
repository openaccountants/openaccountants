---
name: ca-fed-instalments
description: Determine Canadian individual income-tax instalment liability for 2026 from current and prior net tax owing, compare actual reminder, prior-year and current-year options, add applicable CPP and voluntary EI, prepare dated payments and reconcile amounts paid. Covers August-only reminders, farming/fishing, death, Quebec coordination, payment evidence, daily interest and the statutory instalment penalty. Distinguishes income-tax instalments from GST/HST, corporate payments and a final T1 balance.
version: 2.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Canada: individual income-tax instalments

## Scope

Determine the obligation, amount, option, dates, actual-payment credits and interest/penalty consequences of **2026 individual income-tax instalments**. Covers Canadian-resident individuals, including self-employed people and people with insufficient withholding on other income. An individual instalment is a prepayment for that year's tax, not an extra deductible business expense or the prior return's balance. Non-Quebec collection generally combines federal and participating provincial/territorial income tax; Quebec's federal and Revenu Quebec obligations are separate. [ITA 156-156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html), [CRA scope](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [ITA 18(1)(t)(i)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html).

**Quick answer:** establish current/prior NTO and the applicable threshold for each year; determine ordinary versus chief-source farming/fishing; obtain actual reminders; calculate the complete annual amount, including applicable CPP/EI; compare valid options and actual dates/payments; then prepare instructions and reconcile the account. A reminder alone does not prove current liability, and a large CPP bill alone does not pass the income-tax NTO threshold. [Actual 2026 chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [liability/reminders](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html).

Use `ca-fed-t1-return` for the underlying return, `ca-fed-cpp-ei` for contribution outputs, `canada-gst-hst` for GST/HST and `ca-return-assembly` for the whole-return package. This method does not invent a corporate, trust, GST/QST, non-resident or estate tax engine. It preserves the specific farmer/death/Quebec instalment branches below. Actual individual facts and any special tax arrangements may require a separate method before the payment recommendation is complete.

**Source and professional approval:** the earlier v2.0 carried Nathan Wiebe's approval metadata. This substantive replacement has no evidence of his renewed approval; it remains tier 2 with no inherited `reviewed_by`/`reviewed_on`. Source checking is separate from accountant approval. Record the actual returned method version/year and approval/name for the work used; neither a bank classifier, a source reviewer, a historic approval nor a commit identity supplies a current professional approval.

Read the existing intake/records before asking. Use available runtime questions and artifacts; Canadian law and actual facts control over a generic workflow's defaults. Missing material data means **incomplete** for the affected calculation, not a zero/default, a mandatory from-memory fallback or an invented statutory requirement that every estimate be signed by a CPA. Continue supported independent work and state the precise missing item. Preparing instructions does not authorize or execute a payment.

## Ask the client first

Obtain only missing or conflicting facts after reading the available record:

1. Which instalment year and which individual/entity? For each relevant year, obtain December 31 residence/province and any moves, non-residence or special arrangements. Is chief-source income farming/fishing, and has the individual died?
2. Current estimated and two prior years' actual/reassessed NTO, source returns/assessments, income/deductions/withholding/selected credits and material changes. Identify the actual threshold and income facts for each year, not only the current province.
3. Actual February/August INNS1 or November farmer reminder, amounts, boxes and years; whether August is the only reminder and whether it mentions March/June. Obtain any amended assessment/reminder, separate RQ notice and account information.
4. Actual annual CPP and eligible self-employed EI payable for the selected calculation year, from the appropriate method/forms; Quebec contributions/premiums separately. Do not infer zero EI from missing agreement history or put QPP into a federal CPP field without support.
5. Every payment/transfer/refund/reversal, amount, date, authority/account/year, actual bank confirmation and CRA/RQ posting; all existing PAD arrangements. A statement description and a nearby quarter date are clues, not allocation evidence.
6. Is the task a forecast, payment schedule, bank reconciliation, interest/penalty calculation or annual return credit? Obtain the actual reminder, payment history, published rates for every accrued period, balance-due date and actual authority for any payment instructions.

One confirmed current NTO below its threshold can resolve ordinary non-liability without guessing missing history. Conversely, to assert liability obtain the actual relevant prior-year evidence; the two-year history is not an excuse to block a branch already proved by available facts. [ITA 156.1(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html), [actual chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [payment confirmation](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html).

## The method, step by step

### 1. Decide liability separately from the amount

Create one row for **2026, 2025 and 2024**, with residence at year-end, the applicable threshold for that year, NTO, evidence and whether NTO strictly exceeds that year's threshold. Keep a prior year's actual province/threshold if the individual moved. Do not apply the current Quebec threshold to all earlier years merely because the person is now in Quebec. [ITA 156.1(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html).

- Ordinary individual: 2026 must exceed its threshold **and at least one of 2025 or 2024** must exceed its own threshold.
- Chief-source farming/fishing: 2026 **and both 2025 and 2024** must exceed their applicable thresholds; use the special single-payment route, not the ordinary either-prior test.
- Exactly equal to the threshold is not above it. First self-employment is not itself an exemption: previous rental, pension or other income could already have produced relevant NTO.
- If current NTO will be below the threshold despite a reminder, no ordinary instalments are required on that estimate; document the basis and monitor changes. Unknown current income is not proof of either no liability or mandatory payment.

The statutory tests are subject to the actual income/credit definitions, exemptions and death rules; graduated rate estates have an explicit exemption, while other trust regimes cannot be assumed to follow this individual workflow. [ITA 155-156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-160.html), [current CRA 2026 test](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html).

### Rates, bands and thresholds

All money is CAD. Thresholds apply to the relevant year's NTO; the interest rows apply only to their stated periods.

| Item | Amount/rule and conditions | Year or period | Official source |
|---|---|---|---|
| Ordinary federal instalment threshold outside Quebec | NTO **over 3,000**, current and either prior year; each compared with its own year's residence threshold | 2026 test using 2025/2024 history | [ITA 156.1(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html) |
| Quebec resident's federal threshold | NTO **over 1,800**, same current/history test; separate RQ obligation | Relevant year-end residence | [ITA 156.1(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html) |
| Ordinary selected prior/current calculation | Complete annual payment amount divided by **4**, when ordinary quarterly branch applies; actual reminder route is its own option | 2026 | [CRA options and actual chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf) |
| August-only, no March/June entries, prior/current option | **75% September / 25% December** of complete annual amount; actual no-calculation option uses box 2, not invented percentages | 2026 | [CRA August-only instructions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html) |
| Chief-source farmer/fisher statutory branch | **2/3** of applicable current estimate or prescribed prior-year base, subject to actual liability/credit rules; do not equate to chart's 66% | December 31 payment | [ITA 155(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-160.html) |
| Instalment penalty | **50% once** of positive excess of actual instalment interest over greater of **1,000** and **25%** of hypothetical no-payment interest | Applicable year | [ITA 163.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html) |
| Overdue income tax, CPP and EI annual interest rate | **7%**, daily compounding; published overdue rate already includes statutory uplift | January 1-March 31, 2026 | [CRA first quarter](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q1.html) |
| Overdue income tax, CPP and EI annual interest rate | **7%**, same conditions | April 1-June 30, 2026 | [CRA second quarter](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q2.html) |
| Overdue income tax, CPP and EI annual interest rate | **7%**, same conditions | July 1-September 30, 2026 | [CRA third quarter](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q3.html) |
| Overdue income tax, CPP and EI annual interest rate | **7%**, same conditions | October 1-December 31, 2026 | [CRA fourth quarter](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q4.html) |
| Electronic-payment requirement | An amount **over 10,000** must be paid electronically unless the payer cannot reasonably do so; exactly 10,000 is not over | Applicable federal remittance/payment | [ITA 160.5(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-163.html) |

No 2027 interest rate is confirmed here. Do not put an unverified future rate in usable calculations or extend 2026's rate through the following balance-due date. The farmer chart conflict is resolved transparently in step 4, not by treating its two percentages as equal.

### 2. Reconcile NTO, annual amount and actual payments

**NTO threshold computation.** Use the actual source-year assessment/return and the current chart where appropriate, rather than T1 balance owing or a federal-tax subtotal. ITA 156.1 defines NTO and the relevant credits/withholding; its Quebec formula differs. The actual **2026 calculation chart** is a preparation aid that can use 2025 return/assessment figures or a 2026 estimate depending on the chosen option. It is not a filed return or a final 2026 T1 form. [Statutory definition](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html), [actual chart, both pages](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf).

| Actual 2026 chart field | Import and reconciliation |
|---|---|
| 1-5: payable | Net federal tax 42000, social-benefits repayment 42200, provincial/territorial tax 42800 and Yukon First Nations tax 43200, with the actual residence/collection scope. Do not substitute 43500 including CPP/EI. |
| 6: withholding | Actual applicable withholding 43700; Quebec residents use 43850 as directed. Do not subtract the same withholding again after NTO. |
| 7-17: selected credits | Follow the listed abatements and refundable credits, with actual eligibility and amounts: 44000/44100, 45200, 45300, 45350, 45400, 45600, 46900, 47555, 47556, 47900 and 45355. This is not “subtract every refund or credit.” |
| 18-20: credit adjustments | Subtract the chart's Yukon business/mining carbon rebates 63855/63856 from the credit total, as instructed, rather than using all of a provincial credit subtotal blindly. |
| 21: NTO | Payable subtotal minus selected/adjusted credits. This is the threshold measure. Actual instalments paid at 47600 do not reduce it. |
| 22-24: annual amount | Add actual CPP payable 42100 and eligible self-employed EI payable 42120 to NTO to get the complete annual amount for the chosen option. Contributions do not become threshold NTO merely by being added here. |

Retain a worksheet for each relevant source-year base/estimate and its version. Historical returns/reassessments and specified-future-tax-consequence adjustments can alter the base: **ITR 5300** defines the prescribed Part I instalment base, not a universal all-taxes NTO or a claim that CPP/EI are Part I income tax. Follow the actual combined collection chart and actual reminder for payment totals; use the statutory definition when explaining the Part I base. [ITA 156(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html), [ITR 5300](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-5300.html).

**Payments already made** are a third measure. Match each payment to the correct year/account/date, reconcile the remaining scheduled amount and retain the annual return credit once. Do not reduce the NTO eligibility test by payments, treat a future schedule as paid, or deduct the payment in T2125. Actual 2025 payments belong on that return's 47600; recheck the final-year form before using a later layout. [CRA actual 2025 credit instructions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html), [ITA 18(1)(t)(i)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html).

### 3. Compare all three calculation options

| Option | How to prepare the actual 2026 schedule | Decision/evidence |
|---|---|---|
| No-calculation | Obtain actual INNS1 amounts for each due date, including changed reminders and August-only box 2 if applicable. Use the latest relevant assessed information reflected by CRA; do not fabricate reminder amounts from incomplete NTO history. | Useful where income/deductions/credits are stable and the actual reminder is available. Timely payment of the actual required reminder amounts is the practical reference; still settle the final balance separately. [CRA options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html). |
| Prior-year | Calculate the complete amount using 2025 information and actual chart/adjustments, including applicable CPP/EI; apply ordinary quarters or the actual August-only rule. | Useful if 2026 is like 2025 but differs from 2024. A correct actual prior-year basis paid by its due dates can avoid instalment interest even if final current-year tax is larger. Incomplete figures or late/insufficient payment still create risk. [CRA option](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), [ITA 161(4.01)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html). |
| Current-year | Estimate full 2026 income, deductions, selected credits/withholding and contributions, then the complete amount; apply the actual schedule branch. | Useful if current income changes materially. Document assumptions and update them: an underestimated chosen amount can create interest/penalty. A sufficient timely current-year basis can also avoid interest. [CRA option](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), [actual chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf). |

For a statutory two-prior-year explanatory schedule under 156(1)(b), the first two ordinary instalments each use a quarter of the second-prior base, and the final two each use half the **positive** remainder of the prior base over half the second-prior base. Do not generate negative September/December payments, confuse that illustration with an actual reminder, or assume an annual total alone proves the right timing. [ITA 156(1)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html).

For an **August-only reminder with no March/June instalment mentioned**, the actual no-calculation option uses the September/December amount in box 2; prior/current options use the 75/25 rule in the rates table. Do not invent two overdue first-half payments or divide the actual two-payment branch into equal halves. Reconcile any actual payments already made before recommending further payments. [CRA exact August-only instructions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html).

Compare valid options on the same facts and dates. Under **161(4)/(4.01)**, interest/penalty computations use the applicable least statutory/reminder basis, including cumulative amounts due at the relevant dates. It is wrong to say only no-calculation can ever avoid interest, or that a correct prior-year basis must equal higher final current tax. It is also wrong to promise every guessed prior-year/current-year estimate is safe. Separate any remaining April balance and arrears interest from instalment interest. [Actual legal limitations](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html), [CRA interest calculation](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html).

Changing source withholding can reduce current NTO: CRA lists TD1 for relevant pension/EI arrangements, ISP3520OAS/ISP3520CPP for those benefits and a separate QPP route. Do not assume an employer can withhold tax on business, rental, investment or capital income directly. Use the actual source arrangement and recalculate NTO, not a deduction against instalments paid. [CRA reducing instalments](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html).

### 4. Apply special schedules and the farmer source conflict

**Farmer/fisher.** Establish chief-source farming/fishing and the current-plus-both-prior threshold test, then one payment by December 31; CRA generally sends the reminder in November. Use the actual current estimate or prescribed prior-year base and relevant collection adjustments. [ITA 155](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-160.html), [156.1(2)(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html), [CRA due dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html).

The inspected **Act says 2/3** and the actual **2026 federal chart says line 24 multiplied by 66%**. These are not equal: for an eligible, otherwise established 18,000 base with no other component/adjustment, the statutory amount is 12,000 while chart multiplication is 11,880. Do not silently publish the smaller chart result as the statutory amount, claim an unverified concession or round two thirds down to 66%. For the statutory calculation, use the exact statutory fraction. If relying on an actual CRA reminder, record that actual amount and the separate **161(4)** least-basis protection; a hypothetical chart figure is not proof a reminder was issued. Obtain case-specific reconciliation of the actual chart/reminder/collection base where the conflict affects the recommendation. Preserve the supported statutory calculation and explicit unresolved authority conflict rather than dropping the farmer job. [Act](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-160.html), [actual chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [161(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html). The separate RQ form expressly uses 2/3 and does not amend the federal chart. [Actual TP-1026-V, 3.2](https://www.revenuquebec.ca/documents/en/formulaires/tp/TP-1026-V(2026-02).pdf).

**Death.** Instalments due **on or after the date of death** are not required; overdue earlier instalments remain to be settled. Do not claim the entire year's instalments are refunded, demand an instalment on the death date, or use the estate's T3 timetable as the individual's T1 timetable. Determine the actual final-year and any previous-year balance-due date separately. [ITA 156.1(3)-(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html), [CRA instalment dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html), [deceased returns](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/filing-deadlines.html).

The ordinary final-return payment deadline is April 30 following death in January-October; death in November-December generally gives six months. The actual self-employed filing extension is separate and has its own date/tax-shelter conditions; it does not automatically extend payment. Also check the special previous-year return case for an early following-year death, without moving already overdue returns. These are not one universal “six months or later” rule. [CRA final/previous-year payment and filing sections](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/filing-deadlines.html), [248(1) balance-due day](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html).

### 5. Compute interest from actual dates, rates and alternative bases

Build an event ledger: actual eligible obligation/basis, due dates (including holidays/death), source reminders, each dated payment/transfer/reversal, rate-effective intervals and the actual balance-due endpoint. Keep income-tax instalments and separate GST/Quebec arrears distinct.

CRA's published 2026 interest-charge guidance lists three conditions together: the person must be required to pay instalments, must have received a 2026 instalment reminder showing an amount to pay, and must have missed, paid late or paid insufficient amounts. Record the actual reminder and payment evidence alongside the charge calculation. This published charge practice is distinct from the statutory instalment obligation; absence of a reminder is not proof that annual tax or statutory instalment liability disappears. [CRA interest-charge conditions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html), [ITA 155-156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html).

1. Compare valid statutory/reminder/current/prior cumulative requirements using **161(4) or (4.01)**; do not select the largest guessed schedule or compare only final annual totals.
2. Compute daily-compounded interest for the required dated amounts through the applicable payment/balance-due endpoint, using each actually published overdue rate. The underlying ITR 4301(a) T-bill rate plus uplift produces the published overdue rate; do not add another uplift or borrow the non-corporate refund rate. [ITA 161](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html), [248(11)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html), [ITR 4301(a)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-4301.html).
3. Apply the actual same-year payment/contra-interest computation. CRA describes interest A on the instalments required, less B on instalments paid from their dates or January 1 if later, to the balance-due date, using the least-interest calculation option. Do not count all payments as if made on January 1, treat a transfer as posted on a guessed date, or create refundable/carryforward interest from overpayment. A charge is applied under the published administrative guidance only if the difference is more than 25; distinguish the statutory computation from this charge practice. [CRA calculation/credit interest](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html), [161(2.2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html).
4. Separate instalment interest from later unpaid-balance interest under161(1); avoid accruing both as duplicate principal interest for the same endpoint. Unknown future quarterly rates mean an incomplete projection for that interval, not permission to use 7% forever.
5. Retain the method comparison, event/day-count assumptions, interval rates, precision and reconciliation to any actual CRA assessment. A partial daily-growth demonstration is not an assessed interest charge. Reconcile a different CRA amount from its dates/bases rather than inventing an adjustment.

Early or extra instalments can reduce same-year instalment interest via the actual credit/contra calculation. Annual overpayment does not automatically cure a late earlier instalment, and credit interest is not an extra cash refund. Voluntary payments below the liability threshold are allowed; non-liability does not eliminate the final annual tax bill. [CRA interest and options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html), [payment overpayment/refund procedure](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html).

### 6. Apply the instalment penalty once

Let **I** be actual relevant instalment interest after the appropriate computation, and **J** the hypothetical interest if no instalments had been made. Use:

`penalty = 0.5 * max(0, I - max(1000, 0.25 * J))`

The outer half occurs **once**. Do not multiply by 50% and then divide by two again. Interest over 1,000 is a screening trigger, not a guarantee of a positive penalty when the alternative threshold is larger. Do not use income-tax principal or late-return months as I/J. [ITA 163.1(a)-(c)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html), [CRA actual 2026 example](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html).

Keep other charges distinct. The original's late-return topic belongs with the actual T1 filing job: ordinary162(1) depends on a late required return and unpaid tax, while162(2)'s higher repeated-failure rule additionally requires its demand/prior-penalty conditions. Use the full `ca-fed-t1-return` calculation instead of labelling every unpaid instalment a late-filed return or treating June 15 as the balance-due date. [ITA 162(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html), [actual 2025 filing/payment dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html). Current published late-return percentages and limits remain in that owning method; none is removed as though all late-return penalties had disappeared.

### 7. Preserve every bank-pattern family as evidence prompts

Keep bank entries in suspense/unallocated tax payments until authority, individual/entity, account, year, purpose, dated confirmation and CRA/RQ allocation support a classification. Only confirmed income-tax instalments enter the instalment ledger; no real SIN or bank credential belongs in an example. [CRA payment-type distinction](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/make-payment/payment-options-type-payment-you-are-making.html), [actual bank payee/account instructions](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-online-banking.html), [actual payment verification](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html).

| Original CRA pattern | Investigation required, not a deterministic classification |
|---|---|
| `CRA`, `CANADA REVENUE AGENCY` | Could be an individual balance, instalment, business tax or other repayment. Obtain actual payment allocation and year. |
| `CRA INSTALMENT`, `CRA INST` | Stronger intent clue, but still match actual individual/year/account, payment date and posting. |
| `RECEIVER GENERAL`, `REC GEN CANADA` | Government payee is not proof of an income-tax instalment; inspect the selected payee/allocation. |
| `CRA PRE-AUTHORIZED DEBIT` | Read the actual PAD agreement/allocation and withdrawal/confirmation; generic bank wording does not identify the tax or year. |
| `MY PAYMENT CRA` | My Payment supports several taxes/purposes. Obtain the payment type/allocation/receipt, not only its service name. |

| Original timing window | Retained clue and corrected conclusion |
|---|---|
| March 10-20 | Investigate first instalment and actual weekend/holiday date; no automatic high-confidence allocation. |
| June 10-20 | Could relate to an instalment, balance, filing or another account; obtain evidence. |
| September 10-20 | Check ordinary or August-only branch and actual account year. |
| December 10-20 | Check ordinary fourth instalment; chief-source farmer payment may instead be December 31. |
| April-May | Could be prior-year balance, current instalment, transfer or other payment. Flag purpose separately; timing alone proves none. |

| Original other pattern | Treatment after actual evidence |
|---|---|
| `CRA GST`, `GST/HST` | Separate GST/HST account, outside income-tax instalment schedule unless an actual authorized transfer is documented. Use `canada-gst-hst`. |
| `CRA CPP`, `CPP PAYMENT` | Investigate actual contribution/benefit/collection purpose. Applicable CPP can be included in the proper annual instalment amount; a bank string does not prove an additional separate payment or exclusion from the account. |
| `CRA CHILD BENEFIT`, `CCB` | Benefit receipt/repayment investigation, not income-tax instalment merely because CRA is named. |
| `REVENU QUEBEC`, `MRQ` | Usually a separate authority; determine actual provincial payment or the published move/refund/remittance process, never automatically credit federal47600. |
| `CRA PENALTY`, `CRA INTEREST` | Separate actual charge/settlement components from the income-tax instalment principal and return credit. |
| `CRA REFUND` | Reconcile original authority/year and account refund/transfer; do not net a generic refund against current instalments without evidence. |

| Original reference clue | Actual control |
|---|---|
| `SIN + INST` or `INSTALMENT` | Legacy text is an intent clue only. Actual online-bank individual account identifier is the nine-digit SIN; a mandatory literal `INST` suffix is not supported. Follow the bank's actual fields and keep the identifier private. |
| Tax year plus `Q1/Q2/Q3/Q4` | A self-entered description is not CRA allocation. Match the year/period, receipt and actual account entry; correct mistaken allocations. |

Additional real PAD bank descriptors may include `CRA TXD`, `CANADA TXD` and `CRA TXD/DIM`; they are also only evidence prompts. Do not infer legal purpose from a merchant name or transaction sign. Part I income-tax payments are not a business deduction, while eligible contribution deductions/credits follow their actual separate rules. [Actual PAD descriptions](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-authorized-debit.html), [ITA 18(1)(t)(i)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html).

## Boundary and exception table

| Boundary | Action and effect |
|---|---|
| Corporate instalments, R-CA-FI-1 | Use the corporate instalment method; individual thresholds/options cannot establish corporate liability. |
| GST/HST instalments, R-CA-FI-2 | Use `canada-gst-hst`, its account/period/base/deadline rules; keep payment/account evidence distinct. |
| Trust instalments, R-CA-FI-3 | Obtain the actual trust regime; GRE statutory exemption does not exempt every trust. [156/156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html). |
| Unknown year/history | Resolve only the missing facts needed for the actual branch; no mandatory-liability claim from current Quebec2000 alone, nor an invented first-year exemption. |
| Chief-source farming/fishing | Current plus both prior thresholds; statutory/reminder amount, source conflict and one December 31 payment as step 4. |
| Death | No amounts due on/after death; preserve prior overdue instalments and actual final/previous-year payment rules. |
| Quebec or move | Determine each year's actual threshold/collection scope; separate RQ computation and published dated transfer/refund route. |
| Missing reminder | Calculate a supported current/prior basis if enough facts exist; do not invent reminder amounts or assume liability is extinguished. Unavailable evidence can leave a recommendation incomplete. |
| Future unknown rates, changed assessment or allocation | Preserve known intervals/evidence and obtain the missing rate/base/dated posting before a complete charge claim. |

### Quebec coordination, without substituting a federal engine

The federal threshold for a Quebec resident is distinct from Quebec's separate ordinary current-and-either-prior **over 1,800** test. Revenu Quebec may collect applicable QPP, HSF, prescription-drug-plan and QPIP amounts in addition to its tax. Its NTO, credits and actual forms differ from CRA's; do not put an RQ payment into federal47600 or reuse the federal CPP/EI chart as a Quebec calculation. [RQ obligation](https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/instalment-payments/), [actual TP-1026-V 2026-02](https://www.revenuquebec.ca/documents/en/formulaires/tp/TP-1026-V(2026-02).pdf).

Obtain actual **TPZ-1026.A-V** reminders. If missing, determine the obligation using actual **TP-1026-V**, or obtain the actual remittance slip in My Account; TPZ-1026.A-V is not a public blank-download form. Current 2026 notices distinguish February/August and August-only history; farmer notices generally come in November for December 31. RQ receipt is the actual office receipt or financial-institution processing date, not an assumed bank instruction date. [RQ paying/viewing notices](https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/instalment-payments/making-instalment-payments/).

The observed actual 2026 TP-1026-V uses 2025 data for the prior-year method **with estimated 2026 refundable credits**. Its3.1 can apply selected credits against earlier instalments rather than always dividing a net annual amount equally; its3.2 uses exact2/3 for eligible farmers. It uses a dated2025return bridge for a2026estimate, not proof final2026return layouts exist. Route the full provincial calculation to that actual form and required QPP/QPIP/HSF/drug-plan methods. RQ interest/additional-interest rules are separate; do not copy federal163.1 or federal7% into them. [Actual three-page form, Parts1-3/general information](https://www.revenuquebec.ca/documents/en/formulaires/tp/TP-1026-V(2026-02).pdf).

For a person moving out of Quebec with relevant2025RQ instalments, CRA publishes a process: request RQ refund and a statement/letter showing the original payment dates, send the refunded amount and letter to CRA, and have those dates respected in the new province. Do not assume an automatic tax-agency transfer, delete the old payment or count both refund and new remittance as two federal credits. Apply the actual year/account circumstances and retain the dated documents. [CRA dated2025move/claim instructions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html).

## Worked cases

Synthetic amounts illustrate specified facts, not a client's return. All relevant NTO/base/contributions are supplied as supported inputs; the underlying T1/CPP/EI engines must establish them. The checks preserve the five original example families and six original test scenarios, and add the material boundaries below.

### Case 1. Preserve the original no-calculation illustration, with complete bases

The original 2025 illustration had2023NTO25,000 and2024NTO28,000. For this bounded illustration, assume no additional CPP/EI or other base adjustments, ordinary liability, and a matching actual reminder with complete annual source bases25,000/28,000. First two amounts are6,250 each; the second two7,750 each; total28,000. Ordinary2025weekend-adjusted dates derived from the general CRA rule are March 17,June 16,September 15,December 15, 2025. The amounts are not themselves proof such a reminder was issued.

For 2026, the same numbers can illustrate supported 2024/2025 bases, with March 16,June 15,September 15,December 15, 2026 as the actual ordinary calendar. If the prior base were10,000 against a second-prior 40,000, the two earlier10,000 amounts leave no positive remainder: later instalments under the illustrated two-year formula are zero, not negative5,000. This can make the illustrated year's total exceed its prior base; no refund is invented. [156(1)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html), [actual reminder option](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), [date rule](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html).

```oa-check
name: Original no-calculation amounts and positive remainder boundary
inputs:
  second_prior_base: 25000
  prior_base: 28000
  declining_second_prior: 40000
  declining_prior: 10000
steps:
  - first: second_prior_base / 4
  - later: max(0, prior_base - second_prior_base / 2) / 2
  - total: 2 * first + 2 * later
  - declining_first: declining_second_prior / 4
  - declining_later: max(0, declining_prior - declining_second_prior / 2) / 2
  - declining_total: 2 * declining_first + 2 * declining_later
expected:
  first: 6250
  later: 7750
  total: 28000
  declining_first: 10000
  declining_later: 0
  declining_total: 20000
```

### Case 2. Prior-year option, contributions and the smaller current-year choice

Original2025prior-year NTO28,000 with no added contribution/adjustment gives7,000 each and28,000 total, if this complete supported basis and ordinary quarterly branch apply. It need not match a higher final current-year bill to be an eligible interest basis when paid correctly and timely; settle the remaining final balance separately.

In a new2026example, supported2025NTO28,000 plus CPP4,000 and voluntaryEI1,000 gives33,000, or8,250 ordinary quarters. Supported current 2026NTO20,000 plus CPP3,000 and EI500 gives23,500, or5,875 ordinary quarters. The current forecast saves2,375 per quarter relative to that prior-year amount, but its facts must be updated and sufficient. Under the actual August-only prior/current branch, the 23,500forecast becomes17,625 in September and5,875 in December, not four payments. [Options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), [chart additions](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [August-only](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [least-basis rule](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html).

```oa-check
name: Prior-year versus current estimate including contributions and August-only
inputs:
  old_nto: 28000
  prior_nto: 28000
  prior_cpp: 4000
  prior_ei: 1000
  current_nto: 20000
  current_cpp: 3000
  current_ei: 500
steps:
  - original_quarter: old_nto / 4
  - prior_annual: prior_nto + prior_cpp + prior_ei
  - prior_quarter: prior_annual / 4
  - current_annual: current_nto + current_cpp + current_ei
  - current_quarter: current_annual / 4
  - quarterly_difference: prior_quarter - current_quarter
  - september_only: current_annual * 0.75
  - december_only: current_annual * 0.25
expected:
  original_quarter: 7000
  prior_annual: 33000
  prior_quarter: 8250
  current_annual: 23500
  current_quarter: 5875
  quarterly_difference: 2375
  september_only: 17625
  december_only: 5875
```

### Case 3. Below threshold, first self-employment, Quebec and moved residence

Preserve the original2025case: actual 2023NTO2,800 and2024NTO2,500 are both below the non-Quebec threshold, so ordinary2025instalments are not required even if current income rises; ordinary2025balance remains payable by April 30, 2026. The original first-SE example with prior 500/800 and current 25,000 has the same ordinary non-liability result, **because of its actual history**, not the new business label. Where instalments are not required but a final balance is expected, show the supported estimated unpaid balance and its due date and plan funds for it. Do not invent that balance from NTO alone. [156.1(2)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html), [dated annual payment](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html).

For2026outsideQuebec, currentNTO2,500 plus CPP9,000 still does not exceed the NTO threshold; exact3,000 also fails. Current4,000 with 2025NTO3,500 and2024NTO0 satisfies ordinary history. A first-SE taxpayer with that same prior pension/rental NTO can therefore owe instalments.

The old Quebec test's current federalNTO2,000 alone is **incomplete**, not proof of liability. With actualpriorQuebecNTO2,000, current 2,000 passes both relevant1,800thresholds. But if both prior years were non-Quebec withNTO2,000, those years did not exceed their own3,000thresholds: moving intoQuebec does not retroactively apply1,800to that history. Record residence and each statutory year's threshold. [156.1(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html).

```oa-check
name: NTO threshold margins and contributions do not establish liability
inputs:
  prior_a: 2800
  prior_b: 2500
  first_business_a: 500
  first_business_b: 800
  threshold: 3000
  current_low: 2500
  cpp: 9000
  current_above: 4000
  prior_above: 3500
  qc_current: 2000
  qc_threshold: 1800
steps:
  - prior_a_margin: prior_a - threshold
  - prior_b_margin: prior_b - threshold
  - first_business_a_margin: first_business_a - threshold
  - first_business_b_margin: first_business_b - threshold
  - current_low_margin: current_low - threshold
  - misleading_cpp_total: current_low + cpp
  - exact_threshold_margin: threshold - threshold
  - current_above_margin: current_above - threshold
  - prior_above_margin: prior_above - threshold
  - qc_current_margin: qc_current - qc_threshold
  - moved_prior_margin: qc_current - threshold
expected:
  prior_a_margin: -200
  prior_b_margin: -500
  first_business_a_margin: -2500
  first_business_b_margin: -2200
  current_low_margin: -500
  misleading_cpp_total: 11500
  exact_threshold_margin: 0
  current_above_margin: 1000
  prior_above_margin: 500
  qc_current_margin: 200
  moved_prior_margin: -1000
```

### Case 4. Original farmer amount, with the real history and conflict

Preserve the original18,000example, now stipulating actual chief-source farming, NTO above the applicable threshold in current **and both** prior years and a fully established statutory calculation base18,000 with no other contribution/credit adjustment. Exact2/3 is12,000 by December 31. The actual federal chart's66%multiplication is11,880, a120difference, not a rounding equivalent. An actual qualifying reminder/least-basis protection must be proved separately if used. If either prior year's NTO is below its applicable threshold, this farmer branch is not mandatory even though the ordinary either-prior test might pass. [155](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-160.html), [156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html), [actual chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [161(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html).

```oa-check
name: Statutory farmer fraction and observed chart conflict
inputs:
  established_base: 18000
steps:
  - statutory_payment: established_base * 2 / 3
  - chart_multiplication: established_base * 0.66
  - source_difference: statutory_payment - chart_multiplication
expected:
  statutory_payment: 12000
  chart_multiplication: 11880
  source_difference: 120
```

### Case 5. Preserve the bank-line example without inventing allocation

Original line: `15.03.2025 ; CRA INSTALMENT PAYMENT ; DEBIT ; -7,000.00 ; CAD`.

Treat it initially as an instalment-intent clue. March 15, 2025 was Saturday; that string does not prove actual received date, account, year or on-time payment. If the bank receipt and CRA ledger establish7,000 paid as an individual's2025instalment on the applicable actual date, record7,000 as a tax-payment/owner settlement rather than a deductible business expense and include it once in that year's actual instalment credit. If the ledger instead shows2024balance owing or GST, reclassify to that proven purpose. If evidence is missing, leave unallocated and do not claim a current instalment credit. [Actual bank payee](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-online-banking.html), [payment verification](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html), [2025 return credit](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html), [18(1)(t)(i)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html).

```oa-check
name: Confirmed instalment credit once, not business expense
inputs:
  bank_debit: -7000
  proven_instalment: 7000
steps:
  - matched_outflow: abs(bank_debit)
  - unallocated_difference: matched_outflow - proven_instalment
  - credited_once: proven_instalment
expected:
  matched_outflow: 7000
  unallocated_difference: 0
  credited_once: 7000
```

### Case 6. Penalty both ways, not every interest amount over the trigger

CRA's actual 2026example supplies I2,500/J3,200: the alternative25%amount is800, so the greater threshold is1,000; penalty is750. The former twice-halved formula incorrectly gave375. With I1,100/J5,000, the alternative threshold is1,250: the penalty is zero despite I exceeding1,000. With I2,500/J8,000, the threshold is2,000 and penalty250. The hypotheticalJ must come from the correct no-payment interest computation. [163.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html), [CRA worked example](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html).

```oa-check
name: Instalment penalty single half and both threshold branches
inputs:
  interest: 2500
  no_payment_interest: 3200
  lower_interest: 1100
  high_hypothetical: 5000
  second_hypothetical: 8000
steps:
  - alternative: no_payment_interest * 0.25
  - threshold: max(1000, alternative)
  - penalty: max(0, interest - threshold) / 2
  - wrong_double_half: penalty / 2
  - zero_penalty: max(0, lower_interest - max(1000, high_hypothetical * 0.25)) / 2
  - high_threshold_penalty: max(0, interest - max(1000, second_hypothetical * 0.25)) / 2
expected:
  alternative: 800
  threshold: 1000
  penalty: 750
  wrong_double_half: 375
  zero_penalty: 0
  high_threshold_penalty: 250
```

### Case 7. A dated daily-interest component, not a full CRA assessment

For a supplied30-day2026component on1,000 at the actual 7%annual overdue rate with a365-day year, daily growth produces5.77 before the full alternatives/payment-credit/charge-threshold computation. Supply the actual day count from the event ledger; this example does not certify an arbitrary payment date or extrapolate through 2027. With supplied fully recomputed A1,200 and B300, the residual interest is900 before the penalty computation; B is not a refundable cash credit. The actual administrative more-than25charge condition is tested separately; do not round25.004to25before testing an actual CRA-rule precision without support. [Daily compounding](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html), [published2026rates](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q1.html), [actual A-B and charge rule](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html).

```oa-check
name: Known 2026 daily component and supplied contra-interest residual
inputs:
  principal: 1000
  annual_rate: 0.07
  day_fraction: 365
  days: 30
  interest_a: 1200
  credit_b: 300
steps:
  - daily_rate: annual_rate / day_fraction
  - day_one_interest: principal * daily_rate
  - factor: 1 + daily_rate
  - factor_2: factor * factor
  - factor_4: factor_2 * factor_2
  - factor_8: factor_4 * factor_4
  - factor_16: factor_8 * factor_8
  - factor_30: factor_16 * factor_8 * factor_4 * factor_2
  - thirty_day_interest: round(principal * (factor_30 - 1), 2)
  - residual_interest: max(0, interest_a - credit_b)
expected:
  daily_rate: 0.00019178082191780822
  day_one_interest: 0.19178082191780822
  thirty_day_interest: 5.77
  residual_interest: 900
tolerance: 0.000000000001
```

The 30-day growth uses daily compounding, not30times simple interest. The executable block builds the 30-day factor by multiplying the 16-,8-,4-and2-day factors; these periods sum to30 and avoid an unsupported exponent operator. Independent source review must still recompute it from the specified inputs.

### Original six-test regression table

| Original test | Supported revised result |
|---|---|
| No-calculation25,000/28,000 | Case 1 retains6,250/7,750/28,000, conditional on actual complete bases/reminder/ordinary liability, positive remainder and actual dates. |
| Prior-year28,000 | Case 2 retains7,000/28,000 when no added contributions/adjustments; timely correct actual prior-year basis can be interest-safe. |
| Prior NTO2,500/2,800 | Case 3 preserves non-liability under ordinary2025history; no general exemption from the final balance. |
| Farmer18,000 | Case 4 preserves exact12,000 with actual chief-source/current-and-both-prior facts; chart difference explicit. |
| First-SE prior 500/800/current 25,000 | Case 3 preserves ordinary non-liability from those actual prior values, not the first-SE label; changing prior income can change the result. |
| Quebeccurrent2,000 | Case 3 is incomplete without relevant history; with a qualifying prior year it passes. Actual moved-residence history uses each year's own threshold. |

## When to refuse or refer

Preserve R-CA-FI-1 corporate, R-CA-FI-2 GST/HST and R-CA-FI-3 trust routes in the boundary table. Also refer the affected calculation where there is a nonresident/special assessment, unresolved farmer authority conflict, missing actual year/account/reminder evidence, materially contradictory records, unknown future interest rate or unsupported underlying income/contribution computation. Do not stop supported independent work or replace a required calculation with guesses.

If a decision is already established from known facts, give it with its scope rather than demanding irrelevant documents. If not established, identify the exact missing NTO/year/residence/reminder/payment/rate and financial consequence. No payment, account change, PAD agreement, filing or professional approval is authorized merely because the method described it.

## Filing and payment

### Actual 2026 calendar and final balance

| Obligation | Actual ordinary date and conditions | Source |
|---|---|---|
| First ordinary2026instalment | March**16**, 2026: nominalMarch15isSunday, nextbusinessday applies | [CRA dates/holiday rule](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) |
| Second/third/fourth ordinary2026instalments | June 15,September 15,December 15, 2026, subject to actual liability/branch and recognized holidays | [CRA dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) |
| August-only prior/current branch | September 15/December 15, 2026 with actual 75/25; no-calculationbox2 is separate | [CRA August instructions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html) |
| Eligible chief-source farmer/fisher 2026 | December 31, 2026, actual special liability/base/reminder and statutory fraction/chart distinction | [155](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-160.html), [CRA exception](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) |
| Remaining2025T1balance / qualifyingself-employedfiling | PaymentApril30, 2026; qualifyingfilingJune15, 2026. The later filing date is not a later payment deadline | [Actual2025annual dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) |
| Ordinary individual2026finalbalance | April 30, 2027 under actual individual balance-due rule; special/death cases separately checked. No2027quarterlyinterest rate is verified here | [248(1)balance-due day](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html), [156.1(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html) |

Do not roll a missed payment into a future date without showing the overdue amount/period and actual interest basis. A future year's forecast is conditional until its current-year liability and actual reminders/rules are checked. Keep filing dates, instalment dates and balance-due dates separate.

### Payment workflow and receipt

1. Reconcile taxpayer/authority/year, liability, chosen valid option, actual due date, cumulative amounts paid and amount remaining. Obtain actual payment authority and account identifier from the authorized record; keep a real SIN/bank detail private.
2. Select the **individual income-tax instalment** purpose, rather than current-return payment, assessed balance, corporation or GST. In online banking, follow the bank's actual equivalent tax-instalment payee; the individual account number is the nine-digit SIN. Names can differ by institution. Do not tell the user to type an invented mandatory `SIN + INST` suffix. [CRA bank instructions](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-online-banking.html), [payment-type options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/make-payment/payment-options-type-payment-you-are-making.html).
3. Actual channels include supported bank payment, My Payment, authorized PAD, and appropriate in-person/mail options with the correct voucher. An amount over the federal electronic-payment threshold is electronic unless the statutory reasonable-inability exception applies. Use actual **INNS3** for an instalment remittance voucher; **INNS1** is the reminder and **INNS2** the February payment summary. [CRA instalment payment process](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html), [160.5](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-163.html).
4. For **My Payment**, use the actual individual payment type/allocation/details, review before authorized submission and save confirmation. The service supports eligible debit/wallet options, not credit cards; it can be entered via the CRA account or its public service entry. Actual bank/service timing can date a late-evening/weekend/holiday payment on the next business day. Do not equate account display time with the date legally received. [Actual My Payment instructions](https://www.canada.ca/en/revenue-agency/services/e-services/payment-save-time-pay-online.html).
5. For **PAD**, the actual My Account path includes “Proceed to pay”, “Schedule a series of payments”, required agreement fields, review and confirmation. First withdrawal and changes/cancellation require at least5businessdays under the actual instructions. Only the specified legal-representative route can schedule for an individual through Represent a Client; an EFILE/T185 current-year one-time PAD is not an instalment-payment route. Confirm actual allocation, bank details and authority; creation of an agreement is not proof withdrawal occurred. [Actual PAD eligibility/process](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-authorized-debit.html).
6. Retain proof and verify posting: CRA's instalment page says allow3businessdays for online or10for cheque/money-order before checking My Account **Accounts and payments** or the later INNS2 summary. The specific bank/MyPayment/PAD pages separately govern considered-paid/processing timing; these are not grace periods extending a due date. Reconcile amount/year/allocation and any failure/reversal. If wrong, use the actual available transfer-payment function or contact CRA; do not claim a transfer or refund happened until confirmed. [CRA confirmation/correction](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html), [bank](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-online-banking.html), [MyPayment](https://www.canada.ca/en/revenue-agency/services/e-services/payment-save-time-pay-online.html), [PAD](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-authorized-debit.html).
7. Reconcile annual actual instalments once to the proper return year/credit, including proved payments missing from a reminder/summary. Distinguish refund request, approved refund and actual receipt; CRA reviews excess-instalment refunds case by case. Use the published Quebec move process where applicable. No chart is itself submitted as an annual return or payment. [CRA credit/move route](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html), [refund procedure](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html), [chart warning](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf).

### Required output

Supply: (a) year-by-year residence/NTO/threshold evidence and decision; (b) source/version/actual approval record; (c) calculation of complete amount and option comparison; (d) each dated instalment, actual paid/remaining amount and authority/year; (e) interest/penalty work with actual source rates and date assumptions, or exact missing intervals; (f) reconciliation to bank/CRA/RQ and annual return credits; (g) concrete client actions and unresolved items. Label estimates as estimates and distinguish unallocated, instructed, scheduled, withdrawn and posted amounts. A fully supported narrower answer can be given without claiming the whole return is prepared/filed.

## Completion checklist

Retain the ten original self-check subjects, with corrected controls:

- [ ] Current and relevant prior NTO, each year's residence/threshold and ordinary versus farmer test established; no first-SE exemption invented.
- [ ] Actual reminder/prior/current method and complete annual amount, CPP/EI additions, positive remainder and August-only branch checked.
- [ ] Every actual date/year/account and payment schedule, including weekend/holiday/death effects, checked rather than printing nominal dates blindly.
- [ ] NTO imports/selected credits/withholding and payment credits reconciled once; no CPP-only threshold or47600 deduction from NTO.
- [ ] Chief-source farming/fishing and both-prior history checked; statutory fraction/chart conflict/reminder distinction retained.
- [ ] Non-Quebec combined versus Quebec separate tax/contributions, actual forms and any move process established.
- [ ] Interest computed from supported alternatives, dated payments, actual published quarterly rates and contra/charge conditions; unknown future rate not invented.
- [ ] First-business-year case decided from actual history/current figures; all original example/test/pattern families preserved as evidenced guidance.
- [ ] Penalty applies one half of positive excess, not double half; late-return, instalment and unpaid-balance charges remain distinct.
- [ ] Estimate/completion/current professional approval and actual payment status reported honestly, without invented CPA-signoff mandate or a false posted-payment claim.

## Sources

Read date **2026-11-14**, bounded portions below. These are operative-content reads, not status-code stamps. The original and actual 2026 chart were read in full; the three-page Quebec form was read for the coordination/form routes, not certification of every provincial engine. Justice section pages generally show current to October 19, 2026/last amended June 18, 2026; the full-page155 source shows September 30, 2026 with the same amendment date. Record the differing consolidation dates and check later changes before later use. Direct155/FullText attempts that failed are not successful reads; ordinary official full-page155 was read. No access control was bypassed. The prior connector Transport closed is not evidence of a live outage or successful live content verification.

| ID | Official source, portion actually read and short exact locator | Read on |
|---|---|---|
| I01 | [Read for: 155(1)–(2); “chief source of income”; “2/3”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-160.html) | 2026-11-14 |
| I02 | [Read for: 156(1),(3),(4); “Subject to section 156.1”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html) | 2026-11-14 |
| I03 | [Read for: 156.1(1),(1.1),(2)–(4); “No instalment required”; “on or after the day”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html) | 2026-11-14 |
| I04 | [Read for: 5300(a)–(b); “instalment base of an individual”](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-5300.html) | 2026-11-14 |
| I05 | [Read for: 161(1),(2),(2.2),(4),(4.01); “Contra interest”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html) | 2026-11-14 |
| I06 | [Read for: 163.1(a)–(c); “Penalty for late or deficient instalments”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html) | 2026-11-14 |
| I07 | [Read for: 4301(a)–(c); “paid to the Receiver General”](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-4301.html) | 2026-11-14 |
| I08 | [Read for: 26; “the day next following that is not a holiday”](https://laws-lois.justice.gc.ca/eng/acts/I-21/section-26.html) | 2026-11-14 |
| I09 | [Read for: Factors/reminders/August-only; “either 2025 or 2024”; “form INNS1”](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html) | 2026-11-14 |
| I10 | [Read for: Three options and reducing withholding; “3 options”](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html) | 2026-11-14 |
| I11 | [Read for: Both actual pages; “Net tax owing”; “line 24 multiplied by 66%”](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf) | 2026-11-14 |
| I12 | [Read for: Due dates/Exceptions; “next business day”](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) | 2026-11-14 |
| I13 | [Read for: 2026 interest,A−B,penalty and credit sections; “Then the difference is divided by 2”](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html) | 2026-11-14 |
| I14 | [Read for: Income tax; “will be 7%”](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q1.html) | 2026-11-14 |
| I15 | [Read for: Income tax; “will be 7%”](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q2.html) | 2026-11-14 |
| I16 | [Read for: Income tax; “will be 7%”](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q3.html) | 2026-11-14 |
| I17 | [Read for: Income tax; “will be 7%”](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q4.html) | 2026-11-14 |
| I18 | [Read for: Choose/confirm/resolve/overpaid; “form INNS3”; “form INNS2”](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html) | 2026-11-14 |
| I19 | [Read for: Individuals:make payment and processing; “9-digit social insurance number”](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-online-banking.html) | 2026-11-14 |
| I20 | [Read for: Personal income tax versus other accounts; “An instalment payment (current-year taxes)”](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/make-payment/payment-options-type-payment-you-are-making.html) | 2026-11-14 |
| I21 | [Read for: MyPayment personal payment types/processing; “My Payment”](https://www.canada.ca/en/revenue-agency/services/e-services/payment-save-time-pay-online.html) | 2026-11-14 |
| I22 | [Read for: 160.5(1)–(2); “exceeds $10,000”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-163.html) | 2026-11-14 |
| I23 | [Read for: 2025 claim/corrections/QCmove; “line 47600”](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) | 2026-11-14 |
| I24 | [Read for: Filing/payment2025taxes; “April 30, 2026”; “June 15, 2026”](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) | 2026-11-14 |
| I25 | [Read for: 162(1)–(2); “Repeated failure to file”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) | 2026-11-14 |
| I26 | [Read for: Finalreturn/payments and previous-year return; “date of death”](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/filing-deadlines.html) | 2026-11-14 |
| I27 | [Read for: Obligation/death/NTO; “$1,800”](https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/instalment-payments/) | 2026-11-14 |
| I28 | [Read for: When/how/receipt/view; “TPZ-1026.A-V”](https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/instalment-payments/making-instalment-payments/) | 2026-11-14 |
| I29 | [Read for: Catalogue title/version; “2026-02 version”](https://www.revenuquebec.ca/en/online-services/forms-and-publications/current-details/tp-1026-v/) | 2026-11-14 |
| I30 | [Read for: Actual3pages, generalinformation and3.2; “Multiply line 60 by 2/3.”](https://www.revenuquebec.ca/documents/en/formulaires/tp/TP-1026-V(2026-02).pdf) | 2026-11-14 |
| I31 | [Read for: 18(1)(t)(i); “under this Act”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) | 2026-11-14 |
| I32 | [Read for: Operative creation/management/representative/processing; “at least 5 business days”](https://www.canada.ca/en/revenue-agency/services/about-canada-revenue-agency-cra/pay-authorized-debit.html) | 2026-11-14 |
| I33 | [Read for: 248(1) balance-due day(b),(c),248(11); “shall be compounded daily”](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html) | 2026-11-14 |


**Not yet confirmed:** actual client/current-year facts, prior assessments and reminders, payment allocations/processing dates, authorizations, live portal/account results, current professional approval and actual receipts; unpublished 2027 quarterly rates; case-specific resolution of federal farmer chart66% versus statutory2/3 where relied on; final2026annualreturn layouts; a complete provincial or nonresident/estate engine. Do not turn an unknown into zero, an estimated charge into an assessment or an instruction into an executed payment.

**Removed and why:** stale 2025-only metadata and obsolete legacy-facts-generation claim; contradictory interest/penalty/interest-guarantee statements; deterministic bank-label classifications and unsupported literal reference format; wrong GST companion slug; blanket mandatoryCPA/EA/attorney gate. Supported thresholds/options/dates/payment/interest/penalty/provincial/special cases, all five original example families, six tests, ten self-check subjects, three refusal IDs and every original pattern/window/reference survive with the documented corrections. No supported tax job is replaced by a thin router.

### Change log

- **v2.1, 14 November 2026:** Detailed2026source audit of liability/amount/payment distinctions, all options and branches, actual date and interest/penalty rules, bank evidence and full payment workflow; original examples/patterns preserved and expanded. Substantive changed version remains unapproved pending professional approval.
- **v2.0, earlier2025method; metadata updated July 2026:** Historical individual-instalment method; old approval metadata named NathanWiebe. That historical version does not approve this replacement.
