---
name: bq-income-tax
description: >
  Analyse personal income tax for 2026 in Bonaire, Sint Eustatius and Saba.
  Use for BES residence, global income, employment expenses, business profits,
  savings interest, substantial interests, loss carryforwards, annual tariff,
  tax-free sum, contribution credits and assessment procedure. Distinguishes
  taxable income from the taxable sum, the statutory upper-band constant and
  matching insurance credits from separate premiums. Includes employee,
  sole-trader and mixed-income arithmetic under stated assumptions, primary
  sources and refusal conditions. This source-cited draft holds unresolved
  mortgage relief, insurance eligibility, final rounding, foreign relief and
  return mapping. It does not authorise filing or payment.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Calendar 2026 personal income tax; separate insurance and filing conditions"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - income-tax-workflow-base
---

# Bonaire, Sint Eustatius and Saba: personal income tax in 2026

Establish residence, the filing unit and each income source before using the
tariff. This is a dated statutory reference for a qualified reviewer. It adds
personal-income rules to the BES pack; it does not establish a complete country
pack or a complete operational income-tax companion.

Load `workflow-base` and `income-tax-workflow-base`. Preserve their source gates,
profile confirmation, refusal handling, four universal outputs and five income
tax outputs. The examples below are conditional arithmetic, not substitute
returns. Missing mandatory companion slots hold the complete financial output
package; a labelled rule or example remains available for reference.

## Scope, residence and filing unit

The tax year is the calendar year. BES residents are within personal income tax;
the authority describes their reporting basis as worldwide income. Residence is
decided from the circumstances, with the special temporary-absence and
temporary-presence rules in Income Tax BES article 1(2). Establish those facts
before deciding residence. A fixed day count alone does not settle it.
[I1, articles 1, 12 and 27][I1]; [B1, article 1.5][B1]; [G2]

Non-residents are taxed on the particular sources in article 17, subject to its
conditions. For example, the share/debt and substantial-interest disposal
branches in article 17(1)(e) and (f) carry the ten-year former-residence condition
in article 17(2). Do not read the shorter official non-resident summary as
removing it. A visit lasting less than three successive months does not itself
grant the possible ministerial relief mentioned in article 17(1)(d). This guide
does not select non-resident, treaty, migration or split-year outcomes.
[I1, articles 1(3), 2, 12, 17–18 and 24(1)(b), (4)–(5)][I1]; [G3]

Article 20 keeps defined personal income with the individual and attributes
other components between spouses under its full-year marriage, residence and
relative-income conditions. It also contains a separate-property request rule.
Article 20a addresses minor children's income. Establish the applicable unit
and allocations before adding income or allowances; do not assume either a
European Netherlands fiscal partnership or unrestricted joint pooling. [I1]

Amounts below are US dollars (USD). The three BES public bodies share this
national personal-income statute; European Netherlands box rates, euro
allowances and filing dates do not supply missing BES rules. [I1]; [B1, article 1.3][B1]

## Income classification and expenses

Articles 3–11 distinguish movable-capital income, business/labour income and
periodic-payment rights. Substantial-interest income has a separate tariff.
Record the statutory category and timing for every receipt. [I1]

| Receipt or cost | Treatment to establish | Authority in [I1] |
|---|---|---|
| Salary, pension from employment, fees and benefits | Business/labour category; wage definition imports payroll law, with the stated exceptions. Use gross evidence and keep withholding separate. | Article 6 |
| Sole-trader receipts and disposals of business assets | Business profit includes the specified disposal, private-transfer and cessation gains. Establish tax book values before computing a gain. | Article 6(1)–(3) |
| Interest and ordinary dividends | Movable-capital category unless the business or substantial-interest rules apply. Savings-deposit interest has an annual exclusion of up to USD 5,000; do not extend it to every investment return. | Articles 5 and 8(i) |
| Substantial-interest distributions and disposals | Apply article 11's direct/indirect 5% tests, spouse/family and associated-right/debt rules, acquisition basis and deemed disposals before using the separate rate. | Article 11 |
| Annuity or other periodic right | Apply the periodic-payment category and the consideration/recovery conditions. Employment pensions remain in the employment branch. | Articles 6–7 |
| Private asset sale, gift or inheritance | Test article 8's exclusions against business income, periodic payments and the special article 11 inclusions. An income-tax exclusion proves no exemption from another tax. | Articles 8 and 11 |
| Own-account transfer, loan principal or capital introduced | Reconcile supporting records and the actual legal character; a bank credit alone does not prove income or exclusion. | Articles 3 and 5–11 |

Non-business receipts are recognised on receipt, set-off, availability, becoming
interest-bearing, or becoming due and collectible as article 16b specifies.
Related costs and personal/extraordinary expenses follow its payment and
equivalent-event rule. Do not impose that receipt basis on business profit.
[I1, articles 9–10 and 16b][I1]

For employment and other labour outside a business, article 9(3) supplies a
USD 280 expense deduction. Alternatively it permits actual expenses to the
extent they exceed USD 560. Either deduction is capped by the relevant proceeds;
the two alternatives are not added together. Establish which expenses survive
article 9c before choosing the actual-expense alternative. [I1]

Business acquisition, collection and preservation costs require their business
nexus. Capital acquisition/improvement expenditure generally enters the capital
rules, rather than an immediate revenue deduction; depreciation follows sound
business practice. Article 9c contains private-use and specific disallowances,
including commuting, ordinary clothing, private phone/internet subscriptions,
fines and bribes. Its separate restrictions for business entertainment/gifts and
non-business equipment/training must not be replaced by a generic expense
percentage. [I1, articles 9, 9c and 10][I1]

Accelerated depreciation, investment deductions, replacement reserves and
private-use vehicles require the complete article 6, 9(5), 9a–9c and 10
conditions, applicable delegated restrictions and an evidenced asset schedule.
They are not selected in this reference's examples. Ordinary non-business
source costs cannot make that source negative; unused costs may be carried
against that source's positive proceeds in the next five calendar years, in
origin order. This is separate from article 15's income-loss carryforward.
[I1, articles 9(7), 9b and 15][I1]

## Deductions, losses and the taxable sum

Use the statutory ladder, rather than subtracting the tax-free sum from bank
receipts. Article 3 starts with net income by source, deducts personal and
extraordinary expenses to obtain *zuiver inkomen*, then deducts available
article 15 losses to obtain *belastbaar inkomen*. Article 24 forms the ordinary
*belastbare som* by removing the net substantial-interest component and the
applicable tax-free sum and elderly allowance. Keep each rung identifiable.
[I1, articles 3, 15–16a and 24][I1]

An article 15 loss is a negative *zuiver inkomen*. It carries forward to the
next five tax years, earliest year first. Verify the origin, prior use and any
spouse-transfer conditions; an unsupported opening figure supplies no loss
claim. Do not merge this register with the article 9(7) source-cost register.
[I1, articles 9(7) and 15][I1]

Articles 16 and 16a contain conditional personal and extraordinary deductions,
not a general deduction for all household expenditure. They distinguish loan
interest, specified insurance, evidenced qualifying gifts, own-home costs,
illness/support and study, with separate limits, floors, family allocations and
partial-year adjustments. Retrieve the complete applicable branch and evidence
before claiming it. The examples stipulate no such deduction. [I1]

| 2026 item | Amount or rate | Conditions and source |
|---|---:|---|
| Resident tax-free sum | USD 21,956 | I1, article 24(1)(a), (2); R1, article XII(A) |
| Elderly allowance | USD 1,678 | Age qualifying for AOV benefit reached at the beginning of the calendar year; I1, article 24(1)(a)(3), (3); R1 |
| Ordinary taxable sum up to USD 53,198 | 29.4% | I1, article 24a(1); R1, article XII(B) |
| Ordinary taxable sum above USD 53,198 | USD 15,640 plus 38.4% of the excess | Published statutory constant; same provisions |
| Net substantial-interest benefits and specified non-resident sources | 7.5% | I1, article 24b; establish article 11 or article 17 eligibility first |

The indexation instrument takes effect on 1 January 2026 at 00:00 in the BES
public bodies. It supplies the completed tariff after the original 2026 tax
plan's omitted upper-band amount. Use USD 15,640 as published in the upper row;
do not replace it with a recalculated lower-band product. Intermediate tariff
arithmetic is not a final assessment-rounding method. [R1, articles XII–XIII and the explanatory section on BES indexation][R1]; [A1, article XXXV][A1]

### Contribution credits and separate premiums

Article 24a(2)–(7) reduces income tax by the applicable AOV, AWW and healthcare
credits. Each credit uses the relevant prescribed percentage and the base on
which that person owes the matching premium, subject to the USD 38,390 maximum
credit base. Article 24c provides a combined assessment where applicable. The
credit is not permission to omit premiums or deduct them twice. [I1]; [R1]

Current authority guidance lists AOV at 25%, AWW at 1.3% and the employee
healthcare component at 0.5%, with a USD 38,390 maximum base and the applicable
tax-free amounts. These figures alone do not establish insured status, the
correct base/period, age cessation, self-employed healthcare, employer charges
or an international exception. Obtain those determinations from the applicable
insurance rules and contribution workpaper. Do not simply add all three
percentages to the tariff liability. [G1]; [I1, article 24a(2)–(7)][I1]

Show tariff tax, each contribution credit, resulting income tax, each separate
premium, withholding and prepayments as distinct components. Where a verified
premium and its credit are equal, they cancel in the combined arithmetic;
that identity does not establish eligibility or make a credit independently
refundable. This reference does not settle a credit exceeding tariff tax. [I1]

### Own-home relief discrepancy: hold the dependent calculation

The 2026 authority page says qualifying own-home interest and declining
life-insurance premiums receive relief at 29.4%, rather than 38.4%. The retained
statute's article 24a(8)–(10) still adds five percentage points in its specified
upper-band/crossing cases. Those propositions do not produce the same result
after the tariff change. The original 2026 tariff amendment and indexation do
not themselves resolve this discrepancy. Do not silently substitute a
nine-point adjustment or select the more favourable statement. [G1]; [I1]; [A1]; [R1]

Hold a calculation that relies on this relief until its applicable legal
treatment is established. Own-home classification under article 4, the separate
2020 construction policy and property-tax exemptions also remain distinct.
Read `bq-property-tax` and `bq-bonaire-ground-tax` for their separate scope;
neither supplies the missing income-tax resolution. [I1, articles 4 and 16(1)(h)][I1]

## Computation and fictional examples

1. Establish the period, resident status, filing unit and source categories.
2. Reconcile gross amounts to certificates and ledgers. Deduct only established
   source expenses; keep source-cost carryforwards, capital schedules and
   personal deductions separate.
3. Form *zuiver inkomen*, apply evidenced article 15 losses, then form ordinary
   *belastbare som* under article 24. Compute any article 24b component separately.
4. Apply the published tariff, then the applicable contribution credits. Add
   the separately established premiums to the combined position.
5. Reconcile evidenced withholding and provisional assessments, which article
   8.8(4) of B1 credits against the assessment. Record the balance and its limits.
6. Map to the requested year's actual return and rounding instructions before
   producing a filing amount. No bank transfer or submission is authorised here.

The following full-year resident examples assume an established filing unit,
no substantial interest, no elderly allowance, no source-cost carryforward or
income loss, and no personal/extraordinary deduction. All income and allowed
cost classifications are stipulated. The matching contribution-credit/premium
inputs are fictional amounts supplied by a separate verified contribution
workpaper for the example; they are **not** rates or computed insurance results.
Each credit is below tariff tax. Withholding and prepayments are stipulated as
evidenced. These examples test the ladder and double-counting controls, not
social-insurance eligibility or return-field/rounding rules. [I1]; [B1, article 8.8][B1]

| Rung, USD | Employee | Sole trader | Mixed income |
|---|---:|---:|---:|
| Gross employment | 52,236 | 0 | 40,000 |
| Employment expense deduction | 280 | 0 | 280 |
| Gross business receipts | 0 | 90,000 | 50,000 |
| Established business revenue costs | 0 | 28,044 | 18,764 |
| Savings-deposit interest received | 0 | 0 | 6,000 |
| Savings-interest exclusion | 0 | 0 | 5,000 |
| Net source income / *zuiver inkomen* / taxable income | 51,956 | 61,956 | 71,956 |
| Resident tax-free sum | 21,956 | 21,956 | 21,956 |
| Ordinary taxable sum | 30,000 | 40,000 | 50,000 |
| Tariff tax at 29.4% | 8,820 | 11,760 | 14,700 |
| Stipulated contribution credits | 5,000 | 6,000 | 7,000 |
| Income tax after those credits | 3,820 | 5,760 | 7,700 |
| Separate stipulated matching premiums | 5,000 | 6,000 | 7,000 |
| Combined tax and premiums | 8,820 | 11,760 | 14,700 |
| Evidenced withholding | 9,000 | 0 | 8,000 |
| Evidenced provisional payments | 0 | 10,000 | 5,000 |
| Conditional arithmetic balance | 180 credit | 1,760 due | 1,700 due |

For an upper-band check, an already established ordinary taxable sum of
USD 60,000 gives an excess of USD 6,802. The published constant plus 38.4% of
that excess gives an **unrounded intermediate tariff amount of USD 18,251.968**.
It is neither a return amount nor an instruction to round a notice. This check
deliberately preserves the statutory USD 15,640 constant. [I1]; [R1]

## Filing, payment and review

An invitation requires a return. For assessment taxes, the inspector sets a
period of at least two months after issue; request an extension before the
stated deadline and retain the decision. The invitation, relevant-year return
and any granted extension determine the actual calendar. No 2026-income return
deadline in 2027 is inferred from an earlier filing campaign. A missing
invitation is not proof of no duty: B1 article 8.4(4)–(5) contains the separate
request obligation and exception. [B1, articles 8.3–8.6][B1]; [G4]

The authority offers online income-tax filing, with year-dependent paper/form
routes. Identify the actual 2026 form and instructions when available; this
reference does not certify portal acceptance or field mapping. Its guidance
allows an evidenced realistic daily exchange rate as an alternative to the
authority's published annual EUR/USD rate. No final 2026 annual average is
selected here. [G4]

The assessment states payment terms. B1 article 8.43 generally makes an
assessment collectible two months after its date; qualifying provisional
assessments dated before 1 November have the separate remaining-month
instalment rule, and additional/recovery assessments have the separate
one-month rule. Obtain the actual notice and check exceptional collection
provisions before generating dates. Filing extension does not establish a
payment extension. [B1, articles 8.2 and 8.43][B1]

Failure to file after the statutory reminder stage can attract the assessment
return default penalty, whose statutory ceiling is USD 1,400. Do not select
the maximum as an automatic charge or replace it with the payment-on-return
penalty. A reasoned objection to an assessment or appealable decision generally
has a two-month period from the specified notice date; objections to amounts
paid or withheld have the separately stated trigger. Retain proof and obtain
the full procedure before an actual objection. [B1, articles 8.4(2), 8.22(1) and 8.92][B1]

## Defaults, refusals and completion register

No additional missing-fact default is authorised by this reference. Do not
turn missing residence, family status, insurance, eligibility, tax basis,
withholding evidence or legal authority into zero or a chosen adverse outcome.
Report the missing item under the bases' Needs Input/source gates.

Hold the dependent calculation for non-residence, migration, foreign relief,
uncertain filing-unit allocation, special substantial-interest events,
unverified asset incentives, mortgage-relief interaction, unmatched insurance
credits/premiums, a credit exceeding tariff tax or missing operative rounding.
Route corporate entities, employer payroll, property taxes and cross-border
questions to their applicable rules. A treaty income allocation does not itself
settle social-insurance coverage. [I1]; [G5]

Before a complete income-tax workflow result, establish all mandatory country
slots: the actual return/form and field map, complete applicable deductions and
asset methods, contribution eligibility/bases/periods, withholding certificates,
provisional-payment evidence and future instalment terms, currency/rounding,
all material special branches, the current filing/payment calendar and complete
penalty/correction/appeal procedures. Recalculate the engagement workpaper,
produce every required universal/domain output, run their checks and obtain
professional review. No live taxpayer, portal run, workbook or practitioner
sign-off was tested for this reference.

Self-check the distinction between taxable income and taxable sum; source-cost
and income-loss registers; the two employment-expense alternatives; savings
interest and other returns; ordinary and substantial-interest rates; statutory
upper-row constant; credits and separate premiums; evidence-backed settlements;
and filing versus payment dates. Recheck every held branch before lifting it.

## Primary sources and provenance

Read on 17 October 2026. The registry identifies I1 as effective from
1 January 2026 to the consultation date. Pending/undated amendments are not
treated as operative. I1's selected articles 0–20a and 24–27, the current
registry/change entries, R1's BES provisions and explanation, A1's tariff
amendment and the cited B1 provisions were read in context. Official guidance
G1–G5 was read in full. The retained I1 legislative text matches the earlier BES property capture apart
from the consultation-date labels. This is selected-provision verification, not a claim that
every delegated rule or historical instrument has been examined.

[I1]: https://wetten.overheid.nl/BWBR0029281/2026-01-01
[R1]: https://zoek.officielebekendmakingen.nl/stcrt-2025-40487.html
[A1]: https://zoek.officielebekendmakingen.nl/stb-2025-444.html
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[G1]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-particulieren/inkomstenbelasting/tarieven-en-belastingvrije-bedragen-inkomstenbelasting
[G2]: https://english.belastingdienst-cn.nl/topics/tax-individuals/income-tax/domestic-taxpayers
[G3]: https://english.belastingdienst-cn.nl/topics/tax-individuals/income-tax/foreign-taxpayers
[G4]: https://english.belastingdienst-cn.nl/topics/tax-individuals/income-tax/filing-your-income-tax-return
[G5]: https://english.belastingdienst-cn.nl/topics/tax-individuals/income-tax/income-from-outside-of-caribbean-netherlands

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
