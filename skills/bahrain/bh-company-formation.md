---
name: bh-company-formation
description: "Company formation and entity choice in Bahrain, 2026: W.L.L., closed and public shareholding companies, partnerships, branches, individual establishments and Sijili, with minimum capital and commitments from the Sijilat portal. Use for questions like how to set up a company in Bahrain, minimum capital W.L.L. Bahrain, or can a foreigner own 100% in Bahrain."
jurisdiction: BH
tax_year: 2026
last_updated: 2026-11-01
version: 0.3
category: formation
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Company Formation and Entity Choice v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders selecting a Bahrain legal form in 2026. Sijilat Business Types is the official administrative guide read here. Its entity-level ownership statements do not establish that every licensed activity permits foreign ownership. Obtain activity-specific approval before committing capital.

## Rates, bands and thresholds

| Entity | Minimum capital and key rule | Source URL |
|---|---|---|
| W.L.L. | No minimum capital. All shares fully paid at incorporation. One individual or company can own it. No insurance, banking or investing others' funds | https://www.sijilat.bh/guides-laws/BusinessTypes.aspx |
| B.S.C. (public) | BHD 1,000,000; at least two founders; board of at least five | same |
| B.S.C. (closed) | BHD 50,000; at least two persons; board of at least three; at least 50% deposited, rest within three years | same |
| Commandite by shares | BHD 20,000; at least four founders | same |
| Partnership, simple commandite | No minimum capital; at least two partners | same |
| Foreign branch or representative office | Head office in Bahrain required; audited annual budget; a representative office may not deal directly with clients | same |
| Individual establishment | Nationality and Bahrain residence eligibility require the Sijilat individual-establishment checks; age 18 or over; one registration per person | same |
| Sijili (virtual) | Bahraini only; no business address; no foreign worker permits | same |

Sijilat's public-company founder rule exempts companies established by or with government. Foreign participation can be limited by sector/activity decisions. A closed B.S.C. requires the balance of subscribed capital within three years. Sijili also excludes an ICR owner or sole W.L.L. partner, and permits a shareholder only if not a manager/director. Traditional individual establishments require the nationality/residence conditions, age threshold and activity approvals stated by Sijilat; private-sector employees need employer authorisation and government employees face the page's restrictions. These conditions must be checked before selecting the form.

## The base

A W.L.L. has no minimum capital under the Sijilat page; all cash and in-kind shares must be distributed and fully paid, with in-kind contributions delivered, before incorporation. It cannot conduct insurance, banking or investment of others' funds. Partnership partners have unlimited joint personal liability. In a simple commandite, general partners have unlimited liability and sleeping partners are limited to their capital but must not manage; a sleeping partner's knowing inclusion in the name can create general-partner liability. A non-profit W.L.L. cannot distribute profit directly or indirectly.

Sijilat lists an auditor, general assembly, management/financial reporting, reserve capital, UBO and AML tasks for W.L.L.s. It permits an auditor solvency letter instead of the financial report unless losses reach half the share capital. It lists retention of W.L.L. business books for ten years. Shareholding forms also have board/governance requirements. The page lists Economic Substance Reports, but their current legal applicability is held rather than imposed automatically.

## Deadlines and filing

Use https://www.sijilat.bh/ to select the legal form and activity. Check activity licences, nationality/ownership restrictions and required documents before filing. A foreign branch deposits the parent's articles and amendments with the Ministry, uses the prescribed branch name and supplies the annual audited financial position; documents must be Arabic or English, or accompanied by a certified Arabic translation. A representative office cannot transact directly with clients. Obtain the Commercial Registration and required activity approvals before operating.

Exact name-reservation validity/fee, portal screens, document checklist for each activity, completion time, payment reference and annual CR renewal procedure are held. Do not quote a cost or completion date from the predecessor.

## Penalties and interest

Sijilat states that people operating a foreign branch before completing registration are personally and jointly liable. No numeric registration fine is verified here.

## Cross-border points

Sijilat states that GCC nationals and foreigners can own the listed company forms; check the separate activity/sector restrictions. A branch is a foreign company's Bahrain operation; a representative office has the narrower non-trading role above. Tax and payroll obligations need the respective domain screens.

## Two worked examples that recompute

Closed B.S.C. subscribed capital BHD 50,000: depositing half initially means BHD 25,000 paid and BHD 25,000 remaining within the three-year limit.
```oa-check
name: Closed BSC initial capital
inputs:
  capital: 50000
steps:
  - initial: capital * 0.5
  - balance: capital - initial
expected:
  initial: 25000
  balance: 25000
```

Decision: founders have BHD 10,000 and an activity allowed for a W.L.L. Compare only statutory minimum capital, before operating capital, licences and fees. The closed B.S.C. shortfall is BHD 40,000; W.L.L. statutory minimum-capital shortfall is zero. This does not prove BHD 10,000 is adequate to operate the business.
```oa-check
name: Entity minimum-capital choice
inputs:
  funds: 10000
steps:
  - closed_bsc_shortfall: max(50000 - funds, 0)
  - wll_statutory_shortfall: max(0 - funds, 0)
expected:
  closed_bsc_shortfall: 40000
  wll_statutory_shortfall: 0
```

## Ask the client first

- Intended activity and required licence?
- Founders' nationality, residence, number and employment status?
- Available capital and intended contribution type?
- Liability, management and ability-to-distribute-profit requirements?
- Local company, operating branch, representative office or individual establishment?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Sijilat Business Types, entire public page and all entity rows/requirements/notes/commitments read in ordinary browser; selective verbatim browser read receipt saved; raw HTML translation data contains stale values and is not substituted for the visible page | https://www.sijilat.bh/guides-laws/BusinessTypes.aspx | 2026-11-01 |

Not yet confirmed: name reservation 60-day validity/about BHD 10 fee; 1-to-3-day/1-to-3-week completion estimates; SPC conversion under Decree-Law 28/2020; current annual CR renewal procedure; exact activity-specific ownership/licensing approvals; automatic ESR applicability. Earlier BHD 20,000 foreign W.L.L. and BHD 250,000 closed B.S.C. minima are contradicted by Sijilat and are not executable. Full predecessor text and exact destinations are preserved in [the country evidence](../../evidence/ledgers/bahrain-20261101/README.md). These are NON-OPERATIVE holds, never defaults or authority to compute.

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
