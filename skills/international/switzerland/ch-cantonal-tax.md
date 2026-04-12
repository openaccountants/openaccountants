---
name: ch-cantonal-tax
description: >
  Use this skill whenever asked about Swiss cantonal and communal income tax (Staatssteuer / Gemeindesteuer / impôt cantonal et communal) for self-employed individuals. Trigger on phrases like "Kantonssteuer", "Gemeindesteuer", "cantonal tax Switzerland", "Steuerfuss", "tax multiplier Swiss", "kirchensteuer Schweiz", "impôt cantonal", "communal tax rate", "Steuerausscheidung", or any question about cantonal/communal income tax for a self-employed person in Switzerland. This skill covers the cantonal tax multiplier system (Steuerfuss), church tax, inter-cantonal allocation, and the interaction between cantonal and federal returns. MUST be loaded alongside ch-federal-income-tax for the complete picture. ALWAYS read this skill before touching any Swiss cantonal tax work.
version: 1.0
jurisdiction: CH
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ch-federal-income-tax
---

# Switzerland Cantonal and Communal Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Switzerland (Cantonal and Communal level) |
| Jurisdiction Code | CH |
| Primary Legislation | Steuerharmonisierungsgesetz (StHG), SR 642.14 (Federal Tax Harmonisation Act); individual cantonal tax laws (Steuergesetze) |
| Supporting Legislation | Cantonal Steuerverordnungen; Kreisschreiben der SSK (Schweizerische Steuerkonferenz); BGE (Federal Supreme Court rulings on inter-cantonal allocation) |
| Tax Authority | Kantonale Steuerverwaltung (Cantonal Tax Administration) of each canton |
| Filing Portal | Varies by canton (e.g., ZH: steuern.zh.ch; BE: taxme.ch; GE: ge.ch/impots; VD: vd.ch/impots) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Treuhänder or Steuerberater practising in Switzerland |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: Steuerfuss/multiplier mechanics, church tax, basic cantonal rate table interaction, filing deadlines. Tier 2: inter-cantonal allocation, mixed deductions, cantonal-specific deductions. Tier 3: inter-cantonal Steuerausscheidung disputes, Steuererlass, group structures, non-resident taxation. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Treuhänder must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## IMPORTANT: Swiss Tax System Structure [T1]

Switzerland has a **three-level** income tax system:

| Level | Tax Name | Legislation | Rate Structure |
|-------|----------|-------------|----------------|
| Federal | Direkte Bundessteuer (dBSt) | DBG (SR 642.11) | Fixed progressive schedule, same nationwide |
| Cantonal | Staatssteuer / Kantonssteuer | Each canton's Steuergesetz | Base tariff x cantonal Steuerfuss |
| Communal | Gemeindesteuer | Each commune's Steuerfuss | Base tariff x communal Steuerfuss |

Additionally, most cantons levy a **church tax** (Kirchensteuer) for members of recognised churches.

**All three levels are filed on a single combined Steuererklarung (tax return) through the cantonal tax portal.** The federal tax is computed separately but filed together. The cantonal and communal taxes share the same taxable income base (with minor variations) but apply different multipliers.

---

## Step 0: Client Onboarding Questions

Before computing any cantonal/communal income tax, you MUST know:

1. **Canton of tax residence** [T1] -- determines which cantonal law and rate table apply
2. **Municipality (Gemeinde) of tax residence** [T1] -- determines the communal Steuerfuss
3. **Marital status** [T1] -- single, married, registered partnership
4. **Church membership** [T1] -- member of a recognised church? Which denomination? (Determines Kirchensteuer)
5. **Steuerbares Einkommen (taxable income)** [T1] -- after all deductions (uses the federal figure as starting point, with cantonal adjustments)
6. **Does the taxpayer have business activity in multiple cantons?** [T2] -- triggers inter-cantonal Steuerausscheidung
7. **Does the taxpayer own real property in another canton?** [T2] -- triggers inter-cantonal allocation for property income
8. **Children / dependants** [T1] -- Kinderabzug varies by canton
9. **Prior year tax bill (Steuerrechnung)** [T1] -- for provisional tax (Vorauszahlung) reconciliation

**If canton and municipality are unknown, STOP. The cantonal and communal multipliers determine the entire tax burden.**

---

## Step 1: The Steuerfuss / Multiplier System [T1]

**Legislation:** StHG Art. 1; individual cantonal Steuergesetze

### How It Works

Most cantons use a **multiplier system** (Steuerfuss):

1. The cantonal law defines a **base tariff** (Grundtarif / tarif de base) -- a progressive schedule expressed as "einfache Steuer" (simple tax)
2. The canton applies a **cantonal multiplier** (kantonaler Steuerfuss) to the simple tax
3. The municipality applies a **communal multiplier** (Gemeindesteuerfuss) to the same simple tax
4. The church applies a **church multiplier** (Kirchensteuerfuss) to the simple tax (if applicable)

```
Einfache Steuer = base tariff applied to steuerbares Einkommen
Kantonssteuer = Einfache Steuer x kantonaler Steuerfuss (%)
Gemeindesteuer = Einfache Steuer x Gemeindesteuerfuss (%)
Kirchensteuer = Einfache Steuer x Kirchensteuerfuss (%)
Total cantonal/communal tax = Kantonssteuer + Gemeindesteuer + Kirchensteuer
```

### Important Exceptions [T2]

Not all cantons use the simple multiplier system:
- **Basel-Stadt (BS):** Uses a direct tariff without a multiplier -- the cantonal rate schedule IS the final tax. No separate communal tax (city and canton are merged).
- **Geneva (GE):** Uses centimes additionnels. The cantonal rate is applied directly; the communal rate is expressed as a percentage of the cantonal tax.
- **Appenzell Innerrhoden (AI):** Uses a simplified multiplier system with distinct characteristics.
- **Graubunden (GR):** Uses the multiplier system but some municipalities have additional surtaxes.

**[T2] -- Always confirm the specific canton's multiplier mechanics before computing. The general formula above applies to the majority of cantons but not all.**

---

## Step 2: Cantonal Steuerfuss Examples (2025) [T1/T2]

**Note: Steuerfuss values change annually. The values below are indicative for 2025. Always verify the current year's values from the cantonal Steuerverwaltung.**

### Selected Cantons and Municipalities

| Canton | Capital City | Cantonal Steuerfuss | Municipal Steuerfuss (Capital) | Church (Reformed) | Effective Combined Multiple |
|--------|-------------|--------------------|-----------------------------|-------------------|---------------------------|
| Zurich (ZH) | Zurich | 100% | ~119% | ~11% | ~230% of Grundtarif |
| Bern (BE) | Bern | 3.06 (Einheiten) | 1.54 | 0.194 | ~4.79 Einheiten |
| Luzern (LU) | Luzern | 1.60 (Einheiten) | 1.75 | 0.24 | ~3.59 Einheiten |
| Zug (ZG) | Zug | 82% | 60% | ~8% | ~150% of Grundtarif |
| Basel-Stadt (BS) | Basel | Direct tariff | (included) | ~8% of Staatssteuer | N/A (direct tariff) |
| Geneva (GE) | Geneva | 47.79% (centimes) | 45.5 centimes | N/A (church separate) | N/A (centimes system) |
| Vaud (VD) | Lausanne | 154.5% | 79% | ~10% | N/A (composite system) |
| Schwyz (SZ) | Schwyz | 150% | ~130% (varies widely) | ~17% | ~297% of Grundtarif |
| Nidwalden (NW) | Stans | 100% | ~127% | ~9% | ~236% of Grundtarif |
| Ticino (TI) | Bellinzona | 100% | ~95% | ~8% | ~203% of Grundtarif |

**[T2] -- These values are approximate and vary by year and municipality. Verify with the cantonal Steuerverwaltung or use the official online tax calculator for the specific canton.**

### Where to Find Current Steuerfuss

| Source | URL |
|--------|-----|
| ESTV tax calculator | https://swisstaxcalculator.estv.admin.ch |
| SSK cantonal comparison | https://www.steuerkonferenz.ch |
| Individual cantonal portals | See filing portal list above |

---

## Step 3: Taxable Income for Cantonal Purposes [T1]

**Legislation:** StHG Art. 7-9 (income types), Art. 9-10 (deductions)

### Relationship to Federal Taxable Income

The cantonal taxable income (steuerbares Einkommen) generally starts from the same base as the federal taxable income, with the following key differences:

| Item | Federal (DBG) | Cantonal (StHG) |
|------|--------------|-----------------|
| Self-employment income | Art. 18 DBG | StHG Art. 8 -- same definition |
| Geschäftsaufwand (business expenses) | Art. 27-31 DBG | StHG Art. 10 -- largely harmonised |
| AHV/IV/EO deduction | Fully deductible | Fully deductible |
| BVG (Pillar 2) contributions | Fully deductible | Fully deductible |
| Säule 3a (Pillar 3a) | Max CHF 35,280 (2025, self-employed without BVG) or CHF 7,056 (with BVG) | Same limits, fully deductible |
| Kinderabzug (child deduction) | CHF 6,600 per child | **Varies by canton** (CHF 6,500 to CHF 13,000+) |
| Versicherungsabzug (insurance deduction) | CHF 1,800 (single) / CHF 3,600 (married) | **Varies by canton** (often higher than federal) |
| Berufskostenabzug (professional expenses) | Art. 26 DBG | Cantonal law -- may differ |
| Charitable donations | 20% of net income | **Varies by canton** (some allow more) |

### Cantonal Variations in Deductions [T2]

Each canton sets its own deduction amounts for:
- Kinderabzug (child deduction) -- can be substantially higher than federal
- Versicherungspramienabzug (insurance premiums deduction)
- Betreuungskostenabzug (childcare costs)
- Eigenbetreuungsabzug (own childcare deduction -- not available in all cantons)
- Zweiverdienerabzug (dual-income deduction for married couples)
- Krankheitskosten (medical expenses above threshold)
- Gemeinnützige Zuwendungen (charitable donations)

**[T2] -- Always verify cantonal-specific deduction limits. They differ significantly from federal and from each other.**

---

## Step 4: Computation Steps [T1]

### Step 4.1 -- Determine steuerbares Einkommen (cantonal)

```
cantonal_taxable_income = gross_self_employment_income
                        - Geschaeftsaufwand (business expenses)
                        - AHV_IV_EO_contributions
                        - BVG_contributions
                        - Saeule_3a_contributions
                        - cantonal_Kinderabzug (per canton)
                        - cantonal_Versicherungsabzug (per canton)
                        - other cantonal deductions
```

### Step 4.2 -- Look up einfache Steuer (simple tax) from cantonal base tariff

```
einfache_steuer = cantonal_base_tariff(cantonal_taxable_income, marital_status)
```

**The base tariff is a progressive schedule specific to each canton. Use the official cantonal tariff tables.**

### Step 4.3 -- Apply multipliers

```
kantonssteuer = einfache_steuer * kantonaler_steuerfuss
gemeindesteuer = einfache_steuer * gemeinde_steuerfuss
kirchensteuer = einfache_steuer * kirchen_steuerfuss  (if church member)
```

### Step 4.4 -- Total cantonal/communal tax

```
total_cantonal_communal = kantonssteuer + gemeindesteuer + kirchensteuer
```

### Step 4.5 -- Add federal tax

```
total_income_tax = total_cantonal_communal + direkte_bundessteuer
```

**NEVER compute einfache Steuer manually -- always use the official cantonal tariff table or deterministic engine.**

---

## Step 5: Church Tax (Kirchensteuer) [T1]

**Legislation:** Cantonal church tax laws; Bundesverfassung Art. 15 (religious freedom)

### Who Pays

| Status | Church Tax? |
|--------|-------------|
| Member of Evangelisch-Reformierte Kirche | YES -- canton sets rate |
| Member of Römisch-Katholische Kirche | YES -- canton sets rate |
| Member of Christkatholische Kirche | YES -- canton sets rate (where applicable) |
| Member of recognised Jewish community (some cantons) | YES (e.g., BS, BE) |
| No church affiliation (konfessionslos) | NO |
| Austritt (formal exit from church) | NO -- from date of exit |
| Legal entities (Juristische Personen) | **Varies by canton** -- some cantons levy church tax on legal entities |

### How to Exit Church Tax

A formal Kirchenaustritt (church exit declaration) must be made to the Zivilstandsamt (civil registry) or the church. Church tax ceases from the date of exit (some cantons: from the following tax period).

### Church Tax Rates [T1]

Church tax is typically expressed as a percentage of the einfache Steuer:
- Range: 5% to 25% of einfache Steuer, depending on canton and denomination
- Applied as a multiplier alongside cantonal and communal Steuerfuss

---

## Step 6: Inter-Cantonal Tax Allocation (Steuerausscheidung) [T2]

**Legislation:** StHG Art. 20-21; Bundesgerichtsentscheide (BGE) on Doppelbesteuerungsverbot

### When It Applies [T2]

Inter-cantonal allocation is required when a taxpayer has:
- Self-employment activity with a Betriebsstatte (permanent establishment) in another canton
- Real property (Liegenschaften) in another canton
- Residence in one canton but principal business in another

### Allocation Rules [T2]

| Income Type | Allocation Rule |
|-------------|----------------|
| Self-employment income from PE | Allocated to canton where PE is located |
| Real property income | Allocated to canton where property is located |
| Investment income | Allocated to canton of residence |
| Employment income | Generally canton of residence |
| Other income | Canton of residence |

### Procedure [T2]

1. Total worldwide income is determined
2. Income attributed to each canton is identified
3. Each canton taxes its share at the rate applicable to total income (Progressionsvorbehalt)
4. The residence canton taxes the remaining income at the rate applicable to total income

**[T2] -- Inter-cantonal allocation is complex and fact-specific. Flag for Treuhänder whenever activity spans multiple cantons. The Doppelbesteuerungsverbot (prohibition of double taxation under Art. 127 Abs. 3 BV) means no income may be taxed by two cantons.**

---

## Step 7: Provisional Tax Payments (Vorauszahlungen / Akontozahlungen) [T1]

**Legislation:** Cantonal Steuergesetze (varies by canton)

### System [T1]

Most cantons require **provisional tax payments** during the tax year, based on the prior year's tax liability or an estimate:

| Canton Group | System | Notes |
|-------------|--------|-------|
| Praenumerando cantons (e.g., ZH, BE, LU, SG) | Tax on prior-year income; provisional payments based on prior assessment | Adjustments after filing |
| Postnumerando cantons (e.g., BS, TI, VS, FR -- now largely converted) | Tax on current-year income; provisional payments estimated | Most cantons have shifted to Praenumerando since 2003 |

### Payment Schedule (Typical) [T1]

Most cantons issue provisional tax invoices (provisorische Steuerrechnung) in instalments:

| Typical Schedule | Detail |
|-----------------|--------|
| Number of instalments | 9-12 monthly or 3-4 quarterly (varies by canton) |
| Basis | Prior year's final tax assessment |
| Adjustments | Taxpayer can request adjustment if income changes significantly |
| Interest on overpayment | Vergutungszins (credit interest) -- typically 0-1% |
| Interest on underpayment | Verzugszins (arrears interest) -- typically 3-5% |

---

## Step 8: Filing Deadlines [T1]

### Filing the Steuererklarung

| Canton | Standard Deadline | Extension Available? |
|--------|-------------------|---------------------|
| Most cantons | 31 March of the following year | YES -- typically to 30 September or 30 November |
| Zurich (ZH) | 31 March | Extension via Fristverlängerung (online) |
| Bern (BE) | 15 March | Extension available |
| Geneva (GE) | 31 March | Extension available |
| Vaud (VD) | 15 March | Extension available |
| Ticino (TI) | 30 April | Extension available |

### Filing Method [T1]

| Method | Detail |
|--------|--------|
| Electronic filing | Mandatory or preferred in most cantons (e-filing portals) |
| Software | Most cantons provide free tax software or accept commercial software (e.g., Dr. Tax, TaxMe) |
| Paper | Still accepted in most cantons but increasingly discouraged |
| Treuhänder filing | Tax advisor files on behalf of client with power of attorney |

---

## Step 9: Wealth Tax (Vermogenssteuer) -- Brief Reference [T1]

**Legislation:** StHG Art. 13-14; cantonal Steuergesetze

Switzerland levies a **wealth tax** (Vermogenssteuer) at the cantonal and communal level only (no federal wealth tax). This is separate from income tax but filed on the same return.

| Item | Detail |
|------|--------|
| Base | Net wealth (assets minus liabilities) as at 31 December |
| Self-employed | Business assets are included at Steuerwert (tax value) |
| Rates | Progressive, typically 0.05% to 1% (varies enormously by canton) |
| Steuerfuss | Same multiplier system as income tax |
| Low-tax cantons | Zug, Nidwalden, Schwyz -- very low wealth tax rates |
| High-tax cantons | Geneva, Vaud, Basel-Stadt -- relatively higher rates |

**[T2] -- Wealth tax computation is out of scope for this skill. Flag for Treuhänder. The wealth tax base and computation require detailed asset valuation.**

---

## Step 10: Edge Case Registry

### EC1 -- New self-employed person, no prior year assessment [T1]

**Situation:** Client starts self-employment in 2025. No prior year tax assessment exists.
**Resolution:** The cantonal Steuerverwaltung issues a provisional tax invoice based on estimated income (Schätzung). The taxpayer should provide an income estimate to avoid significant underpayment interest. After filing the 2025 return, a definitive assessment (definitive Veranlagung) replaces the provisional one.

### EC2 -- Moving between cantons mid-year [T1]

**Situation:** Client moves from Zurich to Zug on 1 July 2025.
**Resolution:** For Praenumerando cantons: the canton of residence on 31 December (Zug) is the sole tax canton for the entire tax year. Zurich has no claim. The Zug Steuerfuss applies to the full year's income. **This is a significant tax planning point** -- moving to a low-tax canton benefits the entire year.
**Legislation:** StHG Art. 68; BGE 131 I 285.

### EC3 -- Church exit mid-year [T1]

**Situation:** Client formally exits the church on 15 May 2025.
**Resolution:** Treatment varies by canton. Most cantons prorate church tax: church tax applies for Jan-May, no church tax from June onward. Some cantons apply a full-year rule (exit effective from the following year). Verify the specific canton's church tax law.

### EC4 -- Extremely low-tax municipality [T1]

**Situation:** Client lives in Wollerau (SZ), which has a total Steuerfuss of ~90%.
**Resolution:** Apply the Schwyz cantonal base tariff with Wollerau's communal Steuerfuss. The total effective rate may be less than half of Zurich city. This is legitimate -- municipalities compete on Steuerfuss.

### EC5 -- Self-employed with PE in another canton [T2]

**Situation:** Freelance architect lives in Bern but has a studio (Betriebsstatte) in Zurich.
**Resolution:** Inter-cantonal Steuerausscheidung required. Income from the Zurich PE is taxable in Zurich; remaining income is taxable in Bern. Both cantons apply the rate corresponding to total worldwide income (Progressionsvorbehalt). [T2] Flag for Treuhänder: allocation methodology must be documented.

### EC6 -- Foreign national, Quellensteuer (withholding tax) [T3]

**Situation:** Self-employed foreign national without C permit.
**Resolution:** [T3] Escalate. Foreign nationals without a C permit may be subject to Quellensteuer (tax at source) rather than ordinary taxation. The rules differ by canton and by permit type. This skill does not cover Quellensteuer.

### EC7 -- Married couple with significantly different incomes [T1]

**Situation:** Married couple. One earns CHF 200,000, the other CHF 20,000.
**Resolution:** Switzerland taxes married couples jointly (Faktorenaddition). Combined income CHF 220,000 is taxed using the Verheiratetentarif. The Zweiverdienerabzug (dual-income deduction, where available cantonally) partially mitigates the marriage penalty. [T2] Check the specific canton's Zweiverdienerabzug limit.

### EC8 -- Self-employed person with no church affiliation [T1]

**Situation:** Client has formally exited all churches (konfessionslos).
**Resolution:** No Kirchensteuer applies. Only Kantonssteuer + Gemeindesteuer + Bundessteuer. This can reduce the total tax burden by 5-15% depending on the canton's church tax rate.

### EC9 -- Cantonal-specific deductions exceeding federal [T2]

**Situation:** Client in Basel-Stadt claims Kinderabzug.
**Resolution:** Basel-Stadt Kinderabzug is CHF 8,000 per child (cantonal), versus CHF 6,600 per child (federal). Apply the correct deduction at each level. The cantonal taxable income may differ from the federal taxable income. [T2] Confirm current cantonal Kinderabzug amount.

---

## Step 11: Test Suite

### Test 1 -- Single freelancer in Zurich city, standard case

**Input:** Single, age 35, self-employment income CHF 100,000, Geschäftsaufwand CHF 20,000, AHV CHF 7,200, Säule 3a CHF 7,056 (with BVG), no children, Reformed church member. Zurich city Steuerfuss: cantonal 100%, communal 119%, church 11%.
**Expected output:**
- Steuerbares Einkommen (cantonal): approximately CHF 65,744 (after cantonal deductions)
- Einfache Steuer: look up from Zurich Grundtarif -- approximately CHF 4,800
- Kantonssteuer: CHF 4,800 x 100% = CHF 4,800
- Gemeindesteuer: CHF 4,800 x 119% = CHF 5,712
- Kirchensteuer: CHF 4,800 x 11% = CHF 528
- Total cantonal/communal: approximately CHF 11,040
- Plus Bundessteuer: approximately CHF 1,900
- Grand total: approximately CHF 12,940

### Test 2 -- Married freelancer in Zug, no church

**Input:** Married (single income), self-employment income CHF 150,000, Geschäftsaufwand CHF 30,000, AHV CHF 10,800, Säule 3a CHF 7,056, 2 children. Zug Steuerfuss: cantonal 82%, communal 60%, no church.
**Expected output:**
- Steuerbares Einkommen (cantonal): approximately CHF 87,000 (after Zug-specific deductions)
- Einfache Steuer: look up from Zug Verheiratetentarif
- Kantonssteuer: einfache Steuer x 82%
- Gemeindesteuer: einfache Steuer x 60%
- Total cantonal/communal: einfache Steuer x 142%
- Note: Zug is known for very low base tariffs, so the total tax burden will be significantly lower than Zurich.

### Test 3 -- Inter-cantonal allocation

**Input:** Lives in Bern, PE in Zurich. Total self-employment income CHF 200,000. CHF 120,000 attributable to Zurich PE, CHF 80,000 to Bern.
**Expected output:**
- Zurich taxes CHF 120,000 at the rate applicable to CHF 200,000 total income (Progressionsvorbehalt)
- Bern taxes CHF 80,000 at the rate applicable to CHF 200,000 total income (Progressionsvorbehalt)
- Federal tax on total CHF 200,000 (allocated proportionally to each canton)
- [T2] Flag for Treuhänder: confirm allocation methodology.

### Test 4 -- Move from Zurich to Schwyz on 30 November

**Input:** Client moves residence from Zurich to Wollerau (SZ) on 30 November 2025. Self-employment income CHF 250,000.
**Expected output:**
- 31 December residence: Schwyz (Wollerau)
- Full year taxed by Schwyz at Wollerau Steuerfuss
- Zurich has no claim for 2025
- Significant tax saving compared to Zurich

### Test 5 -- Church exit mid-year

**Input:** Catholic member exits church 1 April 2025 in Zurich.
**Expected output:**
- Zurich prorates church tax: 3/12 of the annual Kirchensteuer applies
- From April: only Kantonssteuer + Gemeindesteuer + Bundessteuer

---

## Step 12: Record Keeping [T1]

| Requirement | Detail |
|-------------|--------|
| Steuererklarung and Beilagen | Retain for 10 years |
| Business records (Buchfuhrung) | 10 years from end of business year (OR Art. 958f) |
| Provisional tax invoices and payments | Retain until definitive Veranlagung is final |
| Inter-cantonal allocation working papers | Retain for 10 years |
| Church exit documentation | Retain permanently |

---

## Step 13: Common Pitfalls

| Pitfall | Why It Matters |
|---------|---------------|
| Using federal deductions for cantonal computation | Cantonal deductions (Kinderabzug, Versicherungsabzug) differ from federal -- often higher |
| Ignoring Steuerfuss changes | Municipal Steuerfuss can change annually; always use the current year |
| Not requesting Fristverlängerung | Late filing penalties apply; most cantons grant extensions routinely |
| Underestimating provisional tax | Verzugszins (arrears interest) at 3-5% makes underpayment expensive |
| Assuming church tax is automatic | Only applies to church members; exit saves 5-15% of total tax |
| Ignoring inter-cantonal allocation | Double taxation occurs if not properly allocated -- Doppelbesteuerungsverbot applies |

---

## PROHIBITIONS

- NEVER compute cantonal tax without knowing the specific canton and municipality -- rates vary enormously
- NEVER use federal deduction amounts for cantonal computation -- they differ
- NEVER apply a Steuerfuss without verifying it is current for the tax year
- NEVER assume all cantons use the same multiplier system -- Basel-Stadt and Geneva differ
- NEVER apply church tax without confirming church membership status
- NEVER allocate inter-cantonal income without flagging for Treuhänder review
- NEVER compute einfache Steuer manually -- use official cantonal tariff tables or deterministic engine
- NEVER tax a mid-year mover in two cantons -- only the 31 December residence canton taxes the full year
- NEVER ignore wealth tax -- it is filed on the same return and must be considered
- NEVER present cantonal tax calculations as definitive -- always label as estimated and direct client to their Treuhänder

---

## Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified Treuhänder or Steuerberater must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Treuhänder. Document gap.
```

---

## Contribution Notes

This skill requires validation by a licensed Swiss Treuhänder or Steuerberater. Key areas requiring local expertise:

1. Current Steuerfuss values for all 26 cantons and major municipalities
2. Cantonal-specific deduction amounts (Kinderabzug, Versicherungsabzug, etc.)
3. Inter-cantonal Steuerausscheidung methodology
4. Church tax proration rules by canton
5. Provisional tax payment schedules by canton
6. Quellensteuer rules for foreign nationals (out of scope but must be identified)

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Treuhänder, Steuerberater, or equivalent licensed practitioner in Switzerland) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
