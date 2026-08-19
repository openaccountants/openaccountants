---
name: charity-nonprofit
description: "Use this skill whenever a charity, nonprofit, foundation, NGO, religious organisation, or social enterprise asks about accounting / tax / reporting specific to the nonprofit sector. Trigger on phrases like \"501(c)(3)\", \"private foundation\", \"public charity\", \"UBI\", \"unrelated business income\", \"Form 990\", \"Form 990-PF\", \"CIO\", \"Charity Commission\", \"FRS 102 SORP\", \"Charities SORP\", \"fund accounting\", \"restricted vs unrestricted\", \"gift aid\", \"Public Benefit Test\", \"PBO\", \"Section 18A\", \"trustees report\", \"donor-advised fund\", \"DAF\", \"private operating foundation\", \"minimum distribution requirement\", \"5% payout\", \"self-dealing\", or any nonprofit-sector question. Covers US §501(c) exemption / Form 990 series, UK CIO / Charities Act 2011 / Charities SORP (FRS 102), EU foundation regimes, fund accounting, and the unrelated business income (UBI) / VAT exemption complications. Does NOT cover: fundraising regulation, donor management, or governance procedure beyond tax accounting."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Charity Nonprofit

## What this file is

A sector overlay for charities, nonprofits, foundations, NGOs, religious organisations, and social enterprises.

## Section 1 — Common entity types and exemption regimes

### 1.1 United States

**[T1] IRC §501(c) categories**

| Code | Type | Notable |
| --- | --- | --- |
| **§501(c)(3)** | Charitable, religious, educational, scientific, literary | Donations deductible; public charity vs private foundation |
| **§501(c)(4)** | Social welfare; advocacy organisations | Donations NOT deductible; political activity permitted |
| **§501(c)(6)** | Business leagues, trade associations | Member dues deductible as business expense |
| **§501(c)(7)** | Social clubs | Member-only |
| **§501(c)(19)** | Veterans organisations |  |
| **§4947(a)(1)** | Charitable trusts |  |

- **Public charity vs private foundation - public charity** — Public charity: significant public support (>1/3 from broad public or government); fewer restrictions  _([T1])_
- **Public charity vs private foundation - private foundation restrictions** — Private foundation: typically family-funded; subject to 5% minimum payout (§4942), self-dealing rules (§4941), excess business holdings (§4943), prohibited investments (§4944), taxable expenditures (§4945)  _([T1])_
- **Net investment income excise tax** — 1.39% percent (previously 2% / 1% two-tier; flattened by TCJA + Inflation Reduction Act amendments)  _(§4940)_
- **Filing requirements** — Form 1023 / 1024 application; Form 990 (public charity) / 990-PF (private foundation) / 990-EZ (small) / 990-N (smallest); Form 990-T for UBI; Schedule A (public support test); Schedule B (large donors)  _([T1])_

### 1.2 United Kingdom

- **Charity (CIO / trust / company limited by guarantee)** — Charitable Incorporated Organisation — CIO, or trust, or company limited by guarantee  _(Charities Act 2011)_
- **Public Benefit Test** — Purposes must be charitable and operate for public benefit (post-Charities Act 2006 affirmation)  _([T1])_
- **Charity Commission** — Registers and regulates charities  _([T1])_
- **Charity tax exemptions** — Trading income generally exempt if primary purpose trading; ancillary trading limit per Extra-Statutory Concession C4  _([T1])_
- **Gift Aid top-up** — 25% percent (top-up on donor donations (HMRC reclaims basic-rate tax))  _([T1])_
- **Charities SORP** — Statement of Recommended Practice under FRS 102 — sector-specific accounting  _([T1])_

### 1.3 Germany

- **Gemeinnützige Körperschaft** — Charitable corporation under §§51-68 AO  _([T1])_
- **Spendenrecht** — Donations deductible by donor up to 20% AGI / 4 per mille turnover (companies)  _([T1])_
- **Categories** — gemeinnützig (charitable), mildtätig (relieving distress), kirchlich (religious)  _([T1])_
- **Filing** — Steuererklärung + verbindliche Bestätigung from Finanzamt  _([T1])_

### 1.4 EU foundation regimes

[T1] Country-specific; harmonisation limited. Major regimes:
- **Netherlands** — ANBI (Algemeen Nut Beogende Instelling)
- **France** — Fondation d'utilité publique; Association loi 1901
- **Italy** — Onlus (now ETS — Ente del Terzo Settore under reform 2017)
- **Spain** — Fundación under Ley 50/2002
- **Belgium** — Fondation reconnue d'utilité publique
- **Switzerland** — Stiftung under Civil Code Art. 80
- **Luxembourg** — Fondation d'utilité publique; ASBL

### 1.5 Other major jurisdictions

**Other major jurisdictions status table**

| Country | Status |
| --- | --- |
| **Canada** | Registered Charity under Income Tax Act; T3010 annual filing |
| **Australia** | DGR (Deductible Gift Recipient) endorsement |
| **South Africa** | PBO (Public Benefit Organisation) §30 ITA; Section 18A donations deductible to donor |
| **India** | §12A / §80G registration |
| **Singapore** | IPC (Institution of a Public Character) |
| **Hong Kong** | §88 Inland Revenue Ordinance |
| **Japan** | Public-interest incorporated foundation |

## Section 2 — Fund accounting

**Fund category definitions**  _([T1])_

| Fund category | Definition |
| --- | --- |
| **Unrestricted (net assets without donor restrictions — US ASC 958)** | Donor-imposed restrictions exhausted or never applied |
| **Donor-restricted (with restrictions — US ASC 958)** | Donor specifies purpose or time |
| **Endowment** | Donor specifies permanent or term capital preservation |
| **Quasi-endowment** | Board-designated for long-term investment but not donor-restricted |

- **UK Charities SORP parallel categories** — UK Charities SORP has parallel categories (unrestricted general funds; designated funds; restricted income funds; endowment funds — permanent and expendable).  _([T1])_

## Section 3 — Unrelated Business Income (UBI) — US

- **UBI corporate tax** — Tax-exempt organisations pay corporate income tax (21%) on income from any unrelated trade or business regularly carried on.  _([T1] IRC §511-514)_
- **§512(a)(6) silo rule** — UBI computed separately for each unrelated trade or business (post-TCJA "silo" rule)  _([T1] §512(a)(6))_
- **§513(c) advertising** — Advertising as unrelated business  _([T1] §513(c))_
- **§514 debt-financed income** — Debt-financed income (rental income from leveraged property partly UBI)  _([T1] §514)_
- **§511(b) split-interest trusts** — Split-interest trusts subject to UBI on the unrelated portion  _([T1] §511(b))_
- **UBI exceptions** — Volunteer-labour exception; Convenience exception; Donated goods exception; Bingo (in some jurisdictions); Royalties (passive royalty income generally not UBI)  _([T1])_
- **Form 990-T** — UBI return

## Section 4 — VAT / GST for charities

**Charity VAT treatment by country**  _([T1])_

| Country | Treatment |
| --- | --- |
| **UK** | Charity-specific zero-rated supplies (zero-rated charity sales of donated goods); reduced rate on fuel/power for charity buildings; relief on capital goods for charity buildings |
| **EU** | Article 132 PVD: exempt activities including health, education, social, cultural, sport, religious — but exemption is mandatory for the activity, not optional, and may not align with the charity's profitable activities |
| **US** | n/a (sales/use tax state-level; many states exempt nonprofit purchases) |
| **Australia** | GST-free supplies for charity (e.g., gifts received, donated goods sold) |

## Section 5 — Self-dealing and minimum distribution (US private foundations)

- **§4941 Self-dealing** — A per-se prohibition on most transactions between the foundation and "disqualified persons" (substantial contributors, foundation managers, families). 10% excise on disqualified person + 5% on manager.  _([T1] IRC §4941)_
- **§4942 Minimum distribution** — 5% of average net investment assets must be distributed annually for qualifying charitable purposes; 30% excise tax on undistributed amount.  _([T1] IRC §4942)_
- **§4943 Excess business holdings** — Limits private foundation ownership of business enterprises to 20% (or 35% with limited exceptions); 10% excise.  _([T1] IRC §4943)_
- **§4944 Jeopardising investments** — Investment that risks the foundation's carrying out its exempt purposes (highly speculative investments) — 10% excise.  _([T1] IRC §4944)_
- **§4945 Taxable expenditures** — Certain prohibited expenditures (lobbying, voter registration, grants to non-charitable, etc.) — 20% excise + 100% if not corrected.  _([T1] IRC §4945)_

## Section 6 — Donor-Advised Funds (DAFs)

- **Donor-advised fund** — A charitable account held at a sponsoring organisation. Donor receives immediate tax deduction; gets non-binding advisory right over investment and distribution.  _([T1])_
- **§4966 DAF distributions excise** — Distributions from a DAF to certain disqualified persons or to non-public-charity grantees attract excise tax.  _(US §4966)_

UK has limited DAF equivalents through Charities Aid Foundation and others.

## Section 7 — Cross-border philanthropy

- **US cross-border deduction rules** — Deduction generally only for §170(c) US charity; foreign equivalent only via "friends of" intermediary or §4945 expenditure responsibility  _([T1])_
- **EU cross-border case law** — Persche/Stauffer case law extended deduction to equivalent EU charities (subject to equivalency determination)  _([T1])_
- **UK equivalency requirements** — HMRC equivalency requirements for foreign charities  _([T1])_

## Section 8 — Self-checks

- [ ] Entity correctly classified within country's exempt regime
- [ ] Public charity vs private foundation status confirmed (US)
- [ ] Public benefit test satisfied (UK)
- [ ] Restricted vs unrestricted funds segregated in accounting
- [ ] UBI computation per silo rule (US §512(a)(6))
- [ ] Form 990 / 990-PF / 990-T per applicable status
- [ ] 5% minimum distribution met (US private foundation)
- [ ] Self-dealing transactions reviewed
- [ ] Donor-restricted funds released only when restriction satisfied
- [ ] Charities SORP applied (UK)
- [ ] VAT charity reliefs claimed where applicable
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 9 — Disclaimer

Charity / nonprofit accounting and tax are sector-specific. Outputs must be reviewed by credentialed nonprofit-sector practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

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
