---
name: pk-cgt
description: Use for pakistan capital gains by asset and acquisition date. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 1.1
type: computation
---

# Pakistan capital gains by asset and acquisition date v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Pakistan capital-gains working papers for normal tax year 2026 (1 July 2025-30 June 2026). Separate s.37A securities, s.37(1 A) immovable property and other s.37 capital assets. This is the Finance Act 2025 filing-cycle law; later disposals need later law. Business stock, depreciable/amortisable assets and specified personal-use exclusions need their actual head of income, not a capital-gains label by default. [ITO ss.37/37 A](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

Quick answer: acquisition date and asset class select the rate regime; a universal 15% filer rate is wrong. Securities acquired from 1 July 2024 require ATL status at **both acquisition and disposal** for the 15% branch. New-property ATL treatment uses disposal status. [First Schedule Divisions VII/VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Ask the client first

Obtain name/NTN/CNIC/residence, taxpayer type, exact acquisition/disposal dates, asset description, acquisition basis/transfer history, consideration and evidenced acquisition/disposal/improvement costs, any costs deducted or otherwise deductible, purchase-date bank-transfer evidence, currency evidence, dated ATL evidence at each relevant date, brought-forward losses by class/year and prior claims. For securities obtain broker/CDC/NCCPL records, market/off-market/IPO route and company debt/fund status. For property obtain title/allotment/deed, locality-specific operative FBR valuation and fallback authority evidence, actual s.236C/s.236K certificates and wealth reconciliation. Gift/inheritance needs transferor basis/relationship evidence rather than an automatic market-value uplift. Non-residents need source and actual treaty/protocol analysis.

## Rates, bands and thresholds

### Securities under s.37A: tax-year 2026

| Acquisition/holding/category | Rate and conditions | Official source |
|---|---|---|
| Acquired from 1 July 2024 | 15% if ATL at acquisition **and** disposal; otherwise individual/AOP Division I or company Division II rates, with 15% floor for individual/AOP | [First Schedule Part I Div VII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Acquired 1 July 2022-30 June 2024; holding up to 1 year | 15% | [Div VII table](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Same acquisition window; over 1 to 2 years | 12.5% | [Div VII table](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Same; over 2 to 3 years | 10% | [Div VII table](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Same; over 3 to 4 years | 7.5% | [Div VII table](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Same; over 4 to 5 years | 5% | [Div VII table](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Same; over 5 to 6 years | 2.5% | [Div VII table](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Same; over 6 years | 0% | [Div VII table](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Acquired 1 July 2013-30 June 2022 | 12.5%, subject to specified category exceptions | [Div VII proviso(i)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Acquired before 1 July 2013 | 0%, subject to specified category exceptions | [Div VII proviso(ii)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| PMEX-member future commodity contracts | 5% | [Div VII row 8](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Company debt securities | Company Division II rate, not ordinary 15% stock rate | [Div VII proviso](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Fund/collective-investment/REIT redemption | Individual/AOP 15% stock/other funds; company 15% stock,25% other; stock-fund dividend-vs-gain proviso and pre 1 July 2024 over 6 year no-deduction proviso apply only to specified schemes | [Div VII final provisos](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

Section 37 A includes public-company shares, PTC vouchers, modaraba certificates, redeemable capital, debt securities, ETF units and derivatives; public-company status is tested at disposal. Banks and insurance companies are excluded. Listed shares sold outside a registered exchange **and not settled through NCCPL**, and specified IPO disposals without details supplied to NCCPL, go to s.37. Do not assume all listed-company disposals are covered by the collection mechanism. [s.37A(1)-(3 B)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

### Immovable property under s.37(1 A)

For property acquired **on or before 30 June 2024**, keep the asset-specific holding ladder. A dash below means use the already-reached 0% branch for the relevant property class, not a new rate.

| Exact holding period | Open plot | Constructed property | Flat | Source |
|---|---|---|---|---|
| Up to 1 year | 15% | 15% | 15% | [First Schedule Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Over 1 to 2 years | 12.5% | 10% | 7.5% | [Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Over 2 to 3 years | 10% | 7.5% | 0% | [Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Over 3 to 4 years | 7.5% | 5% | - | [Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Over 4 to 5 years | 5% | 0% | - | [Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Over 5 to 6 years | 2.5% | - | - | [Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Over 6 years | 0% | - | - | [Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

For property acquired **from 1 July 2024**,15% applies to persons on ATL at disposal. Other individual/AOP disposals use Division I rates with a 15% gain floor; companies use Division II. Do not paste the old holding ladder onto new acquisitions, or double CGT merely because a separate advance-tax table has non-ATL rates. [Div VIII](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## The method, step by step

1. Determine chargeability and the actual asset/head before selecting a rate. Section 37 uses consideration less cost; s.37A is a separate block. General s.37(3)'s three-quarter long-term-gain reduction was **omitted in 2022** and cannot be revived from a footnote. [ss.37/37 A](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
2. Establish cost under s.76: purchase consideration, qualifying incidental acquisition/disposal costs and alteration/improvement costs; its incidental/improvement rule excludes amounts already fully allowed. The broader s.37(4) screen excludes expenditure deductible under another Chapter III provision, whether claimed or not, and expenditure referred to in s.21. Also test s.75A: purchases of immovable property with fair market value over 5,000,000 or other assets over 1,000,000 require the specified crossed bank instruments showing account-to-account transfer; the Finance Act 2025 adds digital means. Failure denies the amount as s.76 cost (and ss.22-25 allowances). For this purchase-threshold test alone, property value is the **higher** of the Board's s.68(4) notified value and provincial stamp-duty value; distinguish the general disposal-valuation fallback in step 3. Apply the purchase-date law, not the 2025 digital addition retrospectively. Repairs/capital enhancement and missing basis require evidence, not an invented estimate. Special produced/constructed assets, business-use transitions, foreign-currency borrowing, partial disposals and grants have their own cost branches. [ss.37(4),75A/76](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
3. Consideration under s.77 includes in-kind value and the higher fair-market-value rule. For property, s.68(4)-(6) uses the FBR-notified locality value; only where the Board has not determined that area's value does the statutory provincial/stamp-duty fallback apply. It is not always the maximum of FBR and DC values. Non-arm's-length acquisitions/disposals use s.78's corresponding fair-value treatment. [ss.68/77/78](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
4. Compute each date/category separately, test losses/exemptions, and reconcile collection to actual certificates. Do not blindly total gains and apply 15%. For general other capital assets use the appropriate taxpayer's normal rate/head; unlisted shares also require specific s.37(6)-(10) withholding/information analysis. Obtain that procedure before completing an unlisted transfer.

## Boundary and exception table

| Situation | Treatment and boundary |
|---|---|
| s.37A securities loss | Ring-fenced to chargeable s.37A securities gains; unabsorbed losses from tax year 2019 onward carry forward at most 3 immediately succeeding tax years. [s.37A(5)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| General capital loss | No set-off against other income heads; at most 6 immediately succeeding tax years, earliest first; no carry-back supplied. Loss on an exempt gain asset is not deductible. [ss.38/59](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Collectibles | s.38(5) denies loss recognition for art, jewellery, rare manuscripts/books, stamps/first-day covers, coins/medallions and antiques; do not assume every economic loss is deductible. [s.38(5)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Death transmission to executor/beneficiary; gift to qualifying relative | s.79 non-recognition and carryover character/cost conditions, not a universal market-value step-up. Later sale remains a separate event. [s.79(1)(b)-(c),(3)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Spousal separation; compulsory acquisition/reinvestment; liquidation; AOP dissolution | Preserve s.79's particular branches,1 year like-kind replacement rule and non-resident-acquirer restriction for(d)-(f); obtain facts before relief. [s.79](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Personal residence | No general area/value-limited capital-gains exemption is established here. s.159(1 B)'s 236 C certificate requires the stated residential history/wealth-record conditions for 15 years and is not itself a blanket s.37 exemption. [s.159(1 B)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Non-resident/land-rich indirect transfer | Apply Pakistan-source and actual treaty/indirect-transfer law; do not assume every overseas share sale is outside Pakistan. Refer cross-border/treaty and s.101A cases. |
| Crypto | Economic reconciliation only until tax classification is supported; load `pk-crypto-tax` for current PVARA/SBP framework, not an alleged universal FBR 2023 capital-gains ruling. |

## Worked cases

### Mr. Ahmed: preserve the different acquisition regimes

Mr. Ahmed, Karachi resident, sells Co. X 10,000 shares acquired August 2024 after 11 months and Co. Y 5,000 shares acquired January 2023 after about 30 months in tax year 2026. Assume actual dates support those bands, listed/exchange/NCCPL scope, no loss offsets, allowable evidenced brokerage and ATL at both required Co. X dates. The given sale brokerage 22,500/11,000 equals 0.5% of each sale. Rule 13 N(8) also adds 0.5% of acquisition consideration for these assumed client market trades; actual brokerage is replaced by the prescribed allowance, not deducted again.

```oa-check
name: Mr. Ahmed Co.X and Co.Y
inputs:
  x_proceeds: 4500000
  x_cost: 3000000
  x_brokerage: 22500
  y_proceeds: 2200000
  y_cost: 1800000
  y_brokerage: 11000
steps:
  - x_gain: x_proceeds - x_cost - x_brokerage - x_cost * 0.005
  - y_gain: y_proceeds - y_cost - y_brokerage - y_cost * 0.005
  - aggregate_gain: x_gain + y_gain
  - x_tax: x_gain * 0.15
  - y_tax: y_gain * 0.10
  - combined_tax: x_tax + y_tax
expected:
  x_gain: 1462500
  y_gain: 380000
  aggregate_gain: 1842500
  x_tax: 219375
  y_tax: 38000
  combined_tax: 257375
```

The old 279,975 result used 15% on both gains and omitted the acquisition-side prescribed allowance; the conditional corrected result is 257,375. Reconcile to actual NCCPL certificate rather than assert the collection equals an unverified example.

### Mrs. Khan: older open-plot ladder

Mrs. Khan, Lahore resident filer, acquired the DHA Lahore residential plot in September 2022 and sells in March 2026, over 3 and at most 4 years. The given declared 25,000,000 is below an assumed operative FBR-notified 28,000,000 locality value; obtain that actual notification. The 12,000,000 purchase basis is assumed legally eligible, including original crossed-bank payment records meeting the September 2022 purchase-date s.75A requirements; expense receipts alone do not establish this. Costs 450,000 acquisition and 550,000 disposal are assumed evidenced, eligible under ss.37(4)/76 and not deductible elsewhere or barred by s.21. Missing bank or cost evidence leaves this calculation pending.

```oa-check
name: Mrs. Khan older plot
inputs:
  declared_proceeds: 25000000
  supported_fbr_value: 28000000
  purchase_cost: 12000000
  acquisition_costs: 450000
  disposal_costs: 550000
steps:
  - deemed_proceeds: max(declared_proceeds, supported_fbr_value)
  - gain: deemed_proceeds - purchase_cost - acquisition_costs - disposal_costs
  - capital_gains_tax: gain * 0.075
expected:
  deemed_proceeds: 28000000
  gain: 15000000
  capital_gains_tax: 1125000
```

Seller 236 C advance tax and buyer 236 K advance tax are separate. Mrs. Khan may only reconcile her supported seller credit, not the buyer's credit; actual collection and refund/adjustment law must be checked.

### Mr. Iqbal: preserve crypto facts without inventing a tax classification

Mr. Iqbal, a resident filer, acquired BTC in 2023 for 2,000,000 and sells in tax year 2026 through an offshore exchange for 5,500,000, repatriating to a Pakistan bank. Fees 50,000 are evidenced case inputs.

```oa-check
name: Mr. Iqbal economic crypto gain only
inputs:
  proceeds: 5500000
  cost: 2000000
  fees: 50000
steps:
  - economic_gain: proceeds - cost - fees
expected:
  economic_gain: 3450000
```

This 3,450,000 economic gain is **not** a cleared s.37 taxable gain or tax figure. Regulatory access, source, classification, valuation, foreign assets and reporting require the current-law analysis in `pk-crypto-tax` and specialist review.


### NCCPL computation and collection rules

Rule 13 N(8) uses 0.5% on both disposal consideration deduction and acquisition-cost addition for client market trades,0.25% for broker proprietary trades, in lieu of incidental expenses; open-ended funds and PMEX future contracts are excluded. Rule 13 N(5) uses FIFO on aggregate UIN inventory, with market-transactions-first and same-day/same-contract average-method exceptions. Preserve allowed NCCPL leveraged financing separately. Rule 13 N(10) collects monthly after loss/previous-collection adjustments, rather than certifying every trade is taxed by netting its settlement proceeds. Rule 13 N(12) permits dissatisfied investors to recompute and lodge a refund claim with the Commissioner after filing, and(15)requires annual certificate within 45 days of financial-year end. Rule 13 N(5 A)'s year-end ATL collection-adjustment proviso must be reconciled with the later First Schedule's acquisition/disposal charge conditions; it does not authorize ignoring statutory eligibility. [Rules 13 N(5)-(15)](https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf).

## Deadlines and filing

Reconcile the appropriate IRIS return/capital-gains working papers, wealth statement where required, certificates and payments. Section 118 ordinary individual/AOP deadline is 30 September following year end, subject to actual extension; a company whose tax year ends January-June normally uses 31 December, otherwise 30 September. Do not promise all companies a universal 31 December date or assert the ordinary date is the actual extended 2026 filing deadline. [ss.116/118/119](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

Obtain actual NCCPL collection/computation rules and annual certificate for covered trades; verify off-market/IPO exclusions. Obtain actual registrar/society/collecting-person 236 C/236 K evidence for property; do not assume the buyer's bank always collects. Retain s.174 records for 6 years after tax-year end, and longer for pending proceedings/statutory exceptions; retain old basis/title evidence needed for a later disposal. [s.174](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Penalties and interest

Default, omitted gains, wrong credits and late payment/return require the actual ss.182/205 law and notice facts. No unsourced fixed capital-gains penalty or automatic retrospective ATL refund is supplied. Reconcile actual credits and lawful adjustment/refund under ss.168/170; collection is not evidence of final chargeability.

## When to refuse or refer

Retain refusal/referral for unknown cost/date/class/status, undocumented gift/inheritance basis, AOP-interest disposal, trading/business assets, binding crypto positions, cross-border treaties, mineral/oil/petroleum rights, trusts/estates, material valuation disputes and an unverified period's law. Do not invent a shorter holding period, substitute the highest valuation blindly, or finalise at a guessed non-filer rate. Missing facts stay pending. Sector-specific government bonds, original-allottee/first-sale concessions, special housing and connected-person loss restrictions need the operative provision before relief; they are not discarded topics.

For the actual tax-year-2026 filing cycle, FBR Circular 04 of 2026-27 dated 15 October 2026 extends the filing date to **31 October 2026** for persons originally due 30 September 2026 and previously extended to 15 October. It does not extend every company return. Apply any individual further order only on its evidence; this circular does not itself state a general payment extension. [Official circular](https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf), read and scanned page inspected 2026-11-14.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Circular 04 of 2026-27, 15 October 2026, the 31 October extension for the original 30 September cohort; scanned signed page inspected | https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf | 2026-11-14 |
| Read for Income Tax Rules 13 N(3)-(15), including FIFO/expenses/monthly collection/recomputation/annual certificate, on 2026-11-14 | https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf | 2026-11-14 |
| Read for ITO ss.37/37 A/38/59,68,76-79,159(1 B),174 and First Schedule Part I Div VII/VIII with adjacent conditions and historical omission footnotes | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |
| Read for ss.37(4),75A(1)-(3) with neighboring cost provisions and Finance Act 2025 digital-means footnotes; purchase-date conditions distinguished | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-15 |
| Read for ordinary return/wealth/date framework ss.116/118/119; dated extension handled separately above | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |

Not yet confirmed: case-specific NCCPL discrepancies/transactions and actual collection records; each client's operative locality valuation and certificates; full s.37(6)-(10) transfer procedure; original-allottee/first-sale/government-security or specific housing relief, connected-person loss restrictions and each applicable treaty/indirect-transfer result; any further individual filing orders and later-period rate changes. The former blanket self-occupied-residence exemption, alleged universal 2023 crypto classification, weekly ATL/automatic no-refund promises and flat 15% for every acquisition are not usable instructions.
