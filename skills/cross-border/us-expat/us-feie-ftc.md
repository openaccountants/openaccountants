---
name: us-feie-ftc
description: "US federal tax for citizens and green-card holders living abroad: the Foreign Earned Income Exclusion (IRC §911, Form 2555) versus the Foreign Tax Credit (IRC §901/§904, Form 1116). Covers the bona-fide-residence and physical-presence tests, the foreign housing exclusion, the §911 election and its revocation lock-out, the stacking rule, and the FEIE-versus-FTC decision. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
version: 0.1
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - cross-border-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Foreign Earned Income Exclusion vs Foreign Tax Credit for Americans abroad

This Guide is written for **tax year 2026** (returns filed in 2027). A short dated section near the end covers **2025 returns**, which are still being filed on extension until 15 October 2026. The 2026 Form 2555 instructions were not yet published when this was written (25 September 2026). Where this Guide describes form lines, it uses the 2025 instructions, so check the line numbers against the 2026 instructions before filing.

## Scope and who this is for

It covers a US citizen, or a resident alien (for example a green-card holder), who works abroad and files Form 1040. It explains how to:

- test whether the person qualifies for the foreign earned income exclusion (FEIE) and the foreign housing exclusion or deduction under §911, claimed on Form 2555
- work out the exclusion, the housing amount and the tax on the income that is left
- decide between the FEIE, the foreign tax credit on Form 1116, or the FEIE with the credit on the wages above the limit
- avoid the traps: the lost additional child tax credit and earned income credit, the revocation bar, and self-employment tax, which the FEIE never removes

The mechanics of Form 1116 itself (categories, the limitation formula, carryovers, currency) are in the separate Guide `us-foreign-tax-credit-1116`. This Guide does not cover nonresident aliens, US territories (Puerto Rico, Guam and so on), state returns, or the information returns (FBAR, Form 8938), which are in `us-fbar-fatca-reporting`.

## Ask the client first

- Are you a US citizen or a green-card holder? If a green-card holder, of which country are you a citizen or national?
- Who pays you? If it is the US government or one of its agencies, the FEIE is not available (see Boundaries).
- Where is your main place of work, and where do your family, home and economic ties sit? Do you keep a home in the US that you return to between work periods?
- Exact travel dates for the whole period abroad, including days in the US, days in transit and any time in Cuba. Passport stamps and travel records are the evidence.
- Have you told the foreign tax authority that you are **not** a resident there, and did they accept that?
- What did you earn abroad: wages, self-employment profit, bonuses paid late, housing paid by the employer? Is any of it a pension or investment income?
- How much foreign income tax did you pay or owe on the wages, and for which period?
- Your foreign rent and housing costs, and the city.
- Have you **ever** filed Form 2555? Have you ever revoked it, or claimed the foreign tax credit, the additional child tax credit or the earned income credit instead in a later year?
- Do you have children for whom you want the child tax credit, or plans to contribute to an IRA?
- For self-employed clients: which country's social security system covers you, and do you hold a certificate of coverage?

## The method, step by step

1. **Confirm the person is in scope.** A US citizen or resident alien with income for personal services performed abroad. Separate foreign earned income from pensions, investment income and US government pay, which the FEIE never covers.
2. **Run the tax home test.** The tax home must be in a foreign country throughout the qualifying period. If the person's abode is in the US, they fail, unless serving in a combat zone in support of the US Armed Forces.
3. **Run one presence test.** Either the bona fide residence test (foreign residence for an uninterrupted period that includes a full tax year) or the physical presence test (at least 330 full days in any 12 consecutive months). Record the test, the dates and the day count. If neither is met, the FEIE is unavailable; go to step 7.
4. **Count the qualifying days in the tax year** and prorate the exclusion limit, the housing base and the housing limit if the period does not cover the whole year.
5. **Compute the housing amount first**, then the FEIE. The FEIE is the smaller of the limit and foreign earned income minus the housing exclusion.
6. **Compute the tax on the income that is left** using the stacking rule (the Foreign Earned Income Tax Worksheet). Remove the credits the election blocks: the additional child tax credit and the earned income credit.
7. **Compute the credit path** on Form 1116 with the method in `us-foreign-tax-credit-1116`.
8. **Compare the options** (FEIE only, credit only, FEIE plus credit on the excess) on total US tax and on refundable credits lost. Check the revocation consequences before switching.
9. **Add self-employment tax** on all net self-employment earnings, excluded or not, unless a totalization agreement exempts them.
10. **File on time** with the right forms and statements (see Filing).

## Who qualifies ([Form 2555 instructions](https://www.irs.gov/instructions/i2555); [Pub. 54](https://www.irs.gov/publications/p54); [§911(d)](https://www.law.cornell.edu/uscode/text/26/911))

You qualify only if **both** apply: you meet the tax home test, and you meet either the bona fide residence test or the physical presence test.

**Tax home test.**

- Your tax home is your regular or principal place of business, employment or post of duty, wherever your family lives.
- You do not have a foreign tax home for any period in which your **abode** is in the US. Abode follows family, economic and personal ties.
- Keeping a dwelling in the US does not by itself put your abode there, and nor does a temporary stay in the US, but both can count against you.
- The IRS example: a worker on a foreign offshore rig on a 28-day-on/28-day-off rota who goes home to the US in the off weeks has a US abode and cannot claim either exclusion or the housing deduction.
- Exception: people serving in a combat zone in support of the US Armed Forces can have a foreign tax home even with a US abode.

**Bona fide residence test.**

- Open to a US citizen, and to a resident alien **only if** that person is a citizen or national of a country that has an income tax treaty in force with the US.
- You must be a bona fide resident of a foreign country for an uninterrupted period that includes an **entire tax year** (1 January to 31 December for a calendar-year filer).
- It turns on your intention about the length and nature of the stay; acts outweigh words. Going abroad for a definite, temporary purpose and then returning does not make you a resident.
- If you told the foreign authorities you are **not** resident there and they hold you not subject to their income tax for that reason, or have not ruled against that claim, you are **not** a bona fide resident of that country.

**Physical presence test.**

- Open to US citizens and resident aliens.
- At least **330 full days** in a foreign country or countries during any 12 consecutive months. A full day is the 24 hours from midnight, so travel days usually do not count.
- The days need not be consecutive. Time over international waters is not a day in a foreign country.
- The 12-month period can start or end in another calendar year, but it must include part of the tax year.
- Days in Cuba in breach of US travel restrictions do not count, and income earned there is not foreign earned income.

**Waiver.** If you had to leave a country because of war, civil unrest or similar conditions in a country the IRS lists for that year, the minimum time can be waived. You must show you would otherwise have met it, attach a statement and write "Claiming Waiver" at the top of Form 2555.

## What can be excluded ([§911(b) and (d)](https://www.law.cornell.edu/uscode/text/26/911); [Form 2555 instructions](https://www.irs.gov/instructions/i2555))

Foreign earned income is pay for personal services you performed in a foreign country during the qualifying period: wages, salaries, professional fees, noncash pay (such as a home or car), allowances and reimbursements.

It does **not** include:

- pensions and annuities, including social security
- interest, dividends, capital gains, alimony and other investment income
- amounts paid by the US government or its agencies to their employees
- amounts received after the end of the tax year following the year in which the work was done
- amounts that are really a distribution of company profits rather than reasonable pay for the work

**Business with capital.** If both personal services and capital are material income-producing factors in an unincorporated business, only reasonable pay for your services counts as earned income, capped at **30%** of your share of net profits. If capital is not material, all of the income is earned income.

**Timing.** Income is earned in the year you do the work. Pay received in 2026 for 2025 work is excluded only to the extent it would have been excludable in 2025, and it is reported by statement, not in Part IV of Form 2555.

## Figures for 2026 ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf); [§911(c)](https://www.law.cornell.edu/uscode/text/26/911))

| Item | 2026 | Source |
|---|---|---|
| Maximum FEIE, per qualifying person | $132,900 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) section .39 |
| Base housing amount (16% of the maximum, full year) | $21,264 | [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) section 2 |
| General limit on housing expenses (30% of the maximum, full year) | $39,870 | [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) section 2 |
| Higher limits for listed high-cost cities | See the table | [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) section 3 |

- Both housing amounts are figured on a daily basis and multiplied by the qualifying days in the tax year, so a part year gets a smaller base and a smaller limit.
- Only use a city limit if the city is in the Notice 2026-25 table. For example, the 2026 full-year limit is $68,600 for London, $86,700 for Singapore and $116,900 for Geneva. A city not listed uses the general limit.
- If both spouses qualify, each can exclude up to the maximum on their own Form 2555. Community property rules do not change this.

## Housing exclusion and housing deduction ([Form 2555 instructions](https://www.irs.gov/instructions/i2555); [Pub. 54](https://www.irs.gov/publications/p54); [§911(c)](https://www.law.cornell.edu/uscode/text/26/911))

**Housing amount** = qualifying housing expenses, capped at the housing limit, minus the base housing amount.

- Qualifying expenses are reasonable (not lavish) costs for you and, if they live with you, your spouse and dependents: rent, utilities other than telephone, property insurance, nonrefundable lease fees, furniture rental, residential parking and repairs.
- Not qualifying: deductible interest and taxes, mortgage principal, buying or improving a home, depreciation, domestic help, pay TV, and buying furniture.
- A second foreign household counts only if your family lives away from your tax home because conditions there are dangerous, unhealthful or otherwise adverse.
- Reduce the housing amount by any nontaxable US government housing allowance.

**Exclusion or deduction.**

- The part of the housing amount paid for with **employer-provided amounts** is an exclusion. Employer-provided amounts include the wages your employer pays you, so an employee who pays rent out of salary still uses the exclusion.
- If you choose the housing exclusion, you must claim all of it, and you figure it **before** the FEIE.
- The housing **deduction** is only for the part not paid with employer-provided amounts, so it needs self-employment income. It cannot exceed foreign earned income minus the FEIE and the housing exclusion. A disallowed excess carries forward to the **next year only**.
- The housing exclusion and the FEIE are separate elections and must be revoked separately.

## Stacking and what the election blocks ([§911(f)](https://www.law.cornell.edu/uscode/text/26/911); [Form 2555 instructions](https://www.irs.gov/instructions/i2555); [Pub. 54](https://www.irs.gov/publications/p54); [§24](https://www.law.cornell.edu/uscode/text/26/24))

**Stacking rule.** If you exclude income, the tax on the income left is worked out at the rates that would apply if you had not excluded it. In practice:

- tax on (taxable income + excluded amount), minus tax on the excluded amount alone
- use the Foreign Earned Income Tax Worksheet in the Form 1040 instructions for line 16, and the separate worksheet in the Form 6251 instructions for the alternative minimum tax

**No double benefit.**

- No credit or deduction for foreign tax allocable to excluded income (§911(d)(6)). If all the foreign earned income is excluded, none of the foreign tax on it is creditable.
- Deductions definitely related to the excluded income are also lost, prorated by excludable over total foreign earned income, and entered on line 44 of Form 2555. The housing deduction and the §119 meals and lodging exclusion are not treated as related.

**Credits lost in any year you claim either exclusion or the housing deduction:**

- the **additional child tax credit** (the refundable part of the child tax credit; §24(d) switches it off for anyone who elects the FEIE)
- the **earned income credit**

**Other side effects.**

- For the child tax credit phase-out, modified AGI adds back the excluded income (§24(b)).
- For IRA contributions, excluded wages and housing do not count as compensation. If all of the pay is excluded, the client may have no room to contribute.

## The election, revocation and the 5-year bar ([§911(e)](https://www.law.cornell.edu/uscode/text/26/911); [Reg. §1.911-7](https://www.law.cornell.edu/cfr/text/26/1.911-7); [Pub. 54](https://www.irs.gov/publications/p54))

**Making the election.** File Form 2555 with the return. The election is valid only if made on:

- a timely filed return, including extensions
- an amended return that amends a timely filed return, filed within the §6511(a) refund period
- an original return filed within one year after the original due date
- a later return, if no tax is owed after the exclusion, or if tax is owed and the return is filed before the IRS finds the failure to elect. Write "Filed Pursuant to Section 1.911-7(a)(2)(i)(D)" at the top of Form 1040

**Once made, it continues** for that year and all later years until revoked. You do not need to revoke just because you have no foreign earned income in a year.

**Revoking.**

- Attach a statement to the return or amended return for the first year you do not want the exclusion. Revoke the FEIE and the housing exclusion separately.
- Taking the foreign tax credit or deduction, the additional child tax credit or the earned income credit in a later year **instead of** the exclusion is treated as a revocation for that year (Pub. 54).
- Taking the credit only on the foreign tax on wages **above** the exclusion limit, while still claiming the FEIE, is allowed.

**The bar.** After a revocation you cannot elect the same exclusion again before the **6th tax year after** the year the revocation took effect, unless the IRS consents through a ruling request. The IRS weighs things like a period of US residence, a move to a country with different tax rates, or a change of employer.

## FEIE or credit: how to decide ([Pub. 54](https://www.irs.gov/publications/p54); [Form 1116 instructions](https://www.irs.gov/instructions/i1116); [§904(c)](https://www.law.cornell.edu/uscode/text/26/904))

- **No or low foreign income tax**: the credit gives little relief, so the FEIE usually wins. Check the additional child tax credit and earned income credit you give up.
- **Foreign tax at or above US tax on the wages**: the credit usually removes US tax on the wages, keeps refundable credits and IRA room, and excess credit carries back 1 year and forward 10 years in the same category. There is no election to revoke later.
- **Wages above the limit in a taxed country**: consider the FEIE up to the limit plus the credit on the rest. Tax on the excluded part is not creditable; on Form 1116 the foreign tax is reduced on line 12 by the excluded share, as set out in `us-foreign-tax-credit-1116`. Excluded wages are left out of line 1a but included on lines 3d and 3e.
- **Model the next five years.** If the client may move from a low-tax to a high-tax country, electing the FEIE now and switching to the credit later triggers the revocation bar.
- Document the options you modelled and why you chose one.

## Self-employment and social security tax ([Pub. 54](https://www.irs.gov/publications/p54))

- The FEIE is an income tax exclusion only. Self-employment tax is figured on **all** net earnings from self-employment, including income excluded under the FEIE.
- Self-employment tax is due if net earnings from self-employment are at least $400.
- A totalization agreement between the US and the country of work can assign coverage to one country. If your earnings should be covered only by the US, request a certificate of coverage from the SSA to be exempt from the foreign tax; if only the foreign system covers you, keep that country's certificate as evidence for the US exemption.
- For employees, US social security and Medicare tax generally do not apply to wages for work outside the US, unless an exception applies, such as working for an American employer. The FEIE does not change that answer.

## Boundaries and exceptions

| Situation | Treatment | Source |
|---|---|---|
| US government employee working abroad | Pay is not foreign earned income; do not file Form 2555; use the credit if foreign tax applies | [Form 2555 instructions](https://www.irs.gov/instructions/i2555) |
| Abode in the US (rotational work, family at home) | Fails tax home test | [Form 2555 instructions](https://www.irs.gov/instructions/i2555) |
| Green-card holder from a non-treaty country | Bona fide residence test not available; physical presence test still is | [Form 2555 instructions](https://www.irs.gov/instructions/i2555) |
| Told the foreign country you are nonresident | Not a bona fide resident of that country | [Form 2555 instructions](https://www.irs.gov/instructions/i2555) |
| Fewer than 330 full days in every 12-month window | Physical presence test fails | [Pub. 54](https://www.irs.gov/publications/p54) |
| Housing costs at or below the base amount | No housing exclusion or deduction | [§911(c)](https://www.law.cornell.edu/uscode/text/26/911) |
| Pension, dividends, interest, capital gains | Never excludable; credit only | [Form 2555 instructions](https://www.irs.gov/instructions/i2555) |
| Pay received after the end of the year following the work year | Not excludable | [§911(b)](https://www.law.cornell.edu/uscode/text/26/911) |
| FEIE claimed, children in the family | No additional child tax credit, no earned income credit | [Form 2555 instructions](https://www.irs.gov/instructions/i2555) |
| Self-employed abroad with FEIE | Self-employment tax still due on full net earnings | [Pub. 54](https://www.irs.gov/publications/p54) |
| Revoked FEIE, wants it back within 5 years | Needs IRS consent (ruling) | [Reg. §1.911-7](https://www.law.cornell.edu/cfr/text/26/1.911-7) |
| Work in a US territory (for example Puerto Rico) | Not a foreign country for §911; out of scope | [Form 2555 instructions](https://www.irs.gov/instructions/i2555) |

## Worked cases ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf); [Form 2555 instructions](https://www.irs.gov/instructions/i2555); [Pub. 54](https://www.irs.gov/publications/p54))

These use 2026 figures for a calendar-year filer.

**Case 1: no foreign tax (2026).** A single US citizen works all year in a country with no income tax, meets the physical presence test, earns wages of $100,000 and has no housing costs above the base.

- FEIE: the smaller of $132,900 and $100,000, so $100,000. No US income tax on the wages.
- There is no foreign tax, so the credit gives nothing. The FEIE is the better choice unless refundable credits matter.

**Case 2: housing in a city not listed (2026).** An employee qualifies for the full year, earns wages of $150,000 and pays rent and utilities of $50,000 out of salary.

- Expenses capped at the general limit: $39,870.
- Housing exclusion: $39,870 − $21,264 = $18,606.
- FEIE: the smaller of $132,900 and ($150,000 − $18,606 = $131,394), so $131,394.
- Total excluded: $18,606 + $131,394 = $150,000. The combined exclusion cannot exceed foreign earned income.

**Case 3: FEIE plus credit (2026).** A single filer abroad for the whole year has foreign wages of $180,000, no housing amounts and no deductible expenses. Foreign tax on the wages is $54,000. The client excludes $132,900.

- Wages left in gross income: $180,000 − $132,900 = $47,100. They go on a general category Form 1116.
- Foreign tax allocable to excluded income: $54,000 × 132,900 ÷ 180,000 = $39,870. Not creditable.
- Foreign tax still available for credit: $54,000 − $39,870 = $14,130, subject to the Form 1116 limit.
- US tax on the $47,100 is worked out at the rates that would apply to taxable income including the $132,900 (stacking).
- Compare with the credit alone on all $180,000. In a high-tax country the credit alone can leave the same or less US tax and keeps refundable credits.

**Case 4: part year (2026).** A citizen moves abroad and meets the physical presence test, with 200 qualifying days in 2026.

- FEIE limit: $132,900 × 200 ÷ 365 = $72,822 (rounded to the dollar).
- The base housing amount and the housing limit are also prorated by the 200 days.

**Case 5: self-employed (the Pub. 54 example).** A consultant abroad qualifies for the FEIE. Foreign earned income is $95,000, business deductions are $27,000 and net profit is $68,000.

- Self-employment tax is due on the full $68,000, even though the income is excluded for income tax.

**Case 6: the revocation bar.** A client claimed the FEIE for 2024. For 2025 they claim the foreign tax credit instead of the exclusion, so the election is treated as revoked for 2025.

- They cannot elect the FEIE again before 2031 (the 6th tax year after 2025) without IRS consent.
- 2026 to 2030 are barred years.

## When to refuse or refer

- The client works for the US government or a US agency: do not claim the FEIE; refer on allowances.
- The bona fide residence claim is weak (short or fixed-term posting, nonresident statement filed abroad, family kept in the US) and the physical presence test is not met: do not claim the FEIE; use the credit or refer.
- Day counts cannot be evidenced from travel records.
- The client has revoked the FEIE and wants it back within the bar: a ruling request is needed.
- Income from US territories, the Cuba travel rules, a waiver claim for adverse conditions, a second foreign household, or married couples with separate foreign households: refer.
- An unincorporated business where capital is material (the 30% rule), or pay for work spread over several years: refer unless you can document the allocation.
- A late election under Reg. §1.911-7(a)(2)(i)(D) after the IRS has contacted the client.
- Totalization agreement questions that decide which country's social security applies.

## Filing and deadlines ([Pub. 54](https://www.irs.gov/publications/p54); [Form 2555 instructions](https://www.irs.gov/instructions/i2555); [Reg. §1.911-7](https://www.law.cornell.edu/cfr/text/26/1.911-7))

For a 2026 calendar-year return:

- **Regular due date:** 15 April 2027.
- **Automatic 2-month extension** to 15 June 2027 to file **and pay**, if on the regular due date you live outside the US and Puerto Rico and your tax home is outside them. Attach a statement saying you qualify. Interest still runs from 15 April.
- **Form 4868** extends filing (not payment) to 15 October 2027.
- **Discretionary extra 2 months** to 15 December 2027 for taxpayers out of the country: send the IRS a letter by the extended due date explaining why. Not available if you have a Form 2350 extension.
- **First year, test not yet met:** either file Form 2350 by the due date to get an extension, usually to 30 days after you expect to qualify, or file on time without the exclusion and amend with Form 1040-X once you qualify.
- If filing on paper, attach Form 2555 to Form 1040 and mail it to the special address for Form 2555 filers, not the address for your state.
- Enter the exclusion on Schedule 1 (Form 1040), line 8d, as a negative amount.
- Do not report foreign tax withheld by an employer and paid to the foreign country as US withholding on Form 1040, line 25a or 25b.
- Estimated tax: you may leave out income you reasonably expect to exclude, but you must allow for the foreign tax credit you lose on it.

## 2025 returns (extended returns due 15 October 2026) ([Form 2555 instructions](https://www.irs.gov/instructions/i2555); [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf); [Pub. 54](https://www.irs.gov/publications/p54))

- **FEIE limit:** $130,000.
- **Base housing amount** (16%, full year): $20,800.
- **General housing limit** (30%, full year): $39,000, or $106.85 per day for a part year.
- City limits for 2025 are in Notice 2025-16. A 2025 filer may instead use the 2026 city limit in Notice 2026-25 where it is higher.
- The rules above (tests, stacking, lost credits, revocation, self-employment tax) are the same for 2025.
- The discretionary extension to 15 December 2026 must be requested by letter by 15 October 2026.

## Completion checklist

- [ ] Citizenship or green-card status confirmed; treaty nationality checked for a resident alien using the bona fide residence test.
- [ ] Payer is not the US government.
- [ ] Tax home abroad and abode tested and documented.
- [ ] One presence test met, with dates and a day count from travel records.
- [ ] Qualifying days in the tax year counted; limit, base and housing limit prorated.
- [ ] Only foreign earned income included; pensions, investment income and late pay removed.
- [ ] Housing figured before the FEIE; city limit taken from Notice 2026-25 only if listed.
- [ ] Tax figured with the Foreign Earned Income Tax Worksheet (and the Form 6251 version).
- [ ] No credit on foreign tax allocable to excluded income; related deductions reduced on line 44.
- [ ] Additional child tax credit and earned income credit removed if either exclusion or the housing deduction is claimed.
- [ ] Election history checked; any switch to the credit tested against the revocation bar.
- [ ] Self-employment tax figured on all net earnings, or a certificate of coverage on file.
- [ ] Extension statement, Form 2350 or Form 4868 filed as needed; correct mailing address used.
- [ ] FBAR and Form 8938 reviewed under `us-fbar-fatca-reporting`.

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
