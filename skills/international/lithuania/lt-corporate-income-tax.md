---
name: lt-corporate-income-tax
description: "Use this skill for Lithuanian corporate income tax (pelno mokestis) in tax year 2026. It covers the 17% standard rate, the 0% and 7% rates for entities with income up to EUR 300,000 and the related-entity test that removes them, the taxable profit computation, non-deductible items, representation costs, tax depreciation and immediate write-off, losses carried forward with the 70% cap, the 30% EBITDA interest limit with its EUR 3,000,000 floor, the 4:1 controlled debt rule for interest paid to controlling lenders, passenger car cost caps, the investment project relief, advance payments, the annual return due by the 15th day of the 6th month, fines and late payment interest. Trigger on: Lithuanian corporate tax, pelno mokestis, UAB profit tax, 7% small company rate Lithuania, investicinis projektas, avansinis pelno mokestis. Out of scope: withholding and non-residents (lt-cross-border), transfer pricing (lt-transfer-pricing), payroll (lt-payroll-social), VAT (lithuania-vat-return), personal income tax (lithuania-pit)."
jurisdiction: LT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Lithuania: corporate income tax (2026) v0.1

This skill sets out how a Lithuanian company computes, files and pays corporate income tax (pelno mokestis) for tax year 2026. The law is the Law on Corporate Income Tax No. IX-675 (Pelno mokesčio įstatymas, PMĮ), in its consolidated version in force from 19 May 2026 to 31 December 2026. Procedure, fines and interest come from the Law on Tax Administration No. IX-2112 (Mokesčių administravimo įstatymas, MAĮ). The tax authority is the State Tax Inspectorate (VMI).

Two related topics have their own skills. Withholding on payments to foreign entities, inbound dividends, foreign branches and the exit tax are in lt-cross-border. The arm's length rule, documentation and FR0528 are in lt-transfer-pricing.

## Who this applies to

- **Lithuanian entities (Lietuvos vienetai).** A Lithuanian entity is taxed on its worldwide income, from Lithuanian and foreign sources (PMĮ art. 4(1)). This covers companies (UAB, AB), individual enterprises (IĮ) and the other Lithuanian entities the PMĮ taxes.
- **Foreign branches of Lithuanian entities.** Profit of a branch (permanent establishment) in an EEA or treaty state is left out of the Lithuanian base if it is taxed there by a profit tax or an equivalent tax (art. 4(1)). See lt-cross-border.
- **Foreign entities.** A foreign entity is taxed on the profit of its Lithuanian permanent establishment and, by withholding, on some Lithuanian-source income (art. 5(1)(2), 11(2) and (3)). See lt-cross-border.
- **Tax period.** The calendar year, unless VMI approves another 12-month period on request (art. 6(1) and (2)). The first period starts on registration (art. 6(3)).
- **Named here only.** Shipping companies on the fixed profit tax (art. 38-2), the additional tax on credit institutions (art. 38-3), and the patent box computation (art. 5(7) to (10)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate on taxable profit of a Lithuanian entity or PE (art. 5(1)(1)) | 17% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Small entity, income up to EUR 300,000: first and second tax periods, owners only individuals (art. 5(2)) | 0% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Small entity, income up to EUR 300,000: other tax periods (art. 5(2)) | 7% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Related-entity test that removes the 0% and 7% rates: combined income of the linked entities above (art. 5(3)) | EUR 300,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Agricultural cooperatives, more than 50% of income from farming (art. 5(6)) | 7% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Patent box: profit from own-developed copyrighted software or patented invention (art. 5(7)) | 7% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Losses brought forward: cap as a share of the year's taxable profit before losses; no cap for entities taxed at 7% under art. 5(2) (art. 30(4)) | 70% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Losses on securities and derivatives (non-financial entities): carry-forward period (art. 30(5)) | 5 tax periods | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Net interest cap (art. 30-1(2)) | 30% of tax EBITDA | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Net interest always deductible up to (art. 30-1(3)) | EUR 3,000,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Controlled debt: remunerated debt from controlling lenders above this ratio to fixed capital; interest on the excess is not deductible (PMĮ art. 40(3), Government Resolution No. 1575, VMI commentary) | 4:1 | 2026 | https://www.vmi.lt/evmi/pelno-mokestis |
| Passenger car: deductible part of the cost, by CO2 emissions: 0 g/km; up to 130 g/km; 131 to 200 g/km; above 200 g/km (art. 30-2(1), cars acquired or leased from 1 January 2025) | EUR 75,000; 50,000; 25,000; 10,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Representation costs: share deductible, and cap on the deductible amount as a share of income (art. 22(3)) | 50%; 2% of income | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Residual value for tax depreciation, at most (art. 18(2)) | 10% of cost | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Small entity free to set its own depreciation periods (not buildings): average staff up to 10 and income up to (art. 18(3)) | EUR 150,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Investment project relief: reduction of taxable profit, at most (art. 46-1(2)) | 100% | costs of 2009 to 2028 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Investment project relief: cap on qualifying lorry, trailer and semi-trailer costs per period (art. 46-1(1)) | EUR 300,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| No advance payments if the previous period's taxable income (apmokestinamosios pajamos) did not exceed (art. 47(5)) | EUR 300,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Advance payments on the estimate method must reach at least (art. 47(2)(2)) | 80% of the final tax | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr |
| Fine on tax understated, found in a tax audit (MAĮ art. 139(1)) | 20% to 100% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr |
| Late payment interest (delspinigiai), from 1 August 2026 | 0.027% a day | 2026 | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- |

The 2025 standard rate was 16%. The 17% rate in art. 5(1)(1) applies to 2026 profit.

## The taxable base

**The computation (PMĮ art. 11(1)).** Start from income. Take off non-taxable income (art. 12). Deduct allowable deductions and limited deductions (ribojamų dydžių leidžiami atskaitymai, such as depreciation and representation costs). The result is taxable profit. A cost is deductible only if it is backed by a document with the details accounting law requires (art. 11(4)). A structure set up mainly to get a tax advantage, without real commercial reasons, is ignored (art. 11(8)).

**Small entity rates (art. 5(2) and (3)).**
- An entity whose income for the tax period is not more than EUR 300,000 pays 0% in its first and second tax periods and 7% after that. Income here means all income, including non-taxable income under art. 12 and the income of foreign branches left out of the base, but not dividends received. The limit is tested for each period separately, including a first period shorter than 12 months (VMI commentary on art. 5(2)).
- The 0% rate applies only if all owners are individuals, and only if during three tax periods in a row, counting the first two, the entity's activity is not suspended, it is not liquidated or reorganised, and its shares are not transferred to new owners.
- **When a 0% condition is broken** within those three periods, the entity recomputes the profit of its first and second periods at the small entity rate (7% for periods starting in 2026 or later, 6% for 2025, 5% before), files corrected annual returns for them, and pays late payment interest on the tax paid late under the MAĮ (VMI commentary on art. 5(2)).
- Neither rate applies where linked entities together have income above EUR 300,000 for the period. Linked means: an IĮ whose owner or family members also own other IĮs; an owner and family members holding more than 50% of other entities on the last day of the period; or the same owner, or the same owners together, holding more than 50% in each entity on that day.
- Art. 5(2) has no headcount test. The 10-employee test is in art. 18(3), for depreciation only.

**Non-deductible items (art. 31(1)).** The main ones:
- corporate income tax itself, and VAT paid to the budget (point 1);
- contractual penalties, and fines, late payment interest and other sanctions paid to the state for breaking Lithuanian law (point 3);
- interest or other payments for a related person's failure to perform a contract (point 4);
- the part of a limited deduction above its limit (point 5);
- costs deducted more than 18 months ago but still unpaid to an entity in a target territory (point 8);
- support (donations) other than under art. 28, and gifts other than gifts to employees (point 9);
- payments to entities in target territories unless the payer proves they relate to ordinary activity, the recipient has the assets for it, and the deal has economic substance, and payments on which tax was not withheld under art. 37 (point 10, art. 31(2));
- compensation for damage the entity caused (point 11);
- dividends and other profit distributions (point 12);
- costs not connected with earning income or unusual for the entity's activity (point 13);
- corrections of prior-period errors booked under accounting rules (point 14);
- revaluation losses on assets and liabilities, other than hedging derivatives (point 15);
- costs attributable to non-taxable income (point 17);
- costs of a crime, including bribes (point 20);
- the solidarity contribution under Regulation (EU) 2022/1854 (point 21).
Art. 31(3) to (6) deny deductions in hybrid mismatch cases.

**Representation costs (art. 22(3)).** Only 50% is deductible, and the deductible amount cannot exceed 2% of the entity's income for the period. Costs incurred through shareholders are not representation costs unless they are employees, and gambling costs never are (art. 22(4) and (5)).

**Passenger cars (art. 30-2).** For a car acquired or leased from 1 January 2025, the cost that can be depreciated under art. 18 is capped by its CO2 emissions: EUR 75,000 at 0 g/km, EUR 50,000 up to 130 g/km, EUR 25,000 from 131 to 200 g/km, and EUR 10,000 above 200 g/km. Monthly rent for a car not on the balance sheet is deductible up to the same cap times the annex 1 depreciation rate for the group, divided by 12. The rent cap does not apply to rentals of 30 days or less in the period or to rentals through a platform (art. 30-2(1) to (3)).

**Tax depreciation (art. 18 and annex 1).**
- Fixed assets and goodwill are depreciated over a period the entity chooses, not shorter than the minimum in annex 1. Residual value is at most 10% of cost (art. 18(2)).
- Methods: straight-line, double declining balance, or units of production, as annex 1 allows for each group. The chosen method is kept consistently (art. 18(4)).
- Minimum periods in annex 1 include: new buildings used in business 8 years; residential buildings 20; other buildings 15; machinery and equipment 5; computers and communications equipment 3; software 3; acquired rights 3; other intangibles 4; cars up to 5 years old 6 (4 for rental, driving schools and transport); other cars 10; lorries, trailers and buses 4; furniture 6; other tangible assets 4; goodwill 15. Shorter periods (often 2 years) apply to assets used in R&D.
- Start: an asset bought and put into use by the last day of the 6th month of the tax period is depreciated from that period; after that, from the next period (art. 18(8)). An entity may instead choose to start every asset from the first day of the month after it is put into use, straight-line (art. 18(11)).
- Small entities with average staff up to 10 and income up to EUR 150,000, not caught by the art. 5(3) related-entity test, may set their own periods for all groups except buildings (art. 18(3)).
- **Immediate write-off (art. 18(13)).** The full cost of machinery and equipment, structures, computers and communications equipment, software, acquired rights, and lorries, trailers and semi-trailers (from the annex 1 group for those not older than 5 years) can be deducted in the period the asset is first used. If the asset is used for less than 3 years (exceptions include the end of the entity, a legal requirement, force majeure, crime by third parties and an art. 41 reorganisation where the acquirer completes the 3 years), past tax is recomputed on the annex 1 periods. It cannot be used for an asset whose cost already reduces profit under the investment project relief.

**Losses (art. 30).**
- Ordinary tax losses carry forward without time limit, oldest first (art. 30(3) and (4)). The carry-forward stops if the entity stops the activity that caused the loss, unless for reasons outside its control.
- Losses brought forward can reduce a year's taxable profit by at most 70% of that profit, computed after non-taxable income and deductions but before the losses. The 70% cap does not apply to entities taxed at 7% under art. 5(2) (art. 30(4)).
- Losses on securities and derivatives (non-financial entities) only offset income of the same kind, and carry forward for 5 tax periods (art. 30(2) and (5)). Losses on selling shares in an EEA or treaty company held at more than 10% for at least 2 years (3 years for shares received in an art. 41(2) reorganisation) are neither deductible nor carried forward, unless the shares are sold back to the issuer (art. 30(2)).
- **From 2027 (Law XV-488 of 16 October 2025).** Art. 12(15) (the exemption for gains on such shares) and art. 30(2) are rewritten so that "share" also covers a part in an EEA or treaty limited-liability entity whose capital is made of parts. The law enters into force on 1 January 2027 and applies to 2027 and later tax periods, so it does not change 2026.
- Art. 30 provides only a carry-forward, no carry-back. Loss transfers between group companies are in art. 56-1 and are not covered here.

**Interest limitation (art. 30-1).**
- Interest costs are deductible up to the entity's interest income (art. 30-1(1)).
- Net interest (interest costs above interest income) is deductible up to the higher of 30% of tax EBITDA (art. 30-1(2)) and EUR 3,000,000 (art. 30-1(3)). Tax EBITDA is taxable profit before depreciation and amortisation, the R&D extra deduction, the film relief, support deducted, losses brought forward and net interest.
- "Interest" is wide: profit-participating loans, convertible and zero-coupon bonds, finance lease charges, capitalised interest, guarantee fees on financing, related admin fees and currency differences (art. 30-1(6)).
- In a group, the cap and the EUR 3,000,000 apply jointly to all Lithuanian group entities and PEs (except financial and insurance companies), shared pro rata (art. 30-1(4)). An equity escape applies if the entity's equity-to-assets ratio is no more than 2 percentage points below the group's consolidated ratio (art. 30-1(5)).
- Disallowed net interest carries forward without time limit (art. 30-1(9)).
- The rule does not apply to financial and insurance companies, qualifying EU public infrastructure loans, or **entities that have no related persons** (art. 30-1(7)).

**Interest paid to controlling lenders: the 4:1 rule.** PMĮ art. 40(3) requires income and payments to be recharacterised in the cases the Government sets. Its rules (Government Resolution No. 1575 of 9 December 2003) contain a debt-to-equity test, and VMI applies it alongside art. 30-1 (VMI commentary on art. 30-1 and art. 40(3), updated by VMI letter R-2183 of 7 August 2026):
- A controlling lender is a person that, on the last day of the period, holds directly or indirectly more than 50% of the Lithuanian entity, or more than 50% together with related persons while holding at least 10% itself. It also covers other group members and the controlling individual's spouse, partner and first-degree relatives who lend to the entity.
- Remunerated debt from controlling lenders above 4 times fixed capital is controlled debt. Fixed capital is equity on the last day of the period, without that year's result and without revaluation of assets transferred by the controlling lender. The ratio is tested on the last day of each period.
- Interest on the controlled debt is not deductible. Interest on debt up to 4:1 is deductible only within the art. 30-1 limit. Interest paid abroad is still subject to withholding (lt-cross-border).
- The rule does not apply if the entity proves the same loan on the same terms would be made between independent persons, or to financial institutions that provide leasing.
- A repayment just before the year end that is borrowed again just after it is disregarded where it is a tax avoidance arrangement.

The rate and terms of any related-party loan must also be at arm's length under art. 40; that test and its documentation are in lt-transfer-pricing. Interest or penalties paid for a related person's breach of contract are never deductible (art. 31(1)(4)).

**Investment project relief (art. 46-1).**
- An entity carrying out an investment project can reduce taxable profit by the costs actually incurred in the period on qualifying assets: machinery and equipment, structures, computers and communications equipment, software, acquired rights, and lorries, trailers and semi-trailers (the last group capped at EUR 300,000 of costs per period). The assets must be unused and made no more than 2 years before first use (art. 46-1(1)).
- The reduction can take taxable profit down by up to 100%. Unused costs carry forward for the next 4 tax periods (art. 46-1(2)).
- Costs are reduced by state, EU or other public support used for them (art. 46-1(3)).
- Only costs incurred in the 2009 to 2028 tax periods qualify (art. 46-1(4)).
- The asset must be used in the business for at least 3 years, or the tax saved is paid back by recomputing past periods (art. 46-1(5)).

**Exempt income.** Non-taxable income is listed in art. 12 and is not covered line by line here. Inbound dividends and gains on qualifying shareholdings are in lt-cross-border.

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Annual corporate income tax return (metinė pelno mokesčio deklaracija) for 2026, calendar-year entity | 15 June 2027 (15th day of the 6th month after the period) | PMĮ art. 51(2) |
| Payment of the 2026 balance | 15 June 2027 | PMĮ art. 53(1) |
| Return for the last period when the entity ends | within 30 days of the end of activity | PMĮ art. 51(2) |
| Advance tax return, prior-year method: months 1 to 6 | 15 March (15th day of the 3rd month) | PMĮ art. 51(3)(1) |
| Advance tax return, prior-year method: months 7 to 12 | 15 September (15th day of the 9th month) | PMĮ art. 51(3)(1) |
| Advance tax return, estimate method | 15 March (15th day of the 3rd month) | PMĮ art. 51(3)(2) |
| Advance tax payments | 15th day of the last month of each quarter (15 March, 15 June, 15 September, 15 December) | PMĮ art. 47(6) |

- **Advance payments (art. 47).** The company chooses one of two methods. Prior-year method: each payment for the first two quarters is one quarter of the tax of the year before last; each payment for the last two quarters is one quarter of last year's tax. Estimate method: each quarter is one quarter of the expected tax for the year, and the total must be at least 80% of the final tax.
- **Who does not pay advances.** Entities in their first tax year (art. 47(4)). Entities whose taxable income (apmokestinamosios pajamos) in the previous tax period did not exceed EUR 300,000 (art. 47(5)). In the second year, a company on the prior-year method starts with the 7th month (art. 47(4)).
- The annual balance is the tax for the year less the advances paid (art. 53(1)).
- Related-party transactions are reported on FR0528 with the annual return. See lt-transfer-pricing.

## Penalties and interest

- **Late payment interest (delspinigiai).** Charged on tax not paid by its due date, and on tax found in an audit from the day after the original due date (MAĮ art. 96). The rate is set by the Minister of Finance from the 12-month government securities yield plus 7 points (MAĮ art. 99). From 1 August 2026 it is **0.027% a day** (VMI answer KM2633).
- **Advance payments too low.** If the estimate in the advance return is below 80% of the final tax, late payment interest is charged on the unpaid advance for each quarter (PMĮ art. 47(2)(2)).
- **Fine on tax understated.** Tax found understated in a tax audit carries a fine of **20% to 100%** of the shortfall (MAĮ art. 139(1)). VMI starts from the midpoint and adjusts for mitigating and aggravating circumstances (MAĮ art. 140). A repeat breach of the same tax law within 5 years doubles the fine (art. 139(3)).
- **Voluntary correction.** No fine if the company files a corrected return before VMI orders an audit of it (MAĮ art. 139(4)).
- **Time limit.** Tax can normally be assessed for the current year and the 3 previous calendar years (MAĮ art. 68(1)); 5 years for transfer pricing adjustments (art. 68(4)(4)).
- **Relief.** VMI can waive fines and interest in the cases in MAĮ art. 141.
- **Recomputed past tax.** Breaking the 0% conditions in art. 5(2) means the first two periods are taxed again at the small entity rate, with late payment interest (see the taxable base). Disposing of an asset within 3 years after immediate write-off (art. 18(13)) or after investment project relief (art. 46-1(5)), means past tax is recomputed.

## Cross-border points

Covered in lt-cross-border; only the links are listed here.
- Withholding on dividends, interest, royalties and other payments to foreign entities (PMĮ art. 5(1)(2), 34, 37).
- Exempt profits of foreign branches in EEA or treaty states (art. 4(1)) and the foreign tax credit (art. 55).
- Inbound dividends (art. 35), and losses on qualifying share sales (art. 30(2)).
- Exit tax on transfers of assets abroad (art. 40-2).
- Controlled foreign company income (art. 39).
- Transfer pricing and FR0528: lt-transfer-pricing.

## Worked examples

### Example 1: a UAB on the 17% rate with losses brought forward

A UAB had income of EUR 2,000,000 in 2026 and an accounting profit before tax of EUR 250,000. Charged in the books are EUR 40,000 of corporate income tax expense, a EUR 3,000 fine from a state inspectorate, and EUR 10,000 of representation costs. Tax losses brought forward from earlier years are EUR 300,000. It paid EUR 12,000 of advances for 2026. Its income is above EUR 300,000, so the 17% rate applies.

1. Add back the tax expense (art. 31(1)(1)): EUR 40,000.
2. Add back the fine (art. 31(1)(3)): EUR 3,000.
3. Representation: 50% is deductible, EUR 5,000, which is below 2% of income (EUR 40,000). Add back the other 50%: EUR 5,000 (art. 22(3)).
4. Taxable profit before losses: 250,000 + 40,000 + 3,000 + 5,000 = EUR 298,000.
5. Loss cap: 70% of EUR 298,000 = EUR 208,600 (art. 30(4)). The losses (EUR 300,000) are higher, so EUR 208,600 is used.
6. Taxable profit: EUR 89,400. Tax at 17%: EUR 15,198.
7. Less advances of EUR 12,000: EUR 3,198 to pay by 15 June 2027 (art. 53(1)).
8. Losses carried forward to 2027: 300,000 minus 208,600 = EUR 91,400.

```oa-check
name: UAB at 17% with the 70% loss cap (2026)
inputs:
  income: 2000000
  accounting_profit: 250000
  cit_expense: 40000
  fine: 3000
  representation: 10000
  losses_bf: 300000
  advances: 12000
steps:
  - repr_deductible: min(representation * 50 / 100, income * 2 / 100)
  - repr_addback: representation - repr_deductible
  - profit_before_losses: accounting_profit + cit_expense + fine + repr_addback
  - loss_cap: profit_before_losses * 70 / 100
  - losses_used: min(losses_bf, loss_cap)
  - taxable_profit: profit_before_losses - losses_used
  - tax: taxable_profit * 17 / 100
  - balance_due: tax - advances
  - losses_cf: losses_bf - losses_used
expected:
  repr_addback: 5000
  profit_before_losses: 298000
  loss_cap: 208600
  losses_used: 208600
  taxable_profit: 89400
  tax: 15198
  balance_due: 3198
  losses_cf: 91400
```

### Example 2: a small UAB that loses the 7% rate through its owner's other company

An individual owns 100% of UAB A, now in its fourth tax period. UAB A had income of EUR 280,000 in 2026 and taxable profit of EUR 60,000. On its own it would pay 7% (art. 5(2)). The same individual also owns 60% of UAB B, whose 2026 income was EUR 90,000.

1. UAB A's own income, EUR 280,000, is not above EUR 300,000.
2. But the same owner holds more than 50% of both companies on the last day of the period, so they are linked (art. 5(3)(3)). Combined income: 280,000 + 90,000 = EUR 370,000, which is EUR 70,000 above the EUR 300,000 limit.
3. So art. 5(2) does not apply to UAB A. It pays 17%: 60,000 x 17% = EUR 10,200.
4. At 7% it would have paid EUR 4,200. The link costs EUR 6,000.
5. Two side effects. The 70% loss cap now applies to UAB A, because it is not taxed at 7% under art. 5(2). And because UAB A's own taxable income for 2026 (at most its EUR 280,000 income) was not above EUR 300,000, it pays no advances in 2027 (art. 47(5)); the art. 5(3) link does not affect that test.

```oa-check
name: Related-entity test removes the 7% rate (2026)
inputs:
  income_a: 280000
  income_b: 90000
  threshold: 300000
  taxable_profit_a: 60000
steps:
  - combined_income: income_a + income_b
  - over_threshold: combined_income - threshold
  - tax_at_17: taxable_profit_a * 17 / 100
  - tax_at_7: taxable_profit_a * 7 / 100
  - cost_of_link: tax_at_17 - tax_at_7
expected:
  combined_income: 370000
  over_threshold: 70000
  tax_at_17: 10200
  tax_at_7: 4200
  cost_of_link: 6000
```

## Ask the client first

1. What was the company's income (not profit) for the period, and is it in its first, second or a later tax period?
2. Who owns it, and do the owners or their family members hold more than 50% of any other entity, or own another IĮ? What was that entity's income?
3. Are there losses brought forward, and from which activity (ordinary trading, securities, patent box)?
4. What interest does it pay and receive, does it have related persons or group companies, and how much does it owe to shareholders or group lenders compared with its equity?
5. Did it buy machinery, computers, software, rights or lorries in the year, were they new, and will it keep them for 3 years?
6. Which advance payment method does it use, and what was the tax for each of the last two years?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on Corporate Income Tax No. IX-675, consolidated version from 19 May 2026 to 31 December 2026: art. 4, 5, 6, 11, 18, 22, 30, 30-1, 30-2, 31, 40(3), 46-1, 47, 51, 53 and annex 1 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr | 2026-10-24 |
| Law on Tax Administration No. IX-2112, consolidated version from 1 July 2026: art. 68, 96, 99, 139 to 141 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr | 2026-10-23 |
| VMI, commentary on the Law on Corporate Income Tax (version current at 2026-10-23): art. 5(2) and (3), art. 30-1, art. 40(3) (4:1 controlled debt rule) | https://www.vmi.lt/evmi/pelno-mokestis (PDF "Pelno mokesčio komentaras (aktualus 2026-10-23)") | 2026-10-24 |
| Law No. XV-488 of 16 October 2025 amending PMĮ art. 12 and 30 (in force 1 January 2027) | https://www.e-tar.lt/portal/lt/legalAct/fb90ebe0ae7911f092fda1fd0c194cc5 | 2026-10-24 |
| VMI, late payment interest, answer KM2633 (0.027% a day from 1 August 2026) | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- | 2026-10-24 |

Not yet confirmed: the late payment interest rate after 31 October 2026 (it is reset each quarter); any administrative fine for filing the annual or advance return late (Code of Administrative Offences, not read); the VMI form codes for the annual and advance returns; the text of Government Resolution No. 1575 itself (the 4:1 rule is taken from the VMI commentary, not from the resolution); whether interest is charged when past tax is recomputed under art. 18(13) or 46-1(5); the list of non-taxable income in art. 12 and the R&D extra deduction in art. 17-1 (not read for this skill); group loss transfers under art. 56-1; and the PMĮ version in force from 1 January 2027.
