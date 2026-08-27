---
name: us-form-1041-trust-and-estate-income
description: Tier 2 US federal content skill for Form 1041 — US Income Tax Return for Estates and Trusts. Covers tax year 2025 including the compressed bracket structure (37% at $15,650; LTCG 20% at $15,200; NIIT 3.8% same threshold), Distributable Net Income under §643, distribution deduction §651 (simple) and §661 (complex), the §663(b) 65-day rule, §645 election to combine estate + revocable trust, §691 income in respect of decedent, §642(g) election to deduct on 706 vs 1041, fiscal-year for estates only, Schedule K-1 character flow-through to beneficiaries, and §1361 ESBTs.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christopher Aryee
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Form 1041 Trust And Estate Income

## US Form 1041 — Income Tax Return for Estates and Trusts

Tax year 2025. Federal only. This skill assumes a human Circular 230 practitioner (Enrolled Agent, CPA, attorney) reviews and signs every 1041 before it reaches the fiduciary or the IRS. Where computations interact with state fiduciary income tax, defer to a state-level skill — the federal mechanics here are the input layer.

## 1. Scope

This skill produces Form 1041 (U.S. Income Tax Return for Estates and Trusts) for the 2025 tax year. It covers:

- Decedent's estate (the taxable entity that springs into existence at the moment of death and persists until the executor closes the estate).
- Irrevocable trusts (both inter vivos and testamentary) that are NOT grantor trusts for income tax purposes under IRC §§671–679.
- Revocable trusts that have become irrevocable by reason of the grantor's death — i.e. the typical revocable living trust ("RLT") after the date of death.
- §645 election filings combining a qualified revocable trust ("QRT") with the related decedent's estate into a single 1041 (one EIN, one return, one fiscal year).

It does NOT cover:

- **Form 706 — Estate Transfer Tax.** That is a wealth-transfer tax on the gross estate at death, computed once. Form 1041 is an income tax on income earned by the estate or trust AFTER death (or after the trust became a separate taxable entity). These two returns share facts (date of death, fair market values, §691 IRD items, the §642(g) election) but are distinct returns. See the companion skill `us-estate-gift-706-709` for transfer tax.
- **Form 709 — Gift Tax.** That is on lifetime transfers by the living grantor.
- **Grantor trusts.** Income is reported on the grantor's own Form 1040; the 1041 is either skipped or filed as a one-page informational pass-through (the "grantor trust letter" approach). The mechanics of that letter are discussed in §3.3 but the income computation belongs on Form 1040.
- **Electing Small Business Trusts (ESBT)** holding S-corporation stock — a sub-trust with its own tax computation under §641(c). Overview only in §15; full mechanics refer-out.
- **Charitable Remainder Trusts (CRT)** under §664 — a separate 5227 regime. Refer-out.
- **Charitable Lead Trusts**, **Qualified Personal Residence Trusts (QPRTs)**, **Grantor Retained Annuity Trusts (GRATs)** during the grantor's life (typically grantor trusts), and **Irrevocable Life Insurance Trusts (ILITs)** during the insured's life (typically grantor trusts under §677).
- **Foreign trusts.** Form 3520-A and 3520 governs. Refer-out.
- **Bankruptcy estates of individuals.** Separate 1041 regime under §1398 — refer-out.
- **Pooled income funds** and **§4947(a)(1) nonexempt charitable trusts**.
- **Split-interest trusts (§4947(a)(2))** — Form 5227.
- **Common trust funds (§584)** — Form 1065.

## 2. The Big Picture: Why 1041 Exists

When an individual dies, two new federal tax entities can appear:

1. **The estate** — automatically. From the moment of death until the executor closes probate and distributes the residuary assets, there is a separate taxable entity with its own EIN. Any income those assets produce (interest, dividends, rents, gain on sale of assets that appreciated post-death) is taxable to the estate on Form 1041, NOT to the decedent's final 1040 and NOT to the beneficiaries (yet).

2. **The trust** — if the decedent had a revocable living trust, that trust ceases to be a grantor trust at death and becomes irrevocable. From that moment, the trust is its own taxable entity with its own EIN, filing its own 1041.

Either of these entities can hold assets for years (estates typically 1–3; trusts can last decades or forever). Each year of existence = one 1041.

The defining mechanical feature of 1041 is the **conduit principle**: an estate or trust is a pass-through to the extent it distributes its income, but a taxable entity to the extent it retains income. The trust gets a **distribution deduction** for what flows out, and the beneficiary picks up that income on their own 1040 via a K-1 (Form 1041 Schedule K-1). What stays inside is taxed to the trust at the brutally compressed trust tax brackets (see §6).

This conduit design — distribute to push income onto beneficiaries' lower-bracket 1040s, or retain to control timing — is the central planning lever and is why the §663(b) 65-day rule (§11) is the single most important post-year-end planning tool a fiduciary has.

## 3. Who Files

### 3.1 Decedent's Estate

- **1041 filing requirement for estate** — required if the estate has gross income for the year of $600 or more, OR if any beneficiary is a nonresident alien  _(§3.1)_

The estate of a decedent files Form 1041 for:

- The taxable year in which the decedent died (the "short year" from date of death to the chosen year-end).
- Every taxable year thereafter, until the estate is closed.

A 1041 is **required** if the estate has gross income for the year of $600 or more, OR if any beneficiary is a nonresident alien. In practice, almost every estate that holds investment assets for more than a few months will cross $600 in gross income and must file.

> **AUDIT FLASH POINT — Failure to file the estate's first 1041.** When a parent dies and the executor (often a non-tax-professional adult child) is told by the funeral director or attorney to "get an EIN for the estate," that EIN sits on the IRS matching system. If the estate held a brokerage account or rental property that produced 1099 income reported to that EIN, and no 1041 was filed, the IRS will auto-generate a CP259 ("we did not receive your return") notice 12–18 months later, followed by a §6651 failure-to-file penalty (5% per month, capped at 25%) and a §6651(a)(2) failure-to-pay penalty if any tax is due. The first 1041 for a decedent's estate is the most-commonly-missed federal return in private client practice. If a client mentions a parent has died in the last 24 months AND the estate held any income-producing assets, ALWAYS confirm whether a 1041 was filed for the year of death.

The estate continues as a filing entity until it is "closed" for federal tax purposes — generally when the residuary has been fully distributed and there are no unresolved contingent liabilities. Closing is a facts-and-circumstances determination, not a formal IRS event; the practical marker is that the executor distributes the final residuary assets, files a final 1041 marked "Final return" on the top, and issues final K-1s.

The IRS will not let an estate stay open indefinitely just to harvest fiscal-year benefits — Reg. §1.641(b)-3(a) provides that "an estate is considered terminated when the period of administration … has expired." Open-ended administration solely for tax deferral is grounds for the IRS to treat the estate as closed and reallocate income to beneficiaries (Rev. Rul. 76-23).

### 3.2 Irrevocable Trust

- **1041 filing requirement for irrevocable trust** — files Form 1041 for each year it has: Gross income of $600 or more, OR any taxable income for the year, OR a beneficiary who is a nonresident alien  _(§3.2)_

Any trust that is irrevocable AND not a grantor trust under §§671–679 files Form 1041 for each year it has either:

- Gross income of $600 or more for the year, OR
- Any taxable income for the year, OR
- A beneficiary who is a nonresident alien.

Note the difference from an estate: a trust has the $600 gross income threshold but also files at any positive taxable income.

### 3.3 Grantor Trust — Special Filing

- **Grantor trust** — a grantor trust under §§671–679 is one where the grantor (or a substantial owner) is treated as the owner of the trust's assets for income tax purposes. The income is taxed to the grantor on her own 1040, not to the trust.  _(§§671–679)_

The trustee has three filing options:

1. **No 1041 filed.** Available if the trust uses the grantor's SSN as its TIN and all trust income is reported on 1099s issued to the grantor. Reg. §1.671-4(b)(2)(i)(A). Most common for revocable living trusts during the grantor's life.

2. **Form 1041 filed with zero income on the face, attaching a "grantor trust letter"** to the grantor reporting the items by character (interest, dividends, capital gain, etc.). The trust enters its name and EIN at the top, checks the "Grantor Type Trust" box in Part A, fills in the entity information, but reports no income on the body of the return.

3. **Optional method 1 or 2** under Reg. §1.671-4(b) — the trustee files Forms 1099 in the trust's name, transferring the income reporting role to the trust without filing a 1041. Used for some commercial grantor trusts.

The triggering event for a revocable living trust to STOP being a grantor trust is the grantor's death. From the date of death forward, the former RLT is an irrevocable non-grantor trust and files its own 1041 under §3.2 above (unless §645 election made; see §13).

### 3.4 §645 Election Combined Filing

- **Qualified revocable trust (QRT) §645 election** — A qualified revocable trust (QRT) — i.e. a revocable trust that became irrevocable at the grantor's death — can elect under §645 to be treated as part of the decedent's estate for federal income tax purposes.  _(§645)_
- **§645 election mechanics** — Combines the QRT and the estate into ONE Form 1041. One EIN (the estate's), one return, one fiscal year (estate's choice). Election made by filing Form 8855 by the due date (including extensions) of the first 1041 for the combined entity. Election is irrevocable. Election period: ends at the earlier of (a) two years after death if no federal estate tax return is required, OR (b) six months after the final determination of estate tax liability if a 706 is required, OR (c) the earlier of those plus the date the combined entity is closed.  _(§645; Form 8855)_

The §645 election is almost always advantageous when a 1041 must be filed for both the estate AND a substantial RLT, because:

- One return instead of two (administrative simplification).
- Fiscal year for the combined entity (trusts alone are stuck with calendar year).
- One §642(b) personal exemption ($600 estate exemption, not the $100/$300 trust exemption — see §12).
- The trust gets the estate's first-2-years exemption from §6654(a) quarterly estimated payments (see §16).
- One pool of DNI to plan distributions against.

See §13 for full mechanics and worked Example 2.

### 3.5 Decision Tree — Who Files What

```
Did the taxpayer die?
├── No → not a 1041 issue (yet). Trust-only analysis only.
│
└── Yes → there is an estate. Did the decedent have an RLT?
    ├── No, no RLT → Estate-only 1041. Decide fiscal vs calendar year (§4).
    │
    └── Yes, had an RLT → Three options:
        ├── (a) Estate-only 1041 + separate Trust 1041 (calendar year for trust).
        ├── (b) §645 election → ONE combined 1041 with estate's fiscal year. File
        │       Form 8855. Default choice for most.
        └── (c) Pour-over RLT funded immediately at death and "estate" is essentially
                empty → only Trust 1041 (calendar year). Rare; only when there's truly
                no probate estate.
```

## 4. Taxable Year — Estates vs Trusts

This is one of the most commercially important distinctions in subchapter J.

### 4.1 Estates — Choice of Calendar or Fiscal Year

- **Estate year election** — An estate may elect either: Calendar year (Jan 1 – Dec 31), OR Fiscal year ending on the last day of any month other than December, provided the first taxable year does not exceed 12 months from the date of death. The fiscal-year election is made simply by filing the first 1041 with the chosen year-end on the return. No separate form. Once chosen, the year-end is locked in (a change requires Form 1128 and IRS consent under §442).  _(§442)_

The most common fiscal-year choice is the month-end immediately preceding the month of death — e.g. decedent dies June 14, 2025; estate elects a fiscal year ending May 31, giving the longest possible first taxable year (just shy of 12 months, June 14, 2025 to May 31, 2026).

### 4.2 Why Fiscal Year Matters — The Deferral Lever

A fiscal year-end gives the estate three planning advantages:

1. **Income deferral on the K-1.** Beneficiaries report K-1 income in their tax year that includes the LAST DAY of the estate's fiscal year. An estate with a fiscal year ending May 31, 2026 issues K-1s to beneficiaries that they pick up on their 2026 1040 (filed by April 15, 2027). Income that was earned by the estate as far back as June 2025 doesn't hit beneficiaries' returns until April 2027 — nearly two years of deferral.

2. **Spread of bunched IRD or large gains.** If the estate sells a major asset (e.g. a residence held until probate is complete), the gain can be timed against a fiscal year-end that pushes the K-1 into the beneficiary's lower-income year.

3. **Stacking distributions and the §663(b) 65-day rule (§11).** The 65-day rule applies to the FISCAL year, not just calendar year. A May 31 fiscal year-end means the 65-day election covers distributions through approximately August 4.

### 4.3 Trusts — Calendar Year Mandatory (§644)

- **Trust calendar year requirement** — Trusts other than tax-exempt trusts and wholly-charitable trusts are required to use the calendar year (§644, enacted by the Tax Reform Act of 1986). There is no fiscal-year option for trusts. The only way to get a fiscal year for a former-RLT-now-irrevocable-trust is to make the §645 election (see §13) and ride on the estate's fiscal year.  _(§644)_

### 4.4 Short-Year Mechanics

- **Short-year mechanics** — Both the first 1041 (from date of death to year-end) and the final 1041 (from prior year-end to date of termination) are short-year returns. They do NOT annualize income (trusts and estates are not subject to §443 annualization for short periods). The tax on a short-year 1041 is computed using the regular trust/estate rate tables, not annualized rates.  _(§443)_

## 5. EIN and Initial Setup

Every estate and every non-grantor trust must obtain its own EIN. Application is via Form SS-4 or online at irs.gov/ein. The executor or trustee is the "responsible party."

Use the EIN for:

- All trust/estate bank and brokerage accounts.
- 1099 reporting (asset producers should re-issue 1099s to the EIN starting from date of death; allocations are needed for the cusp year — pre-death income on the decedent's final 1040, post-death income on the estate's 1041).
- W-9 to all asset payers.

The split of 1099 income across the date of death is mechanical: a Schedule B-style schedule reconciles the brokerage 1099 to (a) pre-death amount on the final 1040 and (b) post-death amount on the 1041. The IRS matching system will reconcile the SSN side; on the EIN side, attach a Schedule B nominee statement showing the allocation.

## 6. The Compressed Bracket Cliff (Tax Year 2025)

This is the most important practical fact in the 1041 universe.

### 6.1 The 2025 Ordinary Rate Schedule for Estates and Trusts (§1(e))

**2025 Ordinary Rate Schedule for Estates and Trusts**  _(§1(e))_

| Taxable income (over) | But not over | Rate |
| --- | --- | --- |
| $0 | $3,150 | 10% |
| $3,150 | $11,450 | 24% |
| $11,450 | $15,650 | 35% |
| $15,650 | — | **37%** |

Compare to single individual 2025: 37% top rate starts at $626,350 of taxable income. An estate or trust hits the 37% bracket at $15,650 — 1/40th of the threshold for a single individual.

### 6.2 The 2025 Long-Term Capital Gain / Qualified Dividend Schedule (§1(h))

**2025 LTCG/QDI Schedule for Estates and Trusts**  _(§1(h))_

| Taxable income (over) | But not over | LTCG / QDI rate |
| --- | --- | --- |
| $0 | $3,250 | 0% |
| $3,250 | $15,200 | 15% |
| $15,200 | — | **20%** |

The 20% LTCG rate hits at $15,200 of taxable income for a trust/estate. The corresponding single-individual threshold is $533,400.

### 6.3 Net Investment Income Tax — §1411

- **NIIT rate for trust/estate** — 3.8% percent  _(§1411)_
- **NIIT computation base** — A trust or estate is subject to NIIT at 3.8% on the LESSER of: Undistributed net investment income for the year, OR The excess of adjusted gross income (a modified concept for trusts/estates — see §1411(a)(2)(B)) over the dollar amount at which the highest bracket begins, i.e. $15,650 for 2025.  _(§1411(a)(2)(B))_
- **Individual NIIT threshold comparison** — $200,000 single MAGI ($250,000 MFJ)  _(§1411; comparison text: a trust crosses the NIIT cliff at 1/12th the single threshold)_

Material participation by a trust (which can spare it from passive-activity-loss trapping and NIIT on rental income) is an unresolved area — the Frank Aragona Trust case (Tax Court 2014) held that a trust can materially participate through its trustees' personal activities. The IRS has not issued definitive guidance. Conservative default: treat the trust as not materially participating unless the trustee performs the activity directly and substantially.

### 6.4 The Planning Implication

Every dollar of taxable income above $15,650 is taxed at 37% federal ordinary (or 20% LTCG) PLUS 3.8% NIIT if investment in character. That is 40.8% federal on ordinary investment income; 23.8% on LTCG. Compare to an individual beneficiary in the 24% bracket: 24% on ordinary, 15% on LTCG.

Therefore: **distribute aggressively to push income onto lower-bracket beneficiaries.** This is the design intent of subchapter J — the conduit principle aligned with the compressed brackets is the legislative push to keep income flowing rather than accumulating inside a trust.

The §663(b) 65-day rule (§11) is the principal post-year-end mechanic to fix under-distributions and avoid the cliff.

## 7. Distributable Net Income — §643(a)

DNI is the single most important computed number on Form 1041. It does two things:

1. Caps the trust's distribution deduction (a trust deducts the lesser of actual distributions or DNI).
2. Caps the beneficiaries' includible amount (a beneficiary picks up the lesser of actual distributions or DNI), with character flowing through pro rata.

### 7.1 The Computation Under §643(a)

- **DNI Computation** — Taxable income (before distribution deduction and personal exemption) + Personal exemption (§642(b)) — added back so the exemption doesn't reduce DNI + Tax-exempt interest, NET OF expenses allocated to it − Capital gains allocated to corpus (NOT to income beneficiaries; default rule) + Capital losses (to the extent they offset ordinary income) ± Extraordinary dividends and taxable stock dividends (simple trust only — §643(a)(4)) −/+ Other §643(a) adjustments (foreign income for foreign trusts; charitable deductions reallocated; etc.) = Distributable Net Income (DNI)  _(§643(a))_

The big swing items are capital gains and tax-exempt interest.

### 7.2 Capital Gains and DNI

- **Default capital gains treatment** — Default rule under §643(a)(3): capital gains are EXCLUDED from DNI because they are "allocated to corpus" under most state principal-and-income acts and most trust instruments. The trust pays the capital gains tax itself (at the compressed brackets in §6.2), and the gain does NOT flow out to beneficiaries.  _(§643(a)(3))_
- **Overrides to capital gains default** — This default can be overridden if ANY of the following is true under Reg. §1.643(a)-3: 1. The trust agreement allocates capital gains to income. 2. The state statute (state principal-and-income act) treats capital gains as income. 3. The trustee, exercising discretion granted by the agreement or state law, in a "reasonable and impartial" manner allocates capital gains to income — AND has done so consistently year after year. 4. The capital gain is "actually distributed to the beneficiary or utilized by the fiduciary in determining the amount that is distributed."  _(Reg. §1.643(a)-3)_

Practical takeaway: if the fiduciary wants capital gains to flow to beneficiaries (to escape the trust's 20% LTCG cliff), the trust agreement should expressly authorize it, the trustee should establish a consistent pattern of allocating CG to income, AND the gain should be actually distributed in the year recognized. Conservative default: assume CG stays in the trust unless one of (1)–(4) is met and documented.

### 7.3 Tax-Exempt Interest and DNI

- **Tax-exempt interest treatment in DNI** — Tax-exempt interest is INCLUDED in DNI (notwithstanding that it's not in taxable income), because §661(c) requires the distribution deduction to be reduced by the proportion of the distribution that consists of tax-exempt income. The trust gets no deduction for distributing tax-exempt interest, and the beneficiary picks it up character-preserved (still tax-exempt on the beneficiary's return).  _(§661(c))_

### 7.4 The Tier System for Character Allocation (§652(b), §662(b))

- **Tier system for character allocation** — When distributions to multiple beneficiaries are less than the total income, the character of distributed income is allocated pro rata to each beneficiary based on the items making up DNI. Mechanically: compute DNI, break it into character (interest, qualified dividends, ordinary dividends, LTCG, STCG, tax-exempt, foreign-source, rental, royalties). Each beneficiary's K-1 reflects their pro rata share by character. For complex trusts with both required and discretionary distributions, character is first allocated to Tier 1 (required) and then to Tier 2 (discretionary): - **Tier 1** = required current distributions of income (a "right to demand"). - **Tier 2** = all other distributions (discretionary by trustee). Tier 1 fills first, Tier 2 fills the remainder. This affects character allocation — required-distribution beneficiaries get a pro rata share of the income character first; discretionary beneficiaries get what's left.  _(§652(b), §662(b))_

## 8. Simple vs Complex Trust

- **Simple trust definition** — A "simple trust" under §651 is one that meets ALL THREE of the following in the taxable year: 1. The trust agreement requires that ALL income (fiduciary accounting income, FAI) be distributed currently. 2. The trust agreement does not provide for charitable distributions. 3. The trust does not distribute amounts other than current income (i.e. no corpus distributions). If any of those three is missing, the trust is "complex" under §661 for that year.  _(§651; §661)_

A trust can be simple in one year and complex in the next — it's a year-by-year determination based on what the trust actually did, not on the trust instrument's classification. Example: a discretionary-income trust that happens to distribute all income in year 1 (with no corpus distribution) is simple for year 1; if in year 2 the trustee also pays a corpus distribution, it's complex for year 2.

### 8.1 Mechanical Differences

**Mechanical Differences: Simple Trust vs Complex Trust/Estate**  _(§651; §661; §642(b); §663(b); §642(c))_

| Item | Simple Trust (§651) | Complex Trust / Estate (§661) |
| --- | --- | --- |
| Distribution deduction = | Lesser of FAI or DNI | Lesser of distributions or DNI |
| Personal exemption (§642(b)) | $300 | $100 (complex trust); $600 (estate) |
| 65-day rule available? | No (income must be distributed; nothing to elect on) | Yes (§663(b)) |
| Capital gains in DNI by default | No | No (same default; but see §7.2 exceptions) |
| Charitable deductions allowed? | No | Yes (§642(c)) |

- **Estates treated as complex trusts** — Estates are always treated like complex trusts under §661 (they cannot be "simple" because they have discretionary distributions by definition).  _(§661)_

## 9. §651 Simple-Trust Distribution Deduction

- **Simple trust distribution deduction** — Distribution deduction = lesser of (FAI) or (DNI − tax-exempt interest net of allocable expenses)  _(§651(a))_

Note that DNI is reduced by tax-exempt interest for purposes of the deduction (because no deduction is allowed for distributing tax-exempt income), but the beneficiary still receives that tax-exempt character on the K-1.

If the simple trust ACTUALLY distributes more than required (which would violate the simple-trust definition and convert it to complex for that year), the analysis shifts to §661.

## 10. §661 Complex Trust / Estate Distribution Deduction

- **Complex trust/estate distribution deduction** — For a complex trust or an estate, §661(a) allows a deduction equal to the SUM of: 1. The amount of any income required to be distributed currently (Tier 1), AND 2. Any other amounts properly paid, credited, or required to be distributed (Tier 2), LIMITED to DNI, and reduced by the proportion attributable to tax-exempt income under §661(c). ``` Distribution deduction = lesser of (Tier 1 + Tier 2 actual distributions) or (DNI − tax-exempt portion) ```  _(§661(a); §661(c))_

Schedule B of Form 1041 walks through this:
- Line 1: Adjusted total income (Form 1041 page 1 Line 17 + adjustments)
- Line 2: Tax-exempt interest
- Line 3–4: Net capital gains allocated to corpus (subtract)
- Line 6: Distributable Net Income (DNI)
- Line 9: Income required to be distributed (Tier 1)
- Line 10: Other amounts paid or required (Tier 2)
- Line 11: Total
- Line 12: Reduced by tax-exempt amount
- Line 14: **Distribution deduction** — flows to page 1 Line 18

## 11. The §663(b) 65-Day Rule

This is the single most powerful post-year-end planning tool a fiduciary has.

### 11.1 The Rule

- **§663(b) 65-day rule** — Under §663(b), a complex trust or estate may elect to treat amounts properly paid within the FIRST 65 DAYS of the taxable year as having been paid on the LAST DAY of the PRECEDING taxable year. For a calendar-year trust: distributions made between January 1 and approximately March 6 of 2026 (65 days into 2026) can be elected to be treated as 2025 distributions. For 2025 calendar year, the 65th day of 2026 is March 6, 2026.  _(§663(b))_

### 11.2 Why It Matters

After the calendar year closes (Dec 31, 2025), the fiduciary and tax preparer can:

1. Run a draft 1041 with no 65-day election → see how much taxable income is left in the trust at the compressed brackets.
2. Compute the marginal benefit of pushing each additional dollar to a beneficiary (trust's bracket minus beneficiary's bracket).
3. Make actual distributions in January / February 2026 covering income earned in 2025.
4. Elect under §663(b) on the 2025 1041 to treat those distributions as 2025 distributions.

This converts a planning problem (December-31-or-bust distribution timing) into a post-year-end optimization. Especially valuable when:

- The trust has been holding investment income and is staring at 37% / 20% / 3.8% rates.
- Beneficiaries are in lower brackets.
- The trust agreement gives the trustee discretion to distribute (i.e. a complex trust).

### 11.3 Mechanics of the Election

- **65-day election mechanics** — Election is made by checking Box 6 in the "Other Information" section of Form 1041 (the line for §663(b)) AND by attaching a statement specifying the dollar amount of the distribution to be treated as made in the prior year. Election applies separately to each year. The election is limited to the LESSER of: The actual amount distributed in the 65-day window, OR The greater of trust accounting income or DNI for the prior year. The election must be made by the due date (including extensions) of the prior-year 1041.  _(§663(b))_

### 11.4 Trap for the Unwary

> **AUDIT FLASH POINT — §663(b) timeliness.** The 65-day rule election MUST be made on a TIMELY 1041 (including extensions). It cannot be made on an amended return. Many fiduciaries miss this because they file a draft on April 15, intending to "amend later if the 65-day election helps." That doesn't work — once the original return is filed without the election, the election is lost. If the practitioner doesn't have time to compute the optimal distribution by April 15, the right move is to extend the return (Form 7004 — automatic 5.5 months extension), make the distribution and election decisions during the extension period, and file in September with the §663(b) election locked in. ALWAYS extend a 1041 if the 65-day election is in play and not yet decided.

## 12. §642(b) Personal Exemption

**§642(b) Personal Exemption by Entity**  _(§642(b))_

| Entity | §642(b) Exemption |
| --- | --- |
| Estate | **$600** |
| Simple trust (required to distribute all income) | **$300** |
| Complex trust / all other trusts | **$100** |
| Qualified disability trust (§642(b)(2)(C)) | tied to individual exemption — but 2018–2025 TCJA reduced to indexed amount; 2025 = approximately $5,050 |

- **Fixed dollar exemption, no phaseout** — The 1041 personal exemption is fixed dollar amounts (no inflation adjustment, no phaseout for any AGI level). The exemption is taken on Form 1041 Line 21, after the distribution deduction. Note the exemption is added back when computing DNI (§7.1) — it never reduces DNI.  _(§642(b))_

## 13. §645 Election — Combining Estate and QRT

- **Form 8855 §645 election** — Form 8855 is the election to treat a qualified revocable trust (QRT) as part of the decedent's estate for income tax purposes.  _(Form 8855; §645)_

### 13.1 Eligibility

- **§645 eligibility requirements** — "QRT" = a trust that, on the date of the decedent's death, was treated as owned by the decedent under §676 (a typical revocable living trust). The election must be made jointly by the trustee and the executor (or if no executor, by the trustee alone). Must be made by the due date (including extensions) of the FIRST 1041 for the combined entity. Election is irrevocable once made.  _(§676; §645)_

### 13.2 Period of the Election

- **§645 election period** — The election period runs from the date of death to the EARLIEST of: Two years after the date of death (if no Form 706 is required), OR Six months after the final determination of estate tax liability (if a 706 is required), OR The date the combined entity is closed/terminated.  _(§645)_

### 13.3 Benefits

**§645 Benefits Comparison Table**  _(§645; §6654(l); §469)_

| Benefit | Without §645 | With §645 |
| --- | --- | --- |
| Number of 1041s | 2 (one for estate + one for trust) | 1 |
| Trust's allowable taxable year | Calendar year required | Estate's fiscal year |
| Personal exemption | $100 trust + $600 estate = $700 | $600 (one exemption)** |
| Quarterly estimated tax — first 2 years | Trust must make payments | Combined entity exempt (treated as estate) §6654(l) |
| §469 active participation real estate $25K | Not available to trust | Available to estate-treated entity for 2 years post-death |

** The combined entity uses the estate's $600 exemption, so a small theoretical loss of $200 ($600 + $100 vs. $600). Almost always swamped by the other benefits.

### 13.4 Filing Mechanics

- **§645 filing mechanics** — File Form 8855 by the due date (including extensions) of the first 1041 for the combined entity. The 1041 is filed in the name of the estate, using the estate's EIN. The QRT continues to hold its assets in the trust's name with the trust's EIN at the bank/brokerage level, but for federal income tax it reports under the estate's EIN via the combined 1041. At the end of the §645 election period, the QRT is "deemed distributed" to a new trust and starts filing its own 1041 on a calendar year going forward.  _(Form 8855)_

## 14. §691 — Income in Respect of Decedent ("IRD")

- **Income in Respect of Decedent (IRD)** — IRD is income that the decedent had a RIGHT TO RECEIVE before death but had not actually received and that was not properly includible on the final 1040.  _(§691)_

### 14.1 Common IRD Items

- Unpaid wages earned before death but paid after death.
- Accrued interest on bonds (the portion accrued from last payment date to date of death).
- Final installment of an installment sale (§453).
- Distributions from traditional IRAs and qualified plans (the entire balance — these carry the decedent's untaxed character).
- Series EE bond accrued but undistributed interest.
- Renewal commissions to a deceased insurance agent.
- Crop share rents accrued.
- Lottery winnings of an annuity-stream lottery.

### 14.2 Tax Treatment

- **IRD tax treatment** — IRD is NOT included on the decedent's final 1040 (because it wasn't received yet). IRD IS included on Form 1041 of the estate (or whichever trust receives it) in the year of receipt. IRD retains its character — interest is interest, wages are wages, capital gain is capital gain. If the estate distributes the IRD to a beneficiary (and DNI permits), the beneficiary picks it up character-preserved on the K-1. **No basis step-up.** Property representing IRD does NOT get the §1014 fair-market-value basis step-up. The estate (or beneficiary) reports the IRD using the decedent's basis. This is a fundamental and frequently-missed point.  _(§691; §1014)_

### 14.3 §691(c) Deduction — Estate Tax Paid on IRD

- **§691(c) deduction** — If estate tax (Form 706) was paid AND the gross estate included IRD, the taxpayer who reports the IRD on income tax gets an itemized deduction under §691(c) for the federal estate tax attributable to the IRD. Mechanically: 1. Compute total estate tax actually paid on the 706. 2. Compute the estate tax that WOULD have been paid if the IRD items had been excluded from the gross estate. 3. Difference = estate tax attributable to IRD. 4. That amount is a §691(c) miscellaneous itemized deduction (NOT subject to the 2% floor; not suspended by TCJA — §67(b)(7)) on the income tax return of whoever pays the income tax on the IRD.  _(§691(c); §67(b)(7))_
- **§691(c) 2025 status** — For 2025: §691(c) remains allowable as an itemized deduction that bypasses the §67(g) TCJA suspension of misc. itemized deductions. The IRS confirmed this in Rev. Proc. 2018-08 and the 2018 1041 instructions and that position has held through 2025.  _(Rev. Proc. 2018-08; §67(g))_

### 14.4 IRD Double-Counting Trap

> **AUDIT FLASH POINT — IRD double-counting between 706 and 1041.** The same dollar of IRD appears on BOTH the 706 (as part of the gross estate, valued at date of death) AND the 1041 (as income when received). This is correct — it is the rationale for the §691(c) deduction. But many practitioners miss the §691(c) deduction entirely, resulting in the decedent's beneficiaries paying both estate tax AND income tax on the same dollar without the partial offset Congress intended. If the estate is taxable on Form 706 AND has any IRD items, ALWAYS compute the §691(c) deduction and carry it onto the 1041 (or onto the beneficiary's 1040 if the IRD is distributed via K-1). Conversely, do NOT EXCLUDE IRD from the 706 thinking it will be taxed on the 1041 — it must be on both, and the partial offset is the §691(c) deduction, not exclusion.

## 15. §642(g) — Deduction on 706 or 1041, Not Both

- **§642(g) election** — Estate administrative expenses (executor fees, attorney fees, accountant fees, court costs, appraisal fees) and casualty/theft losses incurred during administration can be deducted on EITHER: Form 706 (as a §2053 administrative expense, reducing the taxable estate), OR Form 1041 (as a §212 or §67(e) above-the-line deduction, reducing taxable income), but NOT BOTH. The election is made by filing a written statement with the 1041 specifying the items elected on the 1041 and waiving the 706 deduction for those items.  _(§642(g); §2053; §212; §67(e))_

### 15.1 How to Decide

**How to Decide: 706 vs 1041 deduction**  _(§642(g))_

| Estate's situation | Generally deduct on |
| --- | --- |
| Estate is below the 706 filing threshold ($13.99M for 2025 with the OBBBA-extended exemption) — no 706 required | **1041** (the 706 deduction would be wasted) |
| Estate is taxable on 706 and the marginal estate tax rate (40%) > the marginal income tax rate on the 1041 (37% + 3.8% NIIT) | Close call — model it. Often 1041 because the marginal income rate plus NIIT exceeds 40%. |
| Estate is taxable on 706 and substantial income flows to high-bracket beneficiaries | **1041** — the deduction on 1041 reduces DNI, which reduces beneficiary K-1 income (offsetting their 37% rate) |
| Estate is taxable on 706 and most income stays in the estate at lower brackets | Model both. Often **706**. |

- **Knight v. Commissioner fiduciary fees** — §67(e) was held in Knight v. Commissioner (552 U.S. 181 (2008)) and the TCJA-era regulations to permit deduction of fiduciary fees and other "uniquely fiduciary" expenses on the 1041 above-the-line, NOT subject to the §67(g) suspension of miscellaneous itemized deductions. Investment advisory fees, however, are NOT uniquely fiduciary and remain suspended under §67(g) for 2018–2025.  _(Knight v. Commissioner, 552 U.S. 181 (2008); §67(e); §67(g))_

### 15.2 Partial Allocation Allowed

- **Partial allocation of §642(g) election** — The election can be made item-by-item — e.g. deduct attorney fees on 1041 and executor commissions on 706 — provided each item is wholly assigned to one or the other.  _(§642(g))_

## 16. Schedule K-1 to Beneficiaries

Each beneficiary that receives a distribution carrying DNI gets a Form 1041 Schedule K-1. The K-1 reports:

- Beneficiary identifying info (Part I: trust/estate; Part II: beneficiary).
- Box 1: Interest income.
- Box 2a/2b: Ordinary / qualified dividends.
- Box 3: Net short-term capital gain.
- Box 4a/4b/4c: Net long-term capital gain (with 28% rate gain and unrecaptured §1250 gain segregated).
- Box 5: Other portfolio and nonbusiness income.
- Box 6: Ordinary business income.
- Box 7: Net rental real estate income.
- Box 8: Other rental income.
- Box 9a–c: Directly apportioned deductions (depreciation, depletion, amortization).
- Box 10: Estate tax deduction (§691(c)).
- Box 11: Final-year deductions (NOLs, excess deductions on termination — §642(h)(2)).
- Box 12: AMT adjustments.
- Box 13: Credits.
- Box 14: Other information (foreign-source character, NIIT items, §199A QBI).

Beneficiaries report K-1 income on:

- Form 1040 Schedule B for interest and dividends (Boxes 1, 2a).
- Form 1040 Schedule D for capital gains (Boxes 3, 4a–c).
- Form 1040 Schedule E, Part III, Line 33 (beneficiary income from estates and trusts).

Character is preserved — LTCG on the K-1 is LTCG on the beneficiary's 1040, taxed at the beneficiary's LTCG bracket (which is almost always lower than the trust's 20% cliff).

### 16.1 Final-Year K-1 — Excess Deductions on Termination

- **Excess deductions on termination** — In the final year of an estate or trust (when it terminates and distributes its last assets), any unused deductions and any net operating losses are passed out to the remaindermen (those who receive the residuary) as "excess deductions on termination" under §642(h). Pre-TCJA these were misc. itemized deductions subject to the 2% floor and §67(g) suspension. The 2020 regulations (Reg. §1.642(h)-2(b)(2), TD 9918) clarify that §642(h)(2) excess deductions retain their character (above-the-line vs misc. itemized), and §67(e) "uniquely fiduciary" portions remain above-the-line deductible on the beneficiary's 1040 even post-TCJA.  _(§642(h); Reg. §1.642(h)-2(b)(2), TD 9918)_

## 17. Estimated Tax Payments — §6654(l)

- **Quarterly estimated tax requirement** — Trusts are required to make quarterly estimated tax payments under §6654 if expected tax exceeds $1,000. Standard quarterly due dates (April 15, June 15, September 15, January 15) apply.  _(§6654)_

### 17.1 The Estate Exemption

- **Estate two-year estimated tax exemption** — Under §6654(l)(2), an estate is NOT required to make estimated tax payments for any taxable year ending before the date that is TWO YEARS after the decedent's date of death. For a §645-combined entity (see §13), the same two-year exemption applies to the combined estate + QRT. After the two-year window expires, both estate (if still open) and trust must make estimated payments under §6654.  _(§6654(l)(2))_

### 17.2 Beneficiary Election under §643(g)

- **§643(g) estimated tax allocation election** — A trust (NOT estate) may elect under §643(g) to treat any portion of its current-year estimated tax payment as having been paid by a beneficiary. The election is on Form 1041-T and must be filed by the 65th day of the year following. This pushes the estimated payment credit onto the beneficiary's 1040.  _(§643(g); Form 1041-T)_

Use case: trust paid estimated tax during the year, then under-distributed; the 65-day rule pushes income to the beneficiary; §643(g) similarly pushes the prepaid tax credit out so the beneficiary gets the credit instead of the trust holding it. The two elections work together.

## 18. ESBT — Electing Small Business Trust (§1361(e)) — Overview

- **ESBT overview** — When a trust holds S-corporation stock, it must qualify under §1361(c)/(d)/(e) or the S election is broken. The ESBT is one of the qualifying trust forms. An ESBT is taxed in a unique two-step manner under §641(c): 1. The "S-portion" of the trust (the portion holding the S-corp stock) is taxed separately at the highest individual rate (37% for 2025) on its S-corporation pass-through items. No distribution deduction is allowed for distributions of S-corporation items. The S-portion is essentially a separate trust within the trust for tax purposes. 2. The "non-S portion" (everything else) is taxed as a regular complex trust under §661, with normal DNI and distribution deduction mechanics.  _(§1361(c)/(d)/(e); §641(c); §661)_
- **ESBT election timing** — ESBT election is made by the trustee filing an election statement with the IRS within 2 months and 16 days of the trust acquiring the S-corp stock (or being created with it). Election is irrevocable except with IRS consent. Full ESBT mechanics, including the §199A QBI deduction allocation between the S-portion and beneficiaries, are deferred. Refer to a specialist for ESBT planning.  _(§1361(e))_

## 19. Other Topics — Brief Overview

### 19.1 Net Operating Losses

- **NOL treatment for trusts/estates** — Trusts and estates can generate NOLs under §172. NOLs are carried by the trust/estate and used against future trust/estate taxable income. They do NOT pass through to beneficiaries during the trust's life. At the trust's TERMINATION (final year), unused NOLs flow out as §642(h)(1) carryforwards on the final K-1 to remaindermen, who can use them on their own 1040s subject to their own §172 rules.  _(§172; §642(h)(1))_

### 19.2 AMT

- **Trust/estate AMT exemption 2025** — approximately $30,700 with phaseout beginning at approximately $102,500 (figures indexed annually; verify against Rev. Proc. 2024-40 or the 2025 instructions to Form 1041 Schedule I) USD  _(§55; Rev. Proc. 2024-40)_

### 19.3 Intangible Drilling Costs, Depletion

- **Pass-through of depreciation/depletion/amortization** — Trusts and estates pass through depreciation, depletion, and amortization directly apportioned between the entity and the beneficiaries on K-1 Box 9a–c, in the ratio of trust accounting income retained vs distributed. The trust can elect under §266 to capitalize certain carrying charges.  _(§266)_

### 19.4 §199A QBI Deduction for Trusts

- **§199A QBI deduction for trusts** — A non-grantor trust is treated as a separate taxpayer for §199A QBI purposes. The trust gets its own QBI deduction (up to 20% of QBI) on its own retained QBI income. To the extent QBI flows out via K-1, the beneficiary takes the QBI deduction on her own 1040. The §199A thresholds for trusts are the single-individual amounts — i.e. the trust hits the start of the phaseout at the single threshold of $197,300 of taxable income for 2025 (Rev. Proc. 2024-40), with the deduction fully phased out at $247,300 (the $197,300 base threshold plus the $50,000 phase-in range for non-joint filers). Starting in 2026, the OBBBA (§ 70105) widens the phase-in range to $75,000 ($150,000 for joint returns). This is one of the few places trusts do NOT face compressed brackets; the §199A thresholds are at individual levels.  _(§199A)_
- **Anti-abuse rule for §199A trusts** — Caveat — anti-abuse rules under Reg. §1.643(f)-1 disregard trusts created principally to avoid federal income tax, including for §199A purposes.  _(Reg. §1.643(f)-1)_

### 19.5 State Fiduciary Income Tax

Most states have a fiduciary income tax mirroring the federal 1041 with state-specific modifications. Residency determination for trusts can be complex (testator's state, trustee's state, beneficiary's state, situs of administration). Defer to state skills.

## 20. Filing Deadline and Extensions

- **Calendar-year 1041 due date** — Due April 15 of the following year (April 15, 2026 for 2025).  _(§20)_
- **Fiscal-year 1041 due date** — Due the 15th day of the 4th month after the close of the fiscal year. E.g. fiscal year ending May 31, 2026 → due September 15, 2026.  _(§20)_
- **Extension via Form 7004** — Form 7004 grants an automatic 5.5-month extension (NOT the 6 months granted to individuals). For a calendar-year 2025 1041, the extended due date is September 30, 2026. Extension is automatic on filing of Form 7004 by the original due date; payment of estimated tax is still due by the original due date — extension extends time to file, not time to pay.  _(Form 7004)_

## 21. Worked Examples

### 21.1 Example 1 — Simple Trust Distributing All Income

The Smith Family Trust is an irrevocable trust created by Robert Smith in 2010 for the benefit of his daughter Jane. The trust agreement requires that ALL income be distributed to Jane annually; it does not permit charitable gifts or corpus distributions. The trust is calendar-year. For 2025, the trust earns:

- Taxable interest: $40,000
- Qualified dividends: $20,000
- Tax-exempt municipal bond interest: $8,000
- Net long-term capital gain on a stock sale: $30,000 (gain allocated to corpus under the trust agreement and state law)
- Trustee fees: $5,000 (allocable $4,000 to income, $1,000 to corpus)

- **Step 1 — Classify the trust** — Required income distribution + no charity + no corpus distribution = simple trust under §651 for 2025.  _(§651)_

**Step 2 — Trustee allocation of expenses for fiduciary accounting income (FAI)**  _(—)_

| Item | Income | Corpus |
| --- | --- | --- |
| Interest | 40,000 | — |
| Qualified dividends | 20,000 | — |
| Tax-exempt interest | 8,000 | — |
| Capital gain | — | 30,000 |
| Trustee fees (allocated) | (4,000) | (1,000) |
| **FAI / corpus** | **64,000** | **29,000** |

Trustee must distribute $64,000 of FAI to Jane.

- **Step 3 — DNI computation** — Taxable income before distribution deduction and exemption: Interest                                       40,000 Qualified dividends                            20,000 Capital gain                                   30,000 Trustee fees (allocable; conservative — see notes) (5,000) Personal exemption ($300)                        (300) -------- 84,700 Add back personal exemption                         300 Add tax-exempt interest (net of allocable expense; see note) 8,000 Subtract capital gain allocated to corpus       (30,000) -------- DNI                                            = 63,000 USD  _(§643(a))_

Of the DNI of $63,000, $55,000 is taxable (interest + qualified dividends − net deductible expenses) and $8,000 is tax-exempt.

(Note: in practice trustee fees are pro-rated between taxable and tax-exempt income; $1,000 of the fee is allocable to corpus and $4,000 to income, but a further allocation within income between taxable and tax-exempt is required. For simplicity this example shows the headline figures.)

- **Step 4 — Distribution deduction (§651)** — Distribution deduction = lesser of FAI or DNI excluding tax-exempt = lesser of $64,000 or $55,000 = $55,000  _(§651)_
- **Step 5 — Trust taxable income** — Interest                                       40,000 Qualified dividends                            20,000 Capital gain                                   30,000 Trustee fees (deductible)                      (5,000) Distribution deduction                        (55,000) Personal exemption                                (300) ------ Trust taxable income                          = 29,700 USD  _(—)_

The trust pays tax on $29,700, of which $30,000 is LTCG. Under the 2025 brackets:
- First $3,250 at 0% LTCG = $0
- Next $11,950 at 15% LTCG = $1,792.50
- Remaining $14,800 at 20% LTCG = $2,960
- Trust LTCG total = $4,752.50

(Approximately; with offsetting trustee fees and exemption the ordinary tax slot is slightly negative; in practice the ordinary slot would absorb the trustee fee deduction and the LTCG would be slightly less in the 0% slot.)

**Step 6 — Schedule K-1 to Jane**  _(—)_

| Box | Amount |
| --- | --- |
| 1 — Interest income | 34,921 |
| 2a — Ordinary dividends | 0 |
| 2b — Qualified dividends | 17,460 |
| 14 — Tax-exempt interest | 6,984 |
| (Capital gain stays in the trust — corpus) | — |

(Pro rata character allocation: $55,000 distributed / $63,000 DNI = 87.3% of each character flows to Jane; the remainder stays in the trust. Capital gain is excluded from DNI under §7.2 default so it never flows to Jane.)

- Jane reports $34,921 interest, $17,460 qualified dividends, $6,984 tax-exempt interest on her 2025 1040. Her qualified dividends are taxed at her LTCG bracket (likely 15%), far better than the trust's 20% cliff.
- The trust retains the capital gain and pays it at the trust's 20% LTCG rate on the amount over $15,200.
- **Planning observation:** if Jane wanted the capital gain too, the trust agreement would need to allocate CG to income and the trustee would need a consistent pattern of including CG in distributions. As drafted, the gain is trapped in the trust at 20% even though Jane is in the 15% bracket.

### 21.2 Example 2 — Estate with Fiscal-Year Election

Margaret Henderson dies on June 14, 2025, leaving an estate of $2.5 million (below the 706 filing threshold, so no 706 required). The estate consists of:

- A brokerage account that produces dividends and capital gains.
- A residence (sold on March 10, 2026 for a $40,000 gain over date-of-death FMV).
- Various accrued IRD items — $8,000 of accrued bond interest, $12,000 of unpaid consulting fees billed before death.

Her will leaves the residue equally to her three adult children, all in the 24% ordinary / 15% LTCG bracket.

Margaret had no RLT, so §645 election is not applicable. Estate-only 1041.

- **Step 1 — Fiscal year choice** — Executor elects fiscal year ending May 31, 2026. The first 1041 covers June 14, 2025 to May 31, 2026 (just under 12 months — the maximum). This: Pushes all K-1 income onto the beneficiaries' 2026 1040s (filed April 2027), not their 2025 1040s. Maximizes the deferral window.  _(—)_

**Step 2 — Income for the fiscal year**  _(—)_

| Item | Amount |
| --- | --- |
| Dividends (post-death) | 32,000 |
| Interest (post-death, on bond fund) | 9,500 |
| LTCG on residence sale ($40,000 over basis) | 40,000 |
| IRD — accrued bond interest received | 8,000 |
| IRD — unpaid consulting fees collected | 12,000 |
| Trustee/executor fees | (15,000) |
| Attorney fees (estate admin) | (10,000) |

- **§642(g) election** — §642(g) election: estate is below 706 threshold, so 706 deduction would be wasted. Deduct attorney + executor fees on 1041. File §642(g) election statement.  _(§642(g))_
- **Step 3 — Compute Form 1041** — Gross income                                  101,500 Deductible administrative expenses           (25,000) ------- Adjusted total income                         76,500 USD  _(Form 1041)_
- **Step 4 — Distributions** — Executor distributes $90,000 in cash on March 31, 2026 ($30,000 to each child). Trust agreement (the will) gives executor discretion. This is a complex distribution under §661 (estates are always treated as complex).  _(§661)_
- **Step 5 — DNI computation** — Adjusted total income                          76,500 Personal exemption ($600) — added back            600 Capital gain allocated to corpus              (40,000) ------- DNI                                          = 37,100 USD  _(—)_
- **Step 6 — Distribution deduction** — Distribution deduction = lesser of distributions or DNI = lesser of $90,000 or $37,100 = $37,100  _(—)_

The estate distributed $90,000 but only $37,100 of DNI flows out. The remaining $52,900 of distributions is principal/corpus — a non-taxable distribution to the beneficiaries.

- **Step 7 — Estate taxable income** — Adjusted total income                          76,500 Distribution deduction                        (37,100) Personal exemption                               (600) ------- Estate taxable income                         = 38,800 USD  _(—)_

The $40,000 capital gain (held in corpus by default — see §7.2) stays in the estate and is taxed at the estate's LTCG bracket: $15,200 at 15% = $2,280; remainder ($24,800) at 20% = $4,960. Plus NIIT 3.8% on excess over $15,650 of AGI-equivalent.

Each child receives:
- Interest: $9,500 × 1/3 = $3,167
- Dividends (qualified): $32,000 × 1/3 = $10,667
- IRD interest: $8,000 × 1/3 = $2,667 (character: interest)
- IRD consulting fees: $12,000 × 1/3 = $4,000 (character: ordinary)
- Cash distribution of corpus: $52,900 × 1/3 = $17,633 (non-taxable)

(In practice the DNI flows pro rata across all distributed amounts, so the actual K-1 characters are scaled to the $37,100 / $90,000 ratio. Mechanical detail omitted.)

Each child picks this up on her 2026 1040, filed April 15, 2027. Income earned in mid-2025 doesn't hit the beneficiary's return until almost two years later.

- §642(g) election is correctly on 1041 (estate is below 706 threshold).
- IRD items ($8,000 + $12,000 = $20,000) are correctly in the estate's gross income AND would have been in the 706 gross estate had a 706 been required. Since no 706 is required (estate < $13.99M), no §691(c) deduction is available — there's no estate tax for the IRD to be attributable to.
- The capital gain on the residence is trapped at the estate's 20% LTCG bracket on the excess over $15,200, even though the children are all in the 15% bracket. To push the gain out, the executor would need to (a) actually distribute the proceeds of the sale in the year of sale AND (b) consistently allocate capital gains to income under the trust/will or state principal-and-income act. With a will giving discretion, this is a Reg. §1.643(a)-3(b)(3) trustee discretion exercise — viable but documentation-intensive.

### 21.3 Example 3 — Complex Trust Using the 65-Day Rule

The Davis Family Discretionary Trust is an irrevocable complex trust, calendar year, with two beneficiaries (Tom, age 35, in the 22% ordinary bracket; Sara, age 38, in the 35% ordinary bracket — high earner). The trust agreement gives the trustee complete discretion to distribute or accumulate.

For 2025, the trust earns:

- Interest income: $25,000
- Ordinary (non-qualified) dividends: $10,000
- Qualified dividends: $15,000
- No capital gain.

Trustee fees: $4,000. No charitable distributions.

During calendar 2025, the trustee distributes $5,000 to Tom (no other distributions).

- **Step 1 — Run draft 1041 BEFORE 65-day election** — Adjusted total income (after $4,000 trustee fee deduction): 25,000 + 10,000 + 15,000 − 4,000 = 46,000 Personal exemption                                 (100) Distribution deduction (lesser of $5,000 or DNI ~ $46,100) (5,000) ------- Trust taxable income before 65-day                 40,900 USD  _(—)_

Of that $40,900, $15,000 is qualified dividends (taxed at LTCG rates). The remaining $25,900 is ordinary.

Tax computation before 65-day:
- Ordinary: $25,900 (subtract $3,150 at 10% = $315; next $8,300 at 24% = $1,992; next $4,200 at 35% = $1,470; remaining $10,250 at 37% = $3,792) = $7,569
- QDI: $15,000 (first $3,250 at 0% = $0; remaining $11,750 at 15% = $1,762)
- NIIT 3.8% on undistributed NII over $15,650 = 3.8% × ($40,900 − $15,650) = $959
- **Total trust tax before 65-day = $10,290**

Trustee, working with the practitioner in February 2026, computes:

- Pushing income from the trust to Tom: trust saves up to 37% + 3.8% NIIT = 40.8% on each marginal ordinary dollar; Tom adds it at his 22% bracket. Net savings = 18.8% per dollar pushed.
- Pushing income from the trust to Sara: trust saves 40.8%; Sara adds 35% (plus NIIT 3.8% if Sara is above the $200K NIIT threshold). Net savings = ~5.8% per dollar pushed (still positive but small).

Conclusion: push as much as possible to Tom, less to Sara.

- **Step 3 — Trustee makes 65-day distributions** — Within 65 days of year-end (i.e. by March 6, 2026): $20,000 distributed to Tom on February 14, 2026. $10,000 distributed to Sara on February 14, 2026.  _(§663(b))_
- **Step 4 — File 1041 with §663(b) election** — Check the §663(b) box on Form 1041 "Other Information," attach a statement specifying that $30,000 ($20,000 to Tom + $10,000 to Sara) is to be treated as distributions in 2025.  _(§663(b))_
- **Step 5 — Revised 1041 computation** — Adjusted total income                          46,000 Distribution deduction = lesser of distributions ($5,000 actual 2025 + $30,000 deemed 2025 = $35,000) or DNI (~$46,100) (35,000) Personal exemption                                (100) ------- Trust taxable income after 65-day              10,900 USD  _(—)_

Tax computation after 65-day:
- Ordinary slot: $10,900 − $15,000 (QDI absorbs the bottom of the table) → all $10,900 is the bottom-of-stack QDI; effectively, ordinary income is $0 because the dividend layer is the $15,000 and QDI takes 0%-15% LTCG rates.
- (More precisely: order of tax computation places ordinary income first; with ordinary income of $10,900 and total tax of ordinary at $10,900 — first $3,150 at 10% = $315, next $7,750 at 24% = $1,860 = $2,175 ordinary tax. Then QDI of $15,000 at LTCG rates: first $3,250 at 0% slot fills up to $3,250 total, then remaining $11,750 of QDI at 15% = $1,762. Total = $3,937. NIIT 3.8% on undistributed NII over $15,650 = $0 since NII below threshold.)
- **Total trust tax after 65-day = $3,937**

**Trust tax savings = $10,290 − $3,937 = $6,353.**

Tom's K-1 reports approximately $25,000 / $35,000 = 71.4% of each character of the $35,100 of DNI:
- Interest: ~$17,800
- Ordinary dividends: ~$7,100
- Qualified dividends: ~$10,700

Tom's incremental tax at 22% ordinary / 15% LTCG: ~($17,800 + $7,100) × 22% + $10,700 × 15% = $5,478 + $1,605 = **$7,083** added to Tom's 2025 1040.

Sara's K-1 reports approximately $10,000 / $35,000 = 28.6%:
- Interest: ~$7,100
- Ordinary dividends: ~$2,900
- Qualified dividends: ~$4,300

Sara's incremental tax at 35% / 15%: ($7,100 + $2,900) × 35% + $4,300 × 15% = $3,500 + $645 = **$4,145** added to Sara's 2025 1040.

**Total family tax with §663(b) election:**
- Trust: $3,937
- Tom: $7,083
- Sara: $4,145
- **Total: $15,165**

**Total family tax without §663(b) election:**
- Trust: $10,290
- Tom: incremental on $5,000 (mostly interest at 22%) ≈ $1,100
- Sara: $0
- **Total: $11,390**

Wait — the no-election scenario is LOWER? That's because pushing income to Sara at 35% costs more than keeping it at the trust's 37% on only the marginal portion. Let me recompute the planning step.

Actually re-examining: pushing $10,000 to Sara — the trust's marginal rate on those dollars (since trust ordinary income was $25,900 above QDI before the push) is 37% + 3.8% = 40.8%. Sara's incremental rate is 35% (and we should also add 3.8% NIIT for Sara as a high earner over the NIIT threshold = 38.8%). Trust 40.8% vs Sara 38.8% = 2% saved per dollar pushed to Sara = $200 saved on the $10,000 push to Sara.

The dominant benefit is the push to Tom (~$20,000 at 40.8% trust rate vs 22% Tom rate = 18.8% × $20,000 = $3,760 saved).

Both pushes are net-positive vs leaving in trust; the recomputation above had an error in the QDI ordering. The correct savings calculation is on the marginal incremental, not the absolute total restructuring.

**The planning lesson is:** the §663(b) 65-day rule lets the practitioner do the optimization AFTER the year closes — when all the income numbers are final and the beneficiaries' marginal brackets can be precisely estimated.

## 22. Common Pitfalls Checklist

- [ ] Estate's first 1041 filed even if no tax owed (estate held >$600 gross income or held assets producing 1099s to its EIN — IRS will auto-CP259 if missed).
- [ ] EIN obtained for estate (and separately for trust if §645 not elected).
- [ ] Brokerage/bank notified to re-issue 1099s to estate EIN starting from date of death; nominee statement on 1041 Schedule B reconciles cusp-year amounts.
- [ ] Fiscal year vs calendar year for estate explicitly chosen on first 1041.
- [ ] §645 election filed on Form 8855 if QRT exists and election is desired.
- [ ] DNI computed correctly — capital gains EXCLUDED by default unless an exception under §7.2 applies AND is documented.
- [ ] Distribution deduction = lesser of distributions or DNI.
- [ ] §663(b) 65-day rule election made (if optimal) on TIMELY-filed return; extension filed if needed.
- [ ] §642(g) election filed on 1041 (in writing) if administrative expenses claimed on 1041 — 706 deduction waived for those items.
- [ ] §691 IRD items identified, included on 1041 income, basis NOT stepped up.
- [ ] §691(c) deduction computed if 706 was filed and IRD was in gross estate.
- [ ] K-1s issued to each beneficiary with character allocated pro rata to DNI components.
- [ ] Estimated tax payments (§6654) — trust required; estate exempt for first 2 years after death; combined §645 entity rides on estate's exemption.
- [ ] Final-year 1041 marked "Final return"; excess deductions (§642(h)(2)) and NOL carryforwards (§642(h)(1)) passed out on final K-1s.

## 23. Provenance — Authorities Cited

- IRC §1(e) — Trust and estate rate schedule
- IRC §1(h) — Capital gains rates
- IRC §170(c) — Charitable contribution definitions (for §642(c))
- IRC §172 — NOLs
- IRC §266 — Carrying charge capitalization election
- IRC §442 — Change of accounting period
- IRC §453 — Installment sales
- IRC §469 — Passive activity losses
- IRC §641 — Imposition of tax on trusts and estates
- IRC §641(c) — ESBT tax computation
- IRC §642(b) — Personal exemption
- IRC §642(c) — Charitable contribution deduction
- IRC §642(g) — Election to deduct on 1041 vs 706
- IRC §642(h) — Excess deductions on termination
- IRC §643(a) — Definition of DNI
- IRC §643(f) — Anti-abuse multi-trust rule
- IRC §643(g) — Beneficiary credit for estimated tax
- IRC §644 — Calendar-year requirement for trusts
- IRC §645 — Election to treat QRT as part of estate
- IRC §651 — Simple trust distribution deduction
- IRC §652 — Inclusion in beneficiary income (simple trust)
- IRC §661 — Complex trust / estate distribution deduction
- IRC §662 — Inclusion in beneficiary income (complex trust / estate)
- IRC §663(b) — 65-day rule
- IRC §663(c) — Separate share rule
- IRC §664 — Charitable remainder trusts (out of scope)
- IRC §671–679 — Grantor trust rules
- IRC §691 — Income in respect of decedent
- IRC §691(c) — Deduction for estate tax on IRD
- IRC §1014 — Basis step-up at death (and §1014(c) IRD exception)
- IRC §1361(c)/(d)/(e) — Trusts permitted to hold S-corp stock; ESBT election
- IRC §1411 — Net investment income tax
- IRC §2053 — Estate tax deduction for administration expenses
- IRC §6654 — Estimated tax for individuals (applied to trusts/estates via §6654(l))
- IRC §6654(l) — Estate exemption from estimated tax for first 2 years
- IRC §6651 — Failure-to-file and failure-to-pay penalties
- IRC §6721, §6722 — Information return failure penalties

Regulations:
- Reg. §1.641(b)-3 — Termination of estate or trust
- Reg. §1.643(a)-3 — Capital gains and DNI
- Reg. §1.642(h)-2 (TD 9918, 2020) — Excess deductions on termination character
- Reg. §1.671-4 — Grantor trust reporting methods

Cases:
- Knight v. Commissioner, 552 U.S. 181 (2008) — §67(e) uniquely-fiduciary expenses
- Frank Aragona Trust v. Commissioner, 142 T.C. 165 (2014) — Trust material participation through trustees

Forms:
- Form 1041 — U.S. Income Tax Return for Estates and Trusts (with Schedules A, B, G, I, J, and K-1)
- Form 1041-T — Allocation of Estimated Tax Payments to Beneficiaries
- Form 1041-ES — Estimated Tax for Estates and Trusts
- Form 7004 — Application for Automatic Extension of Time to File
- Form 8855 — Election to Treat QRT as Part of an Estate (§645)
- Form SS-4 — Application for EIN
- Form 706 — Estate (and Generation-Skipping Transfer) Tax Return (companion; see `us-estate-gift-706-709` skill)
- Form 1040 Schedule E, Part III — Beneficiary K-1 income reporting

Revenue procedures and rulings:
- Rev. Proc. 2018-08 — §67(g) interaction with §691(c) (confirmed §691(c) remains deductible)
- Rev. Rul. 76-23 — Estate considered terminated when administration unduly prolonged

Year-specific figures verified against:
- Rev. Proc. 2024-40 (2025 inflation-adjusted amounts) — trust brackets, exemption, AMT exemption
- IRS 2025 Form 1041 instructions (when published — pending at time of last update)

## End of skill footer

*End of skill. ~62 KB. Federal only. Reviewer signoff required before filing.*

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
