---
name: au-forex-gains-losses
version: 1.4
description: >
  Use this guide for Australian foreign currency gains and losses under Division
  775 of the ITAA 1997. It covers realised foreign exchange amounts, foreign
  currency bank accounts and the treatment of crypto assets such as stablecoins
  within the stated scope. Use it when an accountant needs to establish the
  relevant transaction, source rule, timing and supporting records before
  preparing a computation. The method, client questions and refusal conditions
  must be read together. Confirm the applicable period and cited provisions
  before relying on a result, and refer unresolved classifications for qualified
  review.
jurisdiction: AU
category: international
tax_year: 2026
last_updated: 2026-11-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Foreign currency forex realisation gains and losses under Division 775 in Australia v1.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Division 775 of the *Income Tax Assessment Act 1997* (ITAA 1997) brings specified foreign currency gains and losses to account when a forex realisation event happens, even if the monetary amounts are never converted into Australian dollars. It can affect individuals, trusts, partnerships, companies and funds. Holding foreign currency or recording a book revaluation alone does not establish an assessable gain or deductible loss.

The ordinary Australian dollar method below covers identified transactions and qualifying accounts. Financial arrangements subject to Division 230 (TOFA), functional currency under Subdivision 960-D and complex hedging arrangements require separate work. Subdivision 960-C translation still applies: translate the constituent amounts before calculating an Australian dollar gain or loss under subsection 960-50(4). [ATO overview](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses), [s 960-50](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/960-50).

Rules were checked on 3 November 2026 against the targeted sources below. The Register identifies compilation 268, effective 1 October 2026 to 1 December 2026, as current on that date. Examples using 2026-27 are conditional illustrations of those rules, not confirmation of law for every later transaction in that year. Recheck the applicable version, commencement and application provisions for the actual event. Historical transitional choices and taxpayer eligibility remain fact dependent.

## Ask the client first

- What currency, legal right or obligation is involved? Obtain the contracts, invoices, bank statements, acquisition and settlement dates, amounts and exchange rate sources. Identify the tax recognition time separately from payment.
- Is the item private or domestic, income producing, exempt income related or non-assessable non-exempt income related? Identify the CGT asset and its character before applying any personal-use threshold.
- Was the currency, right or obligation acquired or incurred before the applicable commencement date, or under a qualifying earlier contract? Obtain any transitional election and loan extension documents.
- Does Division 230 apply? Obtain all relevant elections. An accounting revaluation does not prove a tax election.
- For each account, is it a credit card account or held primarily to facilitate transactions? An account primarily holding money as an investment is not a qualifying forex account. Obtain written elections, coverage and effective dates.
- For the limited balance election, obtain all elected accounts, separate aggregate credits and debits, prescribed translation rates and complete increased balance period history, including both sides of year end.
- For crypto assets, establish their legal character. A foreign currency peg does not establish that a stablecoin is foreign currency.

## The method, step by step

### 1. Confirm currency and regime

Section 995-1 excludes Australian currency, digital currency and anything prescribed for that paragraph from foreign currency. Digital currency has the GST Act meaning. TD 2014/25 addresses bitcoin and applies to income years before 1 July 2021; its reasoning does not determine every crypto asset's current treatment. See the crypto section below. Financial arrangements subject to Division 230 are dealt with under that Division rather than Division 775. [s 995-1](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1), [ATO overview](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses).

### 2. Identify the event, time and separate transaction legs

The following is an event map, not a substitute for each provision's conditions, exclusions and tax recognition table. Part of a right or obligation can also be relevant.

| Event | Relevant change | Main provision |
| --- | --- | --- |
| 1 | Disposal of foreign currency **or a right to receive foreign currency** to another entity; this is modified CGT event A1 | s 775-40 |
| 2 | Ceasing to have a qualifying right to receive foreign currency, otherwise than by disposing of it under event 1 | s 775-45 |
| 3 | Ceasing to have an obligation to receive foreign currency | s 775-50 |
| 4 | Ceasing to have an obligation to pay foreign currency | s 775-55 |
| 5 | Ceasing to have a right to pay foreign currency | s 775-60 |

Event 1 occurs on disposal, rather than automatically using the usual CGT contract date. Events 2 to 5 occur when the relevant right or obligation ceases. Determine which statutory class the right or obligation belongs to before selecting its tax recognition time. [ss 775-40 to 775-60](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html), [ATO events](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/forex-realisation-events).

Apply the specific option and forward contract counting rules in subsections 775-65(1) to (3) first. The residual rule in subsection (4) applies only where multiple events happen **at the same time in relation to the same rights or obligations**. It does not collapse every event arising from separate legs of one payment. The no-double-inclusion and no-double-deduction rules also concern the same gain or loss, not all distinct gains and losses in a transaction. [s 775-65](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-65), [ss 775-15 and 775-30](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html).

### 3. Calculate the event-specific exchange component

Use a consistent quotation convention. A rate expressed as foreign currency per A$1 requires **division** to obtain Australian dollars. Retain the source and date of each rate; do not substitute an accounting average without an applicable tax translation rule.

| Event | Calculation starting point |
| --- | --- |
| 1 | Modified CGT gain or loss attributable to a currency exchange rate effect. Under s 775-40(9), substitute event-time market value if actual capital proceeds differ from that value. Do not universally use actual cash proceeds. |
| 2 | Amount received compared with the forex cost base of the right at its statutory tax recognition time (ss 775-45 and 775-85). |
| 3 | Foreign currency received compared with the net costs of assuming the obligation, using the event's tax recognition rule (ss 775-50 and 775-100). |
| 4 | Amount paid compared with the proceeds of assuming the obligation at its statutory tax recognition time (ss 775-55 and 775-95). |
| 5 | Amount paid compared with the forex entitlement base of the right, using the event's tax recognition rule (ss 775-60 and 775-90). |

Only the component attributable to a currency exchange rate effect is a forex realisation gain or loss. Check non-arm's-length, constructive receipt/payment and set-off rules where relevant; the simple cases below do not certify those arrangements. For currency acquired through event 2 or 3, s 775-125 replaces the first element of both its CGT cost base and reduced cost base with market value when received; other allowable elements are not replaced. [ss 775-40 to 775-125](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html), [ATO common transactions](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/common-forex-transactions).

### 4. Trace account rights and obligations

A depositor's credit balance represents rights to receive foreign currency from the bank. A withdrawal can end those rights under event 2; paying down a debit balance can end a payment obligation under event 4. Depositing or disposing of separately held currency can also require event 1 analysis. Do not automatically count both event 1 and event 2 for the same bank right.

Paying a trade payable from a foreign currency bank account can end **2 distinct positions**: the trade payment obligation (event 4) and a bank right (event 2). Calculate each eligible leg and then apply the actual overlap rules. The ATO says FIFO usually applies to foreign currency accounts; confirm the appropriate identification method and records rather than treating FIFO as a universal statutory rule. [ATO common transactions](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/common-forex-transactions), [ATO events](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/forex-realisation-events).

### 5. Apply exceptions separately to gains and losses

**Private or domestic amounts.** Under s 775-15(2), a private or domestic gain is excluded unless a table item applies. Those items concern event 1 or 2 on currency or a right where the relevant CGT gain would be taken into account, certain event 2 rights arising from a CGT realisation and event 4 obligations for acquiring a CGT asset. Read the exact item and its CGT condition. Section 775-30(2) has a different, narrower loss table: certain event 2 rights arising from CGT realisations and event 4 acquisition obligations. It has **no event 1 table exception**. An assessable private gain does not establish deductibility of an equivalent private loss. A personal account label alone does not establish private character. [s 775-15](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-15), [s 775-30](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-30).

The **A$10,000** figure belongs to the personal-use CGT asset gain exemption in subsection 118-10(3): the first element of cost base must be **A$10,000 or less**. Establish that the asset is a personal-use asset and that the relevant CGT conditions apply before using it in s 775-15. It is not a general forex exemption for every withdrawal, account or transaction. Personal-use capital losses are disregarded under s 108-20. An edited private ruling cannot establish another taxpayer's character or entitlement. [s 118-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-10), [s 108-20](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-20).

**Exempt and non-assessable non-exempt (NANE) income.** Check ss 775-20, 775-25 and 775-27 before including a gain. Section 775-27 requires that the hypothetical corresponding loss would be disregarded under s 775-35. For losses, s 775-35(1) covers events 1, 2 and 5 to the extent made in gaining or producing exempt or NANE income. For events 3, 4 and 6, subsection (2) additionally requires that the obligation does not give rise to a deduction. Do not treat every such gain as assessable or every loss as deductible. [ss 775-20 to 775-35](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html).

**Commencement.** The applicable commencement date is generally the first day of the 2003-04 income year, or the first day of 2004-05 where the substituted 2003-04 year began before 1 July 2003 (s 775-155). Section 775-165 can disregard events on earlier acquired currency, rights and obligations, including relevant rights or obligations arising under qualifying pre-commencement contracts. Later loan extensions can remove the earlier-contract protection for later rights **and obligations**. Obtain the contracts and any valid s 775-150 transitional election. Its historical written election deadline and irrevocability are not a new unrestricted choice for a 2026 transaction. [s 775-155](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-155), [s 775-165](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-165), [s 775-150](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-150).

**Short-term capital transactions.** Sections 775-70 and 775-75 replace ordinary forex treatment for specified CGT and depreciating asset transactions unless a valid s 775-80 choice applies. For qualifying CGT disposal rights, foreign currency becoming **due for payment within 12 months** and the specified tax recognition table item can instead produce CGT event K10 (gain) or K11 (loss). For qualifying CGT acquisition obligations and specified later cost base elements, the corresponding due-date and tax recognition conditions can reduce cost base/reduced cost base for a gain or increase them for a loss. The test is not merely the time between actual payments. Depreciating asset first-cost rules use a 24 month window beginning 12 months before holding starts; later-cost and project pool rules have their own conditions and adjustments. Do not apply one blanket 12 month rule to them. A s 775-80 choice must satisfy its statutory written deadline (or a longer period allowed by the Commissioner), is irrevocable and is not a freely available new annual opt-out. [s 775-70](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-70), [s 775-75](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-75), [s 775-80](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-80).

### 6. Check the limited balance election

A qualifying forex account is denominated in a particular foreign currency and is either a credit card account or held primarily to facilitate transactions. An account primarily holding money as an investment is outside that definition. A valid written s 775-230 election identifies the covered accounts; check its effective period, additions, removals and withdrawal. An ADI or non-ADI financial institution cannot make that election. [s 995-1](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1), [s 775-230](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-230), [ATO elections](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/in-detail/forex-elections).

Under s 775-245, aggregate all elected account **credit balances separately from debit balances**, expressing debits as positive amounts for this test. Each total must be **no more than A$250,000**, with no netting. Translate using the average exchange rate for the third month preceding the income year: **April 2026 for a 1 July 2026 start**, rather than the event spot rate.

Buffering is conditional on the statutory increased balance periods in s 775-245(2) and (3), involving totals above A$250,000 but no more than A$500,000. Check both aggregate totals and the complete chronology; do not claim protection for an untested balance above A$500,000.

| Period history | Buffer available under s 775-245(3) |
| --- | --- |
| First increased balance period, 15 days or less, with no year-end continuation | Whole period (item 1) |
| First period continuing from the prior year, combined duration 15 days or less | Combined period (item 2) |
| First period longer than 15 days, including a year-end continuation | First 15 days only, using one combined clock across year end (items 3 and 4) |
| Second period, **only if item 1 or 2 applied to the first** | Whole period if 15 days or less; first 15 days if longer (items 5 and 6) |
| A second period after a first period covered only by item 3 or 4, or a third period | No fresh buffer under this table |

Thus a longer breach does not necessarily remove protection for its first 15 days. Nor does every year supply 2 fresh 15 day allowances.

Section 775-250 disregards specified event 2 and 4 gains/losses and the exchange component of CGT event C1/C2 **only when its conditions hold at the event time**. It does not exempt every currency disposal or event 1 on a deposit. Starting to pass the test can itself cause notional event 2 or 4 realisation under s 775-255; obtain specialist entry/exit calculations rather than simply erasing earlier exchange movements. [s 775-245](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-245), [s 775-250](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-250), [s 775-255](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-255).

### 7. Distinguish the retranslation regimes

The ordinary **s 775-270** choice is a written choice for a qualifying forex account. Do not import the TOFA common audited-financial-report requirements into this separate account choice. It does not apply where a Subdivision 230-D foreign exchange retranslation election is in effect for that account. It continues until the account is no longer held, ceases to qualify or an effective withdrawal occurs. Section 775-275 permits written withdrawal. Whilst the choice is effective, s 775-280 disregards the specified event 2/4 gains/losses and C1/C2 exchange component; it does not disregard every independent transaction leg.

Under **s 775-285 (event 8)**, calculate for the continuous retranslation period within the income year:

**Retranslation amount = closing balance − opening balance − total deposits + total withdrawals**, all translated to Australian dollars.

Express account debit balances as **negative** amounts here, unlike the positive debit totals in the limited balance test. Translate opening balance at the period start, or the previous period's end rate for contiguous periods; translate closing balance at this period's end and each deposit or withdrawal when it occurs. Deposits include amounts paid or transferred in; withdrawals include amounts paid, advanced, drawn or transferred out. A positive result is the forex gain; reverse a negative result to report the positive amount of forex loss. A zero result creates no positive or negative event 8 amount. Closing less opening alone wrongly treats cash movements as exchange gains or losses. [s 775-270](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-270), [s 775-280](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-280), [s 775-285](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-285).

The **Subdivision 230-D / 775-F** retranslation regime is separate and can involve event 9. Its eligibility, scope and cessation rules are not worked through here. Section 775-290 is its introductory guide, not the ordinary s 775-270 choice's cessation provision. Refer TOFA elections for specialist review. [s 775-290](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-290).

### 8. Return and reconcile the supported treatment

Only after classification, timing, overlap, exemptions and elections are resolved should the eligible gain be included under s 775-15 or loss deducted under s 775-30. Reconcile the tax result to opening balances, deposits, withdrawals, settlements and closing statements. Record each event, tax recognition time, rate source, calculation, exception and election considered, plus differences from book revaluations. Obtain the taxpayer's actual return form, reporting label, payment and lodgment dates separately; the sources checked here do not establish those procedural answers.

### Stablecoins and other crypto assets

For an income year that includes 1 July 2021 and later income years, s 995-1 excludes digital currency from foreign currency and adopts the GST Act meaning (Treasury Laws Amendment (2022 Measures No. 4) Act 2023 Sch 2 item 15(2)). TD 2014/25 records that amendment in paragraph 2 and applies to earlier income years. Its bitcoin conclusion must be read within that temporal and asset scope.

GST Act s 195-1 defines digital currency through cumulative conditions: fungibility, use as consideration, public availability without substantial restrictions, the specified denomination test, value not depending on or derived from something else and no entitlement to a particular thing beyond an incidental holding/payment entitlement. It also excludes certain financial supplies. Read the full definition before applying the exclusion. [GST Act s 195-1](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/195-1), [TD 2014/25](https://www.ato.gov.au/law/view/document?docid=TXD%2FTD201425%2FNAT%2FATO%2F00001).

The ATO's GST guidance expressly says a stablecoin pegged to another asset, such as fiat currency, is not digital currency for GST purposes. Because s 995-1 adopts that definition, the digital currency exclusion alone does not settle such an asset's Division 775 classification. It must still be a currency in the relevant sense and satisfy the applicable event and regime rules. The ATO's general crypto guidance says crypto assets are not money for tax purposes and lists USDC as a stablecoin; investment holdings are generally CGT assets and business holdings can be on revenue account. These sources do not establish a universal Division 775 outcome for every stablecoin. Obtain the legal terms and refer unresolved classification, TOFA and CGT/revenue interactions. A price peg or a bitcoin determination is insufficient. [ATO GST and digital currency](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-crypto-assets/gst-and-digital-currency), [ATO crypto assets](https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/what-are-crypto-assets).

## Worked cases

These fictitious cases test arithmetic under express legal assumptions. They do not prove an actual taxpayer's entitlement. Unless varied, assume Australian residence and AUD tax reporting, post-commencement transactions, taxable business income/expense, exchange-only changes, no charges or other cost adjustments, no TOFA, no functional currency choice and no applicable election, private/exempt/NANE exclusion or short-term capital rule. Each tax recognition time and right/obligation classification must be independently established. Rates are foreign currency per A$1. Alternative outcomes are separate scenarios, not amounts to combine.

For buffer and retranslation cases, the particular qualifying-account and valid-election facts override the no-election default. Period examples are conditional on the law applicable to the actual period.

### 1. Income receivable: loss or gain

An Australian resident business recognises USD12,000 ordinary service income at 0.75 USD/AUD. Its qualifying receivable later ceases on receipt at either 0.80 or 0.60. The tax recognition table establishes the original A$16,000 forex cost base. These are alternative outcomes: event 2 gives a A$1,000 loss or A$4,000 gain, subject to the stated general assumptions.

```oa-check
name: income-receivable-exchange
tolerance: 0.000001
inputs:
  usd: 12000
  recognition_rate: 0.75
  strong_aud_rate: 0.8
  weak_aud_rate: 0.6
steps:
  - cost_base: usd / recognition_rate
  - receipt_low: usd / strong_aud_rate
  - receipt_high: usd / weak_aud_rate
  - loss: cost_base - receipt_low
  - gain: receipt_high - cost_base
expected:
  cost_base: 16000
  receipt_low: 15000
  receipt_high: 20000
  loss: 1000
  gain: 4000
```

### 2. Operating payable: reverse the receivable direction

A business incurs a USD12,000 deductible operating service expense at 0.75 USD/AUD. Its payment obligation is extinguished at either 0.80 or 0.60. The event 4 proceeds are A$16,000 at the established tax recognition time. Paying A$15,000 gives a A$1,000 gain; paying A$20,000 gives a A$4,000 loss. This is not a capital acquisition subject to short-term matching.

```oa-check
name: operating-payable-exchange
tolerance: 0.000001
inputs:
  usd: 12000
  recognition_rate: 0.75
  strong_aud_rate: 0.8
  weak_aud_rate: 0.6
steps:
  - proceeds: usd / recognition_rate
  - payment_low: usd / strong_aud_rate
  - payment_high: usd / weak_aud_rate
  - gain: proceeds - payment_low
  - loss: payment_high - proceeds
expected:
  proceeds: 16000
  payment_low: 15000
  payment_high: 20000
  gain: 1000
  loss: 4000
```

### 3. One payment, 2 distinct positions

A business pays a USD10,000 operating payable from its USD credit account. The obligation was recognised at 0.50 USD/AUD; the identified bank right cost 0.625 USD/AUD; settlement is at 0.80. Event 4 produces a A$7,500 gain on the payable and event 2 a A$3,500 loss on the separate bank right, giving net A$4,000. Section 775-65(4) does not collapse these distinct positions merely because they end together. No separate physical-currency disposal is assumed.

```oa-check
name: separate-payable-and-bank-right
tolerance: 0.000001
inputs:
  usd: 10000
  payable_rate: 0.5
  deposit_rate: 0.625
  settlement_rate: 0.8
steps:
  - payable_proceeds: usd / payable_rate
  - bank_cost: usd / deposit_rate
  - settlement: usd / settlement_rate
  - payable_gain: payable_proceeds - settlement
  - bank_loss: bank_cost - settlement
  - net_gain: payable_gain - bank_loss
expected:
  payable_proceeds: 20000
  bank_cost: 16000
  settlement: 12500
  payable_gain: 7500
  bank_loss: 3500
  net_gain: 4000
```

### 4. Identify a partial account withdrawal

For this ordinary business credit account, records and the applicable identification method support FIFO. Deposits of USD1,000 at 0.50 and USD1,000 at 0.80 create rights with costs A$2,000 and A$1,250. A USD1,500 withdrawal at 0.75 uses the first right and half the second. Event 2 loss is A$625; the remaining USD500 right retains A$625 cost. The case does not make FIFO mandatory for every arrangement.

```oa-check
name: fifo-partial-bank-right
tolerance: 0.000001
inputs:
  first_usd: 1000
  first_rate: 0.5
  second_usd: 1000
  second_rate: 0.8
  withdraw_usd: 1500
  withdraw_rate: 0.75
steps:
  - first_cost: first_usd / first_rate
  - second_cost: second_usd / second_rate
  - second_used: withdraw_usd - first_usd
  - used_cost: first_cost + second_used / second_rate
  - receipt: withdraw_usd / withdraw_rate
  - loss: used_cost - receipt
  - remaining_usd: second_usd - second_used
  - remaining_cost: remaining_usd / second_rate
expected:
  first_cost: 2000
  second_cost: 1250
  second_used: 500
  used_cost: 2625
  receipt: 2000
  loss: 625
  remaining_usd: 500
  remaining_cost: 625
```

### 5. Event 1 uses substituted market value

An identified non-private currency CGT asset of USD10,000 costs A$12,500 at 0.80 USD/AUD. On disposal, its market value at 0.50 is A$20,000, whilst actual proceeds are A$18,000. Assume no further cost-base adjustments, non-arm's-length modifications or exemptions. Section 775-40(9) substitutes market value for this event: the stipulated exchange-only event 1 gain is A$7,500. The A$5,500 actual cash profit is not that calculation. Reconciliation of any remaining CGT/non-forex amount requires separate work.

```oa-check
name: event-one-market-value-substitution
tolerance: 0.000001
inputs:
  usd: 10000
  cost_rate: 0.8
  event_rate: 0.5
  actual_proceeds: 18000
steps:
  - cost: usd / cost_rate
  - market_value: usd / event_rate
  - event_one_gain: market_value - cost
  - cash_profit: actual_proceeds - cost
expected:
  cost: 12500
  market_value: 20000
  event_one_gain: 7500
  cash_profit: 5500
```

### 6. Short-term CGT acquisition adjusts cost

A USD12,000 obligation is incurred to acquire a CGT asset with cost base and reduced cost base A$16,000. Stipulate the conditions in s 775-70(1) table item 2 and s 775-75(1) table item 2, including the relevant tax recognition table item and currency becoming due within 12 months of acquisition. No valid s 775-80 choice applies. Alternative payment rates of 0.80 and 0.60 give a A$1,000 forex gain reducing both bases to A$15,000, or a A$4,000 forex loss increasing both to A$20,000. Do not additionally return that amount as ordinary forex income or deduction. Actual payment timing alone would not establish these conditions.

```oa-check
name: short-term-cgt-cost-matching
tolerance: 0.000001
inputs:
  usd: 12000
  recognition_rate: 0.75
  strong_aud_rate: 0.8
  weak_aud_rate: 0.6
steps:
  - original_base: usd / recognition_rate
  - low_payment: usd / strong_aud_rate
  - high_payment: usd / weak_aud_rate
  - gain: original_base - low_payment
  - loss: high_payment - original_base
  - base_after_gain: original_base - gain
  - base_after_loss: original_base + loss
expected:
  original_base: 16000
  low_payment: 15000
  high_payment: 20000
  gain: 1000
  loss: 4000
  base_after_gain: 15000
  base_after_loss: 20000
```

### 7. A valid historical choice changes that treatment

Use case 6, except the taxpayer is an existing company with a valid, timely written and irrevocable s 775-80 choice in force, verified from its historical records. Sections 775-70 and 775-75 therefore do not apply. Under the stated business/taxable-income assumptions, the alternative A$1,000 gain or A$4,000 loss is returned under the ordinary rules and the A$16,000 asset bases receive no short-term forex adjustment. This does not authorise a new unilateral 2026 opt-out.

```oa-check
name: valid-historical-short-term-opt-out
tolerance: 0.000001
inputs:
  usd: 12000
  recognition_rate: 0.75
  gain_payment_rate: 0.8
  loss_payment_rate: 0.6
steps:
  - asset_base: usd / recognition_rate
  - ordinary_gain: asset_base - usd / gain_payment_rate
  - ordinary_loss: usd / loss_payment_rate - asset_base
expected:
  asset_base: 16000
  ordinary_gain: 1000
  ordinary_loss: 4000
```

### 8. Private gain/loss asymmetry and the inclusive threshold

Assume an identified non-collectable currency holding is the relevant single personal-use CGT asset, acquired after commencement and kept mainly for personal use. Asset identification and aggregation are stipulated, not resolved by this case. USD9,000 acquired at 0.75 USD/AUD has first cost-base element A$12,000, no other costs and no other exemption. Disposal market value at 0.60 gives a A$3,000 gain that would be taken into account for CGT apart from Division 775. Section 775-15(2) table item 1 therefore prevents the private-gain exclusion. An alternative disposal at 1.00 produces an economic loss of A$3,000: private event 1 has no s 775-30(2) table exception, and the personal-use capital loss is also disregarded. For the threshold variant, acquisition at 0.90 instead costs exactly A$10,000; disposal at 0.60 gives a A$5,000 gain disregarded under s 118-10(3), so the private forex gain is excluded. The checker recomputes amounts; these asset and eligibility facts must be established separately.

```oa-check
name: private-currency-and-ten-thousand-boundary
tolerance: 0.000001
inputs:
  usd: 9000
  above_limit_rate: 0.75
  at_limit_rate: 0.9
  gain_rate: 0.6
  loss_rate: 1
steps:
  - above_limit_cost: usd / above_limit_rate
  - at_limit_cost: usd / at_limit_rate
  - gain_proceeds: usd / gain_rate
  - loss_proceeds: usd / loss_rate
  - conditional_assessable_gain: gain_proceeds - above_limit_cost
  - private_economic_loss: above_limit_cost - loss_proceeds
  - excluded_threshold_gain: gain_proceeds - at_limit_cost
expected:
  above_limit_cost: 12000
  at_limit_cost: 10000
  gain_proceeds: 15000
  loss_proceeds: 9000
  conditional_assessable_gain: 3000
  private_economic_loss: 3000
  excluded_threshold_gain: 5000
```

### 9. Separate aggregates and the basic balance boundary

For a 1 July 2026 income-year start, assume the prescribed April 2026 average rates are 0.80 USD/AUD and 0.60 EUR/AUD. Validly elected qualifying accounts have USD100,000 and EUR75,000 credits and a USD16,000 debit. Credits total exactly A$250,000 and debits separately A$20,000, satisfying the inclusive basic amounts. Do not test only the A$230,000 net. An additional USD0.80 credit moves credits to A$250,001, above the basic limit; whether buffering saves the account then needs its full period history.

```oa-check
name: limited-balance-separate-aggregates
tolerance: 0.000001
inputs:
  usd_credit: 100000
  eur_credit: 75000
  usd_debit: 16000
  usd_rate: 0.8
  eur_rate: 0.6
  extra_usd: 0.8
  basic_limit: 250000
steps:
  - credits: usd_credit / usd_rate + eur_credit / eur_rate
  - debits: usd_debit / usd_rate
  - net_balance: credits - debits
  - basic_headroom: basic_limit - credits
  - credits_after_extra: credits + extra_usd / usd_rate
  - excess: credits_after_extra - basic_limit
expected:
  credits: 250000
  debits: 20000
  net_balance: 230000
  basic_headroom: 0
  credits_after_extra: 250001
  excess: 1
```

### 10. A longer first period and an eligible second period

Assume valid elections, all relevant increased balances no more than A$500,000, distinct periods within one income year and no year-end continuation. In history A, the first period lasts 20 days: item 3 preserves 15 days and leaves 5 unbuffered; because item 1 or 2 did not apply, a later 10 day second period gets no fresh buffer. In alternative history B, the first lasts 10 days and qualifies under item 1; a 20 day second period gets its first 15 days under item 6, leaving 5 unbuffered. A third period gets no buffer under this table. These calculations do not establish election validity or entry/exit tax consequences.

```oa-check
name: limited-balance-partial-periods
tolerance: 0.000001
inputs:
  history_a_first_days: 20
  history_a_second_days: 10
  history_b_first_days: 10
  history_b_second_days: 20
  third_days: 10
  buffer_days: 15
steps:
  - a_first_buffered: min(history_a_first_days, buffer_days)
  - a_first_unbuffered: history_a_first_days - a_first_buffered
  - a_second_unbuffered: history_a_second_days
  - b_first_buffered: min(history_b_first_days, buffer_days)
  - b_second_buffered: min(history_b_second_days, buffer_days)
  - b_second_unbuffered: history_b_second_days - b_second_buffered
  - third_unbuffered: third_days
expected:
  a_first_buffered: 15
  a_first_unbuffered: 5
  a_second_unbuffered: 10
  b_first_buffered: 10
  b_second_buffered: 15
  b_second_unbuffered: 5
  third_unbuffered: 10
```

### 11. Year end does not restart the buffer clock

Assume the relevant first increased balance period runs for 8 days to the prior year end and continues for 8 days from the new year start, with the statutory balance conditions throughout. Under item 4 the combined 16 day period has only 15 buffered days: 8 before year end and 7 after, leaving 1 day unbuffered. This is not 2 independent 15 day allowances.

```oa-check
name: limited-balance-year-end-clock
tolerance: 0.000001
inputs:
  prior_year_days: 8
  new_year_days: 8
  buffer_days: 15
steps:
  - combined_days: prior_year_days + new_year_days
  - prior_buffered: min(prior_year_days, buffer_days)
  - new_buffered: min(new_year_days, max(0, buffer_days - prior_year_days))
  - new_unbuffered: new_year_days - new_buffered
expected:
  combined_days: 16
  prior_buffered: 8
  new_buffered: 7
  new_unbuffered: 1
```

### 12. Cash movements alone produce no retranslation amount

Assume a valid ordinary s 775-270 choice is effective throughout the relevant continuous retranslation period. All amounts below have already been translated at their prescribed times and the exchange rate is unchanged. Opening A$100 plus deposits A$80 less withdrawals A$30 gives closing A$150. Section 775-285 produces zero, so there is no positive or negative event 8 amount. Closing less opening alone would wrongly report A$50.

```oa-check
name: retranslation-unchanged-rate
tolerance: 0.000001
inputs:
  opening: 100
  deposits: 80
  withdrawals: 30
  closing: 150
steps:
  - reconciled_closing: opening + deposits - withdrawals
  - retranslation: closing - opening - deposits + withdrawals
  - wrong_shortcut: closing - opening
expected:
  reconciled_closing: 150
  retranslation: 0
  wrong_shortcut: 50
```

### 13. Credit account retranslation includes movements

Assume a qualifying account and valid ordinary choice throughout the continuous retranslation period. Opening credit USD10,000 translates at 0.50 USD/AUD; a USD1,000 deposit at 0.80; a USD2,000 withdrawal at 1.00; closing credit USD9,000 at 0.60. The applicable opening/closing dates and each movement rate are stipulated. Retranslation is negative A$4,250, reported as a positive A$4,250 forex loss, subject to the other rules.

```oa-check
name: credit-account-retranslation
tolerance: 0.000001
inputs:
  opening_usd: 10000
  deposit_usd: 1000
  withdraw_usd: 2000
  opening_rate: 0.5
  deposit_rate: 0.8
  withdraw_rate: 1
  closing_rate: 0.6
steps:
  - closing_usd: opening_usd + deposit_usd - withdraw_usd
  - opening: opening_usd / opening_rate
  - deposits: deposit_usd / deposit_rate
  - withdrawals: withdraw_usd / withdraw_rate
  - closing: closing_usd / closing_rate
  - retranslation: closing - opening - deposits + withdrawals
  - loss: 0 - retranslation
expected:
  closing_usd: 9000
  opening: 20000
  deposits: 1250
  withdrawals: 2000
  closing: 15000
  retranslation: -4250
  loss: 4250
```

### 14. Debit account retranslation uses negative balances

Use the same valid-choice assumptions, with opening debit USD10,000 expressed as negative USD10,000 at 0.50 USD/AUD. A USD2,000 deposit at 0.80 reduces the debt; a USD1,000 withdrawal at 1.00 increases it. Closing debit is negative USD9,000 at 0.60. Deposits and withdrawals remain positive flow amounts; opening and closing debt balances are negative. The formula yields a positive A$3,500 forex gain. Do not import the limited balance test's positive-debit convention.

```oa-check
name: debit-account-retranslation
tolerance: 0.000001
inputs:
  opening_usd: -10000
  deposit_usd: 2000
  withdraw_usd: 1000
  opening_rate: 0.5
  deposit_rate: 0.8
  withdraw_rate: 1
  closing_rate: 0.6
steps:
  - closing_usd: opening_usd + deposit_usd - withdraw_usd
  - opening: opening_usd / opening_rate
  - deposits: deposit_usd / deposit_rate
  - withdrawals: withdraw_usd / withdraw_rate
  - closing: closing_usd / closing_rate
  - gain: closing - opening - deposits + withdrawals
expected:
  closing_usd: -9000
  opening: -20000
  deposits: 2500
  withdrawals: 1000
  closing: -15000
  gain: 3500
```
### 15. Market value replaces only the first CGT element

An event 2 receipt gives the taxpayer USD800 of currency with market value A$1,000 at 0.80 USD/AUD. This case varies the no-additional-cost default: assume a further A$20 has independently been established as an allowable additional element of both the CGT cost base and reduced cost base, with no double counting or other adjustment. Section 775-125 replaces only the first element with market value when received. Both complete bases are therefore A$1,020, rather than A$1,000. The checker verifies addition under those stipulated CGT eligibility facts; it does not establish whether an actual expense is allowable.

```oa-check
name: currency-first-cgt-element-only
tolerance: 0.000001
inputs:
  usd_received: 800
  receipt_rate: 0.8
  other_allowable_element: 20
steps:
  - first_element: usd_received / receipt_rate
  - total_cost_base: first_element + other_allowable_element
  - total_reduced_cost_base: first_element + other_allowable_element
expected:
  first_element: 1000
  total_cost_base: 1020
  total_reduced_cost_base: 1020
```

## When to refuse or refer

Refer where Division 230 or functional currency applies, a stablecoin's legal character is unresolved, the right or obligation cannot be identified, or the actual election and event history cannot be substantiated. Options, forwards, shares, hedges, facility rollovers, traditional securities, non-arm's-length arrangements, constructive payments/set-off and detailed election entry/exit consequences need their complete statutory treatment and usually specialist review. This guide does not certify those computations.

Do not rely on another taxpayer's edited private ruling, infer a private loss deduction from gain treatment, apply a new retrospective election without authority or supply an actual return label/deadline without procedural evidence. GST treatment is outside this guide. Named accountant approval and taxpayer-specific professional review remain outstanding.

## Sources

Targeted source text was read on **3 November 2026**. Same-day captures reused from the preceding review were hash checked; reuse is not a claim to have independently fetched them again. Section text below was read for the affected rules, not every linked ruling, history note, amendment or endnote. The Register API identified compilation 268 (C2026C00471) as current/in force with no unincorporated amendments indicated; that metadata does not prove every future or transitional application question.

| Source | URL | Read scope |
| --- | --- | --- |
| Federal Register, ITAA 1997 compilation 268 | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html> | Compilation identity and selected Division 775 event, overlap, private, exempt/NANE, limited balance and retranslation provisions. Extracted s 775-285 formula omitted; readable formula checked in ATO legislation copy below. |
| SECTION 775-15 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-15> | Affected operative section or relevant forex page text |
| SECTION 775-30 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-30> | Affected operative section or relevant forex page text |
| SECTION 775-25 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-25> | Affected operative section or relevant forex page text |
| SECTION 775-20 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-20> | Affected operative section or relevant forex page text |
| SECTION 775-35 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-35> | Affected operative section or relevant forex page text |
| SECTION 775-40 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-40> | Affected operative section or relevant forex page text |
| SECTION 775-45 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-45> | Affected operative section or relevant forex page text |
| SECTION 775-50 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-50> | Affected operative section or relevant forex page text |
| SECTION 775-55 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-55> | Affected operative section or relevant forex page text |
| SECTION 775-60 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-60> | Affected operative section or relevant forex page text |
| SECTION 775-65 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-65> | Affected operative section or relevant forex page text |
| SECTION 775-70 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-70> | Affected operative section or relevant forex page text |
| SECTION 775-75 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-75> | Affected operative section or relevant forex page text |
| SECTION 775-80 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-80> | Affected operative section or relevant forex page text |
| SECTION 775-85 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-85> | Affected operative section or relevant forex page text |
| SECTION 775-105 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-105> | Affected operative section or relevant forex page text |
| SECTION 775-125 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-125> | Affected operative section or relevant forex page text |
| SECTION 775-135 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-135> | Affected operative section or relevant forex page text |
| SECTION 775-140 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-140> | Affected operative section or relevant forex page text |
| SECTION 775-150 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-150> | Affected operative section or relevant forex page text |
| SECTION 775-155 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-155> | Affected operative section or relevant forex page text |
| SECTION 775-165 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-165> | Affected operative section or relevant forex page text |
| SECTION 775-270 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-270> | Affected operative section or relevant forex page text |
| SECTION 775-280 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-280> | Affected operative section or relevant forex page text |
| SECTION 775-285 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-285> | Affected operative section or relevant forex page text |
| Foreign exchange gains and losses / Australian Taxation Office | <https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses> | Affected operative section or relevant forex page text |
| Forex realisation events / Australian Taxation Office | <https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/forex-realisation-events> | Affected operative section or relevant forex page text |
| Common forex transactions / Australian Taxation Office | <https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/common-forex-transactions> | Affected operative section or relevant forex page text |
| Forex elections / Australian Taxation Office | <https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/in-detail/forex-elections> | Affected operative section or relevant forex page text |
| SECTION 775-90 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-90> | Affected operative section or relevant forex page text |
| SECTION 775-95 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-95> | Affected operative section or relevant forex page text |
| SECTION 775-100 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-100> | Affected operative section or relevant forex page text |
| SECTION 775-110 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-110> | Affected operative section or relevant forex page text |
| SECTION 775-115 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-115> | Affected operative section or relevant forex page text |
| SECTION 775-290 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-290> | Affected operative section or relevant forex page text |
| SECTION 960-50 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/960-50> | Affected operative section or relevant forex page text |
| SECTION 118-10 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-10> | Affected operative section or relevant forex page text |
| SECTION 108-20 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-20> | Affected operative section or relevant forex page text |
| 195-1 | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/195-1> | Digital currency definition only |
| TD 2014/25 / Legal database | <https://www.ato.gov.au/law/view/document?docid=TXD/TD201425/NAT/ATO/00001> | Paragraphs 1–3 and relevant ordinary-meaning reasoning |
| What are crypto assets? / Australian Taxation Office | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/crypto-asset-investments/what-are-crypto-assets> | Main crypto classification and common assets text |
| GST and digital currency / Australian Taxation Office | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-crypto-assets/gst-and-digital-currency> | Digital currency definition and stablecoin text |
| 775-230 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-230> | Operative section; same-day capture reused |
| 775-250 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-250> | Operative section; same-day capture reused |
| 775-255 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-255> | Operative section; same-day capture reused |
| 775-245 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-245> | Operative section; same-day capture reused |
| 995-1 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1> | Operative section; same-day capture reused |
| Section 775-27 | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-27> | Entire operative section |

The old edited-private-ruling citation is no longer a general authority for an A$10,000 forex exemption. No current reliance is placed on that ruling or the earlier TOFA elective-method page for the ordinary account choice. The operative provisions and their separate regimes govern the method above.

Drafted by OpenAccountants. Not yet reviewed or approved by a named accountant.

> Contributed by Ryan Duguid.

Not yet confirmed: complete historical amendment/application coverage, every actual taxpayer's character and elections, future law after the checked compilation period, return procedures and deployment/consumer results. The executable cases verify conditional arithmetic; they are not independent legal certification.

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
