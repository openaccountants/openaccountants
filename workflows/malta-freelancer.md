# Malta Freelancer / Self-Employed Tax Workflow

**MCP prompt name:** `malta-freelancer`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/MT`

## Trigger phrases

- "self-employed Malta"
- "freelancer Malta"
- "part-time work Malta"
- "provisional tax Malta"
- "SSC Malta"
- "Malta VAT registration"
- "malta-income-tax"
- "Malta sole trader"
- "tax Malta"

## What it produces

- Part-time final tax (10%) vs progressive rate comparison
- SSC Class 2 contribution computation (self-occupied)
- VAT return working paper (if VAT-registered)
- Provisional tax schedule (20%, 30%, 50%)
- Annual income tax return working paper

## Skills to load

From the MT bundle:
- `malta-income-tax`: tax rates, brackets, single/married/parent computation, part-time 10% final tax
- `malta-ssc`: Social Security Contributions (Class 2 self-occupied rates)
- `malta-vat-return`: VAT tax periods, registration, deductible input VAT
- `mt-estimated-tax`: provisional tax benchmark and due dates

## 6-phase structure

### Phase 1: Intake
Confirm: employment status (full-time employed + part-time self-employed, or full-time self-employed), type of income (service, product, rental), annual gross revenue, major expenses, VAT registration status, marital status (affects rate structure).

### Phase 2: Part-time vs standard rate decision
Part-time self-employed profit is taxed at a final 10% if the person was resident in Malta and had full-time employment registered with Jobsplus, a pension taxable in Malta, or was in full-time education or an apprenticeship ([ITA art. 90A(11)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c); [Part-time Work Rules, S.L. 123.39, rule 2](https://legislation.mt/getpdf/626bac3f56cbc512388f56db)). The 10% is charged on taxable net profit, paid by 30 April of the following year with a statement of accounts, not on gross income ([ITMA art. 42(4)](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b)). The cap is €12,000 of self-employed profit (€10,000 for part-time employment income). Profit above the cap does not lose the regime: only the excess goes into the return at normal rates (S.L. 123.39 rule 3(2)). Conditions (rule 4): the part-time work is registered with Jobsplus; no more than two employees, both part-time; proper books are kept; the work is for someone other than the full-time employer; and the person is VAT registered unless not required to register or exempt. The person may instead declare all part-time income at progressive rates, with the 10% already paid credited or refunded ([ITA art. 90A(2)](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c)). Run both and show which is lower.

### Phase 3: SSC computation
Class 2 is based on the net earnings of the previous calendar year and is paid in three four-monthly periods ending April, August and December ([Social Security Act, Cap. 318, art. 10(3) and 11](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c)). Category SA is a fixed weekly amount, SB is the weekly equivalent of 15% of annual net earnings, and SC is a capped weekly amount (Tenth Schedule, Part III). Take the current weekly amounts from `malta-ssc`. Class 2 depends on social security status, not on the income tax regime. A person in insurable employment who is also self-occupied pays Class 1 through the employer, and may pay Class 2 instead only with approval where the Class 2 rate is higher (art. 14). A pensioner or full-time student who is part-time self-occupied (earnings over €910 a year, art. 2) pays Class 2, even though the income qualifies for the 10% part-time tax; where earnings are in the SA band, the Tenth Schedule lets them pay 15% of annual net earnings instead of the SA amount.

### Phase 4: VAT position
A taxable person established in Malta registers under Article 10 within thirty days of the first taxable supply, unless registered under Article 11, the optional exemption for turnover in the preceding calendar year not above €35,000 ([VAT Act, Cap. 406, art. 10(1)](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) and Sixth Schedule). A tax period is three calendar months unless regulations or a Commissioner notice set another period (art. 17(2), (3), (6)): use the period shown on the registration. Compute output VAT (sales × applicable rate) less deductible input VAT (business purchases).

### Phase 5: Provisional tax
Self-employed taxpayers pay provisional tax under the Payment of Provisional Tax Rules ([S.L. 372.18](https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4)): at least 20% of the benchmark by 30 April, a further 30% by 31 August and a further 50% by 21 December (rules 4 and 5). The benchmark is the tax payable in the self-assessment for the benchmark year of assessment, adding back provisional tax (rule 6(1)). The benchmark year is the last year of assessment whose return was due before the calendar year of the first payment, normally two years back: 2026 provisional tax uses basis 2024, year of assessment 2025 (rule 2(1)). A current-year estimate can only reduce the payments, through the P.T. reduction form (rule 10). FS5 is the employer's monthly payroll payment advice, not a provisional tax form ([FSS Rules, S.L. 372.14, rule 20](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3)).

### Phase 6: Handoff
Recommend review by a Malta-qualified CPA or warranted accountant. Route to: https://www.openaccountants.com

## Verifier

Sourced from the law. Every figure is cited to an official source (legislation.mt). This workflow was corrected on 8 November 2026 and has not been reviewed by an accountant since. Each skill it loads carries its own review status: use the MCP server or bundle API to access the current versions and their labels.
