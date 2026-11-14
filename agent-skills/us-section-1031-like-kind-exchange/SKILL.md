---
name: us-section-1031-like-kind-exchange
description: "US federal like-kind exchanges of real property under section 1031 for tax year 2026 (real property only since 2018). Covers qualifying use, the 45-day identification and 180-day exchange periods and the return due date trap, the qualified intermediary and disqualified persons, the 3-property, 200% and 95% identification rules, reverse exchanges (Rev. Proc. 2000-37 and 2004-51), build-to-suit, boot and liability netting, basis and holding period, section 1245 and 1250 recapture including cost-segregated components, depreciation of the replacement under Reg. 1.168(i)-6, related parties and the 2-year rule, vacation homes (Rev. Proc. 2008-16), the section 121 interaction, tenancy in common, disaster postponements, Form 8824 (2026) reporting, and the state claw-back flag (California Form 3840). Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-section-1031-like-kind-exchange"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US federal like-kind exchanges of real property (section 1031), tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 1031 and 121 (govinfo), Treas. Reg. 1.1031(a)-3, 1.1031(d)-2, 1.1031(k)-1 and 1.168(i)-6 (govinfo, CFR 2025), Form 8824 (2026) and its instructions (2026), IRS Pub. 544, and Rev. Procs. 2000-37, 2002-22, 2004-51, 2005-14, 2008-16 and 2018-58, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Section 1031 defers gain when real property held for business or investment is exchanged for other like-kind real property. The replacement must be identified in writing within **45 days** of transferring the old property and received within **180 days**, or by the due date (with extensions) of the return for the year of transfer if that is earlier. The taxpayer must never touch the money: use a qualified intermediary. Gain is taxed only to the extent of boot (cash, other property, net debt relief). The rules are not indexed and are the same for 2025 and 2026. Public Law 119-21 (the One Big Beautiful Bill Act) did not change section 1031 itself; its items in the 2026 Form 8824 instructions are the new section 1062 farmland election and the end of the Opportunity Zone deferral period on 31 December 2026.

## Scope and who this is for

In scope: any taxpayer that files a federal return (individuals, C and S corporations, partnerships, trusts and estates) and exchanges US real property held for use in a trade or business or for investment for other like-kind real property. It covers the rule itself, deferred exchanges through a qualified intermediary (QI), the identification rules, reverse and build-to-suit exchanges, boot and basis, related parties, depreciation of the replacement property, and Form 8824 ([26 U.S.C. 1031](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm); [Pub. 544](https://www.irs.gov/publications/p544)).

**Real property only.** For exchanges completed after 31 December 2017, section 1031 applies only to real property. A transition rule keeps the old rules for an exchange in which the taxpayer gave up the old property, or received the replacement, on or before 31 December 2017 ([26 U.S.C. 1031, 2017 amendment note](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm); [Instructions for Form 8824 (2026)](https://www.irs.gov/pub/irs-pdf/i8824.pdf)). Machinery, equipment, vehicles, artwork, collectibles, patents and other intangibles, and cryptocurrency, no longer qualify.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Capital gain rates on recognized gain | `us-capital-gains-and-losses` |
| Cost segregation studies and the recapture they create | `us-federal-cost-segregation` |
| Bonus depreciation and section 179 on the replacement's excess basis | `us-section-179-and-bonus-depreciation` |
| Opportunity Zone deferral (the alternative to section 1031) | `us-opportunity-zones` |
| Partnership returns and drop-and-swap structures | `us-form-1065-partnership` (refer the structure) |
| Section 1033 involuntary conversions, section 1043 sales, section 1062 farmland election | refer |
| State rules (annual information returns, claw-back of deferred gain) | the state's own skill, checked on that state's tax agency site |

## Ask the client first

- What is the property given up (the "relinquished property") and what will be received (the "replacement property")? Get each one's address or legal description, and whether each is in a state or DC or outside the United States.
- How was each property used? Rental, own business, land held for appreciation, a home, a vacation home, or bought to fix up and resell? Did the client use either property personally, and on how many days in each of the last two years?
- Is the client a dealer in real estate, or was this property held primarily for sale?
- What are the dates? The contract date, the date the relinquished property was transferred, the date the written identification was delivered, and the date the replacement was (or will be) received. Also ask for the client's tax year and the return due date, and whether an extension is planned.
- Who holds the sale proceeds? Get the exchange agreement and the QI's name. Has the QI (or anyone related to it) acted in the past 2 years as the client's employee, attorney, accountant, investment banker or broker, or real estate agent or broker?
- Is the other party, or the seller of the replacement property, related to the client? That covers family, and entities the client or family own.
- Will the client receive any cash or other non-real property? Ask about mortgages paid off on the old property or taken on with the new one, and about furniture or equipment transferred with either property.
- What are the adjusted basis and the depreciation history of the relinquished property? Was there a cost-segregation study (components classed as section 1245 property)?
- Was the replacement property bought before the old one was sold (a reverse exchange), or is it being built or improved after the sale?
- Is any part of either property the client's main home, now or in the last 5 years?
- Is the property in an area covered by a federal disaster declaration? Which states are the properties in, and where does the client live?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Identification period | 45 days | [26 U.S.C. 1031(a)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm) |
| Exchange period (or the return due date with extensions, if earlier) | 180 days | [26 U.S.C. 1031(a)(3)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm) |
| 3-property rule | up to 3 properties of any value | [Treas. Reg. 1.1031(k)-1(c)(4)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| 200% rule | total FMV of identified property not more than 200% of the FMV of all relinquished property | [Treas. Reg. 1.1031(k)-1(c)(4)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| 95% rule | identified property received worth at least 95% of the FMV of all identified property | [Treas. Reg. 1.1031(k)-1(c)(4)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| Incidental property limit | not more than 15% of the larger item's FMV | [Treas. Reg. 1.1031(k)-1(c)(5)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| Disqualified person lookback (agent of the taxpayer) | 2 years | [Treas. Reg. 1.1031(k)-1(k)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| Related-party holding period | 2 years after the last transfer | [26 U.S.C. 1031(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm) |
| Reverse exchange: written agreement after the EAT takes title | within 5 business days | [Rev. Proc. 2000-37](https://www.irs.gov/pub/irs-drop/rp-00-37.pdf) |
| Reverse exchange: combined holding period in the arrangement | not more than 180 days | [Rev. Proc. 2000-37](https://www.irs.gov/pub/irs-drop/rp-00-37.pdf) |
| Reverse exchange: replacement owned by the taxpayer within this period before transfer to the EAT does not qualify | 180 days | [Rev. Proc. 2004-51](https://www.irs.gov/pub/irs-drop/rp-04-51.pdf) |
| Vacation home safe harbor: fair rental days in each 12-month period | 14 days or more | [Rev. Proc. 2008-16](https://www.irs.gov/pub/irs-drop/rp-08-16.pdf) |
| Vacation home safe harbor: personal use cap in each 12-month period | greater of 14 days or 10% of fair rental days | [Rev. Proc. 2008-16](https://www.irs.gov/pub/irs-drop/rp-08-16.pdf) |
| Leasehold like kind to a fee interest | 30 years or more remaining | [Pub. 544](https://www.irs.gov/publications/p544) |
| No home-sale exclusion if sold within this period of acquisition in a 1031 exchange | 5 years | [26 U.S.C. 121(d)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm) |
| Home-sale exclusion (for the Rev. Proc. 2005-14 stacking) | USD 250,000 | [26 U.S.C. 121(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm) |
| Disaster postponement of the 45-day and 180-day deadlines | 120 days or the general postponement period, capped at the return due date or 1 year | [Rev. Proc. 2018-58, section 17](https://www.irs.gov/pub/irs-drop/rp-18-58.pdf) |

None of these is indexed for inflation. The same numbers apply to exchanges in 2025 and 2026.

### Steps

1. **Confirm both properties qualify.** Both must be real property ([Treas. Reg. 1.1031(a)-3](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031a-3.pdf)). Both must be held for productive use in a trade or business or for investment, and neither may be held primarily for sale ([26 U.S.C. 1031(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm)). The intent test applies to both properties. The statute sets no minimum holding period. A home used only as a personal residence does not qualify ([Instructions for Form 8824 (2026), Property Used as Home](https://www.irs.gov/pub/irs-pdf/i8824.pdf)).
2. **Confirm they are like kind.** Real properties are generally like kind to each other, whether improved or unimproved. US real property and foreign real property are not like kind to each other (section 1031(h)).
3. **Structure the exchange so there is no actual or constructive receipt of the proceeds.** In a deferred exchange, use a QI (or a qualified escrow or trust). The written agreement must stop the taxpayer from receiving, pledging, borrowing or otherwise getting the benefit of the money before the exchange period ends. It may allow only the release events in Reg. 1.1031(k)-1(g)(6) ([Treas. Reg. 1.1031(k)-1](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf)). If the taxpayer receives the money in full before getting the replacement, the whole thing is a sale; any actual or constructive receipt defeats the deferral.
4. **Identify the replacement in writing by day 45.** Count from the date the relinquished property is transferred. The identification must be in a signed written document, delivered to the person who must transfer the replacement or to another person involved in the exchange who is not the taxpayer or a disqualified person. It must describe the property clearly: a legal description, street address or distinguishable name. Any property received before day 45 counts as identified. An identification can be revoked in writing before day 45 ends ([Pub. 544](https://www.irs.gov/publications/p544)).
5. **Apply the identification limits:** the 3-property rule, the 200% rule, or the 95% rule (see the table above and the boundary table). Over-identification with no rescue is treated as if nothing was identified, but property actually received within the 45 days still counts.
6. **Receive the replacement by the earlier of day 180 or the due date of the transferor's return for the year of transfer, including extensions.** The taxpayer must receive substantially the same property that was identified. If several properties are given up on different dates, both periods start on the date of the earliest transfer. A taxpayer who transfers late in the year must extend the return (Form 4868 for an individual) to keep the full 180 days (Case 1).
7. **Work out gain and boot.** Realized gain is the amount realized minus adjusted basis. Recognized gain is the smaller of realized gain or boot. Boot is money plus the fair market value (FMV) of non-like-kind property received, plus net liabilities taken over by the other party, all reduced by exchange expenses. A loss is never recognized on the like-kind part ([26 U.S.C. 1031(b) and (c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm); [Instructions for Form 8824 (2026), Lines 15 to 20](https://www.irs.gov/pub/irs-pdf/i8824.pdf)).
8. **Work out depreciation recapture** within the recognized amount, following the section 1245 and 1250 rules (Form 8824 line 21). Put the rest on line 22 as section 1231 or capital gain.
9. **Work out the basis of the replacement:** Form 8824 line 18, plus line 23, minus line 15. Allocate it among what was received (line 25 and lines 25a to 25c). The holding period of the old property carries over (section 1223(1)).
10. **Set up depreciation for the replacement** under Treas. Reg. 1.168(i)-6, or elect out by the due date of the return for the replacement year ([Treas. Reg. 1.168(i)-6](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol3/pdf/CFR-2025-title26-vol3-sec1-168i-6.pdf)).
11. **Report** on Form 8824 for the year of the transfer. For a related-party exchange, also file it for the next 2 years.

### Depreciation of the replacement property ([Treas. Reg. 1.168(i)-6](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol3/pdf/CFR-2025-title26-vol3-sec1-168i-6.pdf))

- **Exchanged basis** (the carried-over part) keeps being depreciated over the remaining recovery period of the relinquished property. If the replacement has a **longer** recovery period, use the longer period, treating the replacement as placed in service when the old property was. If the replacement's period is **shorter**, keep the relinquished property's remaining period. A less accelerated method for the replacement also changes the method.
- **Excess basis** (for example, extra cash paid or new debt) is treated as newly placed in service in the year of replacement. Use the recovery period, method and convention that apply at that time.
- **Election out:** a taxpayer may elect to treat the whole basis as newly placed in service. The election is made on Form 4562 by the due date (including extensions) of the return for the year of replacement. It is made separately for each exchange, by the partnership or S corporation itself and not by its owners, and it can be revoked only with IRS consent.

### Section 1245 and 1250 recapture in an exchange ([Instructions for Form 8824 (2026), Line 21](https://www.irs.gov/pub/irs-pdf/i8824.pdf))

- **Section 1245 real property** (for example, cost-segregated components that count as real property under Reg. 1.1031(a)-3): the ordinary income is the smaller of (1) the depreciation allowed or allowable (up to the realized gain on line 19), or (2) the line 20 gain plus the FMV of non-section 1245 like-kind property received. So recapture can exceed the boot-driven gain when the replacement property has little section 1245 property (see Case 3).
- **Components that are not real property** under Reg. 1.1031(a)-3 (for example, personal property reclassified in a cost-segregation study that is not an inherently permanent structure or structural component) are not like-kind property at all: they are given up in a taxable exchange, and their gain, including full section 1245 recapture, is recognized even when no cash boot is received. Compute this before the exchange closes.
- **Section 1250 property:** the ordinary income is the smaller of (1) the additional depreciation that would be recaptured on a sale, or (2) the larger of the line 20 gain or the excess of (1) over the FMV of section 1250 property received.
- Recapture potential that is not triggered carries over to the replacement property. The IRS example shows USD 5,000 of potential section 1250 recapture attaching to the building received.

## Boundary and exception table

| Situation | What decides it | Source |
| --- | --- | --- |
| Held primarily for sale (dealer, flipper, developer inventory) | Section 1031 does not apply to real property held primarily for sale | [26 U.S.C. 1031(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm) |
| Home | Property used solely as a personal residence does not qualify. A main home that was rented out, or a home that is partly business, may use section 121 **first** and then section 1031 (Rev. Proc. 2005-14). Boot is taxed only to the extent it exceeds the section 121 excluded gain, and gain from depreciation after 6 May 1997 can be deferred under section 1031. | [Rev. Proc. 2005-14](https://www.irs.gov/pub/irs-drop/rp-05-14.pdf); [Instructions for Form 8824 (2026)](https://www.irs.gov/pub/irs-pdf/i8824.pdf) |
| Vacation or second home | Qualifies only if the facts show a business or investment holding. The safe harbor applies only if **all** its conditions are met: owned 24 months, and in each of the two 12-month periods rented at a fair rental for 14 days or more with personal use not more than the greater of 14 days or 10% of fair-rental days (the 24 months before the exchange for relinquished property, the 24 months after for replacement property). Personal use is counted under section 280A(d)(2). If replacement property later fails the test, file an amended return and do not report the exchange under section 1031. The safe harbor settles only the "held for" test. | [Rev. Proc. 2008-16](https://www.irs.gov/pub/irs-drop/rp-08-16.pdf) |
| Securities, notes, partnership interests, beneficial interests, choses in action | Never real property for section 1031, whatever state law says. **Exception:** an interest in a partnership that has a valid section 761(a) election out of subchapter K is treated as an interest in each partnership asset. Stock in a cooperative housing corporation, and certain qualifying mutual ditch, reservoir or irrigation company shares, are listed as real property. | [Instructions for Form 8824 (2026)](https://www.irs.gov/pub/irs-pdf/i8824.pdf); [26 U.S.C. 1031(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm) |
| Crypto swaps | Not real property, so not section 1031 for exchanges after 2017. For earlier years, the IRS Chief Counsel concluded that exchanges between Bitcoin, Ether and Litecoin completed before 1 January 2018 do not qualify. That advice is limited to those three coins and is not precedent. | [CCA 202124008](https://www.irs.gov/pub/irs-wd/202124008.pdf) |
| Foreign property | Foreign real property is real property not located in a state or DC. It is like kind to other foreign real property but not to US real property. The bar does not apply to replacing condemned property under section 1033. | [Pub. 544](https://www.irs.gov/publications/p544); [26 U.S.C. 1031(h)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm) |
| Constructive receipt | Money is constructively received when it is credited, set apart or made available to draw on. It is not when the taxpayer's control is subject to substantial limits. Receipt by the taxpayer's agent counts as receipt by the taxpayer. The protection ends when the limits lapse or are waived. | [Pub. 544](https://www.irs.gov/publications/p544) |
| When exchange funds can be released (g)(6) | (a) After the 45-day period, if nothing was identified. (b) After the taxpayer receives all the replacement property they are entitled to. (c) After a material and substantial contingency that happens after the identification period, **relates to the exchange, is in writing, and is beyond the control of the taxpayer and any disqualified person** (other than the transferor of the replacement). (d) After the exchange period ends. | [Treas. Reg. 1.1031(k)-1(g)(6)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| Disqualified person as QI | The taxpayer's agent: anyone who acted as employee, attorney, accountant, investment banker or broker, or real estate agent or broker in the 2 years ending on the first transfer. Also persons related to the taxpayer, or to such an agent, under section 267(b) or 707(b), with 10% substituted for 50%. | [Treas. Reg. 1.1031(k)-1(k)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| QI services that do not disqualify | Services for the taxpayer on exchanges intended to qualify under section 1031, and routine financial, title insurance, escrow or trust services by a financial institution, title insurance company or escrow company | [Treas. Reg. 1.1031(k)-1(k)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| Incidental property, for identification | Not a separate property if typically transferred with the larger item in a standard commercial transaction **and** its total FMV is not more than 15% of the larger item's FMV. Example: furniture with an apartment building worth USD 1,000,000, if the personal items total no more than USD 150,000. | [Treas. Reg. 1.1031(k)-1(c)(5)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf) |
| Incidental personal property, for QI restrictions | Disregarded when testing the (g)(6) limits if typically transferred with the real property and not more than 15% of the aggregate FMV of the replacement real property. It is still boot for gain purposes. | [Instructions for Form 8824 (2026)](https://www.irs.gov/pub/irs-pdf/i8824.pdf) |
| QI fails or goes bankrupt | Missing a deadline because of the QI can make the exchange taxable. If the QI defaults because of bankruptcy or receivership and Rev. Proc. 2010-14 is met, gain may be reported as payments are received. | [Instructions for Form 8824 (2026)](https://www.irs.gov/pub/irs-pdf/i8824.pdf) |
| Interest on exchange funds | Interest or a growth factor is taxable interest. If the QI keeps the earnings, the funds are treated as a loan to the QI, and imputed interest may apply. | [Pub. 544](https://www.irs.gov/publications/p544) |
| Reverse exchange | The exchange accommodation titleholder (EAT) holds the replacement (or relinquished) property under a written agreement signed within 5 business days of getting qualified indications of ownership. At that time, the taxpayer must have a **bona fide intent** to do an exchange. The relinquished property must be identified within 45 days and the arrangement completed within 180 days, with the combined holding time not over 180 days. The EAT cannot be the taxpayer or a disqualified person, and must be subject to federal income tax; an EAT that is a partnership or S corporation must be more than 90% owned by persons subject to federal income tax. **Rev. Proc. 2004-51:** replacement property does not count if the taxpayer owned it within the 180 days before its transfer to the EAT. | [Rev. Proc. 2000-37](https://www.irs.gov/pub/irs-drop/rp-00-37.pdf); [Rev. Proc. 2004-51](https://www.irs.gov/pub/irs-drop/rp-04-51.pdf); [Pub. 544](https://www.irs.gov/publications/p544) |
| Build-to-suit (property to be produced) | It can be identified before it exists. What is received must be substantially the same as identified, allowing for usual production changes. Only construction completed by the date of receipt counts, and only to the extent it is real property under local law. Work done after receipt is not like-kind property; that part is a taxable exchange for services. | [Pub. 544](https://www.irs.gov/publications/p544) |
| Related party (section 1031(f)) | Covers family (spouse, siblings, parents, children, grandparents, grandchildren) and related entities under section 267(b) or 707(b)(1). If **either** party disposes of the property received within 2 years of the last transfer, the deferred gain is recognized **as of the date of that disposition**. The 2 years are suspended while the holder's risk of loss is substantially reduced (a put, another person's right to acquire, or a short sale). Exceptions: (A) a disposition after the death of either party; (B) an involuntary conversion, **only if the exchange came before the threat or imminence of the conversion**; (C) it is shown to the IRS's satisfaction that **neither the exchange nor the disposition** had tax avoidance as one of its principal purposes. An exchange structured to avoid these rules, such as buying through a QI from a related party who takes cash, is not a like-kind exchange. | [26 U.S.C. 1031(f) and (g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm); [Instructions for Form 8824 (2026), Line 7](https://www.irs.gov/pub/irs-pdf/i8824.pdf) |
| Non-like-kind property given up | Gain or loss on it is recognized: its FMV minus its adjusted basis | [Pub. 544](https://www.irs.gov/publications/p544) |
| Liabilities | Debt the other party takes on counts as money received. It is netted against debt the taxpayer takes on, cash paid, and the FMV of other property given up. Cash received is **not** offset by debt the taxpayer assumes. Exchange expenses reduce the boot but not below zero. | [Instructions for Form 8824 (2026), Line 15](https://www.irs.gov/pub/irs-pdf/i8824.pdf); [Treas. Reg. 1.1031(d)-2](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031d-2.pdf) |
| Closing-statement items | Exchange expenses include brokerage commissions, attorney fees and deed preparation on the sale, and closing costs on the purchase. Property taxes, rent prorations, security deposits and repairs shown on the closing statement are **not** exchange expenses. | [Pub. 544](https://www.irs.gov/publications/p544) |
| Deadlines in a federally declared disaster | If an IRS news release grants relief, the 45-day and 180-day deadlines, and the Rev. Proc. 2000-37 deadlines, can be postponed by 120 days or to the end of the general disaster postponement, whichever is later. They cannot go past the return due date including extensions, or one year. Relief requires that the relinquished property was transferred (or the EAT got ownership) on or before the disaster date, and that the taxpayer is affected or has difficulty meeting a deadline because of the disaster. | [Rev. Proc. 2018-58, section 17](https://www.irs.gov/pub/irs-drop/rp-18-58.pdf) |
| Section 121 after an exchange | No home-sale exclusion if the property is sold within 5 years of its acquisition in a section 1031 exchange; also applies to anyone whose basis is carried over from the taxpayer | [26 U.S.C. 121(d)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm) |
| Leaseholds | A lease of 30 years or more is like kind to a fee interest. A life estate expected to last less than 30 years is not like kind to a remainder interest. | [Pub. 544](https://www.irs.gov/publications/p544) |
| State claw-back (for example California) | Some states track deferred gain when the replacement is outside the state. California requires Form FTB 3840 (initial, then annual) when California property is exchanged for property outside California; check its current instructions, which now include AGI-based exceptions for individuals. | [FTB 3840 (2025)](https://www.ftb.ca.gov/forms/2025/2025-3840.pdf) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Transfer date of the relinquished property | Do not count the 45 and 180 days until the closing statement is in hand |
| Whether the return will be extended | Assume the return due date may cut the 180 days short (Case 1); extend if in doubt |
| QI's prior relationship with the client | Treat as unverified; get a written representation covering the 2-year lookback |
| Depreciation history and cost segregation | Assume section 1245 components exist if a study was done; get the study before closing |
| Personal use days of a vacation home | The safe harbor is not met until the logs show it |
| Relationship of the buyer or seller | Ask; related-party facts change the treatment and need a referral |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Transfer after 17 October by a calendar-year individual | Day 180 falls after 15 April; without an extension the exchange period ends early |
| Proceeds paid to the client or the client's attorney | Actual or constructive receipt defeats the exchange |
| More than 3 properties identified and over 200% | Needs the 95% rescue or the identification fails |
| Cost-segregation study on the relinquished property | Recapture can be due with no cash boot |
| Related party on either side | 2-year rule and anti-abuse rule; refer |
| Relinquished property in one state, replacement in another | State claw-back or annual filing (for example California Form 3840) |

## Worked cases

Cases 2, 3 and 4 use the IRS's own example figures, from the page linked in each heading. Cases 1, 5, 6 and 7 are made up for illustration. The rules they test come from the linked sources.

**Case 1: when the 180 days outrun the return due date ([26 U.S.C. 1031(a)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm); [IRS extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).** A calendar-year individual transfers the relinquished rental on 15 November 2026. Day 45 is 30 December 2026. Day 180 is 14 May 2027. The 2026 return is due 15 April 2027, earlier than day 180, so without an extension the exchange period ends on 15 April 2027. To keep the full window, request an extension by 15 April 2027, which moves the due date to 15 October 2027; the 180-day limit then controls. The extension moves only the filing date, not the date tax must be paid. Rule of thumb: a transfer on 17 October has day 180 on 15 April of the next year, so a calendar-year individual who transfers after 17 October needs the extension. Entities with an earlier due date reach this point sooner, so use the transferor's own due date.

**Case 2: cash and a mortgage as boot ([Pub. 544, Partially Nontaxable Exchanges](https://www.irs.gov/publications/p544)).** Investment real estate: FMV USD 110,000, adjusted basis USD 80,000. It is exchanged for real estate worth USD 100,000 plus USD 10,000 cash. Exchange expenses are USD 5,000. Amount realized: USD 105,000. Realized gain: USD 25,000. Recognized gain: cash USD 10,000 minus expenses USD 5,000 = USD 5,000. Deferred gain: USD 20,000. Basis of the new real estate (Form 8824 line 18 + line 23 - line 15): USD 80,000 + USD 5,000 - USD 5,000 = USD 80,000, which equals FMV USD 100,000 minus the deferred USD 20,000. Variant: the old property carried a USD 30,000 mortgage that the other party assumes. Realized gain becomes USD 55,000. Recognized gain becomes USD 35,000: USD 10,000 cash plus USD 30,000 debt relief, minus USD 5,000 expenses.

```oa-check
name: Section 1031 boot, cash and debt relief (Pub. 544 example)
inputs:
  fmv_given: 110000
  basis_given: 80000
  cash_received: 10000
  expenses: 5000
  debt_relief_variant: 30000
steps:
  - realized: fmv_given - expenses - basis_given
  - boot: max(cash_received - expenses, 0)
  - recognized: min(realized, boot)
  - deferred: realized - recognized
  - new_basis: basis_given + recognized - boot
  - realized_variant: fmv_given + debt_relief_variant - expenses - basis_given
  - recognized_variant: min(realized_variant, cash_received + debt_relief_variant - expenses)
expected:
  realized: 25000.00
  recognized: 5000.00
  deferred: 20000.00
  new_basis: 80000.00
  realized_variant: 55000.00
  recognized_variant: 35000.00
```

**Case 3: Form 8824 lines with section 1245 real property ([Instructions for Form 8824 (2026), Lines 15 to 25](https://www.irs.gov/pub/irs-pdf/i8824.pdf)).** Taylor's building: FMV USD 220,000, adjusted basis USD 100,000, mortgage USD 80,000. Taylor receives Finley's building (FMV USD 250,000, mortgage USD 150,000, assumed by Taylor) plus USD 40,000 cash. Line 15: USD 40,000 (the USD 80,000 Finley assumed is not added, because it does not exceed the USD 150,000 Taylor assumed). Line 16: USD 250,000. Line 17: USD 290,000. Line 18: USD 100,000 basis plus the USD 70,000 net debt Taylor took on = USD 170,000. Line 19: USD 120,000 realized gain. Line 20: USD 40,000 recognized. Section 1245 real property inside Taylor's building has USD 35,000 of depreciation. Line 21: USD 35,000 ordinary income, because that is smaller than USD 40,000 plus the USD 250,000 FMV of non-section 1245 property received. Line 22: USD 5,000. Line 23: USD 40,000. Line 24: USD 80,000 deferred. Line 25 (basis): USD 170,000 + USD 40,000 - USD 40,000 = USD 170,000.

**Case 4: related party sells within 2 years ([Pub. 544, Like-Kind Exchanges Between Related Persons](https://www.irs.gov/publications/p544)).** In December 2024, a taxpayer exchanged business real property (FMV USD 200,000, basis USD 65,000) plus USD 15,000 cash for a sister's business real property (FMV USD 215,000, basis USD 70,000). The taxpayer realized USD 135,000 of gain and recognized none, and took a basis of USD 80,000. The sister realized USD 145,000 and recognized USD 15,000. In 2025, within 2 years, the taxpayer sold the property to a third party for USD 220,000. The taxpayer reports the USD 135,000 deferred gain on the 2025 return, as well as the gain on the 2025 sale. The sister reports USD 130,000 on her 2025 return and increases her basis to USD 200,000. None of the exceptions applies.

**Case 5, a decision: over-identification and the 95% rule ([Treas. Reg. 1.1031(k)-1(c)(4)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf)).** The relinquished property is worth USD 600,000 on the transfer date. The 200% ceiling is USD 1,200,000. Four candidates at USD 300,000 each total USD 1,200,000, which does not exceed the ceiling, so the identification is valid. A fifth candidate brings the total to USD 1,500,000: more than 3 properties and more than 200%, so it is over-identified. It is rescued only if the taxpayer receives identified property worth at least USD 1,425,000 (95%) by the end of the exchange period, which in practice means all five. Advise identifying the four, not five.

```oa-check
name: Section 1031 identification, 200% and 95% tests
inputs:
  relinquished_fmv: 600000
  candidate_fmv: 300000
steps:
  - ceiling_200: relinquished_fmv * 2
  - four_identified: candidate_fmv * 4
  - four_within_200: ceiling_200 - four_identified
  - five_identified: candidate_fmv * 5
  - over_by: five_identified - ceiling_200
  - must_receive_95: five_identified * 0.95
expected:
  ceiling_200: 1200000.00
  four_identified: 1200000.00
  four_within_200: 0.00
  five_identified: 1500000.00
  over_by: 300000.00
  must_receive_95: 1425000.00
```

**Case 6: vacation home as replacement property ([Rev. Proc. 2008-16](https://www.irs.gov/pub/irs-drop/rp-08-16.pdf)).** In the first 12 months after the exchange, a beach condo is rented at a fair rental for 200 days, and the owner stays 25 days. The personal-use limit is the greater of 14 days or 10% of 200 days (20 days), so it is 20 days. 25 days is over the limit, so the safe harbor fails for that period. The taxpayer can still argue investment intent on the facts, but without the safe harbor; if the return already reported the exchange and the unit does not meet the standards, the Rev. Proc. says to file an amended return. If instead the owner stayed 14 days, and the same test is met in the second 12-month period with 24 months of ownership, the safe harbor applies.

**Case 7: reverse exchange timing ([Rev. Proc. 2000-37](https://www.irs.gov/pub/irs-drop/rp-00-37.pdf)).** An EAT takes title to the replacement on 2 March 2026. The written agreement must be signed by 9 March 2026 (5 business days). The relinquished property must be identified by 16 April 2026 (day 45). The replacement must reach the taxpayer, or the relinquished property must be sold to an unrelated buyer, by 29 August 2026 (day 180). If the taxpayer owned the replacement at any time in the 180 days before 2 March 2026, the safe harbor does not treat it as received in an exchange.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-1031-RELATED | Exchange with a related party, or a related party is the seller of the replacement | Refer: 2-year monitoring, the section 1031(f)(4) anti-abuse rule and Rev. Rul. 2002-83 facts |
| R-1031-REVERSE | Reverse and build-to-suit exchanges outside the exact Rev. Proc. 2000-37 terms | Refer: the IRS draws no inference on parking arrangements outside the safe harbor |
| R-1031-TIC | Tenancy-in-common (TIC) interests | Refer. Rev. Proc. 2002-22 only sets conditions for asking for a ruling (its 15 conditions include no partnership return, unanimous approval of major decisions and pro rata sharing of revenue and costs) and says its guidelines "are not intended to be substantive rules and are not to be used for audit purposes". Do not call it a safe harbor; a failed TIC is a partnership interest, which never qualifies |
| R-1031-DROPSWAP | "Drop and swap" and "swap and drop" partnership structures | Refer: no official safe harbor or minimum holding period exists |
| R-1031-MULTI | Multi-asset exchanges (exchange groups and residual groups under Reg. 1.1031(j)-1) | Refer: the IRS says not to complete lines 12 to 18 and to attach a statement instead |
| R-1031-QI | QI default or bankruptcy (Rev. Proc. 2010-14), missed deadlines, disaster postponements | Refer: relief depends on the specific IRS notice |
| R-1031-FOREIGN | US possessions, foreign property, section 1033 condemnations | Refer |
| R-1031-COMBO | Combining an exchange with Opportunity Zone deferral, section 1062 farmland deferral or an installment sale | Refer |
| R-1031-FACTS | Whether a short-held or recently converted property was "held for investment", whether the taxpayer is a dealer, and any state's treatment | Do not state as settled: name the fact pattern and the official source to check |

## Filing and payment

- **Form 8824** is filed with the return for the year the relinquished property was transferred, even if no gain is recognized. For a related-party exchange, file it for the 2 years after the exchange year as well (complete Parts I and II). Several exchanges can go on one summary Form 8824 with an attached statement for each. Source: [Instructions for Form 8824 (2026), When To File](https://www.irs.gov/pub/irs-pdf/i8824.pdf).
- **Line 5** is the date of written identification, or the receipt date if the property was received within 45 days. **Line 6** is the receipt date. **Line 7** is the related-party question. **Lines 11a to 11c** are the related-party exceptions.
- **Where recognized gain goes:** gain on business property goes to Form 4797 line 5 or 16. Gain on capital assets goes to Schedule D, dated the date of the exchange. If the installment method applies, it goes to Form 6252.
- **Home cases:** write "Section 121 exclusion" and the amount in the space on line 19 (on paper or e-filed), do not reduce line 19 by it, and follow the adjusted steps for lines 20 and 25. Line 25b includes like-kind section 1252, 1254 and 1255 property.
- **Deadlines and payment:** the 2026 individual return is due 15 April 2027; an extension moves the filing date to 15 October 2027, not the payment date ([IRS extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)). For a transfer in late 2025, check whether the 2025 return was extended: if not, the exchange period ended on 15 April 2026 and replacement property received after that date is not like-kind property.

## Completion checklist

- Both properties are real property under Reg. 1.1031(a)-3, held for business or investment, not held primarily for sale, and both in the US or both foreign.
- A home or vacation home was tested under Rev. Proc. 2005-14 or Rev. Proc. 2008-16, with all the conditions.
- The QI is not a disqualified person: 2-year agent lookback, related persons at 10%. The exchange agreement limits access to funds to the (g)(6) events only.
- The written identification was signed, delivered to a proper person and clearly described, by day 45, within the 3-property, 200% or 95% rules.
- The replacement was received by the earlier of day 180 or the return due date including extensions, and an extension was filed where needed.
- For a reverse exchange: the 5-business-day agreement, bona fide intent, 45 and 180 days, the combined 180-day limit, and no ownership in the 180 days before the transfer to the EAT.
- Boot, the liability netting and the exchange expenses tie to Form 8824 lines 15 to 20. Recapture (including cost-segregated components) is on line 21, and basis is on line 25 and split on lines 25a to 25c.
- Related party: 2-year monitoring is calendared, including suspension periods. Form 8824 is diarized for the next 2 years.
- The depreciation of exchanged basis and excess basis is set up, or the election out was made on Form 4562 by the due date.
- State treatment (for example California Form 3840) was checked on each relevant state's own site, and the refer items were sent on.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 1031 (govinfo). Read for (a)(2), (a)(3) 45 and 180 days, (b) and (c) boot, (e), (f) and (g) related parties, (h) foreign property and the 2017 amendment note. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1031.htm | 2026-11-13 |
| 26 U.S.C. 121 (govinfo). Read for (b)(1) USD 250,000 and (d)(10) the 5-year rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec121.htm | 2026-11-13 |
| Treas. Reg. 1.1031(k)-1 (govinfo, CFR 2025). Read for (c)(4) 3-property, 200% and 95% rules, (c)(5) 15% incidental property, (g)(6) and (k) disqualified persons. | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031k-1.pdf | 2026-11-13 |
| Treas. Reg. 1.1031(a)-3 (govinfo, CFR 2025). Read for the definition of real property. | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031a-3.pdf | 2026-11-13 |
| Treas. Reg. 1.1031(d)-2 (govinfo, CFR 2025). Read for liability netting. | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1031d-2.pdf | 2026-11-13 |
| Treas. Reg. 1.168(i)-6 (govinfo, CFR 2025). Read for exchanged and excess basis and the election out. | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol3/pdf/CFR-2025-title26-vol3-sec1-168i-6.pdf | 2026-11-13 |
| Instructions for Form 8824 (2026, dated 9 November 2026). Read for What's New (end of QOF deferral on 31 December 2026), Reminders (line 19 write-in, line 25b), section 1062, real property only, When To File, lines 5 to 25 and the IRS examples. | https://www.irs.gov/pub/irs-pdf/i8824.pdf | 2026-11-13 |
| Form 8824 (2026). Read for Parts I to III. | https://www.irs.gov/pub/irs-pdf/f8824.pdf | 2026-11-13 |
| IRS Pub. 544 (2025). Read for identification, QEAA, build-to-suit, constructive receipt, exchange expenses, related persons and the boot examples. | https://www.irs.gov/publications/p544 | 2026-11-13 |
| Rev. Proc. 2000-37 and Rev. Proc. 2004-51. Read for the QEAA terms and the 180-day prior-ownership bar. | https://www.irs.gov/pub/irs-drop/rp-00-37.pdf | 2026-11-13 |
| Rev. Proc. 2008-16. Read for the 14 days and 10% vacation home safe harbor. | https://www.irs.gov/pub/irs-drop/rp-08-16.pdf | 2026-11-13 |
| Rev. Proc. 2005-14. Read for the section 121 and 1031 stacking. | https://www.irs.gov/pub/irs-drop/rp-05-14.pdf | 2026-11-13 |
| Rev. Proc. 2002-22. Read for the TIC ruling conditions and "not to be used for audit purposes". | https://www.irs.gov/pub/irs-drop/rp-02-22.pdf | 2026-11-13 |
| Rev. Proc. 2018-58, section 17. Read for the 120-day disaster postponement. | https://www.irs.gov/pub/irs-drop/rp-18-58.pdf | 2026-11-13 |
| California FTB 3840 (2025). Read for the initial, annual and final filings and the AGI note. | https://www.ftb.ca.gov/forms/2025/2025-3840.pdf | 2026-11-13 |
| CCA 202124008. Read for exchanges of Bitcoin, Ether and Litecoin completed before 1 January 2018. | https://www.irs.gov/pub/irs-wd/202124008.pdf | 2026-11-13 |
| IRS extensions page. Read for the 15 October extended due date. | https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-13 |

Not yet confirmed: the 2026 edition of Pub. 544 was not yet published when read (the 2025 edition is relied on); California's 2026 FTB 3840 and its AGI exceptions were not read in full and belong to the California skill.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-section-1031-like-kind-exchange` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-section-1031-like-kind-exchange. If neither is available, confirm every figure against the official source pages cited above before relying on it.
