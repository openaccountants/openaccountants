---
name: it-estimated-tax
description: Use this skill whenever asked about Italian estimated income tax advance payments (acconti IRPEF) for self-employed individuals, freelancers, or professionisti. Trigger on phrases like "acconti IRPEF", "acconto imposta", "estimated tax Italy", "Italian advance tax", "primo acconto", "secondo acconto", "historical method", "forecast method", "metodo storico", "metodo previsionale", "F24 payment", or any question about advance income tax obligations under the TUIR. Covers the two-instalment schedule (40% by Jun 30, 60% by Nov 30), historical vs forecast computation methods, the EUR 257.52 threshold, penalties for shortfall, and F24 payment procedures. ALWAYS read this skill before touching any estimated tax work for Italy.
version: 2.2
jurisdiction: IT
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian income tax payments on account (acconti) v2.1

Tax year **2026**. This skill calculates advances paid during 2026, credited against 2026 tax declared in 2027. The published **Redditi PF 2026** instructions report 2025 income and expressly instruct how to calculate **2026 advances**. Return-year and income-year references must not be interchanged. Outputs are working papers for a commercialista.

## Who this applies to

Italian resident individuals paying their own IRPEF or forfettario substitute-tax advances, including self-employed professionals. Cedolare secca, IRAP for entities and INPS gestione separata are separately identified below. A bank debit labelled F24 alone does not identify a tax or a deduction. The rates and dates are sourced from [AdE Come si paga l'Irpef](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) and [Redditi PF 2026, Fascicolo 1, sections 7–8 and RN61–RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026).

Obtain the previous return's RN34 **Differenza**, or recomputed RN61 column4 for a listed special case; for forfettario obtain the previous substitute tax instead. Also obtain regime/ISA status, withholdings, expected current-year income if forecasting, rents and pension fund, and F24 history. Without the historical base, do not invent an advance. Without projections, do not use the forecast method.

This computation excludes non-resident payment procedures, foreign-tax-credit timing and detailed regional/municipal addizionali (R-IT-ET-1 to 3). A regime change or first year following a regime change requires review. Addizionale comunale has its own advance, addressed by RV17; it is not part of IRPEF advances (PF1 section7).

## Rates, bands and thresholds

| Rule | Value | Note (verbatim) | Period | Official source |
| --- | --- | --- | --- | --- |
| No acconto unless last year's tax, after detrazioni, credits, withholdings and surpluses, is above | EUR 51.65 | "superiore a 51,65 euro" | 2026 | [AdE IRPEF payment guidance](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) |
| Acconto as a share of last year's tax, or of the lower tax expected for this year | 100% | "L’acconto è pari al 100%" | 2026 | [AdE IRPEF payment guidance](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) |
| One payment by 30 November if the acconto is below; two instalments if at or above | EUR 257.52 | "inferiore a 257,52 euro" | 2026 | [AdE IRPEF payment guidance](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) |
| First instalment, by 30 June with last year's balance | 40% | "la prima è pari al 40%" | 2026 | [AdE IRPEF payment guidance](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) |
| Second instalment, by 30 November | 60% | "restante 60%" | 2026 | [AdE IRPEF payment guidance](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) |
| ISA taxpayers and forfettari: one payment by 30 November if the total is not above; otherwise two equal instalments on the same dates | EUR 206 | "non supera 206 euro" | 2026 | [AdE IRPEF payment guidance](https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef) |

**Return rules, surcharge, instalment interest and offsets (Redditi PF 2026, Fascicolo 1)**

| Rule | Value | Note (verbatim) | Period | Official source |
| --- | --- | --- | --- | --- |
| The return works in whole euro: no acconto if RN34 (or RN61 column 4) is below | EUR 52 | "è inferiore ad euro 52,00 l’acconto non è dovuto" | 2026 | [PF1 RN62 (2026 advances)](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026) |
| Single payment when the first instalment would not exceed | EUR 103 | "non superi euro 103,00 nel qual caso" | 2026 | [PF1 RN62 (2026 advances)](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026) |
| Surcharge for paying balance and first acconto by 30 July (Deferral and monthly instalments) | 0.40% | "maggiorazione dello 0,40 per cento a titolo di interesse corrispettivo" | 2026 | [PF1 section 7 (payments/instalments)](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026) |
| Interest on instalments, yearly rate (commercial method) | 4% | "interessi nella misura del 4 per cento annuo" | 2026 | [PF1 section 7 (payments/instalments)](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026) |
| Interest added for each further monthly instalment, whatever the payment day; it builds up month by month, and Fascicolo 1 prints the running total for each instalment | 0.33% | "0,33 per cento in misura forfetaria" | 2026 | [PF1 section 7 (payments/instalments)](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026) |
| Credit offset needing a visto di conformità, above | EUR 5,000 | "credito di importo superiore a 5.000 è necessario" | 2026 | [PF1 section 8 (credit offsets)](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026) |

**IRAP acconti (2026 IRAP instructions)**

| Rule | Value | Note (verbatim) | Period | Official source |
| --- | --- | --- | --- | --- |
| Acconto on the historical method, share of last year's IRAP | 100% | "nella misura pari al 100 per cento" | 2026 | [IRAP 2026 instructions, Acconti / DPR 435 art. 17](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414) |
| Partnerships: acconto due only if last year's IRAP is above | EUR 51.65 | "sempreché tale importo sia superiore a euro 51,65" | 2026 | [IRAP 2026 instructions, Acconti / DPR 435 art. 17](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414) |
| Companies and other taxpayers: acconto due only if last year's IRAP is above | EUR 20.66 | "sempreché tale importo sia superiore a euro 20,66" | 2026 | [IRAP 2026 instructions, Acconti / DPR 435 art. 17](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414) |
| First instalment, with the balance | 40% | "la prima, pari al 40 per cento" | 2026 | [IRAP 2026 instructions, Acconti / DPR 435 art. 17](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414) |
| Second instalment, by 30 November 2026 (partnerships) | 60% | "la seconda, pari al residuo 60 per cento, entro il 30 novembre 2026" | 2026 | [IRAP 2026 instructions, Acconti / DPR 435 art. 17](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414) |
| ISA taxpayers: two instalments of | 50% | "in due rate ciascuna nella misura del 50 per cento" | 2026 | [IRAP 2026 instructions, Acconti / DPR 435 art. 17](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414) |

Companies ordinarily pay the balance and first IRAP advance by the last day of the sixth month after year end, with the second in the eleventh month. Late statutory accounts-approval cases have the distinct first-payment rules of DPR 435/2001 art. 17(1). Check the IRAP recomputations and specialist exclusions before using the ordinary historical base (`it-irap`).

**INPS gestione separata acconti (Redditi PF 2026, Fascicolo 2, Appendice)**

| Rule | Value | Note (verbatim) | Period | Official source |
| --- | --- | --- | --- | --- |
| Share of 2025 professional income on which the 2026 acconti total is worked out, at 2026 rates | 80% | "sull’80% del reddito di lavoro" | 2026 | [PF2 Appendice, INPS acconti](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) |

| Item | Rate and conditions | Period | Official source |
| --- | --- | --- | --- |
| Legal interest for late tax | **1.60% a year from 1 January 2026**; daily calculation, separate from 4% instalment interest | 2026 only | [DM 10 December 2025 art.1](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.dataPubblicazioneGazzetta=2025-12-13&atto.codiceRedazionale=25A06705&atto.tipoProvvedimento=DECRETO) |

## The base

### Historical and forecast methods

- **Historical method formula.**acconto = RN34 (or RN61 column 4), split as in the tables. For ISA taxpayers the first instalment is half ("il cinquanta per cento per i soggetti ISA", AdE payment guidance and PF1 RN62).
- **Casi particolari (rigo RN61).** For the 2026 acconto, last year's tax is recomputed in listed cases (occasional boat hire, fuel stations, the new-hires deduction of D.Lgs. 216/2023 art. 4, capital gains under TUIR art. 86(4) as changed by Law 199/2025). The acconto then uses RN61 column 4.
- **First year of activity.** No tax last year means no acconto on the historical method; the first year's balance falls under the following year's ordinary payment timetable.

### Forecast method

- **Forecast method formula.** A client who expects lower tax this year may base the acconti on it, with the same shares and dates. Rigo RN62 still shows the historical amounts, not the lower ones paid (Fascicolo 1).
- **Forecast method risk.** If the forecast leaves an advance shortfall, the unpaid advance is subject to the late-payment rules. The penalty is "venticinque per cento" (twenty-five per cent) of each amount not paid, halved if paid within ninety days, and reduced further up to fifteen days late (D.Lgs. 471/1997 art. 13(1), Penalties and interest). The statute prints these rates only in words. Always flag for commercialista.

### Regime forfettario

- **Regime forfettario computation.** Base = last year's substitute tax, NOT IRPEF. Same minimum and dates as IRPEF, but two EQUAL instalments, and a single payment by 30 November when the total is not above the forfettario threshold in the Rates, bands and thresholds table. Codes 1790 and 1791. The substitute tax and application of IRPEF payment provisions are set by [Law 190/2014 art. 1(64)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-10-29).

### Other advances kept separate

- **Cedolare secca (rigo LC2).** The whole of last year's cedolare secca, with the IRPEF minimum, threshold, shares and dates of Rates, bands and thresholds; codes 1840 and 1841. Forecast method and monthly instalments of the first instalment allowed (Fascicolo 1).
- **IRAP** (partnerships, companies; individuals no longer pay it). See the table below and `it-irap`.
- **INPS gestione separata** (professionals without their own fund). Two acconti of equal amount on the IRPEF acconto dates. Total: 2026 rates on the share of 2025 professional income in the rates table, within the 2026 massimale. They go in the INPS section of the F24 (causale PXX or P10). Rates are in `it-inps-contributions`. Artigiani and commercianti pay acconti on income above the minimale on the same dates: see `it-inps-artigiani-commercianti`.

Use the confirmed regime, not the bank description, to select the base. An F24 tax advance is a payment towards the taxpayer's liability; classification is a working-paper convention, not evidence that the amount is a deductible business expense.

## Deadlines and filing

Ordinary **2026** dates are **30 June** for balance/first advance, **30 July** if using the 30-day **0.40%** deferral, and **30 November** for the second/single advance. These dates are working days in 2026. Check any taxpayer-specific extension before payment. The ordinary deferral does not move the second advance ([DPR 435/2001 art.17](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:2001-12-07;435~art17!vig=2026-10-29); [PF1 section7](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026)).

### Deferral and monthly instalments

- **Maggiorazione for deferral.** Balance and primo acconto may be paid within the 30 days after 30 June, that is by 30 July, adding the surcharge in the Rates, bands and thresholds tables first (D.P.R. 435/2001 art. 17(2)). The secondo acconto cannot be deferred this way. After the deadline, ravvedimento operoso applies (Voluntary regularisation). Deadlines falling on a Saturday or holiday move to the next working day.

### Rateizzazione (monthly instalments)

- The balance and the primo acconto (and the INPS contributions in Quadro RR above the minimale) may be paid in monthly instalments. The secondo acconto may not. The first instalment is due on the normal date (30 June, or 30 July with the surcharge); the later ones by the 16th of each month, except that instalments falling due from 1 to 20 August may be paid by 20 August (DL 223/2006 art. 37(11-bis)). All must be finished by 16 December of the year the return is filed (D.Lgs. 241/1997 art. 20(1), (4)). Instalments may cover only some items: for example, the primo acconto in instalments and the balance in one go. Interest (rates in the Rates, bands and thresholds tables) is paid on its own line (code 1668).

The PF1 instructions cite the newer collection code for instalments, but D.Lgs. 33/2025 annex article 243 now defers that code to **1 January 2027**. For 2026 use the continuing D.Lgs. 241/1997 article 20 and DL 223/2006 article 37(11-bis), which preserve the stated 16 December and August rules.

### F24 codes and payment

### Codici tributo

**Codici tributo table** (Fascicolo 1, "Principali codici tributo")

| Code | Description |
| --- | --- |
| 4001 | IRPEF: saldo |
| 4033 | IRPEF: primo acconto |
| 4034 | IRPEF: secondo acconto or single payment |
| 1668 | Interest on instalments |
| 1792 | Forfettario substitute tax: saldo |
| 1790 | Forfettario substitute tax: primo acconto |
| 1791 | Forfettario substitute tax: secondo acconto or single payment |
| 1842 | Cedolare secca: saldo |
| 1840 | Cedolare secca: primo acconto |
| 1841 | Cedolare secca: secondo acconto or single payment |

INPS gestione separata acconti are not paid with an Erario tax code but in the INPS section, with causale PXX (no other cover) or P10 (pensioner or other cover): see `it-inps-contributions`.

### Filing steps

- **Filing steps.** VAT number holders pay by F24 electronically, directly (F24 online, F24 web) or through an intermediary (Fascicolo 1). Erario section: tax code, reference year (2026 for the 2026 acconti), amount; the "Rateazione" column for instalments. Keep the receipt.

### Compensazione (offsetting)

- **Compensazione rules.** Tax credits can be offset against acconti in the F24. For relevant annual return credits used horizontally against different liabilities, the ordinary EUR 5,000 threshold brings the visto and tenth-day-after-filing requirements in PF1 section8. Check credit-specific exemptions and restrictions; do not apply this as an unconditional rule to every credit or same-tax offset.

### Bank-line classification aids

The following are **unverified bookkeeping cues, not legal due-date rules or proof of payment**. Confirm the actual tax, reference year, amount and receipt. A June/July debit often contains the previous balance and current advance; a November debit can be the second/single advance. An instalment's actual due date comes from the rules above, not a matching window. Preserve the legacy matching patterns only as cues:

Pre-classifier for bank lines. Confirm each match with the F24 receipt.

### F24 IRPEF advance debits

**F24 IRPEF advance debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| F24, MODELLO F24, PAGAMENTO F24 | IRPEF acconto (probable) | Check timing and tax code |
| AGENZIA ENTRATE, AG ENTRATE | IRPEF acconto (probable) | Revenue agency payment |
| ACCONTO IRPEF, PRIMO ACCONTO, SECONDO ACCONTO | IRPEF acconto | Explicit description |
| Tax code 4033 | Primo acconto IRPEF | Code list in F24 codes and payment |
| Tax code 4034 | Secondo or single acconto IRPEF | |
| Tax code 1790 | Primo acconto forfettario | Imposta sostitutiva |
| Tax code 1791 | Secondo or single acconto forfettario | Imposta sostitutiva |
| Tax code 1840 or 1841 | Acconto cedolare secca | Rents, not business income |
| INPS section, causale PXX or P10 | Saldo or acconto INPS gestione separata | Social contribution, not tax (see `it-inps-contributions`) |

### Timing-based identification

**Timing-based identification**

| Debit date range | Likely payment | Confidence |
| --- | --- | --- |
| 25 June to 5 July | Balance plus primo acconto | High if F24 reference |
| 25 July to 5 August | Primo acconto with the deferral surcharge (Deferral and monthly instalments) | High |
| 16th of each month, July to December (20 August in August) | Monthly instalment (Deferral and monthly instalments) | Medium |
| 25 November to 5 December | Secondo or single acconto | High |

### Related but NOT IRPEF acconti

**Related but NOT IRPEF acconti**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IVA, tax code 6099, LIQUIDAZIONE IVA | EXCLUDE | VAT payment |
| INPS, CONTRIBUTI PREVIDENZIALI | EXCLUDE | Social security contribution |
| tax code 1001, RITENUTE LAVORO | EXCLUDE | Employee withholding payment |
| IMU, TASI, TARI | EXCLUDE | Property and municipal taxes |
| SALDO IRPEF, tax code 4001 | Flag for reviewer | Balance for last year, not an acconto |
| Tax code 1668 | Flag for reviewer | Interest on instalments |
| RAVVEDIMENTO | Flag for reviewer | Voluntary regularisation payment |
| ADDIZIONALE REGIONALE, ADDIZIONALE COMUNALE | EXCLUDE | Separate from IRPEF acconti |

## Penalties and interest

### Sanzione for insufficient/omitted acconti

**Sanzione table**

| Violation | Base penalty (D.Lgs. 471/1997 art. 13(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30) |
| --- | --- |
| Omitted acconto | venticinque per cento (twenty-five per cent) of the unpaid amount |
| Insufficient acconto | The same, on the shortfall |
| Paid within ninety days | Half of that |
| Paid within fifteen days | One fifteenth of the halved penalty for each day late |

D.Lgs. 471/1997 art. 13 and D.Lgs. 472/1997 art. 13 are shown on Normattiva as in force until 31 December 2026. The testo unico delle sanzioni tributarie (D.Lgs. 173/2024) applies from 1 January 2027 (its art. 102: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=). For a late 2026 payment regularised in 2027, check which text applies.

### Ravvedimento operoso (voluntary regularisation)

The penalty is reduced if the client pays of their own accord (D.Lgs. 472/1997 art. 13(1): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-06-30). For taxes run by the Agenzia delle Entrate, such as IRPEF, an audit already under way does not bar this; only the notification of an assessment, or of a notice of amounts due after the checks of the return, does (art. 13(1-ter)). Later stages of an audit carry other fractions (letters b-ter to b-quinquies): refer. The statute states the reductions as fractions of the minimum penalty:

**Ravvedimento operoso table**

| Timing | Reduced penalty |
| --- | --- |
| Unpaid tax or acconto paid within thirty days | One tenth of the minimum (letter a) |
| Within ninety days | One ninth (letter a-bis) |
| Within the deadline for the return of the year of the violation | One eighth (letter b) |
| After that deadline | One seventh (letter b-bis) |

- **Legal interest rate.** Legal-rate interest runs daily on the late tax. The rate for 2026 is **1.60% a year from 1 January 2026**, set by DM 10 December 2025 art.1. Split interest at each year's applicable rate if the delay crosses year end; do not assume this rate for 2027.

### Ravvedimento formula

- **Ravvedimento formula.** amount_due = unpaid_tax + (unpaid_tax x base penalty x reduction fraction) + interest, where interest = unpaid_tax x (legal_rate / 365) x days_late. Penalty and interest go on their own F24 lines.

## Cross-border points

Foreign-source income and foreign-tax-credit timing, non-resident methods of paying, and a move into/out of Italy need the dedicated residence and cross-border analysis (`it-cross-border`, `it-income-tax`). This skill does not conclude that residents and non-residents have the same payment procedure. Do not classify an overseas tax payment as Italian acconto from its bank text.

## Two worked examples that recompute

### Example 1: ordinary historical advance

Assume RN34 is **EUR 6,000**, there is no RN61 recomputation, no ISA/forfettario status and no taxpayer-specific extension. The advance is 100% of the base: **EUR 6,000**. The 40% first share is **EUR 2,400**, due 30 June 2026; the 60% remainder is **EUR 3,600**, due 30 November 2026. If the first share is instead deferred to 30 July, its 0.40% surcharge is **EUR 9.60**, giving **EUR 2,409.60**. The second share/date does not change.

```oa-check
name: Italy ordinary 2026 advance and optional July deferral
inputs:
  historical_net_tax: 6000
steps:
  total_advance: historical_net_tax * 1
  first_advance: total_advance * 0.40
  second_advance: total_advance - first_advance
  july_surcharge: first_advance * 0.004
  deferred_first: first_advance + july_surcharge
expected:
  total_advance: 6000
  first_advance: 2400
  second_advance: 3600
  july_surcharge: 9.60
  deferred_first: 2409.60
```

### Example 2: reduced late-payment penalty, paid inside 2026

Assume a second advance of **EUR 3,600** due 30 November 2026 is paid **18 days late**, on 18 December 2026. Assume the taxpayer qualifies for voluntary correction before any barring notice. The ordinary 25% penalty is halved within 90 days, then reduced to one tenth for payment within 30 days: **EUR 45**. Legal interest at 1.60% for 18/365 days is **EUR 2.84**, rounded to cents. Total tax, penalty and interest is **EUR 3,647.84**, on the appropriate separate F24 lines. This is voluntary correction of an overdue amount, not the optional timely July deferral.

```oa-check
name: Italy second advance paid 18 days late during 2026
inputs:
  unpaid_advance: 3600
  days_late: 18
steps:
  reduced_penalty: unpaid_advance * 0.25 / 2 / 10
  legal_interest: round(unpaid_advance * 0.016 * days_late / 365, 2)
  total_payment: unpaid_advance + reduced_penalty + legal_interest
expected:
  reduced_penalty: 45
  legal_interest: 2.84
  total_payment: 3647.84
```

### Preserved qualitative scenarios

Examples use shares; the rates and thresholds are in Rates, bands and thresholds.

#### Legacy scenario 1: Standard two-instalment (historical method)

**Example 1 table**

| Instalment | Due date | Share | Amount |
| --- | --- | --- | --- |
| Primo acconto | 30 June 2026 | First share, Rates, bands and thresholds | Last year's RN34 x first share |
| Secondo acconto | 30 November 2026 | Second share, Rates, bands and thresholds | Last year's RN34 x second share |
| **Total** |  | **The whole of RN34** | **Last year's RN34** |

Applies when RN34 is at or above the two-instalment threshold.

#### Legacy scenario 2: Single instalment (below EUR 257.52)

RN34 above the minimum but below the two-instalment threshold: the whole RN34 by 30 November 2026.

#### Legacy scenario 3: Below minimum threshold

RN34 below the minimum in Rates, bands and thresholds: no acconto.

#### Legacy scenario 4: Regime forfettario

**Example 4 table**

| Instalment | Due date | Codice tributo | Amount |
| --- | --- | --- | --- |
| Primo acconto | 30 June 2026 | 1790 | Half of last year's substitute tax |
| Secondo acconto | 30 November 2026 | 1791 | The other half |

Forfettari pay equal halves; at or below the forfettario single-payment threshold (Rates, bands and thresholds), all by 30 November with code 1791.

#### Legacy scenario 5: Primo acconto deferral

**Input:** the client cannot pay by 30 June 2026 and pays by 30 July 2026.

**Computation:** balance and primo acconto each increased by the Deferral and monthly instalments surcharge. The secondo acconto date does not move.

#### Legacy scenario 6: Bank statement classification

**Input line:** `30.06.2026 ; F24 TELEMATICO AGENZIA ENTRATE ; DEBIT ; COD.4033 ; ANNO:2026`

**Classification:** primo acconto IRPEF for 2026. A tax payment, not a deductible business expense.

### Preserved scenario checks

#### Scenario check 1: Standard two-instalment

Input: last year's RN34 at or above the two-instalment threshold; not ISA. Expected: first share of RN34 by 30 June, the rest by 30 November; total = RN34.

#### Scenario check 2: Single instalment

Input: last year's RN34 above the minimum, below the two-instalment threshold. Expected: the whole RN34 by 30 November.

#### Scenario check 3: Below minimum

Input: last year's RN34 below the minimum. Expected: no acconti.

#### Scenario check 4: Forfettario

Input: last year's substitute tax above the forfettario single-payment threshold. Expected: half by 30 June (code 1790), half by 30 November (code 1791).

#### Scenario check 5: Deferral with maggiorazione

Input: primo acconto paid by 30 July. Expected: primo acconto increased by the Deferral and monthly instalments surcharge; secondo acconto still 30 November.

#### Scenario check 6: First year

Input: first year of activity, no prior return. Expected: no acconti under the historical method.

#### Scenario check 7: Ravvedimento (30-day late)

Input: secondo acconto paid 25 days late, before any audit. Expected: penalty = base penalty (Penalties and interest, halved because within ninety days) x one tenth (Voluntary regularisation), plus legal interest for 25 days.

## Ask the client first

- What was your net tax in last year's return (rigo RN34), and did any of the RN61 special cases apply?
- Are you in the forfettario or the ordinary regime, and did that change this year?
- Is your activity subject to the ISA reliability indices?
- Do you expect this year's income or deductions to be very different from last year's?
- Do you let property under cedolare secca, and which INPS fund do you pay into?
- Were any of this year's dates already missed?

### Review gates and exceptions

- Forecast method: not without a commercialista (penalty risk).
- Non-residents and cross-border income (R-IT-ET-1, R-IT-ET-2).
- A client moving into or out of the forfettario, or with a first year after a change of regime.
- Detailed addizionale regionale or comunale acconti (R-IT-ET-3).
- An audit already under way: refer.

- NEVER use the forecast method without flagging for commercialista and warning about the late payment penalty
- NEVER confuse IRPEF codes (4033 and 4034) with forfettario codes (1790 and 1791) or cedolare secca codes (1840 and 1841)
- NEVER ignore the two-instalment threshold ("pari o superiore")
- NEVER use the general shares for ISA taxpayers or forfettari: they pay equal halves
- NEVER forget the maggiorazione when deferring the primo acconto to July

### Self-checks

Before delivering output, verify:

- [ ] Last year's RN34 (or RN61 column 4) or forfettario substitute tax confirmed
- [ ] Correct threshold applied (minimum, two-instalment threshold, ISA and forfettario threshold)
- [ ] ISA status confirmed: general shares or equal halves
- [ ] Method identified (historical vs forecast), with a flag for forecast
- [ ] Correct codici tributo (4033 and 4034 IRPEF, 1790 and 1791 forfettario, 1840 and 1841 cedolare secca)
- [ ] Penalty and ravvedimento rules current for the date of the violation
- [ ] Maggiorazione noted if deferral is relevant; instalment interest if paying monthly
- [ ] Compensazione visto threshold checked
- [ ] Due dates confirmed with weekend and holiday adjustments
- [ ] Output labelled as estimated until commercialista confirms

## Sources

| Source and provision | Official URL | Read on |
| --- | --- | --- |
| AdE Come si paga l'Irpef, updated 12 March 2026 | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef | 2026-10-29 |
| AdE Redditi PF 2026 Fascicolo 1: sections 7–8,RN61–62,LC2 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026 | 2026-10-29 |
| AdE Redditi PF 2026 Fascicolo 2: QuadroRR/Appendice acconti | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 | 2026-10-29 |
| AdE IRAP 2026 instructions: acconti 2026 | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 | 2026-10-29 |
| DPR 435/2001 art.17 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:2001-12-07;435~art17!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 471/1997 art.13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 472/1997 art.13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-29 | 2026-10-29 |
| DM 10 December 2025 art.1,GU289/2025 | https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.dataPubblicazioneGazzetta=2025-12-13&atto.codiceRedazionale=25A06705&atto.tipoProvvedimento=DECRETO | 2026-10-29 |
| D.Lgs. 173/2024 annex art.102 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 241/1997 art. 20 (2026 instalment rule) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art20!vig=2026-10-29 | 2026-10-29 |
| DL 223/2006 art. 37(11-bis) (August postponement) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 33/2025 annex art. 243 (application from 2027) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2025-03-24;33:1~art243!vig=2026-10-29 | 2026-10-29 |
| Law 190/2014 art. 1(64), forfettario substitute tax and IRPEF payment rules | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-10-29 | 2026-10-29 |

**Not yet confirmed:** taxpayer-specific extensions; detailed addizionale computations/local rates; foreign-credit timing and non-resident payment mechanics; regime-transition bases; post-notice/audit-stage voluntary-correction fractions and successor rules for regularisation in 2027; any 2027 interest rate. The bank matching windows are heuristic cues only. No prior executable check was removed: the earlier skill had none; all six prose examples and seven qualitative scenario checks are retained.

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
