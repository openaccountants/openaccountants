---
name: br-indirect-tax
description: >
  Use this Guide to classify and compute Brazilian ICMS, ISS and IPI for an individual
  professional, sole business or company carrying out a domestic sale, service, industrial
  operation or import in calendar 2026. It explains the tax base, responsible party,
  invoice evidence, input credits, service location, interstate rate route, final-consumer
  DIFAL and interaction with Simples Nacional. It covers ordinary transactions and
  identifies the additional state, municipal or product evidence needed for a calculation.
  Trigger phrases include ICMS, ISS, IPI, nota fiscal, NFS-e, interstate sale, service
  withholding and Brazilian indirect tax. Load brazil-vat for federal PIS/Cofins and
  the CBS/IBS transition, and br-simples-nacional for the unified small-business computation.
version: 3.1
jurisdiction: BR
tax_year: 2026
last_updated: 2026-11-11
category: international
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
depends_on:
  - income-tax-workflow-base
---

# Brazil ICMS, ISS and IPI v3.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

For a 2026 transaction, identify the taxpayer's own regime and the actual supply before choosing a rate. An individual professional can owe municipal ISS without being an ICMS trader; an individual importing goods can have an ICMS or IPI obligation even without habitual trading. Entity size, customer name and bank description do not establish the tax. [LC 116 arts.1,5; LC 87 arts.2,4; RIPI art.24](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html), [LC 87](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html), [RIPI](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html).

This Guide owns the ordinary ICMS/ISS/IPI computation and its evidence. [br-simples-nacional](br-simples-nacional.md) owns the eligibility limits, annexes, payroll ratio, sublimit timing and DAS computation. [brazil-vat](brazil-vat.md) owns PIS/Cofins and the 2026 CBS/IBS implementation. Use both when a transaction bears taxes from both systems; the new system does not erase the old tax liability merely because the year is 2026. [LC 214 art.348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

## Rates, bands and thresholds

Amounts are in BRL. These are national boundaries and an expressly identified São Paulo ordinary rate, not a nationwide internal-rate table.

| Item | 2026 rule and conditions | Official source |
|---|---|---|
| ISS maximum | 5% for services covered by LC 116; the actual municipal item/rate must be established | [LC 116 art.8II](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html) |
| ISS minimum | 2%; art.8-A§1 allows the stated minimum-load benefit exceptions for listed construction/repair and municipal transport services. Do not treat the range as a local rate election | [LC 116 art.8-A, list7.02,7.05,16.01](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html) |
| São Paulo ordinary internal ICMS | 18%, only where none of the section's product/transaction exceptions, exemption, reduction or other applicable special rules changes the result | [SP RICMS art.52I and section exceptions](https://legislacao.fazenda.sp.gov.br/Paginas/art052.aspx) |
| Goods dispatched from SP to N/NE/CO states or Espírito Santo | Ordinary interstate rate 7%, subject to the imported-goods rule and the actual operation/route; a delivery in SP can remain internal even if the customer's address is elsewhere | [SP RICMS art.52II,§§2–3](https://legislacao.fazenda.sp.gov.br/Paginas/art052.aspx) |
| Goods dispatched from SP to other South/Southeast states | Ordinary interstate rate 12%, subject to the same qualifications | [SP RICMS art.52III,§§2–3](https://legislacao.fazenda.sp.gov.br/Paginas/art052.aspx) |
| Qualifying imported goods on interstate sale | 4% for goods not industrialised after clearance or industrialised goods with import content above40%; exceptions include listed goods without national equivalent, qualifying basic production processes and imported natural gas | [Senate Resolution13/2012 arts.1–2](https://legis.senado.leg.br/norma/586999/publicacao?tipoDocumento=RSF&tipoTexto=ATU) |
| Fixed-asset ICMS credit | Ordinarily appropriated in1/48 monthly fractions with the taxable-output proportion and disposal/remaining-balance rules; not an immediate credit of the full purchase | [LC 87 art.20§5](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html) |
| General use/consumption ICMS credit | The general right in art.33I is deferred to1January2033; apply the actual 2026 category and exclusions rather than treating every business purchase as eligible | [LC 87 art.33I](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html) |
| IPI | Product-specific TIPI rate and notes; zero-rated and NT are different. Establish taxpayer/equivalent-industrial status and taxable event before applying the product rate | [RIPI arts.2,8–10,24,35,189](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html); [current RFB TIPI](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi.pdf) |
| Other state/municipal internal rates | Not a uniform national percentage. Resolve state, municipality, product/service item and transaction date before computing | [LC 87 arts.2,13](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html); [LC 116 arts.1,7–8-A](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html) |

For a route starting outside SP, establish that origin state's rule and the applicable Senate resolution; the SP rows do not certify another origin's rate. The previous lists for RJ, MG, BA, PR, RS and SC and the “IT services usually” municipal percentages are not a substitute for those sources. Their unconfirmed figures are listed at the end, so the geographical topics remain visible.

## The base

### Classify the supply, taxpayer and place

Apply these tests to each actual transaction, separating the seller's output liability from the purchaser's potential credit:

| Actual supply | Ordinary treatment and boundary | Official source |
|---|---|---|
| Sale of goods, including food/drinks supplied in bars/restaurants | Test ICMS, including exemptions, substitution and special goods regimes. A restaurant name does not turn food into an ISS service | [LC 87 art.2I](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html) |
| Service in the LC 116 list | Test ISS even if it is not the provider's main activity. Listed services ordinarily exclude ICMS except the list's express goods exceptions; split mixed supplies under their actual statutory item | [LC 116 art.1 and annex](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html); [LC 87 art.2IV–V](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html) |
| Intermunicipal/interstate transport or paid communication | Test ICMS. Municipal transport and listed services require their own ISS classification | [LC 87 art.2II–III](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html); [LC 116 list16](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html) |
| Software licensing/cession, including standard or customised software | The legacy ISS/ICMS distinction follows the STF software rulings: licensing/cession is subject to ISS, not a packaged-versus-custom ICMS shortcut. Check the actual contract and listed service; an imported contract adds the import rules | [STF RE688223, ADIs1945/5659](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=478136&ori=1%2F1000); [LC 116 list1.03–1.09](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html) |
| Manufacturing, processing, assembly or packaging | Test IPI industrialisation under arts.3–5 and all exclusions. A change of presentation can matter, but not every repair or restaurant food preparation is industrialisation | [RIPI arts.3–5](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html) |
| Resale by importer or industrial-equivalent establishment | Do not assume no IPI merely because this particular sale is a resale; establish the art.9/10 equivalence and taxable event | [RIPI arts.9–10,24,35](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html) |
| Salary/employment payment or loan principal | Not a service sale merely because cash moved. LC116art.2II–III excludes the specified employment and institutional credit amounts; separately identify any actual purchased professional/banking service | [LC 116 art.2 and list15](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html) |

ISS is ordinarily due at the provider's establishment, or domicile if there is no establishment, with the specific art.3 exceptions. Identify the establishment performing the activity, the service list item and the destination facts; the invoice customer's address alone is insufficient. Construction, cleaning, storage, events, municipal transport, supplied labour and imports have particular location rules. Financial/card/health-plan destination provisions also require the applicable constitutional case-law position; do not blindly copy historical text from a consolidation. [LC 116 arts.3–4](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html).

### Compute ordinary output and credits separately

**ISS.** Start from the service price under art.7 and its actual permitted exclusions. Obtain the municipal rate for the exact list item and period, and any fixed professional assessment or special regime. There is no ordinary input-credit subtraction resembling ICMS. Decide retention separately: municipal law may expressly assign responsibility, and art.6§2 identifies national responsible-party cases. A large corporate customer is not itself a retention rule. Record gross service value, assessed ISS, withholding, the actual liable party and net settlement; do not pay the same correctly retained liability twice. [LC 116 arts.6–8-A](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html).

**ICMS.** Use the actual statutory base in art.13, including its own tax and the specified freight, insurance, interest and related amounts. The normal invoice value is tax-inclusive: multiply a verified inclusive base by the applicable rate. Only an expressly tax-exclusive contractual input calls for a justified gross-up; do not apply rate/(1−rate) to a value already including ICMS. Import, mixed-supply and DIFAL bases have different provisions. [LC 87 art.13](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html).

For the regular debit/credit regime, total supported output debits, separately examine eligible credits, reversals, previous balances and state adjustments, then reconcile the balance to the actual state record. The right to a credit depends on eligible business use, tax treatment, valid documentation and bookkeeping. Exempt/non-taxed outputs and private/unrelated use can restrict or reverse credits; export exceptions differ. The mere presence of tax on an invoice does not prove the purchaser's right. [LC 87 arts.19–23](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html).

Energy credit is limited in 2026 to the statutory categories, including resale of energy, industrial consumption and proportional export use. Ordinary office use by an ICMS taxpayer does not automatically qualify. Communication credits similarly require the specified same-nature or export use until the general future rule. Apply the fixed-asset fraction separately; ordinary supplies for use/consumption are not automatically resale inputs. [LC 87 arts.20§5,33](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html).

**IPI.** Identify each establishment's industrial/importer/equivalent status, actual event and NCM/TIPI description, including complementary notes and applicable date. The normal method applies the TIPI rate to the applicable taxable value, not a universal product range. Domestic industrial output normally starts from the full operation value; import and equivalent-establishment values need art.190's own rules and later superior law/case law where relevant. Establish adjustments before computing. [RIPI arts.2,24,35,189–190](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html); [TIPI](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi.pdf).

Industrial/equivalent establishments can claim the qualifying IPI credits in arts.225–226, including qualifying raw materials, intermediate products and packaging used in taxed industrialisation, and the prescribed import/equivalent cases. Personal or fixed-asset purchases do not become basic industrial input credits by a business label. Segregate eligible credits, returns and required reversals from ICMS and PIS/Cofins credits. Product-specific incentives, suspension, exempt/zero output and special regimes need their actual rules; do not invent an IPI rate or credit from a bank purchase. [RIPI arts.225–226](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html).

### Final-consumer DIFAL, substitution and Simples

For an interstate supply to a **final consumer**, establish whether the recipient is an ICMS taxpayer. Under LC87art.4§2, the taxpayer recipient is responsible for the stated differential in its case; for a non-taxpayer final recipient, the sender/provider is responsible. A purchase for resale is not final consumption simply because it is B2B. Asset/use purchases can differ from resale. Check art.13IX/X and §§3,6–7 for the correct base, destination law, FECP and procedural obligation. The difference of nominal rates alone is not a complete national calculation. [LC 87 arts.4§2,13](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html).

For ICMS-ST or advance collection, preserve the product, NCM/CEST, agreement, state rule, MVA/base, responsible party and invoice evidence. Do not assume ST from a retailer's name, nor assume its absence when NCM is missing. LC87arts.6–9 provide the national substitution framework; the actual state/agreement computation is needed. [LC 87 arts.6–9](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html).

For an actual Simples seller, segregate revenue under [br-simples-nacional](br-simples-nacional.md). ST/advance ICMS, imports, specified interstate acquisitions, retained/imported ISS and other art.13§1 exceptions can be outside DAS. Exceeding a sublimit has its own timing rules and does not always exclude the business from federal DAS immediately. A regular purchaser's limited ICMS credit on qualifying Simples goods requires commercialisation/industrialisation, the statutory amount and invoice conditions; it is not the supplier's full ordinary state rate. [LC 123 arts.13§1,18,20,23](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

### Workpaper and bank reconciliation

Use an evidence-led transaction sheet: date and assessment period; taxpayer/establishment; counterparty; contract/invoice key; actual goods or service; NCM/list item; origin/destination; final-use and recipient status; own regime; inclusive/exclusive base; rate source/date; output tax; separately eligible credit; retained tax and responsible party; paid amount; unresolved item. Then reconcile monthly revenue, output debits, credits/reversals, withholding and payment references in separate ISS/ICMS/IPI summaries. Add a Simples segregation sheet where applicable and a reviewer exception list. This is a working-paper design, not a statutory return format.

Itaú, Bradesco, Banco do Brasil, Caixa, Santander, Nubank, Inter and C6 statements may be supplied in different exports; inspect the actual columns, dates, decimal separators and credit/debit conventions rather than assume a bank-specific layout. PIX, TED, historical DOC, boleto and card settlement describe payment channels. DAS, DARF, SEFAZ and prefeitura text suggest a tax payment but require the actual taxpayer, code, period and receipt. A tax payment is not a creditable purchase. Loan principal, owner's capital, transfers, personal drawings and cash withdrawals need reconciliation rather than automatic revenue/expense treatment. Keep bank names and terms as search clues, not legal classifications.

Revenue through a marketplace must be reconciled between the underlying sale, seller's gross consideration, platform fees, withheld amounts and net settlement. Professional services, commercial rent, energy, telecom and transport costs need separate tax-specific credit tests; a rent payment's absence of ISS does not decide federal contribution credits. Use [brazil-vat](brazil-vat.md) for those PIS/Cofins questions.

## Deadlines and filing

The state SEFAZ administers ICMS, the competent municipality administers ISS, and Receita administers IPI. The applicable jurisdiction, registration, regime and transaction determine the actual return, deadline and payment reference. Obtain that official obligation/calendar before presenting a payable schedule; neither invoice date nor a bank debit supplies the filing deadline. [LC 87 arts.23–24](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html); [LC 116 arts.3,6](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html); [RIPI art.1](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html).

1. Confirm registrations and period, then retrieve the actual NF-e/NFC-e/NFS-e/CT-e or import record and authorised/cancelled status. Goods, retail-consumer and transport documents have different roles. The recognised models include NF-e55, NFC-e65 and CT-e57; NFS-e is the service document. [Joint Act1/2025 art.2](https://cgibs.gov.br/upload/arquivos/202609/09104120-ato-conjunto-rfb-cgibs-n-1-de-22-de-dezembro-de-2025.pdf).
2. Apply the relevant tax calculations and reconcile the fiscal books/actual state or municipal return, including credits, retention and outside-DAS liabilities. For an opted business, use the separate Simples workflow. Do not manufacture local form boxes from a generic national template.
3. Check the actual payment guide, taxpayer, assessment period, due date, principal and charges. Retain submitted declaration/receipt and payment confirmation as separate evidence. A generated guide is not proof of payment or accepted filing.
4. Check the 2026 CBS/IBS accessory-duty schedule and waiver conditions in [brazil-vat](brazil-vat.md). Joint Act4's new-system dates do not suspend existing legacy invoices or payments. [Joint Act1 art.4](https://cgibs.gov.br/upload/arquivos/202609/09104120-ato-conjunto-rfb-cgibs-n-1-de-22-de-dezembro-de-2025.pdf); [Joint Act4 art.1](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf).

## Penalties and interest

Keep the principal, late-payment interest, late-filing penalty and assessment penalty separate. ICMS/ISS rates and deadlines depend on the actual local legislation and period; specific exemptions, disputes and suspended enforceability need documents. No national late-charge percentage for these local taxes is certified here. IPI charges likewise require the applicable federal provision and factual event before being quantified. Preserve the old ST/incentive/dispute referrals and flag an unverified charge instead of applying a guessed maximum. These unconfirmed amounts are expressly listed in Sources.

For new-system 2026 accessory-duty failures, use the distinct cure and compliance rules in [brazil-vat](brazil-vat.md); they do not waive unrelated legacy debts. [LC 214 art.348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm); [Joint Act1 art.4](https://cgibs.gov.br/upload/arquivos/202609/09104120-ato-conjunto-rfb-cgibs-n-1-de-22-de-dezembro-de-2025.pdf).

## Cross-border points

Goods exports have the LC87art.3II nonincidence, with the law's documentation and export-related credit treatment. Services paid by a foreign customer are not automatically ISS exports: LC116art.2's sole paragraph denies the export rule for services developed in Brazil whose result occurs there. Determine the actual foreign destination/result and supporting contract. [LC 87 arts.3,20–21](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html); [LC 116 arts.1–3](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html).

Imports of goods can attract ICMS even for a nonhabitual individual, and IPI at customs clearance. The bases differ; obtain the customs declaration, product and all applicable components. Imports of services also require the LC116 place/responsibility tests, with federal import contributions, withholding, CIDE and IOF considered separately through [brazil-vat](brazil-vat.md). No foreign supplier brand or currency conversion alone establishes the taxes. [LC 87 arts.2,4,13](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html); [RIPI arts.24,35,190](https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html); [LC 116 arts.1§1,3I,6§2I](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html).

## Two worked examples that recompute

### Ordinary SP regular-regime goods calculation

Assume an established SP trader, outside Simples, makes ordinary taxable internal sales with a verified18% rate and no ST, exemption, reduction or IPI-equivalent issue. Tax-inclusive output bases total100,000. Supported eligible resale purchases have an inclusive base60,000 and highlighted18% tax. There are no other balances or adjustments. SP art.52I supplies the ordinary rate; LC87arts.13,19–23 govern base and eligible credit. Output18,000 less eligible10,800 leaves7,200. If the purchase use or documentation fails the credit conditions, this result does not follow. [SP art.52I](https://legislacao.fazenda.sp.gov.br/Paginas/art052.aspx); [LC 87](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html).

```oa-check
name: Ordinary SP ICMS with eligible resale credits
inputs:
  sales_inclusive: 100000
  eligible_purchases_inclusive: 60000
  rate: 0.18
steps:
  - output: sales_inclusive * rate
  - credit: eligible_purchases_inclusive * rate
  - payable: output - credit
expected:
  output: 18000
  credit: 10800
  payable: 7200
```

### Decide whether an SP to BA sale is final-consumer DIFAL

Assume ordinary domestic goods genuinely dispatched from SP to BA, with a verified7% interstate rate and inclusive base10,000. If the buyer acquires them for resale, the seller's interstate debit is700 and no final-consumer DIFAL follows from that resale fact. If instead the same buyer acquires for its own use or fixed asset, check the final-consumer rule and recipient taxpayer status before computing a differential. The responsible party, actual destination base/rate and FECP must be established; this example deliberately does not substitute an unverified BA internal rate. The supported resale result is700; the final-use alternative requires the missing destination facts before its additional tax can be quantified. [SP art.52II](https://legislacao.fazenda.sp.gov.br/Paginas/art052.aspx); [LC 87 arts.4§2,13](https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html).

```oa-check
name: SP to BA ordinary resale versus final-use decision
inputs:
  invoice_base: 10000
  interstate_rate: 0.07
  supported_final_consumer_difal_on_resale: 0
steps:
  - interstate_debit: invoice_base * interstate_rate
  - supported_tax_on_resale: interstate_debit + supported_final_consumer_difal_on_resale
expected:
  interstate_debit: 700
  supported_tax_on_resale: 700
```

The earlier ISS illustrations remain arithmetic-only checks once actual local facts are established: a supported service-price base50,000 at a verified5% gives2,500; a supported retained-ISS invoice20,000 at that rate gives1,000 tax and19,000 cash before other deductions. Here5% is an assumed actual local rate within the national ceiling, never a default or proof of a municipality's law. Determine who remits under art.6 before counting the retained liability as settled. [LC 116 arts.6–8](https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html).

## Ask the client first

- Which taxpayer and establishment, own regime, registrations, activity and assessment period are involved? Obtain actual election and prior returns rather than infer from the customer. If Simples applies, obtain RBT12 and its domestic/export history for the computation in br-simples-nacional.
- What is supplied, with invoice/contract, registered CNAE as activity evidence, NCM or LC116/local service item, industrial/importer status and gross/net price components? CNAE alone does not decide the tax classification.
- Where do goods move or services occur/result, and is an interstate purchaser an ICMS taxpayer acquiring for resale, production, asset or final use?
- Which exact local/product rule sets the rate/base, exemption, ST/MVA, retention or special professional assessment for that date?
- Which supported credit balances, business uses, valid fiscal documents, reversals, withholding and actual payments must be reconciled?

If a required local rate, credit right, ST agreement or import basis is missing, state the conditional national treatment and pause only that computation. Continue reconciliations and supported ordinary calculations. Refer complex IPI/ZFM/incentive disputes and contested local positions with the actual issue and documents; do not reject every ordinary 2026 reform question as unresolved.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| LC116: arts.1–8-A; software/financial service items; place, export and retention exceptions read | https://www2.camara.leg.br/legin/fed/leicom/2003/leicomplementar-116-31-julho-2003-492028-normaatualizada-pl.html | 2026-11-11 |
| LC87: arts.2–9,13,19–24,33; incidence, final consumer, substitution, bases and credit restrictions read | https://www2.camara.leg.br/legin/fed/leicom/1996/leicomplementar-87-13-setembro-1996-370965-normaatualizada-pl.html | 2026-11-11 |
| SP RICMS: art.52 current operative wording, imported/territorial exceptions and listed exception framework read; historical versions distinguished | https://legislacao.fazenda.sp.gov.br/Paginas/art052.aspx | 2026-11-11 |
| Senate Resolution13: complete arts.1–3, import-content exceptions and natural gas read | https://legis.senado.leg.br/norma/586999/publicacao?tipoDocumento=RSF&tipoTexto=ATU | 2026-11-11 |
| RIPI, Decree7212: arts.2–5,8–10,24,35,189–190,225–226 read; product-specific exceptions require their actual additional rule | https://www2.camara.leg.br/legin/fed/decret/2010/decreto-7212-15-junho-2010-606731-normaatualizada-pe.html | 2026-11-11 |
| RFB TIPI: current compilation cover/update list and notes framework read; no product-specific rate asserted | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi.pdf | 2026-11-11 |
| LC123: arts.3,13,18–20,23; Simples interactions and outside-DAS/credit conditions read | https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html | 2026-11-11 |
| STF software ruling: official RE688223 account, ADIs1945/5659 scope and effective-date discussion read | https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=478136&ori=1%2F1000 | 2026-11-11 |
| LC214 as amended by LC227: art.348 and staged operation read; transition computation owned by brazil-vat | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm | 2026-11-11 |
| Joint Act1/2025: whole act, recognised fiscal models and preserved legacy duties read | https://cgibs.gov.br/upload/arquivos/202609/09104120-ato-conjunto-rfb-cgibs-n-1-de-22-de-dezembro-de-2025.pdf | 2026-11-11 |
| Joint Act4/2026: whole act, document phases and Simples/import exceptions read | https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf | 2026-11-11 |

Not yet confirmed: a current product-specific internal ICMS/FECP table for RJ, MG, BA, PR, RS and SC; municipal SP/RJ service-specific rates and the old “IT usually” or default percentages; destination-specific DIFAL bases, guides and rates; applicable ST agreements/MVA by product/state; a selected IPI product's current TIPI rate, incentive and complex import valuation; local fixed professional ISS assessments; exact state/municipal return boxes/calendars and late-charge amounts; current bank-specific export layouts. These topics remain covered by the decision and evidence steps above, but no unverified amount is supplied for a filing.

**General reference.** This Guide has not received accountant approval for this version. Review the taxpayer's facts and the applicable current official provisions before filing or paying.
