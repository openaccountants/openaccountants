---
name: es-modelo-111
description: "Use this Guide to compute and reconcile Spanish common-territory Modelo 111 withholding remittances for payments made in 2026. It covers payer and recipient classification, professional standard and startup rates, employee withholding inputs, in-kind payments, distinct recipient counts, the numbered form boxes, complementary returns, filing frequency, payment dates, negative returns, annual Modelo 190 reconciliation and certificates. Trigger phrases include Modelo 111, retenciones profesionales, retención siete por ciento, retención quince por ciento, certificado de retenciones, perceptor, ingreso a cuenta, declaración negativa and autoliquidación complementaria. Obtain the paid-income register, recipient tax status, signed reduced-rate evidence, payroll calculations and accepted earlier filings. Corporate service invoices, property rents, capital income and ordinary non-resident payments require their own correctly classified route."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/es-modelo-111"
  jurisdiction: "ES"
  tax_year: "2026"
  last_updated: "2026-10-28"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Spain: Modelo 111 and recipient reconciliation v1.2

Compute the payer's 2026 IRPF withholding remittance from payments made, then reconcile Modelo 111 with recipient records, Modelo 190 and certificates. This revision is sourced from the law; independent whole-pack review is pending and no accountant has signed it off.

## Who this applies to

[RIRPF art. 76](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a76) makes legal persons/entities, business individuals paying in their activity and the specified non-resident payers withholding agents when they pay subject income. A private consumer paying outside an economic activity is not brought into the ordinary business-payer rule merely by receiving a professional invoice. A foreign employer without a Spanish permanent establishment can still have employment-withholding duties under art. 76.1.d; do not assume that absence of a PE removes every withholding duty.

[Orden EHA/586/2011 art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948#a2) puts the following in Modelo 111: employment; the listed professional, agricultural/livestock, forestry and specified modules income; the listed rights/assistance/leasing income **when from economic activities**; subject prizes; public-forest exploitation gains; and the specific art. 92.8 image-right payment on account. Other withholding belongs in the form for its actual income category. This is not a return for every payment bearing the word retención.

An ordinary service invoice from an SL/SA taxed under corporate tax is not an individual's professional IRPF income merely because the company is an SLP or its work is professional. Determine the recipient's legal/tax status, including any income-attribution entity, before selecting IRPF ([LIRPF arts. 8/27](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a8); [LIS arts. 4/7](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328#a7)). Corporate, capital-income, property-rental and ordinary non-resident withholding have separate applicable routes. Use [spain-payroll](spain-payroll.md) for employee rate computation and [es-estimated-tax](es-estimated-tax.md) for the professional's own instalments.

## Rates, bands and thresholds

All figures below apply to the relevant **2026 payments**, subject to the stated eligibility and territorial rules.

| Income/classification | Rate or test | Official source |
|---|---|---|
| Ordinary professional activity | 15% of gross subject income paid | [RIRPF art. 95.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Starting professional activity | 7% in start tax period and following two, if no professional activity in the year before the start date and signed communication retained | [Art. 95.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Specified artistic professional activities | 7% if preceding-year qualifying gross income <15,000 and >75% of total gross work/economic income, with signed communication; other listed 7% cases also apply | [Art. 95.1.a–d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Agriculture/livestock | 2%; pig-fattening/poultry 1%; exclude statutory subsidies/indemnities | [Art. 95.4](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Forestry activity | 2%, excluding statutory subsidies/indemnities | [Art. 95.5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Listed business activities in objective assessment | 1%, subject to exact IAE list and communicated direct-assessment exclusion | [Art. 95.6](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Ordinary employment | Personalised annual/recalculated rate, not professional 15% | [Arts. 80–87](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80) |
| Director/board office | 35%; 19% where last completed payer tax-period turnover <100,000, annualised if short | [Art. 80.1.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80) |
| Courses/conferences classified as employment | 15% | [Art. 80.1.4](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80) |
| Other listed rights/assistance/leasing income | 19%; intellectual property has 15% and specified 7% exceptions; direct image exploitation 24% | [Art. 101](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a101) |
| Special image-right attribution payment on account | 19%, distinct from the direct exploitation rate | [Art. 107; LIRPF art. 92.8](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a107) |

The start concession concerns **professional activity**, not every preceding economic activity, and runs for tax periods, not thirty-six rolling months. Keep the signed eligibility communication; without it, do not apply the startup 7%. The art. 95.1 territorial reduction is 60% where the income actually qualifies under LIRPF art. 68.4. La Palma's 2026 extension has its dated withholding start under [DA 57](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-8); do not infer territorial relief from the invoice address alone.

## The base

### Payment register and subject amount

[RIRPF art. 78](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a78) generally triggers withholding when income is **paid or credited**, not merely when the invoice is dated. For every payment keep payer/recipient NIF and legal status, subject category, gross income, VAT separately, payment date, rate evidence, cash withholding or payment on account, and the return period. Reconcile the subject income and remittance with the liability ledger and bank settlement. An unpaid invoice is not automatically included in that period's 111.

For an ordinary professional invoice, apply the rate to gross professional income, excluding separately charged VAT. Do not reduce the subject professional fee by the recipient's own expenses, employee Social Security or tax instalments. Do not exclude an amount merely because a professional invoice labels it materials, travel or goods: classify the actual service, accessory supply and genuine third-party disbursement before deciding its income treatment ([RIRPF art. 95.1–2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95); [LIRPF arts. 27/28](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a28)).

For a cash fee F with VAT V and withholding H, `supplier_cash = F +V −H`; credit F as gross income/expense in the relevant records and H as the payer's withholding liability, not a fee discount. A partial payment needs its actual gross-fee and VAT allocation; do not apply the rate to the net bank transfer as though it were gross professional income.

For in-kind employment use [RIRPF art. 102](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a102), and for in-kind economic activity apply its rate to market value under [art. 104](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a104). Keep the valued benefit and the payment on account separate. The tax-certificate treatment of employer/payer-borne payment on account under [LIRPF art. 43.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a43) must not cause the same amount to be added twice to a 111 value box.

### Map and total the return

Use the statutory form in [Orden EHA/586/2011 annex I](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948) and the [current AEAT instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/pagos-cuenta/modelo-111-reten_____moniales-imputaciones-renta-autoliquidacion_/instrucciones.html). Count **distinct recipients within each cash/in-kind category**, not invoices or payroll months. A recipient can appear in both relevant cash and in-kind counts; deduplicate inside each count.

| Category | Recipient count | Gross cash/value | Withholding/payment on account |
|---|---:|---:|---:|
| Employment, cash | 01 | 02 | 03 |
| Employment, in kind | 04 | 05 | 06 |
| Economic activities, cash | 07 | 08 | 09 |
| Economic activities, in kind | 10 | 11 | 12 |
| Subject prizes, cash | 13 | 14 | 15 |
| Subject prizes, in kind | 16 | 17 | 18 |
| Public-forest exploitation gains, cash | 19 | 20 | 21 |
| Same gains, in kind | 22 | 23 | 24 |
| Special art. 92.8 image-right payments | 25 | 26 | 27 |

`box28 = box03 +box06 +box09 +box12 +box15 +box18 +box21 +box24 +box27`. Box 29 is used **only for a complementary return**, for the earlier return result(s) for the same taxpayer/year/period. `box30 = box28 −box29`. A complementary return restates the **whole corrected period**, identifies the earlier receipt and pays the incremental result; it does not contain only the newly found invoice ([order art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948#a9)). Do not net an overpayment in another period or use a negative supplementary return as a refund request.

If subject income was paid but the law correctly produced zero withholding, file a **negative 111 with the relevant recipients and income populated**. If no subject income was paid, do **not** file an empty all-zero 111 merely because the payer was registered. Reconcile census cessation/restart obligations using the current census route. The instruction page's historical reference to Modelo 037 does not establish that it remains an available 2026 form ([RIRPF art. 108.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108); [order art. 3.3](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948#a3)).

### Annual reconciliation and recipient's tax

Reconcile the year's 111 withholding/payment-on-account totals to recipient-level **Modelo 190**, using the correct current category/subcategory and any required exempt-income records. Its information population is broader than just positive withholdings. Check recipient identity, cash/in-kind amounts, withheld amounts, applicable reductions and employment circumstances; do not use invoice count as recipient count ([RIRPF art. 108.2–3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108); [190 order arts. 2/4 and annex II](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18567)).

The payer's 111 is separate from the recipient's annual IRPF and Modelo 130. The recipient reports gross income and their applicable tax credits; the payer's failure to remit does not turn the net bank transfer into gross income. Check [LIRPF art. 99](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a99) for a disputed withholding credit rather than inventing a deposit prerequisite. [es-estimated-tax](es-estimated-tax.md) gives the direct-assessment instalment computation and the professional **70% prior-year subject-income test**, including the startup-period rule; 111 registration is not an exemption from the recipient's tax.

## Deadlines and filing

| Obligation | Timing/rule | Official source |
|---|---|---|
| Quarterly 111 | First twenty calendar days of April/July/October/January for preceding quarter; Q4 2026 is filed in January 2027 | [RIRPF art. 108.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108), [111 order art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948#a3) |
| Monthly 111 | First twenty calendar days of next month under the applicable large-company/public-administration tests; not headcount | [RIRPF art. 108.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108) |
| Ordinary turnover trigger | RIVA art. 71.3.1 prior-year operations >6,010,121.04; also check art. 71.3.2 and art. 108 public-budget >6 million cases | [RIVA art. 71](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a71), [RIRPF art. 108](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108) |
| Non-working final day | Next working day | [111 order art. 3.1](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948#a3) |
| Direct debit in 2026 | Quarterly general cut-off 15 January/April/July/October; monthly dates vary with the official calendar | [AEAT 2026 payment calendar](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html) |
| Electronic Modelo 190 | 1–31 January of following year, subject to non-working-day/calendar rules | [190 order art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18567#a5) |
| Recipient certificate | Available before the recipient's IRPF return period opens, not a universal 1 February deadline | [RIRPF art. 108.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108) |

The current [2026 calendar](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html) expressly gives July 2026 monthly 111 **20 August**, with direct debit through **17 August**. Do not carry forward the older form-order July/September exception or assume every debit cut-off is the 15th. Verify the 2027 calendar for Q4/annual filings when published; the 2026 calendar does not establish next year's operational cut-offs.

**Legislative bridge for the July return.** [RD 960/2013 article Segundo.Tercero.Ocho](https://www.boe.es/buscar/doc.php?id=BOE-A-2013-12771) replaced RIRPF article 108.1 **with effects from 1 January 2014**, under the express heading of article Segundo.Tercero. The replacement requires monthly declaration and payment in the first twenty calendar days of the following month and contains no separate July exception; its IRPF preamble also expressly explains the removal of that exception. That later regulatory schedule, [current article 108](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108) and the actual 2026 calendar support July 2026 filing by 20 August. Original [EHA/586/2011 article 3](https://www.boe.es/buscar/doc.php?id=BOE-A-2011-4948) still prints the older July/August–September wording: it is preserved as historical text, not represented as expressly rewritten by RD 960/2013. The current August result is therefore supported by the identified replacement, rather than a missing legislative source or a presumed continuation of the older form-order exception.

Select electronic filing under current [Orden HAP/2194/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-12385) rules; an SL/SA's quarterly frequency does not make paper filing available. Save the accepted declaration, receipt/CSV and separate successful payment evidence. An NRC proves payment, not by itself a filed return; an accepted direct-debit instruction is not proof a later bank debit succeeded. Withholding debts are excluded from ordinary deferral/instalment under [LGT art. 65.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a65).

## Penalties and interest

| Situation | Statutory treatment | Official source |
|---|---|---|
| Unprompted late return with amount due, up to twelve months | 1% plus 1% for each complete month late, subject to statutory conditions | [LGT art. 27.2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| More than twelve months | 15%, plus the specified interest from after twelve months until filing; test art. 27.5 reduction separately | [Art. 27](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| Under-remitted tax outside that voluntary route | Classify art. 191 conduct, amount and withholding-specific seriousness; no automatic universal 150% | [Art. 191](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a191) |
| Required nil return late without economic loss | Baseline 200; half if filed without prior demand, before other applicable reductions | [Art. 198.1–2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198) |
| Annual information return late | Baseline 20 per relevant person/data set, minimum 300 and maximum 20,000; amounts and limits halved without prior demand | [Art. 198.1–2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198) |

Collection surcharges and interest have their own triggers under [LGT arts. 26/28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a28). A prior AEAT demand does not create a simple delay-based 5%/10%/15%/20% penalty ladder. Establish notification, filing/payment dates, loss and the relevant conduct before calculating. A period with no obligation is not a late required nil return.

## Cross-border points

Classify the recipient as resident IRPF, non-resident IRNR, or another tax subject and identify the payer's withholding duty. Ordinary non-resident professional payments use the applicable IRNR/treaty computation and return, rather than automatically Modelo 111 or a blanket 24%. The **special image-right art. 92.8** route is an express 111 exception involving payments to non-residents, so do not apply an absolute “no foreign payment in 111” rule ([111 order art. 2.f](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948#a2)).

Ceuta/Melilla and the dated La Palma treatment require actual income entitlement and timing, not nationality. Foral administration selection must be established under the relevant territorial rules; these common-territory boxes do not prove the state is entitled to every remittance. Keep those unresolved territorial cases separate from a supported ordinary resident-payment computation.

## Two worked examples that recompute

### 1. Professional cash invoice

A resident individual professional is paid a hypothetical **1,000 fee** for an ordinary service subject to general 21% VAT, with 15% IRPF and no reduced/territorial treatment. VAT is 210; withholding is 150; supplier cash is **1,060**. This payment contributes one recipient, 1,000 gross income and 150 withholding to boxes **07/08/09**. The payer remits the 150 through 111, separately from VAT ([RIRPF art. 95.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95); [LIVA art. 90](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a90); [111 statutory form](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948)).

```oa-check
name: Spain 2026 paid professional invoice and withholding remittance
inputs:
  fee: 1000
steps:
  vat: fee * 0.21
  withholding: fee * 0.15
  invoice_total_before_withholding: fee + vat
  supplier_cash: invoice_total_before_withholding - withholding
  payer_cash_total: supplier_cash + withholding
expected:
  vat: 210
  withholding: 150
  supplier_cash: 1060
  payer_cash_total: 1210
```

### 2. Mixed payroll/professionals, repeated recipient and complementary return

For a hypothetical quarter, one ordinary employee receives three 2,500 payments and has 410.50 withheld each time, using the 30,000 annual example in [spain-payroll](spain-payroll.md). Professional A, eligible for startup 7% with signed evidence, receives fee payments 1,000 and 500. Professional B receives 2,000 at 15%. Another 900 professional invoice remains unpaid and is excluded from this period. There are **two**, not three, professional cash recipients.

Boxes 01/02/03 are 1 /7,500 /1,231.50. Boxes 07/08/09 are 2 /3,500 /405. All other withholding/payment-on-account boxes are zero; box 28 is **1,636.50**. If an earlier 111 for the same period had result 1,500 and that was paid, the corrected complementary return restates those totals, puts 1,500 in box 29, identifies the earlier receipt and has box 30 **136.50**. Any lateness is assessed separately; do not add an invented penalty to box 30 ([RIRPF arts. 78/95](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a78); [111 order art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948#a9)).

```oa-check
name: Spain 2026 payment register to complementary Modelo 111
inputs:
  monthly_salary: 2500
  monthly_salary_withholding: 410.50
  professional_a_first_fee_paid: 1000
  professional_a_second_fee_paid: 500
  professional_b_fee_paid: 2000
  unpaid_fee: 900
  earlier_return_result: 1500
steps:
  box02: monthly_salary * 3
  box03: monthly_salary_withholding * 3
  professional_a_paid: professional_a_first_fee_paid + professional_a_second_fee_paid
  box08: professional_a_paid + professional_b_fee_paid
  excluded_unpaid_amount: unpaid_fee
  box09: professional_a_paid * 0.07 + professional_b_fee_paid * 0.15
  box28: box03 + box09
  box29: earlier_return_result
  box30: box28 - box29
expected:
  box02: 7500
  box03: 1231.50
  box08: 3500
  excluded_unpaid_amount: 900
  box09: 405
  box28: 1636.50
  box29: 1500
  box30: 136.50
```

## Ask the client first

1. Which payer, tax administration and monthly/quarterly withholding obligation apply?
2. Which recipients were actually paid or credited, on what dates, and what are their legal/tax status and gross subject amounts?
3. What signed startup/artistic/territorial evidence supports a reduced rate, and what professional activity existed before the start date?
4. Which cash, VAT, in-kind value and payment-on-account records reconcile the invoices/payroll with the bank and liability ledger?
5. What accepted earlier returns, results, receipts, payments and AEAT notices affect correction and lateness?
6. What recipient records and current 190 keys support the annual summary and certificates?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [RIRPF, RD 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 74–80, 95/101/102/104/107/108: payer, income, payment trigger, rates, in-kind and reporting | 2026-10-26 |
| [LIRPF, Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), [LIS](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328), [LIVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740), [RIVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925) | Taxpayer/income status, credit, in-kind valuation, general VAT example and filing-frequency cross-reference | 2026-10-26 |
| [Orden EHA/586/2011](https://www.boe.es/buscar/act.php?id=BOE-A-2011-4948), [AEAT 111 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/pagos-cuenta/modelo-111-reten_____moniales-imputaciones-renta-autoliquidacion_/instrucciones.html) | Scope, statutory form, counts, correction, nil-payment distinction; old 037/July references not carried forward | 2026-10-26 |
| [AEAT 2026 payment calendar](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [Orden HAP/2194/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-12385) | Current filing/payment dates, including July, and electronic channels | 2026-10-26 |
| [Orden EHA/3127/2009](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18567) | Modelo 190 population/design and electronic January filing window | 2026-10-26 |
| [LGT, Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Voluntary late correction, collection, withholding debt deferral exclusion and conduct-based penalties | 2026-10-26 |
| [Original RD960/2013 IRPF preamble/article Segundo.Tercero.Ocho](https://www.boe.es/buscar/doc.php?id=BOE-A-2013-12771), [current RIRPF108](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108) | Full108.1 replacement with effects1January2014; monthlyJuly exception removed in later regulation, distinguished from unchanged oldformorder wording and current2026calendar | 2026-10-28 |

**Not yet confirmed:** 2027 operational/direct-debit dates; case-specific foral allocation, non-resident treaty relief and disputed withholding-credit evidence. Special prize, public-forest and image-right transactions require their full underlying eligibility/base computation before using the mapped boxes. Independent whole-pack review remains outstanding.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-28. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `es-modelo-111` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/es-modelo-111. If neither is available, confirm every figure against the official source pages cited above before relying on it.
