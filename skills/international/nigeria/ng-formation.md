---
name: ng-formation
description: "Use this skill whenever asked about forming, incorporating, or registering a business in Nigeria. Trigger on phrases like \"form company Nigeria\", \"incorporate Nigeria\", \"CAC registration\", \"BN vs LTD Nigeria\", \"PVT LTD Nigeria\", \"register business Nigeria\", \"Business Name Nigeria\", \"Private Limited Nigeria\", \"Plc Nigeria\", \"LLP Nigeria\", \"Incorporated Trustee\", \"NGO Nigeria\", \"FIRS TIN\", \"CAMA 2020\", or any question about choosing or registering a Nigerian entity. Covers entity comparison (BN, Ltd / RC, LLP, Plc, Incorporated Trustee), CAC online portal registration steps, FIRS TIN and state IRS registration, sector-specific licensing (NDPR, SEC, CBN, NCC, NAFDAC), minimum capital and shareholder/director requirements, the SME-friendly thresholds introduced by the Nigeria Tax Act 2025 (NTA 2025), and tax treatment by entity type. Out of scope: immigration / expatriate quota / CERPAC sponsorship, bank account opening procedures (high-level only), full corporate governance and shareholders' agreement drafting, deep sector-specific regulatory licensing beyond signposting, and listing on the NGX. ALWAYS read this skill before advising on Nigerian entity formation."
jurisdiction: NG
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ng-formation

## Section 1 — Quick Reference

**Section 1 — Quick Reference**

| Field | Value |
| --- | --- |
| Country | Federal Republic of Nigeria |
| Currency | NGN (Nigerian Naira) |
| Company registrar | Corporate Affairs Commission (CAC) |
| Tax authority (federal) | Federal Inland Revenue Service (FIRS) — being restructured into the Nigeria Revenue Service (NRS) under NTA 2025 |
| Tax authority (state) | State Internal Revenue Service (e.g., LIRS in Lagos, FCT-IRS in Abuja) for PAYE, personal income tax, and certain state taxes |
| Key legislation | Companies and Allied Matters Act (CAMA) 2020; Finance Acts 2019–2023; Nigeria Tax Act 2025 (NTA 2025); Investments and Securities Act 2025; Nigeria Data Protection Act 2023 |
| Registration portal | pre.cac.gov.ng (CAC public portal) |
| Typical formation time | 3–7 working days for BN; 5–14 working days for Ltd (RC); 4–8 weeks for Plc; 6–12 weeks for Incorporated Trustee |
| Standard corporate tax rate (CIT) | 30% large companies; 20% medium companies (turnover > ₦100M and ≤ ₦50B); 0% small companies (turnover ≤ ₦100M and fixed assets ≤ ₦250M) under NTA 2025 |
| VAT rate | 7.5% (NTA 2025 retains the rate; broader base) |
| Skill version | 1.0 |

## Section 2 — Entity Types Comparison

**Section 2 — Entity Types Comparison**

| Feature | Business Name (BN) | Private Ltd (Ltd / RC) | LLP | Public Ltd (Plc) | Incorporated Trustee (IT) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No (owner = business) | Yes | Yes | Yes | Yes (non-profit) |
| Liability | Unlimited personal | Limited to share capital | Limited to capital contribution (except for own wrongful acts) | Limited to share capital | Trustees personally exempt for proper acts |
| Min. founders / members | 1 sole proprietor or 2+ partners | 1 (post-CAMA 2020) | 2 partners | 2 members; no statutory maximum | 2 trustees (typically 3+ in practice) |
| Max. members | n/a | 50 (excluding employees/former employees who hold shares) | No statutory cap | Unlimited | Unlimited |
| Foreign ownership | Practically restricted (must be resident sole proprietor or partners) | 100% permitted | 100% permitted | 100% permitted | Subject to objects and security vetting |
| Min. share capital / capital | None | ₦100,000 (minimum issued share capital under CAMA 2020 for private companies); sectoral floors override | None statutory | ₦2,000,000 minimum issued share capital under CAMA 2020 | Not share capital based |
| Minimum capital for companies with foreign participation | n/a | ₦100,000,000 minimum issued share capital required for NIPC business permit (foreign-owned companies) | Same NIPC requirement applies | Same NIPC requirement applies | n/a |
| Tax treatment | Personal Income Tax (PIT) at progressive rates | Companies Income Tax (CIT) — 0% / 20% / 30% per NTA 2025 | Pass-through where partners are taxed (state PIT) unless elected; CIT if treated as company | CIT 30% (typically large company) | Tax-exempt for non-trading income; CIT on trading profits not applied to objects |
| Annual filing with CAC | Annual return (Form CAC/BN/7) | Annual return + audited financial statements (small companies exempt from audit under CAMA s.402) | Annual return + statement of accounts | Annual return + audited financial statements | Annual return + statement of affairs |
| Suffix on name | none (use "Enterprises", "Ventures", etc.) | "Limited" or "Ltd" | "Limited Liability Partnership" or "LLP" | "Public Limited Company" or "Plc" | "Incorporated Trustees of …" |
| Admin burden | Low | Medium | Medium | High | Medium–High |

**Recommended defaults:**

- Solo founder, micro turnover, low-risk activity, comfortable with unlimited liability: **Business Name (BN)**.
- Solo or small group founder, wanting limited liability and access to the **0% small-company CIT band**: **Private Limited (Ltd)**.
- Professional services partnership (law, accounting, consulting): **LLP**.
- Plans to raise public capital or list on the NGX: **Plc**.
- Non-profit / NGO / religious / charitable: **Incorporated Trustee**.

## Section 3 — Required Inputs and Refusal Catalogue

### Required intake before recommending an entity

- **Required intake before recommending an entity** — 1. Nationality and residence of each founder. 2. Number of founders / promoters. 3. Intended business activity (objects) and expected SIC / NIPC classification. 4. Expected annual turnover and gross fixed-asset base (drives small-company CIT classification). 5. Whether any foreign shareholder or director is involved (triggers NIPC and CERPAC issues). 6. Capital available for paid-up share capital and any sectoral minimum. 7. Whether the business will hire employees (PAYE registration with state IRS). 8. Whether the business handles personal data (NDPR / Nigeria Data Protection Act 2023 obligations). 9. State / city of principal place of business (drives state IRS and certain local levies).

### Refusal catalogue

- **R-NG-F1 — Fronting / nominee structures** — Using a Nigerian nominee director or shareholder to disguise foreign control in a sector reserved for Nigerian citizens under the NIPC Act (e.g., certain extractive, security, and broadcasting activities) is not advised. The skill will not draft or advise on nominee arrangements designed to circumvent indigenisation or NIPC requirements. Escalate to a Nigerian legal practitioner.  _(R-NG-F1)_
- **R-NG-F2 — Sectors closed or restricted to foreign investment** — Sectors on the NIPC Negative List (production of arms and ammunition, narcotic drugs, military and paramilitary wear) are closed. Petroleum upstream, oil and gas services, broadcasting, and shipping have layered licensing and local content requirements beyond simple CAC registration — out of scope.  _(R-NG-F2)_
- **R-NG-F3 — Immigration, expatriate quota, and CERPAC** — Expatriate quota approvals, Subject to Regularisation (STR) visas, CERPAC residence cards, and business permits for foreign-owned companies are processed by the Federal Ministry of Interior and NIPC. The skill flags requirements but does not handle immigration filings; engage an immigration consultant.  _(R-NG-F3)_
- **R-NG-F4 — Bank account opening for foreigners without local presence** — Tier-1 Nigerian banks require directors to attend in person or appoint a properly notarised attorney for KYC under CBN's Customer Due Diligence Regulations. The skill flags the requirement but does not guarantee any specific bank's onboarding.  _(R-NG-F4)_
- **R-NG-F5 — Regulated sectors: banking, insurance, capital markets, fintech, telecom, pharmaceuticals** — These require sector licences (CBN, NAICOM, SEC, NCC, NAFDAC) in addition to CAC registration. Capital floors are much higher than the CAMA minimums. Formation alone is insufficient — the skill refuses to provide a green-light recommendation without mapping the sectoral licence.  _(R-NG-F5)_
- **R-NG-F6 — Tax avoidance via BN vs Ltd switching** — Recommending a BN purely to access lower personal-income progressive rates while operating de facto as a corporate entity, when substance points to a company, is refused. Document substance and apply the anti-avoidance principles in the NTA 2025 / Finance Act provisions.  _(R-NG-F6)_
- **R-NG-F7 — Charity / NGO used as a tax shield** — Incorporated Trustee status does not by itself confer tax-exempt status on trading income. Trading income unrelated to the objects of the charity remains taxable. The skill refuses to advise on structuring trading activities through an IT to evade CIT.  _(R-NG-F7)_

### Nature

- **Business Name (BN)** — A Business Name is a registration of a trade name with the CAC under Part E of CAMA 2020. It is not a separate legal person. The proprietor (or partners) trade in their personal capacity, with unlimited personal liability.  _(Part E of CAMA 2020)_

### Key features

- **BN key features** — - Sole proprietor (1 owner) or general partnership (2–20 partners; partnerships above 20 must incorporate as a company unless they are a professional partnership permitted by enabling law). - Proprietor / partners must be at least 18 (or 16 if a director of a company; CAMA s.20 — but for BN the practical floor is 18). - All proprietors / partners must be resident in Nigeria in practice, because the business has no separate personality and tax filing is via the resident's personal tax records with the state IRS. - No notarial deed; no audited accounts. - Registered name format: as approved; suffixes like "Enterprises", "Ventures", "Global Services" are common. Cannot use "Limited", "Ltd", "Plc", "LLP", or "Incorporated".  _(CAMA s.20)_

### Formation steps

- **BN formation steps** — 1. Search and reserve the name via the CAC public portal (pre.cac.gov.ng). 2. Complete Form CAC/BN/1 online (proprietor / partners, nature of business, principal office address, signature page). 3. Upload IDs (NIN or international passport) and a passport photograph for each proprietor / partner. 4. Pay the statutory CAC fee. 5. Receive the Certificate of Registration of Business Name (typically 3–7 working days). 6. Register with the relevant State Internal Revenue Service for personal income tax (proprietor) and PAYE if hiring employees. 7. TIN is issued automatically by FIRS at the point of CAC registration (post-CAMA 2020 integration).

### Tax

- **BN tax treatment** — - Profits taxed in the hands of the proprietor (or partners pro rata) under the Personal Income Tax Act (PITA) at progressive rates administered by the state IRS of the proprietor's residence. - 2025 PIT bands (NTA 2025-aligned): 0% on first ₦800,000; 15% on next ₦2,200,000; 18%, 21%, 23%, 25% on subsequent bands; top rate 25% above ₦50,000,000 (verify against current NTA 2025 schedule when filing). - VAT registration mandatory if taxable turnover exceeds ₦100,000,000 small-company threshold (small companies under NTA 2025 are VAT-exempt below this turnover; previously the registration threshold was ₦25,000,000 under Finance Act 2019). - Withholding tax (WHT) at 5% / 10% applies on services received from the BN.  _(Personal Income Tax Act (PITA); Finance Act 2019; NTA 2025)_

### When to use

- Single Nigerian-resident founder with micro turnover and low liability risk.
- Family business / micro-retail / personal services / freelance creative work where simplicity matters.

### When to avoid

- Liability-sensitive activities.
- Foreign shareholder participation desired.
- Plans to raise external equity.
- Anything signalling corporate substance — clients and counterparties prefer "Ltd".

### Nature

- **Private Limited Company (Ltd / RC)** — A Private Limited Company ("Ltd", carrying the registration prefix RC — e.g., "RC 1234567") is a separate legal person incorporated under Part B of CAMA 2020. It is by far the most common corporate vehicle for SMEs in Nigeria.  _(Part B of CAMA 2020)_

### Founders, members, and directors

- **Ltd founders, members, directors** — - Minimum 1 member and 1 director (CAMA 2020 introduced single-member / single-director private companies — a key change from pre-2020 law which required 2). - Maximum 50 members (excluding employees and former employees who hold shares). - Director must be 18 or older (or 16 with parental consent under CAMA s.20(2)). - Foreign directors permitted; if they will work in Nigeria they need expatriate quota and CERPAC (out of scope — see R-NG-F3). - Company Secretary not mandatory for small companies under CAMA 2020 s.330(1) (a key 2020 reform; required for medium and large companies and all Plcs).  _(CAMA 2020 s.20(2), s.330(1))_

### Capital

- **Ltd capital requirements** — - Minimum issued share capital: ₦100,000 for a private company under CAMA 2020 (replacing the old "authorised share capital" concept — CAMA 2020 abolished authorised share capital in favour of issued share capital under s.27). - All issued shares must be paid up to at least 25% at incorporation in practice (CAC requires evidence of share allotment). - Companies with any foreign shareholder must have a minimum issued share capital of ₦100,000,000 to qualify for an NIPC Business Permit and expatriate quota. - Sectoral minimums override (e.g., commercial bank ₦500B post-2024 CBN recapitalisation; insurance ₦10B–₦20B per class; microfinance bank tiered ₦200M–₦5B).  _(CAMA 2020 s.27)_

### Governance

- **Ltd governance** — - Board of directors (one or more). - Members' meetings: a small company may dispense with the AGM (CAMA s.237) — a 2020 reform reducing burden. - Statutory books: register of members, register of directors, register of charges, minute books.  _(CAMA s.237)_

### Formation steps

- **Ltd formation steps** — 1. Search and reserve the company name via pre.cac.gov.ng (name must end with "Limited" or "Ltd"). 2. Prepare and upload Memorandum and Articles of Association (MEMART) — CAC default model articles are available and acceptable for most small companies. 3. Complete the online incorporation form (formerly CAC 1.1 — now a fully electronic process) covering: registered office address, directors, members, share allotment, secretary (if any), persons with significant control (PSC) under CAMA s.119. 4. Upload IDs (NIN for Nigerians; passport for foreigners) and signatures. 5. Pay CAC filing fees and stamp duty on share capital (0.75% of issued share capital, payable to FIRS). 6. Certificate of Incorporation issued with the RC number; TIN issued automatically by FIRS. 7. Open a corporate bank account using the Certificate, MEMART, TIN, and directors' KYC. 8. Register for VAT with FIRS (now NRS) if turnover threshold met. 9. Register with the state IRS for PAYE on employees' salaries. 10. Sector licences where applicable.  _(CAMA s.119)_

### Tax

- **CIT — small company** — 0% percent (turnover ≤ ₦100,000,000 and fixed assets ≤ ₦250,000,000)  _(NTA 2025)_
- **CIT — medium company** — 20% percent (turnover > ₦100M and ≤ ₦50B)  _(NTA 2025)_
- **CIT — large company** — 30% percent (turnover > ₦50B)  _(NTA 2025)_
- **Other Ltd tax obligations** — - Education tax (Tertiary Education Tax) under NTA 2025 — small companies exempt; medium and large pay TET at the prescribed rate (3% of assessable profits under the consolidated NTA 2025 schedule — confirm against the gazetted rate). - Development levy (consolidated) under NTA 2025 — small companies exempt. - VAT 7.5% on taxable supplies; small companies (turnover ≤ ₦100M) are VAT-exempt under NTA 2025. - WHT on services and certain transactions per the WHT Regulations 2024. - Capital Gains Tax 30% on gains realised by companies (aligned to CIT under NTA 2025). - Annual returns and audited financial statements within 42 days of the AGM (or 9 months after FY end if no AGM held — for small companies that dispense with AGM).  _(NTA 2025; WHT Regulations 2024)_

### When to use

- Most SMEs, including freelance software developers, consultancies, e-commerce, light manufacturing.
- Anyone wanting limited liability and the 0% small-company CIT band for the first years of operation.
- Founders planning to raise equity later (clean corporate structure, audited accounts).

### When to avoid

- Pure micro / informal activity where the BN suffices.
- NGO / charitable purposes (use Incorporated Trustee).
- Foreign-capital ventures where the founders cannot meet the ₦100M minimum issued share capital for NIPC Business Permit (some pre-formation planning needed).

### Nature

- **Limited Liability Partnership (LLP)** — LLPs were introduced into Nigerian federal law by CAMA 2020 (Part C). An LLP is a separate legal person; partners' liability is limited to their capital contribution except for liabilities arising from their own wrongful acts. Designated Partners are responsible for compliance.  _(CAMA 2020 Part C)_

### Founders and partners

- **LLP founders and partners** — - Minimum 2 partners; no statutory maximum. - At least 2 Designated Partners; at least one Designated Partner must be resident in Nigeria (CAMA s.747). - Partners can be individuals or bodies corporate (Nigerian or foreign).  _(CAMA s.747)_

### Capital

- **LLP capital** — No statutory minimum capital. Contributions are agreed in the LLP Agreement.

### Formation steps

- **LLP formation steps** — 1. Reserve the LLP name on the CAC portal (name must end with "Limited Liability Partnership" or "LLP"). 2. File Form LLP 01 (incorporation document) and the LLP Agreement (or rely on the default rules in the Second Schedule of CAMA 2020 if no agreement is filed). 3. Provide details of partners and Designated Partners with IDs. 4. Pay CAC filing fee. 5. Certificate of Registration issued; TIN issued automatically.  _(CAMA 2020 Second Schedule)_

### Tax

- **LLP tax treatment** — - Nigerian tax treatment of LLPs is transitional and not yet uniformly resolved: FIRS practice has historically taxed LLPs as if they were partnerships (pass-through to partners under PITA) unless the LLP elects or is treated as a company. - The NTA 2025 begins to align LLP taxation with that of companies in many respects; advise the user that the position is fluid and confirm against the current NTA 2025 implementing regulations. - Conservative default: assume LLP profits are taxable in the partners' hands at PIT rates unless FIRS confirms company treatment.  _(NTA 2025; PITA)_

### When to use

- Multi-partner professional firms (law, accounting, consulting) seeking limited liability without the formality of an Ltd.
- Joint ventures between professionals where pass-through taxation is preferable.

### When to avoid

- Where the partners want clear, settled tax treatment — Ltd is more predictable.
- Where external equity is contemplated — LLPs do not have shares.
- Sectors that require a specific corporate vehicle (banking, insurance) — Ltd or Plc only.

### Nature

- **Public Limited Company (Plc)** — A Plc is a public company incorporated under Part B of CAMA 2020 whose shares can be offered to the public and which may be listed on the Nigerian Exchange (NGX) or remain unlisted. Plcs face the heaviest regulatory burden.  _(Part B of CAMA 2020)_

### Founders, members, and directors

- **Plc founders, members, directors** — - Minimum 2 members; no statutory maximum. - Minimum 3 directors under CAMA s.271 for public companies. - At least one independent director for listed Plcs (per NGX Listing Rules and SEC Code of Corporate Governance). - Company secretary mandatory.  _(CAMA s.271; NGX Listing Rules; SEC Code of Corporate Governance)_

### Capital

- **Plc capital** — - Minimum issued share capital: ₦2,000,000 under CAMA 2020. - At least 25% paid up at incorporation. - Listed Plcs face higher capital and free-float requirements under NGX rules.  _(CAMA 2020)_

### Formation steps

- **Plc formation steps** — 1. Name reservation (must end with "Public Limited Company" or "Plc"). 2. MEMART filing (Plcs cannot rely entirely on model articles — bespoke MEMART required). 3. Statutory declaration of compliance. 4. CAC incorporation and TIN issuance. 5. Registration with the Securities and Exchange Commission (SEC) if offering shares to the public. 6. NGX listing application if listing. 7. Full corporate governance regime: audited accounts, AGM mandatory, quarterly financial reporting if listed.

### Tax

- **Plc CIT rate** — 30% percent (typically falls in the large-company band under NTA 2025)  _(NTA 2025)_
- **Other Plc tax obligations** — Education tax, development levy, withholding obligations as for other companies. Special tax considerations for listed companies (e.g., reduced CGT on quoted-share disposals — confirm against current NTA 2025 schedule).  _(NTA 2025)_

### When to use

- Capital-raising at scale (public offer, NGX listing, private placement to institutional investors).
- Mature businesses with strong governance.

### When to avoid

- SMEs — the compliance cost is disproportionate.
- Family / founder-led businesses where dilution is undesirable.

### Nature

- **Incorporated Trustee (IT)** — An Incorporated Trustee is the Nigerian vehicle for non-profit, charitable, religious, educational, cultural, sporting, or social associations. Registered under Part F of CAMA 2020. The Trustees themselves are incorporated as a body corporate (a body of persons) — sometimes called a "Section 823 entity" after the relevant CAMA section.  _(Part F of CAMA 2020)_

### Founders

- **IT founders** — - Minimum 2 Trustees statutorily, with 3+ in practice for credibility. - Trustees must be of "unimpeachable character" (CAMA s.826) — banned: undischarged bankrupts, persons within 5 years of fraud or dishonesty convictions, persons of unsound mind. - Foreign trustees permitted, subject to NIPC security vetting.  _(CAMA s.826)_

### Formation steps

- **IT formation steps** — 1. Reserve the proposed name — must begin with "Incorporated Trustees of …". 2. Hold a general meeting of the association and pass resolutions appointing Trustees. 3. Newspaper publication: publish the application in at least one national daily newspaper and one local newspaper of the area of operation, giving the public 28 days to object (CAMA s.825). 4. After the objection period, file the application with CAC including: Constitution of the association; Minutes of the appointment meeting; Trustees' details and IDs; Two copies of the trustees' impression / signatures; Newspaper cuttings as proof of publication; Common seal impression. 5. CAC reviews; if approved, issues the Certificate of Incorporation as Incorporated Trustees. 6. TIN issued by FIRS.  _(CAMA s.825)_

### Tax

- **IT tax treatment** — - Income applied wholly to the objects of the association is exempt from CIT under PITA / CITA exemption provisions, retained under NTA 2025 for bona fide non-profits. - Trading income unrelated to the objects is taxable — see R-NG-F7. - VAT on taxable supplies still applies above threshold. - PAYE on staff salaries.  _(PITA; CITA; NTA 2025)_

### When to use

- Genuine NGO, charity, religious body, professional association, alumni group, cultural body.

### When to avoid

- Any commercial / profit-distributing intent — use Ltd.
- "Charity" used to disguise trading or to obtain tax-free status — refused (R-NG-F7).

## Section 9 — CAC Registration Process (Online Portal)

CAC registration is now fully electronic through the public portal at pre.cac.gov.ng (or the legacy portal post.cac.gov.ng for some post-incorporation filings).

### Standard workflow

- **CAC standard workflow** — 1. Account creation. Each applicant creates a CAC portal account using NIN (for Nigerians) or international passport (for foreigners). 2. Name availability search. Two proposed names ranked in order of preference. Reservation valid 60 days. 3. Form completion. Online form covering: type of entity, registered office, principal activity, directors / proprietors / trustees, shareholders / members, share capital and allotment (for companies), PSC (Persons with Significant Control under CAMA s.119), company secretary (if applicable). 4. Document upload. Scanned signatures, IDs, photographs, MEMART (for companies), constitution (for ITs), LLP Agreement (for LLPs), evidence of newspaper publication (for ITs only). 5. Payment. CAC filing fees plus 0.75% stamp duty on share capital (for companies), paid via Remita. 6. Review by CAC. 3–14 working days depending on entity type and any queries raised. 7. Certificate issuance. Downloadable electronic Certificate of Incorporation / Registration with a verifiable QR code. 8. TIN automatic issuance. FIRS receives the registration record and issues a Tax Identification Number automatically, typically within 24–48 hours of the CAC certificate. The TIN appears on the CAC integrated certificate in many cases (post-2021 integration).  _(CAMA s.119)_

### Common pitfalls

- **CAC common pitfalls** — - Name rejected for similarity to existing entity or for restricted words ("Federal", "National", "Chartered", "Cooperative" — restricted; some require ministerial consent). - Inconsistent signatures between portal upload and underlying ID. - Missing PSC declaration — CAMA s.119 mandatory for all companies. - Failure to disclose foreign shareholding — triggers NIPC permit obligations downstream.  _(CAMA s.119)_

### Federal Inland Revenue Service / Nigeria Revenue Service

- **FIRS/NRS registration and filings** — - TIN issuance is automatic at CAC registration (post-CAMA 2020). No separate paper application required for routine cases. - The taxpayer can activate the TIN on the FIRS TaxPro Max portal (taxpromax.firs.gov.ng) to file returns electronically. - Mandatory filings (companies): CIT annual return — 6 months after FY end (s.55 CITA / NTA 2025); VAT monthly return — by the 21st day of the following month; WHT monthly schedule — by the 21st day; Education tax with CIT; Transfer pricing declaration and disclosure forms for related-party transactions (FIRS TP Regulations 2018).  _(s.55 CITA; NTA 2025; FIRS TP Regulations 2018)_

### State IRS (e.g., LIRS, FCT-IRS, OYIRS, RIRS)

- **State IRS obligations** — - All employers (including BNs and Ltds) must register with the state IRS of the state where employees reside / are paid, for PAYE. - Sole proprietors of BNs file annual Form A (PIT) with their state IRS based on personal residence. - Partners in partnerships file individually with their state IRS. - Additional state taxes: development levy, business premises levy (state-specific), and signage / advert levies (local government).

### Other registrations

- **Other payroll-related registrations** — - Industrial Training Fund (ITF) — employers with 5+ employees or ₦50M+ turnover contribute 1% of payroll annually. - Nigeria Social Insurance Trust Fund (NSITF) / Employee Compensation Scheme — 1% of payroll. - Pension Reform Act — mandatory contributory pension for employers with 3+ employees (10% employer + 8% employee of monthly emoluments). - National Housing Fund (NHF) — 2.5% of monthly basic salary deducted from employees earning ₦3,000+ monthly.  _(Industrial Training Fund Act; Employee Compensation Act 2010; Pension Reform Act 2014; National Housing Fund Act)_

## Section 11 — Sector-Specific Licences (Signposting Only)

CAC registration is necessary but not sufficient for regulated activities. Common sector licences:

**Sector-specific licences table**

| Sector | Regulator | Typical licence |
| --- | --- | --- |
| Commercial / merchant / non-interest banking | CBN (Central Bank of Nigeria) | Banking licence; minimum capital ₦200B–₦500B (post-2024 recapitalisation) |
| Microfinance banks | CBN | Tier 1–4 MFB licence; capital ₦200M–₦5B |
| Payment service providers, switching, mobile money, PSB | CBN | PSP / PSSP / MMO / PSB licence; capital ₦100M–₦5B |
| Fintech / virtual asset service providers | SEC (capital markets aspect) and CBN (payments aspect) | SEC VASP registration; CBN no-objection where applicable |
| Insurance | NAICOM (National Insurance Commission) | Life / non-life / composite / reinsurance licence; capital ₦8B–₦20B per class |
| Capital markets (broker, dealer, fund manager, registrar, custodian, investment adviser) | SEC (Securities and Exchange Commission) | SEC functional registration under the **Investments and Securities Act 2025** |
| Pension fund administrators | PenCom | PFA licence; capital ₦5B |
| Telecommunications (ISP, MNO, VAS, infrastructure) | NCC (Nigerian Communications Commission) | Class licence or individual licence |
| Broadcasting (TV, radio, online streaming with broadcast content) | NBC (National Broadcasting Commission) | Broadcasting licence |
| Pharmaceuticals, food, cosmetics, packaged water | NAFDAC | Product registration and facility licence |
| Oil and gas upstream | NUPRC (Nigerian Upstream Petroleum Regulatory Commission) | Petroleum prospecting / mining licence under PIA 2021 |
| Oil and gas midstream / downstream | NMDPRA | Various licences under PIA 2021 |
| Power generation, transmission, distribution, trading | NERC | Generation / transmission / distribution / trading licence |
| Mining | Mining Cadastre Office, Ministry of Solid Minerals | Exploration / mining lease / quarrying licence |
| Aviation | NCAA | Air operator certificate; ground handling licence |
| Shipping | NIMASA | Coastal trading licence; cabotage |
| Construction (foreign companies) | NIPC + sectoral | NIPC business permit; expatriate quota |
| **Personal data processing (any sector)** | **NDPC (Nigeria Data Protection Commission)** | **NDPR / NDPA 2023 registration of data controllers / processors of major importance; appointment of DPO; annual audit return** |
| Health (hospitals, clinics, labs) | Federal / state Ministry of Health, MDCN, MLSCN | Facility licence; practitioner registration |

**Data protection special note.** The **Nigeria Data Protection Act 2023** (NDPA 2023) replaces the NDPR as the primary federal data protection statute. The NDPC supersedes NITDA's data protection mandate. Any business processing personal data above prescribed thresholds (or in sensitive sectors) must register as a **Data Controller / Processor of Major Importance (DCPMI)**, appoint a Data Protection Officer (DPO), and submit annual audit returns. Tech founders in Nigeria should treat NDPA compliance as part of formation.

## Section 12 — Tax Treatment Comparison (Post-NTA 2025)

**Tax Treatment Comparison table**

| Entity | Income tax regime | Statutory rate | Small-company / SME relief | Reporting |
| --- | --- | --- | --- | --- |
| BN (sole proprietor) | PIT (state IRS) | Progressive 0% / 15% / 18% / 21% / 23% / 25% per NTA 2025 PIT schedule | First ₦800,000 of total income exempt | Annual Form A (state IRS) |
| BN (partnership) | PIT pass-through to each partner | Progressive PIT bands | Same as sole proprietor | Each partner files Form A; partnership statement of accounts |
| Ltd / RC | Companies Income Tax | 0% / 20% / 30% per NTA 2025 bands | 0% for small companies (turnover ≤ ₦100M and fixed assets ≤ ₦250M); VAT-exempt; education tax exempt; development levy exempt | Annual CIT return (FIRS) 6 months after FY end |
| LLP | Likely PIT pass-through; subject to FIRS treatment under NTA 2025 implementing regs | Same as PIT bands for partners | Same as BN partnership in conservative view | Annual statement of accounts to CAC; partners file PIT |
| Plc | CIT | 30% (typically large company) | Generally outside small-company band by scale | Annual audited accounts + CIT return; quarterly reporting if listed |
| Incorporated Trustee | Exempt on income applied to objects; CIT on unrelated trading income | 0% on objects-related income; 30% on trading | n/a | Annual return + statement of affairs |

- **Notes on tax treatment comparison** — - NTA 2025 small-company definition: turnover ≤ ₦100,000,000 AND fixed assets (excluding land and buildings) ≤ ₦250,000,000. Both conditions must be met. - VAT registration threshold under NTA 2025: small companies are exempt; entities above ₦100,000,000 turnover must register and charge VAT at 7.5%. - WHT regime updated by the Deduction of Tax at Source (Withholding) Regulations 2024, effective 1 January 2025 (with deferred application for some transactions to 1 July 2025). - Capital allowances and Pioneer Status incentives remain available under NTA 2025 for qualifying companies in priority sectors.  _(NTA 2025; Deduction of Tax at Source (Withholding) Regulations 2024)_

## Section 13 — Decision Tree

```
Q1: Will any non-Nigerian individual or entity hold shares?
  YES → go to Q1a
  NO  → go to Q2

Q1a: Can the founders meet ₦100,000,000 minimum issued share capital
     (required for NIPC Business Permit and expatriate quota)?
  YES → Private Ltd (RC) with NIPC Business Permit; sectoral licence check; CERPAC for foreign directors
  NO  → Defer formation OR consider a 100% Nigerian Ltd with later foreign share transfer (with NIPC permit at that point) OR escalate

Q2: Is the purpose non-profit / charitable / religious / educational?
  YES → Incorporated Trustee (Part F of CAMA 2020); 28-day newspaper publication
  NO  → go to Q3

Q3: Is this a regulated sector (banking, insurance, capital markets, telecom, broadcasting,
     pharma, oil and gas, power, fintech, mining, aviation, shipping)?
  YES → Refuse green-light recommendation; map sectoral licence (R-NG-F5); typically Ltd or Plc
  NO  → go to Q4

Q4: Multiple professional partners wanting limited liability and pass-through-style tax?
  YES → LLP (caveat: tax treatment evolving under NTA 2025)
  NO  → go to Q5

Q5: Plans to raise public equity or list on the NGX within 3 years?
  YES → Plc
  NO  → go to Q6

Q6: Solo or small group; want limited liability; want access to NTA 2025
     0% small-company CIT band?
  YES → Private Ltd (RC) — strong default
  NO  → go to Q7

Q7: Micro turnover; single Nigerian-resident founder; accept unlimited liability;
     simplicity prized?
  YES → Business Name (BN)
  NO  → revisit intake; default = Private Ltd (RC)
```

## Section 14 — Worked Example: Solo Software Developer in Lagos

**Scenario.** Chioma, Nigerian, 29, freelance software developer in Lagos. Expects ₦60,000,000 gross revenue in 2025, mostly Lagos-based SME and one US client. No employees. Home office. Comfortable with corporate substance but cost-conscious.

### Option A — Business Name (sole proprietorship)

- Register a BN with CAC ("Chioma Tech Ventures"). Filing fee modest; 3–7 working days.
- TIN automatic; register with LIRS for personal income tax.
- Tax: PIT progressive bands under NTA 2025. On ~₦60M (assume ₦15M business expenses → ₦45M assessable):
  - First ₦800,000 @ 0% = ₦0
  - Next ₦2,200,000 @ 15% = ₦330,000
  - Next ₦9,000,000 @ 18% = ₦1,620,000
  - Next ₦13,000,000 @ 21% = ₦2,730,000
  - Next ₦20,000,000 @ 23% = ₦4,600,000 (only ₦20M of the remaining ₦20M sits in this band; verify against gazetted NTA 2025 schedule)
  - **Indicative total: ₦9,280,000** (approximately 21% effective on ₦45M).
- VAT: turnover ₦60M is below the ₦100M small-company VAT-exempt threshold under NTA 2025 — no VAT registration required.
- No CAC audit. No limited liability.

### Option B — Private Limited Company (Ltd / RC)

- Incorporate "Chioma Tech Solutions Ltd" with ₦1,000,000 issued share capital (cushion above ₦100,000 minimum).
- Stamp duty on share capital: 0.75% × ₦1,000,000 = ₦7,500.
- CAC fees plus professional fees: ~₦80,000–₦150,000 all-in.
- TIN automatic; register on TaxPro Max.
- Tax: CIT under NTA 2025 — turnover ₦60M ≤ ₦100M and fixed assets well under ₦250M → small company → 0% CIT.
- VAT-exempt under NTA 2025 small-company rules.
- Education tax exempt for small companies.
- Development levy exempt.
- Chioma can pay herself a director's salary subject to PAYE through LIRS; remaining retained profit accumulates in the company.
- Annual return to CAC; statement of accounts (audit not mandatory for small companies under CAMA s.402(3) provided the company meets the small-company criteria).
- **Indicative total federal CIT: ₦0** (PAYE on salary still applies).

### Recommendation

- **Private Limited (Ltd) wins decisively** at this turnover level. The NTA 2025 small-company 0% CIT band, combined with VAT exemption, makes the Ltd the natural choice for a tech founder with ₦60M turnover, far outweighing the higher PIT she would pay on the same profit as a BN.
- Chioma should **incorporate the Ltd**, register on TaxPro Max, register with LIRS for PAYE on her own director's salary (sized to fund living expenses), and budget for **NDPA 2023 registration with the NDPC** because she processes client personal data.

## Section 15 — Conservative Defaults

- **Conservative defaults** — When intake is incomplete or ambiguous, default as follows: 1. Default entity for a solo Nigerian founder with corporate substance: Private Limited (Ltd / RC), because the NTA 2025 0% small-company CIT band (turnover ≤ ₦100M, fixed assets ≤ ₦250M) makes the Ltd materially more tax-efficient than a BN at almost any meaningful turnover. 2. Default entity for a micro Nigerian founder with no corporate ambitions: Business Name (BN). 3. Default entity for 2+ founders, no foreign capital: Private Limited (Ltd). 4. Default entity for any foreign shareholder: Private Limited (Ltd) with ₦100,000,000 minimum issued share capital and NIPC Business Permit + sectoral licence check. 5. Default entity for NGO / charity / religious / educational: Incorporated Trustee. 6. Default sectoral check: always test the proposed business activity against the sectoral matrix in Section 11 before quoting timelines, because regulated activities can add 8–24 weeks for sectoral licensing. 7. Default tax classification (NTA 2025): confirm both turnover and fixed-asset tests against the small-company definition; ineligibility on either drops the company into the 20% medium-company band. 8. Default data protection action: assume NDPA 2023 obligations apply to any tech or services business handling customer data; budget for DCPMI registration and DPO appointment. 9. Default banking caveat: schedule 2–4 weeks for corporate bank account opening (longer if any foreign director / shareholder); CBN AML KYC is rigorous. 10. Default annual compliance reminder: CAC annual return + FIRS / NRS CIT return (where applicable) + VAT monthly (where applicable) + state IRS PAYE monthly + ITF / NSITF / pension as triggered.  _(NTA 2025)_

## Section 16 — Sources

- **Companies and Allied Matters Act 2020** (CAMA 2020) — Parts B (companies), C (LLPs), E (Business Names), F (Incorporated Trustees).
- **Nigeria Tax Act 2025** (NTA 2025) — consolidated tax statute introducing the 0% / 20% / 30% CIT bands, small-company VAT exemption, development levy, and education tax restructuring; restructures FIRS as the Nigeria Revenue Service.
- **Companies Income Tax Act** (CITA) — as amended by Finance Acts 2019, 2020, 2021, 2023 and superseded in parts by NTA 2025.
- **Personal Income Tax Act** (PITA) — as amended.
- **Value Added Tax Act** — as amended.
- **Investments and Securities Act 2025** — capital markets framework.
- **Nigeria Data Protection Act 2023** (NDPA 2023) and NDPR 2019 (residual application).
- **Nigerian Investment Promotion Commission Act** (NIPC Act) — foreign investment framework, Negative List, business permit.
- **Petroleum Industry Act 2021** (PIA 2021) — upstream / midstream / downstream licensing.
- **Pension Reform Act 2014** — contributory pension obligations.
- **Industrial Training Fund Act** (as amended) — 1% payroll levy.
- **Employee Compensation Act 2010** — NSITF.
- **National Housing Fund Act** — 2.5% NHF deduction.
- **Deduction of Tax at Source (Withholding) Regulations 2024** — updated WHT regime effective 1 January 2025.
- **CBN Banking Sector Recapitalisation Programme 2024–2026** — minimum capital ₦200B–₦500B.
- Portals: pre.cac.gov.ng (CAC), taxpromax.firs.gov.ng (FIRS / NRS), nipc.gov.ng (NIPC), sec.gov.ng (SEC), ndpc.gov.ng (NDPC).

Where a specific monetary threshold or sectoral capital floor is uncertain at the time of advice, mark as TBC and verify against the current NTA 2025 schedule, the latest CBN / SEC / NAICOM / NCC circular, and any Finance Act amendment in force before relying on it.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice under Nigerian law. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Nigerian legal practitioner, ICAN / ANAN chartered accountant, or CITN chartered tax practitioner before acting upon. Foreign founders should additionally engage immigration counsel for expatriate quota / CERPAC matters, which are out of scope.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
