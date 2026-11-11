---
name: gf-corporate-income-tax
description: "Apply French corporate income tax to ordinary companies and permanent establishments carrying on business in French Guiana in 2026. Covers entities subject to IS, French territorial profit, normal and small-company rates, expense adjustments, depreciation, provisions, finance-cost limits, loss carry-forward and carry-back, the conditional Guyane ZFANG profit allowance, electronic results returns, instalments, final payments and sanctions. Use for Guyane impôt sur les sociétés, SAS or SARL tax, déclaration 2065, 2571 and 2572, business tax losses and article 44 quaterdecies. Separates tax relief from the Guyane personal income-tax reduction and from octroi. Includes capital-payment eligibility and capped-relief examples. Special holding, consolidated-group, investment-incentive and large-group regimes require their own current-law workpapers."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gf-corporate-income-tax"
  jurisdiction: "GF"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# French Guiana corporate income tax 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

French Guiana (Guyane) is within the French corporate income-tax territory. Ordinary capital companies, including SA, SAS and SARL, are normally subject to **impôt sur les sociétés (IS)**; partnerships, individual-owned EURL and individual enterprises may instead be taxed to owners unless an applicable IS option/assimilation is valid. Confirm legal form, elections, activity, fiscal period and actual establishment before choosing the return. A foreign company can be taxable on a French operation; a French registered company is not automatically taxed on every foreign branch profit. [CGI art.206; DGFiP results guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats); [BOI-IS-CHAMP-60-10-10](https://bofip.impots.gouv.fr/bofip/4262-PGP.html).

Quick answer: reconcile accounting profit to taxable **French operation** profit, apply expense/finance restrictions and eligible losses, then any qualifying ZFANG reduction, then the appropriate IS rates and separate contributions. Credit lawful credits/advances only afterwards. The small-company rate and ZFANG have different eligibility tests. A Guyane address alone grants neither. [CGI art.219](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/); [ZFANG guidance](https://bofip.impots.gouv.fr/bofip/11833-PGP.html).

This Guide owns the pack's **ZFANG business-profit allowance**, including eligible IR businesses. The individual's separate Guyane progressive-tax reduction is in [gf-income-tax](gf-income-tax.md). Related-party pricing and disclosures are in [gf-transfer-pricing](gf-transfer-pricing.md); treaties and outbound withholding in [gf-cross-border-tax](gf-cross-border-tax.md); VAT non-application/import octroi in [gf-import-octroi-and-vat](gf-import-octroi-and-vat.md). These tax boundaries are different.

Ordinary standalone companies are computed here. Tax consolidation, mother/daughter participation exemptions, restructuring, tonnage/IP regimes, CFC/hybrid calculations, tax credits/investment incentives, Pillar Two and exceptional large-company contributions require separate specialist schedules; do not silently treat them as absent. The 2026 return itself has fields for exceptional large-company and shipping contributions. [2026 form 2065](https://www.impots.gouv.fr/sites/default/files/formulaires/2065-sd/2026/2065-sd_5381.pdf).

## Rates, bands and thresholds

EUR; an annual threshold must be adjusted as the cited rule requires for a short/long accounting period.

| Item and conditions | 2026 rule | Official source |
|---|---|---|
| Ordinary IS | 25% of taxable profit | [CGI art.219 I](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/) |
| Small-company profit slice | 15% on first 42,500 taxable profit per twelve months; remainder normal rate | [CGI art.219 I-b](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/) |
| Small-company eligibility | Turnover excluding tax no more than 10 million, annualised; capital fully paid and continuously held at least 75% by natural persons or the qualifying statutory intermediary; fiscal-group turnover aggregation | [CGI art.219 I-b](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/) |
| Corporate loss carry-forward | Unlimited time, but annual use limited to 1 million + 50% of taxable profit above 1 million; remaining valid losses carry forward | [CGI art.209 I; BOI-IS-DEF-10-30 §§1-20](https://bofip.impots.gouv.fr/bofip/2103-PGP.html) |
| Optional carry-back | Current-period loss only against eligible profit of the immediately preceding period; maximum 1 million and that eligible profit | [CGI art.220 quinquies; BOI-IS-DEF-20-10](https://bofip.impots.gouv.fr/bofip/5645-PGP.html) |
| Ordinary net-finance-cost ceiling, non-consolidated company | Higher of 3 million per twelve months or 30% of tax EBITDA; prior interest restrictions applied first | [CGI art.212 bis I-III](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637/) |
| Thin-capitalisation trigger | Average related-party debt above 1.5 times equity, with statutory exclusions/group-ratio escape; split ceiling then required | [CGI art.212 bis VII](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637/) |
| Unused ordinary finance capacity / disallowed ordinary interest | Capacity carried for five following periods; disallowed finance charges generally carried forward subject to the applicable category, not a current tax loss | [CGI art.212 bis VIII](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637/) |
| ZFANG size test, all required at period end | Fewer than 250 employees and annual turnover below 50 million, with prescribed workforce/period rules | [CGI art.44 quaterdecies I; BOFiP §§10-50](https://bofip.impots.gouv.fr/bofip/11833-PGP.html) |
| Guyane ZFANG qualifying operation | 80% allowance on eligible profit after carry-forward losses; allowance capped at 300,000 per twelve months; activity, return and EU-aid conditions apply | [CGI art.44 quaterdecies III; BOFiP §§140-150, 260-300](https://bofip.impots.gouv.fr/bofip/11833-PGP.html) |
| ZFANG aggregate regional operating-aid test | Annual tax saving plus relevant other regional operating aid must fit at least one of: 35% local gross value added, 40% local annual labour cost, or 30% local annual turnover | [BOFiP §300; Regulation651/2014 art.15](https://bofip.impots.gouv.fr/bofip/11833-PGP.html) |
| 2026 simplified business-profit regime ceiling | 945,000 sales / 286,000 services, with activity and prior-year/double-exceedance rules; this is not a VAT registration threshold | [BOI-BAREME-000044 I](https://bofip.impots.gouv.fr/bofip/14069-PGP.html); [DGFiP current regime guidance](https://www.impots.gouv.fr/professionnel/questions/si-mon-chiffre-daffaires-augmente-est-ce-que-je-change-de-regime-juridique) |
| Advance exemption | Prior reference IS no more than 3,000: no 2571 advance/payment; a newly subject company has the statutory first-period exemption | [CGI annex III art.359(3)](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006299811/); [CGI art.1668 / BOI-IS-DECLA-20-10 §360](https://bofip.impots.gouv.fr/bofip/3558-PGP.html) |
| Ordinary advance dates | 15 March, 15 June, 15 September, 15 December; accounting close determines sequence | [CGI art.1668; DGFiP results guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats) |
| Final balance | 15th of fourth month after close; December 31 close or no close in year: May 15 following year; payment date differs from results-return deadline | [DGFiP results guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats) |
| Separate corporate social contribution | 3.3% of relevant IS before credits, less allowance of 763,000 per twelve months; statutory qualifying small-company exemption uses turnover below 7,630,000 and paid-up/75% ownership conditions | [CGI art.235 ter ZC](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715/) |

The small-company rate uses **no more than** EUR 10 million in article 219, despite looser wording on an older DGFiP results page. The separate contribution statute says **below** EUR 7.63 million, rather than extending its exemption to equality on the strength of an authority summary. Use each statute's boundary. [CGI art.219](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/); [CGI art.235 ter ZC](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715/).

## The base

### Ordinary accounting-to-tax reconciliation

Start with annual accounting profit/loss for the taxable French activity, including ordinary trading income, stock movements, accrued receivables and taxable asset gains. Reconcile tax exclusions and timing differences through the tax schedule. Foreign establishments and treaty allocations are addressed below. Guyane does not have a general tax holiday. [CGI arts.38, 39 and 209; DGFiP results guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats); [territorial guidance](https://bofip.impots.gouv.fr/bofip/4262-PGP.html).

Deduct actual, documented expenditure incurred in the business interest and attributable to the correct period, unless specifically prohibited. Salary must correspond to genuine work and not be excessive. Business rent, wages/social charges, purchases, insurance, qualifying repairs and professional fees can qualify; a shareholder distribution or private expense is not deductible remuneration merely because booked as a cost. Add back legal fines/penalties, corporate income tax, non-business and excessive costs, disallowed depreciation/interest, and prohibited luxury expenditure. Donations eligible for a tax reduction are not simply both a profit deduction and a tax credit. [CGI art.39, especially1-1°,2,3,4,5](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542680/); [2026 2033 instructions](https://www.impots.gouv.fr/sites/default/files/formulaires/2033-sd/2026/2033-sd_5395.pdf).

**Assets and depreciation:** capital expenditure is capitalised; do not deduct the full asset cost as routine repairs. Depreciation must be actually booked, follow the permitted useful-life/use rules and begin from the applicable in-service date; separate components where required. Land is not depreciated. Do not assign one universal rate to all equipment or buildings. Provisions need specifically identified probable loss/charge based on events at close and actual accounting recognition; a general future-risk reserve is not enough. Specific impairment, debtor evidence and the later reversal must be reconciled. Retirement departure provisions have a statutory non-deduction rule. [CGI art.39,1-2° and 5°](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542680/); [BOI-BIC-AMT-10-20](https://bofip.impots.gouv.fr/bofip/4590-PGP.html); [2033 instructions, fixed assets/amortisation/provisions](https://www.impots.gouv.fr/sites/default/files/formulaires/2033-sd/2026/2033-sd_5395.pdf).

For an ordinary passenger car acquired from 2021 using **WLTP**, article 39-4 limits depreciable cost to EUR 30,000 below 20gCO2/km; EUR 20,300 from 20 to below 50; EUR 9,900 above 160; otherwise EUR 18,300. Other registration methods/acquisition dates use their own bands. Lease rents can include a corresponding non-deductible depreciation fraction, subject to the short-term exception. Check vehicle classification, emissions method/date, use and any statutory “sauf justifications” exception before using a cap. These are cost caps, not depreciation rates. [CGI art.39-4](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542680/).

### Financing restrictions

### Shareholder and related-enterprise borrowing

**Capital and rate test first.** Ordinary shareholder current-account interest requires fully paid share capital, even where the agreed interest rate is low. Article212IV has a specific cooperative exception; do not generalise it. Use the gross contractual interest and gross reference rate, examine each account separately and add back excess interest without offsetting another shareholder's under-limit rate. Apply the actual advance balances and time outstanding, rather than multiplying the closing balance by a full-year rate. These restrictions apply before article212bis. [CGI art.39(1)(3°)](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542680/); [BOI-IS-BASE-35-20 §§20-30](https://bofip.impots.gouv.fr/bofip/4399-PGP.html/identifiant=BOI-IS-BASE-35-20-20260715); [BOI-BIC-CHG-50-50-30 §130](https://bofip.impots.gouv.fr/bofip/5505-PGP.html).

The ordinary reference is the annual average of the official effective average rates for variable-rate business loans initially longer than two years. It depends on the accounting period, not the payment date alone. The following **twelve-month period** closing-date rates were published/read by 11November2026; they are not interchangeable annual2026 rates.

| Twelve-month period closing date | Ordinary maximum annual interest rate | Official source |
|---|---|---|
| 31December2025 to30January2026 | 4.55% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 31January to27February2026 | 4.49% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 28February to30March2026 | 4.44% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 31March to29April2026 | 4.39% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 30April to30May2026 | 4.37% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 31May to29June2026 | 4.34% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 30June to30July2026 | 4.33% | [BOI-BIC-CHG-50-50-30 §40](https://bofip.impots.gouv.fr/bofip/5505-PGP.html) |
| 31July to30August2026 | 4.33% | [BOI-BIC-CHG-50-50-30 §40](https://bofip.impots.gouv.fr/bofip/5505-PGP.html) |
| 31August to29September2026 | 4.33% | [BOI-BIC-CHG-50-50-30 §40](https://bofip.impots.gouv.fr/bofip/5505-PGP.html) |
| 30September to30October2026 | 4.40% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 31October to29November2026 | 4.43% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |
| 30November to30December2026 | 4.45% | [Service Public official table, checked16October2026](https://entreprendre.service-public.gouv.fr/vosdroits/F32966) |

For a calendar-year close at **31December2026**, the final required quarterly data/reference rate was not yet published in the sources read; do not use4.45% merely because it is the last published row. Open the current [BOI table and method §§20-120](https://bofip.impots.gouv.fr/bofip/5505-PGP.html) at computation time. For a calendar-year period, average its four published quarterly rates; for off-calendar, short or long periods use the BOI weighted-month method and its opening/closing partial-month conventions. If the relevant quarter's rate is available in time, the BOI permits the corresponding quarterly rate for a fraction of that quarter. Retain the dated rate publication and computation, then reconcile gross interest booked to the deductible amount. A short or long period does not qualify for direct use of the twelve-month table.

**Market-rate alternative:** current article212I(a), applicable to periods closed from31December2025, permits the independently supportable higher borrowing rate for funding by an enterprise shareholder, including a minority enterprise shareholder that is not related, or a related enterprise under article39(12). An ordinary private individual simply investing personal capital cannot use that exception. An individual qualifying as an enterprise must meet both professional-holding and professional-funding conditions in BOI§55. A related non-shareholder lender does not itself trigger the paid-capital condition, which remains a shareholder-interest condition. [CGI art.212I/IV](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542930/2026-02-21); [BOI-IS-BASE-35-20 §§30-60](https://bofip.impots.gouv.fr/bofip/4399-PGP.html/identifiant=BOI-IS-BASE-35-20-20260715).

The borrower must demonstrate the rate it could independently obtain in comparable conditions: amount, duration, currency, security and its own credit risk. Keep contemporaneous independent lender offers/comparable financing and the analysis; for a loan the relevant evidence is at grant, for a credit line it can be the relevant period. A shareholder's agreed rate or the group's borrowing rate alone does not establish the borrower's independent rate. Deduct at most the established market rate, with any excess permanently disallowed under this rate test, rather than carried as article212bis-limited interest. These domestic deductions remain owned by this Guide; international pricing and treaty consequences also use [gf-transfer-pricing](gf-transfer-pricing.md). [BOI-IS-BASE-35-20 §§70-90](https://bofip.impots.gouv.fr/bofip/4399-PGP.html/identifiant=BOI-IS-BASE-35-20-20260715).

Apply article 39/212 shareholder and related-enterprise interest/rate conditions before the article 212bis net-finance ceiling; do not treat the general cap as permission to deduct non-arm's-length interest. For a normal non-consolidated company calculate tax EBITDA from tax result before losses and this limitation, using article 212bisII's adjustments. The ordinary higher-of ceiling is in the rates table. A qualifying equity/group-ratio escape can add 75% of current disallowed charges where the company equity/assets ratio is at least the consolidated group ratio, allowing the statutory two-percentage-point tolerance. A strictly standalone company with no consolidated group, foreign establishment or associated enterprise can deduct 75% of current excess under VI bis; for that year IV/VIII carry-forward machinery does not apply. Do not call every non-tax-consolidated company standalone. Under thin capitalisation allocate net charges between the ordinary-debt fraction and the excess related-debt fraction; the latter uses a proportionate higher-of **EUR 1 million or 10%** tax EBITDA ceiling. Only one-third of certain thin-cap excess is carried forward. Track carry-forward interest separately from unused five-year capacity; capacity cannot be used for previously carried interest. [CGI art.212 bis II,VI,VI bis,VII,VIII](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637/); [transfer-pricing Guide](gf-transfer-pricing.md).

### Losses, then ZFANG

Carry-forward losses are not reduced merely because time passes, but must be supported by prior returns and survive the business-change/cessation/transfer rules. Apply the annual cap to profit before using them; record used and remaining amounts. Do not offset a foreign branch loss excluded from the French base. [CGI art.209; BOI-IS-DEF-10-30](https://bofip.impots.gouv.fr/bofip/2103-PGP.html).

Carry-back is an **election by the loss-period results-return deadline**, not an automatic refund of every earlier tax payment. It uses the current loss and previous-period profit actually subject to eligible IS, excluding distributed, exempt and credit-paid portions as prescribed. Where prior profit was taxed at both rates, use normal-rate profit first. It creates an IS receivable rather than reducing the negative loss-period tax below zero; normally use it against IS for the five years following the loss-period closing year; the unused balance is then repayable by the administration, with a claim if it fails to repay. File 2039-SD with the balance statement and identify the election in the results schedule. No double carry-forward of the same loss. Cessation/restructuring/insolvency cases have restrictions. [CGI art.220 quinquies; BOI-IS-DEF-20-10 §§10-30,90-140,250 onwards](https://bofip.impots.gouv.fr/bofip/5645-PGP.html); [BOI-IS-DEF-20-20 §§30-50](https://bofip.impots.gouv.fr/bofip/5647-PGP.html); [2033 instructions line 356](https://www.impots.gouv.fr/sites/default/files/formulaires/2033-sd/2026/2033-sd_5395.pdf).

**ZFANG is conditional, optional and calculated on profit, not on tax.** For a Guyane operation confirm every size, activity, tax-regime and EU-aid condition. The activity must principally be in a sector eligible under article 199undeciesB, with statutory exclusions. Do not give the allowance to an ordinary retailer or liberal/BNC profession: the current guidance expressly excludes buying goods for resale without transformation and BNC for Guyane. The principal activity is tested at the operation, by its largest turnover/receipts category, not necessarily a majority of the whole company's activity. An ancillary excluded activity can coexist under the operation's main-activity rule. [BOFiP §§60-100](https://bofip.impots.gouv.fr/bofip/11833-PGP.html).

IS or IR BIC/BA operations can be eligible. **Actual normal/simplified regimes and micro-BIC/micro-BA are permitted.** Mayotte's temporary enlarged BNC coverage and full allowance are not Guyane rules. Guyane's ordinary enhanced allowance is the rate/cap in the table. Compute it after previous carry-forward losses, prorate the cap for a non-annual period, and allocate profits among operations reasonably where only some qualify. It covers eligible declared profit and relevant ordinary gains, but excludes revaluation gains from the base. Only profit **declared within the legal deadline** qualifies. Optional use is global over the taxpayer's eligible operations, not selective exemption of whichever source produces the best answer. [BOFiP §§100-150,260-290](https://bofip.impots.gouv.fr/bofip/11833-PGP.html).

Check the EU aggregate regional operating-aid ceiling using the **tax saving** rather than the amount of exempt profit, and all relevant aid. At least one alternative ceiling must be respected; do not add the three ceilings together. Where another business exemption can apply, a time-limited irrevocable regime choice may be necessary. Carry-back cannot use earlier profit exempted by ZFANG. The overseas investment incentives have separate cumulation/order rules and are outside this computation. [BOFiP §§300-350](https://bofip.impots.gouv.fr/bofip/11833-PGP.html).

| Boundary or exception | Action |
|---|---|
| Turnover satisfies small-company test but share capital not fully paid | Normal rate applies; do not use the reduced slice |
| Guyane business mainly ordinary resale or BNC profession | ZFANG sector condition fails unless a separately established statutory case applies |
| Eligible micro-BIC/BA | Compute the prescribed taxable business profit first; micro status alone does not disqualify ZFANG |
| ZFANG operation with prior carried loss | Apply eligible loss first, then allowance; do not preserve a loss by exempting gross profit first |
| Loss period | No positive profit allowance is manufactured; examine ordinary loss election instead |
| More than one operation / mainland activities | Allocate profits and aid; Guyane residence does not exempt all French profits |

## Deadlines and filing

Register the business through the INPI guichet unique, confirm its SIREN/SIRET, tax office, IS status and fiscal dates, and activate the professional tax space/payment mandate or EDI access. An IR-to-IS election, business acquisition or non-annual first period needs its own effective-date evidence. [DGFiP current regime guidance](https://www.impots.gouv.fr/professionnel/questions/si-mon-chiffre-daffaires-augmente-est-ce-que-je-change-de-regime-juridique); [results guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats).

**Prepare and file:** reconcile trial balance to accounts and tax adjustments; use 2033-A toG for simplified results or 2050 to2059-G for normal results, plus2065-SD and 2065bis. All IS results returns are electronic; simplified taxpayers can use espace professionnel, while EDI-TDFC handles both regimes. In 2065 confirm A identification, B activities, and C “Récapitulation des éléments d'imposition”: taxable normal-rate and reduced-rate profit, deficit and special-rate gains are distinct. C-3 identifies the ZFANG exemption and exempt result; D identifies applicable credit imputations. Complete distributions on 2065bis as applicable. Save the validated transmission/EDI acceptance, not merely a prepared PDF. [2026 form 2065 and notes](https://www.impots.gouv.fr/sites/default/files/formulaires/2065-sd/2026/2065-sd_5381.pdf); [filing guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats).

On the simplified tax reconciliation,2033-B distinguishes accounting profit312/loss314, add-backs and deductions, carry-back356 and previous loss offset360; final taxable profit370 or deficit372 must reconcile to2065.2033-D tracks loss movements. In the normal package use the corresponding2058-A/B tax and loss schedules rather than copying simplified box numbers. Claim a carry-back receivable on 2039 and attach to2572 under its instructions. [2026 2033 instructions](https://www.impots.gouv.fr/sites/default/files/formulaires/2033-sd/2026/2033-sd_5395.pdf).

**Results deadline:** within three months after a non-December 31 close; for a December 31 close, second working day afterMay1 of the following year. Electronic results filings receive the published fifteen-day extension. Do not use the later results deadline as a payment extension. For a 2026 calendar close the return is in 2027; check that campaign's issued electronic calendar/forms rather than presenting a 2026-millèsime form as the future mandatory edition. [DGFiP results guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats).

**Pay separately:** submit2571-SD and electronic payment on the quarterly dates in the rates table. The ordinary advance uses one-quarter of reference-period tax at the applicable advance rates; annualise the reference result when required and regularise the first advance after the latest result becomes known. A newly subject company's first-period exemption and a prior tax below the threshold are separate exemptions. Lower forecast tax can justify reducing remaining advances under the statutory responsibility/penalty rules; document the forecast. Large companies have forecast-based last-instalment rules, not the simple prior-year quarter. [CGI art.1668; BOI-IS-DECLA-20-10](https://bofip.impots.gouv.fr/bofip/3558-PGP.html).

Compute2572-SD final IS/contributions, subtract creditable credits and advances and pay by the balance deadline. December 31,2026 closing therefore has a statutory **May 15,2027** balance date, subject to the applicable non-working-day/calendar rule. A receivable/refund claim follows the relevant form/process; source deductions or an unrequested carry-back do not automatically equal cash refunded. Separate corporate social-contribution advances use2571 and the final balance2572. [DGFiP results guidance](https://www.impots.gouv.fr/professionnel/imposition-des-resultats); [CGI art.235 ter ZC](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715/).

## Penalties and interest

Late or missing results returns generally trigger **10%** without an unremedied formal notice, **40%** if still not filed within thirty days after notice, or **80%** for hidden activity under CGI 1728; IR's combined twenty-percent rule must not be imported into an IS return. Deliberate understatement is generally **40%**, fraudulent manoeuvres **80%**, with separate abuse and procedural conditions under CGI 1729. The correct statutory ground and base matter; do not accumulate incompatible majorations for the same rights. [CGI arts.1728,1729](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784/).

Late tax generally carries **0.20% monthly interest** and the professional-payment **5% surcharge**, subject to article 1731's late-return-with-full-payment exception, administrative audit/corrective-return exceptions and statutory reduction rules. Unlike the interest base, filing sanctions are not erased merely by advances already paid. Failure to use mandatory electronic filing can trigger the separate article 1738 **0.2%** sanction, minimum EUR 60; where no tax is due, the general fine is EUR15 per document with simultaneous-document total minimum EUR 60 and maximum EUR150, subject to the statutory exceptions. It is not the same as monthly interest. [CGI arts.1727,1731; BOI-CF-INF-10-30 III §§140-195](https://bofip.impots.gouv.fr/bofip/2428-PGP.html); [CGI article 1738](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037312444/); [2026 form 2065 warning](https://www.impots.gouv.fr/sites/default/files/formulaires/2065-sd/2026/2065-sd_5381.pdf). ZFANG's timely declaration condition can additionally remove the allowance even where a late-return sanction is small. [BOFiP §280](https://bofip.impots.gouv.fr/bofip/11833-PGP.html).

## Cross-border points

The French territorial corporate system taxes profits of businesses operated in France and income allocated to France by treaties, with specific statutory extensions. Guyane is expressly part of France for this purpose. A foreign subsidiary is not automatically consolidated into its shareholder's French tax base; a French company normally excludes genuinely foreign branch profits and related losses, subject to treaty/anti-avoidance exceptions. Establish where the activity, branch and dependent agents actually operate. [CGI art.209 I; BOI-IS-CHAMP-60-10-10](https://bofip.impots.gouv.fr/bofip/4262-PGP.html).

Mainland-to-Guyane operations are within France for IS even though VAT/customs rules can treat goods differently. French-source receipts of a non-resident may face withholding distinct from PE profit tax. Check the relevant treaty's territorial definition, residence, PE and article-specific credit or exemption; do not assume a foreign tax is deductible and creditable twice. Mother/daughter dividends, foreign branches, CFC, hybrids and exit/restructuring rules need separate schedules where triggered. [gf-cross-border-tax](gf-cross-border-tax.md); [gf-transfer-pricing](gf-transfer-pricing.md).

## Two worked examples that recompute

### Example 1: paid-up capital changes the rate decision

A standalone Guyane service company has a twelve-month 2026 period, turnover EUR 600,000 and continuous100% natural-person ownership. Accounting profit EUR 100,000 includes a EUR 1,000 legal fine. Valid carried loss is EUR 10,000; its ordinary consulting activity does not qualify for ZFANG. Taxable profit is 100,000+1,000−10,000=EUR 91,000. If capital is fully paid, IS is 42,500×15%+48,500×25%=EUR 18,500. With capital unpaid and no applicable exception, all91,000 is taxed at 25%=EUR 22,750. Establish the capital condition before choosing the reduced rate: the difference isEUR 4,250. AssumeEUR16,000 advances; eligible-company balance isEUR2,500. Separate contribution is nil because the qualifying SME is exempt and, in any event here, IS is below its allowance. [CGI art.219 I-b](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/); [fine](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542680/); [loss](https://bofip.impots.gouv.fr/bofip/2103-PGP.html).

```oa-check
name: Guyane small-company paid-capital decision, 2026
inputs:
  accounting_profit: 100000
  legal_fine: 1000
  loss_brought_forward: 10000
  advances: 16000
steps:
  - profit_before_loss: accounting_profit + legal_fine
  - allowed_loss: min(loss_brought_forward, min(profit_before_loss, 1000000 + max(0, profit_before_loss - 1000000) * 0.50))
  - taxable_profit: profit_before_loss - allowed_loss
  - eligible_tax: min(taxable_profit, 42500) * 0.15 + max(0, taxable_profit - 42500) * 0.25
  - unpaid_capital_tax: taxable_profit * 0.25
  - difference: unpaid_capital_tax - eligible_tax
  - balance: eligible_tax - advances
expected:
  taxable_profit: 91000
  eligible_tax: 18500
  unpaid_capital_tax: 22750
  difference: 4250
  balance: 2500
```

### Example 2: ZFANG cap after losses, then the small-company rate

A qualifying manufacturing operation in Guyane has 2026 profit EUR 500,000 before valid previous losses of EUR100,000. Its size, activity, tax-regime and timely-filing tests are met; paid capital/natural ownership and turnover also satisfy the small-company test. Prior loss first reduces profit toEUR 400,000.80% would beEUR320,000, so the annual allowance is capped at EUR300,000. Remaining taxable profitEUR100,000 gives IS EUR 20,750. Without electing/qualifying for ZFANG, IS onEUR 400,000 would beEUR95,750; tax savingEUR75,000. Assume no other relevant regional operating aid and local labour costsEUR250,000: its40% EU aid ceiling isEUR100,000, so this alternative ceiling supports theEUR75,000 saving. If other aid increases aggregate aid above the applicable limit, or sector/timely-filing evidence fails, do not claim this result unchanged. [BOFiP §§140-150,280,300](https://bofip.impots.gouv.fr/bofip/11833-PGP.html); [CGI art.219](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/).

```oa-check
name: Guyane ZFANG capped allowance and aggregate aid, 2026
inputs:
  profit: 500000
  carried_loss: 100000
  local_labour_cost: 250000
  other_regional_operating_aid: 0
steps:
  - after_loss: profit - carried_loss
  - allowance: min(after_loss * 0.80, 300000)
  - taxable_profit: after_loss - allowance
  - tax: min(taxable_profit, 42500) * 0.15 + max(0, taxable_profit - 42500) * 0.25
  - tax_without_allowance: min(after_loss, 42500) * 0.15 + max(0, after_loss - 42500) * 0.25
  - tax_saving: tax_without_allowance - tax
  - total_aid: tax_saving + other_regional_operating_aid
  - labour_aid_ceiling: local_labour_cost * 0.40
  - headroom: labour_aid_ceiling - total_aid
expected:
  after_loss: 400000
  allowance: 300000
  taxable_profit: 100000
  tax: 20750
  tax_without_allowance: 95750
  tax_saving: 75000
  labour_aid_ceiling: 100000
  headroom: 25000
```

## Ask the client first

- What legal form, IS election/option, fiscal period, French/foreign establishments and activity changes apply?
- What are turnover, group membership, capital-payment dates and the complete continuous ownership chain?
- Which accounts, expense/depreciation/provision schedules, related-party financing and prior losses support the tax reconciliation?
- For ZFANG, what operation, principal activity, employee count, turnover, timely filing and EU aggregate aid evidence exist?
- What prior-period profit distributions, tax credits and tax payments constrain a carry-back election or available credit?
- What advances, withholding, returns, notices and EDI acknowledgements have already been paid/filed/received?

## Sources

| Source and actual reading scope | URL | Read on |
|---|---|---|
| CGI article 219, read for I normal rate, I-b small-company conditions and annualisation | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542939/ | 2026-11-11 |
| CGI article 39, read for ordinary expenditure, remuneration, depreciation/provisions, fines and passenger-car caps | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542680/ | 2026-11-11 |
| CGI article 212bis, read for parts I-III, VI-VIII ceilings, standalone/group adjustments, thin capitalisation and carry-forwards | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637/ | 2026-11-11 |
| CGI article 44quaterdecies, read for I size/regime, III Guyane allowance, VII option and IX EU conditions | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053543403/2026-02-21 | 2026-11-11 |
| BOI-IS-CHAMP-60-10-10, read for French territorial operation and Guyane definition | https://bofip.impots.gouv.fr/bofip/4262-PGP.html | 2026-11-11 |
| BOI-IS-DEF-10-30, read for parts I-III ordinary loss carry-forward and annual use cap | https://bofip.impots.gouv.fr/bofip/2103-PGP.html | 2026-11-11 |
| BOI-IS-DEF-20-10, read for parts I and III current loss, eligible prior profit, exclusions, election and forms | https://bofip.impots.gouv.fr/bofip/5645-PGP.html | 2026-11-11 |
| BOI-BIC-CHAMP-80-10-85 current 8July 2026, read for §§10-150 and 260-350 Guyane eligibility, base, cap, aid and interaction; Mayotte changes not transplanted | https://bofip.impots.gouv.fr/bofip/11833-PGP.html | 2026-11-11 |
| BOI-BAREME-000044 current 19August 2026, read for part I 2026 business-profit regime thresholds | https://bofip.impots.gouv.fr/bofip/14069-PGP.html | 2026-11-11 |
| DGFiP current regime guidance, read for 2026 thresholds and registration/filing choices | https://www.impots.gouv.fr/professionnel/questions/si-mon-chiffre-daffaires-augmente-est-ce-que-je-change-de-regime-juridique | 2026-11-11 |
| DGFiP results guidance, read for forms, electronic procedures, return dates, quarterly payments and balance; its expressly 2023-25 regime thresholds superseded here | https://www.impots.gouv.fr/professionnel/imposition-des-resultats | 2026-11-11 |
| 2026 form 2065-SD/2065bis and notice, read for identification, result/relief/credit fields and electronic requirement | https://www.impots.gouv.fr/sites/default/files/formulaires/2065-sd/2026/2065-sd_5381.pdf | 2026-11-11 |
| 2026 2033 instructions, read for tax reconciliation, assets, depreciation, provision and loss fields, especially356/360/370/372 | https://www.impots.gouv.fr/sites/default/files/formulaires/2033-sd/2026/2033-sd_5395.pdf | 2026-11-11 |
| BOI-IS-DECLA-20-10, read for parts I-II instalment scope, reference tax and first-year exemption | https://bofip.impots.gouv.fr/bofip/3558-PGP.html | 2026-11-11 |
| CGI article 235terZC, read for contribution rate, base allowance and strict small-company exemption boundary | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715/ | 2026-11-11 |
| BOI-BIC-AMT-10-20, read for assets capable of depreciation, land and intangible distinctions | https://bofip.impots.gouv.fr/bofip/4590-PGP.html | 2026-11-11 |
| CGI articles 1728 and 1729, read for late return and deliberate/fraud penalties | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784/ and https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904/ | 2026-11-11 |
| BOI-CF-INF-10-30, read for part III professional-payment surcharge, monthly interest illustration and exceptions | https://bofip.impots.gouv.fr/bofip/2428-PGP.html | 2026-11-11 |

| BOI-IS-DEF-20-20, read for §§30-50 receivable use and ordinary five-year refund obligation | https://bofip.impots.gouv.fr/bofip/5647-PGP.html | 2026-11-11 |
| CGI article1738, read for part1 electronic default percentage and tax/nil-tax minimum/maximum | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037312444/ | 2026-11-11 |

| CGI article212 current21February2026, read for I(a), IV and extension to enterprise shareholders for periods closed from31December2025 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542930/2026-02-21 | 2026-11-11 |
| BOI-BIC-CHG-50-50-30 current5August2026, read §§1-140 for reference-rate tables, period-specific methods and gross separate-account test; Service Public F32966 table read through30December2026 closes | https://bofip.impots.gouv.fr/bofip/5505-PGP.html; https://entreprendre.service-public.gouv.fr/vosdroits/F32966 | 2026-11-11 |
| BOI-IS-BASE-35-20 current15July2026, read §§1-90 for enterprise-shareholder extension, paid-capital requirement, private-individual boundary and market evidence | https://bofip.impots.gouv.fr/bofip/4399-PGP.html/identifiant=BOI-IS-BASE-35-20-20260715 | 2026-11-11 |
| CGI annex III article359(3), read for exact no-more-than3000 reference-tax advance exemption | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006299811/ | 2026-11-11 |

Not yet confirmed: the final ordinary shareholder-interest reference rate for a31December2026 close; the future 2027 administrative return calendar/form edition for a 2026 calendar close; specialist consolidation, holding exemptions, restructuring, investment credits, Pillar Two and exceptional large-company computations are outside this ordinary-company Guide.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gf-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gf-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
