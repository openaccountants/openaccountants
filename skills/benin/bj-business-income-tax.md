---
name: bj-business-income-tax
description: "Prepare a Benin individual business-profit tax working paper for 2026 using the law applicable to the actual income period. Use this Guide for a sole trader, independent professional or taxable transparent-entity member whose IBA status is established. It distinguishes business profits from salary and rental income, screens the separate TPS regime and records the individual-specific deduction, depreciation, loss, ordinary-rate and minimum-tax rules. Two executable cases compare the minimum with profit tax and cash with accrual accounting. It links the existing company Guide only for shared computational and filing methods. Special relief interactions, the numerical TPS eligibility instrument and authenticated filing remain unresolved. Trigger phrases include Benin IBA, independent professional, sole trader profit tax and cash-basis election."
jurisdiction: BJ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.1
---

# Benin individual business IBA working paper v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use this working paper for annual impôt sur les bénéfices d’affaires (IBA) of a natural person carrying on a habitual profit-making activity on their own account. Industrial, commercial, artisanal, liberal-profession and intellectual/industrial-property receipts are within the statutory screen, subject to exemptions. Other habitual or exceptional lucrative receipts fall here only when they do not belong to salary ITS, investment IRCM, rental IRF or property-gain TPVI. Route salaries to [salary ITS](bj-income-tax.md), property rent to [rental IRF](bj-rental-income-tax.md) and a company charged to IS to [corporate IS](bj-corporate-income-tax.md). Do not import the company’s industrial-rate concession into an individual business. [CGI arts. 54–55, 63](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=34)

IBA also covers letting an equipped commercial/industrial undertaking, property or business-sale intermediation, habitual purchase of property for resale and subdivision of land for sale. A normal property-rental classification cannot be assumed for those activities. Members of entities outside IS and co-owners are personally charged on their profit shares, subject to the property-predominance reservation in article 101(2). Resolve that reservation before choosing the profit-share route. [CGI arts. 56–57](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=34)

Screen all article 58 exemptions: agricultural, livestock and fishing operations; specified artists selling only their own art; musicians, actors and other artists’ performance income; income from funds entrusted to venture-capital enterprises for at least three years; gambling gains; and taxpayers within TPS. An exemption from IBA is not evidence of exemption from every other tax. [CGI art. 58](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=34)

**Resolve IBA versus TPS before calculating.** Article 178 assigns IBA-type taxpayers at or below a ministerially fixed turnover threshold to TPS; article 179 excludes persons charged to IS by right or election. The actual numerical threshold order has not been read, so turnover alone cannot establish status from this Guide. Obtain the applicable order and the taxpayer’s existing classification, options, turnover, purchases/equipment and signed contracts. Stop a proposed first classification that relies on an unverified threshold. [CGI arts. 178–179, 182](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=85)

An established TPS taxpayer can expressly request IBA at any time. The service has eight days to accept or refuse; silence is acceptance. The option takes effect on the first day of the month after acceptance and is irrevocable. An established threshold breach triggers IBA no later than the next month; a December breach moves the business in the next year. The threshold also tests purchases of goods/services/equipment and signed contracts. Following a control-discovered breach, reclassification is automatic. A taxpayer whose IBA turnover falls below the limit enters TPS only after two consecutive exercises below it. Preserve the transition assessment: pre-switch TPS is credited half to local taxes and half to State taxes, not entirely against IBA. [CGI arts. 181–182](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=85)

The June rectifying law changes the new-enterprise TPS exemption by excluding article 146(2)(a), (b) and (d) cases: control reassessments, takeover of existing activities and non-resident branches. That overlay must be screened when a new-enterprise exemption or transition credit is claimed. Its precise first operative period and detailed transition-credit instructions remain held here; do not treat the January CGI as containing the June amendment. [LFR 2026 art. 8](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf#page=3); [CGI arts. 146, 180](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=71)

## Rates, bands and thresholds

Use these IBA provisions only after ordinary status, period and absence of a special concession are confirmed. These are individual-business rules, even where a number happens to equal an IS number.

| Item | Rule and conditions | Official source |
|---|---|---|
| Ordinary profit tax | 30% of taxable IBA profit; no general industrial reduction appears in article 63 | [CGI art. 63(1)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=36) |
| Private education | 25% for private school, university, technical and professional educational establishments | [CGI art. 63(2)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=36) |
| Ordinary minimum | 1.5% of produits encaissables, using the definition owned by the [corporate base method](bj-corporate-income-tax.md#the-base); sector exceptions and the absolute floor below also require a check | [CGI art. 64(1)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=36) |
| Building/public works minimum | 3% of produits encaissables | [CGI art. 64(2)(a)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=36) |
| Property-predominant business minimum | 10% of produits encaissables where the article 101(2) definition applies; resolve that definition and taxpayer classification first | [CGI art. 64(2)(b)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37) |
| Absolute IBA floor | FCFA 250,000 under article 64(3)(a), reflecting the original 2026 finance-law amendment; check the actual income period | [CGI art. 64(3)(a)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37); [LF 2026 art. 14](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf#page=4) |
| Used vehicles and specified consumer products | Regulatory minimum; for used vehicles, the importer’s minimum is due per vehicle sold and is liberatory. Do not substitute the ordinary percentage for the missing regulation | [CGI art. 64(2)(c)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37) |
| Service-station minimum | At least FCFA 0.60 per litre sold and the absolute IBA floor. Also covers non-importing distributors sourcing from approved importers and using homologated prices like service stations | [CGI art. 64(3)(b)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37) |
| Separate ORTB levy | FCFA 4,000 in addition to IBA, payable with the March instalment referred to by article 64(4) | [CGI art. 64(4)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37) |
| IBA loss carry-forward | Three years under the IBA override, with the common proof, prior-use, identity and loss-use controls retained; do not substitute the company’s longer period | [CGI arts. 60(2)(b), 43](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35) |
| Voluntary retirement/life premiums | Deduct the operator’s qualifying voluntary retirement payments and life-insurance premiums only within 5% of profit before those payments | [CGI art. 60(3)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35) |
| Insufficiently justified mixed-expense split | Professional deductible share is 30% where sufficient evidence does not establish the business allocation; this is not a substitute for the general deductibility gates | [CGI arts. 60(4), 20](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35) |

Article 65 halves tax for the specified home pieceworkers and artisans. For home piecework, the work must be exclusively to order for industrialists/traders using their materials. Assistance is confined to the spouse, parents, children/grandchildren, one companion and one apprentice under eighteen with a regular apprenticeship contract. The separate artisan limb requires mainly selling the product of one’s own work, at home or elsewhere, with assistance limited to those same persons. This Guide does not settle interaction between that reduction and minimum tax. Exclusive art dealing, new-enterprise, approved-management-centre and other incentive cases also leave this ordinary computation until their conditions and interactions are resolved. [CGI arts. 65, 145–149](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37)

## The base

1. **Choose the taxpayer, period and accounting basis.** Article 60 imports IS profit-determination rules, subject to its IBA overrides. Use the common [company base method](bj-corporate-income-tax.md#the-base) for net-profit reconciliation and general supporting-document tests, not its rates or loss period. Record the accounting close and any valid first-period or education exception. The 2026 intake year does not determine the income year: both finance laws’ article 1 clauses refer income-tax measures to the exercise closed on 31 December 2025 unless specified otherwise; the original law’s final article 48 states commencement on 1 January 2026. [CGI arts. 8–9, 60](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35); [LF arts. 1, 48](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf#page=1); [LFR arts. 1, 48–49](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf#page=1)
2. **Default to accrual accounts.** Professional/habitual business profits require accounting compliant with the applicable accounting law. A liberal professional, non-commercial operator or intellectual/industrial-property income manager can elect cash accounting before 30 November of the preceding year, effective from the following 1 January. Article 67 provides tacit renewal unless denounced before 30 November of the second year. A person simultaneously earning commercial/industrial and non-commercial business profits uses accrual under article 67(3), rather than applying the cash election to the whole mixed business. Evidence of a valid election is essential; detailed change-of-basis adjustments and later renewal-period interpretation remain held. [CGI art. 67](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37)
3. **Apply individual adjustments.** Depreciation is straight-line only. A spouse’s remuneration requires actual participation, a non-abnormally-high salary, social-security contributions and tax withholding. Other family remuneration must be normal, actually paid and for effective work. Apply the retirement/premium and mixed-expense limits in the table. [CGI art. 60(2)–(4)](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35)
4. **Exclude personal items.** The operator’s own remuneration drawings, personal expenditure and interest/remuneration on their own invested capital or the business’s own funds are not deductible. For an asset-booked property, assess professional usefulness separately. Article 60(5) removes non-professional property income from business profit, subjects that removed product to IRF, and requires the corresponding charge reconciliation; charges for a non-income-producing property are not deductible. Exact partial-use allocation requires a separate supported schedule. [CGI arts. 60(5), 61](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35)
5. **Roll losses and calculate the correct minimum.** Reconcile available, evidenced and unused losses within the IBA window, respecting the common first-profitable-result and continuity controls. Compare non-negative profit tax with the applicable sector minimum and absolute IBA floor, then show the levy separately. Reconcile supported credits and instalments once. Special reductions, exemption transitions or regulatory minima prevent an ordinary final amount until resolved. [CGI arts. 43, 60, 63–66](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35)

If the operator dies and direct-line heirs or the spouse continue the business, article 62 defers the business-fund gain until their disposal/cessation, provided the asset valuations in the deceased’s last balance sheet are not increased. It also covers the specified succession allocation or an exclusively heirs/spouse entity outside IS if those values remain unchanged on partition or conversion. This is a gain-deferral condition, not an exemption from all death/cessation declarations. [CGI art. 62](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=36)

## Deadlines and filing

Article 66 makes IBA declaration and payment follow IS. Use the shared [annual return, attachments, instalments, balance and reduction-request procedure](bj-corporate-income-tax.md#deadlines-and-filing), applying the IBA calculation above. An entity outside IS pays IBA for its members under article 51. The common dates stay in that filing owner; they are not a reason to use the company tax rate or loss period. [CGI art. 66](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=37)

Prepare an IBA classification/election record; accounts-to-tax adjustments; depreciation, loss and produits-encaissables schedules; the ordinary/minimum comparison; a separate levy line; annual attachments; and dated credit/instalment evidence. For AIB, article 133 requires the deduction declaration to be supported by the payment receipt. Its unused year-end balance is credited against profit tax, later instalments and profit-tax arrears under article 133(4); do not assume an immediate cash refund or claim the same receipt twice. A full AIB withholding-agent computation is outside this job. [CGI art. 133](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=66)

The pack’s recorded [DGI e-services entry](https://e-services.impots.bj/) is a routing link. Authenticated IBA form names, field identifiers, upload sequence, payment reference and acknowledgement were not accessed. Keep the output as a preparation workpaper until those steps are evidenced. For a cessation/transfer, the June amendment to article 476(1) requires prior written/electronic information with an up-to-date tax position; the cessation/death return process and its period-specific application need separate completion. [LFR art. 9](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf#page=3)

## Penalties and interest

The [overview’s general DGI sanctions and conditional first-declaration relief](bj-tax-overview.md#penalties-and-interest) own those figures. They require the actual failure, notice, tax, due/payment dates and relief facts. Do not treat a valid cash election, TPS switch or tax exemption as waiving other filing obligations. Specific AIB, invoicing and cessation sanctions and a live penalty assessment are not computed here. [CGI arts. 485, 487–488](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=216); [LF art. 3](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf#page=2)

## Cross-border points

Article 59 limits IBA taxable profits to those realised in Benin and those allocated to Benin by a double-tax convention, under articles 5–6. Establish the activity, location and any permanent establishment and read the applicable treaty before allocating foreign receipts or claiming an exclusion. The company-specific residence wording in article 5 is not a verified standalone natural-person residence test. No general worldwide-income charge or automatic foreign-tax credit is asserted here. [CGI arts. 59, 5–6](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35)

Related-party pricing and domestic foreign-payment withholding are separate [TP](bj-transfer-pricing.md) and [cross-border withholding](bj-cross-border-withholding.md) jobs. A gross foreign-client invoice is not automatically a resident salary or a final withholding-tax computation. Treaty relief, foreign-source attribution, foreign credits and interactions between final withholding and IBA remain case-specific unresolved work.

## Two worked examples that recompute

**Ordinary IBA minimum, with a classification boundary.** Assume established ordinary IBA status for an existing individual business, no exemption, incentive, sector minimum, credits or transition. Adjusted taxable profit is FCFA 100,000 and reconciled produits encaissables are 20 million. Profit tax is 30,000. The IBA percentage minimum is 300,000, above its absolute floor, so IBA is 300,000 plus the separate 4,000 levy. The ordinary percentage minimum overtakes profit tax below 1 million profit on this base. Those facts do not establish TPS status: the threshold instrument and classification are separate prerequisites. [CGI arts. 63–64](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=36)

```oa-check
name: IBA percentage minimum and profit boundary
inputs:
  taxable_profit: 100000
  produits_encaissables: 20000000
steps:
  profit_iba: max(taxable_profit, 0) * 0.30
  percentage_minimum: produits_encaissables * 0.015
  annual_iba: max(profit_iba, percentage_minimum, 250000)
  profit_at_percentage_boundary: percentage_minimum / 0.30
  iba_plus_separate_levy: annual_iba + 4000
expected:
  profit_iba: 30000
  percentage_minimum: 300000
  annual_iba: 300000
  profit_at_percentage_boundary: 1000000
  iba_plus_separate_levy: 304000
```

**Cash versus accrual is a permitted-election decision.** An independent liberal professional has established IBA status, no commercial activity, no relief or credits, and fully supported ordinary deductible costs. During the hypothetical year, receipts collected are 20 million and deductible costs paid are 15 million. Accrual revenue is 25 million and deductible accrued costs are 18 million. The independently reconciled produits-encaissables base is 25 million for this comparison. Cash profit is 5 million and accrual profit 7 million, giving IBA of 1.5 million versus 2.1 million; both exceed the minimum, a 600,000 timing difference before the same levy. Use cash only with a valid timely article 67 election. Without it, use accrual, even though cash produces a lower amount. No opening/closing debt adjustment or permanent lifetime saving is implied. [CGI arts. 60, 63–64, 67](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=35)

```oa-check
name: Eligible cash election versus default accrual
inputs:
  cash_receipts: 20000000
  deductible_costs_paid: 15000000
  accrued_revenue: 25000000
  deductible_costs_accrued: 18000000
  reconciled_produits_encaissables: 25000000
steps:
  cash_profit: cash_receipts - deductible_costs_paid
  accrual_profit: accrued_revenue - deductible_costs_accrued
  percentage_minimum: reconciled_produits_encaissables * 0.015
  cash_iba: max(cash_profit * 0.30, percentage_minimum, 250000)
  accrual_iba: max(accrual_profit * 0.30, percentage_minimum, 250000)
  timing_difference_before_levy: accrual_iba - cash_iba
expected:
  cash_profit: 5000000
  accrual_profit: 7000000
  percentage_minimum: 375000
  cash_iba: 1500000
  accrual_iba: 2100000
  timing_difference_before_levy: 600000
```

## Ask the client first

- Who earns each income class, through which legal form, activity and profit share?
- Which income year, existing IBA/TPS classification, threshold instrument, options and breach/transition dates are documented?
- What residence, Benin/foreign activities, treaty and related-party facts are evidenced?
- Are cash-accounting eligibility/election, accounts, family remuneration, personal/mixed expenses, depreciation and available losses supported?
- Do art dealing, artisan work, new-enterprise/CGA relief, property predominance or regulated-sector minimum rules apply?
- Which AIB receipts, instalments, notices and authenticated return/payment records are available?

## Sources

| Official source | What was actually read | Read on |
|---|---|---|
| [DGI CGI, 2026 edition](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf) | Reused official cached PDF and actual extracted clauses: arts. 54–67 in full with adjacent arts. 53/68; common arts. 5–9, 20, 43–47, 49–52, 101(2), 130–134, 145–149, 178–185, 476 and 485–488. The cover consolidates the original finance law; it does not incorporate the June rectifying law. | 2026-11-01 |
| [Original finance law 2025-22 of 8 December 2025](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf) | Cached fiscal arts. 1–17 and final arts. 47–48 read in OCR; PDF pages 1, 4 and 14 visually read for the income-period clause, IBA-floor amendment and commencement/signature. Other measures do not establish an IBA filing or complete currentness chain. | 2026-11-01 |
| [Rectifying finance law 2026-10 of 24 June 2026](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf) | Cached fiscal arts. 1–19 and final arts. 48–49 read in OCR; PDF pages 1, 3 and 17 visually read for income period, TPS exclusion/cessation overlays and final/signature clauses. No budget-table review or automatic January commencement is asserted. | 2026-11-01 |

Not yet confirmed: the actual numerical TPS threshold order and full TPS computation/filing; current first operative period and detailed exemption/credit transition instructions for the June TPS amendment; cash-election renewal-period and change-of-basis adjustments; complete expense-specific, partial-use property and sector/incentive calculations, including reduction/minimum interactions; natural-person residence, treaty allocation, foreign-credit/final-withholding interactions; later instruments not identified by the sources read; authenticated IBA form, field/upload mapping, payment reference and acknowledgement; live cessation/death and penalty assessments. This new job awaits independent source review and has no accountant attestation. All seven country domains remain partial. Rule/figure ledger and preserved prior-file identities are in `evidence/ledgers/benin-business-20261101/`.
