---
name: digital-services-tax-matrix
description: "Use this skill whenever a digital services provider asks about country-level Digital Services Tax (DST) exposure. Trigger on phrases like \"DST\", \"digital services tax\", \"digital tax\", \"France DST\", \"UK DST\", \"Italy DST\", \"Spain DST\", \"Austria DST\", \"Turkey DST\", \"India equalisation levy\", \"Kenya DST\", \"Canada DST\", \"DST nexus\", \"DST scope\", \"user location attribution\", \"DST and Pillar One\", \"DST sunset\", or any request to assess whether a service falls within a country's DST. Covers all DSTs in force or proposed as of mid-2025 across 25+ jurisdictions including the Canada DST (in force from 28 June 2024, retroactive to 2022) and India's equalisation levy regime. Maps the scope, rate, threshold, taxable services definition, user-location attribution method, filing/payment mechanics, and Pillar One Amount A interaction. Does NOT cover: corporate income tax / permanent establishment; VAT/GST on digital services (B2C and OSS); EU DAC7 platform reporting; OECD Pillar One Amount A computation (separate skill); WHT on royalties / technical services. ALWAYS read this skill before computing DST liability or advising on DST mitigation."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Digital Services Tax Matrix

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It maps every Digital Services Tax in force or formally proposed as of mid-2025, with the practical mechanics a freelancer, SaaS company, or marketplace must execute.

**Tax year coverage.** Current for **calendar 2025**, reflecting:
- Canada DST (in force 28 June 2024 under the Digital Services Tax Act, with retroactive accrual back to 2022)
- The repeal of Austria's DST proposal (Austria still applies its 5% DST), repeal of certain Spanish IDSD provisions discussed in 2025
- The OECD's continued work on Pillar One Amount A (status: not yet ratified; many DSTs remain in place pending the Amount A entry into force)
- US §301 retaliatory tariff threats on certain DSTs (active discussion through 2024-2025)

**The reviewer is the customer of this output.** DST scope is contested per service line and changes with national budget cycles. Every output must be reviewed by a credentialed tax practitioner in the source country before filing.

## Section 1 — Scope statement

This skill covers:

- **In-force DSTs** as of mid-2025 in: Austria, Canada, France, Hungary (advertising tax), India (equalisation levy 2.0 — the 2% e-commerce regime was repealed effective 1 August 2024, the 6% advertising levy remains), Italy, Kenya, Nepal, Spain, Tanzania (digital service tax), Tunisia, Turkey, United Kingdom, Uganda (effective 2024), Vietnam (e-commerce platforms), Zimbabwe.
- **Proposed / pending DSTs** in: Brazil, Indonesia (already converted significantly into VAT on digital supplies), New Zealand (DST Bill paused 2024), Pakistan, Poland (paused), Slovakia (paused).
- **DST scope analysis** — what services fall within each regime.
- **User-location attribution methods** for revenue allocation.
- **Threshold tests** — global revenue, domestic revenue, MNE-group scope.
- **Filing and payment mechanics**.
- **Interaction with Pillar One Amount A** and the OECD's DST political commitments.

This skill does NOT cover:

- **VAT/GST on digital services** — see country VAT/GST skills and EU OSS skill (`eu-oss-digital.md`).
- **Permanent Establishment for digital business** — see `permanent-establishment-risk.md`.
- **EU DAC7 platform reporting** — see `dac7-platform-reporting.md` (forthcoming).
- **Pillar One Amount A computation** — see `pillar-one-amount-a-b.md` (forthcoming).
- **Withholding tax on royalties / technical services** to digital service providers — see `withholding-tax-matrix.md`.

## Section 2 — Country-by-country DST matrix

### 2.1 In-force DSTs (Europe)

**In-force DSTs (Europe)**  _(see individual statutes per row)_

| Country | Rate | Global revenue threshold | Domestic revenue threshold | Effective from | Statute |
| --- | --- | --- | --- | --- | --- |
| **Austria** | 5% | EUR 750m worldwide | EUR 25m Austrian online ad revenue | 1 Jan 2020 | Digitalsteuergesetz 2020 |
| **France** | 3% | EUR 750m worldwide digital services | EUR 25m France-attributable digital services | 1 Jan 2019 | CGI Article 299 et seq., Loi 2019-759 |
| **Hungary** (advertising tax) | 0% (suspended through 31 Dec 2025) | HUF 100m Hungarian ad revenue | n/a (no global threshold) | 2014; rate currently 0% but the regime remains in force | Act XXII of 2014 |
| **Italy** | 3% | EUR 750m worldwide | EUR 5.5m Italian digital services revenue | 1 Jan 2020 | Legge 145/2018 Art. 1 commi 35-50, as amended |
| **Spain** | 3% | EUR 750m worldwide | EUR 3m Spanish digital services revenue | 16 Jan 2021 | Ley 4/2020 Impuesto sobre Determinados Servicios Digitales (IDSD) |
| **Turkey** | 7.5% (President may set 1%–15%) | TRY-translated EUR 750m globally; TRY 20m Turkey | n/a (combined) | 1 Mar 2020 | Law 7194 |
| **United Kingdom** | 2% | GBP 500m worldwide | GBP 25m UK digital services revenue with a GBP 25m UK-attributable allowance | 1 Apr 2020 | Finance Act 2020 Part 2 |

### 2.2 In-force DSTs (Americas)

**In-force DSTs (Americas)**  _(Digital Services Tax Act, SC 2024 c. 17)_

| Country | Rate | Threshold | Effective from | Statute |
| --- | --- | --- | --- | --- |
| **Canada** | 3% | CAD 1.1bn (EUR 750m equivalent) global digital services revenue; CAD 20m Canadian digital services revenue | 28 June 2024, with retroactive liability accruing from 1 January 2022 (deemed payment 30 June 2024 for the 2022-2024 catch-up) | Digital Services Tax Act, SC 2024 c. 17 |

### 2.3 In-force DSTs (Asia, Africa, Oceania)

**In-force DSTs (Asia, Africa, Oceania)**  _(see individual statutes per row)_

| Country | Rate | Threshold | Effective from | Statute |
| --- | --- | --- | --- | --- |
| **India — Equalisation Levy 2.0** | 6% on advertising payments by non-residents from Indian payors to non-resident providers; the **2% e-commerce supply levy was repealed effective 1 August 2024** | Per-payment threshold INR 1 lakh aggregate per payer per year for advertising levy | 2016 (advertising), 2020 (e-commerce — repealed 2024) | Finance Act 2016 Chapter VIII; Finance Act 2020 (e-commerce, since repealed) |
| **Kenya** | 1.5% (DST repealed 25 Dec 2024 and replaced by Significant Economic Presence Tax — SEPT — at 6% effective 27 Dec 2024) | No global threshold; KES 5m local | DST: 1 Jan 2021–24 Dec 2024; SEPT: from 27 Dec 2024 | Finance Act 2020, Finance Act 2024 |
| **Nepal** | 2% | NPR 2m | Mar 2022 | Finance Act 2022 |
| **Tanzania** | 2% | n/a | 1 Jul 2022 | Finance Act 2022 |
| **Tunisia** | 3% | n/a | 1 Jan 2020 | Loi de Finances 2020 |
| **Uganda** | 5% (DST on non-resident digital service providers) | UGX 150m | 1 Jul 2023 | Tax Procedures Code (Amendment) Act 2023 |
| **Zimbabwe** | 5% | n/a (broad scope) | 1 Jan 2019 | Income Tax Act §12B |
| **Pakistan** | 5% (DST on digital marketplaces under §6A ITO) | n/a; subject to FBR-administered de minimis | 1 Jul 2024 | Income Tax Ordinance §6A as inserted by Finance Act 2024 |
| **Vietnam** | Various rates by service line (combined VAT + CIT under Decree 91/2022/NĐ-CP for non-resident platforms; effective DST-like CIT typically 5%) | n/a | 1 Jan 2022 | Decree 91/2022 |

### 2.4 Repealed or paused

**Repealed or paused**

| Country | Status |
| --- | --- |
| **Belgium** | Bill never enacted; politically paused |
| **Czech Republic** | DST bill withdrawn 2021 |
| **New Zealand** | DST Bill paused 2024 pending Pillar One |
| **Norway** | Never enacted |
| **Poland** | Paused pending Pillar One |
| **Slovakia** | Paused |
| **India e-commerce levy (2%)** | Repealed effective 1 August 2024 |
| **Kenya DST (1.5%)** | Repealed 25 December 2024 (replaced by SEPT 6%) |

## Section 3 — Scope (taxable services)

The taxable services definition is the single most contested element. Major categories:

**Taxable service category matrix**

| Service category | UK | FR | IT | ES | AT | TR | CA | IN-ad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Online advertising** (sale of ad targeted at users in country) | Yes | Yes | Yes | Yes | Yes (sole) | Yes | Yes | Yes |
| **Sale of user data** | Yes | Yes | Yes | Yes | No | Yes | Yes | No |
| **Online intermediation / marketplace** (matching buyers/sellers) | Yes | Yes | Yes | No | No | Yes | Yes | No |
| **Streaming and digital content** (Netflix-style subscriptions to users in country) | No | No | No | No | No | Yes | No | No |
| **Search engine** | Yes | Yes | Yes (within ads) | Yes (within ads) | Yes (within ads) | Yes | Yes (within ads) | No |
| **Social media platforms** | Yes | Yes | Yes | Yes | No | Yes | Yes | No |

- **Carve-outs commonly applied [T1]** — Payment services (e.g., card processing) — usually excluded; E-commerce sale of own goods to consumers — usually excluded (not DST; VAT applies); Direct B2B sales of SaaS services not advertising-funded — usually excluded but check Turkey (broader scope)  _([T1])_

## Section 4 — User-location attribution

### 4.1 The general principle

- **General principle of revenue allocation** — Revenue is allocated to a DST jurisdiction if the user / advertiser / data subject is located in that jurisdiction. Multiple users in different jurisdictions for the same transaction result in pro-rata allocation.  _([T1])_

### 4.2 Country-specific attribution rules

**Country-specific attribution rules**  _(see per-row citations)_

| Country | Method |
| --- | --- |
| **UK** | User is "normally located" in UK based on indicators (IP address, billing address, telephone, payment instrument, real-world facts). FA 2020 Sch 9 ¶7 |
| **France** | User is located in France if used the device in France during the calendar year. CGI Art. 299 ter |
| **Italy** | User device located in Italy; for ad targeting, indicators include IP, payment, user account country. D.M. 23/06/2022 |
| **Spain** | User device located in Spain; reasonable means including IP, payment instrument, billing address. Reglamento IDSD |
| **Austria** | Online advertising received on a device with an Austrian IP address. Digitalsteuergesetz §1 |
| **Turkey** | Service provided via Turkish IP address or paid from a Turkish bank or card. Communiqué 2020 |
| **Canada** | "Canadian user" determined by indicators including IP address with Canadian location, mailing address, billing address, phone number. DSTA s.6 |
| **India** | Indian IP address; payment by Indian resident; or service availed from India. Finance Act 2016 §165A |

### 4.3 Mixed-jurisdiction transactions

- **Mixed-jurisdiction transaction allocation** — For multi-user transactions (e.g., a UK advertiser targeting a French user via a Spanish platform), allocation generally: 1. Identify the taxable service line per country's scope. 2. Identify whose user/advertiser/data the revenue is attributable to. 3. Allocate the gross revenue pro-rata to each in-scope jurisdiction using each country's attribution method. Each country administers its own DST independently — double DST is structurally possible. Practitioners model the exposure per country.  _([T2])_

## Section 5 — Computing DST liability

### Step 1 — Determine if MNE group is in scope

- **MNE group in-scope test** — 1. Test global revenue against the country's threshold (where applicable). 2. Test in-country revenue against the country's threshold. 3. If both met → in scope. Group thresholds use the entire MNE group (Article 3 group definition per country). For UK / France / Italy / Spain / Canada / Austria the EUR 750m / equivalent figure aligns with CbCR scope.  _([T1])_

### Step 2 — Determine taxable revenue

- **Determine taxable revenue** — Take total revenue from the taxable services (Section 3) for the year. Apply user-location attribution to determine the share allocable to the country. Apply any country-specific allowance (e.g., UK GBP 25m allowance subtracted from UK taxable revenue).  _([T1])_

### Step 3 — Apply rate

- **DST liability formula** — Attributable revenue × rate (Section 2)  _([T1])_

### Step 4 — Loss / deduction relief

- **Loss / deduction relief by country** — UK: "Safe harbour" alternative computation under FA 2020 Sch 8 ¶6, allowing a margin-based reduction where the business has a low UK margin on the taxable activities. France / Italy / Spain: general expense deduction is NOT allowed — DST is a turnover tax. Canada: the in-scope revenue is gross; a CAD 20m deduction is the only allowance.  _([T1]; FA 2020 Sch 8 ¶6)_

### Step 5 — Translation and payment

- **Currency translation and payment** — Translate to local currency at average annual exchange rate (UK), end-of-period (some others). Pay by the country's deadline.  _([T1])_

## Section 6 — Filing mechanics and deadlines

**Filing mechanics and deadlines**  _(see per-row citations)_

| Country | Filing portal | Deadline (annual) | Instalments |
| --- | --- | --- | --- |
| **UK** | HMRC online DST return | 9 months 1 day after end of accounting period | Quarterly payments on account at 5%, 17.5%, 32.5%, 45% (FA 2020 Sch 9 ¶22) |
| **France** | DGFiP forms n° 3310-A-SD and n° 3310-CA3 | 25 October for prior calendar year | One instalment in April + one in October (50% each based on prior year) |
| **Italy** | Agenzia delle Entrate F24 form | 16 May (for prior calendar year) | Single payment |
| **Spain** | Modelo 490 | Quarterly (last 20 days of month after quarter end) | Quarterly payments |
| **Austria** | Form U30 via FinanzOnline | Last day of month after the month service was provided (monthly) | Monthly |
| **Turkey** | Monthly DST return (Beyanname Hizmet Vergisi Dijital) | Last day of following month | Monthly |
| **Canada** | CRA RC4731 form via My Business Account | 30 June following calendar year | One annual payment |
| **India** (advertising EL) | Form 1 (annual) + statement under §40(a)(ib) deduction blackout | Annual + transaction-level reporting | Withheld by payer at transaction level |

## Section 7 — Edge cases and special rules

### 7.1 Pillar One Amount A — DST sunset commitments

- **Pillar One Amount A DST sunset commitments** — Under the OECD/G20 IF Statement of October 2021 and the 2024 Multilateral Convention text, signatory jurisdictions committed to remove DSTs (and refrain from imposing new DSTs) upon Pillar One Amount A entering into force. As of mid-2025 Amount A has not been ratified — DSTs remain in force.  _([T1]; OECD/G20 IF Statement of October 2021; 2024 Multilateral Convention text)_

### 7.2 US §301 retaliatory tariffs

- **US §301 retaliatory tariffs** — USTR investigations have concluded (against multiple countries) that DSTs unreasonably discriminate against US digital companies. Most tariffs were suspended pending Pillar One. Tariff risk remains live if DSTs continue post-Amount A.  _([T2])_

### 7.3 India equalisation levy 2.0 → repeal of e-commerce levy

- **India e-commerce levy repeal** — The 2% e-commerce levy on non-resident e-commerce supplies (introduced 2020) was repealed effective 1 August 2024 by the Finance (No.2) Act 2024. The 6% advertising equalisation levy remains in force.  _(Finance (No.2) Act 2024)_

### 7.4 Kenya DST → SEPT transition

- **Kenya DST to SEPT transition** — The 1.5% DST was repealed by the Tax Laws (Amendment) Act 2024 effective 25 December 2024 and replaced with the Significant Economic Presence Tax (SEPT) at 6% effective 27 December 2024. SEPT applies to non-resident persons whose income from the provision of a service is derived from or accrued in Kenya through a digital marketplace. The 6% rate applies on gross turnover; SEPT is creditable against any Kenya CIT for the same business activity (which is rare for non-residents without PE).  _(Tax Laws (Amendment) Act 2024)_

### 7.5 Canada DST — retroactive period and US response

- **Canada DST retroactive period and US response** — The Canada DSTA imposes liability for calendar years 2022–2023 in a one-time payment due 30 June 2025 (the "retrospective period payment"), in addition to the prospective 2024 onward liability. The US has consistently opposed the retroactive design; potential WTO and §301 challenges remain live.  _(Digital Services Tax Act, SC 2024 c. 17)_

### 7.6 Group-level vs entity-level

- **Group-level vs entity-level filing** — DSTs are generally imposed at the MNE group level with the in-country entity (or designated entity) responsible for filing. Where a group has multiple entities in the same jurisdiction, the group nominates one filer.

### 7.7 Withholding interaction (India advertising EL)

- **India advertising EL withholding** — The 6% Indian advertising equalisation levy is collected by withholding by the Indian payer at the time of payment to the non-resident. The payer must withhold and remit. Failure to withhold leads to disallowance of the deduction under §40(a)(ib) ITA.  _(§40(a)(ib) ITA)_

### 7.8 VAT / GST overlap

- **VAT/GST overlap with DST** — Many DST-imposing countries also impose VAT/GST on the same B2C digital services. The two are independent: VAT collected from the consumer; DST paid by the platform on the gross revenue. No netting.

## Section 8 — Output specification

The reviewer brief must include:

1. **MNE group revenue test** — global and in-country, per DST jurisdiction.
2. **In-scope services analysis** — every revenue stream classified per the country scope tables.
3. **User-location attribution computation** — methodology applied, supporting data.
4. **Annual DST liability** by country, in country currency.
5. **Payment-on-account schedule** for UK, France, Spain, Austria, Turkey.
6. **Filing calendar** with portal references.
7. **Pillar One Amount A status update** — note if any DST has sunset triggered.
8. **Withholding obligations** (India equalisation levy).
9. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 9 — Self-checks

Before delivering output, verify:

- [ ] Group revenue tested at the consolidated group level, not the local entity.
- [ ] In-scope services tested against the specific country scope (not assumed by analogy).
- [ ] User-location attribution applied per the country's prescribed indicators.
- [ ] Country-specific allowances (e.g., UK GBP 25m) deducted before rate applied.
- [ ] Loss / safe harbour relief considered (UK margin-based alternative).
- [ ] Currency translation method per country.
- [ ] Payment-on-account schedule plotted.
- [ ] India advertising EL handled at withholding level by Indian payor.
- [ ] Canada retrospective period payment recognised separately from current year.
- [ ] Pillar One Amount A status checked before relying on long-term DST liability.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 10 — Prohibitions

- **Do not** assume an exemption from VAT/GST means DST does not apply — they are independent regimes.
- **Do not** allocate revenue using a single country's attribution method to compute another country's DST.
- **Do not** treat the OECD Pillar One IF statement as a binding sunset until Amount A actually enters into force.
- **Do not** advise on structuring to escape DST scope (e.g., moving the contracting entity outside the group) without confirming anti-avoidance rules in each affected country.
- **Do not** ignore the retroactive Canada DST liability for calendar 2022 and 2023 — it is due regardless of any going-forward Pillar One outcome.

## Section 11 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. DST regimes change with each national budget and the Pillar One political process. Every output must be reviewed and signed off by a credentialed practitioner in each source country before any DST return is filed.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
