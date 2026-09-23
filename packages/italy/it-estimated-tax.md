---
name: it-estimated-tax
description: Use this skill whenever asked about Italian estimated income tax advance payments (acconti IRPEF) for self-employed individuals, freelancers, or professionisti. Trigger on phrases like "acconti IRPEF", "acconto imposta", "estimated tax Italy", "Italian advance tax", "primo acconto", "secondo acconto", "historical method", "forecast method", "metodo storico", "metodo previsionale", "F24 payment", or any question about advance income tax obligations under the TUIR. Covers the two-instalment schedule (40% by Jun 30, 60% by Nov 30), historical vs forecast computation methods, the EUR 257.52 threshold, penalties for shortfall, and F24 payment procedures. ALWAYS read this skill before touching any estimated tax work for Italy.
version: 2.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian income tax payments on account (acconti)

How an Italian self-employed person pays income tax in advance (acconti): who owes them, how much, when, the historical and forecast methods, penalties, monthly instalments, and the matching acconti for the forfettario, cedolare secca, IRAP and INPS gestione separata. Figures are for tax year 2026. Italy's tax year is the calendar year: the 2026 acconti are paid during 2026 and set off against the tax declared in 2027. The rules come from the Agenzia delle Entrate page on paying IRPEF (updated 12 March 2026) and the instructions to Modello Redditi PF 2026 (Fascicolo 1 and 2), which cover the 2025 return and set out the acconti for 2026. The IRAP rules come from the 2026 IRAP instructions (tax year 2025), used for 2026. Statutes were read on Normattiva as in force on 30 June 2026.

## Section 1: Quick reference

**Section 1 quick reference table**

| Field | Value |
| --- | --- |
| Country | Italy |
| Tax | Payments on account (acconti) of IRPEF, forfettario substitute tax, cedolare secca, IRAP and INPS gestione separata |
| Primary legislation | D.P.R. 435/2001 art. 17 (dates, instalments, the 30-day deferral) |
| Supporting legislation | D.Lgs. 33/2025 art. 10 (monthly instalments); D.Lgs. 471/1997 art. 13 (late payment penalty); D.Lgs. 472/1997 art. 13 (ravvedimento); D.Lgs. 173/2024 (testo unico sanzioni) from 1 January 2027 |
| Authority | Agenzia delle Entrate |
| Portal | Agenzia delle Entrate online services, or an authorised intermediary |
| Currency | Euro only |
| Payment schedule | First instalment with last year's balance by 30 June (or 30 July with a surcharge); second or single instalment by 30 November. Shares and thresholds: the table in Section 5.1 |
| Computation basis | Historical method: last year's net tax (rigo RN34 of Modello Redditi PF). Forecast method: the lower tax expected for this year |
| F24 codes | 4033 and 4034 (IRPEF), 1790 and 1791 (forfettario), 1840 and 1841 (cedolare secca). INPS gestione separata goes in the INPS section with causale PXX or P10 (`it-inps-contributions`) |
| Contributor | Open Accountants Community |
| Validated by | Pending. Requires sign-off by an Italian commercialista |
| Validation date | Pending |

**Instalment schedule summary** (amounts and shares in the tables of Section 5.1)

| Condition | Schedule |
| --- | --- |
| Acconto at or above the two-instalment threshold | First share by 30 June, rest by 30 November |
| Acconto due but below the two-instalment threshold | All of it by 30 November |
| Last year's net tax not above the minimum | No acconto |
| ISA taxpayers and forfettari | Two equal instalments on the same dates, with their own single-payment threshold |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Historical vs forecast method | Historical method |
| Regime unclear (ordinario vs forfettario) | Confirm first: different codes and split |
| ISA status unclear | Ask: ISA means equal halves |
| Primo acconto deferral | Surcharge if paid by 30 July (Section 5.4) |
| Addizionali regionali/comunali | The comunale has its own acconto (rigo RV17). Flag for reviewer |

## Section 2: Required inputs and refusal catalogue

- **Required inputs: minimum viable.** Last year's net IRPEF from Modello Redditi PF (rigo RN34 "Differenza", or rigo RN61 column 4 when one of the "casi particolari" applies), OR last year's forfettario substitute tax.
- **Required inputs: recommended.** Regime, ISA status, this year's expected income (forecast method), withholdings, cedolare secca rents, INPS fund.
- **Required inputs: ideal.** Last year's full return, F24 history, Cassetto Fiscale data.
- **Refusal policy if minimum is missing.** HARD STOP for the historical method without rigo RN34. The forecast method needs this year's projections: flag for commercialista.
- **R-IT-ET-1: Cross-border income.** Trigger: foreign-source income affecting foreign tax credit timing. Message: "Cross-border income interactions with Italian acconti are outside this Guide."
- **R-IT-ET-2: Non-resident advance payments.** Trigger: non-resident client. Message: "Non-resident advance tax obligations have different rules."
- **R-IT-ET-3: Addizionali computation.** Trigger: detailed addizionale acconto computation. Message: "Addizionali advances are separate obligations with local rates. Consult a commercialista."

## Section 3: Payment pattern library

Pre-classifier for bank lines. Confirm each match with the F24 receipt.

### 3.1 F24 IRPEF advance debits

**F24 IRPEF advance debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| F24, MODELLO F24, PAGAMENTO F24 | IRPEF acconto (probable) | Check timing and tax code |
| AGENZIA ENTRATE, AG ENTRATE | IRPEF acconto (probable) | Revenue agency payment |
| ACCONTO IRPEF, PRIMO ACCONTO, SECONDO ACCONTO | IRPEF acconto | Explicit description |
| Tax code 4033 | Primo acconto IRPEF | Code list in Section 7.1 |
| Tax code 4034 | Secondo or single acconto IRPEF | |
| Tax code 1790 | Primo acconto forfettario | Imposta sostitutiva |
| Tax code 1791 | Secondo or single acconto forfettario | Imposta sostitutiva |
| Tax code 1840 or 1841 | Acconto cedolare secca | Rents, not business income |
| INPS section, causale PXX or P10 | Saldo or acconto INPS gestione separata | Social contribution, not tax (see `it-inps-contributions`) |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely payment | Confidence |
| --- | --- | --- |
| 25 June to 5 July | Balance plus primo acconto | High if F24 reference |
| 25 July to 5 August | Primo acconto with the deferral surcharge (Section 5.4) | High |
| 16th of each month, July to December (20 August in August) | Monthly instalment (Section 5.5) | Medium |
| 25 November to 5 December | Secondo or single acconto | High |

### 3.3 Related but NOT IRPEF acconti

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

## Section 4: Worked examples

Examples use shares; the rates and thresholds are in Section 5.1.

### Example 1: Standard two-instalment (historical method)

**Example 1 table**

| Instalment | Due date | Share | Amount |
| --- | --- | --- | --- |
| Primo acconto | 30 June 2026 | First share, Section 5.1 | Last year's RN34 x first share |
| Secondo acconto | 30 November 2026 | Second share, Section 5.1 | Last year's RN34 x second share |
| **Total** |  | **The whole of RN34** | **Last year's RN34** |

Applies when RN34 is at or above the two-instalment threshold.

### Example 2: Single instalment (below EUR 257.52)

RN34 above the minimum but below the two-instalment threshold: the whole RN34 by 30 November 2026.

### Example 3: Below minimum threshold

RN34 below the minimum in Section 5.1: no acconto.

### Example 4: Regime forfettario

**Example 4 table**

| Instalment | Due date | Codice tributo | Amount |
| --- | --- | --- | --- |
| Primo acconto | 30 June 2026 | 1790 | Half of last year's substitute tax |
| Secondo acconto | 30 November 2026 | 1791 | The other half |

Forfettari pay equal halves; at or below the forfettario single-payment threshold (Section 5.1), all by 30 November with code 1791.

### Example 5: Primo acconto deferral

**Input:** the client cannot pay by 30 June 2026 and pays by 30 July 2026.

**Computation:** balance and primo acconto each increased by the Section 5.4 surcharge. The secondo acconto date does not move.

### Example 6: Bank statement classification

**Input line:** `30.06.2026 ; F24 TELEMATICO AGENZIA ENTRATE ; DEBIT ; COD.4033 ; ANNO:2026`

**Classification:** primo acconto IRPEF for 2026. A tax payment, not a deductible business expense.

## Section 5: Computation rules

### 5.1 Historical method (metodo storico): default

**IRPEF acconto (Agenzia delle Entrate page, updated 12 March 2026)**

| Rule | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef |
| No acconto unless last year's tax, after detrazioni, credits, withholdings and surpluses, is above | EUR 51.65 | "superiore a 51,65 euro" |
| Acconto as a share of last year's tax, or of the lower tax expected for this year | 100% | "L’acconto è pari al 100%" |
| One payment by 30 November if the acconto is below; two instalments if at or above | EUR 257.52 | "inferiore a 257,52 euro" |
| First instalment, by 30 June with last year's balance | 40% | "la prima è pari al 40%" |
| Second instalment, by 30 November | 60% | "restante 60%" |
| ISA taxpayers and forfettari: one payment by 30 November if the total is not above; otherwise two equal instalments on the same dates | EUR 206 | "non supera 206 euro" |

**Return rules, surcharge, instalment interest and offsets (Modello Redditi PF 2026, Fascicolo 1)**

| Rule | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026 |
| The return works in whole euro: no acconto if RN34 (or RN61 column 4) is below | EUR 52 | "è inferiore ad euro 52,00 l’acconto non è dovuto" |
| Single payment when the first instalment would not exceed | EUR 103 | "non superi euro 103,00 nel qual caso" |
| Surcharge for paying balance and first acconto by 30 July (Section 5.4) | 0.40% | "maggiorazione dello 0,40 per cento a titolo di interesse corrispettivo" |
| Interest on instalments, yearly rate (commercial method) | 4% | "interessi nella misura del 4 per cento annuo" |
| Interest added for each further monthly instalment, whatever the payment day; it builds up month by month, and Fascicolo 1 prints the running total for each instalment | 0.33% | "0,33 per cento in misura forfetaria" |
| Credit offset needing a visto di conformità, above | EUR 5,000 | "credito di importo superiore a 5.000 è necessario" |

- **Historical method formula.** acconto = RN34 (or RN61 column 4), split as in the tables. For ISA taxpayers the first instalment is half ("il cinquanta per cento per i soggetti ISA", art. 17(3) D.P.R. 435/2001).
- **Casi particolari (rigo RN61).** For the 2026 acconto, last year's tax is recomputed in listed cases (occasional boat hire, fuel stations, the new-hires deduction of D.Lgs. 216/2023 art. 4, capital gains under TUIR art. 86(4) as changed by Law 199/2025). The acconto then uses RN61 column 4.
- **First year of activity.** No tax last year means no acconto on the historical method; the first year is paid as balance the next June.

### 5.2 Forecast method (metodo previsionale): flag for reviewer

- **Forecast method formula.** A client who expects lower tax this year may base the acconti on it, with the same shares and dates. Rigo RN62 still shows the historical amounts, not the lower ones paid (Fascicolo 1).
- **Forecast method risk.** If the forecast proves too low, the acconti not paid are late payments. The penalty is "venticinque per cento" (twenty-five per cent) of each amount not paid, halved if paid within ninety days, and reduced further up to fifteen days late (D.Lgs. 471/1997 art. 13(1), Section 6.1). The statute prints these rates only in words. Always flag for commercialista.

### 5.3 Regime forfettario

- **Regime forfettario computation.** Base = last year's substitute tax, NOT IRPEF. Same minimum and dates as IRPEF, but two EQUAL instalments, and a single payment by 30 November when the total is not above the forfettario threshold in the Section 5.1 table. Codes 1790 and 1791.

### 5.4 Maggiorazione for deferral

- **Maggiorazione for deferral.** Balance and primo acconto may be paid within the 30 days after 30 June, that is by 30 July, adding the surcharge in the Section 5.1 tables first (D.P.R. 435/2001 art. 17(2)). The secondo acconto cannot be deferred this way. After the deadline, ravvedimento operoso applies (Section 6.2). Deadlines falling on a Saturday or holiday move to the next working day.

### 5.5 Rateizzazione (monthly instalments)

- The balance and the primo acconto (and the INPS contributions in Quadro RR above the minimale) may be paid in monthly instalments. The secondo acconto may not. The first instalment is due on the normal date (30 June, or 30 July with the surcharge); the later ones by the 16th of each month, except that instalments falling due from 1 to 20 August may be paid by 20 August (D.Lgs. 33/2025 art. 11). All must be finished by 16 December of the year the return is filed (D.Lgs. 33/2025 art. 10(1)). Instalments may cover only some items: for example, the primo acconto in instalments and the balance in one go. Interest (rates in the Section 5.1 tables) is paid on its own line (code 1668).

### 5.6 Cedolare secca, IRAP and INPS gestione separata

- **Cedolare secca (rigo LC2).** The whole of last year's cedolare secca, with the IRPEF minimum, threshold, shares and dates of Section 5.1; codes 1840 and 1841. Forecast method and monthly instalments of the first instalment allowed (Fascicolo 1).
- **IRAP** (partnerships, companies; individuals no longer pay it). See the table below and `it-irap`.
- **INPS gestione separata** (professionals without their own fund). Two acconti of equal amount on the IRPEF acconto dates. Total: 2026 rates on the share of 2025 professional income in the table below, within the 2026 massimale. They go in the INPS section of the F24 (causale PXX or P10). Rates are in `it-inps-contributions`. Artigiani and commercianti pay acconti on income above the minimale on the same dates: see `it-inps-contributions`.

**IRAP acconti (2026 IRAP instructions)**

| Rule | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| Acconto on the historical method, share of last year's IRAP | 100% | "nella misura pari al 100 per cento" |
| Partnerships: acconto due only if last year's IRAP is above | EUR 51.65 | "sempreché tale importo sia superiore a euro 51,65" |
| Companies and other taxpayers: acconto due only if last year's IRAP is above | EUR 20.66 | "sempreché tale importo sia superiore a euro 20,66" |
| First instalment, with the balance | 40% | "la prima, pari al 40 per cento" |
| Second instalment, by 30 November 2026 (partnerships) | 60% | "la seconda, pari al residuo 60 per cento, entro il 30 novembre 2026" |
| ISA taxpayers: two instalments of | 50% | "in due rate ciascuna nella misura del 50 per cento" |

Companies pay the balance and first IRAP acconto by the last day of the sixth month after the year end, and the second by the last day of the eleventh month (`it-irap`).

**INPS gestione separata acconti (Modello Redditi PF 2026, Fascicolo 2, Appendice)**

| Rule | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 |
| Share of 2025 professional income on which the 2026 acconti total is worked out, at 2026 rates | 80% | "sull’80% del reddito di lavoro" |

## Section 6: Penalties and interest

### 6.1 Sanzione for insufficient/omitted acconti

**Sanzione table**

| Violation | Base penalty (D.Lgs. 471/1997 art. 13(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30) |
| --- | --- |
| Omitted acconto | venticinque per cento (twenty-five per cent) of the unpaid amount |
| Insufficient acconto | The same, on the shortfall |
| Paid within ninety days | Half of that |
| Paid within fifteen days | One fifteenth of the halved penalty for each day late |

D.Lgs. 471/1997 art. 13 and D.Lgs. 472/1997 art. 13 are shown on Normattiva as in force until 31 December 2026. The testo unico delle sanzioni tributarie (D.Lgs. 173/2024) applies from 1 January 2027 (its art. 102: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=). For a late 2026 payment regularised in 2027, check which text applies.

### 6.2 Ravvedimento operoso (voluntary regularisation)

The penalty is reduced if the client pays of their own accord (D.Lgs. 472/1997 art. 13(1): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-06-30). For taxes run by the Agenzia delle Entrate, such as IRPEF, an audit already under way does not bar this; only the notification of an assessment, or of a notice of amounts due after the checks of the return, does (art. 13(1-ter)). Later stages of an audit carry other fractions (letters b-ter to b-quinquies): refer. The statute states the reductions as fractions of the minimum penalty:

**Ravvedimento operoso table**

| Timing | Reduced penalty |
| --- | --- |
| Unpaid tax or acconto paid within thirty days | One tenth of the minimum (letter a) |
| Within ninety days | One ninth (letter a-bis) |
| Within the deadline for the return of the year of the violation | One eighth (letter b) |
| After that deadline | One seventh (letter b-bis) |

- **Legal interest rate.** Legal-rate interest runs daily on the late tax. The 2026 rate was not read on an allowed page; check the ministry decree.

### 6.3 Ravvedimento formula

- **Ravvedimento formula.** amount_due = unpaid_tax + (unpaid_tax x base penalty x reduction fraction) + interest, where interest = unpaid_tax x (legal_rate / 365) x days_late. Penalty and interest go on their own F24 lines.

## Section 7: F24 payment procedure

### 7.1 Codici tributo

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

### 7.2 Filing steps

- **Filing steps.** VAT number holders pay by F24 electronically, directly (F24 online, F24 web) or through an intermediary (Fascicolo 1). Erario section: tax code, reference year (2026 for the 2026 acconti), amount; the "Rateazione" column for instalments. Keep the receipt.

### 7.3 Compensazione (offsetting)

- **Compensazione rules.** Tax credits can be offset against acconti in the F24. Credits above the amount in the Section 5.1 tables need a visto di conformità, and can be offset only from the tenth day after the return showing them is filed.

## Section 8: Edge cases

Moving into or out of the forfettario: which base applies is a judgement call. Flag for commercialista.

Two instalments apply from the Section 5.1 threshold upwards ("pari o superiore"), not only above it.

Cannot pay by 30 June: 30 July with the surcharge (Section 5.4), or monthly instalments (Section 5.5). After that: ravvedimento.

Forecast too low: the shortfall carries the Section 6.1 penalty, reducible by ravvedimento.

## Section 9: Self-checks

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

## Section 10: Test suite

### Test 1: Standard two-instalment

Input: last year's RN34 at or above the two-instalment threshold; not ISA. Expected: first share of RN34 by 30 June, the rest by 30 November; total = RN34.

### Test 2: Single instalment

Input: last year's RN34 above the minimum, below the two-instalment threshold. Expected: the whole RN34 by 30 November.

### Test 3: Below minimum

Input: last year's RN34 below the minimum. Expected: no acconti.

### Test 4: Forfettario

Input: last year's substitute tax above the forfettario single-payment threshold. Expected: half by 30 June (code 1790), half by 30 November (code 1791).

### Test 5: Deferral with maggiorazione

Input: primo acconto paid by 30 July. Expected: primo acconto increased by the Section 5.4 surcharge; secondo acconto still 30 November.

### Test 6: First year

Input: first year of activity, no prior return. Expected: no acconti under the historical method.

### Test 7: Ravvedimento (30-day late)

Input: secondo acconto paid 25 days late, before any audit. Expected: penalty = base penalty (Section 6.1, halved because within ninety days) x one tenth (Section 6.2), plus legal interest for 25 days.

## The method, step by step

1. Take last year's net tax from rigo RN34 of Modello Redditi PF, or rigo RN61 column 4 in the casi particolari, and compare it with the minimum (Fascicolo 1, rigo RN62: https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026).
2. Decide the split and dates under D.P.R. 435/2001 art. 17, as the Agenzia page states them: general shares, or equal halves for ISA taxpayers and forfettari (https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef).
3. If the client expects lower tax this year, decide with the commercialista whether to use the forecast method, weighing the late payment penalty of D.Lgs. 471/1997 art. 13 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30).
4. Add the other acconti due on the same F24: cedolare secca (rigo LC2), INPS gestione separata (Fascicolo 2, Appendice: https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026) and, for partnerships and companies, IRAP (Section 5.6).
5. Pay by F24 with the codes in Section 7.1: by 30 June (or 30 July with the surcharge, or in monthly instalments up to 16 December) and by 30 November. If a date was missed, use ravvedimento under D.Lgs. 472/1997 art. 13 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-06-30).

## Ask the client first

- What was your net tax in last year's return (rigo RN34), and did any of the RN61 special cases apply?
- Are you in the forfettario or the ordinary regime, and did that change this year?
- Is your activity subject to the ISA reliability indices?
- Do you expect this year's income or deductions to be very different from last year's?
- Do you let property under cedolare secca, and which INPS fund do you pay into?
- Were any of this year's dates already missed?

## When to refuse or refer

- Forecast method: not without a commercialista (penalty risk).
- Non-residents and cross-border income (R-IT-ET-1, R-IT-ET-2).
- A client moving into or out of the forfettario, or with a first year after a change of regime.
- Detailed addizionale regionale or comunale acconti (R-IT-ET-3).
- An audit already under way: refer.

## Prohibitions

- NEVER use the forecast method without flagging for commercialista and warning about the late payment penalty
- NEVER confuse IRPEF codes (4033 and 4034) with forfettario codes (1790 and 1791) or cedolare secca codes (1840 and 1841)
- NEVER ignore the two-instalment threshold ("pari o superiore")
- NEVER use the general shares for ISA taxpayers or forfettari: they pay equal halves
- NEVER forget the maggiorazione when deferring the primo acconto to July

## Sources

- Agenzia delle Entrate, Come si paga l'Irpef: https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef
- Modello Redditi PF 2026, Fascicolo 1 instructions: https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-13-05-2026
- Modello Redditi PF 2026, Fascicolo 2 instructions: https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026
- 2026 IRAP instructions: https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414
- D.Lgs. 471/1997 art. 13: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30
- D.Lgs. 472/1997 art. 13: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-06-30

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com.

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
