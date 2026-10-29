---
name: slovakia-vat-registration-4-7-7a
description: Which Slovak VAT registration a client actually needs, the 50 000 / 62 500 / 14 000 eur triggers, and why a §7a registrant pays VAT but cannot deduct it.
jurisdiction: SK
tax_year: 2025
last_updated: 2026-07-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia VAT registration (§4, §7, §7a): how I handle it

Slovakia has three different VAT registrations and only one of them makes you a VAT payer. §4 is the real thing (you charge VAT, you deduct input VAT). §7 and §7a are administrative registrations that give you a VAT number and an obligation to self-assess tax, with **no right of deduction**. Getting this wrong in either direction is expensive: register under §4 too early and you add 23% to prices your clients cannot reclaim; miss a §7a registration and you have been under-declaring reverse-charge VAT on every Google Ireland or Meta Ireland invoice since your first ad. The rules changed materially on 1 January 2025, so anything written before then is unsafe.

## Who this is for

- Slovak sole traders (SZČO) and s.r.o.s approaching the turnover threshold, or wondering whether to register voluntarily.
- Freelancers and small agencies buying services from foreign platforms (ads, SaaS, marketplaces) or billing clients in other EU member states. This is the group that gets caught by §7a, which has **no threshold at all**.
- Anyone who read a pre-2025 guide quoting 49 790 eur and 20%. Both figures are dead.

Non-established (foreign) businesses should read §5, not §4. This Guide covers §5 only where it interacts.

## Before you start, ask the client

1. **What did you actually supply, and where was the place of supply?** Only supplies with a place of supply *in Slovakia* count toward the §4 turnover. Services to business clients in other member states under §15(1) count for nothing. A freelancer billing 100 000 eur to German clients can have a Slovak turnover of zero, and still be obliged to register under §7a.
2. **What is the cumulative turnover this calendar year, from 1 January?** Not the last twelve months. The measurement period changed on 1 January 2025.
3. **Have you bought any service from a foreign business established in another EU member state?** Google Ireland, Meta Ireland, Amazon Luxembourg, Stripe Ireland, a Czech subcontractor. Amount is irrelevant. One euro triggers §7a.
4. **Have you supplied any service to a business in another member state where the customer accounts for the tax?** Also §7a, also no threshold.
5. **Have you bought goods from other member states?** Track the cumulative untaxed value against 14 000 eur for the calendar year. This is §7.
6. **Do your customers reclaim VAT?** If they are all consumers or exempt bodies, voluntary §4 registration makes you 23% more expensive overnight.
7. **Do you have deductible input costs and pre-trading expenditure?** That is the case *for* voluntary registration.

## The method, step by step

### Step 1: Test §4 first, because it overrides the others

Two separate turnover triggers, and they do different things.

**Trigger A, 50 000 eur.** Exceed 50 000 eur of turnover in a calendar year and you become a VAT payer on **1 January of the following year**. Not immediately.

**Trigger B, 62 500 eur.** Exceed 62 500 eur during the year and you become a VAT payer **at the moment of the supply that breaches it**, and you must charge VAT on that very supply.

### Step 2: Note what changed on 1 January 2025

The old threshold was 49 790 eur measured over **up to 12 preceding consecutive calendar months**. It is now 50 000 / 62 500 eur measured over the **calendar year**, resetting every 1 January. A transitional rule (§85kn) keeps the old regime alive for anyone who hit 49 790 eur by 31 December 2024.

### Step 3: Know what counts as "obrat"

Turnover means the net value of goods and services supplied **in Slovakia**, excluding supplies exempt under §28 to §36 and §40 to §42.

Excluded: advance payments (until the supply happens), supplies with a place of supply abroad, free-of-charge supplies, and supplies where the customer accounts for the tax under reverse charge.

Included, and people miss this: exempt insurance (§37), real estate (§38) and financial services (§39) **do** count, and if you cross the threshold purely on those you must still register and must say so on the form.

### Step 4: Voluntary §4 registration

You do not have to wait for 50 000 eur. Four things to tell the client:

- **You must be a "zdaniteľná osoba"** (a taxable person carrying on economic activity). The tax office will test this. Preparatory acts before your first sale are enough on settled CJEU authority (C-110/94 INZO, C-268/83 Rompelman, C-527/11 Ablessio), but you carry the burden of proof.
- **The decision takes up to 21 days.**
- **There is no backdating.** Registration cannot take effect before the application date.
- **The tax office can refuse on fraud-risk grounds**, but only on an overall assessment of the evidence.

Separately, if you have crossed 50 000 but not 62 500 eur, you can elect to become a payer early, either on the application itself (§4 ods. 8 písm. a, effective from the supply that broke 50 000) or later by notification (§4 ods. 8 písm. b, effective the day after you notify).

### Step 5: Test §7, goods from other member states

The application goes in **before** the acquisition that reaches 14 000 eur, not after. Voluntary §7 registration below the threshold is allowed but commits you to taxing acquisitions for at least two calendar years. New means of transport and excise goods are excluded from the count. Non-taxable legal persons (a sports club, a foundation) are caught too.

### Step 6: Test §7a, cross-border services, and note there is no threshold

Two limbs, both with an explicit "the price does not matter": before receiving a service from a foreign person in another member state where you are liable under §69(3), and before supplying a service to another member state where the place of supply is determined by §15(1) and the customer accounts for the tax.

You do **not** register under §7a if: the place of supply is determined by §15(2) or §16 rather than §15(1); you are already registered under §7; the service is exempt at its place of supply; **the counterparty is in a third country** (a US, UK or Swiss supplier or customer); or the counterparty is not a taxable person.

### Step 7: Understand what a §7 or §7a registrant is not

| | §4 VAT payer (platiteľ) | §7 / §7a registrant |
|---|---|---|
| Charges Slovak VAT on own sales | Yes, 23 / 19 / 5% | No |
| Deducts input VAT | Yes | **No** |
| Self-assesses reverse-charge VAT | Yes | Yes |
| Files a VAT return | Every tax period | Only for months where a liability arose. No nil returns. |
| Has a VAT number (IČ DPH) | Yes | Yes, restricted to the registered purpose |
| Net cost of an EU service invoice | Neutral (declare and deduct) | **VAT is a real, unrecoverable cost** |

A §7a-registered freelancer buying 1 000 eur of Meta Ireland advertising declares 230 eur of Slovak VAT and keeps none of it. Under §4 the same 230 eur would net to zero.

### Step 8: File, and then keep filing

The §4 application is due within five working days of the day the turnover was exceeded, or the day payer status was acquired. Decision timing: 10 days for a compulsory §4 registration, 21 days for a voluntary one, 10 days for §7 and §7a. Note that §7(3) and §7a(3) were amended with effect from 1 January 2025 to replace seven days with ten. Several of the tax authority's own information sheets still say seven. The statute says ten.

Ongoing obligations for a §7 or §7a registrant: return and payment within 25 days of the end of the month in which the liability arose, no nil returns, quarterly EC Sales List by the 25th where services are supplied, invoices within 15 days marked "prenesenie daňovej povinnosti", records kept, invoices retained for ten years. No payment is required if the tax due is not more than 5 eur.

## The traps

1. **"I only bill EU clients, so I don't need to register."** Backwards. Those supplies do not count toward the §4 turnover, and they are exactly what triggers §7a. Registration duty is higher, not lower.
2. **The Google Ireland / Meta Ireland trap.** A freelancer running 30 eur of ads is required to have registered under §7a *before* the first invoice, self-assess 23%, and file monthly returns. There is no small-amounts let-off. This is the most common unregistered exposure in Slovakia.
3. **US platforms are different, but you are not off the hook.** A supplier in a third country does not trigger §7a registration. The **liability** still arises: you self-assess and file without registering. Check where the platform entity is actually established, not where the website is.
4. **Not registering does not cancel the tax.** Failure to register under §7 leaves the obligation to pay, declare and file entirely intact.
5. **The 62 500 eur circularity.** If you cross 62 500 eur on a supply priced **VAT-inclusive**, the VAT comes out of your margin, and the net figure may not even have breached the threshold. Price net of VAT in contracts near the threshold.
6. **62 500 eur means immediate, not next year.** Clients who read about the 50 000 rule assume they always have until 1 January. On a lumpy year with one big project, they do not.
7. **Correcting your turnover downward afterwards does not undo registration.** Once payer status is confirmed by decision, a later credit note that drops you back under the line changes nothing.
8. **Exempt supplies still count.** Insurance, real estate and financial services under §37 to §39 are inside the turnover.
9. **§7 is "before the acquisition", §7a is "before the service".** Both are pre-emptive.
10. **Pre-2025 material is actively wrong.** Anything quoting 49 790 eur, a rolling 12-month window, a 20% standard rate or a 7-day decision predates the current law. That includes some documents still published on financnasprava.sk.
11. **You cannot appeal a refusal to register a purported payer** under §4 ods. 10 písm. a). A rejected *voluntary* application under §4 ods. 10 písm. b) can be appealed.

## Rates, thresholds and deadlines

| What | Value | Source |
|---|---|---|
| Standard VAT rate, from 1 Jan 2025 | 23% | financnasprava.sk, Sadzby dane |
| Reduced rates, from 1 Jan 2025 | 19% and 5% | financnasprava.sk, Sadzby dane |
| Standard rate before 1 Jan 2025 | 20% | FS SR §7a information sheet |
| §4 mandatory registration threshold (payer from 1 January following) | 50 000 eur in a calendar year | 2/DPH/2025/MP |
| §4 accelerated threshold (payer at the moment of the breaching supply) | 62 500 eur in a calendar year | 2/DPH/2025/MP |
| Previous §4 threshold, to 31 Dec 2024 | 49 790 eur over up to 12 preceding months (§85kn transitional) | 2/DPH/2025/MP |
| Turnover measurement period, from 1 Jan 2025 | Calendar year, restarting each 1 January | Consolidated VAT Act |
| §4 application deadline | 5 working days | 2/DPH/2025/MP |
| §4 decision, compulsory / voluntary | 10 days / 21 days | 2/DPH/2025/MP |
| Voluntary registration backdating | Not permitted | 2/DPH/2025/MP |
| §7 threshold, goods from other member states | 14 000 eur net in a calendar year | VAT Act §7(1) |
| §7 application timing | **Before** the acquisition that reaches 14 000 eur | VAT Act §7(1) |
| §7 voluntary registration commitment | Must tax acquisitions for at least 2 calendar years | FS SR §7 information sheet |
| §7a threshold | **None** ("nezáleží na výške ceny služby") | FS SR §7a information sheet |
| §7a application timing | Before receiving the service; before supplying the service | VAT Act §7a(1), (2) |
| §7 / §7a decision and IČ DPH allocation | Not later than 10 days (amended from 7, from 1 Jan 2025) | VAT Act §7(3), §7a(3) |
| §7 / §7a input VAT deduction | **None.** Registrant is not a platiteľ dane | FS SR §7a information sheet |
| §7 / §7a return and payment | 25 days after the end of the month in which the liability arose. No nil returns. | FS SR §7a information sheet |
| Minimum tax payable | No obligation where the tax due is not more than 5 eur | FS SR §7a information sheet |
| EC Sales List for §7a services supplied | Quarterly, within 25 days of quarter end. No nil listing. | FS SR §7a information sheet |
| Invoice deadline, §15(1) services to another member state | Within 15 days of month end, marked "prenesenie daňovej povinnosti" | FS SR §7a information sheet |
| Invoice retention | 10 years | FS SR §7 information sheet |
| §7 deregistration test | Below 14 000 eur in the current year **and** the preceding year | FS SR §7 information sheet |
| Registration form version | Confirm before filing (guidance cites ver. 2015) | FS SR §7a information sheet |
| Monthly vs quarterly tax period for a new §4 payer (§77) | Confirm before filing | not verified |
| Public-holiday interaction with "five working days" | Confirm before filing | not verified |
| Late-registration penalties | Confirm before filing | not verified |

## Worked example

**Jana, an SZČO web developer in Košice.** Not VAT-registered at 1 January 2026.

**Part 1, the §7a trigger she did not see coming.** In January 2026 Jana buys 200 eur of advertising from **Meta Platforms Ireland Ltd**. Place of supply Slovakia under §15(1), and Jana is liable under §69(3).

- She was required to file the §7a application **before receiving that first service**. Amount is irrelevant.
- She self-assesses: 200 × 23% = **46 eur**.
- She files a VAT return for January 2026 by **25 February 2026** and pays 46 eur. Above the 5 eur de minimis, so payment is due.
- She **cannot deduct** the 46 eur. Her real cost of the advertising is **246 eur**, not 200.
- She continues to invoice her Slovak clients **without VAT**. The §7a number does not make her a payer.

Had she bought the same ads from a **US** entity, no §7a registration would be required, but the 46 eur of self-assessed VAT and the return would still be due.

**Part 2, the §4 threshold.** Jana bills Slovak clients 4 500 eur net per month, and a German agency 2 000 eur per month for §15(1) services. The German fees have their place of supply in Germany and **do not enter her turnover at all**.

| Date | Slovak supplies (net) | Cumulative turnover |
|---|---|---|
| 31 Jan to 30 Nov 2026 | 11 × 4 500 | 49 500 |
| 10 Dec 2026 | 4 500 | **54 000** |

She exceeds 50 000 eur on 10 December 2026. Trigger A applies (54 000 is over 50 000 but under 62 500), so she becomes a VAT payer on **1 January 2027** and the 10 December invoice is correctly issued **without** VAT. Her application is due within five working days.

**Part 3, the counterfactual that changes everything.** Suppose instead the 10 December invoice is a one-off project at **14 000 eur net**, taking cumulative turnover to **63 500 eur**.

- She now exceeds 62 500, so **Trigger B** applies.
- She becomes a payer **at the moment of that supply**, and must charge VAT **on that invoice itself**: 14 000 × 23% = **3 220 eur**, total **17 220 eur**.
- Had the contract been priced at 14 000 eur **VAT-inclusive**, she would bear the VAT herself: 14 000 / 1.23 = 11 382.11 net, 2 617.89 VAT. And the net figure would have taken cumulative turnover only to 60 882.11, which does **not** exceed 62 500. This circularity is why contracts near the threshold must be priced net.

**Part 4, what §4 registration changes.** From the moment she is a payer, the Meta Ireland VAT reverses out: she declares the 23% and deducts it in the same return, so the advertising costs her 200 eur again.

## Sources

- Finančné riaditeľstvo SR, 2/DPH/2025/MP — Metodický pokyn k registrácii platiteľa DPH podľa § 4 a § 5 zákona č. 222/2004 Z. z. (22 September 2025): https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Metodicke_pokyny/Nepriame_dane/2025/2025.09.22_002_DPH_2025_MP.pdf
- Finančné riaditeľstvo SR, Úplné znenie zákona č. 222/2004 Z. z. o DPH (consolidated to 28 January 2025): https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Sprievodca/Sprievodca_danami/2025/2025.01.28_zakon_DPH.pdf
- Finančná správa SR, Sadzby dane: https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/sadzby-dane
- Finančná správa SR, Registračná povinnosť pre DPH: https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/registracna-povinnost-pre-dph
- FS SR, Informácia k povinnostiam osoby registrovanej podľa § 7: https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DPH/2018/2018.06.19_DPH_reg_par7.pdf
- FS SR, Informácia k povinnostiam osoby registrovanej podľa § 7a: https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DPH/2018/2018.06.18_DPH.pdf

**Caution on the two 2018 information sheets.** They remain published by the tax authority and are the clearest official statements of the §7 and §7a *procedural* obligations and of the no-deduction rule, which is why they are cited. They are **out of date on two points**: they state a 20% tax rate (now 23%) and a 7-day registration decision period (now 10 days from 1 January 2025). Where they conflict with the statute, the statute governs.

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
