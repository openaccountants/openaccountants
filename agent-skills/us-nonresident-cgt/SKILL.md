---
name: us-nonresident-cgt
description: "Work out when the United States taxes a nonresident alien individual's 2026 gain on selling property, and how the tax is withheld and reported. Covers FIRPTA (section 897) gain on US real property interests treated as effectively connected income, US real property holding corporations and the listed-stock 5 percent and REIT 10 percent exceptions, the 183-day rule at 30 percent under section 871(a)(2), the trading safe harbour, sourcing by tax home, buyer withholding under section 1445 at 15 percent, 10 percent for a residence buyer at up to USD 1,000,000 and none at up to USD 300,000, Forms 8288, 8288-A and 8288-B, treaty claims on Form 8833, and the Form 1040-NR due dates. Trigger on \"FIRPTA\", \"nonresident selling US property\", \"15% withholding\", \"8288-B withholding certificate\", \"nonresident capital gains\", \"183-day rule\", \"USRPI\", \"W-8BEN broker\". For US residents use us-capital-gains. Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-nonresident-cgt"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US capital gains of nonresident alien individuals: FIRPTA, the 183-day rule and withholding, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 871, 897, 1411 and 1445 (2024 edition, not amended on these points by Public Law 119-21), IRS Publication 515 (2026), Publication 519 (2025, the latest edition), the 2025 Instructions for Form 1040-NR, the Instructions for Form 8288 and the IRS FIRPTA pages, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A nonresident alien's gain on **US real property** (and on stock of a US real property holding corporation) is taxed as effectively connected income at the ordinary graduated and capital gain rates, and the **buyer withholds 15%** of the amount realized (10% if an individual buyer will live there and the price is no more than **USD 1,000,000**; nothing at no more than **USD 300,000**). Withholding is a credit, not the tax: the seller files Form 1040-NR. Gain on **shares and other personal property** is usually not taxed at all, unless the seller was in the US **183 days or more** in the year and has a US tax home (then 30%, or a treaty rate, on net US-source gain), or the gain is effectively connected with a US business.

## Scope and who this is for

In scope: individuals who are nonresident aliens for the whole of 2026 (including treaty tie-breaker nonresidents whose claim is not in doubt, and exempt individuals such as F, J, M or Q students and A or G visa holders) who sell US real property, shares in US companies, other securities or personal property.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether the person is a resident or nonresident (green card test, substantial presence test, closer connection) | `us-tax-residency` |
| The Form 1040-NR return as a whole (brackets, deductions, Schedule NEC lines) | `us-form-1040-nr-nonresident-return` |
| US residents and citizens selling property | `us-capital-gains` |
| Getting an ITIN, including with Form 8288-B | `us-itin-form-w-7` |
| Installment sales | `us-installment-sale-6252` |
| Renting the property before the sale | `us-schedule-e-rental-income` |
| Former citizens and long-term residents | `us-expatriation-exit-tax` |
| Foreign corporations, partnerships, trusts and estates as sellers; estate and gift tax; dual-status years; state tax | Refer (see When to refuse or refer) |

## Ask the client first

1. **Status for the whole year of sale:** green card at any time? Days in the US in 2026, 2025 and 2024 (substantial presence)? Any treaty tie-breaker claim (Form 8833)? If any part of the year is resident, stop: see `us-tax-residency`.
2. **Days physically present in 2026**, and whether any were as an exempt individual (student, teacher, trainee, foreign-government or international-organisation employee). Exempt days still count for the 183-day capital gains rule.
3. **Tax home:** where is the client's main place of work? On arrival, did they intend to stay more than one year?
4. **What was sold:** US land or buildings; shares in a US corporation (listed or not, and the highest percentage of the class held in the past five years); REIT or fund shares; a partnership or LLC interest; foreign shares; personal-use items.
5. **US business presence:** an office, employees or a fixed place of business in the US? Dealing in securities, or only trading for their own account through a broker?
6. **For real property:** the amount realized (cash, plus fair market value of other property, plus liabilities the buyer assumes or takes subject to); whether the buyer is an individual who plans to live there; co-owners and whether they are US persons; adjusted basis and selling costs; any depreciation taken.
7. **Taxpayer identification number** (SSN or ITIN)? Has the buyer, closing agent or broker asked for Form W-8BEN or a non-foreign certification?
8. **Treaty residence** and whether that treaty has a capital gains article.
9. **Rental history:** was the property rented, and was the election to treat rental income as effectively connected made?
10. **States:** where is the property, and where did the client live or work in 2026?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Tax on net US-source capital gain of a nonresident present 183 days or more (not ECI) | 30% (or treaty rate) | [26 U.S.C. 871(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) |
| Days of presence that trigger it | 183 or more | [26 U.S.C. 871(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) |
| US real property holding corporation: US real property at least this share of real property and business assets | 50% | [26 U.S.C. 897(c)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm) |
| Look-back for USRPHC status: shorter of the holding period and | 5 years | [26 U.S.C. 897(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm) |
| Listed stock is a USRPI only for a holder of more than | 5% of the class | [26 U.S.C. 897(c)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm) |
| Listed REIT stock: limit instead | more than 10% | [26 U.S.C. 897(k)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm) |
| Domestically controlled REIT or RIC: foreign persons held less than | 50% in value | [26 U.S.C. 897(h)(4)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm) |
| FIRPTA withholding, general rule, on the amount realized | 15% | [26 U.S.C. 1445(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm) |
| Residence buyer, amount realized not more than this: no withholding | USD 300,000 | [26 U.S.C. 1445(b)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm) |
| Residence buyer, amount realized more than USD 300,000 and not more than this: 10% | USD 1,000,000 | [26 U.S.C. 1445(c)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm) |
| Reduced residence rate | 10% | [26 U.S.C. 1445(c)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm) |
| Buyer files Form 8288 and pays by the | 20th day after the transfer | [Instructions for Form 8288](https://www.irs.gov/pub/irs-pdf/i8288.pdf) |
| Home sale exclusion on Form 1040-NR (if eligible), maximum | USD 250,000 | [IRS FIRPTA withholding, question 5](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding) |
| Form 8833 non-disclosure penalty, individuals | USD 1,000 per failure | [Publication 519](https://www.irs.gov/publications/p519) |

The FIRPTA dollar limits, rates and the 183-day test are fixed in the statute and not indexed. The 2026 brackets and capital gain rate bands that apply to effectively connected gain are owned by `us-capital-gains` and `us-form-1040-nr-nonresident-return`.

### Step 1: confirm nonresident status for the whole year

1. If the client was a US resident for any part of 2026 (green card, substantial presence, first-year choice), stop: a dual-status year follows Publication 519, chapter 6, and this skill covers only the nonresident part. Treaty tie-breaker nonresidents compute tax as nonresidents and file Form 1040-NR with Form 8833. Source: [Publication 519](https://www.irs.gov/publications/p519); `us-tax-residency`.

### Step 2: classify each asset, in this order

2. **Is it a US real property interest (USRPI)?** If yes, go to Step 3: a USRPI gain is always treated as effectively connected income (ECI), whether or not the property is a capital asset. Source: [26 U.S.C. 897(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm).
3. **If not, is the gain ECI?** Gain from assets used in or held for a US trade or business is ECI. Trading in stocks or securities for one's own account, through a US broker or agent, is **not** a US trade or business; the safe harbour is lost if the client has a US office or other fixed place of business through which, or by whose direction, the trades are carried out. Gain on selling an interest in a partnership with a US business can be ECI under section 864(c)(8), and the buyer generally withholds 10% of the amount realized under section 1446(f): refer (R-NRCG-PSHIP). Source: [Publication 519](https://www.irs.gov/publications/p519); [Publication 515](https://www.irs.gov/publications/p515).
4. **If neither, apply the 183-day rule** (Step 5).

### Step 3: what counts as a USRPI

5. **Real property in the US or the US Virgin Islands:** land, buildings and their structural components, and unsevered natural products (crops, timber, mines, wells). Also personal property associated with the use of the real property (farming or construction equipment, furnishings of lodging facilities), unless it is disposed of more than one year before or after the real property, or sold separately to persons unrelated to the seller or buyer. Source: [26 U.S.C. 897(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm).
6. **Any interest (other than as a creditor) in a domestic corporation that is a US real property holding corporation (USRPHC):** its USRPIs are worth **at least 50%** of its USRPIs, its real property outside the US and its other trade or business assets, at any time in the shorter of the seller's holding period and the 5 years ending on the sale. Stock in a domestic corporation is treated as USRPHC stock unless the seller shows it is not.
7. **Cleansing exception:** an interest in a corporation is not a USRPI if, on the date of disposition, the corporation held no USRPIs, all USRPIs it held in the look-back period were disposed of in fully taxable transactions, and it was not a RIC or REIT in that period. Refer before relying on it. Source: [IRS FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding).
8. **Not a USRPI:**
   - Stock of a class **regularly traded on an established securities market**, unless the seller held **more than 5%** of the class at some time in the testing period (**more than 10%** for a REIT).
   - An interest in a **domestically controlled** REIT or qualifying RIC (foreign persons held less than 50% in value throughout the testing period).
   - REIT stock held by a **qualified shareholder** under section 897(k).
   - An interest in a **foreign corporation**, unless it elected to be treated as domestic.
9. **QIE wash-sale rule:** if the client sells an interest in a domestically controlled REIT or RIC in the 30 days before the ex-dividend date of a distribution that would have been USRPI gain, and acquires a substantially identical interest within the 61-day period, the distribution amount is treated as USRPI gain. It does not apply if the client actually received the distribution, or if the stock is regularly traded and the client held no more than 5% of the class at any time in the 1-year period ending on the distribution date. Source: [26 U.S.C. 897(h)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm).

### Step 4: tax on FIRPTA and other ECI gains

10. ECI and FIRPTA gains are taxed, after allowable deductions, at the same graduated rates and capital gain rates as citizens and residents, using the Form 1040-NR tax computation (with the Qualified Dividends and Capital Gain Tax Worksheet). Nonresident aliens generally **cannot claim the standard deduction**. Source: [Publication 519](https://www.irs.gov/publications/p519); [Instructions for Form 1040-NR](https://www.irs.gov/pub/irs-pdf/i1040nr.pdf).
11. **Minimum tax:** an alternative minimum tax may apply to net USRPI gain; figure it on Form 6251. Source: [26 U.S.C. 897(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm).
12. **USRPI losses** count only if they would be allowed under section 165(c), so a loss on a personal-use home is not deductible. Source: [26 U.S.C. 897(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm).
13. **Depreciation** taken on a rented property is recaptured as unrecaptured section 1250 gain on the sale: take the figures from `us-capital-gains`.
14. **Home sale exclusion:** a nonresident who sells their own former US home may exclude gain under section 121 if the ownership and use tests are met; the maximum on Form 1040-NR is USD 250,000. Withholding can then exceed the tax: consider a withholding certificate. Source: [IRS FIRPTA withholding, question 5](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding).
15. **Net investment income tax** does not apply to a nonresident alien; only a dual-status taxpayer may owe it, for the resident part of the year. Source: [26 U.S.C. 1411(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm).

### Step 5: the 183-day rule for gains that are neither USRPI nor ECI

16. If the client was present in the US **183 days or more** during the tax year, the **net US-source capital gain** is taxed at a flat **30%** (or a lower treaty rate). Below 183 days such gains are exempt. Exactly 183 days is caught. The rule applies even to sales made while the client was outside the US. A client not in a US trade or business, with no earlier tax year established, uses the calendar year. Source: [26 U.S.C. 871(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm).
17. **Sourcing:** gain on personal property (including shares) is generally US-source only if the seller has a **tax home in the United States**. With no US tax home the gain is foreign-source and not taxed under this rule. Most students, scholars and foreign-government employees who come intending to stay more than one year have a US tax home from the day they arrive. Source: [IRS, capital gains of nonresident students, scholars and employees of foreign governments](https://www.irs.gov/individuals/international-taxpayers/the-taxation-of-capital-gains-of-nonresident-alien-students-scholars-and-employees-of-foreign-governments).
18. **Net gain:** US-source capital gains minus US-source capital losses, counting gains and losses only to the extent they would be recognised if effectively connected. Do not take into account a capital loss carryover, capital losses above capital gains, the section 1202 exclusion, or losses on personal-use property. Report on Schedule NEC (Form 1040-NR). Source: [Publication 519](https://www.irs.gov/publications/p519).

### Step 6: treaty relief

19. Most treaties exempt gains on personal property; gains on US real property generally stay taxable. Read the actual treaty article, not the OECD model. Any treaty position that overrides or modifies the Code and reduces, or might reduce, tax is disclosed on **Form 8833**, and it is specifically required for a treaty reduction of tax on USRPI gain or loss. Exceptions include treaty-reduced withholding on FDAP income and disclosable items totalling no more than USD 10,000 (Regulations section 301.6114-1(c)). The penalty for not disclosing is USD 1,000 per failure for an individual, waivable for reasonable cause. Source: [Publication 519](https://www.irs.gov/publications/p519).

### Step 7: FIRPTA withholding on a sale of US real property

20. The **buyer** (transferee) is the withholding agent and must find out whether the seller is a foreign person; a buyer that fails to withhold can be liable for the tax. Source: [IRS FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding).
21. **Amount realized** = cash paid or to be paid (principal only) + fair market value of other property + any liability the buyer assumes or takes subject to. Where US and foreign persons own jointly, the amount realized is allocated by capital contribution (spouses 50% each); the buyer withholds on the amount allocated to the foreign seller or sellers. Foreign co-sellers can ask for the credit to be split as they agree by the 10th day after the transfer; otherwise it is divided evenly.
22. **Rate:** 15% of the amount realized. If the **buyer is an individual** who (or whose family member) has definite plans to live at the property for at least 50% of the days it is used by any person in each of the first two 12-month periods after the transfer (vacant days not counted), the rate is **10%** where the amount realized is more than USD 300,000 but not more than **USD 1,000,000**, and **nil** where it is not more than **USD 300,000**. Above USD 1,000,000 it is 15% even for a residence buyer. It need not be the buyer's main home. The limits test the **total** amount realized on the property, not each seller's share. Source: [26 U.S.C. 1445](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm); [Publication 515](https://www.irs.gov/publications/p515); [IRS, Exceptions from FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/exceptions-from-firpta-withholding).
23. **Other exceptions from withholding:** the seller certifies it is not a foreign person; the interest is in a domestic corporation with a class of stock regularly traded on an established securities market (not for certain dispositions of substantial non-traded interests: refer); a domestic corporation certifies the interest is not a USRPI; the IRS issues a withholding certificate; the seller gives written notice of a nonrecognition or treaty provision, which the buyer files with the IRS by the 20th day after the transfer; the amount realized is zero; or a US government unit acquires the property.
24. **Reporting and paying over:** the buyer files Form 8288 with Copies A and B of Form 8288-A and pays **by the 20th day after the transfer**. The IRS stamps Copy B and sends it to the seller, but not if the seller's TIN is missing; then the seller attaches substantial evidence of withholding (closing documents) and a statement with the Form 8288 and 8288-A information, including the TIN. A seller with no TIN can apply for an ITIN by attaching Form 8288-B to Form W-7. Source: [Instructions for Form 8288](https://www.irs.gov/pub/irs-pdf/i8288.pdf); [IRS, Reporting and paying tax on US real property interests](https://www.irs.gov/individuals/international-taxpayers/reporting-and-paying-tax-on-us-real-property-interests).
25. **Withholding certificate (Form 8288-B):** the buyer, its agent or the seller can apply to reduce or eliminate withholding because the withholding would exceed the seller's maximum tax liability, the gain is exempt, the transfer qualifies for nonrecognition, or a security agreement is made. The IRS generally acts within 90 days of a complete application with all parties' TINs. If an application is pending at closing, the buyer still withholds the full amount and pays over the withheld (or lesser approved) amount within 20 days after the IRS mails its decision; this applies only if the application was submitted on or before the transfer date, and a seller who applies must notify the buyer in writing on the day of the transfer or the day before. If the main purpose of applying was delay, interest and penalties run from the 21st day after the transfer. Report the gain in the year of the actual sale, even if the stamped Form 8288-A shows a later date. Source: [IRS, Withholding certificates](https://www.irs.gov/individuals/international-taxpayers/withholding-certificates).
26. **Withholding is not the tax.** It is a credit on Form 1040-NR (line 25f of the 2025 form, with the stamped Copy B of Form 8288-A). Even where no withholding applies, the seller still reports the gain. Assignment of a purchase contract is also a disposition subject to withholding (FAQ question 4).

### Step 8: shares sold through a broker

27. A nonresident with fewer than 183 days of presence, no US tax home and no US trade or business owes **no US tax** on selling listed US shares, unless the shares are USRPHC stock and the client held more than 5% of the class, or the class is not regularly traded.
28. **Form W-8BEN** establishes foreign status with the broker, which can then treat gross proceeds as exempt from Form 1099 reporting and backup withholding. It generally stays in effect until the last day of the third calendar year after signing, unless circumstances change; if the income becomes ECI, use Form W-8ECI. Source: [Publication 515](https://www.irs.gov/publications/p515); [Instructions for Form W-8BEN](https://www.irs.gov/instructions/iw8ben).
29. **Dividends are not capital gains:** US dividends not effectively connected are generally taxed at 30% or a lower treaty rate, withheld at source (`us-form-1040-nr-nonresident-return`).

### Step 9: file Form 1040-NR

30. Report 183-day gains on Schedule NEC; report ECI and FIRPTA gains on Schedule D (Form 1040) or Form 4797, attached to Form 1040-NR. A FIRPTA seller must file, because USRPI gain is treated as ECI from a US trade or business; the return settles the actual tax and recovers excess withholding. Source: [Publication 519](https://www.irs.gov/publications/p519).

## Boundary and exception table

| Fact pattern | Result |
| --- | --- |
| Presence exactly 183 days, US tax home, non-ECI gain on shares | Taxed at 30% (or treaty rate): the test is "183 days or more" |
| 183 days or more, but no US tax home | Gain is foreign-source, so not taxed under the 183-day rule |
| F-1 student (exempt individual) present 200 days | Still a nonresident, but exempt-individual days count for the 183-day capital gains rule |
| Held exactly 5% of a listed USRPHC class | Not a USRPI: the exception is lost only above 5% |
| Listed REIT shares, more than 5% but not more than 10% | Not a USRPI: the REIT limit is more than 10% |
| Residence buyer, amount realized exactly USD 300,000 | No withholding |
| Residence buyer, amount realized exactly USD 1,000,000 | 10% withholding |
| Foreign spouse and US spouse sell their home to a residence buyer for USD 500,000 in total | The USD 300,000 exemption tests the total, so it is not available; withholding is 10% of the foreign spouse's USD 250,000 share = USD 25,000 |
| Buyer is a company, or an investor who will rent it out | 15%, whatever the price |
| Seller sells their own former US home | Section 121 may exclude up to USD 250,000; consider a withholding certificate |
| Assignment of a purchase contract for US property | A disposition: withholding applies |
| Sale of a partnership interest where the partnership has a US business | Possibly ECI (864(c)(8)); 10% withholding under 1446(f): refer |
| Loss on a personal-use US home | Not deductible (section 165(c) test) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Days present in 2026 | Do not apply the 183-day rule until counted; ask for travel records |
| Tax home | Assume foreign for a short-stay visitor; assume US for a student or employee who came to stay more than a year |
| Whether a US company is a USRPHC | Treat its stock as a USRPI until the company certifies otherwise |
| Buyer's residence plans | 15% withholding unless the buyer signs the residence statement |
| Seller's TIN | Start the ITIN application now; the stamped Form 8288-A will not issue without it |
| Treaty article | No treaty exemption until the article is read |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Withholding far above the likely tax (small gain, loss, section 121) | Apply for a withholding certificate before closing |
| No ITIN at closing | The credit cannot be claimed smoothly |
| Days in the US near 183, or near the substantial presence count | The client may be a resident: `us-tax-residency` |
| A US office, employees or agent directing trades | The trading safe harbour may be lost |
| Unlisted US company shares | USRPHC test needed |
| Property held through an entity | Different withholding rules (section 1445(e)): refer |

## Worked cases

Amounts are invented. The 2026 figure in Case 1 comes from `us-capital-gains` (zero-rate maximum for a single filer, USD 49,450).

**Case 1, a decision: should the seller apply for a withholding certificate?** A nonresident sells vacant US land (never depreciated, not rented) to an investor for USD 750,000. Adjusted basis is USD 640,000 and selling costs USD 40,000, so the long-term gain is USD 70,000. The buyer will withhold 15% x 750,000 = USD 112,500. On Form 1040-NR, with no standard deduction and no other US income, taxable income is the USD 70,000 gain: 0% on the first USD 49,450 and 15% on USD 20,550 = USD 3,082.50 (before any minimum tax and state tax). Apply for a withholding certificate on Form 8288-B on or before the transfer date, with an ITIN application if needed: it frees about USD 109,417.50 at closing instead of waiting for a refund after filing.

```oa-check
name: FIRPTA withholding against the likely tax (2026)
inputs:
  amount_realized: 750000
  basis: 640000
  selling_costs: 40000
  zero_rate_top: 49450
steps:
  - withholding: amount_realized * 0.15
  - gain: amount_realized - basis - selling_costs
  - tax: max(gain - zero_rate_top, 0) * 0.15
  - excess_withheld: withholding - tax
expected:
  withholding: 112500.00
  gain: 70000.00
  tax: 3082.50
  excess_withheld: 109417.50
```

**Case 2: residence band, joint sellers, and the 183-day rule.** (a) A nonresident sells a condo to an individual who will live there: cash USD 520,000 plus an assumed mortgage of USD 230,000, so the amount realized is USD 750,000 and withholding is 10% = USD 75,000 (15% = USD 112,500 for an investor buyer). (b) A foreign spouse and a US spouse sell their home to a residence buyer for USD 500,000; the foreign spouse's share is USD 250,000 and withholding is 10% of it = USD 25,000. (c) An F-1 student with a US tax home, present 200 days in 2026, has US-source capital gains of USD 12,000 and losses of USD 2,000: 30% x 10,000 = USD 3,000 on Schedule NEC, unless the treaty exempts it (then Form 8833 unless an exception applies).

```oa-check
name: FIRPTA rates and the 183-day rule (2026)
inputs:
  cash: 520000
  assumed_mortgage: 230000
  joint_total: 500000
  gains: 12000
  losses: 2000
steps:
  - amount_realized: cash + assumed_mortgage
  - residence_withholding: amount_realized * 0.10
  - investor_withholding: amount_realized * 0.15
  - foreign_spouse_withholding: joint_total * 0.5 * 0.10
  - tax_183_day: max(gains - losses, 0) * 0.30
expected:
  amount_realized: 750000.00
  residence_withholding: 75000.00
  investor_withholding: 112500.00
  foreign_spouse_withholding: 25000.00
  tax_183_day: 3000.00
```

**Other quick results.** Listed shares sold by a nonresident with 20 days in the US, no US office or tax home, and well under 5% of the class: no US tax and no return needed for the gain; keep a current W-8BEN. A residence buyer pays exactly USD 300,000: no withholding, but the seller still reports the gain. A residence buyer pays exactly USD 1,000,000: 10% = USD 100,000. An investor buys for USD 280,000: the residence exception does not apply, so 15% = USD 42,000.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NRCG-RES | Residency unclear: substantial presence near the line, closer connection, a doubtful treaty tie-breaker, or a dual-status year | Refer; `us-tax-residency` |
| R-NRCG-ENTITY | Seller is a corporation, partnership, trust or estate, or the property is held through an entity (section 1445(e)) | Refer |
| R-NRCG-USRPHC | Unlisted US stock needing a USRPHC test, a large holding of a listed class, or REIT and RIC interests beyond the plain exceptions | Refer |
| R-NRCG-PSHIP | Sale of a partnership or LLC interest (sections 864(c)(8) and 1446(f)) | Refer |
| R-NRCG-NONREC | Installment sales, like-kind exchanges, other nonrecognition claims, or a certificate based on a security agreement | Refer |
| R-NRCG-TREATY | A treaty claim that US real property gain is exempt or reduced | Refer |
| R-NRCG-EXPAT | Former US citizens or long-term residents; any estate or gift tax question | `us-expatriation-exit-tax`, `us-estate-gift-706-709` |
| R-NRCG-STATE | Any state tax question | Refer: state rules and state withholding on real property sales are outside this skill |

## Filing and payment

- **Buyer at closing:** withhold, then file Form 8288 with Copies A and B of Form 8288-A and pay by the **20th day after the transfer**; if a Form 8288-B application was pending on the transfer date, within 20 days after the IRS mails its decision. Source: [Instructions for Form 8288](https://www.irs.gov/pub/irs-pdf/i8288.pdf).
- **Seller's 2026 Form 1040-NR:** due **15 June 2027** if the client had no wages subject to US withholding, or **15 April 2027** if they had; Form 4868 extends the time to file (to 15 December 2027 or 15 October 2027), not to pay. Attach the stamped Form 8288-A Copy B, Schedule NEC and/or Schedule D or Form 4797, and Form 8833 where required. Source: [Publication 519](https://www.irs.gov/publications/p519).
- **Estimated tax:** a nonresident expecting 2026 tax not covered by withholding uses Form 1040-ES (NR); see `us-form-1040-nr-nonresident-return`.
- **Refunds** of tax withheld on Form 8288-A can take up to 6 months.
- **2025 returns still open:** due 15 June 2026 (no wages) or 15 April 2026 (wages), extended to 15 December 2026 or 15 October 2026. The FIRPTA rates and limits and the 183-day rule were the same for 2025.

## Completion checklist

- [ ] Nonresident status confirmed for the whole year; any treaty tie-breaker documented.
- [ ] Each asset classified as USRPI, ECI or other, with the USRPHC look-back and the 5% and 10% listed-stock tests where relevant.
- [ ] Days of presence counted (including exempt-individual days) and tax home established.
- [ ] Net 183-day gain computed without carryovers, the section 1202 exclusion or personal-use losses.
- [ ] Amount realized includes assumed liabilities; FIRPTA rate chosen from the buyer's residence facts and the total price.
- [ ] Withholding certificate considered where withholding exceeds the likely tax.
- [ ] Form 8288 and 8288-A filed by the buyer within 20 days; seller's TIN or ITIN in place.
- [ ] W-8BEN current with each broker.
- [ ] Treaty article read; Form 8833 attached unless an exception applies.
- [ ] Form 1040-NR filed by the right due date, with the Form 8288-A credit claimed.
- [ ] State position checked with the state's own revenue department.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 871 (govinfo). Read for (a)(2): "183 days or more", "a tax of 30 percent of the amount by which his gains ... exceed his losses". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm | 2026-11-13 |
| 26 U.S.C. 897 (govinfo). Read for (a) ECI treatment, (b) losses, (c)(2) 50% USRPHC test, (c)(3) "more than 5 percent", (h)(4) "less than 50 percent", (h)(5) wash sales and (k) "more than 10 percent" for REITs. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartD-sec897.htm | 2026-11-13 |
| 26 U.S.C. 1445 (govinfo). Read for (a) "15 percent of the amount realized", (b)(5) "does not exceed $300,000", (c)(4) "does not exceed $1,000,000" and "10 percent". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm | 2026-11-13 |
| 26 U.S.C. 1411 (govinfo). Read for (e) nonresident aliens excluded from the net investment income tax. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-13 |
| IRS Publication 515 (2026). Read for the residence rule: no withholding up to $300,000, 10%, 15% above $1,000,000; W-8BEN; section 1446(f). | https://www.irs.gov/publications/p515 | 2026-11-13 |
| IRS Publication 519 (2025). Read for the 183-day rule, the trading safe harbour, no standard deduction, Schedule NEC, Form 8833 and the $1,000 penalty, and the June 15 due date. | https://www.irs.gov/publications/p519 | 2026-11-13 |
| Instructions for Form 1040-NR (2025). Read for line 25f, Form 8288-A. | https://www.irs.gov/pub/irs-pdf/i1040nr.pdf | 2026-11-13 |
| Instructions for Form 8288 (2026 revision). Read for the 20th-day deadline and pending applications. | https://www.irs.gov/pub/irs-pdf/i8288.pdf | 2026-11-13 |
| IRS, FIRPTA withholding. Read for the amount realized, joint sellers (questions 1 and 17), contract assignments (question 4), section 121 (question 5) and timing (question 3). | https://www.irs.gov/individuals/international-taxpayers/firpta-withholding | 2026-11-13 |
| IRS, Exceptions from FIRPTA withholding. Read for the residence-use test. | https://www.irs.gov/individuals/international-taxpayers/exceptions-from-firpta-withholding | 2026-11-13 |
| IRS, Withholding certificates. Read for Form 8288-B grounds and the 90-day processing time. | https://www.irs.gov/individuals/international-taxpayers/withholding-certificates | 2026-11-13 |
| IRS, Reporting and paying tax on US real property interests. Read for the stamped Copy B and a missing TIN. | https://www.irs.gov/individuals/international-taxpayers/reporting-and-paying-tax-on-us-real-property-interests | 2026-11-13 |
| IRS, Taxation of capital gains of nonresident alien students, scholars and employees of foreign governments. Read for the US tax home rule. | https://www.irs.gov/individuals/international-taxpayers/the-taxation-of-capital-gains-of-nonresident-alien-students-scholars-and-employees-of-foreign-governments | 2026-11-13 |
| Instructions for Form W-8BEN. Read for how long the form stays in effect. | https://www.irs.gov/instructions/iw8ben | 2026-11-13 |

Not yet confirmed: the 2026 Publication 519 and the 2026 Instructions for Form 1040-NR were not published when read, so the line number for the Form 8288-A credit (line 25f on the 2025 form) and the 2026 due-date wording are taken from the 2025 editions; the IRS FIRPTA question numbers (1, 3, 4, 5 and 17) are as the page showed them on the read date and can change.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-nonresident-cgt` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-nonresident-cgt. If neither is available, confirm every figure against the official source pages cited above before relying on it.
