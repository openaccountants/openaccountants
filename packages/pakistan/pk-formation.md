---
name: pk-formation
description: "Use this skill whenever asked about forming, incorporating, or registering a business in Pakistan. Trigger on phrases like \"Pakistan company formation\", \"SECP registration\", \"Pvt Ltd Pakistan\", \"AOP Pakistan\", \"PSEB IT registration\", \"Pakistan sole proprietor\", \"SMC-Pvt Pakistan\", \"incorporate Pakistan\", \"register company Pakistan\", \"FBR NTN\", \"STRN\", \"Companies Act 2017\", or any question about choosing or registering a Pakistani entity. Covers entity comparison (Sole Proprietorship, AOP / Partnership, Single Member Company SMC-Pvt, Private Limited Pvt Ltd, Public Limited PLC, NPO), SECP eServices portal registration steps, FBR NTN and STRN tax registration, sector-specific licensing (SBP for banking and fintech, PTA for telecom, NEPRA for power, SECP for capital markets), the **critical PSEB (Pakistan Software Export Board) registration** that unlocks the 0.25% / 1% concessional final tax on IT and IT-enabled services exports, and tax treatment by entity type. Out of scope: immigration / work visa / POC / NICOP sponsorship, bank account opening procedures (high-level only), full corporate governance and shareholders' agreement drafting, deep sector-specific regulatory licensing beyond signposting, and listing on the PSX. ALWAYS read this skill before advising on Pakistani entity formation."
version: 1.0
jurisdiction: PK
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ibrar Ali
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PK Formation

## Pakistan — Business Formation & Entity Selection — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ibrar Ali** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### pk-formation

- **Company registrar** — SECP (ezfile.secp.gov.pk)  _(Companies Act 2017)_
- **Formation time** — Sole-prop NTN 1 days; SMC-Pvt/Pvt Ltd 4–10 days; PLC 3–6 weeks; NPO 6–12 weeks  _(SECP eServices FBR IRIS Portal)_
- **Name reservation validity** — 60 days for Companies; 30 days for Limited Liability Partnerships (LLPs).  _(SECP)_
- **Sole proprietorship** — 1 owner; unlimited liability; no minimum capital  _(ITO 2001 (NTN-based))_
- **AOP / partnership** — 2–20 partners; unlimited joint & several liability  _(Partnership Act 1932 §4)_
- **SMC-Pvt** — 1 shareholder + 1 nominee; commonly PKR 100,000 capital (no statutory floor)  _(Companies Act 2017)_
- **Private Limited (Pvt Ltd)** — Minimum 2 members & 2 directors; max 50 members; commonly PKR 100,000 (no statutory floor)  _(Companies Act 2017)_
- **Public Limited (PLC)** — Min 3 members & 3 directors (7 if listed); no statutory minimum paid-up capital for unlisted  _(Companies Act 2017)_
- **Section 42 NPO** — Minimum 3 members & 3 Trustees; minimum start-up donation of PKR 200,000  _(Companies Act 2017 §42)_
- **Society** — Minimum 7 members  _(Societies Registration Act 1860 §1)_
- **Trust** — Minimum 2 trustees  _(Trusts Act 1882)_
- **PSEB-registered export final tax** — 0.25% of qualifying export remittances  _(ITO 2001 §154A / SRO 1359(I)/2022)_
- **Non-PSEB export rate** — 1%  _(ITO 2001 §154A)_
- **Reduced dividend tax (PSEB IT profits)** — 15% (Standard rate)  _(Finance Act (verify))_
- **PSEB registration** — Via pseb.org.pk; certificate ~2–4 weeks; annual renewal  _(PSEB)_
- **STZA zone enterprises** — 10-year tax holiday AND exemption from minimum tax, WHT, & custom duties  _(Special Technology Zones Authority)_
- **NTN** — Via FBR IRIS (CNIC functions as NTN for individuals)  _(FBR)_
- **STRN** — FBR for goods; provincial authority (SRB/PRA/KPRA/BRA) for services  _(STA 1990 / Provincial Acts)_
- **EOBI** — Mandatory employer registration at ≥ 5 employees  _(EOBI Act 1976)_
- **Beneficial Ownership Register** — Mandatory disclosure of ultimate beneficial owners (≥ 25% ownership or effective control).  _(SECP Beneficial Ownership Regulations 2020)_

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Islamic Republic of Pakistan |
| Currency | PKR (Pakistani Rupee) |
| Company registrar | Securities and Exchange Commission of Pakistan (SECP) |
| Tax authority (federal) | Federal Board of Revenue (FBR) — income tax, sales tax on goods, customs, federal excise |
| Tax authority (provincial sales tax on services) | PRA (Punjab), SRB (Sindh), KPRA (Khyber Pakhtunkhwa), BRA (Balochistan), ICT (Islamabad) administered by FBR |
| Key legislation | Companies Act 2017; Limited Liability Partnership Act 2017; Partnership Act 1932; Income Tax Ordinance 2001; Sales Tax Act 1990; Societies Registration Act 1860; Trusts Act 1882 |
| Registration portal | SECP eServices (ezfile.secp.gov.pk) |
| Typical formation time | 1 working day for sole proprietorship NTN; 4–10 working days for SMC-Pvt / Pvt Ltd via eServices; 3–6 weeks for PLC; 6–12 weeks for NPO / Section 42 Company |
| Corporate tax rate (CIT) | 29% for companies generally; 20% for small companies (turnover ≤ Rs 250M, paid-up ≤ Rs 50M, employees ≤ 250, no associated undertakings) under Income Tax Ordinance 2001 |
| Super tax | Up to 10% on high-income persons and certain sectors under section 4C ITO 2001 (graduated bands by income) |
| GST / Sales tax rate | 18% federal sales tax on goods (standard rate, may change in Finance Act); 13–16% provincial sales tax on services depending on province |
| PSEB concessional tax | **0.25% final tax on IT / ITeS export remittances for PSEB-registered exporters; 1% in some cases** — verify against current Finance Act and SRO; flagged for review at each Federal Budget |
| Skill version | 1.0 |

## Section 2 — Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Proprietorship | AOP (Partnership) | SMC-Pvt | Private Ltd (Pvt Ltd) | Public Ltd (PLC) | NPO (Section 42 / Trust / Society) |
| --- | --- | --- | --- | --- | --- | --- |
| Legal personality | No (owner = business) | Limited (firm name; separate tax entity) | Yes | Yes | Yes | Yes (non-profit) |
| Liability | Unlimited personal | Unlimited joint and several (general partnership) | Limited to share capital | Limited to share capital | Limited to share capital | Trustees / directors limited for proper acts |
| Min. founders / members | 1 sole proprietor | 2 partners (max 20 under Partnership Act 1932) | 1 shareholder + 1 nominee | 2 members and 2 directors | 3 members and 3 directors (7 for listed) | 3+ trustees / members |
| Max. members | n/a | 20 (general partnership); LLP unlimited | 1 (by definition) | 50 (excluding employees / former employees holding shares) | Unlimited | Unlimited |
| Foreign ownership | Practically restricted (resident NTN holder) | Foreign partners permitted but rare; tax filing complexities | 100% permitted (subject to SBP / BOI permissions) | 100% permitted | 100% permitted | Subject to objects and security vetting |
| Min. paid-up share capital | None | None (capital agreed in partnership deed) | Flexible under Companies Act 2017 (commonly Rs 100,000); no statutory floor for ordinary cases | Flexible (commonly Rs 100,000); sectoral floors override | No statutory minimum paid-up capital for unlisted PLCs (sectoral floors much higher for listed) | PKR 200,000 minimum start-up donation for Section 42 |
| Tax treatment | Personal income tax slabs (individual) | AOP taxed as separate entity at AOP slabs / corporate rate depending on character; share to partners exempt to avoid double tax | CIT 29% (or 20% small company) | CIT 29% (or 20% small company) | CIT 29% (typically large) | Tax-exempt for income applied to objects (clause 58 / 66 of Second Schedule); trading income taxable |
| Annual filing with SECP | None (FBR only) | None (Registrar of Firms only) | Form A annual return + audited accounts (audit threshold-based) | Form A annual return + audited accounts (audit threshold-based) | Form A + audited accounts + half-yearly accounts if listed | Annual return + audited accounts |
| Suffix on name | none | "& Co", "& Partners" (no Ltd / Pvt) | "(SMC-Private) Limited" or "(SMC-Pvt) Ltd" | "(Private) Limited" or "(Pvt) Ltd" | "Limited" or "Ltd" | "(Guarantee) Limited" for s.42; "Foundation", "Trust", "Society" for others |
| Admin burden | Low | Low–Medium | Medium | Medium | High | Medium–High |

**Recommended defaults:**

- Solo Pakistani-resident founder, micro turnover, domestic clients, low-risk activity, comfortable with unlimited liability: **Sole Proprietorship (NTN-based)**.
- Solo founder selling **IT / IT-enabled services exports** wanting limited liability + the **PSEB 0.25% final-tax regime**: **SMC-Pvt with PSEB registration**.
- 2+ founders wanting limited liability and access to the **20% small-company CIT band**: **Private Limited (Pvt Ltd)**.
- Professional services partnership (law, accounting, consulting) where partners want simplicity and provincial bar / ICAP rules permit: **AOP (Partnership)** registered with the Registrar of Firms.
- Plans to raise public capital, list on the **Pakistan Stock Exchange (PSX)**, or undertake regulated banking / insurance / NBFC activity: **Public Limited Company (PLC)**.
- Non-profit / NGO / religious / charitable / research: **Section 42 Company (Companies Act 2017)**, **Trust (Trusts Act 1882)**, or **Society (Societies Registration Act 1860)**.

## Section 3 — Required Inputs and Refusal Catalogue

### Required intake before recommending an entity

1. Nationality, CNIC / NICOP / passport, and tax residence of each founder.
2. Number of founders / promoters and intended directorships.
3. Intended business activity (objects) and FBR business code / principal activity.
4. Expected annual turnover and paid-up capital (drives small-company CIT classification and audit thresholds).
5. Whether any foreign shareholder or director is involved (triggers SBP / BOI permissions and possibly work visa).
6. **Whether the business will earn IT / IT-enabled services export revenue** (drives PSEB registration recommendation — critical).
7. Capital available for paid-up share capital and any sectoral minimum.
8. Whether the business will hire employees (EOBI, social security, withholding tax on salary).
9. Province of principal place of business (drives provincial sales tax on services).
10. Whether the business handles personal data or operates in a regulated sector (banking, telecom, power, capital markets, pharma, food).

### Refusal catalogue

- **R-PK-F1 — Benami / nominee structures** — Using a Pakistani nominee director or shareholder to disguise foreign control where prohibited, or to disguise true beneficial ownership, contravenes the Benami Transactions (Prohibition) Act 2017 and SECP Beneficial Ownership Regulations 2020. The skill will not draft or advise on benami arrangements. Escalate to a Pakistani legal practitioner.  _(Benami Transactions (Prohibition) Act 2017; SECP Beneficial Ownership Regulations 2020)_
- **R-PK-F2 — Sectors closed or restricted to foreign investment** — Sectors on the Negative List under the Investment Policy 2013 (as amended) — including arms and ammunition, high explosives, radioactive substances, security printing and currency, and consumable alcohol — are closed to foreign investment. Agriculture, services, infrastructure, and social sectors have varying restrictions. The skill flags requirements but does not handle BOI / SBP approvals for restricted sectors.  _(Investment Policy 2013 (as amended))_
- **R-PK-F3 — Work visa, POC, NICOP, and expatriate matters** — Work visas, Pakistan Origin Cards (POC), National Identity Cards for Overseas Pakistanis (NICOP), and expatriate employment are processed by the Ministry of Interior, NADRA, and the Board of Investment. The skill flags requirements but does not handle immigration filings; engage an immigration consultant.
- **R-PK-F4 — Bank account opening for foreigners or non-resident directors** — Pakistani banks require directors to attend in person or appoint a properly notarised attorney for KYC under SBP's AML / CFT Regulations and CDD requirements. Special Convertible Rupee Accounts (SCRA) for foreign portfolio investment have separate SBP rules. The skill flags the requirement but does not guarantee any specific bank's onboarding.  _(SBP AML/CFT Regulations)_
- **R-PK-F5 — Regulated sectors: banking, insurance, NBFCs, capital markets, fintech, telecom, power, pharma** — These require sector licences (SBP for banking and microfinance; SECP for NBFCs, insurance, asset management, brokers; PTA for telecom and ISPs; NEPRA for power generation / transmission / distribution; DRAP for pharma; PEMRA for broadcasting) in addition to SECP incorporation. Capital floors are much higher than the Companies Act minimums. Formation alone is insufficient — the skill refuses to provide a green-light recommendation without mapping the sectoral licence.
- **R-PK-F6 — PSEB registration without genuine IT/ITeS export substance** — Claiming the 0.25% / 1% final tax on IT or IT-enabled services exports under PSEB registration when the underlying activity is not genuine IT/ITeS or where the export remittance is round-tripped through related parties is refused. The 0.25% concession requires actual export of qualifying services as defined in the relevant SRO and FBR's IT/ITeS list, with proceeds repatriated through normal banking channels and reported on the appropriate PRC / E-Form.
- **R-PK-F7 — Tax avoidance via sole-prop vs Pvt Ltd switching** — Recommending a sole proprietorship purely to access lower individual-income progressive rates while operating de facto as a corporate entity, when substance points to a company, is refused. Document substance and apply the General Anti-Avoidance Rule (GAAR) in the Income Tax Ordinance 2001 and SRB / PRA anti-avoidance provisions.  _(Income Tax Ordinance 2001)_
- **R-PK-F8 — NPO used as a tax shield** — Section 42 Company / Trust / Society status does not by itself confer tax-exempt status on trading income. The NPO must qualify for and renew its Commissioner's approval under section 2(36) and the Second Schedule clause 58 / 66 ITO 2001, and trading income unrelated to charitable objects remains taxable. The skill refuses to advise on structuring trading activities through an NPO to evade tax.  _(Section 2(36) and Second Schedule clause 58/66 ITO 2001)_

## Section 4 — Sole Proprietorship

### Nature

- **Sole Proprietorship** — A Sole Proprietorship in Pakistan is not a registered "entity" per se — it is simply an individual person carrying on business under a trade name, identified for tax by the proprietor's National Tax Number (NTN), which for individuals is the CNIC. There is no separate legal personality; the proprietor trades in their personal capacity with unlimited liability.

### Key features

- Single proprietor (1 owner only); for 2+ owners, the structure becomes an AOP / partnership.
- Proprietor must be at least 18 (mental capacity rules under contract law apply).
- Proprietor must hold a valid CNIC (or NICOP for overseas Pakistanis) and be tax-resident in Pakistan in practice.
- No SECP filing; no audited accounts; no MEMART.
- Trade name may be used informally; registration with the relevant Chamber of Commerce is common (and required by some clients for verification) but not statutory.
- Cannot use suffixes "Limited", "Pvt Ltd", "SMC-Pvt", "PLC", "LLP", "(Guarantee) Limited", "Foundation", or any other restricted designation.

### Formation steps

1. **Obtain NTN from FBR.** Register on FBR IRIS portal (iris.fbr.gov.pk) using CNIC, mobile number, email, and biometric verification at NADRA e-Sahulat or via the FBR Tax Asaan mobile app. NTN issuance is typically 1 working day.
2. **Choose business name** (informally) and prepare a business letterhead / invoice template showing NTN.
3. **Register for STRN (Sales Tax Registration Number)** with FBR if dealing in taxable goods (federal), or with the provincial revenue authority (SRB / PRA / KPRA / BRA / ICT) if providing taxable services — only required above the relevant threshold or for voluntary registration.
4. **Provincial professional tax / shop registration:** register with the relevant Excise & Taxation Department for shop signage / trade licence as applicable (varies by province and municipality).
5. **Chamber of Commerce membership** (optional but useful for trade verification).
6. **EOBI** (Employees' Old-Age Benefits Institution) registration if hiring 5+ employees.
7. **Provincial social security** (Punjab Social Security, Sindh ESSI, etc.) registration if hiring employees.
8. **PSEB registration** if exporting IT / IT-enabled services (see Section 8 — strongly recommended).

### Tax

- **Sole proprietorship general taxation** — Profits taxed in the hands of the proprietor under the Income Tax Ordinance 2001 at individual progressive slab rates (the slabs for business individuals and salaried individuals differ — Finance Act 2025 updated slab rates).  _(Income Tax Ordinance 2001)_

**2025–26 indicative slabs for business individuals / AOPs**  _(verify against Finance Act 2025 schedule)_

| Band | Rate |
| --- | --- |
| Up to Rs 600,000 | 0% |
| Rs 600,001 – Rs 1,200,000 | 15% |
| Rs 1,200,001 – Rs 1,600,000 | 20% |
| Rs 1,600,001 – Rs 3,200,000 | 30% |
| Rs 3,200,001 – Rs 5,600,000 | 40% |
| Above Rs 5,600,000 | 45% |

- **Super tax under section 4C** — up to 10% on high-income persons (above Rs 500M) graduated  _(section 4C ITO 2001)_
- **Sales tax / GST** — federal sales tax 18% on goods; provincial sales tax on services 13% (PRA), 13–15% (SRB), 15% (KPRA), 15% (BRA), 16% (ICT) — rates vary by service category and province
- **Withholding tax on services received from the sole proprietor** — 10% / 11% (filers) / 22% (non-filers)  _(section 153 ITO 2001)_
- **PSEB-registered IT/ITeS export proceeds** — 0.25% final tax under the IT export regime (verify against current Finance Act and SRO 1359(I)/2022 as amended)  _(SRO 1359(I)/2022)_

### When to use

- Single Pakistani-resident founder with micro to small turnover and low liability risk.
- Family business, retail, personal services, freelance creative or technical work where simplicity dominates.
- **Freelance software developer with low export volumes** (< Rs 5M annually) where the administrative cost of a company is disproportionate — provided PSEB registration is still obtained for the 0.25% concession.

### When to avoid

- Liability-sensitive activities (any work with significant counterparty risk).
- Foreign shareholder participation desired.
- Plans to raise external equity or onboard institutional clients who require a corporate counterparty.
- Anything signalling corporate substance — Pakistani enterprise clients overwhelmingly prefer "Pvt Ltd".
- IT/ITeS exporters with turnover > Rs 50M — the SMC-Pvt + PSEB combination becomes materially more efficient and credible.

## Section 5 — AOP (Association of Persons / Partnership)

### Nature

- **AOP** — An AOP (Association of Persons) in Pakistan is the tax-law term for any association of two or more persons that does not constitute a company. The most common AOP is a general partnership registered under the Partnership Act 1932 by filing Form C with the Registrar of Firms of the relevant province. The partnership is not a separate legal person under the Partnership Act, but is treated as a separate taxable entity under the Income Tax Ordinance 2001.  _(Partnership Act 1932; Income Tax Ordinance 2001)_

### Key features

- **AOP key features** — - Minimum 2 partners; maximum 20 partners under the Partnership Act 1932 (s.4). - Partners may be individuals or bodies corporate (but corporate partners create complexities — typically all-individual). - Partners' liability is joint and several and unlimited in a general partnership. - Partnership deed (written agreement) is essential; oral partnerships are recognised but unsafe. - Registration with the Registrar of Firms is not mandatory for the partnership to exist, but unregistered partnerships cannot sue to enforce contractual rights (s.69 Partnership Act 1932) — registration is therefore strongly recommended. - LLP under the Limited Liability Partnership Act 2017 is a separate regime — see Section 5A.  _(Partnership Act 1932 §4, §69)_

### Formation steps

1. **Draft the partnership deed** covering partners, capital contributions, profit-sharing ratios, management, admission / retirement of partners, and dispute resolution. Stamp the deed with the appropriate provincial stamp duty.
2. **Apply to the Registrar of Firms** of the relevant province (Punjab, Sindh, KPK, Balochistan, ICT) using Form C / Form I with partners' details and partnership deed.
3. Pay the prescribed registration fee.
4. Receive the Certificate of Registration of Firm.
5. **Obtain NTN for the firm** from FBR IRIS portal (separate NTN from individual partners' NTNs).
6. **STRN registration** with FBR (goods) or relevant provincial authority (services) if applicable.
7. **EOBI / provincial social security** as applicable.
8. **Chamber of Commerce membership** (optional).
9. **PSEB registration** if exporting IT/ITeS services.

### Tax

- **AOP taxation** — AOPs are taxed at the same business individual / AOP slabs noted in Section 4. The AOP files its own return; the partners' share of taxed AOP profit is exempt in their personal returns to avoid double tax (clause 4 Part III First Schedule ITO 2001). Sales tax / GST applies as for any business above threshold. PSEB 0.25% final tax regime is available to AOPs that are registered exporters of IT/ITeS.  _(clause 4 Part III First Schedule ITO 2001)_

### When to use

- 2+ professional partners (law firm, accounting firm, consulting practice, architecture practice) where ICAP / Pakistan Bar Council rules or local practice favour partnerships.
- Family businesses where the partners are content with joint and several unlimited liability and want to avoid SECP corporate compliance.
- Small joint ventures where the parties expect to dissolve within a short horizon.

### When to avoid

- Liability-sensitive activities — convert to LLP or Pvt Ltd.
- Where partners want clean exit through share transfer — partnerships restructure messily.
- Where external equity is contemplated — partnerships do not have shares.
- Banking, insurance, NBFC, telecom, listed-company activity — must be Ltd or PLC.

### Section 5A — Limited Liability Partnership (LLP)

- **LLP** — The Limited Liability Partnership Act 2017 introduced LLPs into Pakistan, registered with SECP (not the Registrar of Firms). An LLP is a separate legal person; partners' liability is limited to their capital contribution except for their own wrongful acts. Designated partners are responsible for compliance. LLPs are taxed as AOPs under ITO 2001 (pending further clarification). LLPs are uncommon in practice because Pvt Ltd remains the dominant SECP vehicle, but LLPs suit professional services where partnership culture matters and limited liability is desired.  _(Limited Liability Partnership Act 2017)_

## Section 6 — Single Member Company (SMC-Pvt)

### Nature

- **SMC-Pvt** — A Single Member Company (SMC-Pvt) is a private limited company with exactly one shareholder and a mandatory nominee director (who steps in on the shareholder's death or incapacity). Introduced by SECP and codified in the Companies Act 2017, the SMC-Pvt is the closest Pakistani analogue to a one-person LLC.  _(Companies Act 2017)_

### Founders and directors

- **Founders and directors** — - Exactly 1 shareholder (by definition — if a second shareholder is admitted, the company must convert to Pvt Ltd within 30 days). - Minimum 1 director (commonly the sole shareholder). - Mandatory nominee director who becomes director on the shareholder's death; nominee details filed with SECP. - Company Secretary: not mandatory for SMC-Pvt below the threshold (was previously mandatory; SECP relaxed for small SMCs — verify current SECP Single Member Companies Rules 2003 as amended). - Foreign shareholder permitted; if working in Pakistan, work visa and SBP / BOI permissions may apply.  _(SECP Single Member Companies Rules 2003 as amended)_

### Capital

- **Capital** — Minimum paid-up share capital: flexible under Companies Act 2017 — no statutory floor for ordinary cases; commonly Rs 100,000 in practice. Sectoral minimums override. Companies with foreign shareholders are subject to BOI registration under the Foreign Private Investment (Promotion and Protection) Act 1976 and may face higher capital expectations in practice for visa and SBP repatriation purposes (no fixed statutory floor, but BOI guidelines recommend USD 150,000 for some sectors).  _(Companies Act 2017; Foreign Private Investment (Promotion and Protection) Act 1976)_

### Governance

- Single director or board (at director's discretion).
- Annual general meeting (AGM) requirements are relaxed for SMCs — single-member resolutions in writing suffice for most decisions.
- Statutory books: register of members (one entry), register of directors, register of charges, register of nominee director.

### Formation steps

1. **Reserve the company name** via the SECP eServices portal (ezfile.secp.gov.pk) — name must end with "(SMC-Private) Limited" or "(SMC-Pvt) Ltd". Reservation valid 60 days for Companies; 30 days for Limited Liability Partnerships (LLPs).
2. **Pay name reservation fee** via 1Link / online banking.
3. **File incorporation documents** electronically through eServices:
   - Memorandum and Articles of Association (MEMART) — SECP provides standard templates for SMCs.
   - Form 1 — Declaration of compliance.
   - Form 21 — Notice of registered office address.
   - Form 29 — Particulars of directors, CEO, and nominee director.
   - Form INC.8 — Single Member Company nomination form (nominee director details).
   - CNIC copies for shareholder, director(s), and nominee director.
   - Proof of registered office address.
4. **Pay incorporation fee** (sliding scale by authorised capital).
5. **SECP issues Certificate of Incorporation** with Corporate Universal Identification Number (CUIN) typically within 4–10 working days for eServices submissions.
6. **NTN issued by FBR** — automatic linkage in many cases via FBR–SECP integration; otherwise apply on IRIS portal.
7. **Open corporate bank account** using Certificate of Incorporation, MEMART, NTN, CNIC of director, and SECP's CUIN.
8. **STRN registration** with FBR (goods) or provincial revenue authority (services) if applicable.
9. **PSEB registration** — critical for IT/ITeS exporters (Section 8).
10. **EOBI / provincial social security** as triggered.
11. Sector licences where applicable.

### Tax

- **Standard company rate** — 29% of taxable income (2025–26; verify against Finance Act 2025)  _(Income Tax Ordinance 2001)_
- **Small company rate** — 20% of taxable income, where the company satisfies all of: turnover ≤ Rs 250,000,000; paid-up capital plus undistributed reserves ≤ Rs 50,000,000; employees ≤ 250; not formed by splitting an existing entity; no associated undertakings  _(Income Tax Ordinance 2001)_
- **Super tax** — graduated up to 10% for very high-income companies  _(section 4C ITO 2001)_
- **Minimum tax** — 1.25% of turnover (general rate; lower for specified sectors) if the company would otherwise pay less than this amount  _(section 113 ITO 2001)_
- **Alternative Corporate Tax (ACT)** — 17% of accounting profit if higher than regular tax  _(section 113C ITO 2001)_
- **PSEB-registered IT/ITeS exporters** — 0.25% final tax on export remittances under the concessional regime (verify against Finance Act 2025 and SRO 1359(I)/2022 as amended). This is the central reason most freelance software developers incorporate as SMC-Pvt rather than continue as sole proprietors.  _(SRO 1359(I)/2022)_
- **Sales tax / GST** — federal sales tax 18% on goods; provincial sales tax on services as applicable
- **Withholding tax obligations** — on supplier payments, salaries, rent, and dividends under sections 152 / 153 / 155 / 158 ITO 2001  _(sections 152/153/155/158 ITO 2001)_
- **Dividend tax** — 15% withholding on dividends paid to resident individuals (10% for filers in some categories); 25% for non-filers. PSEB-registered IT/ITeS exporters are subject to the standard 15% dividend rate (verify under current Finance Act).
- **Annual filings** — Form A (annual return) within 30 days of AGM; audited financial statements if turnover or paid-up capital exceeds the SECP audit threshold (currently Rs 1 million paid-up for company audit requirement under Companies Act 2017 — confirm against SECP Audit Oversight Rules); annual income tax return by 31 December for companies with June year-end (corporate returns 31 December annually for tax-year-ending-June companies).  _(Companies Act 2017; SECP Audit Oversight Rules)_

### When to use

- Freelance software developer or other solo IT/ITeS exporter seeking limited liability, corporate substance for clients, and the PSEB 0.25% final-tax regime — the canonical default for this profile.
- Solo professional consultant or trader wanting limited liability without the complexity of a multi-member Pvt Ltd.
- Founder planning to bring in co-founders later — easy conversion to Pvt Ltd.

### When to avoid

- Multi-founder ventures from inception — start as Pvt Ltd directly.
- Pure micro / informal activity where a sole proprietorship suffices and PSEB does not apply.
- Activities where sectoral licence requires Pvt Ltd or PLC (banking, insurance).

## Section 7 — Private Limited Company (Pvt Ltd)

### Nature

- **Pvt Ltd** — A Private Limited Company ("Pvt Ltd") is a separate legal person incorporated under Companies Act 2017 with 2–50 members. The Pvt Ltd is the dominant corporate vehicle for SMEs in Pakistan above the single-founder threshold.  _(Companies Act 2017)_

### Founders, members, and directors

- **Founders, members, directors** — - Minimum 2 members and 2 directors (no statutory floor on paid-up capital; commonly Rs 100,000). - Maximum 50 members (excluding employees and former employees who hold shares). - Director must be 18 or older; foreign directors permitted with work visa / BOI clearance where required. - Company Secretary mandatory for public-interest companies and certain Pvt Ltds above turnover threshold (SECP rules; small Pvt Ltds often exempt). - Chief Executive Officer (CEO) mandatory — one of the directors or a separate person appointed by the board.

### Capital

- **Capital** — Minimum paid-up share capital: flexible — no statutory floor for ordinary cases; commonly Rs 100,000 in practice. Sectoral floors override. All issued shares must be paid up at allotment (SECP practice). Sectoral minimums: scheduled commercial bank Rs 10 billion (SBP), microfinance bank Rs 300M–Rs 1B (tiered), life insurer Rs 700M, non-life insurer Rs 500M, asset management company Rs 230M, brokerage Rs 250M (Trading Right Entitlement Certificate holder), NBFC varying by category. Companies with foreign shareholding must comply with BOI Foreign Investment Policy thresholds (no fixed minimum in Companies Act, but BOI guidance applies for visa and repatriation).

### Governance

- **Governance** — - Board of directors (2 or more); elections every 3 years. - Annual General Meeting (AGM) mandatory; first AGM within 16 months of incorporation, thereafter within 15 months of previous AGM and within 4 months of FY end. - Statutory books: register of members, register of directors, register of charges, minute books, register of debenture-holders (if any). - Beneficial Ownership Register mandatory under SECP Beneficial Ownership Regulations 2020 — disclosure of ultimate beneficial owners (UBOs) (≥ 25% ownership or effective control).  _(SECP Beneficial Ownership Regulations 2020)_

### Formation steps

1. **Reserve the company name** via SECP eServices (ezfile.secp.gov.pk) — name must end with "(Private) Limited" or "(Pvt) Ltd".
2. **Pay name reservation fee.**
3. **Prepare MEMART** (SECP model articles acceptable for most small Pvt Ltds; bespoke MEMART for complex ownership / sectoral needs).
4. **File incorporation documents** electronically through eServices:
   - MEMART.
   - Form 1 — Declaration of compliance.
   - Form 21 — Notice of registered office.
   - Form 29 — Particulars of directors and CEO.
   - Beneficial Ownership Form (BO declaration).
   - CNIC copies for all shareholders and directors; passport copies for foreign shareholders / directors.
   - Proof of registered office address.
5. **Pay incorporation fee** (sliding scale by authorised capital).
6. **SECP issues Certificate of Incorporation** with CUIN within 4–10 working days.
7. **NTN issued by FBR** — automatic via FBR–SECP integration or apply on IRIS portal.
8. **Open corporate bank account.**
9. **STRN registration** with FBR or provincial revenue authority.
10. **PSEB registration** if exporting IT/ITeS.
11. **EOBI / provincial social security** as triggered.
12. **Sector licences** where applicable.

### Tax

- **Companies Income Tax** — 29% standard or 20% small-company rate (same conditions as SMC-Pvt — Section 6)
- **Super tax** — up to 10% for high-income companies  _(section 4C)_
- **Minimum tax** — 1.25% of turnover  _(section 113)_
- **Alternative Corporate Tax (ACT)** — 17%  _(section 113C)_
- **PSEB-registered IT/ITeS exporters** — 0.25% final tax on export remittances
- **Sales tax / GST** — federal 18% goods; provincial services rates
- **Dividend tax** — 15% standard withholding (reduced rates for filers in some categories; 25% non-filers; 15% standard for PSEB-registered IT/ITeS dividends — verify under current Finance Act)
- **Annual filings** — Form A annual return within 30 days of AGM; audited financial statements (audit mandatory under Companies Act 2017 for almost all Pvt Ltds above the small-company audit exemption — confirm against SECP rules); income tax return.  _(Companies Act 2017)_

### When to use

- Most SMEs above the single-founder threshold: consultancies, e-commerce, light manufacturing, services, family businesses with multiple owners.
- IT/ITeS firms with 2+ founders wanting PSEB benefits + limited liability + corporate substance for clients.
- Founders planning external equity raise (clean cap table, audited accounts).

### When to avoid

- Single founder — use SMC-Pvt for simplicity.
- Pure micro / informal activity — sole proprietorship suffices.
- NGO / charitable — use Section 42 Company / Trust / Society.

## Section 8 — PSEB Registration (Pakistan Software Export Board) — CRITICAL

**PSEB registration is the single most important formation-stage decision for any Pakistani software developer, IT services firm, or IT-enabled services exporter.**

### What is PSEB

- **PSEB** — The Pakistan Software Export Board (Guarantee) Limited (PSEB) is the Ministry of IT and Telecommunication's apex body for promoting Pakistan's IT and IT-enabled services exports. Registration is mandatory to access the 0.25% concessional final tax on IT / ITeS export remittances and other incentives.

### Key benefits of PSEB registration

- **Key benefits** — 1. **0.25% concessional final tax** on IT and IT-enabled services export proceeds received from outside Pakistan through normal banking channels (under SRO 1359(I)/2022 and subsequent Finance Act amendments). For non-PSEB-registered exporters, the rate is typically 1% under the same regime. Verify against the Finance Act 2025 and current SRO — this regime is reviewed annually at Budget time and has historically been one of the most negotiated incentives. 2. **Zero-rated sales tax** on IT/ITeS exports (verify under Sales Tax Act 1990 and relevant SROs). 3. **Standard 15% dividend tax** on dividends paid out of PSEB-registered company's profits to resident shareholders, where the dividends are sourced from IT/ITeS export income (verify under current Finance Act). 4. **Eligibility for PSEB-administered training, marketing, and trade-mission programmes**. 5. **Access to STZA (Special Technology Zones Authority)** incentives where applicable — separate regime with its own tax holidays (10-year tax holiday AND exemption from minimum tax, WHT, & custom duties for STZA-licensed zone enterprises). 6. **Credibility** for international clients verifying that the Pakistani counterparty is a legitimate IT exporter.  _(SRO 1359(I)/2022)_

### Eligibility for PSEB registration

- **Eligibility** — - Must be a Pakistani-registered business (sole proprietorship NTN, AOP, SMC-Pvt, Pvt Ltd, PLC, or LLP). - Must engage in the export of IT services (software development, custom software, SaaS, web / mobile development, IT consulting, system integration, etc.) or IT-enabled services (ITeS) (call centres, BPO, KPO, animation, e-commerce platforms, content moderation, data annotation for AI training, etc.) — refer to the PSEB list of qualifying services. - Must have or commit to having a registered office in Pakistan. - Must have a corporate bank account capable of receiving export remittances and issuing Proceeds Realisation Certificates (PRCs) / E-Forms.

### PSEB registration steps

1. **Create an account** on the PSEB portal (pseb.org.pk).
2. **Submit the online application form** including:
   - Company / firm details (CUIN, NTN, STRN, registered office, contact details).
   - List of directors / partners / proprietor with CNIC.
   - Bank account details and authorised signatories.
   - Description of IT/ITeS services offered.
   - Number of employees and key technical personnel.
   - Sample client invoices / contracts (export evidence).
3. **Upload supporting documents**:
   - SECP Certificate of Incorporation (or Registrar of Firms certificate for AOP, or CNIC for sole proprietor).
   - MEMART (for companies).
   - NTN certificate.
   - Bank account details and at least one Proceeds Realisation Certificate (PRC) or E-Form evidencing past or projected IT/ITeS export remittance.
   - Office tenancy / utility bill.
4. **Pay PSEB registration fee** (varies by entity type and turnover band).
5. **PSEB verification** — site visit / desk review.
6. **PSEB Certificate of Registration** issued, typically within 2–4 weeks.
7. **Annual renewal** required to maintain status.

### Tax treatment after PSEB registration

- **Tax treatment after PSEB registration** — Export remittances received through normal banking channels and supported by PRC / E-Form attract 0.25% withholding under section 154A ITO 2001 (IT / ITeS export regime), treated as final tax. The company files its income tax return and reflects the final-tax export turnover separately from any domestic income (which is taxed under the regular CIT regime at 29% / 20%). Domestic IT/ITeS sales (PKR-denominated invoices to Pakistani clients) do not qualify for the 0.25% regime and are taxed under regular CIT. Sales tax: provincial sales tax on services for any domestic sales; exports are zero-rated. The PSEB regime is reviewed at every Federal Budget. The 0.25% final-tax rate has been challenged and modified multiple times since 2022. Always verify against the current Finance Act and SROs in force at the date of advice. Flag any 2026 changes.  _(section 154A ITO 2001)_

### When NOT to register with PSEB

- Pure domestic IT services (PKR-only revenue from Pakistani clients) — no export benefit accrues; registration adds compliance cost without offset.
- Non-IT / non-ITeS activities — ineligible.

## Section 9 — Public Limited Company (PLC)

### Nature

- **PLC** — A Public Limited Company ("Limited" or "Ltd" without "Private") is a public company incorporated under Companies Act 2017 whose shares can be offered to the public and which may be listed on the Pakistan Stock Exchange (PSX) or remain unlisted. PLCs face the heaviest regulatory burden.  _(Companies Act 2017)_

### Founders, members, and directors

- **Founders, members, directors** — - Minimum 3 members and 3 directors (7 directors for listed PLCs under the Code of Corporate Governance). - No statutory maximum members. - At least one independent director for listed PLCs; female director(s) required by the Code of Corporate Governance. - Company secretary mandatory. - Chief Financial Officer (CFO) mandatory for listed PLCs.

### Capital

- **Capital** — Minimum paid-up share capital: No statutory minimum paid-up capital for unlisted PLCs under Companies Act 2017. Listed PLCs face higher capital and free-float requirements under PSX Rule Book (free-float ≥ 25% in most cases). Sectoral floors override for banking, insurance, NBFC.  _(Companies Act 2017; PSX Rule Book)_

### Formation steps

1. Name reservation (must end with "Limited" or "Ltd" — without "Private").
2. MEMART filing (bespoke MEMART required for PLCs; SECP model articles are not appropriate).
3. Statutory declaration of compliance.
4. SECP incorporation and CUIN issuance.
5. Registration with the Securities and Exchange Commission of Pakistan (SECP) for any public offer (separate prospectus filing under Public Offering Regulations 2017).
6. PSX listing application if listing.
7. Full corporate governance regime: audited accounts, AGM mandatory, half-yearly reviewed accounts, quarterly accounts if listed.

### Tax

- **CIT** — 29% (typically large company; small-company 20% rare for PLCs by virtue of scale)
- **Super tax** — up to 10% under section 4C  _(section 4C)_
- **Minimum tax** — 1.25% of turnover under section 113  _(section 113)_
- **ACT** — 17% under section 113C  _(section 113C)_
- **Special tax treatment for listed companies** — reduced rate on disposal of listed securities under Eighth Schedule; CGT on listed securities currently 15% for filers — verify under current Finance Act  _(Eighth Schedule)_

### When to use

- Capital-raising at scale (public offer, PSX listing, private placement to institutional investors).
- Mature businesses with strong governance and stable profitability.

### When to avoid

- SMEs — compliance cost is disproportionate.
- Family / founder-led businesses where dilution is undesirable.
- Early-stage ventures — Pvt Ltd is the appropriate launch vehicle; convert to PLC at IPO stage.

## Section 10 — Non-Profit Organisations (NPOs)

### Nature

- **NPO regimes** — Pakistani NPOs may be formed under three principal regimes: 1. Section 42 Company under Companies Act 2017 — "company limited by guarantee not having share capital", suffix "(Guarantee) Limited" or analogous. 2. Trust under Trusts Act 1882 (private trusts) or provincial Charitable Trust Acts (public charitable trusts). 3. Society under Societies Registration Act 1860 — common for literary, scientific, charitable, educational, professional, and religious associations.  _(Companies Act 2017; Trusts Act 1882; Societies Registration Act 1860)_

### Section 42 Company

- **Section 42 Company** — - Minimum 3 members and 3 Trustees. - Minimum start-up donation: PKR 200,000. - Profits must be applied wholly to the objects; no dividends to members. - SECP licence under section 42 required before incorporation; 6–12 weeks process. - Suffix "(Guarantee) Limited" or other approved designation. - Annual audit and Form A annual return.  _(Companies Act 2017 §42)_

### Trust

- **Trust** — - Minimum 2 trustees (3+ recommended). - Trust deed registered with the Sub-Registrar in the relevant district under the Registration Act 1908. - Stamp duty on trust deed varies by province. - No SECP role. - Public charitable trusts require Commissioner of Auqaf / Charity Commissioner registration in some provinces.  _(Trusts Act 1882; Registration Act 1908)_

### Society

- **Society** — - Minimum 7 members under Societies Registration Act 1860 s.1. - MOA and rules filed with Registrar of Societies (Joint Stock Companies registrar in some provinces). - Annual list of governing body members filed annually. - No SECP role.  _(Societies Registration Act 1860 s.1)_

### Tax (all NPO regimes)

- **Tax (all NPO regimes)** — - Section 2(36) ITO 2001 — definition of "non-profit organisation". - Clause 58 / 66 Second Schedule ITO 2001 — exemptions for NPOs that obtain Commissioner's approval (formerly section 2(36)(c) certificate). - PCP (Pakistan Centre for Philanthropy) certification strengthens the case for donor-side tax credit under section 61 ITO 2001 (donations to PCP-certified NPOs). - Trading income unrelated to charitable objects is taxable under the regular CIT regime — see R-PK-F8. - Sales tax / GST applies on taxable supplies above threshold.  _(Section 2(36) ITO 2001; Clause 58/66 Second Schedule ITO 2001; section 61 ITO 2001)_

### When to use

- Genuine NGO, charity, religious body, professional association, research institute, alumni group, cultural body.

### When to avoid

- Any commercial / profit-distributing intent — use Pvt Ltd.
- "Charity" used to disguise trading or to obtain tax-free status — refused (R-PK-F8).

## Section 11 — SECP eServices Registration Workflow

SECP registration is now fully electronic through the eServices portal at ezfile.secp.gov.pk. Paper filing is residual.

### Standard workflow

1. Account creation. Each subscriber creates an eServices account using CNIC (Pakistanis) or passport (foreigners), email, mobile number, and digital signature (PIN-based).
2. Name availability search. Two proposed names ranked by preference. Reservation valid 60 days for Companies; 30 days for Limited Liability Partnerships (LLPs) (extendable).
3. Form completion. Online forms covering: type of entity, registered office, principal activity, directors / proprietors / trustees, shareholders / members, share capital and allotment (for companies), beneficial ownership (UBO), company secretary (if applicable).
4. Document upload. Scanned signatures, CNICs / passports, MEMART (for companies), constitution / rules (for societies), trust deed (for trusts), declarations.
5. Payment. SECP filing fees plus stamp duty (provincial, on MEMART and forms — paid via challan or 1Link).
6. Review by SECP. 4–10 working days typically; longer for Section 42 Companies (6–12 weeks).
7. Certificate issuance. Downloadable electronic Certificate of Incorporation with CUIN (Corporate Universal Identification Number).
8. FBR NTN linkage. SECP–FBR integration generally issues NTN automatically within 1–3 working days. Otherwise apply manually on FBR IRIS portal.

### Common pitfalls

- Name rejected for similarity, restricted words ("Bank", "Insurance", "Investment", "Trust", "Federal", "National", "Stock Exchange" — restricted; some require regulatory NOC), or trademark conflicts.
- Inconsistent CNIC / signature between portal upload and underlying document.
- Missing beneficial ownership declaration — SECP Beneficial Ownership Regulations 2020 mandatory.
- Failure to disclose foreign shareholding — triggers BOI permit obligations downstream.
- MEMART objects clause too narrow — restricts future business activity.

## Section 12 — FBR NTN, STRN, and Provincial Tax Registrations

### Federal Board of Revenue (FBR)

#### NTN (National Tax Number)

- **NTN** — - For individuals: NTN = CNIC number. Activate via FBR IRIS portal (iris.fbr.gov.pk) using NADRA biometric verification at an e-Sahulat centre, or via the Tax Asaan mobile app. - For AOPs: separate AOP NTN issued by FBR on application. - For companies (SMC-Pvt, Pvt Ltd, PLC, Section 42): NTN issued automatically via SECP–FBR integration in many cases; otherwise apply via IRIS. - Mandatory for: filing returns, opening bank accounts (corporate), receiving payments above thresholds, withholding tax compliance.

#### STRN (Sales Tax Registration Number) — federal sales tax on goods

- **STRN** — - Mandatory for: manufacturers, wholesalers, importers / exporters of goods, and retailers above the Tier-1 threshold under section 14 / SRO definitions. - Apply via FBR IRIS portal under "Registration for Sales Tax". - Issued typically within 5–10 working days subject to biometric / site verification. - Monthly sales tax return (Annexure-A, B, C) by the 18th (filing) / 15th (payment) of the following month.  _(section 14 STA 1990)_

#### Income tax return filing

- **Income tax return filing due dates** — - Companies: due 31 December for tax years ending 30 June (Pakistan's default tax year for companies); 30 September for tax years ending 31 December (special tax year companies). - Individuals and AOPs: due 30 September annually. - E-filing on FBR IRIS portal mandatory.

### Provincial Revenue Authorities — Sales Tax on Services

- **SRB (Sindh Revenue Board)** — Service rate 13% (standard); rates vary by service category. IT services: reduced rate in some cases.  _(sindhrevenue.gov.pk)_
- **PRA (Punjab Revenue Authority)** — Standard rate 16% (reduced 5% / 13% for specified services).  _(pra.punjab.gov.pk)_
- **KPRA (Khyber Pakhtunkhwa Revenue Authority)** — Standard rate 15%.  _(kpra.gov.pk)_
- **BRA (Balochistan Revenue Authority)** — Standard rate 15%.  _(bra.gob.pk)_
- **ICT (Islamabad Capital Territory)** — administered by FBR; standard 16%.
- **Registration threshold** — Registration required if turnover from taxable services exceeds the threshold (typically Rs 4M annually under most provincial regimes — varies).

Pakistan has separate provincial sales tax regimes on services following the 18th Amendment. Monthly return filing by the relevant due date in each province.

### Other registrations

- **EOBI (Employees' Old-Age Benefits Institution)** — mandatory for employers with 5+ employees; contribution 5% of minimum wage (employer) + 1% (employee)  _(EOBI Act 1976)_
- **Provincial Social Security** — (PESSI in Punjab, SESSI in Sindh, etc.) — for industrial / commercial employees earning below wage ceiling; ~6% of wages
- **Workers Welfare Fund (WWF)** — 2% of taxable income for companies with annual income above the threshold
- **Workers Profit Participation Fund (WPPF)** — 5% of profit for companies with 50+ employees (some sectors exempt)
- **Professional tax** — provincial, varies by category and city

## Section 13 — Sector-Specific Licences (Signposting Only)

SECP / sole-prop registration is necessary but not sufficient for regulated activities. Common sector licences:

**Sector-Specific Licences**

| Sector | Regulator | Typical licence |
| --- | --- | --- |
| Commercial / Islamic / microfinance banking | State Bank of Pakistan (SBP) | Scheduled bank licence (paid-up Rs 10B+); microfinance bank tiered (Rs 300M–Rs 1B) |
| Payment service providers, EMI, payment aggregators | SBP | PSP / PSO / EMI licence under SBP Regulations for EMIs 2019 |
| Insurance (life, non-life, takaful) | SECP Insurance Division | Insurer registration; capital Rs 500M–Rs 700M |
| NBFCs (asset management, brokerage, leasing, investment finance, REIT management) | SECP | NBFC licence under NBFC Rules 2003 / 2008 |
| Capital markets (broker, dealer, fund manager, registrar, custodian) | SECP + PSX | TREC holder licence; fund manager licence |
| Modaraba | SECP Modaraba Sector | Modaraba registration under Modaraba Companies Ordinance 1980 |
| Telecom (LL, LDI, WLL, ISP, VAS) | PTA (Pakistan Telecommunication Authority) | Class licence or individual licence |
| Broadcasting (TV, FM radio, cable, satellite, online streaming with broadcast content) | PEMRA (Pakistan Electronic Media Regulatory Authority) | Broadcast licence |
| Pharmaceuticals, food, cosmetics, medical devices | DRAP (Drug Regulatory Authority of Pakistan) + provincial Food Authorities | Product registration; facility licence |
| Oil and gas upstream | OGRA (downstream) + DG Petroleum Concessions (upstream) | Petroleum concession licence |
| Power generation, transmission, distribution, trading | NEPRA (National Electric Power Regulatory Authority) | Generation / transmission / distribution licence |
| Mining | Provincial Mines & Mineral Development Departments | Exploration / mining lease |
| Aviation | PCAA (Pakistan Civil Aviation Authority) | Air operator certificate |
| Shipping | MMD (Mercantile Marine Department) | Coastal trading / cargo licence |
| Foreign investment (any sector) | BOI (Board of Investment) | Investment registration; expatriate quota / work visa endorsement |
| **IT and IT-enabled services exports** | **PSEB (Pakistan Software Export Board)** | **PSEB registration — Section 8 of this skill (CRITICAL)** |
| Special Technology Zones | STZA (Special Technology Zones Authority) | Zone Developer / Zone Enterprise licence; 10-year tax holiday AND exemption from minimum tax, WHT, & custom duties for licensed entities |
| Construction (foreign companies) | PEC (Pakistan Engineers Council) + BOI | Constructor enlistment; BOI registration |
| Health (hospitals, clinics, labs) | Provincial Healthcare Commissions; PMDC | Facility licence; practitioner registration |
| **Personal data processing (any sector)** | **(emerging)** | **Personal Data Protection Bill pending — track status. Currently no general data-protection regulator; sectoral rules apply (SBP for banking data, PTA for telecom data).** |

## Section 14 — Tax Treatment Comparison

**Tax Treatment Comparison**

| Entity | Income tax regime | Statutory rate | Small / SME relief | Reporting |
| --- | --- | --- | --- | --- |
| Sole proprietorship | Individual progressive slabs under ITO 2001 | 0% / 15% / 20% / 30% / 40% / 45% (2025–26 indicative — verify Finance Act 2025) | First Rs 600,000 of total income exempt | Annual return by 30 September; monthly sales tax (if registered) |
| AOP (Partnership) | AOP slabs (same as business individuals) | Progressive slabs as above; partners' share exempt to avoid double tax | Same slab exemption | Annual return by 30 September; partners file individually |
| SMC-Pvt | Companies Income Tax | **29%** standard or **20%** small company | Small company: turnover ≤ Rs 250M, paid-up ≤ Rs 50M, employees ≤ 250 | Annual return by 31 December (June FY end); Form A annual return; audited accounts |
| Pvt Ltd | Companies Income Tax | Same as SMC-Pvt | Same small-company test | Same as SMC-Pvt |
| PLC | Companies Income Tax | 29% (typically large) | Generally outside small-company band | Annual return by 31 December; half-yearly reviewed; quarterly if listed |
| Section 42 / Trust / Society | Exempt on income applied to objects (with Commissioner's approval); CIT on unrelated trading income | 0% on objects; 29% on trading | n/a | Annual return; PCP certification optional |
| **PSEB-registered IT/ITeS exporter (any entity type)** | **Final tax under section 154A ITO 2001 on export remittances** | **0.25% final tax** on qualifying export proceeds (vs 1% non-PSEB; verify under Finance Act 2025) | Export turnover ring-fenced from regular CIT base | Same as base entity; PSEB annual renewal |

## Section 14 — Tax Treatment Comparison

Notes:
- **Small-company test (companies)**: turnover ≤ Rs 250M; paid-up capital + undistributed reserves ≤ Rs 50M; employees ≤ 250; not split from existing entity; no associated undertakings. All conditions must be met.
- **Super tax (section 4C)**: graduated 1%–10% on companies / persons with income above Rs 150M, with banded thresholds up to Rs 500M+. Verify Finance Act 2025 bands.
- **Minimum tax (section 113)**: 1.25% of turnover; lower rates for specified sectors (oil marketing, refineries, etc.).
- **ACT (section 113C)**: 17% of accounting profit; comparison with regular tax; higher applies.
- **Sales tax**: federal 18% on goods; provincial services rates 13–16%.
- **Withholding tax** (services received, section 153): 10% (filers), 11% (filer companies), 22% (non-filers). Filer status (Active Taxpayer List) is critical — verify counterparties.
- **Dividend tax**: 15% standard (resident shareholders); 15% standard PSEB-IT dividend; 25% non-filers (verify Finance Act 2025).

## Section 15 — Decision Tree

Q1: Will any non-Pakistani individual or entity hold shares or be a director?
  YES → go to Q1a
  NO  → go to Q2

Q1a: Is the sector on the Negative List (arms, narcotics, security printing,
     consumable alcohol) or otherwise restricted under BOI Investment Policy?
  YES → Refuse green-light recommendation (R-PK-F2); escalate to BOI / legal counsel
  NO  → Private Ltd (Pvt Ltd) with BOI registration; SBP repatriation rules apply;
        sectoral licence check; work visa for foreign directors if working in Pakistan

Q2: Is the purpose non-profit / charitable / religious / educational / research?
  YES → Section 42 Company OR Trust OR Society (choose by scale and governance);
        seek Commissioner's NPO approval under section 2(36) and Second Schedule clause 58 / 66
  NO  → go to Q3

Q3: Is this a regulated sector (banking, insurance, NBFC, capital markets, telecom,
     broadcasting, pharma, oil and gas, power, mining, aviation, shipping)?
  YES → Refuse green-light recommendation; map sectoral licence (R-PK-F5); typically Pvt Ltd or PLC
  NO  → go to Q4

Q4: Does the business export IT / IT-enabled services (software, SaaS, BPO, KPO, etc.)?
  YES → STRONGLY recommend PSEB registration regardless of entity choice;
        proceed to Q5 for entity selection alongside PSEB registration
  NO  → go to Q5

Q5: Plans to raise public equity or list on the PSX within 3 years?
  YES → Public Limited Company (PLC)
  NO  → go to Q6

Q6: Multiple professional partners (law, accounting, consulting) wanting limited liability?
  YES → LLP under Limited Liability Partnership Act 2017 (SECP-registered),
        OR registered general partnership (AOP) if unlimited liability acceptable
  NO  → go to Q7

Q7: Solo founder wanting limited liability + corporate substance + PSEB benefits?
  YES → SMC-Pvt (Single Member Company) — strong default for solo IT/ITeS exporters
  NO  → go to Q8

Q8: 2+ founders wanting limited liability and small-company 20% CIT band?
  YES → Private Ltd (Pvt Ltd) — strong default for multi-founder SMEs
  NO  → go to Q9

Q9: Micro turnover; single Pakistani-resident founder; domestic clients only;
     accept unlimited liability; simplicity prized?
  YES → Sole Proprietorship (NTN-based)
  NO  → revisit intake; default for solo = SMC-Pvt; default for 2+ = Pvt Ltd

- **R-PK-F2** — Refuse green-light recommendation; escalate to BOI / legal counsel — triggered when a non-Pakistani individual/entity holds shares/director role and the sector is on the Negative List (arms, narcotics, security printing, consumable alcohol) or otherwise restricted under BOI Investment Policy.  _(Section 15 Decision Tree Q1a)_
- **R-PK-F5** — Refuse green-light recommendation; map sectoral licence — triggered for regulated sectors (banking, insurance, NBFC, capital markets, telecom, broadcasting, pharma, oil and gas, power, mining, aviation, shipping); typically Pvt Ltd or PLC.  _(Section 15 Decision Tree Q3)_

## Section 16 — Worked Example: Solo Freelance Software Developer in Lahore

**Scenario.** Bilal, Pakistani, 28, freelance software developer in Lahore. Expects **Rs 30,000,000 gross revenue in 2025–26**, 90% from US and EU clients (export), 10% from one Lahore-based SME (domestic PKR). No employees. Home office. Wants corporate substance for international clients and is cost-conscious.

### Option A — Sole Proprietorship (NTN-based)

- Register NTN on FBR IRIS portal (CNIC-based NTN; same-day to 3 working days).
- Register with **PRA (Punjab Revenue Authority)** for provincial sales tax on services — applies to the Rs 3M domestic PKR revenue (16% PRA standard rate; verify current IT services rate under PRA notifications).
- Register with **PSEB** as a sole proprietor exporter — eligible for the **0.25% final tax** on the Rs 27M export revenue.
- Tax estimate (2025–26 indicative; verify Finance Act 2025):
  - Export revenue Rs 27,000,000 — **0.25% final tax = Rs 67,500**.
  - Domestic revenue Rs 3,000,000, assume Rs 1,500,000 net after deductible expenses — taxed at individual progressive slabs:
    - Up to Rs 600,000 @ 0% = Rs 0
    - Next Rs 600,000 @ 15% = Rs 90,000
    - Next Rs 300,000 @ 20% = Rs 60,000
    - **Domestic tax: Rs 150,000**
  - **Total federal income tax: approx Rs 217,500** (effective 0.7% on Rs 30M gross — driven by the PSEB regime).
- Provincial sales tax on Rs 3M domestic services @ ~16% = ~Rs 480,000 (passed to client; not Bilal's cost provided invoiced correctly).
- No SECP audit; no Form A; unlimited personal liability.
- **Total formation cost**: ~Rs 5,000–15,000 (NTN free; PSEB registration fee; PRA registration fee).

- **PIT slab: up to Rs 600,000** — 0% PKR (Individual progressive slab, Option A worked example)  _(Section 16 worked example)_
- **PIT slab: next Rs 600,000** — 15% PKR (Individual progressive slab, Option A worked example)  _(Section 16 worked example)_
- **PIT slab: next Rs 300,000** — 20% PKR (Individual progressive slab, Option A worked example)  _(Section 16 worked example)_
- **PSEB export final tax (Option A)** — 0.25% (applied to Rs 27,000,000 export revenue = Rs 67,500 final tax)  _(Section 16 worked example; verify Finance Act 2025)_
- **PRA provincial sales tax on services (Option A)** — 16% (standard PRA rate; verify current IT services rate under PRA notifications; applies to Rs 3M domestic PKR revenue)  _(Section 16 worked example)_

### Option B — SMC-Pvt (Single Member Company) with PSEB registration

- Incorporate **"Bilal Tech Solutions (SMC-Private) Limited"** via SECP eServices with Rs 100,000 paid-up share capital.
- Nominee director: Bilal's brother (CNIC, signed nomination Form INC.8).
- SECP fees + stamp duty + professional fees: ~Rs 30,000–60,000 all-in.
- NTN issued automatically.
- Register STRN with FBR (if needed) and PRA for provincial sales tax on services.
- Register with **PSEB** as an SMC-Pvt exporter — eligible for **0.25% final tax** on Rs 27M export revenue.
- Tax estimate (2025–26 indicative):
  - Export revenue Rs 27,000,000 — **0.25% final tax = Rs 67,500**.
  - Domestic revenue Rs 3,000,000, assume Rs 1,500,000 net — taxed under **small-company CIT at 20%** (company qualifies: turnover ≤ Rs 250M, paid-up ≤ Rs 50M, employees ≤ 250): **20% × Rs 1,500,000 = Rs 300,000**.
  - Minimum tax check (section 113): 1.25% × Rs 3,000,000 domestic turnover = Rs 37,500 → regular tax higher, so regular tax applies.
  - **Total company income tax: approx Rs 367,500**.
- Bilal can pay himself a **director's salary** subject to PAYE withholding under section 149 ITO 2001 — structured to fall within lower individual slabs.
- **Dividend tax** if Bilal distributes retained PSEB-export profits: **15%** (standard rate; verify Finance Act 2025).
- Annual filings: Form A, audited accounts (if above audit threshold), annual tax return.

- **PSEB export final tax (Option B)** — 0.25% (applied to Rs 27,000,000 export revenue = Rs 67,500 final tax)  _(Section 16 worked example; verify Finance Act 2025)_
- **Small-company CIT rate (Option B)** — 20% (applied to Rs 1,500,000 domestic net = Rs 300,000; company qualifies as small: turnover ≤ Rs 250M, paid-up ≤ Rs 50M, employees ≤ 250)  _(Section 16 worked example)_
- **Minimum tax check (section 113)** — 1.25% × Rs 3,000,000 domestic turnover = Rs 37,500 → regular tax higher, so regular tax applies  _(section 113 ITO 2001; Section 16 worked example)_
- **Dividend tax rate (Option B)** — 15% (standard rate; verify Finance Act 2025)  _(Section 16 worked example)_

### Comparison summary

**Comparison summary: Sole Prop (Option A) vs SMC-Pvt + PSEB (Option B)**  _(Section 16 worked example)_

| Item | Sole Prop (Option A) | SMC-Pvt + PSEB (Option B) |
| --- | --- | --- |
| Export revenue tax (Rs 27M) | Rs 67,500 (0.25%) | Rs 67,500 (0.25%) |
| Domestic revenue tax (Rs 1.5M net) | Rs 150,000 (PIT slabs) | Rs 300,000 (20% small-co CIT) |
| **Total federal income tax** | **Rs 217,500** | **Rs 367,500** |
| Limited liability | No | Yes |
| Corporate substance for clients | Weak | Strong |
| Dividend tax (if profits paid out) | n/a | 15% standard |
| Director salary (PAYE) | n/a | Available; reduces company profit |
| Formation cost | Rs 5–15K | Rs 30–60K |
| Annual SECP compliance | None | Form A + (potentially) audit |

### Recommendation

- **At Rs 30M turnover with 90% export**, the **headline federal tax is materially lower as a sole proprietorship** (Rs 217,500 vs Rs 367,500) because the **0.25% PSEB regime applies equally** to both, and the domestic slice is taxed at lower individual slabs (15%–20%) vs the corporate 20%.
- **However**, the **SMC-Pvt** offers:
  - **Limited liability** — important if Bilal signs SLAs / IP indemnities with US clients.
  - **Corporate substance** — many US / EU clients require a corporate counterparty, not a freelancer.
  - **Dividend planning flexibility** — Bilal can retain profits inside the company and distribute at 7.5% later, plus pay himself a tax-efficient director's salary.
  - **Scalability** — easier to hire employees, raise capital, or bring in co-founders later.
- **Decision**: at Rs 30M and rising, **SMC-Pvt with PSEB registration is the recommended default** for a serious freelance software developer with international clients, despite the modest tax premium. The premium becomes negligible once director-salary optimisation and dividend planning are applied.
- **Edge case**: if Bilal's international clients are individual founders / micro-clients who do not require a corporate counterparty, and revenue is below Rs 10M, **sole proprietorship with PSEB registration** is acceptable and simpler.

### Option C — Pvt Ltd (rejected for solo founder)

Pvt Ltd requires 2 members and 2 directors. For a true solo founder, the SMC-Pvt is the cleaner vehicle. If Bilal expects a co-founder soon, he can incorporate as Pvt Ltd with a nominee 1-share co-founder, or incorporate SMC-Pvt and convert later.

## Section 17 — Conservative Defaults

- **Default entity: solo Pakistani founder exporting IT/ITeS** — SMC-Pvt with PSEB registration, because the combination of limited liability, corporate substance, dividend planning flexibility, and the 0.25% final-tax PSEB regime dominates almost every alternative at meaningful turnover.  _(Section 17 Conservative Defaults item 1)_
- **Default entity: solo Pakistani founder with purely domestic micro turnover** — Sole Proprietorship (NTN-based).  _(Section 17 Conservative Defaults item 2)_
- **Default entity: 2+ founders, no foreign capital, domestic-or-export** — Private Limited (Pvt Ltd).  _(Section 17 Conservative Defaults item 3)_
- **Default entity: any foreign shareholder** — Private Limited (Pvt Ltd) with BOI registration, SBP repatriation compliance, sectoral licence check, and work-visa planning.  _(Section 17 Conservative Defaults item 4)_
- **Default entity: NGO / charity / religious / educational** — Section 42 Company (Companies Act 2017), or Trust / Society depending on scale and governance preference.  _(Section 17 Conservative Defaults item 5)_
- **Default sectoral check** — Always test the proposed business activity against the sectoral matrix in Section 13 before quoting timelines, because regulated activities can add 8–24 weeks for sectoral licensing.  _(Section 17 Conservative Defaults item 6)_
- **Small company tax classification thresholds** — turnover ≤ Rs 250M, paid-up ≤ Rs 50M, employees ≤ 250, no associated undertakings; failure on any drops the company into the 29% standard band. PKR / count (all four conditions must be confirmed)  _(Section 17 Conservative Defaults item 7)_
- **Default PSEB action** — For any IT/ITeS exporter, register with PSEB as the highest-priority post-incorporation step. Reconfirm the 0.25% / 1% rates against the current Finance Act at the date of advice — flag any 2026 change.  _(Section 17 Conservative Defaults item 8)_
- **Default banking caveat** — Schedule 2–4 weeks for corporate bank account opening (longer for any foreign director / shareholder); SBP AML / CDD is rigorous; export remittances require PRC / E-Form facility on the account.  _(Section 17 Conservative Defaults item 9)_
- **Default annual compliance reminder** — SECP Form A (within 30 days of AGM) + audited accounts (if above threshold) + FBR income tax return (31 December for June year-end companies; 30 September for individuals and AOPs) + monthly sales tax (if registered) + EOBI / WPPF / WWF as triggered + PSEB annual renewal if registered.  _(Section 17 Conservative Defaults item 10)_

## Section 18 — Sources

- **Companies Act 2017** — Primary corporate statute replacing the Companies Ordinance 1984; covers Pvt Ltd, PLC, SMC-Pvt, Section 42 Company.  _(Companies Act 2017)_
- **Limited Liability Partnership Act 2017** — LLP regime under SECP.  _(Limited Liability Partnership Act 2017)_
- **Partnership Act 1932** — General partnership (AOP) regime.  _(Partnership Act 1932)_
- **Income Tax Ordinance 2001 (ITO 2001)** — Federal income tax framework; sections 4C (super tax), 113 (minimum tax), 113C (ACT), 153 (WHT on services), 154A (IT/ITeS export final tax), 2(36) (NPO definition), Second Schedule clauses 58 and 66 (NPO exemptions).  _(Income Tax Ordinance 2001)_
- **Finance Act 2025** — Annual tax amendments effective 1 July 2025 for tax year 2025–26; verify slabs, super-tax bands, PSEB regime, dividend rates, withholding rates against the current Act.  _(Finance Act 2025)_
- **Sales Tax Act 1990** — Federal sales tax on goods.  _(Sales Tax Act 1990)_
- **Sindh / Punjab / KPK / Balochistan / ICT Sales Tax on Services Acts** — Provincial regimes following the 18th Amendment.  _(Sindh / Punjab / KPK / Balochistan / ICT Sales Tax on Services Acts)_
- **SRO 1359(I)/2022 and subsequent SROs** — IT/ITeS export final-tax regime (verify amendments).  _(SRO 1359(I)/2022)_
- **Trusts Act 1882** — Private trust framework.  _(Trusts Act 1882)_
- **Societies Registration Act 1860** — Society framework.  _(Societies Registration Act 1860)_
- **Foreign Private Investment (Promotion and Protection) Act 1976** — Foreign-investment protection framework.  _(Foreign Private Investment (Promotion and Protection) Act 1976)_
- **Benami Transactions (Prohibition) Act 2017** — Anti-benami statute.  _(Benami Transactions (Prohibition) Act 2017)_
- **SECP Beneficial Ownership Regulations 2020** — UBO disclosure.  _(SECP Beneficial Ownership Regulations 2020)_
- **SECP Single Member Companies Rules 2003 (as amended)** — SMC-Pvt framework.  _(SECP Single Member Companies Rules 2003)_
- **Code of Corporate Governance** — Listed-company governance (SECP / PSX).  _(Code of Corporate Governance (SECP / PSX))_
- **Pakistan Stock Exchange Rule Book** — PSX listing rules.  _(Pakistan Stock Exchange Rule Book)_
- **SBP Prudential Regulations** — Banking; SBP Regulations for EMIs 2019.  _(SBP Prudential Regulations)_
- **State Bank of Pakistan Foreign Exchange Manual** — SCRA, export remittance, dividend repatriation.  _(State Bank of Pakistan Foreign Exchange Manual)_
- **PTA Telecom Rules / NEPRA Licensing Regulations / DRAP Act / PEMRA Ordinance** — Sectoral regulators.  _(PTA Telecom Rules / NEPRA Licensing Regulations / DRAP Act / PEMRA Ordinance)_
- **PSEB Registration Rules and website** — IT/ITeS exporter registration and 0.25% final-tax regime.  _(PSEB (Pakistan Software Export Board) Registration Rules; pseb.org.pk)_
- **STZA Act 2021** — Special Technology Zones Authority framework and 10-year tax holiday.  _(STZA Act 2021)_
- **EOBI Act 1976; Provincial Social Security Ordinances; Workers Welfare Fund Ordinance 1971; Companies Profits (Workers' Participation) Act 1968** — Employee-related contributions.  _(EOBI Act 1976; Provincial Social Security Ordinances; Workers Welfare Fund Ordinance 1971; Companies Profits (Workers' Participation) Act 1968)_

Portals: **ezfile.secp.gov.pk** (SECP), **iris.fbr.gov.pk** (FBR), **pseb.org.pk** (PSEB), **stza.gov.pk** (STZA), **sbp.org.pk** (SBP), **boi.gov.pk** (BOI), **sindhrevenue.gov.pk** (SRB), **pra.punjab.gov.pk** (PRA), **kpra.gov.pk** (KPRA), **bra.gob.pk** (BRA).

Where a specific monetary threshold, slab rate, or sectoral capital floor is uncertain at the time of advice, mark as **TBC** and verify against the current **Finance Act 2025** schedule, the latest **SBP / SECP / PTA / NEPRA / DRAP circular**, and any **SRO** amendment in force before relying on it. The PSEB 0.25% / 1% rates and dividend treatment in particular have been reviewed at every recent Federal Budget and may shift in 2026.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice under Pakistani law. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Pakistani legal practitioner, **ICAP** or **ICMAP** chartered accountant, or **PTBA / Pakistan Tax Bar Association** member before acting upon. Foreign founders should additionally engage immigration counsel for work visa / POC / NICOP matters, which are out of scope.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

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
