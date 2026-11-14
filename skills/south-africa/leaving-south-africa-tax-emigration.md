---
name: leaving-south-africa-tax-emigration
description: >
  How a South African tax resident leaves the tax net, for the 2027 year of assessment (1 March 2026 to 28 February 2027). South Africa replaced financial emigration through the Reserve Bank with a tax-driven exit. Ceasing tax residency triggers a deemed disposal of worldwide assets the day before (section 9H, the exit charge), retirement annuity and preservation fund access waits for three uninterrupted years of non-residency, transfers abroad run through a SARS tax compliance status, and South Africans abroad who never ceased residency stay taxable on worldwide income, sheltered only by the R1.25 million foreign employment exemption. Covers the ordinarily resident and physical presence tests, the 330-day rule, the RAV01 declaration, the exit charge, what stays taxable after exit (dividends tax, interest withholding, the section 35A withholding on property sales, estate duty) and the order of steps.
version: 1.0
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "2026-27, the 2027 year of assessment (1 March 2026 to 28 February 2027)"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Leaving South Africa: tax emigration, the exit charge, and the three-year wait

**Why this corridor needs a guide.** South Africa's exit rules were rebuilt in 2021 and most emigrants' mental model has not caught up. **"Financial emigration" through the Reserve Bank no longer ends anything for tax.** SARS says it is "merely one factor" in deciding whether residence was broken. The modern exit is a **tax-residency** event with three parts: a **deemed disposal of worldwide assets** on the day before residency ends (the exit charge), a **three-year non-residency wait** before retirement annuity and preservation fund savings can be taken out, and a **SARS tax compliance gate** on moving money out. Meanwhile the largest group of all, South Africans abroad who never formally ceased residency, remain **taxable on worldwide income**, sheltered only by the R1.25 million foreign employment exemption that many misread as an exit.

## Who this applies to

- **Path A: stay resident and use the exemption.** A South African working abroad who stays ordinarily resident is taxed on worldwide income. Section 10(1)(o)(ii) exempts foreign employment remuneration, up to R1.25 million a year, where the day tests are met (see `za-foreign-employment-exemption`). Everything above the cap, and all non-employment income, stays taxable in South Africa with foreign tax credits. This suits secondments and probable returns. It is **not** an exit.
- **Path B: cease residency (tax emigration).** Break ordinary residence (or end physical-presence residence, or become treaty-resident elsewhere), declare the date to SARS, pay the exit charge, and South African tax narrows to South African source income. Most of this file is Path B.
- **The silent third group.** Left years ago, told nobody, stopped filing. SARS's starting point is that such a person may still be resident, with worldwide income undeclared. Regularising (choosing and evidencing a defensible cessation date and filing for it) is urgent, and doing it voluntarily beats doing it after a SARS letter.

Out of scope: the destination country's rules (UK, Australia, Netherlands, US, UAE and others have their own skills), estate planning beyond the estate duty figures, and exchange control limits for residents.

## Rates, bands and thresholds

| Item | Figure, 2026/27 | Source |
| --- | --- | --- |
| Maximum effective CGT rate for individuals on the deemed disposal | 18% | https://www.sars.gov.za/tax-rates/income-tax/capital-gains-tax-cgt/ |
| Annual CGT exclusion for individuals, YoA 2027 | R50,000 | same |
| Physical presence test: days present in the year of assessment | more than 91 days in aggregate | https://www.sars.gov.za/faq/faq-how-do-i-know-that-i-fall-within-the-definition-of-a-resident/lapd-intr-in-2012-04-resident-definition-natural-person-physical-presence/ |
| Physical presence test: each of the five preceding years | more than 91 days in aggregate in each | same |
| Physical presence test: the five preceding years together | more than 915 days in aggregate | same |
| Physical-presence resident ceases when continuously outside the Republic for | at least 330 full days | https://www.sars.gov.za/individuals/cease-to-be-an-sa-tax-resident-and-reinstatement-of-sa-tax-resident/ |
| Non-residency before full retirement annuity or preservation fund withdrawal | an uninterrupted period of three years or longer, on or after 1 March 2021 | https://www.sars.gov.za/guide-to-tax-directive-for-cease-to-be-resident-and-expiry-of-visa/ |
| Foreign employment exemption cap for those who stay resident | R1.25 million per year of assessment | https://www.sars.gov.za/individuals/tax-during-all-life-stages-and-events/foreign-employment-income-exemption/ |
| Dividends tax (final, withheld) | 20% | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ |
| Withholding tax on South African interest paid to non-residents (final) | 15% | same |
| Withholding on a non-resident's sale of South African immovable property (s 35A, credited against the final tax) | 7.5% individual, 10% company, 15% trust | same |
| Retirement fund lump sum withdrawal benefits, top rate | 36% above R 1,089,000 | same |
| Estate duty on residents' estates and non-residents' South African property | 20% on the first R30 million of dutiable value, 25% above R30 million | same |
| Estate duty basic deduction | R3.5 million | same |
| Interest on late or underpaid tax, from 1 March 2026 | 10.25% a year | same |
| Fixed administrative penalty for an outstanding return | R250 to R16,000 a month, by taxable income, up to 35 months | https://www.sars.gov.za/individuals/what-if-i-do-not-agree/admin-penalty/ |

## The base

### Ceasing residency: the tests

1. **Ordinarily resident**: the country of a person's real home, the place they return to from their wanderings. Breaking it is a factual enquiry: the person's intention to stop making South Africa their real home, supported by objective factors. SARS lists what it looks at: a foreign tax residence certificate; property still available in South Africa and its use; business interests (investment and employment) in South Africa; where the family lives and why; social ties and where personal belongings are; return visits, how often and why. If a person ceases to be ordinarily resident, it is from the day they ceased.
2. **Physical presence**: a day count for those who are not ordinarily resident (thresholds in the table). An ordinarily resident person cannot count days to leave. A physical-presence resident ceases when outside the Republic for a continuous period of at least 330 full days, from the day they left.
3. **Treaty override**: a person deemed exclusively resident of another country under a double tax agreement is excluded from the definition of "resident". SARS examines the substance behind a foreign residence certificate.

### The declaration

Cessation is declared on the **Registration, Amendments and Verification form (RAV01)** on eFiling, by capturing the date residency ceased under the Income Tax Liability Details section. SARS then opens a case and writes asking for supporting documents. The **date** fixes the exit charge valuation, starts the three-year retirement clock, and splits the year of assessment into a resident and a non-resident period.

### The exit charge (s 9H)

On the day **before** residency ends, the person is deemed to have disposed of their worldwide assets at market value and reacquired them. SARS states the deemed disposal covers worldwide assets **excluding immovable property situated in South Africa**, which stays in the South African net and is taxed when actually sold (with s 35A withholding when a non-resident sells). Cash has no gain. Retirement fund interests follow their own rules (the three-year wait).

Everything else is in: the offshore share portfolio, crypto, a foreign holiday home, a stake in a private company (South African or foreign).

- **Value everything on the date.** A defensible market-value schedule matters most for a private-company stake; SARS challenges cheap valuations, and its tax compliance status for transfers asks for the detailed CGT calculation on the deemed disposal under s 9H(2).
- **Liquidity beats surprise.** The charge is part of the return for the year residency ceased. A founder with a large paper gain and no cash should plan how to fund it.
- **The annual exclusion and capital losses** apply as in any CGT year; realising genuine losses in the exit year is legitimate arithmetic.
- **Timing against a sale.** Ceasing **before** a sale of a non-South African asset means growth after the cessation date, and the sale itself, fall outside South African CGT; ceasing **after** means real cash to pay a real bill. Model both and document the commercial reasons.

### What stays South African after exit

- South African source income: rent, South African employment and director days, South African interest (15% withholding unless exempt) and South African dividends (20% dividends tax, reducible under a treaty).
- South African immovable property: CGT on sale, with s 35A withholding on the price.
- Estate duty on the non-resident's South African property.
- Retirement annuity and preservation funds: see Cross-border points.

## Deadlines and filing

| Step | When | How |
| --- | --- | --- |
| Declare cessation | As soon as the date is settled | RAV01 on eFiling, Income Tax Liability Details, cessation date; then respond to the SARS case with documents |
| Return for the year residency ceased (split year, with the s 9H gain) | Individual filing season 2026 ran 13 July 2026 to 23 October 2026; provisional taxpayers have until 22 January 2027 | ITR12 on eFiling |
| Transfers abroad | Before moving funds | Tax compliance status (TCS) application with a statement of assets and liabilities for three years, proof of cessation with the date, and the s 9H(2) CGT schedule; non-residents not on the SARS register need a manual letter of compliance |
| Retirement annuity or preservation fund withdrawal | After three uninterrupted years of non-residency | Tax directive through the fund, reason "Cessation of South African Residence" |

## Penalties and interest

- An outstanding return attracts a fixed administrative penalty of R250 to R16,000 a month, set by taxable income, recurring each month for up to 35 months (s 210 of the Tax Administration Act). Filing the return stops further penalties. Disputes start with a Request for Remission.
- Late or underpaid tax carries interest at 10.25% a year from 1 March 2026.
- Understatement penalties for an undeclared exit charge or undeclared worldwide income are percentage-based and depend on behaviour; voluntary disclosure before SARS starts an audit reduces them. The percentages were not reread today (see Not yet confirmed).

## Cross-border points

- **Retirement savings wait three years.** Since 1 March 2021, full withdrawal from a retirement annuity or preservation fund on leaving needs **three uninterrupted years of non-residency**. From 1 September 2024 the SARB-recognised emigration route was deleted, and after three years a member can take the full value of the vested and retirement components. Per SARS: access to the savings component of any fund does not need the three years; the vested component of a pension or provident fund does not need it either; the vested component of a retirement annuity fund and the retirement component of any fund do. Withdrawals are taxed on the lump sum withdrawal table (top rate 36%). Pension paid as an annuity stays taxed in South Africa at source unless a treaty says otherwise; SARS runs a directive process for treaty relief on pension and annuity income.
- **Moving money out goes through SARS.** The old SARB financial-emigration channel is gone. Transfers need a SARS tax compliance status, which interrogates the asset base and residency status. Messy filings block the money.
- **Destination notes.** Moving to the UAE: the treaty tie-breaker is usually the exit route, and SARS audits the substance (home, days, family). Moving to the UK, Australia, the Netherlands or the US: these tax worldwide income, and an asset deemed disposed of for South African purposes does not automatically enter the new country at that value; check each side to avoid taxing the same gain twice and use the treaty. Each destination's arrival rules are in that country's skill.
- **Estate duty narrows but does not vanish.** A non-resident's South African property stays in the estate duty net (rates in the table).

### Trap list

| Trap | Why it bites |
| --- | --- |
| "I financially emigrated through my bank, I'm done" | SARS treats financial emigration as one factor only; only a ceased tax residence (with the exit charge) ends worldwide taxation |
| Living abroad for years, never told SARS | May still be resident: worldwide income assessable, and CRS data shows SARS the offshore accounts; the R1.25 million exemption covers only foreign employment remuneration |
| Treating R1.25 million as "tax-free abroad" | It is an exemption inside continued residency; investment income, remuneration above the cap and gains stay taxable |
| No valuation file at cessation | The exit charge keys off day-before market values; an undocumented private-company value invites SARS's own |
| Expecting the retirement annuity cash on arrival | Three uninterrupted years of non-residency first, then the lump sum table |
| Messy filings and a big transfer | The tax compliance status is a gate; arrears freeze the money |
| Selling South African property as a non-resident | s 35A withholding comes off the price at transfer; the refund waits for the return |
| Assuming emigration ends estate duty | South African property stays in the 20% and 25% net |

### Sequenced checklist

**Before the move**
1. Choose the path explicitly (exemption or emigration) and write down why.
2. Build the cessation-date evidence (home, family, intention) and choose the date.
3. Value worldwide assets for the day before; compute the s 9H charge; plan how to pay it; realise genuine losses.
4. Decide the South African property's fate (keep it: permanent South African filings and s 35A on a later sale).
5. Map retirement annuity, preservation and pension fund savings against the three-year clock.

**Cessation year**
6. Declare cessation on RAV01 and supply documents; file the split-year return with the s 9H gain; pay.
7. Update banks and brokers on tax residency (CRS) truthfully; get the tax compliance status ready for transfers.
8. Claim treaty relief at source on dividends and interest where it applies.

**After**
9. File South African returns only for South African source items; keep the compliance record clean.
10. Diarise the three-year date; before any South African property sale, brief the conveyancer on s 35A; revisit estate planning in both countries.

## Two worked examples that recompute

### Example 1: the exit charge on an offshore portfolio, YoA 2027

A resident ceases residency on 30 September 2026. On 29 September 2026 the offshore share portfolio is worth R3,500,000 against a base cost of R1,500,000: a deemed gain of R2,000,000. No other disposals that year; the person's other taxable income already puts them in the 45% band.

- Gain R2,000,000 less the 2027 annual exclusion R50,000 = R1,950,000.
- Taxable capital gain at the 40% inclusion rate: R780,000.
- Tax at 45%: **R351,000** (an effective 17.55% of the gain, below the 18% maximum because of the exclusion).

```oa-check
name: Exit charge, deemed gain R2,000,000, YoA 2027, 45% band
inputs:
  deemed_gain: 2000000
  annual_exclusion: 50000
  inclusion_rate: 0.40
  marginal_rate: 0.45
steps:
  - net_gain: deemed_gain - annual_exclusion
  - taxable_capital_gain: net_gain * inclusion_rate
  - exit_tax: taxable_capital_gain * marginal_rate
  - effective_rate: exit_tax / deemed_gain
expected:
  net_gain: 1950000.00
  taxable_capital_gain: 780000.00
  exit_tax: 351000.00
  effective_rate: 0.1755
```

### Example 2: decision, cease residency before or after selling a foreign company stake

A founder holds shares in a foreign company with a base cost of R1,000,000. Today they are worth R6,000,000 (gain R5,000,000). A sale in 18 months is expected at R9,000,000 (gain R8,000,000). Other income keeps them in the 45% band; the annual exclusion is R50,000.

- **Cease first, sell later:** South African tax only on the deemed gain at cessation: (5,000,000 - 50,000) x 40% x 45% = R891,000. The later growth of R3,000,000 falls outside South African CGT (the destination may tax it).
- **Sell first, then cease:** South African tax on the whole gain: (8,000,000 - 50,000) x 40% x 45% = R1,431,000.
- The figure that decides is the post-cessation growth times 18%: R540,000 of South African tax, weighed against the destination's tax on the same growth and the need for cash to pay the exit charge without a sale.

```oa-check
name: Cease before or after a sale, gain R5,000,000 now, R8,000,000 at sale
inputs:
  gain_at_cessation: 5000000
  gain_at_sale: 8000000
  annual_exclusion: 50000
  inclusion_rate: 0.40
  marginal_rate: 0.45
steps:
  - tax_cease_first: (gain_at_cessation - annual_exclusion) * inclusion_rate * marginal_rate
  - tax_sell_first: (gain_at_sale - annual_exclusion) * inclusion_rate * marginal_rate
  - difference: tax_sell_first - tax_cease_first
expected:
  tax_cease_first: 891000.00
  tax_sell_first: 1431000.00
  difference: 540000.00
```

## Ask the client first

1. Do you intend to stop living in South Africa for good, and what is the evidence (home, family, job, school, belongings, visas)?
2. Were you ordinarily resident, or resident only under the physical presence test?
3. Are you, or will you be, treaty-resident in another country, and which one?
4. What do you own worldwide, at what base cost, and what is it worth now (especially private-company shares and crypto)?
5. Do you keep South African property, retirement annuities, preservation funds or pension funds?
6. Have you filed every South African return to date, including since leaving?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| SARS, Cease to be an SA Tax Resident and Reinstatement page: read for the ordinarily resident factors, the 330 full day rule, the treaty override, the s 9H deemed disposal excluding South African immovable property, and the RAV01 declaration steps | https://www.sars.gov.za/individuals/cease-to-be-an-sa-tax-resident-and-reinstatement-of-sa-tax-resident/ | 2026-11-14 |
| SARS, Foreign Employment Income Exemption page: read for "financial emigration is merely one factor", the R1.25 million cap and the 183 and 60 day tests | https://www.sars.gov.za/individuals/tax-during-all-life-stages-and-events/foreign-employment-income-exemption/ | 2026-11-14 |
| SARS Interpretation Note 4 (Issue 5), physical presence test: read for para 4 (91 days in the year and in each of the five preceding years, 915 days in aggregate) | https://www.sars.gov.za/faq/faq-how-do-i-know-that-i-fall-within-the-definition-of-a-resident/lapd-intr-in-2012-04-resident-definition-natural-person-physical-presence/ | 2026-11-14 |
| SARS, Guide to Tax Directive for Cease to be Resident and Expiry of Visas: read for the three-year uninterrupted non-residency rule from 1 March 2021, the 1 September 2024 changes and the directive reason codes | https://www.sars.gov.za/guide-to-tax-directive-for-cease-to-be-resident-and-expiry-of-visa/ | 2026-11-14 |
| SARS, Supporting Documents for Approval of International Transfers: read for the TCS documents for non-residents (cessation proof, the s 9H(2) CGT schedule, three years of assets and liabilities) and which fund components need three years | https://www.sars.gov.za/individuals/manage-your-tax-compliance-status/supporting-documents-for-obtaining-approval-international-transfers/ | 2026-11-14 |
| SARS, Capital Gains Tax (CGT) rate page: read for the 18% maximum effective rate and the R50,000 annual exclusion for 2027 | https://www.sars.gov.za/tax-rates/income-tax/capital-gains-tax-cgt/ | 2026-11-14 |
| SARS, Budget Tax Guide 2026: read for dividends tax 20%, interest withholding 15%, s 35A 7.5%, 10%, 15%, the lump sum withdrawal table, estate duty 20% and 25% with R30 million step and R3.5 million deduction, and interest at 10.25% from 1 March 2026 | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ | 2026-11-14 |
| SARS, Admin Penalty page: read for the R250 to R16,000 monthly fixed penalty, the 35-month maximum and the Request for Remission | https://www.sars.gov.za/individuals/what-if-i-do-not-agree/admin-penalty/ | 2026-11-14 |
| SARS, Filing Season page: read for the 2026 individual filing season (13 July to 23 October 2026, provisional taxpayers to 22 January 2027) | https://www.sars.gov.za/types-of-tax/personal-income-tax/filing-season/ | 2026-11-14 |

Not yet confirmed: the other exclusions from the s 9H deemed disposal (for example assets of a South African permanent establishment and certain share and retirement rights) were not reread in the Act; only the South African immovable property exclusion is stated on the SARS page. The understatement penalty percentages under the Tax Administration Act were not reread today. The earlier version of this file said the South Africa and UAE treaty cuts dividends tax to 10% and 5%: the treaty text was not opened today, so that figure is removed until it is read.

---
*Built for the OpenAccountants migration desk. South Africa's modern exit is honest about its price: one valuation day, one charge, three waiting years, and a compliance record that becomes the passport for every rand that follows you. The people who suffer on this corridor are almost never the ones who declared; they are the ones who assumed leaving was something that happened to them.*
