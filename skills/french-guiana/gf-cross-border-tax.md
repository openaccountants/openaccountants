---
name: gf-cross-border-tax
description: Determine French Guiana cross-border income-tax exposure under French
  law in 2026. Covers French tax residence, Guyane-source income, non-resident minimum-tax
  rules, move-year returns, foreign income and treaty-relief routing. Separates income-tax
  territory from the VAT and octroi borders and demonstrates territorial applicability
  with the actual France-Brazil treaty. Use for Guyane resident abroad, non-resident
  French Guiana income, cross-border employment, Brazil short stays, permanent establishment,
  foreign-tax credit and 2047 reporting. This is a residence and source decision workflow,
  not a blanket treaty-rate table. Includes ordinary non-resident wage, service, royalty and dividend withholding. Exit-tax filings and specialist pensions or offshore income require the separately identified current-law work.
jurisdiction: GF
category: cross-border
type: situation-rules
domain: tax
tax_year: 2026
tier: 2
last_updated: '2026-11-11'
version: '0.1'
---

# French Guiana cross-border income tax 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals arriving in, leaving or earning outside Guyane, businesses operating across borders, and a person paying overseas. Guyane belongs to France for ordinary income/company tax; its separate VAT/octroi treatment does not make a mainland transfer international income. [DGFiP DOM guidance](https://www.impots.gouv.fr/professionnel/impots-professionnels-dom); [BOFiP corporate territoriality, I](https://bofip.impots.gouv.fr/bofip/4262-PGP.html).

Quick answer: classify residence, income type, source and applicable treaty before computing; distinguish ordinary withholding from final annual assessment. Do not extend a treaty to every French overseas territory without reading its definition of France.

## Rates, bands and thresholds

| Rule | Amount or condition | Official source |
|---|---|---|
| Domestic individual residence | Home/principal abode, non-accessory professional activity, **or** centre of economic interests in France; applicable treaty non-residence overrides under current art.4 B | [CGI art.4 B(1)](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051202565) |
| Non-resident ordinary minimum on DOM-source income | 14.4% up to the upper limit of the second income-tax band and 20% above, subject to lower proved worldwide average rate and other statutory rules | [CGI art.197 A; DGFiP](https://www.impots.gouv.fr/particulier/le-calcul-de-votre-impot) |
| Current 2026 assessment dividing point | EUR 29,579 for 2025 income assessed in 2026; do not call it a final future 2027 assessment threshold | [DGFiP](https://www.impots.gouv.fr/particulier/le-calcul-de-votre-impot), [art.197](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006308332/) |
| Brazil employment short-stay | At most 183 days in the fiscal year, non-host employer and no host PE/fixed base bearing remuneration, all together | [France-Brazil art.15(2)](https://www.impots.gouv.fr/sites/default/files/media/10_conventions/bresil/bresil_convention-avec-le-bresil_fd_1799.pdf) |

### Ordinary non-resident withholding in 2026

| Payment | Domestic rule before proved treaty relief | Official source |
|---|---|---|
| French-source salary/pension under art.182 A | Guyane rates 0%, 8%, 14.4%; 2026 annual base bands up to EUR 17,275, then through EUR 50,112, then excess | [CGI art.182 A](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373628), [2026 BOI-BAREME-000043](https://bofip.impots.gouv.fr/bofip/13631-PGP.html) |
| Monthly art.182 A bands | Up to EUR 1,440, then through EUR 4,176, then excess; pay-period table, not annual minimum-tax bands | [2026 table](https://bofip.impots.gouv.fr/bofip/13631-PGP.html) |
| Quarterly / weekly / daily art.182 A boundaries | EUR 4,319 / 12,528; EUR 332 / 964; EUR 55 / 161, respectively | [2026 table](https://bofip.impots.gouv.fr/bofip/13631-PGP.html) |
| Ordinary service/royalty art.182 B | 25% normal corporate rate, generally gross, subject to payer/activity/beneficiary/source conditions below and treaty | [CGI arts.182 B, 219](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179576/), [BOFiP §§20-100](https://bofip.impots.gouv.fr/bofip/2280-PGP.html) |
| Qualifying EU/EEA company art.182 B base | 10% charges allowance where results not taxed through an individual partner, qualifying recipient seat/PE includes income, assistance agreement and non-ETNC conditions met; not for individuals | [Art.182 B I bis](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179576/), [BOFiP §70](https://bofip.impots.gouv.fr/bofip/2280-PGP.html) |
| Dividend to identified non-resident individual beneficial owner | 12.8%, subject to treaty and ETNC rules; not ordinary resident PFU/social rates | [CGI art.187](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179576/), [BOFiP §§10-15](https://bofip.impots.gouv.fr/bofip/2674-PGP.html) |
| Ordinary dividend to non-resident company | 25% normal corporate rate, subject to treaty/statutory exemptions; qualifying EU/EEA non-profit rate is 15% under its separate conditions | [CGI arts.187, 219](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179576/), [BOFiP §20](https://bofip.impots.gouv.fr/bofip/2674-PGP.html) |
| Covered non-salary art.182 B / dividend payment into specified ETNC case | 75% only within the respective statute's scope and exclusions, with genuine-operation/non-fraud safeguard and applicable treaty; not every foreign payment | [Arts.182 B III, 187(2)](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179576/), [BOFiP §§95-97](https://bofip.impots.gouv.fr/bofip/2280-PGP.html) |

For ordinary fixed-income interest paid to a non-resident, do not import the dividend rate: DGFiP describes general French exemption. Article 125 A III instead targets covered French-debtor payments **outside France into an ETNC**, at 75% under III bis, with treaty/safeguard and statutory exclusions. BOFiP defines the payment-location test by the account's establishment; it is not simply the beneficial owner's residence. Section II-A §210 preserves any separately applicable article 119 bis(1) withholding, so legacy/security-specific products need their own classification. Record debt/product, issue date, payer, recipient and payment account before assigning no withholding. [DGFiP, updated March 2026](https://www.impots.gouv.fr/international-particulier/interest); [BOFiP II-A §§80-160, 210](https://bofip.impots.gouv.fr/bofip/12857-PGP.html).

The salary table is **2026 payments**, distinct from 2025 income assessed in 2026. Artist, sport and share-plan special withholding categories need their own rules and are not assigned the ordinary service rate.

The resident Guyane reduction is owned by [gf-income-tax](gf-income-tax.md). It is not an additional discount to apply indiscriminately to a non-resident's minimum-tax calculation. The statute's current bands apply to 2025 and following years as presently enacted, but future annual revaluation must be checked before a 2026-income final return.

## The base

A French-resident individual normally declares worldwide income; a non-resident is taxed on French-source income within domestic and treaty limits. Art.4 B is an alternative-criteria test, not simply a count of days. Its current text expressly prevents domestic residence where a relevant double-tax treaty regards the person as non-resident of France. Record home/family, actual work and economic interests; nationality, passport and a foreign bank account do not decide residence alone. [CGI arts.4 A-4 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051202565); [BOFiP scope](https://bofip.impots.gouv.fr/bofip/1911-PGP.html).

Identify the actual category: employment where duties are exercised, rents/property, business profits, pensions, investment income or gains. Some non-resident earnings have specific withholding under articles 182 A-182 B; the withholding and its final/creditable treatment must be established before applying the ordinary minimum method. Do not deduct the same withholding twice or turn a treaty maximum into a standalone tax. [DGFiP calculation guidance](https://www.impots.gouv.fr/particulier/le-calcul-de-votre-impot).

### Operate the right withholding regime

The 2026 form conditions DOM 8%/14.4% on activity exercised in the DOM or pension instalment payment there. For a non-standard payment period use the daily salary or weekly pension table, counting part of a day/week as one. Columns 9 and 10 tax round to the nearest euro. No deduction is made where calculated withholding for a given month is below EUR 8 per beneficiary. [2494 notes 4-6](https://www.impots.gouv.fr/sites/default/files/formulaires/2494-sd/2026/2494-sd_5450.pdf).

For ordinary salary use taxable net before withholding and the normal professional-expense deduction, not actual-cost deduction; the 2026 2494 instructions use the normal 10% salary deduction. Benefits can enter taxable pay. Test French-source duties and treaty exemption before withholding; the payment location alone is not the source. Article 182 A is **RAS NR**, separate from resident PAS. DGFiP explains the lower-band fraction's final treatment: the fraction subject to 0%/8% in a DOM is not included again in annual progressive income and its withholding is not credited again; the upper 14.4% fraction is assessed with other relevant income and that withholding is credited. Article 197 B refund relief and multiple-payer regularisation remain relevant. The DGFiP explanatory page's numeric example is for 2025; use the separate 2026 band source above. [CGI arts.182 A, 197 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006303131); [DGFiP treatment](https://www.impots.gouv.fr/international-particulier/questions/je-suis-non-resident-je-veux-comprendre-la-retenue-la-source-qui); [2026 form notes](https://www.impots.gouv.fr/sites/default/files/formulaires/2494-sd/2026/2494-sd_5450.pdf).

Article 182 B applies when a debtor exercising activity in France pays a person/company with no permanent professional installation in France for covered professional work in France, royalties/IP or services provided/used in France. Do not treat every overseas invoice as covered, or confuse the domestic installation test with a treaty PE. Default base is gross payment excluding turnover tax; ordinarily no cost deduction, except the qualifying-company allowance above. If the payer bears withholding, gross up: at the ordinary 25% rate tax is net promise × 25/75. Treaty business-profit/royalty articles and qualifying associated-company royalty exemption under article 182 B bis can remove/reduce withholding only with their actual status, ownership, beneficial-ownership, holding and anti-abuse conditions proved. [CGI arts.182 B/B bis](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179576/); [BOFiP §§10-100](https://bofip.impots.gouv.fr/bofip/2280-PGP.html).

Dividend relief requires the actual beneficial owner, residence proof and statutory/treaty conditions, including applicable article 119 ter parent-company exemption. Unidentified beneficial ownership can require the company-rate default. From 1 January 2026, article 119 bis A II changes procedure for treaties giving an unconditional zero/no withholding rate: within its scope apply domestic withholding at payment and claim refund later, rather than automatic treaty-zero at source. The authority distinguishes status/participation-based exemptions. Refund support includes residence form 5000, dividend form 5001, the withholding/payment chain, beneficial-owner declaration and corporate activity/acquisition facts where relevant. [BOFiP 16 March 2026 §§1-50](https://bofip.impots.gouv.fr/bofip/14878-PGP.html); [ordinary rates/identity](https://bofip.impots.gouv.fr/bofip/2674-PGP.html).

For a resident's foreign income, the treaty article controls relief. Depending on its wording, relief may be a credit equal to French tax on that income, a foreign-tax credit with a cap, or exemption with progression. Collect gross income, foreign tax and net receipts; apply the treaty and relevant return instructions. Keep the tax certificate, payment/refund evidence and actual-beneficiary details. Certain exemption-with-progression salary/pension reporting uses net-after-foreign-tax amounts; do not force the credit method's base onto it. An income-tax convention does not automatically cover social contributions or octroi. [DGFiP 2026 brochure, foreign-income and non-resident sections](https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_integral/Brochure-IR-2026.pdf).

For companies, France's territorial business-profit rules govern; do not import an individual worldwide-income rule. A treaty PE analysis depends on the convention, fixed place, agents and activity. Use [gf-corporate-income-tax](gf-corporate-income-tax.md) for the domestic base and [gf-transfer-pricing](gf-transfer-pricing.md) for foreign controlled parties. [BOFiP I-II](https://bofip.impots.gouv.fr/bofip/4262-PGP.html).

## Deadlines and filing

1. Establish residence and exact move date, and split pre/post-move income. For departure, ordinary resident income is generally reported up to departure and only taxable French-source income after it. Check treaty overrides separately. [DGFiP non-resident notice](https://www.impots.gouv.fr/international-particulier/questions/comment-comprendre-mon-avis-dimposition).
2. Log in to the personal space at impots.gouv.fr. Use 2042 with 2042-NR where required for post-departure French-source income, 2047 for foreign-source income, and the relevant category schedules. Use the currently issued form for that income year; do not invent 2027 box numbers.
3. If requesting the lower worldwide average rate, disclose the complete worldwide income and required household/foreign-tax evidence. It applies only to taxable French-source income, not as a demand for French tax on all foreign income. Preserve the evidence and electronic acknowledgement.
4. Reconcile foreign-tax credits and withholding to the assessment and pay on the actual notice date. Correct foreign tax refunds or amended assessments that change a credit. The 2026 filing season concerns 2025 income; 2026 income is filed in 2027 and its calendar was not yet read.

[DGFiP calculation guidance](https://www.impots.gouv.fr/particulier/le-calcul-de-votre-impot), [2026 brochure, 2042-NR and 2047 sections](https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_integral/Brochure-IR-2026.pdf).

For art.182 A/B withholding, use the current **2494-SD (2026)** and remit by the **15th of the month following the calendar quarter of payment** to the competent payer SIE. The current form requires **one copy**, superseding the older web FAQ's two-copy wording. Enter quarter, payer name/address/SIRET/APE, then beneficiary foreign identity/address, residence state, gross/net-before-withholding amount, taxable base and activity/payment duration. Wage columns 6-8 split base by bands, columns 9-10 compute tax and column 11 total; page 1 recaps wage, artist/sport and other-income sections. For ordinary other income page 4 gives base/rate/tax fields. Sign/date, pay by bank transfer with SIE reference, retain return/receipt and reconcile payroll/annual declarations separately. [2026 original form and notes](https://www.impots.gouv.fr/sites/default/files/formulaires/2494-sd/2026/2494-sd_5450.pdf); [BOFiP §100](https://bofip.impots.gouv.fr/bofip/2280-PGP.html).

For dividend withholding use **2777-SD**, electronically declared and paid within fifteen days after the payment month. On 2026 form section 7, ordinary company dividends use HK (25%) and identified individual dividends HE (12.8%); other status/treaty/ETNC lines are separate. Enter payer identity/SIREN, month, base/rate/tax, totals and any properly supported refund/regularisation, validate and keep acknowledgement/payment reference. Forms 5000/5001 do not themselves prove every exemption. [2026 form, pp1, 3 and section 9](https://www.impots.gouv.fr/sites/default/files/formulaires/2777-sd/2026/2777-sd_5335.pdf).

## Penalties and interest

An unsupported treaty or credit claim can lead to reassessment. Ordinary French reporting, late-payment and deliberate-inaccuracy rules continue; use the quantified general rules in [gf-income-tax](gf-income-tax.md). Treaty residence does not waive filing or automatically extend a claim deadline. The actual notice, income type and relief provision must be read before an appeal or refund claim. The 2026 2494 form warns that paying by cheque instead of required transfer attracts article 1738's 0.2% surcharge, minimum EUR 60; this is a payment-method sanction separate from late payment or underdeclaration. [Form footnote 2](https://www.impots.gouv.fr/sites/default/files/formulaires/2494-sd/2026/2494-sd_5450.pdf). [DGFiP](https://www.impots.gouv.fr/particulier/le-calcul-de-votre-impot).

## Cross-border points

**France-Brazil verified territorial example.** Art.3(1)(a) expressly includes Guyane. Art.4 resolves treaty residence, arts.5-7 govern PE/business profits, and art.15 governs employment. Its short-stay day count is the **fiscal year**, not a generic rolling twelve months. All employer/cost-bearing conditions must also hold. Special directors, government, pension and other articles take priority where specified. [Treaty arts.3-7, 15-19](https://www.impots.gouv.fr/sites/default/files/media/10_conventions/bresil/bresil_convention-avec-le-bresil_fd_1799.pdf). The July 2024 French commentary discusses corporate residence and relief, and should be read with the treaty before calculating a specific Brazilian credit. [BOFiP](https://bofip.impots.gouv.fr/bofip/1736-PGP.html).

| Situation | Next step |
|---|---|
| Mainland-to-Guyane move | French domestic territorial reduction and timing; no presumed international departure |
| Brazil employer but Guyane duties | Test French source and all art.15 conditions, including the actual cost bearer |
| Another foreign treaty partner | Fetch that treaty's territorial, residence, income and relief articles; do not infer from Brazil |
| Non-resident wage, royalty, service fee, dividend or company payment | Determine the applicable domestic withholding and treaty conditions before payment |
| Departure with significant shareholdings | Screen CGI art.167 bis exit-tax separately; no threshold is invented here |

No treaty with Suriname or another state is asserted merely from proximity or nationality. VAT non-application does not remove octroi on goods; use [gf-import-octroi-and-vat](gf-import-octroi-and-vat.md).

## Two worked examples that recompute

**Non-resident minimum calculation layer.** For assumed EUR 40,000 ordinary DOM-source net income within art.197 A and the current 2026 assessment bands, the minimum layer is EUR 29,579 × 14.4% + EUR 10,421 × 20% = EUR 6,343.58. If a properly proved worldwide average rate is 10%, that layer instead gives EUR 4,000. This is the minimum/average-rate comparison, not a complete assessment with special withholding, treaty relief and all deductions.

```oa-check
name: Non-resident DOM minimum versus proved average
inputs:
  income: 40000
steps:
  minimum: round(min(income,29579)*0.144+max(0,income-29579)*0.20,2)
  proved_average_tax: income*0.10
  difference: minimum-proved_average_tax
expected:
  minimum: 6343.58
  proved_average_tax: 4000
  difference: 2343.58
```

**Brazil employment decision.** Assume an eligible Brazil treaty resident, 100 days of ordinary employment in Guyane in the fiscal year, EUR 20,000 remuneration and no overriding article. With a non-French employer and no French PE/fixed-base cost bearing, all art.15(2) conditions are assumed proved and the French taxable employment base is zero. If a Guyane PE instead bears the full remuneration, the exemption fails and the French-source employment base is EUR 20,000, before domestic computation/withholding rules.

```oa-check
name: Brazil treaty short-stay cost-bearing condition
inputs:
  remuneration: 20000
steps:
  exemption_proved_base: remuneration*0
  host_pe_bears_base: remuneration
expected:
  exemption_proved_base: 0
  host_pe_bears_base: 20000
```

## Ask the client first

- Home, family, work, economic interests, move date and treaty residence.
- All income sources/categories and actual location of duties/activity.
- Contracting employer, cost bearer, premises and contract authority.
- Actual convention and its definition of France, with applicable amendments.
- Gross foreign income, foreign assessments/tax paid, withholding and refunds.
- Shareholdings at departure, controlled-party payments and filing history.

## Sources

| Source and text actually read | URL | Read on |
|---|---|---|
| CGI art.4 B, complete February 2025 current text, including final treaty-residence sentence; “par application des conventions internationales relatives aux doubles impositions” | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051202565 | 2026-11-11 |
| DGFiP, non-resident tax computation, read for art.197 A minimum, average rate and special withholding | https://www.impots.gouv.fr/particulier/le-calcul-de-votre-impot | 2026-11-11 |
| DGFiP non-resident assessment explanation, read for departure split and 2025-income band | https://www.impots.gouv.fr/international-particulier/questions/comment-comprendre-mon-avis-dimposition | 2026-11-11 |
| France-Brazil treaty, arts.3-7 and 15-22, territorial scope, residence, employment and relief; “Guadeloupe, Guyane, Martinique et Réunion”; “183 jours au cours de l’année fiscale considérée” | https://www.impots.gouv.fr/sites/default/files/media/10_conventions/bresil/bresil_convention-avec-le-bresil_fd_1799.pdf | 2026-11-11 |
| BOFiP BOI-INT-CVB-BRA, read for corporate residence and actual-tax relief conditions | https://bofip.impots.gouv.fr/bofip/1736-PGP.html | 2026-11-11 |
| CGI art.197, current band limits and application to 2025 and following years | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006308332/ | 2026-11-11 |
| DGFiP 2026 brochure, read sections on non-residence, 2042-NR and 2047; not a 2027 filing calendar | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_integral/Brochure-IR-2026.pdf | 2026-11-11 |
| CGI arts.182 A/B/B bis, 187 and 197 B, read for complete ordinary base, rates, relief and exception paragraphs. Art.182 A “ramenés, respectivement, à 8 % et 14,4 %” | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373628, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179576/, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006303131 | 2026-11-11 |
| BOI-BAREME-000043, read for complete 2026 annual/quarter/month/week/day table and DOM footnote | https://bofip.impots.gouv.fr/bofip/13631-PGP.html | 2026-11-11 |
| BOI-IR-DOMIC-10-20-20-50, read for §§10-120 and 160-190, payer/beneficiary, 10% company-base allowance, gross-up, quarterly return and restitution | https://bofip.impots.gouv.fr/bofip/2280-PGP.html | 2026-11-11 |
| 2494-SD 2026, read for all four pages, fields, notes and payment instructions. “en un seul exemplaire”; “le 15 du mois suivant le trimestre civil” | https://www.impots.gouv.fr/sites/default/files/formulaires/2494-sd/2026/2494-sd_5450.pdf | 2026-11-11 |
| DGFiP non-resident withholding explanation, read for final/creditable portions and multiple payers; its numeric 2025 illustration not reused as 2026 bands | https://www.impots.gouv.fr/international-particulier/questions/je-suis-non-resident-je-veux-comprendre-la-retenue-la-source-qui | 2026-11-11 |
| BOI-RPPM-RCM-30-30-10-20, read for §§1-50, beneficial ownership, individual/company rates and ETNC safeguard | https://bofip.impots.gouv.fr/bofip/2674-PGP.html | 2026-11-11 |
| BOI-INT-DG-20-20-20-30, read for §§1-50, January 2026 treaty-zero withholding/refund change and documentary conditions | https://bofip.impots.gouv.fr/bofip/14878-PGP.html | 2026-11-11 |
| 2777-SD 01-2026, read for pp1-3, section 7 rate/base/codes and section 9 regularisation; “dans les quinze jours suivants l'expiration du mois” | https://www.impots.gouv.fr/sites/default/files/formulaires/2777-sd/2026/2777-sd_5335.pdf | 2026-11-11 |
| DGFiP Interest, read for general non-resident exemption and ETNC warning; BOI-INT-DG-20-50-30, read for II-A §§80-160 and 210 payment-location/safeguard/separate withholding conditions. “le paiement s’effectue hors de France dans un ETNC” | https://www.impots.gouv.fr/international-particulier/interest, https://bofip.impots.gouv.fr/bofip/12857-PGP.html | 2026-11-11 |

Not yet confirmed: complete treaty-by-treaty rates and territorial amendments outside the France-Brazil example, full specialist exit-tax/share-plan/artist/sport procedures, and the unissued 2027 calendar for 2026-income returns. No unsupported foreign-payment exemption, final 2027 annual threshold or universal treaty rate is supplied.
