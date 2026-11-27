---
name: 990-returns
description: "Form 990 (full return) in the United States: how I do it"
jurisdiction: US
tax_year: 2025
last_updated: 2026-11-27
version: 0.1
type: filing-howto
category: federal
tax_year_notes: "2025 Form 990: calendar 2025 or fiscal 2025-2026; not a 2026 tax-year guide"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Anthony Bandura"
reviewed_on: 2026-11-03
tier: 1
domain: corporate-tax
---

# Form 990 full return v0.1

> General reference only. This Guide covers the 2025 return, not an individual organization's filing position. A qualified professional must review the completed return and its supporting records before filing. Circular 230 notice: this general reference is not written tax advice for a particular taxpayer or a means of avoiding penalties.

## Scope

Prepare the United States **full Form 990**, an annual information return under IRC §6033 for most section 501(a) exempt organizations, certain section 527 political organizations and section 4947(a)(1) nonexempt charitable trusts. It reports activities, governance, finances and compensation; compute unrelated business tax separately. The return is generally public. Use the 2025 form for calendar 2025 or a fiscal year beginning in 2025 and ending in 2026. [IRS 2025 instructions, Overview and §§A, D](https://www.irs.gov/instructions/i990).

### Choose the return before preparing it

Apply the exclusions first; receipts alone do not establish a filing obligation. Gross receipts mean receipts from all sources **before costs or expenses**.

| Route | Operative condition | Official source |
|---|---|---|
| Full 990 | For an otherwise required section 501(a) filer: receipts at least $200,000 **or** year-end assets at least $500,000, except an organization eligible for 990-N. An eligible shorter-form filer choosing full 990 must complete it fully. | [2025 instructions §A](https://www.irs.gov/instructions/i990) |
| 990-EZ | Receipts **under** $200,000 **and** year-end assets **under** $500,000, subject to forced-full-return rules below. This Guide prepares full 990 if it is chosen instead. | [2025 instructions §A](https://www.irs.gov/instructions/i990) |
| 990-N | Normally $50,000 or less of gross receipts; apply the multi-year/new-organization tests in Appendix B, rather than assuming this year's receipts alone decide it. Supporting and political organizations have special rules. | [2025 instructions §§A–B, Appendix B](https://www.irs.gov/instructions/i990) |
| Full-return overrides | If an annual information return is required: donor-advised-fund sponsors use 990; section 512(b)(13) controlling organizations use 990 if funds were transferred with a controlled entity during the year. Section 501(c)(21) black lung trusts use 990, except where eligible for 990-N. | [2025 instructions §A](https://www.irs.gov/instructions/i990) |
| Supporting organizations | Section 509(a)(3) organizations file 990 or 990-EZ even if normally $50,000 or less. Exceptions: church integrated auxiliaries; exclusively religious activities of religious orders; and organizations normally at most $5,000 supporting a section 501(c)(3) religious organization. The last category submits 990-N unless it voluntarily files 990/EZ. | [2025 instructions §A](https://www.irs.gov/instructions/i990) |
| Political organizations | Required 990/EZ at receipts at least $25,000, or $100,000 for a qualified state/local political organization. Section B excludes the specified party/candidate committees, caucuses/associations of state/local officials and FECA-reporting committees. Political organizations do not submit 990-N. Then apply the full/EZ size tests. | [IRC §6033(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6033.htm); [2025 instructions §§A–B](https://www.irs.gov/instructions/i990) |
| Separate returns or exceptions | Private foundations, including private operating foundations and 4947(a)(1) trusts treated as foundations: 990-PF. Qualifying religious and governmental organizations can be excepted under §B; do not assume every religious nonprofit is exempt from filing. | [2025 instructions §B](https://www.irs.gov/instructions/i990) |
| 990-T in addition | At least $1,000 total gross income from all unrelated trades/businesses triggers 990-T separately, even where 990/EZ/N also applies. Check Part V, 3a–3b; if 990-T has not been filed when filing 990, explain the “No” on 3b in Schedule O. | [2025 instructions, Overview and Part V](https://www.irs.gov/instructions/i990) |

## Ask the client first

Obtain from the records before asking for missing facts:

- Exempt subsection, determination letter, formation date, prior returns, public-charity category, receipts and year-end assets; pending exemption, revocation or group inclusion?
- Accounting-year dates, accounting basis, method/year changes, final trial balance, financial statements and separate versus consolidated audit/review/compilation?
- Related/controlled organizations, disregarded entities, joint ventures, new programs or states, and grants at home or abroad?
- Every officer, voting director/trustee and relevant employee's role/dates, calendar-year W-2/1099 compensation, benefits, related-organization pay and prior five-year reporting?
- Fundraising, gaming, noncash gifts, donor records, lobbying/political activity and interested-person transactions?
- Governing documents, minutes, written policies, compensation decisions and distribution/review of the final return by the board?

## The method, step by step

### 1. Close the books, establish the period and sequence the work

Keep last year's return beside the reconciled trial balance: carry forward classifications, elections and relevant schedules, then test this year's changes. Generally use the accounting method regularly used for the books unless instructed otherwise. Identify year/method changes before entering amounts. Keep a reconciliation between books and the filed return. [IRS §§C–D, J](https://www.irs.gov/instructions/i990).

Follow §C: heading A–F and H(a)–M; identify Schedule R relationships and Part VII people; Parts VIII, IX and X; heading G; Parts III, V, VII, XI and XII; Schedule L if required; Part VI; Part I; Part IV; remaining applicable schedules; signature Part II. Complete **Schedule O as you go**, including mandatory Part VI 11b and 19 explanations; all full-990 filers attach it. Schedule L feeds Part VI 1b independence; Part I derives from the other parts. Assemble the core in numeric order and schedules alphabetically, with only authorized attachments. [IRS §C and §J](https://www.irs.gov/instructions/i990).

### 2. Check Schedule A public-charity status first where applicable

Part IV 1 sends section 501(c)(3) organizations and 4947(a)(1) trusts other than private foundations to Schedule A. Record the correct Part I category. For a charity under section 170(b)(1)(A)(iv)/(vi) or 509(a)(2) **outside its initial five years**, complete the applicable Part II/III support test first. A failed current-year percentage alone does not establish foundation status: apply the previous-year and alternative tests too. [IRS §C](https://www.irs.gov/instructions/i990); [2025 Schedule A instructions](https://www.irs.gov/instructions/i990sa).

- **Part II:** enter the five-year support schedule (2021–2025 for calendar 2025). Compute line 6 public support after the line 5 excess-contributor adjustment and line 11 total support; line 14 is line 6 divided by line 11. Contributions from a donor/related donor group above 2% of five-year total support are excluded from public support, with the governmental/publicly supported donor exceptions in the instructions. Related-activity receipts are disclosed on line 12, not added to the Part II support denominator. At least **33⅓%** on line 14 or prior-year line 15 meets the percentage test (16a/16b). For a qualifying newly recognized charity's first five years, use line 13 and stop the filed computation there. [Schedule A Part II](https://www.irs.gov/instructions/i990sa); [Reg. §1.170A-9(f)](https://www.ecfr.gov/current/title-26/section-1.170A-9).
- **Part III, section 509(a)(2):** report qualifying contributions and related-activity gross receipts; remove disqualified-person receipts at 7a and excess per-payer related receipts at 7b (above the greater of $5,000 or 1% of that year's support). Public support at line 8 must be **more than one-third** of line 13 total support, and line 10c investment/UBTI component **not more than one-third**, using the applicable current/prior-year tests at 19a/19b. A qualifying charity in its first five years checks line 14 and stops there. [IRC §509(a)(2), (d)–(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partII-sec509.htm); [Schedule A Part III](https://www.irs.gov/instructions/i990sa).

Do not declare loss of public-charity status from these abbreviated tests where an unusual grant, an alternative category or the facts-and-circumstances route could change the result. See the bounded holds below. If no applicable public-charity route qualifies, use 990-PF as §C directs.

### 3. Build the core from the records

| Part/heading | Preparation and cross-check | Official source |
|---|---|---|
| A–M | Correct year/dates, legal name/address, EIN, principal officer, status and appropriate change/initial/final/amended/pending checkboxes. Do not combine separate EINs except the permitted group, disregarded-entity or partnership rules. Include all items of a wholly owned disregarded entity and the organization's share of partnership/joint-venture items; investigate Schedule R. | [2025 instructions heading and §J](https://www.irs.gov/instructions/i990) |
| VIII and G | Record contributions gross, not net of fundraising expenses; separate program revenue, investment and other receipts on their designated lines. All filers complete A; except political organizations, B–D classify related/exempt, unrelated, and excluded revenue and must sum to A. VIII 12 totals revenue. Heading G adds VIII 6b, 7b, 8b, 9b and 10b back to VIII 12, including both applicable columns for 6b/7b. | [2025 instructions Part VIII and item G](https://www.irs.gov/instructions/i990) |
| IX | Use the normal accounting method. Section 501(c)(3)/(4) filers complete total, program, management/general and fundraising columns A–D; other organizations must complete A and may complete B–D. Allocate reasonably and document the basis. Do not duplicate expenses already netted on VIII 6b/7b/8b/9b/10b. IX 25 totals the functional expense lines. | [2025 instructions Part IX](https://www.irs.gov/instructions/i990) |
| X | Use the prior closing balances as opening balances and current records for closing assets/liabilities. Complete every applicable balance-sheet line; X 33 = X 26 liabilities + X 32 net assets = X 16 assets. Use the correct donor-restriction/fund categories. | [2025 instructions Part X](https://www.irs.gov/instructions/i990) |
| III | Describe mission and significant new/changed/ceased programs; explain changes on O. Report the three largest program accomplishments by expenses, other programs at 4d/O and total at 4e. Section 501(c)(3)/(4) filers report their specified expenses/grants/revenue; these numeric entries are optional for others. | [2025 instructions Part III](https://www.irs.gov/instructions/i990) |
| V | Answer each applicable compliance question from payroll/information returns, 990-T, foreign-account and activity records. Count information returns and employees for the calendar year ending with/within the tax year as instructed. Investigate every “Yes” and any separate required return; 990 does not replace it. | [2025 instructions Part V](https://www.irs.gov/instructions/i990) |
| XI | Lines 1/2 agree with VIII 12(A)/IX 25(A); 3 is their difference. Add beginning net assets at 4 and adjustments at 5–9 (including unrealized gains, donated services/facilities and prior-period adjustments as applicable); 10 must equal X 32(B). Explain line 9 changes on O. | [2025 instructions Part XI](https://www.irs.gov/instructions/i990) |
| XII / D | Report accounting method and compilation/review/audit facts. Separate independent audited statements trigger IV 12a and D XI–XII; consolidated-only statements at IV 12b make those reconciliations optional if 12a is No. A compilation or review is not an audit. Explain method changes on O. A required [IRC §481(a) adjustment](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partIII-sec481.htm) is reported in VIII–XI and D XI–XII as applicable, with O explanation; a change in reporting a never-adopted tax method does not itself create a §481 adjustment. | [2025 instructions §§C–D, Part IV 12a–b and XII](https://www.irs.gov/instructions/i990) |
| VI | Complete Schedule L before testing board independence at 1b. Answer from actual governance records. Policies at 12–14 cover conflicts, whistleblowing and document retention/destruction; do not imply the Code requires these policies. For 11a, every voting board member must receive the complete final return including schedules before filing; an offer to supply it or a redacted copy is insufficient. Describe actual review or its absence at 11b/O; report compensation-setting process at 15 and public availability at 19/O. | [2025 instructions Part VI](https://www.irs.gov/instructions/i990) |
| I / II | Populate summary from the completed core, reconcile totals, then obtain a current authorized officer's/trustee's signature. A paid preparer signs and supplies PTIN and a copy to the organization; use the form's preparer-contact authorization as instructed. Never enter an SSN in a public field. | [2025 instructions Parts I–II and Overview](https://www.irs.gov/instructions/i990) |

### 4. Build Part VII compensation on the right period

Use the calendar year ending with/within the organization's tax year for compensation, even for current officers whose status is tested during the fiscal year. Reconcile to amounts **required** on W-2/1099, correcting an erroneous information return separately. Reportable compensation generally uses the greater of W-2 boxes 1/5, plus applicable 1099-NEC box 1 / 1099-MISC box 6 amounts; column D is organization pay, E related-organization pay, F other compensation including reportable deferred/health benefits under the instructions. [2025 Part VII instructions](https://www.irs.gov/instructions/i990).

| Person/section | Listing test and conditions | Official source |
|---|---|---|
| Current officers, voting directors/trustees | List all, including unpaid; fiscal-year status is service at any time in that tax year. Top management and financial officials are officers regardless of title. | [Part VII A](https://www.irs.gov/instructions/i990) |
| Key employees | Employee other than officer/director/trustee; over $150,000 reportable compensation; officer-like responsibility for the whole organization **or** management of at least 10% of activities/assets/income/expenses **or** authority over at least 10% of capital spending/operating budget/employee pay; and among the top 20 satisfying pay/responsibility tests. Include related pay under the reporting exceptions. | [Part VII A, Key employee](https://www.irs.gov/instructions/i990) |
| Five highest compensated employees | Up to five over $100,000 reportable compensation, excluding current officers/directors/trustees and listed key employees; rank by reportable compensation to choose the five. | [Part VII A](https://www.irs.gov/instructions/i990) |
| Former persons | Five-year lookback, including those who should have been reported. Former officers/key employees: over $100,000; former directors/trustees: over $10,000 **for past services in that capacity**. Former highest-paid employees must also not be employees at any time in the relevant calendar year and must rank among the current top five if they were employees. Apply all status tests before listing. | [Part VII A, column C](https://www.irs.gov/instructions/i990) |
| Related pay / other pay | Take related organizations into account. Related-organization reportable pay below $10,000 per organization may be disregarded, except pay for former director/trustee services. Other-pay items below $10,000 per item may be disregarded except the five mandatory types: employer qualified defined-contribution contributions; qualified defined-benefit actuarial changes; specified health benefits; nonqualified defined-contribution contributions/deferrals; and nonqualified defined-benefit actuarial changes. These exceptions do not apply to Schedule J. | [Part VII A, $10,000 exceptions and columns E–F](https://www.irs.gov/instructions/i990) |
| Independent contractors, B | List the five highest paid **over $100,000** for services from this organization for that calendar year; individuals and entities count, utilities/insurance providers do not. Related-organization pay is not included here. Separately report the count over the threshold on B 2. | [Part VII B](https://www.irs.gov/instructions/i990) |

List Section A people highest to lowest by D+E+F; ties follow the instructions' role order. Part VII A 3–5/IV 23 trigger J: listed former persons, listed persons with reportable plus other compensation over $150,000, or the specified known unrelated-organization pay for services to the filer. Part IX can differ because it uses the organization's accounting period/method. [Part VII](https://www.irs.gov/instructions/i990).

### 5. Complete every required schedule

Use each actual Part IV question and the schedule's instructions; this map identifies the destination, not permission to omit a lower-dollar transaction otherwise reportable. [2025 Form 990, Part IV](https://www.irs.gov/pub/irs-prior/f990--2025.pdf).

| IV line | Schedule destination and trigger | Official source |
|---|---|---|
| 1–2 | A for covered charities/trusts; B under contributor rules below. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 3–5 | C I for direct/indirect campaign activity; C II for section 501(c)(3) lobbying or a 501(h) election even without lobbying; C III for 501(c)(4)/(5)/(6) receiving specified dues. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 6–10 | D I–V respectively: donor-advised/similar funds; conservation easements; art/treasure collections; escrow/custodial/intermediary or specified credit/debt services; donor-restricted/quasi-endowments including through related organizations. | [2025 Form IV](https://www.irs.gov/pub/irs-prior/f990--2025.pdf) |
| 11a–f, 12 | D VI for land/buildings/equipment; D VII–IX for other securities/program investments/other assets meeting the respective 5%-of-assets tests; D X for other liabilities or uncertain-tax-position footnotes. D XI–XII under the audit distinction above. | [2025 Form IV](https://www.irs.gov/pub/irs-prior/f990--2025.pdf) |
| 13, 20 | E for a covered school; H for hospital facilities, with the most recent audited statements attached (consolidated statements/details if applicable). | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 14–16 | F I/IV for foreign activity revenues/expenses over $10,000 or aggregate foreign-entity investments with book value at least $100,000 at any time in the tax year; F II/IV for grants over $5,000 to any foreign organization; F III/IV for aggregate grants over $5,000 to foreign individuals. Include grants through domestic intermediaries for designated foreign recipients. Answer office/employee/agent question 14a separately. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 17–19 | G I for specified professional fundraising costs over $15,000; G II for total event gross income plus event contributions over $15,000; G III for gaming gross income over $15,000. | [2025 Form IV](https://www.irs.gov/pub/irs-prior/f990--2025.pdf) |
| 21–22 | I I/II for assistance over $5,000 to any domestic organization/government, not aggregate across recipients; I I/III for aggregate assistance over $5,000 to/for domestic individuals. Exclude designated foreign-recipient assistance routed through domestic intermediaries. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 23–24 | J as above; K for each post-December 31, 2002 tax-exempt bond issue with more than $100,000 principal outstanding at year end, except legally defeased bonds; answer 24b–d when 24a is Yes. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 25–28 | L I for applicable 501(c)(3)/(4)/(29) excess benefits, including previously unreported prior-year transactions; L II loans/receivables/payables, III grants/assistance, IV business transactions with interested persons, using its own definitions, thresholds and exceptions. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 29–30 | M if noncash contributions exceed $25,000, or any specified art/historical assets or qualified conservation contributions regardless of amount; services/use of facilities are excluded from the noncash threshold. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 31–32 | N I for liquidation/termination/dissolution and cessation; N II for significant disposition (more than 25% of net assets under the schedule's definitions/exceptions). Check I 2; final return also checks heading B. | [2025 Form IV](https://www.irs.gov/pub/irs-prior/f990--2025.pdf); [instructions](https://www.irs.gov/instructions/i990) |
| 33–37 | R I for wholly owned disregarded entities; II–IV and V 1 for related entities; V 2 for specified controlled-entity transactions and noncharitable related transfers. VI covers each unrelated partnership exceeding the 5% activity test measured by gross revenue or year-end assets, whichever is greater, aggregating indirect holdings; apply the passive-investment exceptions before deciding. | [2025 instructions](https://www.irs.gov/instructions/i990) |
| 38 | O for every filer, including VI 11b and 19. Other schedules' narratives go in their own supplemental parts. | [2025 instructions](https://www.irs.gov/instructions/i990) |

**Schedule B:** generally report donors with at least $5,000 money/property in the tax year; separate independent gifts below $1,000 may be disregarded in aggregation. Qualifying 501(c)(3) organizations meeting the 33⅓% public-support test and checking A II 13/16a/16b use the special rule: at least $5,000 **and in excess of 2%** of annual contributions (VIII 1h), under Reg. §1.6033-2(a)(2)(iii)(A). This is different from A's five-year contributor limitation. Where IRS wording “greater of” would include an amount exactly equal to 2%, the regulation controls the name/address reporting boundary; hold that boundary for review before omitting donor details. For filers other than 501(c)(3)/4947(a)(1) and 527, enter N/A for donor names/addresses but retain them in the records. Special club/fraternal-purpose reporting is held below. [Reg. §1.6033-2](https://www.ecfr.gov/current/title-26/section-1.6033-2); [continuous-use B instructions applicable to 2025](https://www.irs.gov/instructions/i990sb).

## Boundary and exception table

| Boundary | Action |
|---|---|
| Required line versus conditional follow-up | Enter zero where appropriate on applicable amount lines; leave an “If Yes” follow-up blank when its parent answer is No. Do not omit a required schedule or net contributions against fundraising expenses. [IRS §§H, J](https://www.irs.gov/instructions/i990) |
| Rounding | Retain cents while adding, then round the line total to whole dollars; amounts below 50 cents down, 50–99 cents up. [IRS §J](https://www.irs.gov/instructions/i990) |
| Separate EINs | Do not consolidate affiliated corporations merely because there is common control. Permitted group/DE/partnership reporting follows the specific rules; specialist routes below remain holds. [IRS §§A, J](https://www.irs.gov/instructions/i990) |

## Worked cases

These are illustrative checks for this revision. The original Guide contained no numeric worked cases.

**A. Calendar 2025 ordinary full-return filer:** assume no filing exception/990-N eligibility or special route. Gross receipts $200,000, assets $300,000: full 990 is required because equality meets the receipt threshold. At $199,999 with the same assets, 990-EZ is available; electing full 990 still requires all core parts and triggered schedules. Due May 15, 2026; a timely proper 8868 extends filing to November 15, shifted to Monday November 16, 2026. If filed ten days late without reasonable cause and without an extension, the ordinary daily charge is $250, below the $10,000 receipt-based cap. [IRS §§A, E–F](https://www.irs.gov/instructions/i990); [8868 instructions](https://www.irs.gov/instructions/i8868).

```oa-check
name: 2025 full return threshold and 2026 late filing
inputs:
  receipts: 200000
  assets: 300000
  days_late: 10
steps:
  ez_receipt_headroom: 200000 - receipts
  ez_asset_headroom: 500000 - assets
  daily_total: days_late * 25
  receipts_cap: receipts * 0.05
  penalty: min(daily_total, 13000, receipts_cap)
expected:
  ez_receipt_headroom: 0
  ez_asset_headroom: 200000
  penalty: 250
```

The $250 illustration assumes filing was due in 2026, ten penalized days, no reasonable-cause relief and no disaster/special extension; it is not a tax computed by 990.

**B. Fiscal 2025–2026 ordinary charity:** year July 1, 2025–June 30, 2026; Part VII pay is calendar 2025, while current officers include anyone serving during that fiscal year. Assume VIII 12(A) revenue $250,000, IX 25(A) expenses $200,000; opening net assets $400,000; XI 5–9 adjustments $0; closing assets $600,000 and liabilities $150,000. XI 3 = $50,000; XI 10 = $450,000 = X 32(B); X 33 = $600,000 = X 16(B). A listed non-officer employee with $100,000 organization reportable pay and $60,000 from one related organization passes the $150,000 key-employee pay test; list as key **only if** responsibility and top-20 tests also pass. [IRS Parts VII, X–XI](https://www.irs.gov/instructions/i990).

```oa-check
name: 2025-2026 fiscal return reconciliation and related pay
inputs:
  revenue: 250000
  expenses: 200000
  opening_net_assets: 400000
  adjustments: 0
  closing_assets: 600000
  closing_liabilities: 150000
  filer_pay: 100000
  related_pay: 60000
steps:
  surplus: revenue - expenses
  xi10: opening_net_assets + surplus + adjustments
  x32: closing_assets - closing_liabilities
  x33: closing_liabilities + x32
  key_pay: filer_pay + related_pay
expected:
  surplus: 50000
  xi10: 450000
  x32: 450000
  x33: 600000
  key_pay: 160000
```

## When to refuse or refer

The following are **non-usable holds**: collect the original facts, but do not determine these outcomes from this Guide.

- Group returns filed by a central organization: Check this point with one of our partner accountants.
- Lost exemption, three-year nonfiling or reinstatement: Check this point with one of our partner accountants.
- Foreign/U.S.-territory organizations' separate eligibility tests: Check this point with one of our partner accountants. If preparing their otherwise-required full return, use English, combine worldwide amounts in U.S. dollars and state the conversion rate. [IRS §A](https://www.irs.gov/instructions/i990).
- Accounting-year changes, short-year compensation exceptions, Form 3115 consent and the amount/timing of any §481 adjustment: Check this point with one of our partner accountants. Do not silently apply a full-year rule.
- Unusual grants, 10%-facts-and-circumstances public support, supporting-organization status tests, or possible conversion to a private foundation: Check this point with one of our partner accountants. Do not treat 10% support alone as qualification.
- Schedule B exact-2% reporting boundary or 501(c)(7)/(8)/(10) exclusively religious/charitable-purpose gifts: Check this point with one of our partner accountants.
- Interested-person excess-benefit/loan/grant/business-transaction classification or an unresolved Schedule L threshold/exception, and unusual Schedule R passive-partnership exceptions: Check this point with one of our partner accountants. Preserve the transaction details; do not answer No merely because this Guide cannot classify it.

## Filing and payment

The ordinary deadline is the **15th day of the fifth month** after period-end, shifted to the next business day for Saturday/Sunday/legal holiday. Termination uses the fifth month after liquidation/dissolution/termination. File Form 8868 properly by the original due date for an automatic **six-month** filing extension; it does not extend tax payment, other returns or 990-N. [Reg. §1.6033-2(e)](https://www.ecfr.gov/current/title-26/section-1.6033-2); [IRS §§E–F](https://www.irs.gov/instructions/i990); [8868](https://www.irs.gov/instructions/i8868).

As the preparation workflow, use an IRS-authorized e-file provider/software for 2025 Form 990, complete the applicable officer-signature authorization (8879-TE for PIN signing, or 8453-TE) and retain the IRS acceptance acknowledgment; resolve a rejection rather than treating transmission alone as completion. E-filing is required for 2025; availability is current year plus two prior tax periods. An older unavailable return/amendment is paper-filed with “The IRS no longer accepts e-file of the 20XX return year” on page 1. Otherwise-required e-filers filing paper are treated as not filed. [2025 signature authorization/instructions](https://www.irs.gov/pub/irs-pdf/f8879te.pdf); [IRS §§E, H](https://www.irs.gov/instructions/i990).

To amend, use the correct year's complete form and all required schedules; check B “Amended return” and explain changed parts/schedules on O. A final return checks B “Final return/terminated” and includes N and required dissolution/liquidation documents. Check state filings independently: an accrual-basis state 990 may also be filed identically with IRS if it conflicts with no IRS instruction; keep the book reconciliation. State amendment obligations can remain even if IRS accepted the original. [IRS §§D, G, Appendix I](https://www.irs.gov/instructions/i990).

For Form 990 completion help, the IRS number is 877-829-5500. [2025 instructions, Phone Help](https://www.irs.gov/instructions/i990).

### Failure-to-file consequences

These indexed amounts apply to returns **required to be filed in 2026**, including ordinary calendar-2025 returns. Other required-filing years need that year's indexed amounts. [IRC §6652(c)(1), (5), (7)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6652.htm); [Rev. Proc. 2024-40 §2.54](https://www.irs.gov/irb/2024-45_IRB).

| Failure | Daily amount and cap, subject to reasonable cause | Official source |
|---|---|---|
| Organization, ordinary | $25/day; lesser of $13,000 or 5% of year gross receipts. Applies to late, incomplete or incorrect required returns. | [2025 instructions §H](https://www.irs.gov/instructions/i990); [2026-due indexing §2.54](https://www.irs.gov/irb/2024-45_IRB) |
| Organization, larger | If gross receipts **exceed** $1,309,500: $130/day, maximum $65,000 per return. | [2026-due indexing §2.54](https://www.irs.gov/irb/2024-45_IRB) |
| Responsible persons | Only after failure to comply by the IRS's written-demand deadline: $10/day, combined maximum $6,500 for all liable persons for one return. | [IRC §6652(c)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6652.htm); [indexing §2.54](https://www.irs.gov/irb/2024-45_IRB) |

IRC §6033(j) automatically revokes applicable section 501(a) exemption after **three consecutive years** of failing to file the required return/notice, effective on/after the prescribed third due date. An extension is not a cure for earlier nonfiling; hold reinstatement advice as above. [IRC §6033(j)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6033.htm).

## Completion checklist

- Reconcile VIII/IX/X/XI, I summary and VII/J; verify different accounting periods rather than forcing compensation totals to agree. Confirm every IV Yes has its required schedule/part and every required narrative is supplied.
- Have the authorized human review/sign the final return. Check applicable zeros, conditional blanks, gross contributions and every attachment. Retain submission/acceptance and the exact filed copy.
- Build the public copy with schedules/attachments. For non-foundation filers other than 527, withhold contributor names/addresses and information clearly identifying them; do not suppress all of B. A section 527 filer's B is public. Make returns available for inspection for three years after due date including extensions or actual filing, whichever is later; amendments have their own three-year availability. Copies on request remain required unless the regulatory widely-available exception applies; internet posting does not eliminate in-person inspection. [IRC §6104(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapB-sec6104.htm); [Reg. §301.6104(d)-1](https://www.ecfr.gov/current/title-26/section-301.6104(d)-1); [B instructions](https://www.irs.gov/instructions/i990sb).
- Keep records as long as needed for administration: supporting income/deduction/credit records usually at least three years after due/filed, whichever is later; basis records and applicable law/policy can require longer. Keep prior returns and the book-to-return reconciliation. [IRS §J](https://www.irs.gov/instructions/i990).

> Contributed by Anthony Bandura, AL-10921.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| IRS 2025 Form 990 and instructions: general A–J; heading; core I–XII; Part IV checklist; appendices B, D, F and I relevant passages | https://www.irs.gov/instructions/i990 and https://www.irs.gov/pub/irs-prior/f990--2025.pdf | 2026-11-27 |
| IRS 2025 Schedule A: public-charity category, II/III support, first-five-year and current/prior-year tests | https://www.irs.gov/instructions/i990sa | 2026-11-27 |
| IRS Schedule B rev. December 2024, continuous use for 2024 onward: reporting, aggregation, exceptions, inspection | https://www.irs.gov/instructions/i990sb | 2026-11-27 |
| IRC §§6033(a)–(d), (g), (i)–(j), (n); 509(a)(2), (d)–(e); 6104(d); 6652(c)(1), (5)–(7), official 2024 codification and operative IRS 2025 instructions/indexing | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6033.htm ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partII-sec509.htm ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapB-sec6104.htm ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6652.htm | 2026-11-27 |
| Regulations §§1.6033-2(a)(2), (e), (g); 1.170A-9(f)(2)–(4); 301.6104(d)-1(a), (b)(4); web-readable operative text; direct fetch returned access shell | https://www.ecfr.gov/current/title-26/section-1.6033-2 ; https://www.ecfr.gov/current/title-26/section-1.170A-9 ; https://www.ecfr.gov/current/title-26/section-301.6104(d)-1 | 2026-11-27 |
| Rev. Proc. 2024-40 §2.54, 2026-required filing penalty amounts | https://www.irs.gov/irb/2024-45_IRB | 2026-11-27 |
| IRC §481(a): adjustment prevents duplication/omission on a tax-accounting-method change, no amount/timing advice supplied | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partIII-sec481.htm | 2026-11-27 |
| Reg. §1.6012-2(e): corporate exempt-organization gross-unrelated-income filing trigger, confirmed alongside 2025 instructions | https://www.ecfr.gov/current/title-26/section-1.6012-2 | 2026-11-27 |
| 2025 Form 8879-TE and instructions: PIN authorization, 8453-TE alternative, acknowledgement/rejection and retention | https://www.irs.gov/pub/irs-pdf/f8879te.pdf | 2026-11-27 |
| Form 8868 instructions rev. January 2026: ordinary extension for 2025 returns filed in 2026 | https://www.irs.gov/instructions/i8868 | 2026-11-27 |

Not yet confirmed: no usable claim is left unconfirmed. The specifically identified specialist outcomes under “When to refuse or refer” are non-usable holds, not filing conclusions.
