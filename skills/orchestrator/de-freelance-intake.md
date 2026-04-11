---
name: de-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their German tax returns AND mentions freelancing (Freiberufler), self-employment (Selbstständigkeit), trade business (Gewerbetreibender), contracting, or sole proprietorship (Einzelunternehmer). Trigger on phrases like "help me do my German taxes", "prepare my EStE", "I'm self-employed in Germany", "I'm a Freiberufler", "do my Steuererklärung", "prepare my USt and ESt", or any similar phrasing where the user is a Germany-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Germany self-employed tax workflow -- every other skill in the stack (germany-vat-return, de-income-tax, de-social-contributions, de-trade-tax, de-estimated-tax, de-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Germany full-year residents only; self-employed individuals and sole proprietors.
version: 0.1
---

# Germany Self-Employed Intake Skill v0.1

## What this file is

The intake orchestrator for Germany-resident self-employed individuals (Freiberufler and Gewerbetreibende). Every downstream Germany content skill (germany-vat-return, de-income-tax, de-social-contributions, de-trade-tax, de-estimated-tax) and the assembly orchestrator (de-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `de-return-assembly`.

---

## Design principles

v0.1 follows the same upload-first, inference-then-confirm pattern as mt-freelance-intake v0.1:

1. **Compact refusal sweep** using `ask_user_input_v0` -- 3-5 interactive questions, ~30 seconds.
2. **Upload-first workflow** -- after the refusal check, the user dumps everything they have.
3. **Inference pass** -- Claude parses every document and extracts as much as possible.
4. **Gap-filling only** -- Claude asks the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end -- show the full picture, let the user correct anything wrong, hand off to downstream skills.

Target: intake completes in 5 minutes for a prepared user, 15 minutes for a user who has to go fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user is Regelbesteuert, do not later ask about VAT status. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows quarterly Vorauszahlungen to the Finanzamt, do not ask "did you pay estimated tax." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

---

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by Steuerberater before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 German returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a Steuerberater before you file anything with the Finanzamt. I'm not a substitute for professional review.
>
> Scope check:

Then immediately call `ask_user_input_v0` with the refusal questions.

**Do NOT:**
- Write a welcome paragraph
- Explain the phases
- Ask "are you ready to start"
- List what documents you will eventually need
- Give a disclaimer beyond the one reviewer line

---

## Section 2 -- Refusal sweep (compact)

Present the refusal sweep as a single `ask_user_input_v0` call with 3 questions, all single-select.

**The 3 questions to ask first:**

```
Q1: "Germany residency in 2025?"
    Options: ["Full year (unbeschränkt steuerpflichtig)", "Part year", "Did not live in Germany"]

Q2: "Business structure?"
    Options: ["Freiberufler (§18 EStG -- liberal profession)", "Gewerbetreibender (§15 EStG -- trade/business)", "GbR / Partnership", "GmbH / UG / Kapitalgesellschaft", "Not sure"]

Q3: "VAT status?"
    Options: ["Regelbesteuerung (standard VAT -- charge and reclaim USt)", "Kleinunternehmer §19 UStG (no VAT charged, under EUR 22,000)", "Not sure"]
```

**After the response, evaluate:**

- **Q1 = Full year** -> continue
- **Q1 = Part year or did not live in Germany** -> stop. "I'm set up for full-year German residents (unbeschränkt steuerpflichtig) only. Part-year or non-residents have different rules around beschränkte Steuerpflicht. You need a Steuerberater who handles non-resident returns."

- **Q2 = Freiberufler** -> continue. No Gewerbesteuer applies.
- **Q2 = Gewerbetreibender** -> continue with a flag: Gewerbesteuer applies, will need Hebesatz for the municipality.
- **Q2 = GbR / Partnership** -> stop. "Partnerships file a separate Feststellungserklärung with different rules for profit allocation. You need a Steuerberater familiar with partnership returns."
- **Q2 = GmbH / UG / Kapitalgesellschaft** -> stop. "I don't cover corporate returns. Kapitalgesellschaften file KStE and GewStE with separate rules. You need a Steuerberater."
- **Q2 = Not sure** -> ask one follow-up: "What is your main activity? Freiberufler covers professions like software development, consulting, writing, design, medicine, law, engineering (Katalogberufe under §18 EStG). Gewerbetreibender covers trade, retail, manufacturing, or anything not listed under §18. If your Finanzamt issued a Gewerbeschein, you're Gewerbetreibender."

- **Q3 = Regelbesteuerung** -> continue. Standard UStVA monthly/quarterly.
- **Q3 = Kleinunternehmer** -> continue. No UStVA filing required (unless voluntarily opted in). Turnover must stay under EUR 22,000 prior year / EUR 50,000 current year.
- **Q3 = Not sure** -> ask one follow-up: "Do you charge 19% (or 7%) USt on your invoices? If yes, you're Regelbesteuert. If your invoices say 'Kleinunternehmer gemäß §19 UStG' or show no USt, you're Kleinunternehmer."

**After Q1-Q3 pass, ask the second batch of scope questions (also batched):**

```
Q4: "Employees?"
    Options: ["No employees", "1-5 employees", "More than 5 employees"]

Q5: "Partnerships or joint ventures?"
    Options: ["None -- I operate alone", "I'm a partner in a GbR or other partnership alongside this business", "Not sure"]
```

**Evaluate Q4:**
- **No employees** -> continue
- **1-5 employees** -> continue with a flag: Lohnsteuer obligations exist but are out of scope for this workflow. Flag for Steuerberater review.
- **More than 5** -> stop. "I'm set up for sole operators and very small businesses. With more than 5 employees, the payroll and Lohnsteuer complexity requires a dedicated Steuerberater."

**Evaluate Q5:**
- **None** -> continue
- **Partner in a GbR** -> continue with a flag: partnership income will appear in the Feststellungsbescheid and needs to be entered in Anlage S or Anlage G. Will address during gap-filling.
- **Not sure** -> ask one follow-up: "Do you share business income with another person or file a joint business return (Feststellungserklärung)? If not, you operate alone."

**Total time:** ~45 seconds if the user taps through.

---

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2025 -- drop it all in at once:
>
> - Business Kontoauszüge (bank statements) for all of 2025 (CSV or PDF)
> - Ausgangsrechnungen (sales invoices) issued in 2025
> - Eingangsrechnungen (purchase invoices / receipts) for business expenses
> - Prior year Steuerbescheid (tax assessment notice from the Finanzamt)
> - Vorauszahlungsbescheide (estimated tax payment notices)
> - Prior UStVA filings for 2025 (if Regelbesteuert)
> - EÜR from prior year (Anlage EÜR)
> - Krankenversicherung (health insurance) annual statement (Beitragsbescheinigung)
> - Any Finanzamt correspondence
> - Capital asset purchase receipts (computers, equipment, vehicles)
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2025 statements as PDF or CSV
> - Email: search for "Rechnung", "Steuerbescheid", "Vorauszahlung", "Finanzamt", "Krankenkasse"
> - ELSTER portal (elster.de): download prior returns and Steuerbescheide
> - Your Steuerberater from last year, if you had one
> - Dropbox / Google Drive for saved invoices
> - Krankenkasse portal: download Beitragsbescheinigung
>
> Come back when you have something to upload. I'll work with whatever you bring.

---

## Section 4 -- The inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement (Kontoauszüge):**
- Total deposits (candidate Betriebseinnahmen)
- Recurring inflows (client payments with names)
- Outflows to Finanzamt (Vorauszahlungen ESt/SolZ/KiSt with dates)
- Outflows to Finanzamt (USt-Vorauszahlungen with dates)
- Outflows to Krankenkasse GKV or PKV (health insurance premiums)
- Outflows to Rentenversicherung (if voluntary or Pflichtversichert via Künstlersozialkasse)
- Equipment purchases (potential Anlagevermögen)
- Transfers to personal account (Privatentnahmen)
- Office rent payments (Büromiete)
- SaaS / software subscriptions
- Professional memberships (IHK Beiträge, Berufsverband)
- Insurance payments (Berufshaftpflicht, Kfz)
- Telefon / Internet payments
- Kfz expenses (fuel, maintenance, leasing)

**Sales invoices (Ausgangsrechnungen):**
- Client names and amounts (netto + USt)
- Whether USt was charged (Regelbesteuerung indicator)
- Whether invoices say "Kleinunternehmer §19 UStG" (Kleinunternehmer indicator)
- Total Umsatz reconciliation against bank deposits
- Any EU clients (innergemeinschaftliche Leistung -- reverse charge)
- Any non-EU clients (Drittlandsleistung -- §3a UStG)
- Proper invoice format check (§14 UStG requirements)

**Purchase invoices (Eingangsrechnungen):**
- Expense category (Betriebsausgaben, Anlagevermögen, durchlaufende Posten)
- Vorsteuer amount on each (reclaimable for Regelbesteuert, cost for Kleinunternehmer)
- Supplier location (inland, EU, Drittland)
- Any items over EUR 800 netto (GWG threshold for immediate write-off) or over EUR 250 (Pool-Abschreibung)
- Any blocked categories (Bewirtungskosten 70% limit, Geschenke EUR 50 limit)

**Prior year Steuerbescheid:**
- Prior year festgesetzte Einkommensteuer (drives Vorauszahlungen)
- Prior year Solidaritätszuschlag
- Prior year Kirchensteuer (if applicable)
- Any Nachzahlung or Erstattung
- Vorauszahlungen festgesetzt for current year

**Vorauszahlungsbescheide:**
- Quarterly ESt Vorauszahlungen (10 Mar, 10 Jun, 10 Sep, 10 Dec)
- SolZ amounts
- KiSt amounts (if applicable)

**Prior EÜR (Anlage EÜR):**
- Prior year Betriebseinnahmen and Betriebsausgaben
- Prior year Gewinn
- Capital allowances schedule (AfA-Tabelle -- continuing depreciation)
- Any Sonderabschreibung §7g used

**Krankenversicherung Beitragsbescheinigung:**
- Annual GKV or PKV premiums paid
- Basisabsicherung amount (deductible under §10 EStG as Sonderausgaben)
- Pflegeversicherung amount
- Any Zusatzbeiträge

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

---

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Max Mustermann, single
> - Full-year Germany resident (Berlin)
> - Freiberufler (Software-Entwickler), sole proprietor
> - VAT: Regelbesteuerung (USt-IdNr. DE123456789)
>
> **Umsatz (from bank statement + invoices)**
> - Betriebseinnahmen (netto): ~EUR 85,000
>   - TechCorp GmbH: EUR 48,000 (monthly retainer)
>   - StartupAG: EUR 25,000 (project work)
>   - Various smaller clients: EUR 12,000
> - USt collected (19%): ~EUR 16,150
> - EU reverse charge clients: EUR 8,000 (innergemeinschaftliche Leistung)
>
> **Betriebsausgaben (from bank statement + purchase invoices)**
> - Büromiete: EUR 6,000
> - Software / SaaS: EUR 2,400
> - Berufshaftpflicht: EUR 600
> - Steuerberater Vorjahr: EUR 1,200
> - Telefon / Internet: EUR 960 (TBD -- need business use %)
> - Kfz: EUR 3,600 fuel + EUR 800 maintenance (TBD -- need business use % or Fahrtenbuch)
> - MacBook Pro EUR 2,200 netto (April 2025) -- GWG? No, over EUR 800 -> AfA 3 years
> - Vorsteuer auf Eingangsrechnungen: ~EUR 2,300 (reclaimable)
>
> **Sozialversicherung (from Beitragsbescheinigung / bank statement)**
> - GKV (TK): EUR 8,400/year (Basisabsicherung EUR 7,200 + Zusatzbeitrag EUR 1,200)
> - Pflegeversicherung: EUR 1,800/year
> - Rentenversicherung: not detected (freiwillig?)
>
> **Vorauszahlungen (from Vorauszahlungsbescheid / bank statement)**
> - ESt Vorauszahlungen: EUR 2,500 x 4 = EUR 10,000
> - SolZ: EUR 0 (under Freigrenze)
> - KiSt: not detected
>
> **Prior year (from 2024 Steuerbescheid)**
> - 2024 festgesetzte ESt: EUR 12,000
> - 2024 Gewinn aus selbständiger Arbeit: EUR 42,000
> - 2024 AfA-Tabelle: EUR 733 continuing depreciation
>
> **USt (from prior UStVA filings)**
> - Jan-Nov 2025 UStVA filed
> - December UStVA outstanding
> - Dauerfristverlängerung: yes (1/11 Sondervorauszahlung paid)
>
> **Flags I already see:**
> 1. Telefon / Internet -- need business use percentage
> 2. Kfz -- need business use percentage or Fahrtenbuch (1%-Regelung vs Fahrtenbuch)
> 3. MacBook Pro EUR 2,200 netto -- over GWG EUR 800, AfA über 3 Jahre (Nutzungsdauer lt. AfA-Tabelle)
> 4. December 2025 UStVA not yet filed -- will prepare as part of this workflow
> 5. No Rentenversicherung detected -- voluntary contributions?
> 6. Kirchensteuer status unclear
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

---

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Arbeitszimmer (home office)** -- Cannot tell from documents whether a dedicated Arbeitszimmer exists. Since 2023 reform: Tagespauschale (EUR 6/day, max EUR 1,260/year) or actual costs if Mittelpunkt der Tätigkeit.
2. **Private use percentage** -- Telefon, Internet, Kfz business-use split.
3. **Kfz method** -- 1%-Regelung vs Fahrtenbuch.
4. **Capital allowances from prior years** -- Continuing AfA on assets acquired before 2025 (unless prior EÜR has the schedule).
5. **GKV or PKV** -- Whether gesetzlich or privat krankenversichert (affects Sonderausgaben computation).
6. **Kirchensteuer** -- Whether the user pays KiSt (8% or 9% depending on Bundesland).
7. **Bundesland** -- Needed for Kirchensteuersatz and Gewerbesteuer Hebesatz (if Gewerbetreibender).
8. **Other income** -- Employment income (Anlage N), rental (Anlage V), Kapitalerträge (Anlage KAP).

**Home office gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Arbeitszimmer (home office)?"
   Options: [
     "Dedicated room at home, Mittelpunkt der gesamten Tätigkeit (I work there exclusively)",
     "Dedicated room at home, but I also work at client sites",
     "No dedicated room -- I use Tagespauschale (EUR 6/day, max EUR 1,260/year)",
     "Separate business premises (Büromiete already captured)",
     "No home office claim"
   ]
```

If option 1 -> actual cost method available. Ask for room size as % of total Wohnfläche, plus Miete/Nebenkosten amounts.
If option 2 -> Tagespauschale only (since 2023 reform, limited deduction unless Mittelpunkt). Flag as T2.
If option 3 -> ask for number of home office days in 2025. Compute EUR 6 x days, max EUR 1,260.
If option 4 -> rent already in Betriebsausgaben. Skip.
If option 5 -> skip entirely.

**Kfz method example:**

Call `ask_user_input_v0` with:

```
Q: "Kfz -- business use method?"
   Options: [
     "Fahrtenbuch (mileage log maintained all year)",
     "1%-Regelung (Bruttolistenpreis method)",
     "Km-Pauschale only (EUR 0.30/km for business trips, no car in Betriebsvermögen)",
     "No vehicle used for business"
   ]
```

If Fahrtenbuch -> ask for total km, business km, and vehicle costs. Compute business %.
If 1%-Regelung -> ask for Bruttolistenpreis. Compute 1% x 12 months private use addition.
If Km-Pauschale -> ask for business km driven. EUR 0.30/km (EUR 0.38/km above 21st km for Pendlerpauschale, but that's for commuting, not business trips).
If no vehicle -> skip.

**Kirchensteuer:**

Call `ask_user_input_v0` with:

```
Q: "Kirchensteuer?"
   Options: [
     "Yes -- evangelisch or katholisch (church tax applies)",
     "No -- no church membership (ausgetreten or never joined)"
   ]
```

If yes -> need Bundesland for rate (8% in Bayern/Baden-Württemberg, 9% elsewhere).

**Bundesland:**

Call `ask_user_input_v0` with:

```
Q: "Bundesland?"
   Options: [
     "Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen",
     "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen",
     "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen",
     "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen"
   ]
```

Needed for: Kirchensteuersatz and Gewerbesteuer Hebesatz (if Gewerbetreibender -- will look up municipality Hebesatz during assembly).

Flag all private-use percentages as T2 -- Steuerberater must confirm the percentage is reasonable and documented.

---

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `de-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> Freiberufler, single, Regelbesteuerung, full-year Germany resident (Berlin). Betriebseinnahmen EUR 85,000, estimated Gewinn ~EUR 68,000 before Sonderausgaben and außergewöhnliche Belastungen.
>
> I'm now going to run the full German return preparation. This covers:
> 1. UStVA (December 2025 and Umsatzsteuererklärung)
> 2. ESt + EÜR (Einkommensteuererklärung with Anlage EÜR, Anlage S/G, Anlage Vorsorgeaufwand)
> 3. Sozialversicherungsbeiträge reconciliation (KV/PV/RV)
> 4. Gewerbesteuer (if Gewerbetreibender)
> 5. Vorauszahlungen schedule for 2026
>
> You'll get back:
> 1. An Excel working paper with all forms and live formulas
> 2. A reviewer brief with positions, citations, and flags for your Steuerberater
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `de-return-assembly` with the structured intake package.

---

## Section 8 -- Structured intake package (internal format)

The downstream skill (`de-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "DE",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "birth_year": 0,
    "marital_status": "single | married | single_parent",
    "residency": "full_year",
    "bundesland": "",
    "municipality": "",
    "steuernummer": "",
    "ust_id_nr": "",
    "vat_status": "regelbesteuerung | kleinunternehmer",
    "business_type": "freiberufler | gewerbetreibender",
    "industry": "",
    "entity_type": "sole_proprietor",
    "kirchensteuer": true,
    "kirchensteuer_rate": 0.08
  },
  "income": {
    "betriebseinnahmen_netto": 0,
    "ust_collected": 0,
    "eu_reverse_charge_income": 0,
    "drittland_income": 0,
    "other_income": 0,
    "client_breakdown": []
  },
  "expenses": {
    "fully_deductible": [],
    "mixed_use": [],
    "limited_deduction": [],
    "capital_items": [],
    "gkv_pkv": {
      "type": "GKV | PKV",
      "annual_premium": 0,
      "basisabsicherung": 0,
      "pflegeversicherung": 0
    }
  },
  "vat": {
    "ustva_filed": [],
    "dauerfristverlaengerung": false,
    "sondervorauszahlung": 0,
    "vorsteuer_reclaimable": 0,
    "exempt_supplies": false
  },
  "sozialversicherung": {
    "gkv_or_pkv": "GKV | PKV",
    "annual_kv_premium": 0,
    "annual_pv_premium": 0,
    "rentenversicherung": {
      "type": "none | freiwillig | pflicht_ksk",
      "annual_amount": 0
    }
  },
  "vorauszahlungen": {
    "est_quarterly": [],
    "solz_quarterly": [],
    "kist_quarterly": [],
    "total_est_paid": 0,
    "total_solz_paid": 0,
    "total_kist_paid": 0
  },
  "prior_year": {
    "festgesetzte_est": 0,
    "festgesetzter_solz": 0,
    "festgesetzte_kist": 0,
    "gewinn": 0,
    "afa_schedule": []
  },
  "home_office": {
    "type": "mittelpunkt | tagespauschale | none",
    "days_worked_at_home": 0,
    "room_percentage": 0,
    "annual_amount": 0
  },
  "private_use": {
    "kfz_method": "fahrtenbuch | 1pct_regelung | km_pauschale | none",
    "kfz_business_pct": 0,
    "kfz_bruttolistenpreis": 0,
    "telefon_business_pct": 0,
    "internet_business_pct": 0
  },
  "gewerbesteuer": {
    "applies": false,
    "hebesatz": 0,
    "municipality": ""
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

---

## Section 9 -- Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (e.g., GmbH structure discovered in documents).

When a refusal fires:
1. Stop the workflow
2. State the specific reason in one sentence
3. Recommend the path forward (specific practitioner type)
4. Offer to continue with partial help ONLY if the out-of-scope item is cleanly separable (rare)

**Do not:**
- Apologize profusely
- Try to work around the refusal
- Suggest the user "might be able to" fit into scope if they answer differently
- Continue silently

**Sample refusal:**

> Stop -- you have a registered GmbH. I'm set up for Freiberufler and Gewerbetreibende (Einzelunternehmer) only. GmbHs file Körperschaftsteuererklärung and Gewerbesteuererklärung with separate rules for Geschäftsführergehalt and Gewinnausschüttungen. You need a Steuerberater familiar with Kapitalgesellschaften.
>
> I can't help with this one.

---

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay Krankenversicherung" after the bank statement showed TK payments, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `de-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned Steuerberater signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- VAT status was established.** Regelbesteuerung vs Kleinunternehmer was confirmed before inference, as it changes how every transaction is classified.

**Check IN13 -- Business type was established.** Freiberufler vs Gewerbetreibender was confirmed, as it determines Gewerbesteuer applicability.

---

## Section 11 -- Performance targets

For a prepared user (documents in a folder, ready to upload):
- **Refusal sweep**: 45 seconds (1-2 interactive turns)
- **Document upload**: 2 minutes (1 upload turn)
- **Inference and confirmation display**: 1 minute Claude processing + 1 turn for user confirmation
- **Gap filling**: 2 minutes (2-3 interactive turns)
- **Handoff**: immediate
- **Total**: ~6 minutes

For an unprepared user (has to go fetch documents):
- Refusal sweep: same
- Document discovery: 10-20 minutes offline
- Rest: same
- **Total**: 15-25 minutes

---

## Section 12 -- Cross-skill references

**Inputs:** User-provided documents and answers.

**Outputs:** Structured intake package consumed by `de-return-assembly`.

**Downstream skills triggered (via de-return-assembly):**
- `germany-vat-return` -- UStVA / Umsatzsteuererklärung
- `de-income-tax` -- ESt + EÜR (Einkommensteuererklärung with Anlage EÜR)
- `de-social-contributions` -- Krankenversicherung / Pflegeversicherung / Rentenversicherung
- `de-trade-tax` -- Gewerbesteuer (only if Gewerbetreibender)
- `de-estimated-tax` -- Vorauszahlungen schedule

---

### Change log

- **v0.1 (April 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v0.1


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
