---
name: serbia-tax-optimization
description: Use this skill whenever asked about reducing tax in Serbia, tax planning, or legal strategies to minimise tax for an entrepreneur or small company in Serbia, for tax year 2026. Trigger on phrases like "reduce tax Serbia", "paušalno", "flat-rate entrepreneur", "lump-sum tax Serbia", "preduzetnik", "self-employed vs DOO", "Serbia freelancer tax", "save tax Serbia", "tax planning Serbia". This skill covers the choice between the flat-rate (paušalno) entrepreneur regime, the entrepreneur taxed on actual profit (books), the DOO company route and freelance work for foreign clients; the RSD 6,000,000 flat-rate turnover limit; the yearly cap on increases of the flat-rate base; and the disguised-employment (independence test) red line. Out of scope, see serbia-income-tax (computations), serbia-social-contributions, rs-corporate-tax, serbia-vat and rs-cross-border. ALWAYS read this skill before advising on any Serbian tax optimisation.
version: 0.2
jurisdiction: RS
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Serbia Tax Optimization

## Serbia Tax Optimization Skill v0.2

**Tier 2, source-cited draft. Figures for 2026 come from the Ministry of Finance copies of the Službeni glasnik consolidated texts of the Personal Income Tax Act (ZPDG), the Corporate Income Tax Act (ZPDPL) and the Mandatory Social Insurance Contributions Act (ZDOSO), and the Minister's 2026 base notices, all read on 30 October 2026. Figures must agree with `serbia-income-tax`, `serbia-social-contributions` and `rs-corporate-tax`; those skills win if they differ. NOT yet signed off by a Serbian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Serbia |
| Currency | RSD (dinar) |
| Headline lever | **Paušalno** (flat-rate) entrepreneur: tax and contributions on a deemed income set by the Tax Administration, not on real profit; only a turnover book |
| Self-employment income tax (actual profit or flat-rate) | 10% (ZPDG Art. 38) |
| Corporate tax (DOO) | 15% (ZPDPL Art. 39) |
| Dividends and other capital income of individuals | 15% (ZPDG Art. 64) |
| Contributions | PIO 24%, health 10.3%, unemployment 0.75% (ZDOSO Art. 44(1)); 35.05% in total for an entrepreneur paying for themselves |
| Contribution bases 2026 | Minimum RSD 51,297 a month; maximum RSD 732,820 a month (Minister of Finance notices for 2026) |
| Anti-avoidance | Independence test for single-client entrepreneurs (ZPDG Art. 85(1)(17)); flat-rate eligibility conditions (Art. 40) |

> **The Serbian headline is the PAUŠALNO (flat-rate) entrepreneur:** tax and contributions are paid each month on a deemed income that the Tax Administration sets by decision (rešenje), whatever the real profit. The entrepreneur keeps only a turnover book (ZPDG Art. 43(4)) and files no tax balance. When real profit is well above the deemed income, the effective rate is low. The amount depends on activity, municipality and personal factors (Art. 41), so read it from the client's decision; this skill does not estimate it.

## Section 2 -- Paušalno (flat-rate) Entrepreneur

**Paušalno (flat-rate) Entrepreneur features**

| Feature | Detail |
| --- | --- |
| Turnover limit | Not allowed if turnover in the previous year, or planned turnover for a new business, is **over RSD 6,000,000** (ZPDG Art. 40(2)(4)). Fees taxed under the independence test do not count towards it (Art. 40(5)) |
| Who cannot use it | Advertising and market research; wholesale and retail trade, hotels and restaurants, financial intermediation and real estate; a business in which other people invest; a VAT-registered person (Art. 40(2)). Trade or catering from a kiosk, trailer or similar movable structure can be approved on request (Art. 40(3)); so can a person who makes and sells only their own products (Art. 40(4)) |
| Tax/contributions | Income tax 10% (Art. 38) on the deemed income; contributions on the same deemed income (ZDOSO Art. 22(3)), at 24% + 10.3% + 0.75%, never on less than the minimum base of RSD 51,297 a month (ZDOSO Art. 36). The Tax Administration sets both in its decision and bills through ePorezi |
| How the deemed income is set | Entrepreneurs are grouped by main activity. The starting base is tied to the average monthly salary in the Republic and the municipality, then adjusted for registered seat, time since registration, age and work capacity, and other circumstances (Art. 41(1) to (4)). The Government sets the detail by decree (Art. 41(5)) |
| Bookkeeping | Only the turnover book (knjiga o ostvarenom prometu, KPO) (Art. 43(4)); no tax balance |
| Applying | By **31 October** of the current year for the next year, through the Tax Administration portal; a new business applies only at registration (Art. 42(1) and (2)). For 2027 the deadline is 31 October 2026 |
| Losing it | If the conditions stop being met, the Tax Administration orders books from mid-year or from the next year (Art. 42(4) and (5)). On VAT registration, books are due from that day (Art. 42(6)) |
| Base-growth cap | A Government decree limits how fast the flat-rate base may rise from one year to the next, with exceptions when the activity code or municipality changes. The official text was not read today: see "Not yet confirmed" |

Because the tax is set on a deemed income, when real profit is high the **effective rate is very low**. When real profit is low or negative, the flat-rate amount is still due, and actual-profit taxation can be cheaper.

## Section 3 -- Income-Expenses Regime & DOO

**Route comparison**

| Route | Treatment | Best when |
| --- | --- | --- |
| **Paušalno** | 10% tax and 35.05% contributions on a deemed income set by decision; turnover limit RSD 6,000,000; turnover book only | Profitable solo service work under the limit, in an allowed activity, not VAT-registered |
| **Entrepreneur on actual profit (books)** | 10% on taxable profit from the tax balance (Art. 38). Double-entry books (Art. 43(2)). The entrepreneur may pay themselves a personal salary (lična zarada), which is then a cost and taxed as salary; if not, the contributions they pay for themselves are a cost (Art. 37a). Contribution base: the personal salary, or taxable profit if no salary is paid (ZDOSO Art. 22(1)), within the 2026 minimum and maximum monthly bases | Real expenses high, above the flat-rate limit, in an excluded activity, or VAT-registered |
| **DOO** (company) | 15% corporate tax on taxable profit (ZPDPL Art. 39); tax losses carried forward for up to 5 years (Art. 32). Profit paid out to an individual shareholder as a dividend is taxed at 15% (ZPDG Art. 64), withheld by the company (Art. 99(1)(3)). Full books | Higher profit kept in the business, teams, liability and credibility |
| **Freelancer (contract for work) paid from abroad or by private persons** | Self-assessed each quarter (ZPDG Art. 85(1)(18)). Option 1: 20% on quarterly gross less RSD 110,647 (Art. 85(5)(2)(1), Art. 12b(1), Art. 86(1)). Option 2: 10% on quarterly gross less RSD 66,733 and less 34% of gross (Art. 85(5)(2)(2), Art. 12b(2), Art. 86(2)(2)). Contributions also apply: see `serbia-income-tax` and `serbia-social-contributions` | Occasional or low freelance income without registering a business |

The comparison depends on real profit, the flat-rate decision amount, the salary the entrepreneur would pay themselves and the plan for profits. Run the numbers with the client's figures and the domain skills; do not quote a typical monthly amount.

## Section 4 -- Red Lines (do not cross)

- **Disguised employment risk (independence test)** -- Fees an entrepreneur or flat-rate entrepreneur earns from the same client, or a person related to that client, are taxed as other income if at least five of nine criteria are met, for example: the client sets working hours; at least 70% of income in a 12-month period comes from that client; or the work runs for 130 or more working days in 12 months (ZPDG Art. 85(1)(17)). The base is then the full gross fee with no standard costs (Art. 85(5)(1)) and the rate is 20% (Art. 86(1)), withheld by a Serbian payer (Art. 99(1)(9)). The full list of nine criteria is in `serbia-income-tax`. AUDIT FLASH POINT.
- **Base-growth cap conditions** -- Changing activity code or municipality can trigger a fresh (higher) flat-rate assessment outside the yearly cap. Plan moves deliberately. The decree text was not read today (see "Not yet confirmed").
- **Under-declaration prohibition** -- Never under-declare turnover to stay under RSD 6,000,000. The limit is tested on the previous year's turnover, or on planned turnover for a new business (Art. 40(2)(4)).

## PROHIBITIONS

- **Prohibition 1** -- NEVER present paušalno for what is really single-client employment.
- **Prohibition 2** -- NEVER advise gaming the activity-code or municipality rules purely to suppress the base.
- **Prohibition 3** -- NEVER contradict the rates in `serbia-income-tax`, `serbia-social-contributions` or `rs-corporate-tax`.
- **Prohibition 4** -- NEVER present optimisation as definitive advice; route to a licensed Serbian tax adviser.

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dohodak građana (ZPDG), Ministry of Finance copy of the Službeni glasnik consolidated text up to 80/2026: Arts. 12b, 37a, 38, 40 to 43, 64, 85, 86, 99 | https://www.mfin.gov.rs/propisi/zakon-o-porezu-na-dohodak-gradjana (file https://www.mfin.gov.rs//upload/media/MOq4eO_6aa14ac8c7a47.docx) | 2026-10-30 |
| Zakon o porezu na dobit pravnih lica (ZPDPL), Ministry of Finance copy of the Službeni glasnik consolidated text: Arts. 32 and 39 | https://www.mfin.gov.rs/propisi/zakon-o-porezu-na-dobit-pravnih-lica (file https://www.mfin.gov.rs//upload/media/SByOge_6aa127acd2250.docx) | 2026-10-30 |
| Zakon o doprinosima za obavezno socijalno osiguranje (ZDOSO), Ministry of Finance copy of the Službeni glasnik consolidated text: Arts. 22, 36, 37 and 44 | https://www.mfin.gov.rs/propisi/zakon-o-doprinosima-za-obavezno-socijalno-osiguranje (file https://www.mfin.gov.rs//upload/media/c59gCf_6aa14bd2e2c04.docx) | 2026-10-30 |
| Minister of Finance, lowest monthly contribution base for 2026, RSD 51,297 | https://www.mfin.gov.rs//upload/media/nATlw2_69429ec84247a.docx | 2026-10-30 |
| Minister of Finance, highest monthly contribution base for 2026, RSD 732,820 | https://www.mfin.gov.rs//upload/media/mYTnAm_6942704946245.docx | 2026-10-30 |

Not yet confirmed: the Government decree on flat-rate taxation (Uredba o bližim uslovima, kriterijumima i elementima za paušalno oporezivanje), including the rule that the flat-rate base may rise by no more than 10% a year and the year it runs to (the old version said "extended to end-2027"), and its exception for a change of activity code or municipality: only a commercial database copy was found today, not the Službeni glasnik text; typical monthly flat-rate amounts (the old version said about EUR 250 to 400 a month; no official source, and the amount depends on each decision); the EUR equivalent of RSD 6,000,000 (the old version said about EUR 50,000); the old statement that entrepreneurs on books pay contributions "on 60% of a self-set salary" (not found in ZDOSO Art. 22, which uses the personal salary or the taxable profit); how flat-rate income and freelance income from abroad enter the annual personal income tax.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Serbia) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
