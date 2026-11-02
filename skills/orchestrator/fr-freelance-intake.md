---
name: fr-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their French tax returns AND mentions freelancing, auto-entrepreneur, micro-entrepreneur, entreprise individuelle, profession libérale, or self-employment. Trigger on phrases like "aide-moi avec mes impôts", "préparer ma déclaration", "I'm a freelancer in France", "I'm an auto-entrepreneur", "prepare my 2042-C-PRO", or any similar phrasing where the user is a France-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the French self-employed tax workflow -- every other skill in the stack (france-tva, france-income-tax, france-cotisations, fr-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. France full-year residents only; self-employed individuals, micro-entrepreneurs, and sole proprietors.
version: 1.1
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: intake for a self-employed person's tax returns (micro-entrepreneur, entreprise individuelle, profession libérale)

This skill runs the intake for a France-resident self-employed individual: it sorts the client into scope or out of scope, collects and reads the documents, confirms the facts and hands a structured package to `fr-return-assembly`. Figures are for tax year 2026. France taxes the previous year's income, so two sets of numbers are live at once: the micro turnover limits for income of 2025 declared in 2026 come from the rows marked "Income of 2025" in the micro table below, while the VAT franchise limits, the micro-social contribution rates, the Acre rates and the micro limits for income received in 2026 (declared in 2027) are those in force during 2026. The rules stated are those in force on 19 October 2026, read on official pages between 19 September and 19 October 2026; where a page carries its own date stamp, it is given. On 19 October 2026 the filing window for the return on 2025 income has closed (the dates are in the filing table below), so the first job of the intake is to find out which return the client needs.

## What this file is

The intake orchestrator for France-resident self-employed individuals. The French content skills (`fr-income-tax`, `fr-social-contributions`, `france-vat-return`, `fr-cfe`) and the assembly orchestrator (`fr-return-assembly`) expect this skill to run first and produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `fr-return-assembly`.

## Design principles

v1.0 follows the upload-first, inference-then-confirm pattern:

1. **Compact refusal sweep** using `ask_user_input_v0`: 3 interactive questions, about 30 seconds.
2. **Upload-first workflow**: after the refusal check, the user drops in everything they have.
3. **Inference pass**: the assistant parses every document and extracts as much as possible.
4. **Gap-filling only**: the assistant asks the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end: show the full picture, let the user correct anything wrong, hand off to downstream skills.

Target: intake completes in 5 minutes for a prepared user, 15 minutes for a user who has to go and fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user is a micro-entrepreneur, do not later ask about business structure. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows URSSAF payments, do not ask "did you pay cotisations." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in scope or out of scope, ask it on its own.

## The year and the filing window

**Which return is this?** Ask it before anything else, because it decides which column of every table applies.

- **Income of 2025 (the return filed in 2026).** The filing dates have passed. The impots.gouv.fr page "Les modalités de la déclaration de revenus en 2026" gives the online deadlines by département: "jeudi 21 mai au plus tard (23h59) pour les départements n° 01 à 19 et les non-résidents ; jeudi 28 mai au plus tard (23h59) pour les départements n° 20 à 54 ; jeudi 4 juin au plus tard (23h59) pour les départements n° 55 à 974 et 976", and the paper return "au plus tard le mardi 19 mai 2026 à minuit" (https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026). A client who filed online and finds an error can still use the online correction service: "Pour la déclaration des revenus 2025, le service sera disponible mi-août 2026 jusque mi-décembre 2026" (same page). A client who never filed is a late filer: refer (see "When to refuse or refer").
- **Income of 2026 (the return filed in 2027).** The intake can be run now to prepare. Use the 2026 columns of the tables below. The 2027 filing dates are not yet published.

## Section 1: The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check, then upload, then gaps, then handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by an expert-comptable before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`, with the year question first

**Example first message:**

> Let's get your French self-employed return ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by an expert-comptable or qualified tax professional before you file anything with the DGFiP or URSSAF. I'm not a substitute for review.
>
> Scope check:

Then immediately call `ask_user_input_v0` with the year question and the refusal questions.

**Do NOT:**
- Write a welcome paragraph
- Explain the phases
- Ask "are you ready to start"
- List what documents you will eventually need
- Give a disclaimer beyond the one reviewer line

## Section 2: Refusal sweep (compact)

Present the refusal sweep as a single `ask_user_input_v0` call, all single-select.

**The questions to ask first:**

~~~
Q0: "Which income year?"
    Options: ["Income of 2025: correcting the return already filed in 2026", "Income of 2025: return not filed yet", "Income of 2026: preparing the return due in 2027"]

Q1: "Business type?"
    Options: ["Micro-entrepreneur (auto-entrepreneur)", "Entreprise individuelle (EI) au réel", "EURL (gérant associé unique)", "SASU (président associé unique)", "Profession libérale", "Not sure"]

Q2: "Turnover (chiffre d'affaires hors taxes) compared with the micro limits for that year?"
    Options: ["Below the limit for my activity in both of the two previous years", "Above the limit in one of the two previous years", "Above the limit in both of the two previous years", "Not sure"]

Q3: "TVA regime?"
    Options: ["Franchise en base (no TVA charged)", "Réel simplifié (CA12 annual + 2 acomptes)", "Réel normal (CA3 monthly/quarterly)", "Not sure"]
~~~

Show the user the limit that applies to the year chosen at Q0, read from the micro table below. Never show the 2025 limits to a client preparing 2026 income, or the reverse.

**Micro regime (régime micro-fiscal): turnover limits and flat allowances**

The page is stamped "Vérifié le 13 mai 2026".

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |  |
| Income of 2025: sales of goods and accommodation, turnover of 2024 or 2023 | EUR 188,700 | "ne doit pas avoir dépassé 188 700 €" | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |
| Income of 2025: other services (BIC) and liberal activity (BNC), turnover of 2024 or 2023 | EUR 77,700 | "ne doit pas avoir dépassé 77 700 €" | same |
| Income received in 2026: sales of goods and accommodation, turnover of 2025 (N-1) or 2024 (N-2) | EUR 203,100 | "n’a pas dépassé 203 100 €" | same |
| Income received in 2026: services (BIC) and liberal activity (BNC), turnover of 2025 or 2024 | EUR 83,600 | "n’a pas dépassé 83 600 €" | same |
| Flat allowance, sales of goods and accommodation (BIC), other than furnished tourist lets | 71% | "Le taux d'abattement est de 71 %" | same (2026) |
| Flat allowance, services (BIC) | 50% | "Le taux d'abattement est de 50 %" | same (2026) |
| Flat allowance, liberal activity (BNC) | 34% | "Le taux d'abattement est de 34 %" | same (2026) |
| Minimum allowance | EUR 305 | "Le montant de l’abattement ne peut pas être inférieur à 305 €" | same (2026) |
| Flat income tax payment (versement libératoire), commerce, catering and accommodation | 1% | "1 % pour les activités de commerce, restauration et logement" | same (2026) |
| Flat income tax payment, other BIC activities | 1.7% | "1,7 % pour les autres activités relevant des BIC" | same (2026) |
| Flat income tax payment, BNC | 2.2% | "ce taux est de 2,2 %" | same (2026) |
| Flat income tax payment, ceiling on the household's reference income of year N-2, single person | EUR 29,579 | "29 579 € pour une personne seule" | same (2026) |
| Same ceiling, couple sharing one tax household | EUR 59,158 | "59 158 € pour une personne en couple" | same (2026) |
| Same ceiling, couple with one child sharing one tax household | EUR 73,947.5 | "73 947,5 € pour une personne en couple avec 1 enfant et partageant le même foyer fiscal" | same (2026) |
| Same ceiling, couple with two children sharing one tax household | EUR 88,737 | "88 737 € pour une personne en couple avec 2 enfants et partageant le même foyer fiscal" | same (2026) |

The micro regime is lost only after two consecutive years over the limit. The page says the income of year N is excluded "uniquement si l’un des seuils a été dépassé pendant 2 années consécutives, en N-1 et en N-2" (https://entreprendre.service-public.gouv.fr/vosdroits/F23267). One year over the limit does not end the regime. Furnished tourist lets have their own limits and allowances on that page: if the client lets furnished tourist accommodation, read them there, or use `fr-rental-income`.

**The flat-payment ceiling: two official pages disagree**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur |  |
| Option for the versement libératoire in 2026: reference income of 2024, single person (1 part) | EUR 29,315 | "29 315 € pour une personne seule (1 part)" | https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur |
| Same, couple (2 parts) | EUR 58,630 | "58 630 € pour un couple (2 parts)" | same (2026) |
| Same, couple with two children (3 parts) | EUR 87,945 | "87 945 € pour un couple avec deux enfants (3 parts)" | same (2026) |

The service-public page in the micro table gives one ceiling and this impots.gouv.fr page gives a lower one for the option 'en 2026', tested on the 2024 reference income. The service-public page adds that an option made before 30 September of a year applies from 1 January of the next ("Si la demande est effectuée avant le 30 septembre 2026, le versement libératoire s'appliquera aux revenus perçus à partir du 1 er janvier 2027") and, for a business created in the year, before the last day of the third month after creation. Do not pick one. The impots.gouv.fr page sets two more conditions for the option: the previous year's turnover must be below the micro limit for the activity ("Votre chiffre d'affaires de l'année précédente est inférieur à : 188 700 € pour les activités de vente de marchandises, de fourniture de logement ... 77 700 € pour les prestations de services (BIC) et les professions libérales (BNC)") and the client must be in the micro-social regime ("Option pour le régime micro-social"). If the client's 2024 reference income falls between the two values for their household, flag it for the reviewer and ask the client for the URSSAF confirmation of the option. If it is below both, the ceiling is not in question; if it is above both, the option is not available.

**How to read each answer:**

- **Q1 = Micro-entrepreneur**: continue. Micro-fiscal and micro-social regime. Income is declared on the 2042 and its annex the 2042-C-PRO. Without the flat payment, turnover goes in "5KO (pour le déclarant 1) ou 5LO (pour le déclarant 2) : pour les activités de ventes ; 5KP (pour le déclarant 1) ou 5LP (pour le déclarant 2) : pour les activités de prestations de services", and liberal receipts "dans les cases 5HQ (pour le titulaire 1) ou 5IQ (pour le titulaire 2)" (https://www.impots.gouv.fr/professionnel/resultat-imposable-limpot-sur-le-revenu-ir-ou-limpot-sur-les-societes). With the flat payment, the turnover is declared in "5TA / 5TB / 5TE" according to the activity (https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur).
- **Q1 = EI au réel**: continue. Full accounting regime. Forms: 2042, 2042-C-PRO, plus the professional results return: for BIC under the régime simplifié "une télé-déclaration de résultats n° 2031-SD et la liasse fiscale BIC-IS RSI composée des annexes n os 2033-A-SD à 2033-G-SD"; for BNC under the déclaration contrôlée "une déclaration de résultats n° 2035-SD et la liasse fiscale BNC composée des tableaux n os 2035 A, AS, B, E, F et G" (https://www.impots.gouv.fr/professionnel/resultat-imposable-limpot-sur-le-revenu-ir-ou-limpot-sur-les-societes).
- **Q1 = EURL (gérant associé unique)**: continue ONLY if the EURL is taxed under impôt sur le revenu. If the EURL is at impôt sur les sociétés (IS), stop: "An EURL at IS files a corporate return. I'm set up for personal income tax filings. You need an expert-comptable who handles IS returns."
- **Q1 = SASU**: stop. "A SASU is a company. I'm set up for self-employed individuals filing personal income tax. You need an expert-comptable who handles corporate tax and payroll."
- **Q1 = Profession libérale**: continue. BNC: micro-BNC (case 5HQ) or the déclaration contrôlée (2035), as above.
- **Q1 = Not sure**: ask one follow-up: "Did you register on the guichet unique (formalites.entreprises.gouv.fr) as a micro-entrepreneur, or do you have a SIRET with a full accounting obligation? Check your avis de situation SIRENE or your URSSAF online account for your status."
- **Q2 = Below in both years, or above in only one**: continue. The micro regime is available for the year (two consecutive years over the limit are needed to lose it).
- **Q2 = Above in both of the two previous years**: continue with a flag. If the client is still filing as a micro-entrepreneur, the micro regime no longer applies to that year's income and the business moves to a réel regime. Verify against the turnover figures after inference.
- **Q2 = Not sure**: continue, infer from documents.
- **Q3 = Franchise en base**: continue, and test the franchise against the franchise table below. No TVA is charged or recovered. Invoices must carry the wording "TVA non applicable - article 293 B du CGI" (https://entreprendre.service-public.gouv.fr/vosdroits/F21746).
- **Q3 = Réel simplifié**: continue. Annual CA12 with two instalments, in July and December, at the percentages in the VAT filing table below. Input TVA recovery available.
- **Q3 = Réel normal**: continue. Monthly CA3, or quarterly where the VAT due each year is below the quarterly limit in the VAT filing table below.
- **Q3 = Not sure**: ask one follow-up: "Do your invoices include TVA (at one of the rates in the VAT rate table)? If they say 'TVA non applicable, article 293 B du CGI', you're in the franchise en base. If you charge TVA and file monthly or quarterly, you're réel normal. If you file one annual TVA return with two advance payments, you're réel simplifié."

**The franchise en base de TVA for 2026**

The page is stamped "Vérifié le 01 janvier 2026" and says that the proposal from the 2025 finance law "visant à instaurer un seuil unique de franchise en base de TVA de 25 000 € a été abandonnée" (https://entreprendre.service-public.gouv.fr/vosdroits/F21746). Any document or software that applies a single lower threshold is wrong for 2026. Each limit is "inférieur ou égal" to the amount, on turnover excluding VAT. Each activity has two: a basic limit on the previous calendar year (N-1) and a higher limit on the current year (N).

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 |  |
| Abandoned single threshold (never apply it) | EUR 25,000 | "seuil unique de franchise en base de TVA de 25 000 € a été abandonnée" | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 (2026) |
| Sales of goods and accommodation, previous year (N-1) | EUR 85,000 | "est inférieur ou égal à 85 000 € (seuil de la franchise en base de TVA)" | same (2026) |
| Sales of goods and accommodation, current year (N) | EUR 93,500 | "est inférieur ou égal à 93 500 € (seuil majoré de la franchise en base de TVA)" | same (2026) |
| Services and liberal professions other than lawyers, previous year (N-1) | EUR 37,500 | "est inférieur ou égal à 37 500 € (seuil de la franchise en base de TVA)" | same (2026) |
| Services and liberal professions other than lawyers, current year (N) | EUR 41,250 | "est inférieur ou égal à 41 250 € (seuil majoré de la franchise en base de TVA)" | same (2026) |
| A lawyer's regulated work, and authors' and performers' works, previous year (N-1) | EUR 50,000 | "inférieur ou égal à 50 000 € (seuil de la franchise en base de TVA)" | same (2026) |
| Same, current year (N) | EUR 55,000 | "est inférieur ou égal à 55 000 € (seuil majoré de la franchise en base de TVA)" | same (2026) |

Crossing the basic limit of the previous year brings VAT "dès le 1er janvier de l’année suivante"; crossing the higher limit during the current year brings VAT "dès le 1 er jour de dépassement" (https://entreprendre.service-public.gouv.fr/vosdroits/F21746). The franchise limits and the micro limits are different numbers: a micro-entrepreneur can stay in the micro regime and still have to charge VAT.

**After Q0 to Q3 pass, ask the second batch of scope questions (also batched):**

~~~
Q4: "URSSAF registration status?"
    Options: ["Registered and paying cotisations", "Recently registered (started in the last 12 months)", "Not registered / pending", "Cipav-affiliated (profession libérale réglementée)"]

Q5: "Marital status and household?"
    Options: ["Single (1 part)", "Married / PACSé - déclaration commune", "Married / PACSé - déclaration séparée (year of marriage/PACS)", "Single parent (parent isolé)"]

Q6: "Other income sources in the year?"
    Options: ["None: self-employment only", "Employment income (salaires)", "Rental income (revenus fonciers)", "Investment income (dividends, interest, capital gains)", "Multiple of the above"]

Q7: "Prior year filing status?"
    Options: ["Filed the previous year's return on time", "Filed the previous year's return late", "First year filing", "Did not file the previous year's return"]

Q8: "Régime matrimonial (if married/PACSé)?"
    Options: ["Communauté réduite aux acquêts (default)", "Communauté universelle", "Séparation de biens", "Not married / Not applicable"]
~~~

- **Evaluate Q4, registered and paying**: continue. Standard micro-social, or cotisations au réel.
- **Evaluate Q4, recently registered**: continue with a flag. Acre (aide aux créateurs et repreneurs d'entreprise) may apply. For a micro-entrepreneur it is not a three-year relief: the reduced-rate column is headed "Jusqu'à la fin du 3ème trimestre civil suivant celui de la date d'inscription", and the reduced rate depends on whether the activity started up to 30 June 2026 or from 1 July 2026 (micro-social table below). Ask for the start date. Acre is not automatic for a micro-entrepreneur: the page says "une demande doit obligatoirement être adressée à l'Urssaf au plus tard dans un délai de 60 jours suivant la date de début d'activité" and the client must belong to one of the categories of article L. 5141-1 of the code du travail or work in a ZFRR/ZFRR+, and must "ne pas en avoir bénéficié au cours des 3 années précédentes" (same page). Ask whether the application was made and accepted.
- **Evaluate Q4, not registered or pending**: continue with a flag. Registration is required. Note it in the action items.
- **Evaluate Q4, Cipav-affiliated**: continue with a flag. Cipav covers certain regulated liberal professions and has its own micro-social rate (micro-social table below).
- **Evaluate Q5**: note for the family quotient (quotient familial). A couple filing jointly has 2 parts; the page says "1 demi-part pour chacun des 2 premiers enfants à charge 1 part entière à partir du 3 e". For children in shared residence (résidence alternée) the page prints 0.25 part for one child, 0.5 for two, 1 for three, then 0.5 for each further child (https://www.service-public.gouv.fr/particuliers/vosdroits/F2705). Parts for a single parent and the caps on the benefit of each half-part are in `fr-income-tax` and `fr-personal-income-tax`.
- **Evaluate Q6**: note for a multi-schedule return. Employment income goes in the salary section of the 2042, where the flat deduction for professional expenses in the salary table below applies unless actual expenses (frais réels) are claimed. Rental income goes to `fr-rental-income`. Investment income goes to `fr-capital-gains`: the flat tax (prélèvement forfaitaire unique) is made of an income tax part and social levies whose total depends on the income and the year (investment income table below). Never write a single combined rate for it.
- **Evaluate Q7**: note for penalty and interest risk and the prior year reference amounts.
- **Evaluate Q8**: affects whether business assets are common property. Record it for the reviewer.

**Total time:** about 60 seconds if the user taps through.

**Micro-social contribution rates in force from 1 January 2026, and the Acre rates**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html |  |
| Sale of goods (BIC), full rate | 12.3% | "Achat/revente de marchandises (BIC) 12,3 %" | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html (2026) |
| Commercial and craft services (BIC), full rate | 21.2% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" | same (2026) |
| Other services (BNC), full rate | 25.6% | "Autres prestations de services (BNC) 25,6 %" | same (2026) |
| Regulated liberal professions under Cipav, full rate | 23.2% | "Professions libérales réglementées relevant de la Cipav (BIC et BNC) 23,2 %" | same (2026) |
| Acre, sale of goods, activity started up to 30 June 2026 | 6.2% | "Vente de marchandises ( BIC ) 6,2% 9,3% 12,3%" | same |
| Acre, sale of goods, activity started from 1 July 2026 | 9.3% | "Vente de marchandises ( BIC ) 6,2% 9,3% 12,3%" | same |
| Acre, commercial and craft services, started up to 30 June 2026 | 10.6% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" | same |
| Acre, commercial and craft services, started from 1 July 2026 | 15.9% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" | same |
| Acre, other services (BNC), started up to 30 June 2026 | 12.8% | "Autres prestations de services ( BNC ) 12,8% 19,2% 25,6%" | same |
| Acre, other services (BNC), started from 1 July 2026 | 19.2% | "Autres prestations de services ( BNC ) 12,8% 19,2% 25,6%" | same |
| Acre, Cipav, started up to 30 June 2026 | 13.4% | "Professions libérales relevant de la Cipav (BNC) 13,4%* 17,4% 23,2%" | same |
| Acre, Cipav, started from 1 July 2026 | 17.4% | "Professions libérales relevant de la Cipav (BNC) 13,4%* 17,4% 23,2%" | same |

The asterisk on the Cipav Acre rate is the page's: "pour les professions libérales relevant de la Cipav, le taux est réhaussé en tenant compte du taux minimum (somme des taux CSG/CRDS et du taux de retraite complémentaire non exonérés par l'Acre)". The Acre columns are headed "Débuts d'activité Jusqu'au 30/06/2026" and "Débuts d'activité à compter du 1/07/2026"; the full-rate column is headed "A compter du 1/01/2026". These are the rates for 2026 turnover. For turnover of 2025, read the rate printed on the client's own URSSAF declarations; this skill does not carry the 2025 rates. A micro-entrepreneur must declare turnover each month or each quarter, even when it is nil (same page). The flat income tax payment, where opted for, is collected with the contributions on the same periodic declaration.

## Section 3: The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for the year: drop it all in at once.
>
> - Business bank account statements for the whole year (CSV or PDF)
> - Sales invoices issued in the year (or an accounting software export)
> - Purchase invoices and receipts for business expenses
> - The previous year's avis d'impôt, and the return (2042 / 2042-C-PRO) if you have it
> - TVA returns for the year (CA3 or CA12), if you charge TVA
> - URSSAF attestation or contribution statements
> - URSSAF micro-entrepreneur monthly or quarterly declarations
> - CFE (cotisation foncière des entreprises) avis d'imposition
> - Any DGFiP or URSSAF correspondence
> - Purchase receipts for equipment (computers, tools, vehicles)
> - Anything else tax-related you have
>
> Don't worry about labelling or organising: I'll work out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** switch to guided mode:
> Check these places:
> - Business bank: download the year's statements as PDF or CSV
> - impots.gouv.fr: download the previous year's avis d'impôt and your returns
> - autoentrepreneur.urssaf.fr (if micro): download the annual attestation and your declaration history
> - Email: search for "facture", "TVA", "URSSAF", "impôts", "CFE"
> - Your expert-comptable from last year, if you had one
> - Accounting software: export the grand livre or the FEC
>
> Come back when you have something to upload. I'll work with whatever you bring.

## Section 4: The inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement:**
- Total deposits (candidate chiffre d'affaires / recettes)
- Recurring inflows (client payments with names)
- Outflows to URSSAF (cotisations sociales with dates and amounts)
- Outflows to the DGFiP / Trésor Public (income tax payments, instalments)
- Outflows to the DGFiP for TVA
- Outflows to suppliers (business expenses by category)
- CFE payment (the CFE is generally due by 15 December; see the CFE table below)
- Equipment purchases (potential immobilisations)
- Transfers to the personal account (prélèvements de l'exploitant)
- SaaS and software subscriptions
- Professional memberships (ordre professionnel, syndicat)
- Insurance payments (RC Pro, prévoyance, Madelin contracts)

**Sales invoices:**
- Client names and amounts HT (hors taxes) and TTC (toutes taxes comprises)
- Whether TVA was charged, and at which rate (VAT rate table below)
- Whether invoices carry "TVA non applicable - article 293 B du CGI" (franchise en base indicator)
- Total chiffre d'affaires reconciled against bank deposits
- Any foreign clients (EU or non-EU: autoliquidation implications)
- Any invoices with withholding (retenue à la source)

**Purchase invoices and receipts:**
- Expense category (charges courantes, immobilisations, achats de marchandises)
- TVA amount on each (recoverable under a réel VAT regime, a cost in the franchise)
- Supplier location (France, EU, non-EU)
- Any equipment that may have to be capitalised: under BOFiP, materials and tools whose unit value excluding VAT does not exceed the limit in the small-equipment table below may be expensed immediately
- Any blocked categories (dépenses somptuaires: hunting, fishing, pleasure residences, under article 39-4 of the CGI)

**Previous year's avis d'impôt and return:**
- Revenu fiscal de référence (RFR)
- Impôt net
- Number of parts (nombre de parts)
- BIC/BNC amounts declared
- Any carried-forward losses (déficits reportables)
- Prélèvement à la source (PAS) rate applied
- Instalments (acomptes contemporains)

**TVA returns (CA3/CA12):**
- Turnover and TVA collected for each period
- Input TVA claimed (TVA déductible)
- Any VAT credit carried forward
- CA12 annual summary with the instalments paid

**URSSAF statements and micro-entrepreneur declarations:**
- Monthly or quarterly chiffre d'affaires declared to URSSAF
- Contributions paid, and the rate applied (micro-social table above)
- Acre, if it applies, and the start date of the activity
- Versement libératoire, if opted for (rates in the micro table above)
- Any adjustment (régularisation) from prior years

**CFE avis:**
- Amount of CFE paid for the year
- Commune and base d'imposition
- Whether the year of creation exemption or the small-turnover exemption applies (CFE table below)

**After parsing everything, build an internal inference object.** Do not show the raw inference yet: turn it into a compact summary for the user in Section 5.

## Section 5: The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message.** All names and amounts are hypothetical, in euro, for income of 2025. Rates are not repeated: read them off the tables.

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Marie Dupont, married (déclaration commune), 1 child, so 2.5 parts
> - Full-year France resident (Lyon)
> - Micro-entrepreneur, SIRET on file
> - Activity: IT consulting (BNC)
> - TVA: franchise en base (article 293 B)
>
> **Income (from bank statement and invoices)**
> - Receipts: 58,000
>   - Client A SARL: 30,000 (monthly retainer)
>   - Client B GmbH (Germany): 18,000 (project, service to an EU business)
>   - Various smaller clients: 10,000
> - No TVA collected (franchise en base)
>
> **Micro-entrepreneur declarations (from URSSAF)**
> - Quarter 1: 14,000 declared; Quarter 2: 15,500; Quarter 3: 14,500; Quarter 4: 14,000
> - Total declared: 58,000, matching bank deposits
> - Contributions paid at the rate printed on each declaration
> - Versement libératoire: opted for (BNC rate)
>
> **CFE**
> - CFE for the year: 412 (Lyon)
>
> **Previous year (from the avis d'impôt)**
> - RFR: 42,000
> - Parts: 2.5
> - PAS rate on the avis
>
> **Spouse income**
> - Not yet captured: will ask in gap-filling (déclaration commune)
>
> **Flags I already see:**
> 1. EU client (Germany): a service to an EU business. If the service is taxable in Germany, the customer accounts for the VAT and a déclaration européenne de services (DES) may be due. To be checked in `france-vat-return`.
> 2. Receipts of 58,000 are above both services limits of the franchise table. Crossing the current-year limit brings VAT from the first day of the overrun. Red flag: the franchise en base cannot continue on these numbers. TVA registration and invoicing need immediate review.
> 3. Versement libératoire was opted for: check the reference income of year N-2 against the ceilings in both flat-payment tables above.
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

The DES rule: under article 289 B-III of the CGI, a business established in France files a déclaration européenne de services when, among other conditions, it supplies a service to a taxable person in another EU state who is liable for the VAT there (notice to the CA3, https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf).

## Section 6: Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Spouse's income**: if the couple files jointly, the spouse's salary, pension or other income is needed for the full 2042.
2. **Children and dependants**: number, ages, shared residence (résidence alternée), for the parts.
3. **Home office (local professionnel)**: whether a dedicated workspace exists, and the share of the home used.
4. **Frais réels vs the flat deduction**: for employment income, if any: keep the flat deduction in the salary table below or declare actual commuting and professional expenses.
5. **Tax reductions and credits**: donations, employing someone at home, childcare outside the home, investment schemes, energy works. Rates and caps are in `fr-income-tax` and `fr-personal-income-tax`.
6. **Madelin contracts**: prévoyance, mutuelle, supplementary pension for the self-employed. Record the contracts and the amounts paid, and flag them for the reviewer.
7. **Earlier losses (déficits antérieurs)**: carried-forward losses from prior years (not always on the avis d'impôt).

Call `ask_user_input_v0` with:

~~~
Q: "Professional workspace?"
   Options: [
     "Dedicated room at home, used ONLY for work",
     "Shared space at home (not exclusively professional)",
     "Separate business premises (bureau, coworking)",
     "No fixed workspace / work at client sites"
   ]
~~~

Under the micro regime, the page computes taxable income as gross turnover less the flat allowance (https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur), so no home office expense is deducted. Collect the home office facts only for a client under a réel regime:

If option 1, ask for the room area and the total area of the home, for the reviewer's apportionment of rent or mortgage interest, electricity, internet and taxe foncière.
If option 2, flag it as a reviewer item: shared use reduces the deductible share. This skill states no accepted percentage.
If option 3, rent is already captured in expenses. No home office split needed.
If option 4, skip home office entirely.

- **Children and parts**: a couple filing jointly has 2 parts, plus half a part for each of the first two children and a whole part from the third; children in shared residence count for half of that (https://www.service-public.gouv.fr/particuliers/vosdroits/F2705).

Call `ask_user_input_v0` with:

~~~
Q: "Dependants for the quotient familial?"
   Options: [
     "No children or dependants",
     "1 child",
     "2 children",
     "3+ children (specify in follow-up)",
     "Children in résidence alternée (shared residence)"
   ]
~~~

Call `ask_user_input_v0` with:

~~~
Q: "Any of these apply?"
   Options: [
     "Donations to associations / organismes d'intérêt général",
     "Employing someone at home (salarié à domicile)",
     "Childcare outside the home for a young child",
     "Madelin contributions (prévoyance, retraite, mutuelle)",
     "None of these"
   ]
~~~

Flag every credit and reduction for reviewer confirmation.

**Flat deduction on salaries**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 |  |
| Flat deduction for professional expenses on employment income, kept unless actual expenses are claimed | 10% | "Déduction forfaitaire de 10 % pour frais professionnels" | https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 (2026) |

## Section 7: The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `fr-return-assembly`.

**Example handoff message (hypothetical):**

> Intake complete. Here's what's going to the return assembly:
>
> Micro-entrepreneur BNC, married with 1 child (2.5 parts), franchise en base TVA (limit exceeded: TVA registration flag). Receipts 58,000, contributions as declared to URSSAF, versement libératoire opted for.
>
> I'm now going to run the full French return preparation. This covers:
> 1. TVA analysis and the registration obligation
> 2. The income tax return (2042 / 2042-C-PRO)
> 3. Social contributions reconciliation (URSSAF)
> 4. CFE check
> 5. The prélèvement à la source rate and instalments
>
> You'll get back:
> 1. A working paper with all forms and computations
> 2. A reviewer brief with positions, citations and flags for your expert-comptable
> 3. A filing calendar with the upcoming deadlines
>
> Starting now.

Then invoke `fr-return-assembly` with the structured intake package.

## Section 8: Structured intake package (internal format)

The downstream skill (`fr-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

~~~json
{
  "jurisdiction": "FR",
  "income_year": 2025,
  "return_type": "correction_of_filed_return | late_return | preparation_next_year",
  "taxpayer": {
    "name": "",
    "date_of_birth": "",
    "marital_status": "single | married_joint | married_separate | pacs_joint | pacs_separate | single_parent",
    "parts_fiscales": 0,
    "children": [],
    "residency": "full_year",
    "siret": "",
    "activity_code_ape": "",
    "activity_start_date": "",
    "business_type": "micro_entrepreneur | ei_reel | eurl_ir | profession_liberale",
    "regime_fiscal": "micro_bnc | micro_bic | declaration_controlee | reel_simplifie_bic | reel_normal_bic",
    "regime_tva": "franchise_en_base | reel_simplifie | reel_normal",
    "urssaf_status": "registered | recently_registered | cipav",
    "acre_eligible": false,
    "versement_liberatoire_ir": false,
    "regime_matrimonial": "communaute_acquets | communaute_universelle | separation_biens | na"
  },
  "income": {
    "chiffre_affaires_ht": 0,
    "chiffre_affaires_ttc": 0,
    "chiffre_affaires_n_minus_1": 0,
    "chiffre_affaires_n_minus_2": 0,
    "tva_collected": 0,
    "client_breakdown": [],
    "eu_services": 0,
    "non_eu_services": 0,
    "other_income": {
      "salaires": 0,
      "revenus_fonciers": 0,
      "revenus_capitaux_mobiliers": 0,
      "plus_values": 0
    },
    "spouse_income": {
      "salaires": 0,
      "other": 0
    }
  },
  "expenses": {
    "charges_courantes": [],
    "immobilisations": [],
    "charges_mixtes": [],
    "blocked": [],
    "cotisations_madelin": {
      "prevoyance": 0,
      "retraite": 0,
      "mutuelle": 0
    }
  },
  "tva": {
    "regime": "franchise | reel_simplifie | reel_normal",
    "returns_filed": [],
    "tva_collectee_total": 0,
    "tva_deductible_total": 0,
    "credit_tva_bf": 0,
    "franchise_threshold_exceeded": false,
    "franchise_threshold_basis": "previous_year | current_year"
  },
  "cotisations_sociales": {
    "regime": "micro_social | tns_reel",
    "declarations": [],
    "total_cotisations_paid": 0,
    "acre_applied": false,
    "cipav_affiliated": false,
    "versement_liberatoire_ir_paid": 0
  },
  "cfe": {
    "amount_paid": 0,
    "commune": "",
    "exemption_claimed": "none | year_of_creation | small_turnover"
  },
  "prior_year": {
    "rfr": 0,
    "rfr_n_minus_2": 0,
    "impot_net": 0,
    "parts_fiscales": 0,
    "pas_rate": 0,
    "deficits_reportables": 0,
    "bnc_bic_declared": 0
  },
  "home_office": {
    "qualifies": false,
    "percentage": 0,
    "method": "surface | forfait"
  },
  "credits_reductions": {
    "dons": 0,
    "emploi_domicile": 0,
    "garde_enfants": 0,
    "other": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
~~~

## Section 9: Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (for example, a company structure found in the documents).

- **R-FR-1: SASU / SAS.** "A SASU or SAS is a company. I'm set up for self-employed individuals filing personal income tax. You need an expert-comptable who handles IS returns and payroll."
- **R-FR-2: EURL at IS.** "An EURL at IS files corporate returns. I handle personal income tax filings only."
- **R-FR-3: SCI.** "An SCI (société civile immobilière) has its own filing requirements. This is outside my scope."
- **R-FR-4: SAS/SARL with more than 10 employees.** "Companies with more than 10 employees have payroll, DSN and social obligations I don't cover. You need an expert-comptable with a payroll department."
- **R-FR-5: Agricultural activity.** "Agricultural income (bénéfices agricoles) is declared under its own rules and is covered by the MSA, not URSSAF. You need an expert-comptable specialising in agriculture."
- **R-FR-6: Non-resident.** "Non-residents file with the service des impôts des non-résidents and have different rules. I'm set up for full-year France residents only."
- **R-FR-7: Association.** "Associations (loi 1901) have separate filing obligations. Not in scope."
- **R-FR-8: Return on 2025 income never filed.** "Your return for 2025 income was due in May or June 2026. A late return carries penalties and interest that I don't compute. You need an expert-comptable or your service des impôts des particuliers."

When a refusal fires:
1. Stop the workflow
2. State the specific reason in one sentence
3. Recommend the path forward (specific practitioner type)
4. Offer to continue with partial help ONLY if the out-of-scope item is cleanly separable (rare)

**Do not:**
- Apologise profusely
- Try to work around the refusal
- Suggest the user "might be able to" fit into scope if they answer differently
- Continue silently

## Section 10: Self-checks

**Check IN1: No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, the check fails.

**Check IN2: Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3: Upload-first flow honoured.** After the refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4: Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before the gap-filling questions (Section 6).

**Check IN5: Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay URSSAF" after the bank statement showed URSSAF debits, the check fails.

**Check IN6: Open flags captured.** Anything ambiguous, risky or attention-worthy found during inference is in the `open_flags` list in the handoff package.

**Check IN7: Handoff to `fr-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was invoked with the intake package.

**Check IN8: Reviewer step was stated upfront and repeated before handoff.** The opening message mentioned expert-comptable sign-off.

**Check IN9: Refusals were clean.** No hedging. Stop means stop.

**Check IN10: No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," and so on.

**Check IN11: Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch, 1 upload, 1 confirmation, 1 to 3 gap fills, 1 handoff). More than 12 turns for a normal intake is a check failure.

- **Check IN12: Income year and TVA regime established.** The income year (Q0) and the TVA regime (franchise en base, réel simplifié or réel normal) were confirmed before inference, as they change which limits apply and how every transaction is classified.
- **Check IN13: Franchise en base limits tested both ways.** Turnover of the previous year was tested against the basic limit and turnover of the current year against the higher limit, in the franchise table above. If either is exceeded, the franchise ends from the date the page gives, and TVA registration must be flagged.
- **Check IN14: The right year's micro limits.** The micro limits shown to the client and tested were those for the income year at Q0, and the regime was treated as lost only after two consecutive years over the limit.

## Section 11: Performance targets

For a prepared user (documents in a folder, ready to upload):
- **Refusal sweep**: 60 seconds (1 to 2 interactive turns)
- **Document upload**: 2 minutes (1 upload turn)
- **Inference and confirmation display**: 1 minute of processing and 1 turn for user confirmation
- **Gap filling**: 2 minutes (2 to 3 interactive turns)
- **Handoff**: immediate
- **Total**: about 7 minutes

For an unprepared user (has to go and fetch documents):
- Refusal sweep: same
- Document discovery: 10 to 20 minutes offline
- Rest: same
- **Total**: 15 to 25 minutes

## Section 12: Cross-skill references

**Inputs:** user-provided documents and answers.

**Outputs:** structured intake package consumed by `fr-return-assembly`.

**Skills the package feeds (through `fr-return-assembly`):**
- `france-vat-return`: the TVA return (CA3/CA12). A business inside the franchise en base files no VAT return; the franchise test is in this skill.
- `fr-income-tax`: the income tax return (2042 / 2042-C-PRO / 2035 / 2031), the prélèvement à la source and its instalments, and the versement libératoire.
- `fr-social-contributions`: social contributions (URSSAF micro-social or the self-employed réel scales).
- `fr-cfe`: the cotisation foncière des entreprises.
- `fr-personal-income-tax`: the household computation, credits and reductions.
- `fr-capital-gains` and `fr-rental-income`: investment and rental income found at Q6.

## Reference tables used by the inference pass

**VAT rates in mainland France**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1013-PGP.html |  |
| Standard rate | 20% | "la seconde du taux de 20 %" | https://bofip.impots.gouv.fr/bofip/1013-PGP.html (2026) |
| Intermediate rate | 10% | "soumet au taux de 10 % de la TVA les abonnements" | same (2026) |
| Reduced rate | 5.5% | "relevant du taux réduit de 5,5 % de la TVA" | same (2026) |

**VAT filing and instalments (réel simplifié and réel normal)**

The page is stamped "Vérifié le 21 février 2026".

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |  |
| Réel simplifié, year closing 31 December: first instalment in July, share of the previous year's VAT | 55% | "l'entreprise doit verser 55 % de la taxe due l'année précédente" | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 (2026) |
| Réel simplifié: second instalment in December, share of the previous year's VAT | 40% | "l'entreprise doit verser 40 % de la taxe due l'année précédente" | same (2026) |
| Réel simplifié: no instalments the following year where the VAT paid the previous year was below | EUR 1,000 | "un montant de TVA inférieur à 1 000 € l'année précédente est dispensée" | same (2026) |
| Réel normal: the return is quarterly instead of monthly where the VAT due each year is below | EUR 4,000 | "le montant de la TVA exigible chaque année est inférieur à 4 000 €" | same (2026) |

The CA12 is filed "au plus tard le 2 e jour ouvré suivant le 1 er mai" for a year closing on 31 December, and the balance is paid with it (https://entreprendre.service-public.gouv.fr/vosdroits/F23566).

**CFE**

The page is stamped "Vérifié le 02 avril 2026".

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |  |
| Exemption where turnover excluding VAT of the year before last (N-2), or of the first year for a business created in N-1, did not exceed | EUR 5,000 | "n'a pas dépassé 5 000 €" | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 (2026) |

A business is exempt from CFE in the year it is created, "Ensuite, sa base d'imposition est réduite de moitié l'année suivante"; the CFE is in general payable "au plus tard le 15 décembre (inclus)" (https://entreprendre.service-public.gouv.fr/vosdroits/F23547). The amount itself is set by the commune: see `fr-cfe`.

**Small equipment taken to expense**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |  |
| Unit value excluding VAT up to which materials and tools may be deducted immediately | EUR 500 | "d'une valeur unitaire hors taxes n'excédant pas 500 €" | https://bofip.impots.gouv.fr/bofip/2109-PGP.html (2026) |

**Investment income: the flat tax is two parts**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 |  |
| Income tax part of the prélèvement forfaitaire unique | 12.8% | "l'impôt sur le revenu ( 12,8 % )" | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 (2026) |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |  |
| Social levies, investment income of 2026, general case | 18.6% | under "Revenus de 2026", cas général: "18,6 %" in the total row | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| Social levies, investment income of 2025 | 17.2% | under "Revenus de 2025": "17,2 %" in the total row | same |

The levies differ again for rental income, property gains and some savings products: `fr-capital-gains` and `fr-rental-income` carry them.

## The method, step by step

1. **Fix the income year and the return type** (Q0). The filing dates for 2025 income and the online correction window are on https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 . A return on 2025 income that was never filed is referred (R-FR-8).
2. **Fix the legal form and the tax regime** (Q1, Q2). Test turnover of N-1 and N-2 against the micro limits for that income year on https://entreprendre.service-public.gouv.fr/vosdroits/F23267 ; the micro regime is lost only after two consecutive years over the limit. Note the boxes of the 2042-C-PRO or the professional return (2031-SD, 2035-SD) from https://www.impots.gouv.fr/professionnel/resultat-imposable-limpot-sur-le-revenu-ir-ou-limpot-sur-les-societes .
3. **Fix the TVA regime** (Q3). Test the franchise en base on both limits of https://entreprendre.service-public.gouv.fr/vosdroits/F21746 ; for a réel regime, note the frequency and the instalments from https://entreprendre.service-public.gouv.fr/vosdroits/F23566 .
4. **Fix the social status** (Q4). Read the micro-social rate and, for a new business, the Acre rate by start date from https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html .
5. **Fix the household** (Q5 to Q8). Parts from https://www.service-public.gouv.fr/particuliers/vosdroits/F2705 ; other income routed to its skill.
6. **Collect and parse the documents** (Sections 3 and 4). Check the versement libératoire ceiling on both pages (https://entreprendre.service-public.gouv.fr/vosdroits/F23267 and https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur), the CFE exemptions on https://entreprendre.service-public.gouv.fr/vosdroits/F23547 and the small-equipment limit on https://bofip.impots.gouv.fr/bofip/2109-PGP.html .
7. **Confirm, fill the gaps, hand off** (Sections 5 to 7), with every flag in `open_flags`.

## Ask the client first

- Which income year is this, and has a return for it already been filed? It decides the limits, the forms and whether this is a correction, a late return or a preparation.
- What was your turnover excluding VAT in each of the two previous years, and in the current year so far? Two consecutive years over the micro limit end the micro regime, and the current-year turnover alone can end the VAT franchise from the first day of the overrun.
- When did the activity start, and did you apply for Acre? The Acre rate depends on a start date up to 30 June 2026 or from 1 July 2026, and it runs only to the end of the third calendar quarter following the quarter in which the activity started.
- Did you opt for the versement libératoire, and what was your household's reference income two years earlier? Two official pages give different ceilings.
- Are any of your clients outside France, and are they businesses or consumers? A service to an EU business can shift the VAT to the customer and bring a DES.
- Are you married or PACSé, do you file jointly, and how many children live with you full time or in shared residence? It decides the parts and whose income goes on the return.

## When to refuse or refer

- Refuse when any of R-FR-1 to R-FR-8 fires.
- Refer when the turnover of the current year has crossed a franchise limit during the year: invoices already issued without VAT may need correcting, and the start date of VAT has to be fixed by the reviewer.
- Refer when the client was over the micro limit in both of the two previous years but kept filing as a micro-entrepreneur.
- Refer when the client's reference income falls between the two versement libératoire ceilings for their household.
- Refer when the client is in an overseas département, lets furnished tourist accommodation alongside another activity, or has a mixed activity (sales and services): each has its own limits that this skill does not test.
- Do not compute tax, contributions, penalties or interest from this skill. It hands off to `fr-return-assembly`.

### Change log

- **v1.0 (May 2026):** Initial draft. Upload-first, inference-then-confirm pattern.
- **October 2026:** Refreshed against official pages: income year question added; micro limits for both income years; VAT franchise limits for 2026; micro-social and Acre rates for 2026; downstream skill names corrected.

## Sources

- Régime fiscal de la micro-entreprise: https://entreprendre.service-public.gouv.fr/vosdroits/F23267 (read 2026-10-31)
- Comment déclarer les revenus provenant de mon activité de micro-entrepreneur ?: https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur (read 2026-10-31)
- Résultat imposable à l'impôt sur le revenu (IR) ou à l'impôt sur les sociétés (IS): https://www.impots.gouv.fr/professionnel/resultat-imposable-limpot-sur-le-revenu-ir-ou-limpot-sur-les-societes (read 2026-10-31)
- Les modalités de la déclaration de revenus en 2026: https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 (read 2026-10-31)
- Franchise en base de TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F21746 (read 2026-10-31)
- Déclarer et payer la TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F23566 (read 2026-10-31)
- VAT rates on services: https://bofip.impots.gouv.fr/bofip/1013-PGP.html (read 2026-10-31)
- Notice to the CA3, 2026: https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf (read 2026-10-31)
- L'essentiel du statut (auto-entrepreneur): https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html (read 2026-10-31)
- Quotient familial d'un couple marié ou pacsé: https://www.service-public.gouv.fr/particuliers/vosdroits/F2705 (read 2026-10-31)
- Cotisation foncière des entreprises: https://entreprendre.service-public.gouv.fr/vosdroits/F23547 (read 2026-10-31)
- Small-value equipment: https://bofip.impots.gouv.fr/bofip/2109-PGP.html (read 2026-10-31)
- Barème, flat deduction on salaries: https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 (read 2026-10-31)
- Revenus d'épargne et de placement: https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 (read 2026-10-31)
- Prélèvements sociaux sur les revenus du patrimoine et de placement: https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 (read 2026-10-31)

Not yet confirmed: the flat-payment ceiling for the option taken in 2026. F23267 prints EUR 29,579 for a single person against year N-2, and impots.gouv.fr prints EUR 29,315 against the 2024 reference income.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional, such as an expert-comptable or an equivalent licensed practitioner in your jurisdiction, before filing or acting upon.

The most up-to-date version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
