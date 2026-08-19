---
name: au-rd-incentive
description: >
  Use this skill whenever asked about the Australian R&D Tax Incentive (R&DTI) -- the Division 355 tax offset for eligible research and development, who can claim (incorporated R&D entities only), the refundable offset for companies under $20m aggregated turnover, the non-refundable offset with intensity tiers for larger companies, core vs supporting R&D activities, excluded activities, registration with AusIndustry/DISR within 10 months of year end, the $20,000 expenditure threshold, the $150 million cap, feedstock and clawback adjustments, aggregated turnover grouping, and record-keeping. Trigger on phrases like "R&D tax incentive", "R&DTI", "R&D offset", "research and development tax", "43.5% offset", "refundable R&D", "Division 355", "AusIndustry registration", "core R&D activities", "feedstock adjustment", or "R&D intensity". ALWAYS read this skill before touching any R&D tax offset work.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia R&D Tax Incentive Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context.** The R&DTI was reformed for income years starting on or after 1 July 2021 (Treasury Laws Amendment (A Tax Plan for the COVID-19 Economic Recovery) Act 2020): the old flat 43.5% refundable and 38.5% non-refundable rates were replaced with company-tax-rate-plus-premium rates and a two-tier R&D intensity test; the expenditure cap rose from $100m to $150m; a uniform clawback rule and Part IVA were extended to the offset. From income years starting on or after 1 July 2025, R&D activities relating to tobacco or gambling are ineligible unless conducted for the sole purpose of harm minimisation. The statutory four-year amendment period applies to R&D claims. Verify all rates before relying.

> **AUDIT FLASH POINT** The R&DTI is one of the ATO's most actively audited concession areas. Whether an activity is a "core R&D activity" is a technical/engineering judgement about scientific uncertainty and the knowledge threshold, NOT an accounting judgement. Registration is with AusIndustry/DISR; the offset is claimed with the ATO. Both agencies run compliance programs, and expenditure claimed is published in an annual transparency report.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1997 Division 355; Industry Research and Development Act 1986 (IR&D Act) |
| Administrators | Australian Taxation Office (offset/expenditure) + AusIndustry/DISR (registration, activity eligibility, findings) on behalf of Industry Innovation and Science Australia |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027) |
| What it is | A tax OFFSET for eligible R&D, claimed in the company tax return. NOT a grant. |
| Eligible entity | Corporation only (R&D entity, s 355-35): incorporated under Australian law; OR foreign-incorporated but Australian tax resident; OR foreign-incorporated, DTA-country resident, carrying on business through a permanent establishment |
| Not eligible | Individuals/sole traders, partnerships (except R&D partnerships claiming at partner level), trusts (except a body corporate as trustee of a public trading trust), corporate limited partnerships, exempt entities (wholly income-tax exempt) |
| Refundable offset | Aggregated turnover < $20m AND not controlled by exempt entities: company tax rate + 18.5% premium (= 43.5% for a 25% base-rate entity) |
| Non-refundable offset | Aggregated turnover >= $20m OR exempt-controlled: company tax rate + 8.5% premium (R&D up to 2% intensity); company tax rate + 16.5% premium (R&D above 2% intensity) |
| Expenditure cap | $150m notional deductions per year; offset rate drops to the bare company tax rate above it |
| Minimum spend | $20,000 notional deductions, UNLESS via a registered Research Service Provider (RSP) or CRC contribution |
| Registration deadline | With DISR, every income year, within 10 months of year end, BEFORE claiming in the return |
| Amendment window | 4 years (generally), tied to DISR findings |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown whether an activity is core R&D | Do NOT self-classify. This is a technical/engineering judgement about scientific uncertainty -- escalate (R-AU-RD-1) |
| Unknown registration status | Assume NOT registered; confirm the DISR registration (IISA) number and that it matches the income year before computing any offset |
| Unknown aggregated turnover | Compute the group figure (entity + connected + affiliated, net of intra-group dealings) before choosing refundable vs non-refundable; do not guess |
| Software development claimed | Assume the internal-administration exclusion may apply; test dominant purpose before treating as core R&D |
| Business-as-usual / routine activity claimed | Treat as ineligible ordinary business activity until shown to involve scientific uncertainty and the scientific method (TA 2017/3) |
| Feedstock output sold or used | Assume a feedstock adjustment is triggered; quantify |
| Overseas R&D activity | Assume NOT claimable unless a positive DISR overseas finding (s 28D IR&D Act) is in place |
| Expenditure incurred to an associate | Notionally deductible only when PAID, not merely incurred |

## Section 2 -- What it is and who can claim

The R&DTI is a tax offset claimed through the company tax return. It is **not a grant**: there is no application for funding, no competitive round, and no payment independent of the tax system. The benefit is delivered as an offset against tax, and for small companies the excess over tax liability is **paid out in cash**. Eligible expenditure MUST be claimed under the R&DTI -- if you choose not to claim it under the R&DTI, you cannot deduct it elsewhere in the return (unlike the former R&D tax concession).

**The offset rate and refundability depend primarily on aggregated turnover and exempt-entity control, NOT on the size of the R&D spend.**

- **Refundable offset** -- aggregated turnover < $20m AND not controlled by one or more exempt entities. Rate = company tax rate + 18.5%. For a base-rate entity (25%) this is **43.5%**. Where the offset exceeds tax liability the balance is refunded in cash (subject to franking-debit deferral rules).
- **Non-refundable offset** -- aggregated turnover >= $20m OR controlled by exempt entities. Rate = company tax rate + a premium set by R&D intensity (see Rule 5). It reduces tax; any unused amount may be carried forward under the tax offset carry-forward rules. It is never refunded.

## Section 3 -- GL sweep library

R&DTI work starts with the general ledger and the project/time records, not the offset claim the client hopes to make.

| GL pattern | Likely issue | Action |
|---|---|---|
| R&D expense / "R&D project" cost centres | Candidate notional deduction | Map each account to a registered DISR activity; confirm it is core or supporting, not BAU |
| Project codes / job codes linked to a DISR registration number | Expenditure linked to registered activities | Trace to the registration (IISA number) for the correct income year; confirm 10-month deadline met |
| Payroll allocations / timesheet-coded wages to R&D projects | Salary notional deduction | Substantiate time via timesheets/job cards; apportion between R&D and non-R&D on a reasonable, documented basis |
| Contractor / RSP invoices for R&D | External R&D expenditure | Confirm the RSP is registered with DISR; if under $20k total, the RSP pathway is what preserves eligibility |
| Depreciation on assets used in R&D | Asset cost is NOT notionally deductible | Use decline-in-value notional deductions instead; do not claim the asset's acquisition cost |
| Government grant income (recoupment) for R&D | Clawback adjustment | A recoupment for claimed R&D triggers a clawback (assessable income), not a reduction of the grant |
| "R&D" account holding rent, marketing, admin overhead | Ineligible / apportionment risk | Remove general operations and marketing; apply a reasonable, documented apportionment methodology only where there is a direct link |
| Software development capitalised/expensed | Internal-administration exclusion risk | Test dominant purpose; internal admin software for the entity/connected/affiliate is excluded from core |
| Intercompany charges to associates for R&D | Notional deduction only when PAID | Claim in the year paid, not incurred; check TA 2023/4 (R&D delivered by associates) |
| Materials/feedstock consumed in trials | Feedstock adjustment on sale/own use of output | Track feedstock inputs and outputs; quantify the adjustment in the trigger year |

## Section 4 -- Worked examples

### Example 1 -- Small company refundable offset (43.5%)

Innovate Pty Ltd (2026-27): aggregated turnover $4.2m, not exempt-controlled, base-rate entity (company tax rate 25%). Notional R&D deductions $300,000 on registered activities. Taxable income before offset $150,000.

```
Offset rate = 25% + 18.5% = 43.5%
R&D offset = $300,000 x 43.5% = $130,500
Gross tax = $150,000 x 25% = $37,500
Tax after offset = $37,500 - $130,500 = -$93,000
Refund (cash) = $93,000   (excess offset refunded; franking-debit deferral applies)
```

The $93,000 is paid out in cash. This is the refundable offset's core feature: it funds loss-making R&D companies.

### Example 2 -- Loss-making small company (full refund)

StartUp Co (2026-27): aggregated turnover $1.8m, notional R&D deductions $250,000, tax loss for the year (no tax payable).

```
R&D offset = $250,000 x 43.5% = $108,750
Tax liability = $0
Refund = $108,750 (entire offset refunded in cash)
```

A small R&D company with no tax liability still receives the offset as cash. The notional deduction itself is not also claimed as a deduction -- the offset replaces it.

### Example 3 -- Larger company non-refundable offset with intensity tiers

BigCo Ltd (2026-27): aggregated turnover $80m, standard company tax rate 30%, not exempt-controlled. Total expenditure $200m; notional R&D deductions $8m.

```
R&D intensity = $8m / $200m = 4%
First 2% of total expenditure = 2% x $200m = $4m  -> CTR + 8.5% = 38.5%
Above 2% (remaining $4m)                             -> CTR + 16.5% = 46.5%

Offset = ($4,000,000 x 38.5%) + ($4,000,000 x 46.5%)
       = $1,540,000 + $1,860,000
       = $3,400,000  (non-refundable; reduces tax, excess carried forward)
```

### Example 4 -- Expenditure cap ($150m)

Company XYZ (2026-27): aggregated turnover $600m, company tax rate 30%. Total expenditure $250m; notional R&D deductions $170m.

```
2% of total expenditure = 2% x $250m = $5m            -> 30% + 8.5%  = 38.5%
Remaining intensity band to $150m = $150m - $5m = $145m -> 30% + 16.5% = 46.5%
Above the $150m cap = $170m - $150m = $20m             -> 30% (no premium)

Offset = ($5m x 38.5%) + ($145m x 46.5%) + ($20m x 30%)
       = $1,925,000 + $67,425,000 + $6,000,000
       = $75,350,000
```

Above $150m of notional deductions, the offset rate collapses to the bare company tax rate, so the R&D premium (the incentive component) is nil on the excess.

### Example 5 -- Feedstock adjustment (clawback)

Landscape Supplies Pty Ltd: aggregated turnover $15m (base-rate 25%, refundable 43.5%). Notional R&D deductions $22,000, including $10,000 feedstock expenditure. The granite-sand output is sold for $9,000 in the same year.

```
Step 1: clawback amount = lesser of feedstock expenditure ($10,000) and
        feedstock revenue ($9,000) = $9,000
Step 2: incentive component = (starting offset - adjusted offset - deduction amount)
        starting offset = $22,000 x 43.5% = $9,570
        adjusted offset = ($22,000 - $9,000) x 43.5% = $5,655
        deduction amount = $9,000 x 25% = $2,250
        = $9,570 - $5,655 - $2,250 = $1,665
Step 3: gross up to assessable income = $1,665 / 25% = $6,660
```

$6,660 is added to assessable income. The clawback recovers only the 18.5% incentive premium on the feedstock, not the base deduction equivalent.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- It is an offset, not a grant

The R&DTI produces a tax offset under Division 355. It is claimed in the company tax return via the R&D schedule, and is administered jointly: DISR/AusIndustry registers activities and rules on their eligibility (including advance and overseas findings); the ATO administers the offset and the expenditure claimed. Receiving a DISR registration number means only that a complete application was received -- it is NOT a ruling that the activities qualify. Both agencies can take compliance action before or after the offset is paid, and claimed R&D expenditure is published in an annual transparency report (two years after year end).

### Rule 2 -- Eligible entity (s 355-35)

Only a corporation can be an R&D entity: incorporated under Australian law; or foreign-incorporated but an Australian tax resident; or foreign-incorporated, resident in a DTA country whose treaty defines "permanent establishment", and carrying on business in Australia through that PE. **Not eligible:** individuals (sole traders), partnerships as such (partners in an R&D partnership may claim at partner level), trusts (except a body corporate as trustee of a public trading trust), corporate limited partnerships, and exempt entities whose income is wholly exempt. Consolidated/MEC groups claim through the head company only.

### Rule 3 -- Core R&D activities

Experimental activities: (a) whose outcome cannot be known or determined in advance on the basis of current knowledge, information or experience; (b) determined only by applying a systematic progression of work based on established science, proceeding from hypothesis to experiment, observation and evaluation to logical conclusions; and (c) conducted for the purpose of generating new knowledge (including new or improved materials, products, devices, processes or services). All three limbs must be met. This is a **scientific/technical test, not an accounting one** -- whether the outcome "cannot be known in advance" turns on the state of knowledge in the field, which is a judgement for a competent engineer/scientist, not the bookkeeper.

### Rule 4 -- Supporting R&D activities

Activities directly related to core R&D activities. Where the activity produces (or is directly related to producing) goods or services, or is one of the excluded-core categories, it must ALSO have been undertaken for the **dominant purpose** of supporting a core R&D activity. Supporting activities never stand alone -- they exist only in relation to an eligible core activity.

### Rule 5 -- Offset rates and the intensity tiers

- **Refundable** (aggregated turnover < $20m, not exempt-controlled): company tax rate + 18.5%. Base-rate (25%) entity = 43.5%; standard-rate (30%) entity = 48.5%.
- **Non-refundable** (>= $20m or exempt-controlled): company tax rate + 8.5% on notional deductions up to 2% R&D intensity, and company tax rate + 16.5% above 2%. R&D intensity = notional R&D deductions / total expenditure for the year.
- **$150m cap:** for notional deductions above $150m in a year, the offset rate is the bare company tax rate (no premium). For years commencing before 1 July 2021 the cap was $100m.

### Rule 6 -- Excluded core activities (s 355-25(2))

The following CANNOT be core R&D activities (though some may qualify as supporting if directly related and dominant-purpose tests are met):
1. Market research/testing/development or sales promotion (incl. consumer surveys).
2. Prospecting, exploring or drilling for minerals or petroleum (to discover, locate, size or value deposits).
3. Management studies or efficiency surveys.
4. Research in the social sciences, arts or humanities.
5. Commercial, legal and administrative aspects of patenting, licensing or other IP activities.
6. Activities associated with complying with statutory requirements or standards (incl. routine testing/analysis).
7. Reproduction of a commercial product or process (by physical examination or from plans/public information).
8. Developing, modifying or customising computer software for the dominant purpose of internal administration of the entity or a connected/affiliated entity.

**Tobacco and gambling:** from income years starting on or after 1 July 2025, activities relating to tobacco or gambling are ineligible as core or supporting unless conducted for the sole purpose of harm minimisation.

### Rule 7 -- Registration and the 10-month deadline

Activities must be registered with DISR **for every income year**, **within 10 months of the end of the income year** (e.g. 30 April 2027 for a 30 June 2026 year end), and **before** the offset is claimed in the return. The DISR IISA registration number must appear on the R&D schedule and match the income year. Failure to register in time is fatal to the claim -- there is no discretion to backdate. Registration is self-assessment: the number does not certify eligibility.

### Rule 8 -- The $20,000 threshold and the RSP exception

Notional deductions for the year must total at least $20,000. This threshold does NOT apply where the R&D is conducted by a registered Research Service Provider (RSP) on the entity's behalf, or the entity contributes to the Cooperative Research Centres (CRC) program. RSPs must themselves register annually with DISR.

### Rule 9 -- Aggregated turnover grouping

Aggregated turnover = the entity's annual turnover + the annual turnover of every connected entity and affiliate (Australian and foreign) for the period they are connected/affiliated, excluding dealings between them. The rules mirror the small-business-entity aggregated-turnover rules. This grouping decides refundable vs non-refundable, so it must be computed across the whole group before the offset rate is chosen (R-AU-RD-5).

### Rule 10 -- Notional deductions: what can and can't be claimed

Eligible expenditure on registered activities is claimed as a notional deduction in the year incurred. Exceptions: amounts incurred to an associate are claimable only when PAID; prepayment rules apply to services spanning years. **Cannot** be notionally deducted: interest expenditure; expenditure not "at risk" (TR 2021/5); core technology expenditure; expenditure included in the cost of a depreciating asset (decline-in-value notional deductions may apply instead); and expenditure to acquire/construct/improve a building. Eligible R&D expenditure must be claimed under the R&DTI or not at all.

### Rule 11 -- Clawback: feedstock, recoupments, balancing adjustments

A clawback event adds an amount to assessable income (it does not reduce the offset) to recover the incentive/premium component. Triggers: (a) a government recoupment/grant for expenditure already claimed; (b) a feedstock adjustment where claimed feedstock inputs are transformed into products supplied to others or applied to own use; (c) an assessable balancing adjustment on disposal of an R&D asset (a deductible balancing adjustment gives a "catch-up" deduction instead). The clawback is the premium component grossed up to an assessable-income equivalent (see Example 5). From 1 July 2021 Part IVA extends to the R&D offset, including schemes to obtain a refundable rather than a non-refundable offset.

### Rule 12 -- Amendment and objection windows

The amendment period for R&D claims is generally **4 years** (a 2-year period may apply to 2021-22 and earlier). Special rules allow amendment outside the standard window to give effect to DISR findings (registration, overseas activities, core technology) and to DISR internal-review, ART or court decisions. DISR findings bind the Commissioner: the ATO must amend to give effect to them, and will commence an audit 28 days after a finding if the taxpayer does not self-amend.

### Rule 13 -- Interaction with the instant asset write-off and small business concessions

An R&D entity can be a small business entity and use the instant asset write-off ($20,000 for 2025-26; announced permanent from 1 July 2026) for assets used in the business. But the R&DTI and IAWO interact at the asset-cost level: expenditure included in the cost of a depreciating asset is NOT a notional deduction, so an amount immediately written off under the IAWO is not also claimable as R&D expenditure. Instead, the R&DTI gives a notional deduction for the asset's **decline in value** to the extent of R&D use. Do not double-count an asset's cost across both concessions. The aggregated-turnover grouping rules are shared with the small business concessions, but the R&DTI has its own $20m threshold and exempt-entity-control test, which are not the same as the small business entity tests.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Core vs ordinary business activity
**Trigger:** claim includes routine, business-as-usual, or commercial-risk activities. **Issue:** TA 2017/3 targets claims for ordinary business activities dressed as R&D (no scientific uncertainty, no hypothesis-driven experiment, no new knowledge). **Action:** refuse classification (R-AU-RD-1); document; escalate.

### T2-2 -- Software development claims
**Trigger:** software development claimed as core R&D. **Issue:** internal-administration software for the entity/connected/affiliate is excluded from core; even non-internal-admin software must still clear the knowledge threshold (outcome not knowable in advance). Much routine development fails. **Action:** test dominant purpose and the knowledge threshold; escalate (R-AU-RD-1).

### T2-3 -- R&D delivered by associates / overseas related entities
**Trigger:** notional deductions for R&D performed by an associate, or overseas R&D by a foreign related entity. **Issue:** amounts to associates claimable only when paid (TA 2023/4); overseas activities need a positive DISR overseas finding and must be conducted FOR the claimant, not the foreign entity. **Action:** confirm payment and findings; escalate (R-AU-RD-4).

### T2-4 -- Overhead apportionment
**Trigger:** rent, utilities, admin overheads apportioned to R&D. **Issue:** apportionment must reflect the actual extent of R&D use on a reasonable, documented basis; salary-based ratios are appropriate for personnel but not necessarily for utilities. **Action:** sight the documented methodology; flag unreasonable apportionment.

### T2-5 -- Group aggregation and Part IVA
**Trigger:** aggregated turnover near the $20m threshold, or group structures that appear to engineer a refundable rather than non-refundable outcome. **Issue:** connected/affiliate turnover must be aggregated; from 1 July 2021 Part IVA can cancel an offset (including a refundability benefit) where the dominant purpose was to obtain it. **Action:** compute group turnover properly; escalate structuring (R-AU-RD-5).

### T2-6 -- "At risk" expenditure
**Trigger:** R&D funded under arrangements guaranteeing a return, or covered by an indemnity. **Issue:** expenditure not at risk is not claimable (TR 2021/5). **Action:** examine funding terms; escalate.

---

## Section 7 -- Refusal catalogue

These are deliberate refusal-and-escalate zones. Do NOT answer them from this skill.

| Code | Trigger | Message |
|---|---|---|
| R-AU-RD-1 | Whether a specific activity qualifies as a core or supporting R&D activity | "Whether an activity is R&D is a technical/engineering judgement about scientific uncertainty and the knowledge threshold under s 355-25, not an accounting judgement. This needs a competent professional in the field and, for certainty, an AusIndustry/DISR advance finding. I can help organise the project documentation but cannot classify the activity." |
| R-AU-RD-2 | Preparing or lodging the DISR registration application | "Registration is a self-assessed application to AusIndustry/DISR describing the activities against the legislative criteria. I can't draft or lodge it. Refer to AusIndustry (13 28 46) or a registered R&D tax adviser; the registration must be lodged within 10 months of year end." |
| R-AU-RD-3 | Advance findings, overseas findings, or binding certainty on eligibility | "Only DISR can make an advance finding (activity eligibility) or an overseas finding (s 28D IR&D Act). These are binding decisions for your specific facts. Refer to AusIndustry; I can help assemble the supporting records." |
| R-AU-RD-4 | Overseas R&D activities | "Activities conducted overseas are claimable only with a positive DISR overseas finding, and only where conducted for the claimant (not a foreign related entity). This needs the finding in place before claiming. Refer to AusIndustry." |
| R-AU-RD-5 | Aggregated expenditure/turnover across connected or affiliated groups | "Aggregated turnover across connected and affiliated entities (including foreign ones) determines refundable vs non-refundable, and group structuring can attract Part IVA. Compute the group position with the client's adviser; I can prepare the underlying turnover figures per entity." |

---

## Section 8 -- Reading guide

1. Registration first: no valid, in-time DISR registration for the income year means no claim, regardless of how good the R&D is.
2. Entity test second: only a corporation (R&D entity) can claim. A sole trader or trust "doing R&D" has no R&DTI pathway.
3. Activity test third: core activities must clear all three limbs (unknowable outcome, systematic progression, new knowledge) -- and that is a technical judgement this skill refuses to make.
4. Rate test fourth: aggregated turnover and exempt-entity control choose refundable vs non-refundable; intensity tiers set the non-refundable premium.
5. Expenditure test fifth: only eligible notional deductions on registered activities count; associate amounts only when paid; asset costs give decline-in-value, not cost.
6. Clawback always: grants, feedstock outputs and asset disposals pull back the premium through assessable income.

---

## Section 9 -- Onboarding fallback

If the client provides only financial statements:

1. Sweep the GL per Section 3 for R&D-coded accounts, project codes and payroll allocations.
2. Confirm the entity is a corporation and request the DISR registration (IISA) number for the relevant income year.
3. Request timesheets, project plans and the apportionment methodology -- do not accept bare account balances.
4. Compute aggregated turnover across connected/affiliated entities before selecting an offset rate.
5. **Flag:** "Figures prepared from financial statements only. DISR registration number, contemporaneous project documentation, timesheets, apportionment methodology and group turnover not sighted. Activity eligibility is a technical judgement requiring review. No position should be taken until a qualified R&D tax adviser confirms."

---

## Section 10 -- Reference material

### Key figures

| Item | Value |
|---|---|
| Refundable offset (turnover < $20m, not exempt-controlled) | Company tax rate + 18.5% (43.5% for a 25% base-rate entity) |
| Non-refundable offset | Company tax rate + 8.5% (R&D <= 2% intensity); + 16.5% (R&D > 2% intensity) |
| R&D intensity | Notional R&D deductions / total expenditure for the year |
| Expenditure cap | $150m notional deductions; offset drops to bare company tax rate above it |
| Minimum notional deduction | $20,000 (waived for registered RSP / CRC) |
| Registration deadline | Within 10 months of income year end, before claiming, every year |
| Amendment period | Generally 4 years; special rules give effect to DISR findings |
| Tobacco/gambling | Ineligible for income years from 1 July 2025 unless sole-purpose harm minimisation |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Statute | ITAA 1997 Division 355 (ss 355-1 to 355-750); s 355-25 (core activities/exclusions); s 355-35 (R&D entity); Industry Research and Development Act 1986, s 28D (overseas findings) |
| Rates/entitlements | ato.gov.au -- R&D tax incentive rates and entitlements (QC 107282, 70869, 70890, updated 13 May 2026) |
| Eligibility | ato.gov.au -- Eligibility for the R&D tax incentive (QC 70871, updated 13 May 2026) |
| Steps/registration/records | ato.gov.au -- Steps for claiming R&D tax offset (QC 70872); Keeping records and calculating notional deductions (QC 71853) |
| Excluded activities | business.gov.au -- Excluded R&D activities under the R&DTI (s 355-25(2) ITAA 1997) |
| Clawback/feedstock | ato.gov.au -- Clawback of R&D tax incentive offset (QC 70876, 70889); TR 2013/3 (feedstock); TR 2021/5 (at-risk rule) |
| Compliance | ato.gov.au -- Helping you get R&D claims right (QC 70873); TA 2017/3 (ordinary business activities); TA 2023/4 (associates) |
| Amendments | ato.gov.au -- Correcting mistakes and disputing decisions (QC 70877) |

### Test suite

**Test 1:** 25% base-rate entity, turnover $4m, notional deductions $300,000. -> Offset = $300,000 x 43.5% = $130,500 (refundable).

**Test 2:** Sole trader spends $80,000 on genuine R&D. -> No R&DTI claim: not an R&D entity.

**Test 3:** 30% entity, total expenditure $200m, notional deductions $8m. -> Intensity 4%; offset = ($4m x 38.5%) + ($4m x 46.5%) = $3,400,000 (non-refundable).

**Test 4:** Notional deductions $170m, total expenditure $250m, 30% entity. -> Offset $75,350,000; the $20m above the $150m cap earns only the bare 30%.

**Test 5:** Notional deductions $18,000, no RSP/CRC. -> Below the $20,000 threshold; no claim.

**Test 6:** Software built to run the claimant's own payroll. -> Internal-administration software; excluded from core R&D activities.

**Test 7:** Registration lodged 11 months after year end. -> Late; claim fails for that year (no backdating).

**Test 8:** Feedstock revenue $9,000, feedstock expenditure $10,000, 43.5% offset, 25% CTR. -> $6,660 added to assessable income (Example 5).

**Test 9:** $100,000 incurred to an associate for R&D, unpaid at year end. -> Not notionally deductible until paid.

**Test 10:** Company receives a $50,000 government grant recouping claimed R&D expenditure. -> Clawback: the premium component on the recouped amount is added to assessable income; the grant is not netted off.

### Prohibitions

- NEVER treat the R&DTI as a grant -- it is a tax offset claimed in the company return
- NEVER classify an activity as core/supporting R&D -- that is a technical/engineering judgement (R-AU-RD-1); escalate
- NEVER prepare or lodge the DISR registration application -- refer to AusIndustry (R-AU-RD-2)
- NEVER advise on advance or overseas findings -- DISR only (R-AU-RD-3, R-AU-RD-4)
- NEVER compute the offset without first confirming a valid, in-time DISR registration for the income year
- NEVER choose refundable vs non-refundable without computing aggregated turnover across connected/affiliated entities (R-AU-RD-5)
- NEVER claim amounts incurred to an associate before they are paid
- NEVER claim the cost of a depreciating asset -- use decline-in-value notional deductions
- NEVER ignore a feedstock, recoupment or balancing-adjustment clawback
- NEVER present figures as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

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
