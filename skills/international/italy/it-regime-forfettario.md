---
name: it-regime-forfettario
description: "Italy's regime forfettario (flat-rate regime) for individuals running a business or a profession, tax year 2026, under L. 190/2014 art. 1 commi 54-89. Covers the entry and stay conditions (EUR 85,000 revenue, EUR 20,000 staff costs, the employment-income bar raised to EUR 35,000 for 2025 and 2026, the comma 57 exclusions), the same-year exit above EUR 100,000, the full table of coefficienti di redditivita by ATECO group, the 15% substitute tax and the 5% start-up rate, deduction of INPS contributions, no VAT and the invoice wording, e-invoicing, the EUR 2 stamp duty, the 35% INPS cut for artigiani and commercianti, acconti, Quadro LM, leaving the regime, and penalties. Trigger on: forfettario, forfetario, flat tax partita IVA, imposta sostitutiva 15%, 5% startup, coefficiente di redditivita, Quadro LM, superamento 100.000. Out of scope: regime ordinario (it-income-tax), employees (it-irpef-employees), INPS rates (it-inps-contributions), acconti method (it-estimated-tax), VAT returns (italy-vat-return), e-invoice XML (italy-einvoice)."
jurisdiction: IT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Italy: the regime forfettario (flat-rate regime), tax year 2026

The forfettario is the default regime for an individual with a VAT number whose business or professional receipts are small. Taxable income is not profit: it is receipts times a fixed coefficient for the activity, less the social contributions paid. One substitute tax at 15% (5% for qualifying start-ups) replaces IRPEF, the regional and municipal surcharges and IRAP. No VAT is charged.

For 2026 the rules are L. 190/2014, art. 1, commi 54 to 89, as in force on 22 October 2026. From 1 January 2027 those commi are repealed and the regime moves into the new income tax code, D.Lgs. 117/2026, Capo XXI "Regime forfetario" (from art. 232). This skill does not cover the 2027 wording. Income earned in 2026 stays under the L. 190/2014 rules even though the return is filed in 2027.

Related skills, not repeated here:
- `it-income-tax`: the regime ordinario for the self-employed, and what happens when this regime does not apply.
- `it-irpef-employees`: employment and pension income, which a forfettario may also have and which is taxed under IRPEF.
- `it-inps-contributions`: gestione separata rates and bases. Artigiani and commercianti rates are not yet in the pack.
- `it-estimated-tax`: the acconti method and the F24 codes for the substitute tax.
- `italy-vat-return`: the regime ordinario VAT return, for the year after leaving.
- `italy-einvoice`: the FatturaPA file, SdI routing and stamp duty mechanics.

## Who this applies to

**In scope.** Individuals (persone fisiche) who run a business (impresa), including artigiani and commercianti, or practise an art or profession (lavoro autonomo). The regime is "natural": someone already in business who meets the conditions applies it without any election. Someone starting out says in the start-of-activity form (modello AA9/12) that they expect to meet the conditions. Leaving that out does not block the regime but carries a penalty of EUR 250 to 2,000 (Agenzia, "Modalita di accesso al regime").

**Entry conditions, tested on the PREVIOUS year (comma 54).** Both must hold:
1. Revenue or fees, annualised, not above EUR 85,000. With several ATECO codes, add them all together (comma 55(b)). Count on the regime used that year: cash basis for professionals, accrual for an ordinary business (Redditi PF 2026, Fascicolo 3, Quadro LM, citing Circolare 32/E of 5 December 2023).
2. Gross spending on employees, collaborators and accessory work not above EUR 20,000.

**Exclusions (comma 57).** The regime is closed to:
- (a) people using a special VAT regime or another flat-rate method of computing income;
- (b) non-residents, except residents of an EU or EEA state with adequate information exchange who earn at least 75% of their total income in Italy. For VAT, someone established in another EU state uses the EU SME franchise in D.P.R. 633/1972, Title V-ter, instead;
- (c) people who sell, only or mainly, buildings, building land or new means of transport;
- (d) people who at the same time hold a stake in a partnership, professional association or family business, or who control, directly or indirectly, an S.r.l. or an associazione in partecipazione whose activity is directly or indirectly linked to their own. A partnership stake must be disposed of by the end of the previous year. The S.r.l. test is run in the year itself and, if failed, ends the regime from the next year (Fascicolo 3, citing Circolare 9/E of 10 April 2019);
- (d-bis) people who work mainly for a current employer, or one from the two previous tax years, or for parties linked to that employer. This does not apply to someone starting after the compulsory professional traineeship (pratica). Prevalence is tested at the end of each year and bites the next year;
- (d-ter) people whose employment and similar income (TUIR arts. 49 and 50) in the previous year was above EUR 30,000. For the regime years 2025 and 2026 the limit is EUR 35,000 (L. 207/2024, art. 1, c. 12, as amended by L. 199/2025, art. 1, c. 27). "2025 and 2026" are the years the regime is applied, not the years tested: the law raises the comma 57(d-ter) limit for those years, and the Redditi PF 2026 instructions (Fascicolo 3, Quadro LM, for 2025 income) apply EUR 35,000 to someone entering the regime in 2025, which tests 2024 income. So for 2026, employment income received in 2025 must not exceed EUR 35,000. For 2027, the EUR 30,000 limit applies to 2026 employment income unless a new law raises it. The test does not apply if the job ended. The Agenzia adds that it still applies if, in the year the job ended, the person had pension income or income from another job (Agenzia, "Che cos'e").

**When the regime stops (comma 71).**
- A condition in comma 54 fails, or an exclusion in comma 57 applies: the regime ends from the FOLLOWING year.
- Receipts in the year go above EUR 100,000: the regime ends in the SAME year. See "Leaving the regime" below.

**Opting out.** A forfettario may choose ordinary IRPEF and VAT instead. The choice binds for at least three years (comma 70) and is shown in the annual VAT return.

**Not in scope.** Companies, partnerships and professional associations (see `it-ires-corporate-tax`, `it-irap`).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Entry: previous-year revenue or fees, annualised, all ATECO codes together | not above EUR 85,000 | 2026 | L. 190/2014 art. 1 c. 54(a), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-10-22 |
| Entry: previous-year gross staff and collaborator costs | not above EUR 20,000 | 2026 | c. 54(b), same URL |
| Same-year exit: receipts in the year above | EUR 100,000 | 2026 | c. 71, same URL |
| Exclusion: previous-year employment income above (standing figure) | EUR 30,000 | standing | c. 57(d-ter), same URL |
| The same limit, regime years 2025 and 2026 (tested on 2024 and 2025 employment income) | EUR 35,000 | 2025, 2026 | L. 207/2024 art. 1 c. 12, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1 ; extended to 2026 by L. 199/2025 art. 1 c. 27, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1 |
| Non-resident EU/EEA: share of total income earned in Italy | at least 75% | 2026 | c. 57(b), L. 190/2014 URL above |
| Substitute tax (replaces IRPEF, regional and municipal surcharges, IRAP) | 15% | 2026 | c. 64, L. 190/2014 URL above |
| Start-up rate, year activity starts and the next four | 5% | 2026 | c. 65, L. 190/2014 URL above |
| INPS cut for artigiani and commercianti who opt in | 35% off the contributions due | 2026 | c. 77, L. 190/2014 URL above |
| Deadline to opt in to the INPS cut (businesses already active) | 28 February each year | 2026 | c. 83, L. 190/2014 URL above |
| Stamp duty on an invoice without VAT above EUR 77.47 | EUR 2 per invoice | 2026 | Agenzia, stamp duty on e-invoices (June 2026), https://www.agenziaentrate.gov.it/portale/documents/d/guest/l-imposta_di_bollo_sulle_fatture_elettronichegiugno2026 |
| Penalty: start-up form silent on the regime, or opt-out not shown in the VAT return | EUR 250 to 2,000 | 2026 | Agenzia, https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/modalita-di-accesso-al-regime |

**Coefficienti di redditivita (L. 190/2014 allegato 4, as replaced by L. 145/2018 allegato 2).** Taxable income = receipts times the coefficient of the activity's ATECO 2007 group.

| No. | Sector group | ATECO 2007 codes | Coefficient |
|---|---|---|---|
| 1 | Food and beverage manufacturing | 10-11 | 40% |
| 2 | Wholesale and retail trade | 45; 46.2 to 46.9; 47.1 to 47.7; 47.9 | 40% |
| 3 | Street trade in food and drink | 47.81 | 40% |
| 4 | Street trade in other goods | 47.82-47.89 | 54% |
| 5 | Construction and real estate | 41-42-43; 68 | 86% |
| 6 | Trade intermediaries (agents) | 46.1 | 62% |
| 7 | Accommodation and food service | 55-56 | 40% |
| 8 | Professional, scientific, technical, health, education, financial and insurance services | 64-65-66; 69-70-71-72-73-74-75; 85; 86-87-88 | 78% |
| 9 | Other economic activities | 01-02-03; 05-06-07-08-09; 12 to 33; 35; 36-37-38-39; 49-50-51-52-53; 58-59-60-61-62-63; 77-78-79-80-81-82; 84; 90-91-92-93; 94-95-96; 97-98; 99 | 67% |

Source: the Gazzetta Ufficiale page of L. 145/2018 allegato 2, published by the Agenzia (https://www.agenziaentrate.gov.it/portale/documents/20143/241208/allegato+4.pdf/d69be7fc-b18a-3c73-bd2e-b0f3c1970218), and the same table in the Redditi PF 2026 instructions, Fascicolo 3, Quadro LM.

**ATECO 2025.** No ATECO 2025 coefficient table exists. Until new coefficients are approved, income is computed with the allegato 4 coefficient for the activity's ATECO 2007 code (D.Lgs. 81/2025, art. 1, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2025-06-12;81~art1!vig=2026-10-22). Quadro LM asks for both: the ATECO 2025 code in LM21 column 4, and the ATECO 2007 code and its coefficient in LM22 columns 1 and 2. To match a 2025 code to its 2007 code, the Agenzia points to ISTAT's conversion page.

## The taxable base

**Receipts, cash basis.** Revenue and fees count when received, for businesses as well as professionals (Fascicolo 3, Quadro LM). Costs are not deducted: the coefficient stands in for them.

**Computation (comma 64; Quadro LM rows):**
1. For each sector group: receipts x coefficient (LM22 to LM27, column 5). Activities in one group share one row, under the main activity's code. Activities in different groups each get their own row.
2. Gross income = the sum of the rows (LM34, column 3).
3. Less compulsory social contributions PAID in the year (LM35). This includes contributions paid for dependent family helpers in an impresa familiare, and for other family helpers where the owner did not recharge them. Any excess over the forfettario income is deducted from total IRPEF income under TUIR art. 10 (LM49).
4. Net income (LM36).
5. Less losses brought forward from before the regime, under the ordinary TUIR rules (comma 68; LM37).
6. Income subject to substitute tax (LM38) x 15% or 5% = substitute tax (LM39).
7. Less tax credits (LM40), withholding ceded by a consorzio (LM41), acconti paid (LM45): balance due or refundable (LM46 or LM47).

**Special receipts.** Copyright fees linked to the activity go in column 4 and count at 75%, or 60% if the person is under 35 (Fascicolo 3, citing TUIR art. 54-octies). Maternity allowances count in the base but not toward the EUR 85,000 and EUR 100,000 limits (code 1 in column 7). Amateur sports fees are tax-free up to EUR 15,000 but count in full toward the limits (code 2).

**Property** owned by the forfettario is outside the regime. Its income is taxed as building income of the individual (Circolare 10/E of 4 April 2016, cited in Fascicolo 3).

**Forfettario income still counts** wherever another rule depends on income, for deductions, credits or benefits, including non-tax benefits (comma 75).

**Other income** (a salary, rent, investments) is taxed under IRPEF in the usual way: see `it-irpef-employees`.

**The 5% start-up rate (comma 65).** It applies for the tax year the activity starts and the four after it, if:
- (a) the person did not carry on an artistic, professional or business activity, alone, in a partnership or in a family business, in the three years before starting;
- (b) the new activity is in no way a mere continuation of earlier employment or self-employment. A compulsory professional traineeship does not count;
- (c) if the person takes over someone else's business, that business's receipts in the previous year were not above EUR 85,000.

The person confirms these by ticking LM21 column 3. If one year's income has to be split between a "new" activity at 5% and a second activity at 15%, Quadro LM is filled in twice (two modules).

**INPS for artigiani and commercianti (commi 76 to 84).** Forfettari who run a business may ask INPS to compute the artigiani or commercianti contributions on the forfettario income, cut by 35% (comma 77). Someone already in business must apply by 28 February of the year; someone starting applies online when they start. A late application works from the following year (comma 83). The cut ends from the year after the regime ends, and once someone is back on the ordinary INPS regime they can never use the cut again (comma 82). The cut does not apply to professionals in the gestione separata. Contribution rates and the minimum income base are not in this skill. `it-inps-contributions` covers the gestione separata only, so artigiani and commercianti rates are a gap in the pack.

**VAT (commi 58 to 60).** A forfettario charges no VAT on domestic sales, deducts no input VAT, keeps no VAT registers and files no annual VAT return. They still number and keep purchase invoices and customs documents. On reverse-charge purchases, and other operations where they are the debtor, they self-charge VAT and pay it by the 16th of the following month (comma 60). A forfettario may issue a simplified invoice whatever the amount (comma 59). The Agenzia's "Semplificazioni e adempimenti" page still gives the older deadline for this self-charged VAT (the 16th of the second month after each quarter); comma 60 as in force sets the 16th of the following month.

**Invoice wording** (Agenzia, "Fattura elettronica per i forfettari"):
- Tax regime field: "Regime forfettario (art.1, c.54-89, L. 190/2014)" (RF19).
- Each line: VAT rate "0%", nature "Non soggette - altri casi" (N2.2).
- Causale: "Operazione effettuata in regime forfettario ai sensi dell'articolo 1, commi da 54 a 89, della Legge n. 190/2014 e successive modificazioni".
- A professional adds a second causale: "Operazione non soggetta a ritenuta alla fonte a titolo di acconto ai sensi dell'articolo 1, comma 67, Legge n. 190 del 2014 e successive modificazioni". Clients do not withhold tax from forfettario fees (comma 67).
- For an invoice over EUR 77.47 without VAT, add EUR 2 stamp duty (BolloVirtuale "SI"), included in the invoice total.

**E-invoicing.** Every forfettario has had to e-invoice through the SdI since 1 January 2024. Those with 2021 receipts above EUR 25,000 had to start on 1 July 2022 (D.L. 36/2022, art. 18(3)). File format, routing and the quarterly stamp-duty payment are in `italy-einvoice`. The Agenzia's "Semplificazioni e adempimenti" page still contains an older line saying forfettari need not e-invoice. The law and the same page's own list of duties say they must.

**No bookkeeping, no withholding.** Forfettari keep no accounting books (comma 69) and are outside the ISA reliability indices. They do not act as withholding agents, except on employee pay (D.P.R. 600/1973 arts. 23 and 24). They report in the return, in Quadro RS, the payees from whom they withheld nothing.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Return: Modello Redditi PF, Quadro LM section III (plus RS information, and RR for INPS), filed online | 15 April to 31 October of the year after (2026 income: by 31 October 2027) | D.P.R. 322/1998 art. 2(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art2!vig=2026-10-22 |
| Balance (saldo) for 2026 and first acconto for 2027 | 30 June 2027, or within the next 30 days with a 0.40% surcharge | Agenzia, "Come si paga l'Irpef", https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef ; comma 64 applies the IRPEF payment rules |
| Acconti: forfettari pay two EQUAL instalments, 30 June and 30 November | one payment by 30 November if the total is not above EUR 206 | same Agenzia page |
| Acconto base | 100% of the previous year's tax, or of the lower tax expected | same Agenzia page |
| INPS artigiani and commercianti contributions under the cut | same dates as the income tax balance and acconti | comma 79 |
| Opt in to the INPS cut | 28 February | comma 83 |
| Payment channel | F24 | Agenzia payment page |

The forecast method, the minimum below which no acconto is due, the instalment plan and the F24 tax codes for the substitute tax are in `it-estimated-tax`. Do not repeat them from memory.

**2027 caveat.** The filing and payment rules quoted here are the ones in force on 22 October 2026. From 1 January 2027 the payment and penalty rules move into new consolidated codes (see the pack README). Check the 2027 dates on the Agenzia site before relying on them for 2026 income.

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Return not filed | 120% of the tax due, minimum EUR 250; EUR 250 to 1,000 if no tax is due | D.Lgs. 471/1997 art. 1(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-22 |
| Income or tax understated | 70% of the extra tax, minimum EUR 150 | D.Lgs. 471/1997 art. 1(2), same URL |
| Tax paid late or not paid | 25% of the unpaid amount; halved if paid within 90 days; within 15 days, a further cut of one fifteenth per day of delay | D.Lgs. 471/1997 art. 13(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-22 |
| False statement of the comma 54, 57 or 65 conditions, where the income assessed is more than 10% above the income declared | the minimum and maximum penalties of D.Lgs. 471/1997 go up by 10% | L. 190/2014 art. 1 c. 74 |
| Same, once the assessment is final | the regime ends from the year after | c. 74 |
| Start-up form silent on the regime; opt-out not shown in the VAT return | EUR 250 to 2,000 | Agenzia, "Modalita di accesso al regime" |

Interest on late payment and voluntary correction (ravvedimento operoso) follow the general rules. They are not set out here.

No shorter assessment period. Comma 74 used to cut the Agenzia's assessment period by one year for a forfettario whose receipts were all e-invoiced. D.Lgs. 148/2026, art. 21(1), removed that sentence with effect from tax year 2026, so 2026 income has the ordinary assessment period. The Agenzia's "Semplificazioni e adempimenti" page still describes the old reduction; the law governs.

## Cross-border points

- **Non-residents.** Only EU or EEA residents who earn at least 75% of their total income in Italy can use the regime (comma 57(b)). For VAT they use the EU SME franchise (D.P.R. 633/1972, Title V-ter), not the forfettario VAT rules.
- **Selling abroad.** Intra-EU supplies of goods follow D.L. 331/1993 art. 41(2-bis). Services to or from non-residents follow D.P.R. 633/1972 arts. 7-ter and following. Imports and exports follow the general rules, but a forfettario cannot buy VAT-free as a habitual exporter (comma 58). Reverse-charge VAT on purchases is self-charged and paid by the 16th of the following month (comma 60). Cross-border invoice data go to the SdI (`italy-einvoice`).
- **Moving to Italy.** Someone using the impatriati regime must check whether it can be combined with the forfettario before choosing: see `it-impatriati`. This skill does not settle that point.
- **Foreign tax credits** go in LM40 against the substitute tax (Fascicolo 3). Treaty points are in `it-cross-border`.

## Leaving the regime

**Over EUR 85,000 but not over EUR 100,000 in 2026.** The 2026 income stays under the forfettario. The regime ordinario applies from 1 January 2027.

**Over EUR 100,000 during 2026** (comma 71; Agenzia, "Conseguenze della fuoriuscita"; Circolare 32/E of 5 December 2023, cited in Fascicolo 3):
- **VAT** is due from the invoice whose payment takes receipts over EUR 100,000, and on every invoice after it. If that invoice was issued earlier without VAT, the seller adds the VAT with a debit note. Invoices issued without VAT before that payment are not corrected. VAT registers start from that point.
- **Income tax** is computed under the regime ordinario for the WHOLE year, from 1 January. Ordinary records must be set up. The year's income is taxed under progressive IRPEF and the surcharges (`it-income-tax`).
- **Withholding.** For a professional, the client withholds tax from the fee whose payment crosses the limit and from later fees, not from earlier ones. The professional becomes a withholding agent on payments made after crossing.

**After leaving, or in the first ordinary year:**
- Receipts already taxed under the forfettario are not taxed again, and income that was not yet taxed is caught later (comma 72). Costs incurred during the regime are not deductible later.
- Input VAT on stock, unused services and capital goods (5 years; 10 for buildings) is adjusted in one go in the first ordinary VAT return (comma 61; Agenzia, "Conseguenze della fuoriuscita").
- The INPS cut for artigiani and commercianti is lost for good (comma 82).
- If they opted out, they stay in the ordinary regime for at least three years (comma 70).

## Worked examples

### Example 1: freelance consultant at 15%

Giulia is a management consultant (ATECO 70.22, group 8, coefficient 78%), resident in Italy and in her eighth year of activity, so the 5% rate is over. In 2025 her fees were EUR 58,000, she had no employment income and no staff. She meets the entry test for 2026.

In 2026 she receives EUR 60,000 in fees. She pays EUR 9,000 into the INPS gestione separata during 2026 (her 2025 balance and 2026 acconti). Fees x 78% = EUR 46,800. Less the EUR 9,000 contributions = EUR 37,800. Substitute tax at 15% = EUR 5,670. No IRPEF, no surcharges, no IRAP, no VAT. Her clients withheld nothing, so all EUR 5,670 is paid through the return, less any acconti already paid for 2026. Her 2027 acconto, by the historical method, is 100% of EUR 5,670. That is above EUR 206, so she pays two equal instalments of EUR 2,835 on 30 June and 30 November 2027.

```oa-check
name: Forfettario consultant, coefficient 78%, EUR 60,000 fees, 15% (2026)
inputs:
  fees: 60000
  coefficient: 0.78
  inps_paid: 9000
  rate: 0.15
steps:
  - gross_income: fees * coefficient
  - net_income: gross_income - inps_paid
  - substitute_tax: net_income * rate
  - acconto_2027: substitute_tax * 1
  - instalment_each: acconto_2027 / 2
expected:
  gross_income: 46800
  net_income: 37800
  substitute_tax: 5670
  instalment_each: 2835
```

### Example 2: start-up at 5% that crosses EUR 100,000 in October

Marco started as a freelance software developer (ATECO 62.01, group 9, coefficient 67%) in March 2024, with no activity in the three years before and no link to a former employer. 2026 is his third year, so he would pay 5%. His 2025 fees were EUR 80,000, so he entered 2026 in the regime.

In 2026 he receives EUR 96,000 by 30 September. On 20 October he is paid EUR 9,000 on an invoice issued in September without VAT. That takes him to EUR 105,000. In November and December he invoices and is paid a further EUR 6,000. Total 2026 receipts are EUR 111,000. He paid EUR 14,000 to the gestione separata in 2026, and his actual deductible business costs were EUR 12,000.

**What changes:**
1. **VAT.** He issues a debit note adding VAT at 22% on the EUR 9,000 invoice, charges VAT on the EUR 6,000 that follows, and opens VAT registers. Output VAT = EUR 3,300. He now recovers input VAT on costs from that point; this example leaves input VAT aside.
2. **Income tax.** The whole of 2026 moves to the regime ordinario. His professional income is EUR 111,000 received less EUR 12,000 costs = EUR 99,000. Less the EUR 14,000 INPS (TUIR art. 10) = EUR 85,000 taxable. Gross IRPEF at the 2026 bands (23% to EUR 28,000, 33% to EUR 50,000, 43% above) = EUR 28,750. His income is above EUR 50,000, so the self-employed detrazione in TUIR art. 13(5) is nil. Regional and municipal surcharges come on top (`it-income-tax`). As an individual he owes no IRAP (`it-irap`).
3. **Compared with staying in.** Had he stayed in the regime, the tax would have been (111,000 x 67% - 14,000) x 5% = EUR 3,018.50. Crossing EUR 100,000 costs him the start-up rate for the whole year, not only on the receipts above the limit.
4. **2027.** He is in the regime ordinario. His 2026 receipts are above EUR 85,000, so he cannot return in 2027. Whether he can return in 2028 depends on his 2027 receipts.

```oa-check
name: Forfettario start-up at 5% crossing EUR 100,000 mid-year (2026)
inputs:
  receipts_to_sept: 96000
  crossing_receipt: 9000
  later_receipts: 6000
  inps_paid: 14000
  actual_costs: 12000
  coefficient: 0.67
  startup_rate: 0.05
  vat_rate: 0.22
steps:
  - total_receipts: receipts_to_sept + crossing_receipt + later_receipts
  - crossed: total_receipts - 100000
  - vat_due: (crossing_receipt + later_receipts) * vat_rate
  - ordinary_taxable: total_receipts - actual_costs - inps_paid
  - band_23: min(ordinary_taxable, 28000) * 0.23
  - band_33: (min(ordinary_taxable, 50000) - 28000) * 0.33
  - band_43: max(ordinary_taxable - 50000, 0) * 0.43
  - gross_irpef: band_23 + band_33 + band_43
  - forfettario_tax_if_stayed: (total_receipts * coefficient - inps_paid) * startup_rate
expected:
  total_receipts: 111000
  vat_due: 3300
  ordinary_taxable: 85000
  gross_irpef: 28750
  forfettario_tax_if_stayed: 3018.50
```

IRPEF bands: TUIR art. 11(1) as amended by L. 199/2025 (https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-10-22). Detrazione: TUIR art. 13(5) (https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-10-22). The 22% VAT rate is the standard rate. Check the rate for the actual service in `italy-vat-return`.

## Ask the client first

1. What were your revenue or fees in 2025 (annualised if you started mid-year), all activities together, and how much have you received so far in 2026? (Entry test, the EUR 85,000 and EUR 100,000 limits.)
2. Which activities do you carry on, under which ATECO codes? (Coefficient group; several rows if the groups differ.)
3. Did you have a salary or pension in 2025, how much, and has that job ended? Is most of your work for a current or recent employer? (Exclusions d-bis and d-ter.)
4. Do you hold any stake in a partnership, professional association or family business, or control an S.r.l.? (Exclusion d.)
5. When did you start, and did you do any self-employed or business work in the three years before? Is this a continuation of a former job? (5% rate.)
6. Are you a business enrolled with INPS as artigiano or commerciante, and have you applied for the 35% cut? How much INPS did you actually pay in 2026? (Deduction and contributions.)

## Sources

| Source | URL | Read on |
|---|---|---|
| L. 190/2014, art. 1, commi 54-89, as in force 22 October 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-10-22 | 2026-10-22 |
| L. 190/2014, art. 1, as in force 2 January 2027 (commi 54-89 repealed by D.Lgs. 117/2026) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2027-01-02 | 2026-10-22 |
| L. 207/2024, art. 1, c. 12 (EUR 35,000 employment-income limit) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1 | 2026-10-22 |
| L. 199/2025, art. 1, c. 27 (extends the EUR 35,000 limit to 2026) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1 | 2026-10-22 |
| D.Lgs. 81/2025, art. 1 (ATECO 2007 coefficients continue) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2025-06-12;81~art1!vig=2026-10-22 | 2026-10-22 |
| D.Lgs. 117/2026, index (Capo XXI "Regime forfetario", from art. 232) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117 | 2026-10-22 |
| L. 145/2018 allegato 2 (coefficient table), Agenzia copy | https://www.agenziaentrate.gov.it/portale/documents/20143/241208/allegato+4.pdf/d69be7fc-b18a-3c73-bd2e-b0f3c1970218 | 2026-10-22 |
| Agenzia, Redditi PF 2026 instructions, Fascicolo 3 (Quadro LM), updated 13 May 2026 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026 | 2026-10-22 |
| Agenzia, Regime forfetario: Che cos'e (updated 21 July 2026) | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- | 2026-10-22 |
| Agenzia, Modalita di accesso al regime | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/modalita-di-accesso-al-regime | 2026-10-22 |
| Agenzia, Semplificazioni e adempimenti | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/semplificazioni-e-adempimenti | 2026-10-22 |
| Agenzia, Conseguenze della fuoriuscita | https://www.agenziaentrate.gov.it/portale/conseguenze-della-fuoriuscita | 2026-10-22 |
| Agenzia, Fattura elettronica per i forfettari | https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari | 2026-10-22 |
| Agenzia, stamp duty on e-invoices (June 2026) | https://www.agenziaentrate.gov.it/portale/documents/d/guest/l-imposta_di_bollo_sulle_fatture_elettronichegiugno2026 | 2026-10-22 |
| D.Lgs. 148/2026, art. 21 (removes the one-year cut to the assessment period from tax year 2026) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art21 | 2026-10-22 |
| D.L. 36/2022, art. 18 (e-invoicing for forfettari) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2022-04-30;36~art18!vig=2026-10-22 | 2026-10-22 |
| Agenzia, Come si paga l'Irpef (updated 12 March 2026) | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef | 2026-10-22 |
| D.P.R. 322/1998, art. 2 (filing dates) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art2!vig=2026-10-22 | 2026-10-22 |
| D.Lgs. 471/1997, art. 1 (return penalties) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-22 | 2026-10-22 |
| D.Lgs. 471/1997, art. 13 (late payment) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-22 | 2026-10-22 |
| TUIR, D.P.R. 917/1986, art. 11 (2026 IRPEF bands) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-10-22 | 2026-10-22 |
| TUIR, art. 13 (detrazioni) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-10-22 | 2026-10-22 |
| Agenzia, IRPEF rates (updated 13 January 2026; 2026 middle rate in its note) | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef | 2026-10-22 |

Not yet confirmed: (1) no Agenzia circular or FAQ read states in terms which employment-income year the EUR 35,000 limit tests; the reading above rests on the law text and the Fascicolo 3 instructions; (2) the text of D.Lgs. 117/2026 Capo XXI (Normattiva did not return the article text), so whether the 2027 regime keeps the same figures; (3) the 2027 filing and payment dates under the new consolidated codes; (4) the INPS artigiani and commercianti 2026 rates and minimum base (no official INPS page read); (5) whether the impatriati regime can be combined with the forfettario.
