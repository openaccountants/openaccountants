---
name: it-dichiarazione-iva-annuale
description: "Italian annual VAT return (Dichiarazione IVA) for VAT year 2026, filed in 2027, and the December VAT acconto due December 2026. Covers who files and who is exempt, the 1 February to 30 April window, quadri VE, VF, VJ, VH, VL and VX and how the annual balance is built, the 16 March balance or deferral at 0.40% a month, quarterly filers' 1% interest, credits (refund conditions, the EUR 30,000 visto or guarantee rule, F24 offset and the EUR 5,000 visto threshold, carry forward), the acconto methods (storico and previsionale 88%, analitico 100%, EUR 103.29 floor), pro-rata and rettifica in summary, penalties and ravvedimento. Trigger on: dichiarazione IVA, quadro VL, saldo IVA 16 marzo, acconto IVA, rimborso IVA, visto di conformita, credito IVA. Out of scope: periodic settlement and LIPE (italy-vat-return), e-invoicing (italy-einvoice), forfettario (it-regime-forfettario)."
version: 0.1
jurisdiction: IT
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy: annual VAT return (Dichiarazione IVA) and the December acconto, VAT year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Italy.

**What this skill does.** The periodic side of Italian VAT (monthly or quarterly settlement, F24 payments, the quarterly LIPE) is in [italy-vat-return](italy-vat-return.md). This skill picks up where that one stops: the year-end. It covers the December acconto paid in December 2026, the annual return for 2026 filed between 1 February and 30 April 2027, the balance paid on 16 March 2027 (or deferred), and what to do with a credit.

**Which model.** The model in use is Modello IVA 2026, for VAT year 2025. The model for VAT year 2026 (Modello IVA 2027) is approved by 15 January 2027 (D.P.R. 322/1998 art. 8(1)). Row references below (VE26, VL38, VX5 and so on) come from the 2026 model and its instructions. Check them against the 2027 model when it appears.

**The law moves on 1 January 2027.** The VAT consolidated code, D.Lgs. 19 January 2026 n. 10 (Testo unico IVA), applies from 1 January 2027 (its art. 171). From that date its art. 170(1) repeals, among others, D.P.R. 633/1972 arts. 19 to 27, 30 and 38 to 39 (so arts. 19, 19-bis2 and 38-bis) and L. 405/1990 art. 6, and the code restates them: art. 111 (acconto), art. 114 (refund of the annual credit), art. 116 (execution of refunds). The payment code (D.Lgs. 33/2025, art. 243) and the penalty code (D.Lgs. 173/2024, art. 102) also apply from 1 January 2027. D.P.R. 322/1998 art. 8, which sets the filing window, is not repealed. The acconto paid in December 2026 is governed by L. 405/1990 art. 6. The 2026 return, the March 2027 balance and any refund request are made in 2027; D.Lgs. 10/2026 has no transitional rule saying which text governs them, but the figures used here are the same in both texts: 88%, EUR 103.29, the 97% rule (art. 111(1), (4), (7)), EUR 2,582.28 and the refund cases (art. 114(2)), EUR 30,000 and 2% interest (art. 116(1), (3)).

**Sibling skills.** [italy-vat-return](italy-vat-return.md) for classification, rates, the periodic settlement and the LIPE rows. [italy-einvoice](italy-einvoice.md) for SdI invoicing. [it-regime-forfettario](it-regime-forfettario.md) for the flat-rate regime, whose users file no VAT return. [it-ires-corporate-tax](it-ires-corporate-tax.md) and [it-income-tax](it-income-tax.md) for the income tax return, whose payment date the deferred VAT balance follows.

## Who this applies to

**Who files (D.P.R. 322/1998 art. 8(1)).** Every holder of a VAT number carrying on a business, art or profession files an annual VAT return for the previous calendar year, online, between 1 February and 30 April. The return is filed even when the business made no taxable supplies in the year.

**Who does not file.** Art. 8(1) and the Modello IVA 2026 instructions (para. 2.2) exempt, among others:
- traders who recorded only exempt supplies under D.P.R. 633/1972 art. 10 in the year, unless they also had intra-EU operations, made deduction adjustments under art. 19-bis2, or bought goods on which they owed the VAT as purchaser (gold, scrap and similar);
- people in the regime forfettario for the whole year (L. 190/2014 art. 1 commi 54-89) and in the older regime di vantaggio (D.L. 98/2011 art. 27);
- exempt farmers (art. 34(6)), individuals who let their only business and have no other VAT activity, and associations under L. 398/1991;
- non-EU businesses registered in Italy only for the special scheme for services to consumers (art. 74-quinquies).

**Who pays the December acconto.** All VAT payers who make monthly or quarterly settlements (L. 405/1990 art. 6(2)). The Agenzia's acconto page lists who is exempt, because they have no "storico" or "previsionale" figure: those who started the business in 2026; those who ceased by 30 November (monthly) or 30 September (quarterly); those whose last 2025 settlement or 2025 annual return showed a credit; and those who, although they paid for December 2025, expect to close 2026 with a credit. Also exempt: those with only non-taxable or exempt supplies, the art. 34(6) farmers, L. 398/1991 associations, and individuals who let their only business by 30 September (quarterly) or 30 November (monthly).

**Out of scope here.** VAT groups (arts. 70-bis and following) and the art. 73 group settlement (Modello IVA 26 PR), the agricultural and entertainment special regimes, tax-warehouse and margin schemes, and the IVA Base simplified model rules. Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Annual return window | 1 February to 30 April of the following year | Return for 2026: 1 Feb to 30 Apr 2027 | D.P.R. 322/1998 art. 8(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art8!vig=2026-10-23 |
| Late return still valid | Filed within 90 days of the deadline; later counts as omitted | 2026 | Modello IVA 2026 instructions, para. 1.2.1 |
| Annual balance due | 16 March, if above EUR 10.33 (EUR 10 after rounding in the return) | Balance for 2026: 16 Mar 2027 | D.P.R. 542/1999 art. 6(1); Modello IVA 2026 instructions, para. 2.1 |
| Deferral of the balance | To the income tax payment date (30 June), plus 0.40% per month or part month after 16 March | 2026 | D.P.R. 542/1999 arts. 6(1) and 7(1)(b), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art6!vig=2026-10-23 |
| Further deferral | To 30 July, with a further 0.40% on the amount due at 30 June | 2026 | Modello IVA 2026 instructions, para. 2.1 (Risoluzione 73/E of 2017) |
| Instalments | Equal monthly instalments, the last by 16 December; 0.33% a month on each instalment after the first | 2026 | Modello IVA 2026 instructions, para. 2.1 (D.Lgs. 241/1997 art. 20) |
| Quarterly filers' interest | 1% on each quarterly payment and on the annual balance (row VL36) | 2026 | D.P.R. 542/1999 art. 7(3), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-10-23 |
| Quarterly option limits | Previous-year volume d'affari up to EUR 500,000 (services, professions) or EUR 800,000 (other) | 2026 | Agenzia, "Come pagare l'Iva", https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva |
| Acconto, storico and previsionale | 88% of last year's December (or Q4, or annual) payment or, if lower, this year's | Acconto 2026 | L. 405/1990 art. 6(2), where the 65% and 70% rates were unified and raised to 88% by D.L. 155/1993 art. 15(1) (converted by L. 243/1993), printed as note (7) to art. 6 on Normattiva, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-12-29;405~art6!vig=2026-10-23 ; Agenzia acconto page |
| Acconto, analitico | 100% of a special settlement to 20 December | Acconto 2026 | Same Agenzia page; L. 405/1990 art. 6(3-bis) |
| Acconto, large payers (more than EUR 2 million of VAT paid in the previous year, in the groups set by D.M. 366 and 370 of 2000) | 97% of the average of the quarterly payments of the current year | Acconto 2026 | L. 311/2004 art. 1(471), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2004-12-30;311~art1!vig=2026-10-23 ; TU IVA art. 111(7) |
| Acconto floor | Not paid if below EUR 103.29 (ITL 200,000); an acconto of exactly EUR 103.29 is paid under the law (the Agenzia's "Chi deve versare" page says "non superiore", which would exempt it) | Acconto 2026 | L. 405/1990 art. 6(4), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-12-29;405~art6!vig=2026-10-23 ; TU IVA art. 111(4) |
| Acconto deadline | 27 December; 27 December 2026 is a Sunday, so 28 December 2026 | 2026 | L. 405/1990 art. 6(2); weekend and holiday rule in Modello IVA 2026 instructions, para. 2.1 |
| Acconto F24 codes | 6013 (monthly), 6035 (quarterly) | 2026 | Agenzia, "Come si versa", https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24-acconto-iva-f24ivaacc/come-si-versa-f24ivaacc |
| Refund floor | Credit above EUR 2,582.28 (ITL 5 million), except on cessation or the three-year credit rule | 2026 | D.P.R. 633/1972 art. 30(3), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art30!vig=2026-10-23 ; TU IVA art. 114(2) |
| Refunds without guarantee or visto | Up to EUR 30,000 | 2026 | D.P.R. 633/1972 art. 38-bis(3), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art38bis!vig=2026-10-23 ; TU IVA art. 116(3) |
| Interest on refunds | 2% a year from the 90th day after filing | 2026 | D.P.R. 633/1972 art. 38-bis(1) |
| F24 offset of the annual credit | Above EUR 5,000 a year: only from the 10th day after filing the return | 2026 | D.Lgs. 241/1997 art. 17(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art17!vig=2026-10-23 |
| Visto di conformita for F24 offset | Needed above EUR 5,000 a year (EUR 50,000 for innovative start-ups) | 2026 | D.L. 78/2009 art. 10(1)(a)(7) and (7-bis), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2009-07-01;78~art10!vig=2026-10-23 |
| ISA reward (or concordato preventivo biennale): no visto for F24 offset; no visto or guarantee for refunds | Up to EUR 70,000 a year each | 2026 | Modello IVA 2026 instructions, frontespizio and row VX4 (D.L. 50/2017 art. 9-bis(11)(a) and (b)) |
| Annual cap on credits offset or refunded through the collection agent | EUR 2,000,000 | 2026 | L. 388/2000 art. 34(1), raised to EUR 2 million from 1 January 2022 by L. 234/2021 art. 1(72) (note 104 on Normattiva), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-12-23;388~art34!vig=2026-10-23 ; Modello IVA 2026 instructions, rows VX3 and VX4 |
| Pro-rata rounding | Nearest whole percent; a decimal above 0.5 rounds up | 2026 | Modello IVA 2026 instructions, row VF34 field 9 |
| Rettifica period | 5 years for depreciable assets, 10 years for buildings; pro-rata change must exceed 10 points | 2026 | D.P.R. 633/1972 art. 19-bis2(2), (4), (8), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art19bis.2!vig=2026-10-23 |

## The taxable base

The annual return does not tax anything new. It restates the year's settlements and squares them with what was paid.

**The quadri that matter for most businesses (Modello IVA 2026 instructions, para. 4.2).**
- **VE, sales and volume d'affari.** Taxable supplies by rate, with VAT. VE24 totals them; VE26 is the output VAT on taxable supplies. VE50 is the volume d'affari, which decides next year's quarterly option and the pro-rata. Non-taxable, exempt and out-of-scope supplies go in VE30 to VE38.
- **VF, purchases and deductible VAT.** Purchases by rate; VF27 is the VAT on purchases; VF34 holds the data for the pro-rata; VF70 the art. 19-bis2 adjustments; VF71 is the VAT allowed as a deduction. Every filer completes VF71.
- **VJ, VAT the buyer owes.** Reverse-charge purchases: intra-EU acquisitions, services from abroad, domestic reverse charge (art. 17). VJ19 totals that VAT. It enters both the debit side (VL1) and, if deductible, VF.
- **VH, corrections to the LIPE.** Filled only to send, complete or correct LIPE data that were omitted or wrong. Quarterly filers use VH4, VH8, VH12 and VH16; ordinary quarterly filers under D.P.R. 542/1999 art. 7 leave VH16 blank, because their fourth quarter is settled in the return.
- **VL, the annual settlement.**
  - VL1 = VE26 + VJ19 (VAT due). VL2 = VF71 (VAT deductible). VL3 is the difference if due; VL4 if a credit.
  - VL8 and VL9: the 2025 credit carried forward, less what was already offset in F24 before filing. VL25 = VL8 - VL9.
  - VL20 to VL23 add to the debt: interim refunds asked for, credits transferred to a group, Q1 to Q3 credits already offset, and the 1% interest quarterly filers owed on Q1 to Q3 (VL23).
  - VL30 subtracts what was due periodically: the VP14 column 1 amounts from the year's LIPE plus the acconto in VP13. Field 1 is the higher of the amount due and the amount actually paid.
  - VL32 (debt) or VL33 (credit) = (VL3 + VL20 to VL23) - (VL4 + VL11 + VL12 + VL24 to VL31).
  - VL36: quarterly filers' 1% interest on the balance. VL38 = VL32 - VL34 - VL35 + VL36, the VAT to pay. VL39 is the credit.
- **VX, what to do with the result.** VX1 carries VL38 (the amount to pay; left blank if EUR 10.33 or less). VX2 carries the credit (VL39), which is then split among VX4 (refund), VX5 (carry forward or F24 offset) and VX6 (transfer to the IRES group head). VX3 records overpayments.

**The Q4 quarterly balance sits in the return.** An ordinary quarterly filer does not make a separate fourth-quarter settlement. The tax for Q4, with 1% interest, falls out of VL38 and is paid by 16 March (D.P.R. 542/1999 art. 7(1)(b) and (3)). The Q4 LIPE can be sent inside the return (quadro VP) if the return is filed by the end of February; see [italy-vat-return](italy-vat-return.md).

**Credits.** A credit in VX2 can be carried forward into 2027 settlements, offset in F24 against other taxes and contributions, or refunded (D.P.R. 633/1972 art. 30).
- **Refund conditions (art. 30(3); TU IVA art. 114(2)).** A refund of the annual credit is allowed, if the credit exceeds EUR 2,582.28, when the business: (a) sells mainly at rates lower than those on its purchases (the test, from D.L. 250/1995 art. 3(6) and restated in TU IVA art. 114(2)(a): the average rate on purchases exceeds the average rate on sales increased by 10%, leaving out depreciable assets); (b) makes non-taxable exports and similar supplies (arts. 8, 8-bis, 9) above 25% of all its supplies; (c) bought depreciable assets or research goods and services (limited to that VAT); (d) makes mainly supplies outside the scope of Italian VAT under arts. 7 to 7-septies; or (e) is a non-resident in the art. 17(3) position. Outside those cases, a refund is allowed if the two previous years' returns also showed credits, for the lowest of the three, with no floor (art. 30(4)). On cessation, the whole credit is refundable.
- **Refund mechanics (art. 38-bis).** Refunds up to EUR 30,000 need no guarantee and no visto. Above EUR 30,000 the return needs a visto di conformita (or the auditor's signature) and a sworn statement on net assets, share disposals and contributions; or a guarantee for three years. A guarantee is mandatory above EUR 30,000 for businesses under two years old (except innovative start-ups), those with large recent assessments, refunds asked without the visto, and refunds on cessation. ISA-rated businesses entitled to the reward, and those in the concordato preventivo biennale, skip the visto and guarantee up to EUR 70,000.
- **F24 offset.** Offset of the annual VAT credit above EUR 5,000 a year starts only on the 10th day after the return is filed (D.Lgs. 241/1997 art. 17(1)) and needs a visto di conformita on the return (D.L. 78/2009 art. 10(1)(a)(7)). Up to EUR 5,000 a year can be offset from 1 January with neither. The ISA reward lifts the visto threshold for offset to EUR 70,000 (D.L. 50/2017 art. 9-bis(11)(a)).

**Pro-rata (art. 19(5) and art. 19-bis).** A business making both taxable and art. 10 exempt supplies deducts input VAT by its deduction percentage. During the year it uses last year's percentage; the return fixes the final one in VF34 field 9 and the adjustment flows into VF71. The formula is in the instructions to VF34 field 9: taxable and equivalent supplies over total supplies, leaving out incidental exempt supplies, exempt sales of capital goods and the other items the instructions list. The result is rounded to the nearest whole percent. This skill gives the rule, not a full computation; refer complex mixed businesses.

**Rettifica (art. 19-bis2).** Deduction is adjusted when goods or services are used for supplies with a different right to deduct than first assumed. For depreciable assets the adjustment runs over the year of entry into use and the next four years, by fifths; for buildings over ten years. Under the pro-rata it applies only if the percentage moves by more than 10 points (or every year if the business elects to adjust regardless, for at least five years). The total goes in VF70. Assets costing up to ITL 1 million (EUR 516.46) or depreciated at more than 25% a year are not treated as depreciable for this rule. Normattiva shows art. 19-bis2(3), on adjustments when the business changes VAT regime, as repealed by D.Lgs. 186/2025. When that repeal starts to apply is not confirmed here; check it before adjusting for a change of regime.

## Deadlines and filing

| What | When, for VAT year 2026 | Rule |
|---|---|---|
| December acconto | 28 December 2026 (27 December is a Sunday), F24 online only | L. 405/1990 art. 6(2); Agenzia acconto pages |
| Q4 LIPE (quarterly or monthly) | End of February 2027, or inside the annual return if that is filed by end of February | D.L. 78/2010 art. 21-bis; see italy-vat-return |
| Annual balance | 16 March 2027 (a Tuesday) | D.P.R. 542/1999 arts. 6 and 7 |
| Deferred balance | 30 June 2027, plus 0.40% for each month or part month after 16 March; or 30 July 2027 with a further 0.40% | D.P.R. 542/1999; Modello IVA 2026 instructions, para. 2.1 |
| Annual return | 1 February to 30 April 2027 (a Friday), online through Entratel or Fisconline, directly or through an intermediary | D.P.R. 322/1998 art. 8(1) |
| Return filed late but valid | Within 90 days of 30 April 2027 | Modello IVA 2026 instructions, para. 1.2.1 |
| Correcting a filed return (integrativa) | Up to the assessment deadline in art. 57 D.P.R. 633/1972 | D.P.R. 322/1998 art. 8(6-bis) |

**Form.** The return is a separate filing, not part of the income tax return. It is made on the model the Agenzia approves by 15 January each year (art. 8(1)). Simpler businesses may use IVA Base instead. Amounts are in whole euros: 50 cents or more round up (instructions, Premessa). The December acconto is reported in VP13 of the Q4 LIPE (method code 1 storico, 2 previsionale, 3 analitico, 4 special sectors) and is included in VL30.

**Who signs and the visto.** A return with a credit offset above EUR 5,000, or refunded above EUR 30,000 without a guarantee, carries a visto di conformita from an authorised professional or a CAF, or the signature of the company's statutory auditor (D.L. 78/2009 art. 10; art. 38-bis(3)).

## Penalties and interest

| Violation | Penalty | Source |
|---|---|---|
| Annual return not filed | 120% of the VAT due for the year, minimum EUR 250 (the VAT due is net of payments made, last year's credit and properly settled deductions) | D.Lgs. 471/1997 art. 5(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art5!vig=2026-10-23 |
| Return not filed, no VAT due (only non-taxable supplies) | EUR 250 to EUR 2,000 | Art. 5(3) |
| Return filed more than 90 days late, before any audit, within the assessment deadline | The art. 13(1) late-payment penalty (25%) tripled, on the VAT due; if no VAT is due, EUR 250 (EUR 150 to 1,000 under art. 5(3)) | Art. 5(1-bis) and (3) |
| Return filed within 90 days | Valid, but a penalty for late filing; with ravvedimento, one tenth of the minimum for the omitted return | D.Lgs. 472/1997 art. 13(1)(c) |
| Return understates VAT or overstates a credit | 70% of the extra VAT or excess credit, minimum EUR 150; cut by one third if below 3% and below EUR 30,000 | Art. 5(4) and (4-ter) |
| Balance, quarterly payment or acconto paid late or short | 25% of the unpaid amount; halved if paid within 90 days; within 15 days, one fifteenth of the halved penalty per day | D.Lgs. 471/1997 art. 13(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-23 |
| Credit offset without the visto when one was needed | Credit recovered with interest and penalties | D.L. 78/2009 art. 10(1)(a)(7) |
| Credit offset that is not due (non spettante) | 25% of the credit offset | Art. 13(4-bis) |
| Non-existent credit offset | 70% of the credit, up to double where fraudulent | Art. 13(5) and (5-bis) |

**Ravvedimento operoso (D.Lgs. 472/1997 art. 13).** Before any audit is notified, the penalty is reduced if the tax, interest at the legal rate and the reduced penalty are paid: one tenth of the minimum within 30 days of a missed payment or acconto; one ninth within 90 days of the error, or of the return deadline for errors in the return; one eighth by the deadline for the return of the year of the error; one seventh after that. A late acconto is a missed payment: art. 13(1) of D.Lgs. 471/1997 names "versamenti in acconto". From 1 January 2027 the penalty code D.Lgs. 173/2024 restates these rules; TU IVA art. 111(5) points the acconto penalty to its art. 38(1).

## Cross-border points

- **Non-residents registered in Italy.** A non-resident identified directly (art. 35-ter) files the annual return itself through Entratel. One that uses a fiscal representative files through the representative, who signs as declarant with code 6 (instructions, para. 2.3 C). If both were used in the year, one return is filed, with separate modules.
- **EU businesses with no Italian VAT number** recover Italian VAT through the EU refund procedure for non-established businesses (restated in TU IVA art. 118 from 2027), not through the annual return.
- **Non-EU sellers in the special scheme for services to consumers (art. 74-quinquies)** file no Italian annual return.
- **Reverse charge.** Intra-EU acquisitions and services bought from abroad go in quadro VJ (debit) and VF (deduction). They also keep an otherwise exempt-only trader inside the filing duty.
- **Exporters.** Non-taxable exports above 25% of supplies open the refund route in art. 30(3)(b). Habitual exporters report the VAT not charged on their purchases under a letter of intent in VF35.
- **OSS and IOSS** are reported on their own EU returns, not in the annual Italian return; refunds of OSS and IOSS overpayments sit in TU IVA art. 119 from 2027.

## Worked examples

### Example 1: quarterly filer, annual balance due 16 March 2027

Facts (invented): Gamma S.r.l. supplies services, opted for quarterly settlement, and is not in a VAT group. For 2026 its output VAT (VE26) is EUR 44,220, it has no reverse-charge VAT in VJ, and its deductible VAT (VF71) is EUR 18,000. The VAT due on its Q1, Q2 and Q3 settlements was EUR 5,000, EUR 6,000 and EUR 7,000, each paid with 1% interest. The payment due with its 2025 annual return, gross of the 2025 acconto, was EUR 6,500. It used the storico method for the December 2026 acconto. No credit was brought forward from 2025.

Walk-through:
1. VL3 = 44,220 - 18,000 = 26,220.
2. Interest on Q1 to Q3 at 1% = 18,000 x 1% = 180 (VL23). Each LIPE's VP14 shows the tax plus interest: 5,050, 6,060 and 7,070.
3. December acconto, storico: 6,500 x 88% = 5,720, paid by 28 December 2026. The law asks for 88% of last year's figure or, if lower, this year's, so paying the storico figure always meets the obligation. Here it is also below 88% of this year's Q4 tax (26,220 - 18,000 = 8,220; 88% is 7,233.60).
4. VL30 = 5,050 + 6,060 + 7,070 + 5,720 = 23,900.
5. VL32 = 26,220 + 180 - 23,900 = 2,500.
6. VL36, the quarterly filer's 1% on the balance: 25. VL38 and VX1: 2,525, due 16 March 2027 by F24.
7. If Gamma defers to 30 June 2027: 16 March to 30 June is three months and fourteen days, so four months or part months at 0.40%, 1.6% in all. The 0.40% applies to the debt not offset in F24 (instructions, para. 2.1), and that debt is VL38, which already includes the 1% (instructions, row VL38): 2,525 x 1.016 = 2,565.40.

```oa-check
name: Gamma S.r.l., quarterly filer, 2026 annual VAT balance and deferral
inputs:
  output_vat_ve26: 44220
  deductible_vat_vf71: 18000
  q1_tax: 5000
  q2_tax: 6000
  q3_tax: 7000
  balance_2025_gross: 6500
  months_deferred: 4
steps:
  - vl3: output_vat_ve26 - deductible_vat_vf71
  - vl23_interest: (q1_tax + q2_tax + q3_tax) * 0.01
  - acconto_storico: balance_2025_gross * 0.88
  - q4_tax: vl3 - (q1_tax + q2_tax + q3_tax)
  - acconto_ceiling: q4_tax * 0.88
  - vl30: q1_tax * 1.01 + q2_tax * 1.01 + q3_tax * 1.01 + acconto_storico
  - vl32: vl3 + vl23_interest - vl30
  - vl36_interest: vl32 * 0.01
  - vl38_due_16_march: vl32 + vl36_interest
  - due_30_june: vl38_due_16_march * (1 + 0.004 * months_deferred)
expected:
  vl3: 26220
  vl23_interest: 180
  acconto_storico: 5720
  acconto_ceiling: 7233.60
  vl30: 23900
  vl32: 2500
  vl36_interest: 25
  vl38_due_16_march: 2525
  due_30_june: 2565.40
```

### Example 2: December acconto, storico against previsionale

Facts (invented): Delta S.r.l. settles VAT monthly. Its December 2025 settlement was EUR 11,000 and its 2025 annual return showed a further balance (conguaglio) of EUR 1,000, both before deducting the 2025 acconto. In mid-December 2026 it forecasts that its December 2026 settlement will be EUR 9,000. Its actual December 2026 settlement later turns out to be EUR 10,000.

Walk-through:
1. Storico base: the December 2025 payment plus the conguaglio from the 2025 annual return, gross of the 2025 acconto (Circolare 28/E of 2017, para. 1): 11,000 + 1,000 = 12,000. Storico acconto: 12,000 x 88% = 10,560.
2. Previsionale: 9,000 x 88% = 7,920. The law asks for 88% of the lower of last year's and this year's figure, so Delta may pay 7,920 by 28 December 2026 (F24 code 6013).
3. The risk: the actual December 2026 figure is 10,000. The acconto that was due is 88% of the lower of 12,000 and 10,000: 8,800. Delta paid 880 too little.
4. The shortfall is a missed acconto payment: 25% of 880 = 220 before any reduction (D.Lgs. 471/1997 art. 13(1)). Paying the 880 with ravvedimento cuts the penalty (D.Lgs. 472/1997 art. 13).
5. The December 2026 settlement, due 18 January 2027 (16 January 2027 is a Saturday, so the deadline moves to Monday: instructions, para. 2.1), is 10,000 less the 7,920 acconto paid: 2,080. Paying it settles the tax, including the 880; the penalty on the late part of the acconto remains.

```oa-check
name: Delta S.r.l., monthly filer, December 2026 acconto storico vs previsionale
inputs:
  dec_2025_payment: 11000
  conguaglio_2025: 1000
  forecast_dec_2026: 9000
  actual_dec_2026: 10000
steps:
  - storico_base: dec_2025_payment + conguaglio_2025
  - acconto_storico: storico_base * 0.88
  - acconto_previsionale: forecast_dec_2026 * 0.88
  - acconto_paid: min(acconto_storico, acconto_previsionale)
  - acconto_required: min(storico_base, actual_dec_2026) * 0.88
  - shortfall: max(acconto_required - acconto_paid, 0)
  - penalty_before_reduction: shortfall * 0.25
  - december_settlement_18_jan: actual_dec_2026 - acconto_paid
expected:
  storico_base: 12000
  acconto_storico: 10560
  acconto_previsionale: 7920
  acconto_paid: 7920
  acconto_required: 8800
  shortfall: 880
  penalty_before_reduction: 220
  december_settlement_18_jan: 2080
```

The analitico method avoids this risk: it pays 100% of a settlement run on the transactions recorded to 20 December (1 October to 20 December for quarterly filers), plus supplies made from 1 November to 20 December not yet invoiced or recorded (Agenzia, "Come si calcola").

## Ask the client first

1. **Regime and frequency.** Regime ordinario or forfettario; monthly or quarterly; any separate activities (art. 36) or a VAT group. A forfettario for the whole year files no return; a quarterly filer pays 1% on the balance.
2. **The year's settlements.** The four LIPE (or twelve monthly settlements), what was paid on each, and any credit used in F24 before filing. VL30 and VL9 depend on them.
3. **Last year.** The 2025 return result (balance or credit) and the December 2025 settlement, gross of the 2025 acconto. These fix the storico acconto and the credit brought forward.
4. **Credit plans.** If the year ends in credit: refund, carry forward or F24 offset, and how much. Above EUR 5,000 offset or EUR 30,000 refund the return needs a visto (or a guarantee for refunds). Ask also whether the business is under two years old, has had large recent assessments, or has an ISA reward.
5. **Exempt supplies and capital goods.** Any art. 10 exempt supplies (pro-rata), and depreciable assets or buildings bought in the last five or ten years whose use changed (rettifica).
6. **Cross-border.** Exports, intra-EU trade, services bought from abroad, or registration as a non-resident (direct or through a fiscal representative).

## Sources

| Source | URL | Read on |
|---|---|---|
| D.P.R. 322/1998 art. 8, annual VAT return | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art8!vig=2026-10-23 | 2026-10-23 |
| L. 405/1990 art. 6, December acconto, with note (7) on D.L. 155/1993 art. 15(1) (88%); repealed from 1 January 2027 by TU IVA art. 170(1)(n) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-12-29;405~art6!vig=2026-10-23 | 2026-10-23 |
| D.P.R. 633/1972 art. 30, annual balance and refund of the excess | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art30!vig=2026-10-23 | 2026-10-23 |
| D.P.R. 633/1972 art. 38-bis, execution of refunds | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art38bis!vig=2026-10-23 | 2026-10-23 |
| D.P.R. 633/1972 art. 19(5), pro-rata | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art19!vig=2026-10-23 | 2026-10-23 |
| D.P.R. 633/1972 art. 19-bis2, rettifica della detrazione | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art19bis.2!vig=2026-10-23 | 2026-10-23 |
| D.P.R. 542/1999 art. 6, annual balance and 0.40% deferral | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art6!vig=2026-10-23 | 2026-10-23 |
| D.P.R. 542/1999 art. 7, quarterly option and 1% interest | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 241/1997 art. 17, F24 offset and the 10-day rule | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art17!vig=2026-10-23 | 2026-10-23 |
| D.L. 78/2009 art. 10, visto di conformita for offset above EUR 5,000 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2009-07-01;78~art10!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 471/1997 art. 5, return penalties (as amended by D.Lgs. 87/2024) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art5!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 471/1997 art. 13, late payment and credit penalties | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 472/1997 art. 13, ravvedimento | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-23 | 2026-10-23 |
| L. 311/2004 art. 1(471), 97% acconto for large payers | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2004-12-30;311~art1!vig=2026-10-23 | 2026-10-23 |
| L. 388/2000 art. 34(1), EUR 2 million annual offset and refund cap | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-12-23;388~art34!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 33/2025 art. 243, payment code applies from 1 January 2027 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2025-03-24;33:1~art243!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 173/2024 art. 102, penalty code applies from 1 January 2027 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 10/2026, Testo unico IVA, art. 111 (acconto) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art111!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 10/2026, arts. 114 and 116 (refunds) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art114!vig=2026-10-23 and https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art116!vig=2026-10-23 | 2026-10-23 |
| D.Lgs. 10/2026, arts. 170 and 171 (repeals; applies from 1 January 2027) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art170!vig=2026-10-23 and https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art171!vig=2026-10-23 | 2026-10-23 |
| Agenzia delle Entrate, Modello IVA 2026 instructions (VAT year 2025) | https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711 | 2026-10-23 |
| Agenzia delle Entrate, acconto IVA: how it is computed | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24-acconto-iva-f24ivaacc/come-si-calcola-f24ivaacc | 2026-10-23 |
| Agenzia delle Entrate, acconto IVA: who pays | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24-acconto-iva-f24ivaacc/chi-deve-versare-f24ivaacc | 2026-10-23 |
| Agenzia delle Entrate, acconto IVA: how to pay | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24-acconto-iva-f24ivaacc/come-si-versa-f24ivaacc | 2026-10-23 |
| Agenzia delle Entrate, acconto IVA: special cases | https://www.agenziaentrate.gov.it/portale/web/guest/schede/pagamenti/f24-acconto-iva-f24ivaacc/casi-particolari-f24ivaacc | 2026-10-23 |
| Agenzia delle Entrate, Circolare 28/E of 15 December 2017 (acconto methods) | https://www.agenziaentrate.gov.it/portale/documents/20143/297699/Circolare+n+28+del+15+12+2017_Circolare+N.+28_E+DEL+15+DICEMBRE+2017+Acconto+IVA+Split.pdf/cc9c097b-405b-1680-c674-2b65887968ef | 2026-10-23 |
| Agenzia delle Entrate, "Come pagare l'Iva" | https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva | 2026-10-23 |

Not yet confirmed: row numbers are those of Modello IVA 2026 (VAT year 2025) until Modello IVA 2027 is approved; whether the storico base for a quarterly filer by option includes the 1% interest paid with last year's balance (Example 1 states the base as a single figure); the legal interest rate used in ravvedimento for 2026; when the repeal of art. 19-bis2(3) by D.Lgs. 186/2025 starts to apply.

> Contributed by Ryan Duguid.

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
