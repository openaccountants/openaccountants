---
name: eg-formation
description: Use this skill whenever asked about how to register, form, or set up a business in Egypt as a self-employed person, freelancer, professional, sole proprietor, or small company. Trigger on phrases like "register a business Egypt", "tax card Egypt", "how to start a business Egypt", "sole proprietor Egypt", "freelance registration Egypt", "GAFI LLC Egypt", "commercial register Egypt", "open a tax file Egypt", "register with the ETA", "البطاقة الضريبية", "السجل التجاري", "تسجيل منشأة فردية", "فتح ملف ضريبي", "تأسيس شركة ذات مسؤولية محدودة", "نقابة مهنية", "التأمينات الاجتماعية للعمل الحر". Covers obtaining a tax card and tax file with the Egyptian Tax Authority (ETA), the commercial register, professional syndicate (نقابة) membership, choosing the simplified vs general regime at registration, VAT and e-invoicing registration, social insurance registration, and forming an LLC via GAFI. AI replies in the user's language (English or Arabic).
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Formation

## Egypt — Business Formation & Registration for the Self-Employed

This skill walks a self-employed person in Egypt through **getting legally set up**: obtaining a **tax card** (البطاقة الضريبية) and opening a **tax file** (ملف ضريبي) with the **Egyptian Tax Authority — ETA** (مصلحة الضرائب المصرية), entering the **commercial register** (السجل التجاري) where required, joining a **professional syndicate** (نقابة) for regulated professions, choosing a tax regime at the point of registration, registering for **VAT** and **e-invoicing**, registering for **social insurance** (التأمينات الاجتماعية), and — if it makes sense — forming a **limited liability company** (شركة ذات مسؤولية محدودة) through **GAFI** (الهيئة العامة للاستثمار).

> Respond in the user's language. If the user writes in Arabic, reply in Arabic and keep the native legal terms (e.g. البطاقة الضريبية = tax card, السجل التجاري = commercial register, منشأة فردية = sole proprietorship / individual establishment, نقابة = professional syndicate, الهيئة العامة للاستثمار = GAFI).

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Egypt (EG) |
| What this covers | Registering as a self-employed individual / sole proprietor and (briefly) forming an LLC |
| Currency | EGP (Egyptian Pound) |
| Authorities | **ETA** (Egyptian Tax Authority — tax card, tax file, VAT, e-invoicing); **GAFI** (companies / LLCs); **Commercial Register** (السجل التجاري / GAFI); **NOSI** (National Organisation for Social Insurance — التأمينات الاجتماعية); relevant **professional syndicate** (نقابة) |
| Tax card | البطاقة الضريبية — mandatory ETA tax identification document |
| Income tax law (general) | Income Tax Law **No. 91 of 2005** (as amended) |
| Simplified regime | **Law No. 6 of 2025** turnover-based system for turnover ≤ **EGP 20,000,000** (see `eg-sme-tax`) |
| VAT law | VAT Law **No. 67 of 2016** (as amended) — standard rate **14%** |
| VAT registration threshold | Historically **EGP 500,000** turnover; **lowered to EGP 250,000** effective **1 Jan 2026** per **Resolution No. 281 of 2025** — **verify current value with ETA** |
| Social insurance | Law **No. 148 of 2019** — self-employed contribute (commonly cited) **~21%** of a chosen reference wage — **verify current rate/bands** |
| Quality tier | **Research-verified — pending sign-off by an Egyptian accountant** |
| Version | 1.0 |

### Conservative defaults

- **Default to registering, not waiting.** Operating without a tax card / tax file is non-compliant. If income is at or near any threshold, assume registration is required and confirm with ETA.
- **Default to the lower VAT threshold.** Treat **EGP 250,000** (effective 2026) as the trigger to register for VAT and e-invoicing, and flag "verify current value" — do not assume the old EGP 500,000 figure still applies.
- **Default to "syndicate first" for regulated professions.** Lawyers, doctors, engineers, accountants and similar professions generally **cannot practise lawfully** without syndicate (نقابة) membership — treat it as a prerequisite, not optional.
- **Default to sole proprietorship (منشأة فردية) for a solo freelancer** unless there is a specific reason for an LLC (see Section 5). Do not recommend an LLC by default.
- **Never present a fee, threshold, rate, or procedure as final** without an Egyptian accountant's sign-off and a same-day check against ETA / GAFI portals. Fees and thresholds change frequently by decree.

## 2. Sole-proprietor registration step-by-step

A self-employed individual in Egypt typically operates as a **منشأة فردية** (individual establishment / sole proprietorship) or simply as a registered individual taxpayer / professional. There is **no separate legal entity** — the individual and the business are the same person, with unlimited personal liability.

### Step 1 — National ID and eligibility

- **Eligibility requirements** — Egyptian nationals: a valid national ID (الرقم القومي), age 21+ and legal capacity. The national ID number is the backbone of the tax and registration records. Foreign nationals: valid passport, residence permit, and sometimes activity-specific approvals — escalate; foreigners are out of the simple default path. Verify current procedure.

### Step 2 — Proof of place of activity

- **Proof of place of activity** — A lease/rental contract (عقد إيجار) or ownership document for the business address. Many activities require a registered address even for home-based work. Verify whether the specific activity permits a residential address.

### Step 3 — Open a tax file and obtain the tax card (البطاقة الضريبية)

- **Tax file and tax card procedure** — Register with the ETA to open a tax file (ملف ضريبي) at the competent tax office (المأمورية) for the business address, or via the ETA e-services portal (eservice.incometax.gov.eg / eta.gov.eg). Verify which steps can be done fully online vs in person. Typical documents: national ID copy, proof of address (lease), and a description of the activity. Verify the current document checklist with the local tax office. ETA issues the tax card (البطاقة الضريبية) — the tax identification document carrying the Tax ID Number (TIN). This is mandatory and is required to invoice clients, contract with companies/government, and register for VAT.

### Step 4 — Commercial register (السجل التجاري) — for commercial/industrial activity

- **Commercial register requirement** — The commercial register is required for commercial and industrial activities (e.g. trading, retail, manufacturing, most goods-based businesses). Pure liberal/professional activities (المهن الحرة) — e.g. a lawyer, doctor, engineer, accountant practising their profession — are generally registered via their syndicate and may not require a commercial register entry. Verify per activity — the line between "commercial" and "professional" determines which register applies. Commercial register entry for a sole proprietorship is administered via the commercial registry office / GAFI. Fees reported as nominal (e.g. an entry fee in the low tens of EGP, a small annual subscription scaled to declared capital, a name-reservation fee, and a certificate fee) — all amounts must be verified, as they change and vary by office.

### Step 5 — Professional syndicate (نقابة) — for regulated professions

- **Syndicate membership requirements by profession** — For regulated professions, syndicate membership is a legal precondition to practise: Lawyers → Bar Association (نقابة المحامين). Doctors / dentists / pharmacists → respective medical syndicates. Engineers → Engineers Syndicate (نقابة المهندسين) — regulated under Law No. 66 of 1974. Accountants / auditors → Syndicate of Commercial Professions / registration with the Ministry of Finance accountants & auditors register and the relevant society (e.g. ESAA). Verify the exact body and registration path for public accounting practice. Membership usually requires the relevant degree, fees, and sometimes training. Verify current requirements and fees with the specific syndicate.  _(Law No. 66 of 1974 (Engineers Syndicate))_

### Step 6 — Choose the tax regime (see Section 3) and register for VAT / e-invoicing / social insurance (see Section 4)

- **Order of operations** — At or around the time of opening the tax file, decide between the simplified turnover-based regime (Law No. 6 of 2025) and the general system, then complete VAT, e-invoicing, and social insurance registrations as applicable. > **Order of operations (typical):** national ID → proof of address → ETA tax file + tax card → (commercial register **or** syndicate, per activity) → regime choice → VAT / e-invoicing if over threshold → social insurance. **Verify the exact sequence**, as some offices require the commercial register or syndicate card before issuing the tax card for certain activities.

## 3. Choosing the regime at registration (simplified vs general)

At registration the taxpayer is, in effect, choosing how their income tax will be computed. The integrated simplified regime under Law No. 6 of 2025 taxes a flat percentage of turnover (رقم الأعمال), while the general system (Income Tax Law No. 91 of 2005) taxes net profit under progressive brackets.

> Full simplified-regime mechanics, band rates, eligibility, exclusions, and the 5-year lock-in live in **`eg-sme-tax`**. Use this section only for the **registration-time decision**.

### Decision table

**Decision table — Simplified vs General**

| Factor | Lean **Simplified** (Law 6/2025) | Lean **General** (Law 91/2005) |
| --- | --- | --- |
| Annual turnover | ≤ **EGP 20,000,000** (eligibility cap) | Any; required if over the cap |
| Profit margin | **High margin** — turnover tax (0.4%–1.5% of turnover) beats profit tax | **Thin margin / loss-making** — % of turnover can exceed tax on small/zero profit |
| Bookkeeping appetite | Wants **simpler** filing & quarterly VAT | Can maintain **full accounts** and substantiate expenses |
| Deductible expenses | Few real, documentable expenses | **Large documentable expenses** that lower net profit |
| Stability | Comfortable with a **5-year commitment** | Wants flexibility year to year |
| Activity status | Eligible activity (not excluded/regulated-out) | Excluded from the simplified regime |

### Rule of thumb

**Rule of thumb:** a low-cost solo freelancer with a high margin usually pays **less under the simplified turnover regime**; a low-margin reseller or a business with heavy documentable costs may pay **less under the general system**. **Model both** and get accountant sign-off before electing — the simplified regime is a **5-year lock-in** and enrolment is **not automatic** (a request to ETA must be submitted and accepted). See `eg-sme-tax`.

## 4. VAT, e-invoicing and social insurance registration

These are **separate** from income tax and from the tax card — registering for a tax file does **not** by itself register a person for VAT, e-invoicing, or social insurance.

### 4.1 VAT registration (VAT Law No. 67 of 2016)

- **Standard VAT rate** — 14% percent (special/table rates apply to some goods/services — out of scope here)  _(VAT Law No. 67 of 2016)_
- **VAT registration threshold** — Historically EGP 500,000 of annual taxable turnover; under Resolution No. 281 of 2025, lowered to EGP 250,000 effective 1 January 2026, with a registration deadline reported as 31 March 2026 for those who exceeded EGP 250,000 in 2025. Verify the current value and deadline with ETA before relying on it. EGP (⚠ verify current value and deadline with ETA)  _(Resolution No. 281 of 2025)_
- **VAT threshold measurement and registration process** — The threshold is measured on gross revenue (turnover), not profit. Register via the ETA portal once turnover crosses (or is expected to cross) the threshold. Voluntary registration below the threshold may be possible — verify. Within the simplified regime, VAT returns are filed quarterly (vs monthly in the general system). See `eg-sme-tax`.

### 4.2 E-invoicing / e-receipt registration (ETA portal)

- **E-invoicing/e-receipt system and obligations** — Egypt operates a mandatory electronic invoicing (الفاتورة الإلكترونية) and electronic receipt (الإيصال الإلكتروني) system on the ETA platform. Resolution No. 281 of 2025 is reported to expand e-invoicing/e-receipt obligations to smaller businesses in step with the lowered EGP 250,000 threshold, with B2C e-receipt obligations expanding through 2025–2026. Verify the exact phase-in dates and who is in scope. Registration requires an ETA portal account and (typically) a digital signature / e-seal and onboarding of an invoicing solution. Verify the current technical onboarding steps. Penalties for non-registration/non-compliance are significant — sources cite fixed fines plus daily penalties and, ultimately, loss of the ability to issue valid invoices. Verify current penalty figures with ETA.  _(Resolution No. 281 of 2025)_

### 4.3 Social insurance registration (التأمينات الاجتماعية — Law No. 148 of 2019)

- **Social insurance registration for self-employed** — Law No. 148 of 2019 extended social insurance to the self-employed (أصحاب الأعمال / المهن الحرة), sole-proprietor owners, freelancers of specified trades, craftsmen, merchants, and others. Register with the National Organisation for Social Insurance (NOSI / الهيئة القومية للتأمينات الاجتماعية). Self-employed contributions are commonly cited at ~21% of a chosen contribution (reference) wage, selected from a statutory reference table, between a minimum and maximum contribution wage that is uplifted annually. Verify the current rate, the reference-wage table, and the min/max caps — these change each January. This is separate from income tax and VAT and is not covered by the simplified turnover tax. See `eg-social-insurance` for the detailed computation.  _(Law No. 148 of 2019)_

## 5. Sole proprietor vs LLC comparison

Most solo freelancers should default to a sole proprietorship (منشأة فردية). An LLC (شركة ذات مسؤولية محدودة) formed through GAFI adds cost and compliance but provides limited liability and a separate legal personality.

**Sole proprietor vs LLC comparison table**

| Factor | Sole proprietor (منشأة فردية) | LLC (ش.ذ.م.م) via GAFI |
| --- | --- | --- |
| Legal personality | None — same as the individual | Separate legal entity |
| Liability | **Unlimited personal** liability | **Limited** to capital contributed |
| Owners | One individual | One+ (single-member LLC is possible — **verify**) |
| Set-up authority | ETA + commercial register / syndicate | **GAFI** (الهيئة العامة للاستثمار) |
| Minimum capital | N/A | **No statutory minimum** reported (verify) |
| Set-up cost | Low (nominal register fees) | Higher — GAFI incorporation fees, notarisation, bank account, lawyer/accountant |
| Compliance | Lighter; can use simplified regime | Heavier; audited accounts, corporate filings |
| Income tax | Personal income tax (general) or simplified turnover regime | Corporate income tax (the SME turnover regime may apply if eligible — **verify**) |
| Best for | Solo freelancers, professionals, small traders | Businesses wanting liability protection, partners/investors, larger contracts, scaling |

### When an LLC makes sense

- You want **limited liability** (e.g. higher-risk contracts, debt exposure).
- You have or plan **partners or outside investors**.
- **Clients/tenders require** a company rather than an individual.
- You are **scaling** beyond a one-person practice.

### Forming an LLC via GAFI (overview only)

- **LLC formation steps via GAFI** — 1. Create an account on the GAFI e-portal and reserve a company name. 2. Submit the incorporation application with the articles of association, founders' IDs/passports, and required approvals; pay incorporation fees. 3. Obtain the commercial register entry and the company tax card / tax file from ETA. 4. Register for VAT/e-invoicing (if applicable) and social insurance for the company and any employees. > Incorporation fees are reported in the **low hundreds of USD** range depending on entity type, plus professional fees. **Verify all current GAFI fees, capital rules, and the document checklist** — these change. Forming an LLC should be done with a credentialed Egyptian lawyer/accountant.

## 6. Worked examples

> All figures illustrative. Verify current thresholds, fees, rates, and procedures before relying on any output.

### Example 1 — Freelance graphic designer, EGP 180,000/year, solo

- **Path:** Register an individual tax file + obtain the **tax card** at ETA. Likely **no commercial register** (a service/professional activity) — **verify**. No syndicate (unregulated profession).
- **VAT:** Turnover **below** the EGP 250,000 (2026) threshold → **no mandatory VAT registration** yet. Watch the threshold; e-invoicing may still be encouraged — **verify scope**.
- **Income tax:** Eligible for the **simplified turnover regime**; high margin → likely cheapest. Compare with general system. See `eg-sme-tax`.
- **Social insurance:** Should register with **NOSI** as self-employed at a chosen reference wage — **verify rate/bands**.

### Example 2 — Software developer/contractor, EGP 900,000/year, one big client

- **Path:** Tax file + **tax card**. Service activity — check commercial register vs professional treatment. No syndicate.
- **VAT:** **Above** EGP 250,000 → **must register for VAT (14%)** and for **e-invoicing** on the ETA portal; verify the 31 Mar 2026 deadline if 2025 turnover exceeded the threshold.
- **Income tax:** Eligible for simplified regime (≤ EGP 20m). **Flag client concentration** — single-client dependence can raise exclusion/abuse questions in the simplified regime; escalate to `eg-sme-tax`.
- **Social insurance:** Register with NOSI; choose reference wage.

### Example 3 — Licensed engineer starting a consultancy

- **Path:** **Engineers Syndicate (نقابة المهندسين) membership is a precondition to practise** (Law No. 66 of 1974). Then ETA tax file + **tax card**. Professional activity → likely registered via syndicate rather than the commercial register — **verify**.
- **VAT / e-invoicing / social insurance:** as per thresholds in Section 4.
- **Regime:** Compare simplified vs general; engineering services are typically high margin. Confirm the activity is **not excluded** from the simplified regime.

### Example 4 — Two founders launching a product company, expecting investment

- **Path:** Form an **LLC (ش.ذ.م.م) via GAFI** — limited liability, room for partners/investors, credibility for contracts. Reserve name → articles of association → incorporation → company tax card + commercial register → VAT / e-invoicing / social insurance.
- **Why not sole proprietorship:** multiple owners and outside capital make a sole proprietorship unsuitable. Use a credentialed lawyer/accountant for incorporation.

## 7. Tier 2, Reference, and checklist

### Tier 2 — escalate to a credentialed Egyptian accountant/lawyer when

- The activity may sit on the **commercial vs professional** line (which register/syndicate applies).
- A **regulated profession** is involved (syndicate licensing nuances).
- The taxpayer is a **foreign national** or has cross-border / free-zone / SEZ considerations.
- Turnover is near the **VAT threshold** or the **EGP 20m** simplified-regime cap.
- The taxpayer is **choosing between sole proprietorship and an LLC**, or forming an LLC at all.
- There is **single-client concentration** or business **fragmentation** (simplified-regime exclusion risk — see `eg-sme-tax`).
- **Prior-year non-registration**, back taxes, or penalty exposure exists.

### Reference (verify each before relying on it)

- **Income Tax Law No. 91 of 2005** (as amended) — general system.
- **Law No. 6 of 2025** — integrated simplified turnover-based regime (≤ EGP 20m); see `eg-sme-tax`.
- **Law No. 152 of 2020** — MSME Development Law (size definitions/incentives).
- **VAT Law No. 67 of 2016** (as amended) — 14% rate; registration threshold (historically EGP 500,000; **EGP 250,000 from 1 Jan 2026 per Resolution No. 281 of 2025 — verify**).
- **Resolution No. 281 of 2025** — lowered VAT/e-invoicing threshold and expanded e-receipt obligations — **verify scope, dates, and penalties**.
- **Law No. 148 of 2019** — social insurance (incl. self-employed); see `eg-social-insurance`.
- **GAFI** (gafi.gov.eg) — LLC incorporation, name reservation, fees, document lists.
- **ETA** (eta.gov.eg; eservice.incometax.gov.eg) — tax file, tax card, VAT, e-invoicing portals.
- Professional commentary used for this skill: EY, WTS, Andersen Egypt, Deel, and Egyptian law-firm alerts (2025–2026).

### Registration checklist (verify each item before filing)

- [ ] National ID (or passport + residence permit for foreigners).
- [ ] Proof of business address (lease/ownership) — confirm activity allows it.
- [ ] **ETA tax file opened** + **tax card (البطاقة الضريبية)** issued.
- [ ] **Commercial register** entry (commercial/industrial activity) **or** confirm professional/syndicate path applies.
- [ ] **Syndicate (نقابة) membership** secured (regulated professions).
- [ ] **Regime chosen** — simplified (Law 6/2025) vs general — modelled and signed off.
- [ ] **VAT registration** done if over the (verified) threshold.
- [ ] **E-invoicing / e-receipt** onboarding done if in scope.
- [ ] **Social insurance (NOSI)** registration done; reference wage chosen.
- [ ] **(LLC only)** GAFI incorporation, articles of association, name reservation, company tax card, bank account.

### Deregistration / closing down

- **Deregistration process** — To stop activity, notify the ETA and close the tax file, settle any outstanding income tax / VAT and file final returns, cancel the commercial register entry and/or syndicate membership, and stop social insurance contributions with NOSI. For an LLC, follow the GAFI liquidation/strike-off procedure. Deregistering for VAT requires meeting ETA conditions. Verify the current step-by-step deregistration procedure and any clearance requirements — closing badly leaves dormant liabilities and penalties.

## PROHIBITIONS

- **Do NOT** tell anyone they can operate without a **tax card / tax file** — that is non-compliant.
- **Do NOT** state the **VAT threshold** as EGP 500,000 without flagging the **EGP 250,000 (from 1 Jan 2026)** change and "verify current value" — do not present either figure as settled without an ETA check.
- **Do NOT** quote any **fee, threshold, rate, penalty, or deadline** (commercial register fees, GAFI incorporation fees, social-insurance rate/bands, e-invoicing penalties) as final without same-day verification — flag with "verify current value/procedure".
- **Do NOT** tell a member of a **regulated profession** they can practise without the relevant **syndicate (نقابة)** membership.
- **Do NOT** assume an activity is "professional" vs "commercial" (and thus which register applies) — verify per activity.
- **Do NOT** recommend an **LLC by default**; recommend a sole proprietorship for a solo freelancer unless there is a clear reason (Section 5).
- **Do NOT** advise **splitting/fragmenting** a business to stay under a threshold (abuse risk).
- **Do NOT** treat **foreign-national** registration as the simple default path — escalate.
- **Do NOT** present any registration plan as final without **sign-off from a qualified Egyptian accountant/lawyer**.

## Disclaimer

This skill is **research-verified** against the Egyptian Tax Authority (eta.gov.eg), GAFI (gafi.gov.eg), and reputable Egyptian and international tax/legal publications (EY, WTS, Andersen Egypt, Deel, and Egyptian law-firm alerts), current to **May 2026**. It is **not** a substitute for professional advice and has **not yet been signed off by a qualified Egyptian accountant**. Egyptian registration procedures, fees, the VAT rate/threshold (notably the EGP 500,000 → EGP 250,000 change for 2026), e-invoicing scope and penalties, social-insurance rates/bands, and GAFI rules are subject to change by decree. Always verify current figures and procedures with ETA, GAFI, the relevant commercial registry, the relevant syndicate (نقابة), and NOSI, and obtain sign-off from a credentialed Egyptian tax/legal professional before registering, filing, or relying on any output. Provided by **openaccountants.com** as open-source guidance, without warranty.

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
