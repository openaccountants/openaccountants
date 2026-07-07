---
name: sa-gosi-saudization
description: ALWAYS read this skill before touching any Saudi Arabia employer compliance work — social insurance contributions, Saudization quotas, or monthly wage filings. Use whenever asked to compute, review, or advise on Saudi private-sector payroll obligations — General Organization for Social Insurance (GOSI) contributions split between the Annuity (retirement) branch, the Occupational Hazards branch, and the SANED unemployment insurance branch; Saudization compliance under the Nitaqat program administered by the Ministry of Human Resources and Social Development (MHRSD); and the Wage Protection System (WPS) submitted monthly via the Mudad platform. Trigger on phrases like "Saudi GOSI", "Saudization Nitaqat", "Wage Protection System Saudi", "Mudad WPS", "9% GOSI Saudi", "SANED unemployment", "Saudi employer compliance", "Saudi labor law", "Saudi expat 2% GOSI", "Nitaqat Platinum Green Yellow Red", "iqama renewal Saudi", "MHRSD quota", or any request involving running monthly payroll, hiring Saudis vs expats, or assessing Nitaqat tier impact on visa quotas for a private-sector establishment in the Kingdom of Saudi Arabia. This skill is the ORCHESTRATOR for SA employer compliance — it sequences GOSI registration, monthly contribution calculation, Nitaqat tier monitoring, and WPS filing into the correct order, and flags when sector-specific Saudization quotas need verification against the current MHRSD notification.
jurisdiction: SA
domain: international
tax_year: 2025
reviewed_by: Mehran Habib
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# sa-gosi-saudization

## Saudi Arabia — GOSI + Saudization + WPS — Skill v1.0

> **Scope note:** This skill is the **end-to-end employer compliance orchestrator** for private-sector establishments in the Kingdom of Saudi Arabia (KSA). Saudi Arabia does **not levy personal income tax** on employment income for either Saudis or expatriates, so there is no PAYE-style withholding to compute. The employer's monthly obligations are therefore: (a) GOSI contributions, (b) Saudization compliance under Nitaqat, and (c) Wage Protection System (WPS) filing via Mudad. This skill does NOT cover Zakat, corporate income tax, VAT, or e-invoicing — those live in their respective Saudi Arabia skills.
>
> **Tax year 2025 note:** Contribution rates below reflect the structure in force following the GOSI reforms phased in from 2024 onward. The **9%/9% annuity split** is the pre-reform baseline for existing Saudi insured workers; newly insured Saudis (first GOSI registration on or after 3 July 2024) are subject to a phased increase under the Civil Pension and Social Insurance Schemes reform — verify current rate for any Saudi employee first registered after that date. **SANED unemployment insurance** has applied to Saudi nationals since 2014. **Wage base cap** of SAR 45,000/month is the long-standing ceiling — verify against the current GOSI portal before filing. **Saudization quotas were tightened across multiple sectors in 2024–2025** (engineering, accounting, dentistry, pharmacy, retail outlets, telecom retail, real estate brokerage, project management, customer service, etc.) — always flag "verify current sector quota against the latest MHRSD notification" before relying on a percentage.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Mehran Habib** on 2026-06-06.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### GOSI and Saudization

- **Annuity (retirement) — employer** — 9%  _(GOSI Law)_
- **Annuity (retirement) — employee** — 9%  _(GOSI Law)_
- **Occupational Hazards — employer (Expatriate)** — 2%  _(GOSI Law)_
- **SANED (unemployment) — employer** — 0.0075  _(GOSI Law)_
- **SANED (unemployment) — employee** — 0.0075  _(GOSI Law)_
- **Total — Saudi employer** — 0.1175  _(GOSI Law)_
- **Total — Saudi employee** — 0.0975  _(GOSI Law)_
- **Occupational Hazards — employer (Expatriate)** — 2%  _(GOSI Law)_
- **Employee contribution (Expatriate)** — 0%  _(GOSI Law)_
- **Contributory wage cap** — SAR 45,000/month  _(GOSI Law, Part 1 Article 8(2))_
- **GOSI Contribution Base** — Basic salary + housing allowance  _(GOSI Law, Part 1 Article 8(1))_
- **Nitaqat — Platinum tier** — Exceeds target — maximum benefits  _(MHRSD / Qiwa — Nitaqat Mutawar Program procedural guidelines)_
- **Nitaqat — High/Mid/Low Green tier** — Meets target — standard to limited  _(MHRSD / Qiwa — Nitaqat Mutawar Program procedural guidelines)_
- **Nitaqat — Red tier** — Well below — no visas, no iqama renewals  _(MHRSD / Qiwa — Nitaqat Mutawar Program procedural guidelines)_
- **WPS Platform** — Mudad (mudad.com.sa)  _(MHRSD — Wage Protection System)_
- **WPS Requirement** — All salaries via Saudi bank IBAN  _(MHRSD — Wage Protection System, ref. 1.8.4 (59 - ACC))_

## Section 1 — Quick reference: contribution + Saudization table

### 1.1 GOSI monthly contribution table

**GOSI monthly contribution table**

| Branch | Saudi employer | Saudi employee | Expat employer | Expat employee | Wage base |
| --- | --- | --- | --- | --- | --- |
| **Annuity (retirement)** | 9% | 9% | — | — | Contributory wage (basic + housing), capped at SAR 45,000/month |
| **Occupational Hazards** | 2% | — | 2% | — | Same contributory wage cap |
| **SANED (unemployment)** | 1.5% | 1.5% | — | — | Same contributory wage cap, Saudis only since 2014 |
| **TOTAL — Saudi national** | **12.5%** | **10.5%** | — | — | Combined 23% |
| **TOTAL — Expatriate** | — | — | **2%** | **0%** | Occupational Hazards only |

The order of GOSI branches matters because **only Saudi nationals are subject to all three branches** (Annuity, Occupational Hazards, SANED), while **expatriates are subject only to Occupational Hazards**. Calculate per-employee, then aggregate per establishment for the monthly remittance.

- **Contributory wage definition** — GOSI uses basic salary + housing allowance (whether paid in cash or in kind). Other allowances (transport, mobile, food, etc.) are generally excluded unless the employment contract structures them as part of basic. Conservative default: if an allowance is fixed and unconditional, treat it as part of the contributory wage and flag for reviewer.
- **Cap rule** — The contributory wage is capped at SAR 45,000/month per employee for all branches. Salaries above SAR 45,000 still pay GOSI but only on the first SAR 45,000.
- **Conservative default** — When in doubt whether a particular allowance is part of the contributory wage, include it in the base and flag for reviewer. GOSI under-contribution triggers GOSI inspector recovery plus 2%/month penalty; over-contribution is recoverable but administratively painful.

### 1.2 Nitaqat (Saudization) tier table

**Nitaqat (Saudization) tier table**

| Tier | Compliance status | Consequences |
| --- | --- | --- |
| **Platinum** | Exceeds target | Maximum benefits — fastest visa issuance, iqama renewal without restriction, priority on government tenders, ability to "poach" workers from lower-tier establishments |
| **High Green** | Meets target comfortably | Full ability to hire expats, renew iqamas, issue work visas |
| **Mid Green** | Meets target | Hire expats and renew iqamas under standard quota |
| **Low Green** | Barely meets target | Hire expats but at reduced quota; iqama renewal allowed |
| **Yellow** | Below target | Restricted — limited new expat visas; existing iqamas renewable only for limited periods; workers may transfer out to Green/Platinum entities without employer consent |
| **Red** | Well below target | Severe — no new expat visas, no iqama renewals, workers may transfer out freely; government tender access blocked |

The Nitaqat program classifies every private-sector establishment into a colour-coded tier based on the percentage of Saudi nationals in its workforce, measured against the published target for its sector and size band. The tier is computed continuously by MHRSD and reviewed in real time on the Qiwa platform.

- **Sector × size matrix** — Saudization targets range from approximately 5% to 75% depending on the sector (banking, telecom, retail trade, construction, hospitality, professional services etc.) and establishment size band (Giant ≥ 3,000 employees, Big 500–2,999, Medium 50–499, Small 10–49, Tiny 5–9 — verify current size bands on Qiwa). Banking, finance and certain professional sectors carry the highest Saudization targets; construction and unskilled labour carry the lowest. Always verify the current sector quota on the MHRSD/Qiwa portal before relying on a percentage.

### 1.3 WPS (Wage Protection System) filing summary

**WPS (Wage Protection System) filing summary**

| Item | Detail |
| --- | --- |
| **Platform** | Mudad (mudad.com.sa) — gateway to MHRSD |
| **Frequency** | Monthly — file matching actual payroll month |
| **Content** | Per-employee salary file with IBAN, contractual salary, paid amount, payment date, status (paid in full / partial / unpaid) |
| **Bank transfer requirement** | All salaries must be paid via Saudi bank transfer to the employee's IBAN — cash payments do not satisfy WPS |
| **Tolerance** | Salary must be paid in full and on time; partial or late payment is flagged and feeds into Nitaqat tier downgrade and visa freezes |
| **Deadline** | File submitted before salary disbursement; payment must clear within the contractual pay cycle (typically by end of the calendar month for the preceding month) |

## Section 2 — Required inputs & refusal catalogue

### 2.1 Inputs required to run Saudi employer compliance

**Inputs required to run Saudi employer compliance**

| Input | Source | Notes |
| --- | --- | --- |
| GOSI establishment number | GOSI portal | Required for monthly contribution upload |
| Commercial Registration (CR) number | Ministry of Commerce | Links GOSI, ZATCA, MHRSD, Qiwa, Mudad |
| Unified Number (700-series) | National platform | Cross-system identifier |
| Nationality of each employee | HR / iqama / national ID | Saudi vs GCC vs other expat — drives GOSI branches |
| National ID (for Saudis) or Iqama number (for expats) | HR | Required on every GOSI and WPS submission |
| Date of first GOSI registration (Saudis) | GOSI history | Determines whether the post-3-July-2024 reform rate applies |
| Contractual basic salary + housing allowance per employee | Employment contract | Forms the contributory wage |
| Other allowances (transport, mobile, etc.) | Employment contract | Generally excluded from GOSI base; verify per contract |
| Saudi bank IBAN per employee | HR / employee record | Required for WPS — non-Saudi bank IBANs are not accepted |
| Sector classification (ISIC code) | CR | Drives Nitaqat target percentage |
| Establishment size band (employee headcount) | Qiwa | Drives Nitaqat target percentage |
| Current Nitaqat tier | Qiwa | Determines visa and iqama renewal posture |
| Date of joining and iqama expiry per expat | HR | Drives iqama renewal calendar and Nitaqat impact |

### 2.2 Refusal catalogue — out of scope

**Refusal catalogue — out of scope**

| Scenario | Action |
| --- | --- |
| Domestic workers (drivers, housemaids, nannies) under the Musaned platform | Out of scope — Musaned regime differs; refer to a qualified Saudi labour consultant |
| Government / public-sector employees (PPA — Public Pension Agency, not GOSI) | Out of scope — GOSI is private sector only; PPA covers civil servants |
| Military and security forces personnel | Out of scope |
| End-of-service award (gratuity) computation under Articles 84–88 of the Labour Law | Flag — separate legal computation; refer to Saudi labour counsel for senior or contested cases |
| Employees on home-country payroll continuation (shadow payroll) | Out of scope — requires bespoke transfer pricing and GOSI carve-out analysis |
| Employee stock options, RSUs, long-term incentive plans | Out of scope — GOSI treatment and labour law treatment are unsettled; specialist required |
| Treaty positions and totalization agreements (e.g. with GCC states) | Out of scope — refer to Saudi tax counsel; GCC nationals are treated as Saudis for GOSI purposes by Council of Ministers Resolution but specific cases need verification |
| Free zone establishments (e.g. Special Integrated Logistics Zone, NEOM) | Flag — some free zones have bespoke labour and social insurance regimes that override the standard GOSI rules |
| Establishments straddling the pre/post 3-July-2024 GOSI reform with mixed cohorts of Saudi staff | Flag for reviewer — per-employee analysis required to determine the correct annuity rate cohort |
| Saudization exemptions (small establishments under 5, family-owned enterprises, specific sectors) | Flag — verify each exemption claim against current MHRSD notification |

## Section 3 — GOSI (General Organization for Social Insurance)

### 3.1 Statutory basis

- **Statutory basis** — GOSI operates under the Social Insurance Law (Royal Decree M/33, 1421H, as amended) and is administered by the General Organization for Social Insurance headquartered in Riyadh. The three branches are: 1. Annuity Branch (التأمين ضد المعاشات) — retirement, disability, and survivor benefits. Saudi nationals only. 2. Occupational Hazards Branch (التأمين ضد الأخطار المهنية) — work-injury and occupational disease compensation. All employees, Saudi and expat. 3. SANED Unemployment Insurance (نظام ساند) — added in 2014. Saudi nationals only.  _(Social Insurance Law, Royal Decree M/33, 1421H)_

### 3.2 Computation order

- **Computation order** — For each employee, in order: 1. Determine nationality bucket: Saudi (including GCC nationals treated as Saudis), or expatriate. 2. Determine contributory wage: basic salary + housing allowance, capped at SAR 45,000/month. 3. Determine first-registration cohort (Saudis only): if first GOSI registration is on or after 3 July 2024, flag for verification of phased reform rate; otherwise apply the 9%/9% baseline used in this skill. 4. Compute employer contribution: 12.5% (Saudi) or 2% (expat) of contributory wage. 5. Compute employee deduction: 10.5% (Saudi) or 0% (expat) of contributory wage. 6. Aggregate per establishment: sum all employer contributions + all employee deductions = the GOSI monthly remittance. 7. Cross-check against Mudad/WPS payroll file: GOSI base × headcount should reconcile to WPS contractual salary aggregate (after stripping out the SAR 45,000 cap effect).

### 3.3 Wage base — what's in, what's out

**Wage base — what's in, what's out**

| Component | In GOSI base? |
| --- | --- |
| Basic salary | **YES** |
| Housing allowance (cash) | **YES** |
| Housing in kind (employer-provided accommodation) | **YES** — at deemed cash value |
| Transport allowance | Generally **NO** — verify if it's structured as part of basic |
| Mobile / communication allowance | Generally **NO** |
| Food allowance | Generally **NO** |
| Performance bonus (annual) | Generally **NO** for GOSI base (one-off), but flag if recurrent |
| Commission (sales) | **YES** if regular and contractual; flag otherwise |
| End-of-service award accrual | **NO** — separate gratuity regime |
| Overtime | **NO** — excluded by regulation |

### 3.4 Monthly filing & remittance

**Monthly filing & remittance**

| Step | Where | Deadline |
| --- | --- | --- |
| Upload monthly contribution file | GOSI portal (gosi.gov.sa) | By **end of the month following** the contribution month |
| Pay contribution amount via SADAD | SADAD bill payment via any Saudi bank | Same deadline |
| Reconcile against WPS-filed salaries | Mudad ↔ GOSI cross-check | Before next month's filing |

- **Late payment** — GOSI imposes a 2% per month delay penalty on unpaid contributions, calculated from the due date until full settlement.

## Section 4 — Saudization (Nitaqat program)

### 4.1 Statutory basis & administration

- **Statutory basis & administration** — The Nitaqat program is administered by the Ministry of Human Resources and Social Development (MHRSD) under the authority of the Saudi Labour Law (Royal Decree M/51, 1426H, as amended) and successive Council of Ministers resolutions. The program is operationalised through the Qiwa platform (qiwa.sa), which displays each establishment's current Saudization percentage, target percentage, tier, and remaining headroom in real time.  _(Saudi Labour Law, Royal Decree M/51, 1426H)_

### 4.2 How the tier is calculated

- **How the tier is calculated** — For each establishment (identified by CR number, with separate CRs running on separate Nitaqat counters): 1. MHRSD assigns the establishment a sector classification based on the CR's primary economic activity (ISIC code). 2. MHRSD assigns a size band based on the total employee count (Giant ≥ 3,000; Big 500–2,999; Medium 50–499; Small 10–49; Tiny 5–9 — verify current bands). 3. The sector × size band cell has a published target Saudization percentage, ranging from approximately 5% to 75%. 4. Daily computation: MHRSD calculates the establishment's actual Saudization percentage = (Saudi headcount counted under Nitaqat weighting) ÷ (total headcount). 5. Tier assignment: Platinum / High Green / Mid Green / Low Green / Yellow / Red — based on how the actual percentage compares to the target.
- **Nitaqat weighting nuances** — Not every Saudi employee counts as a full "1" in the Saudization headcount. MHRSD has historically applied weighting multipliers for special categories — for example, part-time Saudi workers under the official part-time contract count as a fraction, Saudi women in roles previously male-dominated may carry a multiplier, and Saudi workers with disabilities carry a higher weight. Conversely, certain expat categories may count differently. Verify current weighting rules on Qiwa before relying on a target.

### 4.3 Sector quotas — verify each time

Saudization quotas were tightened across multiple sectors in 2024 and 2025, including but not limited to:

- Engineering professions — graduated Saudization of engineers across staged percentage targets
- Accounting and financial professions — Saudization of accountants, financial analysts, financial managers
- Dentistry and pharmacy — Saudization of pharmacists, pharmacy assistants, dentists
- Retail outlets in specified malls and trade categories — sector-specific staged percentages
- Telecom retail — Saudization of customer-facing telecom staff
- Real estate brokerage — Saudization of real estate brokers
- Project management — Saudization of project management roles
- Customer service — Saudization of customer service centre staff
- Driving schools, gold and jewellery retail, optical, telecom devices retail, watches retail, car rental, communication, electrical appliances retail — various staged percentages

> **Always flag:** "Verify the current Saudization target for this sector × establishment size on Qiwa / MHRSD notification before quoting a percentage." Sector quotas change by ministerial decision and the published percentages drift upward each cycle.

### 4.4 Consequences of tier — operational impact

**Consequences of tier — operational impact**

| Tier | New expat visas | Iqama renewals | Worker mobility | Government tender |
| --- | --- | --- | --- | --- |
| Platinum | Full | Full + extended periods | Can attract workers from other establishments | Priority |
| High Green | Full | Full | Standard | Eligible |
| Mid Green | Standard | Full | Standard | Eligible |
| Low Green | Reduced | Full but with restrictions | Standard | Eligible |
| Yellow | Restricted | Limited renewal periods | Workers can leave to Green/Platinum without consent | Restricted |
| Red | None | Blocked | Workers leave freely | Blocked |

> **Business impact:** A drop from Green to Yellow or Red has substantial commercial impact — projects requiring expat technical staff stall when iqamas cannot be renewed, and government contracts may be cancelled. This is materially more disruptive than a tax penalty.

## Section 5 — Wage Protection System (WPS via Mudad)

### 5.1 Statutory basis

- **Statutory basis** — The Wage Protection System was introduced by MHRSD Resolution to enforce Article 90 of the Saudi Labour Law (timely full-amount payment of wages). It is administered via the Mudad platform (mudad.com.sa), which receives the monthly payroll file from the establishment and reconciles it against actual bank-clearing data drawn from the Saudi banking system.  _(MHRSD Resolution; Saudi Labour Law Article 90)_

### 5.2 What the WPS file contains

For each employee, per month:

- National ID (Saudi) or Iqama number (expat)
- Full name (Arabic + English)
- IBAN (Saudi bank account only)
- Contractual basic salary
- Contractual housing allowance
- Contractual other allowances
- Total contractual salary
- Amount actually paid
- Payment date
- Payment status (paid in full / partial / unpaid / dispute)

### 5.3 WPS compliance feedback loop

- **WPS compliance feedback loop** — Mudad reconciles the submitted file against actual bank-clearing records: 1. Match: salary paid in full and on time → green / compliant. 2. Partial or late payment: flagged → contributes to Nitaqat tier downgrade and triggers MHRSD inspector follow-up. 3. No payment: treated as a labour law violation under Article 90 → fines per employee per occurrence + iqama renewal freeze + Nitaqat consequence.  _(Saudi Labour Law Article 90)_

### 5.4 Cash payments do not satisfy WPS

- **Cash payments do not satisfy WPS** — All salaries must be paid by Saudi bank transfer to the employee's IBAN. Cash payments are not recognised by Mudad and are treated as non-payment for WPS purposes — even if the employee signs a receipt.

## Section 6 — Worked examples

### 6.1 Example: LLC with 10 Saudi + 5 expat employees

**Facts:**
- Saudi LLC with CR registered for IT consultancy sector
- Headcount: 10 Saudi nationals + 5 expatriates (total 15)
- All Saudis: contractual basic SAR 8,000/month + housing allowance SAR 2,000/month = contributory wage SAR 10,000/month
- All expats: contractual basic SAR 12,000/month + housing allowance SAR 3,000/month = contributory wage SAR 15,000/month
- None of the contractual wages exceed the SAR 45,000 cap

**GOSI monthly computation**

| Group | Per-employee contributory wage | Employer rate | Employee rate | Per-employee employer | Per-employee employee | Headcount | Employer total | Employee total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Saudis | SAR 10,000 | 12.5% | 10.5% | SAR 1,250 | SAR 1,050 | 10 | **SAR 12,500** | **SAR 10,500** |
| Expats | SAR 15,000 | 2% | 0% | SAR 300 | SAR 0 | 5 | **SAR 1,500** | **SAR 0** |
| **TOTAL** |  |  |  |  |  | **15** | **SAR 14,000** | **SAR 10,500** |

- **GOSI monthly remittance from establishment to GOSI:** SAR 14,000 (employer portion) + SAR 10,500 (employee portion withheld from Saudi salaries) = **SAR 24,500**.
- **Employer cost of employment per month:** 10 × (SAR 10,000 + SAR 1,250) + 5 × (SAR 15,000 + SAR 300) = SAR 112,500 + SAR 76,500 = **SAR 189,000** (before any other allowances or end-of-service accrual).

**Nitaqat status (IT consultancy, Small size band 10–49):**
- Saudi headcount 10 ÷ total 15 = **66.7% Saudization**.
- For IT consultancy at Small band, the target Saudization percentage is typically in the 30–40% range (verify current quota on Qiwa) — at 66.7%, this establishment would likely be Platinum tier.
- Operational consequence: full ability to hire expats and renew iqamas; priority on government tenders if pursuing public sector work.

**WPS monthly file:**
- 15 employee lines submitted via Mudad
- Each line: contractual salary, IBAN, payment date, status
- Total contractual gross to be paid via Saudi bank transfer: 10 × SAR 10,000 + 5 × SAR 15,000 = **SAR 175,000/month** to be cleared through the banking system by the contractual pay date

### 6.2 Edge case — Saudi employee earning above the SAR 45,000 cap

If a Saudi senior manager earns contractual basic SAR 50,000 + housing SAR 12,000 = contributory wage SAR 62,000/month:

- Capped at SAR 45,000 for GOSI.
- Employer 12.5% × SAR 45,000 = **SAR 5,625/month**.
- Employee 10.5% × SAR 45,000 = **SAR 4,725/month**.
- The SAR 17,000 above the cap (SAR 62,000 − SAR 45,000) is **not subject to GOSI**.
- However, WPS reports the full contractual SAR 62,000 because WPS verifies the actual contractual salary is paid, not the GOSI base.

## Section 7 — Filing & payment calendar

**Filing & payment calendar**

| Obligation | Frequency | Deadline | Channel |
| --- | --- | --- | --- |
| **GOSI monthly contribution upload + payment** | Monthly | End of month following | gosi.gov.sa + SADAD |
| **WPS payroll file** | Monthly | Before contractual pay date | mudad.com.sa |
| **Nitaqat tier monitoring** | Continuous | Real-time on Qiwa | qiwa.sa |
| **Iqama renewal per expat** | Annual (or biennial) | Before iqama expiry | Absher / Qiwa |
| **End-of-service award accrual** | Continuous; payable on separation | At end of contract | HR / payroll system |
| **GOSI annual reconciliation** | Annual | As notified by GOSI | gosi.gov.sa |

> **Calendar discipline:** Set monthly reminders for GOSI upload (last working day of month following), WPS submission (5 working days before contractual pay date), and continuous Qiwa monitoring (weekly check on Nitaqat tier headroom).

## Section 8 — Penalties

**Penalties**

| Breach | Penalty |
| --- | --- |
| **Late GOSI contribution payment** | **2% per month** delay surcharge on unpaid amount, until full settlement |
| **Under-reporting GOSI wage base** | Recovery of underpaid contributions + 2%/month surcharge + administrative penalty per Social Insurance Law |
| **Failure to register an establishment with GOSI** | Per-Royal-Decree-M/33 penalties — administrative fines and back-contribution recovery |
| **Failure to register an employee with GOSI** | Per-employee fine + back-contribution from date of joining |
| **WPS non-compliance (late, partial, or unpaid salary)** | Article 90 Labour Law fines per employee per occurrence; iqama renewal freeze; Nitaqat tier downgrade |
| **Cash salary payment (bypassing WPS)** | Treated as non-payment — WPS does not credit cash; Nitaqat consequences follow |
| **Nitaqat Yellow tier** | Restricted expat visas; limited iqama renewal periods; workers may transfer to Green/Platinum without employer consent |
| **Nitaqat Red tier** | No new expat visas; no iqama renewals; workers leave freely; government tender access blocked |
| **Saudization fraud (fake Saudi headcount — "phantom Saudization")** | Severe — Royal Decree penalties, fines per phantom employee, immediate Nitaqat downgrade, blacklist from government contracts, potential criminal referral |

> **Materiality note:** For most Saudi establishments, the Nitaqat consequences materially exceed the GOSI cash penalties in business impact. A two-tier Nitaqat downgrade can halt an entire engineering or construction project. Treat Saudization compliance as a board-level operational risk, not a back-office administrative item.

## Section 9 — Sources

- **Social Insurance Law**, Royal Decree M/33 of 1421H, as amended — primary legal basis for GOSI.
- **Saudi Labour Law**, Royal Decree M/51 of 1426H, as amended — primary legal basis for employment relations, including Article 90 (timely payment of wages) and Articles 84–88 (end-of-service award).
- **Council of Ministers Resolutions** establishing the Nitaqat program and successive sector quota updates — published by MHRSD.
- **GOSI portal** — gosi.gov.sa — official monthly contribution upload and SADAD payment.
- **Qiwa platform** — qiwa.sa — Nitaqat tier monitoring and establishment workforce data.
- **Mudad platform** — mudad.com.sa — WPS file submission gateway to MHRSD.
- **MHRSD** — hrsd.gov.sa — official Saudization notifications, sector quotas, and labour law guidance.
- **SANED** — Unemployment Insurance Scheme, established by Council of Ministers Resolution in 2014, administered by GOSI.
- **Civil Pension and Social Insurance Schemes reform** — phased adjustments to annuity contribution rates for Saudis first registered on or after 3 July 2024; verify current rate per cohort.

> **Verification discipline:** Before completing any Saudi employer compliance task, verify on the official portals (GOSI, Qiwa, Mudad, MHRSD) that the rates, caps, sector quotas, and size bands quoted in this skill have not been superseded by a subsequent notification. Saudi compliance changes frequently and the cost of relying on stale figures is high.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

### 3.2 Computation order

0. **Step 1: Determine GOSI contribution per employee** — Run GOSI monthly contribution computation per employee (nationality bucket, contributory wage, cohort, employer/employee rates)

### 3.4 Monthly filing & remittance

0. **Step 2: File and remit GOSI monthly contribution** — Upload monthly contribution file to GOSI portal and pay via SADAD by end of month following the contribution month

### 4.2 How the tier is calculated

0. **Step 3: Monitor Nitaqat tier** — Determine sector classification, size band, target Saudization percentage, and current tier on Qiwa; flag if quota needs verification

### 5.3 WPS compliance feedback loop

0. **Step 4: File WPS payroll via Mudad** — Submit monthly payroll file via Mudad before contractual pay date and reconcile against actual bank-clearing data

### 3.4 Monthly filing & remittance

0. **Step 5: Reconcile GOSI against WPS** — Reconcile GOSI contribution base against WPS-filed salaries (Mudad ↔ GOSI cross-check) before next month's filing
