---
name: us-foreign-trust-reporting
description: US foreign trust and large foreign gift reporting for 2026, with dated 2025 thresholds. Apply court and control tests, identify owners and reporting exceptions, distinguish current income from accumulation distributions, and prepare Forms 3520 and 3520-A working papers. Covers foreign gifts, inheritance, section 679, loans and property use, throwback calculations, deadlines and penalties. Unresolved classifications and specialist exceptions require a partner accountant. Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - cross-border-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# US reporting of foreign trusts and large foreign gifts, tax year 2026

> **Source-cited draft.** A working paper and reviewer brief, not a filed return. Apply the rules to the trust instrument and full funding history before selecting forms. Qualified professional review is required before filing; no professional approval is claimed. Sources read on 2026-11-27.

**Answer first.** Establish whether the arrangement is a foreign trust, who owns each portion and whether a reporting exception applies. Form 3520 then addresses reportable transfers, ownership, distributions and large foreign gifts; a foreign trust with a US owner also has the Form 3520-A pathway. Do not decide status from a foreign label or an incomplete deed ([Form 3520 instructions, Who Must File](https://www.irs.gov/instructions/i3520); [Form 3520-A instructions](https://www.irs.gov/instructions/i3520a)).

## Scope and who this is for

US federal reporting for 2026, with a separate historical 2025 filing note. Use with `cross-border-tax-workflow-base` after the cross-border router. Produce the facts, source references, computations, form checklist, deadline calendar and reviewer questions. Do not make elections or file returns from this working paper.

Related jobs: `us-tax-residency` for US status; `us-fbar-and-fatca-8938` for FBAR and Form 8938; `us-form-5471-cfc-information` for foreign corporations; `us-form-1041-trust-and-estate-income` for domestic trusts; `us-estate-gift-706-709` for estate/gift planning; `us-expatriation-exit-tax` for covered expatriates and status changes. These links are routing, not clearance from another obligation.

## Ask the client first

Read the existing record before asking for missing facts. Obtain:

1. Deed, amendments, governing law, court supervision, trustees and every person controlling a substantial decision: distributions, beneficiaries, investments, trustee replacement, termination and litigation.
2. Every settlor/transferor, transfer date, property, value and consideration; US status and residency dates; deaths and trust migrations; all possible beneficiaries, powers and agreements.
3. Revocation and retained powers; whether lifetime payments can reach anyone other than the settlor or spouse; any transfers from a US beneficiary to a foreign settlor.
4. Current distributions, loans, credit-card payments, guarantees and use of homes/cars; amounts paid for use; loan terms, interest, repayment and qualified-obligation history.
5. Owner/Beneficiary Statements, US agent appointment, yearly income/tax/DNI/UNI accounts, years foreign, prior three years' distributions and all previous Schedule A elections.
6. Pension/savings-plan rules, contributions, reporting and withdrawal conditions; Canadian RRSP/RRIF documents; gifts and bequests by donor and related persons/nominees; earlier filings and IRS notices.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount and conditions | Source |
| --- | --- | --- |
| Part IV, nonresident alien/foreign estate gifts or bequests | For US recipients other than section 501(c) organizations exempt under section 501(a): more than USD 100,000 per year; aggregate donors known or reasonably known to be related, including nominees/intermediaries. Once exceeded, identify each gift over USD 5,000. | [Form 3520 instructions, line 54](https://www.irs.gov/instructions/i3520) |
| Part IV, purported gifts from foreign corporations/partnerships | Aggregate all such entities and foreign persons known or reasonably known to be related to them; more than USD 20,573 for taxable years beginning in 2026. Identify each gift and donor. | [IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person); [Rev. Proc. 2025-32 §4.47](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Historical 2025 corporate/partnership gift threshold | More than USD 20,116 for taxable years beginning in 2025; same aggregation rule. | [Rev. Proc. 2024-40 §2.48](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf); [IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person) |
| Initial transfer/distribution reporting penalty | Generally greater of USD 10,000 or 35% of gross property transferred/distribution received for a late, incomplete or incorrect required return; reasonable cause exception below. | [§6677(a),(c)](https://uscode.house.gov/us/usc/t26/s6677/) |
| Initial ownership reporting penalty | Generally greater of USD 10,000 or 5% of the year-end gross value of the owned portion; US owner liable. This is not a monthly 5% charge. | [§6677(b),(c)](https://uscode.house.gov/us/usc/t26/s6677/) |
| Continuing trust reporting failure | USD 10,000 for each 30-day period or fraction after more than 90 days from the IRS notice; when the gross reportable amount is determinable, aggregate penalties are reduced/refunded to that amount. | [§6677(a)](https://uscode.house.gov/us/usc/t26/s6677/) |
| Foreign gift reporting failure | 5% of the gift for each month of failure, capped at 25%; reasonable cause exception below. IRS may determine the receipt's tax consequences. | [§6039F(c)](https://uscode.house.gov/us/usc/t26/s6039F/) |
| Throwback interest, historical periods after 1976 and before 1996 | 6% simple; after 1995 the underpayment rate compounds daily on tax and pre-1996 simple interest. | [Form 3520 instructions, line 51](https://www.irs.gov/instructions/i3520) |

### Classification and ownership

1. **Domestic or foreign.** A domestic trust must satisfy both: a US court can exercise primary supervision over administration, and one or more US persons control all substantial decisions. A trust outside that definition is foreign ([§7701(a)(30)(E),(31)(B)](https://uscode.house.gov/us/usc/t26/s7701/)). If facts are incomplete, record classification as unresolved and hold any dependent tax/form conclusion. Check this point with one of our partner accountants.
2. **Ordinary ownership powers.** Screen sections 673–678 separately for each person and portion, including retained reversions, beneficial-enjoyment, administrative, revocation and income powers and a person's power to vest assets in themselves. This is an intake checklist, not a complete ownership test. Check this point with one of our partner accountants.
3. **Foreign settlor limit.** Section 672(f)(1) generally limits grantor treatment to amounts currently taken into account by a US citizen/resident or domestic corporation. Exceptions include an absolute revesting power exercisable by the grantor alone or with a subservient related/subordinate party, lifetime distributions solely to the grantor/spouse, and compensatory trusts (subject to regulations). Passing an exception removes the limit; it does not by itself prove ownership or foreign status ([§672(f)(1)–(3)](https://uscode.house.gov/us/usc/t26/s672/)). Beneficiary-to-settlor transfers and section 672(f)(5) require separate review: Check this point with one of our partner accountants.
4. **Section 679 US transferor.** Outside the excluded section 6048(a)(3)(B)(ii) trusts, a US direct/indirect transferor owns the attributable portion if the trust has a US beneficiary that year. Apply the death and at-least-FMV exceptions in section 679(a)(2). For consideration consisting of trust/related obligations and guarantees, do not assume that face value counts: Check this point with one of our partner accountants. Lack of retained control or of a current distribution does not dispense with the statutory transfer/beneficiary test ([§679(a)(1)–(3)](https://uscode.house.gov/us/usc/t26/s679/)).
5. **US beneficiary test.** The trust has a US beneficiary unless no income/corpus may be paid or accumulated for a US person during the year and none could reach one on termination. Contingent interests count. A person’s discretion to select beneficiaries gives a US beneficiary unless the trust specifically identifies the permitted class and none is a US person that year. A US transferor’s involvement in an agreement/understanding that may benefit a US person makes that agreement a trust term under section 679(c)(5). A beneficiary first becoming a US person more than five years after the particular transfer is disregarded for that transfer ([§679(c)(1),(3)–(5)](https://uscode.house.gov/us/usc/t26/s679/)).
6. **Timing changes.** An NRA individual's residency starting within five years of a transfer invokes a deemed transfer of the attributable portion on the residency starting date. A domestic trust becoming foreign while its US citizen/resident transferor is alive similarly invokes a deemed transfer of the attributable portion on migration. Section 679(a)(4)(B) addresses prior UNI in the attributable portion. Stop for specialist review of an actual migration or immigration plan ([§679(a)(4),(5)](https://uscode.house.gov/us/usc/t26/s679/)). Check this point with one of our partner accountants.
7. **Loans/use and the beneficiary test.** Section 679(c)(6) treats a loan of cash/marketable securities or property use by any US person as a US benefit, except to the extent the person repays at a market interest rate or pays FMV for use within a reasonable period. Ownership still requires the section 679 transferor gateway ([§679(c)(6)](https://uscode.house.gov/us/usc/t26/s679/)).

### Owner and beneficiary pathways

- **Transfers/reportable events:** complete Form 3520 Part I if responsible for a reportable event, if a US transferor exchanges property with a related foreign trust/person for an obligation, or if holding its currently outstanding qualified obligation. Establish the responsible party and test exceptions first. No US owner and no current distribution do not by themselves clear this pathway ([instructions, Who Must File item 1 and Part I](https://www.irs.gov/instructions/i3520)).
- **US owner:** include income, deductions and credits attributable to the owned portion currently under [§671](https://uscode.house.gov/us/usc/t26/s671/), even without a distribution. Complete Form 3520 Part II annually even with no transactions. For a receipt from the portion the US recipient owns, complete Part III lines 24 and 27; do not use that instruction for an unowned portion ([instructions, Who Must File and Reporting by US owners](https://www.irs.gov/instructions/i3520)). Ensure Form 3520-A and Owner/Beneficiary Statements are completed; use a complete timely substitute if the trust does not file ([Form 3520-A instructions](https://www.irs.gov/instructions/i3520a)).
- **Foreign nongrantor distribution:** distinguish current ordinary income/capital gains, accumulation income and corpus using records and a complete Foreign Nongrantor Trust Beneficiary Statement. Foreign-trust DNI includes net capital gains under [§643(a)(6)](https://uscode.house.gov/us/usc/t26/s643/). UNI is DNI less distributions described in section 661(a)(1),(2) and attributable trust taxes, not merely all undistributed cash ([§665(a)](https://uscode.house.gov/us/usc/t26/s665/)). Do not label every payment above current DNI taxable accumulation: Form 3520 separately identifies corpus at Schedule B line 43 ([Form 3520](https://www.irs.gov/pub/irs-pdf/f3520.pdf)). Unsettled corpus/UNI allocation: Check this point with one of our partner accountants.
- **Actual/default method:** Schedule B requires a complete statement attached and no previous Schedule A use, except in the trust's termination year. Otherwise use Schedule A. A complete statement also permits choosing Schedule A, but that generally binds future years; termination with a complete statement is the exception ([instructions, line 30 and Schedules A/B](https://www.irs.gov/instructions/i3520)). Under [§6048(c)(2)](https://uscode.house.gov/us/usc/t26/s6048/), inadequate records can cause accumulation treatment; the Form's default mechanism must still be applied correctly.
- **Schedule A:** line 33 is the preceding three years' distributions (fewer preceding foreign years if applicable), excluding the current year. Line 34 multiplies by 1.25; line 35 divides by the number of preceding foreign years, up to three, including zero-distribution years. Count partial years as full years; if this is the first foreign year, stop the remainder of Part III. Line 36 is the smaller of current distribution and line 35, reportable as ordinary income; line 37 is the remainder; if positive, line 38 is years foreign including current year divided by 2.0 ([Form 3520 lines 31–38](https://www.irs.gov/pub/irs-pdf/f3520.pdf); [instructions lines 32–37](https://www.irs.gov/instructions/i3520)).
- **Throwback:** use Form 4970 as a worksheet attached to Form 3520 and Schedule C for the tax and interest. Schedule C line 50 rounds the applicable years to the nearest half-year. Line 53 is additional tax on the income tax return (Form 1040 Schedule 2, Part II, “Any other taxes”). The section 668 interest charge is nondeductible; tax plus interest cannot exceed the accumulation distribution excluding tax deemed distributed under section 666(b),(c) ([§668(b),(c)](https://uscode.house.gov/us/usc/t26/s668/); [Form 3520 and instructions lines 49–53](https://www.irs.gov/instructions/i3520)). For an actual interest computation, applicable dates, eligible accumulation years and rates must be established; Check this point with one of our partner accountants.
- **Foreign-owned grantor distribution:** with a complete Foreign Grantor Trust Beneficiary Statement, attach it, answer line 29 and treat the receipt as directly from the owner; if a genuine gift, it is not gross income. Still report the foreign-trust receipt in Part III, not Part IV ([instructions, line 29 and Part IV](https://www.irs.gov/instructions/i3520)). A missing statement does not justify assuming a tax-free gift.
- **Loans/free use:** screen Part III line 25 reporting separately from taxable treatment. FMV of use is reportable even if paid; the payment affects the taxable amount. A qualified obligation and one that loses qualification have different consequences. Do not infer that paying market interest alone disposes of section 643(i). For qualified-obligation terms, guarantees, subsequent repayments and the interaction with US ownership: Check this point with one of our partner accountants ([instructions, lines 25–28](https://www.irs.gov/instructions/i3520)).
- **Gifts:** run Part IV separately using the table's aggregation rules. A foreign trust's “gift” belongs in Part III. A purported corporate/partnership gift may be recharacterized under [§672(f)(4)](https://uscode.house.gov/us/usc/t26/s672/); do not assume exclusion just because it is called a gift. Qualified tuition paid directly to the qualifying educational organization and qualifying medical care paid to the provider are excluded from foreign gifts under [§6039F(b)](https://uscode.house.gov/us/usc/t26/s6039F/) and [§2503(e)(2)](https://uscode.house.gov/us/usc/t26/s2503/); a reimbursement or general education/living allowance is not established as a qualified direct payment by that rule.

### Penalties and assessment

No section 6677 or 6039F penalty applies where reasonable cause and absence of willful neglect are shown; foreign disclosure penalties and trustee reluctance are not reasonable cause ([§6677(d)](https://uscode.house.gov/us/usc/t26/s6677/); [§6039F(c)(2)](https://uscode.house.gov/us/usc/t26/s6039F/); [instructions, Reasonable cause](https://www.irs.gov/instructions/i3520)). Section 6677 penalties do not use deficiency procedures ([§6677(e)](https://uscode.house.gov/us/usc/t26/s6677/)). Do not promise first-time relief or an automatic waiver. Check this point with one of our partner accountants.

Missing section 6048 information can keep assessment open until at least three years after furnishing it; this is not an automatic closing date. Reasonable cause without willful neglect limits that extension to related items ([§6501(c)(8)](https://uscode.house.gov/us/usc/t26/s6501/)). The separate section 6662(j) accuracy-related penalty and its defenses need individual review: Check this point with one of our partner accountants.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Exactly USD 100,000 from nonresident aliens/foreign estates, with no other aggregated gifts | Does not exceed the Part IV threshold. This says nothing about trust receipts or covered expatriates ([instructions, line 54](https://www.irs.gov/instructions/i3520)). |
| Known related nonresident donors give USD 75,000 and USD 40,000 | Aggregate USD 115,000 (computed); report each gift over USD 5,000 ([instructions, line 54](https://www.irs.gov/instructions/i3520)). |
| Canadian RRSP/RRIF or other plan potentially within Rev. Proc. 2014-55 | Hold the exemption conclusion pending plan-specific eligibility review. Check this point with one of our partner accountants. |
| Foreign retirement or medical/disability/education savings trust; Rev. Proc. 2020-17 | Contribution limits alone do not establish eligibility. Hold the exemption and Form 843 relief conclusions. Check this point with one of our partner accountants. |
| Proposed section 1.6048-5 reliance, originally discussed for years ending after 8 May 2024 | Hold reliance, current regulation status and full/consistent application conditions pending specialist review. Check this point with one of our partner accountants. |
| Section 402(b), 404(a)(4), 404A arrangement | The instructions except the specified transfers/amounts from reporting; this is not a blanket exemption for every ownership or receipt involving a workplace plan ([instructions, Exceptions To Filing](https://www.irs.gov/instructions/i3520)). |
| FMV transfer | Most are excepted, but qualified-obligation, unrecognized appreciated-property gain and related-transferor cases may still require reporting ([instructions, Exceptions To Filing](https://www.irs.gov/instructions/i3520)). |
| Trust distribution taxable as compensation | Reporting exception only if it is taxable compensation within section 672(f)(2)(B) and regulations and is reported as compensation on the applicable income tax return ([instructions, Exceptions To Filing](https://www.irs.gov/instructions/i3520)). |

Do not default a pension to required reporting or exemption from incomplete facts. Hold the decision, collect documents and preserve the filing deadline. Review FBAR, Form 8938 and income tax independently; this Guide grants no clearance on those jobs.

## Worked cases

Illustrations with the original amounts and years. Penalties below assume a required filing, no applicable reporting exemption, no reasonable cause and no other fact changing the stated exposure.

**Case 1, decision: gifts and a late filing (2026).** A US citizen receives USD 60,000 from her nonresident mother and USD 45,000 from her nonresident father. Aggregate related donors: USD 105,000 exceeds USD 100,000 by USD 5,000, so file Part IV, listing both gifts. At exactly USD 100,000 the threshold is not exceeded. Assume genuine personal gifts rather than compensation, trust income or income from gifted property; their principal is excluded under [§102(a)–(c)](https://uscode.house.gov/us/usc/t26/s102/). Review any covered-expatriate issue separately. Seven months late gives min(7 × 5%, 25%) × USD 105,000 = USD 26,250 under [§6039F(c)](https://uscode.house.gov/us/usc/t26/s6039F/). For a calendar-year filer, file by 15 April 2027, or 15 October 2027 with a granted income-tax filing extension ([instructions](https://www.irs.gov/instructions/i3520)).

```oa-check
name: Foreign gifts from related donors, Part IV test and late penalty (2026)
inputs:
  gift_mother: 60000
  gift_father: 45000
  threshold: 100000
  months_late: 7
steps:
  - aggregate: gift_mother + gift_father
  - over_threshold: max(aggregate - threshold, 0)
  - penalty_rate: min(0.05 * months_late, 0.25)
  - late_penalty: penalty_rate * aggregate
expected:
  aggregate: 105000.00
  over_threshold: 5000.00
  penalty_rate: 0.25
  late_penalty: 26250.00
```

**Case 2, Schedule A default (2026).** Foreign for ten years including 2026; no Foreign Nongrantor Trust Beneficiary Statement; USD 12,000 distributed in the preceding three years and USD 40,000 in 2026. Under [Form 3520 lines 33–38](https://www.irs.gov/pub/irs-pdf/f3520.pdf), line 34 = USD 15,000; line 35 = USD 5,000; line 36 = USD 5,000 ordinary income; line 37 = USD 35,000 accumulation distribution; line 38 = five applicable years. This is the default calculation, not proof of actual UNI. Form 4970 and interest still require completion; the [section 668(b) cap](https://uscode.house.gov/us/usc/t26/s668/) is USD 35,000 here, excluding any deemed-distributed tax. If this USD 40,000 distribution went unreported, initial exposure under [§6677](https://uscode.house.gov/us/usc/t26/s6677/) is max(USD 10,000, 35% × USD 40,000) = USD 14,000.

```oa-check
name: Schedule A default distribution and section 6677 exposure (2026)
inputs:
  prior_three_years: 12000
  current_distribution: 40000
  years_foreign: 10
steps:
  - line_34: prior_three_years * 1.25
  - line_35: line_34 / 3
  - line_36: min(current_distribution, line_35)
  - line_37: current_distribution - line_36
  - line_38: years_foreign / 2
  - penalty_if_unreported: max(10000, 0.35 * current_distribution)
expected:
  line_34: 15000.00
  line_35: 5000.00
  line_36: 5000.00
  line_37: 35000.00
  line_38: 5.00
  penalty_if_unreported: 14000.00
```

**Case 3, purported company gift (2026).** A foreign corporation owned by the client's nonresident uncle sends USD 21,000 called a gift. It exceeds USD 20,573 by USD 427, so the purported-gift reporting test applies; report in Part IV line 55. Recharacterization remains open; no gift exclusion is concluded ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person)).

**Case 4, unreported trust distribution.** USD 200,000 received by a US beneficiary of a foreign nongrantor trust with no Form 3520: max(USD 10,000, 35% × USD 200,000) = USD 70,000 initial exposure. The continuing-notice penalty and statutory aggregate reduction above also apply where their conditions are met ([§6677](https://uscode.house.gov/us/usc/t26/s6677/)). The original case did not specify a year; none is invented here.

**Case 5, US owner and missing Form 3520-A.** A US citizen is the section 679 owner; the owned trust assets are USD 150,000 at year end. A complete substitute filed with timely Form 3520, and the required statements furnished, avoids the penalty for the trust's failure to file Form 3520-A; it does not waive other failures. If neither is filed, max(USD 10,000, 5% × USD 150,000) = USD 10,000, since 5% is USD 7,500 ([Form 3520-A instructions, Penalties](https://www.irs.gov/instructions/i3520a)). The original case has no specified year.

**Case 6, foreign settlor and US grandchild.** A nonresident grandmother creates an irrevocable discretionary trust abroad for grandchildren including a US citizen; she cannot revoke it and payments can reach grandchildren during her life. Those facts do not establish US foreign-trust status, every potential owner, or all exceptions to section 672(f). Hold the nongrantor classification and “no Form 3520-A” conclusion. In the alternative where she alone can revoke, that power is an exception to the foreign-owner limit, not the entire classification test. Only after ownership is established use the complete-statement pathway above. Check this point with one of our partner accountants.

**Case 7, workplace pension abroad.** A US citizen working abroad has a locally tax-favored, locally reported employer pension, earned-income-only contributions capped by a percentage of pay and withdrawals locked until retirement. Preserve those facts; they are not enough here to certify every Rev. Proc. 2020-17 eligibility condition. Hold the Form 3520/3520-A exemption; review income tax, FBAR and Form 8938 separately. Check this point with one of our partner accountants.

**Historical case, restored: exactly at the threshold (2026).** A US resident receives one USD 100,000 bequest from a foreign estate and nothing else from foreign persons. It does not exceed USD 100,000, so Part IV is not required on those facts; aggregate any related-donor amount first. This is the predecessor's Case 2, distinct from the current trust-distribution Case 2 ([instructions, line 54](https://www.irs.gov/instructions/i3520)).

## When to refuse or refer

Each following point is a non-usable hold: **Check this point with one of our partner accountants.**

| Code | Point requiring review |
| --- | --- |
| R-FT-LOCAL | Foreign-country characterization, including Australian discretionary/unit trusts and foreign relief; no foreign label establishes the US result. |
| R-FT-LATE | Prior Forms 3520/3520-A, IRS notices, compliance route, reasonable cause or penalty-relief request. No promised waiver. |
| R-FT-RECORDS | Long accumulation history, corpus/UNI allocation, missing records, actual throwback and interest. No “highest-rate” or “always higher” shortcut. |
| R-FT-684 | Appreciated-property transfer, trust migration, pre-immigration planning, selling in trust versus distributing before sale, and basis/character consequences. |
| R-FT-2801 | Donor who relinquished citizenship/long-term residence; covered-expatriate gifts/bequests, section 2801 and Form 708. |
| R-FT-EXPAT | Owner/beneficiary status change, section 877A, trust-asset sales and sequencing with `us-expatriation-exit-tax`. |
| R-FT-PROMOTER | Promoter assurances that an arrangement is outside these rules. Obtain documents and do not accept the assurance as proof. |

**AUDIT FLASH POINT:** Resolve funding, ownership, records and reporting before using a tax conclusion. Retain the reviewer handoff for the sale and residency overlays.

## Filing and payment

1. **Form 3520:** normally the 15th day of the fourth month after the filer's tax year; calendar-year 2026: **15 April 2027**. Qualifying US citizen/resident individuals who, on the income-tax due date, both live and have a business/post of duty outside the US and Puerto Rico, or are in military/naval service on duty outside them, have until **15 June 2027**. Check line 1j and attach the required statement ([instructions, When and Where To File; line 1j](https://www.irs.gov/instructions/i3520)).
2. A granted income-tax filing extension extends Form 3520 to no later than the fifteenth day of the tenth month: **15 October 2027** for calendar 2026. Check line 1k and give the income-tax form number. The discretionary December extension does not extend Form 3520 ([instructions](https://www.irs.gov/instructions/i3520); [IRS foreign trust filing tips](https://www.irs.gov/businesses/international-businesses/foreign-trust-reporting-requirements-and-tax-consequences)). Apply next-business-day treatment for weekends/legal holidays and check applicable disaster relief before fixing a particular filer's deadline.
3. File Form 3520 separately from the income-tax return at Internal Revenue Service Center, P.O. Box 409101, Ogden, UT 84409. Use one per trust; spouses filing a joint income-tax return who are both transferors/grantors/beneficiaries of the same trust may file jointly and check line 1i. The individual/fiduciary signs; include all required attachments ([instructions, Joint Returns; When and Where To File; Who Must Sign](https://www.irs.gov/instructions/i3520)). Retain a complete copy and mailing proof.
4. **Form 3520-A:** foreign trust with a US owner, due by the fifteenth day of the third month after trust year end: **15 March 2027** for calendar 2026. Furnish required Owner/Beneficiary Statements by its due date. For an extension, file Form 7004 by the original third-month deadline using the trust's EIN; the owner's income-tax extension does not extend it. Trustee signs. A US-owner-signed complete substitute attaches to Form 3520 by that form's due date, with statements furnished by then ([Form 3520-A instructions](https://www.irs.gov/instructions/i3520a)).
5. Document the US agent at Form 3520 lines 3a–3g. Without the required agent arrangement the IRS can determine the owner's includible amounts ([§6048(b)(2)](https://uscode.house.gov/us/usc/t26/s6048/)). If the income-tax return treats an item inconsistently with the trust's Form 3520-A, file Form 8082 ([instructions, Inconsistent Treatment](https://www.irs.gov/instructions/i3520)). Incorporate income and additional tax in the applicable income-tax return; this Guide supplies no separate payment extension.
6. Screen FBAR/Form 8938 separately. Check Form 3520 item C only if also filing Form 8938 for the same year and including this Form 3520 in the count on Form 8938 Part IV line 15 ([instructions, Item C](https://www.irs.gov/instructions/i3520)); this is not an exemption from testing those forms.

### Historical calendar-year 2025 filings

The December 2025 continuous-use instructions apply to 2025 and subsequent years until superseded. For 2025 use the table's USD 20,116 corporate/partnership threshold and the unchanged more-than-USD-100,000 individual/estate test. Ordinary Form 3520 deadlines were **15 April 2026**, **15 June 2026** for qualifying individuals abroad, and **15 October 2026** with a granted income-tax filing extension. A missing Form 3520-A's substitute was due with that year's Form 3520, not on a new late-filing date ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person); [Form 3520 instructions](https://www.irs.gov/instructions/i3520)). These dates are historical and confer no current extension.

## Completion checklist

- [ ] Classification/ownership for each portion documented or explicitly held; reporting exemptions decided only after their complete conditions are established.
- [ ] Transfer, ownership, distribution/loan/use and gift pathways screened; prior years, statements, records and US agent captured.
- [ ] Default/actual choice documented; case arithmetic recomputed; actual tax/interest not invented from incomplete inputs.
- [ ] Applicable deadlines, filing copies, mailing proof, other forms and all non-usable holds included in the reviewer brief.

## Sources

| Source and portions read | Official URL | Read on |
| --- | --- | --- |
| Form 3520 instructions (12/2025): continuous-use scope, Who Must File, exceptions, statements, Schedules A–C, Part IV, penalties and filing | https://www.irs.gov/instructions/i3520 | 2026-11-27 |
| Form 3520-A instructions (12/2025): US-owner duty, substitute, statements, deadlines, Form 7004, signatures and penalties | https://www.irs.gov/instructions/i3520a | 2026-11-27 |
| Form 3520 (12/2023 continuous-use form): Part III lines 24–53, corpus line 43 and half-year rounding | https://www.irs.gov/pub/irs-pdf/f3520.pdf | 2026-11-27 |
| Rev. Proc. 2025-32 §4.47: 2026 gift threshold only | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| Rev. Proc. 2024-40 §2.48: historical 2025 gift threshold only | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-27 |
| IRS Gifts from foreign person: thresholds, aggregation, listing and separate filing | https://www.irs.gov/businesses/gifts-from-foreign-person | 2026-11-27 |
| 26 USC 7701: (a)(30)(E),(31)(B), court/control and foreign definition | https://uscode.house.gov/us/usc/t26/s7701/ | 2026-11-27 |
| 26 USC 671: owned portion income, deductions and credits | https://uscode.house.gov/us/usc/t26/s671/ | 2026-11-27 |
| 26 USC 672: (f), foreign-owner limitation and exceptions; purported gifts | https://uscode.house.gov/us/usc/t26/s672/ | 2026-11-27 |
| 26 USC 679: (a),(c), transfer, exceptions, residency/migration and beneficiary tests | https://uscode.house.gov/us/usc/t26/s679/ | 2026-11-27 |
| 26 USC 643: (a)(6), foreign-trust DNI; (i) reviewed for loan/use hold | https://uscode.house.gov/us/usc/t26/s643/ | 2026-11-27 |
| 26 USC 665: (a),(b), UNI and accumulation definitions | https://uscode.house.gov/us/usc/t26/s665/ | 2026-11-27 |
| 26 USC 668: interest, applicable years, pre-1996 rule, cap and nondeductibility | https://uscode.house.gov/us/usc/t26/s668/ | 2026-11-27 |
| 26 USC 6048: (a)–(d), reporting, US agent and inadequate records | https://uscode.house.gov/us/usc/t26/s6048/ | 2026-11-27 |
| 26 USC 6677: (a)–(e), penalties, gross bases, reduction, cause and procedures | https://uscode.house.gov/us/usc/t26/s6677/ | 2026-11-27 |
| 26 USC 6039F: foreign gifts, qualified-transfer exclusion and penalties | https://uscode.house.gov/us/usc/t26/s6039F/ | 2026-11-27 |
| 26 USC 102: (a)–(c), genuine gift principal and income/employee exceptions | https://uscode.house.gov/us/usc/t26/s102/ | 2026-11-27 |
| 26 USC 2503: (e)(2), direct qualifying tuition/medical payments | https://uscode.house.gov/us/usc/t26/s2503/ | 2026-11-27 |
| IRS foreign trust reporting, filing tips: no discretionary December extension of Form 3520 | https://www.irs.gov/businesses/international-businesses/foreign-trust-reporting-requirements-and-tax-consequences | 2026-11-27 |
| 26 USC 6501(c)(8): assessment extension and reasonable-cause limitation; unchanged exact rule reused from completed US reporting claims read 26 November, applicability checked | https://uscode.house.gov/us/usc/t26/s6501/ | 2026-11-26 |

Not yet confirmed: arrangement-specific classifications and sections 673–678/672(f)(5); obligation/guarantee and section 643(i) interactions; pension/savings exemptions under Rev. Proc. 2014-55, Rev. Proc. 2020-17 (including contribution/eligibility tests and Form 843) and proposed section 1.6048-5 reliance/current status; actual corpus/UNI, throwback/interest computations; section 6662(j), penalty relief and late-filing route; section 684, sale/distribution basis, foreign-country treatment and sections 2801/877A. Each is held for a partner accountant above. No operative exemption or tax amount is supplied for those held points. Recheck future form revisions and taxpayer-specific deadline relief before filing.
