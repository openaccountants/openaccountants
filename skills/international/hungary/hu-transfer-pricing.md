---
name: hu-transfer-pricing
description: "Hungarian transfer pricing (szokásos piaci ár, transzferár) for tax year 2026: companies and Hungarian branches that deal with related parties. Covers who is related (more than 50% majority influence, common control, PEs, shared management), the arm's length adjustment both ways under Tao. tv. 18. §, the interquartile range and median rule, the new documentation decree 45/2025 (XII. 23.) NGM that replaced 32/2017 from tax year 2026 (local file above HUF 150 million, master file above HUF 500 million, simplified file for low-value services at 5%), the small-enterprise exemption, the ATP data sheets in the corporate tax return, the local business tax (HIPA) follow-on, penalties up to HUF 5 million per missing record, APA fees, country-by-country reporting at EUR 750 million, and MAP. Trigger phrases: transzferár, szokásos piaci ár, kapcsolt vállalkozás, transfer pricing Hungary, fődokumentum, helyi dokumentum, ATP-01. Out of scope: hu-corporate-tax (rate, base, filing), hu-income-tax, hungary-vat-return."
version: 0.1
jurisdiction: HU
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary transfer pricing (szokásos piaci ár): 2026

Source-cited draft: not reviewed by an accountant, not for filing.

**What changed for 2026.** A new ministerial decree, 45/2025. (XII. 23.) NGM rendelet on transfer pricing records and data supply, replaced 32/2017. (X. 18.) NGM rendelet on 23 January 2026 (45/2025, 14. § and 16. §: in force on the 31st day after its 23 December 2025 promulgation). It applies first to records and data supply for tax years starting in calendar 2026 (decree 45/2025, 15. § (1)). The main changes for a typical client:

- The local file (helyi dokumentum) exemption rises from HUF 100 million to **HUF 150 million** per transaction (or aggregated group of transactions) a year (45/2025, 4. § (4) a); old rule: 32/2017, 1. § (2) e)).
- A master file (fődokumentum) is needed only when the transactions that need a local file total **more than HUF 500 million** in the year (45/2025, 4. § (3)).
- Pure cost pass-through recharges are exempt up to HUF 500 million (4. § (4) c)).
- A simplified local file covers low-value services at a **5% net cost plus mark-up** (7. §).
- New rules for database searches: Hungary first, then Czechia, Poland and Slovakia, then the other central and eastern EU states, then the EU (11. § (2)).

For a tax year that started in 2025, the old decree 32/2017 still applies to records due after the new decree came into force, unless the company opts to apply the new decree to some of its 2025 local files (45/2025, 15. § (2)-(3)).

The arm's length rule itself is in Tao. tv. (Act LXXXI of 1996) 18. §. Penalties and the advance pricing procedure are in the Art. (Act CL of 2017); MAP and country-by-country reporting are in the Aktv. (Act XXXVII of 2013). All statute text below was read on the Nemzeti Jogszabálytár at njt.jog.gov.hu, in the version in force from 1 October 2026. The short address njt.hu still refused connections on 2026-10-23. The 9% rate, the tax base, the return and the general penalties are in `hu-corporate-tax`. This skill does not repeat them.

## Who this applies to

**Related parties (kapcsolt vállalkozás, Tao. tv. 4. § 23.).** A taxpayer and another person are related where:

1. the taxpayer has majority influence (többségi befolyás) in the other person, directly or indirectly;
2. the other person has majority influence in the taxpayer;
3. a third person has majority influence in both. Close relatives who hold majority influence in both are treated as one third person;
4. a foreign company and its Hungarian permanent establishment (telephely), its other PEs, and anyone related to the foreign company under 1 to 3;
5. a Hungarian taxpayer and its foreign PE, and that PE and anyone related to the taxpayer;
6. the two share management in a way that gives decisive influence over business and financial policy.

Majority influence follows the Civil Code (Ptk. 8:2. §). It means more than half of the votes, or decisive influence. Decisive influence means being a member with the right to appoint or remove a majority of the directors or supervisory board. It also covers agreements under which other members vote the same way, if together they hold more than half of the votes. Indirect influence counts. The 25% and 50% tests in Tao. tv. 4. § 23. g) apply only to other rules (interest limitation, CFC, hybrids, exit tax), not to transfer pricing.

**The arm's length adjustment (Tao. tv. 18. § (1)-(4), (7))** applies to every taxpayer under the Tao. tv., whatever its size, on every related-party contract. It also covers transactions between a foreign company and its Hungarian PE and between a Hungarian company and its foreign PE (18. § (7)). It also covers non-cash capital contributions, capital reductions, distributions in kind and in-kind dividends between related parties (18. § (6)). A contract with a private individual who is not acting as a sole trader produces no increase (18. § (1) b)).

Two cases are outside 18. § (1)-(2) and (4) altogether (18. § (3)):
- a long-term contract between an SME and a joint purchasing and selling company in which SMEs together hold more than 50% of the votes;
- grants, payments and free transfers to the state or a municipality made under a legal obligation and not repayable.

**The documentation and data supply duty (18. § (5))** applies to business associations (Kft, Zrt, Bt, Kkt), joint ventures (egyesülés), SEs, cooperatives, European cooperatives and foreign companies with a Hungarian PE. It does not apply if, on the last day of the tax year, the taxpayer is a **small enterprise (kisvállalkozás)**. Public-benefit non-profit companies and companies under majority state influence are also exempt.

- A small enterprise has fewer than 50 staff, and net revenue or balance sheet total of at most EUR 10 million in forints (Kkv. tv., Act XXXIV of 2004, 3. § (2)). Micro enterprises count as small (Tao. tv. 4. § 24.).
- A company with linked enterprises adds their figures in full, and partner enterprises (25% or more) in proportion (Kkv. tv. 5. § (5)-(7)). A Hungarian subsidiary of a large group is therefore almost never small.
- Status changes only after two consecutive years over or under the limits (Kkv. tv. 5. § (3)).
- A **medium-sized** enterprise is not exempt. "SMEs are exempt" is a common mistake: only micro and small enterprises are.

**TAO group members** apply 18. § only to dealings with each other that still carry an unmatched adjustment from before they joined. They meet the documentation duty through the group representative (18. § (10), (10a)).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate tax on a transfer pricing adjustment | 9% (see hu-corporate-tax) | 2026 | [Tao. tv. 19. §, njt.jog.gov.hu](https://njt.jog.gov.hu/jogszabaly/1996-81-00-00) |
| Arm's length range | Interquartile range of the comparables, where database or other public data is used | 2026 | [Tao. tv. 18. § (9), 4. § 31e.](https://njt.jog.gov.hu/jogszabaly/1996-81-00-00) |
| Adjustment point when outside the range | Median, unless the taxpayer proves another point in the range fits better | 2026 | [Tao. tv. 18. § (11)-(12)](https://njt.jog.gov.hu/jogszabaly/1996-81-00-00) |
| Local file exemption | Transaction value (aggregated where aggregable) at arm's length price, ex VAT, not above HUF 150,000,000 in the year | 2026 onward (HUF 100,000,000 under the old decree) | [45/2025 NGM rendelet 4. § (4) a), (5)](https://njt.jog.gov.hu/jogszabaly/2025-45-20-2X); [32/2017 NGM rendelet 1. § (2) e)](https://njt.jog.gov.hu/jogszabaly/2017-32-20-2X) |
| Cost pass-through exemption | Unchanged recharge of a cost bought from an unrelated party, up to HUF 500,000,000 | 2026 | [45/2025, 4. § (4) c)](https://njt.jog.gov.hu/jogszabaly/2025-45-20-2X) |
| Master file trigger | Transactions needing a local file total more than HUF 500,000,000 | 2026 | [45/2025, 4. § (3)](https://njt.jog.gov.hu/jogszabaly/2025-45-20-2X) |
| Market analysis can be left out of the local file | Transaction value not above HUF 1,000,000,000 (the economic features of the relevant market, 6. § (3) f) fd), need not be described) | 2026 | [45/2025, 6. § (5)](https://njt.jog.gov.hu/jogszabaly/2025-45-20-2X) |
| Low-value services, simplified local file | Provider earns at least 5% net cost plus; recipient pays a provider earning at most 5% | 2026 | [45/2025, 7. § (1) a)-b)](https://njt.jog.gov.hu/jogszabaly/2025-45-20-2X) |
| Data supply for stock exchange and fixed-price deals (no local file needed) | Only above HUF 500,000,000, and then a short data set | 2026 | [45/2025, 12. § (4)](https://njt.jog.gov.hu/jogszabaly/2025-45-20-2X) |
| Small enterprise (exempt from documentation) | Fewer than 50 staff and revenue or balance sheet total at most EUR 10 million | 2026 | [Kkv. tv. 3. § (2)](https://njt.jog.gov.hu/jogszabaly/2004-34-00-00) |
| Default fine, missing or deficient TP record | Up to HUF 5,000,000 per record; repeat up to HUF 10,000,000 per record; same record missed again, up to 4 times the first fine | 2026 | [Art. 230. §](https://njt.jog.gov.hu/jogszabaly/2017-150-00-00) |
| APA fee (szokásos piaci ár megállapítása) | HUF 10,000,000 unilateral; HUF 14,000,000 bilateral or multilateral; extension or amendment 50%; pre-filing consultation HUF 1,000,000 each | 2026 | [Art. 175. §](https://njt.jog.gov.hu/jogszabaly/2017-150-00-00) |
| Country-by-country report threshold | Group consolidated revenue of EUR 750,000,000 or more in the previous year | 2026 | [Aktv. 2013. évi XXXVII. 4. § 7.17](https://njt.jog.gov.hu/jogszabaly/2013-37-00-00) |
| CbC default fine | Up to HUF 20,000,000 | 2026 | [Aktv. 43/S. §](https://njt.jog.gov.hu/jogszabaly/2013-37-00-00) |
| MAP request deadline | 3 years from notice of the first-instance decision causing the dispute, unless the treaty sets another period | 2026 | [Aktv. 42/A. §, 42/B. § (3)](https://njt.jog.gov.hu/jogszabaly/2013-37-00-00) |

## The taxable base

**The adjustment (Tao. tv. 18. § (1)).** If related parties agree a price (ex VAT) above or below the arm's length price, the pre-tax profit is adjusted by the difference. This is separate from every other adjustment in the Act.

- **Increase (18. § (1) b)).** Required whenever the price makes the Hungarian profit lower than at arm's length: buying too dear or selling too cheap. No document from the other party is needed.
- **Decrease (18. § (1) a)).** Allowed only if all of these hold:
  1. the price made the Hungarian profit higher than at arm's length;
  2. the other party is a Hungarian resident taxpayer, or a foreign person (not a CFC) subject to a tax like corporate tax where it is resident;
  3. the company holds a document signed by both parties showing the difference;
  4. it holds the other party's statement that it has taken (or will take) the difference into account in its own corporate tax base.

  Without these, the overcharge stays taxed in Hungary.

**Methods (18. § (2)).** Comparable uncontrolled price, resale price, cost plus, transactional net margin (TNMM), profit split, or another method if none of these works. The decree lets a company skip justifying TNMM for a contract manufacturer or a routine limited-risk service provider, testing a net cost plus. The same applies to a limited-risk distributor, testing a net margin (45/2025, 6. § (6)-(7)). The decree is written to follow the OECD Transfer Pricing Guidelines (45/2025, preamble [1]).

**Range and median (18. § (9), (11), (12)).**
- Where the analysis uses database or other public comparables, narrow the results to the interquartile range: the middle band holding half the sample.
- If the price is inside the range, no adjustment.
- If it is outside, adjust to the **median**, unless the company proves that another point inside the range fits the transaction best.

**Database searches (45/2025, 11. §).** The final sample must:
- hold identifiable, active, independent companies;
- use data for the three years before the year tested, available for every year (two years where justified);
- exclude companies with losses in at least two consecutive years, or at operating level in more than half the years;
- be screened by primary activity code first (keywords only where justified);
- pass a website check.

Geography steps outward when the sample is too small: Hungary, then Czechia, Poland and Slovakia, then Bulgaria, Estonia, Croatia, Latvia, Lithuania, Romania and Slovenia, then the EU, then wider. Searches are refreshed at least every three years and the financials every year (11. § (8)).

**Local business tax (HIPA).** A company bound by the arm's length rule also measures its HIPA net revenue and its revenue-reducing costs (cost of goods sold, mediated services and so on) at the arm's length price (Htv., Act C of 1990, 39. § (11)). To *reduce* its HIPA revenue or *increase* those costs it needs the other party's statement that it made the mirror HIPA adjustment. If the other party pays no HIPA, the statement must say the adjustment was taken into the equivalent foreign tax, or into corporate tax. The adjustment can be made as one lump sum (39. § (12)).

The practical result:
- An adjustment on sales, goods bought for resale, mediated services, subcontracting or materials changes the HIPA base.
- An adjustment on a management fee, a royalty or interest does not, because those costs never reduce the HIPA base (Htv. 39. § (1)).

**Corresponding (secondary) adjustments abroad** follow the other country's law. A foreign group company that wants relief for a Hungarian increase uses MAP (see Cross-border points).

### What the documentation must contain

For each tax year with a related-party transaction performed, a company under the duty prepares (45/2025, 4. § (1)-(2)):

- **Master file (fődokumentum)**, only above the HUF 500 million trigger: group structure, value drivers, supply chains, main service arrangements, intangibles, financing, financial and tax positions (5. § (1)). If the group's ultimate parent prepares its equivalent later, the Hungarian master file is due by that date, but no later than 12 months after the taxpayer's year end (5. § (2)).
- **Local file (helyi dokumentum)**, per transaction or aggregated transaction. It has a common part prepared once a year and a transaction part. The transaction part covers the contract, the functional analysis, the method, the tested party, the comparables, and a reconciliation of the figures to the books (6. §).
- **Simplified local file (egyszerűsített helyi dokumentum)** (7. §), allowed for:
  - low-value services at the 5% mark-up test;
  - interest-free transfers of funds;
  - unchanged resales or recharges, at the same price, of something bought from an unrelated party, where the group company adds no real function or risk and neither the company nor a related party sells it unchanged to outsiders (7. § (1) d)).

  A low-value service is one that:
  - no group company sells to outsiders;
  - needs and creates no unique and valuable intangible;
  - puts no significant risk on the provider;
  - is not manufacturing or distribution, not financial or insurance, and not extraction of natural resources (2. § (1) 1.).

  Renting property or equipment can qualify (7. § (3)).

**Transactions that need no local file (4. § (4)):**
- annual value at or below HUF 150 million;
- deals covered by a Hungarian APA decision while it binds;
- unchanged cost recharges up to HUF 500 million, where the supplier is unrelated. If the cost is split among several group members, the company must show the split is arm's length (4. § (6));
- stock exchange deals (unless insider dealing or market manipulation, 4. § (7));
- deals at an official fixed price or a price set by law;
- deals with private individuals not acting as sole traders.

The arm's length rule still applies to all of them.

**Aggregation (8. §).** Transactions can be aggregated if comparability is not put at risk, and they either have the same subject and terms or are closely linked. A purchase cannot be aggregated with the sale of goods made from it. A deal where the company is the supplier cannot be aggregated with one where it is the customer. Manufacturing, distribution, services, financing and intangible deals are never aggregated with each other. For the HUF 150 million and HUF 500 million tests, aggregable transactions count together even if the company does not aggregate them (4. § (5)).

**Language, retention and correction.**
- Records can be in Hungarian, English or German (4. § (9)).
- The local file and its annexes are kept for at least 8 years, or 8 years after a fixed asset involved leaves the books (4. § (10)).
- A record can be corrected within the limitation period, but no later than the start of a NAV audit (4. § (8)).

## Deadlines and filing

- **Related-party notification:** report to NAV the name, seat and tax number of each new related party within 15 days after the first contract with it, and the end of the relationship within 15 days (465/2017. (XII. 28.) Korm. rendelet 16. § (4) b)).
- **Documentation:** ready by the time the corporate tax return is filed (Tao. tv. 18. § (5): "a bevallás benyújtásáig"). The return deadline is 31 May 2027 for a calendar 2026 year (see hu-corporate-tax), so a company that files early must have its records ready earlier. It is not filed; NAV asks for it in an audit.
- **Transfer pricing data supply (transzferár-adatszolgáltatás):** made in the corporate tax return itself (Tao. tv. 18. § (5); 45/2025, 12. § and 13. §). For each transaction or aggregated transaction it covers:
  - one of 54 transaction types;
  - the exemption reason, if any, and whether transactions were aggregated;
  - the activity (TEÁOR) code;
  - the counterparty and its tax number and country;
  - the amount booked, in HUF thousands;
  - the signed tax base adjustment;
  - the method and the tested party;
  - the profit level indicator, the arm's length value or range, the result actually reached, and the accounting standard;
  - for financing, the reference rate and margin.

  Transactions at or below HUF 150 million give no data at all (12. § (2)). Low-value services give a short data set (12. § (5)).
- **Which sheets.** In the 2025 return the data went on sheets **2529-ATP-01** and **2529-ATP-KV**, under the old decree's 8/A. §. Line 57 of the main sheet declares whether the company must supply data, or why it is exempt ([NAV guide to form 2529](https://nav.gov.hu/pfile/file?path=/nyomtatvanyok/letoltesek/nyomtatvanykitolto_programok/nyomtatvanykitolto_programok_nav/2529/2529-kitoltesi-utmutato), pages 242 to 251). The 2629 return for 2026 had not been published on 2026-10-23. The data content for 2026 is set by 45/2025, 12. § and 13. §; the sheet names and line numbers for 2026 are not confirmed.
- **APA:** filed electronically with the Minister for tax policy, not NAV, before the transactions take place. A request for a deal already performed is rejected. The procedure takes 120 days, extendable twice by 90 days. Talks with a foreign authority have 2 years, extendable by 1 year, and that time does not count toward the 120 days. The decision covers 3 to 5 full tax years and can be extended once by 3 years if asked at least 6 months before it expires. There is no appeal. A bilateral APA can roll back to open years (Art. 174. § to 183. §). If the request is rejected or ended, 85% of the fee is refunded, except in the cases in 175. § (3a).
- **CbC:**
  - Every Hungarian member of an in-scope group notifies NAV by the last day of the group's reporting year. The notice states whether the member files the report and, if not, who does (Aktv. 43/O. §).
  - A Hungarian ultimate parent, or a member required to file as a surrogate, files the report within 12 months after the end of the reporting year (Aktv. 43/N. § (8)).

## Penalties and interest

- **Missing or deficient TP record (Art. 230. §).** A default fine of up to HUF 5,000,000 per record (or aggregated record) for failing to prepare or keep it. For a repeat breach, up to HUF 10,000,000 per record. If the same record is missed again, up to four times the first fine. The repeat rules lapse if more than two years pass between two failures. If the record is completed before the repeat-penalty decision is notified, the fine can be reduced or waived. The figures in some secondary sources (HUF 2 million and HUF 4 million) are out of date.
- **Tax shortfall from an adjustment.** The extra corporate tax carries the tax penalty of 50% of the shortfall (Art. 215. § (3)), or 200% where the shortfall is tied to hidden income or false or destroyed records (215. § (4)), plus late payment interest at the central bank base rate plus 5 points, per day (Art. 209. § (1)). A self-revision before an audit replaces both with the self-revision surcharge. The figures and sources are in hu-corporate-tax.
- **CbC failures.** Up to HUF 20,000,000 (Aktv. 43/S. §).

## Cross-border points

- **Mutual agreement procedure (MAP).**
  - **Who decides:** the Hungarian competent authority for treaty MAP and for EU dispute resolution is the Minister for tax policy, not NAV (Aktv. 42/B. § (1), 41/B. § (1)). There is no appeal against its decision (42/B. § (1a)).
  - **Treaty partners:** request MAP under the relevant tax treaty and Aktv. chapter IV/A. The general deadline is 3 years from notice of the first-instance decision that causes the dispute, whether or not domestic appeals are used (Aktv. 42/B. § (3)). A different period in the treaty takes precedence (42/A. §), so check the treaty.
  - **EU disputes:** the Dispute Resolution Directive (2017/1852) route under Aktv. chapter III/A has the same 3-year limit (Aktv. 41/B. § (3)). The EU Arbitration Convention route remains available (Aktv. 42. §).
  - **What to send:** a company under the TP documentation duty must send its TP records with the request (Aktv. 42/C. § (1) h)).
  - **Limitation:** a request can be made after the domestic limitation period has run (Art. 205. § (1)). For tax years starting before 1 January 2018 the request had to reach the authorities within the limitation period, unless the treaty says otherwise (205. § (2)).
- **Branches.** Dealings between a foreign company and its Hungarian PE are priced at arm's length (18. § (7)). If a treaty exempts the PE's result from Hungarian tax, the documentation duty falls away (18. § (8), (8a)). Hungarian PE profit rules are in hu-corporate-tax.
- **Low-tax and CFC counterparties.** No downward adjustment is allowed toward a CFC (18. § (1) ab)). The CFC rule and the deduction limits on payments to CFCs are in hu-corporate-tax.
- **Exit and restructuring.** Moving functions, assets or a business out of Hungary can trigger exit tax (Tao. tv. 16/A. §, see hu-corporate-tax). It is also its own transaction type in the TP data supply (45/2025, 13. § (2) 50.).
- **Pillar Two.** Groups at or above EUR 750 million also face the Hungarian top-up tax returns. See hu-corporate-tax; this skill does not cover them.

## Worked examples

### Example 1: a management fee above the range, adjusted to the median

Balaton Kft is a medium-sized Hungarian distributor (180 staff) owned 100% by an Austrian parent. In 2026 the parent charges it a management fee: the parent's cost of HUF 200,000,000 plus a 15% mark-up. Balaton's database study of independent service providers gives a net cost plus range of 4% (lower quartile) to 10% (upper quartile), median 7%.

1. Fee charged: 200,000,000 x 1.15 = HUF 230,000,000.
2. Upper end of the range: 200,000,000 x 1.10 = HUF 220,000,000. The fee is HUF 10,000,000 above the range, so 18. § (12) applies.
3. Fee at the median: 200,000,000 x 1.07 = HUF 214,000,000.
4. Balaton paid too much, so its profit is too low. It must increase its pre-tax profit by 230,000,000 - 214,000,000 = HUF 16,000,000 (18. § (1) b)). No statement from the parent is needed for an increase.
5. Extra corporate tax at 9%: HUF 1,440,000.
6. HIPA: a management fee does not reduce the HIPA base (only cost of goods, mediated services, subcontractors, materials and R&D do), so there is no HIPA effect. Had the overcharge been on goods bought for resale, the HIPA base would rise too (Htv. 39. § (11)).
7. Documentation: the fee is above HUF 150,000,000, so a local file is needed by 31 May 2027. It is not a low-value service at 5% or less, so the simplified file is not available. The documented total is below HUF 500,000,000, so no master file unless other documented deals bring the total above it.
8. If NAV finds the adjustment on audit rather than Balaton making it, the general 50% tax penalty applies to the shortfall, plus late payment interest. The parent can then ask Austria for relief under MAP.

```oa-check
name: Balaton Kft, management fee above the interquartile range, 2026
inputs:
  parent_cost: 200000000
  markup_charged: 0.15
  upper_quartile: 0.10
  median: 0.07
  cit_rate: 0.09
  hipa_rate: 0.02
  hipa_relevant_adjustment: 0
  local_file_threshold: 150000000
  master_file_threshold: 500000000
  audit_penalty_rate: 0.50
steps:
  - fee_charged: parent_cost * (1 + markup_charged)
  - range_top: parent_cost * (1 + upper_quartile)
  - excess_over_range: fee_charged - range_top
  - fee_at_median: parent_cost * (1 + median)
  - adjustment: fee_charged - fee_at_median
  - extra_cit: adjustment * cit_rate
  - extra_hipa: hipa_relevant_adjustment * hipa_rate
  - over_local_file_threshold: fee_charged - local_file_threshold
  - master_file_headroom: master_file_threshold - fee_charged
  - penalty_if_found_on_audit: extra_cit * audit_penalty_rate
expected:
  fee_charged: 230000000
  range_top: 220000000
  excess_over_range: 10000000
  fee_at_median: 214000000
  adjustment: 16000000
  extra_cit: 1440000
  extra_hipa: 0
  over_local_file_threshold: 80000000
  master_file_headroom: 270000000
  penalty_if_found_on_audit: 720000
```

### Example 2: a HUF 120 million purchase, and low-value services at 5%

Mecsek Zrt has 120 staff, so it is not a small enterprise and has the documentation duty. In both 2025 and 2026 it buys components from a German sister company for HUF 120,000,000 a year. In 2026 it also provides back-office services (payroll, bookkeeping) to group companies. These services meet the low-value definition. Its cost for them is HUF 180,000,000, charged at cost plus 5%.

1. Components, 2026: HUF 120,000,000 is HUF 30,000,000 below the HUF 150,000,000 threshold. No local file is needed (45/2025, 4. § (4) a)) and no data goes on the ATP sheets (12. § (2)). The price must still be arm's length, and NAV can still adjust it.
2. Components, 2025: the old threshold was HUF 100,000,000 (32/2017, 1. § (2) e)). HUF 120,000,000 is HUF 20,000,000 above it, so under the old decree a local file was due by the time the 2025 return was filed (31 May 2026 at the latest). Whether opting into 45/2025 for that local file (15. § (2)) also brings in the HUF 150 million exemption is not settled (see Not yet confirmed), so prepare the file.
3. Services, 2026: fee 180,000,000 x 1.05 = HUF 189,000,000. That is HUF 39,000,000 above HUF 150,000,000, so a local file is needed. The two cannot be aggregated: Mecsek is the customer in one and the supplier in the other (8. § (2)), and services are never aggregated with other transaction categories (8. § (3)).
4. Mecsek, as provider, actually earns exactly 5%, which meets the "at least 5%" test in 7. § (1) a). It may prepare the simplified local file and gives only the short data set (12. § (5)). At 4.9% it would need a full local file.
5. Master file: the transactions needing a local file total HUF 189,000,000, HUF 311,000,000 below the HUF 500,000,000 trigger, so none is due.

```oa-check
name: Mecsek Zrt, HUF 120m purchase and low-value services, 2025 and 2026
inputs:
  goods_purchase: 120000000
  lf_threshold_2026: 150000000
  lf_threshold_2025: 100000000
  service_cost: 180000000
  service_markup: 0.05
  low_value_min_markup: 0.05
  mf_threshold: 500000000
steps:
  - goods_headroom_2026: lf_threshold_2026 - goods_purchase
  - goods_excess_2025: goods_purchase - lf_threshold_2025
  - service_fee: service_cost * (1 + service_markup)
  - service_over_threshold: service_fee - lf_threshold_2026
  - markup_margin_over_minimum: service_markup - low_value_min_markup
  - documented_total_2026: service_fee
  - mf_headroom: mf_threshold - documented_total_2026
expected:
  goods_headroom_2026: 30000000
  goods_excess_2025: 20000000
  service_fee: 189000000
  service_over_threshold: 39000000
  markup_margin_over_minimum: 0
  documented_total_2026: 189000000
  mf_headroom: 311000000
```

## Ask the client first

1. Who owns the company, directly and through any chain, and who sits on its board? Are there sister companies, foreign PEs, or shareholders who are private individuals?
2. On the last day of the tax year, is it a small enterprise once linked enterprises' staff, revenue and balance sheet are added in?
3. List every related-party flow for the year with its value ex VAT: goods, services, royalties, loans, guarantees, cash pool, recharges and capital transactions. Which can be aggregated?
4. Do any services meet the low-value definition, and what mark-up is actually earned or paid?
5. Has any related party been reported to NAV within 15 days of the first contract? Is there an APA, a foreign APA or ruling, or a pending audit or MAP?
6. Is the group's consolidated revenue EUR 750 million or more, and who files the CbC report?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tao. tv. (Act LXXXI of 1996), 4. § 23., 24., 31e., 18. §, 19. §; Nemzeti Jogszabálytár, version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/1996-81-00-00 | 2026-10-23 |
| 45/2025. (XII. 23.) NGM rendelet on transfer pricing records and data supply | https://njt.jog.gov.hu/jogszabaly/2025-45-20-2X | 2026-10-23 |
| 32/2017. (X. 18.) NGM rendelet (repealed January 2026; applies to 2025 records) | https://njt.jog.gov.hu/jogszabaly/2017-32-20-2X | 2026-10-23 |
| Art. (Act CL of 2017), 174. § to 183. § (APA), 205. § (MAP and limitation), 209. § (late interest), 215. § (tax penalty) and 230. § (fines); version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 | 2026-10-23 |
| Aktv. (Act XXXVII of 2013), 4. § 7.17, 41/B. §, 42. §, 42/A. § to 42/C. §, 43/N. § to 43/S. § | https://njt.jog.gov.hu/jogszabaly/2013-37-00-00 | 2026-10-23 |
| Htv. (Act C of 1990), 39. § (1), (11), (12) | https://njt.jog.gov.hu/jogszabaly/1990-100-00-00 | 2026-10-23 |
| Kkv. tv. (Act XXXIV of 2004), 3. § and 5. § | https://njt.jog.gov.hu/jogszabaly/2004-34-00-00 | 2026-10-23 |
| 465/2017. (XII. 28.) Korm. rendelet, 16. § (4) b) | https://njt.jog.gov.hu/jogszabaly/2017-465-20-22 | 2026-10-23 |
| Ptk. (Act V of 2013), 8:2. § (net.jogtar.hu, commercial reprint; the official page loaded without Book Eight) | https://net.jogtar.hu/jogszabaly?docid=a1300005.tv | 2026-10-23 |
| NAV information sheet 41: key rules of corporate tax, section 5.13 (2 February 2026) | https://nav.gov.hu/ugyfeliranytu/nezzen-utana/inf_fuz/2026/41.-A-tarsasagi-ado-legfontosabb-szabalyai-2026.02.02 | 2026-10-23 |
| NAV guide to the 2529 return (tax year 2025), ATP sheets and line 57 | https://nav.gov.hu/pfile/file?path=/nyomtatvanyok/letoltesek/nyomtatvanykitolto_programok/nyomtatvanykitolto_programok_nav/2529/2529-kitoltesi-utmutato | 2026-10-23 |
| NAV: information on mutual agreement procedures (dated 21 September 2020; NAV marks it archived and out of force since 29 December 2024; not relied on) | https://nav.gov.hu/ado/egyeb/map_tajekoztato | 2026-10-23 |
| Nemzeti Jogszabálytár short address (official) | https://njt.hu/jogszabaly/1996-81-00-00 | 2026-10-23: connection refused; the same database answered at njt.jog.gov.hu |

Not yet confirmed: the layout of the 2629 return's transfer pricing sheets for tax year 2026 (not yet published by NAV); whether a 2025 taxpayer opting into 45/2025 under its 15. § (2) can also use the HUF 150 million local file exemption for 2025, or only the new content rules; the Ptk. 8:2. § text on the official site (read in the net.jogtar.hu reprint only); NAV's audit practice on choosing a point other than the median; MAP filing details now that the Minister is the competent authority (whether NAV's TPMAP form is still used, whether the request is free of fees, and which treaties set a 2-year deadline: NAV's archived 2020 guide named Canada, Indonesia, the Philippines and Portugal); whether a request is accepted where a good-faith foreign self-revision caused the double taxation (stated only in the archived NAV guide).

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
