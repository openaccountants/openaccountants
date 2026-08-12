---
name: international-incorporation
description: "International company formation and jurisdiction selection guide for solo founders, freelancers, and digital nomads. Use when the user asks about: where to register a company, business jurisdiction selection, Wyoming LLC setup, Delaware LLC, Hong Kong company formation, Singapore Pte Ltd, Estonia e-Residency OÜ, UK Ltd incorporation, Dubai freezone company, offshore company structure, one-person company (一人公司), solo founder incorporation, entity type selection, pass-through vs corporation, company formation costs, annual compliance by jurisdiction, 注册公司, 海外公司, 开公司, 离岸公司, 会社設立, 法人化, incorporating abroad, best country to register a business, cheapest jurisdiction, Stripe Atlas, company for non-US founders, company closure, operating agreement, or any question about choosing where to incorporate an international business."
version: 1.0
jurisdiction: INTL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# International Incorporation

## International Company Formation — Jurisdiction Selection Guide

> **Based on work by [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill provides general guidance on international company formation. It does not constitute legal or tax advice. All structures and tax treatments must be verified with qualified local advisors (CPAs, tax attorneys, chartered accountants) in the relevant jurisdictions before implementation. Tax rules, costs, and compliance requirements change frequently.

## Workflow

0. **Identify the user's profile** — Identify the user's profile — nationality, business type, revenue, customer location, primary goal.
0. **Check forex constraints** — Check forex constraints — if the user's home country has strict forex controls, this narrows jurisdiction choices (see `forex-controls.md`).
0. **Apply the jurisdiction decision tree** — Apply the jurisdiction decision tree — match profile to recommended structure.
0. **Present the comparison** — Present the comparison — costs, tax rates, compliance burden, banking options.
0. **Flag ongoing obligations** — Flag ongoing obligations — annual filings, penalties for non-compliance, substance requirements.

## Tier 1 Jurisdictions — Best for Most Solo Founders

### United States — Wyoming LLC

**United States — Wyoming LLC**

| Factor | Detail |
| --- | --- |
| Corporate tax | 0% federal (pass-through for non-US owners) |
| Personal tax | 0% for non-US owners; US citizens pay federal income + SE tax (~15.3%) |
| Setup cost | $100–500 USD |
| Setup timeline | 1–3 days |
| Annual cost | $60–600 USD (annual report + registered agent) |
| Banking | Mercury (remote opening), Wise Business |
| Substance required | None for non-US LLC owners |

**Best for:** Global SaaS, digital services, any solo founder wanting US credibility without US tax liability.

**Key advantage:** A US LLC owned by a non-US person is a "disregarded entity" for US tax purposes — 0% US federal income tax. Only taxed where the owner is personally tax-resident.

**Watch out:** US citizens face self-employment tax (~15.3%). EIN required for banking. Form 5472 filing mandatory for non-US owners ($25,000 penalty per form per year if missed).

### United States — Delaware LLC / C-Corp

**United States — Delaware LLC / C-Corp**

| Factor | Detail |
| --- | --- |
| Corporate tax | 0% federal (LLC pass-through); 21% federal (C-Corp) |
| Setup cost | $90 filing + $300/year franchise tax (LLC); $500 via Stripe Atlas (C-Corp) |
| Setup timeline | 1–2 days |
| Annual cost | $300+ franchise tax |
| Banking | Mercury, Stripe Atlas pipeline |

**Best for:** Founders planning to raise US VC funding. Delaware is the gold standard for SAFE notes and convertible instruments.

**Stripe Atlas pipeline:** Pay $500 → Delaware C-Corp incorporated → EIN procured → Mercury bank account → Stripe payments activated. Total time: ~1–2 weeks.

### Singapore — Pte. Ltd.

**Singapore — Pte. Ltd.**

| Factor | Detail |
| --- | --- |
| Corporate tax | 17% headline (effective ~8.5% on first SGD 200,000 with startup exemption) |
| Capital gains | 0% |
| Dividend WHT | 0% |
| Setup cost | SGD 300–800 |
| Setup timeline | 1–2 days |
| Annual cost | SGD 3,000–5,000 (nominee director + secretary + filing) |
| Banking | DBS, OCBC (may require in-person visit) |

**Best for:** Asia-Pacific-focused businesses with revenue >$50,000 USD/year.

**Requirements:** At least 1 Singapore-resident director (nominee ~SGD 2,000/year), mandatory company secretary, registered office in Singapore.

### Estonia — e-Residency OÜ

**Estonia — e-Residency OÜ**

| Factor | Detail |
| --- | --- |
| Corporate tax | 0% on retained profits; 20% on distributions |
| Setup cost | ~€385 (e-Residency card + registration) |
| Setup timeline | 2–4 weeks |
| Annual cost | €500–1,500 |
| Banking | Wise Business (primary), LHV |

**Best for:** Non-EU founders needing EU market access who reinvest most profits. Fully remote administration.

**Critical:** e-Residency does NOT confer Estonian tax residency. Personal tax is owed where the owner actually resides.

### Dubai — Freezone

**Dubai — Freezone**

| Factor | Detail |
| --- | --- |
| Corporate tax | 9% on income >AED 375,000; 0% below |
| Personal income tax | 5% (effective January 2026; was 0% until December 2025) |
| Setup cost | AED 5,000–15,000 |
| Setup timeline | 3–10 days |
| Annual cost | AED 10,000–20,000 (license + visa + office + insurance) |
| Banking | Emirates NBD, Mashreq, Wise |

**Best for:** Founders willing to relocate to UAE for low combined personal + corporate tax.

**Requirements:** Must actually live in UAE to establish tax residency. Popular freezones: DMCC, IFZA, Meydan.

## Tier 2 Jurisdictions — Good for Specific Situations

### United Kingdom — Ltd

**United Kingdom — Ltd**

| Factor | Detail |
| --- | --- |
| Corporate tax | 19% (first £50,000); 25% (above £250,000) |
| Setup cost | £12 |
| Setup timeline | Same day |
| Annual cost | £200–500 |
| Banking | Wise Business, Revolut Business |

**Best for:** UK/EU clients, B2B consulting. Cheapest and fastest incorporation globally.

### Hong Kong — Limited Company (有限公司)

**Hong Kong — Limited Company (有限公司)**

| Factor | Detail |
| --- | --- |
| Corporate tax | 8.25% (first HKD 2,000,000); 16.5% above |
| Offshore income | 0% (if properly structured — see substance requirements) |
| Dividend WHT | 0% |
| Setup cost | HKD 3,000–5,000 (~$400–650 USD) |
| Setup timeline | 1–2 weeks |
| Annual cost | HKD 5,000–10,000 |
| Banking | HSBC, ZA Bank, Airwallex HK |

**Best for:** Chinese mainland founders (大陆创始人) — no forex controls in HK, Stripe HK available, offshore income exemption.

**Offshore profits claim (离岸免税):** If business is conducted outside HK (no HK office, no HK employees, contracts signed outside HK), offshore income can be 0% taxed. FSIE rules (2023+) tightened substance requirements for passive income.

## Jurisdiction Decision Tree

```
What is the founder's nationality?
├── Chinese Mainland (中国大陆)
│   └── Global revenue? → YES → Hong Kong Ltd (escape forex controls, Stripe HK)
│                        → NO  → 个体户 or 小规模纳税人
├── Taiwanese (台灣)
│   └── Significant international revenue? → YES → HK Ltd or SG Pte. Ltd.
│                                          → NO  → Taiwan domestic company
├── Indian
│   └── US LLC (fund via LRS $250K) or SG Pte. Ltd. (strong DTAA)
├── US Citizen
│   └── Wyoming LLC (avoid CFC traps of foreign corporations)
└── Other nationality → Where are customers?
    ├── US/Global, no VC  → Wyoming LLC
    ├── US/Global, want VC → Delaware C-Corp (Stripe Atlas)
    ├── EU, reinvest profits → Estonia OÜ (0% retained)
    ├── EU, distribute profits → UK Ltd (cheapest)
    ├── Asia, revenue >$50K → Singapore Pte. Ltd. or HK Ltd
    ├── Asia, revenue <$50K → Wyoming LLC + Wise
    └── Want low personal tax + will relocate → Dubai Freezone
```

### Revenue Thresholds

**Revenue Thresholds**

| Revenue | Guidance |
| --- | --- |
| <$5,000/year | Do not incorporate. Invoice personally or use sole proprietorship. |
| $5,000–$25,000 | Simple single entity (Wyoming LLC or UK Ltd). Monthly overhead: ~$50–100. |
| $25,000–$100,000 | Same structure + proper accounting software. Monthly overhead: ~$100–250. |
| $100,000–$500,000 | Consider Singapore or Estonia for tax optimization. Monthly overhead: ~$300–700. |
| >$500,000 | Multi-jurisdiction structure + accountant + legal counsel. Monthly overhead: $1,000+. |

## Pass-Through vs Corporation

**Pass-Through vs Corporation**

| Entity Type | Tax Treatment | Best For |
| --- | --- | --- |
| US LLC (single-member) | Profits pass to owner's personal return | Non-US founders (0% US tax); US founders (flexible) |
| C-Corp (Delaware) | Corporate tax (21%) + dividend tax | Founders seeking US VC |
| Estonia OÜ | 0% retained; 20% on distributions | EU-serving founders who reinvest |
| Singapore Pte. Ltd. | 17% corporate (effective ~8.5% for small companies) | Asia-Pacific focused |
| UK Ltd | 19–25% corporate | UK/EU clients, low setup cost |
| HK Ltd | 8.25–16.5%; offshore 0% | China/Asia trade, offshore structures |

## Annual Cost Comparison

**Annual Cost Comparison**

| Structure | Setup | Annual Maintenance | Accounting | Total Year 1 |
| --- | --- | --- | --- | --- |
| Wyoming LLC | $160 | $60 | $500–1,500 | **$720–1,720** |
| Delaware LLC | $390 | $300 | $500–1,500 | **$1,190–2,190** |
| Stripe Atlas (DE C-Corp) | $500 | $300 | $1,000–3,000 | **$1,800–3,800** |
| Hong Kong Ltd | $500 | $800–1,500 | $800–1,500 | **$2,100–3,500** |
| Estonia OÜ | $600 | $300–500 | $600–1,200 | **$1,500–2,300** |
| UK Ltd | $60 | $200 | $500–1,500 | **$760–1,760** |
| Singapore Pte. Ltd. | $800 | $3,000–5,000 | $1,000–2,000 | **$4,800–7,800** |
| Dubai Freezone | $3,000 | $3,000–5,000 | $1,000–2,000 | **$7,000–10,000** |

## Key Compliance Requirements by Jurisdiction

**Key Compliance Requirements by Jurisdiction**

| Jurisdiction | Filing | Deadline | Penalty for Late |
| --- | --- | --- | --- |
| Wyoming LLC | Annual Report | 1st day of anniversary month | $50 late fee + $2/month |
| Delaware LLC | Franchise Tax | June 1 | $200 + 1.5%/month interest |
| US LLC (non-US owner) | Form 5472 + pro-forma 1120 | April 15 (extension available) | **$25,000 per form per year** |
| Singapore | Annual Return (ACRA) | Within 30 days of AGM | SGD 300 late fee |
| Singapore | Corporate Tax (Form C-S) | November 30 | Penalties + estimated assessment |
| Estonia OÜ | Annual Report | Within 6 months of FY end | €100–3,200 fine |
| UK Ltd | Confirmation Statement | Anniversary of incorporation | £250, then striking off |
| UK Ltd | Accounts filing | 9 months after FY end | £150–1,500 |
| Hong Kong | Annual Return (NAR1) | Within 42 days of anniversary | HKD 870–3,480 |
| Hong Kong | Profits Tax Return | Within 1 month of issuance | Penalty + estimated assessment |
| Dubai Freezone | License renewal | Annual | License cancellation |

## Entity Structures for Chinese Founders (大陆创始人)

### Recommended: HK Ltd + 个体户 Combination

```
Chinese Founder (个人)
├── Hong Kong Limited Company (有限公司)
│   ├── Receives global payments via Stripe HK / PayPal / Airwallex
│   ├── Offshore profits taxed at 0% (if business conducted outside HK)
│   └── Pays service fees to mainland 个体户 via contract
└── 个体户 (mainland)
    ├── Issues invoice (增值税普票) to HK company
    └── Pays 0.5–2% effective tax (核定征收 rate)
```

**Service fee requirements:** Real service agreement with market-rate pricing, valid 增值税普票 issued, documented deliverables. Service fee should not exceed 50% of HK company revenue (transfer pricing scrutiny threshold).

### Getting Money Back to Mainland

**Getting Money Back to Mainland**

| Method | Tax Treatment |
| --- | --- |
| Salary from HK company | Subject to HK salaries tax if work performed in HK |
| Dividends | No HK WHT; China 20% individual income tax on foreign dividends |
| Service fees to 个体户 | Needs valid contract + 发票; 核定征收 rate (0.5–2%) |
| Personal remittance | Within annual $50,000 USD forex limit |

## Company Closure / Winding Down

**Company Closure / Winding Down**

| Jurisdiction | Process | Cost | Timeline |
| --- | --- | --- | --- |
| Wyoming LLC | Articles of Dissolution + settle debts + final tax return | $0 state fee | 1–3 months |
| Delaware LLC | Certificate of Cancellation + final franchise tax | $200+ | 1–3 months |
| Singapore Pte. Ltd. | ACRA striking off or voluntary winding up | SGD 30–3,000+ | 3–6 months |
| Estonia OÜ | Liquidation via e-Business Register | €200–500 | 3–12 months |
| UK Ltd | Striking off (DS01 form) or voluntary liquidation | £10 | 3–6 months |
| Hong Kong Ltd | Companies Registry deregistration or voluntary winding up | HKD 690 | 5–7 months |
| Dubai Freezone | Cancel license + deregister + cancel visa | AED 2,000–5,000 | 2–4 months |

**Never abandon a company without formal dissolution.** Penalties, late fees, and government liens continue to accrue on dormant entities.

## Operating Agreement (US LLC)

Every LLC — even single-member — needs an operating agreement covering:

1. **Membership interest** — who owns what percentage
2. **Management structure** — member-managed vs manager-managed
3. **Distribution policy** — when and how profits are distributed
4. **Succession / death provisions** — who takes over if the sole member dies or becomes incapacitated
5. **Buy-sell mechanism** — dissolution or transfer procedures

**US estate tax risk for non-US owners:** Non-US persons owning US-sited assets >$60,000 face federal estate tax up to 40% at death. Holding a US LLC through a foreign holding company (e.g., HK Ltd) removes this exposure.

## Official Sources & Further Reading

- **IRS** — EIN application, Form 5472 instructions: https://www.irs.gov
- **Wyoming Secretary of State** — LLC filing: https://sos.wyo.gov
- **Delaware Division of Corporations**: https://corp.delaware.gov
- **ACRA Singapore**: https://www.acra.gov.sg
- **Estonia e-Residency**: https://e-resident.gov.ee
- **UK Companies House**: https://www.gov.uk/government/organisations/companies-house
- **HK Companies Registry**: https://www.cr.gov.hk
- **Stripe Atlas**: https://stripe.com/atlas

## Footer notes

*Data reflects 2024–2026 rules. For amounts >$100,000 USD or life-changing decisions, verify current rules with a qualified advisor in each relevant jurisdiction.*
*Original content: [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise) — MIT License.*
*OpenAccountants — open-source accounting skills for AI — info@openaaccountants.com*

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
