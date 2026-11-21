---
name: ca-like-kind-exchange-form-3840
description: >
  California rules for a section 1031 like-kind exchange in which California
  real property is given up for replacement property outside California, for
  tax year 2026. Covers who must file FTB 3840 (individuals, estates, trusts,
  partnerships, LLCs and corporations, resident or not; the owner files for a
  disregarded entity), the initial, annual, amended and final filings, how the
  California-source deferred gain is preserved and taxed when the replacement
  is later sold even by a nonresident, Schedule A allocation across several
  properties, the end of California personal property exchanges after 2024,
  the Form 593 withholding on boot over USD 1,500 and on failed exchanges, and
  the Notice of Proposed Assessment when the form is not filed. Trigger on
  "FTB 3840", "California 1031 clawback", "exchange California rental for out
  of state property", "deferred gain California nonresident", "annual 3840".
version: 0.1
jurisdiction: US-CA
category: state-tax
tax_year: 2026
last_updated: 2026-11-21
tier: 2
domain: tax
type: situation-rules
depends_on:
  - us-section-1031-like-kind-exchange
---

# California like-kind exchanges and FTB 3840 (claw-back reporting), tax year 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from the FTB 3840 (2025) form and its instructions, the FTB page on reporting like-kind exchanges (last updated 28 January 2026), FTB Publication 1100 (rev. 10/2024) and the FTB Form 593 (2025) instructions, read on 2026-11-21. The California statute site (leginfo.legislature.ca.gov) refused our reader, so statute sections are cited only where an FTB page names them. No accountant has reviewed it.

**Answer first.** California follows federal section 1031, so a valid exchange defers the gain in California too. The difference is what happens when **California real property is exchanged for property outside California**: the deferred gain keeps its **California source** forever, and California taxes it when the replacement property is later sold in a taxable transaction, even if the owner has moved away and the replacement is in another state. To track it, the taxpayer files **FTB 3840** for the year of the exchange and **every later year** until the California-source deferred gain is recognized. A taxpayer who stops filing FTB 3840 and files no return can receive a Notice of Proposed Assessment for the deferred gain plus penalties and interest. From 2025 California, like federal law, allows exchanges of **real property only**.

**Tax year.** 2026. The 2026 FTB 3840 and instructions were not yet published when this was read (2026-11-21); the 2025 form and instructions are relied on, and the 2025 instructions say California conforms to the Internal Revenue Code as of 1 January 2025.

**Circular 230 disclosure.** This material is general information, not written advice on a specific transaction under 31 CFR 10.37. It is not intended to be used, and cannot be used, to avoid penalties.

## Scope and who this is for

In scope: any taxpayer, of any residence or commercial domicile, that gives up California real property in a section 1031 exchange and receives like-kind property located outside California, in the exchange year and in each later year until the California-source deferred gain is recognized ([FTB 3840 instructions (2025), B Who Must File](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html)). "Taxpayer" here covers individuals, estates, trusts, general and limited partnerships, LLPs, LLCs and corporations. A disregarded entity does not file; its owner does.

It also covers the reverse direction (out-of-state property exchanged into California property), because the later sale of the California replacement is California-source ([FTB Pub. 1100, section F](https://www.ftb.ca.gov/forms/misc/1100.html)), and the Form 593 withholding that applies to exchanges of California real property ([FTB 593 instructions (2025)](https://www.ftb.ca.gov/forms/2025/2025-593-instructions.html)).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether the exchange qualifies at all: 45 and 180 days, the QI, boot, basis, related parties | `us-section-1031-like-kind-exchange` |
| California tax rates on the gain once it is recognized | `ca-income-tax` |
| Nonresident and part-year computation on Form 540NR | `ca-540-individual-return` (refer the 540NR computation) |
| Whether the owner is still a California resident | `ca-residency-leaving-california` |
| Partnership or LLC entity-level returns that carry the exchange (Form 565, 568) | `ca-smllc-form-568` or refer |
| Real estate withholding in full (all Form 593 exemptions and methods) | refer; only the exchange rules are here |

## Ask the client first

- Where is each property given up, and where is each property received? Get the street address, or the assessor's parcel number, county and state. For a Delaware statutory trust interest, the trust's name.
- What kind of taxpayer is the exchanger (individual, trust, partnership, LLC, corporation), and is it a disregarded entity whose owner should file?
- When did the exchange happen, and has an FTB 3840 been filed for every year since? Get copies of the initial and the latest annual or amended form.
- Has any replacement property since been sold, given away, or exchanged again? On what date, and for how much?
- Did the exchanger receive any cash or other boot, or did the exchange fail? Who was the qualified intermediary, and was Form 593 filed at closing?
- Was any property in the exchange personal property (equipment, vehicles), and if so when did the exchange start and finish?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule | Conditions | Source |
| --- | --- | --- | --- |
| Personal property exchanges, AGI limit, head of household, surviving spouse or married filing jointly | under USD 500,000 | Only for exchanges initiated after 10 January 2019 and completed before 1 January 2025, AGI for the year the exchange began. None allowed for taxable years beginning on or after 1 January 2025. | [FTB 3840 instructions (2025), What's New](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html) |
| Personal property exchanges, AGI limit, other individuals | under USD 250,000 | Same window and conditions as the row above | same |
| Boot that triggers Form 593 withholding in an exchange | more than USD 1,500 | Money or other property received by the seller. Simultaneous exchange: the real estate escrow person withholds. Deferred exchange: the qualified intermediary withholds. | [FTB 593 instructions (2025)](https://www.ftb.ca.gov/forms/2025/2025-593-instructions.html) |
| Form 593 withholding on a failed exchange | 3 1/3% of the sales price | The intermediary or accommodator withholds when the exchange does not take place or does not qualify; a cash-poor QI's duty is limited to available funds. The alternative method uses gain times ownership share times the applicable rate, less any amount already withheld on boot. | same |
| Form 593 general exception | sales price USD 100,000 or less | A general real estate withholding exception, not specific to exchanges | same |

### Steps

1. **Confirm the federal exchange.** California conforms to section 1031, so the exchange is valid in California only if it is valid federally. Run `us-section-1031-like-kind-exchange` first and use California amounts where they differ (for example California adjusted basis after different depreciation) ([FTB 3840 instructions (2025), Schedule A line 6](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html); [Schedule D-1 instructions (2025)](https://www.ftb.ca.gov/forms/2025/2025-540-d-1-instructions.html)).
2. **Test the two filing conditions.** FTB 3840 is required only when both apply: one or more California properties are exchanged for one or more properties outside California, and any part of the California-source realized gain or loss is not recognized ([FTB, Reporting like-kind exchanges](https://www.ftb.ca.gov/file/personal/reporting-like-kind-exchanges.html)). California property exchanged for California property needs no FTB 3840.
3. **Source the gain.** The source of gain or loss on California property is fixed when the gain or loss is realized and is preserved whenever it is later recognized ([FTB 3840 instructions (2025), sourcing rule](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html)). Residence at the later sale does not change it: a nonresident is taxed on it as California-source income ([FTB Pub. 1100, section F, Example 16](https://www.ftb.ca.gov/forms/misc/1100.html)).
4. **Choose the box (Question B).** Initial: the exchange happened in the current year; complete both sides. Annual: a later year with the deferred gain still not recognized; enter the year of the exchange and repeat the initial (or latest amended) information. Amended: correcting an earlier form; attach a statement of the changes. Final: the deferred gain or loss has been recognized; enter the exchange year and attach a statement of how it was recognized ([FTB 3840 instructions (2025), Question B](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html)).
5. **Question C.** Real property, or personal property (only for an individual's exchange completed before 1 January 2025), or both. Check related party and give the related party's name and SSN, ITIN or FEIN when section 1031(f) applies.
6. **Part I, lines 1 to 6:** the descriptions and dates from federal Form 8824, Part I, lines 1 to 6. **Part II, lines 7 to 20:** federal Form 8824, Part III, lines 12 to 25, in order (line 7 is Form 8824 line 12, through line 20 is line 25) ([same](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html)).
7. **Schedule A, Part I (properties given up).** Line 1: each property, its location and the ownership percentage. Line 3: consideration (cash, notes, debt assumed, fair market value of other property or services). Line 4: selling expenses. Line 6: California adjusted basis. Line 8: the California-source deferred gain. If every property given up was in California, use Side 1, Part II, line 19. If some were outside California, work out each property's deferred gain first and total only the California ones, with a statement.
8. **Schedule A, Parts II and III (properties received and allocation).** Line 9: each property received, its location and ownership percentage. Line 10: one property received, enter the Part I line 8 amount; several, allocate the whole California-source deferred gain across all properties received, wherever they are, and attach a statement. Line 11: for an apportioning business, the Schedule R line 18a apportionment percentage for the exchange year, entered on the first Schedule A only.
9. **File every year.** Attach FTB 3840 to the California return for the year. With no other California filing requirement, complete the whole form, sign Side 1, and file it on its own: Franchise Tax Board, PO Box 1998, Rancho Cordova, CA 95741-1998, or e-file it with the California return ([FTB, Reporting like-kind exchanges](https://www.ftb.ca.gov/file/personal/reporting-like-kind-exchanges.html)). A form attached to a return needs no signature.
10. **When a replacement property is sold.** Report the California-source deferred gain allocated to that property on that year's California return, remove the property from FTB 3840, and attach a statement. Keep filing for the remaining replacement properties. If the property was exchanged again instead, file a new FTB 3840 for the new exchange with that property as the property given up, carrying its share of the original California deferred gain; the duty continues whether or not the new property is in California (FTB page, Examples 1 and 2).
11. **Form 593 at closing.** A deferred exchange is exempt from real estate withholding at the initial transfer; the seller certifies the exchange in Part IV, line 10, and the buyer does not sign. Boot over USD 1,500 and a failed exchange are withheld on as set out in the rates table. For a deferred exchange the Form 593 date is the date boot was distributed, or the date the exchange failed ([FTB 593 instructions (2025)](https://www.ftb.ca.gov/forms/2025/2025-593-instructions.html)).

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| California property given up, California property received | No FTB 3840; California taxes any later sale of the California property as California-source anyway | [FTB, Reporting like-kind exchanges](https://www.ftb.ca.gov/file/personal/reporting-like-kind-exchanges.html) |
| Exchange fully taxable (no part of the California gain deferred) | No FTB 3840 (second condition fails) | same |
| Out-of-state property given up, California property received; later taxable sale of the California property | Gain recognized on that sale, less the deferred out-of-state gain, is California-source for a nonresident (Example 17); a person who has become a resident by the sale is taxed on all of it, with a credit for tax paid to the other state on the deferred part (Example 18) | [FTB Pub. 1100, section F](https://www.ftb.ca.gov/forms/misc/1100.html) |
| Disregarded entity (single-member LLC) holds the property | The owner files FTB 3840 | [FTB 3840 instructions (2025), B](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html) |
| Several exchanges in one year | One FTB 3840 per exchange | same, G |
| Multiple-asset exchange | Follow Treas. Reg. 1.1031(j)-1 and the federal Form 8824 instructions for gain and basis; before 2025, mixed real and personal California property also required the form | same, H |
| Personal property exchange completed on or after 1 January 2025 | Not a like-kind exchange in California; gain is recognized | same, What's New |
| Replacement exchanged again (another 1031) | New FTB 3840 for the new exchange, plus continued annual forms for the rest | [FTB, Reporting like-kind exchanges](https://www.ftb.ca.gov/file/personal/reporting-like-kind-exchanges.html) |
| No FTB 3840 and no return filed | FTB may issue a Notice of Proposed Assessment adding the California-source deferred gain, tax, penalties and interest | same; [FTB 3840 instructions (2025), F](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html) |

**AUDIT FLASH POINT** A taxpayer who moved out of California after the exchange and stopped filing the annual FTB 3840 is the case the reporting rule exists for. When a replacement property is later sold, the California-source share of the original deferred gain must be reported to California even though neither the owner nor the property is in California any more.

## Worked cases

Case 1 uses FTB Pub. 1100 Examples 16 and 17. Case 2 is made up for illustration; the rules it applies come from the linked pages.

**Case 1: a nonresident sells the replacement property ([FTB Pub. 1100, section F](https://www.ftb.ca.gov/forms/misc/1100.html)).** (a) A Texas resident exchanges a California condominium for Texas property and defers a USD 15,000 gain. Later the Texas property is sold at a USD 20,000 gain. The USD 15,000 deferred gain is California-source and taxable by California; the USD 5,000 that arose on the Texas property is not. (b) A Nevada resident exchanges Nevada property for California property and defers USD 10,000. The California property is later sold at a USD 50,000 gain. USD 40,000 is California-source and taxable by California; the deferred USD 10,000 Nevada gain is not.

```oa-check
name: FTB Pub. 1100 Examples 16 and 17, California-source share on a later sale
inputs:
  ex16_deferred_ca_gain: 15000
  ex16_total_gain_on_sale: 20000
  ex17_deferred_nv_gain: 10000
  ex17_total_gain_on_sale: 50000
steps:
  - ex16_ca_source: ex16_deferred_ca_gain
  - ex16_not_ca_source: ex16_total_gain_on_sale - ex16_deferred_ca_gain
  - ex17_ca_source: ex17_total_gain_on_sale - ex17_deferred_nv_gain
expected:
  ex16_ca_source: 15000.00
  ex16_not_ca_source: 5000.00
  ex17_ca_source: 40000.00
```

**Case 2, a decision: does moving to Arizona remove California's claim? (rules from [FTB 3840 instructions (2025)](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html) and [FTB Pub. 1100](https://www.ftb.ca.gov/forms/misc/1100.html)).** A California resident owns two rentals given up in one exchange: a Sacramento duplex (amount realized USD 900,000, California adjusted basis USD 400,000) and an Oregon cabin (amount realized USD 300,000, adjusted basis USD 220,000). No boot is received, so each property's realized gain is fully deferred. The client receives two Arizona properties, worth USD 720,000 and USD 480,000, and plans to move to Arizona.

- Schedule A, Part I, line 8: the duplex's deferred gain is USD 500,000 and the cabin's is USD 80,000. Only the California property counts, so the California-source deferred gain is USD 500,000.
- Schedule A, Part III, line 10: the instructions require the whole USD 500,000 to be allocated across both properties received, with a statement, but do not prescribe a method. Allocated here in proportion to fair market value (a reviewer choice): USD 300,000 and USD 200,000.
- **Way 1: exchange, then move.** The move does not change the source. California taxes USD 300,000 when the first Arizona property is sold and USD 200,000 when the second is sold, as California-source income of a nonresident, and the client files FTB 3840 every year until both are sold.
- **Way 2: sell outright now, then buy in Arizona.** All USD 580,000 of gain is recognized this year by a California resident, so California taxes it now, including the USD 80,000 Oregon gain (with a credit question for Oregon's tax).
- **What decides it:** the move changes nothing for the USD 500,000; only the USD 80,000 Oregon gain is outside California's reach in Way 1. The exchange defers California tax; it does not remove it.

```oa-check
name: Two properties given up, California-source deferred gain and allocation
inputs:
  duplex_realized_amount: 900000
  duplex_ca_basis: 400000
  cabin_realized_amount: 300000
  cabin_basis: 220000
  az_one_fmv: 720000
  az_two_fmv: 480000
steps:
  - duplex_deferred: duplex_realized_amount - duplex_ca_basis
  - cabin_deferred: cabin_realized_amount - cabin_basis
  - ca_source_deferred: duplex_deferred
  - az_one_share: ca_source_deferred * az_one_fmv / (az_one_fmv + az_two_fmv)
  - az_two_share: ca_source_deferred - az_one_share
  - sell_now_gain_taxed_by_ca: duplex_deferred + cabin_deferred
expected:
  duplex_deferred: 500000.00
  cabin_deferred: 80000.00
  ca_source_deferred: 500000.00
  az_one_share: 300000.00
  az_two_share: 200000.00
  sell_now_gain_taxed_by_ca: 580000.00
```

## When to refuse or refer

- The exchange's federal validity is in doubt (missed 45 or 180 days, the taxpayer touched the proceeds, a related-party sale within 2 years): resolve it with `us-section-1031-like-kind-exchange` before any California reporting.
- Years of annual FTB 3840 filings were missed, or the FTB has issued a notice: refer to a California practitioner; a voluntary disclosure or protest may be needed.
- Drop-and-swap, tenancy-in-common, Delaware statutory trust or UPREIT (section 721) structures: refer. The FTB pages read give no rule for how a section 721 contribution of a replacement property is treated for FTB 3840.
- An apportioning multistate business (Schedule R): refer the apportionment; this skill only places the line 18a percentage.
- Part-year residents and anyone who moved into California between the exchange and the sale: refer the 540NR computation and the other-state credit.

## Filing and payment

FTB 3840 is an information form; it carries no payment. It is attached to the California return for each year (Form 540, 540NR, 541, 100, 100S, 565, 568 or 199) by that return's due date, or filed on its own if there is no other California filing requirement. The 2025 instructions give, for calendar-year 2025 filers: individuals, estates and trusts 15 April 2026 (extended 15 October 2026); C corporations and LLCs taxed as C corporations 15 April 2026; S corporations, partnerships and LLCs taxed as either 16 March 2026; exempt organizations 15 May 2026. A due date on a weekend or holiday moves to the next business day ([FTB 3840 instructions (2025), C](https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html)). The 2026 due dates belong to each return's own skill.

Tax on the California-source deferred gain is paid with the return for the year the replacement property is sold.

## Completion checklist

- [ ] Federal exchange validated; California basis and depreciation used where they differ.
- [ ] Both filing conditions tested (California property out, out-of-state property in; some California gain deferred).
- [ ] Correct box: initial, annual, amended or final, with the exchange year entered.
- [ ] Part II matches Form 8824 lines 12 to 25.
- [ ] Schedule A line 8 counts only California properties; line 10 allocates the whole amount with a statement.
- [ ] Every later year has an annual FTB 3840 until the deferred gain is recognized; sold properties removed with a statement.
- [ ] Form 593 checked for boot over USD 1,500 or a failed exchange.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| FTB, 2025 Instructions for Form FTB 3840. Read for What's New (IRC as of 1 January 2025, real property only, the USD 250,000 and USD 500,000 AGI limits and dates), A Purpose, B Who Must File, C When and Where to File and the 2026 due dates, D Signature, F Failure to File, G Multiple Exchanges, H Multiple Asset Exchanges, Questions A to C, Parts I and II, Schedule A lines 1 to 11, and the sourcing rule; it cites R&TC 18031.5, 18032 and 24953. | https://www.ftb.ca.gov/forms/2025/2025-3840-instructions.html | 2026-11-21 |
| FTB 3840 (2025) form. Read for the entity boxes, Initial, Amended, Annual and Final boxes, the AGI note and the layout of Schedule A. | https://www.ftb.ca.gov/forms/2025/2025-3840.pdf | 2026-11-21 |
| FTB, Reporting like-kind exchanges, Internal Revenue Code section 1031 and FTB 3840 (last updated 01/28/2026). Read for the two filing conditions, annual filing, Notice of Proposed Assessment, Examples 1 and 2, mailing address and e-file. | https://www.ftb.ca.gov/file/personal/reporting-like-kind-exchanges.html | 2026-11-21 |
| FTB Publication 1100, Taxation of Nonresidents and Individuals Who Change Residency (rev. 10/2024). Read for section F, Examples 16, 17 and 18. | https://www.ftb.ca.gov/forms/misc/1100.html | 2026-11-21 |
| FTB, 2025 Instructions for Form 593. Read for the exchange rules: Part IV line 10 certification, boot over USD 1,500, the QI's duty, cash-poor exchanges, 3 1/3% on failed exchanges, the alternative exchange methods, the USD 100,000 exception and the line 32 dates. | https://www.ftb.ca.gov/forms/2025/2025-593-instructions.html | 2026-11-21 |
| FTB, 2025 Instructions for Schedule D-1. Read for Form 8824 completed with California amounts. | https://www.ftb.ca.gov/forms/2025/2025-540-d-1-instructions.html | 2026-11-21 |

Not yet confirmed: the 2026 FTB 3840 and instructions (not published on 2026-11-21; the 2025 versions are relied on); the text of R&TC 18031.5, 18032 and 24953 (leginfo.legislature.ca.gov refused our reader; cited as the FTB instructions name them); any FTB method for allocating the California-source deferred gain among several replacement properties (the instructions require an allocation and a statement but name no formula); FTB treatment of a section 721 (UPREIT) contribution of a replacement property.
