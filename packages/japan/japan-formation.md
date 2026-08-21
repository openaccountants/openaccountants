---
name: japan-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Japan. Trigger on phrases like "set up a company in Japan", "KK formation", "GK formation", "kabushiki kaisha", "godo kaisha", "法務局", "Legal Affairs Bureau", "Japanese company formation", "register a business Japan", "会社設立", "定款", "登録免許税", or any question about starting a business entity in Japan. Covers entity types (KK, GK, branch office), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Japanese company formation.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Japan Formation

## Japan Company Formation Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Japan |
| Currency | JPY |
| Company registrar | Legal Affairs Bureau (法務局 / Hōmukyoku) |
| Key legislation | Companies Act (会社法); Commercial Registration Act (商業登記法) |
| Typical formation time | 1--3 weeks |
| Corporate tax rate | ~30--34% effective (national + local; varies by municipality and capital) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Individual Business (個人事業主) | GK (合同会社 / Gōdō Kaisha) | KK (株式会社 / Kabushiki Kaisha) | Branch Office (支店) |
| --- | --- | --- | --- | --- |
| Legal personality | No | Yes | Yes | No (extension of parent) |
| Liability | Unlimited | Limited | Limited | Parent bears liability |
| Min. founders | 1 | 1 | 1 | N/A |
| Min. capital | N/A | ¥1 (statutory) | ¥1 (statutory) | N/A |
| Governance | N/A | Flexible (member-managed) | Formal (board/directors/auditors) | Per parent company |
| Transferability | N/A | Requires all members' consent | Shares freely transferable (unless restricted) | N/A |
| Tax treatment | Personal income tax | Corporate tax | Corporate tax | Corporate tax on Japan-source income |
| Prestige/perception | Low | Medium (growing acceptance) | High (traditional corporate form) | Varies |
| Admin burden | Low | Medium | High | Medium |

**Recommended default:** GK for startups and cost-sensitive formations. KK for investor-facing businesses, B2B credibility, and future equity fundraising.

## Section 3 -- Registration Process

### Step 1: Choose Company Name and Decide Entity Type

- **Company name requirement** — Name must include "合同会社" (GK) or "株式会社" (KK)
- **Name uniqueness check** — Check local uniqueness at the Legal Affairs Bureau for your registered address jurisdiction
- **National vs local uniqueness** — National uniqueness is not required, but local uniqueness is

### Step 2: Prepare Articles of Incorporation (定款 / Teikan)

- **Articles content** — Define: company name, purpose, registered office, capital, fiscal year, members/shareholders, directors
- **KK notarisation requirement** — Articles must be notarised at a public notary office (公証役場)
- **GK notarisation requirement** — No notarisation required (filed directly)

### Step 3: Notarisation (KK only)

- **Notary fee** — ¥30,000--¥50,000 JPY (capital-dependent scale)
- **Revenue stamp (収入印紙)** — ¥40,000 for paper filing; ¥0 for electronic filing (電子定款) JPY
- **Certified copy fee** — ~¥2,000 JPY

### Step 4: Deposit Capital

- **Capital deposit account** — Deposit into a personal bank account of a founding member (company account cannot exist yet)
- **Proof of deposit** — Obtain proof of deposit (通帳コピー / bank book photocopy)
- **Legal minimum capital** — ¥1 JPY (for both KK and GK)
- **Practical minimum capital** — ¥1M--¥5M for banking credibility; ¥30M+ for Business Manager visa (since October 2025) JPY

### Step 5: Prepare Corporate Seal (法人印鑑 / Hōjin Inkan)

- **Seals needed** — Three seals typically needed: representative seal (実印), bank seal (銀行印), company stamp (角印)
- **Corporate seal cost** — ¥10,000--¥30,000 JPY

### Step 6: File Registration at Legal Affairs Bureau (法務局)

- **Submission requirements** — Submit: application form, articles, capital deposit proof, officer consent forms, seal registration
- **Registration tax (登録免許税) KK** — ¥150,000 minimum (or 0.7% of capital if higher) JPY (KK)
- **Registration tax (登録免許税) GK** — ¥60,000 minimum (or 0.7% of capital if higher) JPY (GK)
- **Company legal existence** — Company legally exists from the date of registration

### Step 7: Post-Registration Tax Filings

- **Hōjin Setsuritsu Todoke filing - National Tax Agency** — File Hōjin Setsuritsu Todoke (法人設立届出書) with National Tax Agency (税務署) -- within 2 months
- **Hōjin Setsuritsu Todoke filing - Prefectural tax office** — Prefectural tax office -- within 15 days (varies by prefecture)
- **Hōjin Setsuritsu Todoke filing - Municipal tax office** — Municipal tax office -- within 15 days (varies)
- **Blue Return Filing application deadline** — Apply for Blue Return Filing (青色申告) within 3 months for tax benefits

### Step 8: Social Insurance Registration

- **Shakai Hoken mandatory registration** — Shakai Hoken (社会保険): mandatory from day 1 for all companies (even 1-person companies)
- **Registration bodies** — Register with: Japan Pension Service (年金事務所) and Hello Work (ハローワーク, if hiring)
- **Rōdō Hoken requirement** — Rōdō Hoken (労働保険): mandatory once first employee is hired

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Capital | Paid-Up Timing | Registration Tax | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| GK | ¥1 | Before registration | ¥60,000 (or 0.7% of capital) | Permitted |
| KK | ¥1 | Before registration | ¥150,000 (or 0.7% of capital) | Permitted (shikkin inspection for KK with >¥5M in kind) |
| Branch Office | N/A | N/A | ¥60,000 | N/A |

- **Capital and visa** — **Capital and visa:** Since October 2025, the Business Manager visa requires ¥30,000,000 minimum capital for new applicants.

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | KK (JPY) | GK (JPY) | Notes |
| --- | --- | --- | --- |
| Registration tax (登録免許税) | ¥150,000 | ¥60,000 | Minimum; 0.7% of capital if higher |
| Notary fee (定款認証) | ¥30,000--¥50,000 | ¥0 | KK only |
| Revenue stamp (紙定款) | ¥40,000 (paper) / ¥0 (electronic) | ¥40,000 / ¥0 | Save ¥40,000 with electronic filing |
| Corporate seal set | ¥10,000--¥30,000 | ¥10,000--¥30,000 | 3-seal set |
| Certified copies | ~¥2,000 | ~¥600 |  |
| **Total government fees** | **¥192,000--¥280,000** | **¥70,000--¥130,000** | Electronic filing recommended |
| Judicial scrivener (司法書士) | ¥60,000--¥100,000 | ¥50,000--¥80,000 | Optional but recommended |
| Tax accountant setup | ¥100,000--¥300,000 | ¥100,000--¥300,000 | First-year bookkeeping and filings |
| **Total with professionals** | **¥350,000--¥700,000** | **¥220,000--¥510,000** |  |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (JPY) |
| --- | --- |
| Corporate inhabitant tax (均等割) | ¥70,000/year minimum (even if no profit) |
| Tax accountant (税理士) | ¥300,000--¥600,000/year |
| Social insurance contributions | ~30% of gross salary (employer share ~15%) |
| Annual financial statements | Included in tax accountant fees |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Corporate tax return (法人税) | Within 2 months of fiscal year-end | National Tax Agency (税務署) |
| Consumption tax return (消費税) | Within 2 months of fiscal year-end | Tax office |
| Corporate inhabitant tax | Within 2 months of fiscal year-end | Prefectural/municipal tax office |
| Withholding tax (源泉徴収) | 10th of following month (or semi-annual for small companies) | Tax office |
| Shakai Hoken reports | Monthly contributions; annual Santei Kiso Todoke | Japan Pension Service |
| Financial statements | File with tax return | Tax office |
| Touki (登記) changes | Within 2 weeks of any change (directors, address, capital) | Legal Affairs Bureau |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Documents list** — Tōki Jikō Shōmeisho (登記事項証明書) -- certified registry extract; Inkan Shōmeisho (印鑑証明書) -- seal registration certificate; Articles of incorporation; ID of representative director; Proof of business office address; Business plan or description of activities

### Typical Timeline

- **Major banks timeline** — 2--4 weeks (major Japanese banks are thorough with KYC)
- **New company timeline** — 1--2 months for new companies (banks are cautious with newly formed entities)
- **Digital bank timeline** — Digital banks (PayPay Bank, GMO Aozora): 1--2 weeks

### Common Banks

MUFG (三菱UFJ), SMBC (三井住友), Mizuho (みずほ) (megabanks); Resona, Shinsei (mid-tier); PayPay Bank, GMO Aozora Net Bank (digital)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | KK requires a representative director; GK requires a representative member. Since April 2015, no requirement for a Japan-resident representative (but banks strongly prefer one) |
| Business Manager visa capital | ¥30,000,000 since October 2025 |
| Physical presence required? | Not for registration (power of attorney accepted); required for visa application |
| Registered office | Must be a physical address in Japan (virtual offices accepted for registration but not for visa) |
| Apostille requirements | Foreign documents require apostille + Japanese translation |
| Corporate seal registration | Mandatory for all companies; representative must register in person or via scrivener |
| Japan-resident bank account | Required for capital deposit; non-residents can use a trusted Japan-resident person's account |

## Section 9 -- Common Mistakes and Refusals

- **R-JP-F1 -- ¥1 capital and banking** — While ¥1 capital is legally valid, Japanese banks routinely reject account applications from companies with minimal capital. Recommend at least ¥1,000,000 for banking credibility.  _(R-JP-F1)_
- **R-JP-F2 -- Confusing visa capital with legal minimum** — The legal minimum capital is ¥1, but the Business Manager visa requires ¥30,000,000 since October 2025. These are separate requirements. Always clarify the client's visa intentions before advising on capital.  _(R-JP-F2)_
- **R-JP-F3 -- Failure to register for shakai hoken** — Social insurance (health + pension) registration is mandatory from day 1, even for a single-person company. Non-registration is a violation that can trigger penalties and backdated assessments.  _(R-JP-F3)_
- **R-JP-F4 -- Missing 2-week deadline for registry changes** — Any change to directors, address, or capital must be registered at the Legal Affairs Bureau within 2 weeks. Late registration incurs fines (科料) of up to ¥1,000,000.  _(R-JP-F4)_
- **R-JP-F5 -- Paper filing of articles (KK)** — Electronic filing of KK articles saves ¥40,000 in revenue stamps. Always recommend electronic filing via a qualified scrivener.  _(R-JP-F5)_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Decide KK vs GK; prepare articles | 2--5 days | Day 2--5 |
| Notarisation of articles (KK only) | 1--3 days | Day 3--8 |
| Prepare corporate seal | 3--7 days | Day 6--15 |
| Deposit capital | 1--2 days | Day 7--17 |
| File at Legal Affairs Bureau | 1 day | Day 8--18 |
| Registration complete (certificate available) | 1--2 weeks | Day 15--32 |
| Post-registration tax filings | 1--5 days | Day 16--37 |
| Open bank account | 2--8 weeks | Day 30--93 |
| **Ready to trade** |  | **~3--6 weeks (bank account is the bottleneck)** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
