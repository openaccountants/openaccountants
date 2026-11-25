---
name: au-nonresident-cgt
description: "Use this skill for any non-resident selling Australian assets. Trigger on: \"non-resident CGT Australia\", \"TAP test Australia\", \"taxable Australian property\", \"FRCGW\", \"foreign resident capital gains withholding\", \"15% withholding Australia\", \"12.5% withholding Australia\", \"clearance certificate ATO\", \"sell Australian shares non-resident\", \"sell Australian property non-resident\", \"Australian CGT non-resident seller\", \"no CGT discount non-resident Australia\". Covers the TAP test, the foreign resident rate scale, FRCGW withholding (15%, no threshold, from 1 January 2025), clearance certificates. For Australian residents see au-capital-gains."
version: 1.5
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-22
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# AU Nonresident Cgt

## Section 1 — Quick Reference

**Section 1 Quick Reference table**  _(ITAA 1997 Div 855; TAA 1953 Sch 1 Subdiv 14-D; [ATO, Tax rates: foreign resident](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-foreign-residents))_

| Field | Value |
| --- | --- |
| Country | Australia |
| Applies to | Non-residents of Australia disposing of Australian assets |
| CGT rate (non-resident individual) | Apply the rates in section 4 to total taxable income including the net capital gain. Confirm full-year residence status. ([ATO foreign-resident rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-foreign-residents)) |
| Key test | Taxable Australian property (TAP). Apply the changes effective 1 October 2026 for events from that date. ([ITAA 1997 Div 855](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html)) |
| Withholding | 15% of the statutory amount, ordinarily the arm's-length sale price, from 1 January 2025. There is no real property value threshold for those contracts. The prior 12.5% rate and $750,000 real property market value threshold applied from 1 July 2017 to 31 December 2024. ([Amending Act Schedule 1](https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/pdf); [2017 Act Schedule 1](https://www.legislation.gov.au/C2017A00057/asmade/2017-06-22/text/original/pdf); [ATO FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview)) |
| Primary legislation | ITAA 1997 Div 855; TAA 1953 Sch 1 Subdiv 14-D |
| Tax authority | ATO (ato.gov.au) |
| Verified by | Pending — Australian CPA/CA sign-off required |

## Section 2 — The Core Rule

- **Core rule for non-resident CGT** — Non-residents are only subject to Australian CGT on **Taxable Australian Property (TAP)**. Non-TAP assets sold by non-residents: **no Australian CGT**.  _(ITAA 1997 Div 855)_

## Section 3 — The TAP Test: What Qualifies as TAP

**TAP test asset types table**

| Asset type | TAP? |
| --- | --- |
| Australian real property | TAP. From 1 October 2026 this includes specified interests and rights over Australian land and things fixed or installed on it. |
| Australian mining, quarrying or prospecting rights | TAP if the relevant minerals, petroleum or quarry materials are situated in Australia. |
| Water entitlements for Australian water resources | TAP from 1 October 2026. |
| Shares or units | TAP as an indirect interest where both the non-portfolio and principal asset tests are met. Consider other TAP categories separately. |
| Options or rights | From 1 October 2026, options or rights to acquire taxable Australian real property are themselves taxable Australian real property. Item 4 of s 855-15 continues to cover options or rights to acquire an indirect real property interest or an Australian permanent establishment business asset. |
| Australian permanent establishment business assets | TAP where the asset has been used at any time to carry on business through the Australian permanent establishment. Apply the relevant treaty definition where required. |
| Asset covered by a departure election | TAP where s 104-165(3) applies after a choice to disregard the gain or loss on ceasing Australian residence. |

- **Non-portfolio interest test.** Add direct participation interests of the holder and its associates. The total must be at least 10% at the relevant time or throughout a 12-month period starting no earlier than 24 months before that time and ending by that time (ss 855-25 and 960-195).
- **Principal asset test.** Compare the market values of the entity's taxable Australian real property and other assets using the statutory look-through and duplicate-asset rules. The former must exceed the latter. For CGT events before 1 October 2026 test at the relevant time. For events from that date test at that time or at any time in the preceding 365 days, subject to any alternative time determined under s 855-25(1A). For the test, count Australian mining, quarrying or prospecting information as taxable Australian real property (ss 855-25, 855-30 and 855-32).

## Section 4 — CGT Rate for Non-Residents

**CGT rate for non-residents table**

| Item | Non-resident treatment |
| --- | --- |
| CGT rate (individual, 2025-26 and 2026-27) | Progressive foreign-resident rates: 30% to $135,000; $40,500 plus 37% over $135,000 to $190,000; $60,850 plus 45% over $190,000. Apply to total taxable income, including the net capital gain. No Medicare levy. [ATO foreign-resident rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-foreign-residents) |
| General CGT discount | Do not automatically set the discount to zero. For otherwise eligible gains, apply the acquisition-date, residency-period and 8 May 2012 market-value rules in [ITAA 1997 section 115-115](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-115). Eligible Australian-resident periods and pre-8 May 2012 gains can preserve a partial discount. |
| Renewable energy transitional discount | A separate 50% discount can apply to an eligible foreign resident other than an individual, or to the trustee of a foreign trust for CGT purposes, for a qualifying event from 1 October 2026 to 30 June 2040. For a qualifying indirect interest the Australian renewable energy asset value must be at least 3 times the value of its other taxable Australian real property. See the transitional Act ss 855-5 to 855-20. |
| SBCGT concessions | Available if all basic conditions met (including active asset test) |
| Main residence exemption | Generally unavailable if a foreign resident at disposal. The life-events exception requires a continuous foreign-residence period of 6 years or less and a qualifying terminal illness, death or relationship breakdown, together with the other exemption conditions. Citizenship or permanent residence alone does not qualify. [ITAA 1997 section 118-110](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110) |
| Cost base calculation | Same as residents |

- **Gains, losses and the order of steps** — Calculate each gain from capital proceeds and the adjusted cost base, and each loss from the reduced cost base, then apply capital losses and concessions in the statutory order. An asset that is not TAP produces a disregarded loss as well as a disregarded gain.  _([ITAA 1997 Div 855](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/855-15))_
- **Changes from 1 July 2027** — The Treasury Laws Amendment (Tax Reform No. 1) Act 2026 changes CGT arrangements for events from 1 July 2027. This guide's discount and rate treatment covers events before that date; apply the enacted transitional rules to later transactions. See `au-capital-gains.md`.  _([Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/text))_

## Section 5 — Foreign Resident Capital Gains Withholding (FRCGW)

- **FRCGW obligation.** Apply Subdivision 14-D to taxable Australian real property, indirect Australian real property interests and options or rights to acquire either. Check vendor status, exclusions and any certificate, eligible declaration or variation. The rate applies to the first cost base element just after acquisition, with the statutory adjustment where an option is exercised. This is ordinarily the sale price in an arm's-length real property transaction. Check market value where the transaction is not at arm's length and apply the separate rule for later look-through earnout benefits.
- **FRCGW nature** — **FRCGW nature** — This is a payment on account (not a final tax). Actual tax liability is computed in the non-resident's Australian tax return.

**FRCGW threshold table**

| FRCGW threshold | None, for contracts signed from 1 January 2025 |
| --- | --- |
| Withholding rate | 15% of the statutory amount absent a variation ([ATO FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview)) |
| Who withholds | The buyer (purchaser) |
| Remittance deadline | Day of settlement |

**Example** (synthetic): a full-year foreign resident individual sells taxable Australian real property at arm's length for AUD $10 million under a contract signed after 1 January 2025. With no variation or exclusion, the purchaser withholds and pays 15%, or AUD $1.5 million. Suppose the net capital gain after any available discount is AUD $8 million, with no other taxable income or offsets. Australian tax on the foreign resident scale is $60,850 plus 45c for each dollar above $190,000, giving $60,850 + 0.45 × $7,810,000 = AUD $3,575,350. Crediting the $1.5 million paid leaves AUD $2,075,350 payable through the Australian tax return.

```oa-check
name: AU non-resident TARP sale AUD 10m with 15% FRCGW and AUD 8m gain
inputs:
  sale_price: 10000000
  frcgw_rate: 15
  net_capital_gain: 8000000
  top_threshold: 190000
  top_base_tax: 60850
  top_rate: 45
steps:
  - withholding_paid: pct(sale_price, frcgw_rate)
  - total_tax: top_base_tax + pct(net_capital_gain - top_threshold, top_rate)
  - net_tax_payable: total_tax - withholding_paid
expected:
  withholding_paid: 1500000
  total_tax: 3575350
  net_tax_payable: 2075350
```

```oa-check
name: AU FRCGW AUD 700,000 contract from 1 January 2025 vs pre-2025
inputs:
  sale_price: 700000
steps:
  - withholding_pre_2025: 0
  - withholding_from_2025: pct(sale_price, 15)
expected:
  withholding_pre_2025: 0
  withholding_from_2025: 105000
```

## Section 6 — Clearance Certificate

- **Clearance certificate for resident sellers.** The vendor of taxable Australian real property or a right or option to acquire it can apply to the ATO in the approved form. Give a valid certificate to the buyer by settlement to avoid withholding under the ordinary rules. A certificate is valid for 12 months from issue.
- **Variation.** A vendor can seek a lower withholding amount where it would exceed the expected Australian tax liability, including a nil-rate request when appropriate. Use an approved variation received by the buyer before ownership passes.
- **Vendor declarations.** An eligible residency or non-indirect Australian real property interest (non-IARPI) declaration can relieve withholding under s 14-210(3). Check the declaration type and whether the purchaser knows, or could reasonably be expected to know, that it is false. Qualifying transactions on an approved stock exchange are excluded under s 14-215.
- **Large non-IARPI declarations.** For transactions covered by the rule from 1 October 2026, where the transaction plus related transactions have a statutory value of $50 million or more and no prescribed exception applies, the vendor must give the ATO an approved notice for the buyer to rely on the declaration. For a contract-to-ownership period over 31 days, notify at least 28 days before the end. For a period of 31 days or less, notify before or as soon as reasonably practicable after the contract, and before ownership passes. Give the purchaser the written notice declaration before ownership passes (ss 14-210(3)-(6), 14-225(2A) and 14-226).

Use the ATO's approved online form, or the paper clearance certificate form if needed. The ATO says to allow up to 28 days for a certificate or variation.

## Section 7 — Filing Obligations for Non-Residents

- **Filing requirement.** Check the annual lodgment instrument and the taxpayer's entity type. A full-year non-resident individual who derives taxable Australian income or has FRCGW paid on their behalf generally must lodge. A sale alone does not establish a filing obligation. For 2025-26 the ordinary statutory date was 31 October 2026, with the next-working-day rule applying that year. Check the instrument for 2026-27 and any applicable tax agent program or substituted accounting period.
- **TFN requirement** — **TFN requirement** — Australian Tax File Number (TFN) is required. Non-residents can apply via ATO.
- **Reconcile the withholding credit** — The withheld amount is a credit in the vendor's assessment, not the final tax. Reconcile it in the Australian return, retain the purchaser's payment evidence and confirm the lodgement deadline for the entity.

## Section 8 — Interaction with Tax Treaties

Check the applicable treaty's alienation of property article, permanent establishment definition, relevant protocols and any Multilateral Instrument modification. A treaty may limit Australia's taxing right on an asset that passes the domestic TAP test. From 1 October 2026, where an agreement adopts the Australian law meaning of real property, immovable property or land, use the taxable Australian real property definition under s 3(5) of the International Tax Agreements Act 1953.

## Sources

- ITAA 1997 Division 855 (non-resident CGT)
- Tax Administration Act 1953, Schedule 1, Subdivision 14-D (FRCGW)
- [ATO Foreign residents and capital gains tax](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/cgt-discount-for-foreign-residents) (read 2026-11-22)
- [ATO Foreign resident capital gains withholding overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview) (read 2026-11-22)
- [Treasury Laws Amendment (2024 Tax and Other Measures No. 1) Act 2024 Schedule 1](https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/pdf) and [2017 FRCGW Act Schedule 1](https://www.legislation.gov.au/C2017A00057/asmade/2017-06-22/text/original/pdf) (read 2026-11-25)
- [ATO Tax rates: foreign resident](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-foreign-residents) (read 2026-11-22)
- [ITAA 1997, Div 855 from 1 October 2026](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html) (read 2026-11-22)
- [Treasury Laws Amendment (Strengthening Accountability for Tax Adviser Misconduct and Other Measures) Act 2026, commencement and Schedules 2 and 3](https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html) (read 2026-11-22)
- [TAA 1953 Schedule 1, Subdivision 14-D and Division 18](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) (read 2026-11-22)
- [ATO guidance for non-IARPI notices](https://www.ato.gov.au/api/public/content/0-2f5524ea-eb96-464a-b5e5-b3779f4e2379) (read 2026-11-22)
- [Income Tax Rates Act 1986, Schedule 7 Part II](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) (read 2026-11-22)
- [Taxation Laws (Requirement to Lodge a Return for the 2026 Year) Instrument 2026, ss 6 to 8](https://www.legislation.gov.au/F2026L00618/asmade/2026-05-22/text/original/epub/OEBPS/document_1/document_1.html) (read 2026-11-22)
- [Treasury treaty list](https://treasury.gov.au/tax-treaties/income-tax-treaties) (read 2026-11-22)

> **Working paper only.** The TAP classification requires analysis of the company's asset composition by market value — not book value. Engage a qualified Australian tax adviser for transaction-specific advice.
