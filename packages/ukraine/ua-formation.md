---
name: ua-formation
description: Use this skill whenever asked about registering or forming a business in Ukraine for a self-employed person. Trigger on phrases like "register a FOP", "how do I become a ФОП", "start a business in Ukraine", "open a sole proprietorship Ukraine", "Diia registration", "ТОВ vs ФОП", "LLC vs sole proprietor Ukraine", "choose КВЕД codes", "single tax election", "register for VAT Ukraine", "open a business bank account Ukraine", "close my ФОП", or any question about the formation, registration, tax-system choice at start-up, or deregistration of a Ukrainian sole proprietor (ФОП) or company (ТОВ). Covers registering via Diia or a state registrar/notary, documents required, choosing КВЕД activity codes, electing the single-tax group (1/2/3) vs the general system, the ₴1,000,000 VAT threshold, ЄСВ registration, opening a bank account, the ФОП-vs-ТОВ decision, and closing a ФОП. ALWAYS read this skill before any Ukrainian business-formation work.
version: 1.0
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Formation

## Ukraine Business Formation (Реєстрація ФОП / ТОВ) — Self-Employed Skill v1.0

This skill covers **how a self-employed person sets up a business in Ukraine**: registering as a **ФОП** (фізична особа-підприємець / sole proprietor), choosing **КВЕД** activity codes and a tax system at registration, the **VAT (ПДВ)** threshold, **ЄСВ** registration, opening a bank account, and the decision between a ФОП and a **ТОВ** (товариство з обмеженою відповідальністю / LLC). It is the entry point. Once formed, route ongoing work to the companion skills: `ua-single-tax`, `ua-income-tax`, `ua-social-contributions`, `ua-bookkeeping`, and `ukraine-vat`.

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ukraine (UA) |
| What this covers | Business formation / registration for self-employed people — ФОП registration, КВЕД codes, tax-system election at start-up, VAT registration, ЄСВ, bank account, ФОП vs ТОВ, deregistration |
| Currency | UAH (₴) |
| Registers / authorities | **ЄДР** (Єдиний державний реєстр / Unified State Register, run by the Ministry of Justice); **ДПС** (Державна податкова служба / State Tax Service); **Diia** (Дія — state e-gov portal & app) |
| Sole-proprietor form | **ФОП** (фізична особа-підприємець) |
| Company form | **ТОВ** (товариство з обмеженою відповідальністю / LLC) |
| VAT (ПДВ) threshold | **₴1,000,000** taxable supplies over any rolling 12 months |
| Minimum wage (мінімальна зарплата) 2026 | ₴8,647/month *(verify current value)* |
| Living wage (прожитковий мінімум) 2026 | ₴3,328 for an able-bodied person *(verify current value)* |
| Primary legislation | Tax Code of Ukraine (Податковий кодекс); Law "On State Registration of Legal Entities, Individual Entrepreneurs and Public Formations" No. 755-IV; Law "On Limited and Additional Liability Companies" No. 2275-VIII; Law on ЄСВ No. 2464-VI |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Ukrainian accountant |
| Skill version | 1.0 |

> **Wartime note (martial law):** Figures below are as of **1 January 2026**. Single-tax fixed amounts and the ЄСВ minimum are pinned at their 1-Jan values for the whole year and do **not** change mid-year. The elevated 5% military levy (військовий збір) on wages and the 1% military levy on Group 3 income remain in force under martial law. *(Verify current procedure — wartime rules change frequently.)*

### Conservative defaults

When information is missing, default to the safer (more conservative) assumption and flag it:

1. **Default to Group 3 (5%)** for a freelancer / IT contractor / online business unless the client confirms they only serve Ukrainian consumers and want the lowest fixed cost. Group 3 is the only group that may invoice **foreign clients** and **legal entities** without restriction. Do not assume Group 1 or 2 eligibility.
2. **Assume the single-tax election is NOT automatic.** A ФОП registered without a timely election lands on the **general system** (загальна система) by default. Always confirm the election was filed.
3. **Assume VAT registration is required** once taxable turnover crosses ₴1,000,000 in any rolling 12 months — even for a ФОП — unless the client is a single-tax payer for whom the threshold-based mandatory rule is disapplied (single-tax payers register for VAT only when they opt into the 3% Group 3 rate or voluntarily). *(Verify current procedure.)*
4. **Assume ЄСВ is due** at the minimum monthly amount unless a documented exemption applies (age/length-of-service pensioner, or person with disability receiving the corresponding pension/assistance).
5. **Never confirm a КВЕД code is "allowed on single tax" from memory** — check the barred-activities list (see `ua-single-tax`) and flag for reviewer confirmation.
6. Treat all amounts and deadlines as **"verify current value/procedure"** before relying on them for a filing. Defer the final call to a qualified Ukrainian accountant.

## Section 2 — ФОП registration, step by step

- **Nature of ФОП** — A ФОП is not a separate legal entity — it is an individual who has acquired the status of entrepreneur. There is no charter capital, and the individual is personally liable for business debts with their personal assets. State registration of a ФОП is free of charge.  _(Section 2 — ФОП registration, step by step)_

### 2.1 Choose your registration channel

**Registration channel table**

| Channel | How | Notes |
| --- | --- | --- |
| **Diia portal / app** (recommended) | diia.gov.ua → "Реєстрація ФОП". Authenticate via **BankID**, **Diia.Signature (Дія.Підпис)**, or a **qualified electronic signature (КЕП/QES)**. | Fastest, free, fully online; can take ~5–10 minutes to submit. Registration is automatic with no registrar involvement. Result usually available within ~1 business day (statutory limit up to 24 hours / 1 business day). *(Verify current procedure.)* |
| **State registrar (ЦНАП)** | In person at a Центр надання адміністративних послуг (Administrative Services Centre). | Submit form **Form 1** (заява про державну реєстрацію ФОП) + ID. Useful if you have no QES. |
| **Notary** | A notary acting as a state registrar. | Convenient if you also need notarised documents; notary charges a fee. |

### 2.2 Documents / information needed

- **Ukrainian passport / ID card** (or a valid passport shown via the Diia app v2.0+); foreign nationals: passport with a notarised Ukrainian translation plus a residence document.
- **РНОКПП** (реєстраційний номер облікової картки платника податків — taxpayer ID number, the "tax number"), or **УНЗР** (the 13-digit unique record number on the ID card).
- **Registered address** (місце проживання) — used as the ФОП's address.
- **Chosen КВЕД codes** (see 2.3).
- **Chosen tax system** and, if simplified, the **single-tax group** (see Section 3).
- For Diia: an active **BankID**, **Diia.Signature**, or **QES (КЕП)**.

### 2.3 Choose КВЕД activity codes

- **КВЕД** — Класифікатор видів економічної діяльності (the activity classifier). The current edition is КВЕД-2010 (ДК 009:2010). A migration to NACE 2.1-UA is planned for 1 January 2027 — until then КВЕД-2010 applies. (Verify current value.)  _(2.3 Choose КВЕД activity codes)_
- **Number of codes and primary code** — You may register as many codes as you like, but exactly one must be the primary (основний) code — the one generating the most income. Practitioners typically register 5–7 codes up front to avoid filing changes later.  _(2.3 Choose КВЕД activity codes)_
- **Barred activities block single-tax registration** — Critical for single-tax eligibility: your codes must not fall under the barred activities list for the simplified system (e.g. excise goods production/trade, gambling, currency exchange, mining of precious metals/stones, certain financial intermediation). See `ua-single-tax` for the full list. A barred КВЕД blocks single-tax registration.  _(2.3 Choose КВЕД activity codes)_

Common freelancer/IT examples *(verify the exact code matches the work)*: **62.01** Computer programming; **62.02** Computer consultancy; **63.11** Data processing/hosting; **70.22** Business and management consulting; **73.11** Advertising agencies.

### 2.4 Elect the tax system at registration

- **Filing the single-tax election** — The single-tax election is filed via the заява про обрання спрощеної системи оподаткування (application to choose the simplified system). On Diia it is submitted together with the ФОП registration application.  _(2.4 Elect the tax system at registration)_
- **Timing rule for election** — if the election is filed within 10 days of state registration, the ФОП is treated as a single-tax payer from the date of registration (for Group 3 and the general rule; for Groups 1/2 the simplified status starts from the first day of the following month). Miss this window and you sit on the general system until you can switch from the start of a future quarter. (Verify current procedure.)  _(2.4 Elect the tax system at registration)_
- **Switching later** — to move onto / between single-tax groups afterwards, file the application no later than 15 calendar days before the start of the next quarter; the new status takes effect from that quarter's first day.  _(2.4 Elect the tax system at registration)_
- **Default if no action** — If you take no action, you default to the general system (загальна система — 18% personal income tax + 5% military levy on net profit; see `ua-income-tax`).  _(2.4 Elect the tax system at registration)_

### 2.5 ЄСВ (unified social contribution) registration

- **Automatic ЄСВ registration** — Registration as an ЄСВ payer is automatic on ФОП registration — the State Tax Service picks it up from the ЄДР; no separate ЄСВ application is normally required.  _(2.5 ЄСВ (unified social contribution) registration)_
- **ЄСВ rate/minimum** — 22% of the minimum wage, i.e. a minimum of ₴1,902.34/month in 2026 (≈ ₴5,707.02/quarter), payable regardless of income and even if there was no income that month, unless an exemption applies. (Verify current value.)  _(2.5 ЄСВ (unified social contribution) registration)_
- **Exemptions** — Age/length-of-service pensioners, and persons with disability who actually receive the corresponding pension or social assistance, may be exempt from ЄСВ.  _(2.5 ЄСВ (unified social contribution) registration)_
- **Quarterly reporting from 2026** — From 2026 ФОПs file a unified quarterly report (ЄСВ + PIT/military levy) instead of monthly reporting. See `ua-social-contributions`.  _(2.5 ЄСВ (unified social contribution) registration)_

### 2.6 Open a business bank account

- **Dedicated business account required** — A ФОП should open a dedicated current account for business activity (підприємницький рахунок) — separate from any personal card. Single-tax receipts must flow through the business account.  _(2.6 Open a business bank account)_

Opening is free at most banks (Privat24, Monobank, Oschadbank, Raiffeisen, etc.) and is often available online once the ФОП is in the ЄДР.

- **Heightened monitoring for new ФОП** — Newly registered ФОПs face heightened financial monitoring in roughly the first 6 months — expect transfer limits and documentation requests. (Verify current procedure.)  _(2.6 Open a business bank account)_

### 2.7 What you receive

- An **extract from the ЄДР (витяг з Єдиного державного реєстру)** confirming the ФОП and КВЕД codes — downloadable from the Diia account/cabinet.
- Tax-payer registration with the **ДПС** and, if elected, single-tax status from the relevant start date.

### 2.8 Timing & cost summary

**Timing & cost summary table**

| Item | Cost | Time |
| --- | --- | --- |
| State registration of ФОП | **Free** | Up to 1 business day (often same day via Diia) |
| КЕП / QES (if needed) | Free–₴ small fee depending on provider | Same day |
| Single-tax election | Free (filed with registration) | — |
| Bank account | Usually free | Same day–few days |

## Section 3 — Choosing the tax system at formation (decision table)

**Tax system decision table**

| Question | Group 1 | Group 2 | Group 3 | General system |
| --- | --- | --- | --- | --- |
| Typical user | Market/retail trader, household services | Services & production for **Ukrainian** consumers and single-tax payers | **Freelancers, IT, exporters, B2B, foreign clients** | High-cost or barred-activity businesses; those exceeding limits |
| May serve **legal entities / VAT payers / foreign clients**? | No (only retail to public) | Only the **population** and other single-tax payers — **not** general-system businesses | **Yes — anyone, incl. foreign** | Yes |
| Employees allowed | **0** | up to **10** | **unlimited** | unlimited |
| 2026 annual income limit | **₴1,444,049** (167 × min wage) | **₴7,211,598** (834 × min wage) | **₴10,091,049** (1,167 × min wage) | none |
| Single-tax rate (2026) | up to **₴332.80/month** fixed (≤10% of living wage) | up to **₴1,729.40/month** fixed (≤20% of min wage) | **5% of income** (non-VAT) or **3% + VAT** | n/a |
| Military levy (військовий збір) 2026 | **₴864.70/month** fixed | **₴864.70/month** fixed | **1% of income** | 5% of net profit |
| ЄСВ | ₴1,902.34/month min | ₴1,902.34/month min | ₴1,902.34/month min | ₴1,902.34/month min (on profit, capped) |
| Income tax (ПДФО) | none (covered by single tax) | none | none | **18% of net profit** |
| Bookkeeping burden | Lowest | Low | Low–medium | **Highest** (income & expense ledger, documents) |

*(All amounts: verify current value before relying on them.)*

- **Default routing logic** — - Foreign clients, IT/dev, B2B services, or expecting >₴7.2m → **Group 3 (5%)**. - Local services/production, only Ukrainian customers, ≤10 staff, predictable low cost → **Group 2**. - Tiny local retail/household services, no employees → **Group 1**. - Barred КВЕД, very high turnover, or VAT-recovery-heavy operations → **general system** (and likely VAT registration).  _(Section 3 — Choosing the tax system at formation (decision table))_

> Detailed group rules, limits and barred activities live in **`ua-single-tax`**. General-system profit tax lives in **`ua-income-tax`**. ЄСВ lives in **`ua-social-contributions`**.

## Section 4 — VAT (ПДВ) registration

- **Mandatory VAT threshold** — taxable supplies exceeding ₴1,000,000 (excluding VAT) over the last rolling 12 months. The registration application must be filed no later than the 10th day of the month following the month the threshold was crossed.  _(Section 4 — VAT (ПДВ) registration)_
- **Single-tax payers excluded from mandatory VAT rule** — Single-tax payers are excluded from the turnover-based mandatory rule. A Group 1/2/3 ФОП on the non-VAT track does not auto-register for VAT just for crossing ₴1m; they become a VAT payer only by opting into the 3% Group 3 rate or registering voluntarily. A general-system business does hit the mandatory ₴1m rule. (Verify current procedure.)  _(Section 4 — VAT (ПДВ) registration)_
- **Standard VAT rate** — 20% (reduced rates apply to specific supplies, e.g. certain pharmaceuticals/medical 7%, some agricultural 14%). (Verify current value.)  _(Section 4 — VAT (ПДВ) registration)_
- **Voluntary registration** — Voluntary registration is available before the threshold — useful if your customers are VAT payers who want input-VAT credits, or you incur large input VAT you want to recover. Voluntary VAT for a freelancer is usually not worthwhile due to reporting and the electronic VAT administration system (СЕА ПДВ / electronic VAT account) overhead.  _(Section 4 — VAT (ПДВ) registration)_

Full mechanics, return preparation (Декларація з ПДВ) and the electronic VAT account are in **`ukraine-vat`**.

## Section 5 — ФОП vs ТОВ comparison

**ФОП vs ТОВ comparison table**

| Feature | **ФОП** (sole proprietor) | **ТОВ** (LLC) |
| --- | --- | --- |
| Legal nature | Individual with entrepreneur status — **not** a separate legal entity | Separate **legal entity** |
| Liability | **Personal** — owner liable with personal assets | **Limited** to contributions to charter capital |
| Charter capital | **None** | **No statutory minimum** (can be ₴1); must be declared & contributed within **6 months** of registration *(verify current procedure)* |
| Founders / owners | One individual | 1+ participants (учасники), individuals and/or entities |
| Registration | Free, ~1 day via Diia | Free state fee; needs a **charter (статут)** and founders' decision; ~1 day once docs ready, but more prep |
| Tax options | Single tax (Groups 1/2/3) **or** general system | **Corporate income tax 18%** (general) **or** single tax **Group 3** (5% / 3%+VAT) |
| Drawing money out | Owner's profit is freely available (no extra tax on withdrawal) | Profit distributed as **dividends** — additional taxation on distribution |
| Accounting | Light (single tax) to moderate (general) | **Full double-entry accounting**, financial statements, accountant usually required |
| Closing | Relatively quick (see Section 8) | **Liquidation** procedure — slow, formal, can take months |
| Best for | Freelancers, solo consultants, IT contractors, small service businesses | Multiple founders, investor/partner structures, limited-liability needs, larger operations, businesses needing to scale or sell |

### When a ТОВ makes sense

- **When a ТОВ makes sense** — - You have **partners / co-founders** or want to bring in investors / split equity. - You need **limited liability** to ring-fence personal assets from business risk. - Your turnover/headcount will **exceed the Group 3 single-tax limit** (₴10.09m / 2026) or your activity is **barred** from the simplified system. - You plan to **sell the business** or build something institutional.  _(When a ТОВ makes sense)_

### ТОВ on single tax (Group 3)

- **ТОВ Group 3 election** — A ТОВ may itself elect the Group 3 single tax (5% non-VAT or 3% + VAT) instead of the 18% corporate income tax, if it meets Group 3 conditions (within the income limit, permitted activities, ≤25% owned by non-single-tax legal entities, etc.). This gives a small company a flat 5% turnover tax similar to a Group 3 ФОП — but the company still bears full accounting, and profit taken out as dividends is taxed again. So a Group 3 ФОП is usually cheaper for a true solo operator; a Group 3 ТОВ suits a small team that needs limited liability. (Verify current eligibility conditions.)  _(ТОВ on single tax (Group 3))_

## Section 6 — Worked examples

> Illustrative only. Round figures; **verify current values** before filing.

### Persona A — "Oksana", freelance web developer with foreign clients

Invoices US/EU clients ~₴1.2m/year. Foreign clients ⇒ **must use Group 3** (Groups 1/2 cannot serve foreign or legal-entity clients). Registers ФОП via **Diia**, picks КВЕД **62.01**, files the single-tax election **within 10 days** ⇒ Group 3 from registration date. Annual cost: **5% single tax + 1% military levy** on income, plus **₴1,902.34/month ЄСВ**. Stays **below ₴1m? No — above** — but single-tax payers are exempt from the turnover-based mandatory VAT rule, so **no VAT registration** needed unless she opts for the 3% track. **Routing:** `ua-single-tax`, `ua-social-contributions`.

### Persona B — "Petro", local barber

Serves walk-in customers (the public) only, employs 2 people, ~₴900k/year. Eligible for **Group 2** (services to population, ≤10 employees, within ₴7.21m limit). Fixed **₴1,729.40/month** single tax + **₴864.70/month** military levy + **₴1,902.34/month** ЄСВ, regardless of monthly takings. Registers via Diia with КВЕД **96.02** (hairdressing). **Routing:** `ua-single-tax`.

### Persona C — "Maria & Andrii", two co-founders launching a SaaS

Want **limited liability**, plan to raise investment and hire a team. A ФОП can't have co-owners ⇒ form a **ТОВ** with a charter and two participants. Elect **Group 3 (5%)** while under the ₴10.09m limit to keep tax simple; switch to 18% corporate tax if they outgrow it or need VAT recovery at scale. Note dividends to founders are taxed on distribution. **Routing:** this skill + a qualified accountant for the charter and accounting setup.

### Persona D — "Ihor", IT contractor crossing into VAT territory

Group 3 ФОП billing one large Ukrainian VAT-paying client ~₴3m/year. As a non-VAT single-tax payer he is **not forced** to register for VAT by turnover. But his client wants input-VAT credits, so he considers **voluntary VAT** + the **3% Group 3 track**. Trade-off: 3% + 20% VAT admin (СЕА ПДВ) vs 5% and no VAT. **Routing:** `ukraine-vat` + reviewer to model the net cost.

## Section 7 — Tier 2 (escalate to a qualified Ukrainian accountant)

Stop and route to a credentialed Ukrainian accountant/lawyer when:

- The client is a **foreign national / non-resident** wanting to register a ФОП or ТОВ (residence, translation, immigration and tax-residency issues).
- **КВЕД selection is ambiguous** or may touch a **barred activity** (excise goods, gambling, financial services, precious metals, currency exchange).
- A **ТОВ** is involved — charter drafting, beneficial-ownership (UBO) declaration, charter capital, dividends.
- **VAT** registration, the electronic VAT account (СЕА ПДВ), or the 3% vs 5% decision.
- Mid-year **switching** between tax systems/groups, or retroactive corrections.
- **ЄСВ exemption** claims (pensioner / disability) or **closure / liquidation**.
- Anything under evolving **martial-law** rules where the procedure may have changed.

### 8.1 Closing / deregistering a ФОП (basics)

- **Closing / deregistering a ФОП steps** — 1. **File for state deregistration (припинення підприємницької діяльності)** via **Diia** or a state registrar — free, and the ЄДР record is updated quickly (often ~1 day). 2. **Deregistration does NOT end tax obligations.** You must still: - File a **final single-tax / income declaration** for the period up to the closure date. - **Pay outstanding single tax, military levy, ЄСВ, and any VAT** up to closure. - **Cancel VAT registration** if registered. - **ЄСВ is owed up to the month of closure** — file the closing ЄСВ report and settle. 3. Keep all **records and primary documents** for the statutory retention period (generally **1095 days / 3 years**, longer in some cases). *(Verify current value.)* 4. The ДПС may run a **closing review**; debts surviving closure are pursued against the individual personally. *(Verify current procedure.)*  _(8.1 Closing / deregistering a ФОП (basics))_

### 8.2 Formation checklist

- [ ] РНОКПП / tax number confirmed; ID ready (passport or Diia app)
- [ ] Registration channel chosen (Diia / ЦНАП / notary); QES or BankID ready if online
- [ ] КВЕД codes selected (1 primary + extras; none barred from single tax)
- [ ] Tax system decided (Group 1/2/3 vs general); single-tax **заява** filed **within 10 days**
- [ ] ЄСВ payer status confirmed (auto); exemption checked if pensioner/disability
- [ ] Turnover projected vs **₴1,000,000** VAT threshold; voluntary VAT considered
- [ ] Business **current account** opened; aware of 6-month monitoring on new ФОП
- [ ] ЄДР extract (витяг) downloaded; ДПС registration confirmed
- [ ] Reporting calendar noted (quarterly unified report from 2026); reviewer sign-off obtained

### 8.3 Authorities & sources

- **Diia** — diia.gov.ua (ФОП registration, ЄДР extract, changes, closure)
- **State Tax Service (ДПС)** — tax.gov.ua; taxpayer e-cabinet cabinet.tax.gov.ua
- **Ministry of Justice** — ЄДР (Unified State Register)
- **КВЕД-2010** classifier — kved.ukrstat.gov.ua (State Statistics Service)
- Tax Code of Ukraine; Law No. 755-IV (state registration); Law No. 2275-VIII (LLCs); Law No. 2464-VI (ЄСВ)
- Big-4 reference: PwC *Worldwide Tax Summaries — Ukraine*

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT** assert that single-tax status is automatic on ФОП registration — without a timely **заява** the ФОП defaults to the **general system**. - **Do NOT** place a ФОП with **foreign or legal-entity clients** into Group 1 or Group 2 — only **Group 3** may serve them. - **Do NOT** confirm a КВЕД code is single-tax-eligible from memory; check the barred-activities list in `ua-single-tax` and flag for reviewer confirmation. - **Do NOT** tell a single-tax ФОП they must register for VAT merely for crossing ₴1m — the turnover-based mandatory rule does not apply to single-tax payers (verify). - **Do NOT** state ЄСВ can be skipped because there was no income — it is due at the minimum monthly amount unless a documented exemption (pensioner / disability) applies. - **Do NOT** advise a non-resident / foreign founder without escalating to a qualified Ukrainian professional. - **Do NOT** treat ФОП deregistration as ending tax/ЄСВ liabilities — final declarations, payments and (if applicable) VAT cancellation are still required. - **Do NOT** present any amount, rate, limit, or deadline as final without a **"verify current value/procedure"** flag and reviewer sign-off. - **Do NOT** draft a ТОВ charter, UBO declaration, or liquidation documents — route to a lawyer.  _(PROHIBITIONS)_

## Disclaimer

This skill is **research-verified** against public sources (State Tax Service tax.gov.ua, Diia diia.gov.ua, Ministry of Justice, and Big-4/PwC material) for the **2026** tax year as of **May 2026**, but is **pending sign-off by a qualified Ukrainian accountant**. Ukrainian rules — especially under martial law — change frequently; figures, thresholds, and procedures marked "verify current value/procedure" must be confirmed against current official sources before relying on them. This is general information, **not** tax, legal, or accounting advice, and does not create a professional relationship. Every output must be reviewed and signed off by a qualified Ukrainian accountant or licensed adviser before it reaches a taxpayer or any authority. Part of the Open Accountants open-source tax-skills project — **openaccountants.com**.

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
