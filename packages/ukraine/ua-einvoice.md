---
name: ua-einvoice
description: Use this skill whenever asked about Ukrainian electronic invoicing and digital tax reporting for self-employed people and small businesses. Trigger on phrases like "Ukraine tax invoice", "податкова накладна", "ЄРПН", "VAT invoice registration Ukraine", "register tax invoice Ukraine", "СЕА ПДВ", "VAT account Ukraine", "ПРРО receipt", "fiscal receipt Ukraine FOP", "blocked tax invoice", "зупинення реєстрації ПН", "СМКОР", "КЕП Ukraine", "Електронний кабінет", "SAF-T Ukraine", or any question about how a Ukrainian VAT payer or ФОП issues invoices and reports electronically. Covers the VAT tax invoice and its mandatory ЄРПН registration, the SMKOR registration-blocking system, the СЕА ПДВ electronic VAT administration system and the VAT account, ПРРО software fiscal receipts for retail, qualified electronic signatures (КЕП), the Електронний кабінет, and the status of SAF-T UA. ALWAYS read this skill before any Ukrainian e-invoicing or digital tax-reporting work.
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

# UA Einvoice

## Ukraine Electronic Invoicing & Digital Tax Reporting — Self-Employed Skill v1.0

This skill explains how a Ukrainian self-employed person interacts with the State Tax Service's digital machinery: issuing and registering the VAT tax invoice (**податкова накладна**) in the Unified Register (**ЄРПН**), the risk engine that can freeze that registration (**СМКОР**), the electronic VAT administration system (**СЕА ПДВ**) and its VAT account, software fiscal receipts (**ПРРО**) for anyone taking money at retail, qualified electronic signatures (**КЕП**), the taxpayer portal (**Електронний кабінет**), and where SAF-T UA stands in 2026.

The single most important split: a **non-VAT ФОП** has *light* duties (keep primary documents, run a ПРРО if they take cash/card retail payments) and **never touches ЄРПН**. A **VAT-registered taxpayer** carries the *full* electronic burden — tax invoices, ЄРПН registration deadlines, the СЕА ПДВ VAT account, and exposure to СМКОР blocking.

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ukraine |
| Scope | Electronic invoicing & digital tax reporting for self-employed (ФОП) and small businesses |
| Currency | UAH (₴) |
| Core systems | **ЄРПН** (Unified Register of Tax Invoices) · **СЕА ПДВ** (electronic VAT administration) · **ПРРО** (software fiscal receipts) |
| Tax authority | Державна податкова служба України (**ДПС** / State Tax Service) |
| Portal | **Електронний кабінет платника** — cabinet.tax.gov.ua |
| Authentication | **КЕП** (qualified e-signature), Дія.Підпис, cloud КЕП, BankID/MobileID via id.gov.ua |
| Primary legislation | Tax Code of Ukraine (Податковий кодекс), Art. 187, 201; CMU Resolution No. 1165 (СМКОР); Law on RRO/ПРРО No. 265/95-ВР |
| VAT registration threshold | ₴1,000,000 taxable supplies over the last 12 months (mandatory); voluntary below |
| Standard VAT rate | 20% (also 14% / 7% / 0% in specific cases) |
| ЄРПН registration deadline (martial-law rules, in force 2026) | Invoices dated 1st–15th → by **5th** of next month; 16th–end → by **18th** of next month |
| ЄРПН deadline (peacetime Tax Code baseline) | 1st–15th → by last day of same month; 16th–end → by 15th of next month *(suspended under martial law)* |
| SAF-T UA | On-demand only (no general mandatory periodic filing as of May 2026 — *verify*) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Ukrainian accountant/auditor |
| Skill version | 1.0 |

> **Wartime note.** Martial law has been in force since 24 Feb 2022 and remains in force in 2026. Several deadlines below run on the *special martial-law schedule*, which differs from the peacetime Tax Code baseline. When martial law ends the peacetime ЄРПН deadlines resume. Always confirm the current regime before quoting a date.

### Conservative defaults

When facts are missing, assume the position that **minimises filing risk and penalty exposure**:

1. **If unsure whether the client is VAT-registered → treat them as a non-VAT ФОП** for invoicing (no ЄРПН, no tax invoice) but **flag that VAT status must be confirmed**, because if they *are* VAT-registered, missing ЄРПН registration is the costlier error.
2. **Register the tax invoice as early as possible** — never wait for the deadline; the ЄРПН penalty clock and the СМКОР blocking risk both grow with delay.
3. **Assume a ПРРО is required** for any cash or card retail settlement unless the client is clearly in an exempt category (e.g. Group 1 ФОП within its narrow exemption). Default to issuing a fiscal receipt.
4. **Assume the supplier registers the tax invoice**, not the buyer — only the seller can register a податкова накладна in ЄРПН.
5. **Treat any "blocked invoice" as urgent** — unblocking has its own deadlines; do not let it sit.
6. **Pin amounts and thresholds to 1 January 2026 values** and verify against tax.gov.ua before relying on a figure for a filing.

## Section 2 — Who must do what

### A. Non-VAT ФОП (single tax Group 1/2/3 non-VAT, or general-system non-VAT)

- **Non-VAT ФОП obligations** — A sole proprietor **not registered for VAT** has **no податкова накладна and no ЄРПН obligations whatsoever**. Their electronic duties are limited to: - **Primary documents (первинні документи).** Issue and keep invoices/acts (рахунок, акт виконаних робіт), contracts, and bank records to substantiate income. A non-VAT ФОП's "invoice" is a *commercial* document (рахунок-фактура / invoice), **not** a VAT податкова накладна — these are different things and must not be confused. - **ПРРО fiscal receipts** — required when the ФОП accepts cash or card payments at retail (see Section 4). Group 1 ФОП are largely exempt; Groups 2–3 generally must use a ПРРО. - **Електронний кабінет** for filing the single-tax declaration and viewing obligations, accessed with a **КЕП**. A non-VAT ФОП never registers anything in ЄРПН and is never blocked by СМКОР.

### B. VAT-registered taxpayer (ФОП or company)

- **VAT-registered taxpayer obligations** — A taxpayer registered for VAT (mandatory once taxable supplies exceed **₴1,000,000** over 12 months, or voluntary before that) carries the full electronic load: - **Issue a податкова накладна** for each taxable supply (and розрахунок коригування / adjustment calculation for changes). - **Register every податкова накладна in ЄРПН** within the statutory deadline (Section 3). - **Operate within СЕА ПДВ** — the registration limit (∑Накл formula) and the VAT account (Section 3). - **Survive СМКОР** — risk monitoring may suspend (block) registration of an invoice. - **Run a ПРРО** if also doing retail settlements. - Authenticate everything with a **КЕП**. > A Group 3 ФОП may elect the **3% single-tax + VAT** path (vs the 5% non-VAT path). Electing VAT pulls the ФОП fully into ЄРПН / СЕА ПДВ / СМКОР. Defer the rate-vs-VAT decision to `ua-single-tax`; this skill handles the *mechanics* once VAT-registered.

## Section 3 — Tax invoice (податкова накладна) & ЄРПН registration

### What it is

- **Податкова накладна (ПН) and ЄРПН** — The **податкова накладна (ПН)** is the VAT document a registered supplier issues for each taxable supply. It is the buyer's basis for an input-VAT credit (податковий кредит) — but **only once it is registered in ЄРПН**. An unregistered ПН gives the buyer no credit, so timely registration is a commercial obligation as much as a tax one. The **Єдиний реєстр податкових накладних (ЄРПН)** is the single State-Tax-Service register through which all ПН and розрахунки коригування (РК / adjustment calculations) pass. Only the **supplier** registers a ПН; the buyer cannot.

### When the ПН arises

- **First event rule** — By default a ПН is dated to the **first event** — the earlier of (a) payment received or (b) goods/services supplied (Tax Code Art. 187). The registration deadline runs from that ПН date.  _(Tax Code Art. 187)_

### Registration deadlines

**ЄРПН registration deadlines — martial law**

| ПН/РК dated | Register in ЄРПН by |
| --- | --- |
| 1st – 15th of the month | **5th** calendar day of the following month |
| 16th – last day of month | **18th** calendar day of the following month |

Registration is temporarily permitted on weekends during martial law (so a deadline falling on a weekend is *not* pushed forward, and you can register on the day). Verify the current working/weekend rule before relying on a weekend submission.

**ЄРПН registration deadlines — peacetime baseline**

| ПН/РК dated | Register in ЄРПН by |
| --- | --- |
| 1st – 15th of the month | last day of the **same** month |
| 16th – last day of month | **15th** of the following month |

- **Outer backstop for registration** — Outer backstop in either regime: ПН/РК cannot be registered later than the relevant maximum window the Tax Code allows (commonly cited as up to ~365 days for late registration before the right to register lapses) — *verify* the exact outer limit for the period in question.

### Late-registration penalties

- **Late registration penalty scaling** — Penalties scale with the length of the delay, broadly **2% up to 25%** of the VAT amount in the invoice (graduated by days late), with separate (heavier) rules for invoices that are never registered. Confirm the current banded percentages on tax.gov.ua before quoting them to a client.

### СЕА ПДВ (electronic VAT administration) and the VAT account

- **СЕА ПДВ, VAT account, registration limit** — Registration of a ПН in ЄРПН is gated by the **СЕА ПДВ** (Система електронного адміністрування ПДВ). Each VAT payer has: - A dedicated **electronic VAT account (електронний ПДВ-рахунок)** opened automatically in the Treasury. The payer tops it up; funds there are used to pay VAT liabilities. - A **registration limit (∑Накл / реєстраційна сума)** — the maximum VAT amount of invoices the payer can register at any moment. Simplified, it is built up from the VAT on *received* registered invoices plus customs VAT paid plus money lodged on the VAT account, minus the VAT on *issued* registered invoices and VAT declared. If the registration limit is **insufficient**, the system will **not let the supplier register the ПН** until they top up the VAT account (or until incoming registered invoices raise the limit). This is a cash-flow trap that catches growing businesses — flag it whenever a client reports "the system won't register my invoice and it isn't blocked."

### СМКОР — blocking (зупинення реєстрації) of tax invoices

- **СМКОР definition and layers** — **СМКОР** (Система моніторингу відповідності ПН/РК критеріям оцінки ступеня ризиків; risk-criteria monitoring system, under CMU Resolution No. 1165) automatically screens each ПН/РК on submission. If it trips a risk criterion, registration is **suspended (заблокована / зупинена)** — the invoice is neither registered nor rejected; it is frozen pending documentary justification. Three layers the system checks: 1. **Unconditional-registration criteria** — small/low-risk invoices pass automatically. 2. **Risky-taxpayer status (ризиковий платник)** — if the payer is flagged as risky, its invoices block by default. Risk can be inherited (e.g. a new entity with the same director/founder/accountant as a flagged one is cross-matched and tagged) and must be actively contested. 3. **Risk criteria for the operation** — e.g. **mismatch of input vs output product/service codes (УКТ ЗЕД / ДКПП)**: "bought bricks, sold construction services" looks anomalous and blocks.  _(CMU Resolution No. 1165)_
- **Data Table (Таблиця даних платника) pre-emption** — **Pre-empting blocks — the Data Table (Таблиця даних платника).** A payer can file a **Таблиця даних** declaring its normal input and output codes. Once the tax commission accepts it, future invoices with those codes are not suspended for that reason — the single most effective protection against repeat blocking.
- **Blocked invoice process** — **When an invoice is blocked:** the payer files documentary explanations and supporting documents through the Електронний кабінет; the regional commission decides to register or refuse within the statutory window. A refusal can be appealed administratively to ДПС and then in court. Treat every block as time-sensitive — there are deadlines to submit documents and to appeal.

## Section 4 — ПРРО fiscal receipts (software RRO)

- **ПРРО definition** — A **ПРРО (програмний реєстратор розрахункових операцій)** is the *software* fiscal cash register — a free State-provided app (and third-party equivalents) that issues fiscal receipts and reports settlements to ДПС in real time. It replaced/supplemented the old hardware РРО.

### Who must use a ПРРО (or РРО)

**ПРРО/РРО requirement by taxpayer type**

| Taxpayer | ПРРО / РРО required? |
| --- | --- |
| **Group 1 ФОП** | **No** — broad exemption, *except* sales of technically complex goods under warranty, medicines/medical devices, jewellery & precious-metal goods |
| **Group 2 ФОП** | **Yes** for cash/card settlement transactions (obligation does not depend on turnover or activity in 2026 — *verify wording for the client's exact activity*) |
| **Group 3 ФОП** | **Yes** for cash/card settlements; also triggered once income passes the РРО threshold |
| **General-system FOP / companies** | **Yes** for cash/card settlements |

- **Turnover trigger for ПРРО/РРО** — ~220 minimum wages as of 1 January (≈ ₴1.9 m for 2026 — verify the exact minimum wage and resulting figure) UAH (verify exact figure)
- **High-risk goods override** — Certain high-risk goods (jewellery, medicines, technically complex goods, excisable goods) require a ПРРО **regardless of turnover or group**.

### Fiscal receipt mechanics

- **Fiscal receipt issuance and timing** — - Issue a **fiscal receipt (фіскальний чек)** in paper or electronic form for every settlement. A non-fiscal "sales receipt" does not satisfy the obligation. - Card payments: the fiscal receipt must follow the bank transaction promptly (commonly cited as within ~5–10 minutes). A large gap between the bank transaction and the ПРРО receipt is itself a flagged violation. - Authenticate the ПРРО with a **КЕП**; receipts and the daily Z-report flow to ДПС.

### Penalties

- **ПРРО fiscal violation penalty** — 100% of the value of goods/services sold with a fiscal violation for a first offence; 150% for each subsequent one % (Full (post-moratorium) fines in 2026 — verify current banding before quoting)

> **Important distinction.** The **фіскальний чек** (ПРРО receipt, retail settlement evidence) and the **податкова накладна** (VAT document for ЄРПН) are entirely different documents serving different systems. A non-VAT ФОП issues fiscal receipts but never a ПН.

## Section 5 — КЕП & Електронний кабінет

- **Section intro** — 

### Qualified electronic signature (КЕП)

- **КЕП definition and options** — A **кваліфікований електронний підпис (КЕП)** is the legally binding e-signature used to sign and submit *everything* electronic to the State — ПН, declarations, ПРРО receipts, appeals. Options: - **File-based КЕП** from an accredited provider (наприклад ПриватБанк, Дія, Вчасно, etc.). - **Дія.Підпис** (Diia mobile signature) — issued free to individuals/ФОП. - **Cloud КЕП** — stored with a provider, used without a hardware token. - **BankID / MobileID** for identification (read-level access to some services). КЕП for individuals/ФОП is commonly obtained **free** via Дія or bank apps (e.g. Privat24).

### Електронний кабінет

- **Електронний кабінет portal structure** — The **Електронний кабінет платника** (cabinet.tax.gov.ua) is the ДПС taxpayer portal. It has: - A **public part** (no login) — registers, forms, calendars, validity checks. - A **private part** — accessed with a **КЕП** (or Дія.Підпис / cloud КЕП / id.gov.ua), where the taxpayer files declarations, registers ПН/ЄРПН, monitors the СЕА ПДВ VAT account and registration limit, manages ПРРО, responds to СМКОР blocks, and views liabilities. Most self-employed e-filing in this skill happens through the Електронний кабінет, signed with a КЕП.

## Section 6 — SAF-T UA status

- **SAF-T UA definition** — **SAF-T UA** (Standard Audit File for Tax — Ukrainian standardised XML accounting file) is Ukraine's standardised audit-data format, built for the tax authority's e-audit (електронний аудит) programme.
- **SAF-T UA status as of May 2026** — **Status as of May 2026 — verify before relying:** - The **general mandatory periodic SAF-T filing rollout was formally withdrawn** (Ministry of Finance, mid-2025). The earlier phased plan (large taxpayers from 2025, *all* VAT payers by Jan 2027) is **no longer the active mandate**. - SAF-T UA persists as an **on-demand obligation**: **large taxpayers** must produce the SAF-T UA XML file **on request during a tax audit**, not as routine periodic reporting. - The **e-audit system launched 1 January 2026** uses the SAF-T UA format as its data backbone; the current schema is **SAF-T UA 2.0** (simplified structure published late 2024). - For a **typical self-employed ФОП / small taxpayer, there is no routine SAF-T UA filing obligation in 2026.** Small/medium taxpayers were never the immediate target, and the blanket "all VAT payers by 2027" requirement has been withdrawn.

> **Flag for the reviewer.** The SAF-T timeline has changed repeatedly. Treat "small taxpayers have no SAF-T duty in 2026" as the working position but **confirm against tax.gov.ua / a Ukrainian accountant** for any client near the large-taxpayer threshold (₴500 m revenue over four quarters) or before advising on 2027.

## Section 7 — Worked examples

### Example 1 — Non-VAT Group 3 freelancer (no ЄРПН at all)

*Olena is a Group 3 ФОП on the 5% (non-VAT) path, an IT consultant invoicing a foreign client.*

- VAT-registered? **No.** → **No податкова накладна, no ЄРПН, no СЕА ПДВ, no СМКОР.**
- She issues a **commercial invoice (рахунок-фактура)** and signs an **акт** with the client; she keeps these as primary documents.
- No retail cash/card settlement → arguably **no ПРРО** for this work (bank-to-bank receipts for services to a business client). If she ever takes cash from individuals, the ПРРО question reopens.
- Files her single-tax declaration through the **Електронний кабінет**, signed with her **КЕП** (free via Дія).

**Outcome:** lightest digital footprint — primary documents + e-cabinet + КЕП only.

### Example 2 — VAT-registered Group 3 ФОП issuing and registering a ПН

*Petro is a Group 3 ФОП on the 3% + VAT path. He supplies services on 8 May 2026 for ₴120,000 incl. 20% VAT (₴20,000 VAT).*

- First event = supply on **8 May** → ПН dated 8 May.
- 8 May falls in the **1st–15th** band → register in ЄРПН **by 5 June 2026** (martial-law rule).
- Before registering, the system checks his **registration limit (∑Накл)** in СЕА ПДВ. If it is below ₴20,000, he must **top up his VAT account** to register.
- He registers via the Електронний кабінет, signed with his **КЕП**. Best practice: register the same week, not at the 5 June deadline.

**Outcome:** ПН registered on time; buyer gets input credit; no penalty.

### Example 3 — A blocked invoice (СМКОР)

*Same Petro registers a ПН where the output service code does not match his historical input codes. СМКОР suspends registration (зупинення реєстрації).*

- The ПН is **frozen**, not rejected. The buyer cannot claim credit yet.
- Petro submits **explanations + supporting documents** through the Електронний кабінет within the statutory window; the regional commission decides.
- To prevent recurrence he files a **Таблиця даних платника** listing his normal input/output codes; once accepted, future invoices with those codes won't block for that reason.
- If refused, he **appeals** to ДПС and, if needed, to court.

**Outcome:** registration restored after documentary justification; Data Table filed to stop repeat blocks.

### Example 4 — Group 2 ФОП taking card payments at retail (ПРРО)

*Mariya is a Group 2 ФОП running a small café, non-VAT.*

- Non-VAT → **no ЄРПН/ПН.**
- Cash/card retail settlements → she **must run a ПРРО** and issue a **фіскальний чек** for every sale; card receipts must follow the bank transaction promptly.
- ПРРО is signed/operated with her **КЕП**; daily Z-reports flow to ДПС.
- Failure to issue fiscal receipts → **100% / 150%** penalties.

**Outcome:** no VAT machinery, but full ПРРО/fiscal-receipt discipline.

## Section 8 — Tier 2 + Reference + Checklist

### Tier 2 ambiguities (escalate to a credentialed Ukrainian accountant)

- Whether a specific activity/group combination **triggers ПРРО** (the exemptions and thresholds have edge cases — high-risk goods override the group exemption).
- The **exact current ЄРПН outer registration window** and the **banded late-registration penalty** percentages for the period in question.
- **СМКОР unblocking strategy**, Data Table drafting, and removal from **ризиковий платник** status — these are advisory/contentious and often litigated.
- **SAF-T UA** applicability for any client near the large-taxpayer threshold or planning past 2026.
- The **VAT-vs-non-VAT election** for a Group 3 ФОП (3% vs 5%) — defer to `ua-single-tax`.
- Anything during a **martial-law deadline change** — confirm the live regime.

### Reference

- Tax Code of Ukraine (Податковий кодекс) — Art. 187 (date of liability), Art. 201 (tax invoices & ЄРПН).
- CMU Resolution **No. 1165** — СМКОР risk criteria, blocking and Data Table procedure.
- Law **No. 265/95-ВР** on RRO/ПРРО and fiscal receipts.
- State Tax Service — **tax.gov.ua / dps.gov.ua**; portal **cabinet.tax.gov.ua**.
- PwC Worldwide Tax Summaries — Ukraine (VAT threshold ₴1 m, rate 20%, ЄРПН/СЕА overview).

### Self-employed e-invoicing checklist

- [ ] Confirm **VAT status** — VAT-registered or not? (Determines whether ЄРПН applies at all.)
- [ ] Obtain/renew a **КЕП** (free via Дія / bank) and access the **Електронний кабінет**.
- [ ] **Non-VAT:** issue/keep **primary documents** (рахунок, акт); confirm whether a **ПРРО** is required and issue **fiscal receipts** for retail settlements.
- [ ] **VAT-registered:** for each supply, date the **ПН** to the first event and **register in ЄРПН** by the deadline (martial-law: 5th / 18th).
- [ ] Monitor the **СЕА ПДВ registration limit (∑Накл)** and **top up the VAT account** before registering when needed.
- [ ] File a **Таблиця даних** to pre-empt **СМКОР** blocking; treat any blocked invoice as urgent.
- [ ] **Register invoices early**, never at the deadline.
- [ ] Confirm there is **no routine SAF-T UA filing** duty for the client (small taxpayer) — flag if near the large-taxpayer threshold.

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT** issue or "register" a податкова накладна for a **non-VAT** ФОП — they have no ПН and no ЄРПН access. Confusing a commercial рахунок-фактура with a VAT податкова накладна is a category error. - **Do NOT** tell a buyer they can register a supplier's tax invoice — **only the supplier** registers in ЄРПН. - **Do NOT** quote ЄРПН registration deadlines without stating which regime (**martial-law** vs **peacetime baseline**) applies — they differ and the wrong one causes penalties. - **Do NOT** state exact late-registration or ПРРО penalty percentages, the ₴ ПРРО turnover trigger, or the SAF-T threshold as settled fact without verifying current figures on tax.gov.ua — they are pinned to the minimum wage and to changing law. - **Do NOT** assert that SAF-T UA is mandatory periodic reporting for small taxpayers — as of May 2026 it is **on-demand for large taxpayers**; verify before advising past 2026. - **Do NOT** advise on **СМКОР unblocking, Data Tables, or risky-status removal** as if routine — these are advisory/contentious matters for a credentialed practitioner. - **Do NOT** finalise any filing without **КЕП**-signed submission through the official **Електронний кабінет**. - **Do NOT** treat this skill as a substitute for credentialed review.

## Disclaimer

This skill is **research-verified** open-source guidance produced by the Open Accountants Community for use by AI agents assisting self-employed people. It reflects Ukrainian rules as understood for **tax year 2026 as of May 2026**, under martial law. Ukrainian e-invoicing and digital-reporting rules — ЄРПН deadlines, СМКОР criteria, ПРРО thresholds, penalties, and the SAF-T UA timeline — change frequently and are affected by martial-law measures. Figures and deadlines must be verified against the State Tax Service (tax.gov.ua / dps.gov.ua) before any filing.

It is **pending sign-off by a qualified Ukrainian accountant or auditor** and is **not** a substitute for professional advice or for credentialed review of any specific filing. Use at your own risk. Part of the openaccountants.com open-source skill library.

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
