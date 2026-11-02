---
name: global-ad-platforms
description: "Pattern library for advertising platforms appearing on bank statements worldwide. Covers Google Ads, Meta / Facebook Ads (incl. Instagram), LinkedIn Ads, TikTok Ads / Bytedance, X (Twitter) Ads, Microsoft Ads / Bing Ads, Amazon Ads, Reddit Ads, Pinterest Ads, Snap Ads, Taboola, Outbrain, Quora Ads, Yahoo / Yahoo Japan Ads, Yandex Direct (where applicable), Baidu Ads, Naver Search Advertising, Spotify Ads, Apple Search Ads, RTB / DSP providers (The Trade Desk, DV360, Amazon DSP), and influencer / affiliate platforms (Awin, Impact, ShareASale, Refersion, Partnerize). Provides bank-statement variations, default classification, VAT / GST treatment (notably the India equalisation levy 6% withholding on advertising payments to non-residents), and the relevant DST / sales-tax overlay. Does NOT cover: cloud / hosting (see global-cloud-infrastructure), productivity SaaS (see global-productivity-tools), or payment processors (see global-payment-processors)."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: pattern
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Global Ad Platforms

## Global Ad Platform Vendor Patterns v0.1

## Pattern table

**Ad platform vendor pattern table**  _([Skill markdown pattern table](placeholder))_

value

**Ad platform vendor pattern table**  _(Skill markdown pattern table)_

| Vendor | Bank statement variations | Default category | VAT/GST notes |
| --- | --- | --- | --- |
| **Google Ads** | `GOOGLE*ADS`, `GOOGLE *ADWORDS`, `GOOGLE IRELAND LTD`, `GOOGLE ADS DUBLIN` | Advertising | EU B2B reverse charge (Google Ireland). UK: reverse charge. India: 6% equalisation levy withholding on payments by Indian payors |
| **Meta / Facebook / Instagram Ads** | `FACEBK *`, `META PLATFORMS`, `FACEBOOK IRELAND`, `META PLATFORMS IRELAND` | Advertising | Same as Google Ads — EU/UK B2B reverse charge from Meta Ireland; India 6% EL |
| **LinkedIn Ads** | `LINKEDIN`, `LINKEDIN CORP`, `LINKEDIN IRELAND` | Advertising | Microsoft subsidiary; LinkedIn Ireland for EU |
| **TikTok Ads / Bytedance** | `TIKTOK INFO TECH`, `BYTEDANCE`, `TIKTOK ADS`, `TIKTOK PTE LTD` | Advertising | Singapore (TikTok Pte Ltd) or UK invoicing; EU B2B reverse charge |
| **X / Twitter Ads** | `X CORP`, `TWITTER ADS`, `X HOLDINGS` | Advertising | US (X Corp); EU B2B reverse charge |
| **Microsoft Ads / Bing Ads** | `MICROSOFT ADS`, `MICROSOFT*ADVERTISING`, `MICROSOFT IRELAND OPS` | Advertising | EU B2B reverse charge (Microsoft Ireland) |
| **Amazon Ads** | `AMAZON ADS`, `AMZN ADVERTISING`, `AMAZON ADS EMEA` | Advertising | EU B2B reverse charge (Amazon Online Sales Ireland or AMS EMEA Sarl) |
| **Reddit Ads** | `REDDIT INC`, `REDDIT BUSINESS` | Advertising | US supplier (Reddit Inc); EU B2B reverse charge |
| **Pinterest Ads** | `PINTEREST INC`, `PINTEREST EUROPE` | Advertising | US supplier; EU operations |
| **Snap Ads** | `SNAP INC`, `SNAP*ADS` | Advertising | US supplier |
| **Taboola** | `TABOOLA INC`, `TABOOLA EUROPE` | Advertising / content discovery | US HQ; EU operations |
| **Outbrain** | `OUTBRAIN INC`, `OUTBRAIN EUROPE` | Advertising / content discovery | US HQ; EU operations |
| **Quora Ads** | `QUORA INC` | Advertising | US supplier |
| **Yahoo Ads** | `YAHOO INC`, `VERIZON MEDIA`, `YAHOO INC NEW` | Advertising | US supplier (post-Verizon spin-off) |
| **Yahoo Japan Ads** | `YAHOO JAPAN`, `LY CORP` | Advertising | Japan supplier (now LY Corp after LINE merger) |
| **Baidu Ads** | `BAIDU INC` | Advertising | China supplier |
| **Naver Search Advertising** | `NAVER CORP`, `NAVER*` | Advertising | South Korea supplier |
| **Yandex Direct** | `YANDEX`, `YANDEX RUSSIA` | Advertising | Russia / Nidex (post-2024 spin-off); sanctions check |
| **Spotify Ads / Spotify Ad Studio** | `SPOTIFY ADS`, `SPOTIFY AB` | Advertising / audio | Sweden HQ |
| **Apple Search Ads** | `APPLE SEARCH ADS`, `APPLE INC ADS` | Advertising | Apple Inc / Apple Distribution International |
| **The Trade Desk** | `THE TRADE DESK INC`, `TTD` | Advertising / DSP | US supplier |
| **DV360 (Display & Video 360)** | `GOOGLE DV360`, `GOOGLE *DV360` | Advertising / DSP | Same as Google Ads |
| **Amazon DSP** | `AMAZON DSP`, `AMAZON ADS DSP` | Advertising / DSP | Same as Amazon Ads |
| **Awin** | `AWIN LTD`, `AWIN AG` | Affiliate marketing | UK / Germany supplier |
| **Impact / Impact Tech** | `IMPACT TECH`, `IMPACT.COM` | Affiliate / partnership | US supplier |
| **ShareASale** | `SHAREASALE`, `AWIN US INC` | Affiliate marketing | Awin subsidiary |
| **Refersion** | `REFERSION INC` | Affiliate marketing | US supplier |
| **Partnerize** | `PARTNERIZE LTD` | Affiliate / partnership | UK supplier |

## Special treatment: India Equalisation Levy 2.0

- **Indian payors must withhold 6% Equalisation Levy** — Indian payors must withhold 6% Equalisation Levy on payments for online advertising services to non-residents. Failure leads to disallowance under §40(a)(ib) ITA.  _([T1] Finance Act 2016 §165; §40(a)(ib) ITA)_

The Indian advertiser:
1. Withholds 6% from payment
2. Remits to Income Tax Department
3. Reports annually in Form 1
4. Discloses on income tax return for §40(a)(ib) deduction allowance

See `digital-services-tax-matrix.md` for full DST treatment.

## EU place of supply (B2B advertising)

- **Article 44 PVD B2B place of supply** — Article 44 PVD: B2B services taxed where customer established → reverse charge for cross-border B2B. Article 59a may shift to country of effective use/enjoyment for some non-EU customer cases — confirm.  _([T1] Article 44 PVD; Article 59a PVD)_

## Default classification

- **Schedule C** — Line 8 — Advertising  _(Schedule C)_
- **UK self-employment** — Box 14 (Advertising and entertainment)  _(UK self-employment)_
- **EU bookkeeping** — "Werbung und Marketing" / "Publicité"  _(EU bookkeeping)_

## Self-checks

- [ ] Ad spend separated from creative production / agency fees
- [ ] Indian EL withheld where applicable (Indian payor → non-resident provider)
- [ ] EU/UK B2B reverse charge applied
- [ ] Currency conversion at payment date
- [ ] Russia / sanctioned-jurisdiction advertising screened

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
