---
name: sa-withholding-tax
description: "Use this skill whenever asked to compute, classify, or review Saudi Arabian Withholding Tax (WHT) obligations payable by a resident payer on payments to non-resident recipients for services, rent, royalties, dividends, interest, management fees, insurance premiums, freight, telecommunications, or other in-scope categories under Article 68 of the Saudi Income Tax Law and Articles 63–67 of the Implementing Regulations. Trigger on phrases like \"Saudi WHT\", \"ZATCA withholding\", \"5% WHT KSA\", \"15% WHT KSA\", \"20% management fee WHT\", \"Article 68 Saudi\", \"treaty rates Saudi\", \"WHT Saudi Arabia\", \"Saudi royalty WHT\", \"Saudi dividend withholding\", \"non-resident WHT Saudi\", \"ZATCA monthly WHT return\", \"TRC Saudi treaty\", \"Saudi PE risk WHT\", or any request involving the classification, deduction, or remittance of Saudi withholding tax. This skill covers WHT under the Income Tax Law (Royal Decree No. M/1 dated 15/1/1425H, as amended) and the Implementing Regulations issued by the Zakat, Tax and Customs Authority (ZATCA, formerly GAZT), including the Tier 1 standard rates (services 5%, rent 5%, royalties 15%, dividends 5%, interest 5%, management fees 20%, insurance/reinsurance premiums 5%, international telecommunications 5%, air/sea freight 5%), Tier 2 treaty-rate reductions across Saudi Arabia's growing treaty network (UK, France, China, India, Pakistan, etc.), mixed-source transactions, capital gains by non-residents on Saudi-source assets, and the interaction with the Pillar Two top-up regime. Out of scope: Zakat (Saudi/GCC-owned entity charge — see sa-zakat); Corporate Income Tax on resident non-GCC-owned entities (see sa-corporate-tax); VAT (see saudi-arabia-vat); E-invoicing (see saudi-einvoice); upstream petroleum special regime; expatriate employee levy; the GCC selective tax. ALWAYS read this skill before touching any Saudi WHT work."
jurisdiction: SA
domain: international
tax_year: 2025
reviewed_by: Mehran Habib
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# sa-withholding-tax

## Saudi Arabia — Withholding Tax — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mehran Habib** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Withholding Tax

- **Management fees** — 0.2  _(ITL Art. 68(a)(3))_
- **Royalties (incl. software, IP)** — 0.15  _(ITL Art. 68(a)(2))_
- **Technical/consultancy (related party)** — 0.05  _(ITL Art. 68(a)(3))_
- **Services (general, unrelated)** — 0.05  _(Income tax regulations)_
- **Rent (immovable/movable in KSA)** — 0.05  _(Income tax regulations)_
- **Dividends** — 0.05  _(Income tax regulations)_
- **Interest / loan charges** — 0.05  _(Income tax regulations)_
- **Insurance / reinsurance premiums** — 0.05  _(Income tax regulations)_
- **International telecoms** — 0.05  _(ITL Art. 68)_
- **Other (catch-all)** — 0.15  _(ITL Art. 68)_
- **Monthly return** — Within 10 days of month-end  _(ITL Art. 68(b))_
- **Annual reconciliation** — 120 days after FYE  _(ITL Art. 68)_

## Section 1 — Quick reference (rate table by transaction type)

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Kingdom of Saudi Arabia (KSA) |
| Tax covered | Withholding Tax (WHT) on payments from a Saudi-resident payer to a non-resident recipient on Saudi-source income |
| Currency | Saudi Riyal (SAR, ﷼) — foreign-currency payments converted at the SAMA reference rate on the date of payment / accrual (whichever is earlier) |
| Tax year | Hijri or Gregorian — most corporate payers use the Gregorian calendar year (1 Jan – 31 Dec); WHT itself is administered on a monthly basis |
| Current tax year | 2025 |
| Tax authority | **Zakat, Tax and Customs Authority (ZATCA)** — formerly the General Authority of Zakat and Tax (GAZT), merged with Customs in 2021 |
| Filing portal | ZATCA portal — https://zatca.gov.sa (monthly WHT return + annual reconciliation) |
| Remittance deadline | **Within 10 days of the end of the month in which the payment was made** (Article 68(b), Income Tax Law) |
| Annual reconciliation deadline | Within 120 days of the payer's financial year-end |
| Governing law | **Income Tax Law (Royal Decree No. M/1 dated 15/1/1425H, 15 March 2004) — Article 68**, supplemented by the **Implementing Regulations (Resolution of the Minister of Finance No. 1535 dated 11/6/1425H) — Articles 63–67** |
| Validated by | Pending — requires sign-off by a SOCPA-licensed Saudi tax practitioner |
| Skill version | 1.0 |

### Quick-look: payment type → standard WHT rate (resident payer → non-resident recipient)

**Quick-look rate table**

| Payment type | Standard rate | Common treaty cap (where applicable) | Final / creditable in KSA |
| --- | --- | --- | --- |
| **Management fees** | **20%** | Rarely reduced — treaties typically do not cap management fees | **Final** for the non-resident |
| **Royalties** (including software licences, technical know-how, trademarks, franchises) | **15%** | 5%–10% under most treaties (e.g. UK 5%/8%, France 5%/10%) | Final |
| **Technical / consultancy services from a related party** | **15%** | Per treaty (services article may not exist) | Final |
| Services (general — unrelated party) | 5% | Per treaty | Final |
| Rent (immovable and movable property in KSA) | 5% | Per treaty | Final |
| Dividends | 5% | 0%–5% under most treaties | Final |
| Interest / loan charges | 5% | 0%–10% under most treaties | Final |
| Insurance / reinsurance premiums | 5% | Per treaty (often not specifically capped) | Final |
| International telecommunications services | 5% | Per treaty | Final |
| Air freight / sea freight | 5% | Per treaty (transport article usually exempts) | Final |
| Other payments to non-residents not otherwise listed | 15% (catch-all under Article 68) | Per treaty | Final |

- **Critical rule (Article 68(a))** — WHT is imposed on the gross amount paid to the non-resident — there is no deduction for costs, expenses, or input VAT. The Saudi-resident payer is personally and primarily liable to deduct and remit the tax — failure to deduct does NOT shift the burden to the recipient.  _(Article 68(a) Income Tax Law)_
- **Critical rule (Article 68(b))** — The payer must deduct WHT at the time of payment and remit it to ZATCA within 10 days of the end of the month in which the payment was made. There is no de minimis threshold — even small payments to non-residents are in scope.  _(Article 68(b) Income Tax Law)_
- **Critical rule (no WHT between Saudi residents)** — Saudi WHT under Article 68 applies only to payments from a Saudi-resident payer to a non-resident recipient. Payments between two Saudi-resident entities are NOT subject to Article 68 WHT (they may be subject to Zakat or CIT in the recipient's hands directly).  _(Article 68 Income Tax Law)_

## Section 2 — Required inputs and refusal catalogue

### 2.1 Mandatory inputs before any WHT computation

- **Refusal instruction** — Refuse to compute WHT without ALL of the following inputs.

**Mandatory inputs table**

| Input | Why it matters |
| --- | --- |
| Payer identity, ZATCA Tax/Zakat Number, and entity type (LLC, JSC, branch, individual) | Determines registration status, filing portal access, and remittance obligation |
| Confirmation that the payer is **Saudi-resident** (per Article 3 Income Tax Law — incorporated in KSA, central management in KSA, or branch of foreign entity registered in KSA) | Article 68 applies only to payments **by** Saudi residents |
| Recipient legal name, country of tax residence, and tax ID in home jurisdiction | Determines non-resident status and treaty eligibility |
| Confirmation that the recipient is **non-resident** (no Saudi PE, not registered in KSA) | If the recipient has a Saudi PE, the payment is attributable to that PE and CIT applies — not WHT |
| Nature of the payment (services, rent, royalty, dividend, interest, management fee, insurance, telecoms, freight, mixed) | Determines applicable rate band (5% / 15% / 20%) |
| Whether the parties are **related** for technical/consultancy services | Triggers the 15% related-party rate vs the 5% unrelated rate |
| Gross contract value in payment currency, conversion rate, and SAR equivalent | WHT base is gross — no deductions |
| Date of payment and date of accrual / invoice | Tax point is the earlier of the two |
| For treaty relief: a valid **Tax Residence Certificate (TRC)** issued by the recipient's home tax authority, dated for the relevant year | Without TRC at the tax point, statutory rate applies |
| For related-party services: transfer pricing documentation justifying the fee | ZATCA may challenge the deductibility and the 15% classification |
| Whether the payment relates to a Permanent Establishment of the non-resident in KSA | If yes, PE is taxed under CIT — not WHT |
| For mixed-source transactions (e.g. partly KSA-source services + partly offshore): allocation methodology | Only the KSA-source portion is subject to WHT |

### 2.2 Refusal catalogue

**Refusal catalogue table**

| # | Situation | Reason |
| --- | --- | --- |
| R-SA-WHT-1 | Zakat computation for Saudi/GCC-owned entities | Out of scope — route to `sa-zakat`. |
| R-SA-WHT-2 | Corporate Income Tax (CIT) on resident non-GCC-owned entities or PEs of non-residents | Out of scope — route to `sa-corporate-tax`. |
| R-SA-WHT-3 | VAT, e-invoicing (FATOORA), or selective tax | Out of scope — see `saudi-arabia-vat` and `saudi-einvoice`. |
| R-SA-WHT-4 | Upstream petroleum special regime (Saudi Aramco, hydrocarbon concessionaires) | Specialist domain — refer to a petroleum tax specialist. |
| R-SA-WHT-5 | Treaty rate claim without a valid TRC dated for the relevant period | Default to statutory rate; treaty relief denied without TRC. |
| R-SA-WHT-6 | Recipient has Saudi PE — payment attributable to the PE | Not a WHT case — file under CIT via the PE branch return. |
| R-SA-WHT-7 | Capital gains realised by a non-resident on disposal of Saudi-source assets (other than listed shares on Tadawul, which are generally exempt) | Specialist — flagged separately under Article 68(a)(8); refer for valuation, cost basis, and treaty analysis. |
| R-SA-WHT-8 | Mixed contracts (e.g. supply + installation + training) where the Saudi-source / offshore split is contested | Refuse to apportion without underlying contracts and a supportable allocation methodology. |
| R-SA-WHT-9 | Intra-group reimbursements without supporting invoices in the original supplier's name | Likely re-characterisable as a service fee — refuse and request underlying contracts. |
| R-SA-WHT-10 | Bespoke ZATCA rulings or settlement agreements affecting the rate | Cannot rely on private rulings without sight of the original letter — refuse and request the document. |
| R-SA-WHT-11 | Pillar Two top-up tax computation requiring WHT credit modelling | Specialist — refer to a Pillar Two practitioner; this skill flags the interaction only. |
| R-SA-WHT-12 | Expatriate employee levy or work-permit fees | Not WHT — separate Ministry of Human Resources regime. |

## Section 3 — Tier 1 — common categories and rates

### 3.1 Statutory basis

- **Statutory basis** — WHT is imposed by Article 68 of the Saudi Income Tax Law (Royal Decree No. M/1 dated 15/1/1425H, 15 March 2004) and elaborated in Articles 63–67 of the Implementing Regulations (Ministerial Resolution No. 1535 dated 11/6/1425H). The tax applies to amounts paid by a Saudi-resident payer or by a Saudi PE of a non-resident to a non-resident recipient on Saudi-source income.  _(Article 68 of the Saudi Income Tax Law; Articles 63–67 of the Implementing Regulations)_

### 3.2 The standard rate table (Article 68(a))

**Standard rate table**  _(Article 68(a))_

| Category | Article 68(a) sub-paragraph | Rate |
| --- | --- | --- |
| Management fees | (1) | **20%** |
| Royalties (including software, technical know-how, franchises, trademarks, etc.) | (2) | **15%** |
| Payments for technical and consulting services from a **related party** | (3) | **15%** |
| Payments for technical and consulting services from an **unrelated party** | (3) | 5% |
| Rent (immovable and movable property situated in KSA) | (4) | 5% |
| Dividends | (5) | 5% |
| Loan charges / interest | (6) | 5% |
| Insurance and reinsurance premiums | (7) | 5% |
| International telecommunications services | (8) | 5% |
| Air freight and sea freight | (9) | 5% |
| **Other payments** to non-residents not otherwise listed (catch-all) | (10) | **15%** |

- **20% management fee rate note** — The 20% management fee rate is unique in the region — it is one of the highest WHT rates on management fees globally and rarely reduced by treaty (most treaties do not have a specific "management fees" article, so the domestic 20% applies). Identify and isolate management fee components in mixed contracts to avoid over- or under-withholding.

### 3.3 Saudi-source income definition (Article 5 Income Tax Law)

- **Saudi-source income** — WHT under Article 68 applies only to Saudi-source income. Article 5 deems income to be Saudi-source where it arises from: An activity carried out in KSA, or a property situated in KSA, or services rendered to a Saudi resident, OR services utilised in KSA (the "use" test — even if performed offshore), the use of a right or intangible in KSA (for royalties), a loan secured against KSA assets or used in KSA.  _(Article 5 Income Tax Law)_
- **The 'use' test for services** — The "use" test for services is broad. Even services performed entirely offshore by a non-resident can be deemed Saudi-source if the benefit is consumed in KSA. ZATCA applies this broadly to consulting, technical, and management services.  _(Article 5 Income Tax Law)_

### 3.4 Tax base — gross, no deductions

- **Gross tax base rule** — WHT under Article 68 is computed on the gross amount paid, with no deduction for costs, expenses, agent fees, or any other amounts. There is no input-VAT stripping (VAT is a separate tax and does not interact with WHT base).  _(Article 68)_
- **Gross-up base formula** — If the contract is net of WHT ("gross-up" clause — the non-resident receives 100 and the Saudi payer bears the WHT), the payer must gross up the contract before applying the rate, as follows: Gross-up base = net amount / (1 − rate). Example: SAR 100,000 net to non-resident at 15% royalty rate → gross-up base = 100,000 / 0.85 = SAR 117,647.06 → WHT = SAR 17,647.06.  _(Article 68)_

### 3.5 No de minimis

- **No de minimis exemption** — There is no de minimis exemption under Article 68. Every payment to a non-resident on Saudi-source income is in scope, regardless of value.  _(Article 68)_

### 3.6 WHT is final for the non-resident

- **WHT is final** — WHT under Article 68 is the final and only Saudi tax liability for the non-resident on the income concerned (Article 68(c)). The non-resident is not required to file a Saudi tax return for that income and cannot claim a credit or refund in KSA. However: The non-resident may claim a credit in its home jurisdiction for the Saudi WHT, subject to that jurisdiction's domestic credit rules and the relevant DTT. Where the non-resident in fact has a Saudi PE, the payment is attributable to the PE and falls under CIT — Article 68 then does not apply (Article 68(d)).  _(Article 68(c); Article 68(d))_

### 3.7 Payer liability

- **Payer liability** — The Saudi-resident payer is primarily and personally liable for the WHT (Article 68(b)). If the payer fails to deduct, ZATCA pursues the payer, not the non-resident. The payer cannot generally recover the under-withheld amount from the non-resident retrospectively unless contractually entitled.  _(Article 68(b))_

## Section 4 — Tier 2 — treaty rates, mixed-source transactions, capital gains

### 4.1 Treaty network (as at 2025)

Saudi Arabia has built a wide DTT network — at the time of writing the principal DTTs in force include (non-exhaustive): United Kingdom, France, Germany, Netherlands, Spain, Italy, Austria, Greece, Hungary, Poland, Czech Republic, Romania, Bulgaria, Belarus, Russia (verify ratification post-sanctions), Turkey, Ukraine, Pakistan, India, China, Japan, South Korea, Singapore, Malaysia, Indonesia, Vietnam, Philippines, Bangladesh, Sri Lanka, Egypt, Tunisia, Morocco, Algeria, Jordan, South Africa, Mexico, Venezuela, Azerbaijan, Kazakhstan, Tajikistan, Uzbekistan, Kyrgyzstan, Ethiopia. (List drawn from ZATCA published treaty schedule — always verify the specific treaty article text and ratification status before applying.)

### 4.2 Common treaty caps — illustrative matrix

**Common treaty caps — illustrative matrix**

| Country | Dividends | Interest | Royalties | Notes |
| --- | --- | --- | --- | --- |
| United Kingdom | 5% / 15% | 0% (govt) / 7.5% | 5% (equipment) / 8% (other) | DTT 2007 |
| France | 5% (substantial holding) / 15% | 0% (govt) / 5% (banks) / 10% | 5% (industrial/scientific) / 10% (other) | DTT 1981 (in force long-standing) |
| China | 5% | 10% | 10% | DTT 2006 |
| India | 5% | 10% | 10% | DTT 2006 |
| Pakistan | 5% / 10% | 10% | 10% | DTT 2006 |
| Singapore | 5% | 5% | 8% | DTT 2010 |
| South Korea | 5% / 10% | 5% | 5% (industrial) / 10% | DTT 2008 |
| Japan | 5% / 10% | 10% | 5% (equipment) / 10% | DTT 2010 |
| Germany | 5% / 15% | 0% (govt) / 7.5% | 10% | DTT 2007 (NB: limited treaty — covers air transport historically; verify scope) |
| Netherlands | 5% / 10% | 5% | 7% | DTT 2008 |
| Spain | 0% (substantial) / 5% | 5% | 8% | DTT 2007 |
| Russia | 5% | 5% | 10% | DTT 2010 (verify current standing) |
| Turkey | 5% / 10% | 10% | 10% | DTT 2007 |

- **GCC residents note** — Although the GCC has long-standing economic-integration agreements, Saudi domestic WHT under Article 68 still applies to payments to non-Saudi GCC residents in principle, unless the recipient is GCC-owned and qualifies for Zakat treatment, or a specific GCC-internal exemption applies. Verify in each case — do not assume a blanket GCC exemption.
- **Treaty relief mechanics** — ZATCA grants treaty relief on a withhold-then-refund basis in most cases: The Saudi payer withholds at the statutory rate (e.g. 15% on royalties). The non-resident submits a refund claim to ZATCA with: A valid Tax Residence Certificate (TRC) from the home tax authority for the relevant year; Evidence of beneficial ownership; The original Saudi WHT certificate issued by the payer; The relevant treaty article and computation showing the reduced rate. Direct application of the treaty rate at source is permitted in limited cases and only with ZATCA pre-approval — do NOT apply the treaty rate at source without confirmed approval.

### 4.3 Beneficial ownership and anti-abuse

- **Beneficial ownership and anti-abuse rule** — Most Saudi DTTs include a beneficial ownership requirement and many include limitation-of-benefits (LOB) or principal-purpose-test (PPT) clauses (especially post-BEPS MLI ratification). ZATCA will deny treaty relief where: The recipient is a conduit, agent, or nominee for the true beneficial owner; The arrangement's principal purpose was to obtain the treaty benefit; The recipient has no substance in the treaty country. Saudi Arabia is a signatory to the OECD Multilateral Instrument (MLI) and applies the PPT to most of its treaties post-ratification.

### 4.4 Mixed-source transactions

- **Mixed-source transactions rule** — Where a contract has both KSA-source and non-KSA-source components (e.g. consulting partly performed in KSA, partly offshore; a software licence covering both KSA and non-KSA users), only the KSA-source portion is subject to WHT. Apportionment must be: Reasonable, objective, and supported by underlying records (timesheets, user counts, asset locations, etc.); Documented in the contract or a separate apportionment schedule; Applied consistently across the engagement. ZATCA will challenge weak apportionments and default to a full KSA-source treatment if the apportionment cannot be substantiated. Conservative default: treat the full amount as KSA-source unless apportionment is documented and defensible.

### 4.5 Capital gains by non-residents

- **Capital gains by non-residents** — Capital gains realised by a non-resident on the disposal of Saudi-source assets (e.g. shares in a Saudi company, real estate situated in KSA, intangibles registered in KSA) are subject to Saudi tax under Article 68(a)(catch-all) at 20% on the gain (cost basis vs disposal proceeds). Exceptions: Disposals of shares listed on Tadawul (the Saudi Exchange) are generally exempt under Article 6 Income Tax Law and the implementing regulations, provided the disposal is on the exchange itself. Disposals of unlisted Saudi shares between non-residents may still attract Saudi tax — verify substance and treaty position. Most Saudi DTTs allocate taxing rights on capital gains to the source state for real estate and for shares deriving more than 50% of value from real estate (Article 13 OECD MC); other share gains are typically taxed only in the state of residence. Capital gains computation is complex — refuse without a full valuation, cost basis, and treaty analysis (see Section 2.2 R-SA-WHT-7).  _(Article 68(a); Article 6 Income Tax Law; Article 13 OECD MC)_

### 4.6 Pillar Two interaction

- **Pillar Two interaction** — Saudi Arabia has indicated its intention to implement the OECD Pillar Two Global Minimum Tax (GloBE rules — Qualified Domestic Minimum Top-up Tax or QDMTT) in line with the international framework. Where Pillar Two applies: Saudi WHT paid by a Saudi entity on payments to a non-resident group affiliate is included in the GloBE effective tax rate (ETR) computation of the recipient jurisdiction (creditable under Pillar Two rules), reducing the top-up. Conversely, WHT borne by a Saudi recipient (the inverse case — Saudi entity earning income from abroad subject to foreign WHT) is creditable in the Saudi GloBE computation. This skill does NOT compute Pillar Two top-up. Flag the interaction and refer to a Pillar Two specialist (Section 2.2 R-SA-WHT-11).

### 4.7 Permanent Establishment (PE) risk

- **PE risk indicators and treatment** — A non-resident receiving payments from a Saudi resident may inadvertently create a Permanent Establishment in KSA under Article 4 Income Tax Law or the relevant DTT PE article. Indicators include: A fixed place of business in KSA (office, branch, warehouse); An agent in KSA habitually concluding contracts on the non-resident's behalf; Provision of services in KSA exceeding the treaty-specified threshold (typically 183 days in a 12-month period under most Saudi DTTs); A construction or installation site lasting longer than the treaty threshold (typically 6 months). If a PE exists, the payment is attributable to the PE and falls under CIT at 20% (or the applicable hydrocarbon rate), with normal deduction rules — NOT under Article 68 WHT. Article 68 then does not apply (Article 68(d)). The PE risk is greater than the WHT risk in many engagements — a 5%/15% WHT exposure can transform into a 20% CIT liability on net profits plus registration obligations, late-filing penalties, and director-level personal exposure. Flag any engagement with extended on-the-ground presence.  _(Article 4 Income Tax Law; Article 68(d))_

## Section 5 — Worked examples

### 5.1 Royalty to UK-resident company (treaty relief)

Saudi LLC pays a UK-resident software company SAR 500,000 for an annual SaaS licence (treated as royalty per ZATCA practice).

**Scenario A — no TRC on file.**

- Tax base: SAR 500,000 (gross)
- Rate: 15% (royalty, statutory non-resident rate)
- WHT: **SAR 75,000**
- Net paid to UK: SAR 425,000
- Saudi LLC remits SAR 75,000 to ZATCA via the portal within 10 days of the end of the month of payment.
- UK company may claim refund of the differential (15% − 8% treaty cap = 7% = SAR 35,000) by submitting a TRC and refund claim to ZATCA post-payment.

**Scenario B — valid HMRC TRC pre-approved by ZATCA for treaty-rate-at-source.**

- Treaty rate: 8% (UK DTT Article 12, royalties general)
- WHT: SAR 500,000 × 8% = **SAR 40,000**
- Net paid to UK: SAR 460,000
- Saudi LLC remits SAR 40,000 to ZATCA, attaching the TRC and ZATCA pre-approval to the monthly return.

> **Software-as-royalty caveat.** ZATCA treats most software licences and SaaS subscriptions as royalty (15% statutory, treaty caps apply). Distinct treatment as "business profits" requires clear evidence (no transfer of rights, pure access to a service, no customisation) — default to royalty unless a robust legal opinion supports otherwise.

### 5.2 Management fee to related-party Cayman entity (no treaty)

Saudi LLC pays its Cayman parent SAR 1,000,000 as a management fee under an intra-group services agreement.

- Tax base: SAR 1,000,000
- Rate: **20%** (management fees, Article 68(a)(1))
- WHT: **SAR 200,000**
- Net paid to Cayman: SAR 800,000
- Saudi LLC remits SAR 200,000 to ZATCA within 10 days.
- Cayman has no DTT with KSA → no treaty relief.
- The Saudi LLC must also have transfer pricing documentation supporting the 1,000,000 fee as arm's-length, including a benchmarking study, to claim deductibility for CIT/Zakat purposes.

### 5.3 Technical service from German related-party (15% related-party rate)

Saudi LLC pays its German parent SAR 600,000 for technical engineering services provided remotely from Germany. The parties are related (parent–subsidiary). No TRC on file at tax point.

- Tax base: SAR 600,000
- Rate: **15%** (technical service from related party — Article 68(a)(3))
- WHT: **SAR 90,000**
- Net paid to Germany: SAR 510,000
- Saudi LLC remits SAR 90,000 to ZATCA within 10 days.
- If a valid TRC were on file, the Saudi–Germany DTT services article would need to be checked; many older Saudi treaties (including the Germany 2007 treaty) have limited service article coverage — the 15% domestic rate may stand. Verify the specific treaty text.

### 5.4 Mixed contract — supply + installation

Saudi LLC contracts a French supplier for: (a) supply of equipment (CIF Jeddah) — EUR 2,000,000, and (b) on-site installation and training in KSA — EUR 500,000. Total EUR 2,500,000. Contract clearly separates the two components.

- Component (a) — supply of goods: NOT a service — outside Article 68. (Customs duty and VAT on import apply separately.)
- Component (b) — installation/training in KSA: services with KSA performance → in scope under Article 68(a)(3). If unrelated party: 5%. If related party: 15%.
- Assume unrelated, no TRC pre-approval for treaty rate at source:
  - WHT base: EUR 500,000 × SAMA rate (assume SAR 4.10 / EUR) = SAR 2,050,000
  - WHT at 5%: **SAR 102,500**
- The supply component (a) is not withheld.
- If the contract had NOT separated the two components, ZATCA would default to treating the entire SAR 10,250,000 as services in scope → WHT 5% = SAR 512,500. Apportionment must be documented in the contract.

## Section 6 — Filing and payment

### 6.1 Tax point

- **Tax point definition** — The WHT obligation arises at the earlier of: The date of actual payment to the non-resident, or the date the cost is accrued / liability credited in the payer's books / invoice booked in payables. For accrual-basis companies, the tax point is typically the invoice booking date.  _(Article 68(b) Income Tax Law and Article 63 Implementing Regulations)_

### 6.2 Monthly WHT return — 10 days after month-end

- **Monthly WHT return requirements** — The Saudi-resident payer files a monthly WHT return on the ZATCA portal listing all WHT-attracting payments made (or accrued) during the month, with for each payment: Recipient name, country of tax residence, and tax ID; Nature of the payment (per Article 68(a) category); Gross amount paid (in SAR, converted at the SAMA reference rate on the tax-point date); WHT rate applied; WHT amount; Whether treaty relief is claimed (with TRC reference, if so); Contract reference and invoice number. The monthly return is filed and the WHT is remitted via the ZATCA portal (https://zatca.gov.sa) within 10 days of the end of the month of payment. Payment is by SADAD bill or bank transfer to the ZATCA designated account.

### 6.3 WHT certificate for the recipient

- **WHT certificate requirement** — For each WHT-attracting payment, the Saudi payer issues a WHT certificate to the non-resident recipient on the ZATCA-prescribed format, showing the gross amount, rate, WHT deducted, period, and the unique ZATCA reference number. The non-resident uses the certificate to claim a credit in its home jurisdiction.

### 6.4 Annual reconciliation

- **Annual reconciliation deadline** — Within 120 days of the payer's financial year-end, the payer files an annual WHT reconciliation on the ZATCA portal, reconciling the monthly returns to the annual financial statements and identifying any discrepancies. ZATCA may issue queries based on mismatches.

### 6.5 Penalties for non-compliance

- **Penalties for non-compliance** — Late remittance: penalty of 1% of the unpaid tax for each 30 days of delay (Article 76 Income Tax Law) — calculated from the original 10-day-post-month-end deadline. Failure to file the monthly return: administrative penalty (typically SAR 1,000 – SAR 10,000 per return, depending on payer size). Failure to deduct or under-deduction: the payer is personally liable for the unpaid tax plus the 1%-per-30-days delay penalty. ZATCA assesses on the payer directly and does not pursue the non-resident. Wilful evasion (gross under-reporting, fraudulent treaty claims): additional penalty up to 25% of the tax due and potential criminal referral.  _(Article 76 Income Tax Law)_

### 6.6 Limitation period

- **Limitation period** — ZATCA may assess WHT for 5 years from the end of the year in which the payment was made. The 5-year period is extended to 10 years in cases of fraud or wilful evasion.  _(Article 65 Income Tax Law)_

## Section 7 — Conservative defaults

When any input is ambiguous, missing, or contested, default to the position that minimises the risk of under-withholding — under-withholding makes the Saudi payer personally liable, whereas over-withholding allows the non-resident to claim a refund (administratively burdensome but available).

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Recipient residence unclear (KSA vs offshore) | Treat as non-resident → apply Article 68 WHT |
| Recipient may have a Saudi PE | Refuse — PE risk is greater than WHT risk; refer for PE analysis under CIT |
| Resident payer vs Saudi PE of foreign entity | Both attract Article 68 obligation — apply WHT |
| Service vs goods classification ambiguous | Treat as service → WHT applies |
| Related vs unrelated party for technical/consulting services | Treat as **related** → 15% (not 5%) |
| Royalty vs business profits (software/SaaS) | Treat as **royalty** → 15% (treaty cap may reduce) |
| Treaty rate claim without ZATCA pre-approval for at-source application | Withhold at statutory rate; let non-resident claim refund |
| TRC absent at tax point | Apply statutory rate; do not apply treaty rate retrospectively |
| Mixed KSA-source / offshore split contested | Treat the **full amount** as KSA-source → WHT on the full amount |
| Catch-all category vs specific category | Apply the **higher** category rate (typically 15% catch-all vs 5% services) |
| Reimbursement of expenses unclear | Include in WHT base unless original supplier invoices are in the payer's name |
| Gross-up clause silent | Assume contract is **gross of WHT** (Saudi payer deducts from the contract amount) |
| Currency conversion rate ambiguous | Use the SAMA reference rate on the tax-point date; document the source |
| GCC recipient — exemption claimed | Verify carefully — do **not** assume blanket GCC exemption; default to applying Article 68 |
| Article 68(a)(10) "other payments" catch-all unclear | Apply 15% (Article 68(a)(10) rate); do NOT default to a lower category without documentary support |
| Pillar Two interaction | Flag and refer; do not compute Pillar Two top-up in this skill |

## Section 7 — Conservative defaults

The general principle: withhold the higher rate and let the recipient claim a refund. A refund claim from ZATCA, while administratively heavy, is preferable to under-withholding and assessment of the Saudi payer 5 years later with 1%-per-30-days delay penalty (which can exceed the underlying tax in 8 years).

## Section 8 — Sources

**Primary legislation.**
- **Income Tax Law, Royal Decree No. M/1 dated 15/1/1425H (15 March 2004), as amended** — Article 68 (withholding tax), Articles 3 and 4 (residence and PE), Article 5 (Saudi-source income), Article 6 (exemptions), Article 65 (assessment limitation), Article 76 (penalties).
- **Implementing Regulations to the Income Tax Law, Ministerial Resolution No. 1535 dated 11/6/1425H, as amended** — Articles 63–67 (WHT procedure, rates, treaty relief, refund mechanics).
- **Zakat, Tax and Customs Authority Law (ZATCA Statute)** — institutional basis post-2021 GAZT/Customs merger.

**Subsidiary legislation and ZATCA guidance.**
- ZATCA Circulars on WHT (consolidated guidance on Article 68 categories, treaty relief procedure, TRC requirements, gross-up treatment, mixed-contract apportionment).
- ZATCA Transfer Pricing Bylaws (Resolution No. 6-1-19 of 25 January 2019) — relevant to related-party service classification and 15% rate.
- ZATCA Significant Economic Presence and digital services guidance.

**Treaty network (as at 2025).** Saudi Arabia has DTTs in force with (selection): United Kingdom, France, Germany, Netherlands, Spain, Italy, Austria, Greece, Hungary, Poland, Czech Republic, Romania, Bulgaria, Belarus, Russia, Turkey, Ukraine, Pakistan, India, China, Japan, South Korea, Singapore, Malaysia, Indonesia, Vietnam, Philippines, Bangladesh, Sri Lanka, Egypt, Tunisia, Morocco, Algeria, Jordan, South Africa, Mexico, Venezuela, Azerbaijan, Kazakhstan, Tajikistan, Uzbekistan, Kyrgyzstan, Ethiopia. Always verify the specific treaty article text and ratification status (and MLI position) on ZATCA's published treaty schedule before applying.

**OECD/International.**
- OECD Multilateral Convention to Implement Tax Treaty Related Measures to Prevent BEPS (MLI) — Saudi Arabia is a signatory; PPT applies to most covered tax agreements.
- OECD Pillar Two GloBE Model Rules and Commentary (2023 / 2024 updates) — KSA QDMTT implementation roadmap.

**Portals.**
- **ZATCA portal** — https://zatca.gov.sa — monthly WHT return, annual reconciliation, treaty refund claims, TRC pre-approvals.

## Section 9 — Cross-references

- For Saudi Zakat (the Saudi/GCC-owned entity charge) → see `sa-zakat.md`.
- For Saudi Corporate Income Tax on non-GCC-owned residents and PEs → see `sa-corporate-tax.md`.
- For Saudi VAT → see `saudi-arabia-vat.md`.
- For Saudi e-invoicing (FATOORA) → see `saudi-einvoice.md`.
- For Saudi client intake and identity verification → see `intake.md`.
- For Saudi foundation (currency, calendar, authority, general principles) → see `foundation.md`.

## Skill version 1.0. Tax year 2025. Pending sign-off by a SOCPA-licensed Saudi tax practitioner. Pillar Two GloBE rules and KSA QDMTT implementation are evolving — do not rely on this skill for top-up tax computation. Treaty relief at source requires ZATCA pre-approval — do not apply treaty rates without confirmed approval.

Skill version 1.0. Tax year 2025. Pending sign-off by a SOCPA-licensed Saudi tax practitioner. Pillar Two GloBE rules and KSA QDMTT implementation are evolving — do not rely on this skill for top-up tax computation. Treaty relief at source requires ZATCA pre-approval — do not apply treaty rates without confirmed approval.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
