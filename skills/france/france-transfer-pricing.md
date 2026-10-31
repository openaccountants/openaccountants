---
name: france-transfer-pricing
description: Use this skill whenever asked about France transfer pricing rules, documentation requirements, or prix de transfert compliance. Trigger on phrases like "transfer pricing France", "French TP documentation", "prix de transfert", "master file France", "local file France", "CbCR France", "APA France", "Article L.13 AA", "Form 2257-SD", or any question about intercompany pricing for French entities.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-19
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: transfer pricing (prix de transfert)

This skill covers the French transfer pricing duties of a company that deals with related entities abroad: the arm's length rule of article 57 of the Code général des impôts (CGI), the documentation file under article L. 13 AA of the Livre des procédures fiscales (LPF), the yearly declaration on form 2257-SD, the country-by-country report on form 2258-SD, the fines for each, the information request of article L. 13 B LPF, and advance pricing agreements. Figures are for tax year 2026. Transfer pricing figures attach to the accounting year (exercice), not to an income year, and the documentation threshold and the higher minimum fine below apply to accounting years opened on or after 1 January 2024 and are the rules in force on 19 October 2026. The one change this year is on intra-group interest (Section 8) and it applies to accounting years closed on or after 31 December 2025, so to the 2025 calendar-year accounts as well. Every figure below was read on an official page between 19 September and 19 October 2026; each page's own date is given where it matters.

## Section 1: Quick reference

**Quick reference fields**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Tax authority | Direction générale des Finances publiques (DGFiP) |
| Arm's length rule | Article 57 CGI |
| Documentation file (master file and local file) | Article L. 13 AA LPF; enhanced file for non-cooperative states under article L. 13 AB LPF |
| Information request during an audit (any company; BOFiP routes companies outside L. 13 AA to it) | Article L. 13 B LPF |
| Yearly transfer pricing declaration | Form 2257-SD, article 223 quinquies B CGI |
| Country-by-country report | Form 2258-SD, article 223 quinquies C CGI |
| Fines | Article 1735 ter CGI (documentation), article 1729 B CGI (2257-SD), article 1729 F CGI (2258-SD), article 1735 II CGI (L. 13 B request) |
| Advance pricing agreement | Article L. 80 B 7° LPF, handled by bureau SJCF-4B of the DGFiP |
| Documentation standard | OECD BEPS Action 13 master file and local file |
| Documentation language | In principle French; the administration may ask for a French translation of documents in another language |
| Currency | EUR |
| Thresholds and fines | see the tables in Sections 2 and 6; never assume a threshold from the group's size alone |

**Who is a related ("associated") enterprise**

The documentation file and form 2257-SD both use the related-party test of article 39, 12 CGI. BOFiP states that a dependency link exists where one enterprise holds, directly or through an intermediary, the majority of the other's share capital or in fact exercises decision-making power in it, or where both are under the control of the same third enterprise in those conditions. Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html (BOI-BIC-BASE-80-10-40, § 60). A transaction is any operation that can affect net profit under article 38, 1 or 2 CGI, and dealings between a head office and its branches in other tax jurisdictions must also be described.

## Section 2: Documentation requirements

### 2.1 Who must hold the documentation file (article L. 13 AA LPF)

A legal person established in France is in scope where ANY ONE of the four tests below is met (they are alternatives, joined by "ou"). A foreign company with a French permanent establishment counts as established in France: the turnover or assets test is met if met by the French establishment OR by the foreign company; the "holds more than half" test is judged at the French establishment; the "is more than half held" test is judged at the foreign company.

1. Its annual turnover excluding VAT, OR its gross assets on the balance sheet, is at least the threshold in the table below.
2. At the close of the accounting year it holds, directly or indirectly, more than half of the capital or voting rights of a legal entity that meets test 1.
3. More than half of its capital or voting rights is held, directly or indirectly, at the close of the accounting year by a legal entity that meets test 1.
4. It belongs to a French tax group (article 223 A or 223 A bis CGI) that includes at least one legal person meeting one of the first three tests.

The tests are applied by the administration for each accounting year named in the audit notice. A company outside all four tests is not free of transfer pricing scrutiny: BOFiP says it is subject to the article L. 13 B request (Section 6.3), which the administration can address to any audited company liable to income tax or corporation tax.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| Turnover or gross assets threshold, accounting years opened on or after 1 January 2024 | EUR 150 million | "est supérieur ou égal à 150 millions d’euros" (BOI-BIC-BASE-80-10-40, version in force from 10/12/2025) |
| Previous threshold, earlier accounting years | EUR 400 million | "a abaissé de 400 millions d’euros à 150 millions d’euros ce seuil pour les exercices ouverts à compter du 1 er janvier 2024" |
| Local file: controlled transactions described | aggregated by category, more than EUR 100,000 for the year | "dont le montant, agrégé par catégorie, excède 100 000 € au titre de l’exercice" |

The value EUR 150 million is the pack value `fr.transfer-pricing.documentation.threshold`.

### 2.2 What the file contains

The file has two parts, both following the OECD standard: a master file (fichier principal) giving an overview of the group's activities, its global transfer pricing policy and how profits are allocated worldwide, and a local file (fichier local) giving precise information on the intra-group transactions of the entity producing the documentation. The master file content is set by article L. 13 AA and article R. 13 AA-1 LPF in five categories: organisational structure; the group's business lines; its intangibles; its intercompany financial activities; and its financial and tax position. The local file describes the controlled transactions above the category amount in the table above; a company may add categories or sub-categories below that amount. Amounts come from the company's own statutory accounts, with no netting of income against charges, nor of acquisitions against disposals of assets. Where a company deals with an associated enterprise in a non-cooperative state or territory (ETNC, article 238-0 A CGI), article L. 13 AB LPF adds a further file for each beneficiary of the transfers, including the documents required of a company liable to corporation tax. Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html

### 2.3 Form and timing of the file

The file is held electronically, in a format that allows the documents to be exchanged and read; a PDF made by scanning (".pdf image") is not accepted, and data tables must allow the administration to check calculations, sort and classify. It must be at the administration's disposal on the date the tax audit (vérification de comptabilité or examen de comptabilité) begins, as shown on the audit notice. It does not replace the evidence for each transaction. BOFiP adds that, as a rule, the master file, the local file and the country-by-country report should be reviewed and updated every year. Comparables studies "doivent privilégier les informations les plus récentes disponibles à la date de facturation"; where the conditions of the activity are unchanged, BOFiP accepts that the studies are updated every three years, but the financial data from the comparables must still be updated every year (BOI-BIC-BASE-80-10-40, § 580). Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html (§ 560 to 580).

If the file is missing or partial, the administration sends a formal notice (mise en demeure) by registered letter with acknowledgement of receipt or by hand, naming the documents expected and the fines. The company then has thirty days to produce or complete it. On a written, reasoned request stating the length wanted, the company may obtain an extension "qui, dans tous les cas, ne pourra excéder au total deux mois". The file counts as complete only where it lets the administration assess the whole transfer pricing policy against the arm's length principle and the OECD standards; a file that cites general principles (arm's length, recognised OECD methods) without showing how they apply to the company may be treated as partial. Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html (§ 590 to 630).

### 2.4 Yearly transfer pricing declaration (form 2257-SD, article 223 quinquies B CGI)

Form 2257-SD is a lighter version of the documentation file, filed every year outside any audit. A legal person established in France must file it where ANY ONE of these tests is met: its annual turnover excluding VAT OR its gross balance sheet assets is at least the threshold in the table below; it holds at year end, directly or indirectly, more than half of the capital or voting rights of an entity meeting that test; more than half of its capital or voting rights is held at year end by such an entity; or it belongs to a French tax group (article 223 A or 223 A bis CGI) that includes a legal person meeting one of those tests. The same permanent establishment rules as in 2.1 apply.

A company in scope need not file where it has no transactions at all with related entities established abroad, OR where its transactions with them are below the per-type amount in the table below. The test is made company by company, never on the consolidated group, even where the head of a French tax group files for its members.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11462-PGP.html |
| Turnover or gross assets threshold | EUR 50 million | "est supérieur ou égal à 50 millions d'euros" (BOI-BIC-BASE-80-10-30, version in force from 18/07/2018) |
| Exemption: transactions with related foreign entities below, per type of transaction | EUR 100,000 | "dont le montant est inférieur à 100 000 € par nature de transaction" |
| Amounts listed on the form, per type of flow | aggregated amount above EUR 100,000 | "le montant agrégé des produits, charges, acquisitions et cessions d'actifs supérieurs à 100 000 €, par nature de flux" |

The values EUR 50 million and EUR 100,000 (exemption) are the pack values `fr.transfer-pricing.declaration-2257.threshold` and `fr.transfer-pricing.declaration-2257.de-minimis`. The form threshold is lower than the documentation threshold in 2.1: a company can owe form 2257-SD without owing the full documentation file.

Content: general information on the group (main activities, main intangibles related to the declaring company and the state where their owner is located, the group's transfer pricing policy and changes during the year) and specific information on the declaring company (its activity and changes, a summary of transactions with associated enterprises by type and amount with the states concerned, and the main pricing method applied to each type of transaction, judged by the amount of transactions). Filing: electronically on form 2257-SD (CERFA n° 15221), within six months after the deadline for the company's results declaration. For a company whose year is the calendar year, BOFiP's own example puts the results return in early May of the following year and form 2257-SD six months later, in early November. The head of a French tax group files one form for each member that is actually liable. Source: https://bofip.impots.gouv.fr/bofip/11462-PGP.html (§ 1 to 170).

### 2.5 Country-by-country report (form 2258-SD, article 223 quinquies C CGI)

The report is due, for accounting years opened from 1 January 2016, from (a) groups established in France that draw up consolidated accounts, hold or control companies or branches outside France, are not held by a French or foreign company already liable, and reach the consolidated turnover threshold below in the year BEFORE the year reported; and (b) a French company belonging to a foreign group meeting those criteria, where the group has designated it, or where it cannot show that another French or foreign entity has been designated (for example a French subsidiary of a group whose state has no country-by-country reporting). One report covers all entities of the group. It is filed by the ultimate parent or by a designated surrogate entity. The company liable or designated also ticks the matching box on its results return 2065-SD.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/sites/default/files/formulaires/2258-sd/2025/2258-sd_4927.pdf |
| Consolidated turnover excluding VAT, previous accounting year | at least EUR 750 million | "un chiffre d'affaires annuel hors taxes consolidé supérieur ou égal à 750 millions d'euros" (form 2258-SD, 2025 edition) |
| Fine for not filing | up to EUR 100,000 | "une amende qui ne peut excéder 100 000 euros (article 1729 F du CGI)" |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/la-declaration-pays-par-pays |
| Same threshold as printed on the administration's explanatory page | more than EUR 750 million | "un chiffre d'affaires annuel hors taxes consolidé supérieur à 750 millions d'euros" (page modified 24/05/2022) |

The two official pages differ on a group exactly at the threshold: the 2025 form says "supérieur ou égal" (at least), the older explanatory page says "supérieur" (more than). A group at exactly that turnover is referred (see "When to refuse or refer"). Filing: electronically, within twelve months after the close of the group's accounting year, as stated on the 2025 form (https://www.impots.gouv.fr/sites/default/files/formulaires/2258-sd/2025/2258-sd_4927.pdf). The information is passed to the partner states where the group has at least one entity.

## Section 3: Arm's length standard

### 3.1 Definition

- **Arm's length principle (article 57 CGI).** Article 57 CGI lets the administration check that the profit a company declares in France matches the activities it carries out in France under the arm's length principle, and correct the declared results where profits have been indirectly transferred abroad, either by raising or lowering purchase or sale prices or by any other means. BOFiP states that this text conforms with article 9 of the OECD Model Tax Convention. Prices set arbitrarily, without a defined method applied consistently and capable of justification, carry a higher risk of reassessment. Source: https://bofip.impots.gouv.fr/bofip/9389-PGP.html (BOI-BIC-BASE-80-10-20, § 1 and 10).

### 3.2 Methods named on the official form

Form 2257-SD asks the company to tick, for each type of transaction, the method applied. The form's columns are:

| Method (as named on form 2257-SD) | English name |
| --- | --- |
| Prix comparable sur marché libre | Comparable uncontrolled price (CUP) |
| Prix de revente | Resale price method |
| Coût majoré | Cost plus method |
| Méthode transactionnelle de la marge nette | Transactional net margin method (TNMM) |
| Méthode du partage de bénéfice | Profit split method |
| Autres Méthodes | Other methods |

Source: https://www.impots.gouv.fr/sites/default/files/formulaires/2257-sd/2017/2257-sd_1338.pdf (form 2257-SD, 2017 edition, the latest edition found on impots.gouv.fr).

### 3.3 Choice of method

- **Choice of method.** No allowed page sets a statutory order of methods. BOFiP says the OECD Transfer Pricing Guidelines' recommendations for documentation apply to the L. 13 AA file (§ 50, https://bofip.impots.gouv.fr/bofip/11463-PGP.html). On form 2257-SD only one method is ticked per type of transaction: the one applied to the larger share of the amount (§ 160, https://bofip.impots.gouv.fr/bofip/11462-PGP.html). A mere disagreement over which method is most appropriate does not justify the documentation fine (Section 6.1).

### 3.4 The documented method binds the company (accounting years opened on or after 1 January 2024)

- **Enforceability of the documentation.** For accounting years opened on or after 1 January 2024, where the transfer pricing method actually applied departs from the method documented in the L. 13 AA or L. 13 AB file, and there is a gap between the result shown and the result that following the documentation would have produced, that gap is deemed (last paragraph of article 57 CGI) to be profit indirectly transferred, unless the company shows there was no transfer. The burden of proof is on the company. Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html (§ 585).

## Section 4: Filing obligations

**Filing obligations**

| Obligation | Who | When | Source |
| --- | --- | --- | --- |
| Master file and local file (L. 13 AA LPF) | Entities in 2.1 | Held, not filed; available from the start of an audit | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| Form 2257-SD (223 quinquies B CGI) | Entities in 2.4, unless an exemption in 2.4 applies | Yearly, electronically, within six months after the results return deadline | https://bofip.impots.gouv.fr/bofip/11462-PGP.html |
| Form 2258-SD (223 quinquies C CGI) | Groups and French entities in 2.5 | Yearly, electronically, within twelve months after the group's year end | https://www.impots.gouv.fr/sites/default/files/formulaires/2258-sd/2025/2258-sd_4927.pdf |
| Results return 2065-SD | Every company liable to corporation tax | The country-by-country boxes are ticked on it where 2.5 applies | https://www.impots.gouv.fr/la-declaration-pays-par-pays |
| Answer to an L. 13 B request | Any audited company liable to income tax or corporation tax, including those outside 2.1 | At least two months from receipt (Section 6.3) | https://bofip.impots.gouv.fr/bofip/4332-PGP.html |

The corporation tax return itself and its date are in `fr-business-accounting` and `france-financial-statements`.

## Section 5: Deadlines

**Deadlines**

| Item | Deadline | Source |
| --- | --- | --- |
| Documentation file | Available on the date the audit begins, as shown on the audit notice | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| Answer to a formal notice to produce or complete the file | Thirty days; extension on a written reasoned request, "ne pourra excéder au total deux mois" | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| Form 2257-SD | Six months after the deadline for the results return; for a calendar year, early November of the following year in BOFiP's example | https://bofip.impots.gouv.fr/bofip/11462-PGP.html |
| Form 2258-SD | Twelve months after the close of the group's accounting year | https://www.impots.gouv.fr/sites/default/files/formulaires/2258-sd/2025/2258-sd_4927.pdf |
| Answer to an L. 13 B request | Not less than two months from receipt; extension on a written reasoned request, up to three months in total | https://bofip.impots.gouv.fr/bofip/4332-PGP.html |
| Bilateral advance pricing agreement request | At least six months before the opening of the first accounting year covered | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Renewal of an advance pricing agreement | At least six months before the agreement expires | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |

## Section 6: Penalties

### 6.1 Documentation not produced after a formal notice (article 1735 ter CGI)

Where the company does not produce the file, or produces only part of it, within thirty days of receiving the formal notice (or within the extended period), the fine CAN REACH the higher of the two amounts in the table below; the rate actually applied depends on how serious the failure is (completeness, accuracy, effect on the administration's ability to judge the policy). The maximum is applied in particular where there is no documentation at all, where gaps are serious or the content is misleading, or where the breach repeats over successive audits. Whatever the result, the fine cannot be lower than the minimum below. It is charged for each accounting year covered by the audit. It can apply even where no reassessment is made. It does NOT apply where the only dispute is the transfer pricing policy or method itself. Dividends are not a transaction for the base, except in abuse of law. The fine is not a "serious penalty" under the EU Arbitration Convention, so it does not shut out mutual agreement or arbitration procedures, and it is recalculated on the adjustments confirmed by those procedures. The decision to apply it needs the sign-off of an officer of at least inspecteur divisionnaire rank.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/10389-PGP.html |
| Share of the transactions left undocumented after the notice | 0.5% | "0,5 % du montant des transactions concernées par les documents ou compléments qui n’ont pas été mis à disposition" |
| Share of the article 57 adjustments on those transactions | 5% | "5 % des rectifications du résultat fondées sur l’ article 57 du CGI" |
| Minimum fine, from 1 January 2024 | EUR 50,000 | "Le montant de l’amende ne peut être inférieur à 50 000 €." |
| Minimum fine before 1 January 2024 | EUR 10,000 | "le montant minimal de cette amende de 10 000 € à 50 000 €" |

The share 0.5% is the pack value `fr.transfer-pricing.penalty.share-of-transactions`.

**Worked examples printed by BOFiP (hypothetical amounts, BOI-CF-INF-20-10-40 § 100)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/10389-PGP.html |
| Example 2: brand royalty not booked and not documented, arm's length value and adjustment | EUR 2,000,000 | "0,5 % x 2 000 000 € = 10 000 €" |
| Example 2: fine on the transactions test | EUR 10,000 | "0,5 % x 2 000 000 € = 10 000 €" |
| Example 2: fine on the adjustments test, the higher, so the maximum | EUR 100,000 | "5 % x 2 000 000 € = 100 000 €" |
| Example 4: service charge booked | EUR 1,000,000 | "1 000 000 € - 600 000 €) = 2 000 €" |
| Example 4: adjustment | EUR 600,000 | "5 % x 600 000 € = 30 000 €" |
| Example 4: fine on the transactions test | EUR 2,000 | "1 000 000 € - 600 000 €) = 2 000 €" |
| Example 4: fine on the adjustments test | EUR 30,000 | "5 % x 600 000 € = 30 000 €" |
| Example 4: fine actually due, because the minimum applies | EUR 50,000 | "celle-ci ne saurait être inférieure à 50 000 €" |

In example 4 the higher of the two tests is below the minimum in the table above, so the minimum is charged.

### 6.2 Form 2257-SD late, missing or wrong (article 1729 B CGI)

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/10389-PGP.html |
| Form not filed within the time limit | EUR 150 | "entraîne l’application d’une amende de 150 €" |
| Each omission or inaccuracy, save force majeure | EUR 15 | "une amende de 15 € par omission ou inexactitude" |
| Total of the omission fines, floor | EUR 60 | "ne puisse être inférieur à 60 €" |
| Total of the omission fines, cap | EUR 10,000 | "ni supérieur à 10 000 €" |

These four values are the pack values `fr.transfer-pricing.2257.late-filing-fine`, `fr.transfer-pricing.2257.omission-fine`, `fr.transfer-pricing.2257.omission-fine.floor` and `fr.transfer-pricing.2257.omission-fine.cap`. None of these fines applies to a first breach in the current calendar year and the three previous years, where the company has put it right either of its own accord or within thirty days of a request from the administration (§ 160, https://bofip.impots.gouv.fr/bofip/10389-PGP.html)

### 6.3 Information request during an audit (article L. 13 B LPF, fine under article 1735 II CGI)

A request under article L. 13 B can be made only during an audit (vérification de comptabilité or examen de comptabilité), only where the administration has gathered evidence giving rise to a presumption that the company made an indirect transfer of profits, and only on four areas listed exhaustively. It concerns "toutes les entreprises, quelle que soit leur forme juridique, imposables en France à l’impôt sur le revenu ou à l’impôt sur les sociétés" (BOI-CF-IOR-60-50, § 50); companies outside L. 13 AA are routed to it by BOI-BIC-BASE-80-10-40 § 40. The answer period is not less than two months, extendable on request up to three months in total. If the company does not answer, or answers insufficiently after a formal notice, the fixed fine below applies for each accounting year covered by the request, even where there is no reassessment, and on top of the penalties on any transfer pricing reassessment.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4332-PGP.html |
| Fixed fine per accounting year covered by the request | EUR 10,000 | "une amende fiscale fixe de 10 000 € pour chaque exercice visé par la demande initiale" (BOI-CF-IOR-60-50, version in force from 10/12/2025) |

### 6.4 Surcharges on the tax from a transfer pricing reassessment (article 1729 CGI)

A transfer pricing reassessment under article 57 bears the general surcharges on the extra tax, where their conditions are met.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4911-PGP.html |
| Deliberate breach (manquement délibéré) | 40% | "la majoration de 40 % pour manquement délibéré prévue par l’article 1729 du CGI" |
| Abuse of law where the taxpayer is its main beneficiary, fraudulent manoeuvres, or concealment of the price in a contract | 80% | "80 % sur les droits résultant des rappels (1729)" |

Both are pack values (`fr.penalty.deliberate-breach`, `fr.penalty.fraud`). The surcharge regime and late-payment interest in full are in `fr-tax-audit`.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1458-PGP.html |
| Late-payment interest (intérêt de retard, article 1727 CGI), per month | 0.2% | "taux de l'intérêt de retard de 0,2 % par mois" |

The rate is the pack value `fr.penalty.late-interest.monthly`.

### 6.5 Country-by-country report not filed (article 1729 F CGI)

The fine for not filing form 2258-SD is capped at the amount in the table in Section 2.5.

## Section 7: Advance pricing agreements (APA)

**Advance pricing agreements (accord préalable de prix, APP)**

| Item | Detail | Source |
| --- | --- | --- |
| Legal basis | Article L. 80 B 7° LPF; the guarantee of article L. 80 A LPF applies once the agreement on the method is concluded | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| What it covers | The METHOD for future intra-group transactions, not the prices themselves | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Bilateral agreement | Only with states whose tax treaty with France has a clause equivalent to article 25, paragraph 3, of the OECD Model | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Unilateral agreement and simplified procedure for SMEs | BOI-BIC-BASE-80-10-20 (version of 18/07/2018) says a unilateral agreement is possible "Sous certaines conditions" and a simplified procedure is open to SMEs; the current unilateral and SME pages were not read for this skill | https://bofip.impots.gouv.fr/bofip/9389-PGP.html |
| Where to apply | Bureau SJCF-4B (Prévention et résolution des différends internationaux), DGFiP, by electronic means | https://www.impots.gouv.fr/professionnel/questions/ma-societe-situee-en-france-fait-partie-dun-groupe-international-comment |
| When to apply | At least six months before the opening of the first accounting year covered | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Duration | Set in the negotiation, generally five years | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Roll-back to past or current years | On express request, at the bureau's discretion, no more than three years; in a bilateral agreement only if the other state allows it | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Annual report | Required; failing to produce it within thirty days of a formal notice terminates the agreement from the year for which it was not filed | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Renewal | On request at least six months before expiry; otherwise the agreement ends at its term | https://bofip.impots.gouv.fr/bofip/1053-PGP.html |
| Mutual agreement and arbitration | Available under bilateral tax treaties where a transfer pricing adjustment causes double taxation | https://bofip.impots.gouv.fr/bofip/9389-PGP.html |

No allowed page states an application fee or a typical processing time; this skill gives neither.

## Section 8: Safe harbours and interest

- **General principle.** No allowed page sets a French transfer pricing safe harbour (no statutory margin for low-value services, no safe interest rate). Treat every controlled transaction as needing arm's length support.

**Safe harbours table**

| Area | Status | Source |
| --- | --- | --- |
| Low-value intra-group services | No French safe harbour on an allowed page; price at arm's length and document | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| Small transactions, local file | Categories at or below the local file amount in Section 2.1 need not be described, but the arm's length rule of article 57 CGI still applies to them | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| Small transactions, form 2257-SD | Exemption below the per-type amount in Section 2.4 | https://bofip.impots.gouv.fr/bofip/11462-PGP.html |
| Interest paid to related lenders | Article 212, I-a CGI limit (8.1) | https://bofip.impots.gouv.fr/bofip/8420-PGP.html |
| Net financial charges | Article 212 bis CGI cap (8.1) | https://bofip.impots.gouv.fr/bofip/11787-PGP.html |

### 8.1 Interest limits that sit next to transfer pricing (articles 212 and 212 bis CGI)

The limits apply in this order: first the interest-rate limits (article 212, I-a CGI for associated or related lenders, or article 39, 1-3° CGI for shareholders' current accounts), then the general cap on net financial charges of article 212 bis CGI, each applied net of what the earlier one already added back (BOI-IS-BASE-35-10, version in force from 15/07/2026, § 70 and 80, https://bofip.impots.gouv.fr/bofip/8420-PGP.html)

- **Interest rate (article 212, I-a CGI).** Interest paid to associated enterprises or to enterprises related under article 39, 12 CGI is deductible up to the rate of article 39, 1-3° CGI or, if higher, the market rate the company could have obtained from an independent lender in similar conditions. **2026 change:** the 2026 finance law (loi n° 2026-103 du 19 février 2026, art. 14) extended the market-rate option to interest paid to enterprises that are associated but NOT related under article 39, 12, for accounting years closed on or after 31 December 2025. Source: https://bofip.impots.gouv.fr/bofip/8420-PGP.html (§ 30).
- **General cap (article 212 bis CGI).** Net financial charges are deductible up to the HIGHER of three million euros (per twelve-month accounting year, adjusted pro rata for a longer or shorter year) and the share of tax EBITDA in the table below. Tax EBITDA is built on the tax result and is not accounting EBITDA. BOFiP's worked example on BOI-IS-BASE-35-10 (https://bofip.impots.gouv.fr/bofip/8420-PGP.html) first checks whether the company is under-capitalised, comparing its debts owed to related enterprises with its equity against a ratio of 1.5, before applying the cap; the under-capitalisation rule itself is outside this skill.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11787-PGP.html |
| Second cap: share of tax EBITDA | 30% | "30 % de son résultat fiscal avant impôts, intérêts, dépréciations et amortissements" (BOI-IS-BASE-35-40-10-20, version of 13/05/2020) |

The under-capitalisation rules and the group safeguard clause are outside this skill: see "When to refuse or refer".

## Section 9: Recent developments

**Recent developments**

| Date | Development | Source |
| --- | --- | --- |
| Accounting years opened on or after 1 January 2024 | Documentation threshold in Section 2.1 lowered (2024 finance law, loi n° 2023-1322, art. 116) | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| From 1 January 2024 | Minimum documentation fine raised (Section 6.1) | https://bofip.impots.gouv.fr/bofip/10389-PGP.html |
| Accounting years opened on or after 1 January 2024 | Documented method binds the company; a gap is deemed a transfer of profits (Section 3.4) | https://bofip.impots.gouv.fr/bofip/11463-PGP.html |
| 10 December 2025 | BOFiP published its comments on the 2024 measures (BOI-BIC-BASE-80-10-40 and BOI-CF-INF-20-10-40) | https://bofip.impots.gouv.fr/bofip/10389-PGP.html |
| Accounting years closed on or after 31 December 2025 | Market-rate interest option extended to associated but not related lenders (2026 finance law, art. 14; BOFiP of 15 July 2026) | https://bofip.impots.gouv.fr/bofip/8420-PGP.html |
| Pillar Two | Groups in the global minimum tax file an information return on form 2259-SD (article 223 WW CGI); out of scope here | https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/impot_mondial_15pc_pilier2/gu-2259-sd---2025-v1.pdf |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/impot_mondial_15pc_pilier2/gu-2259-sd---2025-v1.pdf |
| Pillar Two scope: consolidated turnover in at least two of the four previous accounting years | EUR 750 million | "atteint ou dépasse 750 millions d’euros sur au moins deux des quatre exercices précédant l’exercice concerné" |

The Pillar Two test is not the country-by-country test in Section 2.5: it looks at two of the four previous years, not the single previous year. The Pillar Two return is due within fifteen months of the year end, or eighteen months for the first year in scope (same guide).

## Section 10: Interaction with other skills

**Interaction with other skills**

| Related skill | Interaction |
| --- | --- |
| `fr-business-accounting` | Corporation tax rate, results return 2065-SD and its deadline; a transfer pricing adjustment under article 57 CGI changes the corporation tax base |
| `france-financial-statements` | Annual accounts; related-party information in the accounts |
| `france-bookkeeping` | Accounting records that support the documentation; the statutory-account amounts used for the thresholds in 2.1 and 2.4 |
| `fr-tax-audit` | Audit procedure, surcharges, late-payment interest and taxpayer rights during a transfer pricing audit |
| `france-vat-return` | VAT on intra-group invoices; a transfer pricing adjustment may also raise VAT or customs valuation questions, which this skill does not answer |

## The method, step by step

1. **Map the related parties.** List every entity abroad linked to the French company under article 39, 12 CGI (majority of capital, de facto control, or common control), and every foreign branch. Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html
2. **Test the documentation file (article L. 13 AA LPF).** Apply the four alternative tests in Section 2.1 for each accounting year, using turnover excluding VAT and gross balance sheet assets, and the year-end holdings. Use the threshold that matches the year (opened on or after 1 January 2024, or earlier). Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html
3. **Test form 2257-SD (article 223 quinquies B CGI).** Apply the tests in Section 2.4, then the exemptions (no foreign related-party transactions, or all below the per-type amount, measured per company). Source: https://bofip.impots.gouv.fr/bofip/11462-PGP.html
4. **Test the country-by-country report (article 223 quinquies C CGI).** Check the group's consolidated turnover for the year before, whether a parent or surrogate already files, and whether the French entity has been designated. Tick the boxes on form 2065-SD. Source: https://www.impots.gouv.fr/sites/default/files/formulaires/2258-sd/2025/2258-sd_4927.pdf and https://www.impots.gouv.fr/la-declaration-pays-par-pays
5. **Price each controlled transaction at arm's length (article 57 CGI).** Choose and apply a method from the list in Section 3.2 consistently, and keep the evidence for each transaction. For years opened on or after 1 January 2024, make sure the method actually applied is the one documented (Section 3.4). Source: https://bofip.impots.gouv.fr/bofip/9389-PGP.html and https://bofip.impots.gouv.fr/bofip/11463-PGP.html
6. **Check intra-group interest.** Apply the article 212, I-a rate limit, then the article 212 bis cap (Section 8.1). Source: https://bofip.impots.gouv.fr/bofip/8420-PGP.html
7. **Build or update the file.** Master file in its five categories and local file for each category above the amount in Section 2.1, in French, in a readable electronic format, reviewed every year, ready on the first day of any audit. Add the L. 13 AB file for any ETNC counterparty. Source: https://bofip.impots.gouv.fr/bofip/11463-PGP.html
8. **File the yearly forms.** Form 2257-SD within six months after the results return deadline; form 2258-SD within twelve months after the group's year end. Source: https://bofip.impots.gouv.fr/bofip/11462-PGP.html and https://www.impots.gouv.fr/sites/default/files/formulaires/2258-sd/2025/2258-sd_4927.pdf
9. **In an audit.** Produce the file at the start; answer a formal notice within thirty days or ask in writing for an extension; answer any L. 13 B request within the period it sets. Measure exposure with the tables in Section 6. Source: https://bofip.impots.gouv.fr/bofip/10389-PGP.html and https://bofip.impots.gouv.fr/bofip/4332-PGP.html
10. **Consider certainty.** For a stable, material flow with a treaty partner, weigh a bilateral advance pricing agreement, applied for at least six months before the first year covered (Section 7). Source: https://bofip.impots.gouv.fr/bofip/1053-PGP.html

## Ask the client first

- What were the French entity's turnover excluding VAT and gross balance sheet assets for each accounting year in question, and when did each year open? (Decides the documentation threshold and which version applies.)
- Who holds the French entity, and what does it hold, at each year end: does any entity above or below it, or in its French tax group, meet the turnover or assets test? (The holding tests bring small entities into scope.)
- Which transactions with related entities abroad, by type, and for what amounts, including dealings with foreign branches? Are any counterparties in a non-cooperative state? (Decides the 2257-SD exemption, the local file content and the L. 13 AB file.)
- What was the group's consolidated turnover in the previous year, who is the ultimate parent, and has another entity been designated to file the country-by-country report? (Decides form 2258-SD.)
- Is an audit under way, has a formal notice or an L. 13 B request been received, and on what date? (Starts the thirty-day or two-month clock.)
- Does the method applied in the books match the method in the documentation for each year opened on or after 1 January 2024? (A gap is deemed a transfer of profits.)

## When to refuse or refer

- A group whose consolidated turnover is exactly at the country-by-country threshold: the 2025 form and the explanatory page word the test differently (Section 2.5). Refer.
- Pillar Two (global minimum tax, form 2259-SD), under-capitalisation and the group safeguard clause of article 212 bis CGI: not covered. Refer.
- Building the benchmark (comparables search, interquartile ranges) or valuing intangibles or a business restructuring: this skill states the duties, not the economics. Refer to a transfer pricing specialist.
- Negotiating an advance pricing agreement, a mutual agreement procedure or an arbitration, or contesting a fine or a reassessment: refer.
- Unilateral advance pricing agreements and the SME simplified procedure: the current BOFiP pages were not read (Section 7). Refer.
- Customs valuation of related-party imports and the VAT effect of year-end transfer pricing adjustments: not covered. Refer.
- Any accounting year opened before 1 January 2024 where the old threshold or the old minimum fine matters: check the version of BOFiP in force for that year before advising.

## Sources

- BOI-BIC-BASE-80-10-40, documentation obligation (version in force from 10/12/2025): https://bofip.impots.gouv.fr/bofip/11463-PGP.html
- BOI-BIC-BASE-80-10-30, form 2257-SD declaration (version in force from 18/07/2018): https://bofip.impots.gouv.fr/bofip/11462-PGP.html
- BOI-CF-INF-20-10-40, fines for the documentation and the declaration (version in force from 10/12/2025): https://bofip.impots.gouv.fr/bofip/10389-PGP.html
- BOI-BIC-BASE-80-10-20, audit policy (version in force from 18/07/2018): https://bofip.impots.gouv.fr/bofip/9389-PGP.html
- BOI-CF-IOR-60-50, article L. 13 B request (version in force from 10/12/2025): https://bofip.impots.gouv.fr/bofip/4332-PGP.html
- BOI-SJ-RES-20-10, bilateral advance pricing agreement (version in force from 15/04/2026): https://bofip.impots.gouv.fr/bofip/1053-PGP.html
- BOI-IS-BASE-35-10, order of the interest limits (version in force from 15/07/2026): https://bofip.impots.gouv.fr/bofip/8420-PGP.html
- BOI-IS-BASE-35-40-10-20, cap on net financial charges (version of 13/05/2020): https://bofip.impots.gouv.fr/bofip/11787-PGP.html
- Surcharges, article 1729 CGI: https://bofip.impots.gouv.fr/bofip/4911-PGP.html
- Late-payment interest, article 1727 CGI: https://bofip.impots.gouv.fr/bofip/1458-PGP.html
- Form 2258-SD, 2025 edition: https://www.impots.gouv.fr/sites/default/files/formulaires/2258-sd/2025/2258-sd_4927.pdf
- La déclaration pays par pays (modified 24/05/2022): https://www.impots.gouv.fr/la-declaration-pays-par-pays
- Form 2257-SD, 2017 edition: https://www.impots.gouv.fr/sites/default/files/formulaires/2257-sd/2017/2257-sd_1338.pdf
- Securing a transfer pricing policy (modified 04/07/2022): https://www.impots.gouv.fr/professionnel/questions/ma-societe-situee-en-france-fait-partie-dun-groupe-international-comment
- Form 2259-SD user guide, Pillar Two (November 2025): https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/210_declarer_payer/impot_mondial_15pc_pilier2/gu-2259-sd---2025-v1.pdf

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
