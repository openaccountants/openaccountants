---
name: hu-capital-and-rental-income
description: "Hungarian personal income tax on capital income, rental income and the sale of real estate for private individuals, and the annual return (szja bevallás) and NAV's return proposal (bevallási tervezet), tax year 2026. Covers interest (65. §) and dividends (66. §) at 15%; the 13% social contribution tax (szocho) on them and the HUF 7,747,200 cap that applies to dividends but not interest, capital gains on securities (67. §), controlled capital market transactions (67/A. §) and their three-year loss offset, long-term investment accounts (TBSZ, 67/B. §: 0%, 10%, 15%), the NYESZ pension savings credit, rental income (16.-17. §) with the 10% flat cost or itemised costs and no szocho, real estate sales (62.-63. §) with the holding-period reduction, and the 20 May deadline. Triggers: kamatadó, osztalékadó, szocho kamat, TBSZ, NYESZ, árfolyamnyereség, lakáskiadás adó, ingatlan bérbeadás, ingatlaneladás adó, bevallási tervezet, szja bevallás. Out of scope: hu-income-tax (self-employed), hu-payroll (wages), hu-social-contributions, hu-cross-border."
version: 0.1
jurisdiction: HU
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary: capital income, rental income and the annual return for individuals (2026)

> **General reference only.** A source-cited draft, not reviewed by an accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Hungary.

Hungary taxes a private individual's investment and property income under the personal income tax act, 1995. évi CXVII. törvény ("Szja tv."), and adds the social contribution tax under 2018. évi LII. törvény ("Szocho tv."). Procedure and penalties are in 2017. évi CL. törvény ("Art."). All three were read on 2026-10-23 in the consolidated text on the Nemzeti Jogszabálytár (njt.jog.gov.hu), state of 2026-10-01. The tax authority is the Nemzeti Adó- és Vámhivatal (NAV). Amounts are in forint (HUF). The tax year is the calendar year.

See also, in this pack: `hu-income-tax` (sole traders: átalányadó, vállalkozói szja, KATA), `hu-payroll` (wages, the family allowance and the other allowances that reduce the consolidated base), `hu-social-contributions` (TB and szocho for the self-employed), `hu-cross-border` (residence, withholding on payments to non-residents, the foreign tax credit). This skill does not repeat them.

## Who this applies to

- **Resident individuals** on their worldwide interest, dividends, gains and rents, and **non-residents** on Hungarian-source income. Residence rules are in `hu-cross-border` (Szja tv. 3. § 2.-3.). Income from letting or selling real estate is sourced where the property lies (Szja tv. 3. § 4. c)).
- **Private individuals, not sole traders.** A person who lets property as a registered sole trader (egyéni vállalkozó) and does not opt for the private-person rules is taxed under `hu-income-tax`. Bank interest credited to a sole trader's registered business account is business income, not interest income (Szja tv. 65. § (3) b) ba)).
- **Employees and pensioners** who need to check or complete NAV's return proposal: the annual return section below applies to them.
- **Two kinds of tax in this skill.**
  1. *Separately taxed income (külön adózó jövedelem):* interest, dividends, capital gains, controlled capital market transactions, TBSZ yield, real estate sales. Each is taxed on its own at a flat rate. Personal allowances do not reduce it.
  2. *The consolidated base (összevont adóalap):* rental income is income from independent activity (önálló tevékenység) and joins wages and other such income in one base (Szja tv. 16. § (1), 29. §). Allowances such as the family allowance can reduce it (see `hu-payroll`).
- **Out of scope:** short-term holiday letting under the itemised flat tax for private accommodation (tételes átalányadó, Szja tv. 57/A. § and 8. számú melléklet), farmland letting (Szja tv. 73. §), crypto-asset gains (Szja tv. 67/C. §), and trading as a business.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal income tax rate, unless the act says otherwise | 15% of the base | 2026 | Szja tv. 8. § (1), https://njt.jog.gov.hu/jogszabaly/1995-117-00-00 |
| Interest income (kamatjövedelem) | 15% szja; the payer (bank, investment firm) withholds | 2026 | Szja tv. 8. § (1), 65. § (2) |
| Interest on Hungarian state retail bonds (lakossági állampapír) | Not income: no szja and no szocho | 2026 | Szja tv. 65. § (3) a) ab); NAV information sheet 49 |
| Dividend (osztalék) | 15% szja; the paying company withholds | 2026 | Szja tv. 8. § (1), 66. § (3) |
| Capital gain on securities outside a controlled transaction (árfolyamnyereség) | 15% szja | 2026 | Szja tv. 8. § (1), 67. § |
| Controlled capital market transactions (ellenőrzött tőkepiaci ügylet) | 15% szja on the net gain of the year; no szocho | 2026 | Szja tv. 67/A. § (1); Szocho tv. 1. § (5) |
| TBSZ long-term investment account (tartós befektetés) | 0% szja after the five-year period; 10% if closed at the end of the three-year period or broken in years four and five; 15% if broken within three years | 2026 | Szja tv. 67/B. § (5) |
| TBSZ minimum first deposit | HUF 25,000 | 2026 | Szja tv. 67/B. § (2) |
| Szocho on interest, dividends, capital gains (67. §) | 13% | 2026 | Szocho tv. 1. § (5) c), d), f), 2. § (1), https://njt.jog.gov.hu/jogszabaly/2018-52-00-00 |
| Szocho on TBSZ yield (contracts made or renewed after 31 December 2024) | 0% after five years; 8% at three to five years; 13% under three years. A TBSZ made before 1 January 2025 and not renewed bears no szocho | 2026 | Szocho tv. 1. § (5) g), 2. § (1a), 36/I. § (1) |
| Szocho cap (adófizetési felső határ) | 24 times the monthly minimum wage: 24 x HUF 322,800 = HUF 7,747,200. Applies to dividends and 67. § gains (with wages and other consolidated income counted first). Does **not** apply to interest or TBSZ yield | 2026 | Szocho tv. 2. § (2); 426/2025. (XII. 23.) Korm. rendelet 2. § (1), https://njt.jog.gov.hu/jogszabaly/2025-426-20-22; NAV information sheet 49, section 2 |
| Szocho on dividends of securities listed on an EEA regulated market | Exempt | 2026 | Szocho tv. 5. § (3) |
| Szocho on rental income | None | 2026 | Szocho tv. 5. § (2) h); NAV information sheet 10 |
| Rental income: flat cost (10 százalék költséghányad) | Income = 90% of rent received | 2026 | Szja tv. 17. § (3) b) |
| Rental income: quarterly advance | 15%, by the 12th of the month after the quarter, once the year's total due passes HUF 10,000 | 2026 | Szja tv. 46. § (9) |
| Real estate sale: share of the computed gain that is taxable | Year of purchase and next year 100%; 2nd year after 90%; 3rd 60%; 4th 30%; 5th and later 0% | 2026 | Szja tv. 62. § (4) |
| Real estate sale: purchase cost unknown | Revenue reduced by 75%, no other costs | 2026 | Szja tv. 62. § (3) |
| Real estate sale: tax | 15%, self-assessed in the return | 2026 | Szja tv. 63. § (1); NAV information sheet 9, section 8 |
| NYESZ pension savings account credit | 20% of payments in the year, up to HUF 100,000 (HUF 130,000 for someone who reached pension age before 1 January 2020) | 2026 | Szja tv. 44/B. § (1) |
| NYESZ non-pension withdrawal | Credits already paid back with a 20% uplift; the gain over payments is other income | 2026 | Szja tv. 44/B. § (4), 28. § (17) |
| Annual return and payment deadline | 20 May 2027 for tax year 2026 | 2026 | Szja tv. 12/C. § (4), (6), 63. § (1); NAV information sheet 9, section 8 |
| NAV return proposal (bevallási tervezet) available | From 15 March 2027 | 2026 | Szja tv. 12/C. § (1) |
| Failure-to-file penalty (mulasztási bírság), individual | Up to HUF 400,000 | 2026 | Art. 220. § (1), https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 |
| Tax penalty (adóbírság) | 50% of the shortfall; 200% where income was hidden or records falsified | 2026 | Art. 215. § (3), (4) |
| Late payment interest (késedelmi pótlék) | Central bank base rate plus 5 percentage points, divided by 365, per day. With the base rate at 5.50% (unchanged by the MNB Monetary Council on 20 October 2026), 10.50% a year | 2026 | Art. 209. § (1); MNB press release of 20 October 2026, https://www.mnb.hu/en/monetary-policy/the-monetary-council/press-releases/2026/press-release-on-the-monetary-council-meeting-of-20-october-2026 |
| Self-revision surcharge (önellenőrzési pótlék) | Central bank base rate divided by 365, per day (5.50% a year at the 20 October 2026 rate); 1.5 times on a repeat self-revision of the same return | 2026 | Art. 212. § (1), (1a); MNB press release of 20 October 2026 |
| Szocho cap declared but not reached | Szocho due with a 6% uplift, in the annual return | 2026 | Szocho tv. 29. § (2) |

## The taxable base

**Interest (Szja tv. 65. §).** Interest credited on a bank deposit or payment account (only the part up to a market rate), interest and yield on publicly offered debt securities and investment funds, and the gain on redeeming or selling them (computed like a capital gain), plus the excess of some insurance payouts over premiums. Interest on Hungarian state retail bonds is not income (65. § (3) a) ab)). Single-premium insurance: no interest income after five years, half after three; regular-premium: none after ten years, half after six (65. § (3) a) ac)-ad)). A Hungarian payer withholds the 15% (65. § (2) a)); foreign interest is self-assessed in the return (65. § (2) b)).

**Szocho on interest.** 13% on the same base, with no cap (Szocho tv. 1. § (5) f), 2. § (2)). It applies to deposit interest for periods after 30 June 2023 and to securities bought from 1 July 2023 (NAV information sheet 49; Szocho tv. 36/H. §). Interest from real estate fund units is outside it. The bank withholds it with the szja; for foreign interest the individual pays it with the szja in the return.

**Dividends (Szja tv. 66. §).** The whole dividend is income, including an interim dividend and dividends under foreign law. A Hungarian company withholds the 15% at payment (66. § (3)). A foreign dividend paid through a Hungarian bank or broker is withheld by that bank or broker; otherwise the individual self-assesses it in the return and credits the foreign tax (Szja tv. 8. § (2); see Cross-border points).

**Szocho on dividends and on 67. § gains.** 13%, until the individual's income for the year counted towards the cap reaches HUF 7,747,200 (Szocho tv. 2. § (2)). What counts towards the cap: income under Szocho tv. 1. § (1)-(3), which includes wages and other consolidated-base income, plus withdrawals from a business, securities lending income, dividends, 67. § gains and 1/B. § performer income (1. § (5) a)-e)). Interest and TBSZ yield never count and are never capped (NAV information sheet 49, section 2). The payer withholds 13% until the individual declares in writing that the cap has been reached; an individual who declares that the cap *will* be reached but then falls short pays the shortfall plus 6% in the return (29. § (1)-(2)). Overpaid szocho is reclaimed in the return (29. § (3)). Dividends on securities listed on an EEA regulated market carry no szocho at all (5. § (3)).

**Capital gains on securities (Szja tv. 67. §).** Sale proceeds less the purchase price and incidental costs (fees, duty, brokerage) (67. § (1), (9)). The payer withholds on its own figures; the individual can claim costs the payer did not use in the return (67. § (5)-(6)). Szocho 13% applies, within the cap. Typical case: selling shares in a private Kft. or Zrt.

**Controlled capital market transactions (Szja tv. 67/A. §).** Trades through or with an investment firm in financial instruments (not privately placed securities), commodities or spot currency that are either supervised by the Hungarian supervisor (MNB), or made with a firm in an EEA state, an OECD state or a treaty state, supervised there, with information exchange between that supervisor and the MNB where the state is outside the EEA, and for which the individual holds the broker's statement of every trade in the year (67/A. § (3) a)-b)). Most trades in listed shares, ETFs and derivatives through a regulated broker fall here. The income is the year's total gains less total losses and broker fees (67/A. § (1)). The broker issues a statement by 15 February (67/A. § (3a)). The individual self-assesses the 15% in the return (67/A. § (5)). No szocho: 67/A. § income is not in Szocho tv. 1. § (5).

**Loss offset (adókiegyenlítés).** A net loss from controlled transactions in the tax year or either of the two previous years, shown in the return for the year it arose, gives a credit equal to loss x the current rate, limited to the 67/A. § tax declared in the tax year and the two previous years, less credits already used (67/A. § (6)-(8)). In effect: losses offset gains of the same three-year window. Losses cannot offset dividends, interest or wages.

**TBSZ, long-term investment account (Szja tv. 67/B. §).** The individual signs a TBSZ contract with a bank or investment firm and pays in at least HUF 25,000 in one calendar year. The deposit is locked for the three calendar years after the year of payment, and can be extended by two more (67/B. § (2)). Interest, gains and dividends inside are not taxed as they arise. At the end, the yield (value less deposits) is taxed at 0% after five years, 10% after three, 15% if broken earlier (67/B. § (5)). Szocho is 0%, 8% or 13% for contracts made or renewed after 31 December 2024 (Szocho tv. 2. § (1a), 36/I. § (1)); a contract made before 2025 and not renewed bears no szocho, because 1. § (5) g) applies only to the later contracts (36/I. § (1)). Yield taxed at 0% need not be declared; otherwise the individual self-assesses it in the return (67/B. § (7)). A TBSZ can move between providers without breaking the lock (67/B. § (11)).

**NYESZ, pension savings account.** Payments earn a 20% credit from the consolidated-base tax, up to HUF 100,000 a year (Szja tv. 44/B. § (1)); the individual claims it in the return and NAV pays it into the account. A non-pension withdrawal means: no credit that year, repayment of credits already received plus 20%, and tax on the gain above payments as other income (44/B. § (4), 28. § (17)). Converting the whole NYESZ into a TBSZ avoids the other-income charge, but the credits paid for the conversion year and the year before are still repaid with a 20% uplift, and no credit can be claimed for the conversion year (44/B. § (5)).

**Rental income (Szja tv. 16.-18. §).** Letting is an independent activity (16. § (1)). Rent received is revenue. Utility charges passed to the tenant in proportion to use are not revenue; a fixed all-in rent or shared building charges (közös költség) are (17. § (3a); NAV information sheet 10, section 2). Two ways to reach income (17. § (3)):
1. **10% flat cost:** income is 90% of revenue. No receipts needed. Depreciation for the period is deemed claimed (18. § (3)). An individual who used the flat cost for the advances can still itemise in the return, provided the flat cost is not used for any independent-activity income that year (47. § (3)).
2. **Itemised costs (tételes költségelszámolás):** documented costs of the letting under the 3. számú melléklet, plus depreciation and renovation costs of property used only for letting under the 11. számú melléklet, up to the revenue (17. § (3) a) ab)).
The method chosen applies to **all** of the individual's independent-activity income that year (18. § (2)). An individual who rents a flat in another town for more than 90 days can deduct that rent from rent received on their own flat (17. § (5)). Rental income joins the consolidated base and is taxed at 15%. There is no szocho on it (Szocho tv. 5. § (2) h)).

**Sale of real estate (Szja tv. 62.-63. §).** Computed amount (számított összeg) = revenue less the purchase price and related costs, value-adding investments and the costs of the sale (62. § (1)-(2)). Without a provable purchase price, revenue less 75% (62. § (3)). The taxable income is a share of the computed amount by year of purchase: 100% in the year of purchase and the year after, 90% in the second year after, 60% in the third, 30% in the fourth, 0% from the fifth (62. § (4)). For a 2026 sale: bought in 2021 or earlier, no tax (NAV information sheet 9, section 7.3). The same scale applies to homes, holiday homes and land. If the sale is a business activity, the income is independent-activity income instead (62. § (3a)). No szocho: real estate income is not listed in Szocho tv. 1. § (5).

## Deadlines and filing

- **Withheld at source:** Hungarian banks, brokers and companies withhold szja and szocho on interest, dividends and 67. § gains, and pay by the 12th of the following month (Szja tv. 65. § (2), 66. § (3); NAV information sheet 49). Withheld interest need not be declared (Szja tv. 11. § (3) e)).
- **Rental advances:** a tenant that is a company or other payer (kifizető) withholds a 15% advance monthly; the landlord may declare costs to it up to 50% of the rent, otherwise 90% of the rent is the advance base (Szja tv. 47. § (2) a) aa); NAV information sheet 10, section 4.1). A tenant who is a private person withholds nothing: the landlord pays a 15% advance by 12 April, 12 July, 12 October and 12 January, once the year's total exceeds HUF 10,000 (Szja tv. 46. § (9); NAV information sheet 10, section 4.2).
- **Registration:** a private landlord whose only activity is VAT-exempt letting, who is not a sole trader and needs no EU VAT number, does not need a tax number (NAV information sheet 10, section 1.2).
- **NAV return proposal (bevallási tervezet):** built from payer data received by the end of February (Szja tv. 12/B. §), available in eSZJA from 15 March (12/C. § (1)). If the individual does nothing by 20 May, the proposal becomes the return (12/C. § (6)). Sole traders, primary producers and VAT-registered individuals must submit actively (12/C. § (7)).
- **What the proposal misses:** income not reported by a Hungarian payer. The individual must add: rent from private tenants, foreign interest and dividends, real estate sales, 67/A. § results (NAV pre-fills the broker totals, 67/A. § (5a)), TBSZ yield taxed at 10% or 15%, szocho on self-assessed income, the NYESZ credit claim, and any szocho overpaid above the cap.
- **Annual return (form 26SZJA for tax year 2026):** due 20 May 2027 (Szja tv. 12/C. § (4); NAV information sheet 9, section 8). Self-assessed szja and szocho are paid by the same date (Szja tv. 63. § (1), 67/A. § (5); Szocho tv. 27. §).
- **Late notice:** an individual with no business activity who, through no fault of their own, lacks the documents can notify NAV before 20 May; no failure-to-file penalty until 20 November (Szja tv. 11/A. §).
- **Records:** keep contracts and certificates until the assessment period ends; for 2026 income, 31 December 2032 (NAV information sheet 9, section 8).

## Penalties and interest

- **Late or missing return:** mulasztási bírság up to HUF 400,000 for an individual (Art. 220. § (1)). None if the delay is excused (220. § (3)) or after a valid late notice (Szja tv. 11/A. § (2)).
- **Tax shortfall found by NAV:** adóbírság of 50% of the shortfall; 200% where income was hidden or records falsified (Art. 215. § (3)-(4)). Half the penalty is waived if the individual waives appeal and pays by the due date (Art. 216. §).
- **Late payment:** késedelmi pótlék at the central bank base rate plus 5 percentage points a year, charged daily (Art. 209. § (1)).
- **Self-revision (önellenőrzés):** önellenőrzési pótlék at the base rate, daily; 1.5 times for a repeat revision of the same return (Art. 212. §). None if the error came from a wrong payer certificate (Art. 211. § (3) a)).
- **Szocho cap declared too early:** the shortfall plus 6% (Szocho tv. 29. § (2)).
- **Rental cost declaration to a paying tenant:** if the itemised costs in the return are lower than the costs declared to the payer for the advance, a 12% különbözeti bírság on the difference, declared and paid with the return; none if the difference is HUF 10,000 or less (Szja tv. 48. § (4) a), text in force from 1 January 2026). NAV information sheet 10, section 4.1 (3 February 2026) still says 39%; the act says 12%.
- **NYESZ non-pension withdrawal:** repay credits plus 20% (Szja tv. 44/B. § (4) b)).

## Cross-border points

- **Foreign interest and dividends of a resident:** self-assessed at 15%, plus 13% szocho (the szocho base is the part taxable in Hungary, Szocho tv. 1. § (5)). Foreign tax paid is credited against the szja; without a treaty, the Hungarian tax after credit cannot fall below 5% of the base (Szja tv. 8. § (2)). No advance on income from a non-treaty state (Szja tv. 46. § (2) e)).
- **Foreign brokers:** trades through a broker supervised in an EEA state, an OECD state or a treaty state are controlled transactions if, outside the EEA, that supervisor exchanges information with the MNB, and the individual holds the broker's statement of every trade in the year (Szja tv. 67/A. § (3) b)). Otherwise each gain is a 67. § capital gain with szocho.
- **Non-residents receiving Hungarian interest or dividends:** the payer withholds 15%, or the treaty rate if it holds a residence certificate and beneficial owner statement before payment; excess tax is refunded by NAV (Szja tv. 7. számú melléklet 2.-4., 6.-7.). Details are in `hu-cross-border`.
- **Szocho and foreign insurance:** a person insured in another EU state under the coordination regulations, proved by an A1 or similar certificate, pays no szocho (Szocho tv. 5. § (4)). A person who is "foreign" under the Tbj. pays no szocho on interest, dividends, gains, withdrawals or TBSZ yield (5. § (6) a)).
- **Real estate:** Hungarian property is taxed in Hungary wherever the owner lives (Szja tv. 3. § 4. c)). For a resident selling property in a state with no treaty, the gain over purchase cost is other income (Szja tv. 28. § (16)).

## Worked examples

**Example 1: bank interest and a dividend, with the szocho cap.** Anna is a Hungarian resident employee. In 2026 her wages are HUF 6,000,000. Her bank credits HUF 1,000,000 interest on a deposit opened in 2025. In June 2026 her Kft., not listed, pays her a HUF 3,000,000 dividend.

The bank withholds 15% szja, HUF 150,000, and 13% szocho, HUF 130,000. Interest has no cap, so the full HUF 1,000,000 bears szocho.

The Kft. withholds 15% szja on the dividend, HUF 450,000. For szocho, the cap is 24 x HUF 322,800 = HUF 7,747,200. Wages count first: HUF 6,000,000. Only HUF 1,747,200 of the dividend is under the cap, so her true szocho on it is 13% of HUF 1,747,200 = HUF 227,136. Unless she declared to the Kft. that she would reach the cap, it withholds 13% of the whole HUF 3,000,000, HUF 390,000. She reclaims HUF 162,864 in her 2026 return, due 20 May 2027 (Szocho tv. 29. § (3), (4)). The return computes it the way the 25SZJA guide does for 2025: the year's wages, then the dividend up to the cap (NAV 25SZJA kitöltési útmutató, lines 286-290). If she uses NAV's proposal, she checks that it shows the refund before accepting it. Total tax on the capital income: HUF 957,136.

If the dividend came from shares listed on an EEA regulated market, there would be no szocho on it at all (Szocho tv. 5. § (3)).

```oa-check
name: HU capital income 2026, interest and unlisted dividend with the szocho cap
inputs:
  wages: 6000000
  interest: 1000000
  dividend: 3000000
  minimum_wage: 322800
  szja_pct: 15
  szocho_pct: 13
steps:
  - szja_interest: pct(interest, szja_pct)
  - szocho_interest: pct(interest, szocho_pct)
  - szja_dividend: pct(dividend, szja_pct)
  - szocho_cap: minimum_wage * 24
  - room_under_cap: max(szocho_cap - wages, 0)
  - dividend_szocho_base: min(dividend, room_under_cap)
  - szocho_dividend: pct(dividend_szocho_base, szocho_pct)
  - szocho_withheld_on_dividend: pct(dividend, szocho_pct)
  - szocho_refund: szocho_withheld_on_dividend - szocho_dividend
  - total_tax: szja_interest + szocho_interest + szja_dividend + szocho_dividend
expected:
  szja_interest: 150000
  szocho_interest: 130000
  szja_dividend: 450000
  szocho_cap: 7747200
  room_under_cap: 1747200
  szocho_dividend: 227136
  szocho_refund: 162864
  total_tax: 957136
```

**Example 2: a flat let for HUF 250,000 a month with the 10% flat cost.** Bence lets his Budapest flat to a private tenant for all of 2026 at HUF 250,000 a month. The tenant pays the utilities to the providers directly. Bence has no other independent-activity income and chooses the 10% flat cost.

Revenue is HUF 3,000,000. Income is 90%: HUF 2,700,000. It joins his wages in the consolidated base and is taxed at 15%: HUF 405,000. No szocho. The tenant is a private person, so Bence pays the advances himself: each quarter's rent is HUF 750,000, income HUF 675,000, advance HUF 101,250, due 12 April, 12 July, 12 October 2026 and 12 January 2027. He declares the rent in his 2026 return by 20 May 2027; the NAV proposal will not contain it.

Edge cases: the flat cost equals HUF 300,000 of deemed costs. If his documented costs plus depreciation of the flat exceed HUF 300,000, itemising gives a lower tax, and he can switch to itemised costs in the return (Szja tv. 47. § (3)). If the tenant were a company, it would withhold the advance each month: 15% of 90% of HUF 250,000, HUF 33,750 (NAV information sheet 10, section 4.1).

```oa-check
name: HU rental income 2026, flat at HUF 250,000 a month, 10% flat cost
inputs:
  monthly_rent: 250000
  months: 12
  flat_cost_pct: 10
  szja_pct: 15
steps:
  - revenue: monthly_rent * months
  - deemed_cost: pct(revenue, flat_cost_pct)
  - income: revenue - deemed_cost
  - szja: pct(income, szja_pct)
  - quarterly_income: (monthly_rent * 3) - pct(monthly_rent * 3, flat_cost_pct)
  - quarterly_advance: pct(quarterly_income, szja_pct)
  - company_tenant_monthly_withholding: pct(monthly_rent - pct(monthly_rent, flat_cost_pct), szja_pct)
expected:
  revenue: 3000000
  deemed_cost: 300000
  income: 2700000
  szja: 405000
  quarterly_advance: 101250
  company_tenant_monthly_withholding: 33750
```

## Ask the client first

1. Are you tax resident in Hungary, and are you insured in Hungary or in another EU state (A1 certificate)? This decides whether szocho applies at all.
2. What were your wages and other consolidated-base income for the year? This sets how much of a dividend or 67. § gain stays under the HUF 7,747,200 szocho cap.
3. Which broker or bank holds your investments, in which country, and is anything inside a TBSZ or NYESZ? This decides between 67. § and 67/A. §, and whether yield is taxed now or at the end of the lock.
4. Is the dividend from a company listed on an EEA regulated market, and when did you fix each deposit or buy each bond or fund unit? Listed dividends, fixed-term deposits placed before 1 July 2023 and securities bought before that date carry no szocho on their interest.
5. For a letting: is the tenant a person or a company, do you have documented costs above 10% of the rent, and do you have other independent-activity income that would be bound by the same method choice?
6. For a property sale: when and for how much was it bought, what was spent on value-adding works, and was the sale part of a business?

## Sources

| Source | URL | Read on |
|---|---|---|
| 1995. évi CXVII. törvény a személyi jövedelemadóról (Szja tv.), state 2026-10-01: 3. §, 8. §, 11.-12/C. §, 16.-18. §, 28. §, 44/B. §, 46.-48. §, 57/A. §, 62.-63. §, 65.-67/B. §, 7. számú melléklet (annex read via the njtGetBlock service) | https://njt.jog.gov.hu/jogszabaly/1995-117-00-00 | 2026-10-23 |
| 2018. évi LII. törvény a szociális hozzájárulási adóról (Szocho tv.), state 2026-10-01: 1. §, 2. §, 5. §, 27. §, 29. §, 36/I. § | https://njt.jog.gov.hu/jogszabaly/2018-52-00-00 | 2026-10-23 |
| 2017. évi CL. törvény az adózás rendjéről (Art.), state 2026-10-01: 209.-212. §, 215.-216. §, 220. § | https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 | 2026-10-23 |
| Magyar Nemzeti Bank, press release on the Monetary Council meeting of 20 October 2026 (base rate 5.50%) | https://www.mnb.hu/en/monetary-policy/the-monetary-council/press-releases/2026/press-release-on-the-monetary-council-meeting-of-20-october-2026 | 2026-10-23 |
| NAV, kitöltési útmutató a 25SZJA jelű bevalláshoz (szocho cap, lines 286-292) | https://nav.gov.hu/pfile/file?path=%2Fnyomtatvanyok%2Fletoltesek%2Fnyomtatvanykitolto_programok%2Fnyomtatvanykitolto_programok_nav%2F25SZJA%2F25szja-kitoltesi-utmutato | 2026-10-23 |
| 426/2025. (XII. 23.) Korm. rendelet, 2026 minimum wage, 2. § (1) | https://njt.jog.gov.hu/jogszabaly/2025-426-20-22 | 2026-10-23 |
| NAV information sheet 10, Ingatlan bérbeadásának és egyéb hasznosításának adózása (published 2026-02-03) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/10.-Ingatlan-berbeadasanak-es-egyeb-hasznositasanak-adozasa-2026.02.03 | 2026-10-23 |
| NAV information sheet 9, Az ingatlanértékesítésből és a vagyoni értékű jog átruházásából származó jövedelem (2026-02-04) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/09.-Az-ingatlanertekesitesbol-es-a-vagyoni-erteku-jog-atruhazasabol-szarmazo-jovedelem-2026.02.04 | 2026-10-23 |
| NAV information sheet 49, A szociális hozzájárulási adó (2026-01-16) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/49.-A-szocialis-hozzajarulasi-ado-2026.-01.-16 | 2026-10-23 |

Not yet confirmed: whether rental income, which bears no szocho, still counts towards the HUF 7,747,200 szocho cap. Szocho tv. 2. § (2) counts income under 1. § (1)-(3); rental income is consolidated-base income under 1. § (1), but 5. § (2) h) takes it out of the 1. § (1)-(3) liability, and neither the act, NAV information sheet 49 nor the 25SZJA guide (line 286) says whether exempt income still counts. Also not read: the depreciation rates for let property in the Szja tv. 11. számú melléklet and the cost list in the 3. számú melléklet; the definition of a tax-free NYESZ pension payout in the NYESZ act (2005. évi CLVI. törvény) and whether szocho applies to the other income from a non-pension NYESZ withdrawal.

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
