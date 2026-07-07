---
name: ie-formation
description: "Use this skill whenever asked about forming, incorporating, or registering a business in Ireland. Trigger on phrases like \"Ireland company formation\", \"CRO registration\", \"LTD Ireland\", \"DAC Ireland\", \"sole trader Ireland\", \"Form A1 Ireland\", \"PPS number business\", \"incorporate Ireland\", \"CORE portal\", \"register business Ireland\", \"RBO Ireland\", \"TR1 Ireland\", \"TR2 Ireland\", \"Companies Act 2014\", \"CLG Ireland\", \"PLC Ireland\", or any question about choosing or registering an Irish entity. Covers entity comparison (Sole Trader, Partnership, LP, LLP, LTD / CLS, DAC, CLG, PLC), CRO online portal (CORE) registration steps, Revenue TR1 / TR2 tax registration, sector-specific licensing (Central Bank, CCPC, DPC), RBO beneficial ownership filing, PPS number requirements for directors and shareholders, and tax treatment by entity type including the 12.5% trading CT rate and PRSI Class S. Out of scope: immigration / employment permits for non-EEA founders, bank account opening procedures (high-level only), full corporate governance and shareholders' agreement drafting, deep sector-specific regulatory licensing beyond signposting, listing on Euronext Dublin / ISEQ, and Irish Collective Asset-management Vehicles (ICAV). ALWAYS read this skill before advising on Irish entity formation."
jurisdiction: IE
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ie-formation

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Ireland (Éire) |
| Currency | EUR (Euro) |
| Company registrar | Companies Registration Office (CRO) |
| Tax authority | Office of the Revenue Commissioners |
| Beneficial ownership register | Central Register of Beneficial Ownership of Companies and Industrial and Provident Societies (RBO) |
| Key legislation | Companies Act 2014 (consolidated since 1 June 2015); Finance Act (annual); Taxes Consolidation Act 1997 (TCA 1997); Investment Limited Partnerships Act 1994 (as amended by ILPA 2020); Limited Partnerships Act 1907; Charities Act 2009; Data Protection Act 2018 |
| Registration portal | CORE — Companies Online Registration Environment (core.cro.ie) |
| Typical formation time | 5–10 working days for LTD via CORE; 1–2 days for ordinary Business Name (RBN1); 3–6 weeks for PLC; 4–8 weeks for CLG; 2–4 weeks for DAC |
| Standard corporate tax rate (CT) | 12.5% on trading income; 25% on non-trading (passive) income; 15% top-up under Pillar Two for in-scope groups with consolidated revenue ≥ €750M |
| VAT rate | 23% standard; 13.5% reduced; 9% second reduced (hospitality / hairdressing where applicable); 0% zero rate; 4.8% livestock |
| CRO online incorporation fee | €50 via CORE (€100 paper) |
| Skill version | 1.0 |

## Section 2 — Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Trader | Partnership (1890 Act) | LP / LLP | LTD (CLS) | DAC | CLG | PLC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Legal personality | No | No | LP: No; ILP / LLP: Yes | Yes | Yes | Yes | Yes |
| Liability | Unlimited personal | Unlimited joint and several | LP: limited partners limited / general partners unlimited; ILP / LLP: limited | Limited to share capital | Limited to share capital | Limited by guarantee (no shares) | Limited to share capital |
| Min. founders / members | 1 | 2 | LP: 1 general + 1 limited; ILP: 1 general + 1 limited | 1 (single-member possible) | 1 | 1 | 1 (post-2014 Act; was 7) |
| Max. members | n/a | 20 (50 for accountancy partnerships; unlimited for solicitors) | LP: 20 (limited partners); ILP / LLP: no cap | 149 | 149 | Unlimited | Unlimited |
| Min. directors | n/a | n/a | n/a | 1 (LTD only — unique to the CLS form) | 2 | 2 | 2 |
| Company secretary | n/a | n/a | n/a | Required (may be the sole director if there is a separate secretary, or a second director may serve as secretary) | Required | Required | Required |
| EEA-resident director requirement | n/a | n/a | n/a | At least one director must be EEA-resident OR the company must hold a Section 137 bond | Same as LTD | Same as LTD | Same as LTD |
| Min. share capital | n/a | n/a | n/a | None statutory (commonly €100 issued) | None statutory | n/a (limited by guarantee) | €25,000 minimum issued share capital; 25% paid up (€6,250) |
| Audit exemption available | n/a | n/a | n/a (LLP audit rules apply separately) | Yes if small company criteria met | Yes if small company criteria met | Yes if small company criteria met (one-member CLG cannot avail) | No |
| Annual filing with CRO | None (Business Name renewal every 3 years if RBN1 registered) | Generally none unless registered as a Business Name | LP / ILP: annual return; LLP: annual return | Annual Return (Form B1) + financial statements | Same as LTD | Same as LTD | Same as LTD; PLC accounts always audited |
| Tax treatment | Income tax via Form 11 self-assessment | Pass-through to partners; each partner files Form 11 | LP: pass-through; ILP: pass-through (transparent); LLP: pass-through unless elects otherwise | Corporation Tax 12.5% trading / 25% non-trading | Same as LTD | CT 12.5% / 25% but typically charitable / not-for-profit exemption available | Same as LTD |
| Suffix on name | None | None | "LP" / "ILP" / "LLP" | "Limited" / "Ltd" / "Teoranta" / "Teo" | "Designated Activity Company" / "DAC" / "Cuideachta Ghníomhaíochta Ainmnithe" / "CGA" | "Company Limited by Guarantee" / "CLG" / "Cuideachta faoi Theorainn Ráthaíochta" / "CTR" | "Public Limited Company" / "PLC" / "Cuideachta Phoiblí Theoranta" / "CPT" |
| Admin burden | Low | Low | Medium | Medium | Medium | Medium | High |

**Recommended defaults:**

- Solo founder, micro turnover, low-risk activity, comfortable with unlimited liability: **Sole Trader** with optional RBN1 business name registration.
- Solo or small group founder, wanting limited liability and trading income at 12.5% CT: **LTD (Company Limited by Shares — CLS)**.
- Joint venture or special-purpose vehicle where objects clause must be restricted: **DAC**.
- Non-profit / charity / sports club / management company for residential developments: **CLG**.
- Plans to raise public capital or list on Euronext Dublin: **PLC**.
- Professional services partnership (solicitors, accountants): general **Partnership** under the Partnership Act 1890 or, where statute permits, an **LLP** (e.g., solicitors' LLPs under the Legal Services Regulation Act 2015).

### When to use each

- **LTD** — Default SME, owner-managed, single or small group
- **DAC** — Joint venture, SPV, securitisation under s.110, regulated entity requiring objects clause
- **CLG** — Non-profit, club, OMC for residential development, charity (with separate Charities Regulator registration)
- **PLC** — Public capital raise, Euronext Dublin listing, large groups with public shareholding

## Section 3 — Required Inputs and Refusal Catalogue

### Required intake before recommending an entity

- **Intake checklist** — 1. Nationality and residence of each founder (EEA vs non-EEA matters for the Section 137 bond rule). 2. Number of founders / promoters. 3. Intended business activity (objects) and NACE Rev. 2 code. 4. Expected annual turnover and profit base (drives small-company exemptions, VAT registration, and audit thresholds). 5. Whether any non-EEA director is involved (Section 137 bond €25,000 OR appoint an EEA-resident director). 6. Capital available for paid-up share capital (PLC has a €25,000 minimum issued share capital floor). 7. Whether the business will hire employees (PAYE / PRSI / USC employer registration with Revenue via ROS). 8. Whether the business handles personal data (GDPR / Data Protection Act 2018 — DPC registration where applicable). 9. Whether the business will trade in regulated areas (financial services → Central Bank of Ireland; broadcasting → Coimisiún na Meán; aviation → IAA; medicines → HPRA). 10. PPS numbers of all directors and shareholders (mandatory at incorporation since the 11 June 2023 CRO change).

### Refusal catalogue

- **R-IE-F1 — Nominee directors used to evade Section 137** — Appointing a 'shadow' EEA-resident nominee director purely to satisfy the Section 137 EEA-residency requirement, with no genuine governance role, is not advised. The CRO and Revenue treat this as a substance failure and the bond route is the lawful alternative. The skill will not draft or advise on sham nominee arrangements.  _(R-IE-F1)_
- **R-IE-F2 — Tax-avoidance entity selection** — Recommending a particular entity primarily to obtain a tax-residence mismatch (e.g., Irish-incorporated but managed from a no-tax jurisdiction to fall outside Irish CT) is refused. Since the 2014–2015 Double Irish reform and the central management and control / incorporation tests under TCA 1997 s.23A, all Irish-incorporated companies are Irish tax resident unless treaty-resident elsewhere. The skill refuses to structure around this.  _(R-IE-F2; TCA 1997 s.23A)_
- **R-IE-F3 — Regulated sectors: banking, insurance, investment firms, payment institutions, e-money, crypto-asset service providers** — These require Central Bank of Ireland authorisation under the relevant statutes (Central Bank Act 1971; Insurance Acts; IFR / IFD; PSD2 / E-Money Regulations; MiCA from 30 December 2024). Capital floors are much higher than the CRO minimums. Formation alone is insufficient — the skill refuses to provide a green-light recommendation without mapping the sectoral licence.  _(R-IE-F3)_
- **R-IE-F4 — Immigration and employment permits** — Non-EEA founders moving to Ireland to run the business require an appropriate immigration permission (Stamp 0, Stamp 1, Stamp 4, Start-up Entrepreneur Programme — STEP, or Immigrant Investor Programme — IIP closed since 15 February 2023). The skill flags the requirement but does not handle Department of Justice or INIS / ISD filings. Engage an immigration practitioner.  _(R-IE-F4)_
- **R-IE-F5 — Charitable status** — Registering a CLG does NOT itself confer charitable status. A separate application to the Charities Regulator under the Charities Act 2009 is required for CHY tax exemption from Revenue. The skill refuses to imply charitable tax relief follows automatically from CLG incorporation.  _(R-IE-F5; Charities Act 2009)_
- **R-IE-F6 — Sole Trader vs LTD switching for tax arbitrage** — Switching to an LTD purely to access the 12.5% CT rate while retaining all profits personally as drawings — without genuine corporate substance, retained earnings, or a defensible commercial rationale — risks the close-company surcharge under TCA 1997 s.440 (20% surcharge on undistributed investment / professional services income) and may be challenged under the general anti-avoidance rule (TCA 1997 s.811C). The skill will document substance and apply conservative defaults.  _(R-IE-F6; TCA 1997 s.440; s.811C)_
- **R-IE-F7 — Bank account opening for non-resident founders** — Irish pillar banks require directors to attend in person or appoint a properly notarised attorney for KYC under the Criminal Justice (Money Laundering and Terrorist Financing) Act 2010 (as amended). The skill flags the requirement but does not guarantee any specific bank's onboarding. Fintech alternatives (Revolut Business, N26 Business, Wise Business) have lighter onboarding but more limited treasury features.  _(R-IE-F7; Criminal Justice (Money Laundering and Terrorist Financing) Act 2010)_

### Sole Trader

- **Sole Trader** — A Sole Trader is an individual carrying on business in their own name (or under a registered business name) with no separate legal personality. Profits are taxed as Schedule D Case I (trading) or Case II (professions) income under the Taxes Consolidation Act 1997 (TCA 1997).  _(TCA 1997)_

#### Key features

- **Sole Trader key features** — - No CRO incorporation required. - If trading under any name other than the proprietor's own true name, the proprietor must register a Business Name with the CRO using Form RBN1 within one month of commencing business (Business Names Act 1963). Renewal every three years is not required — a Business Name registration persists until ceased — but changes must be notified within one month using Form RBN3. - PPS Number required for Revenue registration. - Income tax via the self-assessment system on Form 11 (paper) or via ROS (Revenue Online Service) for mandatory e-filers. - PRSI Class S at 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 (rate increased from 4% to 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 with effect from 1 October 2024 under Budget 2025) on reckonable income, minimum annual contribution €650. - USC at progressive rates (0.5% / 2% / 3% / 8% / 11% surcharge bands for 2025). - VAT registration threshold from 1 January 2025: €42,500 for services and €85,000 for goods. - No limited liability — personal assets exposed.  _(Business Names Act 1963)_

#### Formation steps

- **Sole Trader formation steps** — 1. Obtain a PPS Number (Department of Social Protection) if the founder does not have one. 2. Register a Business Name with the CRO via CORE using RBN1 if trading under any name other than the proprietor's real name. Fee €20 online / €40 paper. Issued within 1–2 working days. 3. Register with Revenue for Income Tax via the eRegistration module on ROS, or paper TR1 if not eligible for ROS. 4. Register for VAT (TR1) once the relevant threshold is breached or where intra-EU acquisitions or reverse-charge services trigger compulsory registration. 5. Register as an Employer (PAYE / PRSI / USC) if hiring staff. 6. Register for Relevant Contracts Tax (RCT) if operating in construction, forestry, or meat processing.

#### Tax

- **Sole Trader tax** — - Schedule D Case I / II profits at marginal income tax rates (20% standard / 40% higher band for 2025); standard rate cut-off €44,000 single / €53,000 single parent / €88,000 married jointly assessed (verify against Finance Act 2024 schedule). - PRSI Class S 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 (post 1 October 2024 rate). - USC 0.5% / 2% / 3% / 8%; 11% surcharge on self-employed income above €100,000. - Preliminary tax due 31 October each year (or extended ROS deadline mid-November).  _(Finance Act 2024)_

#### When to use

- **When to use Sole Trader** — - Single founder with micro turnover, low risk, no employees beyond the founder. - Testing a business idea before committing to incorporation. - Side-hustle alongside PAYE employment.

#### When to avoid

- **When to avoid Sole Trader** — - Liability-sensitive activities (consulting with errors-and-omissions exposure, products with safety risk). - Plans to bring in equity investors. - Profits expected to materially exceed the founder's living needs (corporate retention of profits at 12.5% CT beats sole-trader marginal taxation at 40% + 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 PRSI + 8–11% USC).

### Partnership (1890 Act)

- **Partnership (1890 Act)** — A general partnership of two or more persons carrying on business in common with a view to profit under the Partnership Act 1890. No separate legal personality. Each partner has joint and several unlimited liability for partnership debts. - Partnership tax: pass-through — each partner files their own Form 11 with their share of partnership profit; the partnership itself files Form 1 (Firms) annually as an information return. - A partnership trading under any name other than the partners' real surnames must register the Business Name with the CRO via RBN1A. - Maximum 20 partners (or 50 for accountancy firms; unlimited for solicitors under specific statutes). - Where a partnership wishes to limit liability, it can re-form as an LP (Limited Partnerships Act 1907) or, for solicitors, an LLP under the Legal Services Regulation Act 2015 Part 7.  _(Partnership Act 1890)_

### Limited Partnership (LP) and Investment Limited Partnership (ILP)

- **LP and ILP** — - LP under the 1907 Act: rarely used outside fund structuring. At least one general partner with unlimited liability and at least one limited partner whose liability is capped at their capital contribution. No separate legal personality. - ILP under the Investment Limited Partnerships Act 1994 (as amended by the ILPA 2020): a regulated investment fund vehicle authorised by the Central Bank of Ireland. Separate legal personality (post-2020 reform). Out of scope for general SME formation — see R-IE-F3 if proposed for use as a fund vehicle. - LLP for solicitors: under the Legal Services Regulation Act 2015, solicitors' practices can authorise themselves as LLPs with the Legal Services Regulatory Authority (LSRA). Limited to solicitors' practices currently.  _(Investment Limited Partnerships Act 1994; ILPA 2020; Limited Partnerships Act 1907; Legal Services Regulation Act 2015)_

### Nature

- **LTD nature** — The LTD (Company Limited by Shares — also called a CLS) is the dominant SME vehicle, introduced as a new model company type by the Companies Act 2014 (commenced 1 June 2015). It replaced the pre-2015 "private company limited by shares" and is now the default form for most Irish SMEs.  _(Companies Act 2014)_

### Distinctive features (post-Companies Act 2014)

- **LTD distinctive features** — - Single director permitted (must then have a separate company secretary — unique to the LTD form). - One-member company permitted. - No objects clause — the LTD has the full and unlimited contractual capacity of a natural person under section 38 CA 2014. This is a deliberate simplification that distinguishes the LTD from the DAC. - No authorised share capital required in the constitution (the LTD has the power to issue shares up to whatever its members authorise; the older concept of nominal / authorised share capital is gone for the LTD form). - Single-document constitution (no separate Memorandum and Articles). - May dispense with holding an AGM where all members agree in writing (s.175 CA 2014). - Maximum 149 members.  _(Companies Act 2014 s.38; s.175)_

### Founders, members, and directors

- **LTD founders, members, directors** — - Minimum 1 member and 1 director. - Maximum 149 members. - At least one director must be EEA-resident OR the company must hold a Section 137 bond (an insurance bond of €25,000 for two years, available from specialist providers). The EEA includes the EU 27 plus Iceland, Liechtenstein, and Norway; post-Brexit, UK-resident directors no longer satisfy this rule. - Company Secretary required. If the company has only one director, the secretary must be a different person. If the company has two or more directors, one of them may also act as secretary. - PPS Numbers for all directors mandatory at incorporation since the CRO change of 11 June 2023. A non-resident director without a PPS Number must obtain a Verified Identity Number (VIN) via the CRO's identity verification process.  _(Companies Act 2014)_

### Capital

- **LTD capital** — - No statutory minimum issued share capital (commonly €100 issued at €1 per share for a single-member LTD; CRO accepts any positive amount). - Stamp duty on share capital was abolished for shares issued by Irish companies under the Stamp Duty (Designation of Certain Other Bonds as Loan Capital) Order — i.e., subscription for new shares does not attract stamp duty in Ireland. - Stamp duty at 1% applies to transfers of shares in Irish companies under the Stamp Duties Consolidation Act 1999.  _(Stamp Duties Consolidation Act 1999)_

### Governance

- **LTD governance** — - Board of directors (one or more). - Members' meetings: an LTD may dispense with the AGM by unanimous written resolution (s.175 CA 2014) — useful for single-member LTDs. - Statutory registers: register of members, register of directors and secretaries, register of beneficial owners (RBO), register of directors' interests in shares, minute books.  _(Companies Act 2014 s.175)_

### Formation steps

- **LTD formation steps** — 1. Choose a name and search the CRO register via CORE. Reserved names cannot conflict with existing companies or business names; CRO can refuse names that are too similar, contain restricted words ("Bank", "Insurance", "Society", "University"), or imply state sponsorship. 2. Prepare a single-document Constitution (CRO model Constitution acceptable for most LTDs). 3. Complete Form A1 online via CORE covering: company name, type (LTD), registered office, directors, secretary, members, share allotment, NACE code, beneficial owners. 4. Provide PPS Numbers for all directors. Non-PPS directors must complete the VIF (Verification of Identity Form) process and obtain a VIN. 5. Pay CRO filing fee €50 (CORE) or €100 (paper Form A1). 6. CRO reviews; if accepted, issues the Certificate of Incorporation with the company number (CRO number) typically within 5–10 working days. 7. TIN equivalent — Tax Reference Number (TRN) is not automatic in Ireland: the company must register with Revenue via eRegistration on ROS or paper Form TR2 for Corporation Tax, VAT, Employer PAYE / PRSI, and RCT as applicable. 8. Register beneficial owners with the RBO within 5 months of incorporation (see Section 8). 9. Open a corporate bank account — pillar banks typically require in-person attendance by all directors and beneficial owners with original IDs and proof of address. 10. Sector licences where applicable (see Section 7).

### Tax

- **Corporation Tax (CT) rates** — 12.5% on trading income (Schedule D Case I / II); 25% on non-trading income (passive: rents, dividends from non-EEA / non-treaty sources, investment income, foreign-source income); 33% Capital Gains Tax on chargeable gains (effective 33% via s.78 CTCA mechanism); 15% Pillar Two top-up (Qualified Domestic Top-up Tax) for in-scope multinational groups with consolidated revenue ≥ €750M %  _(TCA 1997; EU Pillar Two Directive (Directive (EU) 2022/2523); Part 4A TCA 1997; Finance (No. 2) Act 2023; effective for accounting periods beginning on or after 31 December 2023)_
- **Close-company surcharge** — Close-company surcharge (s.440 TCA 1997): a 20% surcharge on undistributed investment and rental income of a close company; a higher surcharge applies to undistributed professional services income of a close service company (s.441) — relevant for one-person LTDs providing services.  _(TCA 1997 s.440; s.441)_
- **R&D Tax Credit** — 30% credit (rate increased from 25% with effect from accounting periods commencing on or after 1 January 2024 under Finance (No. 2) Act 2023) of qualifying R&D expenditure, payable in three instalments. The first instalment threshold was raised to €75,000 under Budget 2025. %  _(TCA 1997 s.766; Finance (No. 2) Act 2023; Budget 2025)_
- **Knowledge Development Box (KDB)** — 6.25% effective rate on qualifying IP income — relevant for software, pharma, and biotech. The KDB sunset was extended by Finance Act 2022 to accounting periods commencing before 1 January 2027. %  _(TCA 1997 s.769G–s.769R; Finance Act 2022)_
- **Start-up Relief for Entrepreneurs (Section 486C)** — New trading companies in their first 3 years may obtain CT relief reducing CT liability up to €40,000 per year, tapered to €60,000, where employer's PRSI payable in the year does not exceed €40,000 (extended through 2026 by Finance Act 2023).  _(TCA 1997 s.486C; Finance Act 2023)_
- **VAT registration thresholds** — €42,500 services / €85,000 goods from 1 January 2025
- **Employer PRSI Class A1** — 11.15% Jan-Sep 2025; 11.25% from 1 Oct 2025 on standard rate band — sub-class A1; lower employer rates for low-earnings sub-classes %
- **Capital allowances** — Plant and machinery 12.5% straight-line over 8 years; industrial buildings 4% over 25 years; accelerated allowances for energy-efficient equipment (s.285A) and certain green vehicles.  _(TCA 1997 s.285A)_
- **Annual filings** — - Annual Return (Form B1) to CRO with an annual return date (ARD) set on incorporation, typically 6 months after the company's first anniversary then annually. Late filing carries €100 late fee + €3/day to a maximum of €1,200 and loss of audit exemption for two years. - Statutory financial statements filed with the B1 (small company abridged accounts acceptable where small-company criteria met). - Corporation Tax return (Form CT1) to Revenue within 8 months and 23 days of the accounting period end (filed via ROS), with preliminary CT due as follows: small companies (CT liability ≤ €200,000 in prior year) pay 100% of prior-year liability OR 90% of current-year liability by the 23rd of the month before the period end; large companies pay 45% by month 6 day 23 and a top-up to 90% by month 11 day 23.

### When to use

- **When to use LTD** — - Most SMEs including freelance software developers, consultancies, e-commerce, light manufacturing. - Anyone wanting limited liability, the 12.5% trading CT rate, and access to R&D Tax Credit, KDB, or Start-up Relief for Entrepreneurs. - Founders planning to raise equity later (clean corporate structure, audited or unaudited accounts).

### When to avoid

- **When to avoid LTD** — - Pure micro / informal side-hustle activity where Sole Trader suffices. - NGO / charitable purposes — use CLG. - Joint ventures where parties want a restricted objects clause and enhanced statutory protections — consider DAC.

### DAC (Designated Activity Company)

- **DAC** — - A DAC is a private company that retains an objects clause in its constitution. Used where the company's legal capacity must be restricted — for example, joint ventures, special-purpose vehicles for securitisation, or where a regulatory regime requires an objects clause. - Two types: DAC limited by shares (the more common) and DAC limited by guarantee with a share capital (rare). - Minimum 2 directors (the LTD's single-director regime is not available to a DAC). - Company secretary required (may be one of the directors). - Maximum 149 members. - Two-document constitution: Memorandum (objects) + Articles. - Suffix: "Designated Activity Company" / "DAC" / Irish equivalents. - CRO filings, tax treatment, and audit exemption mirror the LTD where small-company criteria met. - Used in regulated finance (some Central Bank-authorised entities are required to be DACs), securitisation SPVs under TCA 1997 s.110, and joint ventures where parties demand an explicit objects clause.  _(TCA 1997 s.110)_

### CLG (Company Limited by Guarantee, without share capital)

- **CLG** — - A CLG has no share capital; members give a guarantee to contribute a nominal amount (typically €1) on winding up. - Used for non-profits, sports clubs, professional associations, owners' management companies (OMCs) for multi-unit developments under the Multi-Unit Developments Act 2011, residents' associations, charities. - Minimum 2 directors; company secretary required. - Two-document constitution. - Single-member CLG permitted but cannot avail of audit exemption. - Suffix: "Company Limited by Guarantee" / "CLG" / Irish equivalent. - Charitable status is separate from CLG incorporation: a CLG seeking charitable tax exemption must register with the Charities Regulator under the Charities Act 2009 and obtain a CHY number from Revenue (TCA 1997 s.207 / s.208 charitable tax exemption). See R-IE-F5. - CT treatment: 12.5% on any trading income (rare for a genuine non-profit) and 25% on non-trading income, unless charitable tax exemption applies, in which case income applied for charitable purposes is exempt.  _(Multi-Unit Developments Act 2011; Charities Act 2009; TCA 1997 s.207; s.208)_

### PLC (Public Limited Company)

- **PLC** — - A PLC may offer shares to the public and may list on Euronext Dublin (formerly ISEQ) or remain unlisted. - Minimum 1 member (changed by CA 2014 — previously 7); minimum 2 directors; company secretary required (and the secretary must have appropriate qualifications under s.129 CA 2014). - Minimum issued share capital €25,000, of which at least 25% (€6,250) paid up at incorporation. - Two-document constitution. - Audit always mandatory (PLCs cannot avail of the small-company audit exemption). - Suffix: "Public Limited Company" / "PLC" / Irish equivalent. - Listing additionally requires Euronext Dublin Listing Rules compliance, Central Bank approval of the prospectus under the Prospectus Regulation (EU) 2017/1129 as transposed by SI 380/2019, and ongoing disclosure obligations under the Transparency Regulations (SI 277/2007). - CT treatment: 12.5% trading / 25% non-trading, with Pillar Two top-up where group consolidated revenue ≥ €750M.  _(Companies Act 2014 s.129; Prospectus Regulation (EU) 2017/1129; SI 380/2019; SI 277/2007)_

### When to use each

**When to use each vehicle**

| Vehicle | Use case |
| --- | --- |
| LTD | Default SME, owner-managed, single or small group |
| DAC | Joint venture, SPV, securitisation under s.110, regulated entity requiring objects clause |
| CLG | Non-profit, club, OMC for residential development, charity (with separate Charities Regulator registration) |
| PLC | Public capital raise, Euronext Dublin listing, large groups with public shareholding |

## Section 7 — Sector-Specific Licences (Signposting Only)

CRO registration is necessary but not sufficient for regulated activities. Common sector licences:

**Sector-specific licences**

| Sector | Regulator | Typical authorisation |
| --- | --- | --- |
| Banks, credit institutions | Central Bank of Ireland (CBI) | Banking licence under Central Bank Act 1971; subject to ECB Single Supervisory Mechanism for significant institutions |
| Insurance and reinsurance | Central Bank of Ireland | Authorisation under European Union (Insurance and Reinsurance) Regulations 2015 (Solvency II) |
| Investment firms | Central Bank of Ireland | Authorisation under European Union (Markets in Financial Instruments) Regulations 2017 (MiFID II) |
| Fund managers (UCITS / AIFMD) | Central Bank of Ireland | UCITS ManCo or AIFM authorisation |
| Payment institutions and e-money | Central Bank of Ireland | Authorisation under European Union (Payment Services) Regulations 2018 (PSD2) or European Communities (Electronic Money) Regulations 2011 |
| Crypto-asset service providers | Central Bank of Ireland | MiCA authorisation under Regulation (EU) 2023/1114 with effect from **30 December 2024**; transitional regime for VASPs registered under the Criminal Justice (Money Laundering and Terrorist Financing) (Amendment) Act 2021 |
| Consumer credit, retail credit, credit servicing | Central Bank of Ireland | Authorisation under the Consumer Credit Act 1995 / Central Bank Act 1997 |
| Competition / merger control | Competition and Consumer Protection Commission (CCPC) | Mandatory pre-merger notification under the Competition Act 2002 (as amended by the Competition (Amendment) Act 2022) where worldwide turnover exceeds €60M and Irish turnover of each of at least two parties exceeds €10M |
| Data protection | Data Protection Commission (DPC) | Registration not generally required, but mandatory DPO appointment under GDPR Articles 37–39 for public authorities and certain large-scale processors; controllers and processors must comply with GDPR + Data Protection Act 2018 |
| Telecommunications | Commission for Communications Regulation (ComReg) | General authorisation or specific licence under the European Communities (Electronic Communications Networks and Services) Regulations 2011 |
| Broadcasting and audiovisual media services | Coimisiún na Meán (Media Commission, established by the Online Safety and Media Regulation Act 2022) | Broadcasting contract or video-on-demand service registration |
| Pharmaceuticals and medical devices | Health Products Regulatory Authority (HPRA) | Manufacturer's authorisation, wholesale distribution authorisation, marketing authorisation |
| Food | Food Safety Authority of Ireland (FSAI) and HSE Environmental Health Officers | Food business registration; HACCP compliance |
| Alcohol | Revenue Commissioners (excise) and District Court (publican's / off-licence licences) | Excise licence + court licence |
| Childcare | Tusla (Child and Family Agency) | Early Years Service registration under the Child Care Act 1991 (Early Years Services) Regulations 2016 |
| Healthcare facilities | Health Information and Quality Authority (HIQA) | Registration of designated centres for older persons, disability services, and residential children's services |
| Aviation | Irish Aviation Authority (IAA) | Air operator certificate, ground handling licence |
| Maritime / shipping | Department of Transport and Marine Survey Office | Various certificates under the Mercantile Marine Act 1955 |
| Construction (energy, water, environmental) | Various: Sustainable Energy Authority of Ireland (SEAI), Irish Water (Uisce Éireann), EPA | Sector-specific permits |
| Gambling and gaming | Gambling Regulatory Authority of Ireland (GRAI, established under the Gambling Regulation Act 2024) | Betting / gaming licence as the GRAI's licensing regime is phased in from 2025–2026 |

All Irish controllers and processors of personal data are subject to GDPR (Regulation (EU) 2016/679) as supplemented by the Data Protection Act 2018. Mandatory Data Protection Officer (DPO) appointment applies for public authorities and processors engaged in large-scale systematic monitoring or large-scale processing of special-category data (GDPR Article 37). The DPC supervises and enforces. Tech founders should treat GDPR compliance as part of formation — a documented Record of Processing Activities (Article 30), privacy notices (Article 13/14), and a data breach response procedure are baseline.

### Statutory basis

- **RBO statutory basis** — The Central Register of Beneficial Ownership of Companies and Industrial and Provident Societies ("RBO") is maintained by the CRO under the European Union (Anti-Money Laundering: Beneficial Ownership of Corporate Entities) Regulations 2019 (SI 110/2019), transposing the EU's Fourth Anti-Money Laundering Directive (Directive (EU) 2015/849) as amended by the Fifth AMLD.  _(SI 110/2019; Directive (EU) 2015/849)_

### Scope

- **RBO scope** — Applies to every Irish-incorporated company (LTD, DAC, CLG, PLC, ULC, unlimited companies) and every industrial and provident society. Does not apply to: - Listed companies subject to disclosure rules of an EEA regulated market (exemption under Regulation 4(1)). - Companies in liquidation in certain circumstances. - Branches of foreign companies (which file with CRO under a separate regime).  _(Regulation 4(1))_

### Beneficial owner definition

- **Beneficial owner** — A natural person who ultimately owns or controls the entity through direct or indirect ownership of more than 25% of the shares or voting rights, or through control via other means. Where no natural person meets the 25% test (e.g., widely held company), the senior managing officials (typically the directors) are recorded as beneficial owners by default.

### Filing obligations

- **RBO filing obligations** — - Initial filing within 5 months of incorporation via rbo.gov.ie (the dedicated RBO portal, separate from CORE). - Update within 14 days of any change in beneficial ownership or particulars. - Each beneficial owner must provide: full name, date of birth, nationality, residential address, PPS Number (used solely for identity verification — not displayed on the public extract), nature and extent of the beneficial interest, dates of acquisition and cessation. - Filings are made online only (no paper option); the beneficial owner does not personally sign — the presenter (typically the company secretary or an authorised filer) submits on behalf of the company.

### Public access

- **RBO public access** — The RBO is publicly accessible on a restricted basis following the CJEU judgment in Joined Cases C-37/20 and C-601/20 (Luxembourg Business Registers, 22 November 2022) which struck down general public access. Since then, access is limited to: - Competent authorities (Garda, Revenue, CBI, CAB). - Designated persons under AML legislation (when carrying out customer due diligence). - Members of the public with a demonstrable "legitimate interest" (typically journalists, NGOs, academics investigating money laundering / terrorist financing risks).  _(CJEU Joined Cases C-37/20 and C-601/20 (22 November 2022))_

### Penalties

- **RBO penalties** — - Failure to file: summary conviction class A fine up to €5,000; on indictment fine up to €500,000. - Failure to maintain own internal beneficial ownership register at the company's registered office: same scale. - The company and the responsible officer (typically each director) can both be prosecuted.

### Operational tip

For a single-member LTD where the sole shareholder is the sole director, the RBO filing is straightforward: one beneficial owner (the founder), 100% shareholding, identified by PPS Number. Allow 1–2 hours including portal account creation.

## Section 9 — CRO Registration Process (CORE Portal)

CRO registration is fully electronic through the CORE (Companies Online Registration Environment) portal at core.cro.ie. Paper Form A1 remains available but at higher fee and longer turnaround.

### Standard LTD workflow

- **Standard LTD workflow** — 1. CORE account creation. Each presenter (typically the founder, accountant, or formation agent) creates a CORE account. 2. Name availability search. Submit a proposed name via CORE's name search. Reservation valid 28 days. Restricted words ("Bank", "Insurance", "Society", "University", "Group", "Holding") require evidence of authorisation. Names too similar to existing companies / business names will be refused. 3. Constitution preparation. Draft a single-document Constitution for the LTD (CRO's model Constitution acceptable for the vast majority of LTDs). For DAC, CLG, or PLC, use the two-document Memorandum + Articles format. 4. Form A1 completion. Online form covering: company name, type (LTD / DAC / CLG / PLC / ULC), registered office address (must be a physical Irish address — PO boxes not acceptable), directors (with PPS Number or VIN), secretary, members and shareholding, share capital and allotment (LTD / DAC / PLC), NACE Rev. 2 activity code, ultimate beneficial owners (for RBO purposes), Section 137 bond reference if no EEA-resident director. 5. Document upload. Signed Constitution, statutory declaration of compliance (s.21(2) CA 2014), Section 137 bond (if applicable), VIF / VIN evidence for non-PPS directors. 6. Payment. €50 CORE filing fee (€100 paper Form A1). No stamp duty on subscription for new shares. 7. CRO review. 5–10 working days for routine LTD; longer for DAC / CLG / PLC. Expedited examination available at additional fee in some cases. 8. Certificate of Incorporation. Issued electronically with CRO number; available for download via CORE. 9. Tax Reference Number (TRN) — NOT automatic. Unlike Nigeria's CAC / FIRS integration, the Irish CRO does NOT automatically issue a TRN. The company must separately register with Revenue via eRegistration on ROS or paper Form TR2 (see Section 10). 10. RBO filing. Within 5 months of incorporation, file the company's beneficial owners via rbo.gov.ie (see Section 8).  _(Companies Act 2014 s.21(2))_

### Business Name (RBN1) workflow for sole traders and partnerships

- **RBN1 workflow** — 1. Determine that registration is required (trading under a name other than your real name). 2. Complete RBN1 (sole trader) / RBN1A (partnership) / RBN1B (body corporate) via CORE. 3. Fee €20 online / €40 paper. 4. Issued within 1–2 working days. 5. Display the registered name on business letterhead, premises, and invoices (s.18 Business Names Act 1963).  _(Business Names Act 1963 s.18)_

### Common pitfalls

- Section 137 EEA-residency: founders forget that post-Brexit a UK-resident director no longer satisfies the rule. Either appoint an EEA-resident director or arrange the €25,000 two-year bond.
- PPS Number / VIN gap: all directors must have a PPS Number or a CRO-issued VIN since 11 June 2023. Non-resident directors without a PPS Number must allow 4–6 weeks to obtain a VIN via the CRO identity verification process.
- Registered office vs business address confusion: the registered office must be a physical Irish address where statutory documents can be served. Many SMEs use their accountant's address — acceptable but the accountant must agree.
- Constitution drafted with objects clause for an LTD: an LTD must NOT have an objects clause. If the founders want one, they need a DAC.
- Company secretary same as sole director: if the company has only one director, the secretary must be a different person. Single-director / single-secretary LTDs need two distinct individuals.

### Revenue Online Service (ROS)

- **ROS registration forms** — After CRO incorporation (companies) or commencement of business (sole traders / partnerships), the entity must register for the applicable Irish taxes via Revenue: - Form TR1: Sole traders, partnerships, trusts, and unincorporated bodies — Income Tax / VAT / Employer PAYE-PRSI / RCT. - Form TR1 (FT): Foreign sole traders and partnerships. - Form TR2: Companies — Corporation Tax / VAT / Employer PAYE-PRSI / RCT. - Form TR2 (FT): Foreign-incorporated companies trading in Ireland. Preferred method is eRegistration via ROS rather than paper. Companies must first obtain a ROS Digital Certificate for the company once a TRN is issued.

### Tax registrations

- **Tax registrations** — - Corporation Tax (companies): register from incorporation; first CT1 return due 8 months 23 days after first accounting period end. - Income Tax (sole traders / partnerships): register from commencement of trade; first Form 11 due by 31 October of the year following the year of assessment (extended ROS deadline mid-November typically). - Value Added Tax: register where compulsory (turnover > €42,500 services / €85,000 goods from 1 January 2025, or any intra-EU acquisitions / reverse-charge supplies, or distance sales above the OSS / IOSS thresholds). - Employer PAYE-PRSI: register before paying any salary; payroll runs in real time under PMOD (PAYE Modernisation) with submissions on or before each payday via ROS. - Relevant Contracts Tax (RCT): register if the entity is a "principal contractor" in construction, forestry, or meat processing under TCA 1997 Part 18 Chapter 2. - Subcontractor RCT: separate registration where the entity is a subcontractor.  _(TCA 1997 Part 18 Chapter 2)_

### Sundry registrations

- **Sundry registrations** — - Revenue MyEnquiries / ROS Inbox: enable for digital correspondence. - CSO (Central Statistics Office): VAT-registered traders engaging in intra-EU trade above the Intrastat thresholds (arrivals €500,000 / dispatches €635,000 from 2025) must file Intrastat returns. - Department of Social Protection — Employer registration: triggered automatically by Revenue Employer PAYE-PRSI registration. - WRC (Workplace Relations Commission): not a registration per se, but employers must comply with the Employment (Miscellaneous Provisions) Act 2018, Organisation of Working Time Act 1997, and Payment of Wages Act 1991. - PPS Number for each director and beneficial owner: required by both CRO (since 11 June 2023) and RBO.  _(Employment (Miscellaneous Provisions) Act 2018; Organisation of Working Time Act 1997; Payment of Wages Act 1991)_

## Section 11 — Tax Treatment Comparison

**Tax Treatment Comparison**

| Entity | Income tax regime | Headline rate | Key reliefs and surcharges | Annual filing |
| --- | --- | --- | --- | --- |
| Sole Trader | Income tax (Schedule D Case I / II) | 20% / 40% marginal + PRSI Class S 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 + USC 0.5% / 2% / 3% / 8% (+ 11% surcharge > €100k on non-PAYE income) | Earned income tax credit €2,000 (2025); start-your-own-business relief expired 2018 | Form 11 by 31 October |
| Partnership | Income tax pass-through to partners | Same as sole trader for each partner's share | Same as sole trader | Form 1 (Firms) for partnership + Form 11 for each partner |
| LP | Pass-through | Same as partnership | Same as partnership | Form 1 + partner Form 11s |
| ILP (regulated fund) | Tax-transparent vehicle | n/a — pass-through to investors | Investor-level taxation | Specific to fund regime |
| LLP (solicitors) | Pass-through unless elected | Same as partnership | Same as partnership | Form 1 + partner Form 11s |
| LTD / DAC | Corporation Tax | 12.5% trading / 25% non-trading / 33% CGT effective | Start-up Relief s.486C (up to €40k/yr first 3 years); R&D Tax Credit 30%; KDB 6.25%; Pillar Two QDTT if in scope | Form CT1 by 8 months 23 days after period end; Form B1 annual return to CRO |
| CLG (non-charity) | Corporation Tax | 12.5% trading / 25% non-trading | Same as LTD | CT1 + B1 |
| CLG (charity with CHY) | Charitable exemption on objects-related income | 0% on charitable application; 12.5% / 25% on non-objects trading | TCA 1997 s.207 / s.208 exemption; gift aid not applicable in Ireland; charitable donations scheme s.848A | CT1 (with exemption claim) + B1 + Charities Regulator annual report |
| PLC | Corporation Tax | 12.5% trading / 25% non-trading; Pillar Two 15% top-up if in scope | Same as LTD; quoted-share CGT considerations | CT1 + B1 + audited accounts + listed-company disclosures if listed |

## Section 11 — Tax Treatment Comparison

- **Notes** — - Pillar Two top-up tax (QDTT) under Part 4A TCA 1997 applies to Irish constituent entities of in-scope multinational groups (consolidated revenue ≥ €750M) with effective tax rates below 15%. Out of scope for owner-managed SMEs; flagged here for completeness. - Close-company surcharge under s.440 / s.441 TCA 1997: 20% surcharge on undistributed investment / rental / professional services income retained by an owner-managed LTD beyond 18 months after the period end. Important consideration for service-company LTDs. - CGT at 33% on disposals; Entrepreneur Relief under s.597AA TCA 1997 at 10% rate on qualifying business asset disposals up to a lifetime cap of €1M; Retirement Relief under s.598 / s.599 TCA 1997 on disposals to family or third parties for individuals aged 55+. - VAT rates: 23% standard, 13.5% reduced, 9% second reduced, 4.8% livestock, 0% zero rate. Thresholds €42,500 services / €85,000 goods from 1 January 2025. - PRSI Class S at 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 (post 1 October 2024) for self-employed sole traders and partners; PRSI Class A for employees (employer 8.9% Jan-Sep 2025; 9.0% from 1 Oct 2025 / 11.15% Jan-Sep 2025; 11.25% from 1 Oct 2025 depending on earnings band; employee 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025) — proprietary directors who own more than 50% are Class S, not Class A.  _(Part 4A TCA 1997; TCA 1997 s.440; s.441; s.597AA; s.598; s.599)_

## Section 12 — Worked Example: Solo Software Developer in Dublin

**Scenario.** Aoife, Irish resident, 31, freelance software developer in Dublin. Expects €120,000 gross revenue in 2025, mix of Irish and EU SME clients and one US client. No employees. Home office. Comfortable with corporate substance but cost-conscious.

### Option A — Sole Trader (Schedule D Case II)

- Register a Business Name with CRO ("Aoife Dev Studio") via RBN1; fee €20; 1–2 working days.
- Register with Revenue via eRegistration / TR1 for Income Tax and VAT.
- Profit assumption: €120,000 revenue less €25,000 expenses = €95,000 taxable Case II profit.
- Tax 2025 (single, no children, standard rate cut-off €44,000):
  - Income tax: €44,000 @ 20% = €8,800; €51,000 @ 40% = €20,400. Subtotal €29,200.
  - Less personal credit €2,000 + earned income credit €2,000 = €4,000.
  - Net income tax: €25,200.
  - PRSI Class S: €95,000 × 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 = €3,895.
  - USC: €12,012 @ 0.5% = €60; €13,748 @ 2% = €275; €70,044 @ 8% (rate after €25,760 cumulative threshold; verify against Budget 2025 schedule). Cumulative ~ €6,000.
  - 3% USC surcharge on Case II income above €100,000: not triggered at €95,000.
  - Indicative total: ~€35,000 (≈ 37% effective on €95,000 profit).
- VAT: €120,000 turnover above the €42,500 services threshold — VAT registration mandatory. Charge 23% to Irish / EU B2C customers; reverse charge to EU B2B; export of services to US client outside VAT scope (place of supply rules under VAT Consolidation Act 2010 s.34).
- No corporation tax; no audit; no CRO B1.

### Option B — Private Limited Company (LTD)

- Incorporate "Aoife Dev Studio Limited" via CORE; share capital €100 issued at €1 per share; sole director (Aoife) with separate company secretary (Aoife's spouse or a corporate secretary service).
- CRO fee €50; secretarial / accountant setup fees €400–€800; total all-in ~€500–€900.
- Aoife is EEA-resident (Irish citizen and tax resident) so no Section 137 bond.
- Register with Revenue via eRegistration / TR2 for CT, VAT, Employer PAYE-PRSI.
- File RBO within 5 months — Aoife as 100% beneficial owner.
- Profit assumption: €120,000 revenue less €25,000 business expenses less €60,000 director's salary (gross) = €35,000 corporate profit.
- Corporation tax: €35,000 @ 12.5% = €4,375.
- Director's salary €60,000 taxed via PMOD:
  - Income tax: €44,000 @ 20% + €16,000 @ 40% = €8,800 + €6,400 = €15,200; less PAYE personal credit €2,000 + employee credit €2,000 = €11,200.
  - Employee PRSI Class A: €60,000 × 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 = €2,460 (proprietary directors >50% holding go to Class S — Aoife is 100% so she is Class S, 4.1% Jan-Sep 2025; 4.2% from 1 Oct 2025 as well; net same).
  - USC on €60,000: cumulative ~€2,200.
  - Personal tax burden on €60,000 salary: ~€15,900.
- Total combined tax (Option B): CT €4,375 + personal €15,900 = €20,275, with €35,000 retained in the company (less CT already paid → €30,625 retained after tax).
- Close-company surcharge (s.441): as a service company, undistributed "professional services" income retained beyond 18 months attracts a surcharge — the s.441 surcharge is 15% of half the undistributed estate-and-investment / professional-services income (effective ~7.5% additional on retained professional services income). Aoife should plan distributions or salary uplift to avoid the surcharge. Estimate s.441 exposure on €30,625 retained: ~€2,300/year if undistributed beyond 18 months.
- VAT: same as Option A — mandatory registration; LTD charges VAT, recovers input VAT.
- Annual: Form B1 + small-company abridged accounts to CRO; CT1 to Revenue.

### Recommendation

- The LTD is more tax-efficient on cash-flow when Aoife can leave some profit in the company (e.g., to fund equipment, build a cash buffer, or eventually exploit Entrepreneur Relief s.597AA on exit at 10% CGT instead of 33%).
- The Sole Trader is simpler and cheaper to administer if Aoife intends to spend all the profit each year on personal living costs — in which case the LTD's close-company surcharge erodes most of the saving.
- At €120,000 revenue with material retained profits and a 5–10 year horizon, the LTD wins. At lower revenue (< €70,000) with no retained profits, Sole Trader is usually equivalent or better once you account for accounting fees (€1,500–€3,000/year for an LTD vs €500–€1,000 for a Sole Trader).
- Operational steps for Aoife if she chooses LTD: incorporate via CORE; register with Revenue via TR2; file RBO; engage a payroll provider; set up a SEPA-enabled corporate bank account; register for VAT MOSS / OSS for EU B2C SaaS sales; document her R&D (if any) for the 30% R&D Tax Credit; consider KDB eligibility if she develops original IP.

## Section 13 — Decision Tree

```
Q1: Is at least one founder / proposed director EEA-resident?
  YES → go to Q2
  NO  → can the company obtain a Section 137 bond (€25,000 two-year bond)?
        YES → proceed (Section 137 route); go to Q2
        NO  → defer formation OR appoint an EEA-resident director OR refuse advice (R-IE-F1 — no shams)

Q2: Is the purpose non-profit / charitable / club / OMC / professional association?
  YES → CLG (Company Limited by Guarantee), with separate Charities Regulator registration if charitable status sought
  NO  → go to Q3

Q3: Is this a regulated sector (banking, insurance, investment, payments, e-money, crypto-asset
     under MiCA, broadcasting, telecoms, pharma, gambling)?
  YES → Refuse green-light recommendation; map sectoral licence (R-IE-F3); typically LTD or DAC
        depending on regulator's preferred form
  NO  → go to Q4

Q4: Plans to raise public equity or list on Euronext Dublin within 3 years?
  YES → PLC (minimum issued share capital €25,000; 25% paid up)
  NO  → go to Q5

Q5: Is there a need for a restricted objects clause — e.g., joint venture SPV, securitisation
     vehicle under TCA 1997 s.110, or a regulator requires a DAC?
  YES → DAC (Designated Activity Company)
  NO  → go to Q6

Q6: Solo founder, micro turnover (< €40,000 expected), accept unlimited liability,
     simplicity prized, no plans to retain profits in a corporate vehicle?
  YES → Sole Trader; register Business Name via RBN1 if trading under any name other than
        the founder's real name
  NO  → go to Q7

Q7: Two or more professional partners (solicitors, accountants) wanting pass-through tax
     and informal structure?
  YES → Partnership (1890 Act); consider LLP for solicitors under LSRA 2015
  NO  → go to Q8 (default)

Q8: Default: Private Company Limited by Shares (LTD / CLS) — single-director permitted,
    no objects clause, single-document Constitution, 12.5% trading CT rate, access to
    R&D Tax Credit, KDB, Start-up Relief s.486C, and Entrepreneur Relief on exit.
```

## Section 14 — Conservative Defaults

- **Conservative defaults** — 1. Default entity for a solo Irish-resident founder with corporate substance: Private Company Limited by Shares (LTD / CLS), because the 12.5% trading CT rate combined with Entrepreneur Relief on exit (10% CGT up to €1M lifetime) makes the LTD materially more tax-efficient than a Sole Trader for retained-earnings or exit-driven businesses. 2. Default entity for a micro Irish-resident founder with no corporate ambitions and < €40,000 turnover: Sole Trader with RBN1 if trading under a different name. 3. Default entity for 2+ founders, no foreign capital, owner-managed: Private Company Limited by Shares (LTD). 4. Default entity for any non-EEA founder/director: Private Company Limited by Shares (LTD) plus Section 137 bond OR appointment of an EEA-resident director (do not draft sham nominee arrangements — R-IE-F1). 5. Default entity for NGO / charity / club / OMC: Company Limited by Guarantee (CLG), with separate Charities Regulator registration if charitable tax exemption (CHY number) is sought. 6. Default entity for joint venture SPV or securitisation vehicle: DAC. 7. Default sectoral check: always test the proposed business activity against the sectoral matrix in Section 7 before quoting timelines, because regulated activities can add 12–52 weeks for sectoral authorisation (especially Central Bank-regulated activities). 8. Default tax classification: confirm trading vs non-trading characterisation; 12.5% only applies to trading (Schedule D Case I / II) income; investment / rental / passive income is 25%. 9. Default data protection action: assume GDPR + Data Protection Act 2018 obligations apply to any business handling personal data; budget for Record of Processing Activities, privacy notice, breach response, and DPO appointment if Article 37 thresholds met. 10. Default annual compliance reminder: CRO B1 annual return + Revenue CT1 (companies) or Form 11 (sole traders / partners) + VAT returns (bi-monthly / quarterly / annual depending on turnover) + Employer PMOD real-time payroll + RBO update within 14 days of any beneficial-ownership change. 11. Default PPS Number / VIN check: confirm every director has a PPS Number or has commenced the CRO VIN process before filing Form A1 — incorporation will be rejected since 11 June 2023 otherwise.  _(R-IE-F1)_

## Section 15 — Sources

**Companies Act 2014** (consolidated; commenced 1 June 2015) — Parts 1–25 governing all Irish corporate forms, single-document LTD Constitution, single-director LTD, abolition of authorised share capital for LTDs, audit exemption for small companies.

**Companies (Statutory Audits) Act 2018** — implements Audit Directive 2014/56/EU and Audit Regulation 537/2014/EU.

**Companies (Accounting) Act 2017** — implements Accounting Directive 2013/34/EU.

**Companies (Miscellaneous Provisions) (Covid-19) Act 2020** and subsequent extensions — temporary measures continued under permanent reform in the Companies (Corporate Enforcement Authority) Act 2021.

- **Taxes Consolidation Act 1997 (TCA 1997)** — as amended annually by Finance Acts; key sections: s.21 (CT rate), s.23A (incorporation residence), s.110 (securitisation), s.207 / s.208 (charitable exemption), s.440 / s.441 (close-company surcharges), s.486C (start-up relief), s.597AA (Entrepreneur Relief), s.598 / s.599 (Retirement Relief), s.766 (R&D Tax Credit), s.769G–s.769R (KDB), s.811C (general anti-avoidance), Part 4A (Pillar Two QDTT inserted by Finance (No. 2) Act 2023).  _(Taxes Consolidation Act 1997 (TCA 1997))_

**Finance Act 2024** and **Finance Act 2025** — most recent annual amendments; verify any monetary threshold (VAT registration €42,500/€85,000; standard rate cut-off; PRSI rates; USC bands; R&D Tax Credit instalment threshold).

- **Stamp duty on share transfers** — 1% %  _(Stamp Duties Consolidation Act 1999)_
- **Business Names Act 1963** — RBN1 / RBN1A / RBN1B registration.  _(Business Names Act 1963)_
- **Partnership Act 1890** — general partnerships.  _(Partnership Act 1890)_
- **Limited Partnerships Act 1907** — LPs.  _(Limited Partnerships Act 1907)_
- **Investment Limited Partnerships Act 1994 as amended** — as amended by the **Investment Limited Partnerships (Amendment) Act 2020** — ILPs (regulated funds).  _(Investment Limited Partnerships Act 1994; Investment Limited Partnerships (Amendment) Act 2020)_
- **Legal Services Regulation Act 2015** — solicitors' LLPs.  _(Legal Services Regulation Act 2015)_
- **Charities Act 2009** — Charities Regulator, CHY number.  _(Charities Act 2009)_
- **Multi-Unit Developments Act 2011** — OMCs as CLGs.  _(Multi-Unit Developments Act 2011)_
- **EU AMLD 4 / 5 as transposed by SI 110/2019** — **EU AMLD 4 / 5 (Directives (EU) 2015/849 and (EU) 2018/843)** as transposed by **SI 110/2019** — RBO regime.  _(Directives (EU) 2015/849 and (EU) 2018/843; SI 110/2019)_
- **CJEU Joined Cases C-37/20 and C-601/20** — (Luxembourg Business Registers, 22 November 2022) — restricted public access to beneficial ownership registers.  _(CJEU Joined Cases C-37/20 and C-601/20)_
- **GDPR and Data Protection Act 2018** — **GDPR (Regulation (EU) 2016/679)** and **Data Protection Act 2018** — data protection.  _(Regulation (EU) 2016/679; Data Protection Act 2018)_
- **Criminal Justice (Money Laundering and Terrorist Financing) Act 2010** — as amended through 2021 — AML / KYC.  _(Criminal Justice (Money Laundering and Terrorist Financing) Act 2010)_
- **MiCA (Regulation (EU) 2023/1114)** — crypto-asset service providers; effective 30 December 2024.  _(Regulation (EU) 2023/1114)_
- **EU Pillar Two global minimum tax** — 15% % (transposed via Part 4A TCA 1997)  _(EU Pillar Two Directive (Directive (EU) 2022/2523))_
- **Online Safety and Media Regulation Act 2022** — establishes Coimisiún na Meán.  _(Online Safety and Media Regulation Act 2022)_
- **Gambling Regulation Act 2024** — establishes GRAI.  _(Gambling Regulation Act 2024)_
- **Investments and Securities regulatory framework** — Central Bank Act 1971; Central Bank (Supervision and Enforcement) Act 2013; European Union (Markets in Financial Instruments) Regulations 2017 (MiFID II).  _(Central Bank Act 1971; Central Bank (Supervision and Enforcement) Act 2013; European Union (Markets in Financial Instruments) Regulations 2017)_

Portals: **core.cro.ie** (CRO), **rbo.gov.ie** (RBO), **revenue.ie / ros.ie** (Revenue / ROS), **centralbank.ie** (Central Bank), **dataprotection.ie** (DPC), **charitiesregulator.ie** (Charities Regulator), **ccpc.ie** (CCPC), **comreg.ie** (ComReg), **cnam.ie** (Coimisiún na Meán).

Where a specific monetary threshold or rate is uncertain at the time of advice, mark as **TBC** and verify against the current Finance Act, Revenue eBrief, CRO Information Leaflet, or Central Bank circular in force before relying on it.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice under Irish law. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Irish solicitor, Chartered Accountant Ireland (CAI), Association of Chartered Certified Accountants (ACCA), Chartered Institute of Management Accountants (CIMA), Certified Public Accountant (CPA Ireland), or Irish Tax Institute (ITI) Chartered Tax Adviser (CTA) before acting upon. Non-EEA founders should additionally engage Irish immigration counsel for Stamp 1 / Stamp 4 / STEP matters, which are out of scope.

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
