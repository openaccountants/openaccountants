---
name: mx-freelance-intake
description: Use this skill when onboarding a Mexican persona física con actividad empresarial or RESICO freelancer. Trigger on phrases like "Mexico freelance", "SAT registration", "persona física", "actividad empresarial", "RESICO", "régimen fiscal México", "RFC", "CFDI", "ISR provisional", "declaración anual México", or any initial client conversation involving a Mexican self-employed individual. This skill collects essential information to determine the correct tax régimen, validates SAT compliance, and routes to the appropriate computation skill. ALWAYS read this skill before beginning any Mexican freelance intake.
version: 2.0
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-17
depends_on: []
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
tax_year_notes: "2026 onboarding and monthly compliance. Historical 2025 annual FAQ is explicitly identified; unpublished 2027 annual portal procedures are held."
---

# Mexico freelance intake

## Scope

Establish the actual tax position of a Mexican-resident self-employed **persona física** before calculating or filing anything. This Guide covers 2026 onboarding, the ordinary business/professional regime (**AEP**, LISR Title IV, Chapter II, Section I), and individual RESICO eligibility and monthly compliance. Currency is MXN; SAT administers ISR and IVA. A Mexican resident's ISR scope includes foreign-source income (LISR art. 1); a foreign customer does not by itself make a receipt exempt.

**Quick reference:** determine the regime and its effective dates from the Constancia de Situación Fiscal and change acknowledgements; reconcile actual receipts to CFDI and bank records; classify IVA separately; then send a dated, documented file to [Mexico return assembly](mx-return-assembly.md). Do not turn a registration label into proof of legal eligibility. For ordinary AEP computations, use [Mexico income tax](mx-income-tax.md) and [estimated payments](mx-estimated-tax.md), checking the source period. For RESICO annual relief and exits, follow the current rules below wherever an older pack paragraph conflicts.

This intake does not complete corporate returns, legacy RIF calculations, maquiladora/IMMEX work, nonresident or permanent-establishment returns, platform-regime filings, or treaty claims. It identifies them and preserves the documents for the correct specialist. A hold on computation does not prevent fact gathering or regularisation planning.

## Ask the client first

Use the existing records first, then obtain the six fact groups that change the result:

1. **Person, residence and period:** individual or entity; tax residence; activity; start/suspension/restart dates; calendar year and months needing correction; any foreign establishments, clients, accounts or taxes.
2. **Regime and SAT position:** current Constancia, obligation history and effective dates, RFC status, prior RIF election, shareholders/related parties, notifications, and any SAT reassignment or certificate restriction.
3. **Income and eligibility:** prior-year actual receipts, activity days if the prior period was short, current cumulative receipts, new-business estimate, salary/interest/rent/dividends/gains/platform receipts and extraordinary receipts separately. Record amounts before IVA and the statutory exclusion, if any.
4. **Evidence and payments:** all issued/received XML, cancellations/replacements, PUE/PPD and payment complements, bank and cash records, actual collection dates, tax withheld, monthly declarations, bank payment confirmations, and any zero returns despite receipts.
5. **Ownership and people:** marital property agreement, legal ownership shares and common representative if relevant; own professional work versus jointly owned business/property; employees, payroll, employer IMSS and PTU.
6. **Access, deductions and insurance:** whether the taxpayer can authenticate in SAT, assets/expenses and personal deduction evidence, IMSS scheme/NSS and dates, private insurance, prior losses, prior annual returns, instalment agreements and outstanding refund requests. The taxpayer enters credentials in the official service; do not collect passwords or private keys into the intake record.

### Documents and output record

Retain a working copy of the current Constancia; RFC and regime-change acuses; full-period bank statements for every account and a cash ledger; issued **and received** CFDI XML even for RESICO; PUE/PPD payment links and cancellation history; ISR/IVA declarations, complementary declarations, acuses **and proof of actual payment**; withholding CFDI/certificates from clients, employers, banks and platforms; prior annual return; investments register; accounting entries; payroll and employer SUA/IDSE records if relevant; own IMSS receipts and policy/contract; personal deduction support; 32-D opinion, notifications, debt/instalment records, and an open-items list.

Complete: `Client ___; RFC ___; residence ___; year/months ___; regime by effective date ___; prior-year receipts/days ___; current receipts ___; salary/interest/other chapters ___; IVA classifications ___; DIOT relief basis ___; workers/insurance ___; discrepancies ___; required corrections ___; route ___; responsible professional ___`. A positive compliance opinion is a supplementary check; it does not reconcile the figures or prove that the return is correct. SAT itself describes its declarations-presented certificate as informative, without prejudging correct compliance (CFF art. 31).

## The method, step by step

### 1. Establish the regime and stop unsafe defaults [LISR arts. 100–110, 113-E–J](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf)

| Situation | Rule and next action | Official source |
|---|---|---|
| Ordinary AEP | No RESICO revenue ceiling applies to this section. Business/professional receipts and authorised deductions feed cumulative provisional ISR and annual progressive ISR; use the actual year, not an accrual election. | LISR arts. 100, 102–106, 109, 152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Existing or proposed RESICO | The prior-year qualifying income ceiling is **MXN 3,500,000**; new activity uses a supported estimate. A short prior operating period is annualised: receipts ÷ activity days × **365**. Test all exclusions and combined permitted income, not merely turnover. | LISR art. 113-E: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| RESICO plus salary or interest | Permitted only under art. 113-E's conditions, including the **combined** prior-year income ceiling. Annual salary/interest tax is determined independently; RESICO annual relief does not relieve a separate chapter's annual obligation. | LISR art. 113-E; RMF 2026 rule 3.13.8: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Shareholder/member or related party | The statutory exclusion applies without an invented percentage-of-sales test. RMF 3.13.9 has narrow exceptions described below; obtain the evidence and required clarification before applying one. | LISR arts. 90, 113-E; RMF 3.13.9: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| RESICO exclusion | Foreign resident with Mexican PE, preferential-regime income, or art. 94 III–VI assimilated salary income: do not place the person in individual RESICO. | LISR art. 113-E: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Unknown regime, inactive RFC, missing collections evidence or unresolved mismatch | Continue collecting facts, hold computation/submission, identify the correction. Never default to RESICO, AEP accrual accounting, a tax rate, a zero return, or an automatic split between spouses. | LISR arts. 102, 110, 113-E/G: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

**Shareholder exceptions:** RMF 3.13.9 covers members of Title III entities without distributable surplus, members of art. 79 XIII entities (including their interest), specified exclusively agricultural producer cooperatives that have not used the cited art. 74 exemption, and specified agricultural credit-union members who receive no income from the union. A clarification under **SOC_ACC_3.13.9.** with supporting documents is required. Its family relationship clarification is conditional on no commercial relationship or business influence producing an economic benefit. A spouse, related customer or small shareholding is not a blanket permission. [RMF 3.13.9](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

**Whole activity and other chapters:** the RESICO option applies to all the person's covered business/professional/rental activity. It cannot be selected just for the profitable invoices. RMF 3.13.3 excludes the described combination of platform-taxed activity and other business/professional/rental income from RESICO. Extraordinary income excluded from the ceiling is only that specifically identified by RMF 3.13.4, not every asset sale or every bank transfer. Retain its legal classification. [RMF 3.13.3–4](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

| Other income found at intake | Preserve and route |
|---|---|
| Employment only | Route to the salary annual-return rules; do not manufacture a freelance obligation. Obtain payroll CFDI/retentions and test the actual annual filing conditions. |
| Rent | Identify the rental chapter or valid whole-activity RESICO treatment, contracts, ownership and collection dates. Do not treat property deductions as personal deductions. |
| Interest | Obtain nominal/real interest and withholding records, not just net bank interest. Test its own annual conditions. |
| Dividends | Preserve the dividend and withholding certificate and the art. 140 tax-credit/gross-up analysis; do not add only the net deposit to freelance turnover. |
| Asset disposal/capital gains | Preserve cost, dates, notarial documents and withholding; refer the relevant chapter rather than assume gross sale proceeds are professional fees. |
| Platforms | Separate gross platform receipts, commission, ISR, IVA, direct customer receipts and election notices; follow the boundary below. |
| No other income | Record the negative confirmation; still reconcile bank deposits and cash. |

The separate income chapters and annual aggregation are in [LISR Title IV, arts. 90, 100, 113-A/B, 114, 119, 133–140, 150–152](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf). This intake does not calculate their special bases.

### 2. Validate RFC, credentials and CFDI [RMF 3.13.1–2, 3.13.5](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf)

If the person has no RFC, complete the appropriate SAT registration before filing; for RESICO the current RMF points to **Anexo 2 ficha 1/CFF**. On resumption, use **32/CFF**, and for activity/obligation changes **28/CFF**. Obtain the resulting updated Constancia and acuse, including effective dates. These current references supersede older SAT pages calling the update procedure 71/CFF. Do not assume every registration requires the same office appointment or that SAT ID is a filing credential. [RMF 3.13.1–2, 3.13.5](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

For an ordinary voluntary restart, SAT describes **Personas → Trámites del RFC → Actualización en el RFC → Presenta tu aviso de reanudación de actividades**, then authentication, completion and the saved acuse. Check the actual service shown to the taxpayer. [SAT restart service](https://wwwmat.sat.gob.mx/tramites/00354/presenta-tu-aviso-de-reanudacion-de-actividades-como-persona-fisica). For obligation updates, use SAT's **Aviso de actualización de actividades económicas y obligaciones**, enter the actual activities and dates, review, submit through the official service and save both the notice and acuse. Its general notice timing is within the following month; use the specific regime rule where it prescribes a different condition. [SAT procedure](https://www.sat.gob.mx/gobmx/Paginas/ficha_71_cff.html).

**Authority suspension is a different branch.** From the enacted fourth RMF amendment, a taxpayer can inspect **Consulta de contribuyentes suspendidos o cancelados por inactividad** under **Trámites y servicios → RFC, personas → Información adicional**. To dispute the authority's update, the taxpayer/representative attends an ADSC with evidence; SAT assists with the clarification labelled **SUSPENSION_RFC_POR_AUT** or **CANCELACION_RFC_POR_AUT**. The rule gives **10 business days** for resolution of that case, not guaranteed reactivation on demand. An incorrectly recorded shareholding can be raised through **PF O PM_NO SOCIO_ACCIONISTA** with formal ownership evidence. [RMF 2.5.20 and 2.5.25, effective 30 October 2026](https://dof.gob.mx/nota_detalle.php?codigo=5802597&fecha=30/10/2026).

Check whether authentication, e.firma and any invoicing certificate actually work, including expiry/restriction notices. For individual RESICO, RMF 2026 **Transitory Fifteenth** postpones the cited e.firma and active Buzón obligations under 3.13.32–33 to **1 January 2027**. This is a precisely scoped deferment; it does not erase other duties or supply whatever authentication the selected transaction requires. [RMF 2026 Transitory Fifteenth](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

For full, partial or missing invoicing, compare actual work/collections to XML and SAT status; distinguish a missing invoice from an unpaid invoice. CFDI 4.0 must identify the proper RFC, name, fiscal regime and postal code. SAT offers a free generation service, so hiring a PAC is not a universal prerequisite. For PPD, validate payment complements and PUE corrections against actual receipts; a missing complement does not postpone an income receipt that already occurred. Repair the documentary trail instead of deleting the receipt. [LISR arts. 102, 110 III, 113-E/G](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [SAT free CFDI 4.0 service](https://wwwmatnp.sat.gob.mx/aplicacion/75169/servicio-de-facturacion-cfdi-version-4.0-(vigente-a-partir-del-1-de-enero-de-2022)). Technical invoice corrections belong with [Mexico CFDI](mx-cfdi.md) and [e-invoicing](mexico-einvoice.md).

<a id="3-establish-actual-receipts-and-resico-compliance"></a>

### 3. Establish actual receipts and RESICO compliance [LISR arts. 102, 106, 113-E/J](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf)

Both ordinary AEP under art. 102 and individual RESICO use actual receipt rules for the activities covered here. Exclude IVA from the ISR base, include qualifying cash/advance/noncash receipts, and analyse debt satisfaction and cheque collection; the ordinary AEP export-of-goods rule has its own collection/long-stop provision. Do not total invoice subtotals and assume the result is taxable revenue. Reconcile net deposits back to gross fees and separately evidenced withholding/commissions.

The RESICO monthly table applies one rate to the **whole month's** qualifying receipts, without ISR deductions; it is not a progressive marginal tariff. The statutory top monthly band extends to the annual ceiling, not a ceiling obtained by dividing that annual ceiling by twelve. [LISR art. 113-E](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf).

| Monthly receipts excluding IVA, 2026 | Rate on all qualifying receipts in that month | Official source |
|---|---|---|
| Up to MXN 25,000.00 | 1.00% | LISR art. 113-E, tabla mensual: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 25,000.00 to 50,000.00 | 1.10% | LISR art. 113-E: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 50,000.00 to 83,333.33 | 1.50% | LISR art. 113-E: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 83,333.33 to 208,333.33 | 2.00% | LISR art. 113-E: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 208,333.33, up to MXN 3,500,000.00, subject to annual eligibility/exit | 2.50% | LISR art. 113-E: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

Mexican legal persons paying covered RESICO business/professional/rental receipts withhold **1.25% of the payment excluding IVA**, considered in the individual's monthly payment. Ordinary professional fees paid by legal persons instead engage the **10% ISR** withholding in art. 106; do not apply that percentage automatically to every sale of goods. Preserve the gross income and each credit separately. [LISR arts. 106, 113-J](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf).

RESICO monthly ISR is filed as **ISR simplificado de confianza. Personas físicas**; current RMF 3.13.7 makes those payments definitive and relieves the annual return **only for RESICO income**, preserving applicable PTU determination. The statutory annual table is in **art. 113-F**, not 113-E; it remains relevant only after checking whether a valid annual branch exists, including the optional coownership rules. The table and branch control are linked in [return assembly](mx-return-assembly.md#3-separate-the-resico-monthly-and-annual-branches). Do not generate an annual tax merely because that table exists. [RMF 3.13.7–8](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

Check every due month against filing and actual payment, including any lawful no-obligation period. For arrears, preserve both the original return and correction; a zero filing with actual taxable receipts requires correction, not a harmless “ceros” label. **Three or more omitted monthly payments in a calendar year, consecutive or not**, engage art. 113-I's exit rule; do not wait for more than three. Read it alongside current annual relief so a relieved RESICO annual return is not wrongly called an omission. Dates, notices and actual payment status decide the action. [LISR art. 113-I](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [RMF 3.13.5, 3.13.7](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

<a id="4-resolve-an-exit-or-rif-history"></a>

### 4. Resolve an exit or RIF history [LISR art. 113-E; RMF 3.13.5](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf)

Crossing the RESICO income ceiling triggers general-regime taxation from the **following month**. Update the obligations and select the actual RMF 3.13.5 branch:

- If the person complied with the RESICO section in the immediately preceding exercise, option I permits general provisional and annual treatment only for the remaining months, leaving earlier monthly payments definitive; it does not demand earlier complementary returns solely because of the exit.
- If prior RESICO payments are not treated as definitive, option II uses the relevant cumulative general regime, allowing the earlier RESICO payments to reduce the computation; reconcile rather than deduct or credit them twice.
- Separately test why the person left. Art. 113-E allows return after an income-ceiling exit where the immediately preceding year's income is within the ceiling and compliance is current; an obligations-default exit has a statutory no-return rule. Do not invent a single waiting period for both.

The SAT **2025 annual FAQ** still tells a 2025 excess-income filer to reconstruct January–December general payments. That instruction names the 2025 exercise. It cannot replace the enacted 2026 alternatives above. Save both the exercise and the basis for the selected route. [SAT FAQ, RESICO question 5](https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf).

Legacy **RIF is not automatically abolished for every existing taxpayer**. Check the preserved election/history and remaining entitlement under the transition rules with a RIF specialist. A RIF taxpayer who elects RESICO cannot return to RIF even if its legacy period was not exhausted (RMF 3.13.12). Do not force an otherwise eligible legacy RIF taxpayer to change simply to fit this Guide. [RMF 3.13.12; Transitories Sixteenth–Seventeenth](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

<a id="5-classify-iva-separately"></a>

### 5. Classify IVA separately [LIVA arts. 1, 2-A, 5, 5-D, 15](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf)

Never use an unknown IVA classification as a standard-rate default. Record the supply, where it is performed/used, customer status, dates and relief evidence. RESICO does not by itself exempt the activity from IVA.

| Activity/question | Intake treatment, subject to the stated facts | Official source |
|---|---|---|
| Ordinary domestic professional/software/technical services | Standard **16%** if taxable and no exemption, zero rating or substantiated stimulus applies. Software supplied abroad needs the export analysis, not an automatic domestic treatment. | LIVA arts. 1, 16, 29: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf |
| Food or patent medicines | Test the particular goods and exclusions under **0%** art. 2-A; not every item sold as food or medicine qualifies. Zero-rated and exempt activity have different input-credit consequences. | LIVA arts. 2-A, 5: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf |
| Medical services | Exemption only within art. 15 XIV's professional-title and provider conditions (and XV for the specified public bodies). Retain the practitioner's/provider's actual status. | LIVA art. 15 XIV–XV: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf |
| Education | Exemption for specified public providers or authorised/recognised private education and preschool under art. 15 IV; not all courses or online teaching. | LIVA art. 15 IV: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf |
| Border activity | Record location, establishment, supply and stimulus registration. Refer the operative decree/current eligibility review before claiming a reduced burden; proximity alone is insufficient. | General liability LIVA art. 1: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf; specific relief is held under Sources |
| Digital platforms | Separate a digital supplier from an intermediary collecting for the freelancer. A platform receipt does not itself prove full IVA withholding or a definitive election. | LIVA arts. 1-A BIS, 18-B, 18-J–M: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf |

For ordinary monthly taxable activity, reconcile output IVA actually collected, input IVA actually paid and legally creditable, and IVA withheld by customers. RESICO may still have creditable IVA under RMF 3.13.18 where the expenditure meets the prescribed ISR-deductibility test, even though RESICO ISR permits no expense deduction. The monthly form is **IVA simplificado de confianza** for that branch. [LIVA arts. 1-B, 5, 5-D](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf); [RMF 3.13.18–19](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf). Full supply/credit mechanics belong with [Mexico IVA](mexico-iva.md); do not reproduce an older Guide's incorrect universal withholding rule.

**DIOT:** RESICO taxpayers are relieved under RMF 3.13.17. AEP persons within RMF 2.8.1.17 are also relieved where prior total income did not exceed **MXN 4,000,000**, or starters estimate within that limit. Both rules relieve the stated electronic-accounting submission/DIOT obligations; they do not erase invoices, records or IVA payments. Otherwise determine the actual DIOT obligation. [RMF 2.8.1.17, 3.13.17](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

### 6. Separate marital ownership, platforms and social insurance

**Individual versus jointly owned income.** Record single, separation-of-property, community-property or unmarried status, but allocate income from the legal ownership and applicable election, not the label alone. Mexico's individual return is not a joint-spouse return. LISR art. 92 covers a common representative for coownership and applies those provisions to sociedad conyugal; art. 108 allocates jointly run business profit/loss and provisional credits proportionally. Own professional services must not simply be halved. For RESICO coownership, rule 3.13.20 tests both total coownership income and the individual's stated combined test; 3.13.21 permits a common representative with RFC notification, and 3.13.7 specifies proportional receipts/credits in the optional annual branch. No automatic equal split or duplicate CFDI. [LISR arts. 92, 108](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [RMF 3.13.7, 3.13.20–21](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

**Platforms:** LISR 113-B's definitive-ISR option uses the **MXN 300,000** prior-year platform-income limit (or supported starter estimate/short-period annualisation), permitted other salary/interest income, and an election notice within **30 days of first receipt**. The option has its own **five-year** restriction and loss-of-eligibility consequences. Do not substitute the RESICO limit or call all platform retention definitive. IVA's option is a separate LIVA 18-L/M test. Preserve direct collections and election evidence; refer the actual platform filing. [LISR arts. 113-A/B](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [LIVA arts. 18-L/M](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf); [RMF 3.13.3](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

**Insurance:** no coverage, private medical insurance, PTI independent-worker cover, Modalidad 40 and employer registration are different facts. None can be inferred from an ISR regime.

| Insurance fact | Verified rule / information to record | Official source |
|---|---|---|
| Modalidad 40 continuation | At least **52 weekly contributions in the last five years** before leaving mandatory insurance; exercise the right within **five years of leaving**. It covers the stated pension/invalidity branches, not general medical care. | LSS arts. 218–219: https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf; IMSS: https://www.imss.gob.mx/tramites/imss02007 |
| Modalidad 40 base/payment | Chosen salary at least the last registered salary and within **25 UMA**; monthly advance payments by the **17th of the current month** under the cited regulation. Obtain IMSS's actual quotation; do not apply a uniform old contribution percentage. | LSS art. 218: https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf; IMSS procedure quoting regulation arts. 65, 128: https://www.imss.gob.mx/tramites/imss02007 |
| Independent worker/PTI | Separate incorporation with its own actual occupation/income and IMSS calculation; advance payment can be monthly, bimonthly, semiannual or annual. Do not assign the Modalidad 40 base/rate to PTI. | IMSS PTI explanation: https://www.imss.gob.mx/prensa/archivo/202502/074 |
| UMA reference, effective **1 February 2026** | **MXN 117.31 daily; 3,566.22 monthly; 42,794.64 annually.** January and historical 2025 evidence need the applicable earlier values, not retrospective use of this announcement. | INEGI 2026 announcement: https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/uma/uma2026.pdf; historical series: https://www.inegi.org.mx/temas/uma/ |
| Has employees | Separate employer payroll, insurance and payment calendar; obtain scheme/component-specific assessments and receipts. Employer IMSS paid is an AEP deduction under art. 103 VI, subject to conditions. | LISR arts. 103 VI, 105: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Own voluntary IMSS/private insurance | Own IMSS payments are not automatically a retirement deduction under art. 151 V. Hold classification pending the actual scheme/legal basis. Qualifying private medical insurance has its separate art. 151 VI conditions and annual global cap; neither reduces RESICO ISR. | LISR arts. 113-E, 151 V–VI: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

## Boundary and exception table

| Finding | Decision and reason |
|---|---|
| RESICO label but receipts above the ceiling | Apply the dated exit branches; keep previous definitive months where the actual rule permits. |
| AEP with income below the RESICO ceiling | Eligibility alone does not change the recorded regime. Verify the valid election/obligation update and effective date. |
| Cash income not invoiced | Preserve the receipt as a fact, quantify the omission and correct CFDI/returns. Do not “solve” compliance by omitting the receipt. |
| Zero receipt month but active obligations | Check the return obligations; a nil amount and no filing obligation are different. |
| Rental/coownership/community property | Obtain legal shares and representative/election documents; hold allocation if unresolved. |
| Salary/interest alongside RESICO | Separate annual test and computation; the platform option's income limit is not a combined salary/RESICO rule. |
| Foreign customer or bank account | Residence/worldwide income remains relevant; export IVA and foreign tax credit need their own legal facts. |
| Staff or PTU | Preserve the employer workstream even when RESICO annual filing is relieved. |

## Worked cases

### Case 1 - documented domestic professional receipts in RESICO

Hypothetical 2026 Mexican-resident individual, valid RESICO, no exclusions or other income, prior qualifying receipts MXN 480,000. This month a Mexican corporate client pays fees **40,000**, IVA **6,400**, withholds ISR **500** and IVA **4,266.67** for qualifying independent personal services. The bank deposit is **41,633.33**. Bank cash is not gross fees. Monthly RESICO ISR is **440** (the whole 40,000 at 1.10%); after the separate 500 withholding there is **60 in the taxpayer's favour**, not a negative cash payment. Validate the form and refund route in assembly. IVA is a separate reconciliation and cannot be deducted from fees twice. Sources: LISR 113-E/J above; [LIVA 1-A](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf); [RLIVA 3 I](https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf).

```oa-check
name: Mexico intake RESICO gross-up and separate withholding
inputs:
  fees: 40000
  iva: 6400
  isr_retained: 500
  iva_retained: 4266.67
  monthly_rate: 0.011
steps:
  bank_deposit: fees + iva - isr_retained - iva_retained
  gross_isr: fees * monthly_rate
  balance: gross_isr - isr_retained
  payable: max(0, balance)
  favourable: max(0, 0 - balance)
expected:
  bank_deposit: 41633.33
  gross_isr: 440
  payable: 0
  favourable: 60
```

### Case 2 - short-period eligibility decision

Hypothetical applicant starts activity during 2025 and operates **100 days**, with **MXN 1,000,000 actual qualifying receipts** and no other income. For a proposed 2026 RESICO election, annualised receipts are **3,650,000**. Comparing only the raw million would wrongly admit the person; the annualised amount exceeds the **3,500,000** ceiling by **150,000**. Route to ordinary AEP, subject to the actual registration and other facts; no RESICO tax estimate is issued. [LISR art. 113-E, short-period rule](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf).

```oa-check
name: Mexico intake short-year RESICO eligibility decision
inputs:
  receipts: 1000000
  days: 100
  year_days: 365
  ceiling: 3500000
steps:
  annualised: receipts / days * year_days
  raw_headroom: ceiling - receipts
  annualised_excess: max(0, annualised - ceiling)
expected:
  annualised: 3650000
  raw_headroom: 2500000
  annualised_excess: 150000
```

## When to refuse or refer

Preserve the original refusal identifiers so an existing workflow can still route the file:

| Code | Hold/referral trigger | What can proceed |
|---|---|---|
| **R-MX-1** | Persona moral: the individual workflow cannot assemble an entity return. Title II and Title III entities need the appropriate actual regime; not all SC/AC entities automatically use Title II. | Preserve incorporation, accounts and tax history; corporate specialist. |
| **R-MX-2** | Maquiladora/IMMEX, customs or specialist transfer-pricing structure. | Record the actual transactions and refer; do not relabel them ordinary freelance services. |
| **R-MX-3** | Legacy RIF needs a verified transition/election history. | Check continued legacy entitlement; never force a change solely because this workflow does not calculate RIF. |
| **R-MX-4** | No usable RFC/registration, authority suspension or unresolved reactivation. | Gather evidence and complete the actual registration/clarification route. |
| **R-MX-5** | Nonresident/PE/treaty/complex foreign-source treatment. | Preserve residence, treaty, income, foreign tax and source facts; specialist before calculation. |
| **R-MX-6** | Zero declarations despite actual taxable receipts, missing CFDI or material payment discrepancies. | Reconcile and prepare corrections; hold filing a return known to contain the mismatch. |
| **R-MX-7** | Recorded regime/obligations and actual activity do not agree. | Resolve legal classification, effective date and notices; do not silently select a different form. |

Never invent a bank-deposit tolerance or SAT audit threshold. Document even a small unexplained discrepancy and classify its cause. Tax calculations and outputs are informational working material and require an appropriately qualified professional's review before filing or acting; no professional approval is claimed here.

## Filing and payment

| Obligation/calendar control | Deadline and operative condition | Official source |
|---|---|---|
| Ordinary AEP provisional ISR | **17th of following month**, cumulative computation for the relevant period. | LISR art. 106: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Individual RESICO monthly ISR | **17th of following month**; current RMF definitive-payment branch described above. | LISR art. 113-E; RMF 3.13.7: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Ordinary monthly IVA / RESICO monthly IVA | **17th of following month**, where the activity/obligation requires it; use the correct monthly form. | LIVA art. 5-D: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf; RMF 3.13.19: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| DIOT, only where not relieved | During the **following month** under RMF 4.5.1; document the relief test before adding this to the calendar. | RMF 2.8.1.17, 3.13.17, 4.5.1: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Individual annual ISR, where required | In **April following the calendar year** (normally by 30 April), subject to applicable non-business-day rules. **2026 income is the return due in April 2027**; do not promise future administrative facilities. | LISR art. 150: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf; CFF art. 12: https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf |
| PTU, if the individual is an obligated employer | Within **60 days after the annual tax payment due date**, subject to applicable employer/exemption rules; not a blanket 30 June date. | LFT arts. 122, 126–127: https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf |
| Historical corporate annual deadline | Separate entity job; the old corporate calendar row is a referral, not an individual deadline. | LISR Title II: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

For late tax, the applicable CFF update/recargos rules and current fine classifications are in [return assembly](mx-return-assembly.md#8-penalties-and-regularisation). Do not use “CCP plus 50%”. For any due date, check holidays/extensions for the actual filing period; the fourth RMF amendment identifies **2 and 3 April and 2 November 2026** as the stated SAT non-business days. [RMF 2.1.6 as amended](https://dof.gob.mx/nota_detalle.php?codigo=5802597&fecha=30/10/2026).

## Completion checklist

- [ ] Individual/residence/year confirmed; actual regime and every effective date evidenced.
- [ ] All eight legacy intake questions resolved: regime, RFC, revenue, CFDI, marital ownership, other income, provisional compliance, insurance.
- [ ] Receipts, cash, invoices, bank movements and withholding reconciled; outstanding corrections separately owned.
- [ ] RESICO ceiling/annualisation/exclusions and any exit branch documented; platform/RIF referrals retained.
- [ ] IVA classification and DIOT relief/obligation recorded without a guessed default.
- [ ] Employees, PTU, own insurance and employer IMSS separated; deductions sent to the correct annual branch.
- [ ] Client document checklist and open items handed to assembly; no unsupported figure or unresolved secret placed in the case record.

## Sources

Read on **2026-11-17** means the specified provisions were actually read, not merely downloaded. Native excerpts below identify the controlling propositions; this is a provision-level reading, not a claim that every page of each law was reviewed.

| Source / provisions actually read | Short native wording and application | Official URL | Read date |
|---|---|---|---|
| LISR, current text, last reform 1 April 2024: arts. 1, 92, 102–106, 108–110, 113-A/B, 113-E–J, 150–152 | “en el momento en que sean efectivamente percibidos”; art. 113-E: “a partir del mes siguiente”; actual monthly table, exclusions, representative and annual-base rules read. Official HTML mirror read alongside PDF. | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf; https://www.ordenjuridico.gob.mx/Documentos/Federal/html/wo25.html | 2026-11-17 |
| Enacted RMF 2026: 2.8.1.17; 3.13.1–9, 12, 17–21, 32–34; 4.5.1; Transitories XV–XVII | “será definitivo”; “únicamente por los ingresos que correspondan”; “a partir del 1o. de enero de 2027”. Eligibility, actual exit alternatives, annual relief, DIOT and credential conditions read. | https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf | 2026-11-17 |
| RMF fourth amendment, 30 October 2026: amendment list, 2.1.6, 2.5.20/25, 2.8.1.6 and commencement | “SUSPENSION_RFC_POR_AUT”; “PF O PM_NO SOCIO_ACCIONISTA”; “el día de su publicación”. Read for changed RFC/record duties; core 3.13 rules not amended by this act. | https://dof.gob.mx/nota_detalle.php?codigo=5802597&fecha=30/10/2026 | 2026-11-17 |
| CFF arts. 21, 22, 31, 73, 76, 81–84, current text last reform 9 April 2026 | “únicamente tendrá carácter informativo”; “no se prejuzgará”. Certificates are not a reconciliation or correctness assurance; penalties read for the assembly cross-reference. | https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | 2026-11-17 |
| LIVA arts. 1, 1-A/B, 5, 5-D, 15 IV/XIV/XV, 18-J–M, 32 VIII | “efectivamente pagado”; provider-specific exemptions, credit conditions and platform-option separation read. | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf | 2026-11-17 |
| SAT RFC update/restart and free invoicing services | “Acuse de movimientos de actualización”; “sin necesidad de contratar los servicios de un proveedor”. Read service descriptions; older ficha numbering is not substituted for current Anexo 2. | https://www.sat.gob.mx/gobmx/Paginas/ficha_71_cff.html; https://wwwmat.sat.gob.mx/tramites/00354/presenta-tu-aviso-de-reanudacion-de-actividades-como-persona-fisica; https://wwwmatnp.sat.gob.mx/aplicacion/75169/servicio-de-facturacion-cfdi-version-4.0-(vigente-a-partir-del-1-de-enero-de-2022) | 2026-11-17 |
| LSS arts. 218–220; IMSS continuation and PTI guidance | “cincuenta y dos cotizaciones”; “no genera el derecho a los servicios médicos”; “mensual, bimestral, semestral o anual”. | https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf; https://www.imss.gob.mx/tramites/imss02007; https://www.imss.gob.mx/prensa/archivo/202502/074 | 2026-11-17 |
| INEGI UMA 2026 announcement and historical series | “a partir del 1 de febrero de 2026”; daily, monthly, annual values read; historical 2025 values remain period-specific. | https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/uma/uma2026.pdf; https://www.inegi.org.mx/temas/uma/ | 2026-11-17 |
| LFT arts. 122, 126–127; current text last reform 14 May 2026 | “dentro de los sesenta días siguientes”; timing and neighbouring employer exceptions read. | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf | 2026-11-17 |
| SAT annual PF 2025 FAQ, RESICO questions 1–6 | “únicamente por los ingresos”; excess-income instructions name exercise 2025 and are not applied in place of the 2026 exit alternatives. | https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf | 2026-11-17 |
| RLIVA art. 3 I, current official text, last reform 25 September 2014 | “dos terceras partes”; case 1 uses the professional-services retention provision alongside current LIVA 1-A. | https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf | 2026-11-17 |

Not yet confirmed: current case-specific border ISR/IVA stimulus eligibility and procedures (the old flat reduced-ISR claim cannot be used); the applicable legal deduction for a person's own voluntary IMSS scheme and its component/year contribution calculation; a supposed universal January clients-and-suppliers declaration/amount; any universal equal-spouse allocation or separate-CFDI mandate; authenticated portal screens or administrative facilities for the 2026 annual return to be filed in 2027. These are **non-usable holds**, not implied exemptions or permissions. Unsupported old rules about mandatory PAC use, AEP accrual elections, the RESICO monthly ceiling derived by dividing by twelve, and universal platform finality are corrected above rather than retained as options.
