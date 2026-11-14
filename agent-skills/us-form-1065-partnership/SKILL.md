---
name: us-form-1065-partnership
description: "Prepare the 2026 Form 1065, the US partnership return, with Schedules K and K-1, for general and limited partnerships, LLPs and multi-member LLCs taxed as partnerships. Covers who files, the K-1 items (tax basis capital, liabilities, section 704(c), section 199A code Z), guaranteed payments against distributive share under section 707(c), partner self-employment earnings and the limited partner exclusion in section 1402(a)(13) after Soroban and the Fifth Circuit's Sirius Solutions opinion of August 2026, pointers to the partner's basis, at-risk, passive and excess business loss limits, the Schedules K-2 and K-3 domestic filing exception and the small partnership exception, the BBA centralized partnership audit regime with the Schedule B-2 election out and the partnership representative, and the section 6698 late-filing penalty of USD 260 per partner per month for returns due in 2027 (Rev. Proc. 2025-32 section 4.55). A calendar 2026 return is due 15 March 2027, or 15 September 2027 wit"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-form-1065-partnership"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US Form 1065 partnership return, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 704, 707, 1402, 6221, 6223, 6226 and 6698, Rev. Proc. 2025-32, the Instructions for Form 1065 (2025), the Partner's Instructions for Schedule K-1 (2025), the Partnership Instructions for Schedules K-2 and K-3 (2025), the Instructions for Form 7004, Treas. Reg. 1.707-1(c), the IRS First Time Abate page and the Fifth Circuit's substituted opinion in Sirius Solutions (No. 24-60240, 12 August 2026), read on 2026-11-13. The 2026 editions of Form 1065 and its instructions were not yet published on that date; line and box references are from the 2025 editions and must be checked against the 2026 forms. No accountant has reviewed this skill. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Every partnership, including a multi-member LLC that has not elected corporate treatment, files Form 1065 for 2026 even if it owes no tax. A calendar-year return is due **15 March 2027** (a Monday); Form 7004 filed by that date extends filing six months, to **15 September 2027**. Filing late costs **USD 260 per partner per month or part of a month, for up to 12 months**, under section 6698 as adjusted for returns required to be filed in 2027. A payment to a partner fixed without regard to partnership income is a **guaranteed payment** (section 707(c)): deductible by the partnership, ordinary income to the partner even in a loss year, self-employment income when paid for services (also for limited partners), and not qualified business income. A payment that depends on partnership income is a **distributive share**. A domestic partnership with no foreign activity and only US individual-type partners can skip Schedules K-2 and K-3 if it tells its partners and no partner asks by the 1-month date. A partnership with 100 or fewer eligible partners (individuals, C and S corporations, eligible foreign entities, estates of deceased partners) can elect out of the BBA audit regime on Schedule B-2; otherwise it must name a partnership representative.

## Scope and who this is for

In scope: Form 1065 for tax year 2026 (calendar year 2026, or a fiscal year beginning in 2026) for an entity treated as a partnership for federal tax:

- general partnerships, limited partnerships (including family limited partnerships), LLPs and LLLPs;
- LLCs with two or more members that have not elected to be taxed as a corporation (default classification, Treas. Reg. 301.7701-3(b)(1)(i));
- joint ventures and investment clubs that are partnerships under section 761 and Treas. Reg. 1.761-1(a);
- a foreign partnership with US-source income or income effectively connected with a US trade or business, to the extent Form 1065 is its return (see step 1).

What the skill produces: Form 1065 with Schedules B, K, L, M-1 and M-2; Schedule B-1 (owners of 50% or more) when triggered; Schedule B-2 (election out of the centralized audit regime) when made; one Schedule K-1 per partner; Schedules K-2 and K-3 unless an exception applies; Schedule M-3 when required; the common attached forms; and a reviewer brief covering the audit-regime choice, section 704(b) and 704(c) points, section 752 liability shares, each partner's loss-limit flags and each partner's self-employment classification.

Out of scope, and where it goes:

| Topic | Skill or action |
| --- | --- |
| LLC that elected C corporation treatment (Form 8832) | `us-form-1120-c-corp` |
| LLC that elected S corporation treatment (Form 2553) | the S corporation return skill (Form 1120-S); refer if none is loaded |
| Single-member LLC with no election (disregarded) | `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation` |
| Partner-level self-employment tax computation (Schedule SE, wage base, rates) | `us-schedule-c-and-se-computation` |
| Partner-level qualified business income deduction and its 2026 thresholds | `us-qbi-deduction` |
| Section 179 and bonus depreciation figures | `us-section-179-and-bonus-depreciation` |
| Real estate professional status and short-term rentals | `us-real-estate-professional-and-short-term-rentals` |
| State partnership returns, pass-through entity tax elections, nonresident withholding | `us-pte-state-matrix` and the state's skill |
| Partners' estimated tax | `us-quarterly-estimated-tax` |
| Other 2026 federal changes | `us-2026-federal-tax-changes` |

## Ask the client first

1. **Who were the partners at any time in 2026?** Names, TINs, entity type of each (individual, C corporation, S corporation, partnership, trust, disregarded entity, IRA, estate, foreign), domestic or foreign, and anyone who joined or left during the year. This drives K-1 count, the Schedule B-2 test, the K-2/K-3 exceptions and the section 6698 penalty count.
2. **What does the agreement say about payments to partners?** Each fixed amount (salary, draw, interest on capital, health insurance) and each profit-based amount, and whether any payment has a minimum. This decides guaranteed payment against distributive share (step 4).
3. **What does each partner actually do?** Manager or not, hours, authority to sign contracts, personal liability. This decides Item G and Box 14 self-employment earnings (step 5).
4. **Any foreign activity at all?** Foreign customers paid from abroad, foreign taxes on a broker 1099, foreign funds, foreign accounts, branches, or interests in foreign entities. This decides Schedules K-2 and K-3 (step 11).
5. **Year-end balance sheet and receipts:** total receipts and total assets, prior-year tax basis capital for each partner, all loans with their guarantees and lenders, and any property contributed or distributed. This decides Schedules L, M-1, M-2, M-3, Item K1 to K3, Item L and Items M and N.
6. **Was the 2025 return filed on time, and was a Form 7004 filed for 2026?** Needed for the due date, any penalty exposure and the penalty relief history (Filing and payment).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Late-filing penalty per partner per month, returns required to be filed in 2027 (section 6698(b)(1) as adjusted) | USD 260 | [Rev. Proc. 2025-32, section 4.55](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Maximum months the section 6698 penalty runs | 12 | [26 U.S.C. 6698(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6698.htm) |
| Late S corporation return penalty per shareholder per month, returns due in 2027 (do not confuse with 6698) | USD 260 | [Rev. Proc. 2025-32, section 4.56](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Failure to furnish a correct K-1 (section 6722), general rule, per statement required to be furnished in 2027 | USD 340 | [Rev. Proc. 2025-32, section 4.58](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Same, corrected within 30 days of the furnishing date | USD 60 | [Rev. Proc. 2025-32, section 4.58](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Due date, calendar-year return | 15th day of 3rd month after year end: 15 March 2027 | [Instructions for Form 1065 (2025), When To File](https://www.irs.gov/pub/irs-pdf/i1065.pdf) |
| Form 7004 automatic extension of time to file | 6 months: 15 September 2027 | [Instructions for Form 7004](https://www.irs.gov/pub/irs-pdf/i7004.pdf) |
| Election out of the centralized audit regime: K-1s the partnership must furnish (plus S corporation partners' shareholders) | 100 or fewer | [26 U.S.C. 6221(b)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapC-partI-sec6221.htm) |
| Push-out election window after notice of final partnership adjustment | 45 days | [26 U.S.C. 6226(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapC-partII-sec6226.htm) |
| Push-out interest: underpayment rate with this substitution | 5 percentage points for 3 | [26 U.S.C. 6226(c)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapC-partII-sec6226.htm) |
| K-2/K-3 domestic filing exception: most creditable foreign tax on passive income shown on a payee statement | USD 300 | [Instructions for Schedules K-2 and K-3 (2025)](https://www.irs.gov/pub/irs-pdf/i1065s23.pdf) |
| Schedule B question 4 (no Schedules L, M-1, M-2, Item L; small partnership K-2/K-3 exception): total receipts less than | USD 250,000 | [Instructions for Schedules K-2 and K-3 (2025), Small Partnership Filing Exception](https://www.irs.gov/pub/irs-pdf/i1065s23.pdf) |
| Same test: total assets at year end less than | USD 1 million | [Instructions for Schedules K-2 and K-3 (2025), Small Partnership Filing Exception](https://www.irs.gov/pub/irs-pdf/i1065s23.pdf) |
| Schedule M-3 required: total assets at year end, or adjusted total assets, of | USD 10 million or more | [Instructions for Form 1065 (2025), Item J](https://www.irs.gov/pub/irs-pdf/i1065.pdf) |
| Schedule M-3 required: total receipts of | USD 35 million or more | [Instructions for Form 1065 (2025), Item J](https://www.irs.gov/pub/irs-pdf/i1065.pdf) |
| Schedule M-3 required: a reportable entity partner owns | 50% or more | [Instructions for Form 1065 (2025), Item J](https://www.irs.gov/pub/irs-pdf/i1065.pdf) |
| Mandatory e-filing of Form 1065 and K-1s: partners more than | 100 | [Instructions for Form 1065 (2025), Electronic Filing](https://www.irs.gov/pub/irs-pdf/i1065.pdf) |
| Gross receipts test, 2026 (section 448(c); section 163(j) small business exemption, Form 8990 trigger) | USD 32,000,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess business loss threshold, 2026 (section 461(l)), single (partner level) | USD 256,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess business loss threshold, 2026 (section 461(l)), joint returns (partner level) | USD 512,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

The statutory base of the section 6698 penalty is USD 195, indexed under section 6698(e) and rounded down to a multiple of USD 5. The adjusted amount is keyed to the calendar year the return is **required to be filed**, not the tax year: USD 255 applied to 2025 returns filed in 2026 (Instructions for Form 1065 (2025), Penalties); USD 260 applies to 2026 returns filed in 2027. The Social Security wage base, the self-employment rates and the qualified business income thresholds are owned by `us-schedule-c-and-se-computation` and `us-qbi-deduction`.

### Step 1: does the entity file Form 1065?

Section 6031(a) requires every partnership to file a return. It is an information return: the partnership pays no income tax (except an imputed underpayment after a BBA audit, step 13, and a section 7519 required payment for a section 444 fiscal year). Partners report their shares whether or not distributed.

| Entity | Default federal classification | Form 1065? |
| --- | --- | --- |
| LLC with two or more members, no election | Partnership | Yes |
| Same LLC, Form 8832 election to corporation | Corporation | No: Form 1120 |
| Same LLC, Form 2553 S election | S corporation | No: Form 1120-S |
| General partnership, LP, LLP, LLLP | Partnership | Yes |
| Single-member LLC, no election | Disregarded | No: Schedule C, E or F |
| LLC owned only by spouses as community property, Rev. Proc. 2002-69 treatment chosen | Disregarded (one owner) | No |
| Spouses' qualified joint venture under section 761(f), not held through a state-law entity | Two Schedules C | No |
| Co-owners of rental property only, no business beyond customary services | Co-ownership, not a partnership | No: each files Schedule E |
| Investment club | Usually a partnership | Yes, unless a valid section 761(a) election |

- **Section 761(a) election out of subchapter K.** Available only for investment-only arrangements, joint production, extraction or use of property, and a few narrow cases, where partners can compute their income without a partnership computation (Treas. Reg. 1.761-2). Rare. If claimed, check it was made on a timely Form 1065 for the first year and that no Form 1065 has been filed since.
- **Rev. Proc. 2002-69 and section 761(f) are different.** The first is for an LLC held by spouses as community property under state law with no other owner; the second is for spouses' joint ventures not held through a state-law entity, in any state. Both replace Form 1065 with Schedule C reporting.
- **Foreign partnerships.** A foreign partnership files Form 1065 if it has income effectively connected with a US business or US-source gross income, subject to the exceptions in Treas. Reg. 1.6031(a)-1(b)(3). A US person with a large interest in a foreign partnership may also owe Form 8865; both can apply. This skill flags Form 8865 but does not prepare it (R-1065-8865).

### Step 2: tax year and due date

1. **Tax year.** Section 706(b) requires the partnership's required taxable year: the majority-interest year, then the principal partners' year, then least aggregate deferral. Another year needs a section 444 election (with the section 7519 required payment) or a business-purpose year under Rev. Proc. 2002-39. Most partnerships are calendar year.
2. **Original due date:** 15th day of the 3rd month after year end. Calendar 2026: **Monday 15 March 2027**. Fiscal year ending 30 June 2027: 15 September 2027. When the date is a Saturday, Sunday or legal holiday, the next business day.
3. **Extension:** Form 7004, filed by the original due date, gives an automatic 6 months (calendar 2026: Wednesday 15 September 2027). No reason is needed. A Form 7004 filed late is no extension, and the penalty runs from the original due date.
4. **K-1s** go to partners by the return due date, including extensions. Partners waiting for a September K-1 usually extend their own return to 15 October 2027.

### Step 3: ordinary business income and separately stated items

1. Compute page 1 ordinary business income (loss), line 23 in the 2025 layout: receipts less deductions, with guaranteed payments to partners on line 10 (step 4).
2. Move every separately stated item to Schedule K: rental real estate (Form 8825, line 2), other rental, guaranteed payments (line 4a services, 4b capital, 4c total), interest, dividends, royalties, capital gains, section 1231 gain (Form 4797), section 179 (Form 4562), charitable contributions, investment interest, credits, self-employment earnings (line 14), and other items.
3. Allocate each Schedule K line among the partners under the agreement (subject to section 704(b), step 7) and enter each share on the K-1. **Reconcile:** the sum of every K-1 box equals the matching Schedule K line, partner by partner. Any difference is a preparer error. Put the reconciliation table in the reviewer brief.

### Step 4: guaranteed payment or distributive share

This is the decision most often got wrong on partnership returns.

1. **The test (section 707(c)).** A payment to a partner for services or for the use of capital is a guaranteed payment **to the extent it is determined without regard to the income of the partnership**. It is treated as made to a non-partner only for gross income (section 61(a)) and, subject to section 263, for the deduction (section 162(a)).
2. **If the amount depends on partnership income** (a percentage of profits, a priority allocation of profits), it is part of the distributive share, not a guaranteed payment. The Form 1065 instructions say plainly: do not include distributive shares of partnership profits on line 10.
3. **Minimum guarantees (Treas. Reg. 1.707-1(c), Example 2).** A partner entitled to a share of income but not less than a fixed sum has a guaranteed payment only for the shortfall: 30% of income with a USD 10,000 floor, income of USD 20,000, gives a USD 6,000 distributive share and a USD 4,000 guaranteed payment; with income of USD 60,000 there is no guaranteed payment.
4. **Fixed payment plus a share (Example 3).** A partner paid USD 10,000 plus 30% of income or loss, where the partnership has a USD 9,000 loss after the payment, reports the USD 10,000 as ordinary income and separately a USD 2,700 share of the loss (subject to section 704(d)).
5. **Where it goes:**
   - Partnership: deduct on page 1, line 10, if allocable to a trade or business and not capitalized. Payments for syndication are guaranteed payments but capital expenditures: not deductible on line 10, still reported on Schedule K line 4b and K-1 box 4b. Health insurance paid for a partner (and spouse, dependents, children under 27) is a guaranteed payment on line 10.
   - Schedule K line 4a (services), 4b (capital), 4c (total); K-1 boxes 4a, 4b, 4c.
   - Partner: ordinary income in the partner's tax year in which the partnership year ends, whether or not paid, and even when the partnership has a loss.
6. **Consequences that make the choice matter:**
   - **Self-employment:** guaranteed payments for services are net earnings from self-employment for general and limited partners alike (section 1402(a)(13), step 5).
   - **Qualified business income:** guaranteed payments under section 707(c) and payments under section 707(a) for services are not QBI (Instructions for Form 1065 (2025), section 199A list). A profit share from the same business is QBI.
   - **Passive activity:** guaranteed payments for services are not passive income; guaranteed payments for capital are treated as interest for section 469.
   - **Property in satisfaction:** a transfer of partnership property to pay a guaranteed payment is a sale or exchange, not a distribution (Rev. Rul. 2007-40).
7. **Section 707(a) payments** to a partner acting other than as a partner (an arm's-length fee, rent, a loan) are third-party transactions, not guaranteed payments. Disguised payments for services and disguised sales (section 707(a)(2)) are flagged for the reviewer (R-1065-707A).

### Step 5: self-employment earnings, Schedule K line 14 and K-1 box 14

1. **General partners and LLC member-managers:** box 14, code A is the partner's distributive share of trade or business ordinary income plus guaranteed payments, using the worksheet in the Form 1065 instructions. Excluded for everyone (section 1402(a)(1) to (3)): rentals from real estate (unless a dealer, or significant services to occupants), dividends and interest not received in a dealer business or on business receivables, royalties not received in a trade or business, and gains on property other than inventory, which takes out section 1231 and capital gains. A group investment program's earnings are generally not self-employment earnings for any partner.
2. **Limited partners:** the distributive share is excluded; only guaranteed payments for services actually rendered are included (section 1402(a)(13)). The instructions add that whether a partner is a limited partner for this purpose depends on section 1402(a)(13), not the label.
3. **Who is a limited partner for section 1402(a)(13)?** The law is moving:
   - *Soroban Capital Partners LP v. Commissioner*, 161 T.C. 310 (2023): a functional test; the exclusion is for passive investors, and the partners of an investment manager who ran the business were not limited partners.
   - *Sirius Solutions, L.L.L.P. v. Commissioner*, No. 24-60240 (5th Cir.), substituted opinion filed 12 August 2026 on rehearing: the earlier opinion (165 F.4th 374) was withdrawn. The court held the original public meaning of "limited partner" is **a partner who plays no significant role in managing or running a business**, rejected the Tax Court's reliance on Soroban's passive-investor standard without that analysis, and vacated and remanded. It binds courts in the Fifth Circuit (Texas, Louisiana, Mississippi); elsewhere the Tax Court follows Soroban.
   - The 1997 proposed regulations (proposed Treas. Reg. 1.1402(a)-2) were never finalized: limited partner only if no personal liability, no authority to contract, and no more than 500 hours of service a year. Some practitioners still use them as a guide.
4. **The default in this skill:** a state-law limited partner or non-managing LLC member who plays no significant management role gets box 14 code A of guaranteed payments for services only. A partner labeled limited who manages, signs contracts or works substantially in the business is flagged (R-1065-SE), and the reviewer decides and documents the position; the conservative position subjects the distributive share to self-employment tax to the extent it pays for services. LLC member-managers are treated as general partners.
5. **Codes B and C** carry gross farming or fishing income and gross nonfarm income for the partner's optional method. Do not complete box 14 for a partner that is an estate, trust, corporation, exempt organization or IRA.
6. **Nonresident alien partners** have no net earnings from self-employment, whatever their role (section 1402(b), unless a totalization agreement says otherwise).
7. The partner computes the tax on Schedule SE: see `us-schedule-c-and-se-computation`.

### Step 6: the K-1 items, 2025 layout

| Item or box | What goes there | Watch for |
| --- | --- | --- |
| G | General partner or LLC member-manager, or limited partner or other LLC member | Drives box 14 (step 5) |
| H1, H2 | Domestic or foreign; the owner's TIN and name if the partner is a disregarded entity | Never use a disregarded entity's TIN in item E |
| I1, I2 | Entity type; retirement plan box | IRA partners: an EIN is required after 2025 for an IRA receiving UBTI (box 20 code AR) |
| J | Profit, loss and capital percentages, beginning and end; box if a decrease is from a sale or exchange | |
| K1 | Share of liabilities: nonrecourse, qualified nonrecourse financing, recourse, beginning and end | Sum over K-1s equals partnership totals (step 8) |
| K2, K3 | K2: liabilities include lower-tier partnerships. K3: any liability subject to the partner's guarantee or other payment obligation | |
| L | Capital account, **tax basis method only**: beginning, contributed (cash plus tax basis of property), current-year net income (loss), other increase (decrease), withdrawals and distributions, ending | Not required if Schedule B question 4 is "Yes" |
| M | Did the partner contribute property with built-in gain or loss | Attach a statement if "Yes" |
| N | Share of net unrecognized section 704(c) gain or loss, beginning and end | |
| Boxes 1 to 3 | Ordinary business income; net rental real estate; other net rental | |
| 4a, 4b, 4c | Guaranteed payments for services, for capital, total | Step 4 |
| 5 to 10 | Interest; dividends (6a ordinary, 6b qualified, 6c dividend equivalents); royalties; short-term gain; long-term gain (9a, collectibles 9b, unrecaptured section 1250 9c); net section 1231 gain | |
| 11, 12, 13 | Other income (coded); section 179 deduction; other deductions (coded) | Section 179 is limited at partner level |
| 14 | Self-employment earnings: A net earnings, B gross farming or fishing, C gross nonfarm | Step 5 |
| 15 | Credits (coded) | |
| 16 | Schedule K-3 attached | Step 11 |
| 17, 18, 19 | AMT items; tax-exempt income and nondeductible expenses; distributions (additional codes active for 2025) | |
| 20 | Other information: code Z section 199A, code AA section 704(c), code ZZ other (including section 1062 farmland sale information), code AR, code AZ preformation expenditure reimbursement | Step 10 |
| 21 | Foreign taxes paid or accrued | |
| 22, 23 | More than one activity for at-risk purposes; for passive activity purposes | Partner computes per activity |

**Tax basis capital (Item L).** Required since tax year 2020 (Notice 2020-43, then the 2020 instructions). GAAP, section 704(b) book and "other" methods are not allowed on Item L, although the partnership may keep section 704(b) accounts internally. Tax basis capital is not outside basis: outside basis also includes the partner's section 752 share of liabilities and any section 743(b) adjustment, and a contributor's capital and outside basis differ by section 704(c) items. A partnership still showing section 704(b) or GAAP capital and no tax basis roll-forward has not done the 2020 transition (modified outside basis, modified previously taxed capital, or section 704(b) less section 704(c) methods): stop and refer (R-1065-CAPITAL). Negative tax basis capital is shown as a negative figure on Item L; it is not by itself gain, but a distribution above outside basis is gain under section 731(a)(1), so flag it.

### Step 7: allocations, section 704(b) and section 704(c)

1. **Section 704(a) and (b).** The agreement sets distributive shares, but an allocation without substantial economic effect is reallocated by the partner's interest in the partnership.
2. **Economic effect (Treas. Reg. 1.704-1(b)(2)(ii)(b)):** capital accounts kept under Treas. Reg. 1.704-1(b)(2)(iv); liquidating distributions follow positive capital accounts; a partner with a deficit at liquidation must restore it. Without a deficit restoration obligation, the alternate test needs a qualified income offset.
3. **Substantiality (Treas. Reg. 1.704-1(b)(2)(iii)):** the allocation must have a real chance of changing what the partners get apart from tax. Shifting allocations and transitory allocations (offset within five years) are presumed not substantial.
4. **Partner's interest in the partnership:** relative contributions, interests in economic profit and loss, in cash flow, and in liquidation proceeds.
5. **What this skill does:** applies the agreement as written and flags (R-1065-704B) an agreement that liquidates by units rather than capital accounts, a special allocation with no stated business reason, a loss that pushes a partner below zero section 704(b) capital with neither restoration obligation nor qualified income offset, and section 704(b) accounts never kept. It does not redesign allocations.
6. **Section 704(c).** Income, gain, loss and deduction on contributed property must take account of the difference between its tax basis and its value at contribution: built-in gain or loss stays with the contributor. Methods (Treas. Reg. 1.704-3), chosen property by property: traditional (limited by the ceiling rule), traditional with curative allocations, or remedial. Forward section 704(c) arises on contribution; reverse section 704(c) layers arise on a revaluation under Treas. Reg. 1.704-1(b)(2)(iv)(f) (a new partner, a non-pro-rata distribution, a profits-interest grant under Rev. Proc. 93-27). Report Item M, Item N and box 20 code AA. If property came in at a value different from basis and no method is documented, stop and refer (R-1065-704C).

### Step 8: liabilities, section 752

1. An increase in a partner's share of liabilities is a deemed cash contribution (section 752(a)); a decrease is a deemed distribution (section 752(b)) and can trigger gain under section 731.
2. **Recourse:** the partner (or related person) bearing the economic risk of loss, by constructive liquidation (Treas. Reg. 1.752-2), takes 100% of it.
3. **Nonrecourse** (Treas. Reg. 1.752-3): tier 1, share of partnership minimum gain; tier 2, section 704(c) gain on the property securing the debt, to the contributor; tier 3, excess nonrecourse liabilities by the agreement (usually profit shares).
4. **Qualified nonrecourse financing** (section 465(b)(6)): nonrecourse debt from a qualified lender, secured by real property used in the activity of holding real property. It counts as at-risk.
5. **LLCs:** members are not personally liable, so LLC debt is usually nonrecourse for section 752 even if commercially recourse to the LLC, unless a member guarantees it; the guarantor then takes it. A guarantee is a common way to give a partner basis for losses. Tick K3 when any liability is subject to a partner's guarantee.
6. Classify every loan from the documents, allocate, report Item K1, and flag any partner whose outside basis including the section 752 share is too low for the year's allocated loss.

### Step 9: the partner's loss limits (pointers; the partner applies them)

Losses are tested at partner level in this order:

1. **Outside basis, section 704(d).** A loss above year-end outside basis is suspended and carried forward. Basis: contributions (cash and adjusted basis of property), plus the section 752 share, plus allocated income including tax-exempt income, minus distributions, minus allocated losses and nondeductible expenses, adjusted for section 743(b). The partnership does not track outside basis, but supplying a basis worksheet with the K-1s is good practice.
2. **At-risk, section 465 (Form 6198).** Cash and property contributed, recourse debt allocated, and qualified nonrecourse financing. Other nonrecourse debt is not at risk: an LLC member can clear section 704(d) and still be stopped here. Box 22 is checked when there is more than one activity.
3. **Passive activity, section 469 (Form 8582).** A limited partner's interest is presumptively passive (Treas. Reg. 1.469-5T(e)(3)), with three tests that still let a limited partner materially participate. LLC members may use all seven tests in Treas. Reg. 1.469-5T(a) (*Garnett*, 132 T.C. 368 (2009); *Thompson*, 87 Fed. Cl. 728 (2009)). Rentals are passive per se (section 469(c)(2)) except for real estate professionals (section 469(c)(7)) and rentals with average customer use of 7 days or less. Box 23 is checked when there is more than one activity. See `us-real-estate-professional-and-short-term-rentals`.
4. **Excess business loss, section 461(l).** For 2026, net business losses above USD 256,000 (USD 512,000 for joint returns) are disallowed and carried forward as a net operating loss. The partner applies it.

### Step 10: section 199A information, box 20 code Z

The partnership reports, for each trade or business (and each one it holds through another entity): qualified business income items, W-2 wages allocable to it (Notice 2018-64 methods), unadjusted basis of qualified property, whether it is a specified service trade or business, any aggregation, section 199A REIT dividends and PTP income. In the 2025 layout all of this is one statement under **code Z**; code AA is now section 704(c) information, not a section 199A code. Guaranteed payments are not QBI (step 4).

**Aggregation at partnership level** (Treas. Reg. 1.199A-4(b)(1)): the same person or group owns 50% or more of each business, same tax year, none is a specified service business, and two of three integration factors (same or customary products or services, shared facilities or centralized functions, operated in coordination). Once made it binds and must be disclosed every year (Treas. Reg. 1.199A-4(c)(2)). The partner can aggregate further but cannot split what the partnership aggregated. The partner's deduction, the 2026 thresholds and phase-in, and the 2026 minimum deduction are in `us-qbi-deduction`.

### Step 11: Schedules K-2 and K-3

1. **What they are.** Schedule K-2 is the partnership-level summary of international tax items; Schedule K-3 is each partner's share, furnished on the K-1 timetable. Since tax year 2021 they replace free-text foreign reporting on the K-1. A partnership completes only the parts relevant to its items or the requesting partner.
2. **Who must file.** Any partnership with items relevant to partners' US international tax, withholding or reporting: foreign-source income, foreign taxes, foreign entities or branches, foreign partners, and so on.
3. **Domestic filing exception** (2025 instructions). A domestic partnership (not a QDD partnership) need not file K-2 or furnish K-3 if all four hold for the tax year:
   1. *No or limited foreign activity.* No foreign income taxes, no foreign-source income or loss, no interest in a foreign partnership, foreign corporation, foreign branch or foreign disregarded entity; or foreign activity limited to passive category income with not more than USD 300 of creditable foreign tax, shown on a payee statement (a broker or fund 1099).
   2. *Eligible direct partners only.* US citizen or resident alien individuals; domestic decedents' estates, domestic grantor trusts and domestic non-grantor trusts with only US citizen or resident alien individual grantors and beneficiaries; S corporations; single-member LLCs disregarded into one of these; and (broadened for 2025) domestic partnerships whose direct partners are all of these types. No foreign partner, no C corporation partner.
   3. *Notification.* By the time the K-1 is furnished, each partner is told (an attachment to the K-1 is enough) that it will not get a K-3 unless it asks.
   4. *No request by the 1-month date.* No partner asks for K-3 information on or before the date 1 month before the partnership files Form 1065. From 2025 a request covers only that year unless the partner asks for later years specifically.
4. **Small partnership filing exception** (new for 2025). A partnership answering "Yes" to Schedule B question 4 (receipts under USD 250,000, assets under USD 1 million, K-1s filed and furnished on time, no Schedule M-3) is also excepted from K-2 and K-3, with the same partner notification and the same 1-month request rule.
5. **The 1-month date trap.** A request received on or before the 1-month date means the partnership must file K-2 and K-3 for the parts the requesting partner needs and give that partner the filed K-3 on the filing date. A request after the 1-month date does not take away the exception, but the partnership must give that partner a K-3 within 1 month of the request. For 2025 calendar returns on extension, the instructions put the latest 1-month date at 17 August 2026. Ask partners early (November or December).
6. **Default.** Prepare K-2 and K-3 unless the intake confirms every condition of an exception in writing. A two-person domestic LLC holding an international mutual fund that pays more than USD 300 of foreign tax already fails criterion 1. If neither exception applies, the Form 1116 exemption exception in the same instructions may.

### Step 12: Schedules B, B-1, L, M-1, M-2, M-3 and attached forms

- **Schedule B-1** when question 2a or 2b is "Yes": an entity, or an individual or estate, owning 50% or more of profit, loss or capital directly or indirectly.
- **Schedule B, question 4:** "Yes" only if receipts are under USD 250,000, assets under USD 1 million, K-1s are filed and furnished on time, and no Schedule M-3 is required. Then Schedules L, M-1, M-2, page 1 item F and K-1 Item L are not required. Any one condition failing means they are.
- **Schedule M-3** instead of M-1 when year-end assets or adjusted total assets reach USD 10 million, receipts reach USD 35 million, or a reportable entity partner owns 50% or more on any day.

| Form | When | Note |
| --- | --- | --- |
| 4562 | Depreciation, amortization, section 179 | Section 179 passes to partners in box 12; partner-level limit applies |
| 4797 | Sales of business property, recapture | Section 1231 gain to box 10 |
| 8825 | Rental real estate | To Schedule K line 2 and box 2 |
| 8990 | Business interest limit, unless the section 448(c) test is met (2026: USD 32,000,000) | Excess business interest is allocated to partners and tracked by them |
| 6765 | Research credit | Credit through box 15 |
| 8283 | Noncash charitable contributions over USD 500 | |
| 8082 | Paper AAR, or a partner's inconsistent position | Step 13 |
| 8804, 8805, 8813 | Section 1446 withholding for foreign partners with effectively connected income | Refer (R-1065-1446) |
| 8865 | US persons with interests in foreign partnerships | Refer (R-1065-8865) |
| 8918, 8275, 8275-R | Material advisor disclosure; disclosure statements | Reviewer attention |
| 1062 and Schedule A | Partners electing section 1062 instalments on qualified farmland sold to qualified farmers | Partnership supplies information and the covenant under box 20 code ZZ |

### Step 13: the BBA centralized partnership audit regime

1. **Default.** Since tax years beginning after 2017 (Bipartisan Budget Act of 2015, sections 6221 to 6241), an audit is run at partnership level for the reviewed year, and an imputed underpayment, at the highest section 1 or section 11 rate unless modified, is assessed against the partnership in the adjustment year. The adjustment-year partners bear it economically, even if they were not partners in the reviewed year. Terms: reviewed year (the year examined), adjustment year (the year the adjustment becomes final).
2. **Relief inside the regime.** Modification of the imputed underpayment under section 6225(c) (tax-exempt partners, lower rates, amended partner returns). The push-out election under section 6226: within **45 days** of the notice of final partnership adjustment, the partnership furnishes Form 8986 statements to reviewed-year partners and files Form 8985; each takes the adjustment into account in the year the statement is furnished, with interest at the underpayment rate using 5 percentage points instead of 3. Irrevocable once made.
3. **Election out (Schedule B-2, Schedule B question 33 in 2025).** Allowed for a year only if the partnership must furnish 100 or fewer K-1s (counting each shareholder of an S corporation partner), every partner is an individual, C corporation, S corporation, foreign entity that would be a C corporation if domestic, or estate of a deceased partner, the election is on a **timely** return including extensions, every partner's name and TIN is disclosed (and each S corporation partner's shareholders), and partners are notified. **Any one** of these partners blocks it: a partnership, a trust (including a grantor trust), a disregarded entity (including a single-member LLC owned by an eligible individual), an IRA, a nominee holding for another person, an estate of someone other than a deceased partner, or a foreign entity not like a C corporation. Spouses are two partners. The election is annual: it must be made again on each year's return.
4. **Whether to elect out.** Small, stable partnership of a few individuals with no ineligible partner: elect out (audits partner by partner, no representative with sole authority, no partnership-level tax). Partnerships with changing partners: the regime keeps push-out available. Check whether a state pass-through entity tax election depends on the audit regime. Against electing out: separate audits of each partner, no push-out, refunds claimed partner by partner.
5. **Partnership representative (section 6223).** Unless a valid election out is made, the partnership designates on each year's Form 1065 a partner or other person with substantial presence in the US: a US street address, a US TIN, a phone number with a US area code, and availability to meet the IRS in the US. If the representative is an entity, a designated individual meeting the same test is appointed. The representative has **sole authority**; the partnership and every partner are bound by its actions and any final decision. Designations last until a valid resignation, a revocation with a successor named, or an IRS determination; changes use Form 8979 (see its instructions for when it may be filed, including during an examination). Without a designation the IRS may pick anyone. A partnership that elects out does not designate one for that year.
6. **Correcting a filed return.** Inside the regime a partnership cannot file an ordinary amended return: it files an administrative adjustment request (section 6227), electronically on Form 1065 with the box checked, or Form 8082 on paper, and either pays the imputed underpayment or pushes the adjustments out to reviewed-year partners. Partners generally cannot amend their own returns for a K-1 change without it. No AAR once the IRS has mailed a notice of administrative proceeding. A partnership that elected out files an amended Form 1065 and amended K-1s, and partners amend.
7. **Reviewer brief:** in or out of the regime; representative and designated individual details, an internal acceptance of duties, and whether the agreement covers appointment, indemnity and procedure; for corrections, AAR or amended return; for push-out, the 45-day date.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Fixed draw paid whatever the profit | Guaranteed payment: deduct on line 10, box 4a, ordinary income to the partner even in a loss year |
| Percentage of profits, or a priority share of profits | Distributive share, not line 10 |
| Share of profits with a guaranteed minimum | Guaranteed payment only for the shortfall below the minimum (Treas. Reg. 1.707-1(c), Example 2) |
| Interest on capital fixed by rate, payable regardless of profit | Guaranteed payment for capital, box 4b; interest for section 469 |
| Health insurance paid for a partner | Guaranteed payment; the partner may take the self-employed health insurance deduction |
| Syndication fees paid to a partner | Guaranteed payment, but capitalized: box 4b, not deducted |
| Limited partner paid for services | Guaranteed payments for services are self-employment income; distributive share is not, if the partner is a limited partner under section 1402(a)(13) |
| Partner labeled limited who runs the business | Flag (R-1065-SE): Soroban (Tax Court) and Sirius Solutions (5th Cir., 12 August 2026) both look past the label |
| Nonresident alien partner | No self-employment earnings (section 1402(b)) |
| Corporate, trust, estate, exempt or IRA partner | Box 14 left blank |
| Partner with a single-member LLC, or a trust, or another partnership | Election out of BBA not available |
| Foreign individual partner | Still an eligible partner for the election out (an individual); no domestic filing exception |
| S corporation partner | Eligible; its shareholders count toward the 100 |
| Partner who left during 2026 | Gets a K-1 and counts in the section 6698 penalty |
| Return filed after an extension's due date | Penalty runs from the extended due date; Form 7004 filed late gives no extension |
| Investment fund on a broker 1099 with up to USD 300 of foreign tax on passive income | Domestic filing exception still possible if the other three criteria hold |
| Any foreign partner | No domestic filing exception; K-3 for that partner; section 1446 referral |
| Request for K-3 after the 1-month date | Exception kept; that partner's K-3 within 1 month of the request |
| Receipts USD 250,000 or more, or assets USD 1 million or more | Schedules L, M-1, M-2 and Item L required; small partnership K-2/K-3 exception not available |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Whether all four K-2/K-3 exception criteria are met | Prepare Schedules K-2 and K-3 |
| Whether a partner is a disregarded entity, trust or nominee | Do not elect out on Schedule B-2 without written reviewer confirmation; name a partnership representative |
| What a partner labeled limited actually does | Box 14 of guaranteed payments for services only, flagged R-1065-SE for the reviewer |
| Whether a payment to a partner depends on profits | Read the agreement; if it is silent and the amount was paid in a loss year, treat it as a guaranteed payment and flag it |
| Capital account method | Item L on tax basis, always; never GAAP, section 704(b) book or "other" |
| Whether Form 7004 was filed on time | Treat the original due date as the deadline until the acknowledgement is in the file |

### Red flags for the reviewer brief

| Flag | Why |
| --- | --- |
| Limited partner or non-managing member who works full time | Soroban and Sirius Solutions: box 14 may be understated |
| Fixed "draws" booked as distributions | Probably guaranteed payments: line 10, box 4a and self-employment income |
| Operating agreement liquidates by units, not capital accounts | Allocations may fail economic effect (R-1065-704B) |
| Loss allocated past zero section 704(b) capital, no restoration obligation or qualified income offset | Reallocation risk |
| Distribution above a partner's outside basis, or negative tax basis capital | Gain under section 731(a)(1) |
| Member guarantee of LLC debt | Moves the liability to the guarantor (Item K1, K3) and changes at-risk |
| Broker 1099 showing any foreign tax | Check the USD 300 limit and the domestic filing exception |
| Single-member LLC, trust or partnership among the partners | No Schedule B-2 election out |

### Two more fact patterns (not recomputed)

**Foreign partner.** A Delaware LLP has a US C corporation partner (40%, active), a French resident individual (30%, passive investor) and a US resident alien individual (30%, managing). Two foreign customers pay it with no foreign tax withheld, and a brokerage fund pays foreign dividends with foreign tax withheld. Outcome: the election out is available (section 6221(b)(1)(C) lists "an individual" with no residence condition, so a foreign individual, a C corporation and a resident alien are all eligible, and there are only three K-1s), if the other step 13 conditions are met; if the partnership stays in the regime, the C corporation can be representative with a US designated individual. There is no domestic filing exception (a foreign partner and foreign-source income both fail it), so K-2 and K-3 are prepared: Part II and III for the foreign tax credit inputs, Part X for the foreign partner's effectively connected income. The French partner has box 14 of zero (nonresident alien, section 1402(b)); the corporation has no box 14; the resident alien manager has box 14 code A of his full share. Section 1446 withholding on the foreign partner's share of effectively connected income is referred (R-1065-1446), and her Form W-8BEN must be in the file. The corporate partner's foreign tax credit is figured on its own return under section 901 (section 902 deemed-paid credit was repealed for years after 2017).

**Family limited partnership with contributed property.** A Texas FLP: general partner is a single-member LLC owned by the founder (1%); limited partners are the founder (49%) and two adult children (25% each). In 2020 the founder contributed a rental building worth USD 1,000,000 with a tax basis of USD 200,000 (USD 800,000 of built-in gain), subject to a USD 400,000 bank mortgage. The building is sold in 2026. Outcome: the remaining section 704(c) built-in gain goes to the founder under the documented method (Item M "Yes", Item N closes to zero, box 20 code AA); the mortgage and other bank loans are qualified nonrecourse financing, shared by the three tiers with tier 2 to the founder; box 14 is zero for everyone because rentals, section 1231 gain and interest are excluded under section 1402(a)(1) to (3), so the label of the founder's interest does not matter unless the FLP also runs a services business; the children are passive; the founder's real estate professional status is checked at his level; no election out (the single-member LLC general partner is a disregarded entity); the domestic filing exception is likely met if notices are sent; Schedule L is required (assets over USD 1 million).

## Worked cases

**Case 1, a decision: fixed payment or profit priority for the working member?** Two-member LLC, both US citizens. B manages full time; A is an investor with no role in running the business (a limited partner under section 1402(a)(13) on any of the tests in step 5). They want B to receive USD 90,000 a year for her work before the rest is split 50/50. Option 1: a fixed USD 90,000 regardless of profits (a guaranteed payment). Option 2: 30% of partnership income before any payment, then 50/50. Test a normal year (income before the payment USD 300,000) and a bad year (USD 60,000).

Normal year. Option 1: line 23 income is USD 210,000, box 1 USD 105,000 each; B also has box 4a USD 90,000, total USD 195,000. Option 2: B's box 1 is 30% x 300,000 = USD 90,000 plus half of USD 210,000 = USD 195,000; A's box 1 USD 105,000. B's total and B's self-employment earnings (USD 195,000, as a member-manager) are the same, but her **qualified business income** is USD 105,000 under option 1 and USD 195,000 under option 2: USD 90,000 more QBI, because guaranteed payments are not QBI.

Bad year. Option 1: ordinary loss of USD 30,000, USD 15,000 each; B still reports USD 90,000 guaranteed payment, net USD 75,000; A reports a USD 15,000 loss (subject to his loss limits). Option 2: B 30% x 60,000 = USD 18,000 plus half of USD 42,000 = USD 39,000; A USD 21,000. The guaranteed payment protects B and shifts the downside to A.

Advise: if the partners want B paid whatever the result, option 1 (guaranteed payment) is the honest description and must be reported that way. If B can bear profit risk, option 2 gives B more QBI in a good year (her deduction is then figured in `us-qbi-deduction`, subject to the 2026 thresholds and the specified service rules there). Either way the agreement, not the label on the bank transfer, decides: the test is whether the amount is fixed without regard to partnership income. Self-employment earnings do not change for B; they would change only for a partner who is a limited partner, since a guaranteed payment for services is self-employment income even for that partner.

```oa-check
name: Guaranteed payment against profit priority, normal and bad year (2026)
inputs:
  income_good: 300000
  income_bad: 60000
  payment: 90000
  priority: 0.30
  share: 0.5
steps:
  - gp_box1_each_good: (income_good - payment) * share
  - gp_b_total_good: payment + gp_box1_each_good
  - gp_b_qbi_good: gp_box1_each_good
  - alloc_b_good: income_good * priority + (income_good - income_good * priority) * share
  - alloc_b_qbi_good: alloc_b_good
  - qbi_difference: alloc_b_qbi_good - gp_b_qbi_good
  - gp_box1_each_bad: (income_bad - payment) * share
  - gp_b_total_bad: payment + gp_box1_each_bad
  - alloc_b_bad: income_bad * priority + (income_bad - income_bad * priority) * share
  - alloc_a_bad: (income_bad - income_bad * priority) * share
expected:
  gp_box1_each_good: 105000.00
  gp_b_total_good: 195000.00
  alloc_b_good: 195000.00
  qbi_difference: 90000.00
  gp_box1_each_bad: -15000.00
  gp_b_total_bad: 75000.00
  alloc_b_bad: 39000.00
  alloc_a_bad: 21000.00
```

**Case 2, late-filing penalty with a partner who left.** A calendar-year LLC had three members at 31 December 2026; a fourth member sold out in June 2026. No Form 7004 was filed. The return is filed on 2 June 2027.

Persons who were partners during any part of 2026: 4. Months or parts of months from 15 March 2027 to 2 June 2027: 3 (to 15 April, to 15 May, and part of the third). Penalty: 4 x USD 260 x 3 = USD 3,120. Filed 14 months late, the 12-month cap gives 4 x USD 260 x 12 = USD 12,480. Had Form 7004 been filed on time and the return filed on 1 October 2027, one part-month after 15 September: 4 x USD 260 x 1 = USD 1,040. Before paying, check relief (Filing and payment): the partnership may qualify for First Time Abate or the new automatic exemption if its prior three years were filed on time.

```oa-check
name: Section 6698 penalty, four partners (returns due in 2027)
inputs:
  partners: 4
  rate: 260
  months_late: 3
  months_very_late: 14
  months_after_extension: 1
steps:
  - penalty: partners * rate * min(months_late, 12)
  - penalty_capped: partners * rate * min(months_very_late, 12)
  - penalty_extended: partners * rate * min(months_after_extension, 12)
expected:
  penalty: 3120.00
  penalty_capped: 12480.00
  penalty_extended: 1040.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-1065-CORP | LLC elected corporate or S corporation status | Wrong return: Form 1120 or 1120-S |
| R-1065-SMLLC | Single member, no election | Disregarded: Schedule C, E or F |
| R-1065-PTP | Publicly traded partnership (section 7704; section 1446(f) on transfers) | Refer to a specialist |
| R-1065-TIER | An upper-tier partnership is a partner and the audit-regime position needs handling beyond the default | Refer; the election out is not available |
| R-1065-743 | Section 754 election, section 734 or 743 basis adjustments, reverse section 704(c) layers, disguised sales | Flag and refer to a partnership tax specialist; identify, do not compute |
| R-1065-707A | Possible disguised payment for services or disguised sale (section 707(a)(2)) | Flag for reviewer |
| R-1065-1061 | Carried interest, section 1061 holding-period recharacterization | Refer |
| R-1065-1446 | Foreign partner with effectively connected income (section 1446, Forms 8804, 8805, 8813) | Refer; do not finalize without the withholding work |
| R-1065-8865 | US partner with a reportable interest in a foreign partnership | Flag; Form 8865 out of scope |
| R-1065-PUSH | Preparing a section 6226 push-out statement or a full AAR imputed underpayment computation | Concepts covered here; mechanics refer |
| R-1065-PTET | State pass-through entity tax election | `us-pte-state-matrix` and the state skill |
| R-1065-SE | Partner labeled limited who manages or works substantially in the business | Reviewer decides box 14 and documents the position |
| R-1065-704B | Allocations that may lack substantial economic effect, or no section 704(b) capital accounts kept | Reviewer and partnership counsel |
| R-1065-704C | Contributed property with no documented section 704(c) method | Stop and refer |
| R-1065-CAPITAL | No tax basis capital roll-forward | Stop and refer |
| R-1065-BBA | A partner might be a disregarded entity, trust or nominee and the client wants to elect out | Do not attach Schedule B-2 without written reviewer confirmation |

## Filing and payment

- **Due:** calendar 2026 return, Schedules K-1 and any K-2 and K-3, **15 March 2027**; with Form 7004 filed by then, **15 September 2027**. Furnish K-1s (and any K-3s) to partners by the same date. A section 444 fiscal-year partnership makes any section 7519 required payment; otherwise no tax is paid with the return.
- **E-filing:** required for a partnership with more than 100 partners; under Treas. Reg. 301.6011-3 (T.D. 9972) partnerships filing 10 or more returns of any type in the year must also e-file unless a hardship waiver is granted.
- **Late or incomplete return, section 6698:** USD 260 per person who was a partner at any time in the year, per month or part of a month, up to 12 months, unless the failure is due to reasonable cause. It applies with no tax due and is assessed against the partnership without deficiency procedures. Do not attach a reasonable-cause statement to the return; answer the penalty notice.
- **Relief:**
  - *First Time Abate* covers partnership returns under section 6698(a)(1) when the same return was filed on time for the prior three years with no penalties (or penalties abated for reasonable cause or IRS error). Ask by phone or on Form 843.
  - *Automatic Exemption from Penalty* begins in summer 2026 for Form 1065, starting with 2025 tax-year returns: with three prior years of timely compliance the IRS does not assess the failure-to-file penalty and sends a letter saying so.
  - *Reasonable cause* (illness, destroyed records, reliance on an adviser): document it. Rev. Proc. 84-35 relief for small partnerships was written for the pre-BBA rules; do not rely on it without confirming the IRS still applies it.
- **K-1 penalties:** failing to furnish a correct K-1, section 6722, USD 340 per statement required to be furnished in 2027 (USD 60 if corrected within 30 days); the same amounts apply to filing them with the IRS under section 6721. A timely Form 1065 does not protect against late K-1s: send K-1s the day the return is filed.
- **Other:** section 6707A for undisclosed listed transactions; section 6662 disclosure on Form 8275 where needed.

## Completion checklist

- Classification confirmed (no Form 8832 or 2553; more than one owner; not a qualified joint venture or Rev. Proc. 2002-69 case).
- Every person who was a partner at any time in 2026 has a K-1; count recorded for the penalty.
- Each payment to a partner classed as guaranteed payment or distributive share against the agreement; line 10 and boxes 4a to 4c agree.
- Item G and box 14 decided per partner, with any R-1065-SE position documented.
- Sum of K-1s equals Schedule K, line by line.
- Item L on tax basis; Item K1 equals the partnership's liabilities; K3 ticked for guaranteed debt; Items M and N complete.
- Box 20 code Z statement for each business; code AA if section 704(c) applies.
- K-2/K-3 exception tested against all four criteria (or the small partnership test), partner notices sent, request log kept.
- Schedule B question 4 answered on all four conditions; Schedules L, M-1, M-2 or M-3 as required.
- Schedule B-2 made only if every partner is eligible, on a timely return; otherwise representative and designated individual named.
- Return and Form 7004 dates calendared; e-file acknowledgement kept.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.55 (USD 260 for section 6698(b)(1), returns required to be filed in 2027), section 4.56 (section 6699), sections 4.57 and 4.58 (sections 6721 and 6722 per-return amounts USD 340 and USD 60), the 2026 section 448(c) test (USD 32,000,000) and section 461(l) thresholds (USD 256,000, USD 512,000). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Instructions for Form 1065 (2025), dated 14 January 2026, the current edition. Read for When To File (15th day of the 3rd month), Extension of Time To File, Penalties (USD 255 for 2025 returns, 12-month cap, partner count), Electronic Filing (more than 100 partners), Item J and Schedule M-3 triggers, line 10 and Schedule K line 4 guaranteed payments, the self-employment worksheet and limited partner text, the section 199A exclusion of guaranteed payments, Schedule B question 33 election out and the partnership representative rules, and What's New (codes ZZ, AR, AZ, line 19). | https://www.irs.gov/pub/irs-pdf/i1065.pdf | 2026-11-13 |
| Schedule K-1 (Form 1065) 2025. Read for the item and box layout (G to N, K1 to K3, boxes 1 to 23). | https://www.irs.gov/pub/irs-pdf/f1065sk1.pdf | 2026-11-13 |
| Partner's Instructions for Schedule K-1 (Form 1065) (2025). Read for box 20 code Z (section 199A) and code AA (section 704(c)) and code ZZ. | https://www.irs.gov/pub/irs-pdf/i1065sk1.pdf | 2026-11-13 |
| Form 1065 (2025). Read to confirm that the posted form is still the 2025 edition. | https://www.irs.gov/pub/irs-pdf/f1065.pdf | 2026-11-13 |
| Partnership Instructions for Schedules K-2 and K-3 (Form 1065) (2025). Read for the domestic filing exception (four criteria, USD 300, broadened criterion 2, annual requests), the 1-month date and examples, and the new small partnership filing exception (USD 250,000, USD 1 million). | https://www.irs.gov/pub/irs-pdf/i1065s23.pdf | 2026-11-13 |
| Instructions for Form 7004 (Rev. December 2025). Read for the 6-month automatic extension. | https://www.irs.gov/pub/irs-pdf/i7004.pdf | 2026-11-13 |
| 26 U.S.C. 6698 (govinfo). Read for (a) the 12-month cap and reasonable cause, (b) USD 195 times partners during any part of the year, (c) and (d) assessment, (e) indexing and rounding. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6698.htm | 2026-11-13 |
| 26 U.S.C. 707 (govinfo). Read for (c), guaranteed payments determined without regard to partnership income. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapK-partI-sec707.htm | 2026-11-13 |
| 26 U.S.C. 704 (govinfo). Read for (a) to (d), allocations, contributed property and the basis limit on losses. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapK-partI-sec704.htm | 2026-11-13 |
| 26 U.S.C. 1402 (govinfo). Read for (a)(1) to (3) exclusions, (a)(13) limited partners, and (b) nonresident aliens. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm | 2026-11-13 |
| 26 U.S.C. 6221 (govinfo). Read for (b), the election out: 100 or fewer statements, eligible partners, timely return, disclosure, notice, S corporation shareholders. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapC-partI-sec6221.htm | 2026-11-13 |
| 26 U.S.C. 6223 (govinfo). Read for (a) designation, substantial presence and sole authority, and (b) binding effect. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapC-partI-sec6223.htm | 2026-11-13 |
| 26 U.S.C. 6226 (govinfo). Read for (a) the 45-day push-out election and (c)(2) interest with 5 points for 3. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap63-subchapC-partII-sec6226.htm | 2026-11-13 |
| Treas. Reg. 1.707-1 (eCFR). Read for (c), Examples 1 to 3 on guaranteed payments, minimums and loss years. | https://www.ecfr.gov/current/title-26/section-1.707-1 | 2026-11-13 |
| Sirius Solutions, L.L.L.P. v. Commissioner, No. 24-60240 (5th Cir.), substituted opinion on rehearing filed 12 August 2026 (govinfo). Read for the withdrawal of 165 F.4th 374, the holding on "limited partner" in section 1402(a)(13), and the vacatur and remand; also for its citation of Soroban, 161 T.C. 310 (2023). | https://www.govinfo.gov/content/pkg/USCOURTS-ca5-24-60240/pdf/USCOURTS-ca5-24-60240-0.pdf | 2026-11-13 |
| IRS, Penalty relief due to First Time Abate or other administrative waiver. Read for section 6698(a)(1) eligibility and the Automatic Exemption from Penalty for Form 1065 from summer 2026. | https://www.irs.gov/payments/penalty-relief-due-to-first-time-abate-or-other-administrative-waiver | 2026-11-13 |

Not yet confirmed: the 2026 Form 1065, Schedule K-1 and their instructions, and the 2026 Schedules K-2 and K-3 instructions, were not published when read, so form line and box numbers, Schedule B question numbers, and the latest 1-month date for 2026 returns on extension (the 2025 instructions gave 17 August 2026) are taken from the 2025 editions and must be checked against the 2026 releases. Rev. Proc. 2025-32 sections 4.57 and 4.58 print "August 1, 2026" for the middle correction tier of statements due in 2027, which looks like a misprint; the USD 130 middle tier is therefore left out. Whether the IRS still applies Rev. Proc. 84-35 after the BBA rules was not checked on an official page. The Treasury regulations cited by number other than Treas. Reg. 1.707-1 (sections 1.704-1 to 1.704-3, 1.752-1 to 1.752-3, 1.469-5T, 1.199A-4, 301.6221(b)-1, 301.6011-3, 301.7701-3, 1.761-1 and 1.761-2, 1.6031(a)-1) were carried from the earlier version and not reopened on 2026-11-13. Further proceedings on remand in Sirius Solutions, and any appeal from the Tax Court's Soroban decision, were not checked.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-form-1065-partnership` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-form-1065-partnership. If neither is available, confirm every figure against the official source pages cited above before relying on it.
