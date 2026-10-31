---
name: north-macedonia-cross-border
description: "Use this skill for North Macedonia international income-tax matters for calendar year 2026. Trigger on tax residence, nonresident income, permanent establishment, treaty relief, foreign tax credit, withholding tax, tax residence certificate, moving abroad, liquidation or foreign salary. It distinguishes individuals from foreign legal persons, domestic source taxation from treaty limits, and income-tax relief from VAT and social insurance. It supplies ordinary withholding and gross-up mechanics, certified relief and refund routes, evidence requirements and filing deadlines. Departure and asset-transfer cases require the specifically identified unresolved exit treatment before final advice. This tier 2 skill, checked against the law, includes two recomputing controls and awaits licensed professional sign-off."
jurisdiction: MK
category: cross-border
tax_year: 2026
tier: 2
trust_label: Built by Michael Cutajar and the OpenAccountants team
last_updated: 2026-10-30
version: 0.2
---

# North Macedonia cross-border tax v0.2

**Tax year: 2026. Checked against the law, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

Individuals: [PIT arts. 5-8][pit] tax residents on worldwide income and nonresidents on local-source income. A permanent home/residence or at least **183 days in any 12-month period** establishes the domestic residence basis. Apply the particular treaty's residence tie-breaker after testing both states; counting days alone does not resolve a permanent-home case.

Companies: [Profit Tax Law arts. 4-6][cit] tax entities established or seated locally on worldwide profits and foreign PEs on local business profits. Distinguish a foreign legal-person gross receipt subject to withholding from profits attributable to its local PE. [Tax Procedure Law art. 2(5)][procedure] gives ratified tax treaties priority over national tax laws. The [UJP treaty register][treaties] records application dates; signature or a treaty's mere presence in an old summary is insufficient.

This skill covers ordinary income-tax coordination, not a universal treaty-rate table. It does not certify migration/deemed-disposal, minimum global top-up tax or a particular treaty's beneficial-ownership/PPT/MLI result.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official provision |
|---|---|---|---|
| Ordinary personal income tax | 10% on relevant category base | 2026 | [PIT arts. 9-11][pit] |
| Ordinary company/PE profit tax | 10% | 2026 | [Profit Tax Law arts. 2, 5][cit] |
| Foreign legal-person withholding | 10% of listed gross receipts, unless properly relieved | 2026 | [Profit Tax Law arts. 20-23][cit] |
| Domestic individual residence presence test | 183 or more days in any 12 months | 2026 | [PIT art. 5][pit] |
| Construction/installation/supervisory PE | More than 6 months; counted from commencement including preparatory activity | 2026 | [Profit Tax Law art. 6(3)][cit] |
| Service/consulting PE | More than 90 continuous days for one/connected project in any 12 months; interruptions up to 7 days do not break continuity | 2026 | [Profit Tax Law art. 6(4)-(6)][cit] |
| Foreign corporate profit-tax credit | Foreign tax paid, capped at local 10% tax on foreign profit | 2026 | [Profit Tax Law art. 37][cit] |
| Foreign personal-tax credit | Foreign tax paid, capped at domestic tax on that income | 2026 | [PIT art. 8(4)][pit] |
| Treaty relief decision / individual residence certificate | UJP statutory 30-day decision/issue period | 2026 | [Profit Tax Law art. 23(5)][cit]; [PIT arts. 8(3), 82(4), 89-a(4)][pit] |
| Late-payment interest | 0.03% daily | 2026 | [Tax Procedure Law art. 123][procedure] |

PE thresholds above are domestic-law tests. Read the actual applicable treaty before asserting that a PE exists or is exempt; do not substitute the domestic threshold for a treaty threshold.

## The base

**Foreign legal-person payments:** [Profit Tax Law art. 21][cit] lists dividends; covered resident/local-PE interest and royalties; local entertainment/sports; management, consulting, financial and R&D services paid by a resident or borne by a local PE; insurance/reinsurance of local risks; international telecommunications; and local real-estate rent. The payment can be made abroad and still fall within art. 21. Do not impose WHT on all services indiscriminately.

Art. 21(2) expressly excludes remittance of already taxed local PE profit, interest on specified government/central-bank instruments, bank-deposit interest and specified government-security intermediation/consulting income. Document the particular exclusion. Ordinary final WHT equals listed gross receipt × 10%; gross means the amount before withholding (art. 22). A contract promising a net amount needs algebraic gross-up: `gross = net / (1 - applicable_rate)` and `withholding = gross - net`, where the payer bears the tax. Treaty-reduced rates cannot be used without the relief conditions.

**Individuals:** use the relevant PIT category base, not the corporate gross-payment rule. Employment, services, dividends, rent and gains have different deductions in arts. 16, 21, 40, 50, 53, 57 and 60. Nonresident salary from a resident employer uses the express art. 16(1)(7) salary rule. Treaty relief at source follows arts. 81-83; nonresident self-assessed income uses arts. 89 and 89-a. Sale/exchange gains use actual proceeds/acquisition evidence and the specific exemptions; a bank transfer of capital is not automatically taxable income. For securities/fund units, apply the **1 January 2023 acquisition boundary, including predecessor dates, and chronological FIFO** under Gazette 274/2022 transitional arts. 21-22. Use the income-tax skill's distinct domestic art. 85-a/91-a/93(4) annual reporting/assessment route; foreign receipts outside that route still require testing under arts. 87-88.

**Foreign credit:** compute the North Macedonia tax attributable to the foreign income/profit on its domestic-law base, compare with evidenced foreign income/profit tax paid, and allow no more than that domestic limit. Preserve the source income, allocation, exchange rate and foreign-authority proof. A foreign tax above the ceiling is not a local refund; no carryforward of unused credit is asserted. Avoid crediting a refundable foreign withholding amount as finally borne without checking its status (PIT art. 8; Profit Tax Law art. 37).

**PE attribution and registration:** art. 6 covers fixed business locations and dependent agents as well as the duration tests. Contract-concluding authority, local stock/delivery, preparation/auxiliary exceptions and genuinely independent agency require separate factual analysis. Group control alone does not create a PE (art. 6(11)); absence of a registered branch does not establish absence of a PE. Register at commencement and attribute the local business income/expenses into the ordinary company computation.

**Departure, asset transfers and liquidation:** preserve residence evidence, asset tax cost/location, valuation, ownership and transaction dates. Separate these ordinary events:

- An individual's residence test remains [PIT art. 5][pit]; once nonresident, art. 7 still taxes local-source income. Actual sales/exchanges use arts. 58-63 and the category's filing route. Do not treat a change of address as proof of treaty residence or of a realised disposal.
- A company incorporated locally still meets the domestic incorporation limb of [Profit Tax Law art. 4(2)][cit] when management moves abroad; a treaty residence question is separate. Calculate actual business profit under arts. 7-9 and related-party transfers under arts. 12-15.
- [Arts. 25-27][cit] preserve the specified conversion/status-change continuity at unchanged carrying values and tax the specified revaluation/capital increases where continuity fails. Liquidation continues the last tax period through closing before residue distribution. A registered merger/division/takeover needs accounts/return through the change date and the continuing entity's opening balance.
- Before transferring an investment asset, test five-year relief recapture separately: [Profit Tax Law art. 28(3)-(4)][cit] and [PIT art. 28(3)-(4)][pit]. The corporate and individual reliefs are different computations.

These ordinary transaction rules are confirmed in the cited law. A separate migration/deemed-disposal charge and its specific procedure remain unconfirmed below; no universal nil exit charge is asserted.

## Deadlines and filing

**Individual residence evidence:** apply to the competent UJP office using **B/PDR** under [Residence Rulebook arts. 2-3][residence]. Domestic applicants attach identity/passport copy and fee proof; foreign applicants also supply passport, residence permit, address registration and supporting residence evidence. UJP can certify a foreign authority's treaty form on request. Do not invent the administrative fee amount.

**Corporate relief before payment:** [Profit Tax Law art. 23][cit] requires the prescribed foreign-tax-authority/UJP-certified form or UJP exemption approval. [Profit Rulebook art. 12][profit-rules] identifies **ZD-O/DI** dividends, **ZD-O/KA** interest, **ZD-O/AP** royalties, **ZD-O/DP** other income, and **ZD-DO** exemption with residence certificate. Obtain the foreign certification, submit the required copies and supporting papers through the domestic payer to the competent UJP regional office before payment. Repeated same-basis payments have the rulebook's first-payment submission route. Retain the endorsed form/decision; absent it, withhold domestic tax. Payer is liable for the shortfall if relief conditions fail.

**Corporate refunds:** the foreign recipient applies to the competent UJP regional office with certified **ZD-V/DI, ZD-V/KA, ZD-V/AP or ZD-V/DP**, as appropriate (Profit Rulebook art. 12). Supply receipt/tax-paid and residence/treaty evidence and the designated refund account. UJP refunds excess withholding in domestic currency. Do not state a universal treaty refund claim period without reading that treaty and the applicable limitation rule. UJP issues tax-paid confirmation on nonresident request (Profit Tax Law art. 23(4)).

**Individual relief/refund:** [Individual Treaty Rulebook arts. 2-6][treaty-pit] uses **B-IDD** for exemption and the category-specific **B-IDD/VD** form named in art. 3, certified by the foreign authority and UJP before payment. The rulebook's art. 4 also prints the older suffix **/VP**; obtain the current UJP category form rather than treating the inconsistent suffix as a different substantive relief. Articles 7-8 identify refund forms **B-VD/VD** by income type and **B-VD/KD** for capital gains. Retain foreign residence, payment and withholding evidence; no automatic relief just because a treaty exists.

**Payments and reports:** corporate WHT is remitted **at payment** (art. 20). Domestic legal persons, registered individual businesses and local PEs are the specified remitters. File the annual **DD-I by 15 February 2027** for 2026 (art. 24; Profit Rulebook art. 12). Individual payer calculations are electronic before each covered payment, with remittance at payment (PIT arts. 84-85, 92). Nonresident self-assessed receipts follow art. 89 and certified relief under art. 89-a.

**Residents' foreign receipts:** generally e-PDD calculation/evidence by the **10th of next month**, payment by the **15th** (PIT arts. 88, 93). Foreign salary/pension with foreign tax paid instead has the express calculation/evidence deadline **31 March 2027** for 2026 income (art. 88(2)). Convert individual foreign income at National Bank middle rate on the income date (art. 93(2)). Annual individual return is provided by **30 April**, confirmed/corrected by **31 May**, balance paid by **30 June** next year (arts. 96-100). Company/PE DB and final payments follow the corporate skill; foreign tax evidence does not extend those deadlines. Update registrations after a real move or cessation and retain final-period filings and relief records.

## Penalties and interest

[Profit Tax Law art. 45][cit] covers failure to withhold at payment and file the required report: corporate micro **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, in MKD equivalent; responsible-person ranges respectively **EUR 50-250**, **100-500**, **150-500**, **200-500**. Registered individual business remitters **EUR 100-250**, ordinary physical remitters **EUR 50-250** apply to the listed offences. [PIT arts. 107-108][pit] separately cover individual calculations and payers. Failure of treaty paperwork leaves the payer liable for domestic tax shortfall (Profit Tax Law art. 23(3); PIT art. 83). Interest under [Tax Procedure Law art. 123][procedure] is 0.03% daily from day after maturity.

## Cross-border points

For each treaty case, save the actual operative treaty/protocol and application dates from the official register. Identify the income article, residence, PE/business-profit interaction, beneficial owner and anti-abuse conditions. A maximum treaty rate never creates a domestic charge where domestic law exempts the receipt. Check the particular mutual-agreement/corresponding-adjustment provisions for double-tax disputes; no universal MAP deadline is asserted.

VAT foreign-person registration and imported-service reverse charge remain separate (`north-macedonia-vat`). Social cover follows the specific insurance agreement/status (`north-macedonia-social-contributions`), not a tax-treaty residence conclusion. Related-party pricing and withholding require separate tests even on the same payment. Minimum global top-up taxation is outside this ordinary income-tax skill.

## Two worked examples that recompute

**Simple: foreign corporate royalty, net contract without treaty relief.** A listed royalty is promised at 90,000 net. No domestic exception or certified treaty relief applies. Under arts. 20-22 gross is 100,000, WHT 10,000 and recipient cash 90,000. The payer remits 10,000 at payment; payer-borne WHT also needs its corporate deductibility adjustment under art. 9(1)(13).

```oa-check
name: MK 2026 nonresident royalty gross up
inputs:
  promised_net: 90000
  rate: 0.10
steps:
  - gross: promised_net / (1 - rate)
  - withholding: gross * rate
  - recipient_cash: gross - withholding
expected:
  gross: 100000
  withholding: 10000
  recipient_cash: 90000
```

**Edge: foreign corporate tax above the credit ceiling.** A resident's foreign profit is 100,000 on the domestic tax base, with foreign profit tax 18,000 evidenced by the foreign authority. Art. 37 limits credit to 10,000, so local residual tax on that profit is zero and 8,000 is above the allowable local credit. This does not establish an unused-credit carryforward or foreign refund right.

```oa-check
name: MK 2026 foreign profit credit cap
inputs:
  foreign_profit: 100000
  foreign_tax: 18000
steps:
  - local_tax: foreign_profit * 0.10
  - credit: min(foreign_tax, local_tax)
  - residual: max(0, local_tax - credit)
  - excess_foreign: foreign_tax - credit
expected:
  local_tax: 10000
  credit: 10000
  residual: 0
  excess_foreign: 8000
```

## Ask the client first

- Which states claim residence, and what permanent homes, presence dates and official certificates exist?
- What is the recipient's legal form, income category, gross/net contract and actual beneficial ownership?
- Is there a local fixed place, agent, project or PE bearing the payment, and for how long?
- Which operative treaty, certified relief, foreign tax receipts and refund rights apply?
- Is a move, asset transfer, revaluation, status change or liquidation involved, with asset costs/values documented?

## Sources

| Official source | URL | Read on |
|---|---|---|
| Profit Tax Law, consolidated through Gazette 199/2023 | https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Personal Income Tax Law, consolidated through Gazette 274/2022 | https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Profit Tax implementing rulebook, consolidated through Gazette 6/2020 | https://www.ujp.gov.mk/files/attachment/0000/0990/______________________________________________________________________________________________________________________________________________.pdf | 2026-10-24 |
| Individual treaty-relief Rulebook, Gazette 271/2019 | https://www.ujp.gov.mk/files/attachment/0000/1219/_____________________________________________________________________________271-19.pdf | 2026-10-24 |
| Individual residence certificate Rulebook, Gazette 89/2019 | https://www.ujp.gov.mk/files/attachment/0000/1165/_______________________________________________________________________________________________________________89-2019.pdf | 2026-10-24 |
| UJP, treaty register and application dates | https://www.ujp.gov.mk/mk/regulativa/pregled/tr/md | 2026-10-24 |

[cit]: https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf
[pit]: https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf
[profit-rules]: https://www.ujp.gov.mk/files/attachment/0000/0990/______________________________________________________________________________________________________________________________________________.pdf
[treaty-pit]: https://www.ujp.gov.mk/files/attachment/0000/1219/_____________________________________________________________________________271-19.pdf
[residence]: https://www.ujp.gov.mk/files/attachment/0000/1165/_______________________________________________________________________________________________________________89-2019.pdf
[treaties]: https://www.ujp.gov.mk/mk/regulativa/pregled/tr/md

Not yet confirmed: Standalone migration/deemed-disposal or exit-tax rules and their filing/payment procedure. The retrieved PIT, profit-tax and procedural texts establish ordinary realisation/liquidation rules but do not verify a nil exit charge; departure cases remain incomplete.

