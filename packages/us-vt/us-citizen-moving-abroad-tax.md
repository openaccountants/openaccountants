---
name: us-citizen-moving-abroad-tax
description: "The US taxes citizens wherever they live. What that actually means when you move abroad: the FEIE vs Foreign Tax Credit decision, FBAR and FATCA reporting, the PFIC and foreign-company (GILTI/5471) traps, sticky states, Social Security and totalization, and — for those who go all the way — the §877A exit tax on renouncing. Sequenced by destination type: zero-tax (UAE/Gulf) vs high-tax (EU)."
jurisdiction: US
tax_year: 2025
last_updated: 2026-08-03
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# The American abroad: why moving never ends your US tax life

**The fact every other country's movers don't face.** The United States taxes its **citizens
and green-card holders on worldwide income no matter where they live**. A Brit who leaves
Britain stops filing British returns; an American who leaves America files Form 1040 for life.
Moving abroad doesn't end your US tax life — it *doubles* it: a new country's system on top of
the one you can't leave. Every planning question for this corridor is therefore really one
question: **how do the two systems interlock without taxing you twice — and which US traps get
worse the moment you cross the border?**

**Who this Guide is for.** US citizens and permanent residents moving abroad — employees,
founders, retirees, accidental Americans discovering their status — and the accountants
receiving them. The corridor splits sharply by destination: a **zero-tax landing** (UAE, Gulf,
some territorial regimes) and a **high-tax landing** (most of Europe) produce nearly opposite
optimal setups, and this Guide keeps both threads visible throughout.

## Part 2 — The reporting web: forms that carry four-figure penalties

For Americans abroad the *income* tax is often modest; the **information reporting** is where
lives get ruined. None of these forms raise a dollar of tax by themselves; each carries
penalties that start around $10,000.

| Form | Trigger | The point |
|---|---|---|
| **FBAR** (FinCEN 114) | Aggregate of all non-US financial accounts exceeds **$10,000** at any moment in the year | Every account, even ones you only have signature authority over. Filed with FinCEN, not the IRS. Willful violations are catastrophic. |
| **Form 8938** (FATCA) | Foreign financial assets above thresholds — for genuine expats, **$200k/$300k single, $400k/$600k joint** (year-end/any-time) | Overlaps FBAR but is not a substitute; both file. |
| **Form 5471** | Officer/director/≥10% shareholder of a **foreign corporation** | The founder trap — see Part 3. |
| **Form 8621** | Any interest in a **PFIC** | The investment trap — see Part 3. |
| **Form 3520/3520-A** | Foreign trusts, and foreign gifts/inheritances above ~$100k | Receiving a large gift from a non-US parent is reportable, tax-free or not. |
| **FinCEN/8858, 8865** | Foreign disregarded entities and partnerships | Your foreign LLC-equivalent is not invisible. |

**The banking reality:** FATCA also makes *you* radioactive to some non-US banks and brokers —
expect account refusals, and expect your local bank to report you to the IRS. Keep meticulous
records; the data now flows both ways.

---

## Part 3 — The two traps that define American expat planning

### 3.1 PFIC: never buy foreign funds
Almost any non-US **pooled investment** — a UCITS ETF in Europe, a UAE mutual fund, many
insurance wrappers — is a **Passive Foreign Investment Company**. The default US regime taxes
gains at top ordinary rates *plus an interest charge* as if earned rateably over your holding
period, with a separate Form 8621 per fund. It converts ordinary index investing into a
punitive mess. The playbook is blunt: **keep investments in US-domiciled funds via a US
broker** (using a US address/institution that accepts expats), or hold individual securities
directly. An American who moves to Frankfurt and buys the local ETF has made a four-figure
mistake per year, per fund.

### 3.2 The foreign company: CFC, GILTI and Subpart F
The Dubai free-zone company that works beautifully for a British founder is a trap for an
American one. A foreign corporation that is **>50% owned by US persons** is a **Controlled
Foreign Corporation**; each ≥10% US shareholder picks up **GILTI** — current US tax on the
company's active earnings, largely stripping the deferral the 0% UAE rate seemed to promise —
plus Form 5471 (a substantial return in itself) and Subpart F on passive income.

Mitigations exist, and they are genuinely technical: the **§962 election** (corporate-rate
treatment + partial GILTI deduction for individuals), the **high-tax exclusion** (only helps
where local corporate tax is meaningful — not 0% free zones), checking the entity into
pass-through treatment, or simply operating as a **sole proprietor / disregarded entity**
abroad. The honest rule: **an American should never form a non-US company without US advice
first**. The structure that saves your neighbour six figures costs you five.

---

## Part 4 — Self-employment, Social Security and totalization

- US **self-employment tax** (15.3% up to the wage base, Medicare above) follows citizens
  abroad and is **not** reduced by the FEIE.
- **Totalization agreements** (~30 countries: most of Europe, UK, Japan, Australia…) assign you
  to one social system and let a certificate of coverage switch off US SE tax while you pay the
  local system — and let credits in both systems combine for benefit eligibility.
- **No totalization with the UAE or most of the Gulf**: a self-employed American in Dubai owes
  full US SE tax on worldwide net earnings, FEIE or not. This one line reshapes the
  employee-vs-freelancer decision for Gulf-bound Americans.
- US Social Security benefits remain payable abroad (unlike some countries' frozen pensions),
  and years abroad without covered earnings simply add zeros to your 35-year average.

---

## Part 5 — The states that won't let go

Federal expatriation is only half the departure; your **state** may not recognise it.
- **Sticky states** — California, Virginia, South Carolina, New Mexico are the notorious
  examples — presume continuing residency while you keep ties: driver's licence, voter
  registration, property, spouse, even bank branches. California's FTB litigates this
  aggressively; "I moved to Singapore" is the beginning of the argument, not the end.
- The pattern that works: **sever affirmatively** (licence surrendered/exchanged, voter roll
  moved to federal-only ballots, homes sold or demonstrably rented out arm's-length,
  registrations closed), ideally establishing a domicile pit-stop in a **no-income-tax state**
  (Florida, Texas, Washington, Nevada, South Dakota) before departure when the facts allow it.
- Expect a part-year state return in the departure year and keep the evidence file for four
  more.

---

## Part 6 — Retirement accounts, pensions and the treaty patchwork

- **Keep the 401(k)/IRA** — moving abroad doesn't disturb their US deferral, and most treaties
  respect pension wrappers. Early liquidation "because I'm leaving" is almost always the worst
  move on the board.
- Contributions get harder: IRA contributions require *non-excluded* earned income (FEIE can
  zero out your eligibility — one more vote for FTC in high-tax countries).
- **Foreign pensions** (a UK SIPP, German bAV, Swiss Pillar 2/3) are, absent treaty language,
  just foreign accounts to the US: employer contributions and growth can be currently taxable,
  and some wrappers flirt with trust or PFIC treatment. The UK treaty is famously decent here;
  many others are silent. Get the destination-specific answer before funding anything local.
- **Roth conversions** in low-income expat years (FEIE-excluded salary, little US-taxable
  income) are one of the corridor's best quiet plays — filling the 10–12% brackets annually.

---

## Part 7 — The exit door: renunciation and the §877A exit tax

For some — long-term expats, accidental Americans — the endgame is renouncing citizenship (or
abandoning a long-held green card, which triggers the same regime after 8 of 15 years). The
sequence matters more than anywhere else in this Guide:

1. **Five years of clean compliance first.** Certifying five years of full US tax compliance
   (Form 8854) is a precondition for a non-covered exit; renouncing while non-compliant makes
   you a covered expatriate automatically.
2. **Covered expatriate tests** — any one of: net worth **≥ $2 million**; average net US tax
   liability over the prior five years above an inflation-adjusted threshold (~$200k region —
   check the current figure); or failure of the compliance certification.
3. **The mark-to-market exit tax**: covered expatriates are deemed to sell everything the day
   before expatriation, with a gain exclusion around **$890k** (inflation-adjusted; check the
   year's figure), plus punitive treatment of deferred accounts and — the sleeper — **§2801**:
   US persons who later receive gifts or bequests *from* a covered expatriate pay a transfer
   tax at the top rate. Renouncing "covered" taints your heirs, not just you.
4. The mechanics: appointment at a consulate, the **$2,350** fee, the CLN, and a final
   dual-status return with 8854.

**Planning corollary:** for anyone within sight of the $2m line, the order is *plan → gift →
comply → renounce*, over multiple years — pre-expatriation gifting (using the still-unified
lifetime exemption) is the lever that de-covers borderline cases.

---

## Part 8 — Sequenced checklist

**Before the move**
1. Pick your shield strategy by destination: FEIE (zero-tax landing) vs FTC (high-tax landing);
   don't burn the FEIE election casually.
2. Founders: freeze all entity formation until Part 3.2 has been advised on. Employees:
   confirm whether a totalization agreement covers you.
3. Sever the sticky state affirmatively; consider the no-tax-state pit stop.
4. Move investments to a US brokerage that accepts expats; purge foreign funds *before* they
   become long-held PFICs.

**Each year abroad**
5. File the 1040 (June 15 automatic, October 15 by extension), FBAR, 8938, and whatever the
   entity/trust web requires. Calendar them — the penalties are for silence, not for owing.
6. Track presence days if using the Physical Presence Test; keep the bona-fide-residence
   evidence file otherwise.
7. Harvest the low-bracket years: Roth conversions, gain realisation up to the bracket edges.

**If the end state is renunciation**
8. Five clean years → net-worth management → appointment → 8854. Treat it as a multi-year
   project with its own adviser.

---

## The trap list

| Trap | Why it bites |
|---|---|
| "I don't owe anything so I don't file" | The penalty regime attaches to the *forms*, not the tax. FBAR + 8938 + 5471 silence is how five-figure penalties happen on zero-tax lives. |
| Buying the local index fund | PFIC — punitive rates, interest charges, one 8621 per fund. |
| Forming the Dubai FZ-LLC like everyone else | CFC/GILTI: the 0% local rate becomes current US tax + Form 5471. |
| High earner relying on FEIE in the Gulf | Everything above ~$130k is fully US-taxed; there's no FTC to help. |
| Freelancing in a non-totalization country | 15.3% SE tax survives the FEIE untouched. |
| Leaving California casually | FTB residency audits reach years back; ties you forgot are ties they'll find. |
| Cashing out the 401(k) on departure | Tax + 10% penalty for a problem that didn't exist. |
| Renouncing while non-compliant or above $2m unplanned | Covered-expatriate status: mark-to-market tax now, §2801 tax on your heirs later. |
| Marrying/joint accounts abroad without advice | Non-resident spouse elections (§6013(g)), gift-splitting limits and FBAR scope all shift. |

---

## Sources (primary, verify current-year figures)

IRC §911 and Form 2555 instructions (FEIE, housing exclusion — irs.gov); Form 1116 instructions
(FTC); FinCEN Report 114 + BSA e-filing guidance (FBAR); Form 8938 instructions (FATCA
thresholds); Forms 5471 / 8621 / 3520 instructions; §951A (GILTI) and §962 election guidance;
IRS Publication 54 (Tax Guide for U.S. Citizens Abroad); SSA totalization agreement list
(ssa.gov/international); §877A / Form 8854 instructions and §2801 regulations; state residency:
California FTB Publication 1031 and equivalents.

---

*Built for the OpenAccountants migration desk. Americans are the one nationality whose
cross-border tax problem never ends — which also makes them the clients who need a named,
credentialed accountant on both ends of every move, permanently. Every figure above
inflation-adjusts annually: treat numbers as pointers to their primary sources.*

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
