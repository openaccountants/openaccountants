---
name: it-income-tax
description: >
  Use this skill whenever asked about Italian income tax for self-employed
  individuals (lavoratori autonomi, liberi professionisti) under regime
  ordinario. Trigger on phrases like "Modello Redditi PF", "Quadro RE", "IRPEF",
  "redditi di lavoro autonomo", "imposta sul reddito Italy", "deduzioni",
  "detrazioni", "addizionale regionale", "addizionale comunale", "regime
  ordinario", "acconti IRPEF", "no tax area", "INPS Gestione Separata", "rivalsa
  INPS" or any Italian income tax question for a professional. It covers the
  2025 and 2026 periods: IRPEF bands, the art. 13 detrazione, deductions, the
  addizionali, Quadro RE, filing and penalties. The middle rate is 35% for 2025
  and 33% for 2026. Regime forfettario appears only as an entry gate and
  comparison. This Tier 2 draft supports source checking and reviewer questions;
  it does not authorise filing, payment or a tax position.
version: 2.3
jurisdiction: IT
tax_year: 2026
tax_year_notes: "Coverage starts with the 2025 period (Modello Redditi PF 2026, read at 5 November 2026) and includes the 2026 period, whose return form (Redditi PF 2027) was not available. Only the TUIR text in force to 31 December 2026 is covered; D.Lgs. 117/2026 replaces arts 1-191 for later periods and is not mapped here. The 2027 budget bill is not law."
last_updated: 2026-11-11
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# Italy income tax for self-employed professionals v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Coverage: the 2025 period (Modello Redditi PF 2026, read at 5 November 2026) and the 2026 period, whose return form (Redditi PF 2027) was not available. Only the TUIR text in force to 31 December 2026 is covered; D.Lgs. 117/2026 replaces arts 1-191 for later periods and is not mapped here. The 2027 budget bill is not law.

## Who this applies to

An individual resident in Italy who carries on an art or profession habitually, though not necessarily exclusively (TUIR art. 53(1)), is taxed on cash-basis self-employment income under the ordinary rules (regime ordinario) and files Modello Redditi PF with Quadro RE. Currency is EUR only. The period is the calendar year, as the Redditi PF instructions treat it.

The tax authority is the Agenzia delle Entrate. Primary legislation for the covered periods is DPR 917/1986 (TUIR). Payments are made by F24.

### What this file is

This file is a Tier 2 reference with review pending. It holds the rate tables, the base, the classification patterns, the deadlines and reviewer questions. Treat every computed figure as an estimate for review by a Commercialista or equivalent licensed practitioner in Italy.

**Operational hold.** This file does not fill the complete country companion contract in `income-tax-workflow-base`, so it does not support unattended preparation:

- `it-regime-forfettario` does not exist in this repository, although the prior version of this file pointed to it as a separate skill. No forfettario return can be prepared from this file. R-IT-6 stops that request.
- The base asks for 3 fixtures: one employee, one self-employed and one mixed. Only self-employed fixtures appear here. Employment income is out of scope and mixed income is refused under R-IT-7, so those 2 fixtures do not exist.
- The transaction pattern library and bank formats below are carried from the prior version. Their narrations and file layouts were not tested against bank files.

The position fixtures below number 5, and all 5 are self-employed. They do not close the employee and mixed gaps.

**Reviewer warning.** Any working paper produced under this file is a working paper only. It must show which inputs were confirmed and which are Needs Input, and it must carry the label 'estimated, not reviewed'.

### Question threshold

Tier 2 question threshold: EUR 0. No row is filtered on amount: a material question goes to the client or the reviewer whatever its size, because no text read sets a floor.

### Refusals

A refusal is a full stop. When a trigger applies, output the message verbatim and end. Do not classify part of the file first. Where a trigger is only suspected, ask the client the question that resolves it.

- **R-IT-1, no itemised expenses.** Trigger: the client wants a Quadro RE figure but gives only bank totals. Message: 'Bank totals alone cannot support a Quadro RE figure. Send an itemised expense list with F24 receipts and invoices. This workflow cannot continue until then.'
- **R-IT-2, regime for the year unclear.** Trigger: the records show income treated under both regime ordinario and regime forfettario in one period, or the regime of the period is unknown. Message: 'The regime for this period is not established. L. 190/2014 art. 1(71) ends forfettario from the following year, or in the same year once compensi exceed EUR 100,000. Confirm which regime applied and from when. This workflow cannot continue until then.'
- **R-IT-3, forfettario entry in doubt.** Trigger: the client claims forfettario and compensi exceed EUR 85,000 in the period or the prior year. Apply the matching message.
  - Prior-year compensi, annualised, above EUR 85,000: 'Forfettario is not available this year under L. 190/2014 art. 1(54)(a). Regime ordinario applies if no other regime does. Confirm this before this workflow continues.'
  - Prior-year compensi within the limit, this year above EUR 85,000 and at most EUR 100,000: 'Forfettario continues for this year and ends from next year under L. 190/2014 art. 1(71). This workflow cannot prepare the year. Refer it to a Commercialista.'
  - Prior-year compensi within the limit, this year above EUR 100,000: 'Forfettario ends in this year, with IVA due from the operation that crosses EUR 100,000, under L. 190/2014 art. 1(71). Refer the changeover to a Commercialista before this workflow continues.'
- **R-IT-4, non-resident.** Trigger: the person is, or may be, non-resident under TUIR art. 2. Message: 'Non-residents are taxed only on Italian-source income. TUIR art. 24 limits their deductions and detrazioni and allows no family detrazioni, unless art. 24(3-bis) applies the rules in arts 1 to 23. This workflow covers residents only. Refer it to a Commercialista.'
- **R-IT-5, vehicle facts missing.** Trigger: the client wants a vehicle deduction above the 20% limb without facts for another limb of art. 164. Message: 'A deduction above 20% needs a use that fits another limb of TUIR art. 164. Send the facts and documents for that use. This workflow cannot apply a higher percentage until then.'
- **R-IT-6, forfettario year.** Trigger: forfettario applies to the period. Message: 'This period falls under regime forfettario. This file covers regime ordinario only and the companion `it-regime-forfettario` does not exist in this repository. This workflow cannot prepare the period. Refer it to a Commercialista.'
- **R-IT-7, other income or other form.** Trigger: the person also has employment, rental, partnership, capital or foreign income in the period, or is a company, an association of professionals, or an impresa with Quadro RF or RG income. Message: 'This period includes income this file does not cover, and the reddito complessivo cannot be stated without it. Refer it to a Commercialista.'
- **R-IT-8, special regimes.** Trigger: the person adhered to the concordato preventivo biennale, is an impatriato, or receives copyright income, sports income or volunteer and cooperant compensi that need separate RE rows. Message: 'This period needs a special computation in Quadro RE or Quadro CP that this file does not contain. Check `it-impatriati` where that regime applies, and refer the rest to a Commercialista.'
- **R-IT-9, foreign client tax.** Trigger: foreign tax was withheld or a foreign client is involved in a claimed credit. Message: 'Foreign tax credit under TUIR art. 165 and any treaty need a separate analysis that this file does not contain. Refer it to a Commercialista.'
- **R-IT-10, return not available.** Trigger: a final computation is asked for a period after 2026, or a Redditi PF 2027 row or date is requested. Message: 'This file does not cover that period or form. Read the text in force for the period and the form when published. This workflow cannot continue for that period.'

### Required inputs

- **Minimum viable.** Bank statement for the full calendar year in CSV, PDF or pasted text, confirmation of the regime, the region and comune of fiscal domicile at 1 January of the year, and each confirmed addizionale rate.
- **Recommended.** All client invoices (fatture), F24 receipts for acconti and INPS, the Gestione Separata or cassa contribution statement, Certificazione Unica for withholding and the prior Modello Redditi.
- **Ideal.** Complete books, an asset register with ammortamento schedules, all fatture emesse and ricevute, and family details for art. 12 detrazioni.

### Prohibitions

- Never apply regime forfettario rules to a period here. The only use is the entry gate and the side-by-side comparison in Example 2.
- Never deduct more than 80% of the terminal equipment and service costs within art. 54-quinquies(4).
- Never deduct more for a vehicle than the limb of art. 164 that the facts support; the mixed-use limb is 20%.
- Never deduct more than 75% of hotel and food and drink costs, and never more than 2% of compensi in total under art. 54-septies(1).
- Never fully expense a movable asset with a unit cost above EUR 516.46, and hold a unit cost above EUR 516.40 up to EUR 516.46: see Source conflicts.
- Never treat IRPEF, addizionali or IVA paid by F24 as an expense, and never treat compulsory contributions as a Quadro RE expense.
- Never include IVA in income or expense figures.
- Never use competenza for a professional under art. 54(1), apart from the withholding-agent rule stated in The base.
- Never assume Gestione Separata for a professional enrolled in a cassa previdenziale, and never assume a rate where the status or the rate is unknown.
- Never present a calculation as definitive: label it estimated and direct the client to their Commercialista.

## Rates, bands and thresholds

All amounts are in euro.

### IRPEF bands

Bands apply to the reddito imponibile, that is reddito complessivo net of the art. 10 deductible charges (rigo RN4).

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| First band, to EUR 28,000 | 23%; tax on full band EUR 6,440 | 2025 | [TUIR art. 11(1), text at 31 December 2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2025-12-31) |
| Second band, above EUR 28,000 to EUR 50,000 | 35%; cumulative EUR 14,140 at EUR 50,000 | 2025 | [TUIR art. 11(1), text at 31 December 2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2025-12-31) |
| Third band, above EUR 50,000 | 43% on the excess | 2025 | [TUIR art. 11(1), text at 31 December 2025](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2025-12-31) |
| First band, to EUR 28,000 | 23%; tax on full band EUR 6,440 | 2026 | [TUIR art. 11(1), current text](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=) |
| Second band, above EUR 28,000 to EUR 50,000 | 33%; cumulative EUR 13,700 at EUR 50,000 | 2026 | [TUIR art. 11(1), current text, as amended by L. 199/2025 art. 1(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=) |
| Third band, above EUR 50,000 | 43% on the excess | 2026 | [TUIR art. 11(1), current text](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=) |

```text
gross_tax = 0.23 * min(taxable, 28000)
          + middle_rate * max(min(taxable, 50000) - 28000, 0)
          + 0.43 * max(taxable - 50000, 0)
net_tax   = max(gross_tax - detrazioni, 0)
```

`middle_rate` is 0.35 for 2025 and 0.33 for 2026. Net tax is gross tax less the arts 12, 13, 15, 16 and 16-bis detrazioni, up to the amount of gross tax (TUIR art. 11(3)). An excess detrazione is not refunded under that text.

### Self-employment detrazione, TUIR art. 13(5)

Unchanged between the 2025 and 2026 texts read. RC here is reddito complessivo net of the main home and its appurtenances (art. 13(6-bis)). The form calls it 'Reddito per detrazioni': RN1 col. 1 less RN2 plus RS37 col. 14, taken as zero if negative. It is measured before art. 10 charges, so it is not the taxable income used for the bands.

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| RC up to EUR 5,500 | EUR 1,265 | 2025 and 2026 | [TUIR art. 13(5)(a)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=) |
| RC above EUR 5,500, up to EUR 28,000 | EUR 500 + EUR 765 x (28,000 - RC) / 22,500 | 2025 and 2026 | [TUIR art. 13(5)(b)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=) |
| RC above EUR 28,000, up to EUR 50,000 | EUR 500 x (50,000 - RC) / 22,000 | 2025 and 2026 | [TUIR art. 13(5)(b-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=) |
| RC above EUR 50,000 | 0: no limb applies | 2025 and 2026 | [TUIR art. 13(5)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=) |
| Increase where RC is above EUR 11,000, up to EUR 17,000 | Statute: EUR 50 on the art. 13(5) detrazione. Form: EUR 50 for art. 50(1)(e) to (i) income only. Held: see Source conflicts | 2025 and 2026 | [TUIR art. 13(5-ter)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=); [Fascicolo 1, rigo RN7](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| Ratio in the 2 formulas, if above zero | First 4 decimals, by art. 13(6) | 2025 and 2026 | [TUIR art. 13(6)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=) |

The no-tax area is a computed result, not a band: EUR 1,265 / 23% = EUR 5,500 of taxable income. That figure alone does not establish nil IRPEF: compare gross tax with the detrazione, which runs on RC, not on taxable income. RC EUR 6,000 with contributions of EUR 500 gives taxable income EUR 5,500 and gross tax EUR 1,265, but art. 13(5)(b) gives EUR 1,247.94 on this file's truncation, so net tax is EUR 17.06. RC EUR 6,000 with contributions of EUR 1,000 gives taxable income EUR 5,000 and gross tax EUR 1,150, below that detrazione, so net tax is nil. The detrazione does not combine with art. 13(1) to (4). This file truncates the ratio to 4 decimals because the text says 'the first 4 decimals'; it reads no rounding rule.

### High-income limits on detrazioni

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Limit on detraction charges, RC above EUR 75,000, up to EUR 100,000 | Base EUR 14,000 x family coefficient | 2025 and 2026 | [TUIR art. 16-ter](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=) |
| Limit on detraction charges, RC above EUR 100,000 | Base EUR 8,000 x family coefficient | 2025 and 2026 | [TUIR art. 16-ter](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=) |
| Family coefficient | 0.50 no child; 0.70 one; 0.85 two; 1 more than two or a disabled child, counting only children in the household who meet art. 12(2) | 2025 and 2026 | [TUIR art. 16-ter](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=) |
| Art. 15 detrazioni, RC above EUR 120,000 | Share of the detrazione: (240,000 - RC) / 120,000, so nil from EUR 240,000 | 2025 and 2026 | [TUIR art. 15(3-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art15!vig=) |
| Art. 15 detrazioni kept whole at any RC | Art. 15(1)(a) and (b), art. 15(1-ter) and medical costs in art. 15(1)(c) | 2025 and 2026 | [TUIR art. 15(3-quater)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art15!vig=) |
| Reduction where RC exceeds EUR 200,000 | EUR 440 off the detrazione for the 3 listed charges | 2026, by L. 199/2025 art. 1(4) | [TUIR art. 16-ter(5-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=) |

The 3 charges in art. 16-ter(5-bis) are: (a) charges detractible at 19%, except medical costs under art. 15(1)(c); (b) donations to political parties; and (c) catastrophe insurance premiums. RC in art. 15(3-bis) is net of the main home (art. 15(3-ter)). The reduction applies after arts 16-ter(1) to (5) and 15(3-bis), so a charge that art. 15(3-bis) has reduced to nil leaves nothing to reduce. It offsets the 2-point rate cut at the top: EUR 22,000 x 2% = EUR 440. Art. 16-ter(4) and (5) exclude further items from the limit; read them before applying it. Limited to the detrazione the client has for those charges; Example 5 tests that floor.

### Addizionali

Addizionali use the same base, rigo RV1 (RN1 col. 5 less RN2 less RN3), and are due only if IRPEF net of detrazioni and credits is due. The addizionale regionale is not deductible for any tax.

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Addizionale regionale, base rate | 1.23% | 2025 and 2026 | [D.Lgs. 446/1997 art. 50(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art50!vig=) |
| Region's power to change the rate, ordinary-statute regions | Up to 2.1 points above the base from 2015, on the text read, or down as far as nil. An increase above 0.5 points does not apply to first-band income. The year of first use of the D.Lgs. 147/2026 changes is held | 2025 and 2026 | [D.Lgs. 68/2011 art. 6](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=) |
| Rates each region set | Printed bands run from 0.70% at Friuli Venezia Giulia's first band to 3.63% at Molise's top band. Use the client's own row | 2025 | [Agenzia delle Entrate, Redditi PF 2026, Fascicolo 1, table at end](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| Addizionale comunale, cap on the variation | 0.8 points | 2025 and 2026 | [D.Lgs. 360/1998 art. 1(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=) |
| Rates each comune set | Rates and exemption thresholds by comune. 12 of the 7,896 rows parsed print a rate above 0.8: see Source conflicts. Use the client's own row | 2025 saldo and 2026 acconto | [Agenzia delle Entrate, elenco addizionale comunale 2026](https://www.agenziaentrate.gov.it/portale/documents/d/guest/elenco-annuale-addizionale-comunale-modulistica-2026_def) |
| Acconto comunale | 30% of the addizionale on the prior-year income, at the prior-year rate | 2026 acconto | [D.Lgs. 360/1998 art. 1(4); Fascicolo 1, rigo RV17](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |

The legal basis for the printed rates above 3.33% and above 0.8 points was not read and stays held. The table's casi particolari text changes some rows, such as Veneto's 0.9% reduced rate. Umbria's maggiorazioni of 0.50% and 1.79% are printed there and are not band rates. Above an exemption threshold, the rate applies to the whole of RV1 (Fascicolo 1, rigo RV10). The regional rate follows fiscal domicile at 1 January of the year (D.Lgs. 446/1997 art. 50(5)). The comune rule uses the same date, and rigo RV17 uses 1 January 2026 for the 2026 acconto. Rates for the 2026 saldo were not read.

### Regime forfettario, entry gate only

Read in the current text of L. 190/2014 art. 1 and in Fascicolo 3. It sets when this file must stop. It is not a preparation rule.

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Entry limit, prior-year compensi annualised | EUR 85,000 | 2025 and 2026 | [L. 190/2014 art. 1(54)(a)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=) |
| Prior-year staff and collaborator cost limit | EUR 20,000 gross | 2025 and 2026 | [L. 190/2014 art. 1(54)(b)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=) |
| Prior-year employment and similar income limit, unless the employment has ended | EUR 35,000 for 2025 and 2026; EUR 30,000 in the base text | 2025 and 2026 | [L. 207/2024 art. 1(12), as amended by L. 199/2025 art. 1(27)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=) |
| Exit in the same year | Compensi above EUR 100,000 | 2025 and 2026 | [L. 190/2014 art. 1(71)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=) |
| Substitute tax | 15% | 2025 and 2026 | [L. 190/2014 art. 1(64)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=) |
| New-activity rate, year of start and next 4 | 5%, on the 3 conditions in art. 1(65) | 2025 and 2026 | [L. 190/2014 art. 1(65)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=) |
| Coefficient: professional, scientific, technical, health, education, financial and insurance (ATECO 2007: 64-66, 69-75, 85, 86-88) | 78% | 2025 | [Agenzia delle Entrate, Fascicolo 3, rigo LM21 table](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Coefficient: construction and real estate (41-43, 68) | 86% | 2025 | [Fascicolo 3, rigo LM21 table](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Coefficient: trade intermediaries (46.1) | 62% | 2025 | [Fascicolo 3, rigo LM21 table](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Coefficient: street trade in other goods (47.82-47.89) | 54% | 2025 | [Fascicolo 3, rigo LM21 table](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Coefficient: food and drink industries (10-11); wholesale and retail (45, 46.2-46.9, 47.1-47.7, 47.9); street trade in food and drink (47.81); lodging and catering (55-56) | 40% | 2025 | [Fascicolo 3, rigo LM21 table](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Coefficient: other economic activities (all remaining ATECO divisions listed in the table) | 67% | 2025 | [Fascicolo 3, rigo LM21 table](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |

Coefficients still follow ATECO 2007 until new ones are approved for ATECO 2025 (Fascicolo 3, citing D.Lgs. 81/2025 art. 1). The annex itself was not read. Text extraction scrambled the table, so it was read from PDF page 44 rendered as an image with PyMuPDF. Its 2026 use was not separately confirmed.

The exclusions in art. 1(57) are each a stop, and all these limbs were read:

- (a) a special IVA regime or a forfait regime for income;
- (b) non-residents, except EU or EEA residents with adequate information exchange who produce at least 75% of their total income in Italy;
- (c) those who exclusively or mainly sell buildings, building land or new means of transport;
- (d) those who at the same time hold an interest in a partnership, association or family business, or who control an SRL or association in participation carrying on activities directly or indirectly linked to theirs;
- (d-bis) those whose activity is mainly for current employers, for employers of the prior 2 periods, or for persons linked to them, except a new activity after compulsory practice;
- (d-ter) the employment and similar income limit in the table.

### Withholding, deductions and other limits

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Withholding by art. 23 agents on self-employment compensation to residents | 20%, as an advance. The printed sentence still reads 15%; notes 21a, 30 and 54 to the text carry the changes to 20% | 2025 and 2026 | [DPR 600/1973 art. 25](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art25!vig=) |
| Movable assets, full deduction | Statute: unit cost up to EUR 516.40. Form row: EUR 516.46. A cost between the 2 is held: see Source conflicts | 2025 and 2026 | [TUIR art. 54-quinquies(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=); [Fascicolo 3, rigo RE7](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Mixed-use movables, premises and services | 50% | 2025 and 2026 | [TUIR art. 54-quinquies(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=) |
| Terminal equipment for public electronic communications services | 80% of depreciation, rent, use and maintenance | 2025 and 2026 | [TUIR art. 54-quinquies(4)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=) |
| Hotel and food and drink | 75%, and in total no more than 2% of compensi in the period | 2025 and 2026 | [TUIR art. 54-septies(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=) |
| Representation | Up to 1% of compensi in the period, with traceable payment for costs from 18 June 2025 | 2025 and 2026 | [TUIR art. 54-septies(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=); [D.L. 84/2025 art. 1(5)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2025-06-17;84~art1!vig=) |
| Training, including travel and stay | Up to EUR 10,000 a year. Statute: full deduction. Form: hotel and food at 75% within that limit. That element is held: see Source conflicts | 2025 and 2026 | [TUIR art. 54-septies(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=); [Fascicolo 3, rigo RE17](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Certification and orientation services | Full deduction up to EUR 5,000 a year | 2025 and 2026 | [TUIR art. 54-septies(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=) |
| Cars, caravans, mopeds and motorcycles, mixed use | 20%, one vehicle only for a professional, within cost limits. The full-amount limbs of art. 164(1)(a), for exclusive instrumental use and for vehicles in public use, are held: see Expenses | 2025 and 2026 | [TUIR art. 164(1)(b)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=) |
| Vehicle cost limit, purchase | EUR 18,075.99 car; EUR 4,131.66 motorcycle; EUR 2,065.83 moped | 2025 | [Fascicolo 3, rigo RE7](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Vehicle hire limit, annual charge | EUR 3,615.20 car; EUR 774.69 motorcycle; EUR 413.17 moped | 2025 | [Fascicolo 3, rigo RE9](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Vehicle given to an employee in mixed use for most of the period | 70% | 2025 and 2026 | [TUIR art. 164(1)(b-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=) |
| Cash limit | Transfers of EUR 5,000 or more barred, from 1 January 2023 | 2025 and 2026 | [D.Lgs. 231/2007 art. 49(1) and (3-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art49!vig=) |
| Occasional self-employment, Gestione Separata enrolment | Only if annual income from those activities exceeds EUR 5,000 | 2025 and 2026 | [D.L. 269/2003 art. 44(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=) |
| Rivalsa on Gestione Separata compensi | 4%, charged to clients as a right, not a duty | 2025 and 2026 | [L. 662/1996 art. 1(212)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1996-12-23;662~art1!vig=) |

### Acconti

Full acconti rules, examples and codes belong to `it-estimated-tax`. This table gives the 2026 acconto figures in the form read.

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| No acconto | Rigo RN34 Differenza, or RN61 col. 4 for particular cases, below EUR 52 | 2026 acconto | [Fascicolo 1, rigo RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| Acconto amount | 100% of that Differenza, EUR 52 or more. A lower estimate may be used at the taxpayer's choice | 2026 acconto | [Fascicolo 1, rigo RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| One payment by 30 November | First instalment would not exceed EUR 103: below EUR 257.52 in general, up to EUR 206 for an ISA taxpayer | 2026 acconto | [DPR 435/2001 art. 17(3); Fascicolo 1, rigo RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| 2 instalments, general | 40% then 60% | 2026 acconto | [Fascicolo 1, rigo RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| 2 instalments, ISA taxpayer | 50% then 50% | 2026 acconto | [D.L. 124/2019 art. 58; Fascicolo 1, rigo RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |

An ISA taxpayer here is a person carrying on an activity with an approved ISA, whether or not the ISA is applied, who declares compensi within that ISA's limit. Confirm this for each client. Forfettario taxpayers are excluded from ISA (Fascicolo 3), and R-IT-6 applies to them. See `it-estimated-tax` for the single-instalment boundary.

### Contributions

Rates, parameters and status tests belong to `it-inps-contributions` and are not restated here. Use the rate that guide reaches, or the cassa statement. Inarcassa and other cassa rates are held: collect the annual statement and do not estimate.

### Enactment position

- **2025 period.** Enacted. TUIR art. 11 in the text at 31 December 2025, as set by L. 207/2024 art. 1(2).
- **2026 period.** Enacted. L. 199/2025 art. 1(3) replaced 35 with 33 in art. 11(1)(b); art. 1(4) inserted art. 16-ter(5-bis).
- **Later periods.** D.Lgs. 19 June 2026 n. 117 (the Testo unico) applies from 1 January 2027 by its art. 377 and art. 376(1)(e) repeals TUIR arts 1 to 191 from that date. Normattiva shows the articles as repealed at that date. This file does not map the new numbering.
- **2027 budget.** Announcement only. The Council of Ministers communique of 28 October 2026 says the bill extends the 33% rate to income up to EUR 55,000. It is a bill: no bill text was read and no figure in this file relies on it.

## The base

### Income

Self-employment income is the difference between all sums and values received in the period in relation to the activity and the expenses incurred in the period (TUIR art. 54(1)). Invoice date does not decide timing.

**Timing carve-out.** Sums received in a period later than the one in which the withholding agent paid them are attributed to the period in which the agent must withhold (art. 54(1), second sentence, applying to income from the 2024 period under D.Lgs. 192/2024 art. 6).

Excluded from income under art. 54(2):

- (a) legal social contributions charged to the payer, such as a cassa integrative contribution;
- (b) expense reimbursements analytically re-charged to the client;
- (c) re-charges for shared premises.

Gestione Separata rivalsa does not fall within (a) on the form read: rigo RE2 treats the 4% increase as an integral part of compensi, so it is taxable. Also in Italy, reimbursements for food, lodging, travel, taxi or NCC are taxable if the payment was not traceable (art. 54(2-bis), for costs from 1 January 2025). Where the client pays such costs directly, art. 54(3) applies. Interest and other financial income received in the profession are capital income (art. 54(3-bis)), and gains on professional partnership shares are redditi diversi (art. 54(3-ter)).

### Expenses

All amounts are ex-IVA unless IVA is a real cost, which was not read and needs a reviewer. Expenses must relate to the activity (art. 54(1)).

- **Reimbursable expenses.** Expenses within art. 54(2)(b) and (c) are not deductible (art. 54-ter(1)). Art. 54(2)(b) expenses that go unreimbursed become deductible from an insolvency event, failed enforcement or prescription (art. 54-ter(2) and (3), with foreign equivalents in (4)), or if up to EUR 2,500 including the related fee and unreimbursed after one year from the invoice (art. 54-ter(5)). Traceability applies from 1 January 2025 (art. 54-ter(5-bis)).
- **Assets.** A unit cost is fully deductible up to EUR 516.40 on the statute, or EUR 516.46 on the form: hold a cost between the 2 (see Source conflicts). Above EUR 516.46, annual depreciation applies, up to the ministerial coefficients and halved in the first period (art. 54-quinquies(1)). Extraordinary works spread over 6 periods (art. 54-quinquies(2)). Gains and losses follow arts 54-bis and 54-quater, and intangibles art. 54-sexies. DM 31 December 1988 could not be read: Normattiva returned an error page, so collect the coefficient from a qualified source and treat it as Needs Input.
- **Mixed-use premises.** 50% of the rendita, or of the rent, provided the person has no other property in the same comune used exclusively for the profession. Services and ordinary maintenance for such premises are 50% too (art. 54-quinquies(3)). The prior version's dedicated floor-area test is not in the text read. Use the 50% rule for mixed-use premises and take a dedicated or separate space to the reviewer.
- **Hotels, food and drink.** 75%, and in total no more than 2% of compensi (art. 54-septies(1)). Rigo RE15 measures the 2% on RE6 less RE4. Representation is rigo RE16: up to 1% of compensi, with a 75% limit on hotel and food elements. Strictly social meals have no link to the activity.
- **Traceability.** Food, lodging, travel, taxi and NCC costs incurred in Italy are deductible only if paid by bank or postal payment or a system under D.Lgs. 241/1997 art. 23 (art. 54-septies(6-bis)). [D.L. 84/2025 art. 1(5)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2025-06-17;84~art1!vig=) sets the start by category. From 1 January 2025: such costs reimbursed analytically to employees or other self-employed workers, and arts 54(2-bis) and 54-ter(5-bis). From 18 June 2025: other such costs, including those borne directly, and representation (art. 54-septies(2)). Hold a 2025 cost whose date or category is unclear, including one invoiced before and paid on or after 18 June 2025. Hold an untraceable re-charged cost dated before 18 June 2025: art. 54(6-ter), repealed by D.L. 84/2025 art. 1(2), also covered such costs, and conversion dropped that repeal from art. 1(5), so its date is unclear.
- **Training.** Rigo RE17, up to EUR 10,000 a year. Art. 54-septies(3) deducts these costs in full, including travel and stay. Rigo RE17 col. 1 enters hotel and food for courses and conferences at 75%. Hold a hotel or food element: see Source conflicts. Certification and orientation services: up to EUR 5,000 (art. 54-septies(3); rigo RE17 col. 3).
- **Non-payment insurance and staff.** Art. 54-septies(4) and (5).
- **Family pay.** No deduction for compensation to a spouse, minor children and others listed in art. 54-septies(6).
- **Vehicles.** Art. 164(1) applies a 20% limb for mixed use, for one vehicle only per professional, on depreciation, hire, fuel and other costs, with cost limits. The 70% limb applies only to a vehicle given to an employee in mixed use for most of the period (art. 164(1)(b-bis)). Art. 164(1)(a) gives the full amount for (1) vehicles used exclusively as instrumental assets in the activity of the impresa and (2) vehicles in public use. Whether either limb reaches a professional is held. The prior version's 100% case for vehicles exclusively given to employees and its exclusively-professional exception are not supported for a professional on the text read: R-IT-5 applies. Art. 164(1) does not require a usage log on the text read. Fuel is deductible only if paid by credit, debit or prepaid card (art. 164(1-bis)).
- **Taxes.** Rigo RE19 lists IRAP at 10% and IMU. No form row read gives a deduction for IRPEF, addizionali or IVA: see Prohibitions.

### From Quadro RE to tax

```text
RE21 col. 5   = RE6 - RE20
RE23          = income or loss
RE25          = RE23 - RE24
RC            = max(RE25 + other heads - abitazione principale, 0)
taxable       = max(RE25 + other heads - abitazione principale - art. 10 charges, 0)
gross_tax     = bands applied to taxable
net_tax       = max(gross_tax - art. 13 detrazione - other detrazioni, 0)
RN34          = net_tax - credits - ritenute (RN33)
balance_due   = RN34 - acconti paid (RN38) - any prior credit
addizionali   = row's rate or bands applied to RV1, if IRPEF is due
```

Other heads are outside this file under R-IT-7, so a filing client must have none. In this file, RE23 is before Gestione Separata contributions. Compulsory contributions, whether Gestione Separata or cassa, are oneri deducibili under TUIR art. 10(1)(e), entered in rigo RP21 and deducted from reddito complessivo in rigo RN3 unless already deductible in computing a head of income. The form reads them as not a Quadro RE expense. Contributions are cash paid in the year. Non-residents lose this deduction under art. 24(2).

**Losses.** Self-employment losses reduce reddito complessivo for the same period (TUIR art. 8(1); Fascicolo 3, rigo RE25). Rigo RE24 names only losses formed in 2006 and 2007, carried forward without time limit. No carry-forward rule for later losses was read; hold that point.

**Family detrazioni.** Art. 12 changed for 2025 (Fascicolo 1 records no deduction for children aged 30 or over unless disabled). Family facts are Needs Input and no family figure is computed here.

**Foreign currency.** Convert at the exchange rate on the day received or incurred, or the nearest prior day; otherwise at the month's rate (TUIR art. 9(2)).

**Rounding.** Return amounts round to whole euro, up from 50 cents (Fascicolo 1). Examples show cents before that rounding.

### Withholding

Art. 23 agents withhold on compensation paid to a resident professional. Ritenute go in rigo RE26 and reach rigo RN33. Collect the Certificazione Unica. L. 199/2025 art. 1(112) to (115) adds a separate withholding on business payments, from 2028, at 0.5% or 1%, which does not change the rate above for professionals. Forfettario compensi carry no withholding (L. 190/2014 art. 1(67)).

### Defaults

A default stands only where the law read fixes the result of the missing fact. Everything else is Needs Input.

| Situation | Treatment | Basis |
| --- | --- | --- |
| Regional rate or domicile unknown | Needs Input. The rate differs by region and income band, so no default | D.Lgs. 446/1997 art. 50 |
| Comunale rate, domicile or exemption unknown | Needs Input | D.Lgs. 360/1998 art. 1 |
| Cassa or Gestione Separata status unknown | Needs Input, as in `it-inps-contributions` | That guide |
| Rivalsa on invoices unclear | Needs Input: do not assume 4% was added. If shown on the invoice, it is income | L. 662/1996 art. 1(212); rigo RE2 |
| Deductibility disputed | Needs Input. Leave the item in a suspense line, out of any figure shown as final | Art. 54(1) |
| Receipt of unclear nature | Needs Input. If received in relation to the activity it is income. Leave it in the suspense line | Art. 54(1) |
| Invoice date and payment date differ | Default stands: cash date, subject to the withholding-agent rule | Art. 54(1) |
| Reimbursement documented as analytically re-charged | Default stands: excluded, subject to the art. 54(2-bis) traceability rule | Art. 54(2)(b) |
| Reimbursement not documented | Needs Input, in the suspense line | Art. 54(2)(b) |
| Telecom, hotel, food and vehicle share | Default stands only for the statutory percentage on a documented, confirmed cost | Arts 54-quinquies, 54-septies and 164 |

### Reviewer attention thresholds

Each row is a flag, not a rule of law, unless a source is shown.

| Flag | Threshold | Action |
| --- | --- | --- |
| Compensi above EUR 85,000 | Period or prior year | Confirm the regime; R-IT-2 or R-IT-3 |
| Contributions below 20% of income | Prior-version ratio, no source read | Soft check only: contributions are cash paid, so a low ratio can be correct. Reconcile with `it-inps-contributions` |
| No acconto recorded | Prior-year RN34 was EUR 52 or more | Check whether acconti were due |
| Cash transfer | EUR 5,000 or more | Flag under D.Lgs. 231/2007 art. 49 |
| Undocumented expense | Any amount; the prior version's EUR 5,000 line has no source | Needs Input: no deduction in a final figure until documented |
| Single-client income | Most of the year | Check the prior employer limb in art. 1(57)(d-bis) if forfettario is claimed, and the IVA status |
| EUR 50 increase | RC above EUR 11,000, up to EUR 17,000 | Show both art. 13(5-ter) results and hold: see Source conflicts |
| Asset in the gap | Unit cost above EUR 516.40, up to EUR 516.46 | Hold: see Source conflicts |
| Hotel or food in training costs | Any amount | Hold: see Source conflicts |

### Classifying a bank line

Use this as a pre-classifier. If no pattern fits, apply the rules above. Each row assumes the amount is confirmed as professional, ex-IVA and within the period.

**Credits**

| Pattern | Tax line | Treatment | Notes |
| --- | --- | --- | --- |
| BONIFICO DA [client name] | RE2 compensi | Income | Standard SEPA credit from client |
| VB DA [client name] / VB ENTRATA | RE2 compensi | Income | UniCredit and BancoBPM credit notation |
| ACCREDITO DA [client] | RE2 compensi | Income | Generic bank credit from client |
| STRIPE PAYMENTS EUROPE / STRIPE PAYOUT | RE2 compensi | Income, gross of fee | Match the processor report; the fee is an expense |
| PAYPAL TRANSFER / PAYPAL ACCREDITO | RE2 compensi | Income, gross of fee | The fee is an expense |
| SATISPAY BUSINESS PAYOUT | RE2 compensi | Income, gross of fee | The fee is an expense |
| NEXI PAGAMENTI / NEXI POS VERSAMENTO | RE2 compensi | Income, gross of fee | Nexi merchant settlement |
| SUMUP PAYOUT / ZETTLE PAYOUT | RE2 compensi | Income, gross of fee | Card terminal payout |
| REVERSALE [client] / RIMESSA CLIENTI | RE2 compensi | Income | Public administration or factoring payment |
| RIVALSA INPS (portion of invoice) | RE2 compensi | Income | 4% is part of compensi |
| INTERESSI ATTIVI / INTERESSI MATURATI | Not Quadro RE | Capital income, art. 54(3-bis) | Treatment and form row held; the prior Quadro RW/RL pointer was not confirmed |
| RIMBORSO SPESE [client] | Excluded if art. 54(2)(b) is met | Flag | Needs the client's re-charge note and art. 54(2-bis) check |
| STIPENDIO / SALARIO [employer] | Employment income | Not Quadro RE | R-IT-7 |

**Debits**

| Pattern | Treatment | Rule | Notes |
| --- | --- | --- | --- |
| AFFITTO UFFICIO / CANONE LOCAZIONE / PIGIONE | 100% if used only for the profession; 50% if mixed | Art. 54-quinquies(3) | Mixed needs no other exclusive property in the comune. RE10 |
| ENEL / ENI PLENITUDE / A2A ENERGIA | 100% if only professional premises; 50% if mixed | Art. 54-quinquies(3) | RE14 |
| TELECOM ITALIA / TIM FIBRA / FASTWEB / WIND3 | 80% | Art. 54-quinquies(4) | Reviewer checks that the cost falls within the text. RE14 |
| VODAFONE MOBILE / TIM MOBILE / ILIAD | 80% | Art. 54-quinquies(4) | RE14 |
| ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE | 100% if used in the activity | Art. 54(1) | RE19 |
| COMMERCIALISTA / CONSULENTE FISCALE / STUDIO [name] | 100% if for the activity | Art. 54(1) | RE12 or RE19 |
| AVVOCATO / NOTAIO | 100% if for the activity | Art. 54(1) | Personal matter: not deductible |
| TRENITALIA / ITALO / FRECCIAROSSA | 100% if for the activity; traceably paid in Italy from 18 June 2025 | Art. 54-septies(6-bis) | Needs destination and purpose |
| RYANAIR / EASYJET / ITA AIRWAYS / ALITALIA | 100% if for the activity; traceable when incurred in Italy from 18 June 2025 | Art. 54-septies(6-bis) | Needs itinerary and purpose |
| HOTEL / AGODA / BOOKING.COM | 75%, 2% limit | Art. 54-septies(1) and (6-bis) | RE15. Traceable in Italy from 18 June 2025 |
| RISTORANTE / PIZZERIA / CAFFE | 75%, 2% limit | Art. 54-septies(1) and (6-bis) | Needs a professional purpose. RE15. Traceable in Italy from 18 June 2025 |
| INPS F24 / CONTRIBUTI GESTIONE SEPARATA | Not Quadro RE; art. 10(1)(e) charge | Rigo RP21 | Deducted from reddito complessivo |
| F24 ACCONTO IRPEF / F24 SALDO IRPEF | Not deductible | Rigo RE19 lists no such item | Credit acconti in RN38 |
| ASSICURAZIONE PROFESSIONALE / RC PROFESSIONALE | 100% if for professional risks | Rigo RE19 | |
| ADDIZIONALE REGIONALE / ADDIZIONALE COMUNALE | Not deductible | D.Lgs. 446/1997 art. 50(1) for the regional one; the comunale has no deduction row | Exclude |
| SPESE BANCARIE / COMMISSIONI BANCARIE / CANONE CONTO | 100% if the account is for the profession | Art. 54(1) | A mixed account needs a reviewer |
| AMORTAMENTO / BENE STRUMENTALE | Depreciate above EUR 516.46; hold above EUR 516.40 up to EUR 516.46 | Art. 54-quinquies(1) | RE7 |
| AUTONOLEGGIO / NOLEGGIO AUTO | 20%, charge limit EUR 3,615.20 for a car | Art. 164(1)(b); rigo RE9 | One vehicle |
| CARBURANTE / ENI / Q8 / SHELL | 20%, one vehicle, card payment | Art. 164(1)(b) and (1-bis) | ENI could also be energy: check the narration |
| FORMAZIONE / CORSO / SEMINARIO | 100% up to EUR 10,000 a year; hold any hotel or food element | Art. 54-septies(3) | RE17 |
| CANCELLERIA / MATERIALE UFFICIO / UNIEURO (office) | 100% if used in the activity | Art. 54(1) | Check the unit cost for assets |
| CONTRIBUTO CASSA [profession] / ENPAM / INARCASSA | Not Quadro RE; art. 10(1)(e) charge | Rigo RP21 | Replaces Gestione Separata for those enrolled |
| STRIPE FEE / PAYPAL FEE / SATISPAY FEE | 100% | Art. 54(1) | Deduct the gross-up difference |

### Bank formats and amounts

Carried from the prior version; not checked against bank files.

| Bank | Format | Key fields |
| --- | --- | --- |
| Intesa Sanpaolo | CSV (semicolon) | Data movimento; Valuta; Descrizione; Dare (debit); Avere (credit) |
| UniCredit | CSV / PDF | Data; Descrizione operazione; Dare; Avere; Saldo |
| BancoBPM | PDF / Excel | Data; Causale; Importo Dare; Importo Avere |
| FinecoBank | CSV | Data; Entrata; Uscita; Descrizione; Tipo |
| N26 Italy | CSV (app export) | Date, Payee, Account number, Transaction type, Payment reference, Amount (EUR) |
| Hype Business | CSV | Data; Descrizione; Importo; Tipo (ENTRATA/USCITA) |
| Revolut Italy | CSV | Type, Product, Started Date, Completed Date, Description, Amount, Fee, Currency, State |

| Narration | Meaning | Classification hint |
| --- | --- | --- |
| BONIFICO DA [sender] | Wire transfer credit | Professional income |
| ACCREDITO BONIFICO SEPA | SEPA credit transfer | Income |
| VB DA [sender] | UniCredit credit notation | Income |
| BONIFICO A FAVORE [payee] | Wire transfer debit | Expense |
| ADDEBITO | Direct debit | Recurring expense |
| PAGAMENTO F24 | Tax payment | Exclude as an expense; contributions go to RP21 |
| NEXI PAGAMENTI | Card terminal settlement | Income |
| INTERESSI ATTIVI | Interest earned | Not Quadro RE |
| CANONE CONTO | Account maintenance fee | Bank charges |

- Italian banks: thousands separator `.`, decimal `,` (for example `1.234,56`).
- N26 Italy: period decimal, no thousands separator (for example `1234.56`).
- FinecoBank: comma decimal, no thousands separator.
- Dates: DD/MM/YYYY at Italian banks; YYYY-MM-DD at N26.
- Revolut: filter `State = COMPLETED` only.

### Excel working paper

Working paper only: not a return. Set the period and copy the Needs Input list into Section H.

```text
ITALIAN INCOME TAX WORKING PAPER (REGIME ORDINARIO)
Taxpayer: ________  CF: ________  Period: ____  Region and comune at 1 January: ________

SECTION A: INCOME (Quadro RE)
Compensi received, ex-IVA, including 4% rivalsa     ________
Less: returned amounts or refunds                   (_______)
Net compensi                                        ________

SECTION B: DEDUCTIBLE EXPENSES (Quadro RE)
Rent (100% exclusive; 50% mixed)                    ________
Utilities (100% exclusive; 50% mixed)               ________
Telecoms (80%)                                      ________
Software subscriptions                              ________
Professional fees                                   ________
Legal fees                                          ________
Training (RE17, limit EUR 10,000)                   ________
Travel (traceable: see Traceability dates)          ________
Hotel, food and drink (75%, then 2% of compensi)    ________
Professional insurance                              ________
Bank charges                                        ________
Depreciation (ammortamento)                         ________
Payment processor fees                              ________
Other deductible expenses                           ________
TOTAL DEDUCTIBLE EXPENSES                           ________

SECTION C: INCOME (Quadro RE, rigo RE23)
Income (A less B)                                   ________

SECTION D: REDDITO COMPLESSIVO AND TAXABLE INCOME
Reddito complessivo, for the art. 13 detrazione     ________
Less: contributions paid (art. 10(1)(e), RP21)      (_______)
Reddito imponibile (RN4)                            ________

SECTION E: IRPEF
Gross tax (bands)                                   ________
Less: art. 13 detrazione                            (_______)
Net tax, floor 0                                    ________
Less: ritenute d'acconto                            (_______)
Less: acconti paid (F24)                            (_______)
IRPEF balance due or (refund)                       ________

SECTION F: ADDIZIONALI (base RV1)
Addizionale regionale (___%)                        ________
Addizionale comunale (___%)                         ________
Total addizionali                                   ________

SECTION G: CONTRIBUTIONS (from it-inps-contributions or cassa statement)
Contributions computed there                        ________
Less: advance contributions paid                    (_______)
Contribution balance due                            ________

SECTION H: REVIEWER FLAGS
[ ] Regime confirmed; forfettario gate checked (EUR 85,000 and EUR 100,000)
[ ] Vehicle: art. 164 limb, one vehicle, cost limit, card fuel
[ ] Equipment above EUR 516.46: depreciation schedule used; EUR 516.40 to EUR 516.46 held
[ ] Art. 13 EUR 50 increase, if RC is in range: both results shown and held
[ ] Training: any hotel or food element held
[ ] Telecoms: 80% applied
[ ] Hotel, food and drink: 75% and 2% applied; traceable in Italy from the start date in Traceability
[ ] Mixed-use premises: 50% rule and no other exclusive property
[ ] Acconti verified against F24 receipts
[ ] IVA stripped from all amounts
[ ] Cassa or Gestione Separata confirmed
[ ] Suspense items and Needs Input listed
```

## Deadlines and filing

Modello Redditi PF is filed online through the Agenzia delle Entrate services Fisconline or Entratel, directly or through an intermediary (Fascicolo 1; DPR 322/1998 art. 3). The precompilata service sits in the reserved area of agenziaentrate.gov.it, with SPID, CIE or CNS. RedditiOnLine PF builds the file. A person obliged to file an IVA, sostituto or IRAP return must file online (DPR 322/1998 art. 3(2)), which covers a professional obliged to the annual IVA return.

| Item | Date for the 2025 period | Source |
| --- | --- | --- |
| Modello Redditi PF online | 15 April to 2 November 2026; 31 October 2026 is a Saturday | [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/modello-redditi-persone-fisiche-2026/quando-e-come-presentare-il-modello-redditi-persone-fisiche); DPR 322/1998 art. 2(1) and (9) |
| Paper at the post office, only for those not obliged online | 15 April to 30 June 2026 | Same page; DPR 322/1998 art. 2(1) |
| Non-resident abroad unable to file online | 30 November 2026, by registered post (outside this file: R-IT-4) | [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/come-e-quando-presentare-la-dichiarazione-dei-redditi12) |
| Modello 730, for employees, pensioners and similar | 30 September 2026 | Same page |
| Saldo and first acconto, general | 30 June 2026, or 30 July 2026 with 0.40% | [Fascicolo 1](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026); DPR 435/2001 art. 17 |
| Saldo and first acconto, ISA taxpayer and the others in art. 6(2) | 20 July 2026, or the 30th day after with 0.80%. The August rule below carries that day to 20 August 2026 | D.L. 89/2026 art. 6, repealed by L. 113/2026 art. 1(2), which keeps its effects |
| Second or sole acconto | 30 November 2026 | Fascicolo 1, rigo RN62 |

- **Payment floor.** No payment if each tax is EUR 12 or less (Fascicolo 1).
- **ISA 2026 date.** It moves the date only: the first instalment stays 50%. It is confirmed for 2026 only. D.L. 89/2026 art. 6(2) extends it to those with an ISA exclusion cause, the art. 27(1) D.L. 98/2011 regime, the forfettario regime and partners under TUIR arts 5, 115 and 116 who meet art. 6(1). A forfettario year still stops under R-IT-6.
- **Instalments.** Saldo and first acconto may be paid in instalments, finishing by 16 December of the filing year, by the 16th of each month. Interest is 4% a year, with a flat 0.33% on later monthly instalments (Fascicolo 1, citing D.Lgs. 33/2025 art. 10). Payments due 1 to 20 August may go by the 20th without surcharge (D.Lgs. 33/2025 art. 11).
- **30 June** is a payment date, not a filing date. The prior version carried it in the filing row by mistake; the Redditi PF date moved to 31 October from the 2024 season, and 30 November was the date before that, as the prior version stated. That history was not re-read.
- **Addizionali.** The regional and comunale saldo are paid with the IRPEF saldo. The comunale acconto follows rigo RV17 and may be paid in instalments.
- **Late return.** A return filed within 90 days is valid, with sanctions for delay. After 90 days it counts as omitted but is a title for collection (DPR 322/1998 art. 2(7)).
- **Modello 730.** A person obliged to file IRAP, annual IVA or sostituto returns cannot use it (DM 164/1999 art. 13(5)(a)); the annual decree can exclude other income (art. 13(5)(b)). The Agenzia page sends everyone other than employees and pensioners to Redditi PF. So a professional under this file files Redditi PF, not 730. The prior version's statement that the 30 September date is absolute was not confirmed by any text read, and its fallback to Redditi PF was not tested: both are held.

For the 2026 period: Redditi PF 2027 and its form are not yet published. Under DPR 322/1998 art. 2(1) the online filing window runs 15 April to 31 October 2027; 31 October 2027 is a Sunday, so it moves to the first working day after. Paper at a post office: to 30 June 2027. Saldo 2026 and first acconto 2027: 30 June 2027, or the next 30 days with 0.40%. These dates are statutory and unconfirmed against the Agenzia 2027 pages (unverified).

## Penalties and interest

These rates apply to violations committed from 1 September 2024 (D.Lgs. 87/2024 art. 5(1)). Rates for earlier violations were not read and stay held. Sanctions for 2025-period returns fall under this text.

| Offence | Sanction | Source |
| --- | --- | --- |
| Omitted return | 120% of tax due, minimum EUR 250. If no tax due: EUR 250 to EUR 1,000, which may be doubled if the person must keep accounting records | [D.Lgs. 471/1997 art. 1(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=) |
| Return filed after 90 days, within the art. 43 DPR 600/1973 term and before formal knowledge of any access, inspection, verification or the start of any assessment | Art. 13(1) sanction x 3: 75% of the tax. If no tax due: EUR 250 to EUR 1,000, which may be doubled if the person must keep accounting records. No ravvedimento reduction | D.Lgs. 471/1997 art. 1(1-bis); D.Lgs. 472/1997 art. 13(2-ter) |
| Return filed within 90 days | Ravvedimento reduces the sanction to 1/10 of the minimum for omission: EUR 25 on the EUR 250 minimum. Late-payment sanctions are separate | D.Lgs. 472/1997 art. 13(1)(c). The prior 'EUR 250 reduced sanction' is corrected; administrative practice was not read |
| Under-declaration | 70% of the extra tax, minimum EUR 150. Up by half to double in art. 1(3). Reduced by one third where the error is under 3% and under EUR 30,000, or is only a timing error. EUR 250 if no loss to the Treasury | [D.Lgs. 471/1997 art. 1(2) to (4)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=) |
| Integrative return within the art. 43 DPR 600/1973 term and before formal knowledge of any access, inspection, verification or the start of any assessment | Art. 13(1) sanction x 2: 50%. If no tax due: EUR 150, the art. 1(2) minimum | D.Lgs. 471/1997 art. 1(2-bis) |
| Late payment | 25% of the unpaid amount. Halved to 12.5% within 90 days. Within 15 days, one fifteenth of the 12.5% for each day | [D.Lgs. 471/1997 art. 13(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=) |
| Failure to document a taxable operation (IVA), such as no invoice | 70% of the IVA, minimum EUR 300. EUR 250 to EUR 2,000 when the violation did not affect correct settlement of the tax | [D.Lgs. 471/1997 art. 6(1) and (4)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig=) |

Ravvedimento follows D.Lgs. 472/1997 art. 13: for instance 1/9 of the minimum within 90 days under (1)(a-bis) and 1/8 within the return term under (1)(b). The reduction is excluded for a return filed more than 90 days late (art. 13(2-ter)). Tax and interest at the legal rate must be paid with it (art. 13(2)). Lawful ravvedimento rates depend on the facts; send them to the reviewer. Ravvedimento: unpaid tax or acconto paid within 30 days: one tenth of the minimum penalty (D.Lgs. 472/1997 art. 13(1)(a)). Ravvedimento: after the return deadline for the year of the violation: one seventh of the minimum (D.Lgs. 472/1997 art. 13(1)(b-bis)). Interest with ravvedimento: legal rate, day by day: 1.60% a year from 1 January 2026 (D.Lgs. 472/1997 art. 13(2); D.M. 10 December 2025, GU n. 289 of 13 December 2025) (unverified: the D.M. was not opened). Ravvedimento is barred once a notice of assessment or liquidation is served (art. 13(1-ter)). Smaller reductions (one sixth, one fifth, one quarter) apply after an audit report or a draft assessment (art. 13(1)(b-ter) to (b-quinquies)); refer those.

## Cross-border points

Residence uses TUIR art. 2(2): for the greater part of the period, counting fractions of days, the person has residence or domicile under the civil code (main personal and family relations) or is present in Italy. Registration in the population register gives a presumption, against which contrary proof is allowed. Art. 2(2-bis) adds a rule for Italian citizens who moved to listed states. Residents are taxed on all income; non-residents on Italian-source income only (art. 3(1)). Self-employment activity carried on in Italy is Italian source (art. 23(1)(d)).

- **Non-residents.** Art. 24 allows only the charges in art. 10(1)(a), (g), (h), (i) and (l), allows art. 13 detrazioni and listed others, and denies family detrazioni. Art. 24(3-bis) instead applies arts 1 to 23 to a non-resident where there is adequate information exchange, at least 75% of total income is produced in Italy and the State of residence gives no similar relief. R-IT-4 stops the file in both cases.
- **Non-resident withholding.** DPR 600/1973 art. 25 sets 30% as final withholding. It is outside this file.
- **Foreign clients.** Foreign tax paid definitively can be credited, up to the share of Italian tax under art. 165(1). Treaty analysis is outside this file: R-IT-9.
- **Foreign reimbursements.** The traceability rules read here refer to costs in Italy. Foreign costs still need a link to the activity.
- **IVA.** Cross-border IVA belongs to `italy-vat-return`.

## Two worked examples that recompute

All names are fixtures. Each example shows a decision. Figures are estimates.

### Example 1: Quadro RE limits and the 2 bases

Period 2026. Milan designer, resident, regime ordinario, Gestione Separata confirmed, no other income. Compensi received EUR 60,000 plus EUR 2,400 rivalsa. Hotel and food EUR 3,000, all paid by card. Training EUR 12,000, all course fees with no hotel or food. Other deductible costs EUR 6,000. Contributions paid EUR 8,000. Ritenute EUR 5,000. Acconti EUR 3,000.

The decision is whether rivalsa is income, whether the limits bite, and which income drives the detrazione. Hotel and food meet the 2% limit, not the 75% figure. RC is before contributions, whereas the bands use income after contributions. The prior version's method deducted contributions in Quadro RE, took 75% and full training, and is shown for comparison.

```oa-check
name: IT 2026 Quadro RE limits with detrazione on reddito complessivo
inputs:
  fees: 60000
  rivalsa: 2400
  hospitality: 3000
  training: 12000
  other_costs: 6000
  contributions: 8000
  ritenute: 5000
  acconti: 3000
steps:
  - compensi: fees + rivalsa
  - hospitality_deductible: min(hospitality * 0.75, compensi * 0.02)
  - training_deductible: min(training, 10000)
  - expenses: hospitality_deductible + training_deductible + other_costs
  - rc: compensi - expenses
  - taxable: max(rc - contributions, 0)
  - gross_tax: 0.23 * min(taxable, 28000) + 0.33 * max(min(taxable, 50000) - 28000, 0) + 0.43 * max(taxable - 50000, 0)
  - ratio: floor((50000 - rc) / 22000 * 10000) / 10000
  - detrazione: 500 * ratio
  - net_tax: max(gross_tax - detrazione, 0)
  - balance: net_tax - ritenute - acconti
  - legacy_income: compensi - hospitality * 0.75 - training - other_costs - contributions
  - legacy_gross: 0.23 * min(legacy_income, 28000) + 0.33 * max(min(legacy_income, 50000) - 28000, 0)
  - legacy_ratio: floor((50000 - legacy_income) / 22000 * 10000) / 10000
  - legacy_net: legacy_gross - 500 * legacy_ratio
  - understatement: net_tax - legacy_net
expected:
  hospitality_deductible: 1248
  training_deductible: 10000
  rc: 45152
  taxable: 37152
  gross_tax: 9460.16
  detrazione: 110.15
  net_tax: 9350.01
  balance: 1350.01
  legacy_net: 8109.3
  understatement: 1240.71
```

The balance due is EUR 1,350.01 of IRPEF before addizionali, which stay Needs Input until the Milan rows are confirmed. The prior method would understate net IRPEF by EUR 1,240.71.

### Example 2: regime comparison for the 2025 period

Period 2025. Fixture client in Veneto with fiscal domicile there at 1 January 2025, ATECO 74.10, compensi EUR 70,000, costs EUR 20,000, 2024 compensi EUR 70,000, no employment income, no exclusion in art. 1(57). Contributions EUR 9,000 are assumed equal in both cases for comparison only; actual contributions under each regime come from `it-inps-contributions`. Regional rate 1.23% from the Veneto row of the 2025 table. Comunale rate 0.8% is a confirmed fixture input, with income above any exemption. The client asks which is cheaper.

The decision is the comparison, not a recommendation. At RC of exactly EUR 50,000, art. 13(5)(b-bis) gives a detrazione of 0. The forfettario line carries 2 cases. The 5% rate applies only if art. 1(65) is met; otherwise 15%. A forfettario year stops under R-IT-6, so this example supports the conversation only and does not prepare that year.

```oa-check
name: IT 2025 ordinary and forfettario comparison, no recommendation
inputs:
  compensi: 70000
  costs: 20000
  contributions: 9000
  regional_rate: 0.0123
  comunale_rate: 0.008
  coefficient: 0.78
steps:
  - rc: compensi - costs
  - taxable: max(rc - contributions, 0)
  - gross_tax: 0.23 * min(taxable, 28000) + 0.35 * max(min(taxable, 50000) - 28000, 0) + 0.43 * max(taxable - 50000, 0)
  - detrazione: 500 * max(50000 - rc, 0) / 22000
  - net_tax: max(gross_tax - detrazione, 0)
  - regional: taxable * regional_rate
  - comunale: taxable * comunale_rate
  - ordinary_total: net_tax + regional + comunale
  - forfettario_income: max(compensi * coefficient - contributions, 0)
  - substitute_15: forfettario_income * 0.15
  - substitute_5: forfettario_income * 0.05
  - difference_15: ordinary_total - substitute_15
expected:
  taxable: 41000
  gross_tax: 10990
  net_tax: 10990
  regional: 504.3
  comunale: 328
  ordinary_total: 11822.3
  forfettario_income: 45600
  substitute_15: 6840
  substitute_5: 2280
  difference_15: 4982.3
```

Ordinary is EUR 11,822.30 and forfettario is EUR 6,840 at 15%, or EUR 2,280 at 5% if art. 1(65) is met. Present both and refer the choice to a Commercialista. IVA and contribution differences are not included.

### Example 3: low income, the EUR 50 increase and the floor

Period 2026. Case A: RC EUR 15,000, contributions EUR 3,000. Case B: RC EUR 5,000, contributions EUR 1,200, ritenute EUR 1,000.

In Case A, RC is above EUR 11,000 and at most EUR 17,000. The statute adds EUR 50: detrazione EUR 991.94, net EUR 1,768.06. The form gives the increase only to art. 50(1)(e) to (i) income, so for a professional the detrazione is EUR 941.94 and net tax EUR 1,818.06. Both results are held until a reviewer settles the conflict in Sources. In Case B the detrazione exceeds gross tax, so net tax stops at 0, EUR 391 is not used, and the ritenute give a RN34 credit of EUR 1,000.

```oa-check
name: IT 2026 art. 13 detrazione band, increase and zero floor
inputs:
  rc_a: 15000
  contributions_a: 3000
  rc_b: 5000
  contributions_b: 1200
  ritenute_b: 1000
steps:
  - taxable_a: rc_a - contributions_a
  - gross_a: taxable_a * 0.23
  - ratio_a: floor((28000 - rc_a) / 22500 * 10000) / 10000
  - detrazione_a_statute: 500 + 765 * ratio_a + 50
  - detrazione_a_form: 500 + 765 * ratio_a
  - net_a_statute: max(gross_a - detrazione_a_statute, 0)
  - net_a_form: max(gross_a - detrazione_a_form, 0)
  - taxable_b: rc_b - contributions_b
  - gross_b: taxable_b * 0.23
  - net_b: max(gross_b - 1265, 0)
  - unused_b: max(1265 - gross_b, 0)
  - credit_b: ritenute_b - net_b
expected:
  gross_a: 2760
  detrazione_a_statute: 991.94
  detrazione_a_form: 941.94
  net_a_statute: 1768.06
  net_a_form: 1818.06
  gross_b: 874
  net_b: 0
  unused_b: 391
  credit_b: 1000
```

### Example 4: late payment by days late

Tax of EUR 1,000 unpaid at the due date, for a violation after 1 September 2024. The decision is which limb applies. Interest and ravvedimento are left out and go to the reviewer.

```oa-check
name: IT late payment sanction at 10, 40 and 120 days
inputs:
  tax: 1000
  days_short: 10
steps:
  - sanction_10_days: tax * 0.125 * days_short / 15
  - sanction_40_days: tax * 0.125
  - sanction_120_days: tax * 0.25
expected:
  sanction_10_days: 83.33
  sanction_40_days: 125
  sanction_120_days: 250
```

### Example 5: the EUR 440 reduction and its floor

Period 2026. RC EUR 250,000, net of the main home, contributions EUR 10,000. Two children in the household who meet art. 12(2), so art. 16-ter limit EUR 8,000 x 0.85 = EUR 6,800. Case A: EUR 2,500 of art. 15(1-ter) interest on a 2025 mortgage to build the main home, which art. 15(3-quater) keeps whole, within the EUR 2,582.28 cap and the limit. Case B: the same interest at EUR 1,000. Case C: EUR 3,000 of university fees under art. 15(1)(e), which art. 15(3-quater) does not protect. None includes medical costs.

The decision is what art. 15(3-bis) leaves and whether the reduction can pass the detrazione for those charges. RC is above EUR 240,000, so art. 15(3-bis)(b) leaves nil in Case C, at either printed art. 15(1) rate. Case B stops at 0. The text reduces the detrazione 'spettante in relazione ai seguenti oneri', and this file reads it as not cutting other tax.

```oa-check
name: IT 2026 art. 16-ter(5-bis) reduction with floor
inputs:
  rc: 250000
  contributions: 10000
  interest_a: 2500
  interest_b: 1000
  fees_c: 3000
steps:
  - taxable: rc - contributions
  - gross_tax: 6440 + 7260 + 0.43 * (taxable - 50000)
  - limit: 8000 * 0.85
  - detrazione_a: max(min(min(interest_a, 2582.28), limit) * 0.19 - 440, 0)
  - detrazione_b: max(min(min(interest_b, 2582.28), limit) * 0.19 - 440, 0)
  - ratio_c: max(240000 - rc, 0) / 120000
  - detrazione_c: max(min(fees_c, limit) * 0.19 * ratio_c - 440, 0)
  - net_a: gross_tax - detrazione_a
  - net_b: gross_tax - detrazione_b
  - net_c: gross_tax - detrazione_c
expected:
  gross_tax: 95400
  limit: 6800
  detrazione_a: 35
  detrazione_b: 0
  ratio_c: 0
  detrazione_c: 0
  net_a: 95365
  net_b: 95400
  net_c: 95400
```

### Bank line fixtures

Period 2025 fixtures carried from the prior version. They classify one line and stop. Each assumes the client's facts are confirmed.

**1. Intesa Sanpaolo, Milan, graphic designer.** `03/01/2025;;BONIFICO DA STUDIO GAMBA SRL;;3.500,00`. SEPA credit from a client SRL. Valentina has no pension fund. Confirm the amount is ex-IVA. Cash basis: compensi EUR 3,500.

**2. UniCredit, Turin, IT consultant.** `10/01/2025 | VB DA ACCENTURE SRL | AVERE EUR 6,500.00`. Monthly fee from one client: EUR 6,500 x 10 months = EUR 65,000 for the year. Compensi EUR 6,500. Flag single-client concentration and confirm no forfettario election: R-IT-6 applies if one is active.

**3. FinecoBank, Rome, photographer.** `15/03/2025;NEXI POS VERSAMENTO;Entrata;7.000,00`. Nexi settles net of fees. Match the merchant report for the gross amount and fee. Compensi EUR 7,000, or the gross figure if higher, with the fee as an expense.

**4. N26 Italy, Florence, translator.** `2025-05-20,STRIPE,,,STRIPE PAYOUT,22000.00,,,`. Payout net of fees. The prior version used about EUR 22,660 gross and EUR 660 of fees as an illustration; take the true figures from the Stripe report. Compensi on that illustration EUR 22,660, fee EUR 660 deductible under regime ordinario.

**5. Hype Business, Naples, e-commerce.** `2025-07-15;SUMUP PAYOUT;ENTRATA;15.000,00`. SumUp settlement. An e-commerce seller may earn business income, in which case Quadro RE does not apply and R-IT-7 stops the file. Confirm lavoro autonomo or impresa before any Quadro RE entry.

**6. BancoBPM, Bergamo, architect in Inarcassa.** `20/04/2025 | BONIFICO DA STUDIO ARCHITETTURA XYZ | AVERE EUR 8,500.00`. Gestione Separata does not apply to an Inarcassa member on the client's stated facts. The cassa percentage is held, so collect the annual statement. Compensi EUR 8,500 subject to the integrative contribution exclusion in art. 54(2)(a).

## Ask the client first

1. **Regime and activity.** Regime ordinario or forfettario, with prior-year compensi and employment income; lavoro autonomo or impresa; any other income, residence and special regime. Ask in Italian where useful: 'Regime fiscale: regime ordinario o forfettario?'
2. **Domicile and rates.** Regione e comune del domicilio fiscale al 1 gennaio of the year, and the rate rows that apply.
3. **Contributions.** Cassa previdenziale or Gestione Separata, whether 4% rivalsa was charged, and contributions paid in the year.
4. **Receipts and payments.** Total compensi received ex-IVA, ritenute with the Certificazione Unica, and acconti paid by F24.
5. **Family.** Spouse and children for art. 12 detrazioni, and the number of children in the household who meet art. 12(2), for art. 16-ter.
6. **Mixed use.** Vehicle use and how fuel was paid, and whether premises are exclusive, mixed or in the home, with any other property in the comune.

**If the client has only a bank statement.** Do not produce a figure. Mark credits from SRL and SPA entities as potential compensi. Exclude F24 tax payments. List contributions for rigo RP21. List telecom costs at 80%, hotel and food at 75% and vehicles at 20% for the reviewer. Generate a working paper with Needs Input flags, with no default rate for contributions or addizionali, then ask the 6 facts. R-IT-1 still stops any Quadro RE figure.

### Completion checks

- [ ] Regime and residence confirmed, and no refusal fired?
- [ ] Cash basis applied, with the withholding-agent rule?
- [ ] Telecoms at 80%?
- [ ] Vehicles by art. 164 limb, one vehicle, cost limit?
- [ ] Hotel and food at 75% and within 2%?
- [ ] Equipment above EUR 516.46 depreciated, not expensed, and any cost above EUR 516.40 up to EUR 516.46 held?
- [ ] IVA stripped from all amounts?
- [ ] Contributions deducted from reddito complessivo at RN3, not in Quadro RE?
- [ ] Art. 13 detrazione on RC, with bands on taxable income?
- [ ] F24 tax payments excluded from expenses?
- [ ] Addizionali on RV1, at confirmed rates?
- [ ] Detrazioni treated as tax credits, floor 0, not income deductions?
- [ ] Figures labelled estimated and open items listed?

## Sources

Read on 5 November 2026 unless stated. Normattiva text was read at the date shown by each URL, with a blank date meaning the current text. 'Current' TUIR text reads as in force to 31 December 2026. Arts 11 and 13 and DPR 600/1973 art. 25 were also read at 31 December 2025. The arts 54 to 54-septies and 164 rules were read at the current text only, and Fascicolo 3 supports their use for 2025 row by row. No full version comparison was made.

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| Normattiva, TUIR arts 2, 3, 8, 9 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art2!vig= | 2026-11-05 | Art. 2, art. 3(1), art. 8(1) and (3) and art. 9(2), the last 3 at the same URL pattern. The art. 2(2-bis) state list was not read |
| Normattiva, TUIR art. 10 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art10!vig= | 2026-11-05 | Art. 10(1)(e) contributions, in part |
| Normattiva, TUIR art. 11 at 31 December 2025 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2025-12-31 | 2026-11-05 | 2025 bands and art. 11(3) |
| Normattiva, TUIR art. 11 current | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig= | 2026-11-05 | 2026 bands |
| Normattiva, TUIR art. 11 at 1 January 2027 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2027-01-01 | 2026-11-05 | Repeal marker only; arts 54 and 54-septies checked the same way |
| Normattiva, TUIR art. 12 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art12!vig= | 2026-11-05 | Family detrazioni, in part |
| Normattiva, TUIR art. 13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig= | 2026-11-05 | Art. 13(5) to (6-bis), also at 31 December 2025 |
| Normattiva, TUIR art. 15 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art15!vig= | 2026-11-05 | Art. 15(1) opening words and (a), (b), (c) and (e), (1-ter), (3-bis) to (3-quater) and note 229; the rest was not read |
| Normattiva, TUIR art. 16-ter | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig= | 2026-11-05 | Whole article, current text only |
| Normattiva, TUIR art. 17 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art17!vig= | 2026-11-05 | Separate taxation, not used in a figure |
| Normattiva, TUIR arts 23, 24 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art24!vig= | 2026-11-05 | Art. 24(1) to (3-bis) in full and art. 23(1)(d) at the same URL pattern. The art. 24(3-bis) ministerial decree was not read |
| Normattiva, TUIR art. 53 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art53!vig= | 2026-11-05 | Art. 53(1) and (2) |
| Normattiva, TUIR art. 54 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54!vig= | 2026-11-05 | Whole article, current text only |
| Normattiva, TUIR arts 54-bis to 54-sexies | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig= | 2026-11-05 | Arts 54-ter and 54-quinquies in full at the current text; 54-bis, 54-quater and 54-sexies at the same URL pattern, for scope |
| Normattiva, TUIR art. 54-septies | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig= | 2026-11-05 | Whole article, current text only |
| Normattiva, TUIR art. 67 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art67!vig= | 2026-11-05 | Art. 67(1)(l), in part |
| Normattiva, TUIR art. 164 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig= | 2026-11-05 | Art. 164(1) and (1-bis) |
| Normattiva, TUIR art. 165 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art165!vig= | 2026-11-05 | Art. 165(1) only |
| Normattiva, L. 199/2025 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig= | 2026-11-05 | Art. 1(3), (4), (27) and (112) to (115), read in the capture retained on 31 October 2026 |
| Normattiva, L. 207/2024 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig= | 2026-11-05 | Art. 1(2), (12), (24), (81) and (83) |
| Normattiva, L. 190/2014 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig= | 2026-11-05 | Art. 1(54) to (89), read in the capture retained on 31 October 2026; annex not read |
| Normattiva, D.Lgs. 117/2026 art. 377 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117:1~art377!vig= | 2026-11-05 | Start date; no mapping of articles |
| Normattiva, D.Lgs. 117/2026 art. 376 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117:1~art376!vig= | 2026-11-05 | Art. 376(1)(e), in the capture retained on 31 October 2026 |
| Normattiva, D.Lgs. 446/1997 art. 50 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art50!vig= | 2026-11-05 | Whole article, current text |
| Normattiva, D.Lgs. 68/2011 art. 6 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig= | 2026-11-05 | Whole article; the D.Lgs. 147/2026 amendments were not dated by year of use |
| Normattiva, D.Lgs. 360/1998 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig= | 2026-11-05 | Art. 1(3) to (4) |
| Normattiva, DPR 322/1998 arts 2, 3 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig= | 2026-11-05 | Art. 2(1), (7), (8), (9) and, at the same URL pattern, art. 3(1) to (2-ter) |
| Normattiva, DM 164/1999 art. 13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:ministero.finanze:decreto:1999-05-31;164~art13!vig= | 2026-11-05 | Art. 13(4) and (5) |
| Normattiva, DPR 600/1973 art. 25 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art25!vig= | 2026-11-05 | Text and notes, also at 31 December 2025 and 1 January 2028. The amending Acts behind notes 21a, 30 and 54 were not read |
| Normattiva, D.Lgs. 471/1997 arts 1, 5, 6, 13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig= | 2026-11-05 | Arts 1, 6 and 13 for the rows stated, with art. 5 for scope, at the same URL pattern |
| Normattiva, D.Lgs. 472/1997 art. 13 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig= | 2026-11-05 | Art. 13(1), (2) and (2-ter). No Agenzia practice read |
| Normattiva, D.Lgs. 87/2024 art. 5 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-06-14;87~art5!vig= | 2026-11-05 | Commencement |
| Normattiva, D.Lgs. 192/2024 arts 5, 6 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-12-13;192~art6!vig= | 2026-11-05 | Art. 5 at the same URL pattern, and commencement in art. 6 |
| Normattiva, D.Lgs. 241/1997 art. 23 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art23!vig= | 2026-11-05 | Title and scope only |
| Normattiva, L. 662/1996 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1996-12-23;662~art1!vig= | 2026-11-05 | Art. 1(212) only |
| Normattiva, D.Lgs. 231/2007 art. 49 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art49!vig= | 2026-11-05 | Art. 49(1) and (3-bis) |
| Normattiva, D.L. 269/2003 art. 44 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig= | 2026-11-05 | Art. 44(2) |
| Normattiva, D.L. 34/2019 art. 12-quinquies | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2019-04-30;34~art12quinquies!vig= | 2026-11-05 | Art. 12-quinquies(3) and (4) |
| Normattiva, D.L. 124/2019 art. 58 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2019-10-26;124~art58!vig= | 2026-11-05 | Retained capture; the ISA acconto split only |
| Normattiva, D.L. 84/2025 arts 1, 16 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2025-06-17;84~art1!vig= | 2026-11-05 | Art. 1(1)(c) to (e), (2), (4) and (5), current and original text; art. 16 at the same URL pattern |
| Normattiva, L. 108/2025 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-07-30;108~art1!vig= | 2026-11-05 | Conversion and publication note only |
| Normattiva, DPR 435/2001 art. 17 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-12-07;435~art17!vig= | 2026-11-05 | Retained capture; art. 17(3) only |
| Normattiva, D.L. 89/2026 art. 6 and L. 113/2026 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-05-22;89~art6!vig=2026-05-23 | 2026-11-05 | Units retained from r521: the ISA deferral, art. 6(1) and (2) (text in force 23 May to 27 June 2026), and the repeal that keeps its effects. The annex to L. 113/2026 was not read |
| Agenzia delle Entrate, Redditi PF 2026, Fascicolo 1 instructions | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026 | 2026-11-05 | Rounding, payments, instalments, RN, RP section I on the 19% charges, RP21, RN62 and RV rows and regional table; PDF text, extraction good; the regional table's PDF pages 181 and 182 read as rendered images |
| Agenzia delle Entrate, Redditi PF 2026, Fascicolo 3 instructions | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026 | 2026-11-05 | Quadro RE in full; LM sections for forfettario; coefficient table read from PDF page 44 rendered with PyMuPDF |
| Agenzia delle Entrate, Redditi PF 2026 Fascicolo 1 model | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_modello_2026_agg-13-05-2026 | 2026-11-05 | Row labels only |
| Agenzia delle Entrate, Redditi PF 2026 Fascicolo 3 model | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_modello_2026_agg-13-05-2026 | 2026-11-05 | RE7 label and row labels |
| Agenzia delle Entrate, Redditi PF 2026 update of 28 May 2026 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/aggiornamento-rpf-2026_-28_-05-2026 | 2026-11-05 | Scan for affected rows |
| Agenzia delle Entrate, addizionale comunale list 2026 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/elenco-annuale-addizionale-comunale-modulistica-2026_def | 2026-11-05 | Structure and notes; every row parsed by word position for rates above 0.8, with PDF page 4 checked as a rendered image; no single comune row is relied on |
| Agenzia delle Entrate, Aliquote e calcolo dell'Irpef | https://www.agenziaentrate.gov.it/portale/aliquote-e-calcolo-dell-irpef7 | 2026-11-05 | Page updated 13 January 2026 |
| Agenzia delle Entrate, When and how to file | https://www.agenziaentrate.gov.it/portale/come-e-quando-presentare-la-dichiarazione-dei-redditi12 | 2026-11-05 | Page updated 27 March 2026 |
| Agenzia delle Entrate, Redditi PF 2026, who files | https://www.agenziaentrate.gov.it/portale/modello-redditi-persone-fisiche-2026/che-cos- | 2026-11-05 | Page updated 13 May 2026 |
| Agenzia delle Entrate, Redditi PF 2026, when to file | https://www.agenziaentrate.gov.it/portale/modello-redditi-persone-fisiche-2026/quando-e-come-presentare-il-modello-redditi-persone-fisiche | 2026-11-05 | Dates and online rule |
| Agenzia delle Entrate, Redditi PF 2026, model and legal basis pages | https://www.agenziaentrate.gov.it/portale/modello-redditi-persone-fisiche-2026/modello-e-istruzioni | 2026-11-05 | Index pages, for form versions |
| Presidency of the Council of Ministers, communique 195 | https://www.governo.it/it/articolo/comunicato-stampa-del-consiglio-dei-ministri-n-195/32973 | 2026-11-05 | Announcement of the 2027 budget bill: the bill text was not read |

### Source conflicts

- **EUR 516.40 or EUR 516.46.** TUIR art. 54-quinquies(1) prints EUR 516.40, as does the amending D.Lgs. 192/2024 art. 5. The Redditi PF 2026 RE7 label and instruction print EUR 516.46. Both are stated and neither is adopted: hold a unit cost above EUR 516.40 up to EUR 516.46.
- **Art. 13(5-ter) EUR 50 increase.** The statute, in the current text and at 31 December 2025, raises the detrazione under art. 13(5), which covers art. 53 income. Fascicolo 1, for the 2025 period, gives the increase 'solo per i redditi di cui all'art. 50, comma 1 lett. e), f), g), h) ed i)', other than periodic payments under art. 10(1)(c). No form for the 2026 period was read. Both are stated and neither is adopted: Example 3 shows both results.
- **Hotel and food in training costs.** Art. 54-septies(3) deducts training costs in full, 'comprese quelle di viaggio e soggiorno'. Fascicolo 3 rigo RE17 col. 1 enters hotel and food for courses and conferences at 75%, and col. 2 adds fees, travel and stay not in col. 1, within EUR 10,000. Both are stated and neither is adopted: hold a hotel or food element.
- **Art. 15(1) rate.** The retained text of TUIR art. 15(1) prints 22 per cento. Art. 15(1-ter), art. 16-ter(5-bis)(a) and Fascicolo 1, which lists the art. 15 charges, print 19 per cento. Nothing read explains the difference, and it is held. No figure here rests on it: Example 5 uses art. 15(1-ter), and its Case C is nil at either rate.
- **DPR 600/1973 art. 25.** The printed sentence shows 15%, and the notes to the text record later amendments that reach 20%. The note chain was read; the amending Acts were not read directly.
- **Acconto floor.** The prior version and `it-estimated-tax` print EUR 51.65. Rigo RN62 tests a whole-euro Differenza against EUR 52. The EUR 51.65 statute was not read.
- **Upper regional rate.** The prior version gave 3.33%. The 2025 table prints 3.63% for Molise's top band. Its first band, 2.03%, is 0.8 points above the base, whilst D.Lgs. 68/2011 art. 6(3) says an increase above 0.5 points does not apply to first-band income. The legal basis of neither rate was read.
- **Comunale rates above 0.8.** D.Lgs. 360/1998 art. 1(3) caps the variation at 0.8 points. In the 2026 list, 12 of the 7,896 rows parsed print a rate above 0.8, from 0.9 to 1.2: Alessandria, Avellino, Brindisi, Genova, Lecce, Napoli, Palermo, Potenza, Roma, Salerno, Torino and Vibo Valentia. Their legal basis was not read, and no comune row is relied on.

### Other legacy topics

- **Crypto and NFT.** Separate from professional income and not in Quadro RE. Use `italy-crypto-tax`. L. 207/2024 art. 1(24) sets 33% from 1 January 2026, with 26% on euro-denominated e-money tokens; the prior 26% is not current for 2026. The 2025 rate and the form rows were not read here.
- **Occasional work.** Art. 67(1)(l) treats non-habitual self-employment as redditi diversi. The EUR 5,000 line is a Gestione Separata enrolment test, not an income tax exemption. Confirm habitual or occasional status first. Withholding differences were not read.
- **Known gaps.** Regime forfettario preparation; corporate tax (IRES and IRAP); non-resident income; capital gains (plusvalenze); crypto and NFT; redditi fondiari.
- **Excluded jurisdictions.** The prior version names no fixed excluded jurisdiction. Art. 2(2-bis) refers to a list of states that was not read.

Not yet confirmed: Redditi PF 2027, its rows and dates; the 2026 regional and comunale saldo rates; TU 117/2026 article mapping; final 2027 budget law; legal basis for printed regional rates above 3.33%, Molise's first band and comunale rates above 0.8 points; EUR 516.40 against EUR 516.46; the art. 13(5-ter) increase for art. 53 income; the art. 15(1) rate, printed as 22 and as 19; hotel and food in training costs; the repeal date of art. 54(6-ter) and its effect on re-charged costs; 2025 costs invoiced before and paid after the D.L. 84/2025 start; the art. 24(3-bis) ministerial decree; art. 164(1)(a) for a professional; the ministerial depreciation coefficients; Annex 4 to L. 190/2014 and its 2026 coefficients for ATECO 2025; art. 2(2-bis) state list; loss carry-forward after 2007; sanctions for earlier violations; 730 lateness and fallback; legal interest; Agenzia practice on ravvedimento and art. 54-quinquies(4); INPS rates and the 2025 massimale, owned by `it-inps-contributions`; INPS Circular 8/2026 full text; `dichiarazioni.agenziaentrate.it` as a portal address; `it-regime-forfettario`; employee and mixed fixtures; a reviewer's sign-off on this text.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | November 2026 | Converted to the upstream template. Primary-source check. Corrected contributions (art. 10, not Quadro RE), art. 13 base, telecom, hospitality, training and vehicle provisions, penalties, cash limit and defaults. Added the art. 13(5-ter) and art. 15(3-bis) rows, refusals, an operational hold and forfettario entry figures |
| 2.1 | November 2026 | 2026 IRPEF brackets; Gestione Separata massimale by year; R-IT-3 split at EUR 85,000 and EUR 100,000 |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Italian bank formats (Intesa, UniCredit, FinecoBank, N26, Hype); transaction pattern library; Nexi and Satispay patterns; worked examples; prohibitions and disclaimer added |
| 1.0 | 2025 | Initial version |
