---
name: albania-tax-optimization
description: "Use this skill whenever asked about reducing tax in Albania, tax planning, or legal strategies to minimise tax for a self-employed person or small business in Albania, for tax year 2026. Trigger on phrases like 'reduce tax Albania', '0% tax small business Albania', 'simplified profit tax', 'freelancer Albania', 'self-employed vs company Albania', 'save tax Albania', 'tax planning Albania'. This skill covers the 0% rate for traders, the self-employed and entities with gross income up to ALL 14m (to 2029, Law 29/2023 art. 69(1)(dh)), the repeal of the old simplified profit tax, the freelancer single-client reclassification rule, the standard rates above the threshold, the 2026 social and health contribution floor that still applies at 0%, and the anti-avoidance red lines. Out of scope: full income tax computation (albania-income-tax), companies (al-corporate-tax), VAT (albania-vat), contributions in detail (albania-social-contributions). ALWAYS read this skill before advising on any Albanian tax optimisation."
version: 0.4
jurisdiction: AL
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Albania Tax Optimization

## Albania Tax Optimization Skill v0.4

Albania Tax Optimization Skill v0.4, tax year 2026.

**Tier 2. Sources: Law No. 29/2023 on income tax, consolidated to Law No. 81/2025 of 11.12.2025, as published by the General Directorate of Taxes ([tatime.gov.al](https://tatime.gov.al/wp-content/uploads/2026/09/Ligj-Nr.-29-2023-Per-Tatimin-mbi-te-Ardhurat-i-ndryshuar.pdf), read 2026-10-30); for the VAT threshold Council of Ministers Decision No. 953/2014 art. 11 ([tatime.gov.al](https://tatime.gov.al/wp-content/uploads/2026/09/VKM-Nr.953-date-29.12.2014-i-ndryshuar.pdf), read 2026-10-30); for contributions Council of Ministers Decision No. 77/2015 and the General Directorate of Taxes notice of 14.01.2026 (see Sources). Figures must agree with `albania-income-tax.md` / `albania-social-contributions.md`. NOT yet signed off by an Albanian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Albania |
| Currency | ALL (lek) |
| Tax year | Calendar year; this skill is for 2026 |
| Headline lever | **0% income tax** for individual traders, the self-employed and entities with gross income ≤ **ALL 14,000,000** a year, until 31 Dec 2029 (Law 29/2023 art. 69(1)(dh)) |
| Above the threshold | Traders and self-employed: 15% of taxable profit up to ALL 14,000,000, 23% above (art. 24(2)). Entities: 15% (art. 41) |
| VAT threshold | ALL 10,000,000 turnover a year (VKM 953/2014 art. 11(1)); voluntary registration only above ALL 5,000,000; see `albania-vat` |
| Self-employed contributions, 2026 | Social 23% of a base of at least ALL 50,000 a month (ALL 11,500) plus health 3.4% of ALL 100,000 (ALL 3,400): at least ALL 14,900 a month, due even at the 0% rate; see `albania-social-contributions` |
| Annual return | By 31 March of the following year (art. 61(2)) |
| Anti-avoidance | Freelancer single-client reclassification rule (art. 12(1)(ç)) |

> **Albania's headline is a temporary 0% rate:** individual traders, the self-employed and entities with **gross income up to ALL 14,000,000 a year** pay **0% income tax until 31 December 2029** (Law 29/2023 art. 69(1)(dh)). It is a threshold, not a band: above ALL 14,000,000 of gross income there is no 0% at all.

## Section 2 -- The 0% Small-Business Regime

- **0% rate**: individual traders, the self-employed and entities with gross income up to ALL 14,000,000 a year pay 0% on the whole business profit until 31 Dec 2029. The test is gross income, not profit.  _(Law 29/2023 art. 69(1)(dh); see `albania-income-tax`)_
- **Old simplified profit tax**: repealed. It sat in Chapter III of Law No. 9632/2006 on local taxes, which Law 29/2023 art. 71(2) repealed; the art. 69(1)(dh) 0% rate is the small-business regime now. Art. 69(1)(e) only kept the old forms for the 2024 tax period.  _(Law 29/2023 arts. 69(1)(e), 71(2))_
- **Above ALL 14,000,000 of gross income**: individual traders and the self-employed pay 15% on taxable profit up to ALL 14,000,000 and 23% on taxable profit above it, with no part of the profit at 0%. Entities pay corporate income tax at 15% (see `al-corporate-tax`).  _(Law 29/2023 arts. 24(2), 41)_
- **Company route**: an entity pays 15% on its profit above the threshold, and dividends it pays to an individual are taxed at 8% with no costs deducted (see `al-corporate-tax`, `albania-income-tax`).  _(Law 29/2023 arts. 24(3)(a), 24(4), 41)_
- **After 2029**: art. 69(1)(dh) ends on 31 December 2029. Unless the law is changed, from 2030 business profit falls under the art. 24(2) scale (individuals) or the art. 41 rate (entities).  _(Law 29/2023 arts. 24(2), 41, 69(1)(dh))_

This makes Albania extremely efficient for profitable solo/micro service businesses under the cap, but social and health contributions (at least ALL 14,900 a month in 2026 for a self-employed person, see `albania-social-contributions`) and VAT (mandatory above ALL 10m of turnover, see `albania-vat`) still apply.

## Section 3 -- The Freelancer Single-Client Rule (key constraint)

- **Single client**: income of a self-employed individual is employment income if 80% or more of it comes, directly or indirectly, from one client.  _(Law 29/2023 art. 12(1)(ç)(i))_
- **Few clients**: the same applies if 90% or more of total income comes from fewer than three clients.  _(Law 29/2023 art. 12(1)(ç)(ii))_
- **Self-declaration exception**: the rule does not apply if the person declares, on the self-employed status declaration (model in Annex 1 to the law), filed with the regional tax directorate together with the annual business income return within March, that they are not in an employment situation. The declaration is an assessment tool: the tax administration can still reclassify the income under the tax procedures law if it finds tax avoidance.  _(Law 29/2023 art. 12(1)(ç), paragraph added by Law 81/2025; Annex 1; see `albania-income-tax`)_
- **Non-resident exception**: the rule does not apply where the self-employed person supplies services only to non-residents of Albania or only to entities without an Albanian permanent establishment. The income is then business income.  _(Law 29/2023 art. 12(1)(ç), last paragraph)_

> **AUDIT FLASH POINT.** A single-client "freelancer" is the primary reclassification target. If the 80% or 90% test is met and neither exception applies, the income is taxed as employment income on the art. 24(1) scale (13% on an annual taxable base up to ALL 2,040,000, 23% above), not at the 0% business rate. File the status declaration in March only where the facts support it (own equipment, own hours, own financial risk), and keep the evidence.

## Section 4 -- Red Lines (do not cross)

- **Single-client / few-client reclassification**: the main risk (Section 3).
- **Mandatory VAT registration**: VAT registration is mandatory once turnover goes above ALL 10m in a calendar year or any 12 consecutive months, with the request due within 15 days of the end of the month in which the threshold is passed (VKM 953/2014 art. 11(1); Law 92/2014 art. 122(1)); don't ignore it. Notaries and bailiffs register whatever their turnover (VKM 953/2014 art. 11(2)).
- **Time-limited regime**: The 0% regime is time-limited (to 2029) and income-capped; model the cliff at ALL 14m and the 2030 reversion.
- **No fragmentation without substance**: Don't fragment one business across entities to stay under the cap without substance.

## PROHIBITIONS

- **Prohibition 1**: NEVER present the 0% regime without the ALL 14m cap and the 2029 sunset.
- **Prohibition 2**: NEVER present single-client freelancing as safe self-employment (unless the non-resident exception applies, or the person files a self-employed status declaration that the facts support, art. 12(1)(ç)).
- **Prohibition 3**: NEVER ignore the ALL 10m VAT registration threshold or the self-employed contributions (at least ALL 14,900 a month in 2026).
- **Prohibition 4**: NEVER contradict the rates in `albania-income-tax.md` / `albania-social-contributions.md`.
- **Prohibition 5**: NEVER present [RESEARCH GAP] or "Not yet confirmed" points as confirmed, nor optimisation as definitive advice. Route to a licensed Albanian tax adviser.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Law No. 29/2023 "Për tatimin mbi të ardhurat", consolidated to Law No. 81/2025 (arts. 12, 24, 41, 61, 69, 71, Annex 1), General Directorate of Taxes | https://tatime.gov.al/wp-content/uploads/2026/09/Ligj-Nr.-29-2023-Per-Tatimin-mbi-te-Ardhurat-i-ndryshuar.pdf | 2026-10-30 |
| Council of Ministers Decision No. 953/2014 on the VAT law, consolidated (art. 11, registration threshold) | https://tatime.gov.al/wp-content/uploads/2026/09/VKM-Nr.953-date-29.12.2014-i-ndryshuar.pdf | 2026-10-30 |
| Law No. 92/2014 "Për tatimin mbi vlerën e shtuar", consolidated (art. 122) | https://tatime.gov.al/wp-content/uploads/2026/09/Ligji-Nr.-92-2014-Per-tatimin-mbi-vleren-e-shtuar-ne-Republiken-e-Shqiperise-i-ndryshuar.pdf | 2026-10-30 |
| Council of Ministers Decision No. 77/2015 on compulsory social and health contributions, consolidated (ch. III paras. 6, 7), ISSH copy | https://www.issh.gov.al/wp-content/uploads/2026/08/VENDIM-NR.-77-DATE-28.1.2015-PER-KONTRIBUTET-E-DETYRUESHME-DHE-PERFITIMET-NGA-SISTEMI-I-SIGURIMEVE-SHOQERORE-DHE-SIGURIMI-I-KUJDESIT-SHENDETESOR.pdf | 2026-10-30 |
| General Directorate of Taxes notice "Nga 1 janari 2026, rritet paga minimale dhe maksimale" (14.01.2026) | https://tatime.gov.al/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale/ | 2026-10-30 |

Not yet confirmed: which article of Law 9920/2008 on tax procedures the tax administration would use to aggregate a business split across entities without substance (the fragmentation red line is a planning caution, not a quoted rule); whether income from more than one activity of the same person is added together for the ALL 14,000,000 gross income test; whether the self-employed person's own contributions are deductible in computing business income; whether the 0% rate will be extended past 31 December 2029.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Albania) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Michael Cutajar.

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
