---
name: hu-cross-border
description: "Hub skill for crossing the Hungarian border in tax year 2026. Covers individual tax residence under Szja tv. 3. § 2. (citizenship, EEA nationals present 183 days, long-term residence permits, then permanent home, centre of vital interests and habitual abode); non-residents taxed only on Hungarian-source income; the payer's 15% withholding on dividends, interest and royalties paid to foreign individuals and the treaty rate at source with a residence certificate and beneficial owner statement (Szja tv. 7. számú melléklet); no withholding on payments to foreign companies; the foreign tax credit (Szja tv. 32. §, 90%) and treaty exemption; the corporate exit tax with five instalments for EU and EEA moves (Tao. tv. 16/A. §); A1 certificates; penalties. Trigger phrases: külföldi illetőségű, belföldi illetőség, kettős adóztatás, illetőségigazolás, exit tax Hungary, moving to Hungary, leaving Hungary, non-resident dividend Hungary. Out of scope: hu-corporate-tax, hu-transfer-pricing, hu-income-tax, hu-social-contributions, hungary-vat-return."
version: 0.2
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

# Hungary: cross-border tax for people and companies (2026)

Source-cited draft: not reviewed by an accountant, not for filing.

This is the hub for the Hungarian cross-border (XB) domain. It links rather than repeats:

- Corporate tax, company residence, PE profits, CFC and the 9% rate: [hu-corporate-tax](hu-corporate-tax.md).
- Related-party pricing and MAP: [hu-transfer-pricing](hu-transfer-pricing.md).
- Self-employed income tax (átalányadó, KATA): [hu-income-tax](hu-income-tax.md). Contributions for the self-employed: [hu-social-contributions](hu-social-contributions.md).
- VAT: [hungary-vat-return](hungary-vat-return.md).

The law is the Personal Income Tax Act (1995. évi CXVII. törvény, "Szja tv."), the Corporate Tax Act (1996. évi LXXXI. törvény, "Tao. tv."), the Tax Procedure Act (2017. évi CL. törvény, "Art."), the Social Contribution Tax Act (2018. évi LII. törvény, "Szocho tv.") and the Social Security Act (2019. évi CXXII. törvény, "Tbj."). All were read in the versions in force from 1 October 2026 on njt.jog.gov.hu. Tax year: the calendar year. Currency: forint (HUF).

## Who this applies to

**Individuals: who is resident.** The Szja tv. lists four groups, in order (Szja tv. 3. § 2.):

1. **A Hungarian citizen.** Exception: a dual citizen who has no registered home address or place of stay in Hungary.
2. **An EEA national (or other person with the right of free movement)** who exercises that right in Hungary for at least 183 days in the calendar year. Arrival and departure days count as whole days.
3. **A third-country national with a long-term residence permit (huzamos tartózkodási jogosultság), or a stateless person.**
4. **Anyone else** whose permanent home is only in Hungary; failing that, whose centre of vital interests (closest personal, family and economic ties) is in Hungary; failing that, whose habitual abode is in Hungary.

A permanent home is a home set up for lasting residence where the person actually lives. It does not change because of a temporary longer stay abroad (Szja tv. 3. § 2. d)). A holder of the long-term permit under Act XC of 2023, 83. § (1) e) is non-resident if present fewer than 183 days in any 12-month period (Szja tv. 3. § 3.).

So a Hungarian citizen working abroad for years stays resident under domestic law. NAV says so directly ([NAV information sheet 4, section 2.1](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/04.-Maganszemelyek-kulfoldrol-szarmazo-jovedelme-2026.02.20)). Where the other country also treats the person as resident, the treaty tie-breaker (usually article 4) decides: permanent home, then centre of vital interests, then habitual abode, then nationality, then the competent authorities.

**Scope.** A resident is taxed on worldwide income. A non-resident is taxed only on income whose source is Hungary, or that a treaty or reciprocity lets Hungary tax (Szja tv. 2. § (4)). A treaty overrides the Szja tv. where they differ (Szja tv. 2. § (5)).

**Where income comes from (Szja tv. 3. § 4.).** Employment: where the work is usually done. Self-employment: the state of residence, unless done through a fixed base. Real estate income: where the property is. Directors' fees: where the company has its seat. Interest and royalties: the residence of the payer, or Hungary if the payer owes them through a Hungarian branch or PE (3. § 4. h), i)). Dividends: the residence of the paying company (3. § 4. j)). Any of these is Hungarian-source if the underlying right belongs to the individual's own Hungarian fixed base. Gains on shares in a Hungarian real-estate company: always Hungary.

**Part year.** Residence can change during the year. NAV's example: a citizen who moves abroad for good on 1 September and has a permanent home only abroad from then is resident for January to August and non-resident for September to December (NAV information sheet 4, section 2.4).

**Companies.** A company registered in Hungary is resident; a foreign company is resident if its place of management is in Hungary (Tao. tv. 2. § (2), (3)). A foreign company is taxed on profits of a Hungarian permanent establishment and on gains from selling or withdrawing shares in a Hungarian real-estate holding company (Tao. tv. 2. § (4) a), c)). Details in [hu-corporate-tax](hu-corporate-tax.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal income tax, flat rate (also on dividends and interest) | 15% | 2026 | [Szja tv. 8. § (1)](https://njt.jog.gov.hu/jogszabaly/1995-117-00-00) |
| Residence test for EEA nationals | 183 days in the calendar year, arrival and departure days counted | 2026 | Szja tv. 3. § 2. b) |
| Payer's tax on dividends, interest, royalties and other Hungarian-source income paid to a non-resident individual | 15% unless the treaty rate is documented by the time of payment; paid by the 12th of the month after payment | 2026 | Szja tv. 7. számú melléklet, points 1 and 2; [NAV information sheet 24, section 2.3](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/24.-Bevallasi-adofizetesi-informaciok-2026.01.26) |
| Treaty rate at source | The treaty rate, if by the time of payment the payer holds this year's residence certificate (or accepts the person's written residence statement until it arrives) and, where the treaty asks, a beneficial owner statement | 2026 | Szja tv. 7. számú melléklet, points 2, 6 and 7 |
| Withholding on dividends, interest and royalties paid to a foreign company | None | 2026 | [NAV English summary on business associations](https://nav.gov.hu/pfile/file?path=%2Fen%2Ftaxation%2Ftaxinfo%2Fa-short-summary-on-the-taxation-of-business-associations), sections 2.6 and 7.1; see hu-corporate-tax |
| Social contribution tax (szocho) on a resident's dividends and interest | 13% | 2026 | [Szocho tv. 1. § (5), 2. § (1)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00) |
| Szocho on dividends, interest and gains of a person who is "foreign" under the Tbj. | None | 2026 | Szocho tv. 5. § (6); [Tbj. 4. § 1. and 12.](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| Foreign tax credit, no treaty, consolidated income (employment, self-employment) | 90% of the foreign tax, capped at 15% of that income | 2026 | Szja tv. 32. § (1) |
| Foreign tax credit, no treaty, separately taxed income (dividends, interest) | Foreign tax credited, but Hungarian tax stays at least 5% of the income | 2026 | Szja tv. 8. § (2) |
| Allowances for a non-resident | Only if Hungarian-taxable work and pension income is at least 75% of world income, and no similar allowance abroad | 2026 | Szja tv. 1/A. § (3) |
| Corporate exit tax | 9% corporate tax on market value less tax book value of what leaves | 2026 | [Tao. tv. 16/A. § (2)](https://njt.jog.gov.hu/jogszabaly/1996-81-00-00), 19. § |
| Exit tax instalments (move to an EU state, or an EEA state with a recovery agreement) | 20% with the return, then 4 equal annual instalments of the other 80% | 2026 | Tao. tv. 16/A. § (4), (5) |
| Late payment interest (késedelmi pótlék) | Central bank base rate plus 5 points, per day (1/365) | 2026 | [Art. 209. § (1)](https://njt.jog.gov.hu/jogszabaly/2017-150-00-00) |
| Central bank base rate | 5.50% from 26 August 2026 (late interest 10.50% a year) | 2026 | [NAV base rate notice, 25 August 2026](https://nav.gov.hu/ugyfeliranytu/jegybank) |

## The taxable base

**Residents with foreign income.** NAV sets out four steps (NAV information sheet 4, section I):

1. Decide residence under Hungarian law, the other state's law and the treaty.
2. Find which state may tax the income under the treaty article for that type of income.
3. Apply that state's rules.
4. If the treaty lets both states tax it (dividends, some interest and royalties), Hungary taxes it and credits the foreign tax.

**Treaty exemption.** Where a treaty gives the taxing right to the other state, the income is exempt in Hungary. NAV: income of residents that is taxable abroad under the treaty (typically except dividends) is exempt (NAV English summary on private persons, section 7). It is left out of the consolidated base but shown on the return as information (NAV information sheet 4, sections I and 3.1). Hungary has more than eighty treaties, covering every EU state (sheet 4, section 1).

**Treaty credit.** Where the treaty lets both states tax (dividends are the usual case), Hungary charges its 15% and deducts the foreign tax the treaty allows. NAV's example: with a 15% treaty rate deducted abroad, nothing more is due in Hungary. Foreign tax that the person can reclaim abroad is not credited (sheet 4, section 3.3).

**No treaty.** For consolidated income (employment, self-employment), the Hungarian tax is cut by 90% of the foreign tax, up to the Hungarian tax on that income. Foreign tax on Hungarian-source income is never credited without a treaty (Szja tv. 32. § (1)). For separately taxed income, the foreign tax is credited but at least 5% stays payable in Hungary (Szja tv. 8. § (2)). Since 1 January 2024 the United States is a no-treaty state for Hungary: the 1979 treaty no longer applies (NAV information sheet 4, footnote 4).

**Low-tax and no-treaty interest.** Interest and dividends from a company seated in a low-tax state, and interest paid by a resident of a no-treaty state, are "other income" in the consolidated base, not 15% separate income. Low-tax means corporate tax below 9% and no treaty. Payers seated in an OECD state are excluded (Szja tv. 3. § 5., 28. § (12)).

**Non-residents with Hungarian income.**

- **Employment in Hungary:** the employer withholds through payroll. The treaty can move the taxing right to the residence state for short stays (183 days, foreign employer, no Hungarian PE bearing the cost). See the pack's payroll skill.
- **Dividends, interest, royalties and performers' fees from a Hungarian payer:** the payer withholds 15%, or the treaty rate if the residence certificate and statements are in hand before payment. If the treaty gives Hungary no taxing right and residence is proven, nothing is withheld (Szja tv. 7. számú melléklet, points 1 to 3).
- **Allowances:** a non-resident can claim Hungarian allowances (family allowance and others) only under the 75% rule in Szja tv. 1/A. § (3).
- **Szocho:** a person who is "foreign" under the Tbj. pays no social contribution tax on dividends, interest or gains (Szocho tv. 5. § (6)). Under the Tbj., "domestic" means a Hungarian citizen with a registered Hungarian address, a long-term residence permit holder, a refugee, an EEA national exercising free movement in Hungary with a registered address, or a stateless person (Tbj. 4. § 1.); everyone else is "foreign" (Tbj. 4. § 12.).

**Leaving: individuals.** We found no rule in the 2026 Szja tv. that taxes unrealised gains when a person leaves. A person leaving to settle abroad can ask NAV to assess the tax by decision during the year, if they show the foreign immigration visa and attach the documents needed (Art. 148. § (1)). A person with no Hungarian home, habitual abode, seat or PE who leaves before year end, not intending to return that year for taxable work or income, must notify NAV 30 days before leaving, with the documents; NAV then assesses the tax by decision (Art. 148. § (2)).

**Leaving: companies (exit tax).** The base is increased by the market value less the tax book value of what is moved (Tao. tv. 16/A. § (1), (2)) when a company:

- moves its place of management abroad and becomes resident there;
- moves assets from its Hungarian seat to a foreign PE, or from a Hungarian PE abroad;
- moves a Hungarian PE's business abroad.

The charge applies only where the assets leave the Hungarian tax net. Market value follows the transfer pricing rules (16/A. § (8)). Assets moved for financing, collateral, prudential capital or liquidity and due back within 12 months are out (16/A. § (9)). An asset coming in from another EU state takes that state's exit value as its tax cost, unless it is not market value (16/A. § (10)).

**Instalments.** Moves to another EU state, or to an EEA state with an EU-standard tax recovery agreement, can be paid in five instalments. The company elects on the return, pays 20% with the return, and pays the other 80% in four equal yearly instalments by each year's corporate tax return due date (16/A. § (4), (5)). The whole balance falls due at once if any of these happen (16/A. § (6)):

- the assets or business are sold;
- the assets or the place of management move on to a third country (this does not apply to a move to an EEA state with a tax recovery agreement);
- the company enters insolvency;
- an instalment is 30 days late.

The company must tell NAV within 15 days (16/A. § (7)).

## Deadlines and filing

- **Personal tax return:** 20 May of the following year (20 May 2027 for 2026), on the 26SZJA form or by accepting the NAV draft return ([NAV English summary on private persons](https://nav.gov.hu/pfile/file?path=/en/taxation/taxinfo/a-short-summary-on-the-taxation-of-private-persons), section 8; NAV information sheet 24).
- **Foreign income with no Hungarian payer:** the person pays advance tax on consolidated income by the 12th of the month after the quarter. No advance is due on income from a no-treaty state. Tax on dividends and interest is due by the return deadline (NAV information sheet 4, section 5.2).
- **Treaty-exempt income:** not taxed, but shown on the return as information. A return is not needed for income that a treaty makes untaxable in Hungary (Szja tv. 11. § (3) g)).
- **Non-resident with no Hungarian tax:** may file form NYK by 30 April of the following year to say they had no Hungarian liability. The NAV draft return then does not become their return (NAV information sheet 24, section 2.3).
- **Payer's withholding:** deducted at payment, paid by the 12th of the following month (Szja tv. 7. számú melléklet, point 2).
- **Residence certificate for a non-resident:** an English original, a certified Hungarian translation, or a copy of either. It is needed every tax year, before the first payment of the year or the first payment after a change. It is kept by the payer (melléklet, point 6). If the certificate is not ready by the time of payment, the payer may accept the person's written statement of residence; if the certificate still has not been shown by the payer's return for the last month of the year, the payer must declare and pay the tax it did not withhold, and can correct this by self-revision if the certificate comes later (point 6). Where the treaty turns on it, the beneficial owner statement is made before payment; a statement made after payment but before the payer's return lets the payer correct the tax and settle the difference with the person (point 7).
- **Refund of over-withheld tax:** the non-resident claims from NAV with the residence certificate and the payer's certificate. NAV pays to the account named (melléklet, point 4). A custodian or registered nominee can act for them (point 5).
- **Hungarian residence certificate (for use abroad):** requested from NAV on form IGAZOL. It is free in Hungarian or Hungarian and English ([NAV note on residence certificates](https://nav.gov.hu/pfile/file?path=/en/taxation/taxinfo/tax-residence-certificate)).
- **Exit tax:** declared on the corporate return for the year of the move. The instalment election is made on that return (Tao. tv. 16/A. § (4)).
- **A1 certificate (social security).** EU Regulation 883/2004 applies one state's social security law at a time, normally where the work is done.
  - A posted worker or self-employed person stays in the home system for up to 24 months.
  - In Hungary the A1 is issued by the county government office's district office. In Budapest and Pest county it is the Budapest Government Office, XIII district office (NAV information sheet 4, part II, section 3.1; Tbj. 90 to 92. §).
  - With an A1 or other certificate of insurance in another member state, no Hungarian szocho is due on that person's pay (Szocho tv. 5. § (4)).

## Penalties and interest

- **Late payment interest:** for each day late, the central bank base rate plus 5 percentage points, divided by 365 (Art. 209. § (1)). With the base rate at 5.50% from 26 August 2026, that is 10.50% a year.
- **Tax penalty (adóbírság):** 50% of the shortfall; 200% where income was hidden or records were falsified (Art. 215. § (3), (4)). An individual is not penalised for a shortfall caused by a false certificate from the employer or payer (215. § (2) a)).
- **Default fine (mulasztási bírság):** up to HUF 400,000 for an individual and HUF 1,000,000 for others, for late, missing or wrong filings. For a late filing, no fine if the taxpayer files and shows it acted as could reasonably be expected (Art. 220. § (1) to (3)).
- **Payer that withheld:** once tax is withheld, NAV can collect it only from the payer (Szja tv. 15. § (3)). The treaty rate may be applied only if the documents are in hand by the time of payment; otherwise the payer withholds 15% (Szja tv. 7. számú melléklet, point 2).
- **Exit tax instalments:** a 30-day delay on an instalment makes the whole balance due at once (Tao. tv. 16/A. § (6) e)).

## Cross-border points

- **Dividends to foreign companies:** no Hungarian withholding. The participation exemption and inbound dividend rules are in [hu-corporate-tax](hu-corporate-tax.md).
- **Dividends to foreign individuals:** 15% at source, or the treaty rate with paperwork. No szocho if the person is foreign under the Tbj. Worked in Example 1.
- **Interest:** 15% at source when paid to a non-resident individual. Interest on Hungarian government retail bonds is excluded from income (Szja tv. 65. § (3) a) ab)).
- **Royalties to individuals:** Hungarian source if the payer is resident (Szja tv. 3. § 4. h)); payer withholds under the same annex.
- **Real estate:** income from Hungarian property is Hungarian-source whoever owns it (Szja tv. 3. § 4. c)). Gains on shares in a Hungarian real-estate company are always Hungarian-source (3. § 4. n)). For companies see Tao. tv. 2. § (4) in [hu-corporate-tax](hu-corporate-tax.md).
- **Directors:** fees from a Hungarian company are Hungarian-source wherever the director lives (Szja tv. 3. § 4. f)).
- **Transfer pricing on cross-border flows and MAP:** [hu-transfer-pricing](hu-transfer-pricing.md).
- **United States:** no treaty since 2024. A Hungarian resident with US income gets only the domestic credit: 90% and the 5% floor.

## Worked examples

### Example 1: a HUF 2 million dividend to a foreign individual, treaty rate 5%

A Hungarian Kft pays a dividend of HUF 2,000,000 to an individual shareholder resident in a treaty country. The treaty caps source tax on this dividend at 5%. The shareholder is not a Hungarian citizen and has no registered Hungarian address, so they are "foreign" under the Tbj.

- **If the payer has the paperwork before payment** (this year's residence certificate, plus the beneficial owner statement if the treaty asks for it), it withholds 5%: HUF 100,000.
- **If it has neither the certificate nor a written residence statement it is willing to accept**, it must withhold the domestic 15%: HUF 300,000. The shareholder can then claim the HUF 200,000 difference from NAV with the residence certificate and the payer's certificate.
- **Szocho:** none, because the person is foreign under the Tbj. (Szocho tv. 5. § (6)).
- **Payment:** the payer pays the tax by the 12th of the month after payment.

The shareholder nets HUF 1,900,000 either way once the refund arrives.

```oa-check
name: HUF 2m dividend to a non-resident individual, 5% treaty rate, 2026
inputs:
  dividend: 2000000
steps:
  - domestic_rate: 15 / 100
  - treaty_rate: 5 / 100
  - tax_without_certificate: dividend * domestic_rate
  - tax_with_certificate: dividend * treaty_rate
  - refund_claim: tax_without_certificate - tax_with_certificate
  - net_to_shareholder: dividend - tax_with_certificate
expected:
  tax_without_certificate: 300000
  tax_with_certificate: 100000
  refund_claim: 200000
  net_to_shareholder: 1900000
```

### Example 2: foreign employment income, exemption versus credit

A Hungarian citizen keeps their registered Budapest home and works abroad for a foreign employer all of 2026. They stay Hungarian resident under domestic law (Szja tv. 3. § 2. a)). Pay: the equivalent of HUF 12,000,000. Foreign income tax paid and not refundable: HUF 1,500,000.

- **(a) Treaty country, and the treaty makes them resident in Hungary but gives the taxing right on the pay to the work state.** The income is exempt in Hungary. It is shown on the 26SZJA return as information only. Hungarian tax on it: nil. (If the treaty tie-breaker makes them resident abroad, Hungary does not tax the foreign pay at all.)
- **(b) No-treaty country, for example the United States.** Hungary taxes the pay at 15%: HUF 1,800,000. The credit is 90% of the foreign tax (HUF 1,350,000), capped at the Hungarian tax on that income (HUF 1,800,000). So the credit is HUF 1,350,000. Hungarian tax payable is HUF 450,000, due by 20 May 2027. No quarterly advance is needed for income from a no-treaty state.

Social security is a separate question; the employer's state applies unless an agreement or A1 says otherwise.

```oa-check
name: Resident with HUF 12m foreign pay, treaty exemption vs no-treaty credit, 2026
inputs:
  foreign_pay: 12000000
  foreign_tax: 1500000
steps:
  - pit_rate: 15 / 100
  - credit_share: 90 / 100
  - treaty_exempt_hungarian_tax: foreign_pay * 0
  - hungarian_tax_before_credit: foreign_pay * pit_rate
  - credit_limit_from_foreign_tax: foreign_tax * credit_share
  - credit: min(credit_limit_from_foreign_tax, hungarian_tax_before_credit)
  - hungarian_tax_no_treaty: hungarian_tax_before_credit - credit
expected:
  treaty_exempt_hungarian_tax: 0
  hungarian_tax_before_credit: 1800000
  credit_limit_from_foreign_tax: 1350000
  credit: 1350000
  hungarian_tax_no_treaty: 450000
```

## Ask the client first

1. Citizenship (including dual citizenship), registered Hungarian address, residence permit type, and days spent in Hungary in 2026. Where do they have a permanent home, and where is their family?
2. Are they also resident somewhere else under that country's law? Which country, and is there a treaty in force with Hungary for 2026?
3. What income, from which country, and who pays it: pay, director's fees, dividends, interest, royalties, rent, share sales? How much foreign tax was paid, and can any be reclaimed?
4. For a non-resident receiving Hungarian dividends or interest: did they give the payer this year's residence certificate and beneficial owner statement before payment?
5. For a company: is it moving its place of management, assets or a branch's business abroad? To which state, and when? What are the market and tax book values?
6. For workers moving between states: is there an A1 or other certificate of insurance, and for how long?

## Sources

| Source | URL | Read on |
|---|---|---|
| Szja tv. (Act CXVII of 1995), 1/A. §, 2. §, 3. § 2.–5., 8. §, 11. § (3), 15. § (3), 28. § (12), 32. §, 65. §, 66. §, 7. számú melléklet; Nemzeti Jogszabálytár, version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/1995-117-00-00 | 2026-10-23 |
| Tao. tv. (Act LXXXI of 1996), 2. §, 16/A. §; version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/1996-81-00-00 | 2026-10-23 |
| Art. (Act CL of 2017), 148. §, 209. §, 215. §, 220. §; version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 | 2026-10-23 |
| Szocho tv. (Act LII of 2018), 1. § (5), 2. § (1), 5. § (4), (6); version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/2018-52-00-00 | 2026-10-23 |
| Tbj. (Act CXXII of 2019), 4. § 1. and 12.; version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/2019-122-00-00 | 2026-10-23 |
| NAV information sheet 4: foreign income of individuals (20 February 2026) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/04.-Maganszemelyek-kulfoldrol-szarmazo-jovedelme-2026.02.20 | 2026-10-23 |
| NAV information sheet 24: return and payment information (26 January 2026), section 2.3 | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/24.-Bevallasi-adofizetesi-informaciok-2026.01.26 | 2026-10-23 |
| NAV: short summary on the taxation of private persons in 2026 (English, August 2026) | https://nav.gov.hu/pfile/file?path=/en/taxation/taxinfo/a-short-summary-on-the-taxation-of-private-persons | 2026-10-23 |
| NAV: short summary on the taxation of business associations (English) | https://nav.gov.hu/pfile/file?path=%2Fen%2Ftaxation%2Ftaxinfo%2Fa-short-summary-on-the-taxation-of-business-associations | 2026-10-22 (read for hu-corporate-tax) |
| NAV: how a tax residence certificate is issued (English, January 2025) | https://nav.gov.hu/pfile/file?path=/en/taxation/taxinfo/tax-residence-certificate | 2026-10-23 |
| NAV: central bank base rate notice (25 August 2026) | https://nav.gov.hu/ugyfeliranytu/jegybank | 2026-10-23 |
| Nemzeti Jogszabálytár short address (official) | https://njt.hu/jogszabaly/1995-117-00-00 | 2026-10-23: unreachable; the same database answered at njt.jog.gov.hu |

Not yet confirmed: NAV's 2026 list of applicable treaties (the "Adózói tájékoztató" page named in information sheet 4) was not read, so this skill names no treaty partner or treaty rate other than the US position; which Hungarian treaties use the credit method rather than exemption for employment income; whether the NAV office handling non-resident refund claims is still the one named on NAV's 2017 English page (not relied on); the absence of an individual exit tax rests on two independent full-text searches of the 2026 Szja tv. including its annexes (the only deemed-gain rule found, 65/C. §, covers transfers into a trust or private foundation), not on a NAV statement; payroll withholding for non-resident employees is left to the pack's payroll skill.

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
