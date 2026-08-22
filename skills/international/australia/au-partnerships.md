---
name: au-partnerships
description: >
  Use this skill whenever asked about Australian partnership taxation -- partnership tax returns (form P), how section 90 net income or partnership losses flow through to partners under section 92, partner salaries and drawings, non-commercial loss deferral for partner shares, CGT on fractional partnership interests, admitting or retiring partners, reconstitution versus dissolution, GST registration for partnerships, family or husband-and-wife partnerships, income splitting, Everett assignments, or professional firm profit allocation under PCG 2021/4. Trigger on phrases like "partnership return", "partner salary", "partnership loss", "profit share", "admit a partner", "family partnership", or "Everett". ALWAYS read this skill before touching any partnership work.
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

# Australia Partnerships -- Division 5 Flow-Through Taxation Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context.** Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Royal Assent 26 June 2026) is LAW: from 1 July 2027 the 50% CGT discount for individuals, trusts and partnerships is replaced by cost base indexation plus a 30% minimum rate on capital gains accruing after that date -- partners' fractional-interest gains (Rule 7) are computed under current rules for 2025-26 and 2026-27 only. The $20,000 small business instant asset write-off is legislated for 2025-26; permanence from 1 July 2026 is ANNOUNCED, not yet law. Verify both before relying.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Division 5 (ss 90-94); s 995-1 ITAA 1997 (definition); s 106-5 ITAA 1997 (CGT); Div 35 ITAA 1997 (non-commercial losses) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season for 2025-26 |
| Entity taxation | NONE -- the partnership lodges a return (form P, NAT 0659) but pays no income tax; s 92 flows net income/losses to partners |
| Sharing absent agreement | Equal shares (state Partnership Acts default) |
| Partner "salary" | NOT deductible -- a distribution of profit (TR 2005/7); cannot create or increase a partnership loss |
| Partnership losses | Flow through to partners in the loss year (contrast trusts) -- individuals then gated by Div 35 non-commercial loss rules |
| Div 35 gates | Income requirement < $250,000; then one of: assessable income >= $20,000, profits 3 of 5 years, real property >= $500,000, other assets >= $100,000, or Commissioner's discretion |
| CGT | No partnership-level CGT -- each partner holds a fractional interest in EACH CGT asset (s 106-5) |
| GST | Registers at PARTNERSHIP level; $75,000 registration turnover threshold (GSTR 2003/13) |
| PAYG instalments | Entered and paid by each PARTNER on their instalment-income share, not by the partnership |
| Return due dates | Self-lodged: 31 October; registered agent: per lodgment program (commonly 15 May) |
| Professional firm profits | PCG 2021/4 gateways + risk zones (green <= 7 / amber 8 / red >= 9 on factors 1-2; <= 10 / 11-12 / >= 13 on all three) |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| No written partnership agreement sighted | Assume EQUAL income and loss sharing; flag that salary/interest allocations are unproven |
| Salary or profit-variation agreement undated | Assume made AFTER year end -- ineffective for that year (*Galland*); shares revert to the deed/default |
| Jointly owned rental property, no business | Tax-law partnership by joint receipt only -- split per LEGAL ownership interests (TR 93/32; *McDonald*), agreements ignored; no partnership return required |
| Family partnership genuineness unknown | Test against TR 94/8 factors and run the PSI screen (au-psi) before accepting the split |
| Income vs capital sharing ratios differ | Verify both ratios against the deed; document -- CGT follows asset fractions, s 92 follows income interests |
| Partner joined/left during the year | Assume reconstitution conditions NOT satisfied until evidenced -- two returns and new TFN/ABN exposure (Rule 8) |
| Div 35 test evidence missing | Assume the loss is DEFERRED for individual partners; flag |
| Corporate or trust partner present | Exclude their share from the whole-partnership $20,000 / $500,000 / $100,000 tests; company tax and Div 7A screens apply to the corporate partner |
| Everett assignment mentioned | Treat as unassessed high-risk until PCG 2021/4 gateways are cleared -- escalate (R-AU-PT-1) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- partnership agreement (or confirmation none exists), prior form P return, current-year trial balance/financials, each partner's identity, type (individual/company/trust) and residency, income and capital sharing ratios.

**Recommended** -- partners' capital and drawings ledgers, any salary/interest clauses with the DATE they were agreed, asset register with acquisition dates and cost bases per asset, GST registration status, each individual partner's other taxable income (for Div 35), PCG 2021/4 self-assessment where professional services.

**Ideal** -- deeds of admission/retirement with dates, reconstitution notification evidence (28-day letter to the ATO), work-in-progress and trading stock values at change dates, family-group and associate map, Everett assignment deeds if any exist.

### Refusal catalogue

**R-AU-PT-1 -- Everett assignments.** *Trigger:* executing, valuing, or defending an assignment of a partnership interest to a spouse, trust or other entity; anything failing the PCG 2021/4 gateways. *Message:* "Everett assignments involve equitable assignment of a chose in action, CGT on the assignment, PCG 2021/4 gateway and risk-zone analysis, Part IVA exposure, and (since 8 May 2018) restricted small business CGT concessions. Out of scope -- escalate to a qualified practitioner. This skill only flags and risk-scores existing arrangements (Rule 12)."

**R-AU-PT-2 -- Corporate limited partnerships (Div 5A).** *Trigger:* limited partnership, incorporated limited partnership, or any partnership taxed as a company under ss 94A-94X. *Message:* "Corporate limited partnerships are taxed as companies (Division 5A; s 94K switches off Division 5) -- distributions are deemed dividends. Out of scope. Escalate."

**R-AU-PT-3 -- Foreign hybrids and foreign partners.** *Trigger:* foreign hybrid limited partnership (Div 830 ITAA 1997), non-resident partners, or foreign-source partnership income with treaty questions. *Message:* "Foreign hybrid classification, s 92(1)(b) source apportionment and treaty relief are out of scope. Escalate before lodgment."

**R-AU-PT-4 -- VCLPs and ESVCLPs.** *Trigger:* venture capital limited partnership, early stage venture capital limited partnership, AFOF or VCMP structures. *Message:* "Venture capital vehicles have their own registration, flow-through and exemption regimes (Subdiv 118-F ITAA 1997; Venture Capital Act 2002). Out of scope. Escalate."

**R-AU-PT-5 -- Partnership rollovers and restructures.** *Trigger:* incorporating a partnership (Subdiv 122-B), small business restructure rollover (Subdiv 328-G), s 70-100 trading stock elections on a change of ownership, or merging firms. *Message:* "Rollover eligibility, election deadlines and asset-by-asset consequences are out of scope. Compute nothing -- escalate."

**R-AU-PT-6 -- s 94 uncontrolled partnership income.** *Trigger:* a partner who lacks real and effective control and disposal of their share (sleeping partners, minors as partners, contrived interposed interests). *Message:* "Section 94 ITAA 1936 imposes further tax at penalty rates on uncontrolled partnership income. Identification and computation are out of scope -- document the control facts and escalate."

## Section 3 -- GL sweep library

Partnership work starts with the P&L and the capital accounts, not the profit split the client recites.

| GL pattern | Likely issue | Action |
|---|---|---|
| "Partner salary" / partner names in wages expense; drawings coded as salary or consulting expense | Profit distribution mis-coded as a deduction (TR 2005/7); PAYG-W may have been wrongly applied | Add back to s 90 net income; treat as allocation of the partner's s 92 share -- partners are not employees: no PAYG-W, no SG on drawings |
| Superannuation expense for partners | Partners' personal contributions are NOT partnership deductions | Add back; each partner claims their own s 290-150 deduction personally |
| "Interest on capital" credited to partners | Appropriation of profit, not an expense | Add back to net income; it forms part of the recipient's profit share |
| Interest on genuine external borrowings | Deductible if funding the business -- including refinancing partner capital previously invested (*Roberts & Smith*; TR 95/25) | Verify the borrowing's use; refinancing of capital in excess of contributed amounts escalates |
| One partner's drawings persistently fund private assets | Disguised unequal distribution; family-splitting / s 94 optics | Reconcile drawings to profit shares; check the agreement actually supports the split |
| Loan account: partnership lends to a partner | Not Div 7A (no private company lender) -- but check corporate partners | If a corporate PARTNER's money flows to shareholders/associates, run au-div7a on the company |
| Round-sum monthly "management fee" to a related entity | Profit extraction bypassing s 92 shares | Test substance; PCG 2021/4 / Part IVA optics for professional firms |
| Negative partner capital account | Drawings exceed profit shares -- exit CGT and recovery risk | Flag; check partner's basis on any retirement |
| "Partnership distribution" of rental property between spouses at non-title ratios | TR 93/32 breach | Re-split per legal ownership; amend if lodged |

---

## Section 4 -- Worked examples

### Example 1 -- Equal two-partner split with s 92 inclusion

Ana and Ben run a cafe in equal partnership (no written agreement -- equal sharing by default). 2026-27: accounting profit $86,000 AFTER crediting each partner $2,000 "interest on capital". Both amounts are appropriations of profit, so s 90 net income = $86,000 + $4,000 = **$90,000**. Each partner's s 92(1) share = **$45,000** -- assessable whether or not drawn (Ana drew only $20,000 cash; she is still assessed on $45,000).

Ana has no other income. 2026-27 resident rates: tax = 15% x ($45,000 - $18,201) = 15% x $26,799 = **$4,019.85**, plus Medicare levy 2% x $45,000 = $900, less offsets: the small business income tax offset (turnover < $5m) is 16% x $4,019.85 = $643 (under the $1,000 cap), plus any LITO. The partnership itself pays nothing and remits nothing for the partners.

### Example 2 -- Partner salary recharacterised where it would create a loss

The written agreement (signed before 1 July -- *Galland* timing satisfied) gives Priya a $60,000 "salary" plus 50% of the remainder; Quinn takes the other 50%.

**Case A -- net income $40,000.** The salary is not deductible and cannot create a loss (TR 2005/7 para 7). Priya's s 92 interest = the available net income, capped: **$40,000**. Quinn: **nil**. The $20,000 excess drawn is an advance of future profits -- not assessable now, and brought to account in a later year when sufficient profits exist (TR 2005/7 paras 8-9).

**Case B -- partnership loss $10,000 (before any salary).** The salary agreement merely varies profit shares -- it cannot manufacture or enlarge a loss. The s 90 partnership loss stays **$10,000**, flowing $5,000 to each partner under s 92(2) (equal loss sharing). Priya's $60,000 drawn is simply drawings against her capital account and future profit entitlements.

### Example 3 -- Non-commercial loss deferral for a hobby-farm partner

Sam (salary $185,000) and his spouse run a small olive grove in equal partnership; both are individuals. 2026-27: partnership assessable income $12,000, partnership loss $18,000 -- Sam's s 92(2) share is a $9,000 deduction, IF Div 35 lets him use it.

- Income requirement: Sam's income for Div 35 (taxable income adding back the business loss, plus reportable fringe benefits, reportable super and net investment losses) is about $194,000 < $250,000 -- **met**, so the four tests are available.
- Assessable income test: whole-partnership income $12,000 < $20,000 -- **fail**.
- Profits test: losses every year since planting -- **fail** (needs profits in 3 of the last 5 years including the current year).
- Real property test: grove land worth $380,000 < $500,000 -- **fail**.
- Other assets test: plant and stock $60,000 < $100,000 -- **fail**.
- Commissioner's discretion: no flood/drought special circumstances; olives are past their lead time -- **not sought**.

Result: Sam's $9,000 share is **deferred**, quarantined against future profits of the same activity. The primary production exception cannot save him: it needs other income (excluding net primary production income) under $40,000, and Sam's salary alone is $185,000. His spouse (no other income) meets the income requirement too but fails the same four tests -- also deferred; had she earned nothing else, the $40,000 primary production exception would have let her claim her share immediately. Same partnership, different outcomes per partner.

### Example 4 -- Fractional CGT on admitting a partner

Cate and Dev are equal partners. The partnership's only CGT asset is business premises: cost $400,000 (acquired 2023), market value $600,000. On 1 March 2027 they admit Emil as an equal one-third partner.

There is no partnership-level CGT. Under s 106-5, Cate and Dev each held a 50% fractional interest in the premises; each now disposes of one-sixth of the asset (50% -> 33.33%) to Emil -- CGT event A1 for each of them:

```
Each disposer:  capital proceeds = 1/6 x $600,000 = $100,000
                cost base        = 1/6 x $400,000 =  $66,667
                capital gain     =                    $33,333
                50% discount (individual, held > 12 months) -> $16,667 assessable
```

Emil acquires two one-sixth interests (cost base $200,000 in total) with a fresh acquisition date of 1 March 2027 -- his 12-month discount clock starts then, and from 1 July 2027 the new indexation/30%-minimum-rate regime (law-change banner) governs gains accruing on ALL partners' interests. If the partnership agreement had shared capital 70/30 while sharing income 50/50, the disposal fractions would follow the CAPITAL ratios -- the two can differ (Rule 7).

### Example 5 -- Professional firm profit allocation: risk-zone scoring

Farid is an equity partner (IPP) in an engineering partnership. His total profit entitlement from the firm group is $500,000, routed partly through associated entities. Gateways: the structure has commercial rationale and no high-risk features (no Everett assignment, no non-equity partner issues) -- PCG 2021/4 scoring is available.

**Scenario 1:** Farid returns $200,000 (40%) personally; total tax paid by him and his associates on the $500,000 is $130,000 (effective rate 26%). Factor 1: 40% sits in the ">25% to <50%" band = score 5. Factor 2: 26% sits in ">25% to <30%" = score 4. Aggregate (two factors) = **9 -> RED zone** (>= 9): priority ATO analysis, audit likely if confirmed.

**Scenario 2:** Farid instead returns $300,000 (60%) personally and the group's effective rate is 31%. Factor 1: "50% to 60% inclusive" = score 4. Factor 2: "30% to 35% inclusive" = score 3. Aggregate = **7 -> GREEN zone** (<= 7): compliance attention only in exceptional cases. Returning 100% personally is automatically green with no further scoring.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- What a tax-law partnership is (s 995-1)

A partnership is (a) an association of persons (other than a company or a limited partnership) carrying on business as partners **or in receipt of ordinary income or statutory income jointly**, or (b) a limited partnership. The joint-receipt limb makes the tax definition BROADER than general law: joint investors can be tax-law partners with no business at all. Whether persons carry on business as partners is a fact question -- TR 94/8 factors: mutual assent and intention, joint bank account and who can operate it, capital contributions, agreed profit/loss shares, joint business records, trading in joint names and public recognition. A partnership has no separate legal personality; it needs its own TFN and ABN. Mere co-owners of a rental property are a tax-law partnership by joint receipt but do NOT lodge a partnership return -- each returns their share of net rent directly, split strictly by legal ownership interests (Rule 11).

### Rule 2 -- Flow-through: s 90 net income and s 92 shares

s 90: "net income" = the partnership's assessable income calculated as if it were a resident taxpayer, less all deductions EXCEPT personal super contributions (s 290-150) and prior-year losses (Div 36) -- a partnership cannot carry losses forward because they have already flowed out. "Partnership loss" is the mirror excess. s 92: each partner includes their individual interest in net income (resident partners: all of it; non-resident partners: Australian-source share -- escalate, R-AU-PT-3), or deducts their interest in a partnership loss. Shares follow the agreement; absent agreement, state Partnership Acts default to EQUAL shares. Partners are taxed on their shares whether or not anything is distributed -- drawings are tax-neutral. The partners may vary their profit-sharing arrangement by agreement, but only prospectively within the year: an agreement made after year end is ineffective for that year (*FCT v Galland* (1986) 162 CLR 408).

### Rule 3 -- The partnership return (form P): information only

The partnership lodges a Partnership tax return (form P, NAT 0659) showing business income, deductions, net income/loss and a statement of distribution allocating every partner's share (including salary-style allocations, which are distributions, not expenses). NO tax is payable on the P return. Due 31 October if self-lodged; registered-agent program dates otherwise (commonly 15 May). Each partner separately returns their share in their own return at their own rates -- individuals may also claim the small business income tax offset (16% of the tax on their net small business income share, capped at $1,000, firm turnover < $5m).

### Rule 4 -- Partner salaries are profit distributions (TR 2005/7)

**AUDIT FLASH POINT**

A "partnership salary" is not truly salary and is NOT deductible under s 8-1 in computing s 90 net income -- it is a distribution of profit to the recipient partner, whether or not paid for personal services. Consequences (TR 2005/7):

- A salary agreement merely VARIES the partners' interests in profits. It is effective for a year only if entered into before the end of that year (*Galland*).
- The recipient's s 92(1) interest includes the salary TO THE EXTENT of available net income. Any excess drawn is an advance of future profits -- not assessable when drawn, assessable in a later year when sufficient profits exist.
- A partnership salary can NEVER create or increase a partnership loss (para 7). If the partnership is in loss, the "salary" is just drawings and the s 90 loss flows per the loss-sharing ratios.
- Partners are not employees: no PAYG withholding, no superannuation guarantee on their drawings or salaries; each partner claims their own personal super deduction. Wages to genuine (non-partner) employees remain fully deductible.
- In a corporate limited partnership the same amount is instead a deemed dividend (Div 5A) -- escalate (R-AU-PT-2).

### Rule 5 -- Interest on partner capital, drawings, and borrowings

Interest credited to a partner on capital contributed is, like salary, an appropriation of profit -- not deductible to the partnership; it forms part of the recipient's profit share. Drawings are returns of capital/anticipated profit: never assessable as such, never deductible, and irrelevant to s 92 (partners are taxed on shares, not cash). Distinguish genuine borrowings: interest on external debt used in the business is deductible in computing s 90 net income, INCLUDING borrowings that refinance partner capital previously invested in the business up to the amount contributed (*FCT v Roberts; FCT v Smith* 92 ATC 4380; TR 95/25 refinancing principle -- refinancing beyond contributed capital, or of "internally generated goodwill" revaluations, fails). A partner who borrows personally to fund their capital contribution or acquire their interest deducts that interest in their OWN return against partnership income.

### Rule 6 -- Losses flow through immediately -- then Div 35 gates individuals

**AUDIT FLASH POINT**

Unlike a trust (where losses are trapped in the trust), a partnership loss flows to the partners in the loss year under s 92(2). For an INDIVIDUAL partner whose share is from a non-commercial business activity, Division 35 ITAA 1997 then decides whether the share is usable now or deferred:

1. **Income requirement:** the partner's taxable income (adding back the business loss), reportable fringe benefits, reportable super contributions and total net investment losses must be **under $250,000**. Fail this and only the Commissioner's discretion can help.
2. If met, ONE of the four tests must pass -- with partnership modifications (TR 2003/3):
   - **Assessable income test:** activity income >= $20,000 -- measured across the WHOLE partnership where all partners are individuals; EXCLUDE shares of corporate/trust partners; a partner's own non-partnership income from the same activity counts for that partner only.
   - **Profits test:** THE PARTNER's income from the activity (partnership share plus own-right amounts) exceeded their deductions in at least 3 of the past 5 years including the current year -- partner-level interest costs can fail one partner while another passes.
   - **Real property test:** real property used in the activity >= $500,000 -- whole-partnership value, excluding corporate/trust partners' shares and property partners own personally, EXCEPT the tested partner may add their own property used continuously in the business.
   - **Other assets test:** other assets >= $100,000 -- same whole-partnership/exclusion pattern.
3. **Exceptions/discretion:** primary production or professional arts businesses are exempt where the individual's other income (excluding net PP income) is under $40,000; the Commissioner may exercise discretion for special circumstances (flood, drought, illness) or lead-time activities.
4. **Deferral:** a gated loss share is deferred and quarantined -- deductible against future income of the SAME activity (or when a test is later passed). It never becomes a partnership-level attribute.

Company and trust partners are outside Div 35 -- their shares follow their own loss regimes.

### Rule 7 -- CGT: partners hold fractional interests in each asset (s 106-5)

There is no partnership-level CGT. Any capital gain or loss from a CGT event involving a partnership asset is made by the PARTNERS individually: each partner has a separate cost base and reduced cost base for their fractional interest in EACH partnership CGT asset, in their capital-sharing proportions. Consequences:

- Each partner applies their own method: individuals get the 50% discount on interests held > 12 months (through 30 June 2027 -- see law-change banner), companies get none, and each partner's own capital losses offset their share.
- Income-sharing and capital-sharing ratios can differ under the agreement -- s 92 follows income interests; CGT follows asset fractions. Document both (T2-1).
- A partner can hold different percentages in different assets, and different acquisition dates per interest (e.g. original stake 2019, increased stake 2024).
- Small business CGT concessions are tested at partner level on their interests (see au-small-business-cgt).

### Rule 8 -- Joining and leaving: disposal/acquisition; dissolution vs reconstitution

Any change in composition dissolves the partnership at general law. Tax runs on two tracks:

- **CGT track:** an incoming partner ACQUIRES fractional interests in every partnership CGT asset; continuing partners DISPOSE of the fractions they give up (Example 4); a retiring partner disposes of all their fractions. Trading stock and depreciating asset changes have their own rules (s 70-100 notional disposal at market value unless a >= 25%-continuity election is made; balancing adjustments) -- restructures escalate (R-AU-PT-5).
- **Administration track:** if the change is only a TECHNICAL dissolution -- the continuing (plus any new) partners take over the assets and liabilities and the business continues without apparent break -- the ATO treats it as a RECONSTITUTED partnership: the SAME TFN and ABN continue, ONE form P covers the full year (distributions to everyone who was a partner at any time, with a schedule of changes), and the GST registration continues. Conditions: general law partnership; at least one common partner before and after; an express or implied continuity clause; no break in the enterprise (same business, customers, name); and never a moment with only one "partner" (two-person firms need a direct transfer of interests). Notify the ATO within 28 days. Anything more -- winding up, no continuity -- is a NEW partnership: new TFN and ABN, and two part-year returns (old entity to dissolution date; new entity from formation).

### Rule 9 -- GST registers at partnership level

The partnership is the entity for GST: it registers (compulsorily at $75,000 GST turnover; $150,000 for non-profits), holds the ABN, issues tax invoices, claims input tax credits and lodges the BAS -- not the partners (GSTR 2003/13 for general law partnerships). Partners are jointly and severally liable for the partnership's GST obligations. Supplies between the partnership and a partner can have GST consequences (e.g. asset distributions on retirement) -- escalate valuation-heavy exits. A reconstituted partnership keeps its GST registration (Rule 8). See au-gst-bas for BAS mechanics.

### Rule 10 -- PAYG instalments are the partners' problem

The partnership pays NO PAYG instalments. Each partner includes their share of partnership income in their OWN instalment income: individuals are entered into the system off their latest assessed return, and new partners should budget for tax on shares from day one (no employer withholding exists on profit shares). A partner's gross share of partnership ORDINARY income (not just the net amount) feeds instalment income for rate-method payers. See au-payg-instalments for entry thresholds and variation mechanics -- varying below 85% of actual attracts GIC.

### Rule 11 -- Family partnerships and income-splitting risk

**AUDIT FLASH POINT**

Genuine spouse/family partnerships are legitimate where BOTH partners really carry on the business (TR 94/8 factors: joint conduct, capital, exposure to losses, joint accounts, public holding-out). The traps:

- **Mere co-ownership is not a business partnership.** Jointly held rental property income/losses split per LEGAL title regardless of any agreement (TR 93/32; *FCT v McDonald* (1987) 15 FCR 172 -- the 25/75 "agreement" failed; the 50/50 title governed). No partnership return; no salary allocations.
- **Personal services income cannot be split.** If income is mainly a reward for one individual's personal efforts or skills, the PSI regime attributes it to that individual regardless of the partnership wrapper -- run the au-psi screen (results test, 80% rule, unrelated clients) BEFORE accepting any family split of professional or contractor income.
- **Salary-agreement games fail.** Allocating a "salary" to the low-income spouse cannot create a loss and only redistributes actual profit (Rule 4); backdated agreements are ineffective (*Galland*) and fabricating them is fraud.
- **Part IVA and s 94** sit behind contrived structures: Everett-style splitting of professional income and shares lacking real control escalate (R-AU-PT-1, R-AU-PT-6).
- Employing a genuine-employee spouse instead requires commercial wages for actual work -- excessive amounts are non-deductible under s 26-35 (related-party payments).

### Rule 12 -- Professional firms: PCG 2021/4 and Everett assignments

**AUDIT FLASH POINT**

For individual professional practitioners (IPPs) in law, accounting, engineering, medical and similar firms, PCG 2021/4 (*Allocation of professional firm profits -- ATO compliance approach*, applying from 1 July 2022) sets the ATO's compliance posture on how much of the firm profit the IPP returns personally:

- **Gateway 1:** commercial rationale for the structure. **Gateway 2:** no high-risk features -- e.g. financing around non-arm's-length transactions, assignments materially different in principle from *Everett*/*Galland* (non-equity "partners", fixed draws with no partnership risk, indemnified partners), multiple assignments, SMSF involvement, distributions to loss entities. Fail a gateway and the framework is unavailable: expect direct anti-avoidance (Part IVA) scrutiny -- escalate.
- **Scoring (1-6 per factor):** Factor 1 -- proportion of firm-group profit entitlement returned personally by the IPP (>90% = 1; >75-90% = 2; >60-75% = 3; 50-60% = 4; >25-<50% = 5; <=25% = 6). Factor 2 -- total effective tax rate on the whole entitlement across the IPP and associates (>40% = 1 down to <=20% = 6). Factor 3 (optional) -- IPP remuneration vs commercial benchmark (>200% = 1 down to <=70% = 6).
- **Zones:** two factors -- green <= 7, amber 8, red >= 9; three factors -- green <= 10, amber 11-12, red >= 13. Returning 100% personally is automatically green. Green = compliance attention only in exceptional cases; amber = likely review; red = priority analysis and potential audit.
- **Everett assignments** (assigning part of a partner's interest -- a chose in action -- so the assignee is taxed on that share as income from property): still legally effective per *Everett* (1980) 143 CLR 440 and *Galland*, but execution, valuation and defence are escalation-only (R-AU-PT-1); CGT applies to the assignment, and since 8 May 2018 the small business CGT concessions require the interest to make the entity an actual partner. Re-score existing assignments against PCG 2021/4 every year.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Income vs capital ratio mismatch

**Trigger:** agreement shares income and capital differently, or the split changed during the year. **Issue:** s 92 follows income interests; s 106-5 CGT follows asset fractions; undocumented divergence invites reconstruction. **Action:** minute both ratios, date all variations (before year end), keep per-asset fraction schedules.

### T2-2 -- Mid-year partner change hygiene

**Trigger:** admission/retirement during the year. **Issue:** reconstitution conditions (Rule 8), WIP and trading stock values at the change date, s 70-100 election window, and the retiring partner's fractional CGT. **Action:** gather deeds and dates; confirm one-return vs two-return posture BEFORE lodgment; escalate rollover talk (R-AU-PT-5).

### T2-3 -- Corporate partner in the mix

**Trigger:** a Pty Ltd holds a partnership interest. **Issue:** the company's share is taxed at company rates (base-rate-entity status tested on ITS income); Div 7A risk if the company's money reaches shareholders through the partnership; whole-partnership Div 35 tests exclude its share. **Action:** run au-company-tax and au-div7a on the corporate partner; map cash flows.

### T2-4 -- Existing Everett assignment on the books

**Trigger:** part of a partner's share is returned by a trust/spouse under an old assignment. **Issue:** annual PCG 2021/4 re-scoring; high-risk features void the framework; the assignor still controls the underlying interest. **Action:** score the current year (Example 5); document gateways; escalate any variation or new assignment (R-AU-PT-1).

### T2-5 -- 2026-27 reform horizon

**Trigger:** planning that spans 1 July 2027, or asset write-off assumptions past 30 June 2026. **Issue:** LAW: from 1 July 2027 partners' capital gains move to indexation plus a 30% minimum rate (discount abolished for gains accruing after that date). ANNOUNCED only: permanent $20,000 instant asset write-off from 1 July 2026. **Action:** label every projection LAW vs ANNOUNCED; never model announced measures as enacted.

---

## Section 7 -- Excel working paper template

```
AUSTRALIA PARTNERSHIP -- DISTRIBUTION WORKING PAPER
Partnership: [name]   TFN/ABN: [____]   Income year: 2026-27
Agreement sighted: [YES/NO + date]   Salary/interest clauses dated: [____]

s 90 NET INCOME RECONCILIATION
  Accounting profit/(loss):                AUD [____]
  + Partner "salaries" expensed:           AUD [____]
  + Interest credited on partner capital:  AUD [____]
  + Partner super expensed:                AUD [____]
  + Other non-deductibles:                 AUD [____]
  - Tax-only deductions (e.g. IAWO):       AUD [____]
  = s 90 net income / (partnership loss):  AUD [____]

DISTRIBUTION STATEMENT (per partner)
  Name / type (indiv, company, trust) / TFN / residency: [____]
  Income share %  /  Capital share %:      [____] / [____]
  Salary-style allocation (distribution):  AUD [____]
  Balance share of net income/(loss):      AUD [____]
  s 92 amount to partner's return:         AUD [____]
  Drawings for the year (memo only):       AUD [____]
  Capital account: open / movements / close: AUD [____]

DIV 35 SCREEN (each INDIVIDUAL partner in a loss activity)
  Income requirement < $250,000:           [MET / FAILED]
  Tests: income $20k [ ] profits 3/5 [ ] property $500k [ ] assets $100k [ ]
  PP/arts exception (<$40k other income):  [YES/NO]
  Result: [DEDUCT / DEFER] AUD [____]

CGT FRACTIONS REGISTER
  Asset / cost base / partner fractions / acquisition dates: [____]
  Changes in composition this year (dates, reconstitution evidence): [____]

FLAGS
  [PCG 2021/4 zone if professional firm; refusals triggered; Tier 2 items]
```

---

## Section 8 -- Reading guide

1. Agreement first: income shares, capital shares, salary/interest clauses and THEIR DATES. No agreement = equal shares.
2. Rebuild s 90 net income before allocating -- add back partner salaries, partner super and interest on capital every time.
3. s 92 taxes shares, not cash: reconcile drawings separately and never let them touch the tax computation.
4. Losses: flow now, but run the Div 35 screen per individual partner before anyone banks a deduction.
5. Any partner change: date it, test reconstitution, and price the fractional CGT on both sides.
6. Professional firm? Score PCG 2021/4 before signing anything; 100% returned personally is automatic green.
7. Family split? TR 94/8 genuineness, TR 93/32 title splits, and the PSI screen come before the arithmetic.

---

## Section 9 -- Onboarding fallback

If the client provides only financial statements:

1. Sweep the P&L and equity per Section 3 -- pull partner salaries, super and capital interest back into net income
2. Build the distribution statement from stated ratios; mark the agreement UNSIGHTED and shares unverified
3. List every individual partner in a loss position and mark Div 35 status UNRESOLVED (default: defer)
4. Build the CGT fractions register from the asset schedule; flag missing acquisition dates
5. **Flag:** "Prepared from financial statements only. Partnership agreement, salary/variation dates, Div 35 test evidence and composition-change documents not sighted. Shares and loss deductibility unconfirmed. Reviewer must confirm before lodgment."

---

## Section 10 -- Reference material

### Key figures

| Item | Value |
|---|---|
| Partnership income tax payable | Nil -- flow-through (s 92) |
| Default sharing absent agreement | Equal |
| Div 35 income requirement / four tests | $250,000; $20,000 income / profits 3-of-5 / $500,000 real property / $100,000 other assets |
| Div 35 PP-arts exception | Other income < $40,000 |
| GST registration threshold (partnership level) | $75,000 ($150,000 non-profit) |
| CGT discount for individual partners | 50% (interests held > 12 months) -- replaced by indexation + 30% minimum rate from 1 July 2027 (LAW) |
| Small business income tax offset (individual partners) | 16% of tax on net small business income share, capped $1,000, turnover < $5m |
| Reconstitution notification | 28 days; same TFN/ABN; one form P for the full year |
| PCG 2021/4 zones | Two factors: green <= 7 / amber 8 / red >= 9. Three factors: green <= 10 / amber 11-12 / red >= 13 |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Definition; Division 5 | s 995-1 ITAA 1997; ITAA 1936 ss 90, 91, 92, 94 (current compilation, legislation.gov.au) |
| Partnership returns and flow-through | ato.gov.au -- Income tax return: partnerships and partners; Business, partnership and trust income |
| Partner salaries | TR 2005/7 (consolidated 5 November 2014, incl. CLP addendum); *FCT v Galland* (1986) 162 CLR 408 |
| Partnership existence; co-owners | TR 94/8; TR 93/32; *FCT v McDonald* (1987) 15 FCR 172 |
| Interest deductibility / refinancing | TR 95/25; *FCT v Roberts; FCT v Smith* 92 ATC 4380 |
| Non-commercial losses | Div 35 ITAA 1997; TR 2003/3; ato.gov.au QC 45040 (partnerships, updated 7 April 2025), QC 55240 (income requirement) |
| CGT fractional interests | s 106-5 ITAA 1997; ATO ID 2006/200 |
| Reconstitution / composition changes | ato.gov.au -- Changing the makeup of a partnership (QC 40493, updated 12 July 2023); GSTR 2003/13 |
| Professional firm profits | PCG 2021/4; ato.gov.au QC 42218 (assessing the risk, updated 26 September 2024) |
| Everett assignments | *FCT v Everett* (1980) 143 CLR 440; ato.gov.au QC 46120 (updated 26 September 2024); Treasury Laws Amendment (Tax Integrity and Other Measures) Act 2019 (8 May 2018 SBCGT limits) |
| CGT reform from 1 July 2027 | Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Royal Assent 26 June 2026) |

### Test suite

**Test 1:** Net income $90,000, no agreement, two partners. -> $45,000 each under s 92, taxed whether or not drawn.

**Test 2:** Partner salary $60,000; net income $40,000; remainder 50/50. -> Salaried partner $40,000; other partner nil; $20,000 = advance of future profits, not assessable now.

**Test 3:** Partnership loss $10,000 with a $60,000 salary agreement. -> Loss stays $10,000, shared per loss ratios; salary cannot create or increase it.

**Test 4:** Individual partner, income requirement met, whole-partnership activity income $12,000, all other tests failed. -> Loss share deferred, quarantined to the activity.

**Test 5:** Partnership of two individuals and one company; partnership income $22,000 of which $4,000 is the company's. -> Countable income $18,000 < $20,000: individuals fail the assessable income test on partnership amounts alone.

**Test 6:** Equal partners admit a third; asset cost $400,000, value $600,000. -> Each original partner: proceeds $100,000, cost base $66,667, gain $33,333, discountable.

**Test 7:** Partner retires; remaining partners carry on, continuity clause exists, ATO notified in 28 days. -> Reconstitution: same TFN/ABN, one return. No continuity -> new TFN/ABN, two returns.

**Test 8:** Partnership turnover $80,000. -> Must register for GST at partnership level; partners do not register for the partnership's activities.

**Test 9:** IPP returns 40% personally, group effective tax rate 26%. -> Scores 5 + 4 = 9: red zone. Returns 100% personally -> automatic green.

**Test 10:** Spouses hold a rental 50/50 as joint tenants; "partnership agreement" says 90/10 to the low earner. -> Split 50/50 per title (TR 93/32; *McDonald*); the agreement is ineffective.

**Test 11:** Sleeping partner with no control over their 40% share. -> s 94 uncontrolled partnership income risk: refuse computation, escalate (R-AU-PT-6).

### Prohibitions

- NEVER deduct a partner's salary, super, or interest on capital in computing s 90 net income -- and NEVER let a salary agreement create or increase a partnership loss (TR 2005/7)
- NEVER give effect to a profit-share variation agreed after year end -- and NEVER backdate one
- NEVER carry a loss forward inside the partnership -- losses flow to the partners in the loss year, and an individual's share is never deducted without the Div 35 screen
- NEVER compute CGT at partnership level -- fractional interests per partner, per asset
- NEVER assume a partner change keeps the TFN/ABN without the reconstitution conditions
- NEVER split jointly owned rental income other than by legal title
- NEVER apply PAYG withholding or superannuation guarantee to partner drawings
- NEVER execute, value, or defend an Everett assignment -- flag, score, escalate
- NEVER treat a limited partnership under these rules -- Div 5A taxes it as a company
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
