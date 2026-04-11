---
name: qatar-tax
description: Use this skill whenever asked about Qatar indirect tax, VAT status, or tax obligations. Trigger on phrases like "Qatar VAT", "Qatar tax", "Qatar GST", "does Qatar have VAT", or any request involving Qatar tax compliance. Qatar does NOT have VAT/GST as of April 2026. This skill documents the current tax landscape and the expected future VAT implementation under the GCC Unified VAT Agreement. ALWAYS read this skill before advising on Qatar tax matters.
---

# Qatar Tax Status Skill (No VAT/GST)

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | State of Qatar |
| Jurisdiction Code | QA |
| Primary Legislation | Law No. 24 of 2018 (Income Tax Law); GCC Unified VAT Agreement (signed but not yet implemented) |
| Tax Authority | General Tax Authority (GTA) |
| Tax Portal | https://www.gta.gov.qa |
| VAT/GST Status | **NOT IMPLEMENTED** as of April 2026 |
| Expected VAT Rate | 5% (when implemented, per GCC Unified VAT Agreement) |
| Currency | Qatari Riyal (QAR) |
| Contributor | Open Accounting Skills Registry |
| Validation Date | April 2026 |
| Last Research Update | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: current absence of VAT, corporate income tax basics. Tier 2: expected implementation details. Tier 3: specific corporate tax planning, transfer pricing. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed tax advisor must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed tax advisor.

---

## CRITICAL NOTICE [T1]

**Qatar does NOT have a Value Added Tax (VAT) or Goods and Services Tax (GST) as of April 2026.**

- There is NO VAT return to file
- There is NO VAT registration requirement
- There is NO output VAT to charge on sales
- There is NO input VAT to claim on purchases
- There is NO reverse charge mechanism for services from non-residents
- Invoices issued in Qatar should NOT include any VAT line

**If a client asks about "Qatar VAT", the correct answer is: Qatar has not yet implemented VAT. No VAT obligations exist.**

---

## Step 1: GCC VAT Agreement Context [T1]

Qatar is a signatory to the GCC Unified VAT Agreement (also known as the Common VAT Agreement of the States of the Gulf Cooperation Council). This agreement was signed by all six GCC member states:

| Country | VAT Implemented | Rate | Effective Date |
|---------|----------------|------|----------------|
| Saudi Arabia | Yes | 15% | 1 Jan 2018 (5%), increased to 15% on 1 Jul 2020 |
| UAE | Yes | 5% | 1 Jan 2018 |
| Bahrain | Yes | 10% | 1 Jan 2019 (5%), increased to 10% on 1 Jan 2022 |
| Oman | Yes | 5% | 16 Apr 2021 |
| **Qatar** | **No** | **N/A** | **Not yet determined** |
| **Kuwait** | **No** | **N/A** | **Not yet determined** |

**Legislation:** GCC Unified VAT Agreement (signed 2016); no domestic implementation legislation enacted in Qatar as of April 2026.

---

## Step 2: Expected VAT Implementation [T2]

When Qatar eventually implements VAT, the following is expected based on the GCC Unified VAT Agreement framework:

| Feature | Expected Treatment |
|---------|-------------------|
| Standard rate | 5% (per GCC Agreement; however, Qatar may choose a different rate as Bahrain and Saudi Arabia have demonstrated) |
| Zero-rated supplies | Exports, international transport, healthcare, education, basic food items |
| Exempt supplies | Financial services (margin-based), bare land, residential property (subsequent) |
| Registration threshold | To be determined (likely equivalent to other GCC states, ~QAR 375,000) |
| Filing frequency | Monthly or quarterly (to be determined) |
| Reverse charge | For services from non-residents |
| GCC transitional rules | Will apply for intra-GCC supplies |

**Flag for reviewer:** All expected implementation details are speculative. No legislation has been enacted as of April 2026. Multiple industry sources suggest Qatar may implement VAT during 2026, but no official timeline has been confirmed. Do not advise clients to prepare for specific rules until legislation is published.

---

## Step 3: Current Tax Landscape in Qatar [T1]

While Qatar has no VAT, the following taxes DO exist:

### 3a. Corporate Income Tax (CIT)

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Rate | 10% flat rate | Law No. 24/2018, Article 7 |
| Applicability | Non-Qatari-owned share of profits in entities operating in Qatar | Article 2 |
| Qatari/GCC-owned share | Exempt from CIT | Article 3 |
| Qatari-listed companies | Exempt from CIT | Article 3 |
| Government entities | Exempt from CIT | Article 3 |
| Oil and gas operations | Special rates (up to 35%) under concession agreements | Article 7(2) |
| Filing deadline | Within 4 months of fiscal year end | Article 25 |
| Fiscal year | Calendar year (default) or as approved by GTA | Article 1 |
| Withholding tax on services | 5% on payments to non-residents for services performed in Qatar | Article 11 |

### 3b. Excise Tax

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Scope | Tobacco products, energy drinks, carbonated drinks, special purpose goods | Law No. 25/2019 |
| Tobacco rate | 100% | Article 4 |
| Energy drinks rate | 100% | Article 4 |
| Carbonated drinks rate | 50% | Article 4 |
| Special purpose goods rate | 100% | Article 4 |
| Filing | Monthly return to GTA | Article 12 |

### 3c. Customs Duties

| Feature | Detail |
|---------|--------|
| Standard rate | 5% on CIF value (most goods) |
| Exemptions | GCC-origin goods, certain raw materials, diplomatic imports |
| Special rates | 0% on essential goods; higher rates on tobacco, alcohol |
| Free zones | Exemption from customs duties in designated free zones (e.g., QFC, QSTP, QFZ) |

---

## Step 4: Qatar Financial Centre (QFC) [T2]

The Qatar Financial Centre is a special regulatory zone with its own tax regime:

| Feature | QFC Treatment | Legislation |
|---------|---------------|-------------|
| CIT rate | 10% on locally sourced income | QFC Tax Regulations |
| Foreign income | Not subject to QFC tax | QFC Tax Regulations |
| Transfer pricing | Arm's length principle applies | QFC Tax Regulations |
| VAT | Not applicable (no VAT in Qatar) | N/A |
| Tax residency | QFC entities are Qatar tax residents | QFC Tax Regulations |

**Flag for reviewer:** QFC entities have distinct tax rules. Confirm whether the entity is QFC-registered.

---

## Step 5: Implications for Cross-Border Transactions [T1]

### 5a. Qatar Business Buying from GCC VAT Countries

| Scenario | Treatment |
|----------|-----------|
| Qatar company buys goods from UAE supplier | UAE supplier may zero-rate the export (UAE VAT rules). Qatar company has no VAT obligation. |
| Qatar company buys services from Saudi supplier | Saudi supplier charges 15% VAT (Saudi rules). Qatar company cannot recover (no Qatar VAT system). |
| Qatar company receives invoice with Bahrain VAT | Bahrain VAT is a cost to the Qatar company. No recovery mechanism exists. |

### 5b. Qatar Business Selling to GCC VAT Countries

| Scenario | Treatment |
|----------|-----------|
| Qatar company exports goods to Oman | No Qatar VAT applies. Oman customer may need to account for import VAT under Oman rules. |
| Qatar company provides services to UAE client | No Qatar VAT applies. UAE client may need to reverse charge under UAE rules. |

### 5c. Key Point [T1]

Because Qatar has no VAT, Qatar businesses bear irrecoverable foreign VAT as a cost when purchasing from VAT-implementing GCC states. This is a competitive consideration but there is no mechanism to recover it.

---

## Step 6: GCC Transitional Treatment of Qatar [T1]

Under the GCC Unified VAT Agreement, non-implementing states (Qatar and Kuwait) are treated as non-GCC countries for VAT purposes by implementing states:

| Treatment by implementing states | Detail |
|----------------------------------|--------|
| Exports from implementing state to Qatar | May qualify for zero-rating as export (implementing state rules) |
| Imports from Qatar to implementing state | Subject to import VAT at the implementing state's border |
| Services from Qatar to implementing state | Implementing state customer may reverse charge |

**This means Qatar is treated like any other non-GCC country (e.g., India, US) for purposes of VAT in UAE, Saudi Arabia, Bahrain, and Oman.**

---

## Step 7: When VAT Arrives -- Preparation Checklist [T2]

When Qatar announces VAT legislation, businesses should prepare:

| Action | Timeline | Notes |
|--------|----------|-------|
| Monitor GTA announcements | Ongoing | Subscribe to GTA updates |
| Review contracts for VAT clauses | Upon announcement | Existing contracts may need amendment for VAT pass-through |
| Assess IT/ERP readiness | 6-12 months before go-live | Accounting systems must handle VAT calculations |
| Classify supplies | 3-6 months before go-live | Identify zero-rated, exempt, standard-rated supplies |
| Register for VAT | Per legislation timeline | Registration windows will be announced |
| Train staff | 3-6 months before go-live | Accounts payable/receivable, procurement, sales |
| Review pricing | Before go-live | Impact on margins if VAT cannot be passed to customers |
| Update invoice templates | Before go-live | Must comply with tax invoice requirements |

**Flag for reviewer:** Do not implement any VAT preparation measures until legislation is enacted. These are planning items only.

---

## PROHIBITIONS [T1]

- NEVER state that Qatar has VAT -- it does not, as of April 2026
- NEVER advise a client to charge VAT on invoices issued from Qatar
- NEVER advise a client to file a VAT return in Qatar
- NEVER advise a client to register for VAT in Qatar
- NEVER assume Qatar VAT implementation is imminent without enacted legislation
- NEVER confuse Qatar Excise Tax with VAT -- they are separate regimes
- NEVER apply GCC VAT rules to Qatar domestic transactions
- NEVER advise that foreign VAT paid on purchases from GCC states is recoverable in Qatar
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 8: Edge Case Registry

### EC1 -- Client asks "do I need to charge VAT in Qatar?" [T1]
**Situation:** New business in Qatar asks about VAT obligations.
**Resolution:** No. Qatar has no VAT. Issue invoices without VAT. No registration, filing, or collection required.

### EC2 -- Qatar business receives UAE invoice with 5% VAT [T1]
**Situation:** Qatar company receives a supplier invoice from UAE showing 5% VAT.
**Resolution:** The UAE VAT is a cost to the Qatar company. It cannot be recovered. Record the gross amount as the expense. There is no reverse charge in Qatar (no VAT system exists to reverse charge into).

### EC3 -- Qatar business selling to Saudi Arabia [T1]
**Situation:** Qatar company exports goods to a Saudi customer.
**Resolution:** No Qatar VAT applies. The Saudi customer will account for import VAT at 15% under Saudi VAT rules. Qatar company issues invoice without any VAT.

### EC4 -- Multinational asks about VAT grouping including Qatar entity [T1]
**Situation:** Group has entities in UAE, Bahrain, and Qatar. Asks about consolidated VAT.
**Resolution:** There is no VAT group registration possible in Qatar. Each entity in UAE and Bahrain follows their respective VAT rules independently. The Qatar entity has no VAT obligations.

### EC5 -- Upcoming contract: should we include VAT clause? [T2]
**Situation:** Qatar business negotiating a 5-year contract. Asks whether to include a VAT clause.
**Resolution:** Prudent to include a VAT change-of-law clause allowing price adjustment if VAT is introduced during the contract term. This is commercial advice. Flag for reviewer: legal counsel should draft the clause.

### EC6 -- E-commerce platform selling to Qatar consumers [T1]
**Situation:** Foreign e-commerce platform asks about VAT on digital services to Qatar.
**Resolution:** No Qatar VAT applies. However, the platform may have VAT obligations in its own jurisdiction and in other GCC states where it sells. Qatar has no digital services tax or VAT on imported services.

### EC7 -- Withholding tax on services from non-residents [T1]
**Situation:** Qatar company pays a foreign consultant for services performed in Qatar.
**Resolution:** This is NOT VAT. Qatar imposes 5% withholding tax on payments to non-residents for services performed wholly or partly in Qatar. This is a corporate income tax obligation, not a VAT matter.
**Legislation:** Law No. 24/2018, Article 11.

### EC8 -- Excise tax vs. VAT confusion [T1]
**Situation:** Client asks about the "tax" on energy drinks in Qatar, thinking it is VAT.
**Resolution:** This is Excise Tax, not VAT. Qatar imposes 100% excise tax on energy drinks under Law No. 25/2019. This is a production/import-stage tax, not a consumption tax on all goods and services. It is NOT VAT.

### EC9 -- Free zone entity and tax obligations [T2]
**Situation:** Entity in Qatar Free Zone (QFZ) asks about tax obligations.
**Resolution:** QFZ entities may benefit from CIT exemptions for up to 20 years. No VAT applies (Qatar has no VAT). Excise tax applies regardless of free zone status. Flag for reviewer: confirm specific free zone incentive package.

### EC10 -- Client moving from UAE to Qatar: VAT deregistration [T1]
**Situation:** Business relocating from UAE to Qatar asks about VAT.
**Resolution:** Must deregister from UAE VAT (follow UAE deregistration rules). Qatar has no VAT registration. Business will no longer have any VAT obligations once UAE deregistration is complete. May need to account for deemed supply on assets transferred.

---

## Step 9: EU VAT Comparison [T1]

| Feature | Qatar | EU (Directive 2006/112/EC) |
|---------|-------|---------------------------|
| VAT/GST | None | 15-27% (varies) |
| Registration | None | Mandatory above threshold |
| Returns | None | Monthly/quarterly/annual |
| Reverse charge | None | Yes (Articles 196-199) |
| Input tax recovery | None | Yes (subject to rules) |
| Corporate income tax | 10% (non-Qatari share) | Varies (12.5-33%) |
| Excise tax | Yes (tobacco, drinks) | Yes (harmonised) |
| Customs duties | 5% (default) | Common Customs Tariff |
| Digital services tax | None | Varies by member state |

---

## Step 10: Test Suite

### Test 1 -- Standard domestic sale
**Input:** Qatar company sells consulting services to local client. QAR 50,000.
**Expected output:** No VAT. Invoice QAR 50,000 with no VAT line. No VAT return to file.

### Test 2 -- Purchase from UAE supplier
**Input:** Qatar company buys goods from UAE for AED 10,000 + AED 500 UAE VAT.
**Expected output:** Total cost to Qatar company = AED 10,500 (gross). UAE VAT is irrecoverable cost. No Qatar VAT reporting.

### Test 3 -- Export to Oman
**Input:** Qatar company exports goods to Oman. Invoice QAR 100,000.
**Expected output:** No Qatar VAT. Oman customer handles import VAT at 5% under Oman rules.

### Test 4 -- Service to Saudi client
**Input:** Qatar company provides engineering services to Saudi company. QAR 200,000.
**Expected output:** No Qatar VAT. Saudi company reverse charges at 15% under Saudi rules.

### Test 5 -- Non-resident service fee with withholding tax
**Input:** Qatar company pays UK consultant QAR 30,000 for services performed in Qatar.
**Expected output:** 5% withholding tax = QAR 1,500. Net payment = QAR 28,500. This is CIT withholding, NOT VAT.

### Test 6 -- Excise tax on energy drinks
**Input:** Importer brings 1,000 cases of energy drinks into Qatar. CIF value QAR 20,000.
**Expected output:** Excise tax at 100% = QAR 20,000. Customs duty at 5% = QAR 1,000. Total tax = QAR 21,000. This is NOT VAT.

### Test 7 -- Digital service to Qatar consumer
**Input:** Foreign SaaS company charges Qatar consumer USD 100/month.
**Expected output:** No Qatar VAT. No registration required in Qatar. Platform may have obligations in its home jurisdiction.

### Test 8 -- Long-term contract VAT clause
**Input:** Qatar company enters 7-year lease. Should VAT clause be included?
**Expected output:** Prudent to include change-of-law clause. No immediate VAT impact. Reviewer should advise on clause drafting.

### Test 9 -- QFC entity income
**Input:** QFC-registered entity earns QAR 5,000,000 locally sourced income.
**Expected output:** CIT at 10% = QAR 500,000. No VAT. File CIT return with QFC Tax Department.

### Test 10 -- Corporate income tax on mixed ownership
**Input:** Company in Qatar: 60% Qatari-owned, 40% foreign-owned. Profit QAR 1,000,000.
**Expected output:** CIT at 10% on foreign-owned share: 40% x QAR 1,000,000 = QAR 400,000 x 10% = QAR 40,000. No VAT.

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed tax advisor must confirm.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax advisor. Document gap.
```

---

## Contribution Notes

This skill covers Qatar's current NO-VAT status as of April 2026. When Qatar enacts VAT legislation, this skill must be completely rewritten to include:

1. Full VAT return form structure and box mappings
2. Supply classification matrix with Qatar-specific zero-rated and exempt categories
3. Registration thresholds and procedures
4. Filing deadlines and penalties
5. Reverse charge mechanics
6. Blocked input tax categories
7. Edge cases specific to Qatar's economy (LNG, financial services hub, construction)
8. Test suite with Qatar-specific transactions

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
