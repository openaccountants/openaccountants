---
name: selling-a-company-in-malta
description: "Working method for the accountant handling a sale of shares in a Maltese private company, tax year 2026. Covers the order of work (seller's residence and status, what the company owns, market value under the Capital Gains Rules, duty, income tax on the gain, Business Registry filing), the duty on the share transfer (2% of the higher of price and real value, 5% where 75% or more of the company's assets are immovable property), the seller's 7% provisional tax within 15 days, the 2026 Land Registry site plan requirement where the company holds immovable property, notification to the Commissioner before the Registry will act, Form T within 14 days and the BAROS single point of submission, and reporting the gain in the seller's return by 30 June. Trigger on: sell my company Malta, share transfer Malta, Form T, duty on shares Malta, capital gains on shares Malta."
jurisdiction: MT
category: international
tax_year: 2026
last_updated: 2026-10-23
version: 1.1
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Selling a company in Malta v1.1

Built by Michael Cutajar and the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.**

Tax year 2026. This skill is the working order for a share sale. The income tax rules on the gain (article 5 of the Income Tax Act, the participation exemption, non-resident and listed-share exemptions) are in `mt-capital-gains` and `mt-holding-company-participation-exemption`; it does not repeat them.

## METHOD

### [method:scope_gate] Who this skill is for, and who to refuse

This skill covers the sale, by an individual or a company, of shares in a Maltese private limited company to a third party for money. It is NOT for: an asset sale (business transfer, goodwill, property) rather than a share sale; a reorganisation, merger, or intra-group transfer claiming an exemption; a transfer causa mortis or a donation; shares listed on a stock exchange; or a sale with earn-outs, deferred consideration or vendor loans you cannot value today. Send those to a specialist. Stop before computing anything if the company, directly or through subsidiaries, owns Malta immovable property and nobody has a current architect's valuation: duty, market value and the gain all depend on it.

### [method:sequence] Order of operations

1. Establish the **seller**: individual or company, resident or not, domiciled or not, and how and when the shares were acquired.
2. Establish what the **company owns**: Malta immovable property or rights over it, directly or through subsidiaries. This decides the duty rate (2% or 5%) and whether a site plan and an architect's valuation are needed.
3. Work out the **market value** of the shares under the Capital Gains Rules, and compare it with the agreed price.
4. Compute **duty** on the higher of price and market value.
5. Compute the seller's **income tax position** on the gain, using `mt-capital-gains` (or confirm the exemption that applies, in writing).
6. Pay the seller's **provisional tax** within 15 days of the transfer (7%; see filing mechanics), or file the prescribed form claiming that the transfer is not taxable.
7. Notify the **Commissioner** (MTCA Property Tax Directorate) and get evidence of notification.
8. File **Form T** with the Malta Business Registry within 14 days, with due diligence documents and, if beneficial ownership changes, form BO2.

Never start with the seller's gain. The price on the term sheet is not the base for duty or tax if the market value is higher, and a property in the company changes the duty rate.

### [method:intake_questions] Questions before computing

- Who is selling, and are they resident and domiciled in Malta?
- When and how were the shares acquired, and at what cost? (deed, Form T, or causa mortis declaration)
- Does the company, or any subsidiary, own or hold rights over immovable property in Malta? Has an architect valued it?
- What is the agreed price, and is any of it deferred, contingent or paid in kind?
- Is the buyer related to the seller? (market value then matters even more)
- Will beneficial ownership change? (form BO2)

### [method:evidence] Documents to insist on

- Memorandum and articles, register of members, and the seller's acquisition documents.
- Latest audited financial statements and management accounts to the transfer date, for the market value working.
- For any property in the group: the deed, a current architect's valuation, and, from 2026, a site plan issued by the Land Registry where an architect's valuation of the property is required (LN 156/2026 and LN 158/2026).
- The share purchase agreement and evidence of the price paid.
Take the client's word for nothing in the market value working. The Property Tax Directorate vets the workings and can send its own architect.

### [method:judgment_rule] Price versus market value

Duty is due on the higher of the price and the market value of the shares, and the market value is worked out by an accountant under the Capital Gains Rules. Where the price is clearly below the value of the company's net assets, or the buyer is related, expect the department to test it. Where the company holds property, the department's internal board decides whether to accept the declared property value; if not, its architect sets the market value and the duty is reassessed. Model the transfer at market value and price both, and record which governs and why.

### [method:trap] Most-missed items

- **Using 2% for a property company.** Duty rises from 2% to 5% where 75% or more of the company's assets (current assets excluded, except immovable property) are immovable property or rights over it, or where the company holds shares in such a company and the look-through test reaches 75%.
- **Duty on the price only.** Duty is on the higher of price and market value.
- **No site plan.** Since LN 156/2026 and LN 158/2026, a share transfer in a company holding immovable property needs a Land Registry site plan wherever an architect's valuation is required.
- **Filing Form T before notifying the Commissioner.** The Registrar will not register a share transfer without evidence that it was notified to the Commissioner under the Duty on Documents and Transfers Act.
- **Missing the 14-day window.** Form T is due within 14 days of the transfer (one month for a transmission on death). Late filing brings penalties on company officers, plus daily penalties while the default continues.
- **Forgetting provisional tax.** The seller remits provisional tax within 15 days of the transfer: 7% of the consideration, or 7% of the higher of market value and consideration where a controlling interest is transferred; for shares in a property company the prescribed amount, up to 35%. Where the gain is not taxable, the seller files the prescribed form instead. Provisional tax is not due on shares in public companies.
- **Forgetting the seller's return.** A taxable gain on shares is reported in the seller's income tax return, with form RA2 or a capital gains computation attached.

### [method:cross_check] Reconcile before signing

The number of shares, classes and nominal values on Form T must match the share purchase agreement and the register of members. The value used for duty must match the market value working filed with the Property Tax Directorate. The gain in the seller's computation must start from the same consideration.

### [method:edge_case] When the deal is not a plain share sale

If the company is stripped of cash or property before the sale, if new shares are issued to the buyer instead of existing shares being sold, or if share rights or voting rights are changed around the sale, the duty and income tax analysis changes. A change in share capital or voting rights also has to be notified to the Commissioner before the Registrar acts. Refer these.

### [method:filing_mechanics] How submission works

The share transfer documents and the market value working are submitted to the Property Tax Directorate of the MTCA, which vets them and receipts the notification. Form T (transfer of shares) is then filed with the Malta Business Registry within 14 days, with the evidence of notification, due diligence documents and, if applicable, form BO2. From 1 December 2025, Form T for exempt share transfers with a valid article 47 determination, and for transactions exempt from a capital gains schedule, goes through a single point of online submission on BAROS. The duty-paying sale for money that this skill covers stays on the existing MTCA and MBR procedure; BAROS submission does not apply to it. Within 15 days of the transfer the seller remits provisional tax to the MTCA (Income Tax Management Act art. 43(1)(b)), which is credited against the tax on the gain. The seller reports a taxable gain in their income tax return; for an individual the return and payment are due by 30 June of the year after the sale, with interest of 0.6% a month on tax unpaid after that date.

### [method:handback_protocol] Working paper contents

The market value working, the duty computation, the property valuation and site plan (if any), the seller's gain computation or the exemption relied on with its source, the Commissioner's receipt, the provisional tax receipt (or the exemption form), the filed Form T and BO2, and the return reference.

## FACT CORRECTIONS

**FACT CORRECTIONS**  _(This file previously carried the rental income skill's text in error. Replaced with company-sale content in v1.1.)_

| fact_key | current | correct | source |
| --- | --- | --- | --- |
| share_duty | (none) | 2% of the higher of consideration and real value; plus 3 points (5% in all) where 75% or more of the company's assets, excluding current assets other than immovable property, are immovable property or rights over it, or through a held property company on the look-through test | Duty on Documents and Transfers Act art. 42(1)(b), 42(2) |
| provisional_tax | (none) | Within 15 days of the transfer: 7% of the consideration; 7% of the higher of market value and consideration on a transfer of a controlling interest; prescribed amount up to 35% for property-company shares; not payable where the prescribed form shows no tax, or on public company shares | Income Tax Management Act art. 43(1)(b), 43(2) |
| market_value | (none) | Market value of the shares worked out by an accountant under the Capital Gains Rules; vetted by the Property Tax Directorate | MTCA Share Transfers FAQ; MTCA Share Transfers |
| site_plan_2026 | (none) | Land Registry site plan, signed and stamped by a Perit, to accompany the Perit's valuation of the company's immovable property in the share valuation | LN 156/2026 (Capital Gains Rules r. 5(10), 5A(5)); LN 158/2026 (S.L. 364.06 r. 11(3), 12(5)) |
| form_t | (none) | Notice to the Registrar within 14 days (transmissions 1 month; listed public companies 90 days); evidence of notification to the Commissioner; due diligence documents; BO2 if applicable | MBR Change in Company Details |
| baros | (none) | From 1 December 2025, single point of online submission on BAROS for Form T only on exempt transfers with an article 47 determination and transactions exempt from a capital gains schedule; transfers paying duty or capital gains tax stay on the existing procedure | MBR notice, 28 November 2025 |
| return | (none) | Taxable gains on securities reported in the individual's return with form RA2 or a computation; return and payment by 30 June; 0.6% a month interest after | MTCA tax return booklet 2026; MTCA Tax Return Cycle |

## FLAGS

- [refer] The income tax rate and exemptions on the gain (resident individual, company seller, non-resident, participation exemption) are in `mt-capital-gains` and `mt-holding-company-participation-exemption`. They were not re-read in this refresh.
- [refer] Deadline for notifying the Commissioner of the share transfer, and the duty penalty for late notification: not confirmed from an official source today.
- [unsettled] Earn-outs and deferred consideration: how they enter the market value and the gain is a judgment call; do not finalise without specialist review.

## NOTES

Until v1.1 this file held a copy of the rental income skill under the company-sale title. That text has been removed; it lives in `how-to-account-for-rental-income-in-malta`.

## Sources

| Source | URL | Read on |
|---|---|---|
| Duty on Documents and Transfers Act, Cap. 364, art. 42 (2%, 75% test, 5%) | https://legislation.mt/eli/cap/364/eng | 2026-10-23 |
| Income Tax Management Act, Cap. 372, art. 43 (provisional tax) | https://legislation.mt/eli/cap/372/eng | 2026-10-23 |
| LN 156 of 2026 and LN 158 of 2026 (site plan) | https://legislation.mt/eli/ln/2026/156/eng ; https://legislation.mt/eli/ln/2026/158/eng | 2026-10-23 |
| MTCA, Share Transfers FAQ (2%, 5% property companies, Capital Gains Rules valuation) | https://mtca.gov.mt/personal-tax/sharetransfers/faqs-share-transfers | 2026-10-23 |
| MTCA, Share Transfers (submission to the Property Tax Directorate, vetting, architect) | https://mtca.gov.mt/personal-tax/sharetransfers/share-transfers | 2026-10-23 |
| MTCA, Overview of Legal Notices January to June 2026 (LN 156/2026, LN 158/2026) | https://mtca.gov.mt/docs/default-source/documents/legislative-developments/2026/overview-of-recently-published-legal-notices-january-to-june-2026-memo.pdf?sfvrsn=1191b20d_1 | 2026-10-23 |
| MTCA, Completing your tax return, basis year 2025 (capital gains, RA2) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/tax-return-booklet-individuals/mtca-tax-booklet-2026-eng-17-03.pdf?sfvrsn=5ca02b73_1 | 2026-10-23 |
| MTCA, Tax Return Cycle (30 June, 0.6% a month) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-10-23 |
| Malta Business Registry, Change in Company Details (Form T, 14 days, BO2) | https://www.mbr.mt/website-pages/change-in-company-details | 2026-10-23 |
| Malta Business Registry, Duty on Document Evidence (notification to the Commissioner) | https://www.mbr.mt/post/duty-on-document-evidence | 2026-10-23 |
| Malta Business Registry, Single point of submission for Form T via BAROS | https://www.mbr.mt/post/important-notice-single-point-of-submission-for-form-t-form-h-and-msr-form-f-via-baros | 2026-10-23 |

Not yet confirmed:
- Income tax treatment of the gain under articles 5 and 12 of the Income Tax Act was not re-read; see `mt-capital-gains`.
- The amount prescribed for provisional tax on property-company shares (capped at 35% by the Act) was not looked up.
- The deadline for notifying the Commissioner of a share transfer, and the late-notification duty penalty.
- Budget 2027 is presented on 26 October 2026; nothing from it is reflected here.

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
