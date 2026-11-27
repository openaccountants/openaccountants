---
name: de-non-resident-tax
description: "Germany, tax year 2026: non-residents with German income; residence and limited liability; the § 1(3) application and § 1a spouse route; § 49 source tests; assessment versus final withholding; § 50a deductions and treaty relief; residents' foreign tax credits under §§ 32d(5) and 34c. Trigger on beschränkte Steuerpflicht, Abzugsteuer, non-resident Germany, foreign dividends and Anrechnung ausländischer Steuer. Use de-rental-income for rental computation, de-payroll for payroll, de-corporate-tax for companies, leaving-germany-exit-tax for departure and germany-to-switzerland-cross-border-tax for Swiss commuters. The explicit holds below supply no filing outcome."
version: 0.6
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Germany: non-resident income and foreign tax credits, 2026

First establish residence, the German source of each income item, the applicable treaty and whether withholding settles the tax. This Guide covers both non-residents with German income and German residents claiming foreign tax credit. Its examples retain their original 2026 inputs.

## Who this applies to

- **Residence:** domestic residence or habitual abode establishes unlimited income-tax liability (§ 1(1) EStG). A residence is a dwelling held in circumstances showing it will be retained and used (§ 8 AO); merely counting days does not decide this. Habitual abode means more than temporary presence. A continuous stay exceeding six months counts from its start, ignoring short interruptions; the automatic six-month rule excludes exclusively private visits, holidays, cures or similar stays lasting no more than one year (§ 9 AO).
- **Limited liability:** absent domestic residence/abode, German-source income under § 49 is taxable, subject to § 1(2), § 1(3) and § 1a (§ 1(4)). German public-service cases abroad and their household members: no eligibility conclusion is supplied here. Check this point with one of our partner accountants.
- **§ 1(3) application:** a non-resident individual with § 49 income can apply for full-liability treatment of that income if at least **90%** of calendar-year income is subject to German income tax, or income outside German income tax does not exceed the **EUR 12,348** 2026 basic allowance, reduced where appropriate for residence-state conditions. German income treaty-taxable only at a limited rate counts as outside German tax for this test. Exclude foreign-untaxed income to the extent comparable German income would be exempt (§ 1(3) sentences 1–4). Obtain the foreign tax authority's certificate of income outside German tax; § 50a withholding still applies (sentences 5–6). These are income amounts under German tax rules, not gross receipts.
- **Country reduction:** do not use the former asserted group fractions or Austria/group-1 classification to establish eligibility; this Guide does not establish the applicable country list. Check this point with one of our partner accountants. The 90% alternative remains available without relying on that amount test.
- **Spouses:** for EU/EEA nationals fully liable under § 1(1) or treated so under § 1(3), a spouse without German residence/abode, resident in another EU/EEA state and not permanently separated, may apply for full-liability treatment for § 26(1). For the § 1(3) test use both spouses' income and twice the basic allowance, **EUR 24,696** for 2026; still test the country reduction. Joint assessment and splitting require the remaining § 26 conditions and election (§ 1a(1) no. 2). Do not infer that every non-EU/EEA national is barred under every special provision or treaty; other spouse/public-service/Swiss routes are held. Check this point with one of our partner accountants.
- **Companies:** no German seat or management gives limited corporate liability on German income (§ 2 no. 1 KStG). The 2026 corporate rate is **15% of taxable income** (§ 23), before any other applicable taxes. Withholding finality under § 32(1) no. 2 excludes income arising in a domestic commercial or agricultural/forestry business; § 32(2) also supplies mixed-year, qualifying application and other exceptions. Use **de-corporate-tax** for the computation; no corporate final-liability conclusion is supplied here. Check this point with one of our partner accountants.

## Rates, bands and thresholds

| Item | 2026 rule | Official source |
|---|---|---|
| § 1(3) application | 90% alternative or EUR 12,348 amount test, subject to conditions above | https://www.gesetze-im-internet.de/estg/__1.html; https://www.gesetze-im-internet.de/estg/__32a.html |
| § 1a couple amount test | EUR 24,696, derived as twice EUR 12,348; conditions above | https://www.gesetze-im-internet.de/estg/__1a.html; https://www.gesetze-im-internet.de/estg/__32a.html |
| Tariff used in rental example | For rounded taxable income EUR 17,800–69,878: (173.10 × z + 2,397) × z + 1,034.87; z is one ten-thousandth of rounded income above EUR 17,799; round tax down to whole euros | https://www.gesetze-im-internet.de/estg/__32a.html |
| § 50a gross withholding | 15%; supervisory monitoring fees under subsection (1) no. 4: 30%; travel rule below | https://www.gesetze-im-internet.de/estg/__50a.html |
| § 50a small performance | No withholding for subsection (1) no. 1 only, if receipts per performance do not exceed EUR 250 | https://www.gesetze-im-internet.de/estg/__50a.html |
| § 50a net withholding | 30% individual / 15% eligible entity; only subsection (1) nos. 1, 2 and 4 and the eligibility/evidence gates below | https://www.gesetze-im-internet.de/estg/__50a.html |
| Ordinary dividend withholding | 25% plus solidarity surcharge of 5.5% of withheld tax: derived total 26.375%, before relief and excluding church tax | https://www.gesetze-im-internet.de/estg/__43a.html; https://www.gesetze-im-internet.de/solzg_1995/__3.html; https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| § 50c small-royalty exception | Cumulative same-payer payments no more than EUR 10,000 in the calendar year, only where a treaty excludes German tax | https://www.gesetze-im-internet.de/estg/__50c.html |

## The taxable base

### 1. German-source income: domestic law first, treaty second

This is a screening matrix, not a replacement for all of § 49. A German payer alone does not establish every source category.

| Income | Domestic source test / exception | Official source |
|---|---|---|
| Business | German permanent establishment or permanent representative under no. 2(a) | https://www.gesetze-im-internet.de/estg/__49.html |
| Self-employed work | Performed or exploited in Germany, now or previously, or a German fixed facility/PE under no. 3 | https://www.gesetze-im-internet.de/estg/__49.html |
| Performances | Domestic performance or exploitation under no. 2(d), with employment/self-employment priority; § 50a distinguishes performance from exploitation | https://www.gesetze-im-internet.de/estg/__49.html; https://www.gesetze-im-internet.de/estg/__50a.html |
| Employment | Domestic exercise or exploitation under no. 4(a); German-managed company's managing director, Prokurist or board remuneration under no. 4(c). Public-purse pay, treaty-assigned foreign work, severance, aviation and release-from-work branches require their own conditions; no outcome supplied. Check this point with one of our partner accountants. | https://www.gesetze-im-internet.de/estg/__49.html |
| Dividends | § 20(1) no. 1 income where the debtor has German residence, management or seat, subject to no. 5(a)'s further branches | https://www.gesetze-im-internet.de/estg/__49.html |
| Rent | German-situated immovable property; other property/rights must meet no. 6's domestic location, registration or exploitation test and its category priority | https://www.gesetze-im-internet.de/estg/__49.html |
| Shares | No. 2(e) requires § 17 conditions, and a German seat/management, its restructuring branch, or its property-company branch. For the latter, more than 50% of share value must derive directly/indirectly from German immovable property at some time in the preceding 365 days, with the shares attributable to the seller then. Determine the proportion using active business assets at the book values then applicable. Restructuring and the full § 17/treaty computation are held. Check this point with one of our partner accountants. | https://www.gesetze-im-internet.de/estg/__49.html |
| Registered rights | In both no. 2(f) and no. 6, where registration is the sole domestic link for other rights, exclude income if the relevant transaction is between non-related parties under § 1(2) AStG **or** the applicable treaty, including its statutory application rules, opposes taxation. This does not remove an actual domestic location/exploitation link or exempt German land | https://www.gesetze-im-internet.de/estg/__49.html |
| German land sale | Private property: no. 8 and § 23's period of **no more than ten years**, including its own-home exemption; business/comparable foreign corporate property follows no. 2(f), without that private holding-period exemption. No gain computation supplied; use **de-capital-gains** and **de-rental-income** | https://www.gesetze-im-internet.de/estg/__49.html; https://www.gesetze-im-internet.de/estg/__23.html |
| Pensions | No. 7 includes specified German statutory/professional/insurance/other payers and certain foreign-payer benefits backed by previously deducted contributions; no. 10 separately covers § 22 no. 5 benefits. No blanket exemption for foreign payers or pension computation supplied. Check this point with one of our partner accountants. | https://www.gesetze-im-internet.de/estg/__49.html |

**Property-company separators, preserved:** German real-estate active book assets **EUR 40**, other active book assets **EUR 60** give 40%, failing the strict majority even if property market value is **EUR 90**. Book assets **EUR 60 / EUR 40** give 60%, passing only this percentage gate; the dated attribution, § 17 and treaty tests still apply.

**Interest:** do not use the former blanket exemption for German bank accounts/listed bonds. No. 5(c) contains secured-claim, ship, bond and participation-right distinctions, and no. 5(d) separate coupon/security-payment rules; a business connection can change classification. For anything beyond an ordinary unsecured private bank deposit with no other German source link, no source/tax conclusion is supplied. Check this point with one of our partner accountants.

### 2. Assessment versus final withholding

For individuals remaining under limited liability, wage tax, capital withholding and § 50a generally settle the income tax (§ 50(2) sentence 1). Before using that result test every sentence-2 exception:

- domestic business income (no. 1); retrospectively failed § 1(2), § 1(3) or § 1a status (no. 2); and a mixed-liability year under § 2(7) sentence 3 (no. 3);
- employment under § 49(1) no. 4: § 39a(4) allowance plus annual wages above basic allowance + employee allowance + special-expense allowance (4(a)); application under § 46(2) no. 8 (4(b)); § 46(2) nos. 2, 5, 5a (4(c)); application associated with § 34(1)/(2) nos. 2, 4 extraordinary income (4(d)); or § 50d(7) sentence-2 credit application (4(e));
- § 50a(1) nos. 1, 2, 4 on application (no. 5; BZSt assessment), and the specified no. 5(a) capital income within § 20(1) no. 6 sentence 2 on application (no. 6; debtor's income-tax office, first payer if several).

Only **4(b) and 5** have sentence 7's EU/EEA nationality **and** EU/EEA residence gate. Sentence 8 extends **4(b)** to the specified EU/EEA nationals resident in Switzerland and Swiss nationals resident in the EU or Switzerland. It does not impose those nationality/residence gates on 4(d), 4(e) or 6. Employment cases use the competent Betriebsstättenfinanzamt under sentences 3–6. This list establishes routes, not special-tariff, insurance or foreign-credit amounts. For those computations: Check this point with one of our partner accountants. Income not settled by withholding follows assessment; an actual § 1(3)/§ 1a qualifying person follows that route instead.

### 3. Limited-liability assessment

Deduct business expenses/Werbungskosten only to the extent economically connected with German income (§ 50(1) sentence 1). The personal deductions and reliefs listed in sentence 4, including § 10c, child allowances, extraordinary burdens and § 35a/§ 35c, are excluded; ordinary spouse splitting is unavailable. The professional-pension exception under § 50(1a) has mandatory-admission, nationality/residence, direct-connection, allocation and foreign-deduction limits; no entitlement or amount supplied here. Check this point with one of our partner accountants.

For § 49(1) no. 4 employment, § 50(1) sentence 5 permits the specified § 10(1) no. 2(a)/no. 3 and § 10(3), plus § 10c, only for the German-employment period and up to that employment income. Annual/monthly § 9a no. 1 and § 10c lump sums reduce proportionately for partial periods (sentence 6). Use **de-employee-income-tax** for qualifying deductions; no unrestricted pension/health deduction is implied.

For the tariff, increase taxable income by the **EUR 12,348** basic allowance. For employment under no. 4, add only the positive excess of that allowance over the employment income less sentence-5 deductions (§ 50(1) sentence 2). Special progression/AStG rate cases follow sentence 3; no amount is supplied here. Check this point with one of our partner accountants.

**Solidarity surcharge:** establish the § 3 SolzG assessment base, including the statutory child-allowance recalculation where applicable. Excluding the separate § 32d(3)/(4) component, the ordinary threshold is **EUR 20,350**, or **EUR 40,700** for § 32a(5)/(6) cases. Above it use the smaller of **5.5%** of that base and **11.9%** of its excess over the threshold, dropping fractions of a cent (§ 4). A stipulated ordinary single base of **EUR 20,400** gives min(1,122; 5.95) = **EUR 5.95**. § 32d(3)/(4) tax and capital/§ 50a withholding have their separate **5.5%** treatment without this ordinary threshold/cap.

### 4. § 1(3), employment administration and mixed years

With § 1(3), assess German income with the applicable resident deductions rather than the limited-liability add-back. The § 10c allowance is **EUR 36** absent higher qualifying expenses. Foreign income within § 32b(1) no. 5 changes the rate, not the German taxable base; calculate under subsection (2). The no. 3 foreign-rent exception does not extend to no. 5. Foreign capital income and its interaction with § 2(5b), treaty or extraordinary-income exceptions and the final progression-rounding method are held; no eligibility or filing amount is supplied for those branches. Check this point with one of our partner accountants.

Remaining limited-liability employees generally use class I under § 38b(1) no. 1(b), subject to multiple-employment class VI; use **de-payroll** for payroll. The Betriebsstättenfinanzamt forms/changes the relevant non-resident/§ 1(3) wage data (§ 39(2)); apply there for an initial identification number (§ 39(3)), rather than treating it as the body that allocates every number. § 46(2) no. 7(b) requires assessment where wage data was formed for the specified § 1(3)/§ 1a population; no. 9 covers an assessment application combined with a § 1(3) application, with employer-office jurisdiction.

For a mixed residence year, § 2(7) brings German income of the limited-liability period into the full-liability assessment; § 32b(1) no. 2 governs relevant foreign income of that year. No unconditional progression amount is supplied. Check this point with one of our partner accountants. Departure with shares, extended limited liability and Swiss commuter cases remain routed to **leaving-germany-exit-tax** and **germany-to-switzerland-cross-border-tax**.

### 5. § 50a withholding and § 50c relief

§ 50a(1) covers domestic performances (excluding employment already under the specified wage withholding), domestic exploitation, specified rights/know-how and professional-sports engagement rights, and supervisory monitoring fees. The payer withholds when the creditor receives payment. Gross rates are in the table. Reimbursed/assumed travel and accommodation enter receipts only above actual cost; meal payments only above the statutory travel allowances (§ 50a(2)). Solidarity surcharge is 5.5% of the withholding tax.

The net route applies only to § 50a(1) nos. 1, 2 and 4: directly connected expenses must be proved in a form BZSt can verify or borne by the payer. Individuals must be EU/EEA nationals resident in the EU/EEA (30% net tax). Entities must meet § 32(4) KStG's EU/EEA legal-formation, society, seat and management conditions (15% net tax). Royalties under no. 3 cannot use this route (§ 50a(3)). The EUR 250 performance exception does not cover royalties, supervisory fees or exploitation under no. 2.

A tax office may order withholding to secure tax on otherwise non-withheld income: normally **25% gross**, **15%** for entities, adjustable to expected tax. File/pay to that office on its ordered timetable; § 50(2) finality does not apply (§ 50a(7)).

Ordinary § 50a returns/payment go to BZSt by the **10th of the month after each quarter**, with § 108(3) weekend/holiday adjustment. Returns remain required under the specified small-performance, second-stage and § 50c exemptions. The payer is liable for withholding/remittance; the creditor may be pursued for defective withholding. Give the statutory tax certificate on request (§ 50a(5)). Second-stage withholding relief itself is held. Check this point with one of our partner accountants.

A treaty or §§ 43b/50g entitlement does not alone stop withholding (§ 50c(1)). A BZSt exemption certificate permits relief to its extent; it is limited to at most five years, starts no earlier than receipt of the application, and remains conditional. For treaty capital-withholding certificates the creditor must be a corporation subject to residence-state income/profit tax without exemption, directly holding at least **10%** of the nominal capital of the specified fully taxable German corporation (§ 50c(2)). The small-royalty exception uses cumulative same-payer receipts including the present payment up to **EUR 10,000**, and requires that a treaty bars German tax. Filing remains required; do not simply omit withholding for a royalty treaty that merely reduces the rate.

Refunds under § 50c(3) require a timely BZSt application and tax that was withheld/remitted or paid under the stated liability/recovery notices, and cannot be credited under § 36(2) no. 2. The four-year period starts at the end of the receipt year and ends no earlier than one year after tax payment or the treaty deadline. Supply the capital certificate/data or § 50a certificate as applicable; transmit through the official interface with residence confirmation from the foreign tax authority. A hardship waiver permits the prescribed paper form (§ 50c(5)). No processing-time promise is supplied.

**Entity anti-abuse:** § 50d(3) denies treaty relief to the stated extent where **both** owner/beneficiary direct-entitlement and source-to-economic-activity tests fail. Mere receipt/pass-through or inadequately equipped operations do not establish economic activity. Denial does not apply to the extent the entity proves no main interposition purpose was obtaining a tax advantage, or its main share class is substantially and regularly traded on a recognised exchange; § 42 AO remains applicable. Neither exception creates a relief entitlement by itself.

**Dividend relief:** normal withholding is the table's 26.375% before relief. § 44a(9) provides a **two-fifths** refund of capital withholding actually withheld/remitted for the specified § 2 no. 1 KStG corporate creditor, subject to § 50c(3)/(5) and § 50d(3), leaving further statutory/treaty rights intact. The former example comparing **26.375%** with a hypothetical **15%** treaty rate has a mathematical difference of **11.375 percentage points**, but supplies **no usable refund claim or surcharge outcome** without the treaty's tax coverage and entitlement. Country rates and directive relief: use **de-treaty-withholding-rates**; Check this point with one of our partner accountants.

### 6. Foreign tax credits for German residents

For qualifying private capital income under § 32d(1), § 32d(5), not § 34c, governs the credit: assessed and paid foreign tax, reduced by any foreign refund entitlement; at most **25% of each taxable foreign income item**, and subject to subsection (5) sentence 3's German-tax ceiling; in the simple all-foreign-income example below that ceiling is EUR 2,250. Treaty credits, including deemed-paid tax, follow subsection (5) sentence 2. Without church tax, income tax is **(e − 4q) / 4**, with e the § 20 income and q the eligible credit. Income not subjected to German capital withholding must be declared under § 32d(3); a foreign broker alone does not prove that fact. Business capital, substantial interests, elections and other § 32d(2)/§ 20(8) exclusions need **de-capital-gains**, not automatic flat taxation.

Under a successful § 32d(6) Günstigerprüfung, the § 32d(5) credit is capped at the **additional tariff tax** on capital income. The election covers all capital income for that year, both spouses' income on joint assessment, and must lower income tax including surcharge taxes.

For other eligible foreign income, first establish the source under § 34d and the treaty. Without a treaty, § 34c(1) requires a tax corresponding to German income tax, assessed/paid in the source state and reduced by refund rights. Its cap is the applicable average German rate on the whole taxable income, applied to the eligible foreign income from that state. Exclude capital income within § 32d(1)/(3)–(6) and income not taxed there; use German-law net income. A treaty credit follows § 34c(6)'s conditions and treaty limits. On application, § 34c(2) permits deduction instead of credit for tax on non-exempt foreign income. Do not describe every uncredited excess as irretrievably lost without testing deduction and the treaty.

Preserved cap illustration: taxable income **EUR 60,000**, including **EUR 10,000** eligible foreign rent, and relevant German tariff tax **T** gives **T × 10,000 / 60,000 = T/6**, only after those eligibility conditions. Treaty-exempt income is not automatically creditable; progression under § 32b(1) no. 3 has subsection (1) sentence-2 exceptions, including qualifying non-third-country immovable rent and specified PE profits. Specific treaty exemptions, switch-over, proof-of-foreign-tax and EU/EEA/third-country outcomes are held. Check this point with one of our partner accountants.

## Deadlines and filing

An assessed taxpayer files under § 25, subject to withholding finality and application routes above. Ordinary mandatory **2026 calendar-year** returns are due **2 August 2027** (31 July is Saturday); qualifying adviser-prepared returns **29 February 2028**. Earlier demands, extensions and local holidays can change the result (§§ 149, 108 AO). These dates do not decide voluntary applications or § 50c refunds. Electronic filing under § 25(4) covers income under § 2(1) nos. 1–3 unless a § 46(2) nos. 2–8 case applies; hardship relief is available on application.

Without a domestic residence-office basis, § 19(2) AO generally uses German assets/the most valuable part, then where activity is mainly exercised/exploited; the departure-year no-German-income rule and the special employment/BZSt routes above take priority where applicable. For non-residents assessable **only** on § 49(1) nos. 7/10 income, Finanzamt Neubrandenburg is competent, also for the corresponding § 1(3) application (§ 1 EStZustV). Do not infer that every person receiving any German pension files there.

## Penalties and interest

- **Annual late filing (§ 152 AO):** generally discretionary before the automatic trigger, with an excusable-delay rule. The ordinary trigger is non-filing within **14 months** after year-end or by a qualifying earlier demand; extensions and zero/negative-tax or prepayment/withholding-covered assessments exclude the automatic rule, not every discretionary surcharge. For an ordinary annual return the amount is **0.25%** of assessed tax less prepayments/creditable withholding per started month, at least **EUR 25**, rounded down to whole euros, maximum **EUR 25,000**. A first demand received after the deadline, where the person could assume no return was required, changes the counted months (§ 152(5)). Agricultural/special-period returns and withholding-return penalties are held. Check this point with one of our partner accountants.
- **Assessment interest (§§ 233a, 238):** ordinary 2026 annual-tax balances run from **1 April 2028**, 15 months after year-end, until the assessment takes effect; **0.15% per full month / 1.8% annually**, with the interest base rounded down to a multiple of **EUR 50**. The difference base uses creditable withholding and prepayments determined before interest starts; refund interest is limited by the refund and payment date. This is not the rule for withholding/advance assessments; agriculture, retrospective events and loss carrybacks have special starts and are held. Check this point with one of our partner accountants.
- **Late payment (§ 240 AO):** **1% per started month** on assessed/declared overdue tax rounded down to a multiple of **EUR 50**, excluding ancillary tax charges. The three-day grace excludes § 224(2) no. 1 payment methods. No grace assumption for other payment facts is supplied.

## Cross-border points

Apply the actual treaty before finalising source taxation, relief or credit; this Guide supplies no generic **183-day** exemption. VAT from German property/performances, church tax under state law, departure/extended limited liability, special professional pensions and foreign investment income in § 1(3) are explicit non-usable holds or routes above. Check this point with one of our partner accountants.

## Worked examples

### Example 1: Austrian rental case, 2026

Anna lives in Vienna, with no German home/abode, **EUR 24,000** German flat rental result and **EUR 2,000** Vienna garage rental result, computed under German rules. Assume ordinary full-year private rental, no other income, no higher qualifying personal expenses and no treaty removal of German rental taxation. Invented facts; use **de-rental-income** for the rental result.

Under limited liability, the EUR 36 allowance is unavailable. Add back EUR 12,348: tariff base **EUR 36,348**, z = 1.8549; unrounded formula **EUR 6,076.642509131**, tax **EUR 6,076**, no ordinary solidarity surcharge on that base.

The income share **24,000 / 26,000 = 92.3077%** passes the 90% gate without relying on Austria's country-group classification; obtain the foreign-income certificate. For § 1(3), illustrative taxable income is **24,000 − 36 = EUR 23,964**. Foreign rent enters no. 5 progression: **EUR 25,964** gives tariff tax **EUR 3,107**. The original unrounded-rate arithmetic gives **11.9665691%**, whole-euro illustrative result **EUR 2,867**, difference **EUR 3,209**. These last option-tax/saving figures are **not a usable assessment or election recommendation**: the final progression-rounding method is held. Check this point with one of our partner accountants.

The original alternative **additional Austrian salary EUR 40,000** makes total income EUR 66,000, German share 36.3636% and outside income EUR 42,000, failing both eligibility alternatives even before any reduction. No exact alternative tax calculation is supplied.

```oa-check
name: DE non-resident landlord 2026; option arithmetic only, final rounding held
inputs:
  rent_result: 24000
  foreign_rent: 2000
  grundfreibetrag: 12348
  additional_salary: 40000
steps:
  - base_limited: rent_result + grundfreibetrag
  - z1: (base_limited - 17799) / 10000
  - tax_limited: floor((173.10 * z1 + 2397) * z1 + 1034.87)
  - german_share: rent_result / (rent_result + foreign_rent)
  - taxable_opt: rent_result - 36
  - prog_base: taxable_opt + foreign_rent
  - z2: (prog_base - 17799) / 10000
  - tax_prog_base: floor((173.10 * z2 + 2397) * z2 + 1034.87)
  - rate: tax_prog_base / prog_base
  - illustrative_option: floor(taxable_opt * rate)
  - illustrative_difference: tax_limited - illustrative_option
  - alternative_total: rent_result + foreign_rent + additional_salary
  - alternative_share: rent_result / alternative_total
  - alternative_outside: foreign_rent + additional_salary
expected:
  base_limited: 36348
  tax_limited: 6076
  german_share: 0.923077
  tax_prog_base: 3107
  illustrative_option: 2867
  illustrative_difference: 3209
  alternative_total: 66000
  alternative_share: 0.363636
  alternative_outside: 42000
tolerance: 0.00001
```

### Example 2: foreign dividends, 2026

Jan lives in Munich, receives **EUR 10,000** foreign dividends through a foreign broker, has no other capital income and no church membership. Stipulate ordinary § 32d(1) private dividends, no German withholding, no loss offsets, full unused **EUR 1,000** § 20(9) allowance, and eligible final source tax of **15% / EUR 1,500**, with no refund entitlement; the hypothetical treaty rate is an input, not a country-rate claim.

Income e = EUR 9,000; German tax before credit EUR 2,250. The original per-item ceiling is 25% of the EUR 10,000 dividend, **EUR 2,500**. The binding remaining German tax ceiling after the allowance is **EUR 2,250**; the allowance does not change the foreign payment itself (BMF investment-income guidance, paragraphs 120, 122 and 201–202). Eligible q = EUR 1,500; (9,000 − 4 × 1,500)/4 = **EUR 750**, surcharge **EUR 41.25**, total **EUR 791.25**; the ordinary surcharge threshold does not shield § 32d(3) tax.

If **30% / EUR 3,000** was withheld but the stipulated treaty limits it to 15%, deduct the **EUR 1,500** refund right first, leaving **EUR 1,500** eligible credit. In the distinct original no-refund-entitlement variant, stipulated eligible foreign tax **EUR 3,000** meets the **EUR 2,250** German ceiling, leaving **EUR 750** uncredited under § 32d(5). No foreign refund procedure or alternative tariff liability is supplied.

```oa-check
name: DE foreign dividends 2026; credit and refund-entitlement variants
inputs:
  dividends: 10000
  foreign_rate: 0.15
  sparer_pauschbetrag: 1000
  alternative_rate: 0.30
steps:
  - foreign_tax: dividends * foreign_rate
  - e: dividends - sparer_pauschbetrag
  - german_tax_before: e * 0.25
  - item_cap: dividends * 0.25
  - q: min(foreign_tax, item_cap, german_tax_before)
  - flat_tax: (e - 4 * q) / 4
  - soli: flat_tax * 0.055
  - total: flat_tax + soli
  - alternative_withheld: dividends * alternative_rate
  - treaty_refund: alternative_withheld - foreign_tax
  - eligible_after_refund: alternative_withheld - treaty_refund
  - no_refund_credit: min(alternative_withheld, item_cap, german_tax_before)
  - no_refund_uncredited: alternative_withheld - no_refund_credit
expected:
  foreign_tax: 1500
  german_tax_before: 2250
  item_cap: 2500
  q: 1500
  flat_tax: 750
  soli: 41.25
  total: 791.25
  alternative_withheld: 3000
  treaty_refund: 1500
  eligible_after_refund: 1500
  no_refund_credit: 2250
  no_refund_uncredited: 750
```

## Ask the client first

Obtain German and foreign homes/stay dates; nationality and spouse residence/separation status; each country's income computed under German rules; German work, property and payer details; withholding certificates; foreign assessments, payments and refund rights; and the applicable treaty/residence certificate. For shares obtain seller attribution and dated active-asset book values; for registered rights obtain related-party and actual exploitation facts; for entity relief obtain owners, activity, business premises and rebuttal/listing evidence. Establish any mixed residence year or failed earlier full-liability status before using withholding finality.

## Sources

| Operative source | URL | Read / applicability checked |
|---|---|---|
| ESTG § 1 | https://www.gesetze-im-internet.de/estg/__1.html | 2026-11-27 |
| ESTG § 1a | https://www.gesetze-im-internet.de/estg/__1a.html | 2026-11-27 |
| AO_1977 § 8 | https://www.gesetze-im-internet.de/ao_1977/__8.html | 2026-11-27 |
| AO_1977 § 9 | https://www.gesetze-im-internet.de/ao_1977/__9.html | 2026-11-27 |
| KSTG_1977 § 2 | https://www.gesetze-im-internet.de/kstg_1977/__2.html | 2026-11-27 |
| KSTG_1977 § 23 | https://www.gesetze-im-internet.de/kstg_1977/__23.html | 2026-11-27 |
| KSTG_1977 § 32 | https://www.gesetze-im-internet.de/kstg_1977/__32.html | 2026-11-27 |
| ESTG § 32a | https://www.gesetze-im-internet.de/estg/__32a.html | 2026-11-27 |
| ESTG § 49 | https://www.gesetze-im-internet.de/estg/__49.html | 2026-11-27 |
| ESTG § 23 | https://www.gesetze-im-internet.de/estg/__23.html | 2026-11-27 |
| ESTG § 50 | https://www.gesetze-im-internet.de/estg/__50.html | 2026-11-27 |
| ESTG § 10c | https://www.gesetze-im-internet.de/estg/__10c.html | 2026-11-27 |
| ESTG § 32b | https://www.gesetze-im-internet.de/estg/__32b.html | 2026-11-27 |
| ESTG § 2 | https://www.gesetze-im-internet.de/estg/__2.html | 2026-11-27 |
| ESTG § 38b | https://www.gesetze-im-internet.de/estg/__38b.html | 2026-11-27 |
| ESTG § 39 | https://www.gesetze-im-internet.de/estg/__39.html | 2026-11-27 |
| ESTG § 46 | https://www.gesetze-im-internet.de/estg/__46.html | 2026-11-27 |
| ESTG § 50a | https://www.gesetze-im-internet.de/estg/__50a.html | 2026-11-27 |
| ESTG § 50c | https://www.gesetze-im-internet.de/estg/__50c.html | 2026-11-27 |
| ESTG § 50d | https://www.gesetze-im-internet.de/estg/__50d.html | 2026-11-27 |
| ESTG § 44a | https://www.gesetze-im-internet.de/estg/__44a.html | 2026-11-27 |
| ESTG § 43a | https://www.gesetze-im-internet.de/estg/__43a.html | 2026-11-27 |
| SOLZG_1995 § 3 | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-11-27 |
| SOLZG_1995 § 4 | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-11-27 |
| ESTG § 32d | https://www.gesetze-im-internet.de/estg/__32d.html | 2026-11-27 |
| ESTG § 34c | https://www.gesetze-im-internet.de/estg/__34c.html | 2026-11-27 |
| ESTG § 34d | https://www.gesetze-im-internet.de/estg/__34d.html | 2026-11-27 |
| ESTG § 25 | https://www.gesetze-im-internet.de/estg/__25.html | 2026-11-27 |
| AO_1977 § 19 | https://www.gesetze-im-internet.de/ao_1977/__19.html | 2026-11-27 |
| ESTZUSTV § 1 | https://www.gesetze-im-internet.de/estzustv/__1.html | 2026-11-27 |
| AO_1977 § 149 | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-11-27 |
| AO_1977 § 108 | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-11-27 |
| AO_1977 § 152 | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-11-27 |
| AO_1977 § 233a | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-11-27 |
| AO_1977 § 238 | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-11-27 |
| AO_1977 § 240 | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-11-27 |
| ESTG § 20 | https://www.gesetze-im-internet.de/estg/__20.html | 2026-11-27 |
| ESTG § 52 | https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-27 |
| BMF investment-income guidance, allowance/credit interaction paragraphs 120, 122, 201–202; checked against current §§ 20/32d | https://esth.bundesfinanzministerium.de/esth/2025/B-Anhaenge/Anhang-19/II/inhalt.html | 2026-11-27 |
| EStG § 26, spouse assessment conditions and election; reused DEE-04 proof | https://www.gesetze-im-internet.de/estg/__26.html | 2026-11-26; applicability 2026-11-27 |

Not yet confirmed: no unconfirmed outcome is supplied as usable. The explicit non-usable holds and partner-accountant referrals above identify every unresolved branch.
