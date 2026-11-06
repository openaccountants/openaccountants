---
name: eg-cross-border
description: "Egypt cross-border income tax for tax year 2026 under Income Tax Law 91 of 2005 as amended by Law 30 of 2023 and Law 151 of 2026, and Unified Tax Procedures Law 206 of 2020. Covers residence of individuals (permanent home, more than 183 days, Egyptians paid abroad from an Egyptian treasury) and legal persons (Egyptian incorporation, main or actual management in Egypt, more than 50% state ownership), Egyptian-source income (art. 3), the permanent establishment definition and its 90-day tests (arts. 4 and 4 bis), the 20% withholding on interest, royalties, services and sport or artist fees paid to non-residents (art. 56) and its exemptions, the 10% or 5% dividend tax and the deemed distribution of branch profits (art. 56 bis), capital gains of non-residents on Egyptian shares after Law 151 of 2026, the foreign tax credit (art. 54), treaty refunds and residence certificates. Trigger on: Egypt non-resident tax, Egypt withholding non-resident, Egypt permanent establishment, Egypt branch pro"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eg-cross-border"
  jurisdiction: "EG"
  tax_year: "2026"
  last_updated: "2026-11-02"
---

# Egypt cross-border: residence, source, permanent establishment, non-resident withholding and foreign tax credit v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Income Tax Law 91 of 2005 (قانون الضريبة على الدخل) sets who is resident, what income arises in Egypt, when a non-resident has a permanent establishment (PE, المنشأة الدائمة) and how payments to non-residents are taxed. Law 30 of 2023 (in force 16 June 2023) rewrote the PE and related-person definitions; Law 151 of 2026 (in force 29 July 2026) changed dividends, share gains and two interest rules. The Egyptian Tax Authority (ETA) administers it. Tax year: calendar year, or a legal person's financial year. Reply in English or Arabic; amounts in EGP.

## Who this applies to

- **Resident individuals** (Law 91 art. 2): a permanent home in Egypt; or present in Egypt more than 183 days, continuous or not, within twelve months; or an Egyptian working abroad and paid from an Egyptian treasury. Same tests as `eg-income-tax`.
- **Resident legal persons** (art. 2, second para.): incorporated under Egyptian law; or with its main or actual centre of management in Egypt; or a company in which the state or a public legal person owns more than 50% of the capital. The executive regulations set the rules for permanent home and actual management.
- **Scope.** Resident legal persons pay corporate tax on all profits, in Egypt or abroad; non-resident legal persons pay on profits realised through a PE in Egypt (art. 47). Banks, companies and foreign establishments with branches in Egypt are legal persons for this purpose (art. 48 item 4). Individuals: art. 6 (`eg-income-tax`).
- **Permanent establishment** (art. 4 as replaced by Law 30/2023): a fixed place of business through which all or part of a non-resident's business is carried on, in particular a place of management, branch, office, factory, workshop, mine, oil or gas field, quarry or other place of extracting natural resources, farm or plantation, buildings used as sales outlets, and a building or construction site, installation or assembly project, or supervisory activity lasting more than 90 days in any twelve months. Also treated as a PE:
  - exploration or exploitation of natural resources in Egypt, including substantial equipment, for more than 90 days in any twelve months;
  - services, including consultancy, through employees or other personnel for the same or a connected project for more than 90 days in any twelve months;
  - a foreign insurer collecting premiums in Egypt or insuring risks there through anyone other than an independent agent (reinsurance excepted);
  - a dependent agent who has authority to conclude contracts in the enterprise's name (unless it only buys goods for it), or habitually concludes contracts or plays the principal role leading to contracts routinely concluded without material change, where the contracts are in the enterprise's name, transfer or license its property, or are for its services. An agent acting exclusively or almost exclusively for closely related enterprises is not independent;
  - split contracts: periods spent by closely related enterprises at the same site are added together.
- **Not a PE** (art. 4 bis, added by Law 30/2023): facilities used only to store or display goods; stock held only for storage, display or processing by another enterprise; a fixed place used only to buy goods or collect information, or for any other preparatory or auxiliary activity, or a combination whose overall activity stays preparatory or auxiliary; a foreign subsidiary controlled by an Egyptian company. The exception does not apply where the enterprise or a closely related one carries on business at the same or another place in Egypt and either that place is a PE, or the combined activity is not preparatory or auxiliary, the activities being complementary functions of one cohesive business (anti-fragmentation). Closely related: control on the facts, or more than 50% of shares, votes or equity held directly or indirectly.
- **Not here:** treaty rates and treaty PE articles; VAT on services from non-residents (`egypt-vat`); transfer pricing and the debt to equity limit (`eg-transfer-pricing`); the withholding return, forms and remittance dates (`eg-withholding-tax`); corporate rate and return (`eg-corporate-tax`).

## Rates, bands and thresholds

| Item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Interest, royalties, service fees, sport or artist fees paid to a non-resident | 20% of the gross amount, no costs deducted | Payer: owner of a sole proprietorship, resident legal person, or a non-resident's Egyptian PE (Law 91 art. 56 first para., 2005 text). Treaty may reduce: see "Cross-border points" | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Royalties carve-out | Outside art. 56 | Amounts paid abroad for design or know-how serving industry, in cases the Minister sets with the Minister of Industry (art. 56 item 2) | 2026 | same |
| Services carve-out | Outside art. 56 | Administrative, control and supervision costs a head office abroad charges to its Egyptian PE (art. 56 item 3) | 2026 | same |
| Interest on foreign loans to government | Exempt | Loans and credit facilities from outside Egypt to the government, local units and other public legal persons (art. 56 third para. as replaced by Law 30/2023) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| Interest on company loans of 3 years or more | Exemption repealed from 16 Jun 2023 | Continues only for loans of public, business-sector and private companies on which interest was paid before 16 Jun 2023 (Law 30/2023 art. 6) | 2026 | same |
| Interest on loans for national infrastructure projects | Exempt | Lender not related; loan or facility at least five years; projects named by Prime Minister decision; company's share at least 25% of its investments; ends when the loans and facilities for carrying out the project's main works end (art. 56 fourth para., Law 151/2026 art. 2, as corrected by the Gazette erratum of 8 Aug 2026) | From 29 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Dividends to non-resident individuals and to resident or non-resident legal persons | 10%; 5% if the securities are listed on the Egyptian Exchange; no costs deducted | Art. 56 bis as replaced by Law 151/2026; bonus shares excluded; civil companies treated as partnerships. Resident-to-resident company dividends are left out of the dividend tax and the recipient's corporate base | 2026 | same |
| Branch profits of a non-resident legal person | Deemed distributed within 60 days after the PE's financial year end, so the 10% dividend tax applies | Art. 56 bis | 2026 | same |
| Participation exemption | Dividends a parent or holding company receives from resident and non-resident subsidiaries are exempt | At least 25% of capital or votes, held two years or committed to be held two years (art. 50 item 10 as replaced by Law 151/2026; the 10% add-back of the 2023 text is gone) | From 29 Jul 2026 | same |
| Gains on listed Egyptian securities | Exempt; losses not deductible | Individuals art. 31 item 7, legal persons art. 50 item 7 (Law 151/2026); not exempt where the sale delists the company | From 29 Jul 2026 | same |
| Gains on unlisted securities and company shares | Taxable, wherever realised; a non-resident seller computes and pays within 60 days of the transaction | Art. 46 bis 3 as replaced by Law 151/2026; gain is price less acquisition cost and brokerage (art. 46 bis 4). Treasury bill gains of non-residents are outside | From 29 Jul 2026 | same |
| Treasury bill yields | 20% of the yield, no costs deducted; payer remits the tax the day after deducting it | Art. 58 second para. as replaced by Law 30/2023 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| PE time tests | More than 90 days, in total, in any twelve months | Construction and installation sites, resource activities, services (art. 4) | 2026 | same |
| Refund interest | Central Bank rate on 1 January before the due date plus 2%; 20.50% on 1 Jan 2026, so 22.50% | ETA pays this if a refund is not made within 45 days of a complete application (Law 206 art. 53) | 2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf |

Listed share gains tax left unpaid for 16 June 2023 up to Law 151's start date (29 July 2026) is forgiven (Law 151/2026 art. 5).

## The base

**Egyptian-source income** (art. 3; items (b) and (j) as replaced by Law 30/2023):
- (a) services performed in Egypt, salaries included;
- (b) income borne by an employer resident in Egypt, even if the work is done abroad;
- (c) sportsmen's and artists' income from activity in Egypt;
- (d) business income of a non-resident through a PE in Egypt;
- (e) disposals of movable property of a PE in Egypt;
- (f) exploiting or disposing of real estate in Egypt;
- (g) dividends on shares of a capital company resident in Egypt; (h) profit shares paid by a resident partnership;
- (i) interest paid by the government, local units, public legal persons, any resident, or a PE in Egypt even if its owner is non-resident;
- (j) rent, licence fees and royalties borne by a resident or by a PE in Egypt;
- (k) income from any other activity in Egypt.

**Withholding is a gross tax.** Art. 56 tax is on the amount paid, with no costs deducted. The payer withholds and remits; see `eg-withholding-tax` for the return and dates. The ETA's art. 56 certificate (form 8 اتفاقيات دولية) proves the 20% was withheld, for a foreign credit at home.

**PE profits.** A PE pays corporate tax on its profits like a resident company (`eg-corporate-tax`), files the annual return, and its profits are deemed distributed 60 days after its year end (art. 56 bis). Head office administrative and supervision charges to the PE are outside art. 56, but their deduction is a TP question (`eg-transfer-pricing`).

**Foreign tax credit, resident companies** (art. 54): foreign tax a resident company pays on profits abroad is credited against Egyptian tax, with supporting documents. The credit may not exceed the Egyptian tax on the foreign profits. Foreign losses are not deductible from the Egyptian base, for that year or any later one.

**Resident individuals.** Foreign receipts of an activity centred in Egypt are taxed (`eg-income-tax`). A unilateral credit for individuals was not found in the articles read; use the treaty.

**Treaties.** A treaty overrides the domestic rate only where its conditions are met. ETA's refund route (below) asks for a residence certificate and a beneficial-owner statement, and that the income is not connected with a PE in Egypt.

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Withhold on non-resident payments | At payment; remit and report as in `eg-withholding-tax` | Law 91 art. 56 |
| Dividend tax | The paying or settling body withholds and pays to ETA's central withholding department within five working days of the start of the month after collection | Art. 56 bis (Law 151/2026) |
| Non-resident sale of unlisted shares | Seller computes and pays within 60 days of the transaction | Art. 46 bis 3 (Law 151/2026) |
| PE annual return | Before 1 May, or within four months after the financial year end | Law 206 art. 31(c) |
| Individual leaving Egypt for good | File the return at least 60 days before residence ends, unless the departure is sudden | Law 206 art. 31(d) |
| Treaty refund of excess withholding | Non-resident files form 1 (withholding refund) on the ETA portal after simplified registration, or with ETA's international agreements department; ETA decides within 45 days of a complete file; missing papers must follow within 15 days (10 then 5) or the case closes | ETA Services Guide, 2nd ed., service 5/1 |
| Art. 56 certificate | Form 8 اتفاقيات دولية with form 11 and payment receipts; issued within 7 days | ETA Services Guide, service 5/2 |
| Egyptian residence certificate | Form 9 اتفاقيات دولية; issued within 7 days of a complete application | ETA Services Guide, service 5/3 |
| Advance inquiry on treaty treatment | Form 7 اتفاقيات دولية; answer within 30 days (inquiry) or 60 days (advance opinion) of a complete file | ETA Services Guide, service 5/4 |

**Refund file (service 5/1):** power of attorney; original residence certificate of the foreign company for each year, certified; beneficial-owner certificate saying the income is not connected with a PE in Egypt; incorporation and registry papers; the contracts, translated into Arabic by an accredited office; proof of ownership of the rights; withholding forms 11 and payment receipts; bank transfers abroad; invoices; the Egyptian payer's balance sheets and returns. No fee.

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Late payment of tax, including withholding | Delay charge at the Central Bank rate plus 2% a year (`eg-income-tax`), capped at 100% of the principal tax | Law 91 art. 110; Law 206 art. 45 bis (Law 7/2025) |
| Tax not withheld, or withheld and not remitted (Law 91 art. 135 offence) | Settlement possible: 12.5% of the amounts not withheld or not remitted, plus those amounts and the delay charge | Law 206 art. 75 bis 1 (Law 7/2025) |
| Late or wrong return, no return over 60 days, books not kept, evasion | Fines and prison (amounts in `eg-income-tax`) | Law 206 arts. 69 to 72, art. 70 as replaced by Law 211/2020 |
| Late refund by ETA | ETA owes the Central Bank rate plus 2% | Law 206 art. 53 |

## Cross-border points

- **Treaties.** ETA's list shows 64 entries: 63 bilateral treaties and the Council of Arab Economic Unity agreement (https://www.eta.gov.eg/ar/content/atfaqyat-thnayyt). Treaty rates are out of scope; read the treaty itself. Egypt also publishes an MLI fact sheet (not read here).
- **Transfer pricing.** Dealings between a PE and its head office, and payments to related non-residents, must be at arm's length (`eg-transfer-pricing`).
- **VAT** on services supplied by non-residents: see `egypt-vat`.
- **Information exchange.** Law 206 art. 78 lets ETA exchange information with treaty partners.

## Two worked examples that recompute

**Case 1. Payments to a non-treaty non-resident in 2026.** An Egyptian company pays a related foreign company: royalty EGP 1,000,000, a service fee EGP 500,000, and interest EGP 300,000 on a five-year loan taken in 2025 (no infrastructure project, so no exemption; the 3-year exemption ended in 2023). Withholding: 20% x 1,800,000 = 360,000. The foreign company receives 1,440,000.

```oa-check
name: Art. 56 withholding on royalty, service fee and interest
inputs:
  royalty: 1000000
  services: 500000
  interest: 300000
steps:
  - gross: royalty + services + interest
  - wht: gross * 0.20
  - net_paid: gross - wht
expected:
  wht: 360000.00
  net_paid: 1440000.00
```

**Case 2. Decision: branch or subsidiary for profit kept in Egypt.** A foreign group earns EGP 10,000,000 of profit after corporate tax in Egypt in 2026 and wants to send home only 4,000,000. As a branch (PE), the whole profit is deemed distributed 60 days after year end: 10% x 10,000,000 = 1,000,000. As an unlisted subsidiary, dividend tax falls only on what it pays: 10% x 4,000,000 = 400,000. The subsidiary defers 600,000 on the retained 6,000,000 (treaty rates aside).

```oa-check
name: Branch deemed distribution against subsidiary dividend
inputs:
  profit: 10000000
  paid_out: 4000000
steps:
  - branch_tax: profit * 0.10
  - subsidiary_tax: paid_out * 0.10
  - deferred: branch_tax - subsidiary_tax
expected:
  branch_tax: 1000000.00
  subsidiary_tax: 400000.00
  deferred: 600000.00
```

Whether the deemed distribution is measured after corporate tax is on "Not yet confirmed"; Case 2 assumes it is.

## Ask the client first

1. Is the client an individual or a legal person, and which residence test in art. 2 is met (home, days, incorporation, management, state ownership)?
2. For a non-resident: is there a fixed place, an agent, a site, or services in Egypt, and for how many days in any twelve months?
3. What is being paid (interest, royalty, service, dividend, share sale price), to whom, and under which contract?
4. Is there a treaty with the recipient's country, and does the recipient hold a residence certificate and beneficial-owner statement for the year?
5. For loans: term, start date, lender related or not, infrastructure project or government borrower?
6. For a resident company with foreign profits: foreign tax paid and the documents proving it.

Refuse to help disguise payments, hide a PE or claim treaty relief for someone who is not the beneficial owner.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 91 of 2005, original text: arts. 1 to 4, 47 to 50, 52, 54 to 58 (page images read; Gazette pp. 6 to 9, 30 to 35) | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-02 |
| Law 30 of 2023: arts. 1 (art. 1 definitions, art. 3 items b and j, art. 4, art. 50, art. 52 item 1, art. 56 third para., art. 56 bis, art. 58 second para.), 2 (art. 4 bis, art. 46 bis 3 fourth para.), 5, 6, 12 (text layer and p. 6 image read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | 2026-11-02 |
| Law 151 of 2026, whole text (arts. 31 item 7, 46 bis 3 and 4, 50 items 7 and 10, 52 item 1, 56 fourth para., 56 bis; arts. 5 to 7); Gazette 30 bis (a), 28 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-02 |
| Gazette erratum to Laws 149, 150 and 151 of 2026, Gazette 32 bis, 8 Aug 2026 (page images read; corrects art. 56 fourth para.) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-02 |
| Unified Tax Procedures Law 206 of 2020: arts. 31, 38, 44, 53, 68 to 81 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-02 |
| Law 211 of 2020, arts. 1 to 3 (arts. 44, 70 as replaced) | https://eta.gov.eg/sites/default/files/2026-05/law_no.211-2020.pdf | 2026-11-02 |
| Law 7 of 2025, whole text (arts. 45 bis, 75 bis, 75 bis 1) | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-02 |
| ETA circular 1 of 2026, Central Bank rates on 1 January (page image read) | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | 2026-11-02 |
| ETA Services Guide, 2nd edition: international agreements services 5/1 to 5/4, pp. 97 to 108 | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-02 |
| ETA bilateral treaties page, read for the list of partner states (64 entries counted) | https://www.eta.gov.eg/ar/content/atfaqyat-thnayyt | 2026-11-02 |

Not yet confirmed: whether art. 56 first para. (20% rate and payer list) and its last para. (remittance within 15 days of the following month) were amended after 2005 by a law not read here (Law 206/2020 may override the remittance timing; `eg-withholding-tax` owns it). The tax rate on a non-resident's gain on unlisted Egyptian shares (art. 46 bis 3 names the duty to pay but not the rate for a non-resident) and how the executive regulations compute it. Whether the branch deemed distribution is measured after corporate tax, and its filing form. Whether a non-resident legal person without a PE is within art. 50 item 7 for listed share gains. A unilateral foreign tax credit for resident individuals. The executive-regulation rules on permanent home and actual management (art. 2 last para.). The ETA forms' own article references for treaty refunds, any time limit for claiming a refund, and the MLI positions. Corporate rate for PEs is in `eg-corporate-tax` and was not re-read here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-02. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eg-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eg-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
