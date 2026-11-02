---
name: ba-corporate-income-tax
description: "Corporate income tax (porez na dobit) in Bosnia and Herzegovina for tax year 2026, set out separately for the Federation of BiH (FBiH), Republika Srpska (RS) and Brčko District (BD), each with its own law. Covers who pays and residence; the 10% rate; building the tax base from accounting profit; capped and non-deductible expenses; depreciation; interest limits (FBiH 4:1 related-party debt, RS 30% net interest cap); five-year loss carry-forward; investment, employment and export incentives; the 31 March return; monthly advances; withholding tax on payments to non-residents (FBiH 5% dividends and 10% other, RS 10%, BD 10% with dividends exempt); penalties and interest. Trigger phrases: Bosnia corporate tax, porez na dobit, FBiH profit tax, RS porez na dobit, Brčko profit tax, PP-801, porezni bilans, akontacija. Out of scope: personal income tax (bosnia-income-tax), VAT (bosnia-vat), payroll and contributions (bosnia-payroll, bosnia-social-contributions)."
version: 0.1
jurisdiction: BA
category: international
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina corporate income tax (2026)

Profit tax in Bosnia and Herzegovina is set and collected by the two entities and Brčko District, each under its own law:

- **FBiH:** Zakon o porezu na dobit ("Službene novine FBiH" 15/16 and 15/20), with the Pravilnik o primjeni Zakona o porezu na dobit (consolidated to 39/26). Authority: Porezna uprava FBiH (pufbih.ba).
- **RS:** Zakon o porezu na dobit ("Službeni glasnik RS" 94/15, 1/17, 58/19, 48/24 and 114/25; the 114/25 changes apply from 1 January 2026). Authority: Poreska uprava RS (poreskaupravars.org).
- **BD:** Zakon o porezu na dobit ("Službeni glasnik BD" 17/22 consolidated text and 38/22). Authority: Porezna uprava of the Direkcija za finansije BD.

Find out first where the company has its seat and where it has branches. That decides which law, which return and which tax office. The tax year is the calendar year in all three (FBiH art. 47; RS art. 37; BD art. 21). Amounts are in convertible marks (KM, BAM).

## Who this applies to

- **FBiH resident companies** pay FBiH profit tax on profit from the FBiH, RS, BD and abroad (FBiH art. 3(1)). A company is FBiH resident if its seat is entered in the FBiH court register, or if its place of actual management and supervision is in the FBiH (art. 5(1)).
- **RS resident companies** pay RS tax on profit from any source in the RS, FBiH, BD or abroad (RS art. 3(1)(1), as replaced by 1/17). Residence: seat entered in the RS register, or place of actual management and supervision in the RS (RS art. 3a).
- **BD companies** pay BD tax on profit from any source in BiH or abroad (BD art. 3(a)).
- **Branches of a company from another part of BiH** are taxed where the branch is registered, on the profit it earns there (FBiH art. 3(2); RS art. 3(1)(2); BD art. 3(b)). In the RS, from 2026 the branch base is set by the rules for non-resident permanent establishments (RS art. 5(2), as amended by 114/25).
- **Non-residents** (seat and management outside BiH) are taxed on profit of a permanent establishment, and by withholding tax on other income from that part of BiH (FBiH arts. 3(3), 3(4), 38; RS art. 3(1)(4) and (5); BD arts. 3(c) to (e)).
- **Outside the tax:** the Central Bank of BiH, public bodies, and non-profit bodies on budget income, donations, membership fees and similar non-market income. Their market activity is taxed (FBiH art. 4; RS art. 4; BD art. 4).
- Sole traders (obrtnici, preduzetnici) pay personal income tax, not profit tax. See `bosnia-income-tax`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Profit tax rate, FBiH | 10% of the tax base in the tax balance | 2026 | FBiH Zakon o porezu na dobit art. 31: https://ik.imagekit.io/9qcwbg8wl/15-16_i_15-20-zakon-o-porezu-na-dobit-precisceni_07YP9wNd9.pdf |
| Profit tax rate, RS | 10% | 2026 | RS Zakon o porezu na dobit art. 36(1): https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20porezu%20na%20dobit%20od%2001_01_2016.pdf |
| Profit tax rate, BD | 10% | 2026 | BD Zakon o porezu na dobit art. 20(1): https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf |
| Withholding tax, FBiH: dividends | 5% (lower under a treaty) | 2026 | FBiH art. 38(7) (URL above) |
| Withholding tax, FBiH: interest, royalties, services, rent and other listed payments | 10% (lower under a treaty) | 2026 | FBiH art. 38(1), (7) |
| Withholding tax, RS: all listed payments including dividends | 10% (lower under a treaty); the separate 5% dividend rate was deleted from 2017 | 2026 | RS art. 44, as amended by 1/17 art. 15: https://www.poreskaupravars.org/dokumenti/zakoni/ZakonoizmdopDobit.pdf |
| Withholding tax, BD | 10% of the gross payment; dividends exempt | 2026 | BD arts. 29(2)(d), 30(1) |
| Representation (business entertainment), all three | 30% deductible | 2026 | FBiH art. 12(1); RS art. 15; BD art. 8(2)(a) |
| Donations, FBiH | Up to 3% of total revenue | 2026 | FBiH art. 12(3) |
| Sponsorship, FBiH | Up to 3% of total revenue | 2026 | FBiH art. 12(4) |
| Donations, RS | Up to 3% of total revenue | 2026 | RS art. 16 |
| Sponsorship, RS | Up to 2% of total revenue | 2026 | RS art. 17 |
| Product and service complaints, RS | Up to 3% of operating revenue | 2026 | RS art. 18 |
| Donations, BD | Up to 3% of total revenue (public institutions, humanitarian, cultural, educational, scientific); sport up to 10% | 2026 | BD art. 8(2)(f), (g), as amended by 38/22: https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/06B38-22%20Zakon%20o%20izmjeni%20i%20dopunama%20Zakona%20o%20porezu%20na%20dobit.pdf |
| Sponsorship, BD | Up to 2% of total revenue | 2026 | BD art. 8(2) (sponsorship point, renumbered by 38/22) |
| Chamber membership fees, BD | Up to 0.2% of total revenue | 2026 | BD art. 8(2) (membership point) |
| Warranty provisions, FBiH | Up to 4% of annual turnover of the guaranteed products | 2026 | FBiH art. 13(3) |
| Environmental provision, FBiH | Up to 30% of taxable profit before the provision; total never above registered capital | 2026 | FBiH art. 13(2) |
| Related-party financing, FBiH | Interest on debt above 4:1 debt to registered capital is not deductible (not for banks, leasing and insurance companies) | 2026 | FBiH art. 18(2), (4) |
| Net interest cap, RS | Net interest expense above 30% of the tax base (calculated without interest income and expense) is not deductible | 2026 | RS art. 14a, as added by 1/17 and amended by 114/25 art. 7: https://poreskaupravars.org/wp-content/uploads/2025/12/Dobit-1.pdf |
| Depreciation, FBiH (straight line) | Buildings 5%; roads, utilities, railways 10%; equipment, vehicles, plant 15%; water systems equipment 15%; hardware, software, environmental equipment 33.3%; perennial crops 15%; basic herd 40%; intangibles 20% | 2026 | FBiH art. 19(2) |
| Accelerated depreciation, FBiH | Up to 50% above the art. 19 rates for pollution-prevention assets | 2026 | FBiH art. 20 |
| Depreciation, RS | Real estate and plant 3%, intangibles other than software 10% (straight line, per asset); computers, IT systems, software and servers 40%, equipment and other assets 20% (declining balance, per pool) | 2026 | RS art. 12, as replaced by 1/17 art. 5 |
| Depreciation, BD (machines and equipment) | Accelerated: 40% year 1, 30% year 2, 30% year 3; computer hardware and software fully deductible in the year of purchase | 2026 | BD art. 11(4), (6) |
| Small asset write-off | FBiH and BD: asset costing under KM 1,000 deducted in full in the year of purchase; RS: a pool base under KM 1,000 deducted in full | 2026 | FBiH art. 19(5); BD art. 11(5); RS art. 12(7) |
| Tax loss carry-forward | 5 years, oldest first, all three | 2026 | FBiH art. 25; RS art. 25(2), (3); BD art. 13(2), (3) |
| Investment incentive, FBiH | Tax reduced by 30% if own-funds investment in production equipment is above 50% of the year's profit; or by 50% for KM 20 million invested over five years with KM 4 million in year one | 2026 | FBiH art. 36(2), (4) |
| Employment incentive, FBiH | Double deduction of gross wages of new full-time hires on contracts of at least 12 months | 2026 | FBiH art. 37(1) |
| Investment incentive, RS | Tax base reduced by the value of production equipment and plant invested in the RS | 2026 | RS art. 26, as replaced by 58/19: https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20porezu%20na%20dobit%20SG%202019.pdf |
| Investment incentive, BD | Tax base reduced by the year's investment, capped at 50% of the base; no cap for production land, buildings, plant and machinery | 2026 | BD art. 38(1), (2) |
| Transfer pricing transaction overview, FBiH | Filed with the return when related-party transactions exceed KM 500,000 in the year | 2026 | FBiH art. 49(3) |
| Transfer pricing documentation, RS | Needed for related-party transactions over KM 50,000 in the year; filed electronically within 9 months after year end | 2026 | RS art. 34, as amended by 114/25 art. 10 |
| Late-payment interest, FBiH | 0.04% a day | 2026 | Zakon o visini stope zatezne kamate na javne prihode art. 2: https://pufbih.ba/v1/public/upload/zakoni/1%20Zakon%20o%20visini%20stope%20zatezne%20kamate%20na%20javne%20prihode%20-%20PRECISCEN%20TEKST.pdf |
| Late-payment interest, RS | 0.03% a day | 2026 | Zakon o poreskom postupku RS art. 60(1): https://poreskaupravars.org/wp-content/uploads/2020/11/Zakon-o-poreskom-postupku.pdf |
| Late-payment interest, BD | 0.03% a day, capped at the principal | 2026 | Zakon o Poreznoj upravi BD art. 68: https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20Poreznoj%20upravi%20Brc--ko%20Distrikta%20BiH/011B11-20%20Zakon%20%20o%20poreznoj%20upravi%20Brcko%20distrikta%20BiH.pdf |

## The taxable base

**Starting point.** In all three the base starts from the profit in the financial statements prepared under the accounting rules, adjusted by the profit tax law in a tax balance (FBiH arts. 7, 8; RS arts. 5, 6, 8; BD art. 5). In the FBiH the base is accounting profit plus non-deductible expenses, minus non-taxable items (art. 7(2)). Expenses must be documented, net of deductible VAT, and incurred to earn profit (FBiH art. 7(5)).

**Income left out of the base.**
- FBiH: dividends and profit shares from another taxpayer paid out of taxed profit, with a certified statement from the payer (art. 21); reversals of provisions that were not deducted (art. 23(1)); recoveries of receivables that were not deducted (art. 22(2)).
- RS (art. 7 as replaced by 114/25 from 2026): dividends from a company seated in the RS paid from taxed profit; gains booked directly in equity; reversals of provisions; revaluation income on depreciable assets and inventory; recoveries of receivables not previously deducted; reversals of share impairments that were not deducted. Interest on RS or RS municipality bonds is excluded only for bonds acquired by 31 December 2025.
- BD (art. 7): dividends and profit shares received by a BD company; recoveries of receivables not previously deducted; interest on securities issued or guaranteed by BiH, BD, the entities, the Central Bank, companies, insurers, investment funds and banks; income on which the payer paid withholding tax.

**Non-deductible expenses (main items).**
- FBiH art. 9: late-payment interest and enforcement costs on public revenue; fines; profit tax itself; withholding tax borne by the payer; payments to political parties; profit distributions; expenses not linked to earning profit; interest above the art. 18 limit; write-downs of receivables from a party the company also owes; default interest and penalties between related parties; non-recognised provisions.
- RS art. 9: undocumented expenses; late-payment interest; fines, contract penalties; enforcement costs; expenses linked to exempt income; stock losses from expiry; gifts to political parties; withholding tax borne by the payer; losses booked in equity; revaluation and impairment expenses; goodwill impairment; from 2026 also impairment of shares in other companies (114/25 art. 5).
- BD art. 8(3): profit tax; fines and interest for breaking the law; undocumented expenses; expenses above market price paid to related parties; losses on sales between related parties; donations to political parties; personal costs; dividends; goodwill amortisation.

**Bad debts.**
- FBiH art. 17: deductible if the receivable was in income and is unpaid 12 months after due date, or is sued, in enforcement, or filed in bankruptcy or liquidation.
- RS art. 21: 25% of a receivable older than 12 months, 50% older than 18 months, 75% older than 24 months. 100% if unpaid after 12 months and the company sued, sought enforcement, or filed the claim in bankruptcy. From 2026 the same rules cover write-downs of loans given (114/25 art. 8).
- BD art. 10: unpaid 12 months after due date and sued or in enforcement, or filed in bankruptcy.

**Depreciation** follows the rates in the table. FBiH allows depreciation only on assets in use (art. 19(4)). Right-of-use assets are depreciated by the lessee over the lease term (art. 19(3)). RS allows depreciation on owned assets and assets held under finance lease (art. 12a(3)). Leasehold improvements count where they increase the asset's cost and do not reduce the rent (art. 12a(4)). RS declining-balance pools go up by additions and down by disposal proceeds. A negative pool is added to the base (art. 12(4), (5)).

**Losses.** A tax loss is carried forward for five years and the oldest loss is used first (FBiH art. 25(1) to (3); RS art. 25; BD art. 13). A loss of an FBiH company made in the RS, BD or abroad is not recognised (FBiH art. 25(4)). RS and BD rules exclude losses of branches outside the territory and of foreign permanent establishments (RS art. 25(5), (6); BD art. 13(5)). None of the three laws provides a carry-back.

**Capital gains** are part of the base. In the FBiH the gain is the transaction value less cost minus tax depreciation. Market value is used if the agreed price is lower (art. 24(2) to (4)). RS uses sale price less adjusted base, and the tax office can substitute market price (art. 24). BD is the same (art. 12).

**Incentives** (one per year in the FBiH, art. 36(8)):
- FBiH art. 36(2): 30% off the tax if own-funds investment in production equipment (not passenger cars) exceeds 50% of the year's profit. Art. 36(4): 50% off the tax in the investment years for KM 20 million invested over five years with KM 4 million in year one. The relief is clawed back with interest if the company pays a dividend from the relieved profit up to the third year after the last relief year, misses the KM 20 million, or uses a loss carry-forward before the end of the second year after the last relief year (art. 36(6), (7)).
- FBiH art. 37: double deduction of gross wages for new hires (full-time, at least 12 months, not employed by the company or a related party in the previous five years).
- RS art. 26: base reduced by the value of production equipment and plant put into use in the RS. Selling or letting the asset within three years claws the relief back with interest.
- BD art. 38: base reduced by the year's investment in land, buildings, plant, machinery, furniture and vehicles for the company's own activity, capped at 50% of the base. No cap for production assets. Disposal within five years loses the relief. Art. 39: base reduced by gross wages of new permanent hires. Art. 39a: export relief in proportion to twice the export share of revenue, not for services or intangibles, and only for producers seated in BD (38/22 art. 2).

**Groups.** FBiH: companies with more than 50% direct or indirect control, all FBiH residents, can apply for tax consolidation. Once approved it lasts at least five years (FBiH arts. 41 to 43). BD: groups linked by at least 80% ownership may file a consolidated return (art. 33). The RS law has no group consolidation.

## Deadlines and filing

| Step | FBiH | RS | BD |
|---|---|---|---|
| Annual return | Prijava poreza na dobit (PP-801 for companies) with tax balance PB-800, by 31 March (law art. 49(1): 30 days after the financial statements deadline; Pravilnik art. 101(1)) | Annual return within 90 days of year end, by 31 March for a calendar year (art. 38(1)) | By 31 March for a calendar year (art. 22(1)); paper or electronic (art. 32a) |
| Final payment | Balance within 20 working days after filing (art. 53(2)) | With the return, by 31 March (art. 38) | With the return, by 31 March (art. 22(2)) |
| Monthly advances | Equal monthly advances, each due by the end of the month for the previous month, based on the last return (arts. 52(1), (3), 53(1)) | Monthly, by the 10th for the previous month, based on the last return (art. 39(1)) | Monthly, by the 10th for the previous month, based on the last return (art. 24(1)) |
| First year | No advances until the first return (art. 52(7)) | File a return with a profit estimate within 30 days of starting business (art. 39(3)) | Not stated in the law |
| Changing advances | On request after a status change, an expected loss or a disaster (art. 52(4)) | On request if profit is expected to differ (art. 39(2)) | On request (art. 24(3)) |
| Withholding tax | Payer files and pays within 10 days after the month of payment (art. 38(5)); POD-815 to POD-819 forms | Withheld at payment (art. 47); annual WHT return within 30 days after year end (art. 38(2), added by 1/17) | Withheld at payment (arts. 28, 30); annual WHT return by 31 March (arts. 22, 32) |
| Amended return | Within 180 days of the first return (art. 50(1)) | Under the tax procedure law | Under the tax administration law |
| Transfer pricing | Documentation held at filing; given within 45 days of a request (art. 46); transaction overview with the return above KM 500,000 (art. 49(3)) | Documentation held at filing for transactions over KM 50,000; given within 30 days of a request and filed within 9 months after year end without a request (art. 34) | Tax office adjusts to market price (art. 9) |
| Other | Dividends cannot be paid while direct taxes, contributions or wages are overdue (art. 55) | Dividends cannot be paid while taxes are overdue (art. 54); contracts with a non-resident acting through a PE reported within 5 days (art. 42) | |

Liquidation (FBiH art. 29(2)): returns within 30 days of opening and of closing the liquidation.

## Penalties and interest

**FBiH.**
- Late-payment interest is 0.04% a day on public revenue not paid on time (Zakon o visini stope zatezne kamate art. 2). It applies to unpaid profit tax and unpaid advances (profit tax law art. 54(1)).
- Fine of KM 3,000 to 100,000 for the company, plus KM 2,500 to 10,000 for the responsible person (art. 58(2), (3)). It applies to: not filing the return or tax balance; not filing a withholding tax return; paying a dividend while in arrears; non-arm's-length related-party pricing; missing transfer pricing documentation; and self-assessed tax lower than assessed tax. Repeat offences add 50% (art. 58(4)).
- Fine of KM 2,000 to 30,000 for not paying advances or the final balance on time, plus KM 1,000 to 3,000 for the responsible person (art. 59).

**RS.**
- Interest 0.03% a day from the day after the due date (Zakon o poreskom postupku art. 60).
- Not filing a return, or filing late: KM 2,000 to 6,000 for the company, KM 1,000 to 3,000 for the responsible person (art. 112(1), (3)).
- Neither declaring nor paying a tax: 30% of the tax found in an audit, up to KM 200,000 (art. 115).
- Profit tax law art. 58: KM 20,000 to 60,000 (responsible person KM 5,000 to 15,000) for missing or late transfer pricing documentation, a missing controlled-transaction return, or paying dividends while taxes are overdue.
- Profit tax law art. 59: KM 5,000 to 15,000 for not reporting a PE contract within 5 days.

**BD.**
- Interest 0.03% a day, capped at the principal (Zakon o Poreznoj upravi art. 68).
- Not filing a return or not keeping books: KM 1,000 to 5,000 for the company, KM 200 to 1,000 for the responsible person (art. 76).

## Cross-border points

- **Withholding tax.**
  - FBiH (art. 38): dividends 5%; 10% on interest, royalties, management, technical and training services (including market research, tax advice, audit and consulting), rent, entertainment and sport, insurance premiums and telecom services. Other services are taxed only when paid to residents of countries without a BiH treaty. Exempt: supplier credit interest for production equipment, government bond interest, and some reinsurance premiums (art. 38(3)). The base is the gross amount (art. 38(6)).
  - RS (arts. 44, 45): 10% on dividends, interest, royalties, entertainment and sport, professional, scientific, technical and educational services, insurance, telecom and movable rent. Other services are covered only where there is no treaty (art. 45(2)). Payments in kind are covered too (art. 45(3)).
  - RS exemptions (art. 46, as amended by 58/19, 48/24 and 114/25): no WHT on profit a PE sends home, on interest on loans for production equipment and plant under art. 26, or on interest and insurance premiums on loans for projects the National Assembly declared of special importance. From 1 January 2026 interest on RS and RS municipality bonds is no longer exempt (114/25 art. 14 deleted that point).
  - BD (arts. 29, 30): 10% on interest, entertainment and sport, management, consulting, financial, technical and administrative services, insurance, royalties and movable rent. No WHT on dividends, deposit interest, foreign bank loan interest and some other items (art. 29(2)).
- **Treaty rates.** A lower treaty rate needs the recipient's residence certificate, no older than one year (FBiH art. 40(1); RS art. 52(1)). In the FBiH the recipient also signs a beneficial-owner statement (art. 40(1)). In the RS, for a lower treaty rate, the payer also holds a certified statement on the income and the recipient on the prescribed form and keeps the proof in its own records (art. 52(2), (3), as amended by 114/25 art. 16). If the payer does not withhold, the payer owes the tax (FBiH art. 40(2); RS art. 47(3)).
- **Sale of BiH property or shares by a non-resident.** FBiH taxes income from selling FBiH real estate, long-term shareholdings or industrial property. The non-resident files and pays within 30 days, failing which the buyer or the company whose shares were sold is liable (art. 39). RS taxes non-resident gains on RS real estate and on shares in companies whose assets are mostly RS real estate (art. 43). From 2026 it also taxes FBiH and BD companies on sales of shares in RS residents (art. 3(1)(3), amended by 114/25).
- **Credit for tax paid elsewhere.**
  - FBiH residents credit profit tax paid by branches in the RS or BD and tax paid abroad, capped at the FBiH tax on that profit (art. 32).
  - RS residents credit foreign tax, capped at the RS tax (art. 50). They credit tax paid in the other entity or BD on branch profit (art. 51).
  - BD residents credit tax paid in the entities or abroad, or may deduct it as an expense instead (arts. 23, 27).
- **Permanent establishment.** RS: from 2026 a building or installation site is a PE only if it lasts more than 12 months (art. 41(1)(2), amended by 114/25). A treaty definition prevails (art. 41(7)).

## Worked examples

### Example 1: FBiH d.o.o., ordinary year

A Sarajevo d.o.o. shows accounting profit of KM 200,000 for 2026. It spent KM 10,000 on business entertainment and paid a KM 2,000 fine. It has an unused 2023 tax loss of KM 30,000. It paid monthly advances of KM 1,200 in 2026 (12 payments).

Only 30% of entertainment is deductible (art. 12(1)), so KM 7,000 is added back. The fine is not deductible (art. 9(1)(c)). The 2023 loss is still within five years (art. 25). The tax base is 200,000 + 7,000 + 2,000 - 30,000 = KM 179,000. Tax at 10% (art. 31) is KM 17,900. Advances paid were KM 14,400, so KM 3,500 is due within 20 working days of filing (art. 53(2)). The 2027 monthly advance, until the next return, is 17,900 / 12 = KM 1,491.67 (art. 52(1), (3)).

```oa-check
name: FBiH d.o.o. 2026 profit tax with entertainment add-back and loss
inputs:
  accounting_profit: 200000
  entertainment: 10000
  fine: 2000
  loss_2023: 30000
  monthly_advance_paid: 1200
steps:
  - entertainment_addback: entertainment * 0.70
  - base_before_loss: accounting_profit + entertainment_addback + fine
  - loss_used: min(loss_2023, base_before_loss)
  - tax_base: base_before_loss - loss_used
  - tax: tax_base * 0.10
  - advances_paid: monthly_advance_paid * 12
  - balance_due: tax - advances_paid
  - advance_2027: round(tax / 12, 2)
expected:
  entertainment_addback: 7000
  base_before_loss: 209000
  loss_used: 30000
  tax_base: 179000
  tax: 17900
  advances_paid: 14400
  balance_due: 3500
  advance_2027: 1491.67
```

### Example 2: RS company with the 30% interest cap, a sponsorship cap and a dividend to a foreign parent

A Banja Luka company has 2026 total revenue of KM 1,000,000 and accounting profit of KM 500,000. Interest expense is KM 320,000 and interest income KM 20,000, so net interest expense is KM 300,000. Sponsorship cost KM 30,000. In 2027 it pays a KM 100,000 dividend to its parent in a country with no BiH treaty.

Sponsorship is deductible up to 2% of total revenue (art. 17): KM 20,000, so KM 10,000 is added back. For the interest cap (art. 14a), take the base without interest: 500,000 + 300,000 + 10,000 = KM 810,000. 30% of that is KM 243,000. Net interest above that, KM 57,000, is added back. The tax base is 500,000 + 10,000 + 57,000 = KM 567,000. Tax at 10% (art. 36) is KM 56,700, payable by 31 March 2027 (art. 38). The dividend bears 10% RS withholding tax (arts. 44, 45(1)): KM 10,000. The parent receives KM 90,000.

```oa-check
name: RS company 2026, net interest cap, sponsorship cap, dividend WHT
inputs:
  total_revenue: 1000000
  accounting_profit: 500000
  interest_expense: 320000
  interest_income: 20000
  sponsorship: 30000
  dividend: 100000
steps:
  - net_interest: interest_expense - interest_income
  - sponsorship_cap: total_revenue * 0.02
  - sponsorship_addback: max(0, sponsorship - sponsorship_cap)
  - base_without_interest: accounting_profit + net_interest + sponsorship_addback
  - interest_cap: base_without_interest * 0.30
  - interest_addback: max(0, net_interest - interest_cap)
  - tax_base: accounting_profit + sponsorship_addback + interest_addback
  - tax: tax_base * 0.10
  - dividend_wht: dividend * 0.10
  - net_dividend: dividend - dividend_wht
expected:
  net_interest: 300000
  sponsorship_cap: 20000
  sponsorship_addback: 10000
  base_without_interest: 810000
  interest_cap: 243000
  interest_addback: 57000
  tax_base: 567000
  tax: 56700
  dividend_wht: 10000
  net_dividend: 90000
```

## Ask the client first

1. Where is the company's registered seat, and where is it actually managed? Does it have branches in another entity or in Brčko District? This decides which law applies and where each return goes.
2. Did it make tax losses in the last five years, and in which part of BiH?
3. Does it have loans or other transactions with related parties, and what were the totals for the year? This decides the FBiH 4:1 test, the RS 30% interest cap, the FBiH KM 500,000 overview and the RS KM 50,000 documentation.
4. Does it pay dividends, interest, royalties or service fees to non-residents, and in which countries are they resident?
5. Did it invest in production equipment or hire new staff in the year? Is it a producer that exports?
6. Are any taxes, contributions or wages overdue? If so, no dividend can be paid (FBiH art. 55; RS art. 54).

## Sources

| Source | URL | Read on |
|---|---|---|
| FBiH Zakon o porezu na dobit, Sl. novine FBiH 15/16 and 15/20, consolidated unofficial text published by Porezna uprava FBiH: arts. 3 to 9, 11 to 13, 17 to 25, 29, 31 to 33, 36 to 47, 49 to 55, 58, 59 | https://ik.imagekit.io/9qcwbg8wl/15-16_i_15-20-zakon-o-porezu-na-dobit-precisceni_07YP9wNd9.pdf | 2026-10-30 |
| FBiH Zakon o porezu na dobit, original 15/16 (to check art. 49 and 53 wording) | https://ik.imagekit.io/9qcwbg8wl/15-16-zakon-o-porezu-na-dobit_1_TIDKtIiPQ.pdf | 2026-10-30 |
| FBiH Zakon o izmjenama i dopunama Zakona o porezu na dobit, 15/20 | https://ik.imagekit.io/9qcwbg8wl/15-20-izmjena-zakona-o-porezu-na-dobit_WppmLJCQR.pdf | 2026-10-30 |
| FBiH Pravilnik o primjeni Zakona o porezu na dobit, consolidated to 39/26: arts. 1, 78, 79, 83, 101, 104 | https://pufbih.ba/v1/public/upload/zakoni/03062026%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dobit%2039-26.pdf | 2026-10-30 |
| FBiH Zakon o visini stope zatezne kamate na javne prihode, consolidated, and amendment 35/26: art. 2 | https://pufbih.ba/v1/public/upload/zakoni/1%20Zakon%20o%20visini%20stope%20zatezne%20kamate%20na%20javne%20prihode%20-%20PRECISCEN%20TEKST.pdf | 2026-10-30 |
| Porezna uprava FBiH, list of regulations in force (data behind pufbih.ba) | https://pufbih.ba/api/regulations | 2026-10-30 |
| RS Zakon o porezu na dobit, Sl. glasnik RS 94/15 | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20porezu%20na%20dobit%20od%2001_01_2016.pdf | 2026-10-30 |
| RS amendment 1/17 (arts. 3, 3a, 3b, 7, 12, 12a, 14a, 21, 26, 27, 38, 44, 45, 50, 52) | https://www.poreskaupravars.org/dokumenti/zakoni/ZakonoizmdopDobit.pdf | 2026-10-30 |
| RS amendment 58/19 (arts. 4, 7, 10, 12a, 13, 14, 22, 26, 37, 46) | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20porezu%20na%20dobit%20SG%202019.pdf | 2026-10-30 |
| RS amendment 48/24 (art. 46) | https://poreskaupravars.org/wp-content/uploads/2024/06/Zakon.pdf | 2026-10-30 |
| RS amendment 114/25, in force 1 January 2026 (arts. 2, 3, 5, 7, 9, 10, 14a, 21, 23, 34, 41, 46, 50) | https://poreskaupravars.org/wp-content/uploads/2025/12/Dobit-1.pdf | 2026-10-30 |
| Poreska uprava RS, list of profit tax laws in force | https://poreskaupravars.org/pravna-lica/propisi-o-porezu-na-dobit/?lang=lat | 2026-10-30 |
| RS Zakon o poreskom postupku, Sl. glasnik RS 78/20 (and 37/22): arts. 60, 112, 115 | https://poreskaupravars.org/wp-content/uploads/2020/11/Zakon-o-poreskom-postupku.pdf | 2026-10-30 |
| BD Zakon o porezu na dobit, consolidated text Sl. glasnik BD 17/22 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf | 2026-10-30 |
| BD Zakon o izmjeni i dopunama Zakona o porezu na dobit, 38/22 (applies from 1 January 2023) | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/06B38-22%20Zakon%20o%20izmjeni%20i%20dopunama%20Zakona%20o%20porezu%20na%20dobit.pdf | 2026-10-30 |
| BD Zakon o Poreznoj upravi (2020): arts. 68, 76 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20Poreznoj%20upravi%20Brc--ko%20Distrikta%20BiH/011B11-20%20Zakon%20%20o%20poreznoj%20upravi%20Brcko%20distrikta%20BiH.pdf | 2026-10-30 |

Not yet confirmed: treaty withholding rates (the old version said 0% with Ireland and a 25% holding for many reduced dividend rates; no official treaty text was read, so no treaty rate is given here); the RS and BD form codes and the RS withholding tax payment deadline set in their rulebooks (rulebooks not read); the FBiH and RS financial statements deadlines that the FBiH return date hangs on (the 31 March return date is taken from the FBiH Pravilnik art. 101 and the RS law art. 38 directly); whether BD has later amendments after 38/22 (the BD Assembly list shows none); FBiH late-filing fines under the FBiH tax administration law beyond those in the profit tax law. The RS 94/15, 1/17, 58/19, 48/24, 114/25 and 78/20 texts were read from OCR of the official gazette scans published by Poreska uprava RS.

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
