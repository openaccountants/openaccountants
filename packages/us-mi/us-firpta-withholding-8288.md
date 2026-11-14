---
name: us-firpta-withholding-8288
description: The buyer's side of FIRPTA in 2026, for a US real property purchase from a foreign seller. Covers who must withhold (the transferee), how to tell a foreign seller (certification of non-foreign status), the 15% general rate on the amount realized, the residence exceptions (no withholding up to USD 300,000, 10% up to USD 1,000,000 when the buyer will live there), the other exceptions, withholding certificates on Form 8288-B, and filing Form 8288 with Forms 8288-A and paying by the 20th day after the transfer. Points to the 21% entity rules and the section 1446(f) partnership rules. Trigger on "FIRPTA withholding", "Form 8288", "Form 8288-A", "8288-B withholding certificate", "buying from a foreign seller", "15% FIRPTA", "10% FIRPTA residence", "closing agent FIRPTA". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# FIRPTA withholding by the buyer (Forms 8288, 8288-A and 8288-B), 2026

> **Source-cited draft.** Built from the Instructions for Form 8288 (Rev. January 2026), Form 8288 (Rev. January 2026), IRS Pub. 515 (2026) and 26 U.S.C. 1445, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A buyer of a US real property interest from a foreign person must generally withhold **15% of the amount realized** (the price, plus liabilities taken over), not of the gain. If the buyer is an individual who will live in the property, there is **no withholding** when the amount realized is **USD 300,000 or less**, and **10%** when it is **USD 1,000,000 or less**. The buyer files Form 8288 with Copies A and B of Form 8288-A for each seller and pays the tax **by the 20th day after the date of transfer**. A buyer who fails to withhold can be made to pay the tax.

## Scope and who this is for

In scope: a buyer (transferee), or the closing agent working for one, acquiring a US real property interest from a foreign individual, foreign corporation, foreign partnership, foreign trust or estate in 2026; the withholding amount; the exceptions; Form 8288-B; and Forms 8288 and 8288-A.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The foreign seller's own tax on the gain and claiming the withholding back on Form 1040-NR | `us-nonresident-cgt` |
| Nonresident return mechanics | `us-form-1040-nr-nonresident-return` |
| Withholding on dividends, interest, royalties and other FDAP income (Forms 1042, 1042-S) | `us-nonresident-withholding-1042-w-8` |
| A seller with no US taxpayer number (ITIN application with Form 8288-B) | `us-itin-form-w-7` |
| 21% withholding by US corporations, partnerships, trusts and estates on distributions (section 1445(e)) | refer (see the refusal table) |
| Transfers of partnership interests (section 1446(f), 10%) | refer (see the refusal table) |
| State real estate withholding on non-resident sellers | the state's skill |

## Ask the client first

1. **Is the seller a foreign person?** Ask for a signed certification of non-foreign status (seller's name, US TIN, home address, under penalties of perjury). If the seller gives one and the buyer has no reason to doubt it, no withholding.
2. **Who is buying** (one or more individuals, or an entity), and will the buyer or a family member live in the property at least 50% of the days it is used in each of the first two 12-month periods after closing?
3. **The amount realized:** contract price, any other property given, and any mortgage or other liability the buyer assumes or takes the property subject to.
4. **All sellers,** each one's share, and each one's name, address and US TIN (SSN, ITIN or EIN).
5. **Has anyone applied for a withholding certificate on Form 8288-B,** and when (on or before the date of transfer)?
6. **The date of transfer:** the first date consideration is paid or a liability is assumed (earnest money that binds the contract does not count).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| General withholding rate, on the amount realized | 15% | [26 U.S.C. 1445(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm); [Instructions for Form 8288 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/i8288.pdf) |
| No withholding: buyer acquires for use as a residence and amount realized does not exceed | USD 300,000 | [26 U.S.C. 1445(b)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm) |
| Reduced rate: buyer acquires for use as a residence and amount realized does not exceed USD 1,000,000 | 10% | [26 U.S.C. 1445(c)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm); [Instructions for Form 8288 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/i8288.pdf) |
| Residence ceiling for the reduced rate | USD 1,000,000 | [26 U.S.C. 1445(c)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm) |
| Residence use test: buyer or family plans to live there at least this share of days used, in each of the first two 12-month periods | 50% | [Instructions for Form 8288 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/i8288.pdf) |
| Entity distributions under section 1445(e) | 21% | [Instructions for Form 8288 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/i8288.pdf) |
| Deadline to file Form 8288 and pay | 20th day after the date of transfer | [Instructions for Form 8288 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/i8288.pdf) |
| Keep a non-foreign certification for | 5 years after the year of transfer | [Instructions for Form 8288 (Rev. January 2026)](https://www.irs.gov/pub/irs-pdf/i8288.pdf) |

None of the dollar limits is indexed. "Does not exceed" means exactly USD 300,000 needs no withholding and exactly USD 1,000,000 is in the 10% band.

### Steps

1. **Is it a US real property interest?** Land, buildings, and interests in a US real property holding corporation are. An interest in a domestic corporation whose stock is regularly traded on an established market generally is not (certain large holdings excepted), and a domestic corporation may certify its stock is not a USRPI.
2. **Is the seller foreign?** A nonresident alien individual, foreign corporation (unless it elected under section 897(i) to be treated as domestic), foreign partnership, trust or estate. A disregarded entity is looked through: its owner is the seller. If the seller certifies non-foreign status, keep the certificate 5 years and do not withhold, unless the buyer knows it is false or receives a notice of false certification before closing.
3. **Amount realized** = cash paid or to be paid (not interest), plus the fair market value of other property, plus any liability the buyer assumes or the property is subject to. Usually the contract price.
4. **Rate.** Start at 15%. If the buyer is one or more individuals acquiring for use as a residence (step 5 of "Ask the client first"): 0% up to USD 300,000; 10% from above USD 300,000 to USD 1,000,000; 15% above USD 1,000,000. The limits apply to the whole property, not each seller's share.
5. **Other exceptions** (no withholding): the IRS has issued a withholding certificate for zero; the seller gives a notice of nonrecognition or a treaty provision, and the buyer sends it to the IRS by the 20th day after the transfer; the amount realized is zero; the buyer is a US government unit; the property is acquired by a qualified foreign pension fund in the cases the instructions describe.
6. **Withholding certificate (Form 8288-B).** The buyer or the seller can apply to reduce withholding, usually to the seller's expected maximum tax on the gain. If an application is filed on or before the date of transfer, the buyer still withholds the full amount but may hold it until the 20th day after the IRS mails its decision, then pays the reduced amount and returns the rest to the seller.
7. **Withhold at closing** and **file Form 8288** with **Copies A and B of Form 8288-A** for each foreign seller, and pay, by the 20th day after the date of transfer. Several sellers in one deal: one Form 8288 with a Form 8288-A for each. The IRS stamps Copy B and sends it to the seller, who claims the credit on their return (see `us-nonresident-cgt`). The buyer does not have to give the seller a copy.
8. **Joint sellers.** Split the withholding by each seller's share of the capital invested; spouses are treated as 50% each, unless the sellers agree otherwise and tell the buyer by the 10th day after the transfer.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Buyer is a company, or an individual who will rent the property out | No residence exception: 15% |
| Amount realized exactly USD 300,000, buyer will live there | No withholding |
| Amount realized USD 1,000,001, buyer will live there | 15% on the whole amount |
| Seller's share is under USD 300,000 but the total is above | Withhold: the test is the total amount realized |
| Cash proceeds smaller than the withholding (heavily mortgaged property) | Still withhold the full amount, or get a withholding certificate before closing |
| Seller's certification of non-foreign status shown to be false after closing | Late notice rules in the Form 8288 instructions: withhold from any later payments |
| Seller has no US TIN | Still withhold and file; the IRS will not stamp Copy B until the seller has a TIN |
| Buyer is also foreign | Still the withholding agent |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Seller's status | Treat as foreign and withhold 15% unless a valid certification is in hand |
| Residence intent | 15%; the reduced band needs the buyer's definite plans |
| Liabilities assumed | Ask; the amount realized includes them |
| Each seller's share | Equal shares, and ask |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Closing in under 20 days with a pending Form 8288-B | Withhold the full amount and hold it; do not release it to the seller |
| Seller is a foreign LLC or a US LLC owned by a foreigner | A disregarded US LLC does not make the seller domestic; look through to the owner |
| Seller insists on a nonrecognition notice (for example a like-kind exchange) | The notice must reach the IRS by the 20th day, and nonrecognition rules are narrow for foreign sellers |
| Buyer claims the residence exception but plans to rent the property | The buyer stays liable if the 50% use test fails |

## Worked cases

**Case 1, a decision: does the residence exception apply?** A married couple are buying a house from a nonresident alien for USD 950,000, with no liabilities assumed. If they will live in it for at least 50% of the days it is used in each of the first two years, the rate is 10%: USD 95,000. If they plan to rent it out, the rate is 15%: USD 142,500. The residence plan changes the withholding by USD 47,500. Recommend the 10% rate only with a written statement of the buyers' plans in the closing file; otherwise withhold 15%.

```oa-check
name: FIRPTA residence exception at a price of 950,000 (2026)
inputs:
  amount_realized: 950000
steps:
  - as_residence: amount_realized * 0.10
  - not_residence: amount_realized * 0.15
  - difference: not_residence - as_residence
expected:
  as_residence: 95000.00
  not_residence: 142500.00
  difference: 47500.00
```

**Case 2, two foreign sellers and an assumed mortgage.** A company buys a rental condo from two nonresident spouses. It pays USD 400,000 in cash and takes the property subject to a USD 200,000 mortgage. The amount realized is USD 600,000. A company cannot use the residence exception, so the rate is 15%: USD 90,000. The spouses are treated as 50% each, so each Form 8288-A shows USD 45,000. Form 8288 and the payment are due by the 20th day after closing.

```oa-check
name: Two foreign sellers with a mortgage taken over (2026)
inputs:
  cash: 400000
  liability: 200000
  share_each: 0.5
steps:
  - amount_realized: cash + liability
  - withholding: amount_realized * 0.15
  - per_seller: withholding * share_each
expected:
  amount_realized: 600000
  withholding: 90000.00
  per_seller: 45000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FIRPTA-ENTITY | Distribution by a US corporation, partnership, trust or estate of a USRPI or its proceeds to a foreign person (section 1445(e), 21%) | Refer |
| R-FIRPTA-1446F | Sale of an interest in a partnership (section 1446(f)) | Refer: different forms and a 10% rate |
| R-FIRPTA-QIE | REIT or RIC shares, or a domestically controlled QIE | Refer |
| R-FIRPTA-NONREC | Seller claims a nonrecognition provision or a treaty exemption | Refer: the notice must meet Regulations section 1.1445-2(d)(2) |
| R-FIRPTA-LATE | Withholding not done at closing, or Form 8288 filed after the 20th day | Refer: penalties and interest run from the 21st day; the buyer may owe the tax |

## Filing and payment

Form 8288 with Copies A and B of each Form 8288-A goes to the IRS in Ogden, Utah, with payment, by the 20th day after the date of transfer. The penalty for failing to file or pay is under section 6651, and responsible persons can face a penalty for willful failure. Keep Copy C and the closing file, including any non-foreign certification, for at least 5 years.

## Completion checklist

- Seller's foreign status established, or a valid non-foreign certification kept for 5 years.
- Amount realized includes every liability assumed.
- Rate chosen (0%, 10% or 15%) with the buyer's written residence plans in the file for a reduced rate.
- One Form 8288-A per foreign seller, with TINs where available.
- Form 8288 filed and paid by the 20th day after the date of transfer, or held under a pending Form 8288-B.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 8288 (Rev. January 2026). Read for Amount To Withhold (15%), Purchase of residence for USD 1 million or less (10%), Purchase of residence for USD 300,000 or less (none), the 50% residence test, amount realized, date of transfer, the 20th-day deadline, 21% under section 1445(e), the 5-year record rule and penalties. | https://www.irs.gov/pub/irs-pdf/i8288.pdf | 2026-11-13 |
| Form 8288 (Rev. January 2026). Read for the return layout and the attachment of Forms 8288-A. | https://www.irs.gov/pub/irs-pdf/f8288.pdf | 2026-11-13 |
| 26 U.S.C. 1445 (govinfo, 2024 edition). Read for (a) 15%, (b)(5) residence not over USD 300,000, (c)(4) reduced rate where the amount realized does not exceed USD 1,000,000. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1445.htm | 2026-11-13 |
| IRS Pub. 515 (2026). Read for the overview of section 1445 withholding and the cross-references to Form 8288. | https://www.irs.gov/pub/irs-pdf/p515.pdf | 2026-11-13 |

Not yet confirmed: the rules for splitting withholding among joint sellers (step 8) are taken from the IRS FIRPTA withholding page as summarised in `us-nonresident-cgt` and were not re-read for this skill.
