---
name: ru-formation
description: Use this skill whenever asked about starting, registering, or formally setting up a business in Russia as a self-employed person. Trigger on phrases like "register ИП", "become самозанятый", "start a business Russia", "open sole proprietorship Russia", "ИП vs ООО", "how to register as self-employed in Russia", "Russian business registration", "ОКВЭД codes", "open a расчётный счёт", "choose tax regime at registration", "close ИП", "deregister самозанятый", "регистрация ИП", "как стать самозанятым", "открыть ООО". Covers becoming самозанятый via «Мой налог», registering as ИП (individual entrepreneur) via ФНС / Госуслуги / banks, the 800 ₽ state duty and the free electronic route, choosing ОКВЭД activity codes, choosing the tax regime at or after registration (НПД / УСН / ПСН / ОСНО) including the 30-day УСН election deadline, opening a расчётный счёт, a brief comparison with forming an ООО, the ЕГРИП / ЕГРЮЛ registers, timing and cost, and deregistering / closing an ИП or самозанятый. References ru-self-employed-npd, ru-usn, ru-income-tax, and ru-social-contributions for what happens after the entity exists.
version: 1.0
jurisdiction: RU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RU Formation

## Russia — Business Formation & Registration for Self-Employed People

This skill helps an AI agent guide a user through *legally setting up* to earn business income in Russia: registering as **самозанятый** (НПД), registering as an **ИП** (*индивидуальный предприниматель* — individual entrepreneur / sole proprietor), and understanding when forming an **ООО** (*общество с ограниченной ответственностью* — limited liability company) is worth it. It covers the registration mechanics, the state duty (*госпошлина*), choosing **ОКВЭД** activity codes, electing a tax regime, opening a business bank account (*расчётный счёт*), and deregistering / closing.

The AI replies to the user in the user's own language. Russian legal and tax terms are kept native (самозанятый, ИП, ООО, ОКВЭД, ФНС, Госуслуги, ЕГРИП, ЕГРЮЛ, расчётный счёт, госпошлина) so the meaning maps cleanly to the official wording the user will see on the forms.

This skill stops at *formation*. Once the entity exists, route to the operating skills: **ru-self-employed-npd** (НПД mechanics), **ru-usn** (simplified system), **ru-income-tax**, **ru-social-contributions** (страховые взносы), and **russia-vat** where relevant.

## 1. Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Russian Federation (RU) |
| What this covers | Becoming самозанятый (НПД); registering an ИП; choosing ОКВЭД + tax regime; opening a расчётный счёт; ИП-vs-ООО comparison; deregistration / closing |
| Currency | RUB (Russian ruble, ₽) |
| Registers | **ЕГРИП** (for ИП) / **ЕГРЮЛ** (for ООО and other legal entities); самозанятые are **не** entered in either register |
| Authority | **ФНС** (Federal Tax Service / Федеральная налоговая служба) — nalog.gov.ru |
| State duty (госпошлина) | **800 ₽** to register ИP on paper; **0 ₽** if filed electronically (Госуслуги, ФНС online, bank, МФЦ with e-signature, notary). ООО: **4,000 ₽** on paper, **0 ₽** electronically. Самозанятый: **0 ₽** always |
| Registration time | Самозанятый: minutes (instant). ИП / ООО: **≤ 3 working days** after a complete filing reaches ФНС |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Russian accountant |
| Version | 1.0 |

### Conservative defaults

When the user's facts are incomplete, the agent applies the safest reading and flags the assumption rather than guessing optimistically:

- **Default to the simplest legal form that fits.** If a person is a solo freelancer with no employees, no goods resale, and income comfortably under 2.4 млн ₽/year, default to **самозанятый (НПД)** — it is free, instant, and carries no страховые взносы and no reporting. Only escalate to ИП or ООО when the user's facts genuinely require it.
- **Never let the УСН election lapse silently.** If a new ИП wants УСН, the уведомление о переходе на УСН must be filed **with the registration documents or within 30 calendar days** of registration. Missing it drops the ИП onto **ОСНО** (the general regime, with VAT and НДФЛ) until the next calendar year. Always surface this deadline prominently.
- **Treat all rates, limits, and duties as point-in-time.** Russian tax law changes frequently (the 2026 reform notably cut the УСН/ПСН VAT-exemption and ПСН income limits). Where a figure drives a decision, the agent says "verify current value/procedure on nalog.gov.ru before relying on it".
- **Verify ОКВЭД codes against the official ОКВЭД 2 classifier** rather than inventing codes; the wrong code can block a regime (e.g. ПСН) or trigger questions.
- **Distinguish "can earn income" from "must register".** Casual one-off income may be reportable as an ordinary individual (НДФЛ via 3-НДФЛ); systematic business activity requires самозанятый / ИП / ООО status. When in doubt, flag it and recommend a Russian accountant.
- **No legal/registry actions are taken for the user.** The agent explains; the user files.

## 2. Becoming самозанятый (НПД) — instant registration via «Мой налог»

The **самозанятый** status (the Professional Income Tax / *Налог на профессиональный доход* / **НПД**) is the lightest possible way to legalise freelance income in Russia. There is **no state duty**, **no entry in any business register**, and **no separate filing** — registration is effectively instant.

**Who can become самозанятый**
- A Russian (or eligible EAEU) individual, **or an existing ИП** who switches to НПД.
- No employees (the самозанятый may not hire staff under labour contracts).
- Annual income **≤ 2,400,000 ₽** per calendar year.
- Activity is permitted for НПД — i.e. **own services, work, or self-made goods**. *Excluded*: resale of others' goods, подакцизные / маркированные goods, mining/extraction, agency/commission work, etc. (see ru-self-employed-npd for the full exclusion list).

**How to register (any one of these)**
1. **«Мой налог» app** (lknpd.nalog.ru or mobile) — register by passport photo + selfie, or via the ФНС личный кабинет, or via Госуслуги. This is the primary route.
2. **Госуслуги** (gosuslugi.ru) — links through to НПД registration.
3. **A partner bank** (Сбербанк, Т-Банк, Альфа-Банк, etc.) — many offer in-app самозанятый registration tied to an existing card/account.

**What happens at registration**
- ФНС confirms the status (usually same day; it can refuse within ~6 days if data mismatches).
- The person is **not** added to ЕГРИП or ЕГРЮЛ — they remain a физлицо with an НПД flag. Status can be checked on the public ФНС service (npd.nalog.ru → "Проверить статус самозанятого").
- No расчётный счёт is required — a самозанятый may receive money to an ordinary personal card and issues a **чек** through «Мой налог».

**Key facts to relay** (verify current values on nalog.gov.ru):
- Tax: **4%** on income from individuals, **6%** from legal entities / ИП.
- **No страховые взносы** are mandatory (pension contributions are voluntary).
- The regime is a federal experiment scheduled through **31.12.2028** — confirm it has not been changed before advising on a long horizon.

> Route to **ru-self-employed-npd** for чеки, the 10,000 ₽ deduction, monthly payment, and what to do when the 2.4 млн ₽ cap is hit.

- **НПД tax rate on income from individuals** — 4%  _(Skill body: 'Tax: 4% on income from individuals, 6% from legal entities / ИП.')_
- **НПД tax rate on income from legal entities / ИП** — 6%  _(Skill body: 'Tax: 4% on income from individuals, 6% from legal entities / ИП.')_
- **НПД annual income limit** — 2,400,000 RUB  _(Skill body: 'Annual income ≤ 2,400,000 ₽ per calendar year.')_
- **НПД regime sunset date** — Federal experiment scheduled through 31.12.2028 — confirm it has not been changed before advising on a long horizon.  _(Skill body: 'The regime is a federal experiment scheduled through 31.12.2028')_

## 3. Registering as ИП (individual entrepreneur) — step by step

An **ИП** is the right form when the user outgrows НПД (over 2.4 млн ₽, needs employees, resells goods, or wants ПСН / УСН with expense deductions) but a full company is overkill. An ИП is **not a separate legal person** — the individual remains personally liable for business debts with their own property, but enjoys far simpler accounting and reporting than an ООО.

### 3.1 Step-by-step

- **ИП registration steps** — 1. Choose ОКВЭД codes. Pick one main activity code and any number of additional codes from the official ОКВЭД 2 classifier. Use the narrowest codes that genuinely describe the work; codes can be added/changed later via form Р24001. Some regimes (especially ПСН) depend on the activity. 2. Choose the tax regime (see decision table in §3.3) and prepare the election (e.g. the УСН уведомление) so it can be filed with registration. 3. Prepare form Р21001 (the ИП application) — name, ИНН, passport data, ОКВЭД codes. The applicant needs an ИНН; if they don't have one, it is assigned during registration. 4. Choose a filing channel (see §3.2) and pay the 800 ₽ госпошлина only if filing on paper. Electronic filing is free. 5. Submit to ФНС. Registration is completed within 3 working days of a complete filing. 6. Receive the result. ФНС issues the Лист записи ЕГРИП (record sheet) electronically — the ИП is now entered in ЕГРИП. There is no longer a paper certificate (свидетельство). 7. Open a расчётный счёт if needed (see §3.4) and start operating.  _(Skill body §3.1 Step-by-step)_

### 3.2 Where / how to file (channels)

**Filing channels and state duty**

| Channel | State duty | Notes |
| --- | --- | --- |
| **Госуслуги** (gosuslugi.ru) | **0 ₽** | Electronic; needs a confirmed account / e-signature flow |
| **ФНС online** ("Государственная регистрация ИП", service.nalog.ru) | **0 ₽** electronically | Free if signed with an e-signature / via the app; 800 ₽ if it falls back to paper |
| **Bank** (Сбербанк, Т-Банк, Альфа, ВТБ, etc.) | **0 ₽** | Bank prepares docs + free e-signature and files for you; usually bundled with opening a расчётный счёт |
| **МФЦ** ("Мои документы") | **0 ₽** (if MFC files electronically) | Confirm the specific MFC transmits documents electronically |
| **Notary** | **0 ₽** for duty (notary fee applies) | Notary signs and transmits electronically |
| **Paper to ФНС / by mail** | **800 ₽** | Pay the duty and attach the receipt |

> The cheapest route is almost always **electronic** (Госуслуги / ФНС / bank): **0 ₽ state duty**.

### 3.3 Choosing the tax regime at (or after) registration

- **УСН election deadline consequence** — This is the single most consequential choice. The УСН election must be filed with the registration documents or within 30 calendar days of registration; otherwise the ИП sits on ОСНО until the next calendar year. ПСН requires a separate patent application (form 26.5-1) before the patent start date.  _(Skill body §3.3 intro)_

**Tax regime comparison at registration**

| Regime | Best for | Headline rate (2026 — verify) | Income limit (verify) | Reporting | Election deadline |
| --- | --- | --- | --- | --- | --- |
| **НПД** (самозанятый) | Solo, services / own goods, no staff, < 2.4 млн ₽ | 4% (individuals) / 6% (legal entities) | **2,400,000 ₽**/yr | None (auto via «Мой налог») | Register in «Мой налог» any time; an ИП may switch to НПД |
| **УСН «Доходы»** | Low-expense services, wants simplicity | **6%** of revenue (regions may cut to 1%) | High annual cap — **verify current value** | Annual declaration | With registration **or within 30 days** |
| **УСН «Доходы минус расходы»** | Real, documented costs | **15%** of profit (regions may cut to 5%) | Same УСН cap — **verify** | Annual declaration | With registration **or within 30 days** |
| **ПСН** (patent) | Specific eligible activities, predictable income | Cost of the patent (fixed, region/activity-based) | **20,000,000 ₽**/yr from 2026 (cut from 60 млн — verify) | Patent ledger (КУДиР для ПСН), no declaration | Patent application ≥ 10 working days before start |
| **ОСНО** (general) | Needs VAT, big clients, or fell out of other regimes | НДФЛ on profit + НДС (VAT) | None | Full — НДФЛ + НДС | Default if nothing else elected |

Notes for the agent (all **verify current value/procedure**):
- **2026 reform context:** the VAT-exemption threshold for УСН was reduced (the exemption limit dropped to roughly **20 млн ₽** of revenue for 2026, with further reductions planned for later years), and the **ПСН income limit fell to 20 млн ₽**. This makes "which regime" advice time-sensitive — flag it.
- **ИП on any regime except НПД pays fixed страховые взносы** for themselves (see ru-social-contributions). НПД carries no mandatory contributions.
- УСН and ПСН can be **combined** by one ИП (e.g. patent for one activity, УСН for the rest). Confirm the combination rules currently in force.
- **АУСН** (automated УСН) is an additional special regime in some regions — out of scope here; mention it exists and defer to a current source.

### 3.4 Opening a расчётный счёт (business bank account)

- **Расчётный счёт requirements and process** — - An ИП is **not legally required** to open a расчётный счёт, but in practice needs one to accept card/online payments, work with companies, pay taxes conveniently, and use acquiring. (A самозанятый generally does **not** need one — a personal card suffices.) - Opened at any Russian bank (Т-Банк, Сбербанк, Альфа, Точка, ВТБ, etc.), usually online: provide ИП registration data (ЕГРИП record), passport, ИНН. - The bank notifies ФНС of the account automatically. - Mixing personal and business money on one account is discouraged; a dedicated расчётный счёт keeps accounting clean and is expected by counterparties.  _(Skill body §3.4)_

## 4. ИП vs ООО — comparison

**ИП vs ООО comparison**

| Dimension | ИП (individual entrepreneur) | ООО (limited liability company) |
| --- | --- | --- |
| Legal nature | The individual themselves (физлицо со статусом ИП) | A separate legal person (юрлицо) |
| Register | **ЕГРИП** | **ЕГРЮЛ** |
| Liability | **Personal** — answers for business debts with own property | Limited to the company's assets / charter capital (with exceptions for subsidiary liability) |
| Charter capital | None | Minimum **10,000 ₽** (paid in money within 4 months of registration) |
| State duty (госпошлина) | 800 ₽ paper / **0 ₽** electronic | 4,000 ₽ paper / **0 ₽** electronic |
| Registration form | Р21001 | Р11001 + charter + founder's decision |
| Owners | One individual only | 1–50 participants (участники) |
| Profit withdrawal | Free — business money is the owner's money | Via salary or **dividends** (taxed; distribution rules apply) |
| Accounting | Simplified (no full бухучёт on most regимes) | Full accounting + balance sheet required |
| Tax regimes | НПД*, УСН, ПСН, ОСНО, АУСН | УСН, ОСНО, АУСН (no НПД, no ПСН) |
| Страховые взносы | Fixed "for self" (except on НПД) | For employees / director (min base ~1 МРОТ from 2026 — verify) |
| Closing | Simple — form Р26001, fast, cheap | Liquidation procedure — months, multi-step |

*НПД is available to an individual who is also registered as ИП, with НПД's own limits.

**When an ООО makes sense:**
- More than one owner / investors, or you need to bring in partners with shares.
- You want **limited liability** to ring-fence personal assets from business risk.
- Activities that are **closed to ИП** (e.g. selling strong alcohol at retail, certain licensed/regulated businesses, banking, insurance).
- Larger operations, employees, outside financing, or a plan to sell the business as a transferable asset.

For a solo freelance developer or service provider, **ИП (or самозанятый)** is almost always the right call; an ООО adds cost, bookkeeping, and exit friction for little benefit.

## 5. Worked examples (personas)

### Example A — Solo freelance developer, ~1.5 млн ₽/year

Anna writes code for individuals and small Russian companies, no employees, income about 1.5 млн ₽/year. **Recommendation:** register as **самозанятый (НПД)** via «Мой налог» — free, instant, no register entry, no страховые взносы, no reporting. Tax: 4% from individuals, 6% from companies. Revisit only if she approaches the **2.4 млн ₽** cap or wants to hire.

### Example B — Developer growing past 2.4 млн ₽, wants to hire one helper

Boris earns ~4 млн ₽/year and wants to bring on a contractor and work with larger clients who expect a расчётный счёт. НПД no longer fits (over cap, employees). **Recommendation:** register as **ИП**, file the **УСН «Доходы»** уведомление **with the application or within 30 days** (so he isn't stranded on ОСНО), pick narrow ОКВЭД codes for software development, file electronically (**0 ₽** duty), and open a расчётный счёт. Note he will owe fixed страховые взносы (see ru-social-contributions).

### Example C — Service business with heavy real costs

Galina runs a small studio with substantial documented expenses (subcontractors, equipment, rent). **Recommendation:** **ИП on УСН «Доходы минус расходы» (15%)**, because deductible costs make profit-based tax cheaper than 6% of gross. File the УСН election on time; keep expense documents (КУДиР). Compare against ПСН if her specific activity is patent-eligible and within the **20 млн ₽** ПСН limit.

### Example D — Two co-founders launching a product company

Dmitry and a partner want to split ownership, take outside investment later, and limit personal liability. **Recommendation:** form an **ООО** with **10,000 ₽** charter capital, file Р11001 + charter electronically (**0 ₽** duty), elect УСН within 30 days if eligible, and open a расчётный счёт. Accept the trade-off of full accounting and a longer closing process in exchange for limited liability and transferable shares.

## 6. Tier 2 notes, references, and checklist

### Tier 2 — escalate to a Russian accountant / lawyer when:

- The activity may be **licensed or regulated** (alcohol, finance, medicine, education, transport) — formation form and permissions matter.
- The user is a **foreign national / non-resident**, or registering from abroad — eligibility, ИНН, and e-signature mechanics differ.
- Choosing between **ИП and ООО** with investors, multiple owners, or asset protection at stake.
- The user is near a **regime threshold** (НПД 2.4 млн; ПСН 20 млн; УСН VAT exemption ~20 млн) where the 2026 reform changes the math.
- **Combining regimes** (УСН + ПСН) or planning a **mid-year switch**.
- Any **debt, dispute, or tax arrears** present at closing.

### Reference — key forms & registers

- **Р21001** — Application to register an ИП.  _(Skill body: Reference — key forms & registers)_
- **Р24001** — Change ИП data (e.g. add/remove ОКВЭД).  _(Skill body: Reference — key forms & registers)_
- **Р26001** — Application to close (deregister) an ИП.  _(Skill body: Reference — key forms & registers)_
- **Р11001** — Application to register an ООО.  _(Skill body: Reference — key forms & registers)_
- **26.2-1 (КНД 1150001)** — уведомление о переходе на УСН.  _(Skill body: Reference — key forms & registers)_
- **26.5-1** — Application for a patent (ПСН).  _(Skill body: Reference — key forms & registers)_
- **ЕГРИП** — Unified state register of individual entrepreneurs.  _(Skill body: Reference — key forms & registers)_
- **ЕГРЮЛ** — Unified state register of legal entities.  _(Skill body: Reference — key forms & registers)_
- **ОКВЭД 2** — Activity classifier for picking codes.  _(Skill body: Reference — key forms & registers)_

Services: nalog.gov.ru (ФНС), gosuslugi.ru (Госуслуги), npd.nalog.ru & lknpd.nalog.ru («Мой налог» / самозанятый).

### Deregistering / closing

- **Close a самозанятый (НПД)** — In «Мой налог» → Профиль → "Сняться с учёта НПД", choose a reason, submit. Free, immediate; status can be re-registered later. There is nothing to remove from ЕГРИП (a самозанятый was never in it). Settle any outstanding НПД tax first.  _(Skill body: Deregistering / closing)_
- **Close an ИП** — File form Р26001 to ФНС. State duty is 160 ₽ on paper, 0 ₽ electronically (verify current amount). Before/around closing: settle страховые взносы, file final declarations, pay outstanding tax, and (if any) dismiss employees and deregister as an employer. ФНС removes the ИП from ЕГРИП within ~5 working days. (Closing an ООО is a multi-month liquidation — out of scope here; escalate.)  _(Skill body: Deregistering / closing)_
- **ИП closing state duty (paper)** — 160 RUB  _(Skill body: 'State duty is 160 ₽ on paper, 0 ₽ electronically (verify current amount).')_

### Formation checklist (ИП)

- [ ] Confirm НПД isn't simpler/sufficient first.
- [ ] Pick main + additional **ОКВЭД 2** codes (narrow, accurate).
- [ ] Decide the tax regime; prepare the **УСН уведомление** if applicable.
- [ ] Prepare **Р21001**; have ИНН + passport ready.
- [ ] File **electronically** (Госуслуги / ФНС / bank) → **0 ₽ duty**.
- [ ] Receive **Лист записи ЕГРИП** (within 3 working days).
- [ ] File УСН election **within 30 days** if not filed with the application.
- [ ] Open a **расчётный счёт** if needed.
- [ ] Note ongoing duties: fixed **страховые взносы**, regime reporting.

## PROHIBITIONS

- **Agent prohibitions** — The agent must not: - File, sign, or submit any registration, election, or closing document on the user's behalf, or transmit data to ФНС / Госуслуги / a bank for them. The agent explains; the user acts. - Choose a tax regime as a final decision without flagging that rates, limits, and the 2026 reform changes must be verified on nalog.gov.ru and confirmed with a qualified Russian accountant. - Invent or guess ОКВЭД codes, ИНН/ОГРНИП numbers, form field values, fees, or deadlines — verify against the official classifier and current ФНС sources. - Advise on licensed / regulated activities, foreign-national registration, multi-owner structuring, or anything with debts/disputes without escalating to a qualified professional. - Present this skill's figures (2.4 млн ₽ cap, 800 ₽ / 4,000 ₽ / 160 ₽ duties, 10,000 ₽ charter capital, 20 млн ₽ ПСН / VAT limits, 30-day window, 3-day registration) as guaranteed-current — they are point-in-time and must be re-checked before reliance. - Provide legal opinions on liability, asset protection, or dispute exposure — defer to a lawyer.  _(Skill body: PROHIBITIONS)_

## Disclaimer

This skill is research-verified against ФНС (nalog.gov.ru), Госуслуги (gosuslugi.ru), and reputable Russian sources, current to May 2026 / tax year 2026. It is pending sign-off by a qualified Russian accountant and is provided for informational purposes only. It is not legal, tax, or accounting advice and does not create a professional relationship. Russian registration procedures, state duties, tax rates, regime thresholds, and forms change frequently — the 2026 tax reform in particular altered УСН/ПСН VAT and income limits. Always verify the current value/procedure on the official ФНС and Госуслуги services and have a credentialed Russian accountant or lawyer review any formation, regime-election, or closing decision before acting. Part of the open-source tax skills project at openaccountants.com.

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
