---
name: deadline-engine
description: >
  Intelligence skill that generates a personalised filing calendar based on the user's jurisdiction and obligations. Looks up deadlines from a master table covering 15 jurisdictions, produces a sorted 12-month calendar, flags approaching deadlines with amber (30 days) and red (7 days) urgency, and calculates late-filing penalties by referencing each jurisdiction's penalty rules.
version: 0.1
category: intelligence
depends_on:
  - workflow-base
triggers:
  - filing calendar
  - deadline calendar
  - when is my tax due
  - upcoming deadlines
  - filing deadlines
  - what do I need to file
---

# Deadline Engine v0.1

## What this file is

**Obligation category:** INTEL (Intelligence / Cross-cutting)
**Functional role:** Calendar generation, deadline tracking, penalty estimation
**Status:** Active

This is an intelligence skill that loads on top of `workflow-base`. Unlike content skills that compute a single obligation, this skill reads the user's full obligation profile and produces a consolidated filing calendar.

**The reviewer is the customer of this output.** The calendar and penalty estimates are working aids for a credentialed reviewer, not direct advice to the taxpayer.

> **Disclaimer.** This skill provides deadline information based on general statutory rules for the jurisdictions listed. Actual deadlines may vary due to weekends, public holidays, individual extensions, agent lodgement schedules, or legislative changes. All dates must be verified by a credentialed professional in the relevant jurisdiction before reliance. OpenAccountants does not guarantee the accuracy of any deadline and accepts no liability for late filings. This is not legal or tax advice.

---

## Section 1 -- Scope statement

This skill covers:

- **Jurisdictions:** US (federal + CA), MT, GB, DE, AU, CA (Canada), IN, ES, NL, SG (15 jurisdiction-obligation combinations)
- **Obligation types:** Income tax, estimated/provisional tax, VAT/GST/BTW, social security contributions
- **Output:** Sorted 12-month calendar, urgency flags, penalty estimates

This skill does NOT cover:

- Corporate tax returns, payroll obligations, or employer filings
- Extension requests or amended return deadlines (beyond noting extension availability)
- Sub-national deadlines beyond US-CA (other US states, German Laender, Australian states, etc.)
- Deadlines for obligations not listed in the master table

---

## Section 2 -- Workflow

### Step 0 -- Read the user's obligation profile

Read the user's jurisdiction and obligation types from one of these sources, in priority order:

1. **Intake manifest** -- the structured output from an intake skill (e.g., `us-ca-freelance-intake`)
2. **Explicit user statement** -- "I'm a freelancer in Malta" or "I file in the UK and Germany"
3. **Prior conversation context** -- jurisdiction identified in an earlier turn

If no jurisdiction can be determined, ask:

> "Which country (or countries) do you file taxes in? And what types of obligations do you have -- income tax, VAT/GST, estimated tax payments, social security?"

Do not proceed until at least one jurisdiction is confirmed.

### Step 1 -- Look up filing deadlines

Match the user's jurisdiction + obligation types against the **Master Deadline Table** in Section 3. Pull every matching row.

### Step 2 -- Generate the calendar

1. Anchor to today's date.
2. For each matched obligation, compute the next 12 months of concrete deadline dates.
3. Adjust for weekends: if a deadline falls on a Saturday, move to the preceding Friday; if on a Sunday, move to the following Monday -- unless the jurisdiction has a different convention (noted in the table).
4. Sort all deadlines chronologically.
5. Present as a table:

```
| # | Date | Jurisdiction | Obligation | Form | Action required | Urgency |
|---|------|--------------|------------|------|-----------------|---------|
```

### Step 3 -- Flag approaching deadlines

Apply urgency flags based on days until deadline from today's date:

| Days remaining | Flag | Label |
|---|---|---|
| > 30 days | -- | On track |
| 8--30 days | AMBER | Approaching |
| 0--7 days | RED | Urgent |
| Past due | RED | OVERDUE |

If any deadline is OVERDUE, add a penalty estimate (Step 4) automatically.

### Step 4 -- Calculate penalties for late filing

When a deadline is past due or when the user asks "what if I file late?", compute the estimated penalty using the jurisdiction's penalty rules. Reference the relevant content skill for precise penalty logic. If no content skill is loaded for that jurisdiction, use the penalty summary in Section 4 of this file and flag the estimate as T2 (reviewer judgment required).

Always state: "Penalty estimates are approximations. Actual penalties depend on the amount of tax owed, the length of delay, and jurisdiction-specific rules. A credentialed professional should confirm."

---

## Section 3 -- Master Deadline Table

### 3.1 United States -- Federal

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Federal income tax (filing + payment) | 1040 | Annual | Apr 15 | Auto-extends to Oct 15 for filing (not payment) via Form 4868 |
| Estimated tax -- Q1 | 1040-ES | Quarterly | Apr 15 | Based on prior-year or current-year liability |
| Estimated tax -- Q2 | 1040-ES | Quarterly | Jun 15 | |
| Estimated tax -- Q3 | 1040-ES | Quarterly | Sep 15 | |
| Estimated tax -- Q4 | 1040-ES | Quarterly | Jan 15 (next year) | |

### 3.2 United States -- California

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| CA individual income tax | 540 | Annual | Apr 15 | Conforms to federal date; auto-extends to Oct 15 |
| CA SMLLC annual tax | 568 | Annual | Apr 15 | $800 minimum franchise tax due regardless of income |
| CA estimated tax | 540-ES | Quarterly | Apr 15, Jun 15, Sep 15, Jan 15 | 30/40/0/30 schedule |

### 3.3 Malta

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Income tax return | TA24 | Annual | Jun 30 | For self-employed / self-occupied |
| VAT return | VAT3 | Quarterly | 45 days after quarter end | Quarters: Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec |
| Social security contributions (Class 2) | SSC | Quarterly | Apr 30, Jul 31, Oct 31, Jan 31 | Self-occupied persons |
| Provisional tax -- 1st instalment | PT | Annual | Apr 30 | 20% of prior-year liability |
| Provisional tax -- 2nd instalment | PT | Annual | Aug 31 | 30% of prior-year liability |
| Provisional tax -- 3rd instalment | PT | Annual | Dec 21 | 50% of prior-year liability |

### 3.4 United Kingdom

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Self Assessment (online) | SA100 | Annual | Jan 31 | For tax year ending prior Apr 5 |
| Self Assessment (paper) | SA100 | Annual | Oct 31 | Paper filing deadline |
| Payment on Account -- 1st | POA | Semi-annual | Jan 31 | 50% of prior-year liability |
| Payment on Account -- 2nd | POA | Semi-annual | Jul 31 | 50% of prior-year liability |
| Balancing payment | SA100 | Annual | Jan 31 | Difference from POAs |
| VAT return | VAT100 | Quarterly | 1 month + 7 days after quarter end | Making Tax Digital; quarters vary by stagger group |

### 3.5 Germany

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Income tax return | ESt (Einkommensteuererklaerung) | Annual | Jul 31 | Extends to end of Feb (+2 years) if filed by Steuerberater |
| VAT return (advance) | UStVA (Umsatzsteuer-Voranmeldung) | Monthly or Quarterly | 10th of following month | Monthly if prior-year VAT > EUR 7,500; quarterly if EUR 1,000--7,500 |
| VAT annual return | UStE | Annual | Jul 31 | Reconciliation return |
| Estimated tax -- Q1 | Vorauszahlung | Quarterly | Mar 10 | Based on Vorauszahlungsbescheid |
| Estimated tax -- Q2 | Vorauszahlung | Quarterly | Jun 10 | |
| Estimated tax -- Q3 | Vorauszahlung | Quarterly | Sep 10 | |
| Estimated tax -- Q4 | Vorauszahlung | Quarterly | Dec 10 | |

### 3.6 Australia

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Income tax return (self-lodged) | ITR | Annual | Oct 31 | For FY ending Jun 30 |
| Income tax return (tax agent) | ITR | Annual | May 15 | Agent lodgement programme; dates vary |
| BAS -- GST (quarterly) | BAS | Quarterly | 28th of month after quarter end | Quarters: Jul-Sep, Oct-Dec, Jan-Mar, Apr-Jun |
| PAYG instalments | BAS/IAS | Quarterly | 28th of month after quarter end | Lodged with BAS if registered for GST |

### 3.7 Canada

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Individual income tax (filing) | T1 | Annual | Jun 15 | Extended filing date for self-employed |
| Individual income tax (payment) | T1 | Annual | Apr 30 | Balance owing due regardless of filing deadline |
| GST/HST return | GST34 | Quarterly or Annual | End of month after reporting period | Annual filers: Jun 15 (sole prop) |
| Instalments -- Q1 | -- | Quarterly | Mar 15 | Required if net tax owing > CAD 3,000 |
| Instalments -- Q2 | -- | Quarterly | Jun 15 | |
| Instalments -- Q3 | -- | Quarterly | Sep 15 | |
| Instalments -- Q4 | -- | Quarterly | Dec 15 | |

### 3.8 India

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Income tax return (no audit) | ITR-3 or ITR-4 | Annual | Jul 31 | ITR-4 for presumptive taxation |
| Income tax return (audit required) | ITR-3 | Annual | Oct 31 | If turnover exceeds audit threshold |
| Advance tax -- Q1 | Challan 280 | Quarterly | Jun 15 | 15% of estimated liability |
| Advance tax -- Q2 | Challan 280 | Quarterly | Sep 15 | 45% cumulative |
| Advance tax -- Q3 | Challan 280 | Quarterly | Dec 15 | 75% cumulative |
| Advance tax -- Q4 | Challan 280 | Quarterly | Mar 15 | 100% cumulative |
| GST return | GSTR-3B | Monthly | 20th of following month | Summary return with tax payment |
| GST annual return | GSTR-9 | Annual | Dec 31 | If turnover > INR 2 crore |

### 3.9 Spain

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| IRPF (income tax) | Modelo 100 | Annual | Jun 30 | Renta campaign typically opens Apr 2 |
| IVA (VAT) -- Q1 | Modelo 303 | Quarterly | Apr 20 | |
| IVA (VAT) -- Q2 | Modelo 303 | Quarterly | Jul 20 | |
| IVA (VAT) -- Q3 | Modelo 303 | Quarterly | Oct 20 | |
| IVA (VAT) -- Q4 | Modelo 303 | Quarterly | Jan 30 | Note: Jan 30, not Jan 20 |
| Pago fraccionado -- Q1 | Modelo 130 | Quarterly | Apr 20 | 20% of cumulative net income |
| Pago fraccionado -- Q2 | Modelo 130 | Quarterly | Jul 20 | |
| Pago fraccionado -- Q3 | Modelo 130 | Quarterly | Oct 20 | |
| Pago fraccionado -- Q4 | Modelo 130 | Quarterly | Jan 30 | |
| RETA (social security) | Cuota | Monthly | Last business day of month | Autonomous workers' regime |

### 3.10 Netherlands

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Income tax return | IB (Inkomstenbelasting) | Annual | May 1 | Can request extension to Sep 1 |
| BTW (VAT) return | Aangifte omzetbelasting | Quarterly | Last day of month after quarter end | Quarters: Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec |
| Voorlopige aanslag (provisional assessment) | -- | As assessed | Per Belastingdienst schedule | Monthly instalments based on assessment |

### 3.11 Singapore

| Obligation | Form | Frequency | Deadline | Notes |
|---|---|---|---|---|
| Income tax return | Form B | Annual | Apr 18 (e-filing) / Apr 15 (paper) | For year of assessment (prior calendar year) |
| GST return | GST F5 | Quarterly | 1 month after quarter end | Prescribed accounting periods |
| Estimated chargeable income | ECI | Annual | 3 months after FY end | For companies only; individuals use Form B |

---

## Section 4 -- Penalty summaries (for late-filing estimates)

These are simplified penalty rules for estimation purposes. Always flag as T2 and recommend reviewer verification.

### US -- Federal

- **Failure to file (FTF):** 5% of unpaid tax per month, max 25%. Minimum penalty for returns >60 days late: lesser of $510 or 100% of unpaid tax.
- **Failure to pay (FTP):** 0.5% of unpaid tax per month, max 25%.
- **Estimated tax underpayment:** IRC section 6654 penalty calculated at federal short-term rate + 3 percentage points, compounded daily.

### US -- California

- **Late filing:** 5% of tax due + 0.5% per month (max 25%). Minimum $135 or 100% of tax.
- **Late payment:** Collection cost recovery fee applies after demand notice.

### Malta

- **Late filing of TA24:** Administrative penalty of EUR 50 per month or part thereof (max EUR 500).
- **Late payment:** Interest at 0.54% per month on unpaid tax.
- **Late VAT return:** EUR 20 per day of delay.

### United Kingdom

- **Late SA filing:** GBP 100 immediate; after 3 months, GBP 10/day (max 90 days = GBP 900); after 6 months, 5% of tax due or GBP 300 (whichever is greater); after 12 months, further 5% or GBP 300.
- **Late payment:** 5% surcharge at 30 days, 6 months, and 12 months past due.

### Germany

- **Late filing (Verspaetungszuschlag):** 0.25% of assessed tax per month of delay, minimum EUR 25/month.
- **Late payment (Saumniszuschlag):** 1% per month of the rounded-down tax amount.

### Australia

- **Failure to lodge on time:** AUD 313 per 28-day period, max AUD 1,565 (individual).
- **General interest charge (GIC):** Base rate + 7 percentage points, compounded daily.

### Canada

- **Late filing:** 5% of balance owing + 1% per complete month late (max 12 months = 17% total).
- **Repeated late filing:** 10% + 2% per month (max 20 months).
- **Instalment interest:** Prescribed rate, compounded daily.

### India

- **Late filing (section 234F):** INR 5,000 if filed by Dec 31; INR 10,000 after. INR 1,000 if total income < INR 5 lakh.
- **Late payment interest (section 234B):** 1% per month on shortfall.
- **Advance tax interest (section 234C):** 1% per month on quarterly shortfall.

### Spain

- **Late filing (recargo):** 1% + 1% per complete month of delay (up to 12 months), no penalties/interest. After 12 months: 15% surcharge + interest.
- **Late payment:** 5% (3 months), 10% (6 months), 15% (12 months), 20% + interest (>12 months). Under the new LGT reform, voluntary regularisation recargos apply.

### Netherlands

- **Late filing:** EUR 385 fixed penalty (verzuimboete). Repeated: up to EUR 5,514.
- **Late payment:** Tax interest (belastingrente) at 7.5% (2025 rate for income tax).

### Singapore

- **Late filing:** SGD 200 immediate; if still not filed after 1 month, summons + further penalties up to SGD 1,000.
- **Late payment:** 5% penalty on unpaid tax. After 1 month: additional 1% per month (max 12%).

---

## Section 5 -- Output format

Present the calendar in this structure:

### Part A -- Filing calendar (next 12 months)

```
| # | Date | Days | Urgency | Jurisdiction | Obligation | Form | Action |
|---|------|------|---------|--------------|------------|------|--------|
| 1 | 2026-04-15 | 4 | RED | US | Federal income tax | 1040 | File return + pay balance |
| 2 | 2026-04-15 | 4 | RED | US | Estimated tax Q1 | 1040-ES | Pay Q1 estimate |
| ... | | | | | | | |
```

### Part B -- Overdue items (if any)

List any obligations past their deadline with estimated penalty.

### Part C -- Reviewer notes

- Assumptions made (e.g., "assumed online filing for UK SA100")
- Items requiring reviewer confirmation
- Suggestions for extension filings

---

## Section 6 -- Self-checks

Before delivering output, verify:

- [ ] User's jurisdiction is confirmed, not assumed
- [ ] All obligations for the jurisdiction are included (none omitted)
- [ ] Dates are correct for the current calendar year
- [ ] Weekend adjustment applied where needed
- [ ] Urgency flags match the days-remaining calculation
- [ ] Penalty estimates are flagged T2 with reviewer disclaimer
- [ ] No filing advice is given without reviewer qualification
- [ ] Calendar is sorted chronologically
- [ ] Output uses the format from Section 5


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
