---
name: il-employee-tax-refund
description: Use this skill when advising salaried Israeli employees on voluntary tax refund claims. Trigger on phrases like "tax refund Israel employee", "החזר מס לשכירים", "Form 135", "טופס 135", "Form 106", "טופס 106", "miluim refund", "מילואים החזר מס", "nekudot zikui missed", "yishuv mezakeh", "ישוב מזכה", "Section 46 donations", "תרומות", "oleh chadash credit points", "maternity tax refund Israel", or any Israeli employee tax refund query. ALWAYS read this skill before advising on Israeli employee tax refunds.
version: 1.0
jurisdiction: IL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Employee Tax Refund

## Israel Employee Tax Refund Skill v1.0

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Israel (מדינת ישראל) |
| Scope | Voluntary tax refund claims for salaried employees |
| Currency | NIS (Israeli New Shekel — ₪) |
| Primary form | Form 135 (דוח שנתי מקוצר) or online refund portal |
| Key document | Form 106 (אישור שנתי על משכורת ומס שנוכה) from employer |
| Refund window | 6 years from end of tax year (Section 160, Income Tax Ordinance) |
| Online portal | https://secapp.taxes.gov.il |
| Credit point value (2026) | NIS 2,904/year (NIS 242/month) — frozen 2025–2027 |
| Tax authority | Israel Tax Authority (ITA — רשות המיסים) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Israel-licensed רואה חשבון or יועץ מס |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown credit point eligibility | Apply base resident points only |
| Unknown whether tax coordination (Tium Mas) was filed | Assume it was not filed — calculate refund accordingly |
| Unknown donation institution approval | Verify before claiming Section 46 credit |
| Unknown Yishuv Mezakeh eligibility | Verify against annual ITA locality list |

## Section 2 — Refund window

- **Refund window rule** — The retroactive refund window is 6 calendar years from the end of the tax year, per Section 160 of the Income Tax Ordinance  _(Section 160, Income Tax Ordinance)_

**Refund window deadlines table**

| Tax year | Last day to claim refund |
| --- | --- |
| 2020 | 31.12.2026 |
| 2021 | 31.12.2027 |
| 2022 | 31.12.2028 |
| 2023 | 31.12.2029 |
| 2024 | 31.12.2030 |
| 2025 | 31.12.2031 |

Years older than 2020 can no longer be claimed in 2026.

## Section 3 — Reading Form 106

- **Form 106** — Form 106 (אישור שנתי על משכורת ומס שנוכה) is the annual income summary issued by the employer by March 31 of the following year.

### Key fields

**Key fields table**

| Field | Hebrew label | What it tells you |
| --- | --- | --- |
| 042 | סה"כ מס שנוכה במקור | Total income tax withheld by this employer |
| 158 / 172 | משכורת חייבת | Taxable salary — base for tax-due calculation |
| 218 / 219 | הפקדה לקרן השתלמות | Keren Hishtalmut deposit |
| Months worked | חודשי עבודה | If less than 12, partial-year work — common refund trigger |

- **Multiple Form 106s** — If the employee has multiple Form 106s from the same tax year (job change), sum field 042 across all forms.

### Bituach Leumi income-replacement payments

If the employee received BTL payments during the year, request the annual confirmation (אישור שנתי למס הכנסה) from Bituach Leumi:

**BTL income-replacement payments table**

| BTL payment | Hebrew | Tax treatment |
| --- | --- | --- |
| Maternity pay | דמי לידה | Fully taxable — add to 158/172 and 042 |
| Unemployment pay | דמי אבטלה | Fully taxable — add to 158/172 and 042 |
| Short-term work injury (up to 91 days) | דמי פגיעה | Fully taxable — add to 158/172 and 042 |
| Pregnancy preservation pay | דמי שמירת היריון | Fully taxable — add to 158/172 and 042 |
| Reserve duty pay | תגמולי מילואים | Usually inside Form 106 already; only add direct-from-BTL payments |

**Common pattern:** The refund usually originates from the salary side, not the BTL side. BTL typically under-withholds tax, while the employer over-withholds during worked months (assuming full-year salary).

## Section 4 — Refund triggers

**Refund triggers table**

| # | Trigger | When it applies | Statutory anchor |
| --- | --- | --- | --- |
| 1 | Mid-year job change / multiple employers | Two or more Form 106s for the same year and no Tium Mas was filed | Section 164 ITO |
| 2 | Partial-year work / unemployment | Less than 12 months worked | Withholding over-projection |
| 3 | Maternity / paternity leave | Received דמי לידה from Bituach Leumi | Section 9(6) ITO |
| 4 | Military reserve duty (Miluim — מילואים) | 30+ days of reserve service in the prior tax year | Section 39B ITO (Amendment 283) |
| 5 | Charitable donations | Total donations to Section 46-approved institutions ≥ NIS 207 (2026 minimum) | Section 46 ITO |
| 6 | Yishuv Mezakeh (ישוב מזכה) | Center of life in eligible periphery locality for 12+ months | Section 11 ITO + Negev/Galilee Law |
| 7 | New immigrant credit points | Oleh Chadash within first 54 months of Aliyah (post-2022) | Section 35 ITO + Amendment 262 |
| 8 | Completed academic degree | BA: 1 point/year up to 3 years (graduates 2023+); MA: 0.5 point for 2 years | Section 40g ITO |
| 9 | Single parent / alimony | Court judgment establishing single-parent status | Sections 64, 65, 66 ITO |
| 10 | Disability exemption | 100% medical disability, blindness, or 90%+ multi-organ calculation | Section 9(5) ITO |
| 11 | Self-deposit to pension beyond employer's deposit | Employee deposit to pension fund or life insurance | Sections 45A and 47 ITO |
| 12 | Early Keren Hishtalmut withdrawal | Bank withheld 47% but real marginal rate is lower | Section 9(16a) + Section 164 ITO |
| 13 | Missed child credit points | Custody changed but employer's Form 101 not updated | Section 40 ITO |
| 14 | One-time bonus / 13th salary | Monthly over-withholding on large bonus; annual reconciliation produces refund | Regulation 6 of withholding regulations |

### 5.1 Reserve duty credit points (Section 39B, Amendment 283)

**Reserve duty credit points table**  _(Section 39B ITO, Amendment 283)_

| Days served in tax year | Points awarded | Annual value (NIS) |
| --- | --- | --- |
| 30–39 | 0.5 | 1,452 |
| 40–49 | 0.75 | 2,178 |
| 50–54 | 1.0 | 2,904 |
| Each additional 5 days | +0.25 | +726 |
| Maximum | 4.0 | 11,616 |

- **Realization timing** — Realized in the year AFTER the service (service in 2025 → claim on 2026 refund)  _(Section 39B ITO, Amendment 283)_

### 5.2 New immigrant schedule (post-2022, Amendment 262)

**New immigrant schedule table**  _(Section 35 ITO + Amendment 262)_

| Period from Aliyah date | Monthly points | Annual rate |
| --- | --- | --- |
| Months 1–12 | 1/12 | 1 point |
| Months 13–30 (18 months) | 1/4 | 3 points |
| Months 31–42 (12 months) | 1/6 | 2 points |
| Months 43–54 (12 months) | 1/12 | 1 point |

- **Total points and pre-2022 schedule** — Total: 8.5 credit points over 54 months. For Olim who arrived before 1.1.2022, the pre-Amendment 262 schedule applies (7.5 points over 42 months).  _(Section 35 ITO + Amendment 262)_

**Section 35 is for credit points only — there is no "Section 35 mortgage interest deduction for Olim."** Do not promise a mortgage refund under this section.

### 5.3 Donation credit (Section 46)

- **Minimum donation** — NIS 207 (2026)  _(Section 46 ITO)_
- **Credit rate** — 35% of donated amount  _(Section 46 ITO)_
- **Annual ceiling** — NIS 10,354,816 or 30% of taxable income, whichever is lower  _(Section 46 ITO)_
- **Institution approval requirement** — Institution must hold active Section 46 approval for the year of donation  _(Section 46 ITO)_
- **Valid receipt formats** — Valid receipt formats: original, certified copy, or electronic (marked מסמך ממוחשב)  _(Section 46 ITO)_

### 5.4 Yishuv Mezakeh

- **Yishuv Mezakeh** — Residents of eligible localities receive a percentage discount on tax due, capped at a NIS ceiling. The list of eligible localities and per-locality percentage is published annually by the ITA. Always verify against the current list for the relevant tax year.

### 5.5 Disability exemption (Section 9(5))

**Disability exemption table**  _(Section 9(5) ITO)_

| Duration | Exempt earned income ceiling (2026) |
| --- | --- |
| 365+ days (long-term) | NIS 445,200/year |
| 185–364 days (short-term) | NIS 81,960/year |
| חוק הנכים / חוק נפגעי פעולות איבה pension | NIS 684,000/year |

- **Qualifying conditions** — Qualifying conditions: 100% medical disability, blindness, or 90%+ via multi-organ-injury calculation (ועדה רפואית determination required).  _(Section 9(5) ITO)_

## Section 6 — Estimating the refund

- **Refund estimate formula** — Correct tax (under brackets and credits) − Tax actually withheld (sum of field 042 across all Form 106s)

### 2026 income tax brackets for employees

**2026 income tax brackets table**

| Monthly salary band (NIS) | Annual band (NIS) | Rate |
| --- | --- | --- |
| Up to 7,010 | Up to 84,120 | 10% |
| 7,011 – 10,060 | 84,121 – 120,720 | 14% |
| 10,061 – 19,000 | 120,721 – 228,000 | 20% |
| 19,001 – 25,100 | 228,001 – 301,200 | 31% |
| 25,101 – 46,690 | 301,201 – 560,280 | 35% |
| 46,691 and above | 560,281 and above | 47% |
| Plus surtax | Above 721,560 annual | Additional 3% |

For prior tax years, use the brackets that applied to that year.

Present the estimate as a range, not a single number, and note that the ITA's actual calculation may differ.

## Section 7 — Document checklist by trigger

**Document checklist table**

| Trigger | Required documents |
| --- | --- |
| All claims | Form 106 from every employer; Teudat Zehut (תעודת זהות) + Sipach; bank account confirmation (אישור ניהול חשבון) |
| Multiple employers | All Form 106s — sum field 042 across them |
| Partial year / unemployment | BTL annual confirmation listing months and amounts |
| Maternity/paternity leave | BTL דמי לידה annual confirmation |
| Reserve duty (Miluim) | Form 3010 (אישור על ימי מילואים) from IDF reserve unit |
| Section 46 donations | Signed receipts from each approved institution |
| Yishuv Mezakeh | אישור תושבות from local authority for each year (12+ months residence) |
| New immigrant | Teudat Oleh (תעודת עולה) + Aliyah date |
| Academic degree | Diploma + transcript (verifies completion year) |
| Single parent / alimony | Court judgment + bank transfer records |
| Disability | Medical board determination (ועדה רפואית) + ITA disability committee ratification |
| Pension self-deposit | Annual deposit certificate from pension/insurance provider |
| Keren Hishtalmut early withdrawal | תלוש משיכה showing 47% withholding |

## Section 8 — Submission channels

**Submission channels table**

| Channel | When to use | Where |
| --- | --- | --- |
| Online refund portal | Not obligated to file Form 1301; has digital government identity; has scanned documents | https://secapp.taxes.gov.il |
| Manual Form 135 | Prefers paper; online portal doesn't support the case; identity verification issues | https://www.gov.il/he/service/itc135 — submit at the assigned Misrad Shuma (משרד שומה) |

- **Form 1301 requirement override** — **If the employee is required to file Form 1301** (income above surtax threshold, foreign income, capital gains), neither Form 135 nor the online portal applies. The refund computation must be integrated into Form 1301.

## Section 9 — Prospective fix (Form 101)

- **Form 101 update** — If a refund trigger is ongoing (still a single parent, still an Oleh in credit-point window, still residing in Yishuv Mezakeh), the employee should update their Form 101 at the employer for the current and following year. Form 101 sets the credit-point basis the employer uses for withholding.

Without this fix, the employee will file the same refund every year for the same missed credit. The retrospective refund returns last year's over-withholding; updating Form 101 stops the over-withholding going forward.

## Section 10 — Worked examples

### Example 1 — Two jobs in 2024

**Scenario:** Developer worked 6 months at Employer A (NIS 25,000/month) and 6 months at Employer B (NIS 22,000/month). No mid-year Tium Mas filed.

**Working:**
- Field 042: NIS 24,800 withheld at A + NIS 22,400 at B = NIS 47,200 total withheld
- Aggregate annual income: NIS 282,000
- Correct annual tax (2024 brackets, 2.75 default points for female): ~NIS 43,700
- Estimated refund: NIS 3,100 – NIS 3,800
- Trigger: #1 (mid-year job change)
- Documents: both Form 106s, Teudat Zehut, bank confirmation
- Deadline: 31.12.2030

### Example 2 — Reserve duty 65 days in 2025

**Scenario:** Teacher served 65 days of reserve duty in 2025.

**Working:**
- Section 39B schedule: 50 days = 1.0 point; 15 additional days (over 50) at +0.25 per 5 days = +0.75 points
- Total: 1.75 points × NIS 2,904 = NIS 5,082 expected refund for 2026
- Points are realized in the year AFTER service → claim on 2026 refund
- Document: Form 3010 from reserve unit
- Submit after 2026 Form 106 is issued (by 31.3.2027)

### Example 3 — Section 46 donations for 2022

**Scenario:** Employee donated NIS 6,000 to three Section 46-approved nonprofits in 2022.

**Working:**
- Credit: NIS 6,000 × 35% = NIS 2,100
- Deadline: 31.12.2028 — still open
- Documents: signed original receipts; verify each institution's Section 46 approval was active in 2022

## Section 11 — After submission

- **Processing timeline** — ITA must process and pay the refund within one year from the assessment date, or two years from the end of the tax year, whichever is later
- **Late refund interest** — Refunds paid after the statutory window accrue CPI linkage (הצמדה) plus 4% annual interest
- **Document request response** — If the ITA sends a "Drisha LeHashlamat Mismachim" (דרישה להשלמת מסמכים) — request for additional documents — respond within the stated deadline or the request closes

## Section 12 — Reference material

**Reference material table**

| Resource | Reference |
| --- | --- |
| Tax Authority Form 135 | https://www.gov.il/he/service/itc135 |
| Online refund portal | https://secapp.taxes.gov.il |
| Kol Zchut — tax refund overview | https://www.kolzchut.org.il/he/החזר_מס_הכנסה |
| Kol Zchut — credit points | https://www.kolzchut.org.il/he/נקודות_זיכוי |
| Kol Zchut — reserve duty points | https://www.kolzchut.org.il/he/נקודות_זיכוי_ממס_הכנסה_ללוחמי_מילואים |
| Kol Zchut — Section 46 donations | https://www.kolzchut.org.il/he/זיכוי_ממס_הכנסה_בשל_תרומה_(סעיף_46) |
| Kol Zchut — Yishuv Mezakeh | https://www.kolzchut.org.il/he/זיכוי_ממס_הכנסה_לתושבים_בפריפריה |
| Kol Zchut — disability exemption | https://www.kolzchut.org.il/he/פטור_ממס_הכנסה_לאנשים_עם_נכות |
| Kol Zchut — Form 106 | https://www.kolzchut.org.il/he/טופס_106 |

## Disclaimer

> **חשוב:** כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional — such as a רואה חשבון (Ro'eh Cheshbon — CPA) or יועץ מס (Yo'etz Mas — tax advisor) licensed in Israel — before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
