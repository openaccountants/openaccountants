---
name: liechtenstein-vat
description: Use this skill whenever asked to prepare, review, or advise on a Liechtenstein VAT (MWST) return or any transaction classification for Liechtenstein VAT purposes. Trigger on phrases like "Liechtenstein VAT", "MWST Liechtenstein", "Liechtenstein tax", or any request involving Liechtenstein VAT obligations. Liechtenstein forms a customs union with Switzerland and applies Swiss VAT law. This skill is a reference wrapper that points to the Switzerland VAT skill for substantive rules, with Liechtenstein-specific administrative details noted. ALWAYS read this skill before touching any Liechtenstein VAT-related work.
---

# Liechtenstein VAT (MWST) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Principality of Liechtenstein |
| Jurisdiction Code | LI |
| Tax Name | MWST (Mehrwertsteuer / VAT) |
| Primary Legislation | Swiss Federal Act on Value Added Tax (Mehrwertsteuergesetz, MWSTG) -- applied in Liechtenstein via the Customs Union Treaty of 1923 |
| Supporting Legislation | Customs Union Treaty between Switzerland and Liechtenstein (1923, as amended); Liechtenstein MWST Ordinance; Swiss MWST Ordinance (MWSTV) |
| Tax Authority | Liechtenstein Tax Administration (Steuerverwaltung des Furstentums Liechtenstein) for registration; Swiss Federal Tax Administration (ESTV/AFC) for substantive MWST law |
| Filing Portal | https://www.llv.li/inhalt/118804/amtsstellen/steuerverwaltung (Liechtenstein); returns filed through Swiss FTA system |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, basic classification, customs union treatment. Tier 2: Liechtenstein-specific administrative differences, EEA implications. Tier 3: complex cross-border structures, EEA vs. customs union conflicts. |

---

## CRITICAL: Customs Union with Switzerland [T1]

**Liechtenstein and Switzerland form a customs union established by the Treaty of 29 March 1923.** As a result:

1. **Swiss VAT law applies in Liechtenstein.** The MWSTG (Swiss Federal Act on VAT) is the governing legislation.
2. **There is no separate Liechtenstein VAT system.** The rates, rules, exemptions, and procedures are identical to Switzerland.
3. **Liechtenstein is treated as part of the Swiss VAT territory** for all MWST purposes.
4. **Supplies between Liechtenstein and Switzerland are DOMESTIC supplies** -- NOT imports/exports.
5. **Supplies between Liechtenstein and the EU are treated the same as Switzerland-EU trade** -- i.e., as third-country (non-EU) trade.
6. **MWST registration in Liechtenstein is processed through the Liechtenstein Tax Administration** but follows Swiss MWST law entirely.

**For all substantive VAT rules, rates, classifications, deductions, and return procedures, refer to the Switzerland VAT skill (skills/switzerland/switzerland-vat/SKILL.md).**

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Same as Switzerland VAT skill, plus:

1. **Entity registered in Liechtenstein or Switzerland?** [T1] -- determines which tax administration handles registration
2. **Liechtenstein Tax Administration registration number** [T1] -- if registered in LI
3. **Swiss UID/MWST number** [T1] -- CHE-xxx.xxx.xxx MWST format
4. **EEA membership considerations** [T2] -- Liechtenstein is an EEA member (Switzerland is not); may affect certain regulatory aspects but NOT MWST treatment

**If registration status is unknown, STOP.**

---

## Step 1: VAT Rates (Identical to Switzerland) [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 8.1% | Standard rate | MWSTG Article 25(1) |
| 2.6% | Reduced rate -- food, medicines, books, newspapers, water supply, agricultural inputs | MWSTG Article 25(2) |
| 3.8% | Special rate -- accommodation services (hotel/lodging) | MWSTG Article 25(4) |
| 0% | Export supplies, international transport, diplomatic | MWSTG Article 23 |
| Exempt | Financial services, insurance, medical, education, real property, and others | MWSTG Article 21 |

**These are the Swiss rates effective from January 1, 2024 (as per the popular vote of September 25, 2022 -- AHV 21 reform financing).**

---

## Step 2: Key Administrative Differences [T1]

While substantive MWST law is Swiss, there are administrative differences for Liechtenstein entities:

| Aspect | Liechtenstein Specifics |
|--------|----------------------|
| Registration | Through Liechtenstein Tax Administration (Steuerverwaltung) |
| Tax number format | Same CHE-xxx.xxx.xxx MWST format as Swiss entities |
| Filing | Returns submitted to Swiss FTA via the same system as Swiss entities |
| Payment | To Swiss federal tax accounts (same bank details as Swiss MWST) |
| Audit | May be conducted by either Liechtenstein or Swiss tax authorities |
| Fiscal representation | Liechtenstein entities do NOT need a Swiss fiscal representative (they are within the customs union) |
| Currency | Swiss Franc (CHF) -- Liechtenstein uses CHF as its currency |

---

## Step 3: Supplies Between Liechtenstein and Switzerland [T1]

Supplies of goods and services between Liechtenstein and Switzerland are **domestic supplies**:
- Standard MWST rates apply (8.1%, 2.6%, or 3.8%)
- No import/export treatment
- No customs declaration required
- Invoiced in CHF with Swiss MWST shown
- No reverse charge between LI and CH

---

## Step 4: Supplies Between Liechtenstein and the EU [T1]

Despite Liechtenstein being an EEA member:
- For MWST purposes, Liechtenstein is part of the Swiss customs territory
- Supplies to/from EU countries are treated as **exports/imports** (third-country trade)
- Exports: zero-rated with customs documentation
- Imports: MWST collected at Swiss/Liechtenstein customs border
- **EEA membership does NOT create an intra-community supply regime for MWST**

---

## Step 5: EEA Membership Implications [T2]

Liechtenstein's EEA membership creates some unique considerations:
- **Free movement of goods:** Liechtenstein participates in the EEA single market, but the customs union with Switzerland means goods entering from the EU still pass through Swiss customs
- **Services:** EEA rules on free movement of services apply to regulatory/licensing matters, but MWST treatment follows Swiss law
- **Financial services:** Liechtenstein has a significant financial services sector; MWST exemptions follow Swiss law (MWSTG Article 21)

**Flag for reviewer: EEA implications that create conflicts with customs union treatment require specialist analysis.**

---

## Step 6: Return Form Structure [T1]

**Identical to Switzerland.** Liechtenstein entities file the same MWST return form as Swiss entities. Refer to the Switzerland VAT skill for complete form structure, box mapping, and derived calculations.

Key boxes (summary):
- Ziffer 200: Total domestic turnover
- Ziffer 220: Export/foreign supplies
- Ziffer 289: Exempt supplies
- Ziffer 302-383: Output MWST at various rates
- Ziffer 400-420: Input MWST deductions
- Ziffer 500: MWST payable / refundable

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| MWST return | Quarterly (standard) | 60 days after quarter end | MWSTG Article 71 |
| MWST return | Monthly (optional) | 60 days after month end | MWSTG Article 71 |
| MWST payment | Per return | With return submission | MWSTG Article 86 |
| Annual reconciliation | Annual | 180 days after fiscal year end | MWSTG Article 72 |
| Import MWST | Per import | At customs clearance | Customs law |

---

## Step 8: Blocked Input MWST [T1]

Same as Switzerland:

| Category | Legislation |
|----------|-------------|
| Goods/services for exempt operations | MWSTG Article 29 |
| Entertainment and hospitality (50% blocked) | MWSTG Article 33(2) |
| Motor vehicles for personal use | MWSTG Article 33 |
| Private use of goods/services | MWSTG Article 31 |
| Without valid invoice | MWSTG Article 28 |

---

## Step 9: Edge Case Registry

### EC1 -- Supply from Liechtenstein to Switzerland [T1]

**Situation:** Liechtenstein company sells goods to a Swiss customer.
**Resolution:** Domestic supply. MWST at standard rate (8.1%). No export treatment. No customs. Invoice with MWST like any domestic sale.

### EC2 -- Supply from Liechtenstein to EU (e.g., Austria) [T1]

**Situation:** Liechtenstein company exports goods to Austria.
**Resolution:** This is an export (third-country trade). Zero-rated. Customs export declaration required. Austrian buyer pays import VAT in Austria. NOT intra-community treatment despite LI being in EEA.

### EC3 -- EU company selling services to Liechtenstein entity [T1]

**Situation:** German consulting firm provides services to a Liechtenstein company.
**Resolution:** Place of supply is Liechtenstein (= Swiss MWST territory). Liechtenstein buyer reverse-charges MWST at 8.1% (import of services / Bezugsteuer). Same as a German firm selling to a Swiss entity.

### EC4 -- Liechtenstein financial services [T2]

**Situation:** Liechtenstein trust company provides fiduciary services.
**Resolution:** Financial services are generally exempt from MWST under MWSTG Article 21(2)(19). However, the company may opt to tax certain financial services (Optierung). Flag for reviewer: determine if opting to tax is beneficial for input MWST recovery.
**Legislation:** MWSTG Article 21, Article 22

### EC5 -- EEA vs. customs union conflict [T2]

**Situation:** An EEA regulation affects the treatment of a cross-border supply, but Swiss MWST law treats it differently.
**Resolution:** For MWST purposes, Swiss law prevails (customs union). EEA regulations affect other areas (regulatory, competition) but not MWST. Flag for reviewer if the specific situation creates a genuine conflict requiring specialist analysis.

### EC6 -- Liechtenstein entity with Swiss branch (and vice versa) [T1]

**Situation:** A Liechtenstein company has a branch in Switzerland.
**Resolution:** Both are within the same MWST territory. Intra-entity supplies are not MWST supplies (same legal entity). Single MWST registration covers both. No import/export between LI head office and CH branch.

---

## PROHIBITIONS [T1]

- NEVER treat LI-CH supplies as imports/exports -- they are domestic
- NEVER apply EU intra-community rules to Liechtenstein despite EEA membership
- NEVER use a VAT rate different from Swiss rates
- NEVER apply separate Liechtenstein VAT rules -- Swiss MWSTG applies
- NEVER require a fiscal representative for a Liechtenstein entity (customs union member)
- NEVER compute any number -- handled by deterministic engine

---

## Step 10: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified practitioner must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified practitioner. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Sale from LI to CH customer at 8.1%

**Input:** Liechtenstein company sells consulting to Swiss client. Net CHF 10,000. MWST at 8.1%.
**Expected output:** Domestic supply. Output MWST = CHF 810. Report in Ziffer 302/303. No export treatment.

### Test 2 -- Export from LI to Austria

**Input:** Liechtenstein company exports goods to Austria. CHF 50,000.
**Expected output:** Zero-rated export. Ziffer 220. Customs declaration required. Input MWST deductible.

### Test 3 -- Import of services from Germany (reverse charge)

**Input:** Liechtenstein company engages German consulting firm. EUR 8,000 (equiv. CHF 7,600). No Swiss/LI registration.
**Expected output:** Bezugsteuer (import tax on services). MWST at 8.1% = CHF 615.60. Report as output MWST and input MWST. Net zero.

### Test 4 -- Purchase from Swiss supplier

**Input:** Liechtenstein company buys office furniture from Swiss supplier. Gross CHF 5,405 including MWST CHF 405.
**Expected output:** Domestic purchase. Input MWST CHF 405 deductible. Ziffer 400.

### Test 5 -- Hotel accommodation at 3.8%

**Input:** Liechtenstein hotel provides accommodation. Net CHF 2,000. MWST at 3.8%.
**Expected output:** Output MWST = CHF 76. Report in Ziffer 342/343.

### Test 6 -- Food products at 2.6%

**Input:** Liechtenstein company sells food products. Net CHF 15,000. MWST at 2.6%.
**Expected output:** Output MWST = CHF 390. Report in Ziffer 312/313.

---

## Contribution Notes

This skill requires validation by a licensed Liechtenstein or Swiss tax practitioner. The substantive VAT rules are Swiss, but Liechtenstein-specific administrative nuances require local expertise.

**For complete VAT rule details, always cross-reference the Switzerland VAT skill.**

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
