---
name: nl-tax-objection
description: "Dutch national tax objections (bezwaar), protective objections, assessment/payment deadlines, hearings, payment postponement, collection interest, costs, late decisions and court appeals (beroep), for 2026. Includes two recomputing cases. Special, mass-objection and unresolved eligibility issues require a partner accountant. Triggers: bezwaarschrift, bezwaartermijn, pro forma bezwaar, uitspraak op bezwaar, hoorzitting, ingebrekestelling, dwangsom, ambtshalve vermindering, kostenvergoeding bezwaar. Excludes substantive tax computations, toeslagen, WOZ/local taxes, customs and criminal proceedings."
version: 1.3
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Netherlands tax objections and appeals (bezwaar and beroep), 2026

## Who this applies to

Use this Guide for a Belastingdienst national-tax assessment, objectionable decision, or tax paid/remitted on a return or withheld. Identify the taxpayer entitled to challenge it, the tax, year, exact document/payment and procedural stage first (AWR arts. 26 and 26a). Income tax, corporate tax, VAT, wage tax, dividend tax and gift/inheritance tax are included; substantive tax calculations belong in their respective Guides.

Read the complete notice and remedy instructions, delivery evidence, return, payment history and earlier correspondence before choosing a route. Do not infer service, receipt, eligibility or a filing deadline from a tax year or the date someone forwards an email. For disputed notification or missing decisive documents: **Check this point with one of our partner accountants.**

### Route and exception table

| Situation | Action / exception |
|---|---|
| Assessment, additional/top-up assessment or objectionable decision | Object, identifying each contested item. One letter can cover several assessments, with separate deadlines; an objectionable decision printed on a national-tax assessment is treated as part of it (AWR art. 24a). |
| Payment/remittance on a return, or withholding | The payment/withholding event is itself challengeable; do not wait for an assessment (AWR art. 26(2)). |
| Provisional income tax assessment | Request revision, rather than objecting directly. Refusal is objectionable under Wet IB art. 9.5, but its special objection-end and decision rules apply. **Check this point with one of our partner accountants.** |
| VAT entrepreneur-status notification alone | The authority directs a challenge through VAT paid on the return, or the refund decision following a negative return; do not object to status alone. |
| Decision on an objection | Consider court appeal, rather than another objection. |
| Apparently late objection | Examine notification and excusable delay; consider ex officio reduction separately. |
| Mass objection, including box 3; Wtl decision | Special designation, participation and timing rules require a separate assessment. **Check this point with one of our partner accountants.** |
| Toeslagen, WOZ/local taxes, customs, criminal tax cases or a service complaint | Outside this Guide. A service complaint is not the objection/appeal route. **Check this point with one of our partner accountants.** |

## Rates, bands and thresholds

| Item | Amount / period and operative condition | Year | Source URL |
|---|---|---|---|
| Ordinary objection and court appeal | 6 weeks; establish the correct starting event below | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 6:7) |
| Posting rule | Posted before expiry **and received no later than 1 week after expiry**; applies to objection and appeal | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 6:9) |
| Objection fee | Nil; advisory costs are separate | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 7:15(1)) |
| Ordinary inspector decision | 6 weeks from the day after the objection period ends; suspension/special rules can change it | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 7:10) |
| Inspector's extension | At most 6 weeks; written notification required; further delay only on the statutory grounds | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 7:10(3)–(5)) |
| Eligible objection legal-assistance costs | EUR 666 per point; points × value × applicable weights, subject to eligibility below; not the adviser's invoice | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0006358/2026-01-01_0/xml/BWBR0006358_2026-01-01_0.xml (art. 2 and annex A5/B2/C) |
| Default-notice waiting period | 2 weeks after both expiry of the decision period and receipt of a written default notice; exceptions below | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (arts. 4:17 and 6:12) |
| Dwangsom daily bands and cap | EUR 23 for days 1–14; EUR 35 for days 15–28; EUR 45 for days 29–42; maximum 42 days, EUR 1,442 **computed**; exclusions below | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 4:17) |
| Invorderingsrente | 4.3% from 1 January 2026; 4% in 2025; use the rate for the actual interest period | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente |
| Small collection-interest amount | EUR 49 or less is not charged on the only or last payment of that assessment | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente |
| Income/corporate-tax reduction request | Ordinary published receipt limit: 5 years after the tax year; substantive restrictions still apply | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/te-laat-voor-bezwaar-wat-nu |
| Gift / inheritance reduction request | Published receipt limit: 5 years after the gift / death respectively, not tax-year end | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/te-laat-voor-bezwaar-wat-nu |
| Reduction-request response | Published ordinary period: 8 weeks after receipt; extra time is notified | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/te-laat-voor-bezwaar-wat-nu |
| First-instance court fee, individual | EUR 54 under Awb annex 3; otherwise EUR 200. The AWR reduced category excludes dividend tax, VAT, bpm, excise, soft-drink consumption tax and environmental-tax decisions. Standalone small-fine relief may separately apply; establish the category. | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 8:41(2), annex 3 arts. 1–2) |
| First-instance court fee, non-individual | EUR 397 | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 8:41(2)(c)) |
| Court-fee payment | Credited or deposited within 4 weeks **after dispatch** of the registry's notice; excusable default and inability-to-pay exceptions below | 2026 | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml (art. 8:41(5)–(6)) |

## The taxable base

For each disputed item record the inspector's treatment, the requested correction, relevant facts, the law for the actual tax year, evidence and the amount. A signed objection must give the name/address, date, description of the decision and grounds (Awb art. 6:5).

**Protective objection.** If grounds are unfinished, identify the decision, sign and file on time, requesting time to supply grounds. Awb art. 6:6 requires an opportunity to cure before inadmissibility for a formal defect. Meet the actual supplementation deadline; there is no promised standard extra period. The decision clock is suspended during the statutory cure period.

**Burden of proof.** Where the **required** return was not filed or an information decision has become final, AWR art. 25(3) requires the taxpayer to establish that and to what extent the assessment/decision is wrong. This rule does not apply to the challenge to an intent/gross-negligence fine (vergrijpboete). Do not conclude that any missing return automatically satisfies these legal conditions. **Check this point with one of our partner accountants.**

**Hearing and file.** In national tax, request a hearing (AWR art. 25(1)) and file access. Awb art. 7:3 permits omission for manifest inadmissibility/unfoundedness, waiver, failure to respond within a reasonable invitation period, or full relief where other interested parties cannot be harmed. File inspection is subject to Awb art. 7:4, including confidentiality exceptions. A telephone clarification is not automatically a waiver; a telephone hearing requires both parties' express agreement. Review the hearing report and raise inaccuracies.

**Costs.** Request eligible costs before the objection decision. Awb art. 7:15 requires reversal because of unlawfulness attributable to the authority. Success alone is insufficient; the authority excludes revision caused only by information first supplied during objection. The legal-assistance tariff awards points for the objection and hearing, multiplied by EUR 666 and the applicable weights, with adjustments/special circumstances under the decree. A provisional-estimate amendment is not itself an objection and does not earn an objection-cost award; an objectionable refusal is a different step.

**Withheld tax.** Under AWR art. 25b, a refund resulting from the objection decision goes to the objector. If both the withholding agent and the person withheld from object on the same facts, it goes only to the person withheld from.

**Special procedures.** Mass-objection designation, the designated legal question, timely participation, separate individual issues, hearing/clock suspension, collective decisions, implementation and further remedies need case-specific treatment. Wtl timing also differs from the ordinary objection. **Check this point with one of our partner accountants.**

### Adaptable Dutch letter

```text
[Naam en adres belastingplichtige]
[Datum]
Aan: [belastingkantoor en adres volgens de aanslag/beschikking]
Betreft: bezwaar tegen [aanslag/beschikking/betaling op aangifte]
Kenmerk: [nummer]; dagtekening/betaaldatum: [datum]; tijdvak: [tijdvak]

Hierbij maak ik bezwaar tegen [precies identificeren].
Ik betwist [onderdeel en bedrag]. Volgens mij moet [gewenste correctie], omdat
[feiten, toepasselijke regel en verwijzing naar de bijlagen].

[Alleen indien nodig: Ik verzoek om een termijn om de gronden aan te vullen.]
[Indien gewenst: Ik verzoek om uitstel van betaling voor het betwiste bedrag
van EUR [bedrag]. Het niet-betwiste deel van EUR [bedrag] betaal ik op tijd.]
Ik verzoek om te worden gehoord en vooraf inzage in de stukken.
[Indien van toepassing: Ik verzoek om vergoeding van de kosten van dit bezwaar.]

Bijlagen: [kopieën, nooit originelen]
[Naam, handtekening, telefoon en e-mail; machtiging indien van toepassing]
```

Complete placeholders using the records. This is an objection template; a court appeal must identify the objection decision instead.

## Deadlines and filing

**Starting event.** The ordinary objection period starts the day after the assessment/objectionable decision's printed date, **unless that date precedes legally effective notification** (AWR art. 22j(a), Awb art. 6:8). For return payments, withholding or remittance, use the day after that event (AWR art. 22j(b)). Establish the actual event and retain proof; do not guess a disputed notification date.

**Receipt and calendar.** File so the authority receives it before expiry. The postal exception above is not another week to post. Preserve posting or portal evidence. Under the Algemene termijnenwet, for the six-week procedural periods covered here, an endpoint on Saturday, Sunday or a recognised/equivalent holiday moves to the next non-excluded day. Check the actual calendar and any designated equivalent days.

**Late filing.** Awb art. 6:11 prevents inadmissibility for delay where the filer cannot reasonably be considered at fault. Record what prevented filing and when it ended, and obtain urgent advice; neither acceptance nor inadmissibility is automatic. **Check this point with one of our partner accountants.**

**Channel.** Income tax supports Mijn Belastingdienst, the Bezwaar particulieren PDF or a letter. Specified VAT and corporate-tax objections support Mijn Belastingdienst Zakelijk; use the tax/decision-specific instructions. VAT top-up assessments support that portal, the Bezwaar zakelijk PDF or a letter. In the portal select Btw → Btw-aangifte → Bezwaar. VAT paid on a return and refusal of the VAT cash-accounting scheme require a letter. Send letters to the office on the notice (VAT-payment letters to your tax office); include copies, never originals. Do not extend a portal route to an unlisted tax/decision. The published receipt acknowledgement is normally within 2 weeks, or up to 3 weeks for income tax; its absence does not extend the filing period.

**Representation.** Use the applicable authority/portal authorisation. A paper authorisation identifies who acts and for what, is signed by both and retained; the authority may request it. The published commercial-software intermediary route does not require a separate objection authorisation. This does not authorise an unrelated person to act without the taxpayer's mandate.

**Decision clock.** For an ordinary inspector objection, count 6 weeks from the day after the objection period ends. The familiar 12-week total from the assessment date is only the nominal ordinary case. Cure suspends the clock from the day after the cure request until cure or unused expiry. The inspector may defer by at most 6 weeks; further delay requires the consent/statutory grounds in Awb art. 7:10(4), with written notification. Calendar adjustments and special procedures matter. For a late objection the authority publishes a usual response of 6 weeks after receipt, or 12 with extension; establish the actual legal route before treating it as a default deadline.

**Late decision.** Only after the actual adjusted deadline expires, send a written ingebrekestelling. The authority's signed form is Dwangsom bij niet tijdig beslissen, sent to Belastingdienst, t.a.v. Ingebrekestellingenteam Arnhem, Postbus 4660, 6803 EP Arnhem, marked “Dwangsom”. Retain receipt evidence. The statutory penalty starts when the two-week waiting period after both expiry and receipt has elapsed, subject to the exclusions below. If no decision follows, Awb art. 6:12 normally allows court proceedings after that notice/wait; an unreasonably late appeal is inadmissible. Exceptional no-notice cases: **Check this point with one of our partner accountants.**

**Ex officio reduction.** A late objection is not an unrestricted second chance. The published receipt windows are in the table; for income tax **2021**, the ordinary receipt date is **31 December 2026**. Other decisions normally use 5 years after the year concerned. Income-tax substantive restrictions in Uitvoeringsregeling IB art. 45aa include later case law/policy, untimely facility elections and linked taxation issues. For those restrictions, a request beyond the ordinary window, marginal collection review or an unusual reduction entitlement: **Check this point with one of our partner accountants.** An individual income-tax refusal in whole/part is objectionable under Wet IB art. 9.6(5); do not transplant that right to every tax or collective process. The published ordinary response is 8 weeks, with notification if extra time is needed. A provisional assessment needs the revision route instead.

**Court appeal.** The ordinary 6-week appeal starts the day after the date of the inspector's decision, unless that date precedes notification (AWR art. 26c). The postal rule also applies. Use Mijn Rechtspraak or a signed letter to the court named in the decision; attach the decision and supporting records. Electronic tax-court communications use Mijn Rechtspraak, not ordinary/secure email; professionals and organisations must follow the linked filing requirements. A lawyer is not compulsory. An appeal against a national-tax assessment covers the objectionable decisions on it. Follow the judgment's remedy clause after court: verzet, higher appeal and cassation have distinct routes. **Check this point with one of our partner accountants.**

**Court fees.** Establish the tariff category in the table and pay by the registry's deadline. Awb art. 8:41(6) preserves excusable-default and established inability-to-pay exceptions; seek advice promptly instead of assuming non-payment always ends the case. If the appeal is withdrawn because the authority grants full/partial relief, it reimburses the fee (art. 8:41(7)). Related decisions/multiple filers have special single-fee rules (art. 8:41(3)); **Check this point with one of our partner accountants.**

## Penalties and interest

**Payment during objection.** Identify the disputed amount and explicitly request postponement. The authority's ordinary assessment-objection guidance grants postponement for that part until the objection decision; pay the undisputed part on time. Check the collection response. Invorderingswet art. 25(1) permits conditional postponement and suspends enforced collection while granted; merely drafting a request proves no grant. For a reduction request or court appeal, request postponement separately; do not assume the objection-stage grant continues. A reduction-request grant covers only the requested reduction and ends with that decision. For appeal, send the request with the appeal copy to Postbus 100, 6400 AC Heerlen; for bpm/transfer tax, Postbus 2584, 6401 DB Heerlen.

**Collection interest.** Ordinary delayed payment still incurs invorderingsrente during postponement. Calculate from the day after the applicable due date through the day before payment reaches the authority, on the unpaid assessment amount. The published formula is days × percentage × amount / 36,000, rounded down to whole euros; a full month counts 30 days (February 28), a year 360. Apply the EUR 49 only/last-payment condition. Payments are allocated first to costs, then interest, then the assessment (Invorderingswet art. 7). A principal-sized remittance can leave principal outstanding. Paying on time avoids collection interest; **belastingrente**, imposed with the assessment, is a different charge.

**Refund interest.** Do not promise it merely because a paid assessment is reduced. Invorderingswet art. 28b requires an earlier **refused postponement request** concerning the disputed amount and reduction below what was paid. Other refund-interest routes have separate conditions. For entitlement and period outside that established route: **Check this point with one of our partner accountants.**

**Fines.** Identify the fine as well as the assessment; a decision printed on the assessment is included under AWR art. 24a(2). A fine objection includes its publication decision when both are in one document unless the objection says otherwise (art. 24a(3)). Lack of fault, an arguable position, proportionality, voluntary disclosure and hardship require the particular penalty law/policy and facts. **Check this point with one of our partner accountants.**

**Dwangsom.** The daily bands in the table run for at most 42 days; the Algemene termijnenwet does not extend that 42-day cap. No statutory payment is due if the default notice is unreasonably late, the applicant lacks interested-party status, or the application/objection is manifestly inadmissible or unfounded (Awb art. 4:17(5)). The authority determines entitlement and amount by decision within 2 weeks after the last compensable day (art. 4:18; applies through art. 7:14). Do not confuse this payment owed by the authority with a tax fine owed by the taxpayer.

## Cross-border points

The same national-tax start/receipt rules apply abroad; retain notification evidence and allow for postal transit. Use European login only where the particular filing route permits it. For a national-tax court appeal by someone abroad, the authority identifies **Rechtbank Zeeland-West-Brabant, Postbus 3332, 4800 DH Breda**; the Midden-Nederland/Utrecht address on its page is for toeslagen, outside this Guide. Resolve any conflicting remedy instructions with a partner accountant before choosing the court.

Withholding objections/refund allocation follow AWR arts. 26a and 25b; a separate treaty-refund form has its own eligibility and time limits. **Check this point with one of our partner accountants.**

For tax refunded because it was levied contrary to EU law, Invorderingswet art. 28c provides interest on request where its conditions apply. The request period ends **6 weeks after the date of the inspector's refund decision**, rather than an assumed receipt date. Avoid overlapping interest periods under art. 28c(2). **Check this point with one of our partner accountants.**

## Worked examples

**Example 1: partial income-tax objection, rejected.** A EUR 20,000 assessment dated **1 March 2026**, a stated six-week payment term, EUR 12,000 disputed and EUR 8,000 paid on time. Establish the legally applicable due date from the notice and calendar; these facts alone are not a filing-date recommendation. Assume ordinary postponement was granted, no costs, a constant 4.3% rate and **150 chargeable days** under the authority's convention ending before receipt of the late payment. Interest: 150 × 4.3 × 12,000 / 36,000 = **EUR 215**, above EUR 49. The taxpayer's EUR 12,000 late remittance is allocated first to EUR 215 interest, leaving EUR 11,785 for principal and EUR 215 principal outstanding. Reconcile and settle that balance, including any further interest. Paying principal on time would avoid this interest; a successful objection would **not automatically** earn refund interest.

```oa-check
name: Partial objection, postponed EUR 12,000 paid 150 days late (2026)
inputs:
  assessment: 20000
  disputed: 12000
  days_late: 150
  rate_pct: 4.3
steps:
  - undisputed_paid_on_time: assessment - disputed
  - interest_raw: days_late * rate_pct * disputed / 36000
  - invorderingsrente: floor(interest_raw)
  - late_remittance: disputed
  - principal_paid: late_remittance - invorderingsrente
  - principal_remaining: disputed - principal_paid
expected:
  undisputed_paid_on_time: 8000.00
  interest_raw: 215.00
  invorderingsrente: 215.00
  principal_paid: 11785.00
  principal_remaining: 215.00
```

**Example 2: late VAT objection decision.** A VAT top-up assessment is dated **2 February 2026**. Assume timely objection, an ordinary 6-week objection period, 6-week decision period and 6-week extension. Their **nominal** total is 18 weeks; establish notification, calendar, extension and any suspension before calculating an actual default date. Assume a valid notice was received after that adjusted deadline, the two-week wait has fully expired, the taxpayer is eligible, no exclusion applies and **20 compensable days** accrue through the decision. The first 14 days give EUR 322; the next 6 give EUR 210; total **EUR 532**. For 42 days, the computed cap is **EUR 1,442**. These assumptions do not authorise a notice based only on the printed date.

```oa-check
name: Late objection decision, dwangsom for 20 days (2026)
inputs:
  objection_weeks: 6
  decision_weeks: 6
  extension_weeks: 6
  days_running: 20
steps:
  - weeks_to_decide: objection_weeks + decision_weeks + extension_weeks
  - band1: min(days_running, 14) * 23
  - band2: min(max(days_running - 14, 0), 14) * 35
  - band3: min(max(days_running - 28, 0), 14) * 45
  - dwangsom: band1 + band2 + band3
  - cap: 14 * 23 + 14 * 35 + 14 * 45
expected:
  weeks_to_decide: 18
  band1: 322.00
  band2: 210.00
  band3: 0.00
  dwangsom: 532.00
  cap: 1442.00
```

## Ask the client first

Read the existing case records before requesting anything missing:

- Tax, taxpayer/year and complete assessment/decision/payment record, including remedy instructions and notification evidence.
- Requested correction, disputed/undisputed amounts, substantive grounds, evidence and required-return/information-decision status.
- Payment and collection ledger, postponement request/decision/expiry, interest and costs.
- Existing objections, reduction requests, hearing invitations, cure/extension notices, default notices and submission/receipt evidence.
- Fine/publication decision, representation authority, foreign address and any mass/special-procedure designation.

Do not invent missing facts, assert automatic lateness or wait for perfect grounds while an established deadline expires. For uncertain eligibility, dates, penalty grounds, special procedures or complex legal interpretation: **Check this point with one of our partner accountants.** Reconcile assessment, payments, refunds, interest and costs before closing; record every remaining remedy and deadline.

## Sources

| Source and bounded passages read | URL | Read on |
|---|---|---|
| Awb: arts. 4:17–4:18; 6:5–6:12, 6:16; 7:3–7:4, 7:10, 7:14–7:15; 8:41 and annex 3; current operative edition | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0005537/2026-11-10_0/xml/BWBR0005537_2026-11-10_0.xml | 2026-11-26, read in listed provisions and neighbouring conditions |
| AWR: arts. 22j, 24a–26a, 26c; remedy scope, special procedures, notification and standing | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002320/2026-10-01_0/xml/BWBR0002320_2026-10-01_0.xml | 2026-11-26, read in listed provisions |
| Wet IB: arts. 9.5–9.6, revision and reduction/refusal conditions | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml | 2026-11-26, read in arts. 9.5–9.6 |
| Invorderingswet: arts. 7, 25(1)–(2), 28–28c, payment allocation/postponement/refund conditions | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0004770/2026-10-01_0/xml/BWBR0004770_2026-10-01_0.xml | 2026-11-26, read in listed provisions |
| Algemene termijnenwet: arts. 1–4, calendar and equivalent days | https://wetten.overheid.nl/BWBR0002448/2010-10-10 | 2026-11-26, read in arts. 1–4, bounded display read |
| Besluit proceskosten bestuursrecht: art. 2, annex A5/B2/C | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0006358/2026-01-01_0/xml/BWBR0006358_2026-01-01_0.xml | 2026-11-26, read in tariff, weights and adjustments |
| Uitvoeringsregeling IB: art. 45aa, substantive reduction exclusions | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0012031/2026-01-17_0/xml/BWBR0012031_2026-01-17_0.xml | 2026-11-26, read in art. 45aa |
| Belastingdienst: filing requirements, channels and supporting copies | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/eisen-bezwaar | 2026-11-26, read in filing sections |
| Belastingdienst: specific VAT routes/status/payment/cash scheme | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/bezwaar-omzetbelasting | 2026-11-26, read in route and portal sections |
| Belastingdienst: representation, paper/portal/software authority | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/iemand-anders-bezwaar-laten-maken | 2026-11-26, read in authorisation sections |
| Belastingdienst: acknowledgement and ordinary/late response times | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/wanneer-bericht-over-bezwaar | 2026-11-26, read in acknowledgement/decision/extension sections |
| Belastingdienst: default-notice form, address and court step | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/belastingdienst-is-te-laat-met-beslissen | 2026-11-26, read in steps 1–2 and appeal; Wtl conflict not used |
| Belastingdienst: cost conditions and provisional amendment | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/kostenvergoeding-bij-bezwaar | 2026-11-26, read in eligibility and provisional sections |
| Belastingdienst: hearing/report/telephone procedure | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/hoorprocedure-bij-bezwaar | 2026-11-26, read in hearing/report/file sections |
| Belastingdienst: reduction windows/response/postponement | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/te-laat-voor-bezwaar-wat-nu | 2026-11-26, read in relevant sections; unusual entitlement referred |
| Belastingdienst: ordinary objection postponement | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/bezwaar-en-uitstel-van-betaling | 2026-11-26, read in payment sections; refund simplification corrected to Invorderingswet art. 28b |
| Belastingdienst: collection-interest period, rates, formula, allocation and refund conditions | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente | 2026-11-26, read in listed sections |
| Belastingdienst: appeal scope, postponement addresses and national-tax court abroad | https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/in-beroep-tegen-uitspraak-op-bezwaar | 2026-11-26, read in appeal/postponement/tax-court sections |
| Rechtspraak: ordinary tax appeal, digital channel, named court, representative/organisation requirements | https://www.rechtspraak.nl/onderwerpen/belastingen/procedure | 2026-11-26, read in filing and representation sections |

Not yet confirmed: no unresolved proposition is offered as a usable rule. Mass-objection/Wtl application, unusual reduction or interest entitlement, disputed notification, penalty mitigation and later remedies are referred above. Apply the relevant law to the actual documents before filing.
