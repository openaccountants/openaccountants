---
name: panama-income-tax
description: Use this skill whenever asked about Panama personal income tax (ISR — Impuesto sobre la Renta) for individuals, self-employed persons, or payroll. Trigger on phrases like "how much income tax do I pay in Panama", "Panama ISR", "declaración jurada de rentas", "income tax return Panama", "allowable deductions Panama", "CSS contributions", "Caja de Seguro Social", "seguro educativo", "territorial taxation", "Panama-source income", "self-employed CSS Law 462", "décimo tercer mes", "estimated tax instalments", "DGI filing", "non-resident withholding Panama", or any question about filing or computing personal income tax or social security for an individual or self-employed client in Panama. Also trigger when classifying a Panamanian bank statement, computing CSS/educational-insurance payroll deductions, or advising on the 15 March filing deadline. This skill covers the progressive ISR brackets, personal deductions, CSS + educational insurance under Law 462 of 2025, filing deadlines, estimated tax, penalties, minimum wage, and the territorial source rule. ALWAYS read this skill before touching any Panama income tax work.
version: 0.1
jurisdiction: PA
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Panama income tax (ISR): individuals, the self-employed, payroll, and the company rules they meet

Tax year 2026. Panama's tax year is the calendar year, so "2026" means income earned from 1 January to 31 December 2026, reported on the return due by 15 March 2027 (individuals) or 31 March 2027 (companies). The rules below are as published by the Dirección General de Ingresos (DGI) on dgi.mef.gob.pa, read on 25 September 2026. The DGI tax table has not changed since 2010, so the 2026 figures are the same as 2025. A short dated section covers the 2025 returns filed in 2026.

Amounts are in balboas (B/.), which trade at par with the US dollar; this Guide writes them as USD.

## Scope and who this is for ([DGI, rates](https://dgi.mef.gob.pa/DInforme/Tarifa.php); [DGI, income tax FAQ](https://dgi.mef.gob.pa/Preguntas/Rent.php))

This Guide covers Panama's income tax (Impuesto sobre la Renta, ISR) for:

- Individuals (personas naturales): employees, independent professionals and traders (comerciantes), resident or not, on Panama-source income.
- Employers withholding ISR from salaries.
- At summary level, the company rules an individual client meets: the 25% corporate rate, the alternative minimum calculation (CAIR), dividend tax, the Aviso de Operación tax, and withholding on payments abroad.

It does not cover ITBMS (the goods and services tax), capital gains on real estate or securities, the special regimes (City of Knowledge, SEM, Colón Free Zone, Panamá Pacífico and other free zones), banking and insurance levies, or CSS social security rates. Those are referred.

**The territorial rule.** Panama taxes only income from activities carried out in Panamanian territory, whoever earns it. DGI: the person who must pay is the taxpayer "que reciba ingresos por actividades realizadas en el territorio panameño, independientemente de la nacionalidad, domicilio o residencia del beneficiario" ([DGI FAQ, question 4](https://dgi.mef.gob.pa/Preguntas/Rent.php)). Residence does not widen the base, and non-residents are taxed on Panama-source income, mostly by withholding.

Foreign-source income is still reported on the return, on its own line, "de acuerdo al parágrafo 2 del Artículo 694 del Código Fiscal" ([DGI return instructions, line 19](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf)). It is left out of taxable income, and the costs and expenses of earning it are not deductible ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).

**The offshore services rules: check.** Article 694 parágrafo 2 of the Código Fiscal is generally described as treating three activities run from an office in Panama as not Panama-source: invoicing from Panama for sales of goods or services where the transaction is completed abroad; directing from Panama transactions that are completed and have effect abroad; and distributing dividends out of income that is itself foreign-source. DGI does not publish the text of that paragraph, and the Gaceta Oficial that carries it is not an allowed source for this Guide. Read article 694 in the official Código Fiscal before relying on any of the three cases, and treat mixed contracts (part of the work done in Panama) as a referral.

## Ask the client first

- **Where was each piece of work done, or where is each asset?** Work physically done in Panama, or a Panama property rented out, is Panama-source. Work done wholly abroad for a foreign client is not. Ask this for every income stream before anything else ([DGI FAQ, question 4](https://dgi.mef.gob.pa/Preguntas/Rent.php)).
- **What kind of taxpayer?** A salaried employee with one employer, an employee with more than one employer, an independent professional, a trader, or the owner of a company? The answer decides whether a return is needed and which form (Form 2V for individuals with business or professional income, Form 1V8 for pure salary, Form 1V for companies) ([DGI, returns and due dates](https://dgi.mef.gob.pa/DInforme/Tab-Decla.php)).
- **Filing jointly with a spouse?** The basic deduction of USD 800 is only for spouses who file a joint return ([DGI return instructions, line 86](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf)).
- **Gross and net income for the year.** Income above USD 11,000 means the return must be countersigned by a Panamanian CPA ([DGI FAQ, question 45](https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php)). An independent with net taxable income of USD 1,000 or less and gross income not over USD 3,000 need not file ([DGI, article 710](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php)).
- **Deductions with paperwork:** medical costs in Panama, mortgage interest on the home in Panama (and whether the loan has a preferential rate), school costs for each dependant and any scholarship, pension fund payments, and donations to approved institutions. Only documented deductions count.
- **Tax already paid:** salary withholding (the employer's annual certificate), the three estimated-tax instalments paid in 2026, and any credit carried from the 2025 return.
- **Does the client own a company or run a business?** Ask about the Aviso de Operación, dividends paid in the year, and payments to people abroad.

## The method, step by step

1. **Sort every receipt by source.** Panama-source (taxable), foreign-source (reported, not taxed), exempt (for example interest on Panamanian bank deposits and on government securities, listed in article 708 of the Código Fiscal as quoted by [DGI, Form 07](https://dgi.mef.gob.pa/DInforme/Formulario07.php)). If the source of a stream is unclear, stop and refer.
2. **Decide whether a return is needed.** Check the exemptions in "Filing and payment". A single-employer employee whose tax was fully withheld need not file, but may file to claim deductions such as school costs ([DGI FAQ, question 53](https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php)).
3. **Gross income.** Salaries (including the décimo tercer mes, the 13th-month pay, which DGI lists as employment income), professional fees, trading income, rents from Panama property, and other Panama-source income ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).
4. **Business costs and expenses.** Deduct costs and expenses needed to produce Panama-source income or keep its source going. Costs of foreign-source or exempt income are not deductible, nor are income tax itself, fines, or penalty interest. Salaried workers cannot deduct transport ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).
5. **Personal deductions**, each within its cap (table below). Then losses brought forward, within their limits.
6. **Apply the tax table** for individuals (below) to net taxable income. Representation allowances (gastos de representación) are taxed separately on their own table.
7. **Subtract credits:** salary withholding, estimated tax paid for the year, and any credit brought forward. The result is the balance due or the refund.
8. **Estimated tax for next year.** The return carries an estimate of next year's income, which may not be lower than the income just declared. Tax on the estimate is paid in three instalments ([DGI, article 710](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php)).
9. **Educational insurance** on self-employed income, computed on the same return (below).
10. **Company add-ons**, if the client has a business: Aviso de Operación tax on the return; dividend tax within 10 days of any distribution; withholding on payments abroad.
11. **File** on e-Tax 2.0, countersigned by a CPA if income is above USD 11,000 ([DGI FAQ, question 45](https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php)), and **pay** by the due dates.

## Figures for 2026

### Individuals: the tax table ([DGI, rates](https://dgi.mef.gob.pa/DInforme/Tarifa.php); [DGI, Planilla 03](https://dgi.mef.gob.pa/DInforme/Planilla03.php))

Applies to net taxable income of individuals (article 700 of the Código Fiscal). Unchanged for 2026.

| Net taxable income | Tax |
| --- | --- |
| Up to USD 11,000 | 0% |
| More than USD 11,000 up to USD 50,000 | 15% of the amount over USD 11,000 |
| More than USD 50,000 | USD 5,850 on the first USD 50,000, plus 25% of the amount over USD 50,000 |

Check: (50,000 − 11,000) × 15% = 5,850, which is the fixed amount in the top band. Income of exactly USD 11,000 pays nothing; the 15% starts on the first balboa above it.

DGI's rate page gives only this table for individuals and no separate minimum tax for them. The CAIR alternative calculation described on DGI's pages is written for companies (below).

**Representation allowances** (gastos de representación paid to managers on top of salary) are not added to salary. They are taxed at 10% up to USD 25,000, and above that USD 2,500 plus 15% of the excess ([DGI, Planilla 03](https://dgi.mef.gob.pa/DInforme/Planilla03.php)). They may not exceed 100% of the worker's salary, and a worker whose only extra income is representation allowance need not file ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).

### Personal deductions ([DGI return instructions](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf); [DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php); [DGI income tax FAQ](https://dgi.mef.gob.pa/Preguntas/Rent.php))

| Deduction | Limit and conditions |
| --- | --- |
| Basic deduction | USD 800, only for spouses who file jointly |
| Medical costs | No cap. Costs incurred in Panama for the taxpayer and dependants, backed by legal invoices or insurer certificates; health insurance premiums count. Spouses filing separately may split them but not claim more than the total. |
| Mortgage interest | Up to USD 15,000 a year, on loans used only to buy, build or improve the taxpayer's own principal home in Panama. Loans with preferential interest do not qualify. |
| Interest on education loans | Loans used only for education in Panama, including IFARHU loans. No cap is stated. |
| School costs | Up to USD 3,600 per dependant (dependants up to 25), from the first level of schooling, in Panama only, net of any scholarship. Enrolment, monthly fees, supplies, uniforms and school transport, on invoices in the name of the parent or student. For a disabled dependant attending class there is no cap, but only for a salaried taxpayer with tax withheld who files a return. A salaried taxpayer with tax withheld who pays their own university may deduct enrolment and credit hours on the return. |
| Pension fund contributions | The lower of 10% of gross annual income and USD 15,000 |
| Donations | Up to USD 50,000 a year, to Panamanian educational or charitable institutions approved for the purpose; dues to Panamanian non-profit bodies are also deductible |

A salaried taxpayer earning more than USD 11,000 with tax withheld gets school costs back as a cash credit: 15% of the costs if income is USD 11,000 to USD 50,000, and 25% above USD 50,000. Other filers deduct school costs but get no credit ([DGI FAQ, questions 11 and 19](https://dgi.mef.gob.pa/Preguntas/Rent.php)).

DGI's list of personal deduction lines has no per-dependant deduction. Do not claim one.

**Losses brought forward:** deductible over the next five years at 20% a year, and they may not cut net taxable income by more than 50% ([DGI return instructions, line 92](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf)).

### Educational insurance and CSS for the self-employed ([DGI return instructions, lines 118-123](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf); [DGI, individual returns](https://dgi.mef.gob.pa/DInforme/DJRRPNAPI-Comerciante.php))

- **Educational insurance (seguro educativo)** on non-salary income is computed on the ISR return at 2.75% of a base equal to total income, less salary with withholding, income in kind, representation allowances, directors' fees, exempt income and foreign-source income, less deductible costs and expenses, plus capital gains on real estate and securities. Embassy employees apply 1.25%. It is paid with the estimated tax, in one sum or three equal instalments ([DGI filing instructions](https://dgi.mef.gob.pa/DInforme/pdf/INSTRUCTIVO%20DE%20LLENADO.pdf)).
- **CSS contributions: check.** Law 462 of 2025 changed Caja de Seguro Social contributions for employees, employers and independent workers. DGI's return instructions still describe the old independent-worker formula, and the CSS and Gaceta Oficial sites are not allowed sources for this Guide. Do not quote a CSS rate from this Guide; take current rates from the CSS or the law itself. The ISR return does carry a CSS line for independents, and that amount is due with the annual balance by 31 March.

### Companies, summary only ([DGI, rates](https://dgi.mef.gob.pa/DInforme/Tarifa.php); [DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php))

**Rate.** Companies (personas jurídicas) pay 25% of net taxable income for 2011 and later years. Companies in which the State holds more than 40% of the shares pay 30%. The sectors once taxed at higher rates (electricity, telecoms, insurance, regulated finance companies, cement, gaming, mining, banking) have paid 25% since 1 January 2014 ([DGI, rates](https://dgi.mef.gob.pa/DInforme/Tarifa.php)).

**CAIR, the alternative calculation.** A company whose total taxable income (gross income less exempt, non-taxable and foreign-source income) is more than USD 1,500,000 a year pays tax on the greater of:

1. net taxable income worked out the normal way, and
2. 4.67% of total taxable income.

Both bases are taxed at the company's rate, so at 25% the CAIR floor is 25% of the 4.67% base. A company with taxable income of USD 1,500,000 or less is outside CAIR ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).

A company that would make a loss under CAIR, or whose effective rate under CAIR would exceed the rate in force (DGI's page also mentions 30% in one place: check), may ask DGI not to apply CAIR for up to three years. The request is due no later than 90 calendar days after the year end, or with the return if an extension was granted. If DGI has not decided by the filing deadline, the company pays on the normal method; DGI has six months after the filing deadline to decide, and silence means the request is accepted ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).

**Dividend tax.** A company must withhold dividend tax when it distributes profits ([DGI, Form 07](https://dgi.mef.gob.pa/DInforme/Formulario07.php)):

| Profits distributed | Withholding |
| --- | --- |
| Panama-source profits | 10% |
| Profits from foreign-source or export income, or from exempt interest (government securities, bank deposits) | 5% |
| Companies in the Colón Free Zone or another free zone, whatever the source | 5% |
| Bearer shares | 20% |

- **Complementary tax.** If a company distributes nothing, or less than 40% of the year's net profits after its own tax, it pays 10% of the shortfall. For a company whose dividends are taxed at 5%, the test is 20% of net profits, and the shortfall is still taxed at 10%.
- **Loans to shareholders** are taxed as dividends at 10%, even where the company's normal dividend rate is 5%. The exception is bearer shares: 20% must be withheld before a loan is made to a bearer shareholder.
- **Branches** of foreign companies pay 10% of their Panama taxable income less the tax paid on it.
- A tax treaty rate prevails where one applies. Tax treaty dividends go on Form 929 and the treaty rules are referred.
- **Form 07** must be filed, and the tax paid, within 10 days of the distribution. Late filing adds a 10% surcharge plus interest.

A shareholder whose only income is dividends that have already been taxed at source need not file a return ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).

**Aviso de Operación tax.** A business with an Aviso de Operación (commercial licence) pays an annual tax of 2% of the company's capital (assets less liabilities subject to the tax), with a minimum of USD 100 and a maximum of USD 60,000 ([DGI return instructions, line 83](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf)). It is declared on the ISR return, so a business that holds an Aviso must file even for a year with no operations ([DGI, individual returns](https://dgi.mef.gob.pa/DInforme/DJRRPNAPI-Comerciante.php)). It is due by 31 March, and a filing extension does not defer it ([DGI, filing deadlines](https://dgi.mef.gob.pa/DInforme/P-Presentacion.php)). Liberal professions practised individually or through a sociedad civil, non-profit work, and agricultural activities do not need an Aviso ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).

**Tasa Única.** Separately, every sociedad anónima pays a flat annual fee of USD 300 and every private-interest foundation USD 400, with a USD 50 surcharge if late. Companies registered from 1 January to 30 June pay by 15 July each year; those registered from 1 July to 31 December pay by 15 January ([DGI, Tasa Única FAQ](https://dgi.mef.gob.pa/Preguntas/TasaU.php)).

### Payments to people abroad ([DGI, Form 05](https://dgi.mef.gob.pa/DInforme/Formulario05.php))

Anyone who pays or credits Panama-source income to a person based abroad must withhold tax. The rate for a company (25%) or the individual table applies to 50% of the amounts paid in the year, less withholding already made. The tax goes on Form 05 within 10 days of the payment or credit, whichever comes first ([DGI, returns and due dates](https://dgi.mef.gob.pa/DInforme/Tab-Decla.php)). Treaty relief goes on Form 433 and is referred.

## Boundaries and exceptions ([DGI, article 710](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php); [DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php); [DGI return instructions](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf))

| Situation | Treatment |
| --- | --- |
| Net taxable income exactly USD 11,000 | 0%. Tax starts only on income more than USD 11,000. |
| Net taxable income exactly USD 50,000 | USD 5,850. The 25% rate applies only to income more than USD 50,000. |
| Annual income exactly USD 11,000 | No CPA countersignature needed; it is required when income is more than USD 11,000. |
| Independent with net taxable income of USD 1,000 or less **and** gross income not more than USD 3,000 | No return. Both tests must be met. |
| Agricultural activity with gross income under USD 300,000 | No return, under article 710 as DGI publishes it. DGI's general rules page still says USD 250,000: check which applies before relying on it. |
| One employer, all tax withheld | No return needed. More than one salary means one return for all income. |
| Pension from the CSS and no other taxable income | No return needed. |
| Only income is dividends already taxed at source, or exempt interest | No return needed. |
| Foreign-source income | Reported on its own line, not taxed; related costs not deductible. Mixed-place work: refer. |
| Interest on Panamanian bank deposits and government securities | Exempt (article 708). |
| Pension fund contributions | Lower of 10% of gross income and USD 15,000. |
| School costs abroad or online from abroad | Not deductible; only school costs in Panama count. |
| Mortgage interest at a preferential rate | Not deductible. |
| Office in a property the taxpayer owns | No rent deduction for the space. Rent on property used partly for the business is deductible in proportion to the taxable use. |
| Company taxable income exactly USD 1,500,000 | Outside CAIR; CAIR applies above that amount. |
| Company distributes 40% or more of net profits after tax | No complementary tax (20% test for companies taxed at 5% on dividends). |
| Return being audited by DGI | No amended return can be filed. |

## Worked cases ([DGI, rates](https://dgi.mef.gob.pa/DInforme/Tarifa.php); [DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php); [DGI, Form 07](https://dgi.mef.gob.pa/DInforme/Formulario07.php))

All cases are for tax year 2026 and assume Panama-source income unless stated.

**Case 1. Independent professional, middle band.** Net taxable income after business expenses and deductions USD 40,000. Tax = (40,000 − 11,000) × 15% = 29,000 × 15% = USD 4,350. Income is more than USD 11,000, so the return needs a CPA countersignature; it is due by 15 March 2027.

**Case 2. Independent professional, top band.** Net taxable income USD 75,000. Tax = 5,850 + (75,000 − 50,000) × 25% = 5,850 + 6,250 = USD 12,100.

**Case 3. Consultant working abroad.** A Panama resident invoices USD 5,000 to a foreign client for work done wholly outside Panama. It is foreign-source: reported on the foreign-source line, not taxed, and the costs of earning it are not deductible. If some of the work was done in Panama, or the client relies on the offshore services rules, refer.

**Case 4. Company inside CAIR.** Total taxable income USD 3,000,000; net taxable income by the normal method USD 100,000. Normal tax = 100,000 × 25% = USD 25,000. CAIR base = 3,000,000 × 4.67% = USD 140,100; CAIR tax = 140,100 × 25% = USD 35,025. The company pays the greater, USD 35,025, unless DGI agrees not to apply CAIR. Its effective rate under CAIR, 35,025 ÷ 100,000 = 35%, exceeds the 25% rate, so it may apply for non-application within 90 calendar days of the year end.

**Case 5. Salaried parent claiming school costs.** Salary USD 30,000 from one employer, tax fully withheld; USD 2,000 of documented school costs in Panama for one child with no scholarship. No return is required, but the employee may file to recover school costs as a credit: 2,000 × 15% = USD 300, because income is between USD 11,000 and USD 50,000. The costs are under the USD 3,600 per-dependant cap.

**Case 6. Pension fund cap.** Gross income USD 60,000; pension fund contributions USD 8,000. Cap = the lower of 60,000 × 10% = USD 6,000 and USD 15,000, so USD 6,000 is deductible and USD 2,000 is not.

**Case 7. Estimated tax.** Case 1's return, filed by 15 March 2027, shows tax of USD 4,350 for 2026. The estimated income for 2027 may not be lower than the income declared for 2026, so on the same deductions the estimated tax is USD 4,350, paid as 4,350 ÷ 3 = USD 1,450 by each of 30 June, 30 September and 31 December 2027 (or in one payment). Any balance of 2026 tax not covered by the 2026 instalments is due by 31 March 2027.

**Case 8. Dividends and complementary tax.** A company has net profits after its own tax of USD 600,000, all Panama-source, and distributes USD 200,000. Dividend tax = 200,000 × 10% = USD 20,000, on Form 07 within 10 days. The 40% test is 600,000 × 40% = USD 240,000; the shortfall is 240,000 − 200,000 = USD 40,000, so complementary tax = 40,000 × 10% = USD 4,000.

**Case 9. Payment abroad.** A Panama company pays a foreign company USD 10,000 for services received in Panama, its only such payment in the year. Withholding = 10,000 × 50% × 25% = USD 1,250, on Form 05 within 10 days of payment, unless a treaty applies (refer).

**Case 10. Aviso de Operación tax.** A trader's capital subject to the tax is USD 50,000. Tax = 50,000 × 2% = USD 1,000, between the USD 100 minimum and the USD 60,000 maximum, declared on the ISR return and due by 31 March.

## When to refuse or refer

- **Source unclear.** Work done partly in Panama and partly abroad, or a client relying on the offshore services rules in article 694 parágrafo 2. The split drives the whole computation, and this Guide cannot quote the article's text.
- **Non-residents beyond simple withholding**, treaty claims (Forms 433, 929, 931), tax residence certificates.
- **Companies beyond the summary**: CAIR non-application requests, special fiscal periods, groups, transfer pricing (Form 930), free zones, SEM, City of Knowledge, Panamá Pacífico, tourism and other incentive regimes, AMPYME micro-business exemptions.
- **Capital gains** on real estate (Forms 106 and 107) or on shares and securities (Form 108).
- **CSS contribution rates** for employees, employers or independents under Law 462 of 2025, educational insurance (seguro educativo) withheld from salaries and paid by employers, and the CSS treatment of the 13th-month pay. Not sourced here.
- **Arrears, audits, enforcement**, closure of premises, criminal tax fraud, suspension of the Aviso de Operación, or a client already under DGI audit (no amended return is allowed).
- **Prescription questions.** DGI's FAQ says individual income tax prescribes after 7 years in one answer and 5 years in another ([DGI FAQ, questions 6 and 32](https://dgi.mef.gob.pa/Preguntas/Rent.php)). Check the Código Fiscal before advising.

## Filing and payment ([DGI, filing deadlines](https://dgi.mef.gob.pa/DInforme/P-Presentacion.php); [DGI, article 710](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php); [DGI, returns and due dates](https://dgi.mef.gob.pa/DInforme/Tab-Decla.php))

### Who must file

Every taxpayer files a sworn annual return (declaración jurada de rentas) for the previous year, except ([DGI, article 710](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php); [DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php); [DGI FAQ, question 18](https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php)):

- a worker paid salary (and representation allowance) by one employer during the year, with all tax withheld;
- a CSS pensioner with no other taxable income;
- a person whose only income is dividends already taxed at source, or exempt interest;
- an independent with net taxable income of USD 1,000 or less and gross income not more than USD 3,000 ([DGI, article 710](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php));
- a person in agriculture with gross income under USD 300,000 ([DGI, article 710](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php); see the conflict noted in the boundary table).

Someone exempt from filing must still make a sworn statement of why when asking for a paz y salvo (tax clearance certificate). A person who lost a job part way through the year and earned salary from it still files ([DGI FAQ, question 43](https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php)). A return with income above USD 11,000 must be countersigned by a CPA with a DGI security code.

### Deadlines for the 2026 return

| What | Individuals | Companies |
| --- | --- | --- |
| Annual return (Form 2V; Form 1V for companies) | By 15 March 2027 | By 31 March 2027 |
| Extension, asked for on e-Tax 2.0 before the deadline | To 15 April 2027 | To 30 April 2027 |
| Balance of 2026 tax | By 31 March 2027 | By 31 March 2027 |
| Aviso de Operación tax | Due 31 March 2027, not deferred by an extension | Same |
| Estimated tax for 2027 | 30 June, 30 September, 31 December 2027, or one payment | Same |
| Special fiscal period (with DGI approval) | n/a | Return within 3 months of the year end; estimated tax 6, 9 and 12 months after it |
| Form 1V8 (pure salary, filing only to claim deductions) | No deadline | n/a |

The extension is for a maximum of one month and is granted on payment of the tax the taxpayer estimates is due. Any extra tax found on the return carries late-payment charges ([DGI, article 710, parágrafo 5](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php)). Final returns on ceasing business: companies within 30 days after cancellation in the Public Registry; individuals from 1 to 15 January after the year ends ([DGI, individual returns](https://dgi.mef.gob.pa/DInforme/DJRRPNAPI-Comerciante.php)).

Payment codes on the DGI payment slip: 101 for income tax, 319 for educational insurance, 724 for CSS contributions ([DGI filing instructions](https://dgi.mef.gob.pa/DInforme/pdf/INSTRUCTIVO%20DE%20LLENADO.pdf)). Employers file Planilla 03 (salary withholding) monthly, within 60 calendar days after the CSS payroll is filed ([DGI, Planilla 03](https://dgi.mef.gob.pa/DInforme/Planilla03.php)).

### Amending a return

A return may be amended once per year, within 36 months of the original filing deadline. The fee is USD 100 for individuals and USD 500 for companies. A correction that lowers the tax needs a written request setting out the facts; one that raises the tax is filed online without a request. No amendment is allowed during a DGI audit ([DGI, article 710, parágrafo 4](https://dgi.mef.gob.pa/DInforme/A710codigofiscal.php); [DGI, penalties](https://dgi.mef.gob.pa/DInforme/Sanciones.php)).

### Penalties ([DGI, fines and penalties](https://dgi.mef.gob.pa/MS/MS.php); [DGI declarations FAQ](https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php); [DGI, amending returns](https://dgi.mef.gob.pa/DInforme/R-Dcl.php))

| Failure | Penalty |
| --- | --- |
| Late or missing annual return | USD 100 for an individual, USD 500 for a company (DGI FAQ, question 32, and the Tax Procedure Code article quoted on DGI's amending-returns page). DGI's penalties page cites article 710 of the Código Fiscal: USD 100 to USD 1,000. Check which applies. |
| Not keeping books or records when obliged | USD 100 to USD 500; books not up to date (within 60 days after each month end), USD 100 to USD 500 for each month late |
| Refusing to show books or allow an inspection | USD 100 to USD 5,000 |
| Not providing requested information within 72 hours | USD 1,000 to USD 5,000, USD 10,000 if repeated, plus closure of the premises for 2 days (up to 10 days if repeated, 15 days if it persists) |
| Late dividend tax (Form 07) | 10% surcharge plus interest on the tax |
| Late Planilla 03 | USD 100, USD 500 or USD 1,000, by the employer's annual income |
| Tax paid late | Late-payment interest under article 1072-A of the Código Fiscal (rate not published on DGI's pages: check) |

Estimated tax paid late generates surcharges and interest and blocks the paz y salvo, which matters for public tenders ([DGI, estimated tax notice](https://dgi.mef.gob.pa/New/news?n=194)).

### Returns being filed now: tax year 2025

The 2025 returns were due by 15 March 2026 (individuals) and 31 March 2026 (companies), or 15 April and 30 April 2026 with an extension. The table, deductions and rules above applied to 2025 unchanged. A 2025 return not yet filed is late: file it at once and expect the late-filing fine. The first 2026 estimated-tax instalments (30 June and 30 September 2026) have passed; the last is due by 31 December 2026.

## Completion checklist

- [ ] Each income stream classified as Panama-source, foreign-source or exempt, with the place of work recorded ([DGI FAQ](https://dgi.mef.gob.pa/Preguntas/Rent.php)).
- [ ] Filing exemption tested against every item in "Who must file".
- [ ] Business costs limited to Panama-source income; no ISR, fines or foreign-source costs deducted.
- [ ] Basic deduction only if the spouses file jointly.
- [ ] Mortgage interest (USD 15,000, own home in Panama, no preferential rate), pension (lower of 10% of gross and USD 15,000), school costs (USD 3,600 per dependant, Panama only, net of scholarships) and donations (USD 50,000, approved bodies) within their limits and documented ([DGI return instructions](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf)).
- [ ] No per-dependant deduction claimed.
- [ ] Tax computed on the 2026 table; representation allowances on their own table.
- [ ] Withholding, 2026 instalments and credits brought forward subtracted.
- [ ] Estimated tax for 2027 not lower than the 2026 income declared; instalment dates given to the client.
- [ ] Educational insurance at 2.75% on self-employed income, if any ([DGI return instructions](https://dgi.mef.gob.pa/DInforme/pdf/RENTA%20-%20NATURAL.pdf)).
- [ ] Company matters: Aviso de Operación tax, dividend tax on Form 07 within 10 days, complementary tax, CAIR if taxable income is more than USD 1,500,000, Form 05 on payments abroad, Tasa Única ([DGI, general rules](https://dgi.mef.gob.pa/DInforme/GD-ISR.php)).
- [ ] CPA countersignature if income is more than USD 11,000 ([DGI FAQ, question 45](https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php)).
- [ ] Filed by 15 March 2027 (individuals) or 31 March 2027 (companies), or extension requested in time; balance paid by 31 March 2027.
- [ ] CSS contribution rates and any offshore services claim marked "check" and referred.

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
