---
name: it-income-tax
description: >
  Use this skill whenever asked about Italian income tax for self-employed individuals (lavoratori autonomi, liberi professionisti). Trigger on phrases like "Modello Redditi PF", "Quadro RE", "IRPEF", "redditi di lavoro autonomo", "imposta sul reddito Italy", "deduzioni", "detrazioni", "addizionale regionale", "addizionale comunale", "regime ordinario", "acconti IRPEF", "no tax area", "regime forfettario comparison", "partita IVA", "flat tax 15%", or any question about filing or computing income tax for an Italian freelancer or professional. Covers progressive IRPEF brackets (23–43%), regime forfettario (15% flat tax, 5% startup), deduzioni/detrazioni, addizionali regionali/comunali, acconti IRPEF, Quadro RE, INPS Gestione Separata, and penalties.
version: 2.0
---

# Italy Income Tax — Self-Employed / Libero Professionista (IRPEF)

## Section 1 — Quick Reference

### IRPEF Brackets (2025 — Regime Ordinario)
| Reddito imponibile (EUR) | Aliquota |
|---|---|
| 0 – 28,000 | 23% |
| 28,001 – 50,000 | 35% |
| Over 50,000 | 43% |

**No-tax area (detrazione lavoro autonomo):** Deduction of up to €5,500 for income ≤ €5,500; phases out to zero at €55,000. Reduces IRPEF payable (not taxable income).

**Addizionale regionale:** 1.23%–3.33% (varies by region; 1.23% is the minimum national floor; each region sets its own rate)

**Addizionale comunale:** 0%–0.9% (set by each municipality; average ~0.4%)

### Regime Forfettario (Flat Tax — Alternative to Regime Ordinario)
| Feature | Value |
|---|---|
| Revenue threshold (2025) | ≤ €85,000 |
| Flat tax rate | 15% |
| Startup rate (first 5 years) | 5% (if first-ever business; no prior employment in same sector) |
| Tax base | Revenue × (1 − coefficiente di redditività) |
| Coefficiente di redditività | 78% for most professional activities (so taxable income = 78% × revenue) |
| IVA obligation | Exempt from IVA — no IVA on invoices, no IVA recovery |
| Social contributions (INPS) | Reduced 35% discount for forfettari on Gestione Separata |
| Studi di settore / ISA | Exempt |
| Contraindications | Cannot claim business expenses; cannot recover IVA on purchases |

**Regime forfettario vs ordinario decision:**
- Forfettario better when: revenue ≤ €85,000 AND actual deductible expenses < (1 − coefficiente) × revenue = 22% for professionisti
- Ordinario better when: high deductible expenses (>22% of revenue), OR significant personal detrazioni, OR very high income (43% bracket same as flat tax becomes competitive)

### IRPEF Detrazioni d'Imposta (Tax Credits — Regime Ordinario)
| Detrazione | Amount |
|---|---|
| Lavoro autonomo base detrazione | Up to €5,500 (phases out to 0 at €55,000) |
| Familiari a carico (spouse) | €800 (phases out above €80,000) |
| Familiari a carico (each child <21) | €950 per child (phases out with income) |
| Spese mediche | 19% of expenses exceeding €129.11 |
| Interessi mutuo prima casa | 19% of interest, max €4,000 |
| Spese istruzione universitaria | 19% of university fees |
| Premi assicurazione vita/infortuni | 19%, max €530 |
| Donazioni (onlus) | 30% or 35% (for social enterprises) |
| Spese ristrutturazione (bonus) | 36–50% of works (spread over 10 years) |

### Conservative Defaults
| Item | Default |
|---|---|
| Regime choice | Forfettario if revenue ≤ €85,000 and no documentation of higher expenses |
| Home office % | Do not assume — ask for floor area |
| Vehicle business % | Do not assume — ask for km log |
| Phone/internet | 50% if mixed use |
| Addizionale regionale | Use 1.23% (minimum) unless region confirmed |
| Forfettario coefficiente | 78% (professional activities) unless specific ATECO code confirmed |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Revenue > €85,000 | Must use regime ordinario |
| Revenue approaching €85,000 | Warn — exceeding threshold in-year triggers ordinario for entire year |
| Two employees earning >€20,000 combined | Forfettario exclusion — flag |
| Participation in partnerships | May exclude from forfettario |
| Expenses > 22% of revenue (forfettario) | Forfettario may not be optimal — recalculate |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross revenue (compensi lordi) for the year
2. Regime chosen: forfettario or ordinario
3. If ordinario: itemised deductible professional expenses (spese inerenti)
4. ATECO code (for forfettario coefficiente confirmation)
5. INPS Gestione Separata contributions paid
6. Personal situation: spouse, children, family members a carico
7. Acconti IRPEF already paid during the year

### Refusal Catalogue
**R-IT-1 — Forfettario threshold exceeded**
If gross revenue > €85,000: forfettario not available. State: "Your revenue exceeds the €85,000 forfettario threshold. You must use the regime ordinario and file Modello Redditi PF with Quadro RE."

**R-IT-2 — No expense documentation (ordinario)**
Refuse undocumented professional expenses. State: "Without receipts and records, we cannot deduct these costs as spese inerenti in Quadro RE. Only expenses inherent to and necessary for professional activity are deductible."

**R-IT-3 — Personal expenses as professional costs**
Refuse personal costs (personal vacations, family meals, personal clothing). State: "These are personal expenses. Only costs inerenti to the professional activity are deductible under TUIR art. 54."

**R-IT-4 — IVA amounts included in compensi**
If client has partita IVA in ordinario: compensi on Quadro RE must be net of IVA. State: "IVA collected from clients is not your income — remove IVA before entering compensi on Quadro RE."

**R-IT-5 — Forfettario and IVA recovery**
In forfettario, client cannot recover IVA on purchases. Do not include IVA-recovery calculations for forfettario clients. State: "Regime forfettario clients are exempt from IVA but also cannot deduct input IVA on purchases."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| Bonifico da cliente | Compensi professionali | Include gross (net of IVA if registered) | |
| Pagamento fattura / SEPA credit | Professional fees | Include | |
| Bonifico estero / SWIFT | Foreign client payment | Include — convert to EUR at receipt date | |
| Stripe accredito / STRIPE | Platform receipts | Include net + Stripe fee as expense | |
| PayPal accredito | Platform receipts | EUR equivalent | |
| Marketplace / Fiverr / Upwork | Platform receipts | Gross earnings | Platform fee = spesa |
| Interessi bancari | Interessi (redditi di capitale) | Separate — subject to 26% ritenuta | Not Quadro RE |
| Canoni di locazione | Redditi fondiari | Separate — Quadro RB or cedolare secca | Not Quadro RE |
| Anticipo (advance payment) | Competence-based | Include in year received (cassa principle) | |
| Rimborso spese (pass-through) | Exclude if pure reimbursement | Check if included in fattura or separate | |

### 3.2 Expense Patterns (Spese Inerenti — Regime Ordinario Only)
| Bank Description Pattern | Categoria | Deducibile? | Note |
|---|---|---|---|
| TIM / Vodafone / WindTre / Iliad | Telefono | Parziale — 80% se linea professionale | T2 se uso misto |
| Enel / A2A / Iren / Edison | Energia elettrica | % ufficio domestico | T2 |
| ENI gas / Italgas | Gas riscaldamento | % ufficio domestico | T2 |
| Affitto ufficio / locale professionale | Canone professionale | 100% | Deve essere uso esclusivo professionale |
| Software / SaaS (Adobe, Figma, ecc.) | Software | 100% | Uso professionale |
| Amazon (materiale ufficio) | Cancelleria / forniture | 100% se uso professionale | |
| Trenitalia / Italo / Frecciarossa | Viaggio professionale | 100% — scopo professionale documentato | |
| Alitalia / Ryanair / EasyJet | Viaggio professionale | 100% — documentare | |
| Hotel / Airbnb (deplacement professionale) | Alloggio | 100% — scopo professionale | |
| Ristorante (pasto di lavoro con cliente) | Spese di rappresentanza | 75% (TUIR art. 54 c.5) | Limite annuo |
| INPS Gestione Separata | Contributi previdenziali | Deducibili su Quadro RE (50%) e su Quadro RP (50%) | IMPORTANTE |
| Commercialista / dottore commercialista | Onorari professionali | 100% | |
| Corsi di formazione professionale | Formazione | 100% — inerente attività | |
| Libri / pubblicazioni professionali | Documentazione | 100% — inerenti | |
| Assicurazione professionale (RCP) | Assicurazione | 100% | |
| Materiale amortizzabile (>€516 HT) | Beni strumentali | Quote di ammortamento (TUIR) | Non spesa immediata |
| Materiale <€516 | Attrezzatura minore | 100% nell'anno | |
| IVA versata all'erario | IVA | ESCLUSA — non deducibile IRPEF | |
| IRPEF versata / acconti | Imposta | ESCLUSA | |
| Spese personali | Personale | ESCLUSE | |

### 3.3 INPS Gestione Separata (Special Treatment)
- Self-employed without separate INPS cassa (most liberi professionisti without an Ordine with mandatory cassa): pay into **Gestione Separata INPS**
- Rate 2025: 26.23% of net professional income (up to INPS ceiling; then 0% above)
- 50% deductible directly from Quadro RE (reducing reddito di lavoro autonomo)
- Remaining 50% deductible in Quadro RP as onere deducibile
- Professionals with mandatory INPS cassa (doctors: ENPAM, lawyers: CNPA, engineers: INARCASSA): different — their cassa contributions = 100% deductible from RE

### 3.4 Foreign Currency & Platform Receipts
| Source | Currency | Treatment |
|---|---|---|
| USD from US clients | USD | Convert to EUR at Banca d'Italia rate on invoice/payment date |
| GBP from UK clients | GBP | Convert at payment date |
| Stripe USD | USD | Use Stripe statement EUR equivalent |
| PayPal multi-currency | Various | Use PayPal statement EUR equivalent |
| Upwork USD | USD | Gross USD → convert to EUR; platform fee = spesa deducibile |
| Google AdSense | USD/EUR | Monthly → convert if USD |

### 3.5 Internal Transfers
| Pattern | Treatment |
|---|---|
| Bonifico verso conto risparmio | ESCLUSO — trasferimento interno |
| Pagamento carta di credito | ESCLUSO — singole spese già catturate |
| Bonifico tra propri conti | ESCLUSO |
| Rimborso prestito personale | ESCLUSO — non è reddito |

---

## Section 4 — Worked Examples

### Example 1 — UniCredit: Consulente IT, Regime Ordinario
**Scenario:** Consulente IT, €90,000 compensi, €20,000 spese, INPS Gestione Separata €23,607, single

**Bank statement extract (UniCredit):**
```
Data valuta  | Descrizione                                | Dare (€)      | Avere (€)     | Saldo (€)
15/04/2025   | BON. ACCRED. TECHCORP SRL                 |               | 18,000.00     | 75,000.00
20/04/2025   | BON. ACCRED. STARTUP ITALIA SRL           |               |  9,000.00     | 84,000.00
25/04/2025   | ADD. GESTIONE SEPARATA INPS               | 1,967.25      |               | 82,032.75
28/04/2025   | PAGAMENTO ADOBE CC                        |    79.00      |               | 81,953.75
30/04/2025   | COMMISSIONI BANCARIE                      |    10.00      |               | 81,943.75
```

**Quadro RE Computation:**
| Linea | Importo |
|---|---|
| Compensi lordi (RE5) | €90,000 |
| INPS Gestione Separata 50% deducibile RE (RE17) | (€11,804) |
| Altre spese inerenti (RE14) | (€20,000) |
| **Reddito netto Quadro RE** | **€58,196** |

**IRPEF Computation:**
| Linea | Importo |
|---|---|
| Reddito lavoro autonomo | €58,196 |
| INPS 50% restante (Quadro RP) | (€11,804) |
| Reddito complessivo | €46,392 |
| Detrazione lavoro autonomo (phased out) | ~€0 (reddito > €55,000) |
| IRPEF: 23% × €28,000 + 35% × (46,392−28,000) | €6,440 + €6,437 = **€12,877** |
| Addizionale regionale (~1.7% Roma) | ₩787 |
| Addizionale comunale (~0.5%) | €232 |

### Example 2 — Intesa Sanpaolo: Designer, Regime Forfettario
**Scenario:** Graphic designer, €55,000 compensi, regime forfettario, ATECO 74.10 (coefficiente 78%)

**Bank statement extract (Intesa Sanpaolo):**
```
Data operaz. | Causale                                    | Addebiti (€)  | Accrediti (€) | Saldo (€)
10/03/2025   | RIACCREDITO STUDIO CREATIVO SRL           |               | 8,500.00      | 34,200.00
15/03/2025   | ACCREDITO AGENZIA DIGITALE                |               | 5,000.00      | 39,200.00
20/03/2025   | ADDEBITO FIGMA INC                        | 45.00         |               | 39,155.00
22/03/2025   | ADDEBITO TRENITALIA                       | 89.00         |               | 39,066.00
28/03/2025   | COMMISSIONI SDD                           | 2.50          |               | 39,063.50
```

**Regime Forfettario Computation:**
| Linea | Importo |
|---|---|
| Compensi lordi | €55,000 |
| Reddito imponibile (78%): €55,000 × 78% | €42,900 |
| INPS Gestione Separata (forfettario, riduzione 35%): 26.23% × 65% × €42,900 | €7,314 (approx; reduces taxable income) |
| Reddito imponibile netto | €35,586 |
| Imposta sostitutiva 15% | **€5,338** |
| Note: IVA NOT charged on invoices | Regime forfettario |

**Comparison with ordinario at same revenue:** IRPEF ordinario would be ~€8,500–10,000 → forfettario saves ~€3,000–5,000 at this income level.

### Example 3 — Banco BPM: Avvocato (Lawyer), Cassa Forense
**Scenario:** Avvocato with Cassa Forense (mandatory pension), €120,000 compensi, €30,000 spese, Cassa Forense €15,000

**Bank statement extract (Banco BPM):**
```
Data          | Descrizione                               | Importo addebitato | Importo accreditato | Saldo
08/05/2025    | BON. ENTRATA CLIENTI STUDIO LEGALE       |                    | 25,000.00           | 98,000.00
12/05/2025    | BON. ENTRATA STUDIO LEGALE ASSOC.        |                    | 10,000.00           | 108,000.00
15/05/2025    | VERS. CASSA FORENSE TRIMESTRALE          | 3,750.00           |                     | 104,250.00
20/05/2025    | PAGAMENTO AFFITTO STUDIO                 | 1,200.00           |                     | 103,050.00
25/05/2025    | ADDEBITO LEXIS NEXIS ABBONAMENTO         | 350.00             |                     | 102,700.00
```

**Avvocati note:** Cassa Forense (not INPS GS) = mandatory; contributions 100% deductible on RE (not 50/50 split). Also: lawyers add 4% rivalsa to client invoices (contributo integrativo).

**Quadro RE:**
| Linea | Importo |
|---|---|
| Compensi lordi | €120,000 |
| Contributi integrativi 4% incassati (rivalsa) | Inclusi nei compensi — poi spesa |
| Cassa Forense (100% deducibile RE) | (€15,000) |
| Altre spese | (€30,000) |
| **Reddito RE netto** | **€75,000** |
| IRPEF: 23% × €28,000 + 35% × €22,000 + 43% × €25,000 | €6,440 + €7,700 + €10,750 = **€24,890** |

### Example 4 — Monte dei Paschi di Siena: Freelancer con Home Office
**Scenario:** Copywriter, €38,000 compensi, regime ordinario, home office (appartamento 70mq, studio 10mq)

**Bank statement extract (MPS):**
```
Data         | Descrizione                                | Uscite (€)    | Entrate (€)   | Saldo (€)
05/06/2025   | BONIFICO IN ENTRATA EDITORE SRL           |               | 5,000.00      | 18,500.00
10/06/2025   | BONIFICO IN ENTRATA AGENZIA COPY          |               | 3,200.00      | 21,700.00
15/06/2025   | UTENZA ENEL ENERGIA                       | 180.00        |               | 21,520.00
20/06/2025   | AFFITTO MENSILE (gestore)                 | 900.00        |               | 20,620.00
25/06/2025   | ABBONAMENTO INTERNET TELECOM              | 35.00         |               | 20,585.00
```

**Home office calculation (studio a casa):**
- % uso professionale: 10/70 = 14.3%
- Affitto annuo €10,800 × 14.3% = €1,545 deducibile
- Utenze annue €2,160 × 14.3% = €309 deducibile

**Quadro RE:**
| Linea | Importo |
|---|---|
| Compensi | €38,000 |
| Spese dirette | (€4,000) |
| Home office (affitto + utenze) | (€1,854) |
| INPS GS 50% | (€4,980) |
| **Reddito RE** | **€27,166** |
| IRPEF (23%): €27,166 × 23% | €6,248 |
| Detrazione lavoro autonomo (reddito < €55K) | phased — approx. (€1,200) |
| **IRPEF netta** | **~€5,048** |

### Example 5 — BPER Banca: Developer con Startup Forfettario
**Scenario:** Sviluppatore software, primo anno attività, €42,000 compensi, regime forfettario 5% (startup rate)

**Bank statement extract (BPER Banca):**
```
Data          | Descrizione                               | Addebito (€)  | Accredito (€) | Saldo (€)
12/07/2025    | ACCREDITO CLIENTE STARTUP.IO              |               | 12,000.00     | 32,000.00
18/07/2025    | ACCREDITO FREELANCER PORTAL               |               |  6,500.00     | 38,500.00
22/07/2025    | ADDEBITO GITHUB ENTERPRISE                | 180.00        |               | 38,320.00
26/07/2025    | ADDEBITO AWS AMAZON                       | 245.00        |               | 38,075.00
30/07/2025    | COMMISSIONI BPER                          | 8.00          |               | 38,067.00
```

**Regime forfettario 5% (startup):**
| Linea | Importo |
|---|---|
| Compensi | €42,000 |
| Reddito imponibile (78%): €42,000 × 78% | €32,760 |
| INPS ridotta 35%: approx. €5,600 | deducible from €32,760 |
| Reddito netto | €27,160 |
| Imposta sostitutiva 5% | **€1,358** |
| Note: available for first 5 years if conditions met | |

### Example 6 — Fineco Bank: Architetto con IVA e Acconti
**Scenario:** Architetto (regime ordinario), €150,000 compensi IVA esclusa, €45,000 spese, acconti IRPEF €18,000 già versati

**Bank statement extract (Fineco):**
```
Data valuta   | Descrizione                               | Dare (€)      | Avere (€)     | Saldo (€)
03/08/2025    | ACCREDITO BONIFICO STUDIO ARCH. BIANCHI  |               | 36,600.00     | 142,000.00
10/08/2025    | ACCREDITO BONIFICO PROMOZIONE IMM. SRL   |               | 24,400.00     | 166,400.00
15/08/2025    | VERSAMENTO ACCONTO IRPEF F24              | 9,000.00      |               | 157,400.00
20/08/2025    | ADDEBITO INARCASSA TRIMESTRALE            | 3,500.00      |               | 153,900.00
25/08/2025    | ADDEBITO AFFITTO STUDIO                   | 2,500.00      |               | 151,400.00
```

**Note on bonifici:** €36,600 = €30,000 + €6,000 IVA 20%. Compensi = €30,000 only (HT). Always separate IVA.

**Quadro RE:**
| Linea | Importo |
|---|---|
| Compensi IVA esclusa | €150,000 |
| Inarcassa (100% deducibile RE) | (€21,000) |
| Altre spese | (€45,000) |
| **Reddito RE** | **€84,000** |
| IRPEF: 23%×28K + 35%×22K + 43%×34K | €6,440+€7,700+€14,620 = **€28,760** |
| Meno: acconti già versati | (€18,000) |
| **IRPEF a saldo** | **€10,760** |

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Residenza Fiscale
- **Residente:** Iscritto all'anagrafe OR domicilio/residenza in Italia per >183 giorni → redditi worldwide tassati in Italia
- **Non residente:** Solo redditi di fonte italiana; ritenute alla fonte diverse

### Principio di Cassa vs Competenza
- Lavoro autonomo: **principio di cassa** (cash basis) — compensi e spese nella dichiarazione dell'anno in cui pagati/incassati
- Eccezione: ammortamenti (depreciation) seguono principio di competenza (spread over useful life)

### IVA e Regime Forfettario
- Regime forfettario: esonerato da IVA — nessuna IVA sulle fatture, nessun recupero IVA sugli acquisti
- Regime ordinario: partita IVA attiva — IVA sulle fatture, dichiarazione IVA periodica separata

### Rivalsa INPS
- Professionisti INPS Gestione Separata: possono aggiungere 4% di rivalsa sulle fatture ai clienti (rivalsa previdenziale)
- La rivalsa è reddito — inclusa nei compensi (ma poi diventa costo previdenziale)
- Non confondere con la rivalsa IVA

### Acconti IRPEF
- Se IRPEF anno precedente > €51.65: obbligo acconti
- 1° acconto: 40% dell'IRPEF precedente — scadenza **30 giugno** (o luglio con maggiorazione 0.4%)
- 2° acconto: 60% — scadenza **30 novembre**
- Versamento tramite modello F24

### Deduzioni vs Detrazioni
- **Deduzioni (deducibili):** Riducono il reddito imponibile prima di applicare le aliquote (es. spese inerenti, INPS, contributi previdenziali)
- **Detrazioni (creditorie):** Riducono l'IRPEF lorda dopo il calcolo (es. spese mediche 19%, interessi mutuo 19%, carichi di famiglia)

### Scadenze
| Evento | Scadenza |
|---|---|
| Modello Redditi PF (online) | 31 ottobre (anno successivo) |
| Pagamento saldo IRPEF + 1° acconto | 30 giugno (o 30 luglio +0.4%) |
| 2° acconto IRPEF | 30 novembre |
| Liquidazione IVA trimestrale | Entro il 16° giorno del 2° mese successivo |

### Sanzioni
| Situazione | Sanzione |
|---|---|
| Omessa dichiarazione | 120%–240% dell'imposta dovuta |
| Dichiarazione infedele | 70%–210% dell'imposta |
| Tardivo versamento | 15%–30% dell'importo + interessi |
| Ravvedimento operoso | Riduzione sanzione se regolarizzato spontaneamente |

---

## Section 6 — Tier 2 Catalogue

### T2-IT-1: Studio a Casa / Home Office
**Perché T2:** La proporzione di utilizzo professionale dipende da dati che solo il cliente conosce.

**Metodo:** m² uso professionale ÷ m² totale × canone/utenze
**Requisiti dal cliente:** Superficie totale appartamento (m²), superficie studio/ufficio dedicato (m²), conferma uso esclusivo professionale (non misto).
**Avvertenza:** L'Agenzia delle Entrate può contestare l'uso esclusivo se lo studio è in una stanza condivisa — documentare bene.

### T2-IT-2: Uso Promiscuo del Veicolo (Auto)
**Perché T2:** La proporzione di uso professionale dipende dai km effettivi percorsi.

**Opzioni:**
1. **Rimborso chilometrico ACI:** Usare le tabelle ACI pubblicate annualmente per il rimborso km
2. **Costi reali × %:** Documentare km business vs km totali
3. **Forfait 20%:** Per veicoli ad uso promiscuo — TUIR art. 54 c.1-bis: deducibilità limitata al 20% dei costi (max €5,164.57)

**Requisiti dal cliente:** Tipo veicolo (cilindrata, carburante), km percorsi totali e per motivi professionali, costi sostenuti (carburante, assicurazione, manutenzione).

### T2-IT-3: Telefono e Internet
**Perché T2:** Uso misto professionale/personale — solo il cliente conosce la proporzione.

**Regola TUIR:** Telefono fisso e cellulare: 80% deducibile se uso promiscuo (limite fiscale). Internet: proporzione uso professionale.

**Requisiti dal cliente:** Conferma se linea esclusivamente professionale o mista.

### T2-IT-4: Spese di Rappresentanza
**Perché T2:** La natura (con cliente o da solo) e il motivo professionale devono venire dal cliente.

**Regole TUIR art. 54 c.5:**
- Pasti con clienti: 75% deducibili (con limite plafond annuo = 1% dei compensi)
- Omaggi: 75% fino a €50 unitario
- Senza documentazione del cliente presente: non deducibili

### T2-IT-5: Regime Forfettario vs Ordinario
**Perché T2:** La scelta ottimale dipende da dati specifici del cliente (ammontare spese reali, detrazioni personali disponibili).

**Calcolo comparativo necessario:**
- Ordinario: compensi − spese − INPS → IRPEF progressiva
- Forfettario: compensi × 78% − INPS ridotta → 15% flat
- Considerare anche detrazioni personali (figli, mutuo, spese mediche) che si perdono con forfettario

---

## Section 7 — Excel Working Paper

### Foglio 1: Compensi (Revenue)
| Colonna | Contenuto |
|---|---|
| A | Data incasso |
| B | Cliente |
| C | N° fattura |
| D | Importo IVA esclusa (€) |
| E | IVA (se applicabile) |
| F | Totale fattura |
| G | Categoria (Compensi RE / Altro / Escludere) |

**Totale compensi:** `=SUMIF(G:G,"Compensi RE",D:D)`

### Foglio 2: Spese Inerenti
| Colonna | Contenuto |
|---|---|
| A | Data pagamento |
| B | Fornitore |
| C | Importo IVA esclusa (€) |
| D | Categoria |
| E | % utilizzo professionale |
| F | Importo deducibile (=C×E) |
| G | Riferimento giustificativo |

### Foglio 3: Quadro RE Riepilogo
| Linea | Rif. Quadro RE | Importo |
|---|---|---|
| Compensi lordi | RE5 | |
| Spese inerenti | RE14 | |
| INPS GS 50% | RE17 | |
| **Reddito netto** | RE20 | |
| INPS GS 50% restante | Quadro RP | |

### Foglio 4: IRPEF
| Linea | Importo |
|---|---|
| Reddito complessivo | |
| Oneri deducibili (Quadro RP) | |
| Reddito imponibile | |
| IRPEF lorda (aliquote) | |
| Detrazioni (lavoro autonomo, familiari, ecc.) | |
| IRPEF netta | |
| Acconti versati | |
| **IRPEF a saldo / rimborso** | |

---

## Section 8 — Bank Statement Reading Guide

### UniCredit
- Format: `Data valuta | Descrizione | Dare (€) | Avere (€) | Saldo (€)`
- Date: DD/MM/YYYY
- Income = Avere (credit) column
- Key: "BON. ACCRED." = bonifico accreditato (incoming wire)

### Intesa Sanpaolo
- Format: `Data operaz. | Causale | Addebiti (€) | Accrediti (€) | Saldo (€)`
- Date: DD/MM/YYYY
- Income = Accrediti

### Banco BPM
- Format: `Data | Descrizione | Importo addebitato | Importo accreditato | Saldo`
- Date: DD/MM/YYYY
- Income = Importo accreditato

### Monte dei Paschi di Siena (MPS)
- Format: `Data | Descrizione | Uscite (€) | Entrate (€) | Saldo (€)`
- Date: DD/MM/YYYY
- Income = Entrate column

### Fineco Bank
- Format: `Data valuta | Descrizione | Dare (€) | Avere (€) | Saldo (€)`
- Date: DD/MM/YYYY
- Income = Avere; "ACCREDITO BONIFICO" = incoming wire

### BPER Banca
- Format: `Data | Descrizione | Addebito (€) | Accredito (€) | Saldo (€)`
- Date: DD/MM/YYYY
- Income = Accredito

### Exclusion Patterns (all Italian banks)
| Pattern | Action |
|---|---|
| BONIFICO VERSO CONTO PROPRIO | ESCLUSO — trasferimento interno |
| PAGAMENTO CARTA / ADDEBITO CARTA | ESCLUSO — singole spese già catturate |
| VERSAMENTO IVA F24 | ESCLUSO — non deducibile IRPEF |
| VERSAMENTO ACCONTO IRPEF F24 | Accredito verso erario — NON spesa (diventa credito in dichiarazione) |
| RIENTRO PRESTITO / MUTUO (quota capitale) | ESCLUSO — non è spesa professionale |
| ADDEBITO CANONE BANCA | Sì — spese bancarie deducibili |

---

## Section 9 — Onboarding Fallback

**Priorità 1 (bloccante):**
1. "Qual è stato il totale dei tuoi compensi lordi (IVA esclusa) per l'anno fiscale?"
2. "Stai usando il regime forfettario o il regime ordinario?"
3. "Qual è il tuo codice ATECO di attività?"

**Priorità 2 (per calcolo accurato):**
4. "Hai ricevute e giustificativi per tutte le spese professionali?"
5. "Lavori da casa? Se sì: superficie totale appartamento e superficie ufficio?"
6. "Hai versato contributi INPS Gestione Separata o contributi a una cassa professionale? Importo totale?"
7. "Sei single, sposato/a, o con figli a carico?"

**Priorità 3 (detrazioni aggiuntive):**
8. "Hai avuto spese mediche significative nell'anno?"
9. "Hai un mutuo per la prima casa? Importo interessi passivi pagati?"
10. "Hai già versato acconti IRPEF? Importo totale degli acconti versati?"

**Approccio conservativo:**
- Usa regime forfettario se redditi ≤ €85,000 e nessuna documentazione spese
- Non includere spese non documentate
- Per home office: escludi se non disponibili dati metratura

---

## Section 10 — Reference Material

### Quadro RE — Linee Principali (Modello Redditi PF)
| Linea | Descrizione |
|---|---|
| RE5 | Compensi lordi (totale) |
| RE6 | Compensi in natura / autoconsumo |
| RE14 | Spese inerenti |
| RE17 | Quote di ammortamento |
| RE19 | INPS / contributi previdenziali (50%) |
| RE20 | Reddito o perdita netta |

### Modulo F24 — Codici Tributo Principali
| Codice | Descrizione |
|---|---|
| 4001 | IRPEF saldo |
| 4033 | Primo acconto IRPEF |
| 4034 | Secondo acconto IRPEF |
| 0301–0303 | Addizionale regionale |
| 3844 | Addizionale comunale |

### Riferimenti Normativi
- TUIR art. 54: Redditi di lavoro autonomo (deduzione spese)
- TUIR art. 53: Definizione lavoro autonomo
- Legge 190/2014: Regime forfettario
- D.Lgs. 446/1997: IRAP (se applicabile a liberi professionisti)

### Piattaforme Dichiarazione
- **Redditi Online (SOGEI):** accessibile via SPID / CIE su agenziaentrate.gov.it
- **CAF / Commercialista:** tramite abilitato
- Scadenza: 31 ottobre ogni anno

---

## Prohibitions
- Non fornire consulenza su IVA (imposta sul valore aggiunto) — richiede skill separata IVA Italia
- Non fornire consulenza su IRES (imposta sul reddito delle società) — questa skill copre solo persone fisiche
- Non fornire consulenza su IRAP per liberi professionisti che potrebbero non essere soggetti — verificare con il cliente
- Non fornire consulenza su successioni o donazioni
- Non garantire l'accettazione di posizioni fiscali da parte dell'Agenzia delle Entrate — ogni situazione va verificata

## Disclaimer
Questa skill fornisce orientamento generale a scopo informativo e di pianificazione. Non costituisce consulenza fiscale. La normativa fiscale italiana è amministrata dall'Agenzia delle Entrate. I clienti devono consultare un dottore commercialista o esperto contabile iscritto all'albo per consigli specifici alla propria situazione. Le aliquote, le soglie e le deduzioni cambiano annualmente — verificare sempre le regole aggiornate su agenziaentrate.gov.it.
