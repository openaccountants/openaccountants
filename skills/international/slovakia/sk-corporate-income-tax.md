---
name: sk-corporate-income-tax
description: "Slovak corporate income tax (daň z príjmov právnických osôb) for tax year 2026 under Act No. 595/2003 Coll. as amended, including Act No. 261/2025 Coll. Covers the three rates set by taxable revenue (10% up to EUR 100,000, 24% above EUR 5,000,000, 21% otherwise), the minimum tax with its new EUR 11,520 band for revenue above EUR 5,000,000, the tax base from accounting profit, paid-basis expenses, unrecoverable VAT, depreciation groups 0 to 6, the 5-year loss carry-forward with the 50% cap, the two interest limits (25% EBITDA for related-party loans and 30% above EUR 3,000,000 net interest), dividends, advances, the DPPO return and extensions, and penalties. Trigger on: Slovakia corporate tax, DPPO, s.r.o. tax, 10% rate Slovakia, minimálna daň, daňová licencia, preddavky na daň. Out of scope: individuals (slovakia-pit), payroll (sk-payroll-social), VAT (slovakia-vat-return), company set-up (sk-company-formation)."
version: 0.4
jurisdiction: SK
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovak corporate income tax (DPPO): 2026 rates, minimum tax, losses and filing v0.4

The law is the Income Tax Act, Act No. 595/2003 Coll. (zákon o dani z príjmov). This skill reads the consolidated version in force from 1 January 2026 on slov-lex.sk, which includes the consolidation package Act No. 261/2025 Coll. Penalties and interest come from the Tax Procedure Code, Act No. 563/2009 Coll. (daňový poriadok). The Financial Administration (Finančná správa) runs the return and the portal at financnasprava.sk. Figures are for the 2026 tax period: the calendar year 2026, or a fiscal year (hospodársky rok) that ends in 2026 or 2027. Where a rule applies only to periods that start on or after 1 January 2026, the skill says so.

## Who this applies to

- **Slovak-resident legal persons**: a company with its seat or place of effective management in Slovakia (§ 2(d) second point). Typical clients: s.r.o., a.s., cooperatives. They are taxed on worldwide income.
- **Non-resident legal persons** with Slovak-source income (§ 16), in particular a permanent establishment in Slovakia. A registered permanent establishment files a DPPO return like a resident. Slovak income with no permanent establishment is mostly taxed by withholding (§ 43); see "Cross-border points".
- **Non-profit bodies** (§ 12(3)) are taxed only on part of their income. Not covered here.

Not covered here, refer to a specialist: banks, insurers and leasing companies (special interest and reserve rules); companies in liquidation or bankruptcy (special tax periods in § 41); the special 54% base for banks on card-payment fees to gaming accounts (§ 51eb, new from 2026); the Pillar Two top-up tax under Act No. 507/2023 Coll. (scope check only: multinational and large domestic groups); controlled foreign companies; hybrid mismatches; mergers and divisions; the R&D super-deduction (§ 30c) and the investment deduction (§ 30e) beyond a pointer; transfer pricing documentation.

Related skills: an overview in [sk-tax-overview](sk-tax-overview.md); individuals in [slovakia-pit](slovakia-pit.md); employer contributions in [sk-payroll-social](sk-payroll-social.md); VAT in [slovakia-vat-return](slovakia-vat-return.md); setting up a company in [sk-company-formation](sk-company-formation.md).

## Rates, bands and thresholds

"Taxable revenue" below is zdaniteľné príjmy (výnosy): the company's taxable income in the revenue sense, before expenses. It is not the tax base. The rate band is chosen by revenue, then the single rate applies to the whole tax base after losses. There is no slicing: a company with EUR 100,001 of taxable revenue pays 21% on all of its base.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| CIT rate, taxable revenue up to EUR 100,000 (§ 15(b)(1a)) | 10% of the base after losses | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| CIT rate, taxable revenue above EUR 100,000 and up to EUR 5,000,000 (§ 15(b)(1b)) | 21% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| CIT rate, taxable revenue above EUR 5,000,000 (§ 15(b)(1c)) | 24% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Exit tax special base (§ 17f, rate in § 15(b)(3)) | 21% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Dividends received from a non-cooperating state, special base (§ 51e(4), rate in § 15(b)(2)) | 35% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Yield on Slovak, EU or EEA state bonds and treasury bills, special base (§ 51ea, rate in § 15(b)(4)) | 13% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, taxable revenue up to EUR 50,000 (§ 46b(2)(a)) | EUR 340 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 50,000 up to EUR 250,000 (§ 46b(2)(b)) | EUR 960 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 250,000 up to EUR 500,000 (§ 46b(2)(c)) | EUR 1,920 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 500,000 up to EUR 5,000,000 (§ 46b(2)(d)) | EUR 3,840 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 5,000,000 (§ 46b(2)(e), new: Act No. 261/2025, periods starting on or after 1 January 2026) | EUR 11,520 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2025/261/20260101.html |
| Micro-taxpayer (mikrodaňovník): revenue up to EUR 60,000 **and all §2(w) conditions below** | Full loss offset, no 50% cap | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Loss carry-forward (§ 30) | 5 periods; capped at 50% of the base unless a micro-taxpayer | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Related-party interest limit (§21a), subject to lender/borrower and capitalised-interest boundaries below | Covered interest above 25% of accounting EBITDA is not deductible; no §21a adjustment if §17k increased the base | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Interest limitation rule (§17k), subject to exceptions and contract-date transition below | If covered net borrowing costs exceed EUR 3,000,000, add back their excess over 30% of statutory tax EBITDA; blocked costs have a five-period carry-forward | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Depreciable tangible movable asset (§ 22(2)(a)) | Entry price above EUR 1,700 and useful life over one year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Advances, prior-year tax above EUR 16,600 (§ 42(1)) | Monthly, 1/12 of prior-year tax | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Advances, prior-year tax above EUR 5,000 up to EUR 16,600 (§ 42(2)) | Quarterly, 1/4 of prior-year tax | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| No advances, prior-year tax up to EUR 5,000 (§ 42(3)(a)) | None, unless the tax office orders them | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Withholding tax, standard (§ 43(1)(b)) | 19% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Withholding tax, payee in a non-cooperating state (§ 43(1)(c)) | 35% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Late payment interest (Tax Procedure Code § 156(2)) | 4 times the ECB main rate a year, at least 15% a year, for at most 4 years. At the ECB main refinancing rate of 2.65% (from 16 September 2026) the 15% floor applies | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html |

## The taxable base

**Start from accounting profit.** A company that keeps double-entry books starts from the profit or loss in its statutory accounts (Slovak GAAP or IFRS), then adds back and deducts the items the Act lists (§ 17). The result, less tax losses, is the base the rate applies to.

**Common add-backs.**
- Expenses that are not tax expenses under § 21, such as representation (entertainment) costs, and fines and penalties imposed by public bodies.
- Expenses deductible only when paid (§ 17(19)). Among them: rent and royalties; marketing and market studies; commissions; legal and advisory services under CPA codes 69.1, 69.2, 70.1 and 70.22; contractual penalties and late payment interest owed by the company; payments to a person in a non-cooperating state once withholding duties are met. If they are booked in 2026 and paid in 2027, they come into the 2027 base.
- From 1 January 2026, the nondeductible-VAT rule in § 52zzzk applies specifically to VAT restricted under [VAT Act § 85n](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-85n), as its footnote 161 states. That restricted vehicle-related VAT is not a tax expense and, for the specified tangible vehicle, is not part of its tax entry price; the linked later business/private-use VAT change is outside the income-tax base. This is not a general disallowance of all VAT that an exempt or mixed business cannot recover. Ordinary nondeductible VAT and coefficient VAT follow § 19(3)(k): eligible expense VAT can be a tax expense; VAT included in tangible/intangible asset entry price under § 25(5)(b)/(c) instead follows the asset treatment. For example, outside the § 85n restriction, a qualifying machine costing EUR 10,000 plus EUR 2,300 VAT, with 60% VAT recovery, has EUR 920 nondeductible VAT and tax entry price EUR 10,920, not an automatic EUR 920 add-back ([ITA §§ 19, 25 and 52zzzk](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html)).
- Accounting depreciation above tax depreciation.
- Interest caught by § 21a or § 17k (see below).

**Common deductions.** Income not subject to tax, such as most dividends (§ 12(7)(c), below); tax depreciation above accounting depreciation; the R&D super-deduction (§ 30c: 100% of R&D costs, plus 100% of the increase in the two-year average of R&D costs over the average of the two prior periods) and the investment deduction (§ 30e) where the conditions are met.

**Depreciation (§ 26 and § 27).** Tangible assets go into one of seven groups. Straight-line annual depreciation (§ 27) is entry price divided by the period. In the first year only the months from the month the asset is put into use count. Assets in groups 2 and 3 may instead be depreciated by the accelerated method (§ 28); the method is chosen per new asset and cannot be changed (§ 26(3)). A micro-taxpayer may depreciate assets placed in use in a micro-taxpayer period in groups 0 to 4 in any amount it chooses within the group period, except cars with an entry price of EUR 48,000 or more (§ 26(12)).

| Group | Period | Annual straight-line share |
|---|---|---|
| 0 | 2 years | 1/2 |
| 1 | 4 years | 1/4 |
| 2 | 6 years | 1/6 |
| 3 | 8 years | 1/8 |
| 4 | 12 years | 1/12 |
| 5 | 20 years | 1/20 |
| 6 | 40 years | 1/40 |

**Classify the actual asset before choosing the period.** Annex 1 uses CPA (KP) product codes and KS building codes; its code controls where the short name differs. Keep the asset specification and the vehicle registration certificate. Common entries are:

| Asset and actual Annex 1 entry | CPA/KP or KS code | Group and ordinary period | Official source |
|---|---|---|---|
| Computers and peripheral equipment, item 1-13 | CPA 26.2 | 1: four years | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1) |
| Ordinary passenger car, item 1-24, excluding the qualifying BEV/PHEV entry | CPA 29.10.2 | 1: four years | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1) |
| Passenger car whose registration certificate Part II, field “18 P.3 Druh paliva/zdroj energie”, states BEV or PHEV in any combination with another fuel/energy source, item 0-1 | CPA 29.10.2 | 0: two years | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1) |
| Furniture, item 2-33 | CPA 31.0 | 2: six years | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1) |
| Residential buildings, item 6-1; hotels and similar buildings, item 6-2; administrative buildings, item 6-3 | KS 11; 121; 1220 | 6: forty years, with the specific §26(14) hotel/sports rule below | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1),(14) |
| Culture/entertainment/education/health buildings, item 6-4 | KS 126 | 6: forty years; the sports subset is separately addressed below | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1),(14) |
| Other non-residential buildings, item 6-5 | KS 127, except 1271 agricultural buildings and the stated 1274 firefighter buildings/barracks | 6: forty years for the included codes | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1) |
| Other civil-engineering works, item 6-6 | KS 24 | 6: forty years, with the specific sports rule below | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1),(14) |
| Buildings outside group 6, item 5-1; civil-engineering works outside groups 4/6 and the separately classified components, item 5-2 | KS 1 or 2, subject to the actual exclusions | 5: twenty years | [Annex 1](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf); §26(1) |

An asset fitting no Annex 1 group goes into group 2 only where no useful life is prescribed elsewhere and §26(6),(7) does not provide a special method. Classify a mixed-use building by its main use measured over total usable floor area; classify each structure in a functional complex separately (§26(2),(13)). A label such as “building” or “hybrid car” is insufficient to choose twenty years or group 0.

**Hotel and sports boundary.** Section 26(14) allows straight-line depreciation over **twenty to forty years** for KS 121 buildings used to provide accommodation under an accommodation contract and associated services, and KS 1265/241 buildings/structures used for sport. It is not a general twenty-year election for residential or administrative buildings. Separately, the period's combined technical improvements and repairs on those qualifying properties, including qualifying rented properties, are a separate asset under §22(6)(f)/(g) when they reach **at least 10% of the building/structure's §25 entry price**. Annex 1 items 2-40/2-41 put that separate expenditure in group 2, six years. Below 10%, repairs follow ordinary accounting/tax treatment and technical improvements increase the building's entry price; the six-year rule does not absorb all refurbishment costs. The use/code test for the building's twenty-to-forty-year period and the 10% expenditure test are distinct ([ITA §§22,26,27,52zzzf](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html); [FS 21/DZPaU/2025/I, both pages](https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2025/2025.06.27_021_DZPaU_2025_I.pdf)).

For a new EUR 800,000 administrative building with a full depreciation year, ordinary depreciation is EUR 20,000; a qualifying hotel choosing twenty years gives EUR 40,000. Qualifying hotel improvements/repairs of exactly EUR 80,000 reach the 10% boundary and form a separate six-year asset; EUR 79,999 does not. The original building's shortened period does not turn that separate asset into a twenty-year asset. Section 26(14) first applies to a period whose return is filed after 31 December 2025. The amended expenditure/Annex 1 rule first applies to technical improvements put into use/business assets and repairs booked/tax-recorded in such a period. It can therefore apply to a 2025 period with a return filed in 2026. Apply a changed group, period or annual rate to an existing register prospectively; do not reopen depreciation already claimed (§52zzzf).

**Interest: apply the two limits in order.** Both concern double-entry/IFRS corporate borrowers and relevant Slovak permanent establishments. First test §17k; §21a is switched off **only if the base was increased under §17k**, not merely because §17k was considered (§21a(4)).

1. **§17k scope and exceptions.** It covers net borrowing costs under contracts concluded after 31 December 2023, including later amendments to older contracts (§52zzr). It is not limited to related-party debt. Paragraph (8) excludes banks/foreign-bank branches; the specified insurers/reinsurers and branches; the financial entities identified in footnote 105b; and a borrower whose dependent persons under §2(n) are **only individuals**. Check that last exception before imposing a corporate-group calculation on an owner-managed business. The footnote identifies the statutory pension, supplementary-pension, financial-intermediation and collective-investment entities; this Guide's financial-sector exclusion remains.
2. **Find net borrowing costs N.** From borrowing expenses that otherwise are tax expenses in the period, subtract taxable interest income/economically equivalent returns, including interest finally taxed by withholding under §17k(5) (§17k(3)–(5)). Include debt interest, bond/bill yields, finance-lease interest, debt-related derivatives, financing foreign-exchange differences, guarantees, contractual financing fees, arm's-length financing amounts and equivalent payments. Capitalised interest is included in the proportion in which it enters tax cost through the asset/technical-improvement cost or residual value (§17k(4)(e)); it is not automatically all deducted or blocked when paid.
3. **Build the statutory denominator.** The sum S in §17k(6) is the §§17–29 ordinary base less foreign-taxed income/bases removed by exemption, **plus** the §17f exit-tax base, §51e special base and bases taxed by final withholding. Remove the v.o.s./k.s. partnership base shares specified in §17k(9),(10). Use the pre-adjustment base defined by §17(38), excluding its listed circular adjustments (§17(19)(h),(l), §17(34),(35),(37), §17k, §19(3)(n), §21(1)(h)); do not use taxable revenue, accounting EBITDA or the base after tax losses. Add N and tax depreciation actually included under §19(3)(a)/§22(12): `tax EBITDA = S + N + D`.
4. **Current-period adjustment and carry.** Only if N **exceeds EUR 3,000,000**, increase the base by the amount by which N exceeds `30% × tax EBITDA` (§17k(2)). Exactly EUR 3,000,000 does not trigger that adjustment. The EUR 3,000,000 test is not a deductible allowance to subtract from the excess and is not an alternative floor for the 30% cap. Track blocked N by origin period. It can be deducted in the next **five immediately following periods**, only to the extent current N plus the older amounts deducted does not exceed that period's §17k(2) calculated capacity (§17k(7)); unused capacity itself is not a carried tax asset. For a positive-capacity case with current N = EUR 3,200,000 and 30% capacity EUR 3,600,000, at most EUR 400,000 of still-live blocked costs can be deducted. A EUR 1,900,000 balance becomes EUR 1,500,000; a 2026 blocked amount expires after the fifth following period, 2031 for consecutive calendar years. Paragraph (7) permits qualifying legal-successor carryover only on its stated anti-avoidance conditions, apportioned by transferred equity where there are several successors; reorganisations remain specialist work.
5. **§21a if no §17k increase.** For a related lender, covered interest and borrowing costs above **25% of accounting profit before tax plus the depreciation and interest expense included in that profit** are disallowed. Exclude loans/loan portions whose interest forms asset acquisition/own cost (§21a(1)); that capitalisation exclusion differs from §17k's later tax-cost inclusion. An apparently independent lender is treated as related for the relevant loan if lending is conditional on a directly connected loan, borrowing or deposit supplied to that lender by a related person: the back-to-back rule (§21a(2)). Banks/foreign-bank branches, the specified insurers/reinsurers/branches, footnote-105b financial entities and leasing companies are excluded borrowers (§21a(3)). The deduction is `min(covered costs, max(0, 25% × accounting EBITDA))`; disallow only the covered costs less that deduction. If accounting EBITDA is zero or negative, disallow the covered costs in full, never more than those costs ([Financial Administration, low-capitalisation FAQ5](https://podpora.financnasprava.sk/663968-Pravidl%C3%A1-n%C3%ADzkej-kapitaliz%C3%A1cie-)). Section 21a provides no five-period carry-forward; do not transfer §17k(7)'s carry to it.

For example, a non-excluded borrower has ordinary pre-adjustment base EUR 2,000,000, exempted foreign base EUR 500,000, exit base EUR 200,000, §51e base EUR 100,000 and final-withholding base EUR 200,000: S = EUR 2,000,000. With N = EUR 4,000,000 and D = EUR 1,000,000, tax EBITDA is EUR 7,000,000, capacity EUR 2,100,000 and §17k add-back EUR 1,900,000. There is no additional §21a adjustment. Separately, where §17k makes no increase, EUR 120,000 debt costs including EUR 20,000 capitalised interest leave EUR 100,000 covered expense; accounting EBITDA EUR 300,000 gives a EUR 75,000 cap and EUR 25,000 §21a disallowance. The same result applies to a qualifying back-to-back loan, even with an independent lender ([ITA §§17(38),17k,21a,52zzr](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html)).

**Tax losses (§ 30).** A tax loss is deducted over at most the five periods right after the loss year. The yearly deduction is capped at 50% of the base, unless the company is a micro-taxpayer in the year it deducts. Then the full base can be absorbed. A micro-taxpayer is a company with taxable revenue up to EUR 60,000 that has no controlled transaction with a related person, is not in bankruptcy, liquidation or a payment plan, and has a full 12-month period (§ 2(w)). Note the two thresholds differ: EUR 60,000 for the loss rule, EUR 100,000 for the 10% rate. Unused loss falls away after the fifth period and on entry into liquidation or bankruptcy.

**Dividends received.** A dividend paid out of a company's profit is not subject to tax in the hands of a Slovak company, to the extent it was not a tax expense of the payer (§ 12(7)(c)). The exception: dividends from a company resident in a non-cooperating state go into a special base taxed at 35% (§ 51e(4) and § 15(b)(2)). The Ministry of Finance publishes a list of cooperating states (states with a tax treaty or an information exchange agreement with Slovakia, less those on the EU list of non-cooperative jurisdictions at 1 January and those with no or a zero corporate tax). A state that is not on that list is a non-cooperating state (§ 2(x)). Use the list valid from 1 January 2026.

**Minimum tax (§ 46b).** A company pays the minimum tax for its revenue band (table above) if its tax after reliefs and foreign tax credit is lower than that figure, or if it has a tax loss. A shorter period is pro-rated by months (§ 46b(6)). It is halved for a company whose staff are at least 20% disabled employees (§ 46b(3)). It does not apply to:
- a company filing for the first time, for the period in which it was set up (unless it is a successor of a company dissolved without liquidation);
- non-profit taxpayers under § 12(3) and (4);
- a company running a sheltered workshop;
- the special periods in liquidation or bankruptcy;
- a land community (pozemkové spoločenstvo) with only its own activities and taxable revenue up to EUR 10,000;
- a company from the period in which it receives notice of proceedings to dissolve it;
- a registered social enterprise (§ 46b(7)).

The excess of minimum tax over the computed tax can be credited against tax in the next three periods. Only the part of that later tax above the minimum tax can absorb it (§ 46b(5)). The credit is lost on dissolution without liquidation, liquidation or bankruptcy (§ 46b(8)).

## Deadlines and filing

- **Return.** The DPPO return is due within three calendar months after the end of the tax period: 31 March 2027 for calendar 2026 (§ 49(2)). Tax is payable by the same date.
- **Extension by notice.** A notice filed with the tax office before the deadline moves it by up to three whole calendar months, to 30 June 2027 for calendar 2026. The new date is the end of the month the company names. If the company has foreign-source income, the move is up to six months, to 30 September 2027 (§ 49(3)(a) and (b)). Tax is due on the new date. Companies in liquidation or bankruptcy apply instead, at least 15 days before the deadline (§ 49(3)(c)).
- **Verified current form.** The [actual Ministry forms package](https://www.mfsr.sk/files/archiv/66/prispevok_16.zip), notice MF/014310/2026-721, supplies **MF/014309/2026-721, DPPOv26 v1.13**, a 21-page sample including the annex templates. It applies where the filing deadline falls **after 31 December 2026**, including a calendar-2026 return due in March 2027. The earlier 15-page MF/012187/2025-721 referenced in the prior Guide belongs to deadlines from 1 January through 31 December 2026; it is retained here as historical form information. Choose by the return's deadline rather than the year in the filename. The matching [2026 instructions, MF/014312/2026-721](https://www.mfsr.sk/files/archiv/36/prispevok_18.zip), identify the same current form.
- **Electronic filing and annexes.** A legal person entered in the commercial register, and any VAT payer, must file electronically (Tax Procedure Code §14(1)(a)). Some supporting documents can be supplied separately, but the current form's five annex categories remain part of the return even if blank: the combined §13a/§13b annex, §30c, §30ca, §30e, and the **part VIII** additional-recipient annex. The earlier part VII recipient-annex reference belonged to the prior form. Count additional projects, recipient sheets and other documents as the instructions require (current form p.16; instructions p.28).
- **Minimum tax** is payable by the return deadline (§ 46b(4)).
- **Advances in 2026 (§ 42).** The tax that sets them (§ 42(6)) is the tax on the base after losses, at the § 15 rate shown in the previous period's return, less reliefs under the Act. It is the computed tax, not the minimum tax. Based on the 2025 tax:
  - above EUR 16,600: monthly, 1/12 of that tax, by the end of each month;
  - above EUR 5,000 up to EUR 16,600: quarterly, 1/4, by the end of each calendar quarter (or quarter of the fiscal year);
  - up to EUR 5,000: none, unless the tax office orders them.
  Until the deadline for the 2025 return, advances follow the last known tax, from the 2024 return (§ 42(7)). A company formed during the year (other than by merger or division) pays no advances in its first period (§ 42(4)). A company filing its first return pays no advances until that return is due, then makes up the advances that fell due by the end of the following month (§ 42(8)).
- **Financial transaction tax.** Separate from CIT, Act No. 279/2024 Coll. taxes financial transactions. Its § 6 rates from 1 January 2026: 0.4%, at most EUR 40 per transaction; 0.8% on cash withdrawals; EUR 2 per payment card. This skill does not cover it beyond this pointer.

**Current DPPO mapping for an ordinary company.** Use the actual form and its instructions together; row numbers are the printed fields, not account numbers.

| Stage | Fields and reconciliation |
|---|---|
| Accounting result and adjustments | Profit/loss before tax 100. Table A's nondeductible-expense total 17 goes to 130; representation is A6 and §21a interest A13. Unpaid §17(19) items go to 140; later payment deductions not already in profit go to 270. Table B accounting-versus-tax depreciation differences go to 150 or 250. Current §17k increases go to 310, not 130. Follow the remaining adjustments to 301,315 and 400; do not add a worked variant again to an already stated base. |
| Taxable revenue and rate | Reconcile booked revenue in Table L 1 through its described adjustments to L99, then 560. Select the 10%/21%/24% rate in 550 from that taxable revenue, not 400 or accounting profit. |
| Losses and deductions | Table D tracks prior-period losses from oldest to newest (a current loss is in 400 and enters Table D in the next period): original amount row 1, current use 2, carry balance 3 and previous use 4. Transfer row 2 column 9 to 410; 500 = 400 − 410. Ordinary loss limits above still apply. Any separately supported deductions 501–503 lead to 510; 600 = 510 × 550 /100. |
| Relief and foreign tax credit | Relief 610 gives 700. Table E computes the §45 foreign-tax credit (with country details in part IX); E10 goes to 710, then 800 = 700 − 710. For an ordinary non-hybrid case, E1 is 400, E2 the foreign net base, E3 its percentage of E1, and E4 the proportion of 700; E8 is the supported foreign tax permitted by the treaty, and E10 the lower of E8 and the E9 cap. It is not an unrestricted credit for every foreign deduction. |
| Minimum tax and earlier credits | Applicable minimum 810; 820/900 apply when it exceeds 800, with the positive difference 830 carried under the statutory rule and entered in Table K only from the next period. Earlier minimum-tax balances are tracked in Table K; available credit is limited by 910 = 800 − 810, K row 5 column 4 goes to 920, and 1000 = 800 − 920. Row 1050 selects the resulting ordinary tax or minimum tax. |
| Advances and final payment | Advances 1010, security 1020 and eligible withholding 1030 total 1040. Row 1080 includes 1050 and any applicable special-base taxes; subtract permitted exit-tax instalment amount 1090 and 1040. The nonnegative balance is 1100, a negative balance 1101; apply the EUR 5 payment exception. Request a refund in part XI. |
| Next-period advances | Row 1110 is 500 × 550 /100 less 610 under the instructions. It is not the cash balance 1100, nor automatically the minimum tax. |

The actual form separates the §51e tax in 1070 and §51ea tax in 1071 from ordinary tax, and carries exit tax through 1060 where applicable. Bank-card-fee taxation remains outside this Guide. The loss register and minimum-tax credit register have different expiry rules; never move a balance between them. Current Table I reporting is explained in [sk-transfer-pricing](sk-transfer-pricing.md). Sources: current DPPO form pp.2–11,16; instructions pp.3–7,10–12,15–16,23,28.

## Penalties and interest

From the Tax Procedure Code, Act No. 563/2009 Coll. (version in force from 1 September 2026):

- **Late return (§ 155(1)(a)).** A fine of EUR 100 to EUR 30,000. If the tax office has sent a notice and the return still does not arrive in the time it sets, up to EUR 60,000 (§ 155(1)(b)). A tax office does not impose a fine within a range for the first breach (§ 155(4)).
- **Tax understated in a return and raised by the tax office (§ 155(1)(f)).** 3 times the ECB main refinancing rate a year on the extra tax, at least 10% a year (§ 155(5)). The rate used is the one on the day the assessment is delivered (§ 155(7)). It runs daily from the day after the filing deadline, at least 1% of the extra tax and at most the extra tax (§ 155(2)). Paying the assessed amount within 15 days of delivery cuts the fine to two thirds (§ 155(17)).
- **Correction by a supplementary return (§ 155(1)(g)).** The ECB rate a year on the increase, at least 3% a year. If the supplementary return follows the start of a tax audit: twice the ECB rate, at least 7% a year (§ 155(1)(h) and (5)).
- **Late payment interest (§ 156(2)).** 4 times the ECB main rate in force on the day the arrears arise, at least 15% a year, daily, for at most four years. It applies to late tax and late advances; on a late advance it runs at most to the return deadline (§ 156(4)).
- **At the observed ECB rate.** The actual ECB/NBS history records 2.15% from 11 June 2025,2.40% from 17 June 2026 and 2.65% from 16 September 2026, observed through 27 October 2026. At 2.65%, 3 times is 7.95%, 2times5.3%, 1time2.65% and 4times10.6%, so the 10%/7%/3%/15% floors apply. Use the actual rate on the statutory assessment-delivery, supplementary-filing or arrears date above; a future filing or payment does not inherit today's rate.

## Cross-border points

- **Withholding on payments abroad (§ 43).** Tax is withheld at 19% on Slovak-source income of a non-resident without a registered permanent establishment, such as royalties, interest and certain services. The rate is 35% where the payee is in a non-cooperating state. A treaty or the EU Interest and Royalties Directive can reduce or remove it. For the detailed rules see [sk-cross-border](sk-cross-border.md).
- **Dividends paid abroad.** A dividend paid by a Slovak company to a company is not subject to tax (§ 12(7)(c)). The exception is a recipient company that is a taxpayer of a non-cooperating state (§ 12(7)(c)(1)). That dividend is withheld under § 43(2) (§ 16(1)(e) point 9) at 35% (§ 43(1)(c)).
- **Exit tax (§ 17f).** Moving assets, the seat or the business abroad creates a special base taxed at 21%.
- **Permanent establishments.** The § 21a and § 17k limits and the rate bands apply to a non-resident's Slovak permanent establishment as they do to a resident company.
- **Pillar Two.** Act No. 507/2023 Coll. on top-up tax applies to Slovak members of a multinational or large domestic group whose ultimate parent's consolidated accounts show annual revenue of at least EUR 750,000,000 in at least two of the four preceding periods (§ 3(1)(a)). Those groups also need a top-up tax computation. Not covered here.

## Worked examples

### Example 1: small s.r.o., 10% rate, minimum tax check

Alfa s.r.o. has a calendar 2026 year. Its taxable revenue is EUR 90,000 and its accounting profit is EUR 20,000. It booked EUR 1,500 of representation costs, which are not tax expenses. It has a 2023 tax loss of EUR 4,000 still unused. It has no related-party transactions.

- Base before losses: EUR 20,000 plus EUR 1,500 is EUR 21,500.
- Revenue of EUR 90,000 is above EUR 60,000, so Alfa is not a micro-taxpayer. The loss deduction is capped at 50% of EUR 21,500, EUR 10,750. The whole EUR 4,000 fits.
- Base after losses: EUR 17,500.
- Revenue is not above EUR 100,000, so the rate is 10%: tax EUR 1,750.
- Minimum tax for revenue above EUR 50,000 up to EUR 250,000 is EUR 960. EUR 1,750 is higher, so Alfa pays EUR 1,750 by 31 March 2027.
- 2026 tax is not above EUR 5,000, so there are no advances in 2027.
- The edge: with revenue of EUR 100,500 instead, the rate on the same base would be 21%, tax EUR 3,675. EUR 500 of extra revenue costs EUR 1,925 of tax.

**Filing Alfa's figures.** Enter 100 = 20,000; Table A 6 and its total 17 = 1,500, carried to 130. With no other adjustments,400 = 21,500. Table D records the 2023 loss and current use 4,000; 410 = 4,000,500/510 = 17,500. Table L 99/560 = 90,000; 550 = 10; 600/700/800 = 1,750; 810 = 960, so 820/900 are zero. With no earlier minimum-tax credit or advances,1050/1080/1100 = 1,750. Row 1110 is 1,750, preserving the no-advance result.

For a separate settlement variant, assume Alfa has EUR 500 of unexpired earlier minimum-tax credit and EUR 1,000 of eligible advances. The credit room 910 is `1,750 − 960 = 790`; Table K and 920 use 500,1000/1050 become 1,250,1040 is 1,000 and 1100 is EUR 250. This separate variant leaves the original annual tax computation intact and does not reduce row 1110 to the cash payment.

Separate asset variants, not changes to Alfa's stated profit: a EUR 4,800 computer first used in July has six months of four-year straight-line depreciation, EUR 600; a EUR 30,000 ordinary car gives EUR 3,750, versus EUR 7,500 for a qualifying certificate-coded BEV/PHEV; EUR 6,000 furniture gives EUR 500. The same check recomputes the full-year administrative-building/hotel and exactly-10% improvements boundaries above. These are independent asset assumptions, not deductions to subtract again from Alfa's already stated base.

```oa-check
name: Alfa s.r.o., revenue EUR 90,000, profit EUR 20,000, loss EUR 4,000 (2026)
inputs:
  revenue: 90000
  profit: 20000
  addbacks: 1500
  loss_bf: 4000
  min_tax_band: 960
  computer_price: 4800
  car_price: 30000
  furniture_price: 6000
  use_months: 6
  building_price: 800000
  qualifying_improvements: 80000
  prior_min_tax_credit_variant: 500
  paid_advances_variant: 1000
steps:
  - base_before_loss: profit + addbacks
  - loss_cap: base_before_loss * 0.50
  - loss_used: min(loss_bf, loss_cap)
  - base_after_loss: base_before_loss - loss_used
  - tax_10: base_after_loss * 0.10
  - tax_payable: max(tax_10, min_tax_band)
  - tax_if_21: base_after_loss * 0.21
  - cliff_cost: tax_if_21 - tax_10
  - computer_first_year: round(computer_price / 4 * use_months / 12, 2)
  - ordinary_car_first_year: round(car_price / 4 * use_months / 12, 2)
  - qualifying_bev_first_year: round(car_price / 2 * use_months / 12, 2)
  - furniture_first_year: round(furniture_price / 6 * use_months / 12, 2)
  - admin_building_full_year: building_price / 40
  - qualifying_hotel_full_year: building_price / 20
  - improvements_boundary: building_price * 0.10
  - improvement_excess_over_boundary: qualifying_improvements - improvements_boundary
  - separate_improvements_full_year: round(qualifying_improvements / 6, 2)
  - min_credit_room_variant: max(0, tax_10 - min_tax_band)
  - min_credit_used_variant: min(prior_min_tax_credit_variant, min_credit_room_variant)
  - tax_after_prior_credit_variant: tax_10 - min_credit_used_variant
  - final_payment_variant: tax_after_prior_credit_variant - paid_advances_variant
expected:
  base_before_loss: 21500.00
  loss_cap: 10750.00
  loss_used: 4000.00
  base_after_loss: 17500.00
  tax_10: 1750.00
  tax_payable: 1750.00
  tax_if_21: 3675.00
  cliff_cost: 1925.00
  computer_first_year: 600.00
  ordinary_car_first_year: 3750.00
  qualifying_bev_first_year: 7500.00
  furniture_first_year: 500.00
  admin_building_full_year: 20000.00
  qualifying_hotel_full_year: 40000.00
  improvements_boundary: 80000.00
  improvement_excess_over_boundary: 0
  separate_improvements_full_year: 13333.33
  min_credit_room_variant: 790
  min_credit_used_variant: 500
  tax_after_prior_credit_variant: 1250
  final_payment_variant: 250
```

### Example 2: large company at 24%, loss cap and advances

Beta a.s. has a calendar 2026 year with taxable revenue of EUR 6,200,000. Its tax base before losses is EUR 300,000. It has EUR 400,000 of tax losses from 2024 and 2025.

- Not a micro-taxpayer, so the loss deduction is capped at 50% of EUR 300,000, EUR 150,000. EUR 250,000 of loss carries forward, within the five-year window.
- Base after losses: EUR 150,000.
- Revenue is above EUR 5,000,000, so the rate is 24%: tax EUR 36,000.
- Minimum tax for revenue above EUR 5,000,000 is EUR 11,520. EUR 36,000 is higher, so it does not bite. Had Beta made a tax loss in 2026, it would still pay EUR 11,520. It could then credit that amount against the part of its 2027 to 2029 tax above the minimum tax.
- The § 42(6) tax for 2026 is EUR 36,000 (base after losses at 24%, no reliefs). It is above EUR 16,600, so once the 2026 return is due (31 March 2027, or the extended date) Beta pays monthly advances of EUR 3,000 (1/12 of EUR 36,000). Until then its 2027 advances follow its 2025 tax (§ 42(7)).

**Filing Beta's figures.** Row 400 is 300,000; Table D and 410 use 150,000 of the supported 2024/2025 losses and retain 250,000 by origin year; 500/510 are 150,000. Table L 99/560 is 6,200,000; 550 is 24; 600/700/800 are 36,000; 810 is 11,520, so 1050/1080 are 36,000. The original scenario supplies no advances-paid figure. In a separate normal settlement variant with 30,000 eligible advances in 1010/1040 and no other credits or special bases,1100 is 6,000. Row 1110 remains 36,000 and the subsequent monthly advance remains 3,000; it is not one twelfth of the 6,000 cash balance.

Independent interest variants in the same check use the non-excluded borrower and separate §21a facts above: statutory sum of bases EUR 2,000,000; tax EBITDA EUR 7,000,000; §17k add-back EUR 1,900,000; next-period carry use EUR 400,000 and remaining balance EUR 1,500,000. Exactly EUR 3,000,000 has zero excess over the activation threshold, and therefore no current §17k increase. Separate covered related/back-to-back debt costs EUR 100,000 against the EUR 75,000 §21a limit give EUR 25,000 disallowance. At zero or negative accounting EBITDA, the same EUR 100,000 covered costs are fully disallowed, without an add-back greater than EUR 100,000. These amounts are not additions to Beta's separately stated EUR 300,000 base.

```oa-check
name: Beta a.s., revenue EUR 6,200,000, base EUR 300,000, losses EUR 400,000 (2026)
inputs:
  base_before_loss: 300000
  loss_bf: 400000
  min_tax_band: 11520
  interest_ordinary_base: 2000000
  exempt_foreign_base: 500000
  exit_base: 200000
  special_51e_base: 100000
  withholding_base: 200000
  net_borrowing_costs: 4000000
  interest_tax_depreciation: 1000000
  carry_next_net_costs: 3200000
  carry_next_capacity: 3600000
  thin_total_debt_costs: 120000
  thin_capitalised_interest: 20000
  thin_accounting_ebitda: 300000
  paid_advances_variant: 30000
steps:
  - loss_cap: base_before_loss * 0.50
  - loss_used: min(loss_bf, loss_cap)
  - loss_cf: loss_bf - loss_used
  - base_after_loss: base_before_loss - loss_used
  - tax_24: base_after_loss * 0.24
  - tax_payable: max(tax_24, min_tax_band)
  - monthly_advance: tax_payable / 12
  - statutory_sum_bases: interest_ordinary_base - exempt_foreign_base + exit_base + special_51e_base + withholding_base
  - tax_ebitda: statutory_sum_bases + net_borrowing_costs + interest_tax_depreciation
  - interest_capacity: tax_ebitda * 0.30
  - interest_addback: max(0, net_borrowing_costs - interest_capacity)
  - threshold_boundary_excess: 3000000 - 3000000
  - carry_room: max(0, carry_next_capacity - carry_next_net_costs)
  - interest_carry_used: min(interest_addback, carry_room)
  - interest_carry_left: interest_addback - interest_carry_used
  - thin_covered_costs: thin_total_debt_costs - thin_capitalised_interest
  - thin_capacity: thin_accounting_ebitda * 0.25
  - thin_allowed: min(thin_covered_costs, max(0, thin_capacity))
  - thin_disallowed: thin_covered_costs - thin_allowed
  - thin_negative_ebitda_disallowed: thin_covered_costs - min(thin_covered_costs, max(0, -100000 * 0.25))
  - thin_zero_ebitda_disallowed: thin_covered_costs - min(thin_covered_costs, max(0, 0 * 0.25))
  - final_payment_variant: tax_payable - paid_advances_variant
expected:
  loss_cap: 150000.00
  loss_used: 150000.00
  loss_cf: 250000.00
  base_after_loss: 150000.00
  tax_24: 36000.00
  tax_payable: 36000.00
  monthly_advance: 3000.00
  statutory_sum_bases: 2000000
  tax_ebitda: 7000000
  interest_capacity: 2100000
  interest_addback: 1900000
  threshold_boundary_excess: 0
  carry_room: 400000
  interest_carry_used: 400000
  interest_carry_left: 1500000
  thin_covered_costs: 100000
  thin_capacity: 75000
  thin_disallowed: 25000
  thin_allowed: 75000
  thin_negative_ebitda_disallowed: 100000
  thin_zero_ebitda_disallowed: 100000
  final_payment_variant: 6000
```

## Ask the client first

1. Taxable revenue for the period. It sets the rate band (EUR 100,000 and EUR 5,000,000), the minimum tax band, and micro-taxpayer status (EUR 60,000).
2. The tax period: calendar or fiscal year, and whether it is the company's first period (no minimum tax, no advances).
3. Any controlled transaction with a related person; loan/ amendment dates, lenders and linked deposits, net borrowing costs, capitalised interest and unexpired §17k balances. Identify whether dependent persons are only individuals and whether borrower exclusions apply.
4. Unused tax losses by year, and any minimum tax paid in 2023 to 2025 still to be credited.
5. Unpaid year-end items in the §17(19) list and input-VAT recovery; new assets with actual CPA/KS codes, commissioning dates, vehicle certificate fuel codes and hotel/sports use or improvements/repair amounts.
6. Foreign income or payments to non-residents, and whether any counterparty is in a non-cooperating state.

## Sources

| Source | URL | Read on |
|---|---|---|
| Financial Administration, low-capitalisation FAQ5: negative accounting EBITDA disallows covered costs in full | https://podpora.financnasprava.sk/663968-Pravidl%C3%A1-n%C3%ADzkej-kapitaliz%C3%A1cie- | 2026-10-27 |
| Act No. 595/2003 Coll. on income tax, 2026: existing provisions plus §§17(38),17k,21a,22(6),26–27,52zzr,52zzzf reread for this update | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-27 |
| Act No. 595/2003 Coll., version in force from 1 December 2025 (2025 minimum tax bands, for comparison) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20251201.html | 2026-10-23 |
| Act No. 595/2003 Coll., 31 December 2026 text: assigned corporate provisions unchanged | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20261231.html | 2026-10-27 |
| Actual 2026 Annex 1: CPA/KS classification, items 0-1,1-13,1-24,2-33,2-40/41,5-1/2,6-1 to6-6 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2003/595/20260101_5740211-2.pdf | 2026-10-27 |
| FS 21/DZPaU/2025/I: Act152/2025 new separate hotel/sports improvements/repair assets and §26(14) building periods | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2025/2025.06.27_021_DZPaU_2025_I.pdf | 2026-10-27 |
| Act No. 261/2025 Coll. on consolidation of public finances (new § 46b(2), § 51eb, § 52zzzj, § 52zzzk) | https://static.slov-lex.sk/static/SK/ZZ/2025/261/20260101.html | 2026-10-23 |
| Act No. 563/2009 Coll. Tax Procedure Code, version in force from 1 September 2026 (§ 14, § 154, § 155, § 156) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Act No. 279/2024 Coll. on financial transaction tax, version in force from 1 January 2026 (§ 6) | https://static.slov-lex.sk/static/SK/ZZ/2024/279/20260101.html | 2026-10-23 |
| Ministry of Finance, list of cooperating states under § 2(x), valid from 1 January 2026 | https://www.mfsr.sk/files/archiv/39/Zoznam-spolupracujucich-statov-podla-2-pism-x-zakona-c-595_2003-Z-z_1.1.2026.pdf | 2026-10-23 |
| Act No. 507/2023 Coll. on top-up tax, version in force from 31 December 2025 (§ 3(1)) | https://static.slov-lex.sk/static/SK/ZZ/2023/507/20251231.html | 2026-10-23 |
| European Central Bank, key interest rates (main refinancing rate 2.65% from 16 September 2026) | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html | 2026-10-23 |
| Financial Administration, legal persons' income tax return | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-prijmov/pravnicke-osoby/danove-priznanie-dan-prijem-po | 2026-10-23 |
| Ministry of Finance, notice MF/014310/2026-721 and actual current form MF/014309/2026-721 (DPPOv26 v1.13), actual package | https://www.mfsr.sk/files/archiv/66/prispevok_16.zip | 2026-10-27 |
| Ministry of Finance, notice MF/014312/2026-721 and matching 2026DPPO instructions, actual package | https://www.mfsr.sk/files/archiv/36/prispevok_18.zip | 2026-10-27 |
| NBS, actual ECB key-rate history supplementing the ECB table above | https://nbs.sk/en/statistics/financial-markets/interest-rates/ecb-key-interest-rates/ | 2026-10-27 |

The current form and matching instructions are verified from the actual Ministry packages above. The [31 December 2026 Income Tax Act text](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20261231.html) was compared with the earlier 2026 text: the corporate provisions used here are unchanged. Its §52zzzm directs the specified new §9/§11 rules to 2027 returns; the fact a2026 return is filed in 2027 does not itself move it to those rules. Future ECB rates still require the actual statutory reference date.

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
