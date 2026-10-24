---
name: pt-corporate-tax
description: "Portugal corporate income tax (IRC) for companies resident in mainland Portugal, tax year 2026. Covers the general rate (19% for tax periods starting in 2026, 18% in 2027, 17% from 2028, art. 87 CIRC), the 15% SME and Small Mid Cap rate on the first EUR 50,000, derrama estadual (3%, 5%, 9%, art. 87-A) and derrama municipal (up to 1.5%), autonomous taxation (art. 88), tax losses (no time limit, yearly cap, art. 52), payments on account (arts. 104 to 105-A), the Modelo 22 and the IES, the participation exemption, the interest limit, CFC rules, withholding by the company, and the SIFIDE II and RFAI credits. Trigger on: IRC Portugal, Modelo 22, derrama estadual, derrama municipal, tributação autónoma, pagamentos por conta, prejuízos fiscais, Portugal corporate tax, Portugal R&D credit. Out of scope: Azores, Madeira and the Madeira CINM regime; banks and insurers; investment funds; the simplified regime. Transfer pricing: pt-transfer-pricing. VAT: portugal-vat-return. Shareholders' IRS: pt-income-tax."
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-22
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal corporate income tax (IRC) for resident companies

Figures are for tax year 2026. This skill covers Portuguese corporate income tax (Imposto sobre o Rendimento das Pessoas Coletivas, IRC) for companies resident in mainland Portugal that carry on a commercial, industrial or agricultural activity as their main activity. It covers the IRC rates, the state and municipal surcharges (derrama estadual and derrama municipal), autonomous taxation (tributação autónoma), losses, payments on account, the Modelo 22 return and the IES, the participation exemption, the interest limit, CFC rules, withholding by the company, and the SIFIDE II and RFAI tax credits. Every rate and amount below comes from the consolidated codes on the Portal das Finanças, which print each article with its transitional notes, or from AT's Modelo 22 instructions. The IRC rate changes every year from 2026 to 2028, and the rate depends on the year in which the company's tax period STARTS, so read the first table with care.

## Section 1: Quick reference

| Field | Value |
| --- | --- |
| Country | Portugal (mainland). Azores and Madeira: see Section 3.3 |
| Tax | Imposto sobre o Rendimento das Pessoas Coletivas (IRC) |
| Currency | EUR |
| Tax period | The calendar year, unless the company adopts a different annual period that matches its accounting year (art. 8 CIRC) |
| Main law | Código do IRC (CIRC); 2026 State Budget Law 73-A/2025 of 30 December 2025; IRC rate law 64/2025 of 7 November 2025 |
| Other law | Código Fiscal do Investimento (CFI) for SIFIDE II and RFAI; Lei 73/2013 for derrama municipal; Lei 41/2024 for the global minimum tax |
| General IRC rate | See Section 3.1 |
| SME rate | See Section 3.2 |
| Derrama estadual | See Section 4.1 |
| Derrama municipal | See Section 4.2 |
| Autonomous taxation | See Section 5 |
| Annual return | Modelo 22, sent electronically through the Portal das Finanças |
| Modelo 22 deadline | Last day of May of the following year, working day or not (art. 120 CIRC) |
| IES deadline | 15 July of the following year, working day or not (art. 121 CIRC) |
| Payments on account | Three: July, September and 15 December of the year itself (art. 104 CIRC); amounts in Section 7 |
| Special payment on account (PEC) | Repealed for tax periods starting on or after 1 January 2022 (Section 8) |
| Tax losses | No time limit; yearly deduction capped (Section 9) |
| Tax authority | Autoridade Tributária e Aduaneira (AT) |

### 1.1 Conservative defaults

| Ambiguity | Default |
| --- | --- |
| SME status unknown | Apply the general rate to all taxable income until the SME or Small Mid Cap status under the annex to Decree-Law 372/2007 is confirmed |
| Start date of the tax period unknown | Ask. A period that started in 2025 uses the 2025 rate, not the 2026 rate |
| Municipality unknown | Apply the maximum derrama municipal rate in Section 4.2 until the municipality's rate is confirmed |
| Madeira or Azores company | Do not apply mainland rates or the Madeira CINM regime; refer (Section 3.3) |
| Car autonomous tax, acquisition cost unclear | Use the highest band in Section 5.1 |
| Tax loss in the period | Apply the loss uplift in Section 5.3 unless one of its exceptions is proved |
| SIFIDE II without the certifying declaration or proof it was requested | Apply no credit |
| RFAI region unclear | Apply no credit until the region is confirmed against the regional aid map |
| Participation exemption conditions unclear | Tax the dividend or gain normally |
| Ownership change of more than half the capital | Assume losses are lost until the art. 52(8) and (9) analysis is done |

## Section 2: Required inputs and refusal catalogue

### 2.1 Required inputs

- **Minimum.** Approved annual accounts (balance sheet and income statement); the prior-year Modelo 22 and IES; the SAF-T (PT) accounting file; confirmation of (i) SME or Small Mid Cap status, (ii) the municipality of the head office and of any permanent establishments, (iii) the start and end dates of the tax period, (iv) any Madeira or Azores operations, (v) whether the company is in a group taxed under RETGS.
- **Recommended.** Trial balance and general ledger; depreciation schedule; provisions and impairment schedule; tax losses by year of origin; withholding certificates; receipts for payments on account made in 2026; list of related parties and transactions; car register (plate, acquisition date, acquisition cost, fuel type, user).
- **Ideal.** Statutory audit report where required; transfer pricing documentation; the SIFIDE II certifying declaration; RFAI investment schedule by region; board minutes that record tax options (RETGS, a different tax period).
- **Hard stop.** Without approved accounts and the prior-year Modelo 22, no IRC computation is produced.

### 2.2 Refusal catalogue

- **R-PT-IRC-1: banks, financial institutions and insurers.** Special regimes apply (for example, the interest limit in art. 67 does not apply to entities supervised by the Banco de Portugal or the insurance supervisor). Out of scope; refer.
- **R-PT-IRC-2: oil, gas and extractive industries.** Sector regimes. Out of scope.
- **R-PT-IRC-3: collective investment undertakings and funds.** Own tax regime. Out of scope.
- **R-PT-IRC-4: non-profit entities and entities whose main activity is not commercial, industrial or agricultural.** Taxed on global income under art. 53 and art. 87(5) CIRC. Out of scope.
- **R-PT-IRC-5: non-residents.** A non-resident with no permanent establishment is taxed at the rates in Section 3.1 on Portuguese income, mostly by final withholding. A permanent establishment needs its own attribution analysis. Refer.
- **R-PT-IRC-6: RETGS (group taxation, arts. 69 to 71 CIRC).** The conditions are in Section 12.4. Group computations are not produced in this skill.
- **R-PT-IRC-7: inspections and disputes.** An open tax inspection, enforcement proceeding, administrative claim, court challenge or mutual agreement procedure: refer. Do not produce figures that could prejudice the position.
- **R-PT-IRC-8: reorganisations (mergers, divisions, asset contributions, share exchanges, arts. 73 and following CIRC).** Out of scope.
- **R-PT-IRC-9: payments to listed preferential tax regimes.** The autonomous tax in Section 5.2 applies unless the company proves the operations are real and normal. Partner review required.
- **R-PT-IRC-10: other skills.** VAT: `portugal-vat-return`. Shareholders' personal income tax: `pt-income-tax`. Payroll and employee withholding: `portugal-payroll`. Bookkeeping and SAF-T: `portugal-bookkeeping`. Annual accounts and IES content: `portugal-financial-statements`. Company formation: `portugal-formation`. Treaty relief on foreign income: `pt-foreign-source-treaties`. Final filing package: `pt-return-assembly`.

## Section 3: IRC rates

### 3.1 General rate: 19% for periods starting in 2026

Article 87(1) CIRC now prints a rate that applies only from 2028. The transitional rule printed under the article (art. 3 of Law 64/2025) sets a different rate for tax periods that start in 2026 and in 2027. For a calendar-year company, the 2026 tax year uses the 2026 row. A company whose tax period started in 2025 (for example, 1 July 2025 to 30 June 2026) uses the rate for 2025, which this skill does not state.

| Item | Rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| General rate, periods starting during 2026 (art. 87(1) and (5)) | 19% | "Nos períodos de tributação que se iniciem durante o ano de 2026, a taxa prevista nos n.os 1 e 5 do artigo 87.º do Código do IRC é de 19 %" |
| General rate, periods starting during 2027 | 18% | "Nos períodos de tributação que se iniciem durante o ano de 2027, a taxa prevista nos n.os 1 e 5 do artigo 87.º do Código do IRC é de 18 %" |
| Rate printed in art. 87(1), for periods starting on or after 1 January 2028 | 17% | "A taxa do IRC é de 17 %, exceto nos casos previstos" |
| SME and Small Mid Cap rate, first part of taxable income (art. 87(2)), periods starting on or after 1 January 2026 | 15% | "50 000 € de matéria coletável é de 15 %, aplicando-se a" |
| Band taxed at the SME rate | EUR 50,000 | "a taxa de IRC aplicável aos primeiros 50 000 € de matéria coletável" |
| Startup rate on the same band (art. 87(8)) | 12.5% | "a taxa de IRC prevista no n.º 2 é reduzida para 12,5 %" |
| Non-resident with no permanent establishment to which the income is attributable (art. 87(4)) | 25% | "aí não possuam estabelecimento estável ao qual os mesmos sejam imputáveis, a taxa do IRC é de 25%" |
| Non-resident: capital income of entities domiciled in a listed preferential tax regime, capital income paid to accounts for unidentified third parties, lottery and raffle prizes (art. 87(4)(d), (h), (i)) | 35% | "Ministro das Finanças, em que a taxa é de 35%" |

### 3.2 SME and Small Mid Cap rate

The SME rate in the table above applies only to a company that meets all of these conditions (art. 87(2) and (3) CIRC):

1. It carries on, directly and as its main activity, an economic activity of an agricultural, commercial or industrial nature. For the CIRC, every activity that consists of business economic operations, including the supply of services, counts as commercial, industrial or agricultural (art. 3(4) CIRC), so a services company meets this condition. [art. 3 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc3.aspx)
2. It qualifies as a small or medium-sized enterprise, or as a Small Mid Cap, under the annex to Decree-Law 372/2007 of 6 November. The size thresholds sit in that decree-law, which no allowed page prints; confirm them there, on a consolidated basis with partner and linked enterprises.
3. The reduced rate is State aid: it is subject to the EU de minimis rules (art. 87(3)).

The reduced rate is a band, not a cliff. Taxable income (matéria coletável) up to the band in the table above pays the SME rate; only the excess pays the general rate.

A company that qualifies as a startup under Law 21/2023 of 25 May and meets all the conditions of art. 2(1)(f) of that law pays the startup rate in the table above on the same band (art. 87(8)), also under the de minimis rules.

A transitional rule printed under art. 87 (art. 229 of Law 24-D/2022) keeps the SME rate for the two periods after a merger, division, asset contribution or share exchange carried out between 1 January 2023 and 31 December 2026, where every party qualified as an SME or Small Mid Cap and the receiving company stops qualifying because of the operation. [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx)

### 3.3 Azores, Madeira and the Madeira International Business Centre

The Azores and Madeira set their own regional IRC rates by regional law, and the Madeira International Business Centre (CINM, often called the Madeira IBC) has its own licensing, job and ceiling rules. No allowed page used for this skill prints the 2026 regional rates or the CINM rate and ceilings, so this skill states none. The live Guide's regional rates and CINM table were removed because no allowed page prints them. For a company with its head office, a permanent establishment or a CINM licence in either region: refer to a local accountant and the regional tax authority. For derrama municipal, Modelo 22 Annex A has a separate subtable for the Madeira Free Zone (art. 36-A(12) of the EBF). [Modelo 22 Annex A instructions](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF)

## Section 4: Derrama estadual and derrama municipal

Both surcharges are charged on TAXABLE PROFIT (lucro tributável), which is the profit before tax losses are deducted. IRC itself is charged on taxable income (matéria coletável), after losses. AT's own Annex A example shows a company with taxable profit of EUR 450,000 and taxable income of EUR 350,000 whose derrama is computed on the EUR 450,000. [Modelo 22 Annex A instructions](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF)

### 4.1 Derrama estadual (art. 87-A CIRC)

Who pays: residents whose main activity is commercial, industrial or agricultural, and non-residents with a permanent establishment in Portugal. It applies only to the part of taxable profit above the threshold in the table, by slices, so each rate applies only to the profit inside its slice. There is no lower band below the first rate shown. Under RETGS, each group company computes it on its own individual taxable profit, including the parent (art. 87-A(3)). It is self-assessed in the Modelo 22 (art. 87-A(4)).

| Slice of taxable profit | Rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx |
| Threshold: only profit above this is charged | EUR 1,500,000 | "Sobre a parte do lucro tributável superior a (euro) 1 500 000 sujeito e não isento" |
| Above EUR 1,500,000 up to EUR 7,500,000 | 3% | "uma, igual a (euro) 6 000 000, à qual se aplica a taxa de 3 %" |
| Above EUR 7,500,000 up to EUR 35,000,000 | 5% | "igual ao lucro tributável que exceda (euro) 7 500 000, à qual se aplica a taxa de 5%" |
| Above EUR 35,000,000 | 9% | "à qual se aplica a taxa de 9 %" |
| Size of the first slice | EUR 6,000,000 | "uma, igual a (euro) 6 000 000, à qual" |

### 4.2 Derrama municipal (art. 18 of Lei 73/2013)

Who pays: the same taxpayers as derrama estadual. Each municipality decides each year whether to levy it and at what rate, up to the maximum in the table, on taxable profit. A municipality may also set a reduced rate for small taxpayers by prior-year turnover, and may grant exemptions on its own conditions (for example, job creation or activity code).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF |
| Maximum municipal rate, on taxable profit | 1.5% | "A taxa pode variar até ao limite máximo de 1,5% do lucro tributável apurado no período." |
| Reduced municipal rate allowed for prior-year turnover not above | EUR 150,000 | "taxa reduzida de derrama municipal para os sujeitos passivos cujo volume de negócios no ano anterior não ultrapasse" |
| Annex A required when taxable income is above this AND the company has establishments in more than one municipality | EUR 50,000 | "Tenham matéria coletável no período superior a" |

The Annex A instructions above, which cite art. 18(24) of Lei 73/2013, say a turnover that does "não ultrapasse" (does not exceed) the amount, which includes a turnover exactly equal to it. AT's older help sheet for field 364 (worked examples for the 2016 period) says "inferior a" (below) in its summary, while the municipal rate rows it reproduces say "não ultrapasse":

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/Mod_22_Q_7_Campo_364_derrama_ajudas_preench.pdf |
| Reduced-rate turnover boundary, help sheet wording | EUR 150,000 | "volume de negócios no ano anterior inferior a 150 000,00 euros" |

Whether a municipality's reduced rate covers a turnover exactly at the amount depends on that municipality's own deliberation as published in the Ofício Circulado; where that wording is not available, refer the case. The help sheet also says that if the IES was not filed, AT does not know the turnover and applies the municipality's normal rate.

**Rates by municipality for 2026.** AT publishes each municipality's rates for a year's profits in an Ofício Circulado early in the following year. The list for 2024 profits is Ofício Circulado 20273 of 22 January 2025. No list for 2026 profits exists yet. The Annex A instructions also point to the Portal das Finanças path "Serviços → IRC → Modelo 22 e Derrama de IRC → Derrama IRC → Consultar taxas". Until the municipality's 2026 rate is confirmed, use the maximum rate. The live Guide's table of municipal rates (Lisboa, Porto, Cascais, Sintra and others) was removed: none of those rates is on an allowed page for 2026.

**Several municipalities.** When BOTH conditions in the Annex A table hold (taxable income above the amount shown AND establishments or local representations in more than one municipality), the company files Annex A and splits the derrama between municipalities by the ratio of payroll (massa salarial) in each. The result goes to field 364 of table 10 of the Modelo 22. [Modelo 22 Annex A instructions](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF)

## Section 5: Autonomous taxation (art. 88 CIRC)

Autonomous taxes are separate charges on certain expenses. They are due whether or not the company has taxable income, are self-assessed in the Modelo 22, and no deductions are allowed against the total, even under special laws (art. 88(23)). They do not apply to the expenses of a permanent establishment outside Portugal (art. 88(17)). Under the simplified regime, the rates in art. 88(7), (9), (11) and (13) do not apply (art. 88(16)).

### 5.1 Cars

The car rates apply only to taxpayers that are not subjectively exempt AND carry on a commercial, industrial or agricultural main activity. They apply to charges on light passenger cars, the light goods vehicles of art. 7(1)(b) of the Vehicle Tax Code, and motorcycles. Charges include depreciation, rents, insurance, maintenance, fuel and taxes on ownership or use (art. 88(5)). The band depends on the car's acquisition cost; the rate applies to the year's charges, not to the cost. Excluded: vehicles used in public transport or rented out in the normal course of business, and cars covered by an agreement taxed on the employee under art. 2(3)(b)(9) CIRS (art. 88(6)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Cars with acquisition cost below EUR 37,500 | 8% | "a) 8 % no caso de viaturas com um custo de aquisição inferior a 37 500 €;" |
| Cars costing EUR 37,500 or more and below EUR 45,000 | 25% | "b) 25 % no caso de viaturas com um custo de aquisição igual ou superior a 37 500 € e inferior a 45 000 €;" |
| Cars costing EUR 45,000 or more | 32% | "c) 32 % no caso de viaturas com um custo de aquisição igual ou superior a 45 000 €." |
| Qualifying plug-in hybrids and natural gas (GNV) cars, the same three bands | 2.5%, 7.5% and 15% | "são, respetivamente, de 2,5 %, 7,5 % e 15 %" |
| Fully electric vehicles, only where the acquisition cost exceeds the limit set by the ordinance under art. 34(1)(e) | 10% | "apenas são sujeitos a tributação, à taxa autónoma de 10 %," |

A plug-in hybrid qualifies for the reduced rates only if its battery charges from the grid, it has an electric range of at least 50 km, AND its official emissions are below 50 gCO2/km (or below 80 gCO2/km if type-approved under the Euro 6e-bis standard). This wording is from Law 73-A/2025. A fully electric vehicle costing no more than the ordinance limit bears no autonomous tax. The ordinance amount is not printed on an allowed page; confirm it before relying on it.

### 5.2 Other autonomous taxes

| Expense | Rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Undocumented expenses (also not deductible) | 50% | "As despesas não documentadas são tributadas autonomamente, à taxa de 50 %, sem prejuízo" |
| Undocumented expenses of wholly or partly exempt entities, entities without a commercial, industrial or agricultural main activity, or art. 7 entities | 70% | "é elevada para 70 % nos casos" |
| Representation expenses (receptions, meals, trips offered to clients, suppliers or others) | 10% | "São tributados autonomamente à taxa de 10 % os encargos efetuados ou suportados relativos a despesas de representação," |
| Payments to persons in a listed preferential tax regime, or to accounts there, unless the company proves they are real operations, not abnormal and not exaggerated: ordinary taxpayers | 35% | "sendo as taxas aplicáveis, respetivamente, 35 % ou 55 %, as" |
| The same payments by entities under art. 88(2) | 55% | "sendo as taxas aplicáveis, respetivamente, 35 % ou 55 %, as" |
| Per diem allowances and payments for an employee's own car, not invoiced to clients, except the part taxed in the employee's IRS | 5% | "São ainda tributados autonomamente, à taxa de 5 %, os" |
| Profits distributed to wholly or partly exempt IRC taxpayers where the shares were not held for one year without interruption before the distribution and are not kept to complete it | 23% | "São tributados autonomamente, à taxa de 23 %, os" |
| Manager termination payments not tied to pre-set productivity goals; and manager bonuses that are BOTH above the share of annual pay AND above the amount below | 35% | "São tributados autonomamente, à taxa de 35 %: a) Os gastos ou encargos relativos a indemnizações" |
| Manager bonus test: share of annual remuneration | 25% | "parcela superior a 25 % da remuneração anual e" |
| Manager bonus test: amount | EUR 27,500 | "possuam valor superior a (euro) 27 500, salvo se" |
| Bonus escape: deferred part of at least | 50% | "diferimento de uma parte não inferior a 50 % por um período mínimo de três anos" |

The manager bonus is NOT taxed if at least the deferred share in the table is deferred for at least three years AND payment is conditional on the company's positive performance over that period. If a condition later fails, the autonomous tax that should have been paid is added to the IRC of the period in which it fails (art. 88(21)).

### 5.3 Loss uplift and its 2026 exceptions

All autonomous tax rates in art. 88 rise by 10 percentage points for a taxpayer with a tax loss in the period, where the expenses relate to a commercial, industrial or agricultural activity not exempt from IRC (art. 88(14)). The uplift applies to every rate in the article, including the preferential-regime rates; the live Guide's statement that those rates are excluded was wrong.

The uplift does NOT apply in any of these cases:

1. The tax period in which the activity starts, and the next one (art. 88(15)).
2. For the 2026 tax period only (art. 95(5) of Law 73-A/2025, printed under the article), EITHER (a) the company had taxable profit in one of the three previous tax periods AND filed the Modelo 22 and the IES for the two previous periods on time, OR (b) 2026 is the period in which the activity starts or one of the two following periods.

Under RETGS, the group's tax loss under art. 70 is used for this test (art. 88(22)). [art. 88 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx)

## Section 6: Modelo 22 and IES

### 6.1 Modelo 22

The Modelo 22 is the annual self-assessment return (art. 117(1)(b) and art. 120 CIRC). It is sent electronically:

- calendar-year period: by the last day of May of the following year, whether or not that day is a working day (art. 120(1)). For the 2026 tax year: 31 May 2027;
- a different annual period: by the last day of the fifth month after the period ends (art. 120(2));
- cessation of activity: by the last day of the third month after cessation (art. 120(3));
- RETGS: the parent files the group return AND every group company files its own return as if the regime did not apply (art. 120(6)).

The IRC balance (total tax less payments on account) is paid by the last day for sending the Modelo 22 (art. 104(1)(b)). A refund is paid by the end of the third month after the return is sent, if it was sent on time and without errors (art. 104(3)). [art. 120 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc120.aspx) [art. 104 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx)

### 6.2 Annexes

Annex A (derrama municipal) is covered in Section 4.2. The derrama municipal total goes to field 364 of table 10. The live Guide's list of other annexes (B to H) and of the main tables was removed: it was not checked against an allowed page, and at least one line conflicted with the law (it placed related-party disclosure in a Modelo 22 annex, while art. 63(7) CIRC puts it in the IES). Use the annex list in the current official form and its instructions.

### 6.3 IES

The IES (declaração anual de informação contabilística e fiscal, art. 117(1)(c)) is sent electronically by 15 July of the following year, whether or not that day is a working day (art. 121(2)). For a different annual period: by the 15th day of the seventh month after the period ends (art. 121(3)). For the 2026 tax year of a calendar-year company: 15 July 2027. [art. 121 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121.aspx)

The IES must state whether the company had transactions with related parties in the period and, if so, identify them and the amounts, and declare whether transfer pricing documentation was prepared at the time and is kept (art. 63(7)). [art. 63 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc63.aspx)

## Section 7: Payments on account (arts. 104, 105 and 105-A CIRC)

Companies whose main activity is commercial, industrial or agricultural, and non-residents with a permanent establishment, pay three payments on account in July, September and 15 December of the year the profit relates to (for a different tax period: the seventh month, the ninth month and the 15th day of the twelfth month). The base is the IRC assessed for the PREVIOUS tax period, net of withholding (art. 105(1)). The percentage depends on the PREVIOUS period's turnover. Each payment is one third, rounded up to the euro.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105.aspx |
| Prior-period turnover up to and including this amount | EUR 500,000 | "seja igual ou inferior a (euro) 500 000" |
| Payments on account, prior-period turnover up to that amount | 80% | "correspondem a 80 % do montante do imposto" |
| Payments on account, prior-period turnover above that amount | 95% | "correspondem a 95 % do montante do imposto" |

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx |
| No payments on account when the reference period's IRC is below | EUR 200 | "dispensados de efetuar pagamentos por conta quando o imposto do período de tributação de referência" |
| No balance payment or refund when the amount is below | EUR 25 | "nem ao reembolso a que se refere o n.º 2 quando o seu montante for inferior a" |

Late payments on account start compensatory interest at once (art. 104(5)). A company may skip the third payment on account if, on the information it has, the payments already made are equal to or more than the tax that will be due for the period, or may limit the third payment to the difference (art. 107(1) and (3)). If the return then shows that this left unpaid more than the share in the table below of what a normal third payment would have been, compensatory interest runs from the due date of the third payment (art. 107(2)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc107.aspx |
| Shortfall from skipping or limiting the third payment above which compensatory interest is due | 20% | "deixou de ser paga uma importância superior a 20% da que, em condições normais, teria sido entregue" |

**Additional payment on account (art. 105-A).** A company that owed derrama estadual for the previous period also makes additional payments on account under art. 104-A, computed on the PREVIOUS period's taxable profit above the threshold, by slices. Under RETGS each group company pays its own, including the parent (art. 105-A(4)). The due dates in art. 104-A are not reproduced here.

| Slice of prior-period taxable profit | Rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105a.aspx |
| Above EUR 1,500,000 up to EUR 7,500,000 | 2.5% | "à qual se aplica a taxa de 2,5 %; outra, igual ao lucro tributável que exceda (euro) 7 500 000, à" |
| Above EUR 7,500,000 up to EUR 35,000,000 | 4.5% | "que exceda (euro) 7 500 000, à qual se aplica a taxa de 4,5 %;" |
| Above EUR 35,000,000 | 8.5% | "à qual se aplica a taxa de 8,5 %" |

## Section 8: Special payment on account (PEC): repealed

Article 106 CIRC (pagamento especial por conta) was repealed by Law 12/2022 of 27 June, with effect for tax periods starting on or after 1 January 2022. No company pays a PEC for 2026, whatever its size. The live Guide said the PEC still applied to large companies and gave its formula; that is wrong and has been removed. [art. 106 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc106.aspx)

## Section 9: Tax losses (art. 52 CIRC)

Tax losses are deducted from the taxable profit of one or more later tax periods, with NO time limit (art. 52(1), wording of Law 24-D/2022). This applies to deductions in tax periods starting on or after 1 January 2023, and also to losses from earlier periods whose deduction window was still open when that law entered into force (art. 228(1) of Law 24-D/2022). Losses of earlier periods covered by art. 6(1) of the REAID regime keep the deduction period in force on 31 December 2022 (art. 228(2)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx |
| Yearly cap on the deduction, as a share of that period's taxable profit | 65% | "não pode exceder o montante correspondente a 65 % do respetivo lucro tributável, não" |
| Change of ownership that ends the right to deduct: more than this share of share capital, or the majority of voting rights | 50% | "se verificou a alteração da titularidade de mais de 50 % do capital social ou" |
| Ownership-change exception: acquirer has held, without interruption since the start of the loss period, more than this share of capital or the majority of voting rights | 20% | "mais de 20 % do capital social ou da maioria dos direitos de voto" |

The cap is an allowance: the part not deducted carries forward on the same terms. There is no carry-back. Losses are not deductible in a period whose taxable profit is set by indirect methods, but they are not lost (art. 52(3)).

Losses are lost when, at the end of the period in which they are deducted, more than half of the share capital or the majority of the voting rights has changed hands since the loss period, UNLESS the operation did not have tax evasion as its main purpose or one of its main purposes (which can be shown by valid economic reasons) (art. 52(8)). Art. 52(9) excludes these changes: direct to indirect holding or the reverse, and transfers between companies under common majority control; operations under the reorganisation regime of arts. 73 and following; succession on death; an acquirer that has held more than the share in the table since the start of the loss period; and an acquirer who has been an employee or board member since the start of the loss period. The live Guide said the right could be kept with AT authorisation; the current text has no authorisation procedure.

## Section 10: SIFIDE II (R&D tax credit, arts. 35 to 42 CFI)

SIFIDE II runs for tax periods from 2014 to 2026 (art. 35 CFI, wording of Decree-Law 170/2026). It is available to resident IRC taxpayers whose main activity is agricultural, industrial, commercial or services, and to non-residents with a permanent establishment. The credit is deducted from the IRC assessed, up to that amount, for R&D expenses incurred in tax periods starting between 1 January 2014 and 31 December 2026, to the extent not covered by non-repayable State funding.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-38.aspx |
| Base rate, on the period's eligible R&D expenses | 32.5% | "Taxa de base - 32,5 % das despesas realizadas naquele período" |
| Incremental rate, on the increase over the simple average of the two previous years | 50% | "Taxa incremental - 50 % do acréscimo das despesas realizadas naquele período" |
| Cap on the incremental part | EUR 1,500,000 | "até ao limite de (euro) 1 500 000,00" |
| Uplift to the base rate for micro, small and medium enterprises that have not yet completed two financial years and have not used the incremental rate | 15% | "aplica-se uma majoração de 15 % à taxa base" |

Rules (arts. 38 to 40 CFI):

- An unused credit, for lack of tax, carries forward to the twelfth following period (art. 38(4)). The live Guide said eight periods.
- Only companies whose taxable profit is not set by indirect methods AND that owe no tax or social security contributions (or have payment secured) may claim (art. 39).
- The claim needs a certifying declaration issued by the Agência para a Investigação e Inovação, E. P. E., or proof that it was requested, kept in the tax documentation file (art. 40(1)). The live Guide said the credit could not be used before the declaration is issued; the law also accepts proof of the request.
- Applications are due by the end of the fifth month of the year after the financial year; applications for earlier years are not accepted (art. 40(3)).
- No credit for R&D financed directly or indirectly by SIFIDE II investment funds or other public support (art. 38(10)).

The page shows the article amended by "Decreto-Lei n.º 170/2026" in the text and "Decreto-Lei n.º 171/2026" in the amendment list. Confirm the decree-law number before citing it.

## Section 11: RFAI (investment tax credit, arts. 22 to 26 CFI)

RFAI applies to IRC taxpayers in the sectors listed in art. 2(2) CFI, except activities excluded under the EU regional aid rules (art. 22(1)). Eligible investments are new tangible fixed assets used in the business (excluding, among others, land, most buildings, light passenger or mixed cars, furniture, social equipment), certain technology-transfer intangibles, and the salary costs of new jobs for staff with qualifications at level 7 or 8 of the national framework (art. 22(2), added by Law 82/2023). For a company that is not a micro, small or medium enterprise, the intangibles and salary costs are limited to a share of the eligible investment set in art. 22(3); and in art. 107(3)(c) regions it may claim RFAI only for investment in a new economic activity, meaning a new establishment or the diversification of an existing one, on the conditions in art. 22(7).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-23.aspx |
| Regions eligible under art. 107(3)(a) of the Treaty on the Functioning of the EU: credit on investment up to EUR 15,000,000 | 30% | "i) 30 % das aplicações relevantes, relativamente ao investimento realizado até ao montante de 15 000 000 (euro)" |
| Same regions: credit on investment above EUR 15,000,000 | 10% | "ii) 10 % das aplicações relevantes, relativamente à parte do investimento realizado que exceda o montante" |
| Regions eligible under art. 107(3)(c): credit on all eligible investment | 10% | "constantes da tabela prevista no n.º 1 do artigo 43.º, 10 % das aplicações relevantes" |
| Yearly cap outside the start-up years, as a share of IRC assessed | 50% | "até à concorrência de 50 % da coleta do IRC apurada em cada período de tributação" |

Rules:

- Which regions fall under art. 107(3)(a) or (c) is set by the regional aid map table in art. 43 CFI, which this skill does not reproduce. The live Guide's list of regions (Norte, Centro, Alentejo, Madeira, Azores; Algarve; Lisbon) was not on an allowed page and was removed.
- Investments in the start-up period and the next two periods (unless the company results from a division) can use the credit up to the full IRC of each period; otherwise up to the cap in the table (art. 23(2)).
- Unused credit carries forward to the next 10 tax periods, under the same caps (art. 23(3)).
- The total aid must stay within the regional aid ceiling for the region, counting all State aid to the investment (art. 23(5) and (6)).
- The assets must be kept in the company and the region for at least three years from the investment for micro, small and medium enterprises, or five years otherwise, and the investment must create jobs that are kept for the same period (art. 22(4)). [art. 22 CFI](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-22.aspx)

## Section 12: Holding companies and the participation exemption

### 12.1 Dividends received (art. 51 CIRC)

Profits and reserves distributed to an IRC taxpayer with its head office or effective management in Portugal are excluded from its taxable profit only if ALL of these conditions hold:

| Condition | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc51.aspx |
| (a) Direct, or direct and indirect, holding of at least this share of capital OR voting rights | 10% | "uma participação não inferior a 10 % do capital social ou dos direitos de voto" |
| (d) Payer's statutory tax rate at least this share of the art. 87(1) IRC rate | 60% | "não seja inferior a 60 % da taxa do IRC prevista no n.º 1 do artigo 87.º; e) A" |

1. (a) the holding in the table above;
2. (b) held without interruption for one year before the distribution or, if held for less, kept until one year is completed;
3. (c) the recipient is not under the tax transparency regime of art. 6;
4. (d) the payer is subject to and not exempt from IRC, a tax listed in art. 2 of Directive 2011/96/EU, or a tax similar to IRC, at a statutory rate not below the share in the table. This test is waived where the conditions of art. 66(7) are met (art. 51(2));
5. (e) the payer is not resident in a listed preferential tax regime.

The exemption does not apply to distributions that are deductible for the payer (art. 51(10)(a)) or under a non-genuine arrangement whose main purpose is a tax advantage (art. 51(13) and (14)). Where the conditions fail, a foreign tax credit under arts. 91 and 91-A may still apply (art. 51(9)).

For a tax period that starts in 2026, the transitional rule printed under art. 87 says that the rate in art. 87(1) "é de 19 %" (Section 3.1). Read literally, the rate that art. 51(1)(d) refers to is therefore the 2026 row in Section 3.1, not the rate printed in the article. No AT page read for this skill confirms that reading. A payer whose statutory rate is at least the share in the table of the 2026 rate passes on either reading. A payer that passes only when measured against the printed art. 87(1) rate is unsettled: refer. [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx)

### 12.2 Capital gains on shares (art. 51-C CIRC)

Gains and losses on the sale of shares held without interruption for at least one year are excluded from taxable profit, whatever percentage is sold, if at the date of sale conditions (a), (c) and (e) of art. 51(1) are met, AND condition (d) or art. 51(2). The exclusion covers gains AND losses: a loss on qualifying shares is not deductible. Other equity instruments linked to the shares, such as supplementary capital contributions, are covered too (art. 51-C(2)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc51c.aspx |
| No exclusion when Portuguese real estate (other than property used in an agricultural, industrial or commercial activity other than buying and selling property) is, directly or indirectly, more than this share of the assets | 50% | "represente, direta ou indiretamente, mais de 50 % do ativo." |

Impairment losses on the shares that reduced taxable profit in earlier years are added back in the year of sale when the exclusion applies (art. 51-C(6)).

### 12.3 Interest limit (art. 67 CIRC)

Net financing expenses are deductible up to the HIGHER of the two limits in the table. Non-deductible expenses carry forward to the next five tax periods; unused capacity under the EBITDA limit carries forward to the fifth later period. The fixed limit is pro-rated for a period shorter than a year (art. 67(10)). Banks and insurers are excluded (art. 67(11)). Carry-forwards are lost on a change of more than half the capital or voting rights, with the same exceptions as for losses (art. 67(8)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc67.aspx |
| Fixed limit | EUR 1,000,000 | "a) (euro) 1 000 000; ou b) 30 % do" |
| EBITDA limit: share of profit before depreciation, amortisation, net financing expenses and taxes | 30% | "b) 30 % do resultado antes de depreciações, amortizações, gastos de financiamento líquidos e impostos" |

### 12.4 Group taxation (RETGS, art. 69 CIRC): conditions only

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc69.aspx |
| Parent's direct or indirect holding in each subsidiary, which must also give more than half of the voting rights | 75% | "pelo menos, 75 % do capital de outra ou outras sociedades ditas dominadas," |

The option also requires, among others, that all group companies have their head office and effective management in Portugal and all their income is taxed under the general regime at the highest normal rate, that the parent has held each holding for more than one year when the regime starts, and that the parent is not itself controlled by another resident company that could be a parent (art. 69(3)). Group computations are out of scope (R-PT-IRC-6).

## Section 13: Global minimum tax (Pillar Two)

Portugal's global minimum tax regime (Regime do Imposto Mínimo Global, RIMG) was approved by Law 41/2024 of 8 November, which transposes Directive (EU) 2022/2523. The live Guide named "Lei 27/2024" and that is not the law AT lists. AT publishes the Modelo 62 registration return (Ordinance 290/2025/1 of 2 September) and the Modelo 63 GloBE information return. This skill does not state the scope threshold, the minimum rate or the filing deadlines, because the saved AT pages do not print them. A group that may be in scope: refer to a specialist. [AT Pillar Two legislation page](https://info.portaldasfinancas.gov.pt/pt/Grandes_Contribuintes/Pilar_2/Legislacao_e_regulamentacao_nacional/Paginas/Regime_imposto_minimo_global.aspx)

## Section 14: Transfer pricing (art. 63 CIRC)

Transactions between a taxpayer and any entity with which it has special relations must be agreed and carried out on terms substantially the same as independent entities would agree in comparable transactions (art. 63(1)). The taxpayer must keep transfer pricing documentation in the tax documentation file of art. 130 (art. 63(6)), and must disclose related-party transactions in the IES (art. 63(7), Section 6.3). The methods and documentation rules are set by ordinance (art. 63(15)). The live Guide's revenue thresholds for the master file and local file and for country-by-country reporting were not on an allowed page and were removed. The country-by-country return is a separate filing under art. 117(1)(d) and art. 121-A. [art. 63 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc63.aspx)

## Section 15: Controlled foreign companies (art. 66 CIRC)

Profits of a non-resident entity under a clearly more favourable tax regime are attributed to a resident IRC taxpayer that holds, directly or indirectly (including through a nominee), at least the share in the table of the capital, the voting rights or the rights to income or assets. Holdings of related parties under art. 63(4)(a) to (e) are added together (art. 66(13)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc66.aspx |
| Holding that triggers attribution | 25% | "pelo menos 25% das partes de capital, dos direitos de voto ou dos direitos sobre os rendimentos" |
| More favourable regime: profit tax actually paid is below this share of the tax due under the CIRC | 50% | "O imposto sobre os lucros efetivamente pago seja inferior a 50 % do imposto que seria devido nos termos deste Código" |
| Exclusion: passive income (royalties, dividends and share gains, leasing, intra-group financial and insurance income, low-value invoicing, interest) is no more than this share of total income | 25% | "não exceda 25 % do total dos seus rendimentos" |

A regime is clearly more favourable if the territory is on the ministerial list OR the tax-paid test in the table is met (art. 66(6)). The rule does not apply to an entity resident in the EU, or in an EEA state with equivalent administrative cooperation, if the taxpayer shows valid economic reasons AND a real activity with staff, equipment, assets and premises (art. 66(14)). The live Guide's alternative "10% holding" condition is not in the article and was removed.

## Section 16: Withholding by the company

### 16.1 IRC withholding (art. 94 CIRC)

IRC is withheld on the income listed in art. 94(1) obtained in Portugal, including intellectual property and know-how income, equipment rental, capital income and rental income where the payer is an IRC taxpayer or keeps organised accounts, and board members' fees. For a resident recipient, withholding is a payment on account of its final IRC (art. 94(3)). For a non-resident without a permanent establishment (except rental income) it is final, at the art. 87 rates in Section 3.1 (art. 94(3)(b) and (5)). Amounts withheld are paid to the State by the 20th day of the month after the deduction (art. 94(6)).

| Item | Rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc94.aspx |
| IRC withholding, general rate | 25% | "As retenções na fonte de IRC são efetuadas à taxa de 25 %," |
| IRC withholding on fees of members of statutory bodies (art. 94(1)(d)) | 21.5% | "aplicando-se aos rendimentos referidos na alínea d) do n.º 1 a taxa de 21,5 %." |

Treaty or directive relief at source requires the recipient to prove the conditions to the payer by the deadline for paying over the tax that would have been withheld (art. 98(2)). [art. 98 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc98.aspx)

### 16.2 IRS withholding on payments to individuals (art. 71 CIRS)

| Item | Rate | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx |
| Final (liberatória) IRS withholding on capital income, such as dividends and interest (art. 71(1)) | 28% | "à taxa liberatória de 28 %: a) Os" |
| Final IRS withholding at the higher rate (art. 71(17)), for example capital income paid to entities in listed preferential regimes or to accounts for unidentified holders | 35% | "à taxa liberatória de 35 %: (Anterior" |

For the shareholder's own tax position, use `pt-income-tax`.

### 16.3 Dividends paid to EU, EEA and treaty-country parents (art. 14(3) CIRC)

Dividends a resident company pays are exempt from IRC (and so from withholding) where the parent: (a) is resident in another EU state, in an EEA state with equivalent administrative cooperation, or in a treaty state whose treaty provides for exchange of information; (b) is subject to and not exempt from a tax listed in art. 2 of Directive 2011/96/EU or a similar tax, and, for a treaty-state parent only, at a statutory rate not below the share in the table; (c) holds at least the share in the table of capital or voting rights; AND (d) has held it without interruption for the year before the payment. Proof must be given to the payer BEFORE the payment date; for (a) and (b), by a declaration confirmed by the parent's tax authority (art. 14(4)). The exemption does not apply where an arrangement, or series of arrangements, with the main purpose or one of the main purposes of obtaining a tax advantage is not genuine; an arrangement is not genuine to the extent it is not made for valid economic reasons and does not reflect economic substance (art. 14(17) and (18)).

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc14.aspx |
| Parent's minimum holding | 10% | "uma participação não inferior a 10 % do capital" |
| Treaty-state parent: minimum statutory rate, as a share of the art. 87(1) IRC rate | 60% | "a taxa legal aplicável à entidade não seja inferior a 60 % da taxa do" |

The test in condition (b) refers to the same art. 87(1) rate; the transitional point in Section 12.1 applies to it in the same way.

The live Guide's rule for interest and royalties under Directive 2003/49/EC (holding and period) was not checked on an allowed page and was removed.

## Section 17: Worked examples (hypothetical)

All amounts in these examples are invented. The rates come from the tables above. Arithmetic is shown so it can be checked. Autonomous taxes, tax credits and withholding are left out unless stated.

### 17.1 SME in mainland Portugal: IRC and derrama municipal

Facts (hypothetical): a private limited company (Lda) qualifies as an SME, carries on a commercial main activity, has a calendar tax period, head office in one mainland municipality only, no tax losses and no establishments elsewhere. Its taxable profit for 2026 is EUR 130,000, so its taxable income is also EUR 130,000. The municipality's 2026 rate is not yet known, so the maximum rate is used. [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx)

1. IRC on the first EUR 50,000 at 15%: EUR 7,500. [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx)
2. IRC on the remaining EUR 80,000 at 19%: EUR 15,200. [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx)
3. IRC: EUR 7,500 plus EUR 15,200 = EUR 22,700. [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx)
4. Derrama estadual: taxable profit is not above EUR 1,500,000, so none is due. [art. 87-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx)
5. Derrama municipal at the maximum 1.5% of taxable profit: EUR 130,000 times 1.5% = EUR 1,950. Annex A is not needed because there is only one municipality. [Modelo 22 Annex A instructions](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF)
6. IRC plus derrama municipal: EUR 24,650, before autonomous taxes, credits, withholding and the payments on account made in 2026. [art. 104 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx)

The live Guide's version of this example applied the old general rate and the old SME rate to the same facts.

### 17.2 Tax losses: the yearly cap

Facts (hypothetical): calendar 2026, taxable profit EUR 100,000, tax losses brought forward EUR 80,000, no ownership change. [art. 52 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx)

1. Cap: 65% of EUR 100,000 = EUR 65,000. [art. 52 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx)
2. Losses deducted in 2026: the lower of EUR 80,000 and EUR 65,000 = EUR 65,000. [art. 52 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx)
3. Taxable income for IRC: EUR 100,000 minus EUR 65,000 = EUR 35,000. [art. 52 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx)
4. Losses carried forward, with no time limit: EUR 80,000 minus EUR 65,000 = EUR 15,000. [art. 52 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx)
5. Derrama municipal is still computed on the taxable profit of EUR 100,000, not on the EUR 35,000. [Modelo 22 Annex A instructions](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF)

### 17.3 Derrama estadual by slices

Facts (hypothetical): calendar 2026, taxable profit EUR 10,000,000, single company, not in a group. [art. 87-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx)

1. Profit above EUR 1,500,000 is above EUR 7,500,000 and not above EUR 35,000,000, so it splits into two slices. [art. 87-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx)
2. First slice: EUR 6,000,000 times 3% = EUR 180,000. [art. 87-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx)
3. Second slice: EUR 10,000,000 minus EUR 7,500,000 = EUR 2,500,000, times 5% = EUR 125,000. [art. 87-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx)
4. Derrama estadual: EUR 305,000. Because it was due for 2026, the company also makes additional payments on account in 2027 (Section 7). [art. 105-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105a.aspx)

## Section 18: Conservative defaults (summary)

| Item | Default |
| --- | --- |
| IRC rate | Check the start date of the tax period first; then the general rate for that year (Section 3.1) |
| SME status | Not an SME until confirmed under the annex to Decree-Law 372/2007, consolidated with partner and linked enterprises |
| Municipality | Maximum derrama municipal rate until the 2026 rate is confirmed |
| Madeira, Azores, CINM | Refer; no mainland rates |
| Autonomous tax in a loss year | Apply the uplift unless an exception in Section 5.3 is proved |
| Cars | Highest band when the acquisition cost is unclear |
| Losses | Apply the yearly cap; check ownership changes |
| PEC | None: repealed |
| SIFIDE II | No credit without the declaration or proof it was requested |
| RFAI | No credit until the region and its aid ceiling are confirmed |
| Participation exemption | Confirm every condition; otherwise tax normally |
| Pillar Two | Refer if the group may be in scope |
| Payments on account | Use the prior period's turnover to pick the percentage |
| Filing | Modelo 22 by the last day of May; IES by 15 July; both whether or not a working day |

## The method, step by step

1. Fix the tax period and its start date (art. 8 CIRC), then pick the general rate for that start year from the transitional rule under [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx).
2. Start from the accounting result in the approved accounts and make the tax adjustments to reach taxable profit (lucro tributável), including the participation exemption in [art. 51 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc51.aspx) and [art. 51-C CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc51c.aspx), the interest limit in [art. 67 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc67.aspx) and any CFC attribution under [art. 66 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc66.aspx).
3. Deduct tax losses up to the yearly cap to reach taxable income (matéria coletável), checking ownership changes, under [art. 52 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx).
4. Apply the IRC rate: the SME or startup band if every condition holds, the general rate on the rest, under [art. 87 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx).
5. Compute derrama estadual on taxable profit by slices under [art. 87-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx), and derrama municipal on taxable profit at the municipality's rate, with Annex A where required, under the [Modelo 22 Annex A instructions](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF).
6. Compute autonomous taxes on the year's charges, then check the loss uplift and its 2026 exceptions, under [art. 88 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx).
7. Deduct tax credits from the IRC within their caps: SIFIDE II under [art. 38 CFI](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-38.aspx), RFAI under [art. 23 CFI](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-23.aspx).
8. Deduct withholding suffered and the payments on account made in the year, and work out the balance or refund under [art. 104 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx).
9. File the Modelo 22 by the last day of May under [art. 120 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc120.aspx) and the IES by 15 July under [art. 121 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121.aspx).
10. Set next year's payments on account from this year's IRC and turnover under [art. 105 CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105.aspx), and the additional payments on account if derrama estadual was due, under [art. 105-A CIRC](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105a.aspx).

## Ask the client first

- When did your current tax period start, and does it follow the calendar year? (This decides the IRC rate.)
- Does the company qualify as an SME or Small Mid Cap under Decree-Law 372/2007 on a consolidated basis, is its main activity commercial, industrial or agricultural, and is it a certified startup under Law 21/2023?
- In which municipalities does the company have its head office or establishments, and what was last year's turnover? (Derrama municipal rate, reduced rate and Annex A.)
- Did the company make a tax loss this year, did it make taxable profit in any of the last three years, and were the Modelo 22 and IES for the last two years filed on time? (Autonomous tax uplift.)
- Has more than half of the share capital or voting rights changed hands since any year with unused losses?
- Does the company have operations, a licence or establishments in Madeira or the Azores, or belong to a group that may be in scope of the global minimum tax?

## When to refuse or refer

- Banks, insurers, funds, extractive industries, non-profits and entities whose main activity is not commercial, industrial or agricultural (R-PT-IRC-1 to R-PT-IRC-4).
- Companies in Madeira or the Azores, or with a CINM licence (Section 3.3).
- RETGS group computations, reorganisations and permanent establishments of non-residents (R-PT-IRC-5, R-PT-IRC-6, R-PT-IRC-8).
- Groups that may be in scope of the global minimum tax (Section 13).
- Transfer pricing documentation, CFC attribution with foreign tax credit, and payments to listed preferential regimes, unless a partner reviews the work.
- Open inspections, claims, court cases or mutual agreement procedures (R-PT-IRC-7).
- A tax period that started before 1 January 2026: this skill does not state the 2025 rates.
- A prior-year turnover exactly at the derrama municipal reduced-rate boundary (Section 4.2).
- Never present figures as final: every output is an estimate for review by a certified accountant (Contabilista Certificado) before filing.

## Prohibitions

- Never apply the rate printed in art. 87(1) to a 2026 or 2027 period: use the transitional rule.
- Never apply the SME rate without confirming every condition in Section 3.2, including the de minimis limit.
- Never apply a mainland rate or a CINM rate to a Madeira or Azores company without regional advice.
- Never charge derrama estadual on profit at or below its threshold, and never apply a slice rate to the whole profit.
- Never compute derrama estadual or derrama municipal on taxable income after losses: both use taxable profit.
- Never assume a derrama municipal rate of zero without the municipality's rate for the year.
- Never forget the loss uplift on autonomous taxes, and never apply it without checking its exceptions for 2026.
- Never deduct losses above the yearly cap, and never treat losses as expiring after a fixed number of years.
- Never compute a PEC: it is repealed.
- Never claim SIFIDE II without the certifying declaration or proof it was requested.
- Never apply the participation exemption if the payer is in a listed preferential regime.
- Never apply the outbound dividend exemption without the proof required before the payment date.

## Sources

- Código do IRC, consolidated, Portal das Finanças: [art. 3](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc3.aspx), [art. 8](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc8.aspx), [art. 14](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc14.aspx), [art. 51](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc51.aspx), [art. 51-C](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc51c.aspx), [art. 52](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx), [art. 63](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc63.aspx), [art. 66](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc66.aspx), [art. 67](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc67.aspx), [art. 69](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc69.aspx), [art. 87](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx), [art. 87-A](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx), [art. 88](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx), [art. 94](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc94.aspx), [art. 98](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc98.aspx), [art. 104](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx), [art. 105](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105.aspx), [art. 105-A](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105a.aspx), [art. 106](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc106.aspx), [art. 107](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc107.aspx), [art. 117](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc117.aspx), [art. 120](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc120.aspx), [art. 121](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121.aspx).
- Código do IRS, art. 71: [art. 71 CIRS](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx).
- Código Fiscal do Investimento: [art. 22](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-22.aspx), [art. 23](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-23.aspx), [art. 35](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-35.aspx), [art. 38](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-38.aspx), [art. 39](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-39.aspx), [art. 40](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-40.aspx).
- AT, [Modelo 22 Annex A instructions](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF) and [field 364 help sheet](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/Mod_22_Q_7_Campo_364_derrama_ajudas_preench.pdf).
- AT, [global minimum tax legislation page](https://info.portaldasfinancas.gov.pt/pt/Grandes_Contribuintes/Pilar_2/Legislacao_e_regulamentacao_nacional/Paginas/Regime_imposto_minimo_global.aspx).

## Disclaimer

This skill and its outputs are for information and computation only and are not tax, legal or financial advice. Every output must be reviewed and confirmed by a certified accountant registered with the Ordem dos Contabilistas Certificados, or by a statutory auditor registered with the Ordem dos Revisores Oficiais de Contas, before anything is filed with the Autoridade Tributária e Aduaneira or acted on. The current version of this skill is kept at openaccountants.com.

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
