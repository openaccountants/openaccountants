---
name: nz-tax-residency
description: "New Zealand tax residency for individuals in the 2027 income year (1 April 2026 to 31 March 2027). Covers the 183-day rule, the permanent place of abode test, the new non-resident visitor rule for arrivals on or after 1 April 2026 (275 days in 18 months), ceasing residency (325 days absent and no permanent place of abode) and the 4-year transitional resident exemption. Trigger on NZ tax resident, New Zealand residency 183 days, permanent place of abode NZ, leaving New Zealand taxes, transitional resident NZ, NZ tax emigration, move to New Zealand taxes, cease NZ tax residency, non-resident visitor NZ."
version: "2.0"
jurisdiction: NZ
tax_year: 2026
tax_year_notes: "New Zealand income year 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. Residency rules are day and year counts."
last_updated: 2026-11-14
drafted_by: OpenAccountants
approved_by: pending
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# New Zealand tax residency for individuals, 2027 income year

> **Source-cited draft.** Built from Inland Revenue's residency page, its transitional residents page and guide IR295 (April 2026), read on 14 November 2026. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before anyone relies on them.

## Scope

When an individual becomes or stops being a New Zealand tax resident, the non-resident visitor rule for arrivals on or after 1 April 2026, and the transitional resident exemption for new arrivals. The year covered is the income year from 1 April 2026 to 31 March 2027 (IRD's "2027 income year"). A resident is taxed on worldwide income; a non-resident only on New Zealand-sourced income. Tax residency is separate from immigration status.

Out of scope: companies and trusts (their residence tests differ), double tax agreement tie-breakers (refer), visitors who arrived before 1 April 2026 under the earlier rules (refer), foreign superannuation and foreign trust computations. The income tax computation itself is in [nz-income-tax-ir3](nz-income-tax-ir3.md); the rates are restated here only as a quick reference.

**Quick answer.** A person becomes resident on the first of: more than 183 days present in any 12-month period, or a permanent place of abode in New Zealand. A person stops being resident only when BOTH apply: no permanent place of abode, and away more than 325 days in any 12-month period. A non-resident visitor who arrived on or after 1 April 2026 and meets every condition is not caught by the 183-day rule while present 275 days or fewer in any 18-month period.

## Ask the client first

1. On what dates were you in New Zealand over the last 18 months, and when did you first arrive?
2. Do you have a place in New Zealand where you usually live, owned or rented, and is it kept for you while away?
3. Were you a New Zealand tax resident at any time in the last 10 years?
4. Do you work for a New Zealand employer, sell to New Zealand customers, or receive Working for Families?
5. Where are you tax resident abroad, and do you pay tax there?
6. What foreign income do you have: employment, business, investments, foreign superannuation?

## The method, step by step

1. **Permanent place of abode first.** Decide whether the person has a place where they usually live in New Zealand, using the ties IRD lists (step 2 below). A permanent place of abode makes a person resident whatever the day count, and stops them ceasing to be resident however long they are away.
2. **Weigh the ties.** IRD looks at how often the person returns and how long they stay; family and social connections; economic interests such as investments or superannuation funds in New Zealand; employment or business connections; and whether they intend to return to live. The place need not be owned, and need not be vacant while they are away: a house owned and rented out while abroad can still be one. IRD's detailed view is interpretation statement IS 25/16 on its Tax Technical site.
3. **Non-resident visitor check (arrivals on or after 1 April 2026).** Check every condition in IR295: arrived on or after 1 April 2026 and present 275 days or fewer in any 18-month period; not a tax resident or transitional resident immediately before arriving; not working for a New Zealand resident or a non-resident's New Zealand branch (IRD's page adds "or paid by"); not selling goods or services to people or businesses in New Zealand, including on behalf of someone overseas; not required to be present in New Zealand for work; neither the person nor their spouse or partner receives Working for Families (including Best Start); lawfully present; and required to pay tax in the country where they are tax resident. If all are met, the 183-day rule does not apply.
4. **Count days present.** Count days in New Zealand in any 12-month period. Parts of days, including the days of arrival and departure, count as whole days. The days need not be consecutive. More than 183 days makes the person resident, backdated to the first of the 183 days. Residency starts on the earlier of that date and the date a permanent place of abode is established.
5. **Once resident, stay resident.** IR295: "If you've ever been resident in New Zealand under the 183-day rule you remain resident until you become a non-resident."
6. **Transitional resident.** For a new resident, check the 10-year look-back and work out the exemption end date (see the Boundary table and the transitional dates under Worked cases).
7. **Leaving.** For a person leaving, confirm there is no permanent place of abode, then count days absent in any 12-month period. Parts of days in New Zealand (such as the day of departure) do not count as days absent. More than 325 days absent, with no permanent place of abode, makes the person non-resident, backdated to the first of the 325 days.
8. **Record and tell IRD.** Keep the day count and the ties analysis on file. Tell IRD about a change of status (see Filing and payment).

### Rates, bands and thresholds

Day counts and periods (2027 income year):

| Item | Value | Conditions | Source |
| --- | --- | --- | --- |
| 183-day rule | more than 183 days in any 12-month period | Parts of days count; backdated to the first of the 183 days; not for a qualifying non-resident visitor | https://www.ird.govt.nz/international-tax/individuals/tax-residency-status-for-individuals |
| Non-resident visitor limit | 275 days in any 18-month period | Arrived on or after 1 April 2026 and all conditions met; resident from day 276 if still lawfully present | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf |
| 325-day rule (ceasing) | more than 325 days absent in any 12-month period | Only with no permanent place of abode; backdated to the first of the 325 days | https://www.ird.govt.nz/international-tax/individuals/tax-residency-status-for-individuals |
| Transitional resident look-back | not resident at any time in the 10 years before qualifying | Qualified on or after 1 April 2006; applies once, automatically | https://www.ird.govt.nz/roles/nz-tax-residents/exemption |
| Transitional exemption length | ends 4 years after the end of the month of qualifying | Qualifying date is not backdated for this purpose | same |

Personal income tax rates for residents, "From 1 April 2025" table (IRD publishes no later table, so it applies to the 2027 income year; the computation is in [nz-income-tax-ir3](nz-income-tax-ir3.md)):

| Taxable income (NZD) | Rate | Source |
| --- | --- | --- |
| 0 to 15,600 | 10.5% | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals |
| 15,601 to 53,500 | 17.5% | same |
| 53,501 to 78,100 | 30% | same |
| 78,101 to 180,000 | 33% | same |
| 180,001 and over | 39% | same |

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Non-resident visitor stays more than 275 days, still lawfully present | Resident from day 276 | IR295 |
| Non-resident visitor stops meeting a condition before 275 days | Resident from the earlier of meeting the 183-day rule (visitor days count) or having a permanent place of abode | IR295 |
| Visitor no longer lawfully present | All days count toward the 183-day rule; if met, resident from the first of the 183 days | IR295 |
| Visitor who arrived before 1 April 2026 | IRD's web page states the rule without a start date; the 1 April 2026 arrival date comes from IR295 only. Refer | IR295; IRD residency page |
| Recognised Seasonal Employer Limited Visa or Fishing Crew Work Visa worker | Does not become resident after 183 days, and is taxed as a non-resident, as long as no permanent place of abode is established | IRD residency page |
| Person sent overseas to work for the New Zealand government | Stays resident however long away, with or without a permanent place of abode. Spouse, partner and children work out their own status | IRD residency page |
| Keeps a home in New Zealand, even rented out, while abroad | Can be a permanent place of abode, so does not cease to be resident | IRD residency page |
| Transitional resident: most foreign-source income | Exempt, including overseas interest, dividends, foreign investment fund income and rent | IRD transitional page |
| Transitional resident: income earned overseas from employment or personal services | Not exempt; a double tax agreement may give full or partial relief | IRD transitional page |
| Transitional resident: lump sum from a foreign superannuation fund | Its own 4-year exemption rule, same period calculation. Refer | IRD transitional page |
| Transitional exemption ends early | If the person, or a transitional-resident partner, applies for Working for Families (including Best Start); includes exempt income in the IR3; confirms to a foreign jurisdiction and IRD that New Zealand tax is paid on overseas income from a date in the period; or tells IRD they no longer want it. The opt-out cannot be revoked, though IRD may in limited situations consider a request to amend the return that ended it | IRD transitional page |
| After the exemption ends | Taxed on worldwide income from the day after it ends | IRD transitional page |

### Red flags

- A client says "I left, so I am non-resident" while keeping a house, family or a job in New Zealand: the permanent place of abode test comes first.
- A remote worker selling to New Zealand customers claims non-resident visitor status: selling goods or services to people in New Zealand breaks the conditions.
- A transitional resident has filed an IR3 including foreign interest or dividends: that may have ended the exemption.

## Worked cases

**Case 1: arrival with no home, is she resident? (decision).** Ana arrives on 1 May 2026 on contract to a New Zealand employer, so she cannot be a non-resident visitor. She rents short-term with no permanent place of abode. In the 12 months from 1 May 2026 she is present 190 days (part days counted whole). 190 exceeds 183, so she is resident, backdated to 1 May 2026, the first of the 183 days. Her colleague is present 150 days in the same 12 months, stays below the threshold and is not resident on days alone.

```oa-check
name: NZ 183-day rule, resident or not
inputs:
  days_ana: 190
  days_colleague: 150
  threshold: 183
steps:
  - margin_ana: days_ana - threshold
  - ana_resident: min(max(margin_ana, 0), 1)
  - margin_colleague: days_colleague - threshold
  - colleague_resident: min(max(margin_colleague, 0), 1)
expected:
  margin_ana: 7
  ana_resident: 1
  margin_colleague: -33
  colleague_resident: 0
```

**Case 2: leaving New Zealand, does he cease to be resident? (decision).** Ben sells his house and leaves on 1 June 2026 with no permanent place of abode left. In the following 12 months he is in New Zealand for 30 part or whole days (counted as days present, not absent), so he is absent 365 - 30 = 335 days. 335 exceeds 325, so he ceases to be resident, backdated to the first of the 325 days. Had he kept the family home available to return to, no day count would make him non-resident. His sister, in the same position, visits New Zealand for 45 days in the 12 months, is absent 320 days and stays resident.

```oa-check
name: NZ 325-day rule, ceases or stays resident
inputs:
  days_in_year: 365
  days_present_ben: 30
  days_present_sister: 45
  threshold: 325
steps:
  - absent_ben: days_in_year - days_present_ben
  - ben_ceases: min(max(absent_ben - threshold, 0), 1)
  - absent_sister: days_in_year - days_present_sister
  - sister_ceases: min(max(absent_sister - threshold, 0), 1)
expected:
  absent_ben: 335
  ben_ceases: 1
  absent_sister: 320
  sister_ceases: 0
```

**Transitional dates (IRD's own examples).** Ed arrived 10 March 2023 and moved into a house he bought on 22 April 2023: exemption starts 10 March 2023 and ends 30 April 2027. Sarah arrived 10 March 2023, left 14 March, returned 22 April and qualified under the 183-day rule on 17 October 2023 (5 days in March plus 178 days from 22 April to 16 October): her exemption starts 10 March 2023 and ends 31 October 2027.

## When to refuse or refer

- Refer anyone who may be resident in New Zealand and another country at once: the double tax agreement tie-breaker decides, and IS 25/16 is IRD's detailed view.
- Refer part-year cases (arriving or leaving during the income year) where the backdated start or end date changes what income is taxed.
- Refer transitional residents with foreign superannuation, foreign trusts, or employment income earned partly overseas.
- Refer a person who has already opted out, or filed a return that may have ended the exemption.
- Refer visitors who arrived before 1 April 2026.
- Refuse to state that someone is non-resident only because they left New Zealand: the permanent place of abode test comes first.

## Filing and payment

- Tell IRD about a change of residency status. A transitional resident must tell IRD on becoming non-resident during the exemption period.
- If unsure of status, complete the New Zealand tax residence questionnaire IR886 (May 2026 edition) and send it through a myIR message, or by post to the address on the form.
- A transitional resident with overseas income that is not exempt shows it on the Individual income tax return IR3 ([nz-income-tax-ir3](nz-income-tax-ir3.md)).
- A certificate of residence for a foreign tax authority can be requested in myIR.

## Completion checklist

- [ ] Permanent place of abode decided, with the ties recorded
- [ ] Non-resident visitor conditions checked for an arrival on or after 1 April 2026
- [ ] Days present (or absent) counted in the right 12-month or 18-month window, part days treated correctly
- [ ] Start or end date backdated correctly
- [ ] Transitional look-back and end date worked out, early-ending events checked
- [ ] Referral cases (dual residence, pre-April 2026 visitors, foreign super) referred

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRD, Tax residency status for individuals: read for the 183-day and 325-day rules, day counting, the non-resident visitor conditions, permanent place of abode ties, seasonal workers, government workers, IR886 and IS 25/16 | https://www.ird.govt.nz/international-tax/individuals/tax-residency-status-for-individuals | 2026-11-14 |
| IRD guide IR295 (April 2026), New Zealand tax residence: read for the 1 April 2026 arrival date, the 275-day rule and what happens when a visitor stops qualifying, and the 183-day "remain resident" sentence | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf | 2026-11-14 |
| IRD, Temporary tax exemption (transitional residents): read for who qualifies, exempt and non-exempt income, start and end dates, the Ed and Sarah examples, and early-ending events | https://www.ird.govt.nz/roles/nz-tax-residents/exemption | 2026-11-14 |
| IRD, Tax rates for individuals: read for the "From 1 April 2025" rate table | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals | 2026-11-14 |

Not yet confirmed: the Income Tax Act 2007 section numbers (subpart YD, sections YD 1 to YD 3) and the statutory text of the non-resident visitor rule, because legislation.govt.nz refused script access on 14 November 2026 (HTTP 202 empty and 403); the rules above rest on IRD's pages. Treatment of visitors who arrived before 1 April 2026.

> Working paper only. The permanent place of abode test can catch individuals who believe they have left New Zealand but keep property there. Have a qualified New Zealand chartered accountant review this Guide before departing.

> Contributed by OpenAccountants.
