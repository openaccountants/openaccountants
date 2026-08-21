---
name: de-rental-income
description: Use this skill whenever asked about German rental income taxation (Vermietung und Verpachtung). Trigger on phrases like "Mieteinnahmen", "Vermietung", "Verpachtung", "Anlage V", "§21 EStG", "AfA", "Abschreibung", "Werbungskosten Vermietung", "Hausgeld", "Grundsteuer deduction", "Erhaltungsaufwand", "Herstellungskosten", "verbilligte Vermietung", "Möblierungszuschlag", "rental income Germany", "German property tax deduction", "depreciation German property", "Verlustverrechnung", "rental loss Germany", or any question about computing, filing, or optimising income from letting immovable property in Germany. Covers Anlage V structure, AfA depreciation rates, Werbungskosten, repairs vs improvements, reduced-rent rules, furnished premium, and loss offset. ALWAYS read this skill before touching any German rental income work.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - de-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Rental Income

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Tax | Einkommensteuer auf Einkünfte aus Vermietung und Verpachtung |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Einkommensteuergesetz (EStG) §21 (rental income), §7 Abs. 4 (AfA), §9 (Werbungskosten) |
| Supporting legislation | EStG §§2, 7, 9, 10d (Verlustvor-/rücktrag), 11 (Zufluss-/Abflussprinzip), 21 Abs. 2 (verbilligte Vermietung); EStDV §82b (Erhaltungsaufwand Verteilung) |
| Tax authority | Finanzamt (local tax office) |
| Filing portal | ELSTER (elster.de) |
| Filing deadline | 31 July of the following year (with Steuerberater: end of February year after next) |
| Tax form | Anlage V (Einkünfte aus Vermietung und Verpachtung) to the Einkommensteuererklärung |
| Validated by | Pending — requires sign-off by a German Steuerberater |
| Skill version | 1.0 |

### Income Tax Rates (2025)

**Income Tax Rates (2025)**

| Taxable income (EUR) | Marginal rate |
| --- | --- |
| 0 -- 12,096 | 0% (Grundfreibetrag) |
| 12,097 -- 17,443 | 14% -- 24% (progressive zone 1) |
| 17,444 -- 66,760 | 24% -- 42% (progressive zone 2) |
| 66,761 -- 277,825 | 42% |
| 277,826+ | 45% (Reichensteuer) |

Plus Solidaritätszuschlag (5.5% of income tax, with Freigrenze of EUR 18,130 tax for singles / EUR 36,260 for married filing jointly) and Kirchensteuer (8% or 9% of income tax if applicable).

### Rental Income Formula

- **Rental Income Formula** — Einnahmen (gross rental income including Nebenkosten passed through) - Werbungskosten (deductible expenses: AfA, interest, repairs, insurance, etc.) = Einkünfte aus Vermietung und Verpachtung (net rental income/loss)

Net rental income is added to all other income and taxed at the personal marginal rate.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown building year (Baujahr) | STOP — AfA rate depends on this |
| Unknown Grundstücksanteil (land value) | STOP — land is not depreciable |
| Unknown whether Erhaltungsaufwand or Herstellungskosten | Treat as Herstellungskosten (capitalise, not immediately deduct) |
| Unknown verbilligte Vermietung percentage | STOP — affects Werbungskosten deductibility |
| Unknown whether commercial or residential | Treat as residential |

## Section 2 -- AfA Depreciation (§7 Abs. 4 EStG)

### 2.1 Linear AfA Rates

**Linear AfA Rates**  _(§7 Abs. 4 EStG)_

| Building type | Fertigstellung (completion) | AfA rate | Useful life |
| --- | --- | --- | --- |
| Residential (Wohngebäude) | After 31 December 2022 | 3% per year | 33⅓ years |
| Residential | 1 January 1925 -- 31 December 2022 | 2% per year | 50 years |
| Residential | Before 1 January 1925 | 2.5% per year | 40 years |
| Commercial (nicht Wohnzwecke) | Any date | 3% per year | 33⅓ years |

### 2.2 Degressive AfA (§7 Abs. 5a EStG)

- **Degressive AfA availability and rate** — For residential buildings with Bauantrag or Kaufvertrag from 1 October 2023: 5% degressive AfA in the first year (on remaining book value each subsequent year); switch to linear AfA (3%) permitted at any time; only for new construction (Neubau), not existing buildings.  _(§7 Abs. 5a EStG)_

### 2.3 AfA Basis (Bemessungsgrundlage)

- **AfA Basis (Bemessungsgrundlage)** — Purchase price (Anschaffungskosten) + Acquisition costs (Grunderwerbsteuer, Notar, Makler if buyer pays, Grundbuch) - Land value (Grundstücksanteil) — NOT depreciable = Gebäudeanteil (depreciable building value)

**Kaufpreisaufteilung:** The split between land and building is critical. Methods:
1. Contractually agreed split (if arm's length)
2. BMF Arbeitshilfe (official Excel tool from Bundesfinanzministerium)
3. Expert valuation (Gutachten)

The Finanzamt may challenge the split if the building proportion appears too high.

### 2.4 AfA Start

- **AfA start and pro-rata rule** — Begins in the month of acquisition (Anschaffung) or completion (Fertigstellung); pro-rata for the first year: annual AfA × (remaining months / 12); continues until fully depreciated or property is sold.

## Section 3 -- Werbungskosten (Deductible Expenses)

### 3.1 Fully Deductible Expenses

**Fully Deductible Expenses**

| Expense | German term | Notes |
| --- | --- | --- |
| Mortgage interest (Schuldzinsen) | Darlehenszinsen | Interest only — principal repayment is NOT deductible |
| AfA depreciation | Absetzung für Abnutzung | Per §7 Abs. 4 rates |
| Property tax | Grundsteuer | Annual property tax paid to municipality |
| Building insurance | Gebäudeversicherung | Fire, storm, water damage |
| Landlord liability insurance | Haus- und Grundbesitzerhaftpflicht |  |
| Property management | Hausverwaltung | Monthly management fees |
| Accountancy fees | Steuerberatungskosten | Attributable to Anlage V |
| Legal fees (tenancy disputes) | Rechtsanwaltskosten | Revenue legal costs |
| Advertising for tenants | Inseratskosten | Immobilienscout24, newspaper |
| Travel to property | Fahrtkosten | 0.30 EUR/km (one way) for property inspections |
| Bank account fees | Kontoführungsgebühren | If dedicated rental account |
| Condominium management reserve (Hausgeld -- Verwaltungsanteil) | Nicht umlagefähiges Hausgeld | Portion not passed to tenant |

### 3.2 Erhaltungsaufwand vs Herstellungskosten

**Erhaltungsaufwand vs Herstellungskosten**

| Erhaltungsaufwand (Revenue Repair) | Herstellungskosten (Capital Improvement) |
| --- | --- |
| Restores to original condition | Creates something new or substantially improves |
| Immediately deductible as Werbungskosten | Must be capitalised and depreciated via AfA |
| Option to spread over 2--5 years (§82b EStDV) | Added to AfA basis |
| Painting, replacing broken heating, fixing roof leak | Adding a balcony, converting attic, installing elevator |
| Replacing old windows with equivalent | Upgrading single glazing to triple glazing (if substantial improvement) |

- **15% Rule (Anschaffungsnahe Herstellungskosten)** — If repair/renovation costs within the first 3 years after acquisition exceed 15% of the building purchase price (net of VAT), they are reclassified as Herstellungskosten and must be capitalised — even if they would otherwise qualify as Erhaltungsaufwand.  _(§6 Abs. 1 Nr. 1a EStG)_

### 3.3 Non-Deductible Items

**Non-Deductible Items**

| Item | Reason |
| --- | --- |
| Principal repayments (Tilgung) | Loan repayment, not expense |
| Grunderwerbsteuer (on acquisition) | Part of acquisition cost (AfA basis) |
| Private living costs | Not related to rental activity |
| Fines / penalties (Bußgelder) | Public policy |
| Income tax itself | Tax on income |
| Hausgeld — tenant-reimbursable portion (umlagefähig) | Already passed through to tenant |

## Section 4 -- Verbilligte Vermietung (Reduced-Rent Letting, §21 Abs. 2 EStG)

**Verbilligte Vermietung thresholds**  _(§21 Abs. 2 EStG)_

| Actual rent as % of ortsübliche Marktmiete | Werbungskosten treatment |
| --- | --- |
| ≥66% of market rent | Full Werbungskosten deduction (treated as fully commercial) |
| 50% -- 65% of market rent | Full deduction ONLY if Totalüberschussprognose (lifetime profit forecast) is positive; otherwise proportional |
| <50% of market rent | Proportional split: entgeltlicher Teil (paid portion) gets Werbungskosten; unentgeltlicher Teil (free portion) does not |

- **Ortsübliche Marktmiete** — Determined from the local Mietspiegel (rent index), comparable rents, or expert valuation. It includes Kaltmiete (base rent) plus umlagefähige Nebenkosten (apportionable running costs).  _(§21 Abs. 2 EStG)_

## Section 5 -- Möblierungszuschlag (Furnished Premium)

If a property is let furnished:
- A Möblierungszuschlag (furniture surcharge) can be charged as part of the rent
- The surcharge counts towards the ortsübliche Marktmiete comparison (for §21 Abs. 2)
- The furniture itself can be depreciated: typically over 10 years (10% per year) or per actual useful life
- If the local Mietspiegel does not cover furnished lettings, the surcharge can be estimated based on the monthly AfA value of the furniture or a market-based percentage uplift

## Section 6 -- Transaction Pattern Library

### 6.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MIETE, KALTMIETE, MONATSMIETE | Rental income (Einnahmen) | Base rent — include in Anlage V |
| NEBENKOSTEN, BETRIEBSKOSTEN, HAUSGELD (tenant portion) | Rental income | Pass-through costs are income AND expense |
| NACHZAHLUNG NEBENKOSTEN | Rental income | Year-end settlement surplus from tenant |
| KAUTION, MIETKAUTION | EXCLUDE if refundable | Security deposit — not income unless retained |
| MÖBLIERUNGSZUSCHLAG | Rental income | Furniture premium — part of gross rent |

### 6.2 Expense Patterns (Debits)

**Expense Patterns (Debits)**

| Pattern | Category | Anlage V Line | Notes |
| --- | --- | --- | --- |
| DARLEHENSZINSEN, HYPOTHEKENZINSEN, BANKZINSEN | Schuldzinsen | Zeile 37 | Mortgage interest — fully deductible |
| GRUNDSTEUER | Grundsteuer | Zeile 47 | Municipal property tax |
| HAUSVERWALTUNG, VERWALTUNGSKOSTEN | Hausverwaltung | Zeile 47 | Management fee |
| GEBÄUDEVERSICHERUNG, WOHNGEBÄUDEVERSICHERUNG | Versicherung | Zeile 47 | Building insurance |
| REPARATUR, INSTANDHALTUNG, HANDWERKER | Erhaltungsaufwand | Zeile 40 | Revenue repairs (check 15% rule) |
| MAKLERGEBÜHR (tenant search) | Maklerkosten | Zeile 47 | Deductible when seeking new tenant |
| HAUSGELD (nicht umlagefähig) | Verwaltungskosten | Zeile 47 | Non-recoverable portion of condo charges |
| STEUERBERATER (Anlage V) | Steuerberatung | Zeile 47 | Tax advisor fees for rental income |
| GRUNDBUCH, NOTAR (mortgage refinancing) | Finanzierungskosten | Zeile 37 | Deductible if related to rental financing |
| GARTENPFLEGE, WINTERDIENST | Betriebskosten | Zeile 47 | If not recovered from tenant |
| FAHRTKOSTEN (to property) | Fahrtkosten | Zeile 47 | 0.30 EUR/km one way |

### 6.3 Exclusions

**Exclusions**

| Pattern | Treatment |
| --- | --- |
| TILGUNG, DARLEHENSRÜCKZAHLUNG | EXCLUDE — principal repayment |
| GRUNDERWERBSTEUER (on purchase) | Add to AfA basis — not immediate expense |
| INTERNAL TRANSFER, EIGENES KONTO | EXCLUDE |
| KAUTION RÜCKZAHLUNG | EXCLUDE — deposit refund |
| EINKOMMENSTEUER, KIRCHENSTEUER, SOLI | EXCLUDE — personal taxes |

## Section 7 -- Verlustverrechnung (Loss Offset)

**Verlustverrechnung (Loss Offset) rules**  _(§10d EStG)_

| Rule | Detail |
| --- | --- |
| Horizontal loss offset | Rental losses can offset other rental income in the same year |
| Vertical loss offset | Rental losses can offset OTHER income types (employment, self-employment) in the same year |
| Loss carry-back (Verlustrücktrag) | Up to EUR 1,000,000 (single) / EUR 2,000,000 (married jointly) to the prior year (§10d EStG) |
| Loss carry-forward (Verlustvortrag) | Unlimited carry-forward to future years; offset limited by Mindestbesteuerung (EUR 1M + 60% of excess) |
| Liebhaberei risk | If property shows losses year after year with no realistic prospect of profit, Finanzamt may classify as Liebhaberei (hobby) and deny deductions retroactively |

The ability to offset rental losses against salary income is a core feature of German Immobilien-Steuerplanung, especially in the early years when AfA + Schuldzinsen often exceed rental income.

## Section 8 -- Worked Examples

### Example 1 -- Standard Residential Letting (Post-2022 Building)

**Input:** Apartment completed January 2023. Purchase price EUR 400,000 (building EUR 300,000, land EUR 100,000). Annual rent (Kaltmiete + NK): EUR 14,400. Mortgage interest: EUR 8,000. Grundsteuer: EUR 600. Insurance: EUR 400. Hausverwaltung: EUR 1,200.

**Computation:**
```
Einnahmen:                    EUR 14,400
Werbungskosten:
  AfA (3% × EUR 300,000):    EUR 9,000
  Schuldzinsen:               EUR 8,000
  Grundsteuer:                EUR 600
  Versicherung:               EUR 400
  Hausverwaltung:             EUR 1,200
  Total Werbungskosten:       EUR 19,200

Einkünfte aus V+V:            EUR 14,400 - EUR 19,200 = EUR -4,800 (loss)
```
This EUR 4,800 loss can offset other income (salary, etc.), reducing the overall tax burden.

### Example 2 -- Older Building with Erhaltungsaufwand

**Input:** Building from 1965 (AfA 2%). Building value EUR 200,000. Rent EUR 9,600. New heating system (Heizungsanlage replacement): EUR 12,000 — like-for-like replacement = Erhaltungsaufwand. Owner elects to spread over 5 years (§82b EStDV).

**Computation:**
```
Einnahmen:                    EUR 9,600
Werbungskosten:
  AfA (2% × EUR 200,000):    EUR 4,000
  Erhaltungsaufwand (EUR 12,000 / 5): EUR 2,400
  Other expenses:             EUR 2,000
  Total:                      EUR 8,400

Einkünfte: EUR 9,600 - EUR 8,400 = EUR 1,200
```

### Example 3 -- Verbilligte Vermietung to Family Member

**Input:** Apartment let to daughter at EUR 400/month. Ortsübliche Marktmiete (Mietspiegel): EUR 700/month. Ratio: 400/700 = 57%.

**Analysis:** 57% is between 50% and 66%. A Totalüberschussprognose is required. If the lifetime profit forecast is positive, full Werbungskosten apply. If negative, only 57% of Werbungskosten are deductible.

### Example 4 -- Anschaffungsnahe Herstellungskosten (15% Rule)

**Input:** Property purchased for EUR 250,000 (building EUR 180,000). In Year 2, renovation costs of EUR 30,000 (bathroom + kitchen renovation).

**Test:** EUR 30,000 / EUR 180,000 = 16.7% > 15% threshold.

**Result:** Even if the renovation would otherwise be Erhaltungsaufwand, it is reclassified as Herstellungskosten. The EUR 30,000 is added to the AfA basis (EUR 180,000 + EUR 30,000 = EUR 210,000) and depreciated over the remaining useful life.

## Section 9 -- Edge Cases

### 9.1 Leerstand (Vacancy)

- **Vacancy deduction rule** — Werbungskosten remain deductible during vacancy periods if the owner has the demonstrable intention (Vermietungsabsicht) to re-let. Evidence: property listed on ImmoScout24, letting agent engaged, reasonable asking rent. Extended vacancy without evidence of marketing effort may lead the Finanzamt to deny deductions.

### 9.2 Ferienwohnung (Holiday Let)

- **Holiday let special rules** — Holiday apartments have special rules: the owner must prove Einkünfteerzielungsabsicht (intent to generate income) if the property is also used privately. If personal use exceeds what is typical, proportional restriction of Werbungskosten applies. Exclusively commercially let holiday apartments get full deductions.

### 9.3 Spekulationssteuer (10-Year Rule)

- **10-year speculation tax rule** — If a rental property is sold within 10 years of acquisition, the gain is taxable as privates Veräußerungsgeschäft (§23 EStG). After 10 years, the sale is tax-free. Self-occupied property (≥2 full calendar years + year of sale) is exempt regardless. This is not a rental income issue but is frequently relevant.  _(§23 EStG)_

### 9.4 Umsatzsteuer (VAT) on Commercial Lettings

- **VAT on commercial lettings** — Residential lettings are VAT-exempt. Commercial lettings can optionally be subject to VAT (19%) if the tenant uses the property for VAT-liable activities (§9 UStG option to tax). This allows the landlord to recover input VAT on renovation costs.  _(§9 UStG)_

## Section 10 -- Anlage V Key Lines

**Anlage V Key Lines**

| Zeile | Content |
| --- | --- |
| Zeile 4-6 | Property address and type |
| Zeile 9 | Mieteinnahmen für Wohnungen (residential rent) |
| Zeile 13 | Umlagen/Nebenkosten (pass-through costs received) |
| Zeile 31 | AfA für Gebäude |
| Zeile 33 | AfA für bewegliche Wirtschaftsgüter (furniture, equipment) |
| Zeile 37 | Schuldzinsen (mortgage interest) |
| Zeile 39 | Geldbeschaffungskosten (loan arrangement fees) |
| Zeile 40 | Erhaltungsaufwand (revenue repairs) |
| Zeile 41 | Verteilung Erhaltungsaufwand (spread over 2-5 years) |
| Zeile 46 | Hausgeld (non-recoverable condo charges) |
| Zeile 47 | Sonstige Werbungskosten (other deductible expenses) |
| Zeile 50 | Überschuss/Verlust (net income or loss) |

## PROHIBITIONS

- **Prohibitions list** — NEVER depreciate the land value (Grundstücksanteil) — only the building is depreciable NEVER apply the 3% AfA rate to buildings completed before 2023 — use 2% (or 2.5% for pre-1925) NEVER deduct mortgage principal repayments (Tilgung) — only interest is deductible NEVER immediately deduct renovation costs that exceed 15% of building value within 3 years of purchase — they must be capitalised NEVER allow full Werbungskosten for verbilligte Vermietung below 50% of market rent without proportional split NEVER ignore Liebhaberei risk for properties with persistent losses and no profit outlook NEVER present rental income computations as definitive — always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
