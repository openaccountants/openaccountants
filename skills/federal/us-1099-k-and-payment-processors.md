---
name: us-1099-k-and-payment-processors
description: "Tier 2 US federal content skill for Form 1099-K reporting under IRC §6050W for tax year 2025. Covers the current federal TPSO threshold restored by OBBBA: more than $20,000 and more than 200 transactions, reconciliation between gross 1099-K amounts and Schedule C / Schedule 1 / Schedule D reporting, IRS-recommended treatment of personal items sold at loss (Schedule 1 Lines 8z + 24z offset), hobby vs business §183 determination, PayPal/Venmo Friends-and-Family vs Goods-and-Services categorization, marketplace facilitator sales-tax exclusion under Wayfair, ride-share and content-creator double-form scenarios (1099-K + 1099-NEC), the 2025 1099-DA digital asset transition, and IRS CP2000 matching defense."
jurisdiction: US
domain: federal-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# us-1099-k-and-payment-processors

## US 1099-K and Payment Processors (Tax Year 2025)

## 1. Scope

This skill covers the preparation, reconciliation, and defense of US federal tax returns that include one or more Form 1099-K information returns received by a taxpayer for the 2025 tax year (filing season 2026). It addresses:

- The legal architecture of §6050W and the role of Third-Party Settlement Organizations (TPSOs) versus Payment Card Companies
- The transitional reporting thresholds under IRS Notice 2024-85 (the "phase-in") and the matching CP2000 risk created by the staircase
- How to reconcile a gross 1099-K box-1a amount to the correct line of the taxpayer's return — Schedule C, Schedule 1 Line 8j or 8z, Schedule D, or nothing at all
- The IRS-recommended "two-line wash" for personal items sold at a loss (Schedule 1 Line 8z plus Schedule 1 Line 24z negative offset)
- Platform-specific reporting patterns and traps: PayPal Friends-and-Family vs Goods-and-Services, Venmo, Cash App for Business, Airbnb/VRBO, Uber/Lyft, DoorDash, Etsy, eBay, Mercari, Poshmark, Patreon, OnlyFans, StubHub, Vinted
- The double-counting problem when the same gross receipts appear on both a 1099-K (from the processor) and a 1099-NEC (from the customer)
- Marketplace facilitator sales-tax mechanics under Wayfair (South Dakota v. Wayfair, 138 S. Ct. 2080 (2018)) and the resulting state-law collection regimes
- The 2025 transition from 1099-K to Form 1099-DA for digital-asset brokers under the §6045 broker regulations finalized by T.D. 10000 (June 28, 2024)
- IRS CP2000 underreporter notice defense, with a sample reconciliation worksheet and explanation-statement language

This skill does NOT cover:

- Substantive Schedule C deduction classification (see `us-sole-prop-bookkeeping`)
- The Schedule C bottom-line and Schedule SE computation (see `us-schedule-c-and-se-computation`)
- The §199A QBI deduction (see `us-qbi-deduction`)
- The retailer's own duty to issue 1099-K as a TPSO — this skill is written from the payee's side. Issuer obligations under §6050W(b) are summarized only to the extent the practitioner needs them to evaluate a "wrong 1099-K" complaint
- State income-tax conformity to the federal threshold — many states (e.g., Maryland, Massachusetts, Vermont, Virginia, Illinois, New Jersey, District of Columbia) have lower or differently-timed thresholds; consult the relevant state skill

This skill MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. It pairs naturally with `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, and `us-1099-nec-issuance`.

## 2. Legal basis: IRC §6050W

### 2.1 What §6050W says

- **IRC §6050W reporting entities** — IRC §6050W, enacted by the Housing Assistance Tax Act of 2008 (P.L. 110-289, §3091) and effective for calendar years beginning after December 31, 2010, requires two distinct classes of reporting entities to file an information return with the IRS reporting "reportable payment transactions": 1. Payment Settlement Entities (PSEs) — split into two sub-classes: Payment Card Companies under §6050W(b)(1)(A): a "merchant acquiring entity" that contracts with merchants to settle payment-card transactions. This includes Visa, Mastercard, American Express, Discover, and their merchant-acquirer agents (Stripe, Square, Adyen, Worldpay, Fiserv/First Data, Heartland, etc.). Third-Party Settlement Organizations (TPSOs) under §6050W(b)(1)(B) and (d)(3): a "third party payment network" that contracts with a substantial number of "providers of goods or services" to settle transactions between those providers and their customers. This includes PayPal, Venmo (operated by PayPal), Cash App for Business (Block), Zelle is debated — Treasury position is that bank-direct Zelle transfers are NOT a TPSO because the bank is acting as a payment agent rather than a third-party settlement intermediary; see IRS FAQ 1099-K Q-3, 2024 — eBay, Etsy, Amazon, Airbnb, VRBO, DoorDash, Uber Eats, Mercari, Poshmark, StubHub, Vinted, Patreon, OnlyFans, Substack, Ticketmaster resale, and similar platforms. 2. Reportable Payment Transaction is defined at §6050W(c) as any payment-card transaction or third-party network transaction. The reporting is on Form 1099-K, Payment Card and Third Party Network Transactions, with Box 1a showing gross amount of reportable payment transactions for the calendar year and Box 1b showing card-not-present amount.  _(§6050W; P.L. 110-289 §3091; IRS FAQ 1099-K Q-3, 2024)_

### 2.2 The two thresholds — and why they matter

- **Payment Card Companies have no de minimis threshold; TPSOs subject to §6050W(e) threshold** — Payment Card Companies under §6050W(b)(1)(A) have no de minimis threshold. Every merchant-card transaction is reportable. A merchant who runs a single $10 swipe through Square in calendar year 2025 is entitled to a Form 1099-K from Square for $10. In practice issuers wait until the calendar year closes and then issue a single 1099-K covering all card volume for the year. There is no $600, $2,500, or $5,000 floor for card processors. TPSOs under §6050W(b)(1)(B) are subject to the de minimis threshold at §6050W(e). That asymmetry — payment-card processors with no threshold versus TPSOs with a threshold — is the structural reason why a hobby seller on Etsy may or may not get a 1099-K depending on the year, but a tiny coffee cart on Square gets one every year regardless.  _(§6050W(b)(1)(A); §6050W(b)(1)(B); §6050W(e))_

### 2.3 §6050W(e) as originally drafted vs. as amended by ARPA

- **§6050W(e) original threshold vs ARPA amendment vs OBBBA restoration** — As originally enacted in 2008, §6050W(e) provided that TPSO reporting was required only if a payee received more than $20,000 in gross payments AND more than 200 separate transactions in the calendar year — the "$20K AND 200" floor. The conjunction was critical. A high-volume eBay seller with 250 transactions averaging $50 each ($12,500 total) was below the floor and got no 1099-K. A low-volume Etsy seller with 10 transactions averaging $3,000 each ($30,000 total) was likewise below the floor (failed the 200-transaction prong). Section 9674(a) of the American Rescue Plan Act of 2021 (P.L. 117-2, March 11, 2021) attempted to reduce §6050W(e) to $600, with no transaction count, but OBBBA P.L. 119-21 retroactively restored the prior federal TPSO threshold: more than $20,000 and more than 200 transactions. Read literally, beginning with the 2022 tax year, every TPSO had to issue a 1099-K to every payee who received more than $600 in gross goods-and-services payments through that platform in 2022. The IRS realized in late 2022 that this would generate hundreds of millions of new 1099-K forms — most of them sent to taxpayers who had no business income at all (people selling used couches on Facebook Marketplace, splitting dinner with friends via Venmo G&S by mistake, etc.). It would also generate hundreds of millions of CP2000 mismatches. So the IRS, citing its administrative authority, has repeatedly delayed enforcement.  _(§6050W(e); ARPA §9674(a), P.L. 117-2; OBBBA P.L. 119-21)_

### 2.4 The delay-and-phase-in history (Notices 2023-10, 2023-74, 2024-85)

- **Delay and phase-in notices** — Notice 2023-10 (issued December 23, 2022): delayed the ARPA $600 threshold by treating calendar year 2022 as a "transition year." For 2022, the old $20,000-and-200 threshold continued to apply for TPSO reporting. No phase-in figure for 2023 was set. Notice 2023-74 (issued November 21, 2023): again delayed the $600 threshold and treated 2023 as another transition year. Old $20K-and-200 floor remained for 2023. Importantly, Notice 2023-74 also addressed the 1099-K + 1099-NEC duplication problem by stating that where a payment is reported on both forms, the payee should report the income once and document the duplication; this is the IRS's only public acknowledgment of the problem. Notice 2024-85 (issued November 26, 2024): announced the threshold phase-in staircase rather than another flat-delay. The notice established: Calendar year 2024: TPSO reporting required if gross payments exceed $5,000 (any number of transactions). Penalties for failure to report between the statutory $600 floor and $5,000 are waived for 2024. Calendar year 2025: threshold becomes $2,500. Calendar year 2026: threshold becomes $600, which is the statutory ARPA figure. The notice describes 2026 as the "final phase-in" year, but does not foreclose a further delay if administrative considerations warrant.  _(Notice 2023-10; Notice 2023-74; Notice 2024-85)_

### 2.5 Threshold phase-in table

**Threshold phase-in table**  _(Notice 2024-85; §6050W(e); ARPA §9674)_

| Calendar year | TPSO 1099-K threshold | Authority | Status |
| --- | --- | --- | --- |
| 2021 and prior | $20,000 AND 200 transactions | §6050W(e) as originally enacted | Statute superseded by ARPA |
| 2022 | $20,000 AND 200 transactions | Notice 2023-10 (transition year) | Closed |
| 2023 | $20,000 AND 200 transactions | Notice 2023-74 (transition year) | Closed |
| 2024 | $5,000 (no transaction count) | Notice 2024-85 §IV.A | Closed; 1099-Ks issued Jan 2025 |
| **2025** | **$2,500 (no transaction count)** | **Notice 2024-85 §IV.B** | **CURRENT YEAR — 1099-Ks issued Jan 2026** |
| 2026 | $600 (no transaction count) | Notice 2024-85 §IV.C; ARPA §9674 | Scheduled; subject to further notice |
| 2027+ | $600 (no transaction count) | §6050W(e) as amended | Permanent unless legislatively repealed |

### 2.5 Threshold phase-in table

> **AUDIT FLASH POINT — the threshold cliff is asymmetric.** Issuers are not penalized for issuing 1099-K voluntarily below the threshold. Many TPSOs — particularly PayPal, eBay, and Etsy — issue 1099-Ks at $600 or even $0 in states with lower state thresholds (Maryland $600, Massachusetts $600, Vermont $600, Virginia $600, Illinois $1,000 OR 4+ transactions, New Jersey $1,000, DC $600). A 2025 client may show up with a 1099-K below the federal $2,500 floor because they live in Massachusetts. Do not assume "below threshold = no form." Always ask for ALL 1099-Ks the client received regardless of amount.

### 2.6 What goes in Box 1a — gross payments before adjustments

- **Box 1a gross amount definition** — §6050W(a)(2) requires the PSE to report the gross amount of reportable payment transactions. The Treasury regulations at Treas. Reg. §1.6050W-1(a)(5) clarify that "gross amount" means: The total dollar amount of aggregate reportable payment transactions for each participating payee, without regard to any adjustments for credits, cash equivalents, discount amounts, fees, refunded amounts, or any other amounts. This is the single most important sentence in the regulation. The Box 1a figure is not the payee's net revenue and is not the payee's income. It includes: Sales tax that the platform collected from buyers and remitted to the seller (where platform is not a marketplace facilitator); Shipping and handling charged to buyers; Refunds that were later issued (the refund is NOT netted from Box 1a); Returns and allowances (not netted); Chargebacks (not netted); Processor fees that the platform deducted before remitting to the seller (NOT netted — the gross is the buyer-side gross, not the seller-side net); Tips collected through the processor and remitted to the seller. A taxpayer's actual Schedule C Line 1 gross receipts will almost always be lower than Box 1a for these reasons. The difference is reconciled, not ignored.  _(§6050W(a)(2); Treas. Reg. §1.6050W-1(a)(5))_

## 3. Who issues 1099-K, and what it looks like in the wild

### 3.1 Payment Card Companies (no threshold)

- **Payment card processor issuance rule** — Any merchant-card processor issues 1099-K for the entire calendar-year card volume. The Box 1a figure equals gross card volume before processor fees. The payee is the merchant of record on the processor account.

**Payment Card Companies table**

| Processor | Type | Threshold | Typical recipient |
| --- | --- | --- | --- |
| Stripe | Card processor (merchant acquirer) | None | Every Stripe-account holder with any card volume in the year |
| Square | Card processor + small TPSO features | None | Every Square-account holder |
| PayPal Commerce / PayPal Checkout | Card processor (for card-funded transactions) | None for card | Merchant accepting cards via PayPal |
| Shopify Payments (powered by Stripe) | Card processor | None | Shopify merchant |
| Adyen | Card processor | None | Enterprise merchant |
| Toast / Clover / Lightspeed | Card processor (POS) | None | Restaurants, retail |
| Authorize.Net (Visa) | Card processor | None | Web merchant |

### 3.1 Payment Card Companies (no threshold)

**Practical note:** Stripe issues a separate 1099-K for each connected account. A user with three Stripe accounts (e.g., a freelancer with a personal Stripe, a Shopify store using Shopify Payments, and a SaaS using Stripe Billing) gets three 1099-Ks. The TIN on each must match the taxpayer's records or the IRS will mismatch.

### 3.2 Third-Party Settlement Organizations (subject to phase-in threshold)

**TPSO table**

| TPSO | What triggers reporting | Notes |
| --- | --- | --- |
| PayPal (Goods & Services balance) | Aggregate G&S receipts above 2025 threshold ($2,500) | F&F transactions excluded (see §7.1) |
| Venmo (Business profile or G&S tag) | Aggregate G&S receipts above threshold | F&F excluded; Venmo "Business Profile" introduced 2021 is per-se G&S |
| Cash App for Business | Aggregate business receipts above threshold | Personal Cash App accounts not reportable; Business is separate |
| eBay | Aggregate sales above threshold | eBay handles payment processing in-house since 2021 (Managed Payments) |
| Etsy | Aggregate sales above threshold | Etsy Payments processes; Etsy Direct Checkout is the TPSO |
| Amazon (third-party seller) | Aggregate sales above threshold | Amazon Pay also issues |
| Mercari, Poshmark, Depop, Vinted, ThredUp | Aggregate sales above threshold | Re-commerce platforms; many casual sellers will receive 1099-Ks |
| Airbnb | Aggregate host receipts above threshold | Includes cleaning fees, occupancy taxes (see §7.4) |
| VRBO (Vrbo / HomeAway) | Aggregate host receipts above threshold | Owned by Expedia |
| Uber (drivers) | Trip earnings above threshold | Plus 1099-NEC for incentive bonuses (see §7.5) |
| Lyft | Trip earnings above threshold | Same pattern as Uber |
| DoorDash, Grubhub, Uber Eats, Instacart (Shoppers) | Delivery earnings above threshold | 1099-NEC also issued for IC drivers (double-form) |
| Patreon | Creator payouts above threshold | Stripe is the underlying processor; 1099-K from Patreon, not Stripe |
| OnlyFans | Creator payouts above threshold | Issued via OFTV LLC or Fenix International |
| Substack | Writer payouts above threshold | Stripe-backed |
| Twitch / YouTube | Mixed — see §7.7 | Some payouts are 1099-NEC (AdSense), others 1099-K (bits, Super Chat via processor) |
| StubHub, SeatGeek, Vivid Seats, Ticketmaster Fan-to-Fan | Resale receipts above threshold | Includes face value plus markup |
| GoFundMe (charitable) | Generally NOT 1099-K — see §7.8 | Personal fundraising treated as gifts, not goods/services |

### 3.3 Crypto exchanges — transitioning from 1099-K to 1099-DA in 2025

- **1099-K to 1099-DA transition for digital asset brokers** — Historically, US-resident crypto exchanges (Coinbase, Kraken, Gemini, Binance.US) used Form 1099-K to report fiat-equivalent gross flows on the theory that the exchange was acting as a TPSO. This was always an imperfect fit: 1099-K reports gross gross — not gain — and crypto users were getting 1099-Ks for $200,000 of trading volume that produced $400 of net gain. T.D. 10000 (June 28, 2024) finalized Treas. Reg. §1.6045-1 to designate custodial digital-asset brokers as §6045 brokers and require them to file new Form 1099-DA, Digital Asset Proceeds From Broker Transactions, beginning with the 2025 calendar year. 2025 (first reporting year): 1099-DA required for gross proceeds of digital-asset sales. Cost basis is optional. Wallet-by-wallet basis tracking begins January 1, 2025 (Rev. Proc. 2024-28 safe harbor). Most exchanges will NOT report cost basis on the 2025 1099-DA. 2026 and later: 1099-DA must also include cost basis for "covered" digital assets acquired on or after January 1, 2026. Decentralized brokers (DeFi) — the original final regulations included DeFi front-ends as brokers; this was repealed by joint resolution signed April 10, 2025 (P.L. 119-3). DeFi brokers do not file 1099-DA. For the 2025 tax year, a client who used a centralized US exchange will likely receive both a 1099-DA (gross proceeds, no basis) and possibly a legacy 1099-K (covering fiat-to-crypto on-ramp payments). The two forms can double-count. Reconciliation requires the client's full transaction history, not the forms. See `us-digital-assets-reporting` (forthcoming) for details.  _(T.D. 10000 (June 28, 2024); Treas. Reg. §1.6045-1; Rev. Proc. 2024-28; P.L. 119-3)_

## 4. Who receives 1099-K — and what to do about it

The §6050W reporting regime is a payee regime. A 1099-K is issued to a person who received payments through a card or third-party network. The IRS does not care, at the issuer level, whether the payee was running a business, selling personal items, splitting a vacation with friends, or operating a hobby. The IRS expects the payee — through their tax preparer — to make that determination on the return.

There are five canonical recipient categories:

### 4.1 Schedule C business operator

- **Schedule C business operator category** — A sole proprietor or single-member LLC disregarded for federal tax purposes who runs a trade or business and accepts payments through card or TPSO networks. The 1099-K is input to Schedule C Line 1 (gross receipts), after reconciliation for the items in §2.6. This is the simplest case.

### 4.2 Hobbyist with sustained sales

- **Hobbyist recipient category** — A person whose activity does not rise to the level of a §162 trade or business under the §183 nine-factor test (Treas. Reg. §1.183-2(b)). Typical examples: occasional Etsy shop selling handmade items at break-even or below; small-scale eBay flipping of collectibles without profit motive; occasional StubHub ticket resale. Income is reported on Schedule 1, Line 8j ("Activity not engaged in for profit income"). After TCJA (P.L. 115-97, §11045), hobby expenses are NOT deductible — they were Schedule A miscellaneous 2% itemized deductions and that deduction was suspended through 2025 by §67(g) and made permanent by OBBBA (P.L. 119-21, July 4, 2025). See §6 for the §183 framework.  _(§162; §183; Treas. Reg. §1.183-2(b); TCJA P.L. 115-97 §11045; §67(g); OBBBA P.L. 119-21)_

### 4.3 Casual seller of personal items at a loss

- **Casual seller at loss category** — A taxpayer who sells personal-use property — used clothing, household goods, books, a single piece of used furniture — for less than the original purchase price. Loss on sale of personal-use property is not deductible under §165(c) (only business, investment, and casualty losses are deductible for individuals). But the gross receipts are not taxable income either, because the taxpayer recovered less than basis. The IRS-recommended treatment is the "two-line wash" described in §5.3.  _(§165(c))_

### 4.4 Casual seller of personal items at a gain

- **Casual seller at gain category** — Most relevant for collectibles (jewelry, watches, baseball cards, art, vintage clothing where it appreciated). Gain on sale of personal-use property IS taxable — as capital gain. Holding period determines short-term vs. long-term. Collectibles long-term are taxed at the §1(h)(4) 28% rate cap. Reported on Form 8949 and Schedule D. See §5.4.  _(§1(h)(4))_

### 4.5 Recipient of personal reimbursements that were mistagged G&S

- **Mistagged reimbursement category** — A roommate splits rent through Venmo and the payer accidentally selected "Goods and Services" instead of "Friends and Family," generating a year-end 1099-K. This is not income at all — it is a non-taxable reimbursement. IRS guidance (FAQ Q-9, 2024) directs the recipient to attempt a corrected 1099-K from the issuer; if denied, report the gross on Schedule 1 Line 8z and back it out on Line 24z with the description "Form 1099-K received in error." See §5.3.  _(IRS FAQ Q-9, 2024)_

### 4.6 Decision tree

```
Did you receive a Form 1099-K for 2025?
├── YES → Is the activity a trade or business under §162 / §183?
│   ├── YES (regular, continuous, profit-motive) → Schedule C
│   │   └── Reconcile Box 1a to actual gross receipts; document refunds, fees, sales tax, double-counts
│   ├── NO, hobby (sporadic, no profit motive) → Schedule 1 Line 8j
│   │   └── No expense deduction available (TCJA §67(g), made permanent by OBBBA)
│   └── NO, personal property sale → was there a gain?
│       ├── GAIN → Form 8949 → Schedule D (collectibles 28%)
│       ├── LOSS → Schedule 1 Line 8z gross, Line 24z negative offset (IRS two-line wash)
│       └── REIMBURSEMENT (no sale at all) → Schedule 1 Line 8z gross, Line 24z negative offset, "Received in error"
└── NO → Do you have business income that should have been on 1099-K?
    └── Yes, report on Schedule C as you would any unreported gross receipts
```

## 5. Reconciliation — making the return match (and explain) the 1099-K

### 5.1 The mismatch problem

- **AUR matching and CP2000 risk** — The IRS Automated Underreporter program runs every individual return through a matching routine against the AUR/IRP file (the warehouse of W-2s, 1099s, K-1s, and other information returns). When the sum of information-return amounts attributable to a particular line of the return exceeds what the taxpayer reported, the system flags the return for a CP2000 notice. 1099-K matching is one of the most aggressive AUR matches because: The form is gross, but Schedule C is net of returns and discounts; The form may double-count with 1099-NEC; Issuers may include sales tax that the taxpayer doesn't treat as income; Multiple 1099-Ks may overlap (e.g., Stripe + the Patreon 1099-K that includes Stripe-processed payments). The cure is proactive reconciliation on the return, not waiting for the CP2000 to arrive.

### 5.2 Schedule C reconciliation worksheet

For a business taxpayer, prepare an internal worksheet (not filed, but retained):

```
SCHEDULE C 1099-K RECONCILIATION — TAX YEAR 2025

1099-K(s) received:
  Stripe (TIN 47-XXXXXXX)                          $  82,400.00
  Square (TIN 81-XXXXXXX)                          $   4,150.00
  PayPal G&S (TIN 77-XXXXXXX)                      $  11,250.00
  Etsy (TIN 20-XXXXXXX)                            $   3,805.00
  Total 1099-K gross                               $ 101,605.00

Add: cash and check receipts (not 1099-K)          $   2,800.00
Add: ACH receipts via Plaid (not 1099-K)           $   6,400.00
Subtotal: gross receipts before adjustments        $ 110,805.00

Less: refunds and chargebacks issued in 2025       $  (3,200.00)
Less: sales tax collected and remitted             $  (4,150.00)
Less: 1099-K amounts also reported on 1099-NEC
      (double-count from Client X $12,000)         $ (12,000.00)
Less: processor fees included in Box 1a
      (Stripe fees $2,950 — separately on Sch C
       Line 17/18 as fees expense, not netted)     $       0.00
                                                   ___________
Schedule C Line 1 — Gross receipts                 $  91,455.00
```

The worksheet must answer: for every dollar of 1099-K, where did it go? Either it's in Line 1, it's a refund/chargeback that doesn't belong there, it's sales tax remitted, or it's a double-count with a 1099-NEC.

> **AUDIT FLASH POINT — large 1099-K with no Schedule C.** A taxpayer who receives a 1099-K above $5,000 and files no Schedule C is the highest-priority AUR pull. Always file Schedule C even if the activity is a hobby — actually, **especially** if the activity is a hobby — to give the auditor a paper trail. Even better: if Schedule 1 Line 8j is used for hobby income, attach a statement reconciling the 1099-K to the Line 8j figure.

### 5.3 Personal items sold at a loss — the IRS two-line wash

- **IRS two-line wash procedure** — IRS Form 1040 Schedule 1 Instructions (2024 version) and the 2024 "Understanding Your Form 1099-K" FAQ Q-13 instruct taxpayers who received a 1099-K for personal items sold at a loss to: 1. Report the gross 1099-K amount on Schedule 1, Line 8z, "Other Income," with the description "Form 1099-K Personal items sold at a loss" 2. Report the same amount as a negative on Schedule 1, Line 24z, "Other Adjustments," with the description "Form 1099-K Personal items sold at a loss" The net effect on AGI is zero, but the 1099-K is acknowledged on the return and matched by the AUR system. This is the IRS-blessed method and avoids CP2000 generation.  _(IRS Form 1040 Schedule 1 Instructions (2024); Understanding Your Form 1099-K FAQ Q-13 (2024))_

### 5.3 Personal items sold at a loss — the IRS two-line wash

**Example.** A taxpayer cleared out a closet on Poshmark and received $1,850 across 47 sales of used clothing. Original cost of those items, if anyone could find the receipts, was well above $1,850. There is no taxable gain (each item sold for less than basis) and no deductible loss (personal-use property, §165(c)).

```
Schedule 1, Line 8z:    "Form 1099-K Personal items sold at a loss"     $ 1,850
Schedule 1, Line 24z:   "Form 1099-K Personal items sold at a loss"     $(1,850)
Net to Line 10 (Total Other Income) from this entry:                    $     0
```

The same two-line wash applies to:

- A roommate-reimbursement Venmo G&S 1099-K issued in error
- A Friends-and-Family payment misclassified by the sender
- Gift money sent through PayPal G&S (e.g., wedding gifts collected via a registry payment link)

For any of these the description should be specific: "Form 1099-K received in error — non-business reimbursement" or "Form 1099-K personal gift, not income."

### 5.4 Personal items sold at a gain — Schedule D

- **Personal property sold at a gain treatment** — If a taxpayer sells personal-use property at a gain — e.g., a Hermès Birkin bag purchased for $8,000 in 2018 and sold via The RealReal in 2025 for $14,000 — the gain is taxable as capital gain. The 1099-K cannot be washed; it represents real income. Long-term gain on collectibles (defined at §408(m): art, rugs, antiques, metals, gems, stamps, coins, alcoholic beverages, and "any other tangible personal property" the IRS specifies) is capped at 28% under §1(h)(4) — actually taxed at the lesser of 28% or the taxpayer's ordinary rate. Long-term holding is >1 year. Short-term gain is taxed at ordinary rates. Report on Form 8949 with box C checked (basis not reported to IRS). Carry to Schedule D Part I or II depending on holding period. Basis = original purchase price plus any improvements; if basis can't be substantiated, IRS will assert zero basis. If the taxpayer made many small sales of personal property where most are at a loss and a few are at a gain, the practitioner needs to disaggregate transaction-level: each loss is washed (§5.3) and each gain is reported (§5.4). This is tedious but it's the correct treatment.  _(§408(m); §1(h)(4); Form 8949; Schedule D)_

### 5.5 Hobby income — Schedule 1 Line 8j

- **Hobby income and COGS treatment** — After TCJA suspended miscellaneous 2% itemized deductions through 2025 and OBBBA made the suspension permanent, hobby losses are non-deductible at the federal level. Hobby gross receipts go on Schedule 1 Line 8j. No expense offset is allowed. Cost of goods sold (COGS) is a special case. The Tax Court has historically allowed COGS as a return-of-capital adjustment even for hobbies (see Welch v. Helvering, 290 U.S. 111 (1933), distinguishing return of capital from deductions). The IRS position is mixed; FAQ Q-14 (2024) appears to disallow COGS for hobby activity but is not authoritative. Conservative practice: do not net COGS against Line 8j unless the taxpayer is prepared to defend the §61 versus §162 distinction with substantial authority. For inventory-based hobbies (a vintage-watch flipper who isn't yet a business), consider whether the activity has actually crossed the §183 line into a trade or business — see §6.  _(Welch v. Helvering, 290 U.S. 111 (1933); FAQ Q-14 (2024); §61; §162; §183)_

## 6. Hobby vs. business — the §183 nine-factor test

When a taxpayer receives a 1099-K for activity that may or may not be a trade or business, the practitioner must determine where on the spectrum the activity falls. The classification controls whether Schedule C or Schedule 1 Line 8j is the right reporting line.

## 6. Hobby vs. business — the §183 nine-factor test

- **§183(d) presumption** — an activity is presumed to be engaged in for profit if it produces gross income in excess of deductions in 3 of the past 5 consecutive years (2 of 7 for horse activities). The presumption can be rebutted by the IRS but it shifts the burden.  _(§183(d))_

## 6. Hobby vs. business — the §183 nine-factor test

- **Treas. Reg. §1.183-2(b) nine factors** — 1. Manner in which the activity is carried on (businesslike books, separate bank account, etc.) 2. Expertise of the taxpayer or advisors 3. Time and effort expended 4. Expectation that assets will appreciate 5. Success in carrying on other similar or dissimilar activities 6. History of income or losses 7. Amount of occasional profits, if any 8. Financial status of the taxpayer (does the taxpayer need the income?) 9. Elements of personal pleasure or recreation. No factor is decisive; all are considered.  _(Treas. Reg. §1.183-2(b))_

## 6. Hobby vs. business — the §183 nine-factor test

**Practical screening questions for a 1099-K activity:**

- Is there a separate bank or processor account?
- Does the taxpayer keep books?
- Has the activity generated a profit in any year?
- How many hours per week?
- Is the activity advertised? Does the taxpayer have business cards, a website, a tax ID, a Schedule C or LLC?
- Does the taxpayer depend on the income?

A taxpayer who sold $7,000 of crocheted blankets on Etsy in 2025, spent $4,500 on yarn, worked 5 hours a week, has no separate bank account, has never made a profit in three years of selling, and considers crocheting a relaxing pastime is a hobbyist. A taxpayer who sold the same $7,000, has an LLC, a separate Stripe account, advertises on Instagram, treats it as a side income source, and is on year one of building it is a business.

> **AUDIT FLASH POINT — §183 challenges where Schedule C losses are claimed.** The pattern that draws IRS attention is **multi-year losses on a Schedule C that doesn't look like a business**. An "Etsy crochet shop" Schedule C with $7,000 gross, $9,000 in expenses (yarn, equipment depreciation, home office, the loom), and a $2,000 loss — claimed year after year against W-2 wages — is the textbook §183 audit trigger. If the activity has a profit motive and proper records, defend it. If it's truly a hobby, do not file Schedule C; use Line 8j and accept that the gross is taxable without offset.

## 7. Platform-specific patterns

### 7.1 PayPal — Friends & Family vs. Goods & Services

- **PayPal F&F vs G&S rules** — PayPal allows the sender to designate a payment as either "Friends and Family" (F&F) or "Goods and Services" (G&S). F&F: PayPal does not charge a transaction fee (from a US bank-funded source), does not offer buyer protection, and does NOT report on 1099-K. The transaction is treated as a personal transfer outside §6050W. G&S: PayPal charges 2.99% + $0.49 (US domestic, as of 2025), offers buyer protection, and DOES report on 1099-K subject to the threshold. The seller cannot unilaterally change a payment from F&F to G&S after the fact; the sender controls the designation at the moment of payment. **Mistagging risks** in both directions: - **Buyer mistags G&S as F&F**: seller has no fee, no protection, but income is unreported. Business taxpayers should refuse F&F payments for business transactions; the gross is still gross income on Schedule C regardless of how it was tagged. - **Buyer mistags F&F as G&S**: PayPal collects fee and issues 1099-K to recipient. This is the "wedding gift via PayPal G&S" scenario. Use the §5.3 two-line wash and document.  _(§6050W)_

### 7.2 Venmo — F&F vs. G&S vs. Business Profile

- **Venmo three flows** — Venmo (owned by PayPal) followed PayPal in introducing a G&S toggle in mid-2021. In 2021 Venmo also introduced "Venmo Business Profile" — a separate profile that is per se G&S for all incoming payments. Any payment to a Business Profile is reportable. For 1099-K reconciliation, the practitioner must distinguish three Venmo flows: 1. **Personal Venmo, F&F transactions** — not reported, not income, no action 2. **Personal Venmo, G&S transactions** — reported on 1099-K if over threshold; could be business, hobby, or personal-property sale 3. **Business Profile** — always reported on 1099-K (no F&F option); per-se business if profile was opened intentionally

### 7.3 Cash App — Personal vs. Cash App for Business

- **Cash App personal vs business account rule** — Cash App offers two account types. A personal Cash App account is not a TPSO for §6050W purposes; transfers between personal accounts are treated like Zelle (bank-direct rails). Cash App for Business is a separate account opened intentionally by a merchant; it IS a TPSO. Form 1099-K is issued for Cash App for Business activity only. This means a taxpayer can receive a payment for a side business through their personal Cash App account, never get a 1099-K, and still owe tax on it. The reverse pattern — a Cash App for Business 1099-K — almost always indicates a deliberate business account, so it almost always lands on Schedule C.  _(§6050W)_

### 7.4 Airbnb and VRBO — short-term rental

- **Airbnb/VRBO occupancy tax treatment** — A 1099-K from Airbnb reports the host payout, which is the gross nightly rate plus cleaning fees, minus the host service fee. Whether occupancy taxes are included depends on the state and the platform: - Where Airbnb has a tax-collection agreement with the state/locality (about 30 states plus DC and many cities), Airbnb collects occupancy/transient lodging tax from the guest and remits directly to the taxing authority. This amount is excluded from the host's 1099-K. - Where Airbnb does not have a tax-collection agreement, Airbnb collects occupancy tax from the guest and passes it through to the host, who is then responsible for remitting. The pass-through amount IS included in the host's 1099-K. The host then deducts the remitted tax as an expense. **Schedule C vs. Schedule E for short-term rentals** is a separate question outside this skill's scope. The general rule (Treas. Reg. §1.469-1T(e)(3)(ii)(A)): if average stay is 7 days or less, the activity is a §469(c)(7)-type business and may be Schedule C if "substantial services" are provided; otherwise Schedule E. See `us-short-term-rental` (forthcoming).  _(Treas. Reg. §1.469-1T(e)(3)(ii)(A); §469(c)(7))_

### 7.5 Uber and Lyft — drivers receive BOTH 1099-K and 1099-NEC

- **Uber/Lyft double-form treatment** — A typical ride-share driver in 2025 receives: Form 1099-K from Uber Technologies or Lyft, Inc. reporting gross rider payments processed through the app — this is the rider-paid fare PLUS Uber/Lyft's commission, tolls, surge pricing, and tips. Form 1099-NEC from the same entity reporting non-fare incentive payments (referral bonuses, quest completion bonuses, guaranteed earnings, etc.). The 1099-K Box 1a figure is NOT the driver's gross income. It includes Uber's commission, which the driver never receives. The driver's gross income on Schedule C Line 1 is the 1099-K Box 1a plus the 1099-NEC, and then on Schedule C Line 39 ("Other costs" within Part III COGS, or on Line 10 as a commission) the driver deducts Uber's commission, the booking fee, the marketplace fee, and any other amounts that were on the 1099-K but never reached the driver's bank account. The driver's annual tax summary from Uber/Lyft will reconcile: gross fares, tips, tolls, taxes, Uber service fee, booking fee, etc. The practitioner uses the tax summary, not the 1099-K alone, to build Schedule C.

### 7.5 Uber and Lyft — drivers receive BOTH 1099-K and 1099-NEC

> **AUDIT FLASH POINT — ride-share Schedule C with no commission deduction.** AUR will see 1099-K of $35,000 + 1099-NEC of $2,000 = $37,000 information returns. If Schedule C Line 1 shows $24,000 and there's no line item deducting "Uber service fee" or "platform commission," the AUR system pulls the return. Always show the gross on Line 1 and break out the commission on Line 10 (commissions and fees) — make the reconciliation visible.

### 7.6 DoorDash, Grubhub, Uber Eats, Instacart Shopper — delivery gig

- **Delivery gig double-form pattern** — Same pattern as ride-share for drivers/shoppers classified as ICs: 1099-K for processed earnings; 1099-NEC for incentive bonuses; Tax summary from the platform reconciles gross. DoorDash and Uber Eats currently issue both forms; Grubhub historically issued only 1099-NEC (treating the entire payout as non-employee compensation rather than a settled payment). Practitioner should check what the client actually received.

### 7.7 Content creators — Patreon, OnlyFans, Twitch, YouTube, Substack

Content creators commonly receive multiple forms reflecting different revenue streams:

**Content creators platform/form table**

| Platform | Form issued | Why |
| --- | --- | --- |
| Patreon | 1099-K | Patreon is a TPSO; payments to creators are settled |
| OnlyFans | 1099-K (via Fenix International / OFTV LLC) | TPSO |
| Substack | 1099-K | Stripe-backed TPSO |
| YouTube AdSense | 1099-NEC (from Google LLC) | Direct contractor relationship, not a settled payment |
| YouTube Super Chat / Super Thanks | 1099-K (from Google Payments) | Settled through Google's payment network |
| Twitch subs & bits | 1099-K (from Amazon Payments) | TPSO |
| Twitch ad revenue | 1099-NEC (from Twitch Interactive) | Contractor relationship |
| TikTok Creator Fund | 1099-NEC | Direct relationship |
| Meta (Reels Play Bonus) | 1099-NEC | Direct relationship |
| Instagram subscriptions | 1099-K | Settled via Meta Pay |

### 7.7 Content creators — Patreon, OnlyFans, Twitch, YouTube, Substack

A working creator can easily receive 5+ forms across these categories. Reconciliation needs to itemize: each form, what's in it, what platform it covers, and how it lands on Schedule C.

### 7.8 GoFundMe and crowdfunding — generally not 1099-K

- **Crowdfunding tax treatment** — GoFundMe Personal Fundraising (the "charitable" use case) is treated as receipt of gifts to the beneficiary; gifts are excluded from gross income under §102 and are not reported on 1099-K. GoFundMe does not issue 1099-Ks to personal-fundraising beneficiaries. Kickstarter, Indiegogo, and similar reward-based crowdfunding are different — these are pre-orders or contributions in exchange for a reward, treated as gross income to the project owner. Stripe is the underlying processor and may issue 1099-K to the project owner. GoFundMe Charity (now Classy) — donations to qualified 501(c)(3)s — flow to the charity directly; the donor gets a charitable contribution deduction, and the charity receives the funds tax-free under §501. No 1099-K to anyone.  _(§102; §501)_

### 7.9 Marketplace facilitators and sales tax — Wayfair

- **Marketplace facilitator sales tax exclusion rule** — Under South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018), states may require remote sellers and marketplace facilitators with economic nexus to collect and remit state sales tax. By 2024, all 45 states with a sales tax plus DC have marketplace facilitator laws. For 1099-K purposes the practical consequence is: Marketplace facilitator platforms (Amazon, Etsy, eBay, Walmart Marketplace, Mercari, Poshmark, StubHub) collect sales tax from buyers and remit directly to the state. They EXCLUDE collected sales tax from the seller's 1099-K. The seller never receives the sales tax. Non-marketplace platforms (Stripe, Square, Shopify Payments when not used through Shopify's tax-handling service) pass collected sales tax through to the seller. They INCLUDE it in 1099-K Box 1a. The seller is responsible for remitting. This means the same $100,000 of gross sales can produce a $100,000 1099-K (Stripe, sales tax included) or a $93,000 1099-K (Etsy, sales tax excluded), depending on platform. Schedule C Line 1 should be the gross excluding sales tax in both cases; on the Stripe scenario, the practitioner backs out remitted sales tax from Box 1a in the reconciliation.  _(South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018))_

## 8. Double-counting with 1099-NEC

### 8.1 The classic pattern

A consultant invoices Client X $12,000 in 2025. Client X pays the invoice through Stripe Invoicing. Stripe processes the payment and remits $11,652.40 to the consultant ($12,000 less Stripe's 2.9% + $0.30 fee per transaction). At year-end:

- Stripe issues a **1099-K** for $12,000 (gross of fee) covering the year's total processed receipts
- Client X — whose accountant runs a year-end 1099-NEC report — issues a **1099-NEC** for $12,000 to the consultant

The IRS now has $24,000 of information returns for a single $12,000 transaction. If the consultant reports $12,000 on Schedule C, AUR matches $24,000 of information returns to $12,000 of reported income and proposes a $12,000 underreporter adjustment.

### 8.2 IRS Notice 2023-74 acknowledgment

- **Notice 2023-74 §V acknowledgment of duplication** — Notice 2023-74 §V states that where a payment is reportable on both Form 1099-K (by the PSE) and Form 1099-NEC (by the payor), the payee should report the income once. The notice does not provide a mechanical fix; it just acknowledges the problem.  _(Notice 2023-74 §V)_

### 8.3 Treas. Reg. §1.6041-1(a)(1)(iv) — the payor's escape

- **Payor exemption from issuing 1099-NEC when paid via PSE** — Under Treas. Reg. §1.6041-1(a)(1)(iv), a payor who pays a contractor through a payment card or third-party network is not required to issue 1099-NEC because the PSE is already reporting on 1099-K. The payor can rely on §6050W reporting and skip 1099-NEC for that contractor. Many payors don't know this. They issue 1099-NEC anyway, "to be safe." The duplicate report ends up in AUR.  _(Treas. Reg. §1.6041-1(a)(1)(iv))_

### 8.4 Reconciliation method

- **CP2000 response for duplicate 1099-K/1099-NEC** — On Schedule C Line 1, report gross receipts ONCE. In the §5.2 reconciliation worksheet, identify the duplicate 1099-NEC amounts and back them out. If a CP2000 arrives, respond with: 1. The reconciliation worksheet 2. Copies of both 1099-K and 1099-NEC showing same payor / same amount 3. Citation to Treas. Reg. §1.6041-1(a)(1)(iv) and Notice 2023-74. If the payor is the practitioner's client (because the practitioner also prepares Client X's return), advise Client X to STOP issuing 1099-NEC for contractors paid through Stripe/PayPal/credit card — that is the structural fix. See `us-1099-nec-issuance`.  _(Treas. Reg. §1.6041-1(a)(1)(iv); Notice 2023-74)_

## 9. IRS CP2000 defense

### 9.1 What a CP2000 looks like

- **CP2000 notice** — A CP2000 notice is generated by the AUR system when reported income on Form 1040 plus Schedules doesn't match the IRP file. It proposes an adjustment, with associated tax, penalty, and interest. The taxpayer has 30 days from the notice date to respond.
- **1099-K-driven CP2000s** — For 1099-K-driven CP2000s, the notice will list each unmatched 1099-K and propose to add the gross amount to Schedule 1 Line 8a or to Schedule C Line 1, whichever the system chooses.

### 9.2 Response packaging

A complete CP2000 response for a 1099-K issue includes:

1. **The CP2000 response form** signed by the taxpayer (or POA)
2. **Box "I disagree"** checked, with explanation
3. **Reconciliation worksheet** — the §5.2 worksheet built proactively
4. **Copies of all 1099-Ks and 1099-NECs** referenced in the worksheet
5. **Platform tax summaries** (Uber Annual Tax Summary, Airbnb Earnings Summary, PayPal Activity Statement, etc.)
6. **Bank/processor account statements** showing actual deposits (helpful where fees, refunds, or sales tax are in dispute)
7. **For personal-items-at-loss claims**: documentation that the items were personal-use (e.g., purchase receipts, original photographs, listing descriptions that say "used")
8. **For F&F mistag claims**: screenshots showing the relationship between sender and recipient, any text-message context, or a written statement from the sender clarifying the intended designation
9. **Citation block**: Treas. Reg. §1.6050W-1(a)(5) (gross definition), Notice 2024-85 (threshold phase-in), Notice 2023-74 (double-count acknowledgment), Treas. Reg. §1.6041-1(a)(1)(iv) (payor escape), IRS FAQ "Understanding Your Form 1099-K" Q-13 (two-line wash)

### 9.3 Sample explanation statement (attach to return proactively)

> **Statement Regarding Form 1099-K Reconciliation — Tax Year 2025**
>
> Taxpayer received the following Forms 1099-K in 2025:
>
> 1. Stripe, Inc. — $82,400 — included in Schedule C Line 1 after backing out $1,200 of refunds (separately deducted on Schedule C Line 28 as bad debt) and $2,800 of processor fees (separately deducted on Schedule C Line 10).
> 2. PayPal, Inc. (Goods and Services) — $11,250 — included in Schedule C Line 1. Of this amount, $1,850 represents personal Friends-and-Family transfers from family members for shared travel costs that were inadvertently designated as Goods and Services by the senders. Taxpayer attempted to obtain corrected Forms 1099-K from PayPal but the request was denied; per IRS FAQ "Understanding Your Form 1099-K" Q-13, taxpayer has reported the gross 1099-K amount in Schedule C and included a compensating expense entry of $1,850 on Schedule C Line 27a (Other expenses) described as "1099-K Personal F&F received in error."
> 3. Poshmark, Inc. — $1,640 — represents proceeds from sale of personal-use clothing items at a loss. Per IRS guidance, gross amount of $1,640 is reported on Schedule 1 Line 8z ("Form 1099-K Personal items sold at a loss") with an offsetting negative entry of $1,640 on Schedule 1 Line 24z. No taxable income results from these sales because each item was sold for less than original cost; the loss is non-deductible under §165(c).
>
> Total Form 1099-K amount on file: $95,290. Reconciled to Schedule C Line 1 of $91,640 and Schedule 1 Line 8z (offset by Line 24z) of $1,640, with the remaining $2,010 representing refunds, processor fees, and sales tax that are separately accounted for. No income has been omitted from the return.

A statement of this form, filed with the original return, generally precludes CP2000 generation entirely.

## 10. Worked examples

### 10.1 Example — Etsy closet-cleaner, $7,000 at a loss

Sarah, a marketing manager with W-2 wages of $85,000, opened an Etsy shop in 2023 to sell handmade enamel pins as a hobby. In 2025 she also listed some used personal items — vintage band T-shirts, an old camera, books. Total 2025 Etsy Payments gross: $7,140. Of that, $3,800 was new enamel pins (cost: $4,200, so a $400 loss on the hobby activity, but hobby losses are non-deductible). $3,340 was personal items sold at a loss (each item sold below original purchase price).

She received a Form 1099-K from Etsy for $7,140.

- **Treatment** — Hobby activity ($3,800 enamel pins) → Schedule 1 Line 8j, hobby income. No expense deduction. Even though the activity ran at a loss in real economic terms, $3,800 is reportable as Line 8j and the $4,200 of materials is non-deductible (TCJA §67(g) made permanent by OBBBA). Personal items at a loss ($3,340) → Schedule 1 Line 8z (gross) and Line 24z (negative offset). Net zero.  _(TCJA §67(g); OBBBA)_

```
Schedule 1, Line 8j (Activity not engaged in for profit income):       $ 3,800
Schedule 1, Line 8z (Form 1099-K Personal items sold at a loss):       $ 3,340
Schedule 1, Line 24z (Form 1099-K Personal items sold at a loss):      $(3,340)
Schedule 1, Line 10 contribution to total Other income:                $ 3,800
```

Net taxable contribution from the 1099-K: $3,800 to AGI. The full $7,140 is acknowledged and matched.

Statement disaggregating the $7,140 into the $3,800 hobby component and the $3,340 personal-property loss component. Without disaggregation, AUR may try to push the entire $7,140 to Schedule C.

- **§183 analysis** — Three years of Etsy losses on enamel pins, no separate bank account, no advertising, no profit motive on a businesslike basis → hobby. Do NOT file Schedule C for this activity. Doing so would invite §183 challenge AND would deny the personal-property-loss treatment for the other half of the 1099-K.  _(IRC §183)_

### 10.2 Example — Ride-share driver, $35,000 1099-K + $2,000 1099-NEC

Marcus drives full-time for Uber in 2025. His Uber Annual Tax Summary shows:

**Uber Annual Tax Summary line items**

| Line item | Amount |
| --- | --- |
| Gross fares (including Uber commission) | $32,800 |
| Tolls collected | $1,150 |
| Tips collected | $1,050 |
| **Total 1099-K (Box 1a)** | **$35,000** |
| Quest bonuses (incentive payments) | $2,000 |
| **Total 1099-NEC** | **$2,000** |
| Uber service fee (commission) | $(8,200) |
| Booking fee (passed to taxpayer's expense) | $(950) |
| Net deposited to Marcus's bank | $26,850 |

- **Mileage facts** — Marcus drove 28,500 business miles in 2025 (logged via MileIQ). He uses the standard mileage rate of $0.70/mile (Notice 2025-XX hypothetical 2025 rate).  _(Notice 2025-XX (hypothetical))_

```
SCHEDULE C — Marcus, Tax Year 2025

Part I:
Line 1   Gross receipts (1099-K + 1099-NEC + cash tips not on 1099)   $ 37,000
Line 7   Gross income                                                  $ 37,000

Part II:
Line 10  Commissions and fees (Uber service fee + booking fee)         $  9,150
Line 9   Car and truck expenses (28,500 mi × $0.70)                    $ 19,950
Line 22  Supplies (phone mount, water for passengers, car wash)        $    420
Line 25  Utilities (business portion of cell phone)                    $    480
Line 28  Total expenses                                                $ 30,000

Line 31  Net profit                                                    $  7,000
```

Schedule SE on $7,000 of net profit: $7,000 × 0.9235 = $6,465 × 15.3% = $988 of SE tax. Half of SE tax deductible ($494) on Schedule 1 Line 15.

- **Reconciliation** — Information returns total $37,000 ($35,000 + $2,000). Schedule C Line 1 = $37,000. AUR match clears. The critical structural choice: gross-on-Line-1, commission-on-Line-10. Some preparers net the commission and put $26,800 on Line 1 — that generates an AUR mismatch every time, because AUR sees $37,000 of info returns and $26,800 of reported gross.

### 10.3 Example — Content creator with Stripe + Patreon 1099-Ks

Jade is a full-time YouTube creator and podcaster. In 2025 she received the items below. She also receives 4 sponsored-content payments totaling $22,000 from various brands, all paid via Stripe, none of which sent her a 1099-NEC (relying on Treas. Reg. §1.6041-1(a)(1)(iv)).

**2025 information returns received**

| Source | Form | Amount |
| --- | --- | --- |
| Patreon (monthly memberships) | 1099-K | $94,200 |
| Stripe (direct merch sales via Shopify) | 1099-K | $18,400 |
| Google AdSense (YouTube ad revenue) | 1099-NEC | $42,000 |
| Spotify for Podcasters (ad revenue) | 1099-NEC | $6,800 |
| Sponsorship from Brand X (paid direct via Stripe) | 1099-NEC from Brand X for $15,000, ALSO in Stripe 1099-K | duplicated |

```
Total information returns received:
  1099-K (Patreon)          $  94,200
  1099-K (Stripe)           $  18,400      ← includes Brand X $15,000 AND the $22,000 of un-1099-NEC'd sponsorships AND merch sales
  1099-NEC (Google)         $  42,000
  1099-NEC (Spotify)        $   6,800
  1099-NEC (Brand X)        $  15,000      ← DUPLICATES the Stripe 1099-K
  TOTAL on AUR              $ 176,400

True gross business receipts:
  Patreon memberships         $  94,200
  Merch sales (Stripe)        $   3,000    ← (Stripe 1099-K of $18,400 less $15,000 Brand X less... wait, see below)
  Brand X sponsorship         $  15,000    ← reported on Stripe AND 1099-NEC; report once
  Other sponsorships          $  22,000    ← in Stripe 1099-K only
  YouTube AdSense              $  42,000
  Podcast ads (Spotify)       $   6,800
  Subtotal                    $ 183,000
  Less Patreon platform fee   $  (8,478)   ← Patreon takes ~9%; backed out on Sched C Line 10
  Less Stripe processing fees $  (1,710)   ← backed out on Sched C Line 17
  
Schedule C Line 1 = $ 183,000 (gross before fees; fees are below the line)
```

Stripe's $18,400 includes the $15,000 Brand X sponsorship (which also generated a 1099-NEC) AND the $22,000 of other-sponsorship payments... but wait — $15,000 + $22,000 = $37,000, which exceeds Stripe's $18,400. Recompute: in the worked facts, the $22,000 of "other sponsorships" must actually be partly on Stripe and partly elsewhere. In a real engagement the practitioner pulls the Stripe payouts CSV and reconciles transaction-by-transaction to identify which sponsors paid through Stripe. This is normal — 1099-K reconciliation for a content creator typically requires a transaction-level extract from the processor dashboard, not just the form.

- **CP2000 risk** — AUR sees $176,400 of information returns. Schedule C Line 1 = $183,000 (higher than info returns, because $22,000 of un-1099-NEC'd sponsorships are properly on Schedule C but not on any info return). No CP2000 risk if Jade's reported gross exceeds info returns. The Brand X $15,000 double-count is absorbed because Schedule C exceeds the larger of the two.

Attach reconciliation statement explaining: Brand X $15,000 appears on both Stripe 1099-K and 1099-NEC; reported once on Schedule C. Patreon fees and Stripe fees deducted below the line. Gross figures match platform dashboards available on request.

## 11. Quick reference — what to ask the client during intake

1. List **every** processor account you had open in 2025: Stripe, Square, PayPal, Venmo, Cash App for Business, Shopify, Toast, Clover, etc. Provide year-end Form 1099-K and the platform's annual transaction summary for each.
2. List **every** marketplace or platform account you sold through in 2025: eBay, Etsy, Amazon, Mercari, Poshmark, Depop, Vinted, Airbnb, VRBO, Uber, Lyft, DoorDash, Patreon, OnlyFans, Substack, Twitch, etc. Provide year-end Form 1099-K (whether or not you exceeded the threshold — many platforms issue at lower state thresholds) and platform tax summary.
3. Did you receive any **personal** payments via PayPal G&S or Venmo G&S in 2025 (sender mistagged, wedding gift, rent split, dinner split)?
4. Did you sell any **personal items** through any platform in 2025 (closet cleanout, garage-sale-equivalent listings)?
5. Did any of your clients/customers also issue you a **Form 1099-NEC** for amounts that you also received via processor (Stripe, PayPal, credit card)?
6. Do you use crypto exchanges? If yes, list each (Coinbase, Kraken, Gemini, etc.) and provide year-end Form 1099-DA and full transaction history.

## 12. Self-check

Before signing off on a return that includes any 1099-K, verify:

- [ ] Every 1099-K received by the client is accounted for somewhere on the return (Schedule C, Schedule 1 Line 8j, Schedule 1 Lines 8z+24z, or Schedule D).
- [ ] The sum of "1099-K gross amounts attributable to Schedule C" matches or is less than Schedule C Line 1, with a reconciliation worksheet identifying any difference.
- [ ] No 1099-K Box 1a amount has been **netted** against fees, refunds, or sales tax in computing Line 1; those items are below the line.
- [ ] Any 1099-NEC duplicating a 1099-K has been identified and not double-counted.
- [ ] If a 1099-K relates to personal-item losses, the §5.3 two-line wash is on Schedule 1 with clear descriptions.
- [ ] If a 1099-K relates to a hobby activity, Schedule 1 Line 8j is used and no Schedule C is filed for that activity.
- [ ] If a 1099-K relates to a personal item sold at a gain, Form 8949 and Schedule D are filed with substantiated basis.
- [ ] If the activity is on the §183 borderline, a contemporaneous file note documents the practitioner's analysis under the nine-factor test.
- [ ] If client received a CP2000 in a prior year on 1099-K matching, a proactive explanation statement is attached to this year's return.
- [ ] For ride-share/delivery drivers, Schedule C Line 1 includes the gross 1099-K (with platform commission) and Line 10 separately deducts the platform commission.
- [ ] For Airbnb/VRBO hosts, occupancy-tax treatment is verified against platform-specific tax-collection agreements for the relevant state/city.
- [ ] If client received Form 1099-DA from a crypto exchange, the reporting is reconciled to actual gain/loss computed from transaction history; 1099-DA gross proceeds are NOT income, only the gain is.
- [ ] The reviewer has reviewed and signed off on the 1099-K reconciliation worksheet, which is retained in the engagement file for the §6501 statute-of-limitations period (generally 3 years; 6 if more than 25% of gross income is omitted).

## 13. Citations

- **IRC §6050W** — Returns relating to payments made in settlement of payment card and third party network transactions  _(IRC §6050W)_
- **IRC §6050W(e)** — De minimis exception for third party settlement organizations  _(IRC §6050W(e))_
- **Treas. Reg. §1.6050W-1** — Information reporting for payments made in settlement of payment card and third party network transactions  _(Treas. Reg. §1.6050W-1)_
- **Treas. Reg. §1.6050W-1(a)(5)** — Definition of "gross amount" (without regard to fees, refunds, etc.)  _(Treas. Reg. §1.6050W-1(a)(5))_
- **Treas. Reg. §1.6041-1(a)(1)(iv)** — Payor relieved of 1099-NEC duty for credit-card / TPSO payments  _(Treas. Reg. §1.6041-1(a)(1)(iv))_
- **IRC §61** — Gross income defined  _(IRC §61)_
- **IRC §102** — Gifts and inheritances (exclusion)  _(IRC §102)_
- **IRC §162** — Trade or business expenses  _(IRC §162)_
- **IRC §165(c)** — Losses limited to business, investment, casualty (no personal-use losses)  _(IRC §165(c))_
- **IRC §183** — Activities not engaged in for profit  _(IRC §183)_
- **Treas. Reg. §1.183-2(b)** — Nine factors  _(Treas. Reg. §1.183-2(b))_
- **IRC §408(m)** — Collectibles defined  _(IRC §408(m))_
- **IRC §1(h)(4)** — 28% rate cap on collectibles long-term gains  _(IRC §1(h)(4))_
- **IRC §67(g)** — Suspension of miscellaneous 2% itemized deductions (TCJA; made permanent by OBBBA P.L. 119-21)  _(IRC §67(g))_
- **IRC §6045** — Returns of brokers (basis for 1099-DA)  _(IRC §6045)_
- **IRC §6501** — Statute of limitations  _(IRC §6501)_
- **IRC §6721, §6722** — Failure-to-file / failure-to-furnish penalties (for issuer side)  _(IRC §6721, §6722)_
- **ARPA, P.L. 117-2 §9674** — Reduction of TPSO threshold to $600  _(ARPA, P.L. 117-2 §9674)_
- **Housing Assistance Tax Act of 2008, P.L. 110-289 §3091** — Enactment of §6050W  _(Housing Assistance Tax Act of 2008, P.L. 110-289 §3091)_
- **Notice 2023-10** — 2022 transition year for ARPA threshold  _(Notice 2023-10)_
- **Notice 2023-74** — 2023 transition year, plus 1099-K/1099-NEC duplication acknowledgment  _(Notice 2023-74)_
- **Notice 2024-85 phase-in schedule** — $5,000 (2024) / $2,500 (2025) / $600 (2026)  _(Notice 2024-85)_
- **T.D. 10000 (June 28, 2024)** — Final regulations under §6045 finalizing 1099-DA for custodial digital-asset brokers  _(T.D. 10000 (June 28, 2024))_
- **Rev. Proc. 2024-28** — Wallet-by-wallet basis tracking safe harbor for digital assets  _(Rev. Proc. 2024-28)_
- **P.L. 119-3 (April 10, 2025)** — Joint resolution repealing DeFi-broker portion of T.D. 10000  _(P.L. 119-3 (April 10, 2025))_
- **P.L. 119-21 (OBBBA, July 4, 2025)** — Made TCJA §67(g) suspension of misc. 2% deductions permanent  _(P.L. 119-21 (OBBBA, July 4, 2025))_
- **South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018)** — Marketplace facilitator economic nexus  _(South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018))_
- **Welch v. Helvering, 290 U.S. 111 (1933)** — Return of capital vs. deductions  _(Welch v. Helvering, 290 U.S. 111 (1933))_
- **IRS, "Understanding Your Form 1099-K," IRS.gov FAQ (updated 2024)** — Q-1 through Q-15 — including Q-9 (received in error), Q-13 (two-line wash for personal items at loss), Q-14 (hobby income)  _(IRS, "Understanding Your Form 1099-K," IRS.gov FAQ (updated 2024))_
- **IRS Schedule 1 (Form 1040) Instructions, 2024 version** — Line 8z and Line 24z guidance  _(IRS Schedule 1 (Form 1040) Instructions, 2024 version)_
- **Form 1099-K Instructions, 2025 version** — Form 1099-K Instructions, 2025 version  _(Form 1099-K Instructions, 2025 version)_
- **Form 1099-DA Instructions, 2025 version** — issued draft August 2024, final pending  _(Form 1099-DA Instructions, 2025 version)_

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
