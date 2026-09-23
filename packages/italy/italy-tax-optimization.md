---
name: italy-tax-optimization
description: Use this skill whenever asked about reducing tax in Italy, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals in Italy. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "risparmiare sulle tasse", "ottimizzazione fiscale", "pagare meno tasse", "detrazioni", "deduzioni". ALWAYS read this skill before advising on any Italian tax optimization strategy.
version: 1.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tax planning for the self-employed in Italy

Lawful tax planning for a self-employed person in Italy: forfettario or ordinario, sole trader (ditta individuale) or S.r.l., pensions, family business, losses, timing, and where planning becomes abuse of law. Figures are for tax year 2026, the calendar year. The old TUIR (D.P.R. 917/1986) applies for 2026 income; the new TUIR (D.Lgs. 117/2026) applies only from 1° gennaio 2027 (art. 377); statutes were read on Normattiva as in force on 30 June 2026. The IRAP rate is from the tax year 2025 instructions. No saving amounts are given. Detail sits in the sibling Guides named below.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Key legislation | TUIR art. 5, 8, 10, 11, 16-ter, 54 to 54-octies, 84, 102, 164; L. 190/2014 art. 1 co. 54-89 (forfettario); D.Lgs. 252/2005 (pension funds); L. 212/2000 art. 10-bis (abuse of law) |
| Attitude to planning | Choosing between regimes and lawful options is free (art. 10-bis(4)); abuse is disregarded (Section 10) |
| Currency | EUR |
| Tax year | Calendar year |
| Return | Modello Redditi PF online by 31 October of the following year (D.P.R. 322/1998 art. 2). Not the 730 for VAT-number income. See `it-income-tax` |

### IRPEF Rates 2026 (Legge di Bilancio 2026)

- Top of the first bracket: EUR 28,000; top of the second bracket: EUR 50,000 ([TUIR art. 11](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig=)): "a) fino a 28.000 euro, 23 per cento"; "fino a 50.000 euro".

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef |
| First bracket | 23% | "sull’intero importo" |
| Second bracket, from 2026 income | 33% | "dal 35 al 33 per cento" |
| Old second-bracket rate, 2024 and 2025 only | 35% | "Dall’anno 2024" |
| Above the second bracket | 43% | "sul reddito eccedente i 50.000 euro" |

- Regional and municipal surcharges come on top (not on forfettario income): `it-income-tax`.

### Detrazioni Limits (Art. 16-ter TUIR, from 2025)

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207 |
| Reddito complessivo above which the cap applies | EUR 75,000 | "reddito complessivo superiore a 75.000 euro" |
| Income at which the base amount drops | EUR 100,000 | "non superiore a 100.000 euro" |
| Base amount, up to that level | EUR 14,000 | "a) 14.000 euro" |
| Base amount, above it | EUR 8,000 | "b) 8.000 euro" |

- Reddito complessivo above which a further cut applies (art. 16-ter(5-bis)): EUR 200,000; cut to the detrazioni for certain oneri: EUR 440 ([L. 199/2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199)): "reddito complessivo superiore a 200.000 euro"; "pari a 440 euro".
- Above the first limit, oneri giving a detrazione count only up to the base amount times a family coefficient that rises with the number of children; some items are outside the cap (art. 16-ter(4) and (5)).

### Regime Forfettario vs Regime Ordinario

The first decision. The entry conditions decide whether the forfettario is open; a taxpayer who qualifies may still choose the ordinario.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |
| Entry: PREVIOUS-year revenue or fees, annualised, all ATECO codes together, not above | EUR 85,000 | "ragguagliati ad anno, non superiori a 85.000 euro" |
| Exit in the SAME year once revenue or fees go over | EUR 100,000 | "dallo stesso anno" |
| Entry: previous-year gross staff and collaborator costs not above | EUR 20,000 | "20.000 euro lordi" |
| Exclusion: previous-year employment income above (standing rule) | EUR 30,000 | "superiore a 30.000 euro" |
| The same limit for 2025 and 2026 only | EUR 35,000 | "elevato a 35.000 euro" |
| Substitute tax, replacing IRPEF and both surcharges | 15% | "un’unica imposta" |
| Start-up rate, first five years, if conditions are met | 5% | "per i primi cinque anni di attività" |

- Coefficient, professional/scientific/technical/health/education/financial services: 78%; other activities incl. IT services: 67% (L. 145/2018 allegato 2, [Agenzia table](https://www.agenziaentrate.gov.it/portale/documents/20143/241208/allegato+4.pdf/d69be7fc-b18a-3c73-bd2e-b0f3c1970218)).

- **Forfettario mechanics.** Taxable income is revenue or fees times the coefficient, less compulsory contributions (any excess comes off total income); real costs are ignored. No IVA charged or recovered (`italy-vat-return`); no withholding on fees.

- **Two limits.** Over the entry limit, the regime ends the FOLLOWING year; over the higher one, in the SAME year, with IVA due from the crossing sale.
- **Temporary employment limit.** Written "for the years 2025 and 2026"; the standing limit returns for 2027 unless extended. Does not bite if that job ended last year with no pension or other job income that year.
- **Other exclusions** (same page): non-residents, except EU/EEA residents earning most income in Italy; mainly selling buildings, building land or new vehicles; a stake in a partnership, professional association or impresa familiare, or control of a linked S.r.l.; working mainly for an employer of the current year or of the two previous years, or for someone linked to that employer (not after compulsory practice); using special VAT schemes or other flat-rate income schemes.
- **Start-up rate**: no such activity in the previous three years, and not a mere continuation of previous work (compulsory practice excepted); and if a business is taken over from someone else, its previous-year revenue must be within the entry limit.
- **How to compare.** The forfettario wins when real costs are below what the coefficient assumes. Compare both on the client's own figures (method below).

### SRL (Società a Responsabilità Limitata) vs Ditta Individuale

| What | Value | Note (source) |
| --- | --- | --- |
| IRES, corporate income tax | 24% | "con l'aliquota del 24 per cento" ([art. 77](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig=)) |
| IRAP standard rate, before regional changes | 3.9% | "l’aliquota del 3,9 per cento" ([IRAP istr.](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414)) |
| Withholding/substitute tax on capital income of TUIR art. 44, incl. profits paid out | 26% | "sono stabilite nella misura del 26 per cento" ([D.L. 66/2014](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2014-04-24;66~art3!vig=2026-06-30)) |
| Final withholding on profits paid by an S.r.l. to a resident individual, qualified or non-qualified holding, not held in a business | 26% | "partecipazioni qualificate e non qualificate" ([D.P.R. 600/1973](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art27!vig=2026-06-30)) |

| Factor | Ditta Individuale | SRL |
| --- | --- | --- |
| Income tax | IRPEF or the forfettario | IRES on the company's profit |
| IRAP | Not due by individuals since 2022 (`it-irap`) | Due; regions vary the rate |
| Extraction | Profit is the owner's | Profits paid out are taxed again |
| Forfettario | Open if conditions are met | Control of an S.r.l. with a linked activity excludes the member's forfettario |
| Set-up | Registration | Notarial deed, capital "non inferiore a diecimila euro" ([Civil Code art. 2463](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2463!vig=)); a reduced capital "pari almeno a un euro" is allowed, paid in full in cash; annual accounts (`italy-formation`) |

- IRES and IRAP have different bases and are never combined into one figure. INPS for S.r.l. members was not read: refer.

### Impresa Familiare (Family Business)

- Largest share of the owner's declared income attributed to family members: 49% ([TUIR art. 5](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art5!vig=2026-06-30)): "limitatamente al 49 per cento".
- Conditions (art. 5(4)): members named, with relationship, in a public or authenticated private deed dated BEFORE the tax year starts; the return states the shares and that they match the work done; each member declares continuous, prevalent work. Family: spouse, relatives to the third degree, in-laws to the second (art. 5(5)).
- **Businesses only.** Art. 5(4) speaks of the income of "imprese familiari" and of the "imprenditore"; a professional (arti e professioni) should not rely on it: refer.
- **No split in the forfettario:** the owner pays the substitute tax on income before the family's shares (Agenzia forfettario page).

### Oneri Deducibili (reduce taxable income): TUIR Art. 10

| Deduction | Detail | Legislation |
| --- | --- | --- |
| Contributi previdenziali | Compulsory contributions (gestione separata, artigiani, commercianti, a cassa), and voluntary ones to the same scheme | [TUIR art. 10(1)(e)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art10!vig=2026-06-30) |
| Fondi pensione integrativi | Within the D.Lgs. 252/2005 art. 8 limit (Section 8) | Art. 10(1)(e-bis) |
| Assegni periodici | To a spouse on separation or divorce, by court order; not child maintenance | Art. 10(1)(c) |

### Detrazioni (reduce tax payable): TUIR Art. 15

- Detrazioni cut the tax, not the income. Normattiva's art. 15(1) still prints its original rate and some limits only in lire; no detrazioni table or bonus rates are given here, nor family detrazioni (art. 12). Most detrazioni for oneri fall in the art. 16-ter cap; medical costs are outside the high-income cut. Use the Redditi PF instructions for 2026 income and `it-income-tax`.

## Section 4: Capital Allowances Optimization

- Businesses: TUIR art. 102. Professionals: TUIR art. 54-quinquies, own small-asset limit. Ignored in the forfettario (costs excluded).

### Ammortamento (Depreciation)

- Depreciation may not exceed the ministerial coefficient, "ridotti alla metà per il primo esercizio" (art. 102(2)). The D.M. 31 December 1988 table was not read; no per-class rates given here.

### Small assets expensed in the year

| What | Value | Note (source) |
| --- | --- | --- |
| Business asset: unit cost up to which it is expensed in the year bought | EUR 516.46 | "non è superiore a 516,46 euro" ([art. 102(5)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30)) |
| Professional's asset: the same limit | EUR 516.40 | "euro 516,40" ([art. 54-quinquies](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30)) |

### Motor Vehicle Deduction Limits (Art. 164 TUIR)

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30 |
| Cars not used only as business tools; individual professional: one vehicle only | 20% | "nella misura del 20 per cento" |
| Sales agents and representatives | 80% | "attività di agenzia" |
| Cars given to employees for mixed use most of the year | 70% | "uso promiscuo" |
| Sales agents: purchase cost counted up to | EUR 25,822.84 | "elevati rispettivamente a euro 25.822,84" |

- Only vehicles used exclusively as tools of the business itself (impresa) are deducted in full (art. 164(1)(a)). Cost caps still apply: purchase and hire costs count only up to limits that art. 164(1)(b) writes in lire; for sales agents the article prints the raised purchase limit in euro (table). Fuel is deductible only if paid by credit, debit or prepaid card (art. 164(1-bis)).

## Section 5: Loss Utilization

- Share of later business income that carried-forward business losses may offset: 80% ([TUIR art. 8](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art8!vig=2026-06-30)): "all'80 per cento dei relativi redditi".

| Relief | Detail |
| --- | --- |
| Professional losses | Subtracted from total income in the same year (art. 8(1)) |
| Business losses (individuals, s.n.c., s.a.s.) | Only against business income of the same year, then carried forward within the share above (art. 8(3)); never against rental or other income |
| First three tax periods | Carried forward in full, without the share limit above, if they relate to a new productive activity (art. 8(3) applying art. 84(2)) |
| Carry-back | Not provided in art. 8 or 84 |
| Forfettario | No loss. Contributions above forfettario income are deducted from total income the same year (Agenzia page); they do not carry forward |

### Strategy

- Start-up losses keep full value only under art. 84(2). Spending with no business purpose creates no loss.

## Section 6: Timing Strategies

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef |
| Payments on account, as a share of last year's tax (or of the lower tax expected) | 100% | "dell’imposta dichiarata nell’anno" |
| First instalment, by 30 June, general rule (not ISA taxpayers or forfettari) | 40% | "entro il 30 giugno" |
| Second instalment, by 30 November, general rule | 60% | "entro il 30 novembre" |

- **ISA taxpayers and forfettari** pay the acconto in two equal instalments on the same dates (Agenzia payment page; `it-estimated-tax`).

| Strategy | Detail |
| --- | --- |
| Forfettario limits | Tested on revenue earned or fees received in the year; watch both during the year. Splitting activity or invoices only to stay under them is a Section 10 risk |
| Costs (ordinario) | Professionals use the cash basis: costs count when paid (TUIR art. 54(1)) |
| Acconti | A lower forecast is allowed; underpaying on a wrong one brings penalties and interest (`it-estimated-tax`) |
| Pension fund | Paid by 31 December, within the Section 8 limit |

## Section 7: VAT Optimization (IVA)

| Strategy | Detail |
| --- | --- |
| Forfettario | No IVA charged or recovered; helps with private clients |
| Regime dei minimi | Closed to new entrants |
| IVA per cassa | By option, on supplies to business or professional customers: IVA due on payment, and IVA on purchases deductible on payment, for volume d'affari "non superiore a 2 milioni di euro" ([D.L. 83/2012 art. 32-bis](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-06-22;83~art32bis!vig=2026-06-30)); due anyway after one year. Not with special VAT schemes or reverse charge |
| Split payment, refunds, reverse charge | `italy-vat-return` |

## Section 8: Social Security Optimization

### INPS Contribution Structures

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf |
| Gestione separata: professionals with no other compulsory cover | 26.07% | "Soggetti non assicurati presso altra forma" |
| Gestione separata: pensioners or otherwise insured | 24% | "l’aliquota è confermata" |
| Gestione separata: maximum income | EUR 122,295 | "è pari a 122.295,00 euro" |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15162/Allegati/16561_Circolare-numero-14-del-09-02-2026.pdf |
| Artigiani rate | 24% | "Titolari e coadiuvanti" |
| Commercianti rate | 24.48% | "Titolari e coadiuvanti" |
| Income above which each rate rises by one point | EUR 56,224 | "all’importo di 56.224,00 euro" |
| Minimum income (minimale): contributions due even if income is lower | EUR 18,808 | "è pari a 18.808,00 euro" |
| Fixed contribution on the minimale, artigiani | EUR 4,521.36 | Circolare 14/2026, minimale table |
| Fixed contribution on the minimale, commercianti | EUR 4,611.64 | Circolare 14/2026, minimale table |
| Artigiani and commercianti: maximum income, contributors before 1996 | EUR 93,707 | "è pari a 93.707,00 euro" |
| The same, enrolled from 1996 with no earlier contributions | EUR 122,295 | "per il 2026, a 122.295,00 euro" |
| Optional cut for forfettario artigiani and commercianti | 35% | "riduzione contributiva" |

- A cassa member pays the cassa; its rates are on no allowed page (`it-inps-contributions`).

### Optimization Strategies

| Strategy | Detail |
| --- | --- |
| Forfettario cut | Forfettario artigiani and commercianti only, on application; continues unless renounced or conditions end. Renouncing is final. Lowers the future pension. Not for the gestione separata |
| Other cuts | Circolare 14/2026 also keeps a cut for artigiani and commercianti over 65 already drawing an INPS pension, and one for those first enrolled in 2025: `it-inps-contributions` |
| Minimum contribution | Artigiani and commercianti owe the fixed amount whatever their income |

### Fondi Pensione Integrativi (Supplementary Pension): TUIR Art. 10, D.Lgs. 252/2005

| What | Value | Note |
| --- | --- | --- |
| Source | D.Lgs. 252/2005 art. 8 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-12-05;252~art8!vig=2026-06-30 |
| Yearly deduction limit, from tax year 2026 | EUR 5,300 | "innalzato a euro 5.300" |
| Previous limit | EUR 5,164.57 | "non superiore ad euro 5.164,57" |
| Final withholding on the taxable part of the benefit (art. 11) | 15% | "con l'aliquota del 15 per cento" ([art. 11](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-12-05;252~art11!vig=2026-06-30)) |

- **Exit tax** falls by 0.30 percentage points per year of membership after the fifteenth, with a maximum cut of 6 percentage points (art. 11(6)).
- **First job started after 1 January 2007:** in the twenty years after the fifth year of membership, the unused limit of the first five years may be deducted, up to half the yearly limit (art. 8(6)).
- **Forfettario:** the deduction runs against total income; with no other income it may give nothing.

### PIR (Piani Individuali di Risparmio)

- PIR limits (L. 232/2016 art. 1 commi 100-114) could not be read (Normattiva returns only the first hundred commi). Out of scope; crypto: `italy-crypto-tax`.

### Bonus Investimenti

- None was read for 2026. Do not advise from this Guide.

### Impatriati and new residents

- Someone moving to Italy should check the impatriati regime first (D.Lgs. 209/2023 art. 5, linked in the method below): part of qualifying work income is exempt for five years, within a yearly cap. Detail: `it-impatriati`.

## Section 10: Red Lines

**Abuse of law, L. 212/2000 art. 10-bis** ([text](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-07-27;212~art10bis!vig=2026-06-30)):

- **Abuse:** operations without economic substance that, while formally within the rules, essentially produce undue tax advantages; the advantage is disregarded (art. 10-bis(1)).
- **Not abuse:** operations with valid, non-marginal non-tax reasons, including organisational ones that improve the business or profession (art. 10-bis(3)); the free choice between regimes (art. 10-bis(4)).
- **Procedure:** an interpello can be asked first (art. 10-bis(5)); the Agenzia must ask for explanations before assessing, and proves the abuse, while the taxpayer proves the non-tax reasons (art. 10-bis(6) and (9)).
- **Penalties:** abuse is not a crime; administrative penalties apply (art. 10-bis(13)); no penalty range is printed in the article.

| Risk | Detail |
| --- | --- |
| Forfettario splitting | Several VAT numbers in a family, or a linked S.r.l., to stay under the limits |
| False invoices | Four to eight years of prison ([D.Lgs. 74/2000 art. 2](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2000-03-10;74~art2!vig=2026-06-30)); less below centomila euro of fictitious costs |
| Evasion vs avoidance | Not filing is a crime above cinquantamila euro of tax evaded for any one tax ([art. 5](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2000-03-10;74~art5!vig=2026-06-30)); an understated return, above centomila euro evaded AND hidden income above ten per cent of that declared or two million euro ([art. 4](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2000-03-10;74~art4!vig=2026-06-30)) |

## Section 11: Annual Tax Planning Calendar

| Month | Action |
| --- | --- |
| January | Test last year's revenue and employment income against the forfettario conditions; confirm the INPS cut |
| May | Artigiani and commercianti: first fixed INPS instalment (`it-inps-contributions`) |
| June | By 30 June: IRPEF balance and first acconto; review the regime for the year |
| October | Modello Redditi PF by 31 October; estimate the year for the second acconto |
| November | By 30 November: second acconto |
| December | Pay deductible costs and pension contributions for the year |

## The method, step by step

1. Check residence and arrival date: impatriati first ([D.Lgs. 209/2023 art. 5](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-12-27;209~art5!vig=2026-06-30); `it-impatriati`).
2. Test the forfettario on the [Agenzia forfettario page](https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-); if open, compute both regimes on the client's figures (`it-income-tax`), add IVA effects, show both, without promising a saving.
3. Choose the legal form: IRPEF for a sole trader, IRES ([TUIR art. 77](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig=)) and IRAP for an S.r.l., profits paid out taxed again.
4. Set the INPS position from [Circolare n. 14/2026](https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15162/Allegati/16561_Circolare-numero-14-del-09-02-2026.pdf) (artigiani, commercianti) or Circolare n. 8/2026 (gestione separata); consider the forfettario cut.
5. Use contributions ([TUIR art. 10](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art10!vig=2026-06-30)) and the pension fund limit ([D.Lgs. 252/2005 art. 8](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-12-05;252~art8!vig=2026-06-30)).
6. Test each idea against [art. 10-bis](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-07-27;212~art10bis!vig=2026-06-30): a real non-tax reason? If in doubt, interpello.
7. Pay acconti as the [Agenzia payment page](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) sets out; file by 31 October ([D.P.R. 322/1998 art. 2](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30)).

## Ask the client first

- Revenue/fees last year and expected this year? Which ATECO code?
- Employment or pension income last year, how much? Job ended? Working mainly for a former employer?
- Stake in a partnership, professional association, impresa familiare, or control of an S.r.l.?
- Artigiano, commerciante, gestione separata or cassa member? Already a pensioner?
- When did you become resident in Italy?
- Profits kept in the business, or taken out each year?

## When to refuse or refer

- Splitting activity, invoices or VAT numbers, or moving income abroad, only to cut tax: refer, explaining art. 10-bis.
- S.r.l. incorporation, INPS for members, directors' pay, dividends: refer (`italy-formation`).
- Impatriati, new residents, non-residents, treaties: `it-impatriati`, or refer.
- 2026 detrazioni, building bonuses, PIR, investment credits, cassa rates: not proven here.
- Anything to be filed: estimate only, for a commercialista to confirm.

## Sources

- Every page used is linked once in the tables or text above; plus D.Lgs. 117/2026 art. 377: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117:1~art377

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Commercialista or equivalent licensed practitioner in Italy) before filing or acting upon.

> Contributed by OpenAccountants.

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
