---
name: us-charitable-giving-strategies
description: Plan and compute a US individual's 2026 federal charitable deduction after the One Big Beautiful Bill Act (Public Law 119-21) - the new non-itemizer deduction of $1,000 ($2,000 joint) for cash gifts, the 0.5% floor for itemizers, the 2/37 itemized deduction reduction that caps the value of a deduction at 35% for top-bracket donors, the section 170 percentage limits, bunching against the standard deduction, donor-advised funds, gifts of appreciated stock, qualified charitable distributions from IRAs ($111,000 for 2026), carryovers and substantiation. Trigger on "charitable deduction", "donor-advised fund", "bunching", "QCD", "donate stock", "0.5% floor", "non-itemizer charity". Federal only.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: decision
---

# Charitable giving for individuals, tax year 2026: the new floor, the non-itemizer deduction, bunching, donor-advised funds, stock and IRA gifts

> **Source-cited draft.** Built from Public Law 119-21 sections 70111, 70424 and 70425, 26 U.S.C. 63, 170, 408 and 4966, Treas. Reg. 1.170A-10, Rev. Proc. 2025-32, Notice 2025-67 and IRS Pubs. 526, 544, 561 and 590-B, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Three rules are new for 2026, all from Public Law 119-21 and all for taxable years beginning after 31 December 2025. (1) A person who does **not** itemize may deduct cash gifts to public charities up to **USD 1,000 (USD 2,000 joint)**, on top of the standard deduction; gifts to a donor-advised fund or a supporting organization do not count. (2) A person who itemizes loses the first **0.5%** of the contribution base (about AGI) each year: only gifts above that floor are deductible. (3) A person whose income reaches the start of the 37% bracket has itemized deductions cut by **2/37**, which limits the tax value of each deducted dollar to **35 cents** instead of 37. The 60% limit for cash gifts to public charities is now permanent. Bunching two or more years of gifts into one year, often through a donor-advised fund, beats the floor and the standard deduction; giving long-term appreciated stock avoids the gain; a person aged 70½ or older can give up to **USD 111,000** straight from an IRA, outside income.

## Scope and who this is for

In scope: an individual (and the adviser) who gives to charity in 2026 and wants the largest federal income tax benefit from it: a high earner, a retiree with an IRA, or someone holding shares that have risen in value. It covers the choice between itemizing and the non-itemizer deduction, the section 170 limits, the 0.5% floor, the 2/37 reduction, bunching, donor-advised funds, appreciated stock, qualified charitable distributions, carryovers and the paperwork.

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| Every 2026 federal change in one list | `us-2026-federal-tax-changes` |
| Gift tax and estate planning for large gifts | `us-estate-gift-706-709` |
| Holding periods, basis and capital gains rates | `us-capital-gains` |
| SEP and SIMPLE IRAs, required minimum distributions | `us-self-employed-retirement` |
| The state and local tax cap and other itemized deductions | `us-form-1040-individual-return` |
| Gifts by corporations (the 1% floor and 10% cap), trusts or estates | `us-form-1120-c-corp`, `us-form-1041-trust-and-estate-income` |
| Charitable remainder and lead trusts, gift annuities, conservation easements, private foundation management | refer |
| State income tax treatment | the state's own rules |

## Ask the client first

1. **Will you itemize for 2026, and how far above or below the standard deduction are your other itemized deductions?** This decides between bunching, the non-itemizer deduction or giving as usual.
2. **Expected 2026 AGI, and will taxable income plus itemized deductions pass the start of the 37% bracket?** This sets the 0.5% floor, the percentage limits and whether the 2/37 reduction applies.
3. **What will you give (cash, listed shares, other property) and to whom** (a public charity, a donor-advised fund, a private foundation, a supporting organization)? Each pairing has its own limit and paperwork.
4. **For shares:** when were they acquired, what is the basis, are they publicly traded?
5. **Are you (or your spouse) aged 70½ or older with a traditional IRA, and is there a 2026 required minimum distribution?** This opens the qualified charitable distribution.
6. **Charitable carryovers from 2021 to 2025**, which use up room under the 2026 limits.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Non-itemizer deduction for cash gifts to public charities, single and other returns | USD 1,000 | [Public Law 119-21, section 70424](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Non-itemizer deduction, joint return | USD 2,000 | [Public Law 119-21, section 70424](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Floor for individuals who itemize (share of contribution base lost each year) | 0.5 percent | [Public Law 119-21, section 70425](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Cash gifts to public charities, limit (made permanent) | 60 percent | [Public Law 119-21, section 70425(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Itemized deduction reduction for the 37% bracket (new section 68) | 2/37 | [Public Law 119-21, section 70111](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Start of the 37% bracket, married filing jointly and surviving spouses | USD 768,700 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Start of the 37% bracket, single and head of household | USD 640,600 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Start of the 37% bracket, married filing separately | USD 384,350 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, married filing jointly and surviving spouses | USD 32,200 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, head of household | USD 24,150 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, single and married filing separately | USD 16,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Gifts to public charities (section 170(b)(1)(A)), general limit | 50 percent | [26 U.S.C. 170(b)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Gifts to other organizations such as most private foundations (lesser of this or the room left under 50 percent) | 30 percent | [26 U.S.C. 170(b)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Long-term capital gain property to a public charity | 30 percent | [26 U.S.C. 170(b)(1)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Long-term capital gain property to other organizations (lesser of this or the room left under 30 percent) | 20 percent | [26 U.S.C. 170(b)(1)(D)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Carryover period for gifts above a percentage limit | 5 years | [26 U.S.C. 170(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Contemporaneous written acknowledgment for any single contribution of | USD 250 or more | [26 U.S.C. 170(f)(8)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Property: description with the return when the deduction claimed is more than | USD 500 | [26 U.S.C. 170(f)(11)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Property: qualified appraisal when the deduction claimed is more than (not for publicly traded securities) | USD 5,000 | [26 U.S.C. 170(f)(11)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm) |
| Qualified charitable distributions excluded from income, per taxpayer | USD 111,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Charitable standard mileage rate (fixed by section 170(i)) | 14 cents | [Notice 2026-10](https://www.irs.gov/pub/irs-drop/n-26-10.pdf) |

The 35% figure is arithmetic, not a number printed in the Act: a deduction cut by 2/37 is worth 37% x (1 minus 2/37) = 35% of each dollar deducted. Only the 2/37 fraction is law.

### Steps

1. **Itemize or not.** Compare itemized deductions (charity after the floor in step 4, plus state and local taxes, mortgage interest and the rest) with the 2026 standard deduction.
2. **Not itemizing:** apply the non-itemizer deduction (section 170(p) as amended by section 70424) and stop. Only cash gifts to an organization described in section 170(b)(1)(A) count, not gifts to a section 509(a)(3) supporting organization and not gifts "for the establishment of a new, or maintenance of an existing, donor advised fund". Property never counts. It is taken on top of the standard deduction (section 63(b)(4)). It is computed without the 0.5% floor and without carryovers (section 170(p) is applied "without regard to subsections (b)(1)(G)(ii), (b)(1)(I), and (d)(1)"). The Act removed the old "beginning in 2021" limit, so it has no end date.
3. **Itemizing:** sort each gift by what was given (cash, long-term appreciated property, other property) and to whom (a public charity or another organization). Apply the percentage limits to the contribution base, which is AGI computed without any net operating loss carryback (section 170(b)(1)(H)).
4. **Apply the 0.5% floor** (section 170(b)(1)(I), added by section 70425): the deduction is allowed "only to the extent that the aggregate of such contributions exceeds 0.5 percent of the taxpayer's contribution base". It is a floor, not a cliff. It is taken from the gift categories in the order the Act sets: first (D) (capital gain property to non-public charities), then (C), then (B), then (E), then (A), and last (G) (cash to public charities). The amount lost to the floor carries forward only from a year in which a percentage limit is also exceeded (section 170(d)(1)(C)); in any other year it is lost for good.
5. **Apply the 2/37 reduction** (new section 68, section 70111) if taxable income plus itemized deductions passes the start of the 37% bracket: reduce total itemized deductions by 2/37 of the lesser of (a) the itemized deductions and (b) taxable income, increased by the itemized deductions, above the start of the 37% bracket. It is applied after every other limit.
6. **Carry forward** any excess over a percentage limit for up to 5 years.
7. **Age 70½ or older with a traditional IRA:** test a qualified charitable distribution before writing a cheque.
8. **Collect the paperwork before filing:** the charity's written acknowledgment, the bank record, Form 8283 for property and a qualified appraisal where needed.

## Boundary and exception table

### What changed for 2026, and what did not

| Change | Rule |
| --- | --- |
| Non-itemizer deduction (section 70424, section 170(p)) | New for 2026; for 2025 it did not exist. Cash to public charities only; no donor-advised funds, no supporting organizations, no property; no floor, no carryover |
| 0.5% floor for itemizers (section 70425, section 170(b)(1)(I)) | New for 2026; floor order (D), (C), (B), (E), (A), (G); lost amount carries forward only from a year a percentage limit is exceeded |
| 60% cash limit (section 70425(b)) | Made permanent; the Act also reworded the coordination clause in section 170(b)(1)(B) |
| 2/37 reduction (section 70111, section 68) | New for 2026; only where taxable income plus itemized deductions reaches the start of the 37% bracket |
| Gift timing | A gift is deducted in the year it is paid (section 170(a)(1)); a 2026 gift cannot be moved back into 2025 |
| Percentage limits (50, 30, 20 percent) and substantiation amounts | Unchanged |

Who is a public charity for these limits: churches, schools, hospitals, publicly supported charities and the other organizations listed in section 170(b)(1)(A). A donor-advised fund's sponsoring organization is never a private foundation (section 4966(d)(1)).

### Bunching gifts into one year

The standard deduction is fixed; itemized deductions help only above it, and from 2026 the floor takes a slice off each year's gifts. Giving two or more years of gifts in one year, then taking the standard deduction in the others, can raise the total deduction over the period. A donor-advised fund lets the person deduct the bunched amount now and choose the charities later. Bunching does not help a person who would itemize every year with a wide margin, or one who would take the standard deduction even in the bunched year. In a non-itemizing year, cash gifts made directly to a public charity (not to a donor-advised fund) can still use the non-itemizer deduction. A person with a carryover should use it in the bunched year (see carryovers below).

### Donor-advised funds

A donor-advised fund is a fund or account separately identified by reference to a donor's contributions, "owned and controlled by a sponsoring organization", over which the donor (or an appointee) has or expects advisory privileges (section 4966(d)(2)).

- **Timing.** The deduction is for the year the donor pays into the fund (section 170(a)(1)). The sponsor owns the money from then on; its later grants are its own distributions.
- **Conditions.** No deduction unless the sponsor is not a war veterans' organization, a fraternal society or a nonprofit cemetery company (Pub. 526), and not a type III supporting organization that is not functionally integrated, and the donor gets a contemporaneous written acknowledgment that the sponsor "has exclusive legal control over the assets contributed" (section 170(f)(18)).
- **Not for non-itemizers.** Cash paid to a donor-advised fund never counts for the section 170(p) deduction.
- **Not for IRA distributions.** A qualified charitable distribution cannot go to a donor-advised fund (section 408(d)(8)(B)(i)).

### Giving appreciated long-term stock

Capital gain property is a capital asset that would have produced long-term capital gain if sold at fair market value at the time of the gift (section 170(b)(1)(C)(iv)).

- **Amount.** Section 170(e)(1)(A) reduces a gift of property only by the gain that would not have been long-term. For long-term shares given to a public charity the reduction is nil, so the deduction is generally fair market value on the date of the gift (Pub. 526: "you can generally use the FMV of the property"). It is cut to basis for gifts to certain private nonoperating foundations (other than qualified appreciated stock) and the other cases in section 170(e)(1)(B).
- **The gain.** Giving the shares outright is not a sale or exchange: "A sale is a transfer of property for money or a mortgage", note or other promise to pay money (Pub. 544). Only a bargain sale to a charity is "partly a charitable contribution and partly a sale or exchange" (Pub. 526). Selling first and giving the cash means the gain is reported.
- **Limits.** 30% of the contribution base for public charities, counted after the other gifts; for most private foundations the lesser of 20% and the room left under 30% (section 170(b)(1)(D)). The donor may elect the 50% limit instead, but only by reducing every capital gain gift that year to the amount section 170(e)(1) leaves, usually basis (section 170(b)(1)(C)(iii)).
- **Shares held one year or less** are ordinary income property: the deduction is fair market value minus the short-term gain, which "Generally ... limits the deduction to your basis" (Pub. 526).
- **Timing.** A properly endorsed certificate is delivered on the date of mailing or delivery to the charity or its agent. If given to the donor's own agent or the issuer for transfer, the gift "isn't delivered until the date the stock is transferred on the books of the corporation" (Pub. 526). Ask the broker for the transfer date before relying on a late-December gift.
- **Paperwork.** Form 8283 Section A when noncash gifts for the year are deducted at more than USD 500 in total (Section A is also used for publicly traded securities). Publicly traded securities need no qualified appraisal even above USD 5,000 (section 170(f)(11)(A)(ii)(I)).

### Qualified charitable distributions from an IRA

A distribution from an IRA, other than an ongoing SEP or SIMPLE IRA (section 408(k) or (p)), that (section 408(d)(8)):

- is made directly by the trustee to a section 170(b)(1)(A) organization, not to a supporting organization and not to a donor-advised fund;
- is made on or after the date the owner reaches age 70½; and
- would be fully deductible under section 170 ignoring the percentage limits, with the same written acknowledgment a deductible gift needs (Pub. 590-B).

It is left out of income up to USD 111,000 for 2026, per taxpayer: on a joint return each qualifying spouse has a separate limit. Anything above is taxed like any other distribution. The excluded amount is not also deductible (section 408(d)(8)(E)). The exclusion is reduced by deductible IRA contributions for years ending on or after age 70½, to the extent not already used. Only the otherwise-taxable part can qualify. "A QCD will count towards your required minimum distribution" (Pub. 590-B). Because the amount never enters income, it helps a person who takes the standard deduction and avoids the 0.5% floor and the 2/37 reduction. The limit is indexed from 2024 (section 408(d)(8)(G)).

### Carrying excess gifts forward

Gifts to public charities above the year's limit are treated as paid in each of the 5 succeeding years, in order of time, to the extent of room under the limit in each later year (section 170(d)(1)(A)); the 30% and 20% categories carry forward the same way (sections 170(b)(1)(B), (C)(ii) and (D)(ii)). From 2026 the amount lost to the 0.5% floor joins the carryover only for a year in which a percentage limit is exceeded (section 170(d)(1)(C)). The non-itemizer deduction ignores carryovers. A standard deduction year still uses up carryover: the regulation treats it as "paid (but not allowable as a deduction)" in that year (Treas. Reg. 1.170A-10).

### Proof the gift was made

| Gift | What is needed |
| --- | --- |
| Any cash gift, any size | A bank record or a written communication from the charity with its name, the date and the amount (section 170(f)(17)) |
| Single contribution of USD 250 or more | Contemporaneous written acknowledgment: cash amount, description (not value) of any property, and whether anything was given in return with a good faith estimate of its value (section 170(f)(8)); obtained by the earlier of the filing date and the due date including extensions |
| Noncash gifts deducted at more than USD 500 in total | Form 8283 with the return; Section A for items of USD 5,000 or less and for publicly traded securities of any amount (Pub. 526) |
| Property deducted at more than USD 5,000 (not publicly traded securities) | Qualified appraisal by a qualified appraiser and Form 8283 Section B signed by the charity (Pub. 526; valuation in Pub. 561) |
| Donor-advised fund | The sponsor's acknowledgment of exclusive legal control (section 170(f)(18)) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether the client itemizes | Compute both ways; never assume |
| Type of recipient | Treat as a non-public charity (the lower limits) until the charity's status is confirmed |
| Holding period of shares | Treat as short-term (basis only) until dates are confirmed |
| Carryovers | Zero; ask for the 2021 to 2025 returns |
| Acknowledgment for a USD 250 gift | No deduction until it is in hand |

### Red flags to raise

| Flag | Why it matters |
| --- | --- |
| Non-itemizer counting a donor-advised fund gift | Not allowed under section 170(p) |
| QCD sent to a donor-advised fund or before age 70½ | Not a QCD; taxable distribution |
| Property other than listed shares over USD 5,000 with no appraisal | Deduction lost |
| Late-December stock gift through the donor's broker | May fall into 2027 |
| Income near the 37% bracket | 2/37 reduction; consider a QCD or bunching |

## Worked cases

**Case 1, a decision: bunch two years of gifts into 2026?** A married couple files jointly. Assumed for both 2026 and 2027: contribution base USD 300,000, other itemized deductions USD 18,000, usual giving USD 20,000 a year in cash to public charities, and the 2026 standard deduction of USD 32,200 also used for 2027 (the 2027 amount will be indexed and differ). The floor is 0.5% of USD 300,000, USD 1,500, each year it applies. Plan A, give each year: itemized USD 18,000 + (USD 20,000 minus USD 1,500) = USD 36,500 each year, more than USD 32,200, so itemize both years: USD 73,000 over two years. Plan B, give USD 40,000 to a donor-advised fund in 2026 and nothing in 2027: 2026 itemized USD 18,000 + (USD 40,000 minus USD 1,500) = USD 56,500, then the standard deduction of USD 32,200 in 2027: USD 88,700. Bunching gives USD 15,700 more deductions. The floor is charged once instead of twice and the 2027 standard deduction is not wasted. The cash is well inside the 60% limit, and income is far below the 37% bracket, so the 2/37 reduction does not apply. Recommend Plan B.

```oa-check
name: Bunching decision, married filing jointly (2026)
inputs:
  contribution_base: 300000
  other_itemized: 18000
  yearly_gifts: 20000
  standard_deduction: 32200
steps:
  - floor: contribution_base * 0.005
  - plan_a_year: max(other_itemized + yearly_gifts - floor, standard_deduction)
  - plan_a_total: plan_a_year * 2
  - plan_b_2026: max(other_itemized + 2 * yearly_gifts - floor, standard_deduction)
  - plan_b_total: plan_b_2026 + standard_deduction
  - extra_from_bunching: plan_b_total - plan_a_total
expected:
  floor: 1500
  plan_a_year: 36500
  plan_a_total: 73000
  plan_b_2026: 56500
  plan_b_total: 88700
  extra_from_bunching: 15700
```

**Case 2, a top-bracket donor: the floor and the 2/37 reduction together.** A married couple files jointly with a contribution base (AGI) of USD 1,200,000. They give USD 100,000 in cash to public charities and have USD 30,000 of other itemized deductions (state and local tax at the USD 10,000 phase-down floor plus USD 20,000 of mortgage interest). The floor is 0.5% x USD 1,200,000 = USD 6,000, so USD 94,000 of the gift is allowed and itemized deductions are USD 124,000. Taxable income plus itemized deductions is USD 1,200,000, which is USD 431,300 above the USD 768,700 start of the 37% bracket. The reduction is 2/37 of the lesser of USD 124,000 and USD 431,300: USD 6,702.70. Itemized deductions after section 68: USD 117,297.30. The gift itself is deducted at USD 94,000 x 35/37 = USD 88,918.92, worth USD 32,900 at 37%, so the USD 100,000 gift saves 32.9% instead of 37%. A qualified charitable distribution (if either spouse is 70½ or older) or a gift of appreciated stock would beat cash here.

```oa-check
name: Floor and 2/37 reduction, top-bracket joint return (2026)
inputs:
  contribution_base: 1200000
  cash_gift: 100000
  other_itemized: 30000
  bracket_37_start: 768700
steps:
  - floor: contribution_base * 0.005
  - charity_allowed: cash_gift - floor
  - itemized: charity_allowed + other_itemized
  - excess: max(contribution_base - bracket_37_start, 0)
  - reduction: min(itemized, excess) * 2 / 37
  - itemized_after: itemized - reduction
  - gift_deducted: charity_allowed * 35 / 37
  - gift_tax_saving: gift_deducted * 0.37
expected:
  floor: 6000
  charity_allowed: 94000
  itemized: 124000
  excess: 431300
  reduction: 6702.70
  itemized_after: 117297.30
  gift_deducted: 88918.92
  gift_tax_saving: 32900.00
```

**Case 3, stock or cash (decision).** A single donor who itemizes holds listed shares bought in 2019 for USD 4,000, now worth USD 20,000, and wants to give USD 20,000 to a public charity. Giving the shares: deduction USD 20,000 (fair market value), subject to the 30% limit, and the USD 16,000 gain is never reported. Selling and giving the cash: the same USD 20,000 deduction (60% limit) but USD 16,000 of long-term gain is reported. Give the shares, unless the 30% limit binds and the carryover would go unused.

**Case 4, non-itemizer (decision).** A single filer takes the USD 16,100 standard deduction and gives USD 1,500 in cash to a church and USD 500 to a donor-advised fund. The non-itemizer deduction is USD 1,000: the church gift counts up to the cap, the donor-advised fund gift never does.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-CH-APPR | Property other than listed shares worth more than USD 5,000 (real estate, private company shares, art, collectibles) | Refer for a qualified appraisal; the valuation is outside this skill |
| R-CH-SPLIT | Charitable remainder or lead trusts, gift annuities, the one-time QCD to a split-interest entity (section 408(d)(8)(F)) | Refer; for gift and estate tax see `us-estate-gift-706-709` |
| R-CH-EASE | Conservation easements or any gift of a partial interest | Refer |
| R-CH-ENTITY | Gifts through a partnership, S corporation, trust or estate, or a corporation's own gifts | Out of scope |
| R-CH-QUID | The donor receives a benefit (a dinner, membership, tickets) or makes a bargain sale | Compute only after the charity states the value of the benefit; refer if unclear |
| R-CH-STATE | State income tax treatment | Out of scope; states decide for themselves |
| R-CH-DAF | A request to treat a donor-advised fund gift as a non-itemizer deduction or to fund it with a QCD | Refuse; the law says it cannot |

## Filing and payment

Itemized gifts go on Schedule A (Form 1040); the non-itemizer deduction is taken on Form 1040 on top of the standard deduction (check the line on the final 2026 Form 1040). Form 8283 goes with the return for noncash gifts over USD 500 in total. A qualified charitable distribution is reported as an IRA distribution with the excluded part shown as not taxable (Pub. 590-B). The 2026 return is due **15 April 2027**; an extension to 15 October 2027 moves only the filing date. Gifts must be paid by 31 December 2026 to count for 2026.

## Completion checklist

- Itemizing compared with the standard deduction plus the non-itemizer deduction.
- Each gift sorted by type and recipient; percentage limits applied to the contribution base.
- 0.5% floor applied in the statutory order; lost amount carried only where a limit was exceeded.
- 2/37 reduction tested against the start of the 37% bracket for the filing status.
- Carryovers from earlier years used in order; new carryover recorded.
- QCD tested for anyone aged 70½ or older; not sent to a donor-advised fund.
- Acknowledgments, bank records, Form 8283 and appraisals in the file before filing.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Law 119-21 (One Big Beautiful Bill Act). Read for section 70111 (2/37, new section 68), section 70424 (USD 1,000 / USD 2,000, "beginning in 2021" struck) and section 70425 (0.5% floor, floor order, section 170(d)(1)(C), 60% made permanent, section 170(p) coordination), all for taxable years beginning after 31 December 2025. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the 2026 standard deductions and the start of the 37% bracket. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 170 (govinfo, 2024 edition, before the Act). Read for (a)(1), (b)(1)(A) to (D) percentages, (b)(1)(H), (d)(1), (e)(1), (f)(8), (f)(11), (f)(17), (f)(18) and (p). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm | 2026-11-13 |
| 26 U.S.C. 63 (govinfo). Read for (b)(4), the section 170(p) deduction on top of the standard deduction. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partI-sec63.htm | 2026-11-13 |
| 26 U.S.C. 408 (govinfo). Read for (d)(8), qualified charitable distributions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408.htm | 2026-11-13 |
| 26 U.S.C. 4966 (govinfo). Read for (d)(1) and (d)(2), donor-advised fund definitions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleD-chap42-subchapG-sec4966.htm | 2026-11-13 |
| Notice 2025-67. Read for the 2026 QCD limit, increased from USD 108,000 to USD 111,000. | https://www.irs.gov/pub/irs-drop/n-25-67.pdf | 2026-11-13 |
| Notice 2026-10. Read for the 14 cents charitable mileage rate. | https://www.irs.gov/pub/irs-drop/n-26-10.pdf | 2026-11-13 |
| Treas. Reg. 1.170A-10 (eCFR). Read for carryovers used up in a standard deduction year. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR4f0b2f9ff1b8a63/section-1.170A-10 | 2026-11-13 |
| IRS Pub. 526 (2025), Charitable Contributions. Read for fair market value of property, delivery of stock, donor-advised fund sponsors and Form 8283. | https://www.irs.gov/pub/irs-pdf/p526.pdf | 2026-11-13 |
| IRS Pub. 544, Sales and Other Dispositions of Assets. Read for the definition of a sale. | https://www.irs.gov/pub/irs-pdf/p544.pdf | 2026-11-13 |
| IRS Pub. 561, Determining the Value of Donated Property. Read for appraisals. | https://www.irs.gov/pub/irs-pdf/p561.pdf | 2026-11-13 |
| IRS Pub. 590-B (2025). Read for QCDs counting toward the required minimum distribution and the per-spouse limit. | https://www.irs.gov/pub/irs-pdf/p590b.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Pub. 526 and the 2026 Form 1040 and Schedule A were not yet published when read, so the line on which the non-itemizer deduction is entered is not quoted; the 2026 rules above are taken from the Act itself.
