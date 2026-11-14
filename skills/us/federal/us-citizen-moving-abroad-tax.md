---
name: us-citizen-moving-abroad-tax
description: Plan the US federal tax side of a US citizen or green card holder moving abroad in 2026, and route each issue to the skill that computes it. Covers worldwide taxation by citizenship, the choice between the foreign earned income exclusion (USD 132,900 for 2026, 330 full days or bona fide residence) and the foreign tax credit by destination (zero-tax Gulf against high-tax Europe), the reporting web (FBAR, Form 8938, Form 5471, Form 8621, Forms 3520), the PFIC and foreign company traps, self-employment tax and totalization agreements, states that keep taxing leavers, retirement accounts abroad, and renunciation with the section 877A exit tax (covered expatriate threshold USD 211,000, exclusion USD 910,000 for 2026). Trigger on "moving abroad", "American expat taxes", "US citizen living abroad", "FEIE or foreign tax credit", "Dubai US tax", "renounce US citizenship", "exit tax", "accidental American". Federal only.
version: "1.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# A US citizen moving abroad: what changes, what does not, and which skill computes it, tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32 (2026 inflation figures), 26 U.S.C. 877, 877A and 911 (2024 edition), IRS Publication 54 (2025, the latest edition), the 2026 Instructions for Form 2555 and the Instructions for Form 8854, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** The United States taxes its **citizens and green card holders on worldwide income wherever they live**, so moving abroad adds a second tax system rather than replacing the first: Form 1040 is still filed every year. Two tools stop double tax: the **foreign earned income exclusion** (up to **USD 132,900** of 2026 earned income, if the person passes the 330-full-day or bona fide residence test) and the **foreign tax credit**. In a **zero-tax country** (UAE, most of the Gulf) only the exclusion helps, and income above it is fully taxed in the US. In a **high-tax country** (most of Europe) the credit usually wipes out the US tax. The traps are the information returns (each with penalties from about USD 10,000), foreign funds (PFICs), foreign companies (CFCs), self-employment tax in countries without a totalization agreement, and states that keep treating the leaver as resident. Renouncing is possible, but a **covered expatriate** (net worth USD 2,000,000 or more, average net income tax above **USD 211,000**, or not compliant for 5 years) pays an exit tax on gains above **USD 910,000**.

## Scope and who this is for

In scope: US citizens and green card holders who move, or have moved, abroad in 2026 (employees, founders, retirees, accidental Americans) and their advisers. This skill sets out the sequence and the decisions, and sends each computation to its own skill.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The foreign earned income exclusion and housing exclusion on Form 2555, line by line | `us-foreign-earned-income-2555` |
| Choosing between the exclusion and the credit, and combining them | `us-foreign-earned-income-2555` and `us-foreign-tax-credit-1116` |
| The foreign tax credit on Form 1116 | `us-foreign-tax-credit-1116` |
| FBAR and Form 8938 thresholds and filing | `us-fbar-and-fatca-8938` |
| A foreign company the client owns: Form 5471 and the inclusions | `us-form-5471-cfc-information`, `us-gilti-fdii-beat` |
| Foreign trusts, foreign gifts and inheritances (Forms 3520 and 3520-A) | `us-foreign-trust-reporting` |
| Renunciation and the exit tax computation | `us-expatriation-exit-tax` |
| Self-employment tax | `us-schedule-c-and-se-computation` |
| Residency status and the green card test | `us-tax-residency` |
| Leaving a state | `us-multi-state-residency-and-allocation`, `ca-residency-leaving-california` |
| Gift and estate tax | `us-estate-gift-706-709` |
| The destination country's own tax | That country's skills |

## Ask the client first

1. **Status:** US citizen (including by birth abroad to a US parent), or green card holder? Since when? Any other citizenship?
2. **Destination and dates:** which country, the date of the move, and the days expected in the US in 2026 and 2027 (the 330-day count).
3. **Income after the move:** salary (from whom, paid where), self-employment, rental, pensions, dividends and gains, and the foreign tax expected on each.
4. **Accounts and assets abroad:** bank and brokerage accounts, pensions, insurance wrappers, and any foreign mutual funds or ETFs bought or planned.
5. **Companies:** does the client own, or plan to form, a company abroad? What share, and with whom?
6. **Family:** a spouse who is not a US person? Gifts or inheritances expected from non-US relatives?
7. **State ties left behind:** home, driver's licence, voter registration, bank branch, spouse or children, business.
8. **US retirement accounts** (401(k), IRA, Roth) and any plans to cash them out.
9. **Compliance history:** have all US returns, FBARs and information returns been filed for the last 5 years?
10. **Is renunciation in view?** Net worth, and US income tax paid in each of the last 5 years.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Foreign earned income exclusion, maximum per person | USD 132,900 | [Rev. Proc. 2025-32, section 4.39](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Physical presence test: full days in a foreign country in any 12-month period | 330 | [26 U.S.C. 911(d)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| Foreign housing: base amount (16% of the exclusion), full year | USD 21,264 (derived: 16% of the USD 132,900 exclusion) | [26 U.S.C. 911(c)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm) |
| Foreign housing: expense limit for most locations (30% of the exclusion), full year | USD 39,870 | [Instructions for Form 2555 (2026)](https://www.irs.gov/pub/irs-pdf/i2555.pdf) |
| Standard deduction, single | USD 16,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Self-employment tax rate (not reduced by the exclusion) | 15.3% | [IRS, Self-employment tax](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) |
| Covered expatriate: average annual net income tax for the 5 prior years more than | USD 211,000 | [Rev. Proc. 2025-32, section 4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Covered expatriate: net worth of | USD 2,000,000 or more | [26 U.S.C. 877(a)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877.htm) |
| Exit tax: gain on the deemed sale reduced by | USD 910,000 | [Rev. Proc. 2025-32, section 4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Covered gifts and bequests from a covered expatriate: taxed above | USD 19,000 a year | [Rev. Proc. 2025-32, section 4.42](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Annual gift exclusion to a non-citizen spouse | USD 194,000 | [Rev. Proc. 2025-32, section 4.42](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Gifts from foreign corporations or partnerships: reportable above | USD 20,573 | [Rev. Proc. 2025-32, section 4.47](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

The FBAR and Form 8938 thresholds are owned by `us-fbar-and-fatca-8938` and are not restated here. The 2026 income tax brackets used in Case 1 are from Rev. Proc. 2025-32 (via `us-form-1040-individual-return`).

### Step 1: what does not change

1. A US citizen files Form 1040 on worldwide income for every year, wherever they live. A green card holder does too, until the green card is formally given up or the person is treated as a nonresident under a treaty (which has its own consequences: see `us-tax-residency`). Giving up a green card held in at least 8 of the last 15 years triggers the same expatriation rules as renouncing citizenship (Step 8). Source: [Publication 54](https://www.irs.gov/publications/p54).

### Step 2: choose the shield by destination

2. **Foreign earned income exclusion** (Form 2555): excludes **earned** income (salary, self-employment), never dividends, interest, gains or pensions, up to **USD 132,900** for 2026, plus a housing exclusion for housing costs above **USD 21,264** and up to (for most places) **USD 39,870**. The person needs a **tax home abroad** and either **330 full days** outside the US in any 12-month period (a partial day in the US is not a full foreign day), or **bona fide residence** abroad for a full tax year. The remaining income is taxed at the rates that would apply without the exclusion (the stacking rule in section 911(f)). Source: [26 U.S.C. 911](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm); [Instructions for Form 2555](https://www.irs.gov/pub/irs-pdf/i2555.pdf).
3. **Foreign tax credit** (Form 1116): a dollar-for-dollar credit for foreign income tax actually paid, by category, with unused credit carried back 1 year and forward 10 years. Computation: `us-foreign-tax-credit-1116`.
4. **Zero-tax landing (UAE, most of the Gulf):** there is no foreign tax to credit, so the exclusion is the only shield; everything above it is taxed in the US as if the person lived in the US. High earners are often surprised by the bill (Case 1).
5. **High-tax landing (Germany, France, the UK):** local tax usually exceeds the US tax on the same income, so the credit wipes out the US tax and builds carryforwards. Advisers often prefer the credit alone there, partly because a person who revokes the exclusion cannot choose it again for 5 years without IRS consent. Source: [Instructions for Form 2555](https://www.irs.gov/pub/irs-pdf/i2555.pdf).
6. **Mixed lives** (Gulf salary, European rent, US portfolio) use both, income type by income type: `us-foreign-earned-income-2555` and `us-foreign-tax-credit-1116`.
7. **Timing:** a citizen living abroad on the due date gets an automatic 2-month extension to **15 June** (interest still runs from 15 April) and can extend to 15 October; Form 2350 gives more time to meet the presence or residence test in the first year. Source: [Publication 54](https://www.irs.gov/publications/p54).

### Step 3: the reporting web

8. These forms raise no tax by themselves, but each carries penalties of about USD 10,000 or more for not filing, and the penalties apply even when no tax is owed:

| Form | Trigger, in short | Skill |
| --- | --- | --- |
| FBAR (FinCEN Form 114) | Foreign financial accounts above the aggregate threshold at any time in the year, including signature-only accounts; filed with FinCEN, not the IRS | `us-fbar-and-fatca-8938` |
| Form 8938 | Specified foreign financial assets above the thresholds for people living abroad; overlaps the FBAR but does not replace it | `us-fbar-and-fatca-8938` |
| Form 5471 | Officer, director or 10% shareholder of a foreign corporation | `us-form-5471-cfc-information` |
| Form 8621 | Any interest in a PFIC (most foreign funds) | Refer |
| Forms 3520 and 3520-A | Foreign trusts, and large gifts or inheritances from foreign persons | `us-foreign-trust-reporting` |
| Forms 8858 and 8865 | Foreign disregarded entities and partnerships | `us-form-8865-foreign-partnership` |

9. Foreign banks report US account holders to the IRS under FATCA, and some refuse US customers. Keep complete records.

### Step 4: the two traps that define expat planning

10. **PFICs: avoid foreign funds.** Almost any non-US pooled investment (a European UCITS ETF, a Gulf mutual fund, many insurance wrappers) is a passive foreign investment company. The default regime taxes gains at the top ordinary rate plus an interest charge, with a separate Form 8621 for each fund. The usual approach is to hold US-domiciled funds through a US broker that accepts clients living abroad, or individual shares. Refer any PFIC already held (R-ABROAD-PFIC).
11. **A foreign company: CFC rules.** A foreign corporation more than 50% owned by US shareholders is a CFC, and each 10% US shareholder includes its share of **net CFC tested income** (formerly GILTI) each year, as ordinary income at up to 37% with no credit for the company's foreign tax unless the **section 962 election** is made, plus subpart F income and a Form 5471. A 0% free-zone company gives an American founder little deferral. Options include the section 962 election, the high-tax exclusion (only where local tax is above 18.9%), a check-the-box election to treat the company as a pass-through, or trading as a sole proprietor. Computations: `us-gilti-fdii-beat`. An American should not form a foreign company without US advice first.

### Step 5: self-employment tax and totalization

12. US self-employment tax (15.3% up to the wage base, 2.9% above) follows a citizen abroad and is **not** reduced by the foreign earned income exclusion. Source: [IRS, Self-employment tax](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes); computation in `us-schedule-c-and-se-computation`.
13. **Totalization agreements** with about 30 countries (most of Europe, the UK, Japan, Australia, Canada and others) assign the person to one country's social security system; a certificate of coverage switches off US self-employment tax while the person pays into the local system, and credits in both systems can be combined. Source: [Publication 54](https://www.irs.gov/publications/p54) (IRS.gov/TotalizationAgreements).
14. **No agreement with the UAE or most of the Gulf:** a self-employed American there owes full US self-employment tax on worldwide net earnings, exclusion or not. That changes the employee or freelancer choice for Gulf moves.
15. US Social Security benefits stay payable abroad in most countries; years abroad without covered earnings add zeros to the 35-year average.

### Step 6: states that keep taxing leavers

16. Leaving the US does not by itself end state residence. Some states (California, Virginia, South Carolina and New Mexico are often cited) look at continuing ties such as a driver's licence, voter registration, property, a spouse, or a bank branch, and treat the person as still domiciled there. Sever ties affirmatively (licence exchanged, voter registration changed to federal-only overseas ballots, home sold or let at arm's length), keep the evidence, and expect a part-year return for the year of departure. Detail: `us-multi-state-residency-and-allocation`, `ca-residency-leaving-california`.

### Step 7: retirement accounts and pensions

17. **Keep the 401(k) or IRA.** Moving abroad does not end US deferral, and many treaties respect the wrapper; cashing out on departure triggers tax and, under age 59 and a half, the 10% additional tax.
18. **IRA contributions** need taxable compensation that is not excluded; the foreign earned income exclusion can remove eligibility, which is another reason the credit is often better in a high-tax country.
19. **Foreign pensions** (a UK SIPP, a German company pension, Swiss pillar 2 or 3) are, without treaty language, foreign accounts for US purposes: employer contributions and growth can be taxable each year, and some can be treated as foreign trusts or PFICs. The UK treaty is comparatively generous; many others are silent. Get the country answer before funding a local plan (R-ABROAD-PENSION).
20. **Roth conversions** in low-income years abroad (salary excluded, little other US income) can fill the low brackets each year.

### Step 8: the exit door: renunciation and the section 877A exit tax

21. **Five years of compliance first.** A person who cannot certify on Form 8854 that they met all federal tax obligations for the 5 years before expatriation is a covered expatriate automatically. Source: [Instructions for Form 8854](https://www.irs.gov/pub/irs-pdf/i8854.pdf).
22. **Covered expatriate tests:** any one of: average annual net income tax for the 5 years before expatriation of more than **USD 211,000** (2026); net worth of **USD 2,000,000** or more (not indexed); or failure to certify compliance. Narrow exceptions exist for some dual citizens from birth and some people who renounce before age 18 and a half. Source: [Rev. Proc. 2025-32, section 4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [26 U.S.C. 877(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877.htm); [26 U.S.C. 877A](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877A.htm).
23. **Mark-to-market:** a covered expatriate is treated as selling all property on the day before expatriation; the net gain is reduced by **USD 910,000** for 2026 (Case 2), with separate rules for deferred compensation, specified tax-deferred accounts and interests in non-grantor trusts. Source: [Rev. Proc. 2025-32, section 4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).
24. **Section 2801:** a US person who later receives gifts or bequests from a covered expatriate pays tax on them above **USD 19,000** a year (2026), at the highest estate and gift tax rate, so covered status also affects heirs. Source: [Rev. Proc. 2025-32, section 4.42](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).
25. **Mechanics:** an appointment at a US consulate, the State Department fee, the certificate of loss of nationality, and a final dual-status return with Form 8854. The computation is in `us-expatriation-exit-tax`.
26. **Planning order** for anyone near the USD 2,000,000 line: plan, then gift (the 2026 basic exclusion is in `us-estate-gift-706-709`), then become compliant, then renounce, over several years.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Moves abroad on 1 July 2026 | Physical presence test can be met with 330 full days in a 12-month period that straddles the years; exclusion prorated by qualifying days; Form 2350 if the test is not yet met at the due date |
| 329 full days abroad in every 12-month window | Physical presence test failed; consider bona fide residence |
| Only investment income abroad (dividends, gains, pension) | The exclusion does not apply; foreign tax credit only |
| Self-employed in a totalization country with a certificate of coverage | No US self-employment tax for that period |
| Self-employed in the UAE | Full US self-employment tax; the exclusion does not reduce it |
| Revoked the exclusion in 2025 | Cannot choose it again until 2030 without IRS consent |
| Green card holder moves abroad but keeps the card | Still a US resident for tax: worldwide income |
| Net worth exactly USD 2,000,000 at expatriation | Covered expatriate ("2,000,000 or more") |
| Non-US spouse | Election to file jointly (section 6013(g)) changes the return and the FBAR scope: `us-tax-residency` |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Days in the US | Do not claim the exclusion under the physical presence test until a day count exists |
| Foreign tax the client will pay | Model both the exclusion and the credit |
| Whether a foreign fund is a PFIC | Treat as a PFIC until shown otherwise |
| Whether prior FBARs and information returns were filed | Assume not, and review the last 6 years before planning anything else (R-ABROAD-BACK) |
| State ties | Assume the state still treats the person as resident until the ties are documented as cut |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| "I owe nothing, so I don't file" | The penalties attach to the forms, not the tax |
| A local index fund or insurance wrapper bought abroad | PFIC: punitive tax and one Form 8621 per fund |
| A free-zone company like everyone else's | CFC rules: current US tax and Form 5471 |
| A high earner relying on the exclusion in the Gulf | Income above USD 132,900 is fully taxed in the US |
| Freelancing in a country with no totalization agreement | 15.3% self-employment tax survives the exclusion |
| Leaving California without cutting ties | Residency audits reach back years |
| Cashing out the 401(k) on departure | Tax and the 10% additional tax for no reason |
| Renouncing while not compliant, or above USD 2,000,000 without planning | Covered expatriate: exit tax now, section 2801 tax on heirs later |

## Worked cases

Figures are invented; 2026 rates and thresholds are real.

**Case 1, a decision: exclusion or credit for a single employee moving to Dubai.** A single US citizen earns USD 200,000 of 2026 salary in Dubai (no UAE income tax), passes the physical presence test, and has no other income. Taxable income before any exclusion: 200,000 - 16,100 standard deduction = USD 183,900, tax USD 36,734. With the exclusion, the stacking rule taxes the income as if not excluded and subtracts the tax on the excluded USD 132,900 (USD 24,494): US tax USD 12,240. The foreign tax credit gives nothing because no UAE tax is paid. Choose the exclusion; the client still owes USD 12,240 (plus the housing exclusion may reduce it). Had the move been to Germany with German tax above the US tax, the credit would usually reduce the US tax to nil and keep the exclusion unused.

```oa-check
name: Foreign earned income exclusion with the stacking rule, Dubai (2026)
inputs:
  salary: 200000
  standard_deduction: 16100
  exclusion: 132900
steps:
  - taxable_income: salary - standard_deduction
  - tax_no_exclusion: 0.10 * min(taxable_income, 12400) + 0.12 * max(min(taxable_income, 50400) - 12400, 0) + 0.22 * max(min(taxable_income, 105700) - 50400, 0) + 0.24 * max(min(taxable_income, 201775) - 105700, 0)
  - tax_on_excluded: 0.10 * min(exclusion, 12400) + 0.12 * max(min(exclusion, 50400) - 12400, 0) + 0.22 * max(min(exclusion, 105700) - 50400, 0) + 0.24 * max(min(exclusion, 201775) - 105700, 0)
  - tax_with_exclusion: tax_no_exclusion - tax_on_excluded
  - saving: tax_no_exclusion - tax_with_exclusion
expected:
  taxable_income: 183900.00
  tax_no_exclusion: 36734.00
  tax_on_excluded: 24494.00
  tax_with_exclusion: 12240.00
  saving: 24494.00
```

**Case 2: the exit tax exclusion for a covered expatriate.** A US citizen with a net worth of USD 3,000,000 renounces in 2026. Her assets (no deferred compensation, no retirement accounts, no trust interests) have a built-in gain of USD 1,500,000 on the day before expatriation. She is a covered expatriate on the net worth test. The deemed-sale gain is reduced by USD 910,000, leaving USD 590,000 taxable on her final return, at the capital gain rates in `us-capital-gains`. With a net worth of USD 1,900,000, average net income tax below USD 211,000 and 5 years of certified compliance, she would not be covered and would have no deemed sale.

```oa-check
name: Section 877A exclusion for a covered expatriate (2026)
inputs:
  net_worth: 3000000
  built_in_gain: 1500000
  exclusion: 910000
  net_worth_test: 2000000
steps:
  - covered_by_net_worth: clamp(net_worth - net_worth_test + 1, 0, 1)
  - taxable_gain: max(built_in_gain - exclusion, 0) * covered_by_net_worth
expected:
  covered_by_net_worth: 1
  taxable_gain: 590000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-ABROAD-BACK | Missed FBARs, Forms 8938, 5471 or 3520, or unfiled returns | Refer: delinquency and streamlined filing procedures need a US international preparer |
| R-ABROAD-PFIC | Foreign funds already held | Refer: PFIC elections and Form 8621 |
| R-ABROAD-CFC | The client owns or will form a foreign company | `us-form-5471-cfc-information`, `us-gilti-fdii-beat`, and a US adviser before formation |
| R-ABROAD-PENSION | Foreign pension or insurance wrapper | Refer: treaty-by-treaty analysis |
| R-ABROAD-EXIT | Renunciation or giving up a long-held green card | `us-expatriation-exit-tax` and a specialist |
| R-ABROAD-STATE | A state residency dispute | The state skill and a state specialist |
| R-ABROAD-TREATY | A treaty claim to be a nonresident | `us-tax-residency`; Form 8833 |

## Filing and payment

- **2026 Form 1040** for a citizen living abroad on 15 April 2027: due **15 June 2027** under the automatic 2-month extension (interest from 15 April 2027); **15 October 2027** with Form 4868; Form 2350 for more time to meet the presence or residence test. Source: [Publication 54](https://www.irs.gov/publications/p54).
- **FBAR and Form 8938** dates: `us-fbar-and-fatca-8938`.
- **Form 8854** with the final dual-status return for the year of expatriation: `us-expatriation-exit-tax`.
- **Estimated tax** on income not covered by the exclusion or foreign tax: `us-quarterly-estimated-tax`.

## Completion checklist

- [ ] Status confirmed (citizen or green card) and the move date recorded.
- [ ] Shield chosen by destination (exclusion, credit or both), with Case 1 arithmetic for the client's figures.
- [ ] 330-day count or bona fide residence evidence on file.
- [ ] Every information return listed with its owner skill and due date.
- [ ] PFIC review of every foreign fund and wrapper.
- [ ] Any foreign company reviewed under the CFC rules before it is formed.
- [ ] Totalization agreement and certificate of coverage checked for self-employment.
- [ ] State ties cut and documented; part-year return planned.
- [ ] Retirement accounts left in place unless there is a reason.
- [ ] If renunciation is in view: 5-year compliance, net worth and average tax tested against 2026 figures.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.37 ($211,000), 4.38 ($910,000), 4.39 ($132,900), 4.42 ($19,000; $194,000 to a non-citizen spouse; section 2801 above $19,000), 4.47 ($20,573) and the standard deduction ($16,100). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 911 (govinfo). Read for the 330-day test, the 16% housing base and the section 911(f) stacking rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm | 2026-11-13 |
| 26 U.S.C. 877 (govinfo). Read for (a)(2)(B) net worth of "$2,000,000 or more". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877.htm | 2026-11-13 |
| 26 U.S.C. 877A (govinfo). Read for the deemed sale and the covered expatriate definition. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877A.htm | 2026-11-13 |
| Instructions for Form 2555 (2026). Read for the $132,900 exclusion, 330 full days, the $39,870 housing limit and revoking the choice. | https://www.irs.gov/pub/irs-pdf/i2555.pdf | 2026-11-13 |
| IRS Publication 54 (2025). Read for the June 15 automatic extension, Form 2350, totalization agreements and self-employment tax abroad. | https://www.irs.gov/publications/p54 | 2026-11-13 |
| Instructions for Form 8854. Read for the 5-year compliance certification. | https://www.irs.gov/pub/irs-pdf/i8854.pdf | 2026-11-13 |
| IRS, Self-employment tax. Read for the 15.3% rate. | https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes | 2026-11-13 |

Not yet confirmed: the 2026 Publication 54 was not published when read, so the extension and totalization statements come from the 2025 edition; the count of about 30 totalization agreements and the list of countries were not re-checked against the Social Security Administration page, which did not open for a scripted read; the State Department renunciation fee is not quoted because its current amount was not checked.
