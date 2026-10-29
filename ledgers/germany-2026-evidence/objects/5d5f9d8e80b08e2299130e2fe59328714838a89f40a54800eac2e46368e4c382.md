---
name: de-estimated-tax
description: "German income tax prepayments (Einkommensteuer-Vorauszahlungen, § 37 EStG) for individuals, tax year 2026. Covers who pays them, the four due dates (10 March, 10 June, 10 September, 10 December), how the tax office sets the amount from the last assessment, the EUR 400 and EUR 100 minimums, the EUR 600 small-deductions rule, increases, reductions and the 15-month adjustment window, the solidarity surcharge (EUR 20,350 / 40,700 limits, 5.5%, 11.9% mitigation) and church tax riding on prepayments, the year-end balance, the 1% late payment surcharge and 1.8% interest after assessment, and new businesses. Trigger on: Vorauszahlungen, Vorauszahlungsbescheid, estimated tax Germany, quarterly tax Germany, Herabsetzung Vorauszahlungen, Säumniszuschlag, Nachzahlungszinsen. Out of scope: the tariff and the return (de-einkommensteuer-freelancer, de-self-employed-income-tax), trade tax prepayments (de-trade-tax), VAT advance payments (germany-vat-return), corporate tax (de-corporate-tax), non-residents (de-non-resident-tax)."
version: 2.4
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - de-self-employed-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German income tax prepayments 2026 (Einkommensteuer-Vorauszahlungen)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific taxpayer's facts. A Steuerberater should confirm results before acting.

"Estimated tax" is a US phrase. In Germany the taxpayer does not work out prepayments. The tax office (Finanzamt) sets them in a prepayment notice (Vorauszahlungsbescheid), and the taxpayer pays the amounts printed on it. § 37 EStG has no safe harbour percentage, no annualised method and no penalty for an estimate that turns out too low. What costs money is paying a set amount late, and interest on the final balance.

## Who this applies to

- **Individuals whose income tax is not fully collected by withholding:** freelancers, sole traders, partners, landlords, investors with assessed income, and employees with large side income. They pay prepayments on the income tax they are expected to owe for the current year ([§ 37(1) EStG](https://www.gesetze-im-internet.de/estg/__37.html)).
- **Only once a notice sets them.** Prepayments are set by prepayment notice (§ 37(3) sentence 1 EStG). With no notice, nothing is payable in advance. Set money aside.
- **When the claim arises.** Each prepayment arises at the start of the calendar quarter in which it is due, or when tax liability begins, if later (§ 37(1) sentence 2 EStG).
- **Not here:** trade tax prepayments (set by the municipality, `de-trade-tax`), VAT advance payments (`germany-vat-return`), wage tax withheld by an employer (`de-payroll`), and companies (`de-corporate-tax`). Partnership prepayments are set on each partner personally; the partnership itself pays none for income tax. Partners: `de-partners-and-part-year`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Due dates | 10 March, 10 June, 10 September, 10 December | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Minimum yearly total, below which no prepayments are set | EUR 400 | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Minimum per due date (both minimums must be met) | EUR 100 | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Minimum increase per due date (ordinary increase) | EUR 100 | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Minimum for a later increase under § 37(4) | EUR 5,000 | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Small deductions left out of the base if together not above | EUR 600 | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Adjustment window after the tax year | 15 calendar months (23 if farming and forestry dominates) | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Solidarity surcharge exemption limit, single | EUR 20,350 of income tax | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html |
| Solidarity surcharge exemption limit, splitting (joint) | EUR 40,700 of income tax | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html |
| Solidarity surcharge rate | 5.5% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Mitigation cap: surcharge not above this share of the excess over the limit | 11.9% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Church tax, members only, on the income tax | 8% or 9% by federal state | 2025 booklet | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf |
| Late payment surcharge, per started month | 1% of the overdue tax rounded down to a multiple of EUR 50 | 2026 | https://www.gesetze-im-internet.de/ao_1977/__240.html |
| Grace period before the surcharge is charged | 3 days (not for cash or cheques) | 2026 | https://www.gesetze-im-internet.de/ao_1977/__240.html |
| Interest after assessment (§ 233a AO) | 0.15% per full month (1.8% a year), amount rounded down to EUR 50 | 2026 | https://www.gesetze-im-internet.de/ao_1977/__238.html |
| Interest-free period | 15 months after the end of the tax year (23 for farming and forestry); longer for 2019 to 2024 only | 2026 | https://www.gesetze-im-internet.de/ao_1977/__233a.html |
| Registration questionnaire for a new business | within 1 month | 2026 | https://www.gesetze-im-internet.de/ao_1977/__138.html |

The 2026 solidarity surcharge limits first apply for assessment period 2026 ([§ 6(27) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__6.html)). Older material shows lower limits.

## The taxable base

**The starting figure.** Prepayments are measured, as a rule, by the income tax of the last assessment after crediting withholding taxes such as wage tax and investment income tax (§ 37(3) sentence 2 EStG, with § 36(2) number 2). The tax office may adjust them to the tax it expects for the current year (§ 37(3) sentence 3). Adjusting covers a rise and a cut.

**Small deductions are ignored.** Church tax paid, childcare costs, own vocational training, school fees (§ 10(1) numbers 4, 5, 7 and 9), the § 10(1a) special expenses, donations (§ 10b), extraordinary burdens (§ 33) and the § 33a amounts are left out if together they do not exceed EUR 600 (§ 37(3) sentence 4).

**Always left out.** The § 34a reduction for retained profits and the § 10a(1) pension special expense (§ 37(3) sentences 5 and 6). § 37(3) does not list the § 35 trade tax credit, so the credit is not excluded; if a notice ignores it, apply for an adjustment. For parents: where child benefit does not fully achieve the tax relief for a child's subsistence minimum (§ 31 EStG), the § 32(6) child allowances and the child benefit to be offset are also left out (§ 37(3) sentence 12). The prepayment base is then worked out with child benefit, not with the allowances; the comparison happens only in the assessment.

**Rental losses on a new building.** A loss from letting a building counts only for calendar years that begin after it was bought or completed (§ 37(3) sentence 8). If the building is bought before the calendar year in which it is completed, completion takes the place of purchase (sentence 9). Sentence 10 lifts this for buildings with § 7b special depreciation and some older incentives. The same rule applies to a loss from letting another asset within § 21(1) sentence 1 numbers 1 to 3 EStG, with the start of the taxpayer's own use in place of purchase or completion (sentence 11).

**Surcharges.** The solidarity surcharge is measured on the prepayments (§ 3(1) number 2 SolzG) and charged only if the base exceeds the limit in the table (§ 3(3)). Above the limit, it is 5.5% of the whole base, but not more than 11.9% of the excess over the limit (§ 4). Worked from § 4, the cap stops biting once the base passes EUR 37,838.28 (single) or EUR 75,676.56 (joint), where 5.5% of the whole base equals 11.9% of the excess. Income tax at the flat rate under § 32d(3) and (4) EStG is left out of the limit test (§ 3(3) SolzG). Joint filers use the EUR 40,700 limit; do not double the single limit by hand. Church tax prepayments are paid with the income tax prepayments ([§ 51a(4) EStG](https://www.gesetze-im-internet.de/estg/__51a.html)). The EUR 400 and EUR 100 minimums do not apply to them (§ 51a(4) sentence 1).

**How the yearly amount is split.** § 37 does not print a split across the four dates. Read the amounts from the notice.

**Year-end settlement.** Prepayments paid and withholding taxes are credited against the assessed tax ([§ 36(2) EStG](https://www.gesetze-im-internet.de/estg/__36.html)). A balance due (Abschlusszahlung) is payable within one month of the assessment notice; the part equal to prepayments due but unpaid is payable at once (§ 36(4) sentence 1). An overpayment is refunded after the notice (§ 36(4) sentence 2).

**Prepayments are not a business expense.** Income tax, solidarity surcharge and the late payment surcharge and interest on them may not be deducted from profit or income ([§ 12 number 3 EStG](https://www.gesetze-im-internet.de/estg/__12.html): taxes on income "sowie die auf diese Steuern entfallenden Nebenleistungen"; late payment surcharges and interest are Nebenleistungen under [§ 3(4) numbers 4 and 5 AO](https://www.gesetze-im-internet.de/ao_1977/__3.html)). Book them as private withdrawals. Church tax paid, including church tax prepayments, is the exception: it is a special expense in the year paid ([§ 10(1) number 4 EStG](https://www.gesetze-im-internet.de/estg/__10.html)), except church tax on flat-taxed investment income.

## Deadlines and filing

- **Four dates:** 10 March, 10 June, 10 September, 10 December 2026. In 2026 none falls on a weekend. If a deadline ends on a Saturday, Sunday or public holiday, it moves to the next working day ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)).
- **Day of payment** ([§ 224(2) AO](https://www.gesetze-im-internet.de/ao_1977/__224.html)): a transfer counts on the day the tax office's account is credited; under a SEPA direct debit mandate, on the due date; cash on receipt; a cheque three days after receipt.
- **A later increase** adjusts the last prepayment of the year and is payable within one month of the notice (§ 37(4) EStG).
- **Changing the amount.** A prepayment notice is always set subject to review, and the taxpayer may apply at any time for it to be changed ([§ 164(1) and (2) AO](https://www.gesetze-im-internet.de/ao_1977/__164.html)). Use the Mein ELSTER form "Antrag auf Anpassung von Vorauszahlungen" with a profit projection. The tax office decides at its discretion: § 37(3) sentence 3 EStG says it "kann" adjust, so an application does not by itself change anything. The current notice stays in force until it is replaced ([§ 124(2) AO](https://www.gesetze-im-internet.de/ao_1977/__124.html)), so pay it until a new notice arrives.
- **Adjustment window.** The tax office may adjust 2026 prepayments until the end of March 2028 (15th month after the year). Longer periods applied for 2019 to 2024 only ([§ 52(35d) EStG](https://www.gesetze-im-internet.de/estg/__52.html)).
- **New business.** The registration questionnaire (Fragebogen zur steuerlichen Erfassung) is due within one month of starting ([§ 138(1b) and (4) AO](https://www.gesetze-im-internet.de/ao_1977/__138.html)). Its expected-profit answer drives the first prepayment notice.

## Penalties and interest

- **Late payment surcharge** ([§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)). For each started month after the due date: 1% of the overdue tax rounded down to a multiple of EUR 50. None for a delay of up to three days, except for cash or cheques (§ 240(3)). None before the tax is set (§ 240(1) sentence 3), but solidarity surcharge and church tax prepayments are payable with the set income tax prepayments even without their own notice, and that protection does not apply to them (§ 51a(4) sentences 2 and 3 EStG). No surcharge on surcharges or interest (§ 240(2)).
- **Interest after assessment** ([§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html), [§ 238 AO](https://www.gesetze-im-internet.de/ao_1977/__238.html)). 0.15% for each full month, on the balance rounded down to EUR 50, both ways. For 2026 it starts on 1 April 2028. Older years had a longer interest-free period: 2019 from 1 October 2021; 21 months for 2020 and 2021, 20 for 2022, 18 for 2023 and 17 for 2024 (the 2024 interest period is Art. 97 § 36(3) number 7(d), distinct from the 16-month § 152 late-filing rule in number 5(d); [Art. 97 § 36(2) and (3) EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)). Do not carry those periods into 2026. The base is the assessed tax less withholding and less prepayments set before interest starts (§ 233a(3)). Prepayment notices themselves bear no § 233a interest (§ 233a(1) sentence 2). Voluntary payments accepted before the assessment stop interest (§ 233a(8)).
- **Started versus full months.** The surcharge counts each started month; § 233a interest counts full months only (§ 238(1) sentence 2).
- **Too-low prepayments.** No penalty in § 37. The cost is a larger balance and, after the interest-free period, interest.
- **False facts in a reduction application.** Giving the tax office incorrect or incomplete facts that lead to tax being cut is tax evasion, punishable by up to five years' imprisonment or a fine; the attempt is punishable too ([§ 370(1) and (2) AO](https://www.gesetze-im-internet.de/ao_1977/__370.html)). A prepayment notice is a tax assessment (§ 164(1) sentence 2 AO), so a reduction won on false facts falls under it. Do not prepare or file a reduction application on a profit projection you know to be wrong.
- **A client who cannot pay.** The tax office may defer (Stundung) a payment where collecting it when due would be a considerable hardship and the claim is not put at risk; deferral is as a rule granted only on application and against security ([§ 222 AO](https://www.gesetze-im-internet.de/ao_1977/__222.html)). Apply before the due date. Deferral interest is charged for the deferral period ([§ 234(1) AO](https://www.gesetze-im-internet.de/ao_1977/__234.html)) at 0.5% for each full month ([§ 238(1) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html)). That is not the 0.15% § 233a rate, which § 238(1a) limits to § 233a cases; do not mix them. § 233a interest set for the same period is credited against deferral interest (§ 234(3)). If the hardship comes from lower income, apply for a reduction of the prepayments as well.

## Cross-border points

- Non-residents with German income assessed under § 49 EStG can also receive prepayment notices; § 37 is not limited to residents. See `de-non-resident-tax`.
- Foreign tax credits and treaty exemptions change the expected tax. If a notice is based on a year before a move, apply for an adjustment. The year of moving in or out: `de-partners-and-part-year`; leaving: `leaving-germany-exit-tax`.
- Pay in EUR to the tax office's account; the payment day is when the account is credited, so allow for foreign transfer time.

## Worked examples

**Example 1: freelancer, steady income.** The last assessment showed income tax of EUR 9,600, with EUR 1,200 of investment income tax credited. The base is EUR 8,400. The notice sets four equal prepayments of EUR 2,100. Both minimums are met. EUR 8,400 is below the EUR 20,350 single limit, so no solidarity surcharge. She is a church member in a 9% state: church tax prepayments total EUR 756 for the year, paid with the same instalments.

```oa-check
name: DE 2026 prepayment base, minimums, surcharge and church tax
inputs:
  last_income_tax: 9600
  withholding_credited: 1200
  soli_limit_single: 20350
  church_rate_pct: 9
steps:
  - base: last_income_tax - withholding_credited
  - per_date: base / 4
  - soli_excess: max(0, base - soli_limit_single)
  - soli: min(base * 0.055, soli_excess * 0.119)
  - church: base * church_rate_pct / 100
expected:
  base: 8400
  per_date: 2100
  soli: 0
  church: 756
```

**Example 2: higher earner, mitigation zone and a late payment.** A single sole trader's notice sets income tax prepayments of EUR 22,000 for 2026. That is over the EUR 20,350 limit. 5.5% of 22,000 is EUR 1,210, but the cap is 11.9% of the EUR 1,650 excess, EUR 196.35, so the surcharge prepayments are EUR 196.35 for the year. His 10 September instalment of EUR 5,549 is credited 40 days late. That is two started months. The overdue tax rounds down to EUR 5,500, and the surcharge is 1% x 2 x 5,500 = EUR 110.

```oa-check
name: DE 2026 solidarity mitigation and late payment surcharge
inputs:
  prepayments_year: 22000
  soli_limit_single: 20350
  overdue: 5549
  days_late: 40
steps:
  - soli_full: prepayments_year * 0.055
  - soli_cap: (prepayments_year - soli_limit_single) * 0.119
  - soli: min(soli_full, soli_cap)
  - started_months: ceil(days_late / 30)
  - rounded_overdue: floor(overdue / 50) * 50
  - surcharge: rounded_overdue * 0.01 * started_months
expected:
  soli_full: 1210
  soli_cap: 196.35
  soli: 196.35
  started_months: 2
  rounded_overdue: 5500
  surcharge: 110
```

The 30-day month in the steps is a simplification for this example; count calendar months from the due date on a real file.

**Five further qualitative cases.** These retain the earlier scenarios without inventing a client amount.

| Case | Declared input | Result |
|---|---|---|
| Notice-based instalments | A 2026 Vorauszahlungsbescheid lists an amount for each date: 10 March, 10 June, 10 September and 10 December | Report those four amounts and dates; do not invent an equal split (§ 37(1)/(3) EStG). |
| Below the minimum | The annual income tax prepayments are below EUR 400, or a payment date is below EUR 100 | No income tax prepayments are set: both minimums must be met (§ 37(5)). |
| Late Q2 transfer | Due 10 June 2026; the tax office is credited on 15 July 2026 | Two started months, beyond the three-day grace. The surcharge is 2 × 1% × the unpaid tax rounded down to EUR 50 (§ 240 AO). |
| Solidarity exemption | Single filer; the annual prepayment base does not exceed EUR 20,350; no assessed § 32d(3)/(4) flat-rate tax | No solidarity surcharge on that base (§ 3(3) SolzG). |
| Bank line checked to its notice | `10.06.2026 ; LASTSCHRIFT FINANZAMT MUENCHEN ; DEBIT ; ESt-VZ Q2/2026 ; amount ; EUR`, with the reference/amount confirmed against the income tax notice | Classify this stipulated payment as Q2 income tax prepayment and a private withdrawal, not a deductible business expense (§ 12 number 3 EStG). A payee or date alone is not proof. Church tax has its separate § 10(1) number 4 treatment. |

## Ask the client first

1. Do you have a current Vorauszahlungsbescheid? Send it and the last assessment notice.
2. What do you expect this year's profit or income to be, compared with the year the notice is based on? Any one-off gain in that year?
3. Are you a church member, and in which federal state?
4. Are you assessed jointly with a spouse or partner?
5. Did you start, stop or move a business, or move into or out of Germany, this year or last?
6. Do you pay by SEPA direct debit or by transfer?

## Sources

| Source | URL | Read on |
|---|---|---|
| EStG § 37 (prepayments) | https://www.gesetze-im-internet.de/estg/__37.html | 2026-10-24 |
| EStG § 36 (crediting, balance, refund) | https://www.gesetze-im-internet.de/estg/__36.html | 2026-10-27 |
| EStG § 51a (surcharge taxes, church tax prepayments) | https://www.gesetze-im-internet.de/estg/__51a.html | 2026-10-24 |
| EStG § 52(35d) (2019 to 2024 periods) | https://www.gesetze-im-internet.de/estg/__52.html | 2026-10-24 |
| SolzG § 3 (base and limits) | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-10-24 |
| SolzG § 4 (rate and mitigation) | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-10-24 |
| SolzG § 6(27) (2026 limits apply) | https://www.gesetze-im-internet.de/solzg_1995/__6.html | 2026-10-26 |
| EStG § 10(1) number 4 (church tax as a special expense) | https://www.gesetze-im-internet.de/estg/__10.html | 2026-10-26 |
| EStG § 12 number 3 (taxes on income not deductible) | https://www.gesetze-im-internet.de/estg/__12.html | 2026-10-27 |
| AO § 3(4) (late payment surcharges and interest are Nebenleistungen) | https://www.gesetze-im-internet.de/ao_1977/__3.html | 2026-10-27 |
| AO § 108 (weekends, holidays) | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-10-24 |
| AO § 124 (notice stays in force until replaced) | https://www.gesetze-im-internet.de/ao_1977/__124.html | 2026-10-27 |
| AO § 138 (registration questionnaire) | https://www.gesetze-im-internet.de/ao_1977/__138.html | 2026-10-24 |
| AO § 164 (prepayment notices subject to review) | https://www.gesetze-im-internet.de/ao_1977/__164.html | 2026-10-27 |
| AO § 222 (deferral) | https://www.gesetze-im-internet.de/ao_1977/__222.html | 2026-10-27 |
| AO § 224 (day of payment) | https://www.gesetze-im-internet.de/ao_1977/__224.html | 2026-10-24 |
| AO § 233a (interest after assessment) | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-10-24 |
| AO § 234 (deferral interest) | https://www.gesetze-im-internet.de/ao_1977/__234.html | 2026-10-27 |
| AO § 238 (interest rate) | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-10-24 |
| AO § 240 (late payment surcharge) | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-10-24 |
| AO § 370 (tax evasion) | https://www.gesetze-im-internet.de/ao_1977/__370.html | 2026-10-27 |
| EGAO Art. 97 § 36 (2019 to 2024 interest periods) | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-10-24 |
| EGAO Art. 97 § 36(3), numbers 5(d) and 7(d): distinguish 2024 late-filing and interest periods; selected text reread | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-10-29 |
| Finance ministry, "Steuern von A bis Z" (church tax 8% or 9%) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf | 2026-10-24 |
| Mein ELSTER, "Antrag auf Anpassung von Vorauszahlungen" | https://www.elster.de/eportal/formulare-leistungen/alleformulare/eingvorauszlg | 2026-10-27 (named from the earlier version; page not re-read) |

Not yet confirmed: how the solidarity surcharge limit is applied to a notice issued part way through a year; church tax rates per state for 2026 (the booklet is the 2025 edition); the old version's bank-statement pattern tables (Finanzamt debit references, timing windows, telling ESt from VAT, wage tax and trade tax debits) are working conventions with no official source and were not carried over as rules; the federal founders' portal advice on first-year prepayments was not re-read.

> Contributed by Michael Cutajar.

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
