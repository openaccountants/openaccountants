---
name: japan-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (計算書類 / 財務諸表) for a Japanese company. Trigger on phrases like "計算書類", "財務諸表", "会社法", "金融商品取引法", "J-GAAP", "日本基準", "決算書", "貸借対照表", "損益計算書", "大会社", "会計監査人", "有価証券報告書", or any question about preparing and filing statutory accounts under Japanese corporate law. Covers J-GAAP framework, company categories (大会社/中小), required statements, formats, notes, filing, and audit requirements.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Japan Financial Statements

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Japan (日本国) |
| Currency | JPY |
| Filing authority | Legal Affairs Bureau (登記所) for Companies Act; FSA/EDINET for FIEA |
| Primary legislation | Companies Act (会社法, Act No. 86 of 2005); Financial Instruments and Exchange Act (金融商品取引法, FIEA) |
| Supporting legislation | Companies Accounting Regulations (会社計算規則); Corporate Tax Act (法人税法) |
| Accounting standards | J-GAAP (企業会計基準 — ASBJ standards); IFRS permitted for listed companies |
| Financial year | Any 12-month period (March 31 year-end most common — ~70% of listed companies) |
| Filing deadline (Companies Act) | 2 weeks after AGM (登記); AGM within 3 months of year-end |
| Filing deadline (FIEA) | 3 months after fiscal year-end (有価証券報告書) |
| Digital filing | EDINET (for securities filings); e-Tax (for tax filings) |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity type | Applicable standard |
| --- | --- |
| All Stock Companies (株式会社) — Companies Act | J-GAAP (会社計算規則 basis) |
| Listed companies — FIEA | J-GAAP, IFRS, US GAAP, or modified IFRS (Japan's modified international standards) |
| Large Company (大会社) | J-GAAP with mandatory external audit |
| Small and Medium Companies (中小企業) | 中小企業の会計に関する指針 (SME Accounting Guidelines) or 中小企業の会計に関する基本要領 |
| Consolidated (listed) | J-GAAP or IFRS (choice for listed companies) |

### J-GAAP vs IFRS adoption in Japan

Japan allows a choice of four frameworks for listed companies' consolidated financial statements:
1. J-GAAP (most common)
2. IFRS as issued by IASB
3. US GAAP (legacy — being phased out)
4. Modified International Standards (JMIS — Japan-modified IFRS)

### Large Company (大会社) — Companies Act Art. 2(vi)

- **Large Company definition** — A Stock Company is a Large Company if either criterion is met (stated capital or total liabilities threshold).  _(Companies Act Art. 2(vi))_

**Large Company thresholds**  _(Companies Act Art. 2(vi))_

| Criterion | Threshold |
| --- | --- |
| Stated capital (資本金) on latest balance sheet | ≥ JPY 500,000,000 (¥5 billion) |
| Total liabilities (負債の部合計) on latest balance sheet | ≥ JPY 20,000,000,000 (¥200 billion) |

- **Either criterion triggers Large Company status** — Meeting either criterion triggers Large Company status (and mandatory external audit).  _(Companies Act Art. 2(vi))_

### Implications

**Implications table**

| Category | Financial auditor required? | Consolidated required? |
| --- | --- | --- |
| Large Company (大会社) | Yes — mandatory (会計監査人) | If has subsidiaries |
| Non-large Stock Company | No (unless voluntarily appointed or articles require) | Not required under Companies Act |
| Listed companies (FIEA) | Yes — mandatory | Yes (consolidated reporting) |
| SME (中小企業) | No | No |

### Under Companies Act (計算書類 — for all Stock Companies)

**Required financial statements under Companies Act**

| Document | Required |
| --- | --- |
| 貸借対照表 (Balance sheet) | Required |
| 損益計算書 (Profit and loss statement) | Required |
| 株主資本等変動計算書 (Statement of changes in shareholders' equity) | Required |
| 個別注記表 (Notes) | Required |
| 事業報告 (Business report) | Required |
| 附属明細書 (Supplementary schedules) | Required |

### Under FIEA (財務諸表 — for listed/reporting companies)

**Required financial statements under FIEA**

| Document | Required |
| --- | --- |
| 貸借対照表 (Balance sheet) | Required |
| 損益計算書 (P&L) | Required |
| 株主資本等変動計算書 (Changes in equity) | Required |
| キャッシュ・フロー計算書 (Cash flow statement) | Required |
| 注記 (Notes) | Required (extensive) |
| 連結財務諸表 (Consolidated financial statements) | Required (listed) |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Japan-specific notes |
| --- | --- | --- |
| 1 | 減価償却 (Depreciation) | Declining balance (定率法) or straight-line (定額法); tax useful lives per MOF ordinance |
| 2 | 引当金 (Provisions) | 賞与引当金 (bonus), 退職給付引当金 (retirement), 貸倒引当金 (bad debts) |
| 3 | 退職給付 (Retirement benefits) | ASBJ Statement 26; projected benefit obligation; discount rate |
| 4 | 貸倒引当金 (Bad debt allowance) | General + specific; tax law sets maximum rates for general allowance |
| 5 | 棚卸資産 (Inventory) | ASBJ Statement 9; lower of cost and NRV; FIFO, moving average, identified cost |
| 6 | 税効果会計 (Tax-effect accounting) | ASBJ Statement 27; temporary differences; effective rate ~30% (corporate + local + enterprise) |
| 7 | 為替差損益 (FX differences) | Monetary items at closing rate; non-monetary at historical |
| 8 | リース (Leases) | ASBJ Statement 13; finance/operating distinction (IFRS 16 not yet adopted in J-GAAP) |
| 9 | 減損 (Impairment) | ASBJ Statement 6; undiscounted cash flow test then fair value measurement |
| 10 | 繰延資産 (Deferred charges) | Stock issuance costs, bond issuance costs — amortise per regulations |
| 11 | 有価証券 (Securities valuation) | Trading: fair value through P&L; available-for-sale: fair value through OCI |
| 12 | 消費税 (Consumption tax) | Tax-exclusive or tax-inclusive method; reconcile input/output |

## Section 6 -- 損益計算書 Format (P&L)

Companies Act standard format (会社計算規則):

```
I.  売上高 (Net sales / Revenue)
II. 売上原価 (Cost of sales)
      ─── 売上総利益 (Gross profit) ───

III. 販売費及び一般管理費 (Selling, general and administrative expenses)
      ─── 営業利益 (Operating income) ───

IV. 営業外収益 (Non-operating income)
      受取利息 (Interest income)
      受取配当金 (Dividend income)
      為替差益 (FX gains)
      その他 (Other)

V.  営業外費用 (Non-operating expenses)
      支払利息 (Interest expense)
      為替差損 (FX losses)
      その他 (Other)
      ─── 経常利益 (Ordinary income) ───

VI. 特別利益 (Extraordinary income)
      固定資産売却益 (Gain on disposal of fixed assets)

VII. 特別損失 (Extraordinary losses)
      固定資産売却損 (Loss on disposal)
      減損損失 (Impairment loss)
      ─── 税引前当期純利益 (Income before taxes) ───

法人税、住民税及び事業税 (Corporate tax, resident tax, enterprise tax)
法人税等調整額 (Deferred tax adjustment)
      ─── 当期純利益 (Net income) ───
```

## Section 7 -- 貸借対照表 Format (Balance Sheet)

Companies Act standard format:

```
資産の部 (ASSETS)

流動資産 (Current assets)
  現金及び預金 (Cash and deposits)
  受取手形及び売掛金 (Notes and accounts receivable)
  有価証券 (Securities)
  棚卸資産 (Inventories)
  前払費用 (Prepaid expenses)
  その他 (Other)
  貸倒引当金 (Allowance for doubtful accounts) (△)

固定資産 (Non-current assets)
  有形固定資産 (Tangible fixed assets)
    建物 (Buildings)
    機械及び装置 (Machinery and equipment)
    土地 (Land)
    建設仮勘定 (Construction in progress)
  無形固定資産 (Intangible fixed assets)
    のれん (Goodwill)
    ソフトウェア (Software)
  投資その他の資産 (Investments and other)
    投資有価証券 (Investment securities)
    繰延税金資産 (Deferred tax assets)

─────────────────────────────────────

負債の部 (LIABILITIES)

流動負債 (Current liabilities)
  支払手形及び買掛金 (Notes and accounts payable)
  短期借入金 (Short-term borrowings)
  未払法人税等 (Income taxes payable)
  賞与引当金 (Provision for bonuses)
  その他 (Other)

固定負債 (Non-current liabilities)
  長期借入金 (Long-term borrowings)
  退職給付引当金 (Provision for retirement benefits)
  繰延税金負債 (Deferred tax liabilities)

─────────────────────────────────────

純資産の部 (NET ASSETS / EQUITY)

株主資本 (Shareholders' equity)
  資本金 (Share capital)
  資本剰余金 (Capital surplus)
  利益剰余金 (Retained earnings)
  自己株式 (Treasury shares) (△)

その他の包括利益累計額 (Accumulated OCI)
  その他有価証券評価差額金
  為替換算調整勘定
```

## Section 8 -- 注記 / 個別注記表 (Notes)

**Notes disclosure requirements**

| # | Disclosure | SME | Large Company | Listed (FIEA) |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies (重要な会計方針) | Required | Required | Required (extensive) |
| 2 | Notes on balance sheet items | Simplified | Required | Required |
| 3 | Contingent liabilities (偶発債務) | Required | Required | Required |
| 4 | Related party transactions | Not required | Required | Required (extensive) |
| 5 | Per-share information | Not required | Required | Required |
| 6 | Subsequent events (後発事象) | Required | Required | Required |
| 7 | Segment information | Not required | Not required (Companies Act) | Required (FIEA) |
| 8 | Tax-effect accounting | Simplified | Required | Required |
| 9 | Financial instruments | Simplified | Required | Required (extensive) |
| 10 | Retirement benefits | Simplified | Required | Required |
| 11 | Asset retirement obligations | Not required | If applicable | Required |
| 12 | Revenue recognition details | Simplified | Required (from 2021) | Required |

### Companies Act filings

**Companies Act filings**  _(Companies Act Art. 440)_

| Item | Detail |
| --- | --- |
| AGM deadline | Within 3 months from fiscal year-end |
| 計算書類 approval | By board of directors before AGM; submitted to AGM for approval |
| Public notice of balance sheet (決算公告) | Required for all Stock Companies (Art. 440); via official gazette, newspaper, or website |
| Filing with registry | Changes to directors/registered matters — not the accounts themselves |
| Penalty for non-disclosure | Up to JPY 1,000,000 administrative fine (過料) for failure to make public notice |

### FIEA filings (listed/reporting companies)

**FIEA filings**

| Item | Detail |
| --- | --- |
| 有価証券報告書 (Annual securities report) | Within 3 months of fiscal year-end |
| Filing method | EDINET (Electronic Disclosure for Investors' NETwork) |
| 四半期報告書 (Quarterly report) | Within 45 days of quarter-end (being replaced by semi-annual from 2025) |
| Format | XBRL (Inline XBRL for annual filings) |
| Late filing penalty | Criminal penalty possible (up to JPY 5,000,000 or imprisonment) |
| Audit requirement | Both Companies Act and FIEA audits required for listed companies |

### Tax filing

**Tax filing**

| Item | Detail |
| --- | --- |
| Corporate tax return (確定申告) | Within 2 months of fiscal year-end (extendable by 1 month) |
| Local tax returns | Same deadline; filed with prefectural/municipal tax offices |
| Format | e-Tax (electronic) or paper |

## Section 10 -- Audit Requirements

**Audit Requirements**

| Category | Requirement |
| --- | --- |
| Large Company (大会社) — capital ≥ ¥500M or liabilities ≥ ¥20B | Mandatory 会計監査人 (financial auditor) — Companies Act audit |
| Listed companies (FIEA) | Mandatory — both Companies Act audit + FIEA audit (can be same firm) |
| Non-large Stock Company | Not required (unless articles of incorporation specify) |
| 有限会社 (special limited company — legacy) | Not required |
| Membership company (合同会社/合名会社/合資会社) | Not required |

### Dual audit system for listed companies

Listed companies are subject to two separate (but usually combined) audit requirements:
1. **Companies Act audit** (会社法監査): auditor reports on 計算書類
2. **FIEA audit** (金商法監査): auditor reports on 財務諸表 in the securities filing

### Auditor qualification

- 公認会計士 (Certified Public Accountant) registered with JICPA
- 監査法人 (Audit corporation / firm) registered with JICPA
- For Companies Act: 会計監査人 appointed by shareholders at AGM
- For FIEA: registered audit firm meeting independence requirements

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
