---
name: au-deceased-estates
description: >
  Use this skill whenever a client has died or a deceased estate needs tax work -- the
  date-of-death final return and DECEASED annotation, notifying the ATO, trust returns
  for the estate, stages of administration and present entitlement under IT 2622,
  section 99 concessional rates for the first three income years versus the compressed
  year-4+ bands, Division 128 CGT on death, the 2-year main residence window and PCG
  2019/5, CGT event K3, super death benefits via the estate, testamentary trusts, and
  losses that die with the deceased. Trigger on "deceased estate", "date of death
  return", "executor tax", "inherited property CGT".
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

# Australia Deceased Estates -- Date-of-Death Returns, Estate Trust Returns & Death CGT Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context (three live fronts, verified 20 August 2026).** (1) The enacted individual rate cut (16% -> 15% from 1 July 2026, -> 14% from 1 July 2027) flows into date-of-death returns and the first-3-years concessional estate rates for 2026-27; the ATO's published year-4+ compressed bands are current only to 2025-26 -- see Rule 5. (2) Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Royal Assent 26 June 2026): from 1 July 2027 the 50% CGT discount is replaced by cost base indexation plus a 30% minimum rate on capital gains, and pre-CGT (pre-20 September 1985) status ends after 30 June 2027 -- this is LAW and interacts with Div 128 legatee cost bases (Rule 14). (3) The announced 30% minimum tax on discretionary trust distributions from 1 July 2028 explicitly CARVES OUT testamentary trusts and deceased estates -- ANNOUNCED, NOT LAW (Rule 13). Verify all three before relying.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Div 6 (ss 95-99A), s 101A, Div 6AA & s 102AG; ITAA 1997 Div 128, Subdiv 118-B (s 118-195), s 104-215 (CGT event K3), Div 302 |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season for 2025-26 |
| Date-of-death (final) return | 1 July to date of death; FULL tax-free threshold (not pro-rated); Medicare levy applies as for a normal individual year; paper form or via appointed tax agent -- never myTax |
| If no final return needed | Non-lodgment advice marked 'DECEASED' + date of death |
| Estate trust returns | LPR/executor is "trustee" (s 6(1) ITAA 1936); estate needs its OWN TFN; first income year = day after death to 30 June |
| Estate years 1-3 (s 99) | Resident individual rates WITH full $18,200 tax-free threshold; NO Medicare levy; NO tax offsets (no LITO) |
| Estate year 4+ (s 99) | Compressed bands -- threshold collapses to $416 (2025-26: $417-$611 at 50% of excess; $612-$45,000 at $97.76 + 16% of excess over $611, whole amount taxed from $0 once over $611) |
| Death and CGT | NOT a CGT event where the asset passes to the LPR or a beneficiary (Div 128 rollover); K3 override for exempt entities, super funds and foreign-resident beneficiaries |
| Inherited main residence | Full exemption if contract settles within 2 years of death (s 118-195); PCG 2019/5 automatic safe harbour extension up to 18 months |
| Super death benefit via LPR | Fund withholds NIL; trustee taxed on the share expected to benefit non-dependants at up to 15% (taxed element) / 30% (untaxed) with NO Medicare levy |
| Losses | Carried-forward revenue AND capital losses die with the deceased -- no transfer to the estate or beneficiaries |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Probate status unknown | Treat administration as INCOMPLETE -- no present entitlement; trustee assessed |
| Administration completion date unverified | Assume not complete; s 99 trustee assessment, not beneficiary returns |
| Which estate income year unclear | Count income years from the day after death (a part-year counts as year 1); assume year 4+ compressed bands until the count is proven |
| Beneficiary residency unknown | Assume foreign resident -- screen every in-specie asset for CGT event K3 and trustee assessment exposure |
| Dwelling's status at death unknown | Assume NOT the deceased's main residence and NOT pre-CGT -- no s 118-195 exemption until evidenced |
| 2-year window missed, extension claimed | Assume PCG 2019/5 conditions NOT met until each of the 5 conditions is documented |
| Super death benefit recipient's dependancy unknown | Assume NON-dependant for tax purposes (adult child default) -- 15%/30% exposure |
| Asset history unsighted | Assume post-CGT asset at the deceased's (unknown) cost base -- obtain records before computing anything |
| Testamentary trust asset provenance unknown | Assume s 102AG(2AA) NOT satisfied -- minors' penalty rates until will-derivation is traced |
| Pre-death income received post-death | Income of the ESTATE (s 101A), not the final return |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- death certificate date, the will (or intestacy position), probate/letters of administration status and date, income records straddling death, prior-year lodgment history, asset schedule with acquisition dates and cost bases, beneficiary list with residency/age.

**Recommended** -- ATO deceased estate data package (3 years of returns, income data, NOAs, debts, super accounts), estate bank statements by administration stage, dwelling occupancy history, super fund death benefit statements with component breakdown, distribution history.

**Ideal** -- solicitor's administration timeline (debts paid/provided for), evidence of the date administration completed, valuations at date of death (pre-CGT assets and main residence), BDBN documents, testamentary trust deed with asset provenance trace.

### Refusal catalogue

**R-AU-DE-1 -- Probate and estate legal advice.** *Trigger:* grant applications, will interpretation, executor appointment/removal, executor duties disputes, intestacy entitlements. *Message:* "Probate and estate administration are legal practice, not tax. Engage an estates lawyer; this skill resumes once the LPR's authority and the administration timeline are documented."

**R-AU-DE-2 -- Family provision claims.** *Trigger:* a family provision / testator's family maintenance claim (actual or threatened), or distributions being delayed by one. *Message:* "Family provision claims change who takes what and can reopen the CGT and s 118-195 analysis. Legal matter -- flag the tax consequences of any settlement to the estate lawyer and escalate."

**R-AU-DE-3 -- Super death benefit disputes.** *Trigger:* contested trustee discretion, claim-staking objections, AFCA complaints, BDBN validity challenges. *Message:* "Death benefit payment disputes are superannuation law and fund-rules territory. Out of scope beyond the tax treatment of whatever is ultimately paid. Escalate."

**R-AU-DE-4 -- Foreign estates and non-resident parties beyond flagging.** *Trigger:* non-resident deceased, foreign LPR, estate administered offshore, Australian beneficiary of a FOREIGN estate (s 99B exposure), treaty questions. *Message:* "This skill only FLAGS non-resident issues (K3, trustee assessment under s 98, s 99B on foreign-estate distributions). Computation and treaty analysis are out of scope. Escalate before any distribution."

**R-AU-DE-5 -- Insolvent estates.** *Trigger:* estate liabilities exceed assets, Part XI Bankruptcy Act administration, creditor priority questions. *Message:* "Insolvent estate administration has its own priority and personal-liability regime for the LPR. Out of scope. Escalate to an insolvency practitioner and estates lawyer."

**R-AU-DE-6 -- Testamentary trust drafting and structuring.** *Trigger:* requests to design, draft or amend testamentary trust terms, or to plan will structures around the announced minimum tax. *Message:* "Testamentary trust drafting is legal work, and structuring around announced-not-law measures is premature. This skill covers only the tax treatment of an EXISTING testamentary trust. Escalate."

## Section 3 -- Administration timeline and estate-year decision tables

### 3.1 Stages of administration (IT 2622) -- who is assessed

| Stage | Facts | Present entitlement? | Assessed to | Rate |
|---|---|---|---|---|
| 0. Death | Final individual return, 1 July to date of death | n/a | Deceased (LPR lodges) | Individual rates, full threshold, Medicare levy |
| 1. Initial (to grant of probate/LoA) | Debts unquantified; *Whiting*: no beneficiary can be presently entitled | NO | Trustee, s 99 | Estate rates (3.2) |
| 2. Intermediate (grant to residue ascertained) | Trustee MAY pay interim distributions if remainder clearly covers liabilities | Only to amounts ACTUALLY PAID to (or applied for) a beneficiary | Beneficiary s 97 (or trustee s 98 for minors/non-residents) on paid amounts; trustee s 99 on the rest | Beneficiary marginal / estate rates |
| 3. Final (debts paid or provided for; residue ascertained) | Administration complete -- even if transfers not yet executed | YES -- residuary beneficiaries presently entitled | Beneficiaries s 97; trustee s 98 for legal-disability/non-resident beneficiaries | Beneficiary marginal rates |
| Completion-year practice | Administration completes mid-year | ATO practice (IT 2622 paras 17-19) | Beneficiaries assessed on their share of the FULL year's net income; OR apportion (pre-completion income to trustee, post-completion to beneficiaries) if actual derivation is evidenced AND apportionment is requested | Mixed |

### 3.2 Estate trustee rates (s 99), no present entitlement

| Estate income year | Rates |
|---|---|
| Years 1-3 (year 1 = day after death to 30 June) | Resident individual rates + FULL $18,200 threshold; NO Medicare levy; NO offsets (no LITO); applied for in the first trust return; cannot be extended past year 3 |
| Year 4 onwards (2024-25 and 2025-26 published table) | $0-$416 nil; $417-$611 50% of excess over $416; $612-$45,000 $97.76 + 16% of excess over $611 (once over $611 the WHOLE amount is effectively taxed at 16%); $45,001-$135,000 $7,200 + 30%; $135,001-$190,000 $34,200 + 37%; $190,001+ $54,550 + 45%. NO Medicare levy |
| Year 4 onwards, 2026-27 | 16% -> 15% rate cut is LAW; ATO has not yet republished the compressed band boundaries (the $611/$97.76 shade-in constants derive from the 16% rate and will change) -- verify QC 49909 before lodging any 2026-27 estate return |

The year-4+ compression is deliberate anti-prolongation policy: parking income in a long-running estate stops being concessional after three years, so there is no rate incentive to leave administration open. s 99A (47% flat) is the default for trusts generally; resident deceased estates get s 99 treatment in practice unless property has been injected into the estate or the Commissioner otherwise considers s 99A appropriate (s 99A(2) factors).

### 3.3 First-90-days checklist (LPR tax workflow)

| Step | Detail |
|---|---|
| Notify the ATO of the death | Australian Death Notification Service or ATO notification form; the deceased's agent links are SEVERED on death -- the former tax agent has no authority |
| Establish authority | Grant of probate / letters of administration -> become the "authorised LPR" on ATO records; an executor WITHOUT a grant is not an authorised LPR |
| Get the data package | 3 years of returns, income/investment data, NOAs, statement of account, ATO debts, super accounts, current-year payroll -- issued to the authorised LPR or their appointed agent |
| Estate TFN | Apply for a NEW TFN for the estate trust; never lodge trust returns under the deceased's TFN |
| Final return | Lodge if tax was withheld, taxable income exceeded the threshold, or returns were lodged/outstanding in prior years; else non-lodgment advice marked 'DECEASED' + date of death; paper form headed 'LEGAL REPRESENTATIVE OF [name] (DECEASED)' |
| Outstanding prior years | Lodge any outstanding pre-death returns |
| Provide for tax before distributing | The LPR is personally liable (up to the value of estate assets) for tax not provided for -- PCG 2018/4 sets out the ATO's practical liability approach and notification/waiting safe harbour |

---

## Section 4 -- Worked examples (2025-26 rates -- the year being lodged)

### Example 1 -- Final return: part-year income, full threshold, franking refund

Leo died 31 October 2025. Salary to date of death $48,000 (PAYG withheld $9,000); fully franked dividend $1,400 (franking credit $600) paid 15 October 2025. Taxable income = 48,000 + 1,400 + 600 = **$50,000**.

Tax at 2025-26 resident rates with the FULL threshold (never pro-rated for a part year): 16% x (45,000 − 18,200) = $4,288; + 30% x (50,000 − 45,000) = $1,500 -> $5,788. LITO applies (this is an ordinary individual return, unlike the estate assessments in Rule 4): $325 − 1.5% x (50,000 − 45,000) = $250, so $5,538. Medicare levy 2% x 50,000 = $1,000. Less franking offset $600 (refundable in a final return). Net $5,938; withheld $9,000 -> **refund $3,062**, released to the authorised LPR. Four months of income against a full-year threshold and withholding scales makes a refund the normal outcome -- lodge even when marginal. The November salary run and any dividends paid after 31 October are NOT in this return: they are estate income (Rule 10).

### Example 2 -- Estate year 2: s 99 concessional assessment

Leo's estate (year 1 was 1 November 2025 - 30 June 2026) derives net income of $30,000 in 2026-27 (year 2); administration incomplete, nothing paid out. No beneficiary is presently entitled -> trustee assessed under s 99 at individual rates with the full threshold and NO Medicare levy. At 2025-26 rates: 16% x (30,000 − 18,200) = **$1,888.00**. (For the actual 2026-27 assessment the enacted 15% rate gives 15% x 11,800 = $1,770.00 -- confirm the ATO 2026-27 tables at lodgment.) No LITO: a living individual on $30,000 would pay less after offsets; estates get rates and threshold only.

### Example 3 -- Estate year 5: compressed bands and the anti-prolongation cliff

Same estate still open in year 5 with $30,000 net income (2025-26 published bands): $97.76 + 16% x (30,000 − 611) = 97.76 + 4,702.24 = **$4,800.00** -- exactly 16% of the whole amount, because once income exceeds $611 the nil and 50% bands wash out. The identical income in year 2 cost $1,888. Prolonging administration past year 3 cost $2,912 on this income alone. (At $500 of income the tax is 50% x (500 − 416) = **$42.00** -- the compressed bands only shelter trivial amounts.)

### Example 4 -- Inherited dwelling: month 20 vs month 30

Nina died 1 September 2024. Her home (acquired 2001, main residence, never income-producing) passes to her son Marco, who rents it out. Cost base = market value at death, $900,000 (s 128-15(4) item 3). Sale proceeds $1,000,000 less $20,000 selling costs; gain **$80,000**.

- **Contract settles May 2026 (month 20):** within 2 years of death -> s 118-195 FULL exemption. Renting during the window is irrelevant -- the 2-year disposal limb ignores post-death use. Tax **nil**.
- **Settles March 2027 (month 30), no eligible occupant, no extension:** full exemption fails; with nobody in s 118-195 occupation, the post-death period is non-exempt and the partial-exemption formula (s 118-200) leaves the whole $80,000 taxable. Marco's discount clock runs from Nina's 2001 acquisition (s 115-30) -> 50% discount -> $40,000 assessable; at a 37% + 2% marginal stack that is **$15,600**.
- **PCG 2019/5 rescue:** if >12 months of the first 2 years was consumed by a listed circumstance (will challenge, life/equitable interest, estate complexity, settlement collapse beyond control, COVID restrictions), the dwelling was listed as soon as practicable, settlement occurred within 12 months of listing, none of the disqualifying factors (waiting out the market, refurbishment for price, inconvenience, unexplained executor inactivity) materially contributed, and the extension needed is <= 18 months -- the extension is AUTOMATIC and no application is made; retain the evidence. Outside the safe harbour: written discretionary request to the Commissioner.

### Example 5 -- CGT event K3: shares to a non-resident daughter

Iris (Australian resident) dies holding ASX shares: market value at death $300,000, cost base $120,000, held since 2015. Her will leaves them to her daughter in London (foreign resident). Listed shares are not taxable Australian property in the daughter's hands -> **CGT event K3** (s 104-215): the event happens JUST BEFORE death, and the $180,000 gain goes in **Iris's date-of-death return** -- the estate does not pay it, the final return does. Iris's $10,000 carried-forward capital losses (which would otherwise die -- Rule 11) absorb first: (180,000 − 10,000) x 50% discount = **$85,000 net capital gain** in the final return. If the shares pass years later when administration completes, the final return must be AMENDED. Contrast: same shares to her resident son -> no CGT event, rollover at $120,000 cost base with the 2015 acquisition date. If the asset were Australian real property (TAP), K3 would NOT happen -- rollover applies and Australia taxes the foreign beneficiary on eventual sale. Pre-CGT assets: any K3 gain is disregarded (s 104-215(5)). Which beneficiary takes which asset is will-drafting territory -- flag, never advise (R-AU-DE-1).

### Example 6 -- Super death benefit: adult child direct vs via the estate

Ken dies with $500,000 super: tax-free component nil, taxable component all taxed element. Sole beneficiary is his financially independent adult daughter (SIS dependant as his child, but NOT a tax dependant).

- **Paid directly by the fund:** 15% + 2% Medicare levy on the taxed element = 17% x 500,000 = **$85,000**.
- **Paid to the LPR and distributed under the will:** the fund withholds NIL (Schedule 12). The trustee is assessed (s 101A(3) ITAA 1936 with s 302-10 ITAA 1997) on the amount to the extent a NON-dependant benefits or may be expected to benefit, at the same component caps but with **no Medicare levy** (trustee assessments never carry it): 15% x 500,000 = **$75,000**. Saving **$10,000**.
- Had the recipient been his spouse (tax dependant), the lump sum would be tax-free either way. A death benefit received by the estate is statutorily income to which NO beneficiary is presently entitled -- it never flows out pre-tax. Routing choices (BDBN to the LPR vs direct) sit in super-fund law and estate planning: a BDBN is a direction to the FUND trustee, not will property -- flag, and send disputes to R-AU-DE-3.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- Two taxpayers from the date of death

Death splits the file: (1) the deceased's FINAL individual return, 1 July to the date of death; (2) the estate, a trust from the day after death, with the LPR as trustee (s 6(1) ITAA 1936 defines "trustee" to include executors and administrators) lodging trust returns under a new estate TFN for income derived after death. Never mix the two: income is allocated by DERIVATION date against the date of death, not by receipt-vs-bill logic (Rule 10 for the s 101A override).

### Rule 2 -- The final return mechanics

Lodgment is required if the deceased had tax withheld, taxable income above the threshold, or a lodgment history/outstanding returns; otherwise send a non-lodgment advice with 'DECEASED' and the date of death. The authorised LPR (grant in hand, recorded on ATO systems after notification) lodges on PAPER headed 'LEGAL REPRESENTATIVE OF [name] (DECEASED)' -- myTax/myGov cannot be used, though an appointed tax agent can lodge online. The FULL tax-free threshold applies with no pro-rating, the Medicare levy and full-year low-income levy thresholds apply as for any individual year (see au-medicare-levy), and study loans get a final assessed repayment with the balance of the debt cancelled. Refunds and franking credit refunds are released only to the authorised LPR. The LPR must provide for tax before distributing or becomes personally liable up to the value of estate assets (PCG 2018/4).

### Rule 3 -- Access, authority and the data package

Death severs all pre-death agent authorisations. Sequence: notify the ATO -> obtain the grant -> be recorded as authorised LPR -> (optionally) appoint an agent with a declaration -> request/receive the deceased estate data package (3 years of returns, income and investment extracts, NOAs, account statement, ATO debts, super accounts, current-year payroll). Without a grant the ATO discloses only what its risk settings allow -- an executor without probate is NOT an authorised LPR. If nobody administers an intestate estate within 6 months, the ATO can raise assessments and recover itself.

### Rule 4 -- Present entitlement through the stages (IT 2622)

*FCT v Whiting* (1943) 68 CLR 199: no beneficiary can be presently entitled to estate income until administration is complete (debts, funeral and testamentary expenses, legacies paid or provided for and the residue ascertained -- actual transfers can lag). Consequences by stage per the Section 3.1 table: initial stage -> trustee s 99 on everything; intermediate stage -> amounts the executor ACTUALLY PAYS to or applies for beneficiaries are deemed presently entitled (IT 2622 para 14) and assessed to them (s 97) or via the trustee for minors/non-residents (s 98), the balance staying with the trustee; once residue is ascertained -> full present entitlement. In the completion YEAR, ATO practice assesses beneficiaries on their share of the whole year's net income, unless actual pre/post-completion derivation is evidenced and apportionment is requested (income to the completion date then stays with the trustee). Minors' shares via s 98 use ADULT rates -- Div 6AA does not touch deceased-estate income, and the trustee can claim the beneficiary's offsets; Medicare levy applies to those s 98 assessments (unlike s 99 assessments on the estate itself).

### Rule 5 -- s 99 rates: three concessional years, then compression

Apply for the concessional rate in the estate's FIRST trust return: resident individual rates with the full threshold for the first three income years (the short period to the first 30 June counts as year 1), no Medicare levy, no offsets, no extension beyond year 3, and the concession can be lost on material changes to the estate's circumstances (e.g. assets injected -- also a s 99A(2) trigger). From year 4 the published bands compress (Section 3.2): $416 nil band, 50% shade-in to $611, then $97.76 + 16% to $45,000 with the whole amount effectively at 16% once over $611, then the ordinary 30/37/45 brackets -- still no Medicare levy. **2026-27 caution:** the 15% second rate is law and mechanically shifts the shade-in constants; the ATO table (QC 49909) is published only to 2025-26 as at 20 August 2026 -- re-verify before lodging 2026-27.

### Rule 6 -- Death is not a CGT event (Div 128)

Any capital gain or loss on death is disregarded where the asset passes to the LPR or to a beneficiary (ss 128-10, 128-15, 128-20 -- passing under the will, intestacy, appropriation or deed of arrangement). Cost base to the LPR/beneficiary (s 128-15(4)): pre-CGT asset of the deceased -> market value at date of death; post-CGT asset -> the deceased's cost base at death; two market-value overrides -- the deceased's main residence just before death (not then income-producing, passing after 20 August 1996, not as surviving joint tenant) and assets passing to a special disability trust. The beneficiary adds LPR-incurred costs (conveyancing, probate-defence legal costs) to their own cost base (s 128-15(5)). Assets the LPR SELLS instead of transmitting do not pass -- the estate returns that gain normally. Discount clock (s 115-30(1) item 4): the inheritor is deemed to have acquired a post-CGT asset when the DECEASED acquired it, and a pre-CGT asset at the date of death -- so shares the deceased held 10 years are discount-eligible on day one in the beneficiary's hands.

### Rule 7 -- Inherited main residence and the 2-year window (s 118-195)

Full exemption for a dwelling that was (a) the deceased's pre-CGT asset, or (b) their main residence just before death and not then income-producing, IF EITHER the ownership interest ends (contract settles) within 2 years of death -- post-death renting is irrelevant under this limb -- OR from death the dwelling was the main residence of the deceased's spouse, a person with a right to occupy under the will, or the disposing beneficiary. Failing both limbs, s 118-200 gives a days-based partial exemption. The Commissioner can extend the 2 years; PCG 2019/5 makes extensions up to 18 months AUTOMATIC where all five safe-harbour conditions hold (Example 4), with discretionary requests beyond it. Foreign-resident overlays kill the exemption: a deceased who was a foreign resident more than 6 years at death (no life event) had no main-residence status to inherit, and a beneficiary selling while a long-term foreign resident loses their period too -- flag and escalate (R-AU-DE-4, au-nonresident-cgt).

### Rule 8 -- CGT event K3 (s 104-215): the Div 128 override

**AUDIT FLASH POINT**

K3 happens when a CGT asset of the deceased passes to a beneficiary who, when it passes, is an exempt entity, the trustee of a complying superannuation entity, or a foreign resident. Foreign-resident limb: only if the deceased was an Australian resident just before death AND the asset is NOT taxable Australian property in the beneficiary's hands (TAP -- Australian real property, mining interests, land-rich entity stakes -- stays in the Australian net, so rollover applies instead). The event time is JUST BEFORE death: gain = market value at death less cost base, returned in the deceased's DATE-OF-DEATH return, discount-eligible, and able to absorb the deceased's otherwise-dying capital losses. Pre-CGT assets: disregarded (s 104-215(5)); testamentary gifts to deductible gift recipients: s 118-60 exception. Because "passing" may occur years after lodgment, K3 routinely forces an AMENDMENT of the final return -- screen beneficiary residency at day one, not at transfer (Conservative defaults).

### Rule 9 -- Super death benefits: dependant status and the estate route

Superannuation is NOT will property: it is paid under the fund's rules and SIS law, by trustee discretion or a binding death benefit nomination (a BDBN binds the FUND trustee and can be lapsing -- validity disputes go to R-AU-DE-3). Tax dependant (s 302-195: spouse/former spouse, child under 18, interdependency, actual financial dependant) -> lump sum entirely tax-free. Non-dependant (typically an independent adult child) -> lump sum only: tax-free component NANE; taxable component taxed element at max 15%, untaxed element at max 30%, PLUS 2% Medicare levy when paid directly. Paid to the LPR instead: the fund withholds nothing (Schedule 12), the benefit is statutorily income with no present entitlement, and the trustee is assessed under s 101A(3)/s 302-10 as if paid to those who benefit or may be expected to benefit -- tax-dependant shares tax-free, non-dependant shares at the 15%/30% caps WITHOUT Medicare levy (Example 6). Keep death benefits out of the s 99 rate analysis: Div 302 rates apply to them specifically.

### Rule 10 -- Unfinished business: s 101A, franking refunds, dying losses

(1) Amounts received AFTER death that would have been the deceased's assessable income if received in life (final wages, director's fees, trail commissions, pre-death invoices) are assessable income of the ESTATE (s 101A(1)), not the final return -- and death-benefit ETPs and super paid to the LPR fall in s 101A(3). (2) The final return still claims the deceased's franking offsets, and excess credits are refunded to the LPR -- lodge for the refund even where income is trivial. (3) Carried-forward losses DIE with the deceased: revenue losses and net capital losses cannot transfer to the estate or beneficiaries. Last chance to use them is the final return -- pre-death disposals and K3 gains can absorb capital losses (Example 5); nothing else can. Never model estate income as sheltered by the deceased's losses.

### Rule 11 -- Testamentary trusts: Div 6AA excepted income and s 102AG(2AA)

**AUDIT FLASH POINT**

Income of a trust that resulted from a will, codicil, intestacy or court order (s 102AG(2)(a)(i)) is EXCEPTED trust income: minor beneficiaries are taxed at ordinary adult rates with the full threshold instead of Div 6AA penalty rates -- the core testamentary-trust advantage. The s 102AG(2AA) integrity rule (from 1 July 2019) confines this to income derived from property transferred FROM the deceased estate (or accumulations of it, and property representing successive reinvestment/proceeds of it). Assets injected from outside -- gifts from relatives, borrowings, a related discretionary trust "topping up" the TT -- generate ORDINARY (penalty-rate) income for minors. Trace asset provenance before applying adult rates; apportion where the corpus is mixed. Note also s 102AG(2)(d)(ii) excepted income for property transferred directly to a minor from a deceased estate outside any trust.

### Rule 12 -- LPR liability and estate distributions discipline

Before interim or final distributions: quantify final-return tax, estate tax by year, K3 exposure, super benefit tax at trustee level, and any pre-death ATO debts from the data package. The authorised LPR is liable for the deceased's tax up to the value of estate assets, and personally exposed where assets are distributed leaving tax unprovided for -- PCG 2018/4 describes when the ATO treats an LPR as having notice. Interim distributions also flip present entitlement on the amounts paid (Rule 4), changing who is assessed -- document stage, date and amount for every payment out.

### Rule 13 -- Announced 30% trustee minimum tax: the testamentary carve-out

The 2026-27 Budget measure (30% minimum tax on discretionary trust distributions from 1 July 2028; Treasury consultation closed 31 July 2026) explicitly CARVES OUT deceased estates and testamentary trusts -- pre-1 July 2028 testamentary trusts excluded where genuinely testamentary with assets from the estate (or injected before 12 May 2026), later ones only if beneficiaries are limited to individuals/tax-exempts. ANNOUNCED, NOT LAW: never model it, never restructure around it, and treat carve-out design as unstable (R-AU-DE-6 for planning requests). See au-trust-distributions Rule 14 for the full landscape table.

### Rule 14 -- 1 July 2027 CGT reform interaction (LAW)

Tax Reform No. 1 Act 2026 (Assent 26 June 2026): from 1 July 2027, for gains accruing after that date, the 50% discount for individuals and trusts is replaced by cost base indexation plus a 30% minimum rate, and pre-CGT status ends after 30 June 2027. Deceased-estate flow-ons to flag on every file: (a) the market-value-at-death uplift for a deceased's pre-CGT assets (s 128-15(4) item 4) only works its old magic while pre-CGT status exists -- deaths after the transition sit under the new regime; (b) the inherited discount clock (Rule 6) matters differently once discounts give way to indexation; (c) estates and s 99 assessments will need the new trustee gain-categorisation statements. Detailed ATO guidance is still emerging -- verify before advising on any post-June-2027 death or estate disposal.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Surviving joint tenants

**Trigger:** assets held as joint tenants (home, bank accounts, shares). **Issue:** survivorship assets do NOT pass through the estate -- s 128-50 vests the deceased's interest in the survivor with Div 128-style cost base rules; the market-value main-residence uplift is modified. **Action:** split the asset schedule joint-vs-estate before anything else; compute survivor cost bases separately.

### T2-2 -- Dwelling occupied by spouse or right-to-occupy beneficiary

**Trigger:** widow/widower stays in the home; will grants occupation rights; life interests. **Issue:** s 118-195 occupation limb can fully exempt WITHOUT the 2-year clock, but life and equitable interests have their own CGT rules and can also ground a PCG 2019/5 circumstance. **Action:** document occupier identity and instrument; escalate life-interest structures (legal + TR 2006/14 territory).

### T2-3 -- Estate sells vs transmits

**Trigger:** LPR deciding whether to sell assets and distribute cash, or transfer in specie. **Issue:** sale by the LPR is a normal CGT event to the estate (s 99 rates, trust discount rules); in-specie passing defers to the beneficiary but triggers K3 screening for non-resident takers -- the choice changes who pays and at what rate. **Action:** model both routes before probate assets are liquidated; check the will's powers; escalate beneficiary-residency conflicts (R-AU-DE-4).

### T2-4 -- Australian beneficiary of a foreign estate

**Trigger:** client inherits from an overseas estate, or receives distributions from a foreign LPR years after death. **Issue:** s 99B can assess distributions of accumulated foreign-estate income at marginal rates; corpus exceptions need evidence. **Action:** flag only -- computation out of scope (R-AU-DE-4).

### T2-5 -- Main residence absence choices interacting with death

**Trigger:** deceased had rented out the home under the 6-year absence rule, or moved to aged care before death. **Issue:** "main residence just before death" can be satisfied by a continuing absence CHOICE, changing both the s 128-15 uplift and s 118-195 eligibility. **Action:** reconstruct the deceased's residence elections year by year; see au-capital-gains Section 6.

### T2-6 -- Superannuation proceeds trusts

**Trigger:** will directs super death benefits into a separate trust for minors. **Issue:** excepted-income status for the minors turns on s 102AG conditions tracking who could benefit (tax dependants) and asset provenance (2AA). **Action:** confirm trust terms mirror the excepted categories before applying adult rates; escalate drafting (R-AU-DE-6).

### T2-7 -- Amendment traps on the final return

**Trigger:** K3 discovered at transmission; late super statements; post-lodgment income recharacterised between estate and deceased. **Issue:** the final return often needs amendment years later; time limits run from its assessment. **Action:** diarise amendment windows at first lodgment; hold the K3 screen open until every asset has passed.

---

## Section 7 -- Excel working paper template

```
AUSTRALIA DECEASED ESTATE -- WORKING PAPER
Deceased: [name]   DOD: [date]   Grant: [probate/LoA + date]
Authorised LPR: [name]   Estate TFN: [____]   Prepared: [date]

FINAL RETURN (1 July - DOD)
  Income to DOD (by derivation):        AUD [____]
  K3 gains (non-resident/exempt/super
  beneficiaries, MV at DOD - cost base): AUD [____]
  C/f revenue losses used (last chance): AUD [____]
  C/f capital losses used (last chance): AUD [____]
  Tax + full-year Medicare levy:         AUD [____]
  Franking offsets (refundable):         AUD [____]
  Lodged: [paper/agent]  'DECEASED' annotation: [Y/N]

ESTATE TRUST RETURNS (per year since DOD)
  Estate income year number:             [1/2/3/4+]
  Administration stage at 30 June:       [initial/intermediate/final]
  Interim distributions PAID:            AUD [____] -> beneficiary s 97/98
  Balance no present entitlement:        AUD [____] -> trustee s 99
  Rate basis: [Y1-3 individual+threshold, no ML / Y4+ compressed]
  Tax: AUD [____]   (NO Medicare levy on s 99)
  s 101A receipts (pre-death income):    AUD [____]
  Super death benefit via LPR: taxed element AUD [____] x 15%,
  untaxed AUD [____] x 30%, tax-dependant share NANE, NO ML

ASSET REGISTER (per asset)
  Pre/post-CGT for deceased: [____]  Cost base at DOD / MV at DOD: [____]
  Passes to: [LPR sale / beneficiary + residency]
  K3 screen: [n/a / TAP / K3 -> final return]
  Dwelling: MR at death? [Y/N]  Income-producing? [Y/N]
  2-year window ends: [date]   PCG 2019/5 conditions: [notes]

REVIEWER FLAGS
  [Stage evidence, missed windows, refusals triggered, 2027 reform notes]
```

---

## Section 8 -- Reading guide

1. Date of death first: it splits every number into final-return vs estate, fixes the estate-year count, and starts the 2-year dwelling clock.
2. Authority second: grant status decides who may lodge, who gets the data package, and whether anyone is an "authorised LPR" at all.
3. Stage third (IT 2622): initial/intermediate/final determines present entitlement -- and therefore whether s 97, s 98 or s 99 carries each dollar.
4. Count estate years honestly: the part-year to the first 30 June is year 1; year 4 pricing is a cliff (Example 3).
5. Screen every asset for K3 at day one -- beneficiary residency at PASSING is what counts, and the charge lands in the final return.
6. Never let the 2-year dwelling window expire silently: diarise it at engagement, and document PCG 2019/5 conditions contemporaneously.
7. Label reform items correctly: 15% rate flow-through (LAW, 2026-27), 1 July 2027 CGT changes (LAW), 30% trustee minimum tax with testamentary carve-out (ANNOUNCED).

---

## Section 9 -- Onboarding fallback

If engaged mid-administration with a shoebox:

1. Build the timeline: DOD, grant date, debts paid/provided for, distributions made (date + amount + recipient)
2. Request the ATO data package via the authorised LPR; list outstanding pre-death returns
3. Split every receipt since 1 July of the death year: deceased (derived pre-DOD) / s 101A estate income / estate income proper
4. Register assets with acquisition dates, cost bases, DOD market values (pre-CGT and dwelling), and destination beneficiary + residency
5. **Flag:** "Prepared without sighting the will/grant/administration records as noted. Stage of administration, present entitlement, estate-year count, K3 screening and the s 118-195 window are unverified. Reviewer must confirm before lodgment or distribution."

---

## Section 10 -- Reference material

### Key figures (2025-26 -- the year being lodged)

| Item | Value |
|---|---|
| Final return threshold / Medicare levy | Full $18,200 threshold, no pro-rating; Medicare levy at 2% with full-year low-income thresholds |
| Estate years 1-3 (s 99) | Individual rates + $18,200 threshold; NO Medicare levy; NO offsets |
| Estate year 4+ bands (2024-25/2025-26) | $0-$416 nil; $417-$611 50% of excess; $612-$45,000 $97.76 + 16% over $611 (whole amount at 16% once over $611); then $7,200+30% / $34,200+37% ($135k) / $54,550+45% ($190k) |
| 2026-27 flow-through | 15% second rate is LAW; year-4+ boundaries not yet republished by ATO -- verify QC 49909 |
| Inherited dwelling window | 2 years from death to settlement; PCG 2019/5 automatic extension <= 18 months if all 5 conditions met |
| Super death benefit (non-dependant) | Taxed element 15%, untaxed 30%; + 2% Medicare direct, NO Medicare via LPR; tax dependant: lump sum tax-free |
| K3 measurement | MV at death − cost base, in the deceased's final return; pre-CGT disregarded; DGR gifts excepted (s 118-60) |
| Losses at death | Revenue and capital carry-forwards lapse -- usable only in/for the final return |

### Primary sources (verified 20 August 2026 against ato.gov.au)

| Topic | Source |
|---|---|
| Final return, DECEASED annotation, refunds to LPR | ato.gov.au -- Doing a final tax return for the deceased person (QC 40481, updated 4 June 2026) |
| Notification, authority, data package | ato.gov.au -- Accessing a deceased person's tax and super information (QC 56976); Checklist: what to do when someone dies; PCG 2018/4 (LPR liability) |
| Estate trust returns and stages | ato.gov.au -- Doing trust tax returns for the deceased estate (QC 67527); Who pays tax on deceased estate income (QC 49907) |
| Present entitlement during administration | IT 2622 (6 December 1990); *FCT v Whiting* (1943) 68 CLR 199; ITAA 1936 ss 95-99A, 101A |
| Estate tax rates | ato.gov.au -- Tax rates – deceased estate (QC 49909, updated 4 June 2026); Income Tax Rates Act 1986 |
| Death CGT rollover and cost bases | ITAA 1997 Div 128 (ss 128-10, 128-15, 128-20, 128-50); s 115-30(1) item 4; ato.gov.au -- Cost base of inherited assets (QC 66053); Inherited property and CGT (QC 66054) |
| Main residence on death | ITAA 1997 ss 118-195, 118-200; ato.gov.au -- Extensions to the 2-year ownership period (QC 66057); PCG 2019/5 |
| CGT event K3 | ITAA 1997 s 104-215; s 118-60 |
| Super death benefits | ITAA 1997 Div 302 (ss 302-10, 302-60, 302-140/145, 302-195); ITAA 1936 s 101A(3); ato.gov.au -- Superannuation death benefits (QC 44997); Paying superannuation death benefits (QC 45254); Schedule 12 withholding table |
| Testamentary trusts | ITAA 1936 Div 6AA, s 102AG(2)(a)(i), s 102AG(2AA) (Treasury Laws Amendment (2019 Measures No. 3) Act 2020, from 1 July 2019) |
| 2026 reforms | Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Assent 26 June 2026); 2026-27 Budget (12 May 2026) + Treasury consultation 8 July 2026 (30% minimum tax, testamentary carve-out -- ANNOUNCED, NOT LAW) |

### Test suite

**Test 1:** Died 31 October; income to DOD $50,000 incl. $600 franking credit. -> Tax $5,788 + $1,000 ML − $600 offset = $6,188; full threshold, no pro-rating.

**Test 2:** Estate year 2, $30,000, no present entitlement. -> s 99 at individual rates: $1,888 (2025-26), no Medicare levy, no LITO.

**Test 3:** Estate year 5, $30,000. -> $97.76 + 16% x $29,389 = $4,800.00; whole amount effectively at 16%.

**Test 4:** Estate year 5, $500. -> 50% x (500 − 416) = $42.00.

**Test 5:** MR dwelling, MV at DOD $900k, settles month 20 after renting throughout. -> Fully exempt (2-year limb ignores use).

**Test 6:** Same dwelling settles month 30, vacant, no safe-harbour circumstance. -> No full exemption; gain over MV-at-DOD cost base taxable (discount from deceased's acquisition date).

**Test 7:** Post-CGT shares (MV $300k, CB $120k) pass to foreign-resident daughter. -> K3: $180k gain just before death, in the FINAL return; resident son instead -> rollover at $120k.

**Test 8:** Pre-CGT beach house passes to foreign-resident nephew. -> K3 gain disregarded (s 104-215(5)); nephew's cost base = MV at DOD.

**Test 9:** $500k taxed-element super to adult child: direct $85,000 (17%); via LPR $75,000 (15%, no ML).

**Test 10:** Deceased's $40k carried-forward capital loss; estate sells shares at a $40k gain in year 2. -> Loss CANNOT offset -- it died with the deceased; estate pays s 99 tax on the gain.

**Test 11:** Minor receives $20,000 testamentary trust income from will-derived assets. -> Adult rates (excepted income); if from assets injected by grandparents post-death -> Div 6AA penalty rates (s 102AG(2AA)).

### Prohibitions

- NEVER lodge a final return via myTax, or without the DECEASED/LPR annotations
- NEVER pro-rate the tax-free threshold in a date-of-death return
- NEVER apply Medicare levy to a s 99 deceased-estate trustee assessment -- and never skip it in the final return or s 98 beneficiary assessments
- NEVER use the deceased's TFN for estate trust returns, or treat the former agent's authority as surviving death
- NEVER treat beneficiaries as presently entitled during administration beyond amounts actually paid to them
- NEVER apply years 1-3 concessional rates from year 4, or assume the estate-year count without the date of death
- NEVER apply the deceased's carried-forward losses to estate income
- NEVER skip the K3 screen because "death is not a CGT event" -- check every beneficiary's residency and each asset's TAP status
- NEVER assume a missed 2-year window is fatal (PCG 2019/5) or that an extension is available without evidencing the conditions
- NEVER treat super as will property, or apply Div 302 rates without the fund's component breakdown
- NEVER apply adult rates to testamentary trust income for minors without tracing s 102AG(2AA) asset provenance
- NEVER present the announced 30% trustee minimum tax (or its testamentary carve-out design) as law
- NEVER present figures as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
