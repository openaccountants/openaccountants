---
name: au-trust-distributions
description: >
  Use this skill whenever asked about Australian discretionary or family trust distributions -- trustee resolutions, present entitlement, section 95 net income versus trust income, streaming capital gains or franked distributions, minors' penalty rates under Division 6AA, section 99A trustee assessments, family trust elections, interposed entity elections, family trust distribution tax, section 100A reimbursement agreements, unpaid present entitlements after Bendel, TFN withholding for closely held trusts, or trust losses. Trigger on phrases like "trust distribution", "trustee resolution", "distribution minute", "streaming", "FTE", "FTDT", "s 100A", "bucket company", "UPE", or "30 June deadline". ALWAYS read this skill before touching any trust distribution work.
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

# Australia Trust Distributions -- Discretionary & Family Trusts Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context (three live fronts).** (1) *Commissioner of Taxation v Bendel* [2026] HCA 18 (10 June 2026): a UPE owed to a corporate beneficiary is not, of itself, a Div 7A loan; ATO decision impact statement 26 June 2026 accepts it -- see Rule 10 and the au-div7a skill. (2) Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Royal Assent 26 June 2026): from 1 July 2027 the 50% CGT discount for individuals, trusts and partnerships is replaced by cost base indexation plus a 30% minimum rate on capital gains, with new trustee capital-gain categorisation/statement obligations -- LAW, see Rule 14. (3) A 30% minimum tax on discretionary trust distributions from 1 July 2028 (testamentary trusts carved out) was ANNOUNCED in the 2026-27 Budget and is NOT in that Act -- consultation closed 31 July 2026, not yet law. Verify all three before relying.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Division 6 (ss 95-102), Div 6AA, Div 6D, Div 6E, s 100A; ITAA 1997 Subdivs 115-C, 207-B; Sch 2F ITAA 1936 (FTE/FTDT/trust losses) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season for 2025-26 |
| Present entitlement deadline | 30 June (11:59pm) -- or EARLIER if the deed requires |
| Capital-gain specific entitlement recording | Within 2 months of year end (31 August) via appointment of trust capital |
| Franked-distribution specific entitlement recording | By 30 June (in the trust's records, in its character) |
| s 99A rate (no present entitlement) | 45% + 2% Medicare levy = 47% flat, no tax-free threshold |
| Div 6AA minor's eligible income (resident) | $0-$416 nil; $417-$1,307 = 66% of excess over $416; over $1,307 = 45% of the WHOLE amount |
| Family trust distribution tax (FTDT) | 47% of distributions outside the family group; due 21 days after the distribution; non-deductible |
| TFN withholding (closely held trusts, no TFN quoted) | 47%; annual report 30 Sep; activity statement + payment 28 Oct; quarterly TFN report ABOLISHED from 1 July 2026 |
| UPE to corporate beneficiary | NOT a Div 7A loan while passive (*Bendel* [2026] HCA 18); s 100A and Subdiv EA survive -- see au-div7a |
| s 100A guidance | TR 2022/4 + PCG 2022/2 (white/green/red zones) -- in force, under post-Bendel review |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Deed not sighted | Do NOT assume trust income = s 95 net income; obtain the deed (income clause, default beneficiaries, vesting date, deadline for resolutions) |
| Resolution date unverified | Assume made AFTER 30 June; test the default-beneficiary clause, else s 99A at 47% |
| Streaming records unsighted | Assume NO specific entitlement -- gains and franked amounts flow proportionately |
| FTE status unknown | Check ATO records; assume no FTE for franking-credit flow-through; assume FTE EXISTS when scanning for FTDT exposure on unusual beneficiaries |
| Beneficiary's family-group status unknown | Assume OUTSIDE the group -- FTDT exposure at 47% until mapped |
| Minor beneficiary, income character unknown | Assume eligible (penalty rates), not excepted income |
| Beneficiary TFN status unknown | Assume not quoted -- 47% withholding exposure |
| UPE credit balance in the books | Passive UPE = no Div 7A loan (post-Bendel), but ALWAYS run the s 100A screen |
| Trust has carried-forward losses | Schedule 2F tests unresolved -- escalate before offsetting |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- trust deed (plus amendments), the signed distribution resolution/minute with its date, draft trust income and s 95 net income, beneficiary list with residency/age/TFN status, FTE/IEE status.

**Recommended** -- prior-year statements of distribution, beneficiary loan/UPE ledgers, franking account of any corporate beneficiary, capital gains schedule with acquisition dates, evidence of payment of entitlements.

**Ideal** -- family group map around the test individual, streaming clauses marked up in the deed, bank evidence of where entitlement cash actually went (s 100A), loss schedules with Sch 2F test evidence.

### Refusal catalogue

**R-AU-TR-1 -- Deceased estates and testamentary trusts.** *Trigger:* deceased estate in administration, testamentary trust, s 99 concessional-rate questions, excepted-income status of testamentary distributions to minors. *Message:* "Deceased estate and testamentary trust taxation (s 99 discretion, stages of administration, Div 6AA excepted income, and the announced minimum-tax carve-out) is out of scope. Escalate to a qualified practitioner."

**R-AU-TR-2 -- Special disability trusts.** *Trigger:* special disability trust or vulnerable-beneficiary trust. *Message:* "Special disability trusts have their own concessional rules and social-security interactions. Out of scope. Escalate."

**R-AU-TR-3 -- Non-resident beneficiaries or trustees.** *Trigger:* any non-resident beneficiary, foreign trust, or beneficiary who changed residency. *Message:* "Trustee assessment under s 98(2A)/(3)/(4), withholding, treaty issues and the *Greensill* line on capital gains are out of scope. Escalate before any resolution is signed."

**R-AU-TR-4 -- Circular trust distributions / TBNT.** *Trigger:* trust-to-trust distributions that loop back (directly or indirectly), or trustee beneficiary statement failures. *Message:* "Circular distributions attract trustee beneficiary non-disclosure tax at 47% (s 102UM) -- family trusts included. Computation and remediation are out of scope. Escalate."

**R-AU-TR-5 -- s 100A red-zone positions.** *Trigger:* facts matching any PCG 2022/2 red-zone scenario, or entitlement cash that went to someone other than the beneficiary. *Message:* "This has red-zone s 100A features. Document the flows; do not sign off or restructure. Escalate."

**R-AU-TR-6 -- Trust loss recoupment.** *Trigger:* prior-year losses claimed as deductions in net income. *Message:* "Schedule 2F testing (50% stake, control, pattern of distributions, income injection) is out of scope beyond the overview in Rule 13. Escalate."

**R-AU-TR-7 -- FTE revocation, variation or FTDT remediation.** *Trigger:* request to revoke/vary an FTE or IEE, or FTDT already triggered. *Message:* "Revocation and variation windows are narrow and FTDT is joint-and-several for directors. Escalate."

## Section 3 -- Distribution-resolution timeline and GL sweep

### 3.1 Compliance timeline (2025-26 year being lodged; same shape every year)

| Deadline | Obligation |
|---|---|
| Before 30 June (check deed -- some require earlier, e.g. 28 June) | Trustee resolution conferring present entitlement to trust income; written record if deed requires (write it regardless) |
| By 30 June | Franked-distribution streaming: specific entitlement recorded in trust records in its character (s 207-58) |
| By 31 August | Capital-gain streaming via appointment of trust CAPITAL: specific entitlement recorded within 2 months of year end (s 115-228) -- cannot override amounts already dealt with by 30 June |
| 21 days after distribution | FTDT payment where an FTE trust distributes outside the family group |
| By 30 September | Annual TFN withholding report (only if amounts were withheld) |
| By 14 October | Payment summaries to beneficiaries who had TFN amounts withheld |
| By 28 October | Annual activity statement + payment of TFN amounts withheld |
| Trust return lodgment | Statement of distribution (annual trustee payment report); beneficiary TFNs reported here from the 2027 return; TB statements where Div 6D applies |

### 3.2 GL / document sweep

| Pattern | Likely issue | Action |
|---|---|---|
| "Beneficiary loan" / "distribution payable" credit balances | UPEs | Age them; s 100A screen; post-Bendel no Div 7A while passive (au-div7a) |
| UPE unpaid beyond ~2 years with funds retained | Falls outside parts of the PCG 2022/2 green zone | Document green-zone conditions or escalate (T2-5) |
| Distributions exactly $416 to children | Div 6AA planning at the tax-free band | Confirm eligible vs excepted income; confirm actual payment/benefit |
| Distribution to a loss entity | Red zone scenario 5 if outside family group | s 100A screen; Sch 2F escalation |
| Franking credits claimed by beneficiary of non-fixed trust | Qualified-person rules | Confirm FTE in force (Rule 7) |
| First-time or unusual beneficiary | Family-group breach | Map against test individual; FTDT at 47% (Rule 8) |
| Trust lends cash to the person who funded a beneficiary's entitlement | Circular benefit | Red zone screen (R-AU-TR-5) |
| Resolution undated / signed with return | Backdating risk; s 99A | Sight contemporaneous evidence (emails, file notes) |

---

## Section 4 -- Worked examples

### Example 1 -- Proportionate approach (trust income vs s 95 net income)

Deed defines income as ordinary income. Trust income $100,000; s 95 net income $120,000 (non-deductible amounts and timing differences). Resolution: A 60%, B 40% of trust income.

Bamford proportionate approach: each beneficiary is assessed on their PERCENTAGE of net income, not the dollars they were promised. A: 60% x $120,000 = **$72,000**. B: 40% x $120,000 = **$48,000**. The $20,000 gap is taxed even though nobody can bank it -- flag to the client.

### Example 2 -- Streaming a capital gain and a franked dividend

2026-27 receipts: $80,000 gross capital gain (asset held > 12 months), $70,000 fully franked dividend (franking credit $70,000 x 30/70 = $30,000), $40,000 rent. Trustee validly streams: gain 100% to A (individual; capital appointment recorded 20 August 2027 -- inside 31 August), franked dividend 100% to C Pty Ltd (recorded by 30 June 2027), rent to B.

- A (Subdiv 115-C): attributable gain $40,000 (post-discount share) grossed up x2 = $80,000 capital gain in A's own return; A applies A's own 50% discount (no losses) = **$40,000 assessable**. (From 1 July 2027 this discount mechanic changes -- Rule 14.)
- C (Subdiv 207-B): includes $70,000 + $30,000 credit = $100,000; tax at 30% (bucket company is not a base rate entity on passive trust income) = $30,000 less $30,000 franking offset = **nil net**, franking account credited $30,000.
- B (Div 6/6E): assessed on the $40,000 rent share.

### Example 3 -- Minor beneficiaries (Division 6AA)

Resolutions give grandchild G1 (age 9) $416 and grandchild G2 (age 12) $1,200, both eligible (unearned) income; trustee assessed under s 98(1) as they are under a legal disability.

- G1: $416 sits in the $0-$416 band -> **tax nil** (assuming no other income).
- G2: 66% x ($1,200 - $416) = 66% x $784 = **$517.44** -- a 43% average rate on a $1,200 entitlement.
- Had G2 received $5,000: over $1,307, so 45% x THE WHOLE $5,000 = **$2,250** (plus Medicare levy where applicable; LITO cannot reduce tax on minors' unearned income).

Distributing eligible income beyond $416 per minor is almost always pointless. Excepted persons (e.g. minors in full-time work, certain disabled minors) and excepted income (employment, testamentary trust income, compensation, deceased estate income) escape Div 6AA -- testamentary questions escalate (R-AU-TR-1).

### Example 4 -- Family trust distribution tax

FTE in force, test individual David. Trustee distributes $20,000 to David's cousin. Cousins are OUTSIDE the s 272-90 family group.

FTDT = 47% x $20,000 = **$9,400**, payable by the trustee (directors of a corporate trustee jointly and severally liable), due 21 days after the distribution, non-deductible. The $20,000 is then excluded from the cousin's assessable income. There is no materiality threshold and no Commissioner discretion -- map the family group BEFORE every unusual distribution.

### Example 5 -- No resolution, no default clause (s 99A)

Deed requires a resolution by 30 June and names no default beneficiaries. The 2026-27 minute is signed 15 July 2027. Net income $150,000.

No beneficiary was presently entitled at 30 June -> trustee assessed under s 99A: 47% x $150,000 = **$70,500** flat (no tax-free threshold). A default-beneficiary clause would have rescued present entitlement -- but check WHO defaults: minor default beneficiaries swap a 47% problem for a Div 6AA one. The s 99 concessional alternative is confined to deceased estates and other Commissioner-discretion cases -- escalate (R-AU-TR-1).

### Example 6 -- s 100A red zone -> s 99A exposure

Adult child at university (marginal rate ~nil) is made presently entitled to $100,000. Under a pre-existing family understanding the cash is paid to the parents' loan offset; the child never benefits. This is PCG 2022/2 red zone scenario 1 (entitlement gifted/lent to another party).

If s 100A applies (TR 2022/4 elements: connection, benefit-to-another, tax-reduction purpose, not ordinary family/commercial dealing), the child's present entitlement is deemed never to have existed -> trustee assessed under s 99A: 47% x $100,000 = **$47,000**, and s 100A assessments are not sheltered by the standard amendment periods. Contrast the green zone: if the child had actually received and used the money, scenario 2 applies. *Guardian* confirms the agreement must exist at or before the entitlement is created; *BBlood* shows contrived dealings fail the ordinary-dealing exception. Escalate red-zone facts (R-AU-TR-5).

---

## Section 5 -- Tier 1 rules

### Rule 1 -- Division 6 architecture

s 95 "net income" = the trust's taxable income computed as if the trustee were a resident taxpayer. "Income of the trust estate" (distributable/trust income) is a TRUST-LAW amount fixed by the deed. Beneficiaries presently entitled and not under a legal disability are assessed under s 97 on their share of net income; trustees are assessed under s 98 for presently entitled beneficiaries under a legal disability (e.g. minors) and non-residents; s 99A (or rarely s 99) taxes the trustee on anything nobody is presently entitled to. Div 6E carves streamed capital gains and franked distributions out of the Div 6 math so Subdivs 115-C and 207-B can tax them instead (no double count).

### Rule 2 -- Present entitlement by 30 June and trustee resolutions

Present entitlement = a vested, indefeasible, immediately demandable interest in trust income, existing by 11:59pm 30 June. It is created by the deed (default clauses), by trustee resolution, or both. The ATO does not require writing unless the deed does -- but an unwritten resolution is unprovable, so ALWAYS have a signed, dated minute before 30 June (or the deed's earlier deadline). Entitlements must identify beneficiary and share (percentages beat dollar figures; include a balance clause). An invalid or late resolution hands the income to the default beneficiaries, or failing that to s 99A. Backdating is fraud -- never assist it.

### Rule 3 -- Proportionate approach (Bamford)

*FCT v Bamford* [2010] HCA 10: a beneficiary's assessable share = (beneficiary's share of TRUST income / total trust income) x s 95 NET income. Differences between the two amounts (depreciation clawbacks, non-deductibles, deed income clauses) change WHO pays tax, not how much income exists. Read the deed's income clause first: an "income equalisation" / s 95 clause aligns the amounts; a pure ordinary-income clause guarantees gaps in gain years.

### Rule 4 -- s 99A trustee assessment

Income to which no beneficiary is presently entitled (and no valid streaming applies) is assessed to the trustee at 45% + 2% Medicare levy = 47%, flat from the first dollar. s 99 (ordinary progressive rates) is available only where the Commissioner considers s 99A unreasonable -- in practice deceased estates and a few statutory trusts (escalate, R-AU-TR-1). Common causes: late/defective resolutions, distributing "income" the deed doesn't recognise, vesting-date breaches.

### Rule 5 -- Division 6AA minors' rates

Applies to "eligible taxable income" (unearned income, including discretionary trust distributions) of resident minors who are not excepted persons: $0-$416 nil; $417-$1,307 taxed at 66% of the excess over $416; over $1,307 the ENTIRE amount at 45% (cliff, not marginal). Non-resident minors get no tax-free band: $0-$416 at 30% of the entire amount (the non-resident first rate from 2024-25), then 66% of the excess, then 45% of the whole amount (ATO "Tax rates if you're under 18 years old"). The trustee pays under s 98(1) while the minor is under a legal disability; the minor also returns the share with a credit for the trustee's tax if they must lodge. LITO cannot offset Div 6AA tax. Excepted income (employment, testamentary trusts, compensation, inheritances) is taxed at adult rates -- verify character before assuming.

### Rule 6 -- Streaming capital gains (Subdiv 115-C)

A beneficiary is "specifically entitled" to a capital gain to the extent they have received, or can reasonably expect to receive, the financial benefit referable to the gain AND that entitlement is recorded in its character in the trust's accounts/records by the deadline: 30 June where the gain forms part of trust income, or 31 August (2 months after year end) where the trustee appoints trust CAPITAL. The deed must permit streaming. The specifically entitled beneficiary grosses up their attributable gain and applies their own discount/losses; unstreamed gains flow proportionately, and gains nobody is presently or specifically entitled to are assessed to the trustee (s 115-222) at 47%. You cannot create a specific entitlement after 30 June over amounts a default beneficiary already became presently entitled to.

### Rule 7 -- Streaming franked distributions (Subdiv 207-B)

Franked distributions and their credits follow the beneficiary specifically entitled, recorded in the trust's records IN CHARACTER by 30 June -- no 31 August grace. Credits require the beneficiary/trustee to be a "qualified person" (45-day holding rule); for a discretionary (non-fixed) trust, beneficiaries generally CANNOT be qualified persons for credits > $5,000 unless a family trust election is in force. Small individual beneficiaries: the $5,000 franking-credit ceiling applies per taxpayer, not per trust.

### Rule 8 -- FTE, IEE and family trust distribution tax

An FTE (s 272-80 Sch 2F) makes the trust a "family trust" for: trust-loss testing (only the modified income injection test), franking-credit flow-through (Rule 7), company loss tracing, and trustee-beneficiary reporting exclusions. The election names a test individual; the family group (s 272-90) is roughly the test individual, spouse, lineal ancestors/descendants, siblings, nieces/nephews, their spouses, family companies/trusts/partnerships with IEEs, and certain charities. An IEE (s 272-85) brings an entity into the group. THE PRICE: any conferral/distribution of income or capital outside the group triggers FTDT at 47% (Div 271), payable by the trustee -- directors jointly and severally -- due 21 days after the distribution, non-deductible, with the amount excluded from the recipient's assessable income. Elections are effectively permanent: revocation/variation windows are narrow (escalate, R-AU-TR-7). Review the group EVERY year before signing resolutions.

### Rule 9 -- s 100A reimbursement agreements

**AUDIT FLASH POINT**

s 100A strikes where a beneficiary's present entitlement arises from a "reimbursement agreement" -- someone other than the beneficiary gets the benefit, a purpose of the arrangement is that somebody pays less tax, and the dealing is not ordinary family or commercial dealing. Beneficiaries under a legal disability are outside it. Consequence: the entitlement is ignored and the trustee is assessed under s 99A at 47%, with no standard amendment-period shelter. Current framework:

- **TR 2022/4** -- ATO's view of the elements (connection, benefit-to-another, purpose, ordinary-dealing exception).
- **PCG 2022/2** risk zones: WHITE = arrangements in years ended before 1 July 2014 (no new compliance resources, limited exceptions); GREEN = documented low-risk scenarios (entitlement paid to and used by the beneficiary or their family; funds retained by the trustee on documented terms; TR 2022/4 ordinary-dealing examples) -- document how you qualify; RED = priority review/audit: entitlements gifted or lent back, income round-robined to the trust, unit-issue set-offs, share-of-net-income >> entitlement, loss beneficiaries outside the group, Taxpayer Alert arrangements (e.g. TA 2022/1 -- parents enjoying adult children's entitlements).
- **Cases:** *Guardian AIT* ([2021] FCA 1619; [2023] FCAFC 3) -- no reimbursement agreement where none existed when the entitlement was created; Part IVA partially succeeded instead. *BBlood* ([2022] FCA 1112; upheld [2023] FCAFC 89; special leave refused 2024) -- s 100A applied to a contrived buy-back arrangement.
- **Post-Bendel posture:** TR 2022/4 and PCG 2022/2 remain IN FORCE but under review; with the Div 7A route to UPEs closed, s 100A is the ATO's primary lever on trust entitlements that don't reach the named beneficiary. Expect s 100A questions wherever UPE balances age.

### Rule 10 -- UPEs to corporate beneficiaries post-Bendel

*Bendel* [2026] HCA 18: a UPE owed to a corporate beneficiary is not "financial accommodation" and so not a Div 7A loan while the company stays PASSIVE. ATO DIS 26 June 2026 accepts this. Still live: (1) s 100A on the arrangement creating the UPE; (2) Subdiv EA (trust pays/lends to the company's shareholders while the UPE is unpaid); (3) any ACTIVE step -- conversion to a loan, promissory note, call for payment -- can create a real s 109D loan from that point; (4) the announced UPE/Div 7A legislative response (2018-19 Budget measure, still unenacted) and the announced 30% minimum trustee tax (Rule 14). Full mechanics, guidance-status table and examples: **au-div7a skill, Rule 11** -- read it before touching any bucket-company structure.

### Rule 11 -- TFN withholding (closely held trusts)

Beneficiaries of closely held trusts (discretionary trusts and trusts with < 20 members holding >= 75%) must quote their TFN before being paid or made presently entitled; otherwise the trustee withholds at 47% from the payment/entitlement (to the extent of the share of net income), registers for PAYG withholding (closely held), lodges an Annual TFN withholding report by 30 September, gives payment summaries by 14 October, and pays via annual activity statement by 28 October. Exclusions: beneficiaries under a legal disability, non-residents, exempt entities, amounts subject to FTDT or a TB statement, s 98 liabilities, and entitlements under $120 for the year. From 1 July 2026 the quarterly TFN report is ABOLISHED (final report for April-June 2026 was due 31 July 2026); beneficiary TFNs are instead reported in the statement of distribution in the trust return (2027 return onward). Withholding obligations themselves are unchanged.

### Rule 12 -- Trustee beneficiary statements and circular distributions (Div 6D)

A closely held trust distributing a share of net income to a TRUSTEE beneficiary must make a TB statement in the return; failure = trustee beneficiary non-disclosure tax at 47% on the untaxed part. s 102UM imposes TBNT where a distribution ultimately circles back to the originating trust -- and since 1 July 2019 this catches FAMILY trusts too (an FTE does not immunise round-robins). Any loop pattern -> refuse and escalate (R-AU-TR-4).

### Rule 13 -- Trust losses (Schedule 2F) -- overview only

Carried-forward trust losses are deductible only if the trust passes the relevant tests: non-fixed trusts face the 50% stake test (where applicable), control test, pattern of distributions test, and income injection test; family trusts (FTE in force) face only a modified income injection test. This is the main practical reason FTEs exist. Do not compute recoupment from this skill -- escalate (R-AU-TR-6).

### Rule 14 -- 2026 reform landscape: what IS law vs what is ANNOUNCED

| Measure | Status (verified 20 August 2026) |
|---|---|
| Treasury Laws Amendment (Tax Reform No. 1) Act 2026 + Income Tax Rates Amendment (Tax Reform No. 1) Act 2026 | **LAW** -- Royal Assent 26 June 2026 |
| 50% CGT discount for individuals, trusts, partnerships replaced by cost base indexation + 30% minimum rate on capital gains (direct or through trusts) | **LAW**, applies from 1 July 2027, and only to gains accruing after that date; discount retained for eligible new dwellings/affordable housing |
| New trustee obligations to categorise capital gains and issue statements so beneficiaries can apply indexation and the 30% minimum rate | **LAW**, from 1 July 2027 -- detailed ATO forms/guidance still emerging; verify before building 2027-28 templates |
| Pre-CGT (pre-20 Sep 1985) status ends after 30 June 2027; capital losses ordered against discounted gains first; SBE 50% reduction turnover threshold $2m -> $10m | **LAW** (same Act) |
| 30% minimum tax on TRUSTEE distributions of discretionary trusts from 1 July 2028 (trustee-level tax on s 95(1) net income; non-refundable offset for individual beneficiaries; corporate beneficiaries DENIED the offset; franking credits proposed to stop flowing through; directors jointly/severally liable) | **ANNOUNCED, NOT LAW** -- 2026-27 Budget (12 May 2026); Treasury consultation paper 8 July 2026, consultation closed 31 July 2026; expected in a LATER bill |
| Carve-outs from the announced minimum tax: testamentary trusts (pre-1 July 2028 trusts excluded if genuinely testamentary and assets from the estate or injected before 12 May 2026; later ones only if beneficiaries limited to individuals/tax-exempts), fixed trusts, widely held trusts, complying super funds, special disability trusts, deceased estates, charities, primary production income, Div 6AA vulnerable-minor categories | **ANNOUNCED, NOT LAW** -- design still in consultation |
| Restructure rollover relief (Subdiv 328-G-style, from 1 July 2027, ~3 years) out of discretionary trusts | **ANNOUNCED, NOT LAW** |

Never present an announced measure as enacted, and never advise restructures around it -- note it, quantify nothing, escalate planning (T2-6).

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Deed income clause vs s 95

**Trigger:** deed not sighted, or income clause silent on capital gains/franking gross-up. **Issue:** streaming power and Bamford percentages both hang off the deed. **Action:** obtain and quote the clause; if the deed lacks streaming powers, streaming fails regardless of records.

### T2-2 -- Disclaimers, variations and late "fixes"

**Trigger:** beneficiary wants to disclaim after year end, or trustee wants to "amend" a resolution. **Issue:** disclaimers can trigger s 99A and green-zone exclusions; amendments after 30 June cannot create present entitlement retrospectively. **Action:** escalate; document only.

### T2-3 -- Bucket company with no cash movement

**Trigger:** corporate beneficiary entitlements accrue year after year, never paid. **Issue:** passive UPEs are Div 7A-safe post-Bendel but are s 100A magnets and the company still returns the s 97 share -- tax without cash. **Action:** run the au-div7a UPE screen; confirm the company actually returned its shares of net income.

### T2-4 -- Part IVA overlay

**Trigger:** arrangement survives s 100A but exists mainly to route income at lower rates (cf. *Guardian* round two). **Issue:** general anti-avoidance is a live fallback for the ATO. **Action:** flag dominant-purpose facts; escalate.

### T2-5 -- Aged UPEs and the green-zone clock

**Trigger:** individual-beneficiary entitlements retained by the trustee beyond 2 years, or undocumented retention terms. **Issue:** parts of the PCG 2022/2 green zone expressly exclude prolonged retention; documentation is a green-zone entry condition. **Action:** document lending/retention terms or escalate.

### T2-6 -- Announced 30% minimum trustee tax horizon

**Trigger:** structuring, FTE, or bucket-company decisions with effect past 1 July 2028. **Issue:** announced-not-law measure would tax trustees at 30% with corporate beneficiaries denied the offset (effective rates to ~60-70% on corporate chains per Treasury's consultation design). **Action:** note on all forward-looking advice; escalate planning; never model it as enacted.

### T2-7 -- Vesting date and appointor checks

**Trigger:** old deed (pre-1990s), unclear appointor succession, or vesting date within 5 years. **Issue:** distributions after vesting are void; appointor gaps break resolutions. **Action:** flag for legal review.

---

## Section 7 -- Excel working paper template

```
AUSTRALIA TRUST DISTRIBUTIONS -- WORKING PAPER
Trust: [name]   Income year: 2026-27   Deed sighted: [YES/NO + date]
Prepared: [date]

DEED CHECKS
  Income clause type:            [ordinary income / s 95 equalisation / other]
  Streaming powers:              [YES/NO -- clause ref]
  Default beneficiaries:         [names / NONE]
  Resolution deadline per deed:  [30 June / earlier: ____]
  Vesting date:                  [____]
  FTE / IEE status:              [FTE year + test individual / none]

INCOME RECONCILIATION
  Trust (distributable) income:  AUD [____]
  s 95 net income:               AUD [____]
  Difference explained:          [____]

RESOLUTION REGISTER (per beneficiary)
  Name / TFN quoted / residency / age:  [____]
  Family-group member:           [YES/NO/UNKNOWN -> FTDT check]
  Share of trust income:         [% and AUD]
  Assessed share of net income (Bamford %):  AUD [____]
  Streamed amounts (character):  [capital gain / franked + credits]
  Recording deadline met:        [30 Jun franked / 31 Aug capital -- evidence]
  Minor? Div 6AA band:           [nil / 66% band / 45%]
  Entitlement PAID or UPE:       [paid date / UPE balance]
  s 100A zone assessment:        [white/green/red + why]

TRUSTEE-ASSESSED AMOUNTS
  s 99A income (no entitlement): AUD [____] x 47% = AUD [____]
  s 98 amounts (minors/non-residents -- escalate non-residents): AUD [____]

WITHHOLDING / FTDT
  TFN withholding 47%:           AUD [____]  (report 30 Sep; pay 28 Oct)
  FTDT events:                   AUD [____] x 47% = AUD [____] (due 21 days)

REVIEWER FLAGS
  [Tier 2 flags, refusals triggered, reform-horizon notes]
```

---

## Section 8 -- Reading guide

1. Deed first, always: income clause, streaming powers, default beneficiaries, deadlines, vesting date. Every later step depends on it.
2. Date-stamp the resolution before anything else -- a perfect resolution signed 1 July is a 47% problem.
3. Reconcile trust income to s 95 net income before allocating; the Bamford percentage applies to net income.
4. Sweep beneficiary loan/UPE accounts: aged UPEs are the s 100A and Bendel intersection.
5. Map the family group annually where an FTE exists -- FTDT has no de minimis.
6. Minors: check the character of what they receive before assuming penalty rates (or assuming they don't apply).
7. Label every 2026 reform item as LAW (Tax Reform No. 1 Act, from 1 July 2027) or ANNOUNCED (30% trustee minimum tax, from 1 July 2028) -- never blur them.

---

## Section 9 -- Onboarding fallback

If the client provides only financial statements and a trial balance:

1. Pull trust income and any "distributions" from equity/liability movements; list beneficiary credit balances as UPE candidates
2. Build the resolution register with resolution date UNKNOWN flagged; request the signed minutes and the deed
3. Recompute Bamford shares from stated percentages against net income per the return workpapers
4. Screen every UPE for s 100A zone features; screen every beneficiary against the (unconfirmed) family group
5. **Flag:** "Prepared from financial statements only. Deed, signed resolutions, streaming records, TFN evidence and FTE status not sighted. Present entitlement at 30 June unverified -- s 99A exposure unquantified. Reviewer must confirm before lodgment."

---

## Section 10 -- Reference material

### Key figures

| Item | Value |
|---|---|
| s 99A / FTDT / TFN-withholding / TBNT rate | 47% (45% + 2% Medicare levy) |
| Div 6AA minor bands (resident) | $416 nil / $417-$1,307 at 66% of excess over $416 / > $1,307 at 45% of whole |
| Streaming recording deadlines | Franked: 30 June. Capital gains via capital appointment: 31 August |
| FTDT due date | 21 days after distribution (or after election if later) |
| TFN withholding calendar | Report 30 Sep; payment summaries 14 Oct; pay 28 Oct; quarterly TFN report abolished 1 July 2026 |
| TFN withholding de minimis | $120 per beneficiary per year |
| Franking-credit ceiling without FTE (non-fixed trust) | $5,000 per beneficiary |
| CGT reform start (LAW) | 1 July 2027 (indexation + 30% minimum rate; trustee statements) |
| Trustee minimum tax (ANNOUNCED, not law) | 30% from 1 July 2028; testamentary and other carve-outs under consultation |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Division 6, 6AA, 6D, 6E, s 99A, s 100A | ITAA 1936 (current compilation, legislation.gov.au); ITAA 1997 Subdivs 115-C, 207-B |
| Minor rates | ato.gov.au -- Tax rates if you're under 18 years old; Income Tax Rates Act 1986 |
| Trustee resolutions & streaming deadlines | ato.gov.au -- Trustee resolutions checklist (QC 25912); Becoming specifically entitled |
| Proportionate approach | *FCT v Bamford* [2010] HCA 10 |
| s 100A | TR 2022/4; PCG 2022/2 (8 Dec 2022); *Guardian* [2023] FCAFC 3; *BBlood* [2022] FCA 1112, [2023] FCAFC 89; TA 2022/1 |
| Bendel / UPEs | [2026] HCA 18 (10 June 2026); ATO decision impact statement 26 June 2026; au-div7a skill Rule 11 |
| FTE / FTDT | ato.gov.au -- Family trusts (FTDT 47%, due 21 days, joint & several directors); Sch 2F ITAA 1936 |
| TFN withholding | ato.gov.au -- TFN withholding for closely held trusts: What trustees need to do (QC 23140, updated 16 July 2026); Changes to beneficiary TFN reporting (QC 107776, 14 July 2026) |
| Circular distributions | s 102UM ITAA 1936; Treasury Laws Amendment (2019 Tax Integrity and Other Measures No. 1) Act 2019 |
| 2026 reforms | Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Assent 26 June 2026); ATO -- Reforming negative gearing and CGT (QC 107304, updated 29 June 2026); 2026-27 Budget (12 May 2026); Treasury consultation paper 8 July 2026 |

### Test suite

**Test 1:** Trust income $100,000, net income $120,000, 50/50 resolution. -> Each beneficiary assessed on $60,000.

**Test 2:** No resolution, no default clause, net income $80,000. -> s 99A: $37,600.

**Test 3:** Resident minor's eligible trust income $416 -> nil. $1,200 -> $517.44. $10,000 -> $4,500 (whole amount at 45%), before Medicare levy.

**Test 4:** Capital-gain streaming minute signed 15 September. -> Too late (31 August); gain flows proportionately or to the trustee at 47%.

**Test 5:** Franked-distribution streaming recorded 15 July. -> Too late (30 June); credits follow the proportionate/adjusted Div 6E shares instead.

**Test 6:** FTE trust distributes $50,000 to a beneficiary outside the family group. -> FTDT $23,500, due 21 days after the distribution; excluded from recipient's assessable income.

**Test 7:** Beneficiary refuses to quote a TFN; entitlement $1,000. -> Withhold $470 at the time of entitlement; report by 30 Sep; pay by 28 Oct.

**Test 8:** UPE to bucket company sits unpaid, company passive. -> No Div 7A loan (*Bendel*); run s 100A / Subdiv EA screens per au-div7a; corporate beneficiary still assessed on its s 97 share.

**Test 9:** Trust A distributes to Trust B which distributes back to Trust A. -> s 102UM TBNT at 47% even with an FTE; refuse and escalate.

**Test 10:** Client asks you to apply the 30% trustee minimum tax to 2026-27 distributions. -> Refuse: announced-not-law, proposed start 1 July 2028; the ENACTED changes start 1 July 2027 and concern CGT.

### Prohibitions

- NEVER backdate, or help reconstruct after 30 June, a trustee resolution
- NEVER assume trust income equals s 95 net income without the deed
- NEVER stream a capital gain recorded after 31 August or a franked distribution recorded after 30 June
- NEVER apply adult rates to a minor's eligible trust income -- and never assume Div 6AA applies to excepted income
- NEVER let an FTE trust distribute to an unmapped beneficiary without pricing FTDT at 47%
- NEVER treat a passive UPE as a Div 7A loan post-Bendel -- and NEVER skip the s 100A / Subdiv EA screen
- NEVER claim green-zone protection without documenting how the scenario conditions are met
- NEVER present the announced 30% minimum trustee tax (or any consultation design detail) as law
- NEVER compute trust loss recoupment, non-resident trustee assessments, or TBNT without escalating
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
