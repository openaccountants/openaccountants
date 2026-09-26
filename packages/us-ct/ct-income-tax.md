---
name: ct-income-tax
description: Use this skill whenever asked about Connecticut individual income tax for self-employed individuals or sole proprietors — filing Form CT-1040, CT estimated tax (Form CT-1040ES), Connecticut tax brackets, Connecticut personal exemption, or any query involving Connecticut state income tax compliance. Trigger on phrases like "Connecticut income tax", "CT income tax", "Form CT-1040", "Connecticut estimated tax", "Connecticut self-employed tax", "DRS income tax", "CT AGI", or "Conn. Gen. Stat. §12-700".
version: "0.1"
jurisdiction: US-CT
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Connecticut resident income tax (Form CT-1040), including sole proprietors

## Scope and who this is for ([2025 Form CT-1040 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

This Guide covers the Connecticut resident individual income tax return, **Form CT-1040**, for **tax year 2026** (returns filed in 2027), with a dated section for **2025 returns** (due 15 April 2026, or 15 October 2026 on extension). It is written for full-year Connecticut residents, including sole proprietors and owners of a single-member LLC that is disregarded for federal tax, whose business profit reaches Connecticut through federal adjusted gross income (AGI).

The Connecticut tax tables (Tables A to E) for 2026 are the same as for 2025: the 2026 Form CT-1040ES prints "Table A - Personal Exemptions for 2026 Taxable Year", "Table B - Initial Tax Calculation for 2026 Taxable Year" and "Table E - Personal Tax Credits for 2026 Taxable Year" with the same amounts as the 2025 instructions. The 2026 Form CT-1040 instructions were not published when this Guide was written (25 September 2026); where a 2026 figure comes only from the 2025 instructions, it is labelled 2025.

It does **not** cover part-year residents or nonresidents (Form CT-1040NR/PY), trusts and estates (Form CT-1041), the pass-through entity's own return (Form CT-PET), or the Connecticut alternative minimum tax computation (Form CT-6251). See "When to refuse or refer".

**Who is a resident** ([DRS tax information](https://portal.ct.gov/drs/individuals/resident-income-tax/tax-information)). You are a resident for the year if Connecticut was your domicile for the entire year, **or** you were not domiciled in Connecticut but "maintained a permanent place of abode in Connecticut during the entire 2025 taxable year and spent a total of more than 183 days in Connecticut". Both parts of the second test must be met. A Connecticut domiciliary can still be treated as a nonresident only if every condition in Group A (no permanent place of abode in Connecticut all year, one outside all year, and not more than 30 days in Connecticut) or Group B (the 548-day foreign presence test) is met.

**Who must file (2025).** A resident must file if any of these is true: Connecticut tax was withheld; estimated tax or an extension payment was made; the person had a PE Tax Credit; the gross income test is met; the person had a federal alternative minimum tax liability; or the person claims the Connecticut earned income tax credit. The gross income test is met when gross income **exceeds** $12,000 (married filing separately), $15,000 (single), $19,000 (head of household) or $24,000 (married filing jointly or qualifying surviving spouse). Gross income means gross, not net: DRS's own example is a sole proprietor with $100,000 of Schedule C gross income and $8,000 net profit, who must file. Gross income also includes any additions required on Form CT-1040, Schedule 1, for example interest on other states' bonds or a 168(k) or 179 add-back. Federally non-taxable Social Security is not gross income. For 2026, the same amounts are the Table A exemption maximums in the 2026 Form CT-1040ES; confirm the gross income test when the 2026 instructions are published.

## Ask the client first

- Which tax year? 2025 and 2026 use the same Tables A to E, but the IRA share of the pension subtraction rises from 75% (2025) to 100% (2026) ([2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf)).
- Resident all year? Domicile, any Connecticut home kept all year, and days in Connecticut (more than 183). If the person moved in or out, stop (Form CT-1040NR/PY).
- Filing status. It generally must match federal status, but a Connecticut resident married to a nonresident files married filing separately unless they file jointly federally and elect to be treated as both residents.
- Federal AGI (2025 Form 1040, line 11a) and the pieces inside it: Schedule C profit, taxable IRA distributions (line 4b), taxable pensions and annuities (line 5b), taxable Social Security (line 6b).
- For the business: was federal **bonus depreciation (section 168(k))** or a **section 179** deduction claimed this year or in the previous four years? Each needs a Connecticut adjustment.
- Interest from other states' bonds (addition), and interest from U.S. or Connecticut obligations (subtraction).
- Is the client a partner, LLC member or S corporation shareholder of an entity that elected to pay the Connecticut pass-through entity (PE) tax? Get Schedule CT K-1, Part 4, Line 1.
- Income taxed by another state (for example wages taxed by New York), and a copy of that state's return.
- Federal earned income credit, qualifying children, investment income.
- Property tax paid in the year to a Connecticut town on the main home and on up to one or two cars (see Property tax credit).
- Connecticut withholding, estimated payments (dates and amounts), prior-year Connecticut tax, and any extension payment.

## The method, step by step

Form CT-1040 line numbers are from the 2025 return.

1. **Line 1, federal AGI.** Enter federal adjusted gross income from Form 1040 line 11a, not federal taxable income. A sole proprietor's Schedule C profit, the deduction for half of self-employment tax, self-employed health insurance and SEP or solo 401(k) contributions all sit inside federal AGI, so they flow through with no Connecticut entry. The same goes for a home office deduction taken on Schedule C: Connecticut AGI is federal AGI plus only the Schedule 1 modifications ([DRS tax information](https://portal.ct.gov/drs/individuals/resident-income-tax/tax-information)), and none of them adjusts it. Deductions taken after federal AGI do not reach Connecticut: on the 2025 [Form 1040](https://www.irs.gov/pub/irs-pdf/f1040.pdf) these include the qualified business income deduction (line 13a), the Schedule 1-A additional deductions (line 13b, which carry the new federal deductions for tips, overtime, car loan interest and seniors) and the federal standard deduction.
2. **Line 2, additions (Schedule 1, Line 38).** For a business owner the key ones are 100% of the section 168(k) bonus depreciation deducted this year (Line 36, [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf)) and 80% of the section 179 deduction (Line 36a). Others: interest and exempt-interest dividends from non-Connecticut state and local bonds (Lines 31-32), lump-sum distributions taxed on Form 4972 (Line 33), and Connecticut income tax deducted in reaching federal AGI (Line 37).
3. **Line 4, subtractions (Schedule 1, Line 50).** For a business owner: 25% of the 168(k) amount added back in each of the four preceding years (Line 48a, [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf)) and 25% of the 179 amount added back in each of the four preceding years (Line 49, item 10). Others: U.S. obligation interest (Line 39), the Social Security adjustment (Line 41), state income tax refunds (Line 42), railroad retirement (Line 43), military retirement pay (Line 44), 50% of Connecticut teachers' retirement pay (Line 45), CHET contributions (Line 48), the pension and annuity subtraction (Line 48b) and ABLE contributions (Line 48d).
4. **Line 5, Connecticut AGI** = Line 1 + Line 2 - Line 4. If Line 5 is at or below the Table A exemption maximum for the filing status, Line 6 is 0.
5. **Tax Calculation Schedule** (instructions page 19; 2026 Form CT-1040ES page 3):
   - Line 2: personal exemption from **Table A**. Line 3: Connecticut taxable income = Connecticut AGI minus the exemption.
   - Line 4: **Table B** on taxable income.
   - Line 5: **Table C** 2% phase-out add-back, looked up on Connecticut **AGI**, not taxable income ([2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf)).
   - Line 6: **Table D** recapture, also on Connecticut AGI.
   - Line 7 = Lines 4 + 5 + 6.
   - Line 8: **Table E** personal tax credit decimal, on Connecticut AGI. Line 9 = Line 7 x decimal. Line 10 = Line 7 - Line 9 = Form CT-1040 Line 6.
   - DRS tax tables may be used instead where Connecticut AGI is $102,000 or less ([2025 instructions, page 2](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf)).
6. **Line 7, credit for income tax paid to qualifying jurisdictions** (Schedule 2): other U.S. states, their local governments and DC only, never foreign countries. The credit is the least of the tax paid there, the Connecticut tax on that income, or Line 6. Complete Schedule 3 before Schedule 2.
7. **Line 9, Connecticut AMT** only if the client paid federal AMT (Form CT-6251).
8. **Line 11, property tax credit** (Schedule 3); **Line 13**, other credits (Schedule CT-IT Credit, never the PE Tax Credit); **Line 14**, Connecticut income tax; **Line 15**, use tax from Schedule 4 (enter 0 if none, or no use tax return has been filed).
9. **Payments and refundable credits:** withholding (Line 18), estimated payments (Line 19), extension payment (Line 20), CT EITC (Line 20a), claim of right credit (Line 20b), PE Tax Credit from Schedule CT-PE (Line 20c).
10. **Lines 22 to 30:** overpayment or tax due, then late payment penalty (Line 27), interest (Line 28) and estimated tax interest (Line 29).

## Rates, thresholds and figures by year

### Table B, initial tax (2025 and 2026, all rates from 2024) ([2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf))

The two lowest rates were cut for tax years from 2024: Conn. Gen. Stat. § 12-700 shows 3.0% and 5.0% for years before 2024 and 2.0% and 4.5% "For taxable years commencing on or after January 1, 2024" ([Chapter 229](https://www.cga.ct.gov/current/pub/chap_229.htm)).

| Connecticut taxable income (single or married filing separately) | Tax |
| --- | --- |
| Not more than $10,000 | 2.00% |
| More than $10,000, not more than $50,000 | $200 plus 4.5% of the excess over $10,000 |
| More than $50,000, not more than $100,000 | $2,000 plus 5.5% of the excess over $50,000 |
| More than $100,000, not more than $200,000 | $4,750 plus 6.0% of the excess over $100,000 |
| More than $200,000, not more than $250,000 | $10,750 plus 6.5% of the excess over $200,000 |
| More than $250,000, not more than $500,000 | $14,000 plus 6.9% of the excess over $250,000 |
| More than $500,000 | $31,250 plus 6.99% of the excess over $500,000 |

| Connecticut taxable income (married filing jointly or qualifying surviving spouse) | Tax |
| --- | --- |
| Not more than $20,000 | 2.00% |
| More than $20,000, not more than $100,000 | $400 plus 4.5% of the excess over $20,000 |
| More than $100,000, not more than $200,000 | $4,000 plus 5.5% of the excess over $100,000 |
| More than $200,000, not more than $400,000 | $9,500 plus 6.0% of the excess over $200,000 |
| More than $400,000, not more than $500,000 | $21,500 plus 6.5% of the excess over $400,000 |
| More than $500,000, not more than $1,000,000 | $28,000 plus 6.9% of the excess over $500,000 |
| More than $1,000,000 | $62,500 plus 6.99% of the excess over $1,000,000 |

| Connecticut taxable income (head of household) | Tax |
| --- | --- |
| Not more than $16,000 | 2.00% |
| More than $16,000, not more than $80,000 | $320 plus 4.5% of the excess over $16,000 |
| More than $80,000, not more than $160,000 | $3,200 plus 5.5% of the excess over $80,000 |
| More than $160,000, not more than $320,000 | $7,600 plus 6.0% of the excess over $160,000 |
| More than $320,000, not more than $400,000 | $17,200 plus 6.5% of the excess over $320,000 |
| More than $400,000, not more than $800,000 | $22,400 plus 6.9% of the excess over $400,000 |
| More than $800,000 | $50,000 plus 6.99% of the excess over $800,000 |

### Table A, personal exemption (2025 and 2026) ([2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf))

Connecticut has no standard deduction. The exemption is subtracted from Connecticut AGI. It falls by $1,000 for each $1,000, or part of $1,000, of Connecticut AGI above the start point.

| Filing status | Full exemption | Reduction starts when Connecticut AGI is more than | Exemption is $0 when Connecticut AGI is more than |
| --- | --- | --- | --- |
| Single | $15,000 | $30,000 | $44,000 |
| Married filing jointly or qualifying surviving spouse | $24,000 | $48,000 | $71,000 |
| Married filing separately | $12,000 | $24,000 | $35,000 |
| Head of household | $19,000 | $38,000 | $56,000 |

### Table C, 2% phase-out add-back (2025 and 2026) ([2025 instructions, page 21](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

Looked up on Connecticut AGI. The add-back grows by one step for each band, or part of a band, above the start point, up to a maximum.

| Filing status | No add-back if Connecticut AGI is not more than | Step | Maximum, reached when Connecticut AGI is more than |
| --- | --- | --- | --- |
| Single | $56,500 | $25 per $5,000 | $250 above $101,500 |
| Married filing jointly or qualifying surviving spouse | $100,500 | $50 per $5,000 | $500 above $145,500 |
| Married filing separately | $50,250 | $25 per $2,500 | $250 above $72,750 |
| Head of household | $78,500 | $40 per $4,000 | $400 above $114,500 |

The 2026 Form CT-1040ES prints the same Table C.

### Table D, tax recapture (2025 and 2026) ([2025 instructions, page 22](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

Looked up on Connecticut AGI. **Single and married filing separately share one column** in Table D (unlike Tables A, C and E). Key points; use the full table for AGI between them:

- **Single or married filing separately:** $0 up to $105,000; then $25 per $5,000 band, reaching $250 for AGI more than $150,000 and not more than $200,000; then $340 for more than $200,000 up to $205,000, rising $90 per $5,000 band to $2,950 for more than $345,000 and not more than $500,000; then $3,000 for more than $500,000 up to $505,000, rising $50 per $5,000 band to **$3,400 for more than $540,000**.
- **Married filing jointly or qualifying surviving spouse:** $0 up to $210,000; $50 per $10,000 band to $500 (more than $300,000 up to $400,000); then $680 for more than $400,000 up to $410,000, rising $180 per band to $5,900 (more than $690,000 up to $1,000,000); then $6,000 for more than $1,000,000 up to $1,010,000, rising $100 per band to **$6,800 for more than $1,080,000**.
- **Head of household:** $0 up to $168,000; $40 per $8,000 band to $400 (more than $240,000 up to $320,000); then $540 for more than $320,000 up to $328,000, rising $140 per band to $4,600 (more than $552,000 up to $800,000); then $4,680 for more than $800,000 up to $808,000, rising $80 per band to **$5,320 for more than $864,000**.

The 2026 Form CT-1040ES prints the same Table D.

### Table E, personal tax credit (2025 and 2026) ([2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf))

A decimal of the tax on Line 7, looked up on Connecticut AGI. It starts at .75 and falls in steps. Key points:

| Filing status | .75 when Connecticut AGI is more than / not more than | .10 when Connecticut AGI is more than / not more than | .00 when Connecticut AGI is more than |
| --- | --- | --- | --- |
| Single | $15,000 / $18,800 | $33,300 / $60,000 | $64,500 |
| Married filing jointly or qualifying surviving spouse | $24,000 / $30,000 | $52,000 / $96,000 | $100,500 |
| Married filing separately | $12,000 / $15,000 | $27,000 / $48,000 | $52,500 |
| Head of household | $19,000 / $24,000 | $46,000 / $74,000 | $78,500 |

### Social Security (Line 41) ([2025 instructions, page 24](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

- Fully exempt: single or married filing separately with federal AGI (CT-1040 Line 1) **less than $75,000**; married filing jointly, qualifying surviving spouse or head of household with federal AGI **less than $100,000**. Subtract the whole federally taxable amount (Form 1040 line 6b).
- At or above those amounts, use the Social Security Benefit Adjustment Worksheet: A = federal Social Security Benefits Worksheet line 1; B = line 9 (line 7 if filing separately and living with the spouse at any time in the year); C = lesser of A and B; D = 25% of C; E = federally taxable benefits (worksheet line 18); subtraction F = E - D, or 0 if D is at least E. In effect Connecticut taxes no more than 25% of the benefits.
- The 2026 Form CT-1040ES uses the same $75,000 and $100,000 tests.

### Pension, annuity and IRA subtraction (Line 48b) ([2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf))

- No age test. The test is **federal** AGI. Full subtraction if federal AGI is less than $75,000 (single, married filing separately, head of household) or less than $100,000 (married filing jointly). Nothing is allowed at federal AGI of $100,000 or more (single, separately, head of household) or $150,000 or more (jointly). Between, multiply by the phase-out decimal: .85, .70, .55, .40, .25, .10, .05, .025 (for example .85 for $75,000 to $77,499 single, and $100,000 to $104,999 joint).
- Amount before phase-out: 100% of taxable pensions and annuities (Form 1040 line 5b) minus military retirement pay, railroad retirement and Connecticut teachers' retirement pay, **plus** a share of taxable non-Roth IRA distributions (line 4b): **75% for 2025, 100% for 2026 and later** (Conn. Gen. Stat. § 12-701(a)(20)(B), [Chapter 229](https://www.cga.ct.gov/current/pub/chap_229.htm): "for the taxable year commencing January 1, 2025, seventy-five per cent ... and (III) for the taxable year commencing January 1, 2026, and each taxable year thereafter, any distribution").
- Not included: Roth IRA distributions, corrective distributions and disability pensions received before minimum retirement age. No double benefit for teachers' pay (Line 45 or Line 48b, not both).
- Filing status "qualifying surviving spouse" is not named in the phase-out table; check with DRS before using the joint column.

### Business depreciation add-backs ([2025 instructions, page 7](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

- **Section 168(k) bonus depreciation:** add back 100% of the federal bonus depreciation deducted in federal AGI for the year (Line 36); subtract 25% of that add-back in each of the four following years (Line 48a).
- **Section 179:** add back 80% of the section 179 amount deducted in federal AGI (Line 36a; statute: "For taxable years commencing on or after January 1, 2018, eighty per cent of any deduction claimed for federal purposes under Section 179"); subtract 25% of the added-back amount in each of the four following years (Line 49, item 10).
- These rules have no end date in the statute, so they apply to 2026 as well. They matter more now that federal law allows 100% bonus depreciation again.

### Federal conformity and P.L. 119-21 ("OBBBA") ([2026 legislative summary from DRS](https://portal.ct.gov/drs/miscellaneous-taxes/other-tax-page/state-tax-developments/2026-developments))

- Connecticut starts from federal AGI "as properly reported" on the federal return for the same year, and "Your federal adjusted gross income may not be further modified ... except as expressly provided by Conn. Gen. Stat. § 12-701(a)(20)". So federal changes that move AGI flow through for the same year unless Connecticut has a specific modification (as it does for 168(k) and 179).
- The new federal deductions for tips, overtime, car loan interest and seniors are taken after AGI (Schedule 1-A, Form 1040 line 13b), so they do not reduce Connecticut AGI.
- The 2026 session decoupled from IRC § 168(n) and delayed conformity to IRC § 174A, but DRS lists those changes under the **corporation business tax**. DRS's summary lists no matching change for the personal income tax. If a sole proprietor or pass-through owner deducted domestic research costs under § 174A, or took the retroactive small-business deduction under Section 70302(f) of P.L. 119-21, check current DRS guidance before filing.

### Connecticut earned income tax credit (CT EITC) ([2025 legislative overview](https://portal.ct.gov/drs/miscellaneous-taxes/other-tax-page/state-tax-developments/2025-developments/income-tax))

- 40% of the federal earned income credit claimed and allowed for the same year, **plus $250** if the taxpayer has at least one federal qualifying child. The $250 applies to tax years from 1 January 2025, so to 2026 as well.
- Only **full-year residents** who claimed and were allowed the federal credit. For 2025, not allowed if investment income is more than $11,950 (federal limit). Taxpayer, spouse and each child need a valid SSN by the due date, including extensions.
- Refundable: any excess over Connecticut tax is refunded without interest. Attach Schedule CT-EITC.

### Property tax credit (Line 11, Schedule 3) ([2025 instructions, page 14](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

- For property tax **paid in the year** to a Connecticut town or district on the primary residence, a privately owned or leased motor vehicle, or both. Late-payment interest and fees do not count. One vehicle for single, separately and head of household; two for joint filers and qualifying surviving spouses. A leased vehicle counts only with a written lease of more than one year.
- Maximum **$300 per return**, whatever the filing status. It cannot exceed the tax paid or the tax on Line 10. It is not refundable and cannot be carried forward.
- Phase-out on Connecticut AGI (2025 table): full credit if AGI is not more than $49,500 (single), $70,500 (joint or qualifying surviving spouse), $35,250 (separately) or $54,500 (head of household). Above that, it drops by 15% of the credit for each $10,000 or part ($5,000 for married filing separately). It is 100% phased out above $109,500 (single), $130,500 (joint), $65,250 (separately) and $114,500 (head of household).
- The $300 limit applies "for taxable years commencing on or after January 1, 2022" (§ 12-704c), so it continues for 2026.

### Pass-through entity (PE) tax and the PE Tax Credit ([2025 Form CT-PET instructions](https://portal.ct.gov/-/media/drs/forms/2025/pass-through/ct-pet-instructions_1225.pdf))

- For tax years from 2024 the PE tax is **optional**. A partnership or S corporation elects it each year on a timely Form CT-1065/CT-1120SI, no later than the due date or extended due date; "This election cannot be amended or revoked."
- The entity pays 6.99% on its tax base (the resident portion of unsourced income plus modified Connecticut-source income), Conn. Gen. Stat. § 12-699 ([Chapter 228z](https://www.cga.ct.gov/current/pub/chap_228z.htm)).
- Each member's PE Tax Credit is 87.5% of the member's share of PE tax paid (Form CT-PET, "Multiply Column H by 87.5% (.875)"). The member claims it on Schedule CT-PE, which must be attached, and enters it on CT-1040 Line 20c. Any excess over the member's liability is refunded, but DRS pays no interest on a refund that results from a PE Tax Credit.
- A resident's Schedule 2 credit can include the resident's share of a substantially similar entity-level tax paid to another state.

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Single, Connecticut AGI exactly $30,000 | Full $15,000 exemption. The reduction starts only when AGI is **more than** $30,000 | [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf) |
| Single, Connecticut AGI $15,000 or less | Line 6 is 0; no tax | same |
| Gross income exactly $15,000, single | Gross income test not met: it must **exceed** $15,000. File anyway if any other trigger applies (withholding, estimates, PE Tax Credit, federal AMT, CT EITC) | [DRS tax information](https://portal.ct.gov/drs/individuals/resident-income-tax/tax-information) |
| Single, federal AGI exactly $75,000, taxable Social Security | Not fully exempt ("less than $75,000"); use the worksheet | [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf) |
| Joint, federal AGI exactly $150,000, pension income | Pension subtraction is 0 ($150,000 "and up") | [2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf) |
| Married filing separately and Table D | Use the single column in Table D, but the separate columns in Tables A, C and E | [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf) |
| Connecticut tax after withholding and PE Tax Credit under $1,000 | No estimated payments required | [2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf) |
| Resident with no 2025 return because no Connecticut liability | No 2026 estimated payments required | same |
| Credit for tax paid to Canada or another foreign country | Not allowed; only U.S. states, their local governments and DC | [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf) |
| Extension payment made after 15 April | DRS will deny the extension request | [DRS tax information](https://portal.ct.gov/drs/individuals/resident-income-tax/tax-information) |
| Part-year resident wanting the CT EITC | Not allowed; full-year residents only | [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf) |
| Property tax bill paid late, with interest | The late payment and the interest do not qualify for the property tax credit | same |

## Worked cases ([2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf); [2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

Illustrations with assumed facts; check each lookup against the full DRS tables.

**Case 1: single sole proprietor, 2026.** Federal AGI $80,000, all from Schedule C profit after the self-employment tax deduction; no Connecticut modifications. Connecticut AGI is $80,000. Table A: AGI is more than $44,000, so the exemption is $0, and taxable income is $80,000. Table B: $2,000 plus 5.5% of $30,000 ($1,650) = $3,650. Table C: $80,000 falls in the band more than $76,500 and not more than $81,500, so $125. Table D: $0 (not more than $105,000). Line 7 = $3,775. Table E: .00 (more than $64,500). **Connecticut income tax: $3,775.**
Estimated tax: 90% of $3,775 is $3,397.50. If the 2025 Connecticut tax was $3,200, the required annual payment is the lesser, $3,200, paid as four installments of 25% ($800 each) on 15 April, 15 June, 15 September 2026 and 15 January 2027.

**Case 2: married couple, pensions, 2025 and 2026.** Married filing jointly. Federal AGI $121,250, which includes a $30,000 pension (line 5b) and a $20,000 traditional IRA distribution (line 4b). Pension worksheet for 2025: 75% of $20,000 is $15,000, plus $30,000 = $45,000. Federal AGI of $121,250 is in the $120,000 to $124,999 row, so the decimal is .25, and the subtraction is $11,250. Connecticut AGI = $110,000. Exemption $0 (more than $71,000). Table B: $4,000 plus 5.5% of $10,000 ($550) = $4,550. Table C: more than $105,500 and not more than $110,500, so $100. Table D: $0. Table E: .00. **2025 tax: $4,650.** For 2026 with the same facts, 100% of the IRA counts: $50,000 x .25 = $12,500, so Connecticut AGI would be $108,750.

**Case 3: lower-income single filer with property tax, 2026.** Connecticut AGI $40,000. Table A: more than $39,000 and not more than $40,000 gives a $5,000 exemption, so taxable income is $35,000. Table B: $200 plus 4.5% of $25,000 ($1,125) = $1,325. Tables C and D: $0. Table E: .10 (more than $33,300 and not more than $60,000), so the credit is $132.50 and the tax is $1,192.50. The client paid $2,400 of property tax on their home in 2026. AGI is not more than $49,500, so the full $300 property tax credit applies (below the tax on Line 10). **Tax after the credit: $892.50.**

**Case 4: property tax credit phase-out, 2025.** Married filing jointly, Connecticut AGI $95,000, qualifying property tax paid $1,800. Credit before phase-out: the lesser of $1,800 and $300 = $300. AGI is more than $90,500 and not more than $100,500, so the decimal is .45: $300 x .45 = $135 reduction. **Credit: $165.**

**Case 5: Social Security above the threshold, 2025.** Single, federal AGI $80,000, including $17,000 of federally taxable benefits. Federal worksheet line 1 is $20,000 and line 9 is $30,000. C = $20,000; D = 25% = $5,000; E = $17,000. **Subtraction on Line 41: $12,000**, so Connecticut taxes $5,000 of the benefits.

**Case 6: bonus depreciation and section 179, 2025.** A sole proprietor deducted $50,000 of section 168(k) bonus depreciation and a $40,000 section 179 deduction federally. Connecticut additions: $50,000 (Line 36) and 80% of $40,000 = $32,000 (Line 36a). In each of 2026 to 2029: subtract 25% of $50,000 = $12,500 (Line 48a) and 25% of $32,000 = $8,000 (Line 49).

**Case 7: PE tax member, 2025.** A resident is a partner in a Connecticut partnership that elected the PE tax. The partner's share of the entity's tax base is $100,000, so the partner's share of PE tax is 6.99% = $6,990. **PE Tax Credit: 87.5% x $6,990 = $6,116.25**, entered on Line 20c with Schedule CT-PE attached. If it exceeds the partner's Connecticut tax, the excess is refunded, without interest.

**Case 8: high-income single filer, 2026.** Connecticut AGI $600,000. Exemption $0. Table B: $31,250 plus 6.99% of $100,000 ($6,990) = $38,240. Table C: $250. Table D: $3,400. Table E: .00. **Tax: $41,890.**

## When to refuse or refer

- Part-year residents, nonresidents, or anyone whose residency is disputed (domicile, the permanent place of abode and more-than-183-days test, Group A or Group B). Refer.
- Clients with a federal AMT liability (Form CT-6251), or a prior-year Connecticut AMT credit.
- Multistate business income that needs allocation or apportionment, the Schedule 2 credit with more than one jurisdiction, city-and-state overlaps, or a "convenience of the employer" dispute with another state.
- The PE tax election decision itself, tiered partnerships, or a PE Tax Credit that does not match Schedule CT K-1.
- Research expenditure deductions under IRC § 174A or Section 70302(f) of P.L. 119-21 in a pass-through or Schedule C business, until DRS confirms the personal income tax treatment.
- Angel investor, film, historic homes or other voucher credits; Connecticut estate or gift tax; trusts and estates.
- Audits, DRS notices, penalty waivers and any appeal.
- Any request to hide income, invent expenses or take an aggressive position.

## Filing and payment ([DRS tax information](https://portal.ct.gov/drs/individuals/resident-income-tax/tax-information))

- **2025 returns:** due 15 April 2026 (15th day of the fourth month for non-calendar years; next business day if on a weekend or holiday). Form CT-1040 EXT gives a six-month extension to **15 October 2026**, "to file", not to pay ([2025 Form CT-1040 EXT](https://portal.ct.gov/-/media/drs/forms/2025/income/ct-1040-ext_1225.pdf)). Form CT-1040 EXT is not needed if the client has a federal extension and expects to owe no more Connecticut tax, or pays the expected tax by credit card by the due date.
- **2026 returns:** tax must be fully paid by 15 April 2027, with a timely return or an extension request.
- **Estimated tax for 2026** ([2026 Form CT-1040ES](https://portal.ct.gov/-/media/drs/forms/2025/income/ct1040es-flat0126.pdf)): required if Connecticut tax after withholding and the PE Tax Credit is $1,000 or more **and** withholding (including the PE Tax Credit) is expected to be less than the required annual payment. The required annual payment is the lesser of 90% of the 2026 tax or 100% of the 2025 tax (only if the 2025 return covered 12 months). Installments of 25% of the required annual payment are due 15 April, 15 June, 15 September 2026 and 15 January 2027. On the 90% basis, each installment is 22.5% of the 2026 tax. The annualized income installment method (Worksheet CT-1040 AES) can reduce early installments. Farmers and fishermen make one payment by 15 January 2027 (the lesser of 66 2/3% of 2026 tax or 100% of 2025 tax). A farmer or fisherman who files the 2026 return and pays in full by 1 March 2027 is not charged interest for underpaying estimated tax.
- **Interest on underpaid estimates:** 1% per month or part of a month, per installment, until the earlier of 15 April 2027 or payment. No interest for the missed January installment if the 2026 return is filed and paid in full by 31 January 2027. Use Form CT-2210, or let DRS send a bill.
- **Late payment:** penalty of 10% of the tax due, plus interest at 1% per month or part of a month from the due date. Interest cannot be waived. With a granted extension, there is no late payment penalty if at least 90% of the tax was paid by the original due date and the rest is paid with the return by the extended date.
- **Late filing with no tax due:** DRS may impose a $50 penalty. If DRS files the return for the client, the penalty is 10% of the balance due or $50, whichever is greater ([DRS tax information](https://portal.ct.gov/drs/individuals/resident-income-tax/tax-information)).
- **Hardship:** Form CT-1127 can give up to six months more to pay; interest still runs from the original due date.
- File and pay through myconneCT or approved software; by mail, use Form CT-1040V or CT-1040ES.

## Completion checklist ([2025 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

- [ ] Residency and filing status confirmed; Form CT-1040 is the right return.
- [ ] Line 1 equals federal Form 1040 line 11a; nothing from Schedule 1-A or the QBI deduction applied.
- [ ] 168(k) and 179 add-backs for the year, and the 25% subtractions for the four prior years, entered.
- [ ] Social Security and pension subtractions tested against **federal** AGI, with the right IRA share (75% for 2025, 100% for 2026).
- [ ] Tax Calculation Schedule: Table A on AGI, Table B on taxable income, Tables C, D and E on AGI; single column used for married filing separately in Table D.
- [ ] Schedule 2 attached, or the other state's return kept if e-filed.
- [ ] Property tax credit limited to $300, phased out, only for tax paid in the year.
- [ ] CT EITC: full-year resident, 40% of federal credit, plus $250 with a qualifying child; Schedule CT-EITC attached.
- [ ] PE Tax Credit agrees to Schedule CT K-1; Schedule CT-PE attached.
- [ ] Use tax Line 15 filled in (0 if none).
- [ ] 2026 estimated payments set up, or a reason recorded why none are needed.
- [ ] Return filed and tax paid by 15 April, or Form CT-1040 EXT filed with payment by then.

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
