---
name: mx-return-assembly
description: "Use this skill when assembling or reviewing a Mexican persona física annual tax return (declaración anual). Trigger on phrases like \"declaración anual México\", \"ISR anual\", \"return assembly Mexico\", \"cross-check CFDI\", \"IVA reconciliation\", \"provisional vs annual\", \"RESICO annual\", \"AEP annual return\", or any task involving the compilation, verification, or filing of a Mexican individual's annual income tax return. This skill orchestrates cross-checks between ISR, IVA, IMSS, and CFDI data. ALWAYS read this skill before assembling any Mexican annual return."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mx-return-assembly"
  jurisdiction: "MX"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Mexico return assembly

## Scope

Build and reconcile the annual ISR working papers for a Mexican-resident **persona física** with ordinary business/professional income (AEP), or establish why individual RESICO income has definitive monthly treatment instead. Start with [Mexico freelance intake](mx-freelance-intake.md); carry forward its actual regime dates, residence, receipts, other chapters, IVA position, workers, insurance and unresolved corrections. SAT is the filing authority; amounts are MXN and the income period is the calendar year.

**Quick reference:** this Guide covers the enacted **2026 income calculation and monthly-to-annual controls**. Ordinary individual annual ISR is declared in April of the following year (LISR art. 150). For **2026 income that means April 2027**; final 2027 portal screens, refund facilities and instalment rules must be checked when published. The enacted Anexo 8 already supplies a distinct **2026 annual tariff**. SAT's currently published annual application FAQ is explicitly for **2025 income filed in 2026**; its instructions below remain useful for a late/corrective 2025 return and are not presented as a published 2026-income application.

Do not file a RESICO annual return simply because a statutory annual table exists. First resolve the definitive-monthly branch under RMF 3.13.7, any optional coownership branch, an exit, and independent annual obligations for salary/interest. A workpaper is not a submitted return, a CFDI subtotal is not necessarily income, and an acuse is not proof of bank payment.

This workflow assembles the individual's file. Specialist corporate, RIF, maquiladora/IMMEX, platform, nonresident/PE, treaty, complex gains and incentive filings remain identified referrals. No professional approval of this version is asserted. Outputs require a suitably qualified professional's review before filing or acting.

## Ask the client first

Resolve these six groups from the existing record before requesting missing evidence:

1. **Year, residence and regime by date:** the exercise, initial/corrective return, start/suspension dates, Constancia and every regime-change acuse; why RESICO continued or ended.
2. **Actual income:** all issued XML, cash and bank records, collections, PUE/PPD complements, cancelled/replaced invoices, debt satisfaction/advances, withholding, foreign receipts and other income chapters.
3. **Business deductions:** received XML, actual payments, inventories/purchases, operating expenses, business-use proportions, investments and dates first used, business insurance, employees, employer IMSS, local business-income taxes, PTU paid and prior losses.
4. **Tax and information already filed:** every due monthly ISR/IVA return and correction, acuses plus bank receipts, ISR and IVA retained, DIOT relief or submissions, outstanding debts/instalments, requests/notices and prior annual return.
5. **Personal and ownership facts:** legal coownership/community-property shares and representative, personal deduction CFDI/payment evidence, family eligibility, home-loan certificate, qualifying retirement plan, own IMSS scheme and private insurance.
6. **Submission/result:** taxpayer's working official authentication, own active bank CLABE, existing refund/FED status, intended refund/compensation election and actual payment capacity. Taxpayer enters passwords/private keys in SAT; retain no secret in the workpapers.

## The method, step by step

### 1. Gather a complete period and control every document

Download issued and received CFDI XML, including payment, withholding and payroll documents, status and cancellation/replacement relationships. Gather all account statements and cash records, provisional/definitive returns, complementary-return history, acuses, bank payment receipts, client/employer/bank/platform withholding certificates, IMSS assessments/receipts, asset register, prior return/loss schedule and personal-deduction evidence. Record which months were actually subject to an obligation; a partial trading year does not automatically have a full year's identical return requirements. These documents support the obligations in [LISR arts. 103–110, 113-G, 151](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf).

Build a monthly control file with: period; regime/effective date; gross receipts excluding IVA; output IVA; business deductions; ISR withheld; actual ISR paid; input IVA eligible for credit; IVA withheld by clients; IVA due/favourable; original and latest return folios; payment date/reference; DIOT obligation or relief; discrepancy and corrective action. Preserve the original submission when a complementaria replaces its tax outcome. Do not add all versions as if they were separate tax payments.

### 2. Reconcile revenue, expenses and the actual base [LISR arts. 102–106](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf)

| Phase/control | Required analysis | Official source |
|---|---|---|
| Issued CFDI and bank/cash receipts | Link invoices, gross collections, withholding, commissions, advances and cash/noncash receipts. Explain loans, transfers between own accounts and other non-fee deposits; do not presume all deposits taxable or use a percentage tolerance. | LISR arts. 90, 102, 113-E: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| PUE/PPD and payment complements | Test actual payment date and amount. Correct missing/misclassified CFDI evidence; absence of a complement does not make an actually received payment disappear. | LISR arts. 102, 113-E/G: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Cancelled/replaced invoice | Identify the underlying transaction, replacement, receipt and any actual refund. Avoid duplicate billing/income; cancellation alone does not exclude money retained for completed taxable work. | LISR arts. 102, 103 I, 113-E/G: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Ordinary AEP income timing | **Actual receipt**, not a general accrual basis or an invented CFF election. Include qualifying advances, goods/services and satisfaction of the creditor; cheque rules use collection/qualifying transfer. Exported goods have the specific twelve-month long stop in art. 102. | LISR art. 102: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| AEP expense categories | Authorised purchases, expenses, investments, business interest, employer IMSS and local business/professional-income tax, subject to the actual category's rules. Inventory purchases are not automatically a corporate cost-of-sales computation. | LISR arts. 103–105: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| General deduction requirements | Indispensability, actual payment where required, valid CFDI, correct timing, only once, accounting and relevant withholding/other statutory conditions. Art. 105 incorporates the specified art. 27 clauses; do not cite corporate art. 27 alone as the entire individual rule. | LISR art. 105: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Banking condition | Payments **exceeding MXN 2,000** use the specified taxpayer-account transfer, named cheque, card or authorised electronic wallet; fuel uses those methods **regardless of amount**, with the stated permit evidence. Check an applicable official rural exception rather than invent one. | LISR arts. 105 final paragraph, 27 III: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Investment and timing | Separate assets from operating expenses. Apply art. 104 and the referenced investment rules, business use, first-use year and applicable rate; the ordinary actual-payment rule has a specific investment exception. Do not expense the entire paid asset automatically. | LISR arts. 104, 105 I/III/VI: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Mixed use, insurance, payroll and local taxes | Support the business share and each relevant condition. Business insurance and employee pay/IMSS are separate from personal insurance and own voluntary contributions. | LISR arts. 103, 105, 27 V, 151 VI: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

Missing evidence creates an unresolved item to correct or exclude from the claimed deduction, not authority to reduce income by an unsupported estimate. **RESICO has no ISR expense deduction**, but preserve its received CFDI because IVA credit and documentary obligations remain separate. Do not treat all IVA shown on received XML as automatically creditable.

<a id="3-separate-the-resico-monthly-and-annual-branches"></a>

### 3. Separate the RESICO monthly and annual branches [RMF 3.13.5, 3.13.7–8](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf)

1. Apply the [intake monthly table and eligibility/withholding rules](mx-freelance-intake.md#3-establish-actual-receipts-and-resico-compliance). Reconcile each month's actual receipts, selected whole-base rate, legal-person ISR retention, definitive payment, and any favourable balance. Monthly payments made under current RMF 3.13.7 are definitive and the annual relief is **only for RESICO income**; applicable PTU determination remains.
2. Determine salary/interest annual obligations and tax **independently** under 3.13.8. Do not use a platform threshold to aggregate salary with RESICO, or apply personal deductions against definitive RESICO receipts.
3. For an exit, preserve the date and apply [intake's two actual 2026 exit branches](mx-freelance-intake.md#4-resolve-an-exit-or-rif-history). Option I of 3.13.5, where its prior-year compliance condition is satisfied, leaves the earlier RESICO months definitive and uses general treatment for remaining months. Option II instead reconstructs the cumulative general computation and recognises earlier payments once. Do not impose full-year recomputation on every 2026 exit.
4. If a documented **optional coownership annual branch** under 3.13.7 and 3.13.20–21 applies, obtain the legal shares and representative's income/payment records. Apply the proportionate receipts and credits specified by the rule. Other claimed exceptional annual branches require their actual legal basis before use.

The statutory annual computation remains **LISR art. 113-F**, not art. 113-E. Its table is retained as a conditional legal reference, not an instruction to override current annual relief:

| Qualifying annual cash receipts excluding IVA | Statutory rate on the entire eligible base; no ISR deductions | Official source |
|---|---|---|
| Up to MXN 300,000 | 1.00% | LISR art. 113-F, subject to RMF annual branch: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 300,000 to 600,000 | 1.10% | LISR art. 113-F: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 600,000 to 1,000,000 | 1.50% | LISR art. 113-F: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 1,000,000 to 2,500,000 | 2.00% | LISR art. 113-F: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Above MXN 2,500,000 to 3,500,000 | 2.50% | LISR art. 113-F: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

Conditional annual workpaper: **A** = qualifying actual receipts supported by CFDI excluding IVA, allocated to the person; **B** = valid annual table rate; **C** = A × B; **D** = eligible monthly ISR **actually paid** for that same annual branch/share; **E** = separately evidenced ISR withheld for that branch/share; **F** = C − D − E. First document why the annual calculation is permitted/required and reconcile every credit to avoid double counting. Do not aggregate gross monthly liabilities, monthly bank payments and already-used retentions as three separate credits. [LISR art. 113-F](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [RMF 3.13.7](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

Monthly RESICO favourable balances have their own FED route under **3.13.34**: request in the following month or request the **total** of the exercise's favourable balances together from **17 January of the following year**, using FED and the supporting documentation in **Anexo 2 ficha 70/CFF**. This is not the annual automatic refund facility. [RMF 3.13.34](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

### 4. Assemble the ordinary annual ISR workpaper [LISR arts. 109, 150–152](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf)

Use the tariff for the income year. The complete tables have one pack home: [2026 annual brackets](mx-income-tax.md#isr-annual-brackets-2026-personas-físicas-régimen-general) and [historical 2025 annual brackets](mx-income-tax.md#isr-annual-brackets-2025-personas-físicas-régimen-general). The native **Anexo 8 C I explicitly covers 2025**, and **C II explicitly covers 2026**; each has eleven bands. Check the precise limits and fixed quotas there, not a 2025 table relabelled as 2026. Apply fixed quota + (taxable base − the band's lower limit) × that band's excess rate; for no positive base, do not create negative tax. [RMF 3.17.1 and Anexo 8 C I–II](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf).

| Workpaper field retained from the assembly engine | Correct input/calculation | Official source |
|---|---|---|
| **A1**, AEP income | Actual business/professional receipts including taxable non-invoice adjustments, excluding IVA. | LISR arts. 101–102: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **A2**, other chapters | Keep separate schedules for salary, rent, gains, interest, dividends and other reportable income. Only the correctly determined amounts that art. 152 aggregates enter the progressive annual calculation; exclude exempt/definitive income from its taxable base and preserve disclosure duties. | LISR arts. 150–152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **A3**, income reconciliation | Reconcile A1 plus the other-chapter schedules to declared and disclosed income; this is a control total, not a substitute for the chapter-specific base. | LISR arts. 109, 150–152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **B1**, purchases; **B2**, operating expenses | Authorised paid purchases/expenses with evidence; classify returns/discounts correctly. Do not deduct both purchases and cost of sales for the same goods. | LISR arts. 103, 105: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **B3**, investments; **B4**, business insurance | Investment deduction by its actual rules; business premiums only where authorised/indispensable. Personal medical premiums go in F instead. | LISR arts. 104–105, 151 VI: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **B5**, employees; **B6**, employer IMSS | Qualifying salary/payroll costs and employer contributions actually paid, with relevant CFDI, withholding and employment records. Own insurance is not B6 by default. | LISR arts. 103 VI, 105, 27 V: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **B7**, total business deductions | Sum the validated B items and any other specifically authorised business deductions once, with a reconciliation to the ledger. | LISR arts. 103–105: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **C**, AEP fiscal profit/loss | A1 − B7. Maintain a separate PTU-paid adjustment, because art. 109 then reduces fiscal profit by qualifying PTU and prior losses. | LISR art. 109: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **D**, previous AEP losses | Valid pending loss, indexed for the statutory periods, within the following **ten exercises**; only against the same section's profit and only to the usable amount. Loss unused when it could have been used is forfeited to that extent. | LISR art. 109: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **E**, aggregate taxable income before personal deductions | Non-negative eligible AEP profit after qualifying PTU/D, plus the properly determined aggregable A2 chapters. A business loss does not automatically reduce salary, and definitive RESICO receipts do not enter this base. | LISR arts. 109, 152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **F**, personal deductions; **G**, tariff base | Valid art. 151 deductions subject to their individual and global rules; G = max(0, E − F). They do not create a general carry-forward loss. | LISR arts. 151–152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **H**, annual ISR | Apply the **correct exercise's** annual progressive tariff to G. | LISR art. 152; RMF 2026 Anexo 8 C: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf |
| **I**, separately supported other credits | No general AEP “subsidio para el empleo” credit. If salary/subsidy, foreign tax, dividend credit or an incentive is involved, use a separate legally supported schedule and actual eligibility; no guessed credit. | LISR art. 152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| **J**, provisional ISR; **K**, retentions | Credit actual eligible tax paid and independently evidenced withholding once. Check whether an amount already formed part of J; the acuse alone does not prove payment. | LISR arts. 106, 152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf; SAT FAQ I A6/C.3: https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf |
| **L**, outcome | H − I − J − K = net outcome; show payable and favourable balance separately. A favourable balance is not a guaranteed automatic refund. | LISR art. 152: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

For losses: retain the year originated, original loss, PTU component, available amount, each indexation period/factor, amount usable/used each year and remaining life. RESICO's no-deductions method does not generate an ordinary AEP fiscal loss or allow a historic AEP loss to reduce current definitive RESICO receipts. The SAT 2025 FAQ's historic transition references do not create a new 2026 loss election. [LISR arts. 109, 113-E](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [SAT FAQ RESICO questions 4 and 8](https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf).

### 5. Validate personal deductions and insurance [LISR art. 151](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf)

These deductions apply to the eligible individual's annual progressive-tax calculation; they do not reduce definitive RESICO ISR. A prefilled invoice is a candidate, not proof. Require the proper CFDI, actual eligible payment, correct beneficiary and any certificate. Do not duplicate a business deduction.

For medical and funeral deductions under art. 151 I–II, the fiscal evidence must establish amounts actually paid during the calendar year to institutions or persons resident in Mexico. Record any recovered or reimbursed amount and deduct only the unrecovered difference. Carry these tests into the medical and funeral validation below before including either amount in F. [LISR art. 151, common paragraph for I–II](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf).

| Personal deduction | Conditions and cap | Official source |
|---|---|---|
| Medical/dental, qualifying psychology/nutrition and hospital costs | Proper professional title/provider, eligible taxpayer/spouse/cohabiting partner/direct ascendant or descendant; qualifying family-income condition; specified taxpayer-account cheque, transfer or card payment. Ordinary costs are subject to the global cap. | LISR art. 151 I: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Certified incapacity/disability medical costs | Specific certified qualifying costs, specified CFDI and evidence; the relevant partial incapacity/disability test is at least **50%**. The qualifying statutory exception is outside the global cap; this does not exempt all medical spending. | LISR art. 151 I, additional paragraphs: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Funeral costs | Actual qualifying family costs, within the **annual UMA** ceiling, with fiscal proof; apply the relevant year's value and global rules. | LISR art. 151 II and final paragraphs: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf; INEGI: https://www.inegi.org.mx/temas/uma/ |
| Non-onerous/non-remunerative qualifying donations | Authorised beneficiary/legal category and proof; at most **7%** of prior-year qualifying accumulated income before personal deductions; government sub-limit **4%**, within the same combined ceiling. Donations **also enter the global cap** under the current final paragraph. A payment to any trust is not automatically eligible. | LISR art. 151 III and final paragraph: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Home mortgage interest | **Real interest actually paid**, not loan principal or all nominal interest; own-home loan through the specified financial institutions, total qualifying credits not above **750,000 UDI**; retain lender's certificate. | LISR art. 151 IV: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Qualified retirement contributions | Art. 151 V scheme and permanence conditions; up to **10%** of current accumulated income and not above **five annual UMA**. This category is outside the global cap but retains its own limits; not every Afore/IMSS payment qualifies. | LISR art. 151 V and final paragraph: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Private medical insurance premiums | Eligible policy/beneficiaries under art. 151 VI, including complementary/independent cover; global cap still applies. | LISR art. 151 VI: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| School transport | Required by local law or included for **all pupils** in tuition; transport separately stated on the CFDI and specified bank/card payment; global cap. No automatic per-child deduction for optional transport. | LISR art. 151 VII: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Local tax | Personal provision is for qualifying **salary-income local tax at a rate not above 5%**, not general property predial. Business/rental predial requires that separate chapter's legal and business-use analysis. | LISR art. 151 VIII: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |
| Global cap | Lesser of **15% of total income, including exempt income**, and **five annual UMA**. Art. 151 V retirement is excluded; the specifically certified medical exception is separately provided in I. Donations are included. | LISR art. 151 final paragraph: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf |

Use INEGI's applicable annual UMA from [the period-specific reference](mx-freelance-intake.md#6-separate-marital-ownership-platforms-and-social-insurance). For 2026 the published annual value times five is the UMA side of the cap; calculate the lesser-of test for the actual taxpayer. The **2025** FAQ prints **206,367.36** for five UMA, whereas INEGI's published **2025 annual 41,273.52 × 5 = 206,367.60**. The difference is **0.24**: retain the official annual-value arithmetic in the historical workpaper and investigate any portal discrepancy; do not silently substitute the FAQ scalar or apply either 2025 amount to 2026. [INEGI historical series](https://www.inegi.org.mx/temas/uma/); [SAT FAQ I D3](https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf).

**IMSS control:** distinguish own Modalidad 40, PTI, private insurance and employer contributions. Match the actual contract/assessment, base, occupation/branch, payment frequency and covered period; a universal count of twelve monthly or six bimonthly receipts is not a complete test. Modalidad 40 is paid monthly in advance, PTI permits its stated frequency choices, and employer components have their own schedules. Employer IMSS belongs in the valid AEP business deduction under 103 VI. A person's own voluntary IMSS payment is **not automatically art. 151 V retirement saving**; hold the claimed deduction until its exact legal classification is established. [LISR arts. 103 VI, 151 V–VI](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [IMSS continuation](https://www.imss.gob.mx/tramites/imss02007); [IMSS PTI guidance](https://www.imss.gob.mx/prensa/archivo/202502/074).

### 6. Reconcile IVA month by month [LIVA arts. 1-B, 5, 5-D](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf)

Use the actual supply classification established at intake, not a blanket percentage of annual ISR revenue. For each calendar month, reconcile output IVA on actual taxable collections, separately stated input IVA actually paid and legally creditable, client withholdings, applicable adjustments and balance/payment. Then compare the latest operative return with proof of payment. The sum of the months is an **annual control schedule**, not a new annual IVA tax. Do not net an annual surplus against another period without its lawful credit/refund treatment.

Input credit requires the art. 5 conditions: qualifying business use/taxable or zero-rated activity, valid separate tax/CFDI or import evidence, actual payment, retained-tax payment/timing where relevant and mixed-use allocation. Exempt and non-object activity can restrict the credit; capital assets have specific adjustment rules. RESICO ISR's lack of deductions does not prohibit every IVA credit: current rule 3.13.18 provides its stated deductibility test. [LIVA art. 5](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf); [RMF 3.13.18](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

| Withholding situation | Amount and condition to reconcile | Official source |
|---|---|---|
| Legal person receives independent personal services, commission services or temporary use of goods from an individual | **Two thirds of IVA transferred and actually paid** within RLIVA art. 3 I; not all goods sales or all individual-to-company payments. Keep ISR withholding separate. | LIVA 1-A II; RLIVA 3 I: https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf |
| Intermediary collects for an individual on covered platforms | **50% of IVA collected** under 18-J II a); **100%** where the individual has not provided the RFC required there. Other 100% cases have their own defined nonresident digital-service facts. | LIVA art. 18-J II a): https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf |
| Government payer | Identify the particular entity, transaction and governing LIVA art. 3/RLIVA provision. Do not automatically apply a universal full withholding. | LIVA art. 3: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf; RLIVA art. 4: https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf |
| Definitive platform IVA option | Separately test LIVA 18-L/M, including the qualifying income/activity and election conditions. Do not assume ISR or RESICO status makes the IVA final. | LIVA arts. 18-L/M: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf |

Test DIOT relief before seeking missing reports: RESICO rule 3.13.17; qualifying AEP rule 2.8.1.17 (the [intake threshold and conditions](mx-freelance-intake.md#5-classify-iva-separately)). Where DIOT remains due, reconcile the actual report to eligible supplier transactions; RMF 4.5.1 provides the following-month period. There is no verified universal August 2025 date that makes every individual file twelve DIOTs. [RMF 2.8.1.17, 3.13.17, 4.5.1](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

### 7. Apply the reconciliation matrix and evidence controls

| Control | Compare | Required resolution |
|---|---|---|
| Revenue integrity | Issued CFDI, actual bank/cash/noncash collections, gross-up of retentions and fees | Explain every difference by timing, tax, transfer/loan, cancellation/replacement or missing transaction. No general percentage safe harbour. |
| Expense backing | Authorised deduction schedule versus XML, payment, business purpose, asset/payroll records | Exclude or cure unsupported claims; do not confuse cost, payment and the year's deduction. |
| IVA | Each month's legally derived output/input/retention versus latest filed return/payment | Correct the actual period and retain the trail; annual addition is only a control. |
| Provisional ISR | Due periods, original/complementary acuses, bank payments and SAT preload | Credit the amount actually paid once; identify any duplicate, failed payment or correction. |
| Retentions | Gross invoice, client/employer/bank/platform certificates and SAT preloads | Correct missing/incorrect documents or source returns and substantiate the claimed credit. |
| IMSS | Actual scheme/assessment/period and receipts versus claimed deduction | Employer and own payments separately classified; no blanket personal deduction. |
| DIOT | Obligation or relief record; submitted transactions versus supplier/IVA schedule | Resolve differences if due; document lawful non-filing where relieved. |
| Prior years | Prior return, loss roll-forward, debt and refund history versus current workpapers | Explain regime changes, loss use and duplicate credits/refunds. |

Retain the old risk topics as **documentary review prompts**, without invented SAT probabilities or thresholds: unexplained bank deposits; unusually large refunds; bank activity without invoice records; generic RFC or customer-identification problems; zero provisional filings despite receipts; unusually high business deductions; personal claims at the legal cap; and a substantial year-on-year revenue decline. None by itself proves wrongdoing or creates a statutory audit trigger. Do not apply the old percentage tolerances or supposed fixed generic-RFC threshold.

<a id="8-penalties-and-regularisation"></a>

### 8. Penalties and regularisation [CFF arts. 21, 73, 76, 81–84](https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf)

Determine the actual omission, year, taxpayer category, voluntary/required correction and any notification before quoting a fine. Do not add every listed range together. Spontaneous compliance can avoid fines under art. 73's conditions; tax, updating and late-payment charges still need their own analysis. Notification/discovery can switch off spontaneity.

| 2026 item | Verified amount/rule and its scope | Official source |
|---|---|---|
| Missing declaration, art. 82 I a) | **MXN 2,050–25,360 per undeclared obligation**, with the clause's additional-return condition. Apply only after art. 81 classification and any art. 73 relief. | CFF art. 82 I a); Anexo 5 A: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-5-RMF-2026_DOF-28122025.pdf |
| Failure/late response to a filing requirement, art. 82 I b) | **MXN 2,050–50,710 per affected obligation** under this clause; different electronic-filing breaches have their own clause. Not a universal per-requerimiento annual fine. | CFF art. 82 I b); Anexo 5 A: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-5-RMF-2026_DOF-28122025.pdf |
| Omitted tax discovered using authority examination powers | **55%–75% of omitted contributions** under art. 76's first paragraph; correction-stage reductions and other provisions can change the result. | CFF art. 76: https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf |
| CFDI breach classified under art. 83 VII / 84 IV | General clause a) **MXN 22,300–127,530**; clause b) for Title IV Chapter II Sections II/IV (including individual RESICO) **MXN 1,910–3,800**. Repetition may bring closure. Do not call the general range a fine per every invoice or ignore the RESICO clause. | CFF art. 84 IV a)–b), current text: https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf; general indexed amount Anexo 5 A: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-5-RMF-2026_DOF-28122025.pdf |
| DIOT breach, only if the person actually had the duty | Art. 81 XXVI / 82 XXVI: **MXN 14,880–29,750**; the stated repeated-breach increase is **100% for each new noncompliance**. Relief must be checked first. | CFF arts. 81–82 XXVI; Anexo 5 B: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-5-RMF-2026_DOF-28122025.pdf |
| Overdue 2026 tax | Update under CFF 17-A/21 and apply recargos for each **month or fraction** on updated principal. LIF 2026 art. 11 I is **1.38% monthly** for extension; CFF 21's **50% increase** gives **2.07% monthly mora (derived)** for 2026. Use each year's rate for a cross-year debt. | CFF art. 21: https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf; LIF 2026 art. 11: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIF_2026.pdf |
| False/inexistent invoices or simulated operations | Preserve facts and refer immediately. CFF 69-B/49 Bis procedures, deduction/credit consequences, art. 83/84 and criminal provisions are not one interchangeable percentage penalty. | CFF current text: https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf; case-specific procedure/penalty held under Sources |

Do not use CCP as the interest base. Recompute updating/charges for the actual due and payment dates and any applicable statutory exceptions. Obtain the official payment calculation/capture line and reconcile it; a voluntary payment arrangement is not the special annual-return instalment facility below.

## Boundary and exception table

| Boundary | Assembly action |
|---|---|
| RESICO stayed valid throughout 2026 | Reconcile definitive monthly payments; record the annual relief rather than invent an annual progressive or flat-rate top-up. |
| 2026 RESICO exit | Identify the trigger/effective month and the actual 3.13.5 option; preserve earlier definitive periods when permitted. |
| Late/corrective 2025 excess-income RESICO file | Use the 2025 legal/administrative route and dated SAT FAQ, not the new 2026 option retroactively. |
| Salary, interest, rent or dividends alongside AEP | Chapter-specific schedules and credits, then the actual art. 152 aggregation. No universal addition of every net deposit. |
| Salary/interest alongside RESICO | Independent annual determination; relief for RESICO does not settle the other chapter. |
| Coownership/sociedad conyugal | Legal share/representative/election evidence, proportional taxable amounts and credits. No automatic equal split or joint return. |
| AEP loss | Apply only as permitted by art. 109, with dated indexing and remaining life; no deduction against definitive RESICO. |
| Research/development, film/theatre or border incentive | Preserve the original requested topic and refer before claiming a credit. Art. 202 is an incremental-base/authorised-project regime, not a credit on all spending; arts. 189–190 have their own approved-project/cap rules. RESICO art. 113-I restricts combining incentive treatments. Current implementation/authorisation and border eligibility are non-usable holds here. |
| Donation/trust contribution | Test the actual art. 151 III beneficiary and individual/global caps. A “trust” description alone supplies no deduction. |
| Foreign customer/account/tax | Preserve worldwide-income/residence, collection, export-IVA facts and foreign tax certificate; obtain the treaty/credit analysis before finalising that component. |

## Worked cases

### Case 1 - ordinary 2026 AEP annual workpaper

Hypothetical resident individual, valid ordinary AEP throughout 2026, no other income, employees, PTU or previous losses. Actual business receipts excluding IVA are **MXN 500,000**. Valid deductions are paid purchases/expenses **170,000** plus an independently substantiated investment deduction **30,000**. Valid ordinary personal deductions **20,000** are below both sides of the art. 151 global cap; there are no donations or special exceptions. Base: **280,000**. Anexo 8 C II places it in the band starting **210,403.70**, fixed quota **22,282.14**, excess rate **21.36%**. ISR = **37,147.91** before separately evidenced actual provisional payments **20,000** and withholdings **10,000**. Balance **7,147.91 payable**. These assumed credits are distinct, not gross tax plus its own credit repeated. [LISR arts. 109, 151–152](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [Anexo 8 C II](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf). This is a 2026 statutory workpaper, not a claim that its 2027 portal is open.

```oa-check
name: Mexico assembly 2026 AEP annual computation
inputs:
  receipts: 500000
  paid_expenses: 170000
  investment_deduction: 30000
  personal_deductions: 20000
  lower: 210403.70
  quota: 22282.14
  rate: 0.2136
  actual_provisionals: 20000
  distinct_withholding: 10000
steps:
  fiscal_profit: receipts - paid_expenses - investment_deduction
  base: fiscal_profit - personal_deductions
  gross_isr: quota + (base - lower) * rate
  balance: gross_isr - actual_provisionals - distinct_withholding
expected:
  fiscal_profit: 300000
  base: 280000
  gross_isr: 37147.91
  balance: 7147.91
```

### Case 2 - deciding whether a RESICO annual calculation belongs in the file

Hypothetical resident individual validly in RESICO throughout 2026, no other income, coownership, employees or exit; twelve equal months of qualifying receipts **MXN 100,000**, no deductions and no withholding. Each month uses **2%**, giving **2,000**, and the **24,000** paid for the year is definitive under RMF 3.13.7. The mathematical statutory annual-table calculation would be **1,200,000 × 2% = 24,000**, but its arithmetic equality does **not** create an annual filing obligation. Choose the definitive-monthly reconciliation branch and document relief. If salary/interest or a real optional annual branch existed, reopen that precise branch; do not infer it from the table. [LISR arts. 113-E/F](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [RMF 3.13.7–8](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

```oa-check
name: Mexico assembly RESICO monthly versus conditional annual decision
inputs:
  monthly_receipts: 100000
  months: 12
  monthly_rate: 0.02
  conditional_annual_rate: 0.02
steps:
  annual_receipts: monthly_receipts * months
  monthly_isr: monthly_receipts * monthly_rate
  definitive_paid: monthly_isr * months
  hypothetical_annual: annual_receipts * conditional_annual_rate
  arithmetic_difference: hypothetical_annual - definitive_paid
expected:
  annual_receipts: 1200000
  monthly_isr: 2000
  definitive_paid: 24000
  hypothetical_annual: 24000
  arithmetic_difference: 0
```

## When to refuse or refer

Carry forward intake's **R-MX-1–7**: entity, maquiladora/IMMEX, unresolved RIF, no usable RFC, nonresident/PE or complex international work, zero returns despite receipts, and mismatched obligations. Also hold submission where a material receipt/deduction/credit remains unsubstantiated, a legal ownership allocation is unknown, a taxpayer cannot authenticate, or the chosen year's operative form/procedure has not been confirmed. Continue the reconciliation and assemble a precise missing-evidence list; do not disguise the gap with a different year or return type.

Do not sign a taxpayer declaration for the person or assert their personal facts. Record the taxpayer/professional's approval of final figures and submission as an actual human action. This Guide gives no authority to invent approval or credentialed attestation.

## Filing and payment

### Filing sequence and period controls [LISR art. 150; SAT annual PF 2025 FAQ](https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf)

For the **2026 income year**, finish the working papers now and confirm the published 2027 annual service, forms, rule changes and deadlines before submission. The statutory annual period is April following the year; apply CFF art. 12's actual non-business-day and bank-payment rules rather than extrapolating an unverified capture-line expiry. No future instalment or automatic-refund facility is promised here. [LISR art. 150](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf); [CFF art. 12](https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf).

For a **2025 income return filed/corrected in 2026**, SAT's 2025 FAQ supplies the following ordered steps:

1. Open the official SAT **Declaración Anual de personas físicas** service through **Trámites y servicios → Declaraciones para personas** and choose the annual service. Authenticate using RFC/Contraseña and the service challenge, or the taxpayer's e.firma certificate/key/password in the official application. Login access and the signing requirement for the selected refund route are separate tests.
2. In **Perfil del contribuyente**, select **Ejercicio 2025**, the correct normal/complementary type and all actual income sections. Keep the exercise visible in the saved workpaper; do not select a different year to force a desired form.
3. Review the prefilled **Ingresos**, provisionals, withholding and personal deductions against the reconciled schedules. In the business/professional section, **Pagos provisionales del ejercicio** is the actual eligible ISR paid. Correct a wrong provisional source return using its proper complementary procedure; do not invent a matching annual credit.
4. Where applicable, answer **¿Los ingresos fueron obtenidos a través de copropiedad o sociedad conyugal?** and enter the actual representative/share information. That field does not itself authorise an equal split.
5. Validate personal deduction candidates. SAT's **Motivo de no clasificación**, **Validar** and **Guardar** controls assist review/reclassification, but the statutory conditions and evidence still decide eligibility.
6. In **Determinación**, review the calculation, credits and **¿Qué deseas hacer con tu saldo a favor?**. Select the lawful refund/compensation destination using the actual available balance and prior requests; enter/confirm the taxpayer's own active CLABE where needed. Do not assume every balance can be freely offset against IVA or an unrelated tax.
7. Review the entire return, obtain the actual taxpayer/professional approval, sign/send using the required authentication, and save the **acuse de recibo**, operation number, date, complete return and any **FCF/línea de captura**. An unpaid capture line is not settlement of the tax.
8. Pay through an authorised bank using the correct current capture line and its actual expiry/due date; save the bank receipt and match the payment to the return/period. Follow the refund or debt status to its actual resolution and retain any notices/responses.

Source scope: [SAT 2025 FAQ, I A, C.3, D, E, F, G and II RESICO](https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf). The taxpayer must handle the real service's authentication challenge; no secret or challenge is bypassed. Changes to a filed return require the proper **declaración complementaria**, preserving the original and replacement folios and actual payments; do not erase history or assume unrestricted amendments after an examination begins. [CFF art. 32](https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf).

### Ordinary annual payment and the dated 2025 instalment facility

| Route | Conditions / action | Official source |
|---|---|---|
| Ordinary annual balance | Statutory filing in **April following the income year**; read actual payment due date, CFF deadline rules and any operative extension. A capture line has its own stated validity, not a universal fixed life. | LISR art. 150: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf; CFF art. 12: https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf |
| Special **2025 annual** instalments offered in RMF 2026 | Up to **six monthly successive instalments**, only where both return and first instalment were within the statutory April filing period. It is not an option first elected within a period after a late November filing. SAT's 2025 FAQ says the facility is unavailable for RESICO. | RMF 2026 rule 3.17.3: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf; SAT FAQ II question 3: https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf |
| First instalment | Total debt divided by the number selected, no more than the stated maximum. | RMF 3.17.3 I: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Following instalments | Balance after the first instalment divided by the rule's factor: **2 = 0.9859; 3 = 1.9581; 4 = 2.9167; 5 = 3.8619; 6 = 4.7938**. Financing is included; use the actual generated FCFs. | RMF 3.17.3 II: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Payment/arrears within that facility | Later instalments due by the end of their month (stated next-business-day rule); the ultimate **30 September 2026** settlement condition has already passed as at this reading. A late instalment uses the prescribed **0.0207 per month** factor and current payment line procedure. An unpaid arrangement now needs debt regularisation, not a newly invented timely election. | RMF 3.17.3 II–III and final paragraphs: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| **2026 income filed in 2027** instalments | **Non-usable hold:** the specific 2027 administrative facility/conditions have not been read or confirmed. Do not reuse the preceding 2025-only rule as an entitlement. | Period limitation in RMF 2026 3.17.3: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |

### Refund route, credentials and follow-up [RMF 2.3.2; CFF art. 22](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf)

The **2026 automatic annual-refund facility** covers the **2025 exercise** and the option through **31 July 2026**. That cutoff has passed at the 17 November 2026 read date. A late/corrective annual return filed after that date does not acquire automatic treatment merely by reporting a small balance. Use the applicable **FED** request route with the evidence and e.firma requirements where automatic treatment is unavailable; avoid duplicate requests for the same amount.

| RMF 2026 automatic facility condition, historical 2025 exercise | Rule | Official source |
|---|---|---|
| Eligible balance up to **MXN 10,000** | Contraseña is permitted by this rule; all other eligibility conditions still apply. | RMF 2.3.2 I: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| **MXN 10,001–150,000** | This rule requires e.firma/e.firma portable; logging in with Contraseña alone is not enough for this refund election. | RMF 2.3.2 I: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Above **MXN 150,000** | Excluded from this automatic facility; use the supported request route. | RMF 2.3.2 exclusion II: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Bank details | **18-digit CLABE**, active and in the taxpayer's own name, with the stated bank details. | RMF 2.3.2 II: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |
| Other exclusions | Coownership/community property/estate income, different exercises, specified late/non-elected/duplicate FED situations, published tax-status or false-invoice conditions, certificate cancellation and other listed grounds must be checked. | RMF 2.3.2 exclusions I–XI: https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf |

Monitor **Estado de tu devolución**, correspondence and any **solventar inconsistencias** option. The rule describes a resulting FED submission with RFC, Contraseña and e.firma/e.firma portable when that option is used. A result authorising only part of a refund does not authorise repeatedly requesting the whole balance without accounting for the amount already paid. [RMF 2.3.2](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

CFF art. 22's ordinary **40-day** return period starts from a properly supported request with the required data. Error corrections, first/second information requests, suspended counting periods and a formal examination under art. 22-D can alter the elapsed time; it is not a guaranteed maximum bank-credit date. The article specifies the first request/response periods, limited subsequent request and suspension rules. No universal refund-size trigger or promised short refund timetable is used here. For 2026 income filed in 2027, the future automatic facility/credentials/cutoff must be confirmed then. [CFF art. 22](https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf).

## Completion checklist

- [ ] Intake's regime, residence, period, effective dates and referral/hold decisions carried forward.
- [ ] All due ISR/IVA periods and corrections reconciled; actual payments separated from acuses, liabilities and withholding credits.
- [ ] Issued/received XML, bank/cash, cancellations, payment timing and all other income schedules reconciled.
- [ ] AEP deductions, investments, payroll/employer IMSS, PTU and indexed losses substantiated; personal deductions and own insurance classified correctly.
- [ ] RESICO definitive-monthly/annual/exit branch explicitly selected from its actual conditions, with no duplicate credits.
- [ ] IVA input eligibility and monthly balances checked; DIOT relief or reporting supported for the actual person/period.
- [ ] Correct year's annual tariff and operative administrative procedure used; 2025 screens not passed off as the 2026-income service.
- [ ] CLABE, election and existing requests checked; payment/refund/debt follow-up assigned.
- [ ] Human approval, submitted return, acuse, capture line, actual bank receipt and subsequent status retained where submission occurred. Otherwise label the output **working papers only**.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público Certificado, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

All dates below are **actual provision-level readings on 2026-11-17**. Long texts were read for the listed sections and neighbouring conditions; a download alone is not a full-source read. Legal excerpts identify the native controlling text.

| Source / sections read | Native text / evidence boundary | Official URL | Read date |
|---|---|---|---|
| Current LISR, last reform 1 April 2024: arts. 1, 27 III–V, 92, 102–110, 113-E–J, 150–152; incentive arts. 189–190/202 consulted for referral | “efectivamente percibidos”; “diez ejercicios siguientes”; “no será aplicable tratándose de la fracción V”. Receipt basis, deductions/losses, personal caps and correct annual table identity checked; incentive authorisations not determined here. | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf; official HTML: https://www.ordenjuridico.gob.mx/Documentos/Federal/html/wo25.html | 2026-11-17 |
| Enacted RMF 2026: 2.3.2, 2.8.1.17, 3.13.3–9, 17–21, 34, 3.17.1/3, 4.5.1, Transitory XV | “será definitivo”; “por el ejercicio 2025”; “hasta el día 31 de julio”. Read actual branches, exclusions, payment factors and deadline conditions. | https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf | 2026-11-17 |
| Anexo 8 C I–II, official DOF 28 December 2025 | “correspondiente al ejercicio de 2025”; “correspondiente al ejercicio de 2026”. All eleven bands in each annual table read and checked against rendered pages, including the continued 2026 rows. | https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf | 2026-11-17 |
| Current CFF, last reform 9 April 2026: arts. 12, 21–22, 31–32, 73, 76, 81 XXVI, 82, 84 IV | “cada mes o fracción”; “incrementar en 50%”; “cuarenta días”; “no es espontáneo”. Current duty/fine classifications and refund request/suspension conditions read; criminal fact patterns not resolved. | https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | 2026-11-17 |
| LIF 2026 art. 11 and commencement | “Al 1.38 por ciento mensual”; extension and instalment rates distinguished from mora. Derived mora: 1.38% × 1.5 = 2.07%. | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIF_2026.pdf | 2026-11-17 |
| Anexo 5 A and B, CFF arts. 82 I, 82 XXVI, 84 IV | “por cada una de las obligaciones no declaradas”; “fracción XXVI”. Updated general fines and compiled DIOT amount read; RESICO's distinct 84 IV b) checked in the current CFF. | https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-5-RMF-2026_DOF-28122025.pdf | 2026-11-17 |
| LIVA arts. 1, 1-A/B, 3, 5, 5-D, 15, 18-J–M, 32 VIII | “efectivamente pagado”; “el 50%”; “la retención se deberá efectuar al 100%”. Read withholding conditions, input-credit restrictions and separate platform option. | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf | 2026-11-17 |
| RLIVA art. 3 I and art. 4, current official text, last reform 25 September 2014 | “dos terceras partes”; exact independent-services/commission/temporary-use scope. Current regulation text, status and arts. 3–4 read alongside current LIVA. | https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf | 2026-11-17 |
| SAT annual PF 2025 FAQ: I A, C.3, D–G; II RESICO | “pagos efectivamente realizados”; “Ejercicio 2025”; “no ... disponible para RESICO”. Actual annual screens, preloads, documents, refund election and period-specific RESICO guidance read. | https://sat.gob.mx/minisitio/DeclaracionAnual/Personas/documentos/PreguntasFrecuentes_AnualPF2025.pdf | 2026-11-17 |
| INEGI 2026 UMA announcement and historical series | “a partir del 1 de febrero de 2026”. Period values and the FAQ's differing historical five-UMA scalar reconciled explicitly above. | https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/uma/uma2026.pdf; https://www.inegi.org.mx/temas/uma/ | 2026-11-17 |
| IMSS continuation/PTI guidance; LSS arts. 218–220 | “mensualidades adelantadas”; “mensual, bimestral, semestral o anual”. Schemes/frequencies separated; own-payment tax deduction not inferred. | https://www.imss.gob.mx/tramites/imss02007; https://www.imss.gob.mx/prensa/archivo/202502/074; https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf | 2026-11-17 |
| RMF fourth enacted amendment, amendment list and relevant 2.5/2.8 changes/commencement | “el día de su publicación”. Core 2.3.2/3.13/3.17/4.5 rules used above were not changed by this act; current accounting record duties must still be applied where relevant. | https://dof.gob.mx/nota_detalle.php?codigo=5802597&fecha=30/10/2026 | 2026-11-17 |

Not yet confirmed: the published 2027 annual application/screens and administrative refund/instalment rules for 2026 income; case-specific current border stimulus qualification and filing; R&D/film/theatre project authorisation, current application procedures and all incentive caps for a particular claim; a person's own voluntary-IMSS deduction classification and exact component-rate schedule; procedure/penalty consequences for a particular false-invoice case; treaty/foreign-tax-credit computations and exceptional coownership elections beyond the cited branch. These are **non-usable holds**. The old unsupported SAT audit percentages, fixed generic-RFC trigger, automatic equal-spouse allocation, predial personal deduction, blanket government/platform withholding, arbitrary capture-line life, refund-size timetables and January clients/suppliers mandate are not usable rules.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mx-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mx-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
