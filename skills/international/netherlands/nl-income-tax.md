---
name: nl-income-tax
description: Use this skill whenever asked about Netherlands income tax for self-employed individuals (zzp'ers). Trigger on phrases like "how much tax do I pay in the Netherlands", "aangifte inkomstenbelasting", "income tax return Netherlands", "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "Box 1 income", "Box 3 wealth tax", "heffingskortingen", "arbeidskorting", "KIA investment deduction", "self-employed tax Netherlands", or any question about filing or computing income tax for a Dutch zzp'er or eenmanszaak. Covers Box 1 progressive rates (36.97%/49.50%), entrepreneur deductions (zelfstandigenaftrek, startersaftrek, MKB-winstvrijstelling), urencriterium, tax credits (heffingskortingen, arbeidskorting), provisional assessment (voorlopige aanslag), and penalties.
version: 2.0
---

# Netherlands Income Tax — ZZP'er / Eenmanszaak (Inkomstenbelasting Box 1)

## Section 1 — Quick Reference

### Box 1 Tax Rates (2025)
| Belastbaar inkomen | Tarief |
|---|---|
| 0 – €75,518 | 36.97% |
| Above €75,518 | 49.50% |

**Note:** The 36.97% rate includes both income tax (inkomstenbelasting) and national insurance premiums (volksverzekeringen: AOW, ANW, WLZ). The 49.50% rate is pure income tax (national insurance capped at €75,518).

**AOW retirement age taxpayers (2025, born before 1960):** Lower combined rate on first bracket (~19.07% + 17.90% = 36.97% for those below AOW age; above AOW age: pay only income tax portion, not AOW premium — effectively lower rate on first bracket).

### Entrepreneur Deductions (Ondernemersaftrek) — Requires Urencriterium
| Deduction | Amount (2025) |
|---|---|
| Zelfstandigenaftrek | €2,470 (reduced annually; was €7,280 in 2020; phasing to €900 by 2027) |
| Startersaftrek (first 3 years) | Additional €2,123 on top of zelfstandigenaftrek |
| Meewerkaftrek (partner contribution) | 1.25%–4% of profit, depending on partner hours |
| Aftrek speur- en ontwikkelingswerk (R&D) | €14,202 + €7,101 starters supplement |

**MKB-winstvrijstelling:** 12.7% of profit after ondernemersaftrek — does NOT require urencriterium

### Urencriterium (1,225 Hours Rule)
- Minimum **1,225 hours** worked in the business in the tax year to qualify for zelfstandigenaftrek and startersaftrek
- Hours include all business activities: client work, admin, marketing, training, travel for business
- Must be able to substantiate with time records (urenregistratie)
- **Starting year:** If also employed (partially), the 1,225-hour test becomes a "more than half" rule (majority of working time in business)

### Heffingskortingen (Tax Credits — reduce final tax)
| Credit | Amount (2025) |
|---|---|
| Algemene heffingskorting (AHK) | Max €3,362 (phases out above €75,518) |
| Arbeidskorting | Max €5,532 (phases out above €43,071) |
| Jonggehandicaptenkorting (disability) | €887 |
| Inkomensafhankelijke combinatiekorting (IACK) | Max €2,950 (working parent with child <12) |
| Ouderenkorting (65+) | Up to €2,010 |
| Alleenstaande ouderenkorting | €524 |

**Note:** Arbeidskorting applies to self-employed profit (winst uit onderneming) — NOT just employment income.

### Conservative Defaults
| Item | Default |
|---|---|
| Urencriterium | Do not assume met — ask client for hour log |
| Home office % | Do not assume — ask for floor area |
| Vehicle | Do not assume business % — ask for km records or use forfait |
| Phone/internet | 50% if mixed use |
| Provisional assessment | Check with Belastingdienst if not already set up |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Profit > €75,518 | 49.50% rate kicks in — significant jump |
| Hours < 1,225 | No zelfstandigenaftrek or startersaftrek |
| Revenue approaching BTW threshold (€20,000) | KOR (kleineondernemersregeling) territory |
| Box 3 wealth > €57,000 | Vermogensrendementsheffing applies |
| More than 3 years in business | Startersaftrek no longer available |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross revenue (omzet) for the year
2. Deductible business expenses
3. Whether urencriterium is met (1,225+ hours — time records)
4. Whether first, second, or third year in business (startersaftrek check)
5. Personal situation: partner, children, other Box 1 income
6. Box 3 assets and debts (savings, investments, property) as of January 1
7. Voorlopige aanslag (provisional assessment) payments already made

### Refusal Catalogue
**R-NL-1 — Urencriterium not met**
If client worked < 1,225 hours in business: cannot claim zelfstandigenaftrek or startersaftrek. State: "Without meeting the 1,225-hour requirement, zelfstandigenaftrek and startersaftrek cannot be claimed. MKB-winstvrijstelling (12.7%) still applies without the urencriterium."

**R-NL-2 — No expense documentation**
Refuse undocumented business expenses. State: "Without receipts or records, we cannot deduct these as zakelijke kosten. The Belastingdienst requires documentation for all business expense deductions."

**R-NL-3 — Personal expenses as business costs**
Refuse personal costs. State: "These are privé-uitgaven and cannot be deducted as zakelijke kosten."

**R-NL-4 — BTW (VAT) included in revenue**
If BTW-registered: revenue figures must exclude BTW. State: "Omzet in your income tax return must be ex-BTW. Remove BTW from all revenue amounts before calculating profit."

**R-NL-5 — Startersaftrek beyond year 3**
If client is in their 4th year or beyond: no startersaftrek. State: "Startersaftrek is only available in the first three years of running a business. It is no longer applicable."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| Overboeking / SEPA credit + client | Omzet (business revenue) | Include ex-BTW | |
| Incasso van / SEPA Credit Transfer | Client payment | Include ex-BTW | |
| Internationale overb. / SWIFT | Foreign client | Include — convert to EUR at payment date | |
| Stripe storting / STRIPE | Platform receipt | Include net + add Stripe fees as cost | |
| PayPal overb. | Platform receipt | EUR equivalent | |
| Freelancer.com / Upwork | Freelance platform | Gross payment; platform fee = aftrekpost | |
| Rente credit | Bank interest | Box 3 — not Box 1 income | Separate |
| Huur ontvangen | Rental income | Box 3 (if not substantial) or Box 1 (if entrepreneurial) | Confirm categorisation |
| Verkoopprijs activa | Sale of business asset | Possible winst (profit) on sale — report | |
| Privé-stortingen | Owner contribution | EXCLUDE — not business income | |

### 3.2 Expense Patterns (Zakelijke Kosten)
| Bank Description Pattern | Kostencategorie | Aftrekbaar? | Opmerkingen |
|---|---|---|---|
| KPN / Odido / T-Mobile | Telefoon | Gedeeltelijk — zakelijk % | T2: bevestig % |
| Ziggo / KPN internet | Internet | Zakelijk % | T2 |
| Eneco / Vattenfall / Essent | Energie | Kantoor aan huis % | T2 |
| Huur woning (kantoor aan huis) | Huur | Beperkt aftrekbaar (zie T2) | T2 |
| Adobe / Figma / Notion / Slack | Software/SaaS | 100% | Zakelijk gebruik |
| Bol.com / Coolblue / MediaMarkt | Apparatuur | Afschrijving (>€450) of direct (<€450) | T2 kapitaalgoederen |
| NS / OV chipkaart | Reiskosten OV | 100% zakelijke reizen | Privé woon-werk: Forfait |
| Vliegticket / KLM / easyJet | Zakelijke vlucht | 100% — doel documenteren | |
| Hotel / Airbnb (zakelijk) | Verblijf | 100% zakelijk | |
| Restaurant (zakelijk diner client) | Representatiekosten | 80% aftrekbaar (WBSO of drempel) | T2 |
| Cursus / opleiding (zakelijk) | Scholingskosten | 100% — beroepsgerelateerd | |
| Boeken / vakliteratuur | Documentatie | 100% — beroepsgerelateerd | |
| Beroepsaansprakelijkheid (verzekering) | Verzekering | 100% | |
| Accountant / boekhouder | Professionele kosten | 100% | |
| Belasting (omzetbelasting / BTW) | BTW afdracht | GEEN — btw-aangifte apart | |
| Inkomstenbelasting | Belasting | GEEN — niet aftrekbaar | |
| KVK registratiekosten | KVK | Ja — eenmalige zakelijke kosten | |

### 3.3 Zakelijke Kilometers / Vehicle
| Method | Details |
|---|---|
| Forfaitaire kostenvergoeding (€0.23/km) | Apply to actual business km driven; no other vehicle costs deductible |
| Werkelijke kosten × zakelijk % | All vehicle costs × business km ÷ total km |
| Auto op naam zaak (business-owned car) | Full deduction of costs + bijtelling for private use |

**Private use bijtelling:** If car registered to business and used privately: add 16%–22% of list price as bijtelling income per year (afhankelijk van brandstof/emissie).

### 3.4 Foreign Currency
| Source | Currency | Treatment |
|---|---|---|
| USD client wire | USD | Convert to EUR at ECB rate on receipt date |
| GBP client | GBP | Convert at receipt date |
| Stripe USD | USD | Use Stripe EUR equivalent or convert at payout date |
| PayPal multi-currency | Various | PayPal statement EUR equivalent |
| Upwork USD | USD | Convert using DNB/ECB rate |

### 3.5 Internal Transfers
| Pattern | Treatment |
|---|---|
| Overboeking naar spaarrekening | EXCLUDE — privé-spaar |
| Privé-opname | EXCLUDE — owner drawing (not expense) |
| Creditcardafschrijving | EXCLUDE — afzonderlijke uitgaven al geboekt |
| Overb. tussen eigen rekeningen | EXCLUDE |

---

## Section 4 — Worked Examples

### Example 1 — ING: IT Consultant, Meets Urencriterium
**Scenario:** IT consultant (zzp'er), €95,000 omzet, €18,000 zakelijke kosten, urencriterium met, 3rd year (startersaftrek available)

**Bank statement extract (ING Zakelijk):**
```
Datum       | Omschrijving                                | Af (€)        | Bij (€)       | Saldo (€)
15-04-2025  | SEPA overboeking TechCorp BV               |               | 15,000.00     | 78,500.00
20-04-2025  | SEPA overboeking StartupNL                 |               |  8,000.00     | 86,500.00
25-04-2025  | iDEAL betaling Adobe Inc                   | 65.00         |               | 86,435.00
28-04-2025  | Automatische incasso KPN Zakelijk          | 89.00         |               | 86,346.00
30-04-2025  | ING transactiekosten                       | 12.50         |               | 86,333.50
```

**Winstberekening:**
| Regel | Bedrag |
|---|---|
| Omzet | €95,000 |
| Zakelijke kosten | (€18,000) |
| **Winst uit onderneming** | **€77,000** |
| Zelfstandigenaftrek | (€2,470) |
| Startersaftrek | (€2,123) |
| Winst na ondernemersaftrek | €72,407 |
| MKB-winstvrijstelling (12.7%) | (€9,196) |
| **Belastbaar inkomen Box 1** | **€63,211** |

**IB berekening:**
| Regel | Bedrag |
|---|---|
| Box 1 belasting: €63,211 × 36.97% | €23,373 |
| Algemene heffingskorting (AHK) | (€3,362) |
| Arbeidskorting (phases out above €43,071 — partial) | (€2,100 approx) |
| **Te betalen IB** | **~€17,911** |

### Example 2 — Rabobank: Designer, Eerste Jaar (Year 1)
**Scenario:** Designer, year 1 of business, €45,000 omzet, €8,000 kosten, startersaftrek available

**Bank statement extract (Rabobank Zakelijk):**
```
Datum       | Boekingsomschrijving                        | Debet (€)     | Credit (€)    | Saldo (€)
10-03-2025  | SEPA-betaling Studio Rood                  |               | 7,500.00      | 32,100.00
15-03-2025  | SEPA-betaling FashionBrand NL              |               | 4,000.00      | 36,100.00
20-03-2025  | Incasso Ziggo Zakelijk                     | 75.00         |               | 36,025.00
22-03-2025  | Pinbetaling MediaMarkt apparatuur          | 650.00        |               | 35,375.00
28-03-2025  | Rabobank servicekosten                     | 9.50          |               | 35,365.50
```

**Winstberekening:**
| Regel | Bedrag |
|---|---|
| Omzet | €45,000 |
| Kosten | (€8,000) |
| Winst | €37,000 |
| Zelfstandigenaftrek | (€2,470) |
| Startersaftrek | (€2,123) |
| Winst na aftrek | €32,407 |
| MKB-winstvrijstelling (12.7%) | (€4,116) |
| **Belastbaar Box 1** | **€28,291** |
| IB: €28,291 × 36.97% | €10,461 |
| AHK (max) | (€3,362) |
| Arbeidskorting (partially phased) | (€3,800 approx) |
| **Te betalen IB** | **~€3,299** |

### Example 3 — ABN AMRO: Developer, No Urencriterium (Hobby/Side Business)
**Scenario:** Developer, side income alongside employment, 800 hours in freelance (below 1,225), €30,000 omzet, €5,000 kosten

**Bank statement extract (ABN AMRO Zakelijk):**
```
Datum       | Omschrijving                                | Bedrag (€)    | Saldo (€)
08-05-2025  | Bijschrijving TechConsult BV               | +12,000.00    | 48,000.00
12-05-2025  | Bijschrijving App Dev Project              | +8,000.00     | 56,000.00
15-05-2025  | Afschrijving AWS Amazon                    | -380.00       | 55,620.00
20-05-2025  | Afschrijving GitHub Enterprise             | -200.00       | 55,420.00
25-05-2025  | ABN AMRO bankkosten zakelijk               | -15.00        | 55,405.00
```

**Without urencriterium:**
| Regel | Bedrag |
|---|---|
| Omzet | €30,000 |
| Kosten | (€5,000) |
| Winst | €25,000 |
| Zelfstandigenaftrek | ~~NOT APPLICABLE — <1,225 hours~~ | €0 |
| Startersaftrek | NOT APPLICABLE | €0 |
| MKB-winstvrijstelling (12.7%) | (€3,175) |
| **Belastbaar Box 1** | **€21,825** |

**If also employed:** This income adds to employment income; total Box 1 determines marginal rate.

### Example 4 — SNS Bank: Consultant met Kantoor aan Huis
**Scenario:** Consultant, €70,000 omzet, €12,000 directe kosten, kantoor thuis (huis 110m², kantoor 18m²)

**Bank statement extract (SNS Bank Zakelijk):**
```
Datum       | Omschrijving                                | Debet (€)     | Credit (€)    | Saldo (€)
05-06-2025  | Overboeking McKinsey NL                   |               | 22,000.00     | 95,000.00
10-06-2025  | Overboeking StartupFactory                |               |  8,500.00     | 103,500.00
15-06-2025  | Automatische incasso Eneco Energie         | 285.00        |               | 103,215.00
20-06-2025  | Huur woning (SEPA Debet LL)               | 2,100.00      |               | 101,115.00
25-06-2025  | Pinbetaling HEMA kantoorspullen           | 78.50         |               | 101,036.50
```

**Kantoor aan huis — aftrekbaarheid:**
De aftrek voor een kantoor aan huis is sterk beperkt in NL. Alleen aftrekbaar als:
1. Het kantoor een zelfstandige ingang en sanitair heeft (zelfstandig gedeelte), OR
2. Het gebruikt wordt door een huurder (niet van toepassing hier)

**Praktisch:** De meeste zzp'ers kunnen de huur thuis NIET aftrekken. Wel aftrekbaar: extra energiekosten × zakelijk %.

**Winstberekening:**
| Regel | Bedrag |
|---|---|
| Omzet | €70,000 |
| Directe kosten | (€12,000) |
| Extra energie zakelijk (€3,420 × 16.4%) | (€561) |
| Huur thuis | €0 (niet aftrekbaar zonder zelfstandig gedeelte) |
| Winst | €57,439 |
| Zelfstandigenaftrek | (€2,470) |
| MKB-winstvrijstelling (12.7%) | (€6,984) |
| **Belastbaar Box 1** | **€47,985** |
| IB: €47,985 × 36.97% | €17,740 |
| AHK + Arbeidskorting (approx.) | (€6,400) |
| **Te betalen IB** | **~€11,340** |

### Example 5 — Triodos Bank: Schrijver/Creatief met KIA
**Scenario:** Freelance schrijver, €38,000 omzet, €6,000 kosten, koopt laptop €2,200 (KIA investeringsaftrek)

**Bank statement extract (Triodos Zakelijk):**
```
Datum       | Omschrijving                                | Debet (€)     | Credit (€)    | Saldo (€)
12-07-2025  | Overboeking Uitgeverij de Geus             |               | 6,000.00      | 22,400.00
18-07-2025  | Overboeking Tijdschrift NRC               |               | 3,500.00      | 25,900.00
22-07-2025  | Pinbetaling Apple Store MacBook Pro        | 2,200.00      |               | 23,700.00
26-07-2025  | Automatische incasso Odido               | 55.00         |               | 23,645.00
30-07-2025  | Triodos banktransactiekosten              | 8.00          |               | 23,637.00
```

**KIA — Kleinschaligheidsinvesteringsaftrek:**
- Investering €2,200 kwalificeert (≥ €2,901 drempel voor volle scale, maar geldt al bij totaal zakelijke investeringen > €2,901 — als totaal > €2,901 dan 28% aftrek)
- Als totaal zakelijke investeringen dit jaar = €2,200: net below threshold → check of andere investeringen ook in jaar vallen
- Boven €2,901 investering totaal: KIA = 28% × investering

**Winstberekening (met KIA aanname €2,901+ totaal):**
| Regel | Bedrag |
|---|---|
| Omzet | €38,000 |
| Directe kosten (excl. laptop) | (€6,000) |
| Afschrijving laptop (3 jr: €2,200÷3) | (€733) |
| KIA (28% × €2,200) | (€616) |
| Winst | €30,651 |
| Zelfstandigenaftrek | (€2,470) |
| MKB-winstvrijstelling (12.7%) | (€3,574) |
| **Belastbaar Box 1** | **€24,607** |

### Example 6 — Bunq (Online Bank): Developer, Voorlopige Aanslag
**Scenario:** Developer, €115,000 omzet, €25,000 kosten, reeds €15,000 voorlopige aanslag betaald

**Bank statement extract (Bunq Zakelijk):**
```
Date        | Description                                 | Out (€)       | In (€)        | Balance (€)
03-08-2025  | SEPA credit from ClientA BV                |               | 28,000.00     | 185,000.00
10-08-2025  | SEPA credit from Software House            |               | 12,000.00     | 197,000.00
15-08-2025  | SEPA debit Belastingdienst voorl. aanslag  | 7,500.00      |               | 189,500.00
20-08-2025  | SEPA debit Slack Technologies             | 240.00        |               | 189,260.00
25-08-2025  | SEPA debit bunq subscription               | 19.99         |               | 189,240.01
```

**Winstberekening:**
| Regel | Bedrag |
|---|---|
| Omzet | €115,000 |
| Kosten | (€25,000) |
| Winst | €90,000 |
| Zelfstandigenaftrek | (€2,470) |
| Winst na aftrek | €87,530 |
| MKB-winstvrijstelling (12.7%) | (€11,116) |
| **Belastbaar Box 1** | **€76,414** |
| IB: €75,518 × 36.97% + (€76,414−75,518) × 49.50% | €27,924 + €444 = **€28,368** |
| AHK (phased out above €75,518) | ~€0 |
| Arbeidskorting | (min amount) |
| Voorlopige aanslag betaald | (€15,000) |
| **Te betalen bij aangifte** | **~€13,368** |

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Fiscale Woonplaats
- **Inwoner NL:** Duurzame band met Nederland (woning, gezin, werk) → worldwide inkomen belast
- **Niet-inwoner:** Alleen Nederlands-bron inkomen belast; aparte regels (buitenlandse belastingplichtige)

### Box Systeem
| Box | Inkomen | Tarief |
|---|---|---|
| Box 1 | Werk en woning (winst onderneming, arbeid, eigen woning) | 36.97% / 49.50% |
| Box 2 | Aanmerkelijk belang (≥5% aandelen eigen BV) | 24.5% / 31% (2024: tiered) |
| Box 3 | Spaargeld en beleggingen | Forfaitair (fictief rendement × 32%) |

### BTW en Inkomstenbelasting
- BTW (omzetbelasting): aparte aangifte; omzet inclusief BTW op bankrekening → altijd BTW eraf halen voor IB
- KOR: omzet < €20,000 → vrijstelling BTW mogelijk (geen BTW op facturen, geen aftrek)

### Afschrijvingen
| Activum | Minimale afschrijvingstermijn |
|---|---|
| Computer / laptop | 3 jaar (minimaal) |
| Bedrijfsauto | 5 jaar |
| Inventaris | 5–10 jaar |
| Goodwill | 10 jaar |
| Gebouwen (eigen) | Beperkt — afhankelijk WOZ-waarde |

### Fiscale Oudedagsreserve (FOR) — Afgeschaft
- FOR per 2023 niet meer op te bouwen voor nieuwe gevallen
- Bestaande FOR-stands: blijven staan, maar geen toevoeging meer

### Lijfrentepremie Aftrek
- Zelfstandigen kunnen lijfrentepremies aftrekken als pensioenopbouw via jaarruimte/reserveringsruimte
- Jaarruimte: 30% × (inkomen − drempelinkomen) − pensioenaangroei
- Vervangt de afgeschafte FOR

### Aangifte Deadlines
| Gebeurtenis | Deadline |
|---|---|
| Aangifte inkomstenbelasting | 1 mei (verlengbaar op verzoek) |
| Voorlopige aanslag aanpassen | Gedurende het jaar via Mijn Belastingdienst |
| Bezwaar tegen aanslag | 6 weken na dagtekening aanslag |

### Boetes en Rente
| Situatie | Boete |
|---|---|
| Te late aangifte | €68 (first offence) → oplopend |
| Opzettelijk onjuiste aangifte | Tot 100% van ontdoken belasting |
| Belastingrente | 7.5% per jaar (2025) |

---

## Section 6 — Tier 2 Catalogue

### T2-NL-1: Kantoor aan Huis
**Waarom T2:** De aftrekbaarheid hangt af van de fysieke inrichting — alleen de klant weet dit.

**Strikte voorwaarden voor aftrek:**
1. **Zelfstandig gedeelte:** Eigen ingang + eigen sanitair = zelfstandig → dan marktconforme huur aftrekbaar
2. **Niet-zelfstandig:** Bureau in woonkamer / slaapkamer → niet aftrekbaar
3. **Verhuurde werkkamer:** Als klant ruimte verhuurt aan eigen bedrijf → complex, structuur vereist advies

**Praktisch advies:** De meeste zzp'ers die thuis werken kunnen de huurkosten NIET aftrekken. Wel aftrekbaar: extra energiekosten pro rata zakelijk gebruik.

**Nodig van klant:** Soort kantaalruimte (eigen ingang + sanitair?), oppervlaktes, maandelijkse huur, jaarlijkse energiekosten.

### T2-NL-2: Auto (Zakelijk vs Privé)
**Waarom T2:** Rijgedrag en zakelijk/privé-splitsing zijn klantspecifiek.

**Opties:**
1. **Forfait €0.23/km:** Eenvoudig; houd zakelijke km bij; geen andere autokosten aftrekbaar
2. **Werkelijke kosten × zakelijk %:** km-registratie vereist; hogere aftrek bij hoge kosten
3. **Auto op naam van zaak:** Volle kostenaftrek + bijtelling voor privégebruik (16–22% cataloguswaarde)

**Nodig van klant:** Totaal km, zakelijk km, kenteken auto, brandstof, of auto op eigen naam of naam zaak staat.

### T2-NL-3: Telefoon & Internet
**Waarom T2:** Verdeling privé/zakelijk is klantspecifiek.

**Richtlijn:**
- Zakelijke telefoonabonnement: 100%
- Privételefoon ook zakelijk gebruikt: schatting zakelijk %, max 80%
- Internet thuis: zakelijk % (of max 50% als mede-thuiswerker)

### T2-NL-4: Representatiekosten (Zakelijke Maaltijden)
**Waarom T2:** Aanwezigheid van client en zakelijk karakter moet van klant komen.

**Regelgeving:** 80% van representatiekosten aftrekbaar (WBSO-drempel vervallen; nu 80% direct)
- Maaltijden met cliënten: 80% aftrekbaar, mits zakelijk doel gedocumenteerd
- Maaltijden alleen: niet aftrekbaar als representatie

**Nodig van klant:** Wie aanwezig, wat besproken, ontvangstbewijzen.

### T2-NL-5: Urenregistratie (Urencriterium Onderbouwing)
**Waarom T2:** Uren zijn een klantspecifiek gegeven — essentieel voor zelfstandigenaftrek.

**Vereiste documentatie:**
- Dagelijks of wekelijks bijgehouden urenadministratie
- Categorieën: klantwerk, acquisitie, administratie, marketing, opleiding, reistijd zakelijk
- Belastingdienst kan urenregistratie opvragen bij controle

**Nodig van klant:** Urenregistratie over het gehele jaar (minimaal 1,225 uur aangetoond).

---

## Section 7 — Excel Working Paper

### Blad 1: Omzet
| Kolom | Inhoud |
|---|---|
| A | Datum |
| B | Klant |
| C | Factuurnummer |
| D | Bedrag ex-BTW (€) |
| E | BTW |
| F | Totaal incl. BTW |
| G | Categorie (Omzet / Anders / Uitsluiten) |

**Totale omzet ex-BTW:** `=SUMIF(G:G,"Omzet",D:D)`

### Blad 2: Zakelijke Kosten
| Kolom | Inhoud |
|---|---|
| A | Datum |
| B | Leverancier |
| C | Bedrag ex-BTW (€) |
| D | Categorie |
| E | Zakelijk % |
| F | Aftrekbaar bedrag (=C×E) |
| G | Bonreferentie |

### Blad 3: Winstberekening
| Regel | Bedrag |
|---|---|
| Omzet | |
| Zakelijke kosten | |
| Afschrijvingen | |
| KIA | |
| **Winst uit onderneming** | |
| Zelfstandigenaftrek (indien van toepassing) | |
| Startersaftrek (indien van toepassing) | |
| MKB-winstvrijstelling (12.7%) | |
| **Belastbaar inkomen Box 1** | |

### Blad 4: IB Berekening
| Regel | Bedrag |
|---|---|
| Box 1 inkomen | |
| IB (36.97% / 49.50%) | |
| AHK | |
| Arbeidskorting | |
| Overige kortingen | |
| **IB netto** | |
| Voorlopige aanslag betaald | |
| **Verschuldigd / terug** | |

---

## Section 8 — Bank Statement Reading Guide

### ING Zakelijk
- Format: `Datum | Omschrijving | Af (€) | Bij (€) | Saldo (€)`
- Date: DD-MM-YYYY
- Income = Bij (credit) column
- "SEPA overboeking" = bank transfer; "Bijschrijving" = credit

### Rabobank Zakelijk
- Format: `Datum | Boekingsomschrijving | Debet (€) | Credit (€) | Saldo (€)`
- Date: DD-MM-YYYY
- Income = Credit column

### ABN AMRO Zakelijk
- Format: `Datum | Omschrijving | Bedrag (€) | Saldo (€)` — single amount; positive = credit, negative = debit
- Date: DD-MM-YYYY
- "Bijschrijving" = incoming; "Afschrijving" = outgoing

### SNS Bank Zakelijk
- Format: `Datum | Omschrijving | Debet (€) | Credit (€) | Saldo (€)`
- Date: DD-MM-YYYY

### Triodos Zakelijk
- Format: `Datum | Omschrijving | Debet (€) | Credit (€) | Saldo (€)`
- Date: DD-MM-YYYY

### Bunq Zakelijk
- Format: `Date | Description | Out (€) | In (€) | Balance (€)`
- Date: DD-MM-YYYY (may use English)
- Income = In column

### Exclusion Patterns (all Dutch banks)
| Pattern | Action |
|---|---|
| Overb. naar eigen spaarrekening | UITSLUITEN — privé-spaar |
| Privé-opname | UITSLUITEN — opname eigenvermogen |
| BTW-afdracht Belastingdienst | UITSLUITEN — BTW-aangifte apart |
| Voorlopige aanslag IB betaling | UITSLUITEN van kosten — wordt verrekend aangifte |
| Creditcardafschrijving | UITSLUITEN — afzonderlijke uitgaven al geboekt |
| Lening ontvangst | UITSLUITEN — niet omzet |

---

## Section 9 — Onboarding Fallback

**Prioriteit 1 (blokkerend):**
1. "Wat was je totale omzet (excl. BTW) in het afgelopen jaar?"
2. "Hoeveel uur heb je aan je bedrijf gewerkt — haal je de 1.225 uur?"
3. "Is dit je eerste, tweede of derde jaar als ondernemer?"

**Prioriteit 2 (voor nauwkeurige berekening):**
4. "Heb je bonnen en facturen voor alle zakelijke kosten?"
5. "Werk je thuis? Heeft je werkruimte een eigen ingang en sanitair?"
6. "Gebruik je een auto voor zakelijke ritten? Hoeveel zakelijke km per jaar?"
7. "Heb je grotere investeringen gedaan (>€2.901) in machines of apparatuur?"

**Prioriteit 3 (extra aftrekposten):**
8. "Heb je al een voorlopige aanslag ontvangen / betaald? Hoeveel?"
9. "Heb je gestort in een lijfrenteverzekering of bankspaarrekening?"
10. "Heb je een partner / kinderen?"

**Conservatieve aanpak:**
- Neem aan dat urencriterium niet gehaald is als geen registratie beschikbaar
- Sluit thuiswerkruimte uit als niet zelfstandig gedeelte bevestigd
- Gebruik forfait €0.23/km voor auto als geen km-registratie

---

## Section 10 — Reference Material

### Aangifteplatform
- **Mijn Belastingdienst:** belastingdienst.nl — DigiD inloggen
- **Boekhoudpakketten:** Moneybird, e-Boekhouden, Exact Online — meeste integreren direct met IB-aangifte

### Key Forms
| Formulier | Doel |
|---|---|
| Aangifte Inkomstenbelasting | Jaarlijkse belastingaangifte (IB) |
| Voorlopige aanslag | Periodieke betaling gedurende het jaar |
| Suppletie BTW | Correctie BTW-aangifte |

### Handige Links
- Belastingdienst: belastingdienst.nl
- KvK (Kamer van Koophandel): kvk.nl
- Urenregistratie tools: Toggl, Clockify, Harvest

---

## Prohibitions
- Do not advise on BTW (omzetbelasting / VAT) filing or calculation — separate Dutch BTW skill required
- Do not advise on BV / vennootschapsbelasting (corporate tax) — this skill covers eenmanszaak / zzp'ers only
- Do not advise on Box 3 wealth tax computation in detail — confirm assets and liabilities with client; Box 3 has complex new rules post-2021 Kerstarrest
- Do not advise on payroll tax (loonbelasting) for employees
- Do not advise on inheritance or gift tax (schenk- en erfbelasting)

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. Dutch tax law is administered by the Belastingdienst (Dutch Tax and Customs Administration). Clients should consult a registered belastingadviseur or accountant for advice specific to their circumstances. Tax brackets, deductions, and credits change annually — verify current rules at belastingdienst.nl.
