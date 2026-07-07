---
name: ga-net-worth-tax
description: Tier 2 Georgia content skill for the Net Worth Tax under Form 600 Part II — a separate capital/equity tax distinct from corporate income tax. Covers tax year 2025 including the application to C-corporations, S-corporations, and LLCs taxed as corporations (NOT to sole props, partnerships, or multi-member LLCs taxed as partnerships), the tax base as the greater of issued+outstanding capital stock+paid-in-capital or net worth (assets minus liabilities), the graduated rate structure with cap at $5,000, apportionment for multistate corporations, and filing combined with the corporate income tax Form 600.
jurisdiction: US-GA
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ga-net-worth-tax

## Georgia Net Worth Tax — Form 600 Part II

## 1. Scope and Purpose

- **Net Worth Tax filing forms** — This skill prepares the Georgia Net Worth Tax computation for corporations and LLCs taxed as corporations that are subject to Georgia's separate capital/equity tax under O.C.G.A. § 48-13-70 et seq. The Net Worth Tax is filed annually on Form 600 Part II (for C-corporations) or Form 600S Part III (for S-corporations), combined with the corporate income tax return.  _(O.C.G.A. § 48-13-70 et seq.)_
- **Scoped narrowly to** — C-corporations chartered in Georgia or doing business in Georgia; S-corporations chartered in Georgia or doing business in Georgia; Domestic LLCs that have elected to be taxed as corporations (Form 8832 or Form 2553); Foreign corporations registered to do business in Georgia (qualified through the Georgia Secretary of State)
- **Out of scope** — Sole proprietorships (no entity to tax); General partnerships; Limited partnerships (LPs); Multi-member LLCs taxed as partnerships (default federal classification); Single-member LLCs disregarded for federal tax (disregarded for GA net-worth tax too — see Section 4.4); Trusts and estates; Nonprofit corporations exempt under O.C.G.A. § 48-13-73 (these are exempt from net worth tax even though they file Form 600-T for unrelated business income); Insurance companies (subject to premium tax in lieu of net worth tax under O.C.G.A. § 33-8-4); Financial institutions subject to the Georgia Financial Institutions Business Occupation Tax under O.C.G.A. § 48-6-93 (which is in lieu of net worth tax); Public utilities subject to gross receipts tax in lieu  _(O.C.G.A. § 48-13-73; O.C.G.A. § 33-8-4; O.C.G.A. § 48-6-93)_
- **Critical architecture note** — The Net Worth Tax is completely separate from the Georgia corporate income tax (the 5.39% rate for 2025 under O.C.G.A. § 48-7-21, as reduced by HB 1437 / HB 1015 acceleration). An entity can owe ZERO income tax (loss year, full credit offset, S-corp with no GA-source income at entity level) and still owe net worth tax. This is the #1 source of taxpayer confusion and the most common audit-letter trigger.  _(O.C.G.A. § 48-7-21)_

## 2. What It Is — Net Worth Tax vs. Corporate Income Tax

### 2.1 The two taxes side by side

**The two taxes side by side**  _(O.C.G.A. § 48-7-21; O.C.G.A. § 48-13-70 et seq.)_

| Feature | Corporate Income Tax | Net Worth Tax |
| --- | --- | --- |
| **Statutory base** | O.C.G.A. § 48-7-21 | O.C.G.A. § 48-13-70 et seq. |
| **Form location** | Form 600 Part I (Schedule 1) | Form 600 Part II (Schedule 2) |
| **Tax base** | Federal taxable income, with GA adjustments, apportioned/allocated | Greater of (a) issued and outstanding capital stock + paid-in capital, or (b) net worth (assets − liabilities), apportioned if multistate |
| **Rate (2025)** | 5.39% flat (HB 1015, effective for tax years beginning on or after January 1, 2024, applied for 2025 unless further accelerated) | Graduated table: $10 to $5,000 cap |
| **Who pays** | C-corps and certain elective S-corps (PTET election) | C-corps, S-corps, LLCs-as-corps — regardless of income tax election |
| **Driven by profit** | Yes — no income, no tax | NO — driven by balance sheet, not P&L |
| **Apportionment** | Single-factor sales (gross receipts) under O.C.G.A. § 48-7-31, as amended | Same apportionment factor applies to net worth |
| **Loss carryforwards** | Yes (subject to GA NOL rules) | None — there is no "loss" concept |

### 2.2 The most important conceptual point

**The Net Worth Tax is a TAX ON BEING A CORPORATION IN GEORGIA, not a tax on earnings.**

It is functionally Georgia's equivalent of:
- Delaware's annual franchise tax
- California's $800 minimum franchise tax / 1.5% S-corp tax (under Cal. R&TC §§ 17941, 23153)
- Texas's franchise tax (which has its own structure — see the Texas franchise skill)
- Tennessee's franchise tax (1/4 of 1% of net worth)

Like all of these, it is owed even in a loss year, even in a startup year (subject to the new-corporation first-period rules in Section 7), and even when the entity is dormant but still in existence.

### 2.3 Why this matters operationally

Because the tax is balance-sheet-driven:

1. A profitable startup with a high paid-in-capital amount (think: VC-funded Delaware C-corp registered in Georgia) can owe MORE net worth tax than income tax in its early years.
2. A holding company with no operations but large paid-in capital owes net worth tax annually.
3. An S-corp distributing all earnings (so book equity stays flat) still owes net worth tax based on its balance sheet.
4. Dissolution does NOT terminate the obligation — the entity must continue filing until formally dissolved with the Georgia Secretary of State AND the Georgia Department of Revenue (see Section 9.4 on final returns).

### 2.4 Historical note (do not rely on this for current filings)

The Net Worth Tax has existed in essentially its current form since 1979 (Ga. L. 1979, p. 5). The rate brackets were last adjusted by Ga. L. 2017, Act 284 (HB 283), which is what created the current $10 floor and $5,000 cap. Earlier filings (pre-2018) used a different schedule — do not apply the current schedule to prior-year returns.

## 3. Statutory Authority

**Statutory Authority**  _(O.C.G.A. § 48-13-70 et seq.)_

| Provision | Subject |
| --- | --- |
| O.C.G.A. § 48-13-70 | Definitions |
| O.C.G.A. § 48-13-71 | Imposition of net worth tax on corporations |
| O.C.G.A. § 48-13-72 | Domestic corporation net worth tax |
| O.C.G.A. § 48-13-73 | Exemptions (nonprofits, certain entities) |
| O.C.G.A. § 48-13-74 | Foreign corporations doing business in Georgia |
| O.C.G.A. § 48-13-75 | Apportionment of net worth |
| O.C.G.A. § 48-13-76 | Rate schedule (the graduated brackets) |
| O.C.G.A. § 48-13-77 | Due date — combined with income tax return |
| O.C.G.A. § 48-13-79 | Penalty for failure to file |
| Ga. Comp. R. & Regs. r. 560-7-3 | Departmental regulations on net worth tax |
| Form 600 instructions (2025) | Computational guidance from GA DOR |
| Form 600S instructions (2025) | S-corp version |

Cite to the O.C.G.A. section in any reviewer brief — Georgia Department of Revenue audit letters routinely reference these section numbers, and the reviewer needs to be able to trace any position back to the statute.

## 4. Who Pays — Entity-by-Entity Walk-Through

### 4.1 Domestic C-corporations

- **Domestic C-corp obligation** — A C-corporation chartered under Georgia law (filed Articles of Incorporation with the Georgia Secretary of State) pays net worth tax on its entire net worth, regardless of where it operates, subject to the apportionment rule in Section 6 if it does business outside Georgia. The fact that a Georgia-domiciled corporation may apportion only a small fraction of its activity to Georgia does NOT exempt it — it apportions the net-worth base.

### 4.2 Foreign C-corporations qualified in Georgia

- **Foreign corp registration obligation** — A corporation chartered in another state (most commonly Delaware) but registered to do business in Georgia (filed Application for Certificate of Authority with the Georgia Secretary of State) pays net worth tax on the portion of its net worth apportioned to Georgia. CRITICAL: Registration with the Georgia Secretary of State creates the net-worth filing obligation. Even if the foreign corporation has minimal Georgia activity, the registration itself triggers the obligation. The only way to terminate this obligation is to formally withdraw the certificate of authority through the Secretary of State.

[AUDIT FLASH POINT — FOREIGN CORP REGISTRATION] A Delaware C-corp that registered in Georgia ten years ago, opened a small sales office, closed the office, but never withdrew its certificate of authority, is still on the hook for annual net worth tax filings. Georgia DOR routinely cross-references the Secretary of State active-entity list against filed Form 600s and sends "failure to file" notices. The remediation is (a) file delinquent returns (often $10 each plus penalties), then (b) formally withdraw via Secretary of State. Do NOT advise the client to simply "stop filing" — this triggers the 5%/month penalty under O.C.G.A. § 48-13-79.

### 4.3 S-corporations (BOTH domestic GA S-corps and foreign S-corps registered in GA)

- **S-corps pay net worth tax** — Yes, S-corporations pay Georgia Net Worth Tax. This is one of the most common mistakes made by out-of-state CPAs preparing Georgia returns. Federal S-corp status (an income tax election under IRC § 1362) has no effect on Georgia's net worth tax. The net worth tax is imposed on the corporate entity, not on its income. The S-corp computes net worth tax on Form 600S Part III using the same graduated schedule as a C-corp. There is no "small S-corp" exception, no "single-shareholder" exception, no "S-corp with QBI passthrough" exception.  _(IRC § 1362)_

[AUDIT FLASH POINT — S-CORP OWNERS SURPRISED BY NET-WORTH TAX] The most frequent client complaint Charlie Barmore flagged is the S-corp owner who:

1. Forms a Georgia S-corp expecting to save self-employment tax
2. Receives an audit-style notice from GA DOR a year later for unpaid net worth tax
3. Insists "but my S-corp pays no Georgia tax — all income passes through to my 500 individual return"

The conversation must clarify: yes, income tax passes through, but the net worth tax is an entity-level tax that survives the S-election. Build this into the intake conversation up front. See Section 11 worked example #3.

### 4.4 LLCs

**LLC classification and GA net worth tax treatment**  _(O.C.G.A. § 48-13-71)_

| Federal classification | Georgia net worth tax treatment |
| --- | --- |
| Disregarded entity (single-member LLC, no Form 8832 election) | **Not subject** to net worth tax. Activity reported on owner's return. |
| Partnership (multi-member LLC, no election) | **Not subject** to net worth tax. |
| C-corp (Form 8832 election to be taxed as a corporation) | **Subject** to net worth tax under O.C.G.A. § 48-13-71 |
| S-corp (Form 2553 election) | **Subject** to net worth tax (same treatment as a corporate S-corp) |

- **Federal classification controls; regulation citation** — GA DOR Regulation 560-7-3-.06 confirms that the federal entity classification controls. There is no separate state-level LLC election in Georgia.  _(GA DOR Regulation 560-7-3-.06)_
- **Disregarded SMLLC owned by corporation** — A single-member LLC disregarded for federal tax purposes is not subject to the GA net worth tax, but the LLC's owner — if a corporation subject to GA net worth tax — must include the LLC's assets and liabilities in computing its own net worth (because the LLC is invisible for tax purposes).

### 4.5 Quick decision flowchart

```
Is the entity a corporation or LLC?
├── Sole prop / partnership / LP / multi-member LLC as partnership → NOT SUBJECT (skill exits)
└── Corporation or LLC taxed as corporation
    ├── Is it exempt under § 48-13-73?
    │    (nonprofit, insurance co, financial inst., utility)
    │    ├── Yes → NOT SUBJECT (skill exits, refer to specialized skill)
    │    └── No → continue
    ├── Is it chartered in Georgia?
    │    ├── Yes → domestic; tax on full net worth (apportioned if multistate)
    │    └── No → foreign
    │         ├── Registered with GA Secretary of State? → SUBJECT (apportion to GA)
    │         └── Not registered AND no nexus? → NOT SUBJECT
    └── Apply rate schedule from Section 5
```

## 5. Tax Base — The "Greater Of" Rule

### 5.1 The two competing bases

- **Base A and Base B definitions** — Under O.C.G.A. § 48-13-72, the net worth tax base for a domestic corporation is the greater of: Base A — Capital stock + paid-in capital: - Issued and outstanding capital stock (par value, or stated value if no par), PLUS - Paid-in capital (additional paid-in capital from share issuances above par/stated value) Base B — Net worth: - Total assets MINUS total liabilities (from the balance sheet as of the end of the tax year) The taxpayer computes both A and B and uses whichever is larger. There is no taxpayer election — the statute mandates the greater amount.  _(O.C.G.A. § 48-13-72)_

### 5.2 Why two bases?

The dual-base rule prevents two avoidance patterns:

1. Pattern 1 — Low capital stock, high retained earnings. A mature corporation with a tiny par value ($0.01 par × 1,000 shares = $10 capital stock) but $50M of retained earnings would owe almost no tax under a capital-stock-only system. The "net worth" alternative (which includes retained earnings) catches this.

2. Pattern 2 — Large IPO proceeds, accumulated deficit. A pre-IPO biotech with $200M of paid-in capital but $180M of accumulated deficit (net worth = $20M) would owe little under net worth alone. The "capital stock + paid-in capital" alternative ($200M) catches this.

The greater-of rule effectively imposes the tax on whichever balance-sheet measure is harder to manipulate.

### 5.3 Defining "issued and outstanding capital stock"

- **Issued and outstanding capital stock** — Includes: Common stock issued at par or stated value; Preferred stock issued at par or stated value; Any class of equity security issued by the corporation, valued at par or stated value. Excludes: Treasury stock (shares repurchased and held by the corporation) — subtracted from issued shares to get outstanding; Authorized but unissued shares; Convertible debt prior to conversion (debt, not equity, until conversion); Stock options and warrants (not yet exercised — no shares outstanding). For corporations with no-par stock, use stated value as set by the board of directors. If no stated value has been set, the GA DOR position (Regulation 560-7-3-.05) is that the no-par stock is included at the consideration received at issuance — which effectively merges with paid-in capital.  _(Regulation 560-7-3-.05)_

### 5.4 Defining "paid-in capital"

- **Paid-in capital** — Paid-in capital (sometimes called "additional paid-in capital" or "capital surplus" on older balance sheets) is the amount paid by shareholders above the par or stated value of the shares. Example: 1,000 shares at $0.01 par sold for $100 each. - Capital stock (par): 1,000 × $0.01 = $10 - Paid-in capital: 1,000 × ($100 − $0.01) = $99,990 - Total Base A: $100,000 Items typically classified as paid-in capital: - Premium on stock issuance - Stock-based compensation expense credited to APIC (under ASC 718, GAAP) - Tax benefit from stock option exercises (legacy ASC 718 treatment, pre-2017) - Capital contributions from shareholders without share issuance ("paid-in surplus") Items NOT in paid-in capital: - Retained earnings (those are in net worth, Base B) - Other comprehensive income (also in net worth, Base B) - Loans from shareholders (those are liabilities)

### 5.5 Defining "net worth" (Base B)

- **Net worth (Base B)** — Net worth means total assets minus total liabilities as shown on the balance sheet for the last day of the tax year (the same balance sheet used on federal Form 1120 Schedule L or Form 1120-S Schedule L). The GA DOR position (Reg. 560-7-3-.04) is that net worth is computed on the same accounting basis used for the federal return (typically GAAP, occasionally tax basis for small corporations using Schedule M-1 differences). The skill does NOT allow restating the balance sheet to a non-federal basis just to reduce net worth. Specific adjustments: - Treasury stock: reduces equity (and therefore net worth) - Accumulated deficit: reduces equity (negative net worth IS possible — see Section 5.7) - Goodwill: included in assets at book value, NOT removed - Intercompany receivables from affiliates: included in assets (no consolidated reporting for net worth) - Negative balance sheet items: do not net against positive items outside the same line  _(Reg. 560-7-3-.04)_

### 5.6 Where the numbers come from

**Form 600 Part II source mapping**

| Form 600 Part II item | Source on federal return |
| --- | --- |
| Issued capital stock | Form 1120 Sch L Line 22(a) common + Line 22(b) preferred (or 1120-S Sch L equivalent) |
| Paid-in capital | Form 1120 Sch L Line 23 (additional paid-in capital) |
| Total assets | Form 1120 Sch L Line 15(d) |
| Total liabilities | Form 1120 Sch L Lines 16-21(d) sum |
| Net worth (Base B) | Form 1120 Sch L Line 27(d) (total stockholders' equity) |

- **S-corp equivalent lines and Schedule L exemption** — For S-corps, the equivalent lines on Form 1120-S Schedule L. If the corporation does not file Schedule L (because total receipts and total assets are both under $250,000), it must still compute and report the balance sheet figures for the GA net worth tax. The Schedule L filing exemption is a federal procedural exemption, not a substantive one — Georgia still requires the underlying numbers.

### 5.7 Negative net worth

- **Negative net worth treatment** — If net worth (Base B) is negative — i.e., liabilities exceed assets — the entity still computes the tax using the greater of Base A or Base B. If Base A is positive (which it usually is, since shareholders had to invest something) and Base B is negative, the entity uses Base A. If BOTH Base A and Base B are zero or negative — extremely rare; would require a corporation with no par/stated value capital stock and no paid-in capital and negative equity — the corporation still owes the minimum $10 net worth tax. There is no zero-tax floor below the first bracket.

## 6. Apportionment for Multistate Corporations

### 6.1 The basic rule

- **Apportionment formula** — A multistate corporation apportions its net worth to Georgia using the same apportionment factor that it uses for Georgia corporate income tax (single-factor sales / gross receipts under O.C.G.A. § 48-7-31). The formula: ``` GA Net Worth = Total Net Worth × Georgia Apportionment Factor ``` The Georgia apportionment factor is: ``` Georgia gross receipts / Everywhere gross receipts ``` (For tax year 2025, Georgia is a single-sales-factor state. The historical three-factor formula was phased out over 2008-2010 and is no longer applicable.)  _(O.C.G.A. § 48-7-31)_

### 6.2 When apportionment applies

- **When apportionment applies** — Apportionment applies if the corporation has nexus and files corporate income tax returns in at least one state other than Georgia AND has property, payroll, or sales attributable to that other state. A corporation that does business only in Georgia uses 100% as its apportionment factor (and would not benefit from filing apportionment schedules).

### 6.3 Allocable vs. apportionable

- **Net worth is unitary — no allocation** — Under O.C.G.A. § 48-13-75, the entire net worth is treated as apportionable — there is no separate allocation of specific assets to specific states (unlike income tax, where some intangibles can be allocated). Net worth is a unitary base.  _(O.C.G.A. § 48-13-75)_

### 6.4 The 100% Georgia trap for domestic GA corporations

- **100% Georgia trap** — A Georgia-chartered corporation operating only in Georgia apportions 100% of its net worth to Georgia. There is no benefit to being "headquartered" in Georgia for net worth purposes (in contrast, some other states give a partial home-state benefit).

[AUDIT FLASH POINT — MISSING APPORTIONMENT FOR MULTISTATE] A surprising number of Georgia-chartered C-corps with operations in multiple states fail to apportion their net worth. The default — if the taxpayer leaves apportionment blank — is that GA DOR applies 100%. The taxpayer ends up paying $5,000 cap when proper apportionment would have produced a far lower bracket. This is recoverable by amended return (Form 600-X) within the statute of limitations, but only if caught. Build a checklist item: "If multistate operations, confirm Schedule 6 (apportionment) is completed and the same factor is applied to BOTH income tax AND net worth tax."

### 6.5 Apportionment for foreign corporations

- **Foreign corp apportionment example** — A foreign corporation registered in Georgia uses its Georgia apportionment factor to compute the portion of its net worth subject to Georgia tax. If the foreign corporation has, say, 3% of its sales in Georgia, then 3% of its net worth is the GA net worth base. Example: A Delaware C-corp with $200M total net worth and 3% GA apportionment factor has GA net worth of $6M, which falls into the bracket at Section 7 producing a $100 tax (or whatever the bracket dictates at that level). The corporation does NOT pay the $5,000 cap merely because its TOTAL net worth is high.

## 7. Rate Schedule (Tax Year 2025)

### 7.1 The graduated table

**Graduated table under O.C.G.A. § 48-13-76**  _(O.C.G.A. § 48-13-76)_

| Net worth (Georgia apportioned, Base A or B greater) | Tax |
| --- | --- |
| $0 to $10,000 | $10 |
| $10,001 to $25,000 | $20 |
| $25,001 to $40,000 | $40 |
| $40,001 to $60,000 | $60 |
| $60,001 to $80,000 | $75 |
| $80,001 to $100,000 | $100 |
| $100,001 to $150,000 | $125 |
| $150,001 to $200,000 | $150 |
| $200,001 to $300,000 | $200 |
| $300,001 to $500,000 | $250 |
| $500,001 to $750,000 | $300 |
| $750,001 to $1,000,000 | $500 |
| $1,000,001 to $2,000,000 | $750 |
| $2,000,001 to $4,000,000 | $1,000 |
| $4,000,001 to $6,000,000 | $1,250 |
| $6,000,001 to $8,000,000 | $1,500 |
| $8,000,001 to $10,000,000 | $1,750 |
| $10,000,001 to $12,000,000 | $2,000 |
| $12,000,001 to $14,000,000 | $2,500 |
| $14,000,001 to $16,000,000 | $3,000 |
| $16,000,001 to $18,000,000 | $3,500 |
| $18,000,001 to $20,000,000 | $4,000 |
| $20,000,001 to $22,000,000 | $4,500 |
| Over $22,000,000 | $5,000 (cap) |

This table is reproduced on the Form 600 instructions (page 5 of the 2025 instructions). Always confirm against the published table for the year being filed — the schedule has been amended several times historically (1979 original, 1989 revision, 2017 revision), and even though it has been stable since 2017, the bracket points may shift in future legislation.

### 7.2 How to read the brackets

- **Flat brackets, not marginal** — The brackets are NOT marginal — they are flat brackets. If your net worth is $1,500,001, you pay $750, not $750 + 1¢ extra. The entire net worth is taxed at the bracket-specific dollar amount. This means there are slight cliff effects at each bracket boundary. A corporation with net worth of $1,000,000 owes $500; a corporation with net worth of $1,000,001 owes $750. The $1 of extra net worth costs $250 in tax. For corporations near a bracket boundary, distribution timing can matter — paying a dividend on December 30 to drop net worth below a bracket cutoff saves the bracket differential. (This is a legitimate planning point, but be cautious about year-end distributions that create § 1368 or § 301 issues federally. Document the business purpose.)

### 7.3 The $5,000 cap

- **Maximum net worth tax** — $5,000 per year USD (applies to any corporation with apportioned Georgia net worth exceeding $22 million)

This cap is one reason large corporations sometimes prefer Georgia as a state of operations — Texas's franchise tax has no comparable cap and can run into seven figures for large corporations. Georgia's $5,000 cap is the highest individual line item, but it's still small relative to other state franchise taxes.

### 7.4 The $10 minimum

- **Minimum net worth tax** — $10 USD (Even a dormant corporation with zero assets owes $10 per year. Failure to file is what triggers the penalty under § 48-13-79, not failure to pay (since the amount is so small).)  _(O.C.G.A. § 48-13-79)_

### 7.5 First-period and short-period returns

- **No proration for short periods** — Under O.C.G.A. § 48-13-72(b), the first net worth tax period for a new corporation runs from the date of incorporation (or date of qualification, for a foreign corp) through the end of the corporation's first fiscal year. If this period is less than 12 months, the tax is NOT prorated — the corporation owes the full bracket amount based on its net worth at the end of the short period. For subsequent short periods (e.g., a change in accounting period), the tax is also not prorated — each accounting period generates a full net worth tax. Example: A corporation incorporates on October 1, 2025, and adopts a calendar year. Its first net worth tax return covers October 1, 2025 to December 31, 2025 (3 months). The full bracket amount is due — not 3/12 of the bracket amount.  _(O.C.G.A. § 48-13-72(b))_

## 8. Estimated Payments

### 8.1 The $500 threshold

- **De minimis estimated tax threshold** — $500 USD (A corporation owing $500 or less in net tax is not required to make estimated payments.)  _(O.C.G.A. §48-7-115)_
- **Threshold application examples** — For net-worth-tax-only purposes: since the cap is $5,000, a corporation with no income tax liability but with a net worth tax of $750 or more is required to make estimated payments (because $750 > $500 threshold). For corporations with both income and net worth tax: the $500 threshold applies to the COMBINED liability. A corporation expecting $400 of income tax and $200 of net worth tax has combined $600 > $500 and must pay estimates.

### 8.2 Estimated payment schedule

**Estimated payment schedule (Form 602-ES)**

| Installment | Due date (calendar year corp) |
| --- | --- |
| Q1 | April 15 |
| Q2 | June 15 |
| Q3 | September 15 |
| Q4 | December 15 (note: NOT January — Georgia is one of the few states with a December Q4 due date for corporate estimates) |

- **Fiscal-year corporation schedule** — For fiscal-year corporations: the 15th day of the 4th, 6th, 9th, and 12th months of the fiscal year.

### 8.3 Safe harbor

- **Underpayment safe harbor** — A corporation avoids the underpayment penalty if it pays the lesser of: 100% of the current year's total liability, OR 100% of the prior year's total liability (provided the prior year was a full 12 months and showed positive liability). The prior-year safe harbor is the operationally simpler choice for net-worth-tax-only situations, since the prior-year amount is known with certainty.

### 8.4 Underpayment penalty

- **Underpayment penalty rate (Form 600 UET)** — 9% per annum (or the federal short-term rate plus 3%, whichever is lower — for 2025 the GA DOR-published rate is 9%)  _(Form 600 UET (Underpayment of Estimated Tax))_

## 9. Filing Mechanics

### 9.1 Form 600 layout (C-corporations)

**Form 600 section layout**

| Form 600 section | Content |
| --- | --- |
| Page 1 | Identifying info, NAICS, dates |
| Part I | Computation of net income tax |
| Part II | **Computation of net worth tax** ← this skill's focus |
| Schedule 1 | Federal-to-Georgia income adjustments |
| Schedule 2 | Net worth tax computation details (issued/outstanding stock, paid-in capital, net worth, apportionment) |
| Schedule 6 | Apportionment factor computation |
| Schedule 7 | Allocation (rarely used now under single-factor) |
| Schedule 10 | Credits |

### 9.2 Form 600S layout (S-corporations)

**Form 600S section layout**

| Form 600S section | Content |
| --- | --- |
| Page 1 | Identifying info |
| Part I | Computation of income tax (typically zero for pure S-corp absent PTET election) |
| Part II | Schedule of shareholders |
| Part III | **Computation of net worth tax** ← this skill's focus |
| Schedule 6 | Apportionment |

- **Identical computation to Form 600 Part II** — The Net Worth Tax computation on Form 600S Part III is IDENTICAL to Form 600 Part II — same rate schedule, same base, same apportionment.

### 9.3 Due dates

**Due dates by entity type**

| Entity | Original due date | Extended due date |
| --- | --- | --- |
| Calendar year C-corp | April 15 | October 15 (with Form IT-303 / federal Form 7004) |
| Calendar year S-corp | March 15 | September 15 |
| Fiscal year corp | 15th day of 4th month after FYE | 6-month extension |

- **Same due date as federal** — The Form 600 due date is the SAME as the federal Form 1120 due date (per O.C.G.A. § 48-13-77, which ties to the federal date).  _(O.C.G.A. § 48-13-77)_

### 9.4 Final returns

- **Final return requirement** — When a corporation dissolves or withdraws its Georgia certificate of authority, it must file a final Form 600 covering the short period from the start of the fiscal year through the date of dissolution / withdrawal. The "Final Return" box on page 1 must be checked. Failure to file a final return is the most common reason for ongoing net-worth-tax assessments against dissolved entities. The Secretary of State and the Department of Revenue do not communicate well, and DOR will continue assessing minimum $10 tax + penalties for years against an entity that "dissolved" with the SOS but never filed a final return.

### 9.5 Where to file

- **Filing address and e-file requirement** — Mail: Georgia Department of Revenue, Processing Center, P.O. Box 740397, Atlanta, GA 30374-0397. E-file: Required for corporations with total receipts of $1M or more (O.C.G.A. § 48-2-32(f) and DOR Reg. 560-3-2-.26). Smaller corporations may e-file or paper file. E-filing is done via approved software (Drake, ProSystem fx, UltraTax, Lacerte, GoSystem, etc.) or directly through GTC (Georgia Tax Center).  _(O.C.G.A. § 48-2-32(f); DOR Reg. 560-3-2-.26)_

## 10. Penalties

### 10.1 Late filing penalty — O.C.G.A. § 48-13-79

- **Late filing penalty** — 5% of the tax due per month or fraction of a month, capped at 25% percent per month (Computed on the net worth tax portion of Form 600 separately from any income tax penalty. For a corporation that owes only the $10 minimum and files 6 months late: penalty is $10 × 5% × 5 (capped at 25%) = $2.50, plus interest. The DOR generally rounds to the dollar. For a corporation that owes the $5,000 cap and files 6 months late: $5,000 × 25% = $1,250 penalty.)  _(O.C.G.A. § 48-13-79)_

### 10.2 Late payment penalty — O.C.G.A. § 48-2-44

- **Late payment penalty** — 0.5% per month (capped at 25%) percent per month (for failure to pay tax shown on the return. This stacks with the late filing penalty up to a combined 25% cap (under § 48-2-44(b)).)  _(O.C.G.A. § 48-2-44)_

### 10.3 Interest

- **Interest rate on unpaid tax** — 9% per annum, compounded annually (Interest accrues on unpaid tax at the federal short-term rate plus 3%, compounded annually. The DOR publishes the rate annually — for 2025, it is 9%.)

### 10.4 Reasonable cause

- **Penalty abatement for reasonable cause** — Under O.C.G.A. § 48-2-44(a), the DOR may abate penalties for reasonable cause shown. Standard abatement requests use Form RD-1000 (penalty waiver request). Reasonable cause is interpreted similarly to the IRS standard.  _(O.C.G.A. § 48-2-44(a))_

## 11. Worked Examples

### 11.1 Example 1 — Small Georgia C-corporation

**Facts:**
- Atlas Manufacturing Inc., Georgia C-corp incorporated 2018
- Operations entirely in Georgia (100% apportionment)
- Year-end balance sheet (12/31/2025):
  - Issued common stock (par $1, 10,000 shares): $10,000
  - Paid-in capital: $90,000
  - Retained earnings: $700,000
  - Total liabilities: $0
  - Total assets: $800,000

**Computation:**
- Base A = $10,000 (capital stock) + $90,000 (paid-in capital) = $100,000
- Base B = $800,000 (assets) − $0 (liabilities) = $800,000
- Greater of A or B = **$800,000** (Base B wins)
- Apportionment: 100% Georgia
- GA net worth = $800,000

**Look up the bracket** in the Section 7 table: $750,001 to $1,000,000 → **$500 net worth tax**

**Result:** Atlas owes $500 net worth tax for 2025. Combined with income tax, Atlas exceeds the $500 estimated-payment threshold, so it must file Form 602-ES quarterly for 2026.

### 11.2 Example 2 — Large Georgia C-corporation at the cap

**Facts:**
- Peachtree Holdings Inc., GA-chartered C-corp
- Operations in Georgia, Tennessee, Florida (multistate)
- Year-end balance sheet (12/31/2025):
  - Issued common stock: $1,000
  - Paid-in capital: $100,000,000
  - Retained earnings: ($20,000,000) (accumulated deficit)
  - Total net worth (Base B): $80,001,000
  - Total assets: $250,000,000
- Georgia apportionment factor: 40% (40% of sales in Georgia)

**Computation:**
- Base A = $1,000 + $100,000,000 = $100,001,000
- Base B = $80,001,000
- Greater of A or B = **$100,001,000** (Base A wins because of the accumulated deficit)
- Apportionment: 40% × $100,001,000 = **$40,000,400**

**Look up the bracket** in Section 7: Over $22,000,000 → **$5,000 cap**

**Result:** Peachtree owes $5,000 net worth tax (the cap). Note that even if its GA apportioned net worth were $22,000,001 OR $200,000,000, the tax would still be $5,000. The cap means the marginal rate on apportioned net worth above $22M is zero.

[AUDIT FLASH POINT — accumulated deficit traps] Note in this example that Base A ($100M paid-in capital) is much larger than Base B ($80M net worth) precisely because of the $20M accumulated deficit. Tax preparers who default to "use net worth" without computing capital stock + paid-in capital understate the tax. For startups with heavy losses against high VC funding, Base A is almost always the controlling base.

### 11.3 Example 3 — S-corporation with surprised owner

**Facts:**
- Magnolia Consulting Inc., Georgia S-corp (incorporated 2024 as a C-corp, elected S-corp via Form 2553 effective 2024)
- Sole shareholder: an individual residing in Georgia
- Operations 100% in Georgia
- Year-end balance sheet (12/31/2025):
  - Issued common stock: $1,000
  - Paid-in capital: $50,000
  - Retained earnings (AAA equivalent): $1,949,000
  - Total assets: $2,000,000
  - Total liabilities: $0
- 2025 net income (federal Form 1120-S, passed through to shareholder): $400,000

**Computation:**
- Base A = $1,000 + $50,000 = $51,000
- Base B = $2,000,000
- Greater of A or B = **$2,000,000** (Base B wins)
- Apportionment: 100%

**Look up the bracket** in Section 7: $1,000,001 to $2,000,000 → **$750 net worth tax**

(If the net worth were $2,000,001 — one dollar higher — the tax would be $1,000. Bracket cliff in action.)

**Result:** Magnolia owes $750 net worth tax for 2025, filed on Form 600S Part III. The owner is surprised because:
- The S-corp owes zero Georgia income tax at the entity level (income passes through to the shareholder's Form 500)
- The owner did not anticipate any entity-level Georgia tax
- The $750 is real, owed by the corporation, and not deductible against the owner's individual return except as an ordinary business expense flowing through K-1

**Owner conversation script:** "Your S-corp pays Georgia Net Worth Tax — a separate capital tax that exists alongside income tax. It's based on your balance sheet, not your profits. For 2025, it's $750. Going forward, plan on this amount escalating as retained earnings grow, or distribute earnings annually to keep net worth in a lower bracket. The next bracket is $1,000 if you cross $2,000,000."

### 11.4 Example 4 — Foreign corporation registered in Georgia

**Facts:**
- Hyperion Software Inc., Delaware C-corp
- Registered with Georgia Secretary of State as a foreign corporation since 2020
- Total operations: $50M in revenue, of which $5M is from Georgia customers
- Year-end balance sheet (12/31/2025):
  - Issued common stock (no par, stated value $0.0001 × 50M shares): $5,000
  - Paid-in capital: $80,000,000
  - Retained earnings: $20,000,000
  - Total net worth (Base B): $100,005,000
- Georgia apportionment factor: $5M / $50M = 10%

**Computation:**
- Base A = $5,000 + $80,000,000 = $80,005,000
- Base B = $100,005,000
- Greater of A or B = **$100,005,000** (Base B wins)
- Apportionment: 10% × $100,005,000 = **$10,000,500**

**Look up the bracket** in Section 7: $10,000,001 to $12,000,000 → **$2,000 net worth tax**

**Result:** Hyperion owes $2,000 GA net worth tax for 2025, filed on Form 600 Part II. Combined with whatever its GA income tax liability is (5.39% × apportioned GA taxable income), the total likely exceeds $500, so Hyperion must file Form 602-ES estimates for 2026.

**Common error trap:** A Delaware C-corp with $100M+ total net worth might assume it owes the $5,000 cap. But apportionment matters — at 10% GA apportionment, the GA net worth base is only $10M, falling well below the cap. Always apply the apportionment factor BEFORE looking up the bracket.

### 11.5 Example 5 — LLC with C-corp election

**Facts:**
- Verdant Wellness LLC, single-member LLC organized in Georgia 2023, owned by an individual GA resident
- Elected to be taxed as a C-corp effective 1/1/2024 via Form 8832
- Operations 100% in Georgia
- Year-end balance sheet (12/31/2025):
  - Member's contribution (deemed paid-in capital): $250,000
  - No common stock issued (LLCs don't issue stock — but Form 8832 deems the entity a corporation)
  - Retained earnings (corporate-equivalent): $50,000
  - Total assets: $300,000
  - Total liabilities: $0

**Treatment of LLC capital:**
- LLCs don't have "issued capital stock" in the corporate-law sense
- For GA net-worth-tax purposes, the entire member's capital contribution is treated as paid-in capital (Regulation 560-7-3-.05)
- The greater-of test still applies, but Base A typically equals total contributions and Base B equals contributions plus retained earnings — so Base B is usually larger

**Computation:**
- Base A = $0 (capital stock) + $250,000 (paid-in capital from member contribution) = $250,000
- Base B = $300,000
- Greater of A or B = **$300,000**
- Apportionment: 100%

**Look up the bracket** in Section 7: $200,001 to $300,000 → **$200 net worth tax**

**Result:** Verdant Wellness LLC files Form 600 (NOT Form 1065 or Schedule C) and owes $200 net worth tax. The Form 8832 election locks the LLC into corporate treatment until revoked (60-month rule under federal regulations).

### 11.6 Example 6 — Dormant corporation

**Facts:**
- Riverside Properties Inc., Georgia C-corp incorporated 2015
- No operations since 2022
- Has not been formally dissolved with the Secretary of State
- Year-end balance sheet (12/31/2025):
  - All previous assets distributed
  - Total assets: $0
  - Total liabilities: $0
  - Common stock issued: $1,000
  - Paid-in capital: $9,000

**Computation:**
- Base A = $1,000 + $9,000 = $10,000
- Base B = $0
- Greater of A or B = **$10,000**
- Apportionment: N/A (no activity, default 100% to GA as domiciliary)

**Look up the bracket:** $0 to $10,000 → **$10 net worth tax**

**Result:** Riverside owes $10 minimum net worth tax. It must continue filing annually until formally dissolved. Failure to file triggers 5%/month penalty (although applied to $10, the absolute dollar penalty is small — but the DOR can suspend the corporation's "good standing" and refer to the Secretary of State for administrative dissolution, which has downstream consequences for any creditor pursuing the dissolved entity).

**Recommendation:** advise client to file Articles of Dissolution with the Secretary of State AND file a final Form 600 (marked "Final Return") to end the obligation cleanly.

## 12. Common Errors and Audit Flash Points (Consolidated)

1. [FLASH] S-corp owners assuming no entity-level GA tax. S-corps absolutely owe net worth tax. The S-election is federal only. See Section 4.3 and Example 3.

2. [FLASH] Foreign corporations forgetting the obligation after closing GA operations. Registration creates a perpetual filing duty until formal withdrawal. See Section 4.2.

3. [FLASH] Missing apportionment for multistate corporations. Defaulting to 100% GA on a multistate entity routinely overstates the tax — especially because the cap kicks in only after $22M apportioned. A 5% GA apportionment factor on a $100M net-worth corp produces $5M apportioned → $1,250 bracket, not the $5,000 cap. See Section 6.4 and Example 4.

4. Forgetting to compute Base A. Defaulting to Base B (net worth) without computing Base A (capital stock + paid-in capital) understates tax for any corporation with accumulated deficit. See Example 2.

5. Pro-rating for short period. The tax is NOT pro-rated for a short first period or a short final period. Each filing period generates a full bracket-based tax. See Section 7.5.

6. Failing to file a final return. Dissolved corporations that don't file a final return continue accumulating $10 minimum tax + penalties indefinitely. See Section 9.4.

7. Computing net worth at a date other than fiscal year-end. The balance sheet date is the LAST day of the corporation's tax year — not a quarter-end, not the date estimated payments are due. See Section 5.5.

8. LLCs that elected corporate treatment treating "no stock" as "no paid-in capital." Member contributions ARE paid-in capital for net worth purposes once the LLC is taxed as a corporation. See Example 5.

9. Treating intercompany payables as reducing net worth. Intercompany debt between affiliates is still a liability for net worth purposes (no consolidated reporting for GA net worth tax). However, the receivable on the related affiliate's balance sheet is still an asset. Net effect across the group is positive — but each entity files separately.

10. Bracket cliff failures. Year-end planning to drop below a bracket boundary saves bracket differential (e.g., $250 by going from $1,000,001 to $1,000,000). Worth doing when on the cliff.

## 13. Skill Output

When this skill is invoked, produce a reviewer-ready package containing:

1. Net Worth Tax Computation Worksheet (Section 5/7 above) — showing both Base A and Base B, the greater-of selection, the apportionment factor, the apportioned net worth, the bracket, and the resulting tax.

2. Form 600 Part II (or Form 600S Part III) line-by-line entries — ready to be transcribed onto the return or imported into preparation software.

3. Estimated Tax Analysis — does combined liability exceed $500? If yes, generate Form 602-ES schedule for the following year.

4. Penalty Analysis (if late) — late filing, late payment, interest, and total.

5. Reviewer Brief — one-page summary citing:
   - O.C.G.A. § 48-13-72 (base computation)
   - O.C.G.A. § 48-13-75 (apportionment)
   - O.C.G.A. § 48-13-76 (rate schedule)
   - Form 600 instructions (2025) page reference
   - Any audit flash points triggered

6. Open Questions / Reviewer Decisions — anything where the conservative-defaults principle was invoked, or where the reviewer must confirm a position before filing.

## 14. Skill Boundaries — What This Skill Does NOT Do

- **Out-of-scope items and dependencies** — This skill does not: - Compute Georgia corporate income tax (Form 600 Part I) — load `us-ga-corporate-income-tax` (or equivalent) alongside - Handle the Georgia PTET (pass-through entity tax) election under HB 149 — separate skill - Handle multistate income tax apportionment computations beyond consuming the GA factor produced by the income tax skill - Compute net worth tax for insurance companies (subject to premium tax in lieu under O.C.G.A. § 33-8-4) - Handle financial institutions (Georgia Financial Institutions Business Occupation Tax under O.C.G.A. § 48-6-93) - Handle public utility companies (gross receipts tax in lieu) - Handle nonprofits exempt under § 48-13-73 (these are net-worth-tax-exempt but may still file Form 600-T for UBIT — separate concern) - Handle voluntary withdrawal mechanics with the Georgia Secretary of State (refer to corporate counsel) - Handle administrative dissolution proceedings (refer to corporate counsel) - Provide opinion on whether a foreign entity has nexus sufficient to require GA registration in the first place (separate nexus skill needed) - Cover prior tax years before 2018 (rate schedule was different — do not apply the current table) MUST be loaded alongside `us-tax-workflow-base` v0.2 or later for workflow scaffolding.  _(O.C.G.A. § 33-8-4; O.C.G.A. § 48-6-93; O.C.G.A. § 48-13-73)_

## 15. Conservative Defaults

- **Default positions when facts unclear** — Where the facts are unclear, this skill applies conservative defaults: - If apportionment data is missing or incomplete, default to 100% Georgia (overstates tax — safer for filing posture). - If Base A vs Base B is borderline, compute both fully and use the larger (statutorily required). - If estimated payments may or may not be required (combined liability near $500), recommend filing estimates (avoids penalty exposure for de minimis savings). - If a balance sheet item is ambiguous (e.g., shareholder loan vs. capital contribution), default to capital contribution (increases base — conservative for filing). - If a foreign entity's GA registration status is unclear, default to "subject to net worth tax" and recommend client confirm with the Secretary of State. The reviewer must override these defaults explicitly with documented support for any aggressive position.

## 16. Reviewer Sign-Off Required

- **Sign-off requirement** — Every output of this skill requires sign-off by a Circular 230-credentialed reviewer (Enrolled Agent, CPA, or attorney) before filing. Georgia-specific sign-off should come from a reviewer with current Georgia experience — the bracket cliffs, apportionment subtleties, and the dual-base computation are easy to misapply without local familiarity. Per the verification model, Georgia state-tax outputs require the Georgia lead accountant or a contributor accountant sign-off in addition to the general federal reviewer.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
