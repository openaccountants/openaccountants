---
name: ph-sss-philhealth
description: >
  Philippine SSS, PhilHealth and Pag-IBIG contributions for self-employed people
  in 2026. Classifies active self-employment, voluntary continuation, employees,
  overseas workers and other earning groups before calculating contributions.
  Includes the SSS salary-credit brackets, mandatory provident allocation and
  Employees’ Compensation; PhilHealth income floor, ceiling, 2026 annual
  settlement and missed-premium rules; and Pag-IBIG’s different member and
  employer shares. Use to prepare a monthly budget, reconcile payment records,
  register with the correct fund, generate payment references or address a gap.
  Covers concurrent employment, domestic workers, older members and the
  distinction between compulsory contributions and optional savings. Benefit
  awards, loan approval, MP2 pre-termination and income-tax deductions require
  their separate eligibility and evidence checks.
version: 1.1
jurisdiction: PH
tax_year: 2026
last_updated: 2026-11-16
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Philippines SSS, PhilHealth and Pag-IBIG for Self-Employed People

2026 rules checked on 2026-11-16; version 1.1. Source-cited draft; no professional approval is implied.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, labour law practitioner, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Scope

Calculate in **PHP**, normally by applicable month, but establish the member category separately for each fund. Active self-employment is not interchangeable with voluntary continuation, an employee account, an OFW classification or Pag-IBIG’s Other Earning Groups. Benefits such as retirement, disability, death, sickness and maternity, PhilHealth inpatient/outpatient/primary-care packages, and Pag-IBIG housing, multi-purpose or calamity loans have their own qualifying conditions. A contribution calculation does not award a benefit or approve a loan. In particular, do not promise an unemployment benefit merely because a freelancer stops earning. [SSS coverage](https://www.sss.gov.ph/compulsory-coverage/); [SSS law, sections 9-A and 14-B](https://www.sss.gov.ph/wp-content/uploads/2022/04/Booklet_SS-ACT-OF-2018_05172019_2.pdf); [UHC Act, sections 5-9](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html); [HDMF Act, sections 6 and 10](https://lawphil.net/statutes/repacts/ra2009/ra_9679_2009.html).

| Fund and applicable category | Current contribution basis | Monthly amount or limit | Authority |
|---|---|---|---|
| SSS compulsory self-employed | **15%** of the applicable **PHP 5,000-35,000 MSC**, including the regular SS/mandatory provident split, **plus EC** | **PHP 760-5,280** (computed from SS plus EC), including EC; not merely PHP 750-5,250 | [Circular 2024-008, combined PDF page 3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf); [SSS payment guidance](https://www.sss.gov.ph/pay-contribution) |
| PhilHealth earning self-paying member | **5%** of documented/attested monthly income, floor **PHP 10,000**, ceiling **PHP 100,000** | **PHP 500-5,000**, entirely paid by the member; employed members ordinarily split the premium equally with the employer | [UHC Act, section 10](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html); [PhilHealth’s 2026 rate announcement via PIA](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| Pag-IBIG mandatory self-employed under C.1.1.3 | Employee **1%** at fund salary up to **PHP 1,500**, otherwise **2%**, plus employer **2%**; MFS **PHP 10,000** | Pays both shares; maximum compulsory total **PHP 400** (computed: 4% × PHP 10,000) | [Circular 460, C.1.1.3](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| Pag-IBIG Other Earning Groups under C.1.6 | **1%** for fund salary **PHP 1,000-1,500**, **2%** above it, subject to the MFS | Maximum **PHP 200** (computed: 2% × PHP 10,000) under this category; do not automatically add the C.1.1.3 employer share | [Circular 460, C.1.6](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |

## Ask the client first

- What work do you perform, when did it start, and what are your age, citizenship and location? Obtain the agency-recorded categories, including any overseas or domestic-worker status.
- What are the actual monthly earnings and their evidence? Establish each fund’s own basis; an SSS salary credit is not automatically PhilHealth income or Pag-IBIG fund salary.
- Do you also have an employer, more than one employer, prior employment, or periods without income? Obtain contribution histories and existing SS number, PIN and MID before attempting another registration.
- For Pag-IBIG, does the Fund record mandatory self-employment under C.1.1.3, Other Earning Groups under C.1.6, or voluntary coverage? Resolve that classification from the work and Fund record before quoting PHP 200 or PHP 400.
- Which months are unpaid, incorrectly posted or disputed? Obtain receipts, SSS PRNs, PhilHealth SPAs and the agency statements; distinguish old arrears from current premiums and loan payments.
- Is the task compulsory compliance, optional Regular Savings/MP2, a benefit/loan claim, or an income-tax deduction? Obtain the tax method and supporting records for a deduction question.

## The method, step by step

### 1. Confirm coverage and register without inventing income

For SSS, compulsory self-employed coverage includes persons practising their profession and other covered self-employed occupations. The old **PHP 1,000 monthly earnings** statement is not a general registration exemption: section 9-A does not impose that floor, while section 19-A allows the Commission to reduce contributions for low earners. Initial SE coverage normally starts no later than age **60**; an existing member with at least one prior contribution who becomes self-employed after 60 but before **65** remains within the agency’s stated compulsory rule. SSS says SE coverage starts with the first paid contribution, no earlier than the start of self-employment. Register an employer account as well if you employ staff. [RA 11199, sections 9-A and 19-A](https://www.sss.gov.ph/wp-content/uploads/2022/04/Booklet_SS-ACT-OF-2018_05172019_2.pdf); [SSS self-employed registration guidance](https://www.sss.gov.ph/self-employed/).

Use the SSS Personal Record/Member Data Change Request route appropriate to a new or existing SS number; the agency specifies supporting identity, civil-status and occupation documents by case. Declare actual/estimated earnings honestly, keep the existing number and reconcile earlier employment. The older RS-1/two-ID checklist is preserved under Sources because it is not the current universal checklist read here. Do not treat unverified income as permission to declare the minimum. Changes from age **55** have special limits: generally one bracket increase once in a calendar year, with the stated exception for a newly increased maximum MSC. [SSS SE registration/contribution guidance](https://www.sss.gov.ph/self-employed/); [SSS contribution changes](https://www.sss.gov.ph/pay-contribution).

All Filipino citizens are automatically included in NHIP; earning self-employed people are direct contributors. For PhilHealth, update the **PMRF**, income, dependants and contact details and complete the primary-care provider selection/registration process. Use the LHIO, an authorised registration partner, Member Portal or eGovPH route that supports the transaction. The income basis can be a BIR-received ITR, income attested in the PMRF, or other documents validated by PhilHealth; overseas members have additional documentary alternatives. Reuse the existing PIN. An unknown income amount requires reconciliation, not an invented minimum declaration. The original blanket extension to every permanent resident is not established by the Filipino-citizen provisions; obtain the foreign-member classification separately. [UHC Act, sections 4-10](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html); [PC 2026-0011, V.A](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf).

For Pag-IBIG, use the **Member’s Data Form (MDF)** or supported electronic registration/update route, retain the member identification and reconcile earlier contributions. Circular 274 C supports online/manual MDF registration; actual membership commences with the initial contribution. Apply Circular 460’s newer contribution categories. Voluntary coverage is available to eligible individuals at least **18** and no more than **65**; it is not the default for every active self-employed worker. A Loyalty Card is distinct from registration or a MID, and is not an SSS UMID equivalent. The old universal document count, 12-digit assertion and free-card claim are held under Sources pending current transaction-specific evidence. [Circular 274, C](https://naro.law.upd.edu.ph/storage/01JW8VAVJXMC6VDPV5AJK9PJJP.pdf); [Circular 460, C.1-C.2](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf).

### 2. Calculate SSS including EC and the provident allocation

Use **Circular 2024-008 for self-employed members**, effective **1 January 2025**, not employee Circular 2024-006. The combined official PDF contains both: the SE table is **page 3**. The statutory historical schedule was **14%**, MSC **PHP 4,000-30,000**, for **2023 and 2024**; the current table is **15%**, MSC **PHP 5,000-35,000**, from 2025. These historical rows do not calculate a 2026 payment. [RA 11199, section 4(a)(9)](https://www.sss.gov.ph/wp-content/uploads/2022/04/Booklet_SS-ACT-OF-2018_05172019_2.pdf); [SE circular/table](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf).

The table below retains every selected bracket from the earlier Guide and adds the EC amount it omitted. **EC is PHP 10 at MSC up to PHP 14,500 and PHP 30 at MSC PHP 15,000 and above**. These are selected brackets, not a complete earnings lookup: for omitted earnings use the full official table. For example, do not round an arbitrary amount to the next displayed row. [SSS contribution guidance](https://www.sss.gov.ph/pay-contribution); [Circular 2024-008, table](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf).

| Monthly earnings (PHP) | MSC (PHP) | SS including MPF (PHP) | EC (PHP) | Total payable (PHP) | Authority |
|---|---|---|---|---|---|
| Below 5,250 | 5,000 | 750 | 10 | 760 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 5,250-5,749.99 | 5,500 | 825 | 10 | 835 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 5,750-6,249.99 | 6,000 | 900 | 10 | 910 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 6,250-6,749.99 | 6,500 | 975 | 10 | 985 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 6,750-7,249.99 | 7,000 | 1,050 | 10 | 1,060 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 7,250-7,749.99 | 7,500 | 1,125 | 10 | 1,135 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 7,750-8,249.99 | 8,000 | 1,200 | 10 | 1,210 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 8,750-9,249.99 | 9,000 | 1,350 | 10 | 1,360 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 9,750-10,249.99 | 10,000 | 1,500 | 10 | 1,510 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 11,750-12,249.99 | 12,000 | 1,800 | 10 | 1,810 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 14,750-15,249.99 | 15,000 | 2,250 | 30 | 2,280 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 19,750-20,249.99 | 20,000 | 3,000 | 30 | 3,030 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 24,750-25,249.99 | 25,000 | 3,750 | 30 | 3,780 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 29,750-30,249.99 | 30,000 | 4,500 | 30 | 4,530 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| 34,750 and above | 35,000 | 5,250 | 30 | 5,280 | [SE table p.3](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |

At MSC **PHP 35,000**, regular SS is **PHP 3,000** on the first PHP 20,000 and the mandatory provident allocation is **PHP 2,250** on the remaining PHP 15,000: **PHP 5,250 SS/MPF plus PHP 30 EC = PHP 5,280**. The provident allocation is part of the 15%, not another 15% on top of the full salary credit. The SE member shoulders the full contribution; there is no separate employer to fund part of it. [Circular 2024-008, regular SS/MPF/EC columns](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf).

Generate a **PRN** for the correct applicable months and category. The agency payment guidance permits SE/voluntary/non-working-spouse remittance monthly or quarterly, due by the **last day of the month following the applicable month or calendar quarter**; check the selected period and PRN rather than applying the obsolete last-digit 10th/15th/20th/25th schedule. A deadline on a weekend/holiday moves to the next working day. The agency’s SE page expressly describes the monthly deadline, while its general payment page also covers the quarterly option. Neither supports filling old SE gaps after the applicable deadline. [SSS payment periods and deadlines](https://www.sss.gov.ph/pay-contribution); [SSS SE guidance](https://www.sss.gov.ph/self-employed/).

Use the current **individual-member** payment channel list. On **13 November 2026** it included accredited collecting banks, Landbank Link.BizPortal, Bayad, ECPay, SM, GCash, Maya and the SSS mobile app, with different facilities by channel. The old BDO/BPI/7-Eleven list is not a universal current individual-member list. Retain the PRN, receipt and posted contribution and resolve failures before paying twice. [SSS payment channels](https://www.sss.gov.ph/sss-payment-channels/).

### 3. Calculate PhilHealth and follow the 2026 settlement rules

For an earning self-paying member, apply **5%** after the **PHP 10,000 floor/PHP 100,000 ceiling**. The 2026 PhilHealth announcement confirms the rate; the following amounts are arithmetic from that rate, not a new benefit eligibility table. Employed members’ equal split does not halve a self-paying member’s own premium. [UHC Act, section 10](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html); [2026 announcement](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/).

| Documented monthly income (PHP) | Full monthly premium (PHP, computed) | Calculation and authority |
|---|---|---|
| 10,000 and below | 500 | 10,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 15,000 | 750 | 15,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 20,000 | 1,000 | 20,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 25,000 | 1,250 | 25,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 30,000 | 1,500 | 30,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 40,000 | 2,000 | 40,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 50,000 | 2,500 | 50,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 60,000 | 3,000 | 60,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 70,000 | 3,500 | 70,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 80,000 | 4,000 | 80,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 90,000 | 4,500 | 90,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |
| 100,000 and above | 5,000 | 100,000 × 5% (computed); [2026 rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) |

Obtain a **Statement of Premium Account (SPA)** and match the payment to it. PC 2026-0011 requires SPA for payment channels, except the stated collecting-agent exception for geographically isolated/disadvantaged areas. It provides **2026 transition flexibility** for specified verification/system situations, with strict implementation from **1 January 2027**; do not apply the earlier blanket April 2026 “No SPA, no payment” date without the later circular. Automatic SPAs for unpaid months from **January 2026** use the last posted premium, subject to income reconciliation; generate/request a corrected SPA when it is wrong. Representatives need the member’s authorisation plus one government photo ID each for member and representative. [PC 2026-0011, V.B and VIII](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf).

Members may pay for any number of months. Treat monthly, quarterly, semi-annual and annual budgeting as choices within the new annual settlement rule: pay the year’s premiums by **31 December of that year**. There is an interest-free grace period through **31 January of the following year**. If unpaid beyond that grace period, interest runs from the actual December due date; the self-paying rate is **not more than 1.5% compounded monthly**, not the former Guide’s blanket 2% monthly. Reconcile the agency assessment before calculating an arrears payoff. [PC 2026-0011, V.B.12-14 and V.C](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf); [UHC Act, section 9](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html).

**Missed premiums alone do not suspend benefits.** Immediate eligibility and the debt are separate. Do not demand nine months’ payments or promise that three months’ payment “reactivates” coverage. Intentional fraud/collusion can have consequences after due process. A person unable to pay should obtain the licensed social worker’s financial-capacity assessment and submit the required documentation for POS-FI/indirect classification: PC 2026-0011 V.C.3-5 provides relief for the current month and outstanding contributions from November 2019 when its conditions are met. Do not self-classify an earning member as financially incapable. [PC 2026-0011, V.C](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf); [UHC Act, sections 6 and 9](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html).

For arrears in **November 2019-December 2025**, PC 2026-0010 supplies a separate **one-time interest waiver**, not an automatic waiver of principal or a refund of interest already paid. It requires current **2026 and succeeding premiums**, updated income/dependant records, and YAKAP assignment/first-patient encounter conditions, with the application and supporting evidence specified in V.D. Apply by **31 December 2027**, unless a later period is prescribed. Approved instalments depend on missed months: **1-12 → up to 12 months; 13-24 → 24; 25-36 → 36; 37-48 → 48; over 48 → 60**. No additional interest accrues while complying with the approved arrangement. Financial incapacity/misclassification requires documentary review; non-compliance can revoke the arrangement after notice and opportunity to cure. [PC 2026-0010, V and VII](https://www.philhealth.gov.ph/circulars/2026/PC2026-0010.pdf).

Pay through the Member Portal, LHIO or an accredited collecting agent available for the transaction, keeping the SPA and receipt. Do not promise that every bank/wallet formerly named in this Guide currently accepts every self-paying transaction; current channel acceptance and the correct SPA take precedence. [PC 2026-0011, V.B.15-16](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf).

### 4. Apply the Pag-IBIG category before combining the funds

Contribution correction credit retained: **Corrected by Jonathan I. Ruiz (CPA, Philippines)**. Circular 460 increased the maximum fund salary from **PHP 5,000 to PHP 10,000**, effective **February 2024**, and expressly separates these routes. [Circular 460, C and F](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf).

| Category | Required savings and boundary | Authority |
|---|---|---|
| Employed | Employee 1% at fund salary up to PHP 1,500, otherwise 2%; employer 2%, each subject to the PHP 10,000 MFS. Employer cannot recover its contribution from the worker. At the ceiling this is PHP 200 each. | [Circular 460, C](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| Mandatory self-employed, C.1.1.3 | Treated as employee and employer, paying both shares. Above PHP 1,500, 4% of capped fund salary gives up to PHP 400; this is not a fixed PHP 200 voluntary contribution. | [Circular 460, C.1.1.3](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| Other Earning Groups, C.1.6 | Farmers, fisherfolk, vendors, transport workers and specified similar self-employed/service/occasional workers: 1% at PHP 1,000-1,500, 2% above, subject to MFS. Do not assume this classification from the word “freelancer” alone. | [Circular 460, C.1.6](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| Non-working spouse | Eligible voluntary membership with the working member-spouse’s consent; use 50% of that spouse’s monthly fund salary and the 1%/2% table. No employer counterpart is required. | [Circular 460, C.2.1](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| Other eligible voluntary member | Apply the applicable C.2 category, including eligible members who stopped employment/self-employment; no universal PHP 200 minimum is established by the percentage table. | [Circular 460, C.2](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| More Regular Savings by choice | A member may save more than required. An employer need only pay its statutory contribution unless it agrees to match the increase. **PHP 5,000 is an optional example, not a statutory maximum.** | [Circular 460, C.3](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |

For direct self-employed/voluntary remittance, Circular 274 **E.8** states **on or before the 10th of the month following the period covered**, or quarterly by the **10th of the quarter’s beginning month**. This corrects the former 15th-of-next-month claim. Circular 460 replaces the older **D contribution** provisions; do not reuse D’s old PHP 5,000 MFS. Keep employer remittance schedules separate: the Fund’s 2026 index lists new employer/electronic-payment circulars **499/500**, whose complete operational text was inaccessible here. The old blanket semi-annual/annual advance-payment and all-channel lists remain unconfirmed under Sources. Use the current Fund-issued payment instruction and reconcile the receipt to the recorded period. [Circular 274, E.8](https://naro.law.upd.edu.ph/storage/01JW8VAVJXMC6VDPV5AJK9PJJP.pdf); [Circular 460, D](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf); [agency circular index](https://www.pagibigfund.gov.ph/about_publication_circulars_memberservices.html).

For a gap or loan question, obtain the statement of savings, current member status, existing loans and product-specific eligibility. A blanket “24 contributions guarantees every loan” or “paying a lump sum creates 24 backdated months” is unsafe. The Fund index lists newer MPL and calamity rules **469/470**; this Guide does not reproduce their unread qualifications. Membership savings and monthly loan amortisations are different obligations. [Circular 274, E.3 and E.6-F](https://naro.law.upd.edu.ph/storage/01JW8VAVJXMC6VDPV5AJK9PJJP.pdf); [agency circular index](https://www.pagibigfund.gov.ph/about_publication_circulars_memberservices.html); [RA 9679, section 10](https://lawphil.net/statutes/repacts/ra2009/ra_9679_2009.html).

**MP2 is optional savings**, separate from compulsory Regular Savings. The Fund’s published news material describes the **PHP 500 minimum and five-year term**, while section 19 of RA 9679 supplies the Fund/benefit tax exemption. A historical dividend range is not a guaranteed future rate. The index lists enhanced **Circular 487, effective 28 February 2026**; its full text could not be read because the agency returned a CAPTCHA. Do not use this Guide to decide early-withdrawal grounds, rollover, a dividend payout, current account limits or enhanced housing-loan eligibility from MP2. The older feature claims are retained under Sources for recovery. [Pag-IBIG’s news archive, MP2 descriptions](https://pagibigfund.gov.ph/about_news.html); [RA 9679, section 19](https://lawphil.net/statutes/repacts/ra2009/ra_9679_2009.html); [current circular index](https://www.pagibigfund.gov.ph/about_publication_circulars_memberservices.html).

### 5. Handle concurrent work, overseas status, household work and age

| Situation | Required decision | Primary authority |
|---|---|---|
| Employee and self-employed at once | SSS says both contributions apply; excess above the maximum contribution is refunded from the SE payments. Reconcile rather than silently suppressing one. For PhilHealth, use the existing PIN and reconcile employment/self-paying months and income with the agency; one PIN is not proof no further amount is due. Pag-IBIG C.4 requires contributions per employer where there are two or more employers; separately classify actual SE work. | [SSS compulsory coverage](https://www.sss.gov.ph/compulsory-coverage/); [PC 2026-0011, V.A-B](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf); [Circular 460, C.4](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| OFW | SSS compulsory coverage includes sea- and land-based OFWs, so “voluntary OFW” is not a universal rule. The payment page specifies a **PHP 8,000 minimum MSC for land-based OFWs**, distinct from domestic SE’s PHP 5,000. PhilHealth’s 2026 self-paying circular includes overseas Filipinos except seafarers/other sea-based workers. Pag-IBIG C.1.4 includes Filipinos working for foreign employers. Obtain the applicable overseas assessment instead of using the domestic examples. | [SSS coverage](https://www.sss.gov.ph/compulsory-coverage/); [SSS payment guidance](https://www.sss.gov.ph/pay-contribution); [PC 2026-0011, scope and V.A](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf); [Circular 460, C.1.4](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| Kasambahay | RA 10361 section 30 makes employer-paid contributions the default; the worker contributes a proportionate share at **PHP 5,000 and above**. Exactly PHP 5,000 is not in an “employer pays all” exemption. Pag-IBIG Circular 460 specifically uses **less than PHP 5,000** for employer-only savings and **PHP 5,000 and above** for 2% each. Use the SSS household table, not the SE table. | [RA 10361, section 30](https://lawphil.net/statutes/repacts/ra2013/ra_10361_2013.html); [Circular 460, C.1.5](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf); [SSS combined table, page 2](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) |
| Age 60+ | SSS’s SE age rule and retirement eligibility are separate: ordinary optional retirement at **60** requires cessation of covered work; technical retirement is **65**, with special occupations having exceptions. A retirement applicant short of **120** qualifying contributions may elect voluntary continuation to reach the pension condition. PhilHealth’s earlier blanket “120 contributions means no more premiums” is not a universal rule for an earning senior: establish current direct/indirect classification. Pag-IBIG voluntary eligibility runs up to **65** under C.2; a retirement withdrawal needs its separate claim rules. | [SSS SE guidance](https://www.sss.gov.ph/self-employed/); [SSS retirement qualifying conditions](https://www.sss.gov.ph/retirement-benefit/); [UHC Act, sections 4-10](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html); [Circular 460, C.2](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) |
| No earnings or interrupted payments | SSS says no contribution is required for an SE month without earnings; it cannot later be paid to backfill that gap. Prior contributions remain in the record; each benefit has its own qualifying period. Voluntary continuation after ceasing SE is a separate category. PhilHealth missed payments do not bar benefits; use the documented debt/waiver/financial-incapacity rules above. Pag-IBIG requires a record/status/loan review rather than a universal “no arrears, just 24 months” answer. | [SSS SE guidance](https://www.sss.gov.ph/self-employed/); [PC 2026-0010](https://www.philhealth.gov.ph/circulars/2026/PC2026-0010.pdf); [PC 2026-0011, V.C](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf); [Circular 274, E-F](https://naro.law.upd.edu.ph/storage/01JW8VAVJXMC6VDPV5AJK9PJJP.pdf) |

### 6. Separate the contribution budget from income-tax deductions

Tax-correction credit retained: **Corrected by Jonathan I. Ruiz (CPA, Philippines)**. Under an **OSD election**, the standard deduction replaces the specified itemised deductions; do not add a separate deduction for these payments. MP2 contributions are savings, not an ordinary premium expense. Employer contributions for staff require the ordinary-and-necessary expense and substantiation analysis; the owner’s own payments are a different question. Employee mandatory contributions also have their own compensation-income treatment, illustrated in RR 8-2018, and should not be confused with an SE expense. [TRAIN, section 11 amending NIRC 34(L)](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html); [RR 8-2018, section 3 compensation illustrations](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf); [RA 9679, section 19](https://lawphil.net/statutes/repacts/ra2009/ra_9679_2009.html).

Do **not** resurrect the old **PHP 2,400 health-insurance deduction** from the original NIRC 34(M) as a current entitlement: current section 34(M), as amended by **CMEPA section 9**, addresses qualifying employer PERA contributions. That is a different scheme. The previous categorical “NO” for every owner’s SSS/PhilHealth/Pag-IBIG payment under itemised deductions, and its precise TRAIN-repeal explanation, were not fully established by the primary provisions read here. They are preserved as unresolved evidence under Sources; obtain the applicable BIR authority and the taxpayer’s facts before signing off a deduction. RR 11-2018 is a withholding regulation, not general authority for all these social-insurance deduction claims. [RA 12214, section 9](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213); [TRAIN, section 11](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html).

## Worked cases

All cases assume genuine domestic SE coverage, earning PhilHealth self-paying status, the stated income sustained for **12 months**, no arrears and no separate employment. Confirm the **Pag-IBIG category** before selecting either total. These are contribution budgets, not income tax, take-home pay, benefit awards or loan limits. [SSS SE table](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf); [2026 PhilHealth rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/); [Pag-IBIG Circular 460, C.1.1.3/C.1.6](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf).

### A. Freelancer earning PHP 30,000: classification changes the total

MSC PHP 30,000 gives SS/MPF **PHP 4,500 plus EC PHP 30 = PHP 4,530**. PhilHealth is **PHP 1,500**. If the Fund confirms mandatory SE under C.1.1.3, Pag-IBIG is **PHP 400**, giving **PHP 6,430 monthly / PHP 77,160 annually**. If it confirms C.1.6 Other Earning Groups, Pag-IBIG is **PHP 200**, giving **PHP 6,230 / PHP 74,760**. The prior PHP 6,200/PHP 74,400 example omitted EC and did not establish its Pag-IBIG category. [SE table](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf); [PhilHealth rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/); [Circular 460](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf).

```oa-check
name: Thirty thousand income and Pag-IBIG category decision
inputs:
  msc: 30000
  income: 30000
  ec: 30
  fund_salary_cap: 10000
steps:
  sss: msc * 0.15 + ec
  philhealth: income * 0.05
  pagibig_both: fund_salary_cap * 0.04
  pagibig_other: fund_salary_cap * 0.02
  monthly_both: sss + philhealth + pagibig_both
  annual_both: monthly_both * 12
  monthly_other: sss + philhealth + pagibig_other
  annual_other: monthly_other * 12
expected:
  sss: 4530
  philhealth: 1500
  pagibig_both: 400
  pagibig_other: 200
  monthly_both: 6430
  annual_both: 77160
  monthly_other: 6230
  annual_other: 74760
```

### B. Freelancer earning PHP 15,000: include EC before annualising

SS/MPF is **PHP 2,250**, EC **PHP 30**, PhilHealth **PHP 750**. The C.1.1.3 both-share payment gives **PHP 3,430 monthly / PHP 41,160 annually**; C.1.6 gives **PHP 3,230 / PHP 38,760**. The original PHP 3,200/PHP 38,400 total omitted EC and used PHP 200 without classifying the member. [SE table](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf); [PhilHealth rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/); [Circular 460](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf).

```oa-check
name: Fifteen thousand income and mandatory shares
inputs:
  msc: 15000
  income: 15000
  ec: 30
steps:
  sss: msc * 0.15 + ec
  philhealth: income * 0.05
  monthly_both: sss + philhealth + 400
  annual_both: monthly_both * 12
  monthly_other: sss + philhealth + 200
  annual_other: monthly_other * 12
expected:
  sss: 2280
  philhealth: 750
  monthly_both: 3430
  annual_both: 41160
  monthly_other: 3230
  annual_other: 38760
```

### C. At the ceilings: distinguish required from optional savings

Assume income at least **PHP 100,000** and MSC **PHP 35,000**. SSS including EC is **PHP 5,280** and PhilHealth **PHP 5,000**. Under C.1.1.3, required Pag-IBIG PHP 400 makes **PHP 10,680 monthly / PHP 128,160 annually**. Choosing **PHP 5,000 Regular Savings** instead makes **PHP 15,280 / PHP 183,360**, of which **PHP 4,600 monthly** is above that mandatory Pag-IBIG amount. This is not a statutory maximum or MP2 contribution. Under C.1.6, the required-base total would be **PHP 10,480 monthly**. The former PHP 15,250/PHP 183,000 figure omitted EC and mislabelled the optional saving as a maximum. [SE table](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf); [PhilHealth rate](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/); [Circular 460, C.1.1.3, C.1.6 and C.3](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf).

```oa-check
name: Contribution ceilings versus optional Regular Savings
inputs:
  max_msc: 35000
  health_cap: 100000
  optional_pagibig: 5000
steps:
  sss: max_msc * 0.15 + 30
  philhealth: health_cap * 0.05
  mandatory_monthly: sss + philhealth + 400
  mandatory_annual: mandatory_monthly * 12
  optional_monthly: sss + philhealth + optional_pagibig
  optional_annual: optional_monthly * 12
  extra_savings: optional_pagibig - 400
  other_group_monthly: sss + philhealth + 200
expected:
  sss: 5280
  philhealth: 5000
  mandatory_monthly: 10680
  mandatory_annual: 128160
  optional_monthly: 15280
  optional_annual: 183360
  extra_savings: 4600
  other_group_monthly: 10480
```

## When to refuse or refer

- Do not invent income, select the minimum by default, or use one fund’s basis for all three. Resolve missing evidence and recorded classifications first.
- Do not quote the both-share PHP 400 or Other Earning Groups PHP 200 total merely from the word “freelancer”. Obtain the Fund classification; refer disputed coverage to the agency.
- Do not backfill SSS SE gaps by applying the former 2%-monthly penalty, promise an unemployment/retirement benefit from a budget, or use the SE table for a household worker or OFW.
- Do not suspend PhilHealth benefits for non-payment, erase the principal automatically, or apply an interest waiver without its conditions. Refer inability to pay for the required social-worker assessment and agency classification.
- Do not promise loan eligibility from a generic contribution count or optional saving. Obtain the current product rules, member record and approval.
- Do not calculate an MP2 pre-termination, rollover, current transaction limits or card charge from unread rules. Do not sign off the unresolved owner-itemised-deduction claim.

## Sources

| Source | Read date | Read for |
|---|---|---|
| [SSS combined 2025 contribution circulars/tables](https://www.sss.gov.ph/wp-content/uploads/2024/12/2025-SSS-Contribution-Table-rev.pdf) | 2026-11-16 | Read for: Pages 1-3 visually read. Page 3 is Circular 2024-008 SE: all earnings bands, regular SS, MPF, EC and totals. Page 2 household table is separate. Other pages not relied on. |
| [RA 11199, SSS official booklet](https://www.sss.gov.ph/wp-content/uploads/2022/04/Booklet_SS-ACT-OF-2018_05172019_2.pdf) | 2026-11-16 | Read for: Section 4(a)(9) historical schedule; sections 9/9-A coverage, 14-B unemployment boundary, 18/19/19-A and 22-A contributions/no retroactive SE payments. Selected provisions only. |
| [SSS self-employed guidance](https://www.sss.gov.ph/self-employed/), [coverage](https://www.sss.gov.ph/compulsory-coverage/) and [payment guidance](https://www.sss.gov.ph/pay-contribution) | 2026-11-16 | Read for: Full operative registration/contribution and coverage material read: ages, existing record, actual income, EC, MSC changes, concurrent EE/SE, periods/PRN, gaps and no-income months. |
| [SSS payment channels](https://www.sss.gov.ph/sss-payment-channels/) | 2026-11-16 | Read for: Individual-member list dated 13 November 2026 read; other payor lists are not a universal individual checklist. |
| [SSS retirement guidance](https://www.sss.gov.ph/retirement-benefit/) | 2026-11-16 | Read for: Definition, qualifying conditions and voluntary continuation for applicants short of 120 contributions. Pension formula/amounts are not calculated here. |
| [RA 11223, UHC Act](https://lawphil.net/statutes/repacts/ra2019/ra_11223_2019.html) | 2026-11-16 | Read for: Sections 4-10, citizen coverage, direct/indirect categories, immediate eligibility, arrears and scheduled premium floor/ceiling/rate. |
| [PhilHealth 2026 rate announcement, PIA](https://pia.gov.ph/news/philhealth-sets-5-premium-contribution-rate-for-2026/) | 2026-11-16 | Read for: Article’s operative premium statements: 5%, PHP 10,000/100,000 boundaries, PHP 500/5,000, employed equal split and self-paying income. Web copy read; direct download was blocked. |
| [PhilHealth PC 2026-0011](https://www.philhealth.gov.ph/circulars/2026/PC2026-0011.pdf) | 2026-11-16 | Read for: Operative V.A-C, VIII transition and effectivity: registration/income, SPA, annual settlement/grace, debt/eligibility and financial incapacity. |
| [PhilHealth PC 2026-0010](https://www.philhealth.gov.ph/circulars/2026/PC2026-0010.pdf) | 2026-11-16 | Read for: Full operative V, transition and effectivity: 2019-2025 missed premiums, conditional one-time interest waiver, principal, instalments, application period and revocation. |
| [Pag-IBIG Circular 460, ONAR official copy](https://naro.law.upd.edu.ph/storage/01JQWKTTA92H57M9EWV31W8F1D.pdf) | 2026-11-16 | Read for: All five pages visually read: MFS, mandatory and Other Earning Groups, voluntary spouse/age, extra savings, multiple employers and repeal/effectivity. |
| [Pag-IBIG Circular 274, ONAR official copy](https://naro.law.upd.edu.ph/storage/01JW8VAVJXMC6VDPV5AJK9PJJP.pdf) | 2026-11-16 | Read for: Pages 3-6 visually read, C registration and E remittance/gaps/F status. D’s older contribution rules are superseded by Circular 460 and not used as current rates. |
| [RA 9679](https://lawphil.net/statutes/repacts/ra2009/ra_9679_2009.html) | 2026-11-16 | Read for: Sections 6-11 coverage/benefits and section 19 tax exemption. The original statutory PHP 5,000 MFS is superseded by the later circular. |
| [Pag-IBIG news archive](https://pagibigfund.gov.ph/about_news.html) and [circular index](https://www.pagibigfund.gov.ph/about_publication_circulars_memberservices.html) | 2026-11-16 | Read for: Agency’s indexed/cached descriptions of voluntary MP2, PHP 500/five years and newer circular titles/effective dates; full news/index direct fetch returned CAPTCHA. No detailed 487/499/500 terms inferred. |
| [RA 10361](https://lawphil.net/statutes/repacts/ra2013/ra_10361_2013.html) | 2026-11-16 | Read for: Section 30 social contributions; PHP 5,000-and-above worker-share boundary. |
| [TRAIN, section 11](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html); [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf); [CMEPA, section 9](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) | 2026-11-16 | Read for: OSD replacement of itemised deductions; RR 8 section 3 employment contribution illustrations; current 34(M) PERA provision. Not a universal ruling on an SE owner’s itemised expense. |

Not yet confirmed:

The old MP2 table’s **PHP 500 monthly or lump sum, five-year term, tax-free dividends historically 6%-7%, withdrawal on qualified events, and increased housing-loan eligibility** is retained here as the original topic set. The minimum/term and general tax exemption have the bounded primary support above; no future dividend rate, automatic loan enhancement or current withdrawal entitlement is confirmed. Full Circular 487 and its account transition conditions remain unread after ordinary official-site access returned CAPTCHA; no security challenge was bypassed. Circulars 499/500/503 were discovered in the agency index but their full operational rules were not read. Do not use older channel or payout lists to substitute for them.

The former **15th** direct Pag-IBIG deadline is corrected by the readable Circular 274 E.8 **10th** rule. The former blanket semi-annual/annual advance-payment claim and named Pag-IBIG channels **BDO/BPI/Landbank/Metrobank, GCash/Maya, Bayad/SM/7-Eleven and branches** are retained for recovery, not a confirmed current channel instruction. The old blanket **24-month loan eligibility** and “no back-payment required” gap cure remain unconfirmed for individual products.

Original portal pointers retained for recovery: **my.sss.gov.ph** (contributions, PRN and claims), **memberinquiry.philhealth.gov.ph** (membership, updates and MDR), **virtual.pagibigfund.gov.ph** (savings, loans and updates), the **SSS Mobile App**, and **bir.gov.ph** (eFPS/ITR). The public agency guidance above supports the stated workflows; authenticated screens and every former portal function were not tested in this review.

The old registration checklist **SSS RS-1/two government IDs/proof of income; PhilHealth first-time birth certificate; Pag-IBIG ID/income proof, 12-digit MID and free Loyalty Card/UMID equivalence** is retained for documentary recovery. Use the actual transaction checklist; no free card or universal document count is promised. The earlier universal senior **PhilHealth 120-month/lifetime** exemption and Pag-IBIG retirement-after-65 statement also require the applicable category/claim rules rather than this generic checklist.

The prior owner-itemised-deduction table’s categorical **NO for own SSS, PhilHealth and Pag-IBIG** and precise claim that **TRAIN repealed the PHP 2,400-per-year section 34(M) deduction from 2018** are retained with Jonathan’s tax-correction credit above. The exact historical repeal explanation and all owner-expense categories were not fully established here. Current 34(M) is a PERA provision; OSD does not permit a second itemised deduction. The earlier RR 11-2018 and RR 7-2012 references are preserved as historical references, not treated as current social-deduction or complete BIR-registration authority.
