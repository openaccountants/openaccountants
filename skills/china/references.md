---
name: china-references
description: Use this file to find the official primary sources for mainland China tax work in tax year 2026 and to route a question to the right China skill. It lists the State Taxation Administration, National People's Congress and Ministry of Finance pages the China pack relies on, and two open-source projects that are reference-only (no licence). Built from the law, not reviewed by an accountant.
jurisdiction: CN
tax_year: 2026
tax_year_notes: "Calendar tax year 2026. The router notes selected individual income tax figures and links to the full rules."
last_updated: 2026-11-27
version: "2.1"
category: international
tier: 2
type: router
---

# China: primary sources and related open-source projects

> **General reference only.** This file is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## The method, step by step

1. **Find the job, then load the skill.** Individual income tax: `cn-iit` (quick computation: `china-pit`). Company tax: `cn-corporate-tax`. VAT: `cn-vat`. Social insurance and housing fund: `cn-social-insurance`. Payer withholding: `cn-withholding`. Transfer pricing: `cn-transfer-pricing`. Cross-border: `cn-cross-border`. Stamp tax: `cn-stamp-tax`. Fapiao and e-invoices: `cn-fapiao-einvoice`. Company formation: `cn-formation`. Freelancer intake: `cn-freelance-intake`. Return assembly: `cn-return-assembly`. Moving to Singapore: `china-to-singapore-relocation-tax`.
2. **Take every figure from the official text,** never from a third-party copy. The official places are:
   - State Taxation Administration (国家税务总局): https://www.chinatax.gov.cn, with the national policy library at https://fgk.chinatax.gov.cn and the provincial bureaus' policy libraries (for example Shanghai, https://shanghai.chinatax.gov.cn/zcfw/zcfgk/), which reproduce national laws and announcements as plain HTML.
   - National People's Congress law database: https://flk.npc.gov.cn and https://www.npc.gov.cn.
   - Central government and State Council documents: https://www.gov.cn.
   - Ministry of Finance: https://www.mof.gov.cn.
3. **Check the status line** (状态：全文有效 or 部分有效) on an STA policy library page before relying on it, and look for a later announcement that extends, amends or repeals it.
4. **Use the two open-source projects below as reference only.** They carry no explicit licence, so no code or text is copied from them, and they are not a source for any figure.

### Related open-source projects (reference only)

#### individual-income-tax-law

- Repository: [cn/individual-income-tax-law](https://github.com/cn/individual-income-tax-law)
- Licence: no explicit licence
- Language: Chinese
- Scope: a copy of the PRC Individual Income Tax Law (中华人民共和国个人所得税法), including the 7-band comprehensive income scale from 3% to 45% and the statutory deduction categories.
- Use: reference only; validate against the STA copy of the law (see Sources), which is the authority. Cannot incorporate code directly.

#### personal-income-tax-calculator

- Repository: [YutHelloWorld/personal-income-tax-calculator](https://github.com/YutHelloWorld/personal-income-tax-calculator)
- Licence: no explicit licence
- Language: JavaScript, Chinese
- Scope: a 2019 calculator for the cumulative withholding method with the 专项附加扣除 (special additional deductions).
- Use: reference only for the cumulative withholding logic. Its deduction amounts predate the 2023 increase. The current monthly standard is CNY 2,000 per eligible child for either education or care of a child under 3. Parents can allocate the whole deduction to one parent or split it equally. The elderly care deduction is CNY 3,000 a month for an only child. Other claimants share CNY 3,000 with their siblings, capped at CNY 1,500 each. Use `cn-iit` for the full eligibility rules. Cannot incorporate code directly.

## When to refuse or refer

- A question about Hong Kong, Macao or Taiwan: those are separate tax systems; use the corresponding `hong-kong`, `macau` or `taiwan` pack.
- A figure that only appears in a third-party copy or a repository: do not use it until it is found on an official page.
- A question the China pack does not cover: say so and refer to a qualified professional in China.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| STA Shanghai policy library, PRC Individual Income Tax Law. Read for the official text and the status line format | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html | 2026-11-14 |
| Ministry of Finance, State Council 国发〔2023〕13号. Read for the 2023 increase in the child, infant and elderly care deductions | https://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/202308/t20230831_3905100.htm | 2026-11-14 |

Not yet confirmed: see each China skill for its open items.
