---
name: slovakia-vat-registration-4-7-7a
description: "Which Slovak VAT registration a client needs in 2026 under Act No. 222/2004 Coll.: § 4 (VAT payer, EUR 50,000 calendar-year turnover for payer status from 1 January of the next year, EUR 62,500 for payer status at the crossing supply, application within five working days), voluntary § 4 registration, § 7 (goods from other member states, EUR 14,000) and § 7a (cross-border services, no threshold), and why a § 7 or § 7a registrant self-assesses VAT but cannot deduct it. Covers the 2025 change from EUR 49,790 over 12 months to the calendar-year test, decision times, and the fine for late registration. Trigger on: Slovak VAT registration, registracia DPH, platitel dane, § 7a, IC DPH, Meta or Google Ireland invoices Slovakia. Out of scope: the periodic return, rates, control statement and penalties (slovakia-vat-return), income tax (slovakia-pit)."
version: 1.2
jurisdiction: SK
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia VAT registration (§4, §7, §7a), 2026

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team. The 2026 VAT Act and the Tax Procedure Code were read on 27 October 2026. Article references below are to Act No. 222/2004 Coll. unless another act is named. The Financial Administration (Finančná správa SR) administers VAT.

Section 4 gives VAT-payer status (platiteľ), with output-tax and conditional input-deduction rights. Sections 7 and 7a give a VAT number for specified cross-border obligations without making the person a payer. A small business can owe recipient-accounted VAT before it reaches the domestic turnover threshold. The periodic return, detailed rate scopes, control statement and late-return penalties are in [slovakia-vat-return](slovakia-vat-return.md); income tax is in [slovakia-pit](slovakia-pit.md).

## Who this applies to

- Slovak sole traders (SZČO), s.r.o.s and other taxable persons with the domestic establishment or residence connection in §4(1), approaching the turnover threshold or considering voluntary registration.
- Freelancers and small agencies buying business services from EU platforms or supplying services to business customers in other member states. Section 7a has no monetary threshold.
- A taxable person not required to apply under §4 or §5, or a non-taxable legal person such as a sports club or foundation, acquiring goods from another member state: test §7 and §11.
- Businesses using older guidance must distinguish historical rules from current ones. The EUR 49,790 rolling-period threshold and 20% standard rate are historical, not the 2026 rules.

A non-established foreign business tests §5 and its exceptions; the domestic §4 thresholds are not a universal foreign-business exemption. Section 4(1)(i) also has a separate rule for a person with only a Slovak fixed establishment, subject to its foreign-small-enterprise exception. This Guide covers §5 only where it interacts with the three registrations above.

## Rates, bands and thresholds

| Item | Rate, amount or boundary | Year | Official source |
|---|---|---|---|
| Standard VAT rate | 23% | 2026 | VAT Act §27(1), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Reduced rates; the applicable goods/services must qualify | 19% and 5%; scope changed on 1 January 2026, see the return Guide | 2026 | §27(2), (3) and Annexes 7/7a, https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Ordinary domestic §4 threshold | Turnover **exceeds** EUR 50,000 in the calendar year: payer from 1 January of the next year, subject to earlier statutory triggers/election | 2026 | §4(1)(a), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Immediate domestic §4 threshold | Turnover **exceeds** EUR 62,500: payer from the supply causing the excess, including that supply | 2026 | §4(1)(b), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Turnover measurement period | Calendar year, restarting on 1 January | From 2025 | §4(1), (15), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html; FS registration method §1.5 |
| §7 goods-acquisition threshold | **Reaches** EUR 14,000, excluding VAT, in the calendar year | 2026 | §7(1), §11(4) to (6), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Voluntary acquisition taxation | At least two calendar years | 2026 | §11(7), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| §7a cross-border service threshold | None | 2026 | §7a(1), (2), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| §7/§7a deduction | No input deduction as a non-payer; a VAT number alone does not confer it | 2026 | §49(1), (2), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Non-payer's minimum payment | Tax of **not more than EUR 5** need not be paid; this does not remove the return or registration duty | 2026 | §78(3), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Quarterly period for a §4 payer | More than 12 calendar months since the end of the month of becoming a payer, with prior-12-month turnover **below EUR 100,000** | 2026 | §77(1), (2), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Historical domestic registration threshold | EUR 49,790 over up to 12 preceding consecutive calendar months; transitional cases preserved by §85kn | To 2024 | Historical §4(1), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20240101.html; current §85kn, https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Historical standard rate and registration decisions | 20%; §7/§7a decision within seven days | To 2024 | Historical §27(1), §7(3), §7a(3), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20240101.html |

The words matter: exactly EUR 50,000 or EUR 62,500 does not exceed the respective §4 threshold, while exactly EUR 14,000 reaches the §7 threshold. A §7/§7a registrant does not add Slovak VAT to ordinary domestic sales merely because it has an IČ DPH. If a supplier wrongly states VAT on an invoice, §69(5) separately makes that VAT payable.

## The taxable base

**The §4 turnover calculation.** Start with the value excluding VAT of goods and services supplied with their place of supply in Slovakia (§4(15)). Exclude supplies exempt under §28 to §36 and §40 to §42. Insurance (§37), property (§38) and financial services (§39) are generally included, but ancillary insurance and financial services supplied with another supply are excluded. Also exclude occasional disposals of tangible assets other than stock and occasional disposals of intangible assets. If the threshold is crossed exclusively through §37 to §39 exempt supplies, state that on the application (§4(3)); do not assume exemption eliminates registration.

Advance payments are not turnover until the supply occurs; supplies placed abroad and free supplies are outside the ordinary turnover count (FS method §1.5). The method's reverse-charge exclusion concerns supplies **received as buyer**, not a blanket exclusion for the business's own domestic sales. Purchases on which the business self-accounts are not its sales turnover. The supplier's own domestic supplies remain subject to §4(15). The property-specific advance-payment trigger in §4(1)(f), (g) must still be checked: an advance for a building, part of a building or building land can create payer status before delivery where the statutory condition is met.

**The two domestic turnover triggers.** Above EUR 50,000, payer status ordinarily starts on 1 January of the following year (§4(1)(a)); above EUR 62,500 it starts with the supply causing the excess (§4(1)(b)). That entire supply is taxed at its applicable rate, not merely the excess above the threshold (FS method §2.1). Legal succession, acquiring a payer's business or an independent business part, demergers and the other events in §4(1)(c) to (i) have their own status dates. Test those facts before applying the ordinary next-year rule.

**Historical transition.** Before 2025 the threshold was EUR 49,790 measured over up to twelve preceding consecutive calendar months. Section 85kn(1) preserves the former application/authority procedure for persons who reached that old threshold by 31 December 2024. The modern test uses a calendar year; historical 20% rates and seven-day §7/§7a decisions must not be applied to 2026 transactions.

**Voluntary §4 registration.** Before exceeding EUR 50,000, a person can apply under §4(6)(a), (7). It must be a taxable person carrying on economic activity. The authority's method recognises preparatory acts before the first sale, supported by evidence and the CJEU authorities C-110/94 INZO, C-268/83 Rompelman and C-527/11 Ablessio. Registration is effective on the date in the decision, with a 21-day decision limit; this ordinary voluntary route is not backdated before the application/decision (FS method §2.5). A fraud-based refusal requires objective evidence and an overall assessment, as explained in that method, rather than an unsupported assumption about the applicant.

After turnover has exceeded EUR 50,000 but before it exceeds EUR 62,500, §4(8) supplies two distinct early-status elections: mark the application to become a payer from the supply which exceeded EUR 50,000 (§4(8)(a)); or, **after the registration decision has been delivered**, notify an election taking effect the day after notification (§4(8)(b)). The first election is a separate statutory route and is not defeated by the ordinary voluntary no-backdating rule.

**Goods acquisitions under §7.** Apply before the acquisition taking the calendar-year net total to EUR 14,000 (§7(1)). The §11(4)(b) below-threshold exemption requires the threshold not to have been reached in the preceding year or the current year. New means of transport and excise goods are excluded from that count (§11(6)), but have their separate tax rules, so excluded from the count does not mean tax-free. Voluntary acquisition taxation below EUR 14,000 is allowed but binds the acquirer for at least two calendar years (§7(2), §11(7)). Section 7(4) avoids a duplicate application where the person is already registered under §7a or §4(7); it does not replace the acquisition-tax test.

**What the number changes.**

| Obligation/right | §4 VAT payer | §7/§7a registrant who is not a payer |
|---|---|---|
| Ordinary Slovak sales | Charge the applicable 23%, 19% or 5%, subject to exemption/reverse-charge rules | Do not charge Slovak VAT solely because of this registration |
| Input VAT | Deduct only under the eligibility/document conditions in §§49 to 51 | No ordinary input deduction |
| Foreign-service reverse charge | Self-assess where §69 applies; eligible credit can offset it | Self-assess where §69 applies; VAT is an unrecoverable cost |
| VAT returns | Each tax period, with the exclusively-exempt exception in §78(2)(a)(2) | Only months in which a tax liability arises; no nil returns (§78(3)) |
| IČ DPH | Payer VAT number | Number for the relevant registration purposes; not payer status |

For example, EUR 1,000 of taxable Meta Ireland advertising produces EUR 230 of Slovak reverse-charge VAT at 23%. A non-payer registrant cannot deduct it. A full payer using it wholly for deductible activity can self-assess EUR 230 and deduct EUR 230 under §49(2)(b), subject to §51. Voluntary registration affects both sale prices and input costs: if the business keeps a net price on a standard-rated sale, a consumer or exempt customer pays 23% more; if the gross contract price stays fixed, the supplier's net revenue falls instead.

## Deadlines and filing

| Action | Statutory time | Official source |
|---|---|---|
| §4 application after the relevant threshold/status trigger | Five working days; identify the event and date | §4(2), (3), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Mandatory §4 decision and number | Within ten days of receipt; for §4(4)(b)(2), the application and required evidence govern the start | §4(4), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html; FS method §2.3 |
| Ordinary voluntary §4 decision | Within 21 days | §4(7), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| §7 application | Before the threshold acquisition | §7(1), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| §7a application | Before receiving/supplying the qualifying service | §7a(1), (2), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| §7/§7a decision/number | Within ten days of receipt | §7(3), §7a(3), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Non-payer's reverse-charge return and payment | Within 25 days after the month of liability; no nil returns; payment exception up to EUR 5 | §78(3), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| New §4 payer's period and ordinary return/payment | Calendar month; return/payment within 25 days after period end | §77(1), §78(1), (2), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Qualifying quarterly payer election | Notify within 25 days after the month conditions are met; quarter starts under §77(3) | §77(2), (3), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| §7/§7a EC Sales List for reportable services supplied | Quarterly, within 25 days after quarter end; no nil list | §80(3), (5), (9), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Invoice for §15(1) service placed in another member state | Within 15 days after month-end of supply or advance; reverse-charge wording where customer is liable | §72(2), §73(1)(d), §74(1)(k), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Ordinary non-payer invoice retention | Ten years following the year concerned | §76(2), (3), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Deadline ends on Saturday, Sunday or public holiday | Next working day | Tax Procedure Code §27(4), https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html |

After an application following EUR 50,000 turnover, a later immediate-payer event before year-end must be notified **without delay**, giving its date (§4(5)). If EUR 62,500 is exceeded within the initial five-working-day application window before the first application was filed, the special application rule in §4(2)(c) applies. Do not submit an application on the assumption that status can wait until next January.

If the EUR 50,000 applicant needs a §7/§7a number before next January and has none, notify before the triggering transaction. Section 4(11) establishes the interim §7/§7a status from the day after notification if the decision was already delivered, or from delivery of that decision if it was not. An existing §7/§7a number is reused on becoming a payer (§4(12)). The decision date, payer-status date and number's effective date must be distinguished (§4(4), §5a). A timely applicant without its number by the first return deadline uses the five-working-day-from-decision rule in §78(2)(a)(1); §73(2) has a corresponding invoice rule.

A §7/§7a registrant keeps records of its EU acquisitions, outgoing §15(1) services to other member states, and received services for which it owes tax (§70(4)), and retains invoices for the statutory period. The outgoing EU B2B service invoice carries “prenesenie daňovej povinnosti” where the customer is liable. The EU invoice deadline is measured from **month-end**, not fifteen days from each invoice date. A third-country §15(1) service invoice follows §72(2) and the applicable ordinary §73 timing.

**Ending registration.** A §4 payer can request deregistration after at least one calendar year from becoming a payer if the preceding calendar year's turnover did not exceed EUR 50,000 (§81(1)(a)). A §7 registrant can apply when net EU acquisitions stay below EUR 14,000 in both the current and preceding year (§82(1)), subject to the two-year voluntary-taxation commitment. A §7/§7a registrant must apply without delay on ending Slovak business, and those limited registrations are cancelled on becoming a payer (§82(2), (3)). A later credit note reducing turnover below the threshold does not by itself reverse status already confirmed by decision (FS method §2.3, example 6).

## Penalties and interest

| Failure | Consequence | Official source |
|---|---|---|
| Registration obligation missed | EUR 100 to EUR 30,000; a tax/customs office does not impose a range-based fine on the first breach under §155(4) | Tax Procedure Code §154(1)(b), §155(1)(c), (4), https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html |
| Payer failed to register and missed returns/control statements | File every required missed period in chronological order from the first; non-registration does not erase tax | VAT Act §78(9), §78a(14), https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html |
| Tax paid late | Daily interest using four times the ECB basic rate at the statutory reference date, with a 15% annual minimum; subject to §156's limits and exceptions | Tax Procedure Code §156(1), (2), (6), https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html |

The same registration-fine range and first-breach rule were read in both 2026 Tax Procedure Code versions, January to August and September to December. First-breach fine relief does not excuse filing, payment or interest. A non-payer who missed a §7/§7a obligation still accounts for tax under §69 and files under §78(3). Full late-return and control-statement penalties are in the return Guide.

A refusal of a purported compulsory registration under §4(10)(a) cannot be appealed. A refusal of an ordinary voluntary application under §4(10)(b) can be appealed (FS method §2.5). Positive registration decisions under §4(4), (7), §7(3) and §7a(3) have their statutory no-appeal rules (§4(9), §7(3), §7a(3)); do not confuse these with a voluntary refusal or an ex-officio procedure.

## Cross-border points

**Services under §7a have no monetary safe harbour.** A taxable person not required to apply under §4 must apply before receiving a service from a foreign person in another member state for which it owes tax under §69(3), or before supplying a §15(1) service placed in another member state for which the customer owes tax (§7a(1), (2)). A business spending only EUR 1 can still trigger registration. For EUR 30 of ordinary taxable EU advertising at 23%, the VAT is EUR 6.90: registration is still required before the service, and the liability month requires a return and payment under §78(3). A freelancer earning EUR 100,000 exclusively from ordinary §15(1) services to German business establishments can have zero domestic turnover and still require §7a registration.

Identify the actual contract supplier/customer and the establishment involved. Meta Ireland, Google Ireland, Amazon Luxembourg, Stripe Ireland or a Czech subcontractor are prompts to inspect the invoice, not proof that every service is taxable. Check the nature of the service, §15/§16 place of supply, exemption and whether an EU foreign supplier uses the §68f(2) small-enterprise exemption expressly excepted by §69(3). An exempt financial service is not made taxable by a platform brand.

Section 7a's general-service route does not apply to a service placed under §15(2) or §16, an exempt service, or an actual third-country counterparty; an existing §7 registration avoids a separate §7a application. For customer status, §15(4)(b) treats a VAT-identified non-taxable legal person as taxable for the service-place rules. Thus “not a taxable person” is not a sufficient conclusion without checking that deeming rule. The special-place service can still produce a tax duty under §69(2), even though it is outside the §7a route.

**Third-country services.** An ordinary taxable service received by the Slovak business from a US, UK or Swiss business and placed in Slovakia under §15(1) produces recipient liability under §69(3), despite not itself requiring §7a registration. File and pay under §78(3). Conversely, ordinary §15(1) business services supplied to a third-country establishment are placed abroad, do not count as Slovak §4 turnover and do not trigger §7a; the invoice requirement under §72(2) remains. Registration and the tax liability are separate questions.

## Worked examples

### Example 1: Jana's first EU service, unrecoverable VAT, then full-payer credit

Jana is an SZČO web developer in Košice, not a VAT payer on 1 January 2026. In January she receives EUR 200 of ordinary taxable advertising from Meta Platforms Ireland Ltd, with no earlier advance and no applicable small-enterprise exemption. Its place is Slovakia under §15(1), and she owes the tax under §69(3).

She must apply under §7a **before receiving the first service**, regardless of amount. She self-assesses EUR 200 × 23% = EUR 46, files the January return and pays by 25 February 2026 (§78(3)). EUR 46 is above the EUR 5 payment exception. She cannot deduct it, so her advertising costs EUR 246. Her ordinary Slovak client invoices remain without VAT: §7a has not made her a payer.

If the actual supplier were a US business, the same facts produce EUR 46 tax and a return, but no §7a registration trigger. Once Jana is a §4 payer with the number and documentation required by §51, an equivalent later EUR 200 service used wholly for deductible activity produces EUR 46 output and EUR 46 input VAT, a zero net effect and EUR 200 cost. This later-service credit does not automatically reopen the January return. Any claim for pre-registration inputs must separately satisfy §55(1), (2), including its first-period, expense-year and general deduction conditions (§49(2)(b), §51).

```oa-check
name: SK first EU service as non-payer and equivalent service after payer registration, 2026
inputs:
  service_net: 200
  rate: 23
steps:
  - output_vat: round(service_net * rate / 100, 2)
  - nonpayer_credit: 0
  - nonpayer_tax: output_vat - nonpayer_credit
  - nonpayer_cost: service_net + nonpayer_tax
  - payer_credit: output_vat
  - payer_net_vat: output_vat - payer_credit
  - payer_cost: service_net + payer_net_vat
expected:
  output_vat: 46.00
  nonpayer_tax: 46.00
  nonpayer_cost: 246.00
  payer_net_vat: 0.00
  payer_cost: 200.00
```

### Example 2: Jana's December turnover, the crossing invoice and net/gross prices

Jana supplies ordinary web-development services to Slovak clients for EUR 4,500 a month and to a German business agency at its German establishment for EUR 2,000 a month. The latter services follow §15(1), so those German fees do not enter Slovak turnover. Assume no special §4 trigger or early-status election.

| Date | Domestic supplied value | Cumulative domestic turnover |
|---|---|---|
| January to November 2026 | 11 × EUR 4,500 | EUR 49,500 |
| 10 December 2026, ordinary variant | EUR 4,500 | EUR 54,000 |

On the ordinary variant she exceeds EUR 50,000 but remains below EUR 62,500. She applies within five working days of 10 December and becomes a payer on 1 January 2027. The 10 December supply is invoiced without VAT (§4(1)(a), (2)).

If instead the 10 December project is **EUR 14,000 net**, domestic turnover is EUR 63,500. Payer status starts with that supply, and the entire EUR 14,000 is taxed at 23%: EUR 3,220 VAT, EUR 17,220 total (§4(1)(b), §22(1), §27(1)). Do not tax only the EUR 1,000 excess over EUR 62,500. The five-working-day application follows the status trigger; if a prior application had already been filed, notify the changed status without delay under §4(5).

**Fixed gross-price comparison.** Once payer status applies to a standard-rated supply, a contract fixed at EUR 14,000 **including VAT** yields EUR 14,000 / 1.23 = EUR 11,382.11 net and EUR 2,617.89 VAT. This is the price-extraction rule in §22(1), not authority to reverse an already-established registration trigger. For comparison, the old calculation EUR 49,500 + EUR 11,382.11 = EUR 60,882.11 is retained here only as arithmetic; its claimed conclusion that the same fixed-price crossing supply cannot create payer status is specifically unconfirmed below. Contracts near a threshold need an express agreement on whether the customer pays VAT in addition to the price.

```oa-check
name: SK domestic thresholds and net versus fixed-gross invoice prices, 2026
inputs:
  domestic_monthly: 4500
  earlier_months: 11
  ordinary_december: 4500
  alternative_project_net: 14000
  fixed_gross_price: 14000
  rate: 23
steps:
  - turnover_before: domestic_monthly * earlier_months
  - ordinary_turnover: turnover_before + ordinary_december
  - ordinary_excess_50000: ordinary_turnover - 50000
  - ordinary_room_to_62500: 62500 - ordinary_turnover
  - alternative_turnover: turnover_before + alternative_project_net
  - alternative_excess_62500: alternative_turnover - 62500
  - project_vat: round(alternative_project_net * rate / 100, 2)
  - project_total: alternative_project_net + project_vat
  - gross_price_net: round(fixed_gross_price / (1 + rate / 100), 2)
  - gross_price_vat: fixed_gross_price - gross_price_net
expected:
  turnover_before: 49500.00
  ordinary_turnover: 54000.00
  ordinary_excess_50000: 4000.00
  ordinary_room_to_62500: 8500.00
  alternative_turnover: 63500.00
  alternative_excess_62500: 1000.00
  project_vat: 3220.00
  project_total: 17220.00
  gross_price_net: 11382.11
  gross_price_vat: 2617.89
```

## Ask the client first

1. What was supplied, when, and where was its VAT place of supply? Separate domestic turnover, foreign §15(1) services, acquisitions and special-place services. What is cumulative qualifying turnover from 1 January, and were either EUR 50,000 or EUR 62,500 exceeded? Any property advances, business acquisition or succession event?
2. Has the business received a service from another EU member state, and when was the first service or advance? Inspect the actual legal supplier, exemption and receiving establishment.
3. Has it supplied §15(1) services to business customers in another member state where the recipient owes tax? Which VAT numbers and establishment received the service?
4. What are net EU goods acquisitions in the current and previous calendar years? Any new means of transport, excise goods or voluntary acquisition-tax election?
5. Do customers recover VAT, and are contracts net plus VAT or fixed gross? What deductible input and pre-trading costs support voluntary registration?
6. Which applications, decisions, notifications and VAT numbers already exist, with what dates? Any 2024 transition, unfiled liability month or requested deregistration?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act 222/2004, full 2026 version: §§3,4,5a,7,7a,11,15,19,22,27,49,51,55,70,72–74,76–78a,80–82,85kn | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html | 2026-10-27 |
| Tax Procedure Code 563/2009, full version September to December 2026: §§27,154–156 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-27 |
| Tax Procedure Code, full version January to August 2026: same relevant fine/first-breach and timing rules checked | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260101.html | 2026-10-27 |
| FS SR registration method 2/DPH/2025/MP, 22 September 2025: economic activity/preparatory acts, turnover, status, voluntary timing, credit-note and appeal treatment | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Metodicke_pokyny/Nepriame_dane/2025/2025.09.22_002_DPH_2025_MP.pdf | 2026-10-27 |
| Historical VAT Act, 2024 version: §4(1), §7(3), §7a(3), §27(1); not used as current law | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20240101.html | 2026-10-27 |
| FS SR §7 information sheet, historical 2018 procedure | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DPH/2018/2018.06.19_DPH_reg_par7.pdf | 2026-10-27 |
| FS SR §7a information sheet, historical 2018 procedure | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DPH/2018/2018.06.18_DPH.pdf | 2026-10-27 |

The two historical 2018 sheets remain published, but their 20% rate and seven-day registration decisions are outdated. The 2026 statute sets 23% and ten days; current statutory provisions support the procedures above. The former Guide also linked the authority's January 2025 consolidation, rates page and registration overview; those references are retained here for their history: https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Sprievodca/Sprievodca_danami/2025/2025.01.28_zakon_DPH.pdf ; https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/sadzby-dane ; https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/registracna-povinnost-pre-dph . Current figures above are sourced to the full 2026 Act.

Not yet confirmed: the current registration form version and identifiers; the former example's specific conclusion that extracting EUR 2,617.89 VAT from a fixed EUR 14,000 crossing price at EUR 49,500 prior turnover prevents §4(1)(b) payer status (the statutory net-value test and gross-price arithmetic were read, but an official interpretation resolving that exact circularity was not obtained).

> Contributed by Michael Cutajar.

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
