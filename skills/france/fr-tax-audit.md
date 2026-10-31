---
name: fr-tax-audit
description: French tax audit procedures, penalties, and taxpayer rights (contrôle fiscal). Trigger on phrases like "contrôle fiscal", "vérification de comptabilité", "redressement fiscal", "DGFIP contrôle", "proposition de rectification", "pénalités fiscales", "majoration 40%", "manquement délibéré", "intérêts de retard", "abus de droit", "commission départementale", "recours hiérarchique", "charte du contribuable vérifié", "FEC contrôle", "rejet de comptabilité", "acte anormal de gestion", "tax audit France", "tax penalties France", "objection tax France", "délai de reprise", "prescription fiscale", "régularisation spontanée". Covers the 8 verification axes (FEC, IS, charge deductibility, CCA 455, revenue, TVA, fixed assets, international), penalty schedules, audit procedures, and taxpayer rights.
version: 1.4
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: tax audits of a business, penalties and taxpayer rights (contrôle fiscal) v1.4

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

This skill covers the French tax audit of a business (vérification de comptabilité and examen de comptabilité) by the DGFiP: the notice, the accounting entries file (FEC), the time limits, the proposition de rectification and the answer to it, the appeals, the reassessment periods, the surcharges and late-payment interest, and the points an inspector checks. Figures are for tax year 2026. The procedure rules, surcharges and interest rates below are those in force on 19 October 2026, read on official pages on 19 October 2026; an audit run in 2026 can reach income of 2025 declared in 2026 and every earlier year still open under the reassessment periods, and each audited year is taxed under the corporation tax and VAT figures of its own year, so the 2026 figures shown for those two taxes must be checked again for each year under audit. Each official page's own publication date is given in its table where it matters.

> **Disclaimer:** This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing or answering the administration.

## Section 1: Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | France |
| Authority | Direction Générale des Finances Publiques (DGFiP) |
| Scope | Vérification de comptabilité (on site) and examen de comptabilité (at the office, from the FEC) of businesses taxed under corporation tax (IS) or income tax (IR) on a real regime |
| Key legislation | Livre des procédures fiscales (LPF) and Code général des impôts (CGI), read here through BOFiP because legifrance cannot be read by our fetcher |
| FEC obligation | LPF art. L. 47 A; format in LPF art. A. 47 A-1 |
| Notices | form 3927-SD (vérification de comptabilité), form 3923-EC-SD (examen de comptabilité), form 3929-SD (personal tax situation, ESFP, out of scope here) |
| Related skills | `france-bookkeeping` (the FEC and the chart of accounts), `fr-business-accounting` (corporation tax and VAT map), `france-vat-return`, `france-transfer-pricing`, `france-financial-statements` |

## Section 2: Audit procedure (phases)

The phases below follow BOFiP. The time limits are in words because the pages print them in words.

**Audit procedure phases**

| Phase | Legal basis | What the page says |
| --- | --- | --- |
| 1. Avis de vérification (form 3927-SD) or avis d'examen de comptabilité (form 3923-EC-SD) | LPF art. L. 47; BOI-CF-PGR-20-10 (https://bofip.impots.gouv.fr/bofip/236-PGP.html) | The service must inform the taxpayer in writing before the audit. The notice must say the taxpayer may be assisted by an adviser of their choice, on pain of nullity. The first visit can only take place after a reasonable time to get an adviser. The page cites the Conseil d'État setting at least "deux jours francs" (two clear days), and also a decision on a delay "qui ne peut être inférieur à deux jours ouvrés" (not less than two working days). To count the two clear days the page says: "il convient de ne retenir ni : le jour de réception de l'avis de vérification ; le jour du début du contrôle ; les samedis, dimanches et jours fériés". The page recommends sending the notice about three weeks ("trois semaines environ") before the first visit. |
| 2. FEC hand-over, vérification de comptabilité | LPF art. L. 47 A; BOI-CF-IOR-60-40-10 (https://bofip.impots.gouv.fr/bofip/9026-PGP.html) | Where the books are kept on a computer, the taxpayer meets the duty to present the accounts by handing over a copy of the FEC "au début des opérations de contrôle" (at the start of the audit operations). Not within a fixed number of days. |
| 2 bis. FEC sending, examen de comptabilité | LPF art. L. 47 AA; BOI-CF-PGR-20-10 (https://bofip.impots.gouv.fr/bofip/236-PGP.html) | The notice 3923-EC-SD says the FEC must be sent "sous quinze jours à compter de la réception de l'avis" (within fifteen days of receiving the notice). |
| 3. On-site work and its length | LPF art. L. 52; BOI-CF-PGR-20-30 (https://bofip.impots.gouv.fr/bofip/243-PGP.html) | See "Length of the on-site audit" below. |
| 4. Proposition de rectification | LPF art. L. 57; BOI-CF-IOR-10-50-10 (https://bofip.impots.gouv.fr/bofip/5510-PGP.html) | The formal written notice of each adjustment. It interrupts the reassessment period and opens the answer period. |
| 5. Taxpayer's answer | LPF art. L. 11, L. 57 and R.* 57-1; BOI-CF-IOR-10-50-10 | Thirty clear days from receipt, extended by thirty days on an express timely request. LPF L. 57 says the request must be received before expiry; the published BOFiP practice accepts a request presented or dispatched before expiry, with La Poste's stamp proving postal dispatch. Exclude the receipt day and the expiry day when counting the clear period; if the last permissible day is Saturday, Sunday or a public holiday, use the next working day. A late request is inadmissible save exceptional circumstances. |
| 6. Administration's reply to the observations (form 3926-CFE-SD) | LPF art. L. 57 and L. 57 A | Each point kept or dropped, with reasons for any point on which disagreement persists. |
| 7. Recours hiérarchique, then interlocution | BOI-CF-PGR-20-10 (https://bofip.impots.gouv.fr/bofip/236-PGP.html) | Two distinct routes. During the control, raise actual procedural difficulties with the superior then the interlocutor before the proposition de rectification in the contradictory procedure; for an ex officio assessment, before notification of its bases, or collection if LPF L. 76 dispenses with that notification. The later merits route in a contradictory procedure opens after form 3926-CFE-SD: thirty clear days from its receipt for the first level, then thirty clear days from receipt of the first-level report for interlocution. Exclude the receipt and dispatch days. If the superior signed penalties exclusive of good faith, expressly request direct interlocution within thirty clear days of receiving form 3926. A merits request immediately after the proposal is premature. |
| 8. Commission départementale des impôts directs et des taxes sur le chiffre d'affaires | LPF art. L. 59 A and R.* 59-1; BOI-CF-CMSS-20-30 (https://bofip.impots.gouv.fr/bofip/4355-PGP.html) and BOI-CF-CMSS-20-10 (https://bofip.impots.gouv.fr/bofip/873-PGP.html) | For a disagreement that persists. The taxpayer has thirty days from receipt of the administration's reply to ask for it. Above the turnover limits in the commission table below, the national commission is competent instead. An abuse of law case goes to the comité de l'abus de droit, not to this commission. |
| 9. Mise en recouvrement | | The additional tax, interest and surcharges are put into collection (avis de mise en recouvrement). |

### Length of the on-site audit (LPF art. L. 52)

BOFiP BOI-CF-PGR-20-30 (version published 20 December 2017, https://bofip.impots.gouv.fr/bofip/243-PGP.html) says LPF art. L. 52 "limite à trois mois la durée de la vérification sur place de la comptabilité des entreprises dont le montant du chiffre d'affaires ou des recettes brutes n'excède pas les limites d'admission au régime simplifié d'imposition". So:

- The three-month limit covers only a business whose turnover or gross receipts do not exceed the admission limits of the simplified tax regime (régime simplifié d'imposition, CGI art. 302 septies A). The page does not print those limits in digits and this skill does not either: read them on the official page for the year concerned.
- It runs from the first on-site visit, and it limits only the time spent on site.
- It becomes six months where the accounts have serious irregularities that deprive them of probative value (LPF art. L. 52, II, 4°).
- It is suspended until the business hands over a FEC that meets the standards of LPF art. A. 47 A-1.
- It does not apply in the cases of LPF art. L. 52, II (for example after a flagrance fiscale report, II-5°; and the time limit cannot be raised against the administration while it examines observations the taxpayer presents after the on-site work, II-1°), nor to the holding companies covered by LPF art. L. 52 A.
- For an examen de comptabilité, within six clear months of receiving **all conforming FEC copies**, the administration must dispatch either the proposition de rectification (2126-EC-SD) or an avis d'absence de rectification (3953-EC). Exclude the receipt and dispatch days. Incomplete or nonconforming copies do not start that clock and the remote procedure can be cancelled; this does not replace the distinct FEC penalties or on-site rules (LPF art. L. 47 AA, 4°).

### Taxpayer guarantees

**Taxpayer guarantees**

| Right | Source |
| --- | --- |
| Written notice before the audit, naming the right to an adviser | LPF art. L. 47; https://bofip.impots.gouv.fr/bofip/236-PGP.html |
| Oral and adversarial discussion of the accounting findings before any reassessment | LPF art. L. 47 A; https://bofip.impots.gouv.fr/bofip/9026-PGP.html |
| Charte des droits et obligations du contribuable vérifié, made available with the notice and updated every year; its provisions bind the administration ("opposables à l'administration") | https://www.impots.gouv.fr/charte-des-droits-et-obligations-du-contribuable-verifie |
| Recours hiérarchique and interlocution: procedural difficulties during control, and the separate thirty-clear-day post-reply merits route, as set out above | https://bofip.impots.gouv.fr/bofip/236-PGP.html |
| Departmental tax commission | https://bofip.impots.gouv.fr/bofip/4355-PGP.html |
| On-site length limited for small businesses (three months, six months on serious irregularities) | LPF art. L. 52; https://bofip.impots.gouv.fr/bofip/243-PGP.html |

**Which commission is competent (BOI-CF-CMSS-20-10)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/873-PGP.html |
| Turnover excluding VAT above which the departmental commission is NOT competent, for a business carrying on an industrial or commercial activity whose main trade is selling goods, food to take away or eat on site, or providing accommodation | EUR 50,000,000 | "excède 50 000 000 € s'il s'agit d'entreprises dont le commerce principal est de vendre des marchandises" |
| The same limit for other businesses | EUR 25,000,000 | "ou de 25 000 000 € s'il s'agit d'autres entreprises" |

Above those limits the commission nationale des impôts directs et des taxes sur le chiffre d'affaires is competent. The page version is dated 5 August 2013.

## Section 3: The 8 verification axes

These are practical review questions, not statutory presumptions of risk, concealment or non-deductibility. Account codes and the eight-axis layout are this Guide’s working method, not a list prescribed by the administration. An unexplained balance or missing document requires facts and the applicable rule before a tax adjustment.

### Axis 1: FEC examination (LPF art. L. 47 A)

**Checks on the FEC file**

| Check | Consequence of failure |
| --- | --- |
| Format as set by LPF art. A. 47 A-1 (the first eighteen fields; a nineteenth for an establishment code where several establishments are merged), described in BOI-CF-IOR-60-40-20 (https://bofip.impots.gouv.fr/bofip/9028-PGP.html) | The file does not meet the standard: the fine in the table below, and the L. 52 time limit stays suspended |
| Global balance: total debits = total credits | Points to unreliable books (comptabilité non probante) |
| Per-entry balance: each EcritureNum is balanced | Points to unreliable books |
| Sequential numbering, rising, with no break or inversion | The format page requires it |
| Dates within the financial year | Possible fictitious entries |
| PieceRef populated for every entry | Missing supporting documents |
| CompteNum consistent with PCG roots | Irregular accounts |

**FEC: fine for not presenting the accounts in the required form (CGI art. 1729 D)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/9026-PGP.html |
| Fine where no tax is adjusted | EUR 5,000 | "d’une amende égale à 5 000 €" |
| Where tax is adjusted: increase of the duties charged, if higher than the fine | 10% | "majoration de 10 % des droits" |
| Duties recalled over the period above which the increase applies instead of the fine | EUR 50,000 | "supérieur à 50 000 €, l’amende est égale à 10 % de ces droits" |

The page (version published 15 December 2021) puts it as two cases: no adjustment, the fine; an adjustment, the fine or the increase on the duties charged if that is higher. If the business does not meet the duty to hand over the FEC, the second paragraph of LPF art. L. 74 provides that the tax bases are assessed by estimate (évaluées d'office). Where the accounts lose probative value, the general consequence is set by the burden of proof rules of LPF art. L. 192; this skill does not restate them because no saved page was read for them.

### Axis 2: Corporation tax (IS) control (CGI art. 38 to 39 and 219)

**Corporation tax rates and the PME reduced rate, 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Standard rate | 25% | "imposée au taux normal de 25 %" |
| Reduced rate | 15% | "un taux réduit fixé à 15 %" |
| Slice of profit the reduced rate covers | EUR 42,500 | "la part des bénéfices allant jusqu'à 42 500 €" |
| Turnover condition, for the financial year, brought to twelve months where needed | EUR 10,000,000 | "Chiffre d'affaires inférieur ou égal à 10 000 000 €" |
| Ownership condition, with the capital fully paid up | 75% | "détenu pour au moins 75 % par des personnes physiques" |

The page is "Vérifié le 17 février 2026". Apply the full CGI art. 219, I-b conditions together: turnover at or below the table limit, annualised where required; capital entirely paid up and **continuously** at least 75% held by individuals, or by a company meeting the same conditions whose capital is at least 75% held by individuals. For a parent of an art. 223 A/223 A bis group, add the turnover of all group members. The statutory percentage excludes holdings of sociétés de capital-risque, fonds communs de placement à risques, the specified pre-2013 fonds professionnels spécialisés, fonds professionnels de capital investissement, sociétés de développement régional and sociétés financières d'innovation only where there is no CGI art. 39, 12 dependence between the company and those vehicles. Year-end individual ownership alone, or a corporate shareholder satisfying only the 75% individual-ownership limb, is insufficient. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562/2026-10-29

**IS control checkpoints**

| Checkpoint | Legal basis | Detail |
| --- | --- | --- |
| IS add-back (account 695) | CGI art. 213 | Corporation tax is expressly non-deductible: verify its add-back |
| PME reduced rate eligibility | CGI art. 219, I-b | Both conditions in the table above. The turnover limit is brought to twelve months for a short or long year; CGI art. 219 I-b also expressly states the EUR 42,500 profit slice per twelve months, so adjust that slice to the accounting-period length |
| Non-deductible charges | CGI art. 39 | Fines, luxury expenses, personal expenses |
| Acte anormal de gestion | Case law (Conseil d'État) | Charges unrelated to the interest of the business |

### Axis 3: Charge deductibility (CGI art. 39-1)

**Cumulative charge checks:**
1. Incurred in the interest of the business or as part of its normal management
2. An effective charge supported by sufficient invoices or documentation
3. Included in the expenses of the period in which it was incurred
4. A charge rather than acquisition of an asset: test the decrease of net assets and the specific capitalisation rules
5. Not excluded by a specific tax provision

**Systematic examination grid**

| Account | Typical audit question |
| --- | --- |
| 604 (Subcontracting, APIs) | Exclusively professional use? Invoices in the company name? |
| 6132 (Home office) | Justified proportion? Conforming to BOFiP? Agreement exists? |
| 6135 (SaaS, hosting) | Wholly professional? No personal consumption? |
| 6181 (Documentation) | Link with the business activity? |
| 622 (Intermediaries) | Nature and supporting documents? |
| 6231 (Advertising) | Gifts or advertising? Directories = advertising? |
| 627 and 6278 (Banking) | Consistent with bank statements? |
| 651 (Domain names) | All related to the business activity? |
| 654 (Chargebacks) | Irrecoverability documented? |

### Axis 4: Shareholder current account 455 (CGI art. 39-1-3° and 212)

**High fiscal risk**, especially for an SASU or EURL.

**Current account (455) checks**

| Check | Detail |
| --- | --- |
| Pre-incorporation expenses | Taken over by the company in the form company law requires (état des actes annexed to the statuts, or a later decision)? Professional character? |
| Home office | Justified surface proportion? Plan available? Mortgage principal is never deductible |
| Interest on the current account | If no interest is paid, there is no interest expense to cap; that alone does not settle transfer-pricing, distribution or abnormal-management issues. If interest is paid, test the applicable deductible-rate limit. The reference rate is "la moyenne annuelle des taux effectifs moyens pratiqués par les établissements de crédit pour des prêts à taux variable aux entreprises d'une durée initiale supérieure à deux ans" (BOI-BIC-CHG-50-50-30, https://bofip.impots.gouv.fr/bofip/5505-PGP.html). It is not an ECB rate. Not yet confirmed in this Guide’s selected source chain: the complete art. 39-1-3° paid-up-capital gate and its interaction with art. 212’s proven higher market-rate option. Establish those gates through the corporation-tax/transfer-pricing method before deducting interest; the reference-rate quotation alone is not the entire entitlement |
| Currency conversion | Rate used and its consistency; the inspector may ask for the rate of each transaction |

### Axis 5: Revenue (CGI art. 38-2)

**Revenue checks**

| Check | Detail |
| --- | --- |
| Revenue completeness | Cross-check payment platforms (Stripe, PayPal) against the accounts |
| Period cut-off | Revenue booked in the right financial year |
| Credit balance on 411 (Clients) | Abnormal: an advance? Omitted revenue? |
| Asset disposals | Proper classification (account 775)? |
| Commissions and ancillary revenue | Nature? Foreign withholding tax? |

### Axis 6: VAT (TVA)

**If franchise en base (CGI art. 293 B):**

**VAT franchise thresholds in force for 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 |
| Services: prior-year turnover limit | EUR 37,500 | "est inférieur ou égal à 37 500 € (seuil de la franchise en base de TVA)" |
| Services: current-year higher limit | EUR 41,250 | "est inférieur ou égal à 41 250 € (seuil majoré de la franchise en base de TVA)" |
| Goods and accommodation: prior-year turnover limit | EUR 85,000 | "est inférieur ou égal à 85 000 € (seuil de la franchise en base de TVA)" |
| Goods and accommodation: current-year higher limit | EUR 93,500 | "est inférieur ou égal à 93 500 € (seuil majoré de la franchise en base de TVA)" |

The page is "Vérifié le 01 janvier 2026" and says the franchise thresholds for 2026 "restent inchangés"; the single lower threshold proposed by the 2025 finance law was abandoned. Lawyers, authors and performers have their own limits on the same page: see `france-vat-return`.

**Franchise en base checks**

| Check | Detail |
| --- | --- |
| Threshold monitoring | The limits in the table above, prior year and current year, for the activity concerned |
| Invoice mention | "TVA non applicable, art. 293 B du CGI" |
| Asset disposals | Subject to VAT or exempt? |
| Intra-EU and extra-EU services received | Reverse charge (CGI art. 283-2)? |

**If VAT is collected:**

**VAT collected checks**

| Check | Detail |
| --- | --- |
| CA3 or CA12 agrees with the accounts | |
| Deductible VAT documented | |
| Deduction pro-rata if mixed activity | |

### Axis 7: Fixed assets and depreciation (CGI art. 39-1-2°)

**Small equipment taken to expense (BOI-BIC-CHG-20-30-10)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |
| Unit value excluding VAT up to which tools and equipment (PCG accounts 2154 and 2155), office furniture and equipment, and software may be expensed at once | EUR 500 | "valeur unitaire hors taxes n'excédant pas 500 €" |

The limit is a tolerance, measured excluding VAT per unit, and on the global price where several items form one piece of equipment. It excludes transport equipment. The initial-furniture/full-renewal exclusion quoted below has an express exception when the entire initial equipment or renewal itself does not exceed EUR 500. The page does not say a franchise business measures it including VAT; ask the accountant. For furniture the page excludes the initial furnishing of an office building, restaurant or shop and its complete renewal: "La mesure n'est notamment pas applicable à l'équipement initial en mobilier d'un immeuble de bureaux, d'un restaurant ou d'un magasin commercial, ni au renouvellement complet de ce mobilier, même si la valeur unitaire de chaque meuble est inférieure à 500 € hors taxes".

**Fixed assets checks**

| Check | Detail |
| --- | --- |
| Capitalisation | Test whether the expenditure acquires an asset; exceeding EUR 500 only removes this immediate-expense tolerance and does not turn every operating cost into a fixed asset |
| Depreciation method | Period consistent with the normal use of the asset; pro rata temporis from the date the asset is put into service |
| Mixed use | Phone and computer: wholly professional use justified? If mixed, only the professional part is deductible |

### Axis 8: International operations

**International operations checks**

| Check | Detail |
| --- | --- |
| Transfer pricing | Applies where there is a foreign subsidiary or intra-group transactions: see `france-transfer-pricing` |
| Withholding tax (CGI art. 182 B) | Payments to foreign providers for services used in France: withholding due? Check the tax treaty. The rate is not on a page read for this skill |
| DES (déclaration européenne de services) | Due only where the supplier has its seat in France, or a French establishment providing the service, or failing those its domicile/habitual residence there; the recipient is a taxable person acting as such with its seat, receiving establishment, or domicile/habitual residence in another EU State; the service is located there under Directive 2006/112/EC art. 44; and that recipient owes the tax under art. 196. Omit services exempt in the recipient State. This is an outbound-supply obligation, not a purchase declaration. The CA3 notice says: "toute personne physique ou morale est tenue de souscrire une déclaration européenne de services (DES) lorsque les conditions suivantes sont réunies" (https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf) |

## Section 4: Penalty schedule

### Interest on late payment (intérêt de retard, CGI art. 1727)

**Interest parameters**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1458-PGP.html |
| Rate per month of delay | 0.2% | "taux de l'intérêt de retard de 0,2 % par mois" |
| Reduction of the interest where the taxpayer regularises during an audit (LPF art. L. 62) | 30% | "l'intérêt de retard est réduit de 30 % lorsqu’au cours d'un contrôle" |

- Start: interest runs from the first day of the month after the one in which the tax should have been paid.
- End: for tax paid late by the taxpayer, the last day of the month of payment. For additional tax assessed after an audit (an insufficiency under CGI art. 1729), the last day of the month of the proposition de rectification, or of the issue of the rôle where the additional tax is staggered (CGI art. 1727, IV-4). For a return not filed (CGI art. 1728 cases), the last day of the month the return is filed or the bases are notified. For a corrective declaration, including CGI art. 1727 V or LPF L. 62 regularisation, stop at the end of the month that declaration is filed; do not automatically use the later proposal or payment month.
- The interest is due on top of any surcharge.
- A taxpayer in good faith who files a corrective return spontaneously has the interest reduced by half only if the infringement is not exclusive of good faith and there is payment of the resulting tax with the corrective declaration, or for a rôle by the payment deadline on the notice. An accepted public-accountant plan for the tax preserves the reduction in place of immediate/deadline payment (CGI art. 1727, V; BOI-CF-INF-10-10-20). Filing alone without one of these statutory payment routes does not establish this reduction. Current source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330/2026-10-29
- Do not quote a yearly rate: the page prints only the monthly rate.

### Surcharges (majorations, CGI art. 1728 and 1729)

**Surcharge schedule**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4911-PGP.html |
| Return filed late, spontaneously or within thirty days of a formal notice (CGI art. 1728) | 10% | "la majoration de 10 % prévue par l’article 1728 du CGI" |
| Return filed more than thirty days after a formal notice (mise en demeure), even in good faith (CGI art. 1728) | 40% | "40 % sur le tout (1728)" |
| Deliberate breach (manquement délibéré, CGI art. 1729), on the additional tax | 40% | "la majoration de 40 % pour manquement délibéré prévue par l’article 1729 du CGI" |
| Abuse of law where principal initiative or principal benefit is established; fraudulent manoeuvres; concealment of a contractual price (CGI art. 1729) | 80%; abuse reduced to 40% otherwise | "80 % sur les droits résultant des rappels (1729)" |

- In the page's table, additional tax in good faith ("Rappels en cas de bonne foi") carries only the CGI art. 1728 surcharge where the return was late (the rate in the table depends on whether it was filed before, within, or more than thirty days after a mise en demeure), and no CGI art. 1729 surcharge; additional tax with a deliberate breach adds the CGI art. 1729 rate. Interest is due in both cases.
- Under current CGI art. 1729 b, abuse of law carries 80%, reduced to 40% unless the administration establishes that the taxpayer had the principal initiative or was the principal beneficiary. The older BOFiP combination-table example names the beneficiary case; it is not an exhaustive statement of the statutory initiative alternative.

### Computation example: deliberate breach (hypothetical)

Hypothetical amounts in euro, for illustration only. A company already well above the reduced-rate slice, so all the extra profit falls in the standard rate in the IS table above; the deliberate breach rate and the monthly interest rate from the tables above; twelve months from the month after the due date to the month of the proposition de rectification.

~~~
Disallowed charges:                          10,000.00
Additional IS (standard rate):                2,500.00
Late interest (12 months at the monthly rate):   60.00
Surcharge (deliberate breach rate):           1,000.00
Total assessment:                             3,560.00
~~~

If the taxpayer had regularised during the audit under LPF art. L. 62, the interest would be reduced as in the interest table, and the conditions of that procedure apply.

**Qualification of that counterfactual.** The deliberate-breach facts in the illustration do not qualify for LPF L. 62: good faith is a separate mandatory gate. Only a different, eligible good-faith case meeting all Section 8 conditions gets the reduction. If that case has EUR 60 unreduced interest, the 30% reduction leaves EUR 42 (60 × 70%); it does not reduce the EUR 1,000 deliberate-breach surcharge in the original fixture or make that fixture eligible.


### Recomputable checks of the existing penalty methods

The first block recomputes the hypothetical deliberate-breach illustration above. Its twelve chargeable months and valid 40% deliberate-breach finding are declared facts, not inferences from an arithmetic discrepancy.

```oa-check
name: Existing audit illustration, EUR 10000 disallowed charge
inputs:
  disallowed: 10000
  tax_rate: 0.25
  months: 12
  monthly_interest: 0.002
  deliberate_rate: 0.40
steps:
  - extra_tax: disallowed * tax_rate
  - interest: extra_tax * months * monthly_interest
  - surcharge: extra_tax * deliberate_rate
  - total: extra_tax + interest + surcharge
expected:
  extra_tax: 2500
  interest: 60
  surcharge: 1000
  total: 3560
```

For the existing on-site FEC fine, assume one control with EUR 60,000 recalled duties over its covered periods: max(EUR 5,000, 10% of 60,000) is EUR 6,000, once for the control. At exactly EUR 50,000 duties the result remains EUR 5,000. A remote-examination failure uses the separately stated fixed fine instead.

```oa-check
name: On-site FEC fine, recalled duties EUR 60000
inputs:
  recalled_duties: 60000
  floor: 5000
  share: 0.10
steps:
  - proportional: recalled_duties * share
  - fine: max(floor, proportional)
  - at_boundary: max(floor, 50000 * share)
expected:
  proportional: 6000
  fine: 6000
  at_boundary: 5000
```

## Section 5: Risk assessment grid

### Aggravating factors

The following labels are internal triage prompts, not verified empirical audit probabilities or automatic legal consequences.

**Aggravating factors**

| Factor | Impact |
| --- | --- |
| SASU or EURL without a statutory auditor | Heightened scrutiny of personal charges |
| First financial year | Limited history, frequent errors |
| Revenue in foreign currency | Conversion rate risk |
| High 455 current account balance | Suspicion of confusion between the company's and the owner's assets |
| Internet or SaaS activity | Territorial allocation difficulties |

### Mitigating factors

**Mitigating factors**

| Factor | Impact |
| --- | --- |
| Small size, within the simplified-regime admission limits | The on-site audit is limited in time (Section 2) |
| Regular bookkeeping | Compliant FEC, balanced entries |
| First year in good faith | No CGI art. 1729 surcharge on additional tax in good faith, and a spontaneous corrective return halves the interest |
| No employees | Check officer remuneration, earlier employment periods and other payroll obligations before concluding there is no payroll exposure |
| Franchise en base | No collected-VAT risk while within the limits |

## Section 6: Common adjustment scenarios

### Scenario 1: Personal expenses in account 455

**Assessment:** Add-back of the personal portion. Possible requalification as disguised pay, with social contributions. For large amounts: acte anormal de gestion.

### Scenario 2: Overstated home office

**Assessment:** Add-back of the excess, (declared share minus actual share) times the charges. Interest in all cases; the deliberate breach surcharge only if a deliberate breach is established, which the inspector may argue where the overstatement recurs.

### Scenario 3: Pre-incorporation expenses without état des actes

**Assessment:** Establish who incurred the expense, valid company takeover, its business purpose and its expense/asset classification. The absence of an état des actes is a review flag, not by itself a sourced rule that every pre-incorporation amount must be fully added back. Add back the amount only where the applicable charge conditions fail; compute extra IS on that disallowed amount. The complete company-law takeover method is not established in this Guide.

### Scenario 4: Omitted revenue (credit balance on 411)

**Assessment:** If the inspector treats it as undeclared revenue: added to the taxable result, IS, interest, and the deliberate breach surcharge if a deliberate breach is established.

### Scenario 5: Incorrect currency conversion

**Assessment:** Recalculation of the foreign-currency charges at the correct rate. IS on the difference.

## Section 7: Statute of limitations (droit de reprise)

BOFiP BOI-CF-PGR-10 (version of 19 May 2021, https://bofip.impots.gouv.fr/bofip/937-PGP.html) and BOI-CF-PGR-10-20 (version of 3 February 2016, https://bofip.impots.gouv.fr/bofip/1396-PGP.html) set out the periods. They print them in words.

**Statute of limitations**

| Tax | Period | Source |
| --- | --- | --- |
| IR and IS (LPF art. L. 169, first paragraph) | Until the end of the third year following the year for which the tax is due | https://bofip.impots.gouv.fr/bofip/1396-PGP.html |
| Turnover taxes, VAT (LPF art. L. 176, first paragraph) | Three years (prescription triennale) | https://bofip.impots.gouv.fr/bofip/937-PGP.html |
| IFI, registration duties, land publicity tax, stamp duties (LPF art. L. 186) | Until the end of the sixth year after the taxable event, where the shortened three-year period of LPF art. L. 180 does not apply | https://bofip.impots.gouv.fr/bofip/937-PGP.html |
| Hidden activity (activité occulte) or flagrance fiscale, and the conditions of LPF art. L. 169 second, fourth and fifth paragraphs, L. 176 second paragraph and L. 174 second paragraph | Ten years | https://bofip.impots.gouv.fr/bofip/937-PGP.html |
| IR and IS where the foreign-asset or foreign-income return duties (CGI art. 123 bis, 1649 A and others) were not met (LPF art. L. 169, fourth paragraph) | From three to ten years, under the conditions on the page | https://bofip.impots.gouv.fr/bofip/1479-PGP.html |
| Fraud leading to a criminal complaint (LPF art. L. 187) | Two years beyond the ordinary period | https://bofip.impots.gouv.fr/bofip/1479-PGP.html |

- The ten-year period is not a general rule for "fraud". It applies to the hidden-activity and flagrance cases and to the listed conditions; ordinary fraud discovered in an audit extends the period only through LPF art. L. 187 after a complaint.
- A proposition de rectification interrupts the period (BOI-CF-IOR-10-50-10).
- A period that is time-barred can still be examined for its effect on an open year (for example a carried-forward deficit).
- Document retention: keep the books and supporting documents for at least as long as the longest period that can apply to the business. This skill does not state a retention period because no page read for it prints one; see `france-bookkeeping`.

## Section 8: Voluntary regularisation

If the taxpayer corrects before an audit:
- Late interest still applies at the monthly rate in the interest table. The spontaneous corrective-return half reduction requires good faith, no infringement exclusive of good faith, and payment of the resulting tax with the corrective declaration, or for a rôle by the payment deadline on the notice. An accepted public-accountant plan for the tax preserves the reduction in place of immediate/deadline payment (CGI art. 1727, V).
- No CGI art. 1729 surcharge applies to a good-faith correction.

If the taxpayer corrects during an audit:
- **LPF art. L. 62 positive method.** Start from a return filed on time and an error not exclusive of good faith. In a vérification de comptabilité or ESFP request regularisation before any proposition de rectification. For the other covered route, request within thirty days of receiving an LPF L. 10, L. 16 or L. 23 A request or a proposition de rectification. File the supplementary declaration within thirty days of the regularisation request. Pay all additional tax and reduced interest on filing, or, for a rôle, by its stated payment deadline; an accepted public-accountant payment plan for the tax preserves the reduction if immediate/deadline payment is absent. The interest payable is 70% of the ordinary amount, with its endpoint the end of the supplementary-declaration filing month. A late original return or deliberate breach fails this procedure. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037312536/2026-10-30

For significant cases (crypto, foreign income, unreported gains), refer to an avocat fiscaliste; see also `fr-crypto-tax`.

## Section 9: Audit report format

For each anomaly, the adjustment is set out as a **chef de redressement** containing:

1. **Tax concerned** (IS, VAT, other)
2. **Financial year**
3. **Legal basis** (CGI article, BOFiP reference)
4. **Nature** of the adjustment
5. **Factual finding**
6. **Legal foundation and case law**
7. **Amount** (base, additional tax, interest, surcharge, total)
8. **Risk level** (high, medium, low)
9. **Corrective recommendation**

## Section 10: Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Charge deductibility doubtful | Flag as potentially non-deductible |
| Surcharge unclear | Show interest only as the base case, and the deliberate breach rate as the risk if intent could be argued; say which |
| FEC gap found | Investigate file completeness and reliability; do not infer intentional concealment from a gap alone |
| Revenue source unclear | Establish the nature, ownership, period and tax treatment before deciding whether it is taxable revenue |
| Small-business three-month limit | Do not assume it applies until the turnover is checked against the simplified-regime admission limits for the year |

## Section 11: Key legal references

**Key legal references**

| Rule | Article |
| --- | --- |
| Taxable profit | CGI art. 38-1 |
| Net asset variation | CGI art. 38-2 |
| General deductible-charge conditions | CGI art. 39-1 |
| CCA interest cap | CGI art. 39-1-3° and 212 |
| IS rates | CGI art. 219, I |
| PME reduced rate | CGI art. 219, I-b |
| Franchise en base | CGI art. 293 B |
| Reverse charge | CGI art. 283-2 |
| DES | CGI art. 289 B, III |
| Late interest | CGI art. 1727 |
| Late filing surcharge | CGI art. 1728 |
| Surcharges | CGI art. 1729 |
| FEC fine | CGI art. 1729 D |
| FEC obligation | LPF art. L. 47 A |
| Examen de comptabilité | LPF art. L. 47 AA |
| Audit notice | LPF art. L. 47 |
| Small-business on-site length | LPF art. L. 52 and L. 52 A |
| Rectification notice and answer period | LPF art. L. 57, L. 11 and R.* 57-1 |
| Regularisation during an audit | LPF art. L. 62 |
| Departmental commission | LPF art. L. 59 A and R.* 59-1 |
| Assessment by estimate after FEC refusal | LPF art. L. 74 |
| Reassessment periods | LPF art. L. 169, L. 176, L. 180, L. 186, L. 187 |
| Home office (BOFiP) | BOI-BIC-CHG-40-20-10 |
| Pre-incorporation expenses (BOFiP) | BOI-IS-BASE-30-10 |

## The method, step by step

1. Identify the procedure from the notice: form 3927-SD (vérification de comptabilité, on site) or form 3923-EC-SD (examen de comptabilité, remote). Check it names the right to an adviser and the years and taxes covered, and check the time before the first visit (BOI-CF-PGR-20-10, https://bofip.impots.gouv.fr/bofip/236-PGP.html).
2. Prepare the FEC to the standard of LPF art. A. 47 A-1 (https://bofip.impots.gouv.fr/bofip/9028-PGP.html). Hand it over at the start of the operations for an on-site audit, or send it within fifteen days of receiving the notice for an examen de comptabilité (https://bofip.impots.gouv.fr/bofip/9026-PGP.html and https://bofip.impots.gouv.fr/bofip/236-PGP.html). For an on-site audit, the missing or non-compliant file uses the art. 1729 D I fine in the FEC table. For an examen de comptabilité, failure to transmit within fifteen days or the specified non-compliance uses the separate art. 1729 D II fixed EUR 5,000 fine, once per control; BOFiP also describes cancellation of that remote procedure and possible commencement of an on-site verification. Do not substitute the on-site 10% alternative for the remote fixed fine.
3. Test whether the three-month on-site limit applies: compare turnover with the simplified-regime admission limits for each audited year, and note the six-month case and the suspension until the FEC is handed over (LPF art. L. 52, https://bofip.impots.gouv.fr/bofip/243-PGP.html).
4. Check which years are still open, using the periods in Section 7 (https://bofip.impots.gouv.fr/bofip/937-PGP.html and https://bofip.impots.gouv.fr/bofip/1396-PGP.html).
5. Run the eight axes of Section 3 on each open year, with the corporation tax and VAT figures of that year (https://entreprendre.service-public.gouv.fr/vosdroits/F23575 and https://entreprendre.service-public.gouv.fr/vosdroits/F21746).
6. On the proposition de rectification, diary thirty days from receipt, using the clear-period and non-working-day rules in Section 1. If needed expressly request the extra thirty days in time, including the published timely-posted route and La Poste evidence there (LPF art. L. 57, https://bofip.impots.gouv.fr/bofip/5510-PGP.html).
7. Test each positive LPF art. L. 62 gate in Section 8, calculate ordinary interest to the supplementary-declaration filing month, then multiply it by 70% only for an eligible regularisation. Do not apply it to a deliberate-breach fixture (https://bofip.impots.gouv.fr/bofip/1458-PGP.html).
8. For procedural difficulties during control, use the early hierarchical/interlocution route and its procedure-specific cutoff in Section 1. For a later merits disagreement after form 3926-CFE-SD, use the separate thirty-clear-day first-level and interlocution periods there, or expressly request direct interlocution where its penalty-signature condition applies (https://bofip.impots.gouv.fr/bofip/236-PGP.html), and within thirty days on the departmental commission where it is competent (https://bofip.impots.gouv.fr/bofip/4355-PGP.html and https://bofip.impots.gouv.fr/bofip/873-PGP.html).
9. Compute each chef de redressement: additional tax, interest at the monthly rate to the applicable endpoint in Section 4: the corrective-declaration filing month for regularisation, otherwise the proposal month for the ordinary insufficiency case (https://bofip.impots.gouv.fr/bofip/1458-PGP.html) and any surcharge (https://bofip.impots.gouv.fr/bofip/4911-PGP.html), in the format of Section 9.

## Ask the client first

- Which notice did you receive (form 3927-SD or form 3923-EC-SD), on what date, and for which years and taxes?
- What was your turnover or gross receipts in each audited year, and which tax regime were you under? This decides whether the on-site time limit applies.
- Are your books kept on a computer, and can your software produce a FEC to the official standard?
- Have you already received a proposition de rectification? On what date exactly, and has the thirty-day answer period started?
- Do you hold foreign accounts or foreign income, or did any activity go undeclared? This decides whether a longer reassessment period applies.
- Do you want to correct any error yourself now, before or during the audit?

## When to refuse or refer

- Any audit where the administration alleges fraudulent manoeuvres, abuse of law or a hidden activity, or has filed or may file a criminal complaint: refer to an avocat fiscaliste.
- Examen contradictoire de la situation fiscale personnelle (ESFP) of an individual: out of scope.
- Transfer pricing adjustments: use `france-transfer-pricing` and refer.
- Large businesses above the departmental commission limits, and groups in tax consolidation: refer.
- Litigation after collection (réclamation contentieuse, the tribunal administratif): out of scope.
- Any answer to the administration, signed or sent: it must be reviewed by the expert-comptable or avocat fiscaliste first.
- A figure this skill says is not printed on a page read for it (the simplified-regime limits, the withholding rate, a retention period): do not supply one from memory.

## Sources

- BOI-CF-PGR-20-10, notice of audit, appeals and the charte: https://bofip.impots.gouv.fr/bofip/236-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-PGR-20-30, length of on-site audits: https://bofip.impots.gouv.fr/bofip/243-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-IOR-60-40-10, FEC hand-over and the fine: https://bofip.impots.gouv.fr/bofip/9026-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-IOR-60-40-20, FEC format: https://bofip.impots.gouv.fr/bofip/9028-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-IOR-10-50-10, effects of the proposition de rectification: https://bofip.impots.gouv.fr/bofip/5510-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-CMSS-20-10, competence of the departmental commission: https://bofip.impots.gouv.fr/bofip/873-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-CMSS-20-30, referral to the departmental commission: https://bofip.impots.gouv.fr/bofip/4355-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-PGR-10, reassessment periods: https://bofip.impots.gouv.fr/bofip/937-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-PGR-10-20, reassessment periods for IR and IS: https://bofip.impots.gouv.fr/bofip/1396-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-PGR-10-50, extensions of the reassessment period: https://bofip.impots.gouv.fr/bofip/1479-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-INF-10-10-20, late payment interest: https://bofip.impots.gouv.fr/bofip/1458-PGP.html Selected cited scope read 2026-10-29.
- BOI-CF-INF-10-20-30-10, surcharges: https://bofip.impots.gouv.fr/bofip/4911-PGP.html Selected cited scope read 2026-10-29.
- BOI-BIC-CHG-50-50-30, current account interest reference rate: https://bofip.impots.gouv.fr/bofip/5505-PGP.html Selected cited scope read 2026-10-29.
- BOI-BIC-CHG-20-30-10, small equipment expensed: https://bofip.impots.gouv.fr/bofip/2109-PGP.html Selected cited scope read 2026-10-29.
- Impôt sur les sociétés, taux: https://entreprendre.service-public.gouv.fr/vosdroits/F23575 Selected cited scope read 2026-10-29.
- Franchise en base de TVA: https://entreprendre.service-public.gouv.fr/vosdroits/F21746 Selected cited scope read 2026-10-29.
- Notice 3310-NOT-CA3-SD, 2026 (DES): https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf Selected cited scope read 2026-10-29.
- Charte des droits et obligations du contribuable vérifié: https://www.impots.gouv.fr/charte-des-droits-et-obligations-du-contribuable-verifie Selected cited scope read 2026-10-29.
- Selected current statutory rate, twelve-month reduced slice and tax exclusion: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562/2026-10-29 and https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373444/2026-10-29
- Current abuse-of-law 80%/40% conditions: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904/2026-10-29
- General charge conditions and mixed expenses: https://bofip.impots.gouv.fr/bofip/3848-PGP.html and https://bofip.impots.gouv.fr/bofip/468-PGP.html Selected cited scope read 2026-10-29.
- Remote-examination procedure and separate FEC fine: https://bofip.impots.gouv.fr/bofip/3750-PGP.html Selected cited scope read 2026-10-29.

Selected-source update, 29 October 2026: the figure ledger records actual native-LF reads separately from acquired bodies and earlier author reading. The complete current paid-up-capital/market-interest interaction, corporate takeover formalities, detailed foreign-currency rules and every underlying accounting-code instruction are not derived here. Practical review grids do not establish those missing legal methods or an automatic tax result.

Selected repair reads, 31 October 2026: the retained official BOFiP clauses above supply both hierarchical routes, the remote no-adjustment endpoint, timely-posted extension practice, cumulative DES conditions and the corrective-declaration interest endpoint. The rendered current LPF L. 62 supplies the full regularisation gates, and CGI art. 219 I-b supplies continuous ownership and qualifying corporate-owner conditions. Actual selected reading is recorded separately from acquisition and from prior full-pack review; no new whole-country verdict is made.

## Footer

*OpenAccountants: open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest skills: **openaccountants.com** | Report errors: **github.com/openaccountants/openaccountants***

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
