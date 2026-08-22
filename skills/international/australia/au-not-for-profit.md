---
name: au-not-for-profit
description: >
  Use this skill whenever asked about Australian not-for-profit (NFP) tax compliance -- income tax exemption self-assessment, the annual NFP self-review return, ACNC charity registration and ATO endorsement, the mutuality principle for licensed clubs and member associations, taxable NFP shade-in rates, deductible gift recipient (DGR) endorsement and gift/contribution deductibility, FBT rebate and exemption caps for NFP employers, GST concessions for NFPs, PAYG withholding for NFP employees, or NFP salary packaging. Trigger on phrases like "NFP tax", "charity tax concession", "DGR", "deductible gift", "mutuality", "self-review return", "FBT rebate", "club taxable income". ALWAYS read this skill before touching any NFP tax work.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 (NFP self-review return season: by 31 Oct 2026)"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Not-for-Profit -- NFP/DGR Tax Compliance Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context.** (1) From 1 July 2026 the $2 minimum threshold for DGR gift deductions is REMOVED -- backdated to gifts made from 1 July 2024 (all amounts deductible regardless of size; political donations excluded). (2) The NFP self-review return is an ANNUAL obligation from the 2023-24 income year -- non-charitable NFPs with an active ABN self-assessing as income-tax-exempt must lodge by 31 October each year; the 2023-24 return deadline was extended to 31 March 2025, but 31 October applies from 2024-25 onwards. (3) GIC and SIC incurred on or after 1 July 2025 are non-deductible for taxable NFPs.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1997 Div 50 (income tax exemption), Div 30 (gifts); FBTAA 1986 (ss 65J rebate, 57A exemption); GST Act 1999 (Div 176, 40-160 etc.) |
| Tax Authorities | ATO (income tax, DGR endorsement, FBT, GST); ACNC (charity registration) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); 2025-26 self-review return season closing |
| Exempt pathways | (1) ACNC-registered charity + ATO endorsement; (2) self-assessment under one of 8 Div 50 categories (non-charity) |
| Self-assessment categories (Div 50) | 8 categories: community service, cultural, educational, health, employment (trade unions, employer/employee associations), resource development, scientific, sporting |
| NFP self-review return | Annual, due 31 October, for non-charitable NFPs with active ABN self-assessing as exempt; first year 2023-24 |
| Taxable NFP company threshold | Taxable income <= $416: nil tax + non-lodgment advice; > $416: lodge company return |
| NFP shade-in (2026-27) | Base rate entity: $417-$762 at 55% of excess over $416, $763+ at 25% on whole; non-BRE: $417-$915 at 55%, $916+ at 30% on whole |
| FBT rebate (rebatable employers) | 47% of gross FBT payable, capped at first $30,000 grossed-up per employee per FBT year |
| FBT exemption (PBI/HPC) | Full exemption up to $30,000 grossed-up per employee; hospitals/ambulance $17,000 |
| GST registration threshold (NFP) | $150,000 (vs $75,000 for for-profit) |
| DGR gift minimum | From 1 July 2026 (backdated to 1 July 2024): no minimum. Before 1 July 2024: $2 |
| DGR contribution (minor benefit) | Contribution > $150 AND benefit < lesser of 20% of contribution and $150; deduction = contribution - benefit |
| PAYG withholding | Applies normally -- NFP status does NOT exempt from withholding for employees |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown charity status | Assume NOT a charity -- cannot self-assess as exempt; taxable until ACNC registration confirmed on the ACNC Register |
| Self-review return lodgment status unknown | Assume NOT lodged; flag ATO may treat the NFP as taxable for that year |
| NFP category unclear | Do NOT self-assess exemption; compute as taxable; escalate category fit |
| Member vs non-member split unknown | Assume all revenue non-member (assessable) until attendance/visitor records produced |
| DGR endorsement unknown | Check ABN Lookup DGR listing before telling any donor their gift is deductible |
| FBT status unknown (rebate vs exemption vs none) | Assume NO concession until endorsement type confirmed on ABN Lookup |
| Governing documents not sighted | Assume NFP character NOT established; mutuality and exemption both unavailable |
| Entertainment benefits salary packaged by NFP employer | Flag separately -- salary-packaged meal entertainment counts toward caps; non-salary-packaged does not count toward the rebate cap |

## Section 2 -- Refusal catalogue

Compute nothing in these areas; document the trigger and escalate to a specialist reviewer.

| Code | Trigger | Action |
|---|---|---|
| R-AU-NFP-1 | Charitable purpose or purposes questions: whether purposes are charitable at law, public benefit test, disqualifying purposes, Charities Act 2013 interpretation | Refuse; escalate to a lawyer. The ACNC's guidance is administrative, not legal advice |
| R-AU-NFP-2 | Public benevolent institution (PBI) status: whether the organisation's main purpose is benevolent relief of poverty/sickness/distress, PBI vs ordinary charity distinction | Refuse; escalate. PBI status changes FBT treatment (exemption vs rebate) and DGR eligibility -- a wrong call is a concession-integrity issue |
| R-AU-NFP-3 | DGR endorsement applications and pre-conditions: constitution amendments, gift fund requirements, winding-up clauses, specific DGR category fit, overseas aid fund questions | Refuse; escalate to the ACNC/ATO application process. You may assemble supporting documents but never submit or advise on eligibility |
| R-AU-NFP-4 | Political campaigning, advocacy and lobbying limits: whether activities breach charity law, disqualifying political purpose, election campaigning | Refuse; escalate to a lawyer. Both charity law and electoral law apply; the ACNC has deregistration powers |
| R-AU-NFP-5 | State-based concession applications: payroll tax exemption, land tax, stamp duty, gaming machine concessions -- each state and territory differs | Refuse; escalate to the relevant state revenue office process. This skill is Commonwealth tax only |
| R-AU-NFP-6 | Charity registration itself: ACNC application, subtype selection (advancing health, education, religion, PBI etc.), governing document review for ACNC purposes | Refuse; escalate to the ACNC registration process or a charity lawyer |
| R-AU-NFP-7 | Mutuality boundary disputes: whether a particular receipt is mutual or assessable where members and non-members are mixed (e.g. reciprocal club arrangements, joint memberships, corporate members) | Compute both ways; escalate the characterisation judgement |
| R-AU-NFP-8 | Ancillary funds (private or public): establishment, winding up, distribution rules, trustee obligations | Refuse; escalate. Ancillary funds carry special DGR conditions and ACNC/ATO dual oversight |

## Section 3 -- GL sweep library

Signs an NFP's books need attention before any compliance position is taken.

| GL pattern | Likely issue | Action |
|---|---|---|
| No NFP self-review return lodged for a self-assessing NFP | ATO may treat as taxable for that year; FTL penalties possible | Flag urgently; lodge ASAP; compute taxable fallback position |
| Gifts received booked as revenue without DGR check | Donor deduction risk; receipts may be misleading | Check DGR endorsement on ABN Lookup; if not endorsed, gifts are income but not deductible to donors |
| Member subscriptions and bar sales in one revenue account | Mutuality not separated | Split member vs non-member revenue before computing taxable income |
| "Donations" received for event tickets, auction items, raffle entries | Contributions, not gifts -- minor benefit rules apply | Apply 20%/$150 test per contribution; only excess is deductible to the donor |
| FBT rebate claimed on all benefits including amounts over $30,000 grossed-up | Rebate cap breach | Recompute: rebate = 47% x FBT on first $30,000 grossed-up per employee only |
| Salary-packaged meal entertainment in NFP employer books | Separate cap treatment -- counts toward $30,000 exemption/rebate cap | Flag; check aggregate against cap; entertainment facility leasing expenses also flagged |
| Employee wages with no PAYG withholding | NFP status wrongly assumed to exempt PAYG | Withholding applies from first dollar; register for PAYG withholding; check super guarantee too |
| Volunteer reimbursements with GST credits claimed | GST credit rules for volunteers differ | Only endorsed charities/gift-deductible entities claim GST credits on volunteer reimbursements |
| Fundraising event income with no GST treatment choice recorded | Fundraising input-taxed election not documented | Election must be made and recorded BEFORE supplies take place |
| "Charity" in the name but no ACNC registration | Cannot self-assess as exempt if all purposes charitable | Check ACNC Register; if charitable and unregistered, the NFP is taxable |

---

## Section 4 -- Worked examples

### Example 1 -- Self-assessing NFP: exemption confirmed, self-review return lodged

A community service association (not a charity) has an ABN and governing documents prohibiting distributions to members. Its purposes are community service (not political/lobbying) and it passes the physical presence in Australia test. It self-assesses as income-tax-exempt under Div 50.

```
2025-26 self-review return: lodged 15 October 2026 (before 31 October 2026)
Income tax result: exempt -- no company return, no income tax payable
```

Had the return NOT been lodged by 31 October: the ATO may treat the NFP as taxable for 2025-26, issue a lodgment demand, and FTL penalties can apply. Lodge immediately and document the board's self-assessment review.

### Example 2 -- Taxable NFP company: $900 taxable income, base rate entity

A social club (NFP company, BRE) computes taxable income of $900 for 2026-27 after mutuality apportionment.

```
Taxable income $900 falls in the $417-$762 band? No: $900 > $762.
Therefore: $763 and above -> 25% on the WHOLE amount.
Tax = $900 x 25% = $225
```

**Contrast -- same club but NOT a base rate entity** (e.g. high passive income):

```
$900 falls in the $417-$915 band -> 55% of excess over $416.
Tax = ($900 - $416) x 55% = $484 x 55% = $266.20
```

### Example 3 -- Taxable NFP company: $500 taxable income (shade-in band)

An NFP company (BRE) has taxable income of $500 for 2026-27.

```
$500 is in the $417-$762 band (BRE):
Tax = ($500 - $416) x 55% = $84 x 55% = $46.20
```

The shade-in ensures tax at $762 = ($762 - $416) x 55% = $190.30, which is less than $762 x 25% = $190.50 -- the bands meet at the crossover. Above $762 the flat 25% on the whole amount applies.

### Example 4 -- Mutuality apportionment: licensed club, Waratahs formula

A licensed club has for 2026-27: total visitors (A) = 18,000; members' guests (B) = 4,000; average subscribed members (R) = 2,200; average daily member attendance percentage (S) = 8%; trading days (T) = 360.

```
C = A - B = 18,000 - 4,000 = 14,000
Non-member percentage = [(B x 75%) + C] / [(R x S x T) + A]
  = [(4,000 x 0.75) + 14,000] / [(2,200 x 0.08 x 360) + 18,000]
  = [3,000 + 14,000] / [63,360 + 18,000]
  = 17,000 / 81,360
  = 20.9% (rounded)
```

The club applies 20.9% to apportionable bar and catering revenue and expenses:

```
Apportionable revenue $1,450,000 x 20.9% = $303,050 assessable (non-member share)
Apportionable expenses $1,280,000 x 20.9% = $267,520 deductible
Net contribution from non-member trading = $35,530
Plus investment income (fully assessable) = $12,000
Taxable income = $47,530 -> tax at 25% (BRE) = $11,882.50
```

The ATO accepts the Waratahs formula as a reasonable basis for registered/licensed clubs (NAT 73436). Simple methods (ticket counts, revenue percentages) are equally acceptable where they reasonably reflect member/non-member split. Recalculate the percentage EVERY year.

### Example 5 -- FBT rebate: rebatable employer over the cap

A community service NFP (rebatable employer, not a PBI) provides fringe benefits to an employee in the 2026-27 FBT year (1 April 2026 - 31 March 2027). Grossed-up taxable value = $38,000.

```
Rebate applies to the first $30,000 grossed-up only.
FBT on $30,000 x 47% FBT rate = $14,100 gross FBT
Rebate = 47% x $14,100 = $6,627
FBT on excess $8,000 x 47% = $3,760 (no rebate)
Net FBT payable = ($14,100 - $6,627) + $3,760 = $11,233
```

**Contrast -- same benefits provided by a PBI (FBT-exempt):**

```
First $30,000 grossed-up: exempt (FBT = nil)
Excess $8,000 x 47% = $3,760 FBT payable
```

### Example 6 -- DGR gift vs auction purchase contribution

**(a) Genuine gift.** Priya donates $200 cash to a DGR-endorsed charity, receiving nothing in return. From 1 July 2024 the $2 minimum no longer applies, so the full $200 is deductible (no benefit received).

**(b) Auction purchase with minor benefit.** Liam bids $500 at a DGR's charity auction for a ticket with a GST-inclusive market value of $90.

```
Contribution $500 > $150                                  PASS
Benefit $90 < lesser of (20% x $500 = $100) and $150      PASS ($90 < $100)
Deductible amount = $500 - $90 = $410
```

**(c) Benefit too large -- no deduction.** Bernie pays $400 for a gala ticket with a $100 market value: 20% of $400 = $80; benefit $100 > $80 -> minor benefit rules FAIL; no part of the $400 is deductible, even though the charity keeps it all.

**(d) Small gift under old rules.** A $1 donation made on 15 June 2024: not deductible (under the old $2 minimum). The same $1 donation made on or after 1 July 2024: deductible ($2 threshold removed, backdated).

---

## Section 5 -- Tier 1 rules

### Rule 1 -- Two exemption pathways: charity vs self-assessment

**Charity pathway:** an NFP whose purposes are ALL charitable must register with the ACNC and be endorsed by the ATO to be income-tax-exempt. A charitable NFP that does not register CANNOT self-assess -- it is taxable. Endorsement as a tax concession charity (TCC) also unlocks GST charity concessions and the FBT rebate or exemption, and refunds of franking credits.

**Self-assessment pathway:** a non-charitable NFP can self-assess as income-tax-exempt if it fits one of 8 categories in ITAA 1997 Div 50: community service, cultural, educational, health, employment (registered/recognised trade unions and employee/employer associations), resource development (aviation, tourism, ICT, agriculture etc.), scientific, and sporting. Each category has its own tests (generally: NFP character, society/association/club form, main purpose, not a charity, and one of three tests -- physical presence in Australia, prescribed by law, or listed by name), plus the governing rules condition and the income and assets condition. The $416/$762/$915 taxable-NFP thresholds do NOT apply to exempt organisations -- they apply only to NFPs that are taxable.

### Rule 2 -- The NFP self-review return (annual, from 2023-24)

Non-charitable NFPs with an active ABN that self-assess as income-tax-exempt must lodge an NFP self-review return each year, between 1 July and 31 October following the income year (substituted accounting periods: check the ATO page). The return confirms the organisation's continued eligibility -- purpose, NFP clauses in governing documents, and category fit. Not lodged -> the ATO may treat the NFP as taxable, issue a company return demand, and apply FTL penalties. The return is lodged via ATO online services (for business or agents); there is no paper form. Registered charities do NOT lodge this return -- their exemption rests on ACNC registration plus ATO endorsement, and they report to the ACNC via the Annual Information Statement instead.

### Rule 3 -- Taxable NFP companies: the $416 threshold and shade-in rates

An NFP company (including incorporated and unincorporated associations treated as companies) that is NOT exempt is taxable. Special rates apply (Income Tax Rates Act 1986): taxable income <= $416 -> nil tax, and the NFP may notify a non-lodgment advice instead of a return. Above $416, lodge a company return:

| Taxable income | Base rate entity | Not a base rate entity |
|---|---|---|
| $0-$416 | Nil (non-lodgment advice) | Nil (non-lodgment advice) |
| $417-$762 | 55% of excess over $416 | 55% of excess over $416 |
| $763-$915 | 25% on whole amount | 55% of excess over $416 |
| $916 and above | 25% on whole amount | 30% on whole amount |

The BRE test (aggregated turnover < $50m AND <= 80% passive income) applies to NFP companies in the same way as to for-profit companies (see au-company-tax). Clubs whose documents do NOT prohibit member distributions are "other taxable companies" -- no $416 threshold, standard company rates, return every year.

### Rule 4 -- Mutuality principle

Receipts from mutual dealings with members are NOT assessable income (mutual receipts); expenses incurred in deriving them are NOT deductible. The principle applies where the organisation and its members share a common identity: contributions to a common fund, and participation in the surplus only as member benefits, not distributions. Typical application: licensed clubs, sporting clubs, professional associations that are taxable. Members' subscriptions, bar sales to members, and members' raffle tickets are mutual receipts; sales to non-members, interest, rent, and grants from outside are assessable. Apportion mixed revenue and expenses using a reasonable method: simple methods (ticket counts, non-member revenue percentage) or the Waratahs formula for clubs (Example 4). The chosen method must reasonably reflect the actual member/non-member split and be recalculated each year. Mutuality does NOT apply to exempt organisations (no need), to "other taxable companies" (no NFP clause), or to dealings that are not truly mutual (e.g. a club trading with the public through a separate entity).

### Rule 5 -- DGR endorsement and gift deductibility

Only gifts to organisations with DGR status are deductible. DGR status comes from ATO endorsement (Item 1 -- the entity itself falls within a DGR category in Div 30 ITAA 1997, e.g. public benevolent institutions, public universities, public hospitals, public ancillary funds) or from being listed by name in the law (Item 2 / specific listing -- particular organisations named in the Div 30 tables or by legislative instrument). Most charities are NOT automatically DGRs -- ACNC registration is necessary but not sufficient except for PBIs and HPCs (which generally access DGR endorsement). Check ABN Lookup's DGR tool before advising any donor.

Gift conditions: voluntary transfer of money or property, no material benefit to the donor, and any special conditions on the DGR category (gift funds, overseas aid etc.). From 1 July 2026 the $2 minimum is removed, backdated to gifts from 1 July 2024. Issued receipts must show the fund name, ABN, that it is for a gift, and (community charities and ancillary funds) the donor's name.

Contributions (donor receives a benefit -- dinners, auctions, event tickets) are deductible only under the minor benefit rules: contribution exceeds $150, and the GST-inclusive benefit is less than the lesser of 20% of the contribution and $150. Deduction = contribution minus benefit. Maximum 2 attendance contributions per event per individual; auction purchases unlimited; a DGR running 15 or more same-type eligible events in a year loses eligibility for the later ones. Political contributions follow separate rules (the $2 removal does not apply).

### Rule 6 -- FBT for NFP employers

Two regimes, never mixed:

**FBT exemption (s 57A FBTAA):** PBIs and health promotion charities (ACNC-registered, ATO-endorsed) -- benefits exempt up to $30,000 grossed-up per employee per FBT year; public/NFP hospitals and public ambulance services -- $17,000 cap. A PBI that is also a hospital gets the hospital cap only. Amounts over the cap are fully taxable.

**FBT rebate (s 65J FBTAA):** rebatable employers -- charity institutions (not PBIs), religious institutions, certain scientific and public educational institutions, trade unions, employer associations, and NFPs established for community service, cultural, sporting, or resource-development purposes. Rebate = 47% of gross FBT payable, but only on the first $30,000 grossed-up per employee; excess attracts full FBT with no rebate. The rebate is claimed in the FBT return; the employer still lodges an FBT return and pays the net amount.

**Capping exclusions (both regimes):** car parking fringe benefits, meal entertainment NOT provided under a salary packaging arrangement, and entertainment facility leasing expenses do NOT count toward the $30,000 cap. Salary-packaged meal entertainment DOES count toward the cap (separately grossed-up). FBT year is 1 April - 31 March. NFP status does NOT exempt an employer from FBT registration where benefits are provided -- register, compute, claim the concession in the return.

### Rule 7 -- GST concessions for NFPs

Available concessions (GST Act 1999): the $150,000 GST registration threshold (all NFPs, automatic; vs $75,000 standard); no GST on genuine gifts received (voluntary, no material benefit); GST groups and non-profit sub-entities (choice); cash-basis accounting regardless of turnover (endorsed charities, gift-deductible entities, government schools -- must choose); non-commercial supplies GST-free (nominal consideration -- endorsed charities and gift-deductible entities); fundraising events input-taxed (choice, recorded before the event); raffles and bingo GST-free (lawful events); school tuckshop sales input-taxed (choice); volunteer expense reimbursement GST credits; donated second-hand goods GST-free; religious services GST-free (advancing religion subtype). Where a DGR is endorsed in part (for a fund only), concessions apply only to supplies connected with the fund's principal purpose. Register when turnover reaches $150,000; voluntary registration below that makes input tax credits available.

### Rule 8 -- PAYG withholding and payroll obligations

NFP status -- exempt, endorsed, or taxable -- does NOT relieve an employer of PAYG withholding. Withhold from employee wages from the first dollar, report via Single Touch Payroll, pay super guarantee (12% from 1 July 2026 -- see au-super-guarantee), and meet workers compensation and state payroll tax obligations unless a state exemption applies. Volunteers are not employees; genuine reimbursements of volunteer expenses are not wages, but allowances and honoraria can be -- characterise before assuming no withholding. Contractors: check the employee/contractor boundary the same as for any employer.

### Rule 9 -- Salary packaging in the NFP sector

NFP employees can salary-package benefits up to the employer's cap ($30,000 grossed-up for PBI/HPC-exempt employers or rebatable employers; $17,000 for hospitals) with the FBT concession absorbing the cost that a for-profit employer would pay. Common packaged items: living expenses (mortgage, rent, general purchases up to the cap), meal entertainment (separate rules; salary-packaged meal entertainment counts toward the cap), and venue hire. Novated leases and remote-area benefits follow the standard FBT rules. Amounts packaged beyond the cap attract full FBT (for exempt employers) or unrebated FBT (for rebatable employers) -- model the employee's package against the cap before committing. Reportable fringe benefits (RFBA) still appear on the employee's income statement where the grossed-up taxable value exceeds $2,000, affecting HELP repayments, Medicare levy surcharge, and some offsets even though the employer paid no FBT.

### Rule 10 -- State concessions (flag only)

States and territories grant payroll tax exemptions, land tax concessions, stamp duty relief, and gaming concessions, generally keyed to charity status (ACNC registration) or to specific purposes. Each state's tests differ -- e.g. NSW payroll tax exemption under Sch 2 of the Payroll Tax Act 2007 (NSW) for charitable organisations; Victoria, Queensland and others have their own Acts and public benevolent/charitable tests. Do NOT advise on eligibility or applications (R-AU-NFP-5); flag the existence of the concession and refer to the state revenue office.

### Rule 11 -- ACNC vs ATO division of labour

The ACNC registers charities, determines charity subtypes (including PBI), maintains the Charity Register, receives Annual Information Statements, and regulates charity governance. The ATO administers ALL tax outcomes: endorsement for charity tax concessions (income tax exemption, GST charity concessions, FBT rebate/exemption), DGR endorsement, the NFP self-review return, taxable NFP returns, and all FBT/GST/PAYG administration. One application to the ACNC can be forwarded to the ATO for endorsement; the ATO decides the tax questions independently. An organisation dealing with "charity status" goes to the ACNC; one dealing with "tax status" goes to the ATO; most questions involve both.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Self-review return never lodged

**Trigger:** self-assessing NFP with ABN; no self-review return on file for 2023-24 or later years. **Issue:** ATO may treat the NFP as taxable from the first missed year; historical FTL exposure. **Action:** lodge outstanding returns immediately; compute the taxable fallback for each missed year; document the board's exemption review.

### T2-2 -- Charity-shaped but unregistered

**Trigger:** purposes all charitable, no ACNC registration, client assumes exemption. **Issue:** self-assessment is NOT available to charities -- the NFP is taxable regardless of how worthy its purposes are. **Action:** compute as taxable; escalate ACNC registration (R-AU-NFP-6); amend any prior positions taken on an exempt basis.

### T2-3 -- DGR receipt practice

**Trigger:** the NFP issues "tax deductible" receipts but DGR endorsement is unconfirmed, in part only, or for a fund whose purpose the receipted gift does not match. **Issue:** donors claim deductions they are not entitled to; the NFP risks misleading-conduct exposure. **Action:** verify endorsement scope on ABN Lookup; restrict deductible receipts to the endorsed fund/purpose; review receipt wording.

### T2-4 -- Mutuality method shopping

**Trigger:** the apportionment method changes year to year, or the chosen method produces an implausibly low non-member percentage. **Issue:** the method must reasonably reflect the actual split; the ATO can substitute its own apportionment. **Action:** document the method and data (registers, surveys, till splits); keep it consistent unless the facts change.

### T2-5 -- FBT cap tracking across benefit types

**Trigger:** salary-packaged meal entertainment plus living-expense benefits for the same employee. **Issue:** packaged meal entertainment counts toward the $30,000 cap alongside other benefits; non-packaged meal entertainment does not. **Action:** track the grossed-up aggregate per employee per FBT year; model before packaging more.

### T2-6 -- NFP trading subsidiary

**Trigger:** the NFP channels commercial activity through a separate company. **Issue:** mutuality does not reach the subsidiary; income tax exemption depends on the subsidiary's own status (charitable purpose and ACNC registration, or taxable at standard rates with possible donation back under gift rules). **Action:** map the structure; compute the subsidiary standalone; escalate structuring questions.

---

## Section 7 -- Excel working paper template

```
AUSTRALIA NFP -- ANNUAL COMPLIANCE WORKING PAPER
Organisation: [name]   ABN: [____]   Income year: [2025-26 / 2026-27]   Prepared: [date]

STATUS
  ACNC-registered charity? [Y/N -- check ACNC Register]   Subtype: [PBI/HPC/religion/etc.]
  ATO endorsement: ITEx [Y/N]  TCC [Y/N]  DGR [Y/N -- item/fund scope: ____]
  Self-assessment category (non-charity): [community service / cultural / educational /
    health / employment / resource development / scientific / sporting]
  Governing documents sighted, NFP clauses present: [Y/N]

INCOME TAX
  Exempt (charity + endorsed / self-assessed + return lodged): [Y/N]
  Self-review return lodged by 31 October: [Y/N/NA-charity]
  If taxable -- mutuality method: [simple / Waratahs / other]  Non-member %: [____]
  Assessable income: AUD [____]   Deductible expenses: AUD [____]
  Taxable income: AUD [____]   Rate band: [$0-416 / $417-762 / $763-915 / $916+]
  BRE limbs (turnover < $50m; BREPI <= 80%): [Y/N]   Tax: AUD [____]
  Return lodged / non-lodgment advice: [____]

DGR / GIFTS
  DGR endorsement scope confirmed on ABN Lookup: [Y/N]
  Gifts: AUD [____]   Contributions (events/auctions): AUD [____]
  Minor benefit valuations documented: [Y/N]   Receipts compliant: [Y/N]

FBT (year ended 31 March [__])
  Status: [exempt PBI/HPC $30k / exempt hospital $17k / rebatable 47% $30k / none]
  Per-employee grossed-up over cap? [list]   Packaged meal entertainment in cap: [Y/N]
  FBT return lodged; rebate/exemption claimed: [Y/N]

GST
  Turnover: AUD [____]  Registered: [Y/N]  $150,000 threshold: [met/not]
  Concessions used: [cash basis / fundraising input-taxed / sub-entities / other]
  Elections recorded before supplies: [Y/N]

PAYROLL
  PAYG withholding registered and withheld: [Y/N]   STP current: [Y/N]
  Super guarantee 12% (from 1 Jul 2026): [Y/N]
  State payroll tax exemption claimed: [Y/N -- state: ____]

FLAGS
  Refusal triggers hit (R-AU-NFP-1..8): [____]   Tier 2 flags (T2-1..6): [____]
```

---

## Section 8 -- Reading guide

1. Status before numbers: establish charity registration, endorsement, or self-assessment category from the ACNC Register and ABN Lookup before computing anything -- income tax, FBT, GST and receipts all depend on it.
2. Charities cannot self-assess: all-charitable purposes plus no ACNC registration means taxable, no matter how worthy the purposes look.
3. The self-review return is annual and cheap; the cost of not lodging is a taxable year plus penalties. Diarise 31 October.
4. Mutuality only helps taxable NFPs. Exempt organisations do not need it; "other taxable companies" cannot use it.
5. FBT: exemption (PBI/HPC) and rebate (everyone else) are mutually exclusive, both capped at $30,000 grossed-up per employee; salary-packaged meal entertainment counts toward the cap, non-packaged does not.
6. Gifts and contributions are different animals: a ticket, dinner or auction win is a contribution needing the 20%/$150 minor benefit test, and only the excess over the benefit is deductible.

---

## Section 9 -- Onboarding fallback

If the client provides only financial statements and an ABN:

1. Look up the ABN: charity registration, ITEx/TCC endorsement, DGR status and scope
2. Run the Section 3 sweep; list mutuality data gaps and DGR receipt risks
3. Compute the taxable fallback (mutuality NOT applied where records are absent -- treat all revenue as assessable)
4. Draft the FBT and GST position as "no concession" pending endorsement evidence
5. **Flag:** "Computed from financial statements and public registers only. Governing documents, member/non-member records, endorsement instruments, election records and board reviews not sighted. Self-review return lodgment status unconfirmed. Reviewer must verify before any position is taken."

---

## Section 10 -- Reference material

### Key figures (2025-26 and 2026-27)

| Item | 2025-26 | 2026-27 |
|---|---|---|
| NFP company nil threshold | $416 | $416 |
| Shade-in band (BRE / non-BRE) | $417-$762 / $417-$915 at 55% over $416 | same |
| Flat rate above band (BRE / non-BRE) | 25% from $763 / 30% from $916, whole amount | same |
| Self-review return due | 31 October 2025 | 31 October 2026 |
| FBT rebate / cap | 47% / $30,000 grossed-up per employee | same |
| FBT exemption caps (PBI/HPC / hospital) | $30,000 / $17,000 grossed-up | same |
| FBT rate | 47% | 47% |
| GST registration threshold (NFP) | $150,000 | $150,000 |
| DGR gift minimum | $2 (removed from 1 Jul 2026, backdated to 1 Jul 2024) | none |
| Contribution minor benefit test | > $150 contribution; benefit < lesser of 20% and $150 | same |
| Super guarantee rate (see au-super-guarantee) | 11.5% | 12% |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Exemption categories | ITAA 1997 Div 50; ato.gov.au Types of income tax exempt organisations (8 categories); Income tax exempt organisations |
| Self-review return | ato.gov.au NFP self-review return reporting requirement (QC 73184); due date 31 October; first year 2023-24 |
| Taxable NFP rates | Income Tax Rates Act 1986 s 23; ato.gov.au Taxable NFP organisations (QC 33593, updated 26 August 2025); Changes to company tax rates (NFP $416/55% bands). Currency confirmed: the ATO's Changes to company tax rates page states the base-rate-entity shade-in limit of $762 applies "for the 2021-22 income year and later years", so the $762/$915 crossovers stand for 2026-27 |
| Mutuality | ato.gov.au Mutuality and taxable income for not-for-profits (NAT 73436); Waratahs formula [(B x 75%) + C] / [(R x S x T) + A]; TD 93/194 |
| DGR endorsement | ITAA 1997 Div 30; ato.gov.au Is my organisation eligible for DGR endorsement; ABN Lookup DGR tool |
| Gift deductions | ato.gov.au Gifts and donations (QC 72185, updated 6 July 2026 -- $2 threshold removed from 1 Jul 2026, backdated to 1 Jul 2024) |
| Contribution minor benefit | ato.gov.au Plan fundraising dinners or auctions with confidence (QC 107542, 16 June 2026); Valuing contributions and minor benefits |
| FBT rebate | FBTAA 1986 s 65J; ato.gov.au FBT rebatable employers (QC 71167); Completing your FBT return 2026 -- NFP employers |
| FBT exemption | FBTAA 1986 s 57A; ato.gov.au FBT-exempt organisations (PBI/HPC $30,000; hospital/ambulance $17,000) |
| GST concessions | A New Tax System (GST) Act 1999; ato.gov.au GST concessions available to your organisation (QC 107815, published 30 July 2026) |
| ACNC/ATO roles | acnc.gov.au Charity tax concessions; acnc.gov.au Organisations that have been self-assessing as income tax exempt |
| PAYG | TAA 1953 Sch 1 Div 12; ato.gov.au PAYG withholding (no NFP carve-out) |

### Test suite

**Test 1:** Self-assessing community service NFP, ABN active, 2025-26 return lodged 20 October 2026. -> Exempt; timely (before 31 October 2026).

**Test 2:** Same NFP, no return lodged by December 2026. -> ATO may treat as taxable; lodge immediately; compute taxable fallback.

**Test 3:** Taxable NFP company (BRE), taxable income $500. -> ($500 - $416) x 55% = $46.20.

**Test 4:** Taxable NFP company (BRE), taxable income $900. -> $900 > $762, so 25% on whole = $225. (Non-BRE: ($900-$416) x 55% = $266.20.)

**Test 5:** Waratahs: A=18,000, B=4,000, R=2,200, S=8%, T=360. -> Non-member % = 17,000/81,360 = 20.9%.

**Test 6:** Rebatable employer, grossed-up benefits $38,000 for one employee. -> Rebate = 47% x FBT on $30,000 = $6,627; excess $8,000 fully taxed; net FBT $11,233.

**Test 7:** PBI employer, same $38,000. -> First $30,000 exempt; FBT only on $8,000 x 47% = $3,760.

**Test 8:** Auction bid $500, benefit $90. -> $500 > $150; $90 < lesser of $100 and $150; deduction $410.

**Test 9:** Gala ticket $400, benefit $100. -> 20% of $400 = $80; $100 > $80 -> no deduction.

**Test 10:** $1.50 gift to a DGR made August 2024. -> Deductible ($2 minimum removed from 1 July 2026, backdated to 1 July 2024). Same gift made May 2024 -> not deductible.

### Prohibitions

- NEVER treat a charitable-purpose NFP as self-assessing -- charities need ACNC registration plus ATO endorsement
- NEVER skip the NFP self-review return for a self-assessing NFP with an ABN -- annual, 31 October
- NEVER apply the $416 threshold or shade-in rates to an exempt organisation -- they are for taxable NFPs only
- NEVER tell a donor a gift is deductible without confirming DGR endorsement and scope on ABN Lookup
- NEVER treat an event ticket, dinner or auction purchase as a plain gift -- run the 20%/$150 minor benefit test
- NEVER claim the FBT rebate above the $30,000 per-employee grossed-up cap, or for a PBI/HPC (they are exempt, not rebatable)
- NEVER count salary-packaged meal entertainment outside the cap -- packaged entertainment counts toward it
- NEVER assume NFP status removes PAYG withholding, STP, or super guarantee obligations
- NEVER advise on ACNC registration, DGR applications, PBI status, charitable purpose at law, political activity limits, or state concessions -- escalate (Section 2)
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
