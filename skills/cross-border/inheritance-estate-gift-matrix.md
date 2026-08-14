---
name: inheritance-estate-gift-matrix
description: "Use this skill whenever an executor, donor, donee, or beneficiary asks about inheritance tax (IHT), estate tax, or gift tax across jurisdictions. Trigger on phrases like \"inheritance tax\", \"IHT\", \"estate tax\", \"gift tax\", \"Erbschaftsteuer\", \"Schenkungsteuer\", \"droits de succession\", \"imposta sulle successioni\", \"impuesto sucesiones donaciones\", \"ISD\", \"ISD Spain\", \"Spanish inheritance tax regional\", \"IRPH\", \"Form 706\", \"Form 709\", \"DSU\", \"résidence fiscale du défunt\", \"EU Succession Regulation 650/2012\", \"trust deemed UK domicile\", \"step-up basis\", \"carryover basis\", \"agricultural property relief\", \"business property relief\", \"spousal exemption\", \"intercohabitant exemption\", or any request to compute inheritance, estate, or gift tax in any jurisdiction. Maps in-force regimes globally with relationship-based rate schedules, exemptions, reliefs, and cross-border situs rules. Does NOT cover: probate procedure, trust administration beyond tax mechanics, will drafting, or income tax on inherited assets (see country income tax skills). ALWAYS read this skill before computing transfer-on-death or inter-vivos gift tax."
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

# Inheritance Estate Gift Matrix

## Inheritance / Estate / Gift Tax Matrix v0.1

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It maps the world's principal transfer taxes on death and gift, as of mid-2025.

**Tax year coverage.** Current for **calendar 2025**, reflecting:
- **US OBBBA** (P.L. 119-21, July 2025) — confirms unified gift / estate / GST exemption at USD 13.99m (2025), rising to ~USD 15m per OBBBA's permanent extension of TCJA increase
- **UK IHT** — frozen nil-rate band at GBP 325,000 and residence nil-rate band at GBP 175,000 through April 2030; **domicile concept replaced by long-term residence from 6 April 2025** under FA 2025
- **German Erbschaftsteuer** — Bundesfinanzhof July 2024 ruling on business property relief constitutionality; rates and brackets per ErbStG as last amended
- **French droits de succession** — unchanged rates; Pacte Dutreil at 75% reduction
- **Spanish ISD** — strong regional variation; some autonomous communities (Andalucía, Madrid) effectively reduce to 0% via rebates; national surcharge mechanics
- **Italian successioni** — generous spouse / child exemptions; ongoing parliamentary discussion of rate increases

**The reviewer is the customer of this output.** Cross-border succession is one of the most error-prone areas of practice. Every output must be reviewed by a credentialed local tax / estate planning practitioner before any return is filed.

## Section 1 — Scope statement

This skill covers:

- **Inheritance tax** (paid by beneficiary) — German, French, Spanish, Italian, Belgian, Dutch, Japanese model
- **Estate tax** (paid by estate) — US, UK model
- **Gift tax** — unified with estate/inheritance (US) or separate (FR, DE)
- **Generation-Skipping Transfer (GST) tax** — US-specific
- **Cross-border situs rules** and double taxation treaties (limited bilateral coverage)

This skill does NOT cover:

- **Probate procedure** and grant-of-representation mechanics
- **Trust administration tax** beyond a reference
- **Will drafting** and conflicts of law (e.g., EU Succession Regulation 650/2012 forum rules)
- **Income tax on inherited assets** post-death — see country income tax skills

## Section 2 — United States (federal estate, gift, GST)

### 2.1 Unified exemption (2025)

- **Basic exclusion amount (BEA)** — USD 13,990,000 USD (per individual (2025))  _([T1] Per OBBBA (P.L. 119-21))_
- **BEA rising** — ~USD 15,000,000 USD (from 2026 under OBBBA's permanent extension)  _([T1] Per OBBBA (P.L. 119-21))_
- **Portability** — Married couple portability: surviving spouse can use deceased spouse's unused exclusion (DSUE)  _([T1] Per OBBBA (P.L. 119-21))_
- **GST exemption** — same amount as BEA  _([T1] Per OBBBA (P.L. 119-21))_

### 2.2 Rate

- **Top estate/gift/GST rate** — 40% % (flat top rate above the exemption (graduated brackets 18-40% but most transfers hit the top rate due to lifetime exhaustion of lower brackets via prior gifts))  _([T1])_

### 2.3 Annual gift exclusion

- **Annual gift exclusion** — USD 19,000 USD (per donor per donee for 2025 (indexed))
- **Spousal annual exclusion for non-US-citizen spouse** — USD 190,000 USD (2025; raised from USD 175k)
- **Educational and medical exclusion** — unlimited if paid directly to institution

### 2.4 Marital and charitable deductions

- **Marital deduction** — Unlimited marital deduction for US citizen spouse
- **Charitable deduction** — Unlimited charitable deduction for qualified §501(c)(3) recipients

### 2.5 Non-US residents (estate)

- **NRA situs assets subject to estate tax** — US-situs assets subject to estate tax (real estate in US, US-domiciled corporation shares including foreign corporation US-business income, tangible personal property in US)  _([T1] Non-resident aliens (NRAs))_
- **NRA exemption** — USD 60,000 USD (treaty may increase)  _([T1] Non-resident aliens (NRAs))_
- **NRA top rate** — 40% %  _([T1] Non-resident aliens (NRAs))_
- **Treaties** — Treaties exist with: Australia, Austria, Canada (under §2056A protocol), Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, Netherlands, Norway, South Africa, Sweden, Switzerland, UK  _([T1] Non-resident aliens (NRAs))_

### 2.6 Filing

- **Form 706** — Estate
- **Form 706-NA** — Non-Resident Alien Estate
- **Form 709** — Gift
- **Filing deadline** — 9 months from date of death (estate); 15 April following year of gift
- **DSUE election** — must be made on a Form 706 even if no tax due

### 2.7 Step-up in basis (income tax interaction)

- **§1014 step-up in basis** — inherited assets receive a step-up in basis to FMV at date of death. Critical for capital gains planning. Note: some carryover basis rules apply where modified estate tax regime elected.  _([T1] §1014)_

## Section 3 — United Kingdom — Inheritance Tax (IHT)

### 3.1 Major reform: domicile → long-term residence (6 April 2025)

- **FA 2025 domicile replaced by long-term residence (LTR)** — **Long-term resident**: UK tax resident in at least 10 of preceding 20 years. **Long-term residents are subject to IHT on worldwide assets** for 10 years after losing LTR status. **Non-LTR individuals**: IHT on UK-situs assets only. Previously, non-UK domiciled individuals could shelter foreign assets via "excluded property trusts" — these largely lose their effectiveness for individuals settling after 6 April 2025.  _([T1] FA 2025)_

### 3.2 Rates and exemptions

- **Nil-rate band (NRB)** — GBP 325,000 GBP (frozen through April 2030)  _([T1])_
- **Residence nil-rate band (RNRB)** — GBP 175,000 GBP (for qualifying residential property passing to direct descendants (tapered above estates of GBP 2m))  _([T1])_
- **Spousal exemption** — unlimited (UK-domiciled or LTR spouse); GBP 325,000 limit for non-LTR/non-domiciled spouses  _([T1])_
- **Charitable exemption** — unlimited  _([T1])_
- **Standard rate** — 40% % (above NRB (and RNRB) — reduced to 36% if 10%+ of net estate goes to charity)  _([T1])_
- **Lifetime gift rate** — 20% % (if chargeable lifetime transfer; 40% on death within 7 years subject to taper (the "7-year rule"))  _([T1])_

### 3.3 Reliefs

- **Agricultural Property Relief (APR)** — 100% for owner-occupied farmland (50% for tenanted); post-April 2026 cap of GBP 1m of combined APR + BPR before the rate halves
- **Business Property Relief (BPR)** — 100% for unquoted trading business shares; 50% for quoted controlling shareholdings; same GBP 1m cap from April 2026
- **Quick succession relief** — tapered for transfers within 5 years

### 3.4 Filing

- **Form IHT400** — estate exceeding NRB
- **Form IHT205** — smaller estates
- **IHT due date** — 6 months from end of month of death
- **Form C5** — for Scotland confirmation

## Section 4 — Germany — Erbschaftsteuer / Schenkungsteuer

### 4.1 Three classes of beneficiary

**Three classes of beneficiary (ErbStG §15)**  _([T1] ErbStG §15)_

| Class | Relationship |
| --- | --- |
| **I** | Spouse, registered partner, children, stepchildren, grandchildren, parents (on death only) |
| **II** | Siblings, nieces/nephews, in-laws, divorced spouses, parents on lifetime gift |
| **III** | All others |

### 4.2 Personal exemptions

**Personal exemptions (§16 ErbStG)**  _([T1] §16 ErbStG)_

| Beneficiary | Exemption |
| --- | --- |
| Spouse / registered partner | EUR 500,000 |
| Children (per child) | EUR 400,000 |
| Grandchildren (per child) | EUR 200,000 |
| Parents (death only) | EUR 100,000 |
| Class II | EUR 20,000 |
| Class III | EUR 20,000 |

- **Renewal** — Per donor per beneficiary; renews every 10 years.

### 4.3 Rates

**Rates (§19 ErbStG — graduated by amount and class)**  _([T1] §19 ErbStG)_

| Net amount (after exemption) | Class I | Class II | Class III |
| --- | --- | --- | --- |
| ≤ EUR 75,000 | 7% | 15% | 30% |
| ≤ EUR 300,000 | 11% | 20% | 30% |
| ≤ EUR 600,000 | 15% | 25% | 30% |
| ≤ EUR 6,000,000 | 19% | 30% | 30% |
| ≤ EUR 13,000,000 | 23% | 35% | 50% |
| ≤ EUR 26,000,000 | 27% | 40% | 50% |
| > EUR 26,000,000 | 30% | 43% | 50% |

### 4.4 Business property relief (§§13a, 13b ErbStG)

- **Verschonungsabschlag (relief deduction)** — 85% standard relief for qualifying business assets (Regelverschonung); 100% optional relief (Optionsverschonung) if administrative-asset ratio ≤ 20%; Holding-period and payroll requirements (5 years for 85%; 7 years for 100%); BFH 27 May 2024: confirmed need for partial restriction on company-size grounds; transitional rules pending  _([T1] §§13a, 13b ErbStG)_

### 4.5 Filing

- **Erbschaftsteuererklärung** — due 3 months after notification (Finanzamt typically requests within 4-6 months of death)
- **Schenkungsteuererklärung** — due 3 months after gift becomes known to Finanzamt

## Section 5 — France — Droits de succession / donation

### 5.1 Relationship-based rates

- **Spouse / PACS partner** — 100% exempt on death.  _([T1] CGI Article 777)_

**Children, parents (each child / parent has separate allowance + rates)**  _([T1] CGI Article 777)_

| Net portion (after allowance) | Rate |
| --- | --- |
| ≤ EUR 8,072 | 5% |
| ≤ EUR 12,109 | 10% |
| ≤ EUR 15,932 | 15% |
| ≤ EUR 552,324 | 20% |
| ≤ EUR 902,838 | 30% |
| ≤ EUR 1,805,677 | 40% |
| > EUR 1,805,677 | 45% |

- **Siblings** — 35% to EUR 24,430; 45% above.  _([T1] CGI Article 777)_
- **Nieces/nephews** — 55%  _([T1] CGI Article 777)_
- **Cousins or unrelated** — 60%  _([T1] CGI Article 777)_

### 5.2 Allowances

- **Spouse / PACS** — 100% on death; EUR 80,724 on lifetime gift
- **Children, parents** — EUR 100,000 per parent-to-child relationship; renews every 15 years
- **Grandchildren** — EUR 31,865 per donor; renews every 15 years
- **Disabled persons** — additional EUR 159,325
- **Siblings** — EUR 15,932 (life-living-together additional rules)
- **Other relatives / unrelated** — limited

### 5.3 Pacte Dutreil (CGI Article 787 B)

- **75% reduction on the taxable value of qualifying business shares** — 2-year prior commitment to retain shares (held collectively); 4-year individual commitment after transmission; Family member must continue an executive function for 3 years; Reduces effective French succession tax on family businesses by 75%  _([T1] CGI Article 787 B)_

### 5.4 Filing

- **Déclaration de succession** — due 6 months from death (12 months if deceased died abroad); Submitted to local Service de l'enregistrement; Payment terms: 5-10 years installment for family businesses

## Section 6 — Spain — Impuesto sobre Sucesiones y Donaciones (ISD)

### 6.1 Highly variable by autonomous community

- **Regional administration** — ISD is regulated nationally (Ley 29/1987) but administered by each Comunidad Autónoma, which can modify allowances, rates, and rebates. Some autonomous communities effectively eliminate ISD via 99-100% rebates (Madrid, Andalucía, Murcia, Cantabria for Group I/II); others retain full national rates.  _([T1])_

### 6.2 National default schedule

**Four groups of relationship**  _([T1])_

| Group | Relationship |
| --- | --- |
| I | Descendants < 21 |
| II | Descendants ≥ 21, ascendants, spouse |
| III | Siblings, in-laws, nieces/nephews, ascendants/descendants by affinity |
| IV | All others |

- **National default allowances (modified by autonomous communities)** — Group I: EUR 15,956 + EUR 3,990 per year < 21 (max EUR 47,858); Group II: EUR 15,956; Group III: EUR 7,993; Group IV: 0; Disabled persons: EUR 47,859 (≥33% disability) or EUR 150,253 (≥65% disability)  _([T1])_
- **National default rate schedule** — CC: 7.65% to 34% with multipliers by Group; effective top rate ~81.6% for Group IV taxpayers  _([T1])_

### 6.3 Major reliefs

- **Business inheritance** — 95% reduction (national) when relevant inheritance taxes apply; conditional on continuation
- **Habitual residence** — 95% reduction up to certain limits
- **Family operations** — pacto sucesorio (heredamientos) in Cataluña and Balearic Islands receives favorable treatment

### 6.4 Regional examples (illustrative; verify current law)

**Regional examples**

| CCAA | Group I/II rebate | Notes |
| --- | --- | --- |
| **Madrid** | 99% rebate on tax due | Effectively eliminates ISD for direct family |
| **Andalucía** | 99% rebate Group I/II | Effective elimination |
| **Murcia** | 99% rebate Group I/II | Effective elimination |
| **Cantabria** | 99% rebate (Group I < 22) | Effective elimination |
| **Cataluña** | Reduced bonificaciones (slow phaseout); 99% rebate Group I/II up to EUR 100k; reduced thereafter | Material tax for large estates |
| **Galicia** | 99% Group I (up to EUR 1m); reduced bonifications above | n/a |

### 6.5 Filing

- **Model 660 and Model 650** — Model 660 (Declaración) and Model 650 (Autoliquidación) of the relevant CCAA; 6 months from death (extendable 6 more months)

## Section 7 — Italy — Imposta sulle successioni

### 7.1 Generous spouse / child exemptions

- **Spouse and direct line** — EUR 1,000,000 exemption each  _([T1] D.Lgs. 346/1990)_
- **Siblings** — EUR 100,000 each  _([T1] D.Lgs. 346/1990)_
- **Other relatives within 4th degree** — 0 exemption  _([T1] D.Lgs. 346/1990)_
- **Disabled beneficiaries** — EUR 1,500,000  _([T1] D.Lgs. 346/1990)_

### 7.2 Rates

**Rates above exemption**

| Relationship | Rate above exemption |
| --- | --- |
| Spouse, direct line | 4% |
| Siblings | 6% |
| Other relatives to 4th degree | 6% |
| Unrelated | 8% |

### 7.3 Filing

- **Dichiarazione di successione** — due 12 months from death; Asset-by-asset valuation with cadastral values for real estate; FMV for movable; Periodic parliamentary discussion of rate increases / threshold reductions

## Section 8 — Belgium, Netherlands, Japan, Denmark, Switzerland

### 8.1 Belgium — three regions

- **Regional inheritance tax** — Inheritance tax is regional (Flanders, Wallonia, Brussels-Capital). Rates vary materially.  _([T1])_
- **Flanders direct-line example** — 3% to EUR 50,000; 9% from EUR 50,000 to 250,000; 27% above EUR 250,000; Spouse exemption for movable property: EUR 50,000  _([T1])_

### 8.2 Netherlands

- **Erfbelasting spouse exemption** — EUR 765,000 EUR (2025, indexed)  _([T1])_
- **Children exemption** — EUR 25,000+ depending on age/disability  _([T1])_
- **Rates** — 10% / 20% (partner & children); 18% / 36% (others to second-degree); 30% / 40% (other)  _([T1])_

### 8.3 Japan

- **Basic exemption** — JPY 30,000,000 + (statutory heirs × 6,000,000)  _([T1] Inheritance Tax Act)_
- **Rates** — 10% to 55% (progressive, graduated by heir's share)  _([T1] Inheritance Tax Act)_
- **Worldwide asset taxation** — Worldwide assets if heir is Japan-resident for ≥ 10 of preceding 15 years  _([T1] Inheritance Tax Act)_

### 8.4 Denmark

- **Spouse exemption** — 100% (boafgift)  _([T1] Bo- og gaveafgift)_
- **Children rate** — 15% above DKK 333,100 (2025)  _([T1] Bo- og gaveafgift)_
- **Other rate** — 36.25%  _([T1] Bo- og gaveafgift)_
- **Gaveafgift on inter-vivos gifts** — 15% gaveafgift on inter-vivos gifts above DKK 76,800  _([T1] Bo- og gaveafgift)_

### 8.5 Switzerland

- **Cantonal/municipal tax; no federal IHT/gift tax** — Cantonal/municipal — federal level no IHT/gift tax. Most cantons exempt direct descendants and spouses. Rates for unrelated persons vary (Schaffhausen, Lucerne historically high; Schwyz, Obwalden, Nidwalden no IHT for direct line).  _([T1])_

## Section 9 — Other notable

**Other notable countries**

| Country | Status |
| --- | --- |
| **Sweden** | IHT and gift tax abolished 2004 |
| **Norway** | IHT abolished 2014 |
| **Austria** | IHT abolished 2008 |
| **Czech Republic, Slovakia, Hungary** | IHT abolished (Slovakia 2004, Hungary 2010, CZ for direct line) |
| **Australia** | No federal IHT/estate tax. Capital gains tax may apply on death depending on asset; small business CGT concessions |
| **Canada** | No estate/gift tax. **Deemed disposition** at FMV on death triggers capital gains tax on terminal T1 |
| **New Zealand** | No estate/gift tax |
| **Singapore** | No estate/gift tax |
| **Hong Kong** | No estate/gift tax |
| **UAE** | No estate/gift tax |
| **India** | No central IHT. Gift tax abolished 1998. Gifts > INR 50k generally treated as recipient's taxable income unless exempt category (relatives, marriage, will, inheritance) |
| **China** | Periodic IHT proposals; never enacted |
| **South Africa** | Estate Duty Act: 20% (up to ZAR 30m); 25% above. Donations Tax: same rates |
| **Brazil** | State-level ITCMD: 1-8% (varies by state) on death and inter-vivos gifts |
| **Mexico** | No federal IHT/gift. Gifts > 10% UMA × annual minimum days exempt to direct family |
| **Argentina** | Provincial IHT in Buenos Aires only (1.6-6.4%); other provinces have abolished |
| **South Korea** | High graduated rates: 10% to 50% on death; specific gift tax to 50% |

## Section 10 — Cross-border situs and double taxation

### 10.1 Situs rules (general)

- **General situs rules** — Most jurisdictions tax: Worldwide assets if the deceased was a tax/domicile resident; Local-situs assets only if non-resident/non-domiciled; Real estate ALWAYS at situs (regardless of deceased's residence) per most treaty practice  _([T1])_

### 10.2 Common situs definitions

**Common situs definitions**

| Asset class | Typical situs |
| --- | --- |
| Real estate | Country where land is located |
| Tangible movable | Country where located at date of death/gift |
| Shares in companies | Country of company's incorporation OR country of share register |
| Bank accounts | Country where bank is located |
| Government bonds | Country issuing the bonds |
| Private equity / unlisted shares | Country of company's residence |
| Cash | Country where cash is held |
| Crypto-assets | Highly debated; commonly attributed to deceased's residence |

### 10.3 Double taxation treaties

- **US bilateral treaties** — Bilateral estate/inheritance tax treaties exist between US with: Australia, Austria, Canada (limited), Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, Netherlands, Norway, South Africa, Sweden, Switzerland, UK  _([T1])_
- **UK bilateral treaties** — UK with: France, Ireland, Italy, India, Netherlands, Pakistan, South Africa, Sweden, Switzerland, US  _([T1])_
- **France bilateral treaties** — France with: Algeria, Austria, Bahrain, Belgium, Cameroon, Canada (Quebec only), Italy, Lebanon, Mauritius, Monaco, US, UK  _([T1])_
- **Germany bilateral treaties** — Germany with: Denmark, France, Greece, Sweden, Switzerland, US  _([T1])_
- **Unilateral relief** — Where no treaty, unilateral relief is usually available (foreign tax credit on the same asset class).  _([T1])_

### 10.4 EU Succession Regulation 650/2012

- **Scope of Regulation 650/2012** — Does NOT cover tax. Governs: Applicable law (residence at death by default; election possible to nationality law); Forum (residence at death); Recognition of grants; European Certificate of Succession. Tax remains national.

## Section 11 — Output specification

The reviewer brief must include:

1. **Decedent / donor profile** — residence, citizenship, domicile/LTR status, prior gift history
2. **Asset inventory** by situs with valuation methodology and supporting documentation
3. **Beneficiary inventory** with relationship classification per jurisdiction
4. **Exemption / allowance schedule** per applicable jurisdiction
5. **Relief schedule** — Agricultural Property Relief, Business Property Relief, Pacte Dutreil, German Verschonung, US marital deduction
6. **Tax computation** per jurisdiction
7. **Double taxation analysis** — credits available, treaty article references
8. **Filing deadlines and forms** per jurisdiction
9. **Step-up in basis analysis** for US-citizen beneficiaries (income tax consequence)
10. **Reviewer questions** — open items flagged as [T2] or [T3]

## Section 12 — Self-checks

- [ ] Domicile / LTR / residence tested per each jurisdiction's specific definition
- [ ] Asset situs determined per each jurisdiction's rules, not assumed by analogy
- [ ] Relationship classification per jurisdiction (Class I-IV in DE; Group I-IV in ES)
- [ ] Exemptions per jurisdiction applied to net not gross
- [ ] Business property reliefs verified for qualifying conditions (active business, holding period, payroll)
- [ ] Charitable and spousal deductions confirmed
- [ ] Treaty foreign tax credits applied where bilateral treaty exists
- [ ] Filing forms and deadlines per jurisdiction plotted
- [ ] US step-up basis recorded for beneficiary income tax planning
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 13 — Prohibitions

- **Do not** assume a country exempts inheritance because there is "no estate tax" — many countries instead tax inherited gains via income tax (Canada deemed disposition; Australia CGT on death).
- **Do not** apply pre-FA-2025 UK domicile rules to FY 2025/26 cases — long-term residence applies from 6 April 2025.
- **Do not** treat Spanish ISD as eliminated nationally because Madrid exempts it — regional variation is the rule, not the exception.
- **Do not** claim US estate tax exemption of USD 13.99m for a non-resident alien — NRA exemption is only USD 60k (treaty-modifiable).
- **Do not** apply Pacte Dutreil or German Verschonung without confirming the holding-period and payroll commitments are sustainable post-transmission.

## Section 14 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Cross-border succession is highly fact-specific and irreversibly affects family wealth. Every output must be reviewed and signed off by credentialed estate planning practitioners in each affected jurisdiction before any return is filed.

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
