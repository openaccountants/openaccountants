---
name: ab-corporate-tax
description: Use this skill for Alberta provincial corporate income tax. Triggers "Alberta CIT", "AT1 Alberta", "Alberta small business deduction", "Job Creation Tax Cut Alberta", "Alberta corporate tax 8%". ALWAYS read alongside federal T2.
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v2.0 (content)
category: international
version: "2.0"
type: computation
tier: 2
domain: income-tax
---

# AB Corporate Tax

## Scope

> **Scope:** Alberta provincial corporate income tax (Alberta Corporate Tax Act, RSA 2000, c A-15) for tax year 2026. The IEG method here covers current SR&ED costs; eligibility of restored federal capital expenditures is held below pending reconciliation of the operative Alberta text. ALWAYS load this skill alongside the federal T2 skill :  Alberta is a non-agreeing province for corporate tax and runs its own AT1 system in parallel with the federal T2.

## Ask the client first

1. **Permanent establishment (PE)** in Alberta :  confirmed via federal Schedule 5 allocation
2. **Alberta taxable income allocation** :  % of taxable income earned in Alberta (Schedule 5, federal T2)
3. **Active business income (ABI)**, aggregate investment income and adjusted aggregate investment income (AAII), with their different purposes
4. **CCPC status** for the entire tax year
5. **Associated corporation group** :  for SBD limit sharing
6. **Federal SR&ED current expenditures and reconciliation**: T661 line 557 for the 2026 IEG current-cost method
7. **Fiscal year-end (FYE)** date
8. **Alberta Corporate Account Number (CAN)** :  Corporate Access Number on the Alberta Certificate of Incorporation, not a guessed-length identifier


Ask also for prior-year associated-group taxable capital and adjusted aggregate investment income, Alberta income/CCA differences, prior AT1 assessments and payments, short tax years, SR&ED current expenditure reconciliation and documented Alberta work location.

## The method, step by step

### 1. Quick reference :  Alberta vs federal combined CIT

**Quick reference :  Alberta vs federal combined CIT**

| Income type | Federal | Alberta | **Combined** | Official source |
| --- | --- | --- | --- | --- |
| **General active business income** | 15% | **8%** | **23%** | https://kings-printer.alberta.ca/documents/Acts/A15.pdf ; https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| **SBD income** (first $500,000 active business income, CCPC) | 9% | **2%** | **11%** | https://kings-printer.alberta.ca/documents/Acts/A15.pdf ; https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| **Investment income (CCPC, non-active)** | 38 2/3% before dividend refund, foreign-tax and other adjustments | 8% | 46 2/3% before refunds/credits | https://kings-printer.alberta.ca/documents/Acts/A15.pdf ; https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-123.3.html ; https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-129.html |
| **Ordinary M&P income** (no separate AB rate; special qualifying zero-emission technology rates require the federal method) | 15% | 8% | 23% | https://kings-printer.alberta.ca/documents/Acts/A15.pdf ; https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |

Alberta has the **lowest general provincial corporate income tax rate in Canada** following the Job Creation Tax Cut (Bill 3, 2019), which reduced the general rate from 12% to 8% in stages from 12% to 11% on July 1, 2019, 10% on January 1, 2020 and 8% on July 1, 2020; the final reduction was accelerated.

**Comparable provinces (2026 general rate):**
- Alberta: 8%
- BC: 12%
- Saskatchewan: 12%
- Manitoba: 12%
- Ontario: 11.5%
- Quebec: load the separate Quebec method; the CRA comparison table expressly excludes it

### 3. General rate :  8% (Job Creation Tax Cut)

- **General corporate income tax rate**: 8% throughout an ordinary 2026 year; historical rate-change straddlers use the section 21 daily formula  _(s.21 of the Alberta Corporate Tax Act)_

### Rate history (Job Creation Tax Cut, Bill 3, 2019)

**Rate history (Job Creation Tax Cut, Bill 3, 2019)**

| Effective date | General rate | Official source |
| --- | --- | --- |
| Before July 1, 2019 | 12% | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |
| July 1, 2019 | 11% | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |
| January 1, 2020 | 10% | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |
| July 1, 2020 | **8%** (accelerated from the originally planned 2022) | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |
| 2026 | **8%** (current) | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |

- **Combined federal + Alberta general rate** :  23% (15% federal + 8% AB)

### Straddling tax years

- **Proration for straddling fiscal years** :  A corporation with a fiscal year straddling a rate change date must prorate. For 2026, the rate has been stable at 8% since July 1, 2020, so no proration applies to any FYE in 2026.

### 4. Small Business Deduction (SBD) :  2% Alberta rate

- **SBD availability** :  Alberta provides a small business deduction under s.22 of the Alberta Corporate Tax Act on the first $500,000 of active business income of a Canadian-controlled private corporation (CCPC).  _(s.22 of the Alberta Corporate Tax Act)_

### Effective rates

- **Alberta SBD rate** :  2% (general rate of 8% minus SBD of 6%)
- **Federal SBD rate**: ordinary 9% after the 38% basic rate, 10% federal abatement and 19% small business deduction; the general tax reduction is not stacked on this same income
- **Combined federal + AB SBD rate** :  11% (on first $500,000 ABI)

### Business limit grind

- **Taxable capital employed in Canada (TCEC) grind** :  Alberta mirrors the federal grind :  the $500,000 business limit is reduced where TCEC of the associated group exceeds $10M, fully phased out at $50M (consistent with the federal expansion applicable to years beginning on or after April 7, 2022 from the prior $10M-$15M phase-out band).
- **Passive investment income grind** :  ACTA 22(4) incorporates ITA 125(5.1): using group AAII for years ending in the preceding calendar year, the full $500,000 limit falls by $5 per $1 above $50,000 and reaches nil at $150,000. Scale the reduction where the otherwise available business limit is smaller; do not subtract the full-limit reduction from an already allocated partial limit.  _(ITA s.125(5.1))_
- **Associated corporations sharing** :  Associated corporations must share the $500,000 business limit via AB Schedule 3 (mirrors federal T2 Schedule 23 allocation).

The section 125(5.1) reduction is the **greater of**, not the sum of, the capital and passive-income reductions. For a tax year shorter than 51 weeks, section 125(5)(b) prorates the business limit by days / 365. Confirm association, the relevant preceding-year capital and each group member's prior-calendar-year AAII before filing. [ACTA 22(4)](https://kings-printer.alberta.ca/documents/Acts/A15.pdf), [ITA 125(5)-(5.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-125.html).

### Specified Investment Business (SIB) and Personal Services Business (PSB)

- **SIB income** :  SIB income does not qualify for the SBD; taxed at 8% Alberta general rate (plus federal refundable rates on investment income).
- **PSB income** :  PSB income is excluded from the SBD by ITA s.125(7); Alberta follows. PSB also faces the federal 5% additional tax under ITA s.123.5 :  Alberta does not apply an additional provincial PSB surtax.  _(ITA s.125(7); ITA s.123.5)_

### 5. AT1 return :  Alberta's standalone corporate tax return

Alberta is one of the two provinces without a current CRA corporation tax collection agreement, alongside Quebec; Ontario is administered by CRA. Corporations with a PE in Alberta file:

- **Federal T2** with the Canada Revenue Agency (CRA), AND
- **AT1 :  Alberta Corporate Income Tax Return** with **Alberta Tax and Revenue Administration (TRA)**

> Note: Alberta participates in the federal-provincial Tax Collection Agreement (TCA) for **individuals** (CRA administers the AB personal income tax under the same T1), but **not for corporations**. The AT1 system is administered directly by TRA at Alberta Treasury Board and Finance.

### AT1 return and current schedules

Reconcile Alberta taxable income separately; discretionary CCA or other deductions can differ from federal. The live TRA form list supplies these titles, rather than federal schedule numbers reused as Alberta numbers. Do not file a non-existent schedule because its number looks familiar.

| Form | Purpose and condition | Official source |
| --- | --- | --- |
| AT1 | Identification, tax year, Alberta taxable income, deductions, credits and balance; use the current form and software fields | https://www.alberta.ca/corporate-income-tax |
| Schedule 1 / AT2 | Alberta small business deduction; associated business-limit evidence must agree with the federal agreement, ACTA 22(3) | https://www.alberta.ca/corporate-income-tax |
| Schedule 2 / AT271 | Alberta income allocation factor, coordinated with federal Schedule 5 | https://www.alberta.ca/corporate-income-tax |
| Schedule 3 / AT3 | Other tax deductions and credits; not the associated-group SBD allocation form | https://www.alberta.ca/corporate-income-tax |
| Schedule 4 / AT201 | Foreign investment income tax credit on foreign non-business sources; not a separate business-income credit | https://www.alberta.ca/corporate-income-tax |
| Schedule 10 / AT293 | Loss carry-back application; not loss carry-forward continuity | https://www.alberta.ca/corporate-income-tax |
| Schedule 12 / AT112 | Alberta income/loss reconciliation to federal amounts | https://www.alberta.ca/corporate-income-tax |
| Schedule 13 / AT13 | Capital cost allowance, including the applicable Class 14.1 treatment; not IEG or historic Schedule 14 | https://www.alberta.ca/corporate-income-tax |
| Schedule 18 / AT18 | Dispositions of capital property, including the appropriate capital-gain/LPP treatment; not PE allocation | https://www.alberta.ca/corporate-income-tax |
| Schedule 21 / AT173 | Calculation of current-year loss and continuity of losses; not the tax payable schedule | https://www.alberta.ca/corporate-income-tax |
| Schedule 29 / AT29 | Innovation Employment Grant calculation and associated agreements; retain project details on AT4970 for production on request | https://www.alberta.ca/corporate-income-tax |

The old Schedule 9/LPP and Schedule 14/CEC assertions are not current form directions; use Schedule 18 for relevant dispositions and Schedule 13 for CCA. Historic SR&ED forms and CEC years require the form applicable to that old year, not a 2026 claim.

### Filing channel

- **Net file AT1** through TRA-certified return software, then transmit and retain the accepted confirmation. TRACS is for account management, documents and notices, not the certified return-preparation channel
- **Software selection**: use the current TRA-certified product/version list; do not rely on a static vendor list
- **Electronic filing**: for years beginning after December 31, 2024, prescribed corporations must net file except insurance corporations, non-resident corporations, functional-currency filers and ACTA section 35 exempt corporations. A paid preparer preparing more than five AT1 returns in a calendar year also has a separate mandate, with the listed exclusions and employee exception

### Account number

- Use the **Alberta Corporate Account Number (CAN)**, which is the Corporate Access Number shown on the certificate; establish the correct extra-provincial registration/account where applicable
- TRACS enrolment is separate from net file: no registration or access code is needed just to net file an AT1

### 6. Filing deadlines

**Filing deadlines**

| Item | Deadline | Official source |
| --- | --- | --- |
| **AT1 return filing** | **6 months after FYE** (same as federal T2) | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |
| **AT1 tax payment** | Generally end of 2nd month after FYE; qualifying CCPC exemptions below allow end of 3rd month | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |
| **Instalments** | Generally monthly, last day of each tax-year month; Alberta exemptions below are not the federal quarterly regime | https://www.alberta.ca/corporate-income-tax |
| **Notice of objection** | 90 days from Notice of (Re)assessment | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |
| **Record retention** | Generally 6 years from the last relevant tax year; prescribed-period records, late returns and objections/appeals have the ACTA 61 exceptions | https://kings-printer.alberta.ca/documents/Acts/A15.pdf |

### Alberta instalment exemptions and notices

Under ACTA section 38, ordinary instalments are monthly using one of the current-year estimate, first instalment base, or mixed second/first instalment-base methods. A full-year CCPC is exempt from instalments and has a third-month balance date if it claimed Alberta SBD and current taxable income is no more than $500,000, or claimed it in the preceding year with preceding taxable income no more than $500,000, or current tax / first instalment base is no more than $2,000. A non-CCPC meeting the $2,000 test is exempt from instalments but pays at the end of month two. A new corporation other than an amalgamation is exempt in its first year but normally still pays at the end of month two. Weekend/holiday dates move to the next business day. These are **Alberta** rules; do not import federal quarterly instalment eligibility. [ACTA 38](https://kings-printer.alberta.ca/documents/Acts/A15.pdf), [TRA payment requirements](https://www.alberta.ca/corporate-income-tax).

TRA online mail became the default on April 1, 2026 for new incorporations, existing TRACS accounts and corporations with third-party account access. Monitor the authorised TRACS account rather than waiting for paper. A mailing address is not changed by entering a different address on AT1. The announced verified-identity changes start January 30, 2027, so they are not a current November 2026 login requirement. Keep return confirmations, payment references and assessments separately. [TRA notices](https://www.alberta.ca/corporate-income-tax).

### Late filing penalties and corrections

ACTA 37(1) sets a 5% component plus 1% for each complete month, up to 12 months. Its two statutory bases are not identical where refundable credits apply: the initial component includes the listed credit offsets while the monthly component follows paragraph (b). Do not mechanically use tax-before-credits for both. The old claim of an automatic repeat-offender 10% plus 2% for 20 months was not supported by section 37 and is not a usable Alberta rule. Late-payment/instalment interest is prescribed separately and compounds daily; fetch the applicable quarter rather than assuming the CRA rate plus a margin. A corporation's net-file failure penalty is $1,000 (37.3), and a preparer's is $100 per failure (37.4). [ACTA 37-38](https://kings-printer.alberta.ca/documents/Acts/A15.pdf), [TRA](https://www.alberta.ca/corporate-income-tax).

Federal assessment changes affecting an Alberta balance and errors discovered within the normal reassessment period require the information/amended AT1 under **ACTA 36.2**, generally within 90 days of the later of the event and the original filing due date. File a separate objection for each year/assessment within 90 days of the notice date; apply for an extension if late, with the outer one-year-plus-90-day limit. R-AB-CIT-8 still refers disputes to a practitioner. [ACTA 36.2](https://kings-printer.alberta.ca/documents/Acts/A15.pdf), [TRA objections](https://www.alberta.ca/corporate-income-tax).

### 7. Alberta Investor Tax Credit (AITC): historical certificates only

This is not an open 2026 investment incentive. For corporate claims, **ACTA 25.01** defines the balance from valid certificates for purchases in the current and four preceding taxation years, less previous deductions. The deduction is limited to available tax after sections 22/23; certificates must not be cancelled and may be requested by TRA. The rule carries into qualifying amalgamations and wind-ups. Do not assume a 2019 certificate remains usable in an ordinary 2026 year, or that a personal $60,000 annual cap is a corporate cap. Reconcile the original investment, certificate date, prior claims and actual tax-year lengths. [ACTA 25.01](https://kings-printer.alberta.ca/documents/Acts/A15.pdf).

Historical programme rates, recipient caps and sunset dates are not used to calculate a current corporate claim; confirmation gaps are recorded under Sources.

### 8. Capital Investment Tax Credit (CITC): historical certificates only

Do not offer a new 2026 CITC investment approval. For a valid existing corporate certificate, **ACTA 25.02** includes the acquisition year's amount and ten preceding taxation years, less prior deductions. The deduction is non-refundable, limited to available tax after sections 22/23, and certificates are applied in issue order. Revoked, renounced or cancelled certificates do not count. Keep the TRA certificate/approval letter and acquisition evidence; check amalgamation or wind-up continuity where relevant. [ACTA 25.02](https://kings-printer.alberta.ca/documents/Acts/A15.pdf).

For a historical certificate the original programme and approval terms must support the amount. Unconfirmed programme rates, project limits and sunset dates are recorded under Sources.

### 9. Innovation Employment Grant (IEG) :  refundable R&D credit

The IEG is Alberta's refundable R&D tax credit, introduced effective January 1, 2021 to partially replace the wound-down Alberta SR&ED tax credit (which was eliminated effective January 1, 2020).

### Rate structure (ss.26.95-26.98 Alberta Corporate Tax Act)

**Rate structure (ss.26.95-26.98 Alberta Corporate Tax Act)**  _(ss.26.95-26.98 Alberta Corporate Tax Act)_

| Tier | Rate | Base | Official source |
| --- | --- | --- | --- |
| **Base credit** | **8%** | First **$4M** of eligible R&D expenditures (in Alberta) | https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf |
| **Incremental credit** | **12% additional** | Expenditures **above the prior 2-year average** R&D spend, up to the $4M cap | https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf |

### Eligibility

- **IEG eligibility criteria** :  - Corporation with **PE in Alberta** at any time in the tax year - Eligible expenditures = the Alberta-adjusted portion of **federal current SR&ED expenditures at T661 line 557** for years ending after December 15, 2024; use the June 2026 guide, location evidence and two-step reconciliation below - **Refundable**: Excess credit over Alberta tax payable refunded to the corporation (no carry-forward needed)  _(ITA s.37; Regulation 2900)_

### Expenditure cap

- **IEG expenditure cap rules** :  - The **$4M expenditure cap** is shared among **associated corporations** - The cap is **prorated** for short tax years

### Claim mechanics

- **IEG claim filing mechanics** :  - File **AT1 Schedule 29** (detailed eligible expenditures, allocation among associated group) - File **AT1** (claim the Schedule 29 amount in the return; Schedule 13 is CCA) - Reconciles to **federal T661** (SR&ED claim) line entries restricted to Alberta-located expenditures

### Interaction with federal SR&ED

- The IEG and federal SR&ED may support the same project, but the IEG is provincial government assistance that must be reflected in the federal expenditure/assistance computation. Follow the two-step AT29/T661 reconciliation below rather than claiming both on an unreduced pool or asserting an unconditional receipt-year income inclusion and no Alberta adjustment. [June 2026 IEG guide](https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf).

### 10. Investment income and federal coordination

Alberta applies its 8% general rate to ordinary investment taxable income; there is no separate Alberta RDTOH account. Federal CCPC investment tax is not the 15% active-business rate: ordinary investment income can face 38 2/3% federal Part I before foreign credits and other adjustments, including 10 2/3 percentage points of additional refundable tax under ITA 123.3. **10 2/3% is not the total refundable component**; the federal refundable portion calculation under ITA 129(4) can reach 30 2/3% of aggregate investment income subject to its limits. Together with Alberta 8%, the simple pre-refund combined illustration is 46 2/3%, not a final effective tax rate. Canadian dividends, foreign investment income/credits and dividend refunds require the federal T2 method; do not apply that illustration to every investment receipt. The old Saskatchewan surtax comparison is not an Alberta rule and has not been verified here. [ACTA 21](https://kings-printer.alberta.ca/documents/Acts/A15.pdf), [ITA 123.3](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-123.3.html), [ITA 129](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-129.html).

## Worked cases

### Case 1: Calgary tech CCPC

### Facts

- **Corporation**: Cascade Code Inc., a CCPC incorporated in Alberta, FYE December 31, 2026
- **Single PE**: Calgary, Alberta (100% Alberta allocation per federal Schedule 5)
- **Gross revenue**: $2,000,000 (Canadian-source SaaS development services)
- **Net income for tax purposes (line 300, federal T2)**: $400,000
- **Active business income (ABI)**: $300,000 (after federal Schedule 7 calculation)
- **Investment income**: $20,000 (interest on cash reserves)
- **Taxable capital employed in Canada (TCEC)**: $3,200,000 (below $10M :  no TCEC grind)
- **Associated corporations**: none
- **SR&ED qualified expenditures (Alberta)**: $250,000 (current-year)
- **Prior 2-year average Alberta R&D spend**: $180,000

### Step 1: Federal T2 and taxable-income reconciliation

The original facts reported $400,000 net income, $300,000 ABI and $20,000 interest, leaving $80,000 unclassified. Net income is not automatically taxable income. For this Alberta example, assume the reconciliation establishes **Alberta taxable income of $400,000**, no other credits and **Alberta SBD base of $300,000**. Obtain the remaining income classification before computing federal tax. The old $42,000 federal estimate taxed all $100,000 at 15% even though $20,000 was interest; it is not a valid final federal result. The $27,000 calculation on $300,000 at the ordinary 9% federal small-business rate remains a conditional component only. [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html).

### Step 2 :  Alberta AT1 tax payable, not Schedule 21

- **Alberta taxable income**: $400,000 (100% Alberta allocation)
- **SBD-rate portion** (matches federal SBD claim): $300,000 × **2%** = **$6,000**
- **General-rate portion**: $100,000 × **8%** = **$8,000**
- **Alberta tax before credits**: **$14,000**

### Step 3 :  Innovation Employment Grant (AT1 Schedule 29)

- Eligible AB SR&ED expenditures: $250,000
- Prior 2-year average: $180,000
- **Base credit** (8% on first $4M of $250,000): $250,000 × 8% = **$20,000**
- **Incremental credit** (12% additional on amount above prior 2-yr avg, up to $4M cap):
  - Incremental: $250,000 − $180,000 = $70,000
  - 12% × $70,000 = **$8,400**
- **Total IEG**: $20,000 + $8,400 = **$28,400** (refundable)

### Step 4 :  Net AT1 result

- Alberta tax before credits: $14,000
- Less: IEG (refundable): ($28,400)
- **Alberta net refund: $14,400**
- (The IEG creates a refundable position because credits exceed tax payable; TRA issues the refund.)

### Step 5: Federal coordination, not a false combined effective rate

The Alberta result is $14,000 tax less $28,400 IEG, a $14,400 refundable excess before other balances and verification. Do not retain the old $56,000 combined tax / 14% effective rate: the federal income classification is incomplete and federal SR&ED assistance adjustments are not yet calculated. Compute federal SR&ED and RDTOH separately, then reconcile the two returns. [IEG guide](https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf).

### Step 6 :  Deliverables for the client

1. AT1 return + Schedules 1 and 29, plus any actual CCA, loss, allocation and reconciliation schedules required
2. Federal T2 with consistent Schedule 1, 7, 23, 31, 49 entries
3. T661 federal SR&ED claim (Alberta-located expenditures flagged for IEG cross-reference)
4. Alberta refundable excess $14,400 on these assumptions; payment follows CRA expense verification and TRA Alberta-location confirmation, with no guaranteed 6-9 month time
5. Instalment recalculation for the following year using the actual assessment and Alberta exemption tests

```oa-check
name: Calgary CCPC Alberta tax and corrected IEG, 2026
inputs:
  taxable_income: 400000
  sbd_base: 300000
  eligible_expenditures: 250000
  base_spending: 180000
steps:
  - alberta_before_credits: sbd_base * 0.02 + (taxable_income - sbd_base) * 0.08
  - grant_base: min(eligible_expenditures, 4000000) * 0.08
  - grant_incremental: max(0, min(eligible_expenditures, 4000000) - base_spending) * 0.12
  - ieg: grant_base + grant_incremental
  - refundable_excess: max(0, ieg - alberta_before_credits)
expected:
  alberta_before_credits: 14000
  grant_base: 20000
  grant_incremental: 8400
  ieg: 28400
  refundable_excess: 14400
```

### Case 2: IEG taxable-capital boundary and independent instalment decision

My unassociated Alberta corporation has $200,000 eligible current Alberta SR&ED spending, a two-year base of $250,000 and preceding-year taxable capital of $30 million. There is no incremental credit because spending is below the base. The ordinary $16,000 grant is reduced by the capital factor ($50 million - $30 million) / $40 million to **$8,000**. At $50 million of taxable capital it is nil. Independently, a full-year CCPC with a $1,900 first instalment base qualifies for Alberta's no-instalment/third-month-payment rule; a non-CCPC with the same base still has the second-month balance date. The IEG phase-out is not the SBD phase-out or federal quarterly-payment test. [IEG guide](https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf), [ACTA 38](https://kings-printer.alberta.ca/documents/Acts/A15.pdf).

```oa-check
name: IEG below historic spending, taxable-capital phase-out
inputs:
  expenditure: 200000
  historical_base: 250000
  taxable_capital: 30000000
steps:
  - base_credit: min(expenditure, 4000000) * 0.08
  - additional_credit: max(0, min(expenditure, 4000000) - historical_base) * 0.12
  - capital_factor: min(1, max(0, (50000000 - taxable_capital) / 40000000))
  - net_ieg: (base_credit + additional_credit) * capital_factor
  - upper_boundary_grant: (base_credit + additional_credit) * max(0, (50000000 - 50000000) / 40000000)
expected:
  base_credit: 16000
  additional_credit: 0
  capital_factor: 0.5
  net_ieg: 8000
  upper_boundary_grant: 0
```

### IEG filing safeguards and federal expenditure reconciliation

For 2026 use **federal current SR&ED expenditures at T661 line 557**, not all restored federal capital expenditure at line 559. The June 30, 2026 Alberta guide expressly distinguishes years ending after December 15, 2024 from the older line-559 basis. Prepare AT4970 project records first; it need not be filed but must be produced on request. In AT29 enter Alberta-located spending, subtract the federal proxy and add the allowed Alberta proxy; the latter is generally 55% of qualifying Alberta salaries, subject to its limits. Include prescribed assistance adjustments, recapture and any valid transfers; neither a federal SR&ED acceptance nor an Alberta employee address alone proves that every remote expenditure is Alberta eligible. [June 2026 IEG guide, pages 1 and 4-6](https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf).

For an unassociated full-year corporation, use the lower of actual eligible expenditure and $4 million. A short year prorates the expenditure cap by days / 365, or 366 where February 29 is included. Associated corporations must allocate the cap and incremental allowed amount using the AT29 group agreement: do not simply multiply the company's own spending by 20%. The unassociated spending base averages the two preceding years, counting a missing/zero year as zero rather than dividing by one. The grant has a separate taxable-capital reduction from $10 million to $50 million. [IEG guide, expenditure limit, base and capital-grind sections](https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf).

Calculate provisional AT29 **line 130**, include it in the federal provincial-assistance computation, then perform the guide's **Step 2** to re-enter T661 expenditure at AT29 **003/005** and add the IEG already reducing federal expenditure at **011**, avoiding a circular calculation. Finish **031** eligible expenditure and **134** net grant after recapture; reconcile the figure to AT1. Payment awaits CRA verification and TRA location checks. [IEG guide, Step 1 and Step 2](https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf).

## When to refuse or refer

- **R-AB-CIT-1** :  Multi-provincial PE allocation with disputed Schedule 5 attribution
- **R-AB-CIT-2** :  Non-resident corporation carrying on business in Alberta (Part XIV branch tax interaction)
- **R-AB-CIT-3** :  Insurance corporations, banks, and financial institutions (special AT1 schedules)
- **R-AB-CIT-4** :  Crown corporations, exempt entities under s.35 of the Act
- **R-AB-CIT-5** :  Mutual fund corporations, mortgage investment corporations
- **R-AB-CIT-6** :  Reorganizations involving Alberta-allocated assets (s.85, s.86, s.87 with cross-border consequences)
- **R-AB-CIT-7** :  Voluntary disclosure under the Alberta TRA VDP :  credentialed practitioner only
- **R-AB-CIT-8** :  AT1 objections, notices of appeal, Alberta Court of King's Bench tax matters


### 12. Conservative defaults

- **Conservative default rules** :  When information is missing, the skill applies these conservative defaults (always flag for reviewer confirmation): 1. **Allocation %**: If federal Schedule 5 not yet finalized, assume **100% Alberta** only when the corporation has confirmed sole-PE Alberta status; otherwise **refuse** and request allocation. 2. **CCPC status**: Confirm CCPC status throughout the year :  do **not** assume; non-CCPC status disqualifies SBD entirely. 3. **Associated group sharing**: Default the SBD allocation to **$0 for the subject corporation** until associated group T2-Sch 23 allocation is confirmed in writing. 4. **TCEC grind**: If group capital is near $10M, withhold the final SBD/grant result until the preceding-year Schedule 33 and group computation are available; do not report an invented full grind as the tax due. 5. **IEG prior-2-year average**: If unavailable, show **8% before capital reduction and recapture only as a provisional ceiling for that component**, not a final grant; obtain the two historic years and associated allocation before filing. 6. **IEG eligibility**: Apply **only to expenditures with documented Alberta location** (work performed at AB PE, AB-resident employees); refuse to extend to ambiguous remote-work expenditures without payroll address evidence. 7. **AITC / CITC carry-forwards**: Assume **none** unless prior AT1 credit continuity / TRA certificate and approval letter confirms balance. 8. **Instalment base**: Default to **prior-year method** unless current-year estimate is substantially lower and documented. 9. **Filing penalty exposure**: Flag any late filing :  even by 1 day :  for immediate reviewer escalation.

#
## Completion checklist

- Confirm PE, CAN, tax-year length, whole-year CCPC status and the federal/Alberta income reconciliation.
- Complete the correct SBD/allocation/CCA/loss/credit schedules rather than the former erroneous schedule list.
- Calculate federal T2 separately; reconcile SR&ED and assistance through both AT29 steps.
- Apply Alberta instalment exemptions, balance date and actual quarter's interest rate.
- Retain the net-file acknowledgement, payment reference, AT4970 evidence, assessment and TRACS mail alert.

## Sources

| Official source | Read date | What was read and used |
|---|---|---|
| https://kings-printer.alberta.ca/documents/Acts/A15.pdf | 2026-11-14 | Read for: March 26, 2026 consolidation; sections 21-22 (rate/history/SBD and federal incorporation), 25.01-25.02 (historic certificates), 26.95-26.98 (IEG), 36.2-38 (amendments, penalties and payments), 39 interest and 61 records |
| https://www.alberta.ca/corporate-income-tax | 2026-11-14 | Read for: Who files, current form/schedule titles, CAN, certified net file and exceptions, instalment exemptions, balance dates, TRACS notices, objections and IEG payment conditions |
| https://www.alberta.ca/innovation-employment-grant | 2026-11-14 | Read for: Grant eligibility, base/incremental rates, capital phase-out and federal/provincial verification |
| https://www.alberta.ca/system/files/custom_downloaded_images/tra-guide-claiming-the-innovation-employment-grant.pdf | 2026-11-14 | Read for: June 30, 2026 guide: current-versus-qualified T661 expenditure, AT4970 and AT29 lines, two-step assistance reconciliation, group cap, base averaging, short years and capital grind |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html | 2026-11-14 | Read for: Ordinary federal general/small-business rates and provincial comparison table; special zero-emission and bank rates are outside this ordinary illustration |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-125.html | 2026-11-14 | Read for: ITA 125(2)-(5.1), group allocation, shortened years and capital/passive-income limit reductions incorporated by ACTA 22(4) |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-123.3.html | 2026-11-14 | Read for: Additional federal refundable tax on CCPC aggregate investment income |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-129.html | 2026-11-14 | Read for: Subsection 4 refundable portion definition and limits, distinct from the additional tax rate |

Not yet confirmed: the quarter-specific Alberta interest rate, the old Quebec 11.5% comparison rate, individual historic AITC/CITC programme termination and investment caps (old 30%/$60,000/$5 million/March 30, 2020 AITC and 10%/$1 million/$5 million/2020 CITC statements), and historic Schedule 9/14 form versions. The former claimed Alberta repeat-offender 10%/2%/20-month penalty and Saskatchewan investment surtax comparison are unsupported by the sources read and must not be used. The historical credit topics are retained above using current certificate/carry rules. The 2026 IEG guide updates federal expenditure references beyond the March 2026 Act consolidation; if a claim relies on a later enacted Alberta amendment, obtain that operative text before extending the grant to restored federal capital costs. The final federal tax on the worked company's unclassified $80,000 income and assistance/RDTOH adjustments is not determined here.
