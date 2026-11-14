---
name: bq-tax-compliance
description: >
  Analyse 2026 national tax procedure in Bonaire, Sint Eustatius and Saba.
  Use for filing invitations, assessments, payment terms, records, objections,
  first-instance appeals, payment relief, allocation and collection interest.
  Separates return deadlines from assessment collection, taxpayer remedies from
  enforcement opposition, and statutory rules from older guidance. Includes
  primary legislation, current authority pages, conditional calendar and monetary
  examples, evidence controls and source discrepancies. This source-cited draft
  holds unresolved interest methods, relief interactions, late filings, special
  collection cases and actual form mapping. Load with the universal workflow
  base and relevant tax companions; professional review remains required.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "2026 national procedure; tax-specific periods, decisions and transitional rules established separately"
tier: 2
last_updated: 2026-10-17
version: 0.2
review_status: pending_review
depends_on:
  - workflow-base
---

# Bonaire, Sint Eustatius and Saba: national tax compliance in 2026

Identify the tax, taxpayer/withholding agent, requested period, decision and
procedural event before selecting a deadline or remedy. A return period, payment
term, objection term and court-fee term are different obligations. General
national procedure does not establish the treatment of every island levy.

Load `workflow-base` and the applicable BES tax/domain companions. Preserve
source gates, profile confirmation, refusals, the four universal outputs and
every applicable domain output/check. This Tier 2 reference supplies selected
general procedure and conditional components. It does not certify every country
slot, a complete controversy strategy or a live filing. Unknown mandatory
conditions hold the complete financial output package.

## Registration, records and the authority

Belastingwet BES distinguishes the inspector's assessment role from the
receiver's collection role. The assessment notice records the liability and
payment term; an authority reference is not an amount independently verified
by a bank statement. Establish the actual authority and legal basis. Local
taxes need their own adopting and procedural rules. [B1, articles 8.1–8.2 and 8.38][B1]

Article 8.86 includes business/professional individuals, withholding individuals
and entities as administration-obligated persons. It requires records showing
rights, obligations and relevant tax facts, allowing inspection within a
reasonable time. The prescribed languages are Dutch, Papiaments or English.
General tax records and data carriers have a seven-year retention duty.
Specific payroll, distribution-note and company-law duties remain separate;
the shorter period does not authorise destruction of another required record.
[B1]; `bq-payroll`; `bq-corporate-tax`; `bq-financial-statements`

Administration-obligated persons apply for an identification number under
article 8.86(8)–(9). The reviewer retains the legal identity, CRIB value and
identification evidence outside the agent; use stable case references and
confirmation that registration and authority records match. The statutory duty
to show identification to the inspector is not authority for an agent to collect
or submit it. Apply the same privacy control to tax notices and payment details.
[B1]

Article 8.87 has separate reporting duties for specified non-employee service
providers and employees within three months after calendar year-end. Its
exceptions, prescribed form and any delegated reporting rules matter. Annual
accounts under article 8.87a generally go to the inspector within nine months
after financial year-end, including the specified deemed-Dutch entities and
foreign businesses with a BES permanent establishment/representative. The
inspector can grant an extension. Use `bq-financial-statements` for its complete
reporting conditions; tax submission is separate from preparing, adopting or
publishing accounts under company law. [B1]

## Returns and assessments

The inspector may invite a person believed liable or obliged to withhold to
file; a person requesting an invitation is entitled to one under article 8.3.
An invitation requires the requested information to be completed clearly,
unreservedly, signed and submitted. Electronic obligations and exceptions are
set through the implementing rules and the actual invitation. Do not assume a
paper download exempts a person from a mandatory electronic route. [B1]; [RULES]

| Event | General rule to establish before selecting a date |
|---|---|
| Assessment-based return | Inspector's term is at least two months after issue of the form, article 8.4(1). This is a minimum, not a universal fixed annual due date. |
| No assessment-return form within six months after the tax debt arises | Request one within fifteen days after that period, subject to article 8.4(5)'s express conditions. Missing a form is not an automatic nil liability. |
| Payment/remittance-on-return tax | Article 8.5 generally gives fifteen days after period-end or, for a point-in-time return, the tax-debt event. Establish the actual assigned period and tax-specific exceptions. |
| No remittance-return form | Request it before the payment due time under article 8.5(3). |
| Filing extension | Article 8.6 allows a conditional grant, generally no later than eighteen months after the debt arose. Retain the decision; an application alone is not a grant. |
| Intention to leave BES or transfer the place of establishment outside BES | Article 8.6(2) imposes immediate returns for its specified taxes through the end of liability; do not apply an ordinary annual calendar automatically. |

[B1]

Apply the actual tax companion: ABB/payroll return periods, distribution tax's
no-distribution exception, transfer-deed registration and minimum-tax transition
rules cannot be replaced by this general table. Article 8.11(5) extends the
specified fifteen-day payment-on-return term by a granted filing extension's
duration. It does not automatically extend an assessment's collection term or
create relief for every obligation. [B1]; `bq-abb`; `bq-payroll`;
`bq-corporate-tax`; `bq-transfer-tax`

Articles 8.7–8.12 distinguish the original assessment, provisional assessment,
additional assessment (*navordering*) and assessment for unpaid remittance
(*naheffing*). A provisional assessment is reconciled, with evidenced
withholdings, against the assessment under article 8.8(4). Do not deduct it a
second time as both tax credit and cash payment. The original, additional and
remittance-assessment powers have different conditions and time limits; they
are not a generic permission to reopen every year. Actual time-bar conclusions,
correction duties, penalties and exceptional assessments require their full
applicable branch and are held here. [B1]

## Assessment payment and deadline extensions

Article 8.43 supplies these collection terms for assessments. They are separate
from article 8.11's remittance-on-return rules. [B1]

| Assessment | Collection term |
|---|---|
| Ordinary assessment | Two months after notice date. |
| Provisional assessment dated before 1 November of the relevant tax year | Equal instalments in the months remaining after the notice month, each due on that month's last day. |
| Additional or unpaid-remittance assessment | One month after notice date. |

Article 8.43(4) expressly excludes the General Time Limits Act from those
terms. A Sunday therefore does not itself move an article 8.43 payment date
to Monday. Accelerated collection under article 8.52 and an actual relief
decision also require separate treatment. [B1]

The General Time Limits Act applies in BES through article 5a. Where applicable,
article 1 moves an ending Saturday, Sunday or recognised holiday to the next
eligible day. Article 2 has a separate minimum-working-days rule for terms of
at least three days. Article 4 excludes its specified long, hourly and other
terms, including terms exceeding three months; it is not a universal extension
for every reporting or response period. Article 5 addresses terms in general
administrative orders. Check the source establishing the particular term and
any express exclusion first. [ATW]

The Act lists recognised holidays and equates Good Friday. Its delegated order
additionally designates **2 January and 15 May 2026**, with separate future-year
dates. Do not substitute a general employment-holiday list, treat every local
holiday as an ATW holiday, or carry the 2026 extra days into another year.
[ATW, articles 1–5a][ATW]; [EXTRA]

These fictional calendar components stipulate a valid ordinary assessment with
the displayed notice date, no accelerated collection or relief, a standard
two-calendar-month objection term and no unusual service/admissibility issue.
They compare the ordinary candidate dates with the stated statutory extension;
they do not certify a real notice, filing receipt or complete calendar. [B1]; [ATW]; [EXTRA]

| Notice date | Ordinary two-month candidate | Article 8.43 payment date | Objection component after applicable ATW extension |
|---|---|---|---|
| 1 January 2026 | 1 March 2026, Sunday | 1 March | 2 March, Monday |
| 15 March 2026 | 15 May 2026, designated extra day | 15 May | 18 May, Monday, after the weekend |

For a separate stipulated USD 1,200 provisional assessment dated 10 September
2026 in that tax year, three equal USD 400 instalments fall on 31 October,
30 November and 31 December. Article 8.43 excludes the general weekend extension
even though 31 October is Saturday. Establish the actual year, notice and any
special decision before applying this pattern. [B1]

## Objection, court appeal and enforcement opposition

Use `bq-penalties-corrections` for selected administrative-penalty ceilings,
current policy and correction/reduction routes. An actual culpability finding
or a statutory maximum is not an automatically imposed amount.

Article 8.92 generally permits a reasoned objection within two months after
the assessment notice date or the stated posted/delivered decision copy's date.
For self-paid/remitted or withheld tax, paragraph 2 instead uses the payment
or withholding event. Preserve the correct event and documentary receipt;
do not use the assessment-date clock for every remedy. One objection can cover
multiple identified decisions. An objection to an assessment generally also
covers the penalty on the same notice unless the objection indicates otherwise.
[B1]

The authority accepts its objection form or a written paper letter. The letter
identifies its purpose, date, taxpayer, decision/reference and reasons, and is
signed; supporting copies may be attached. Its guidance says not to send
originals. A representative supplies authorisation. The reviewer holds actual
identifiers and correspondence details; this reference supplies the field
requirements, not a completed private submission. Keep proof of timely delivery
and the authority's receipt. [G-OBJECT]; [B1]

Request a hearing in the objection where wanted. Article 8.93 provides the
hearing and decision conditions, normally treating a decision not made within
nine months as late. Article 8.94 permits at most nine additional months only
on its specified grounds and with written notice, requiring a decision as soon
as reasonably possible. Do not turn this into an automatic eighteen-month
response term or invent a late-decision remedy without its procedure. [B1]

| Route | Statutory distinction |
|---|---|
| Tax objection | Inspector/competent decision-maker under title 8; article 8.95 charges no objection fee. A qualifying cost-reimbursement request must be made before the objection decision and meet its conditions. |
| First-instance tax appeal | Article 8.101 permits eligible persons to appeal an objection decision to the Gerecht in eerste aanleg within two months after that decision's date. |
| Court-appeal document and fee | Articles 8.103–8.104 prescribe signature, identifying decision and grounds, documents where possible, defect/late-filing conditions and USD 30 court fee, payable within six weeks after the registrar's notice. Use the actual court instructions. |
| Opposition to execution of a collection writ | Article 8.53 is a separate route with service and one-month commencement formalities and limits on grounds. It is not the tax objection or ordinary tax appeal. Actual enforcement litigation is held for specialist review. |

[B1]

Article 8.96 says an objection does not suspend payment; article 8.102 says
the same for tax appeal. Article 8.53 gives a distinct specified effect for
opposition to execution, which must not be copied into ordinary objection.
Higher appeal, cassation, disputed service, late filing, missing decisions,
restoration of defects and actual litigation require their complete applicable
sources and professional handling. This reference does not calculate a real
litigation deadline or submit a document. [B1]

### Public payment-relief page and the statutory route

The personal payment-relief page describes a ten-day appeal to the director
after refusal and an eight-week response. Current articles 8.41a, 8.57(2) and
8.58(3), and implementing regulation article 8.10(3), make the stated collection
decisions objectionable under title 8. The statutory reference route above
must not be replaced by the website's unsupported general director procedure.
Where an actual notice or agency instruction conflicts, preserve it and obtain
prompt professional clarification; do not assume that relying on a longer
period protects every potentially relevant step. This guide holds that actual
conflict rather than resolving it from the web summary alone. [B1]; [RULES]; [G-RELIEF]

## Payment relief, set-off and allocation

Article 8.57 permits payment relief under the delegated rules and continues
collection interest during relief. Implementing regulation articles 8.10–8.18
address a written request, complete information, dated decision, temporary
difficulty, security, disputed amounts, expected refunds, collection conduct
and ending relief. An application, appeal or expected refund is not by itself
a complete approved payment plan. Distinguish deferment of collection from
extension of filing or the underlying debt. [B1]; [RULES]

The collection policy gives separate routes. Its short-relief rule is at most
four months after the oldest assessment's last due date, with cumulative
conditions including debt below USD 20,000 after its stated exclusion, no
specified other relief and no served collection writ. It precludes subsequent
ordinary relief under its specified individual/business routes after that
short route. Do not present short relief as automatically available. [POLICY, 8.57.4][POLICY]

The implementing regulation's temporary-difficulty route generally limits
relief to twelve months from the day after the decision, except its stated
accumulation case. The policy separately describes individual relief from the
grant date and business relief from the assessment's last due date, with a
conditional longer business route and supporting expert evidence. Those
different starts/exceptions must be established against the applicable rule
and actual decision. This guide does not certify a single universal twelve-month
plan. Security, assets, ability to pay and future compliance also matter.
[RULES, article 8.13][RULES]; [POLICY, 8.57.5–8.57.6][POLICY]

The receiver may take collection measures despite a request where the stated
State-interest condition exists; ongoing obligations must be met. Relief can
end on its conditions/events. The policy's section 8.57.1.5 heading mentions
ten days, but its body distinguishes a normal two-month wait after the stated
refusal/termination from ten days after notified expiry by operation of law,
with conditions permitting shortening. A waiting policy is not an extension
of a return, remedy or debt-payment term. Actual relief/termination calendars,
remission and special departure cases remain held until all applicable
conditions and the decision are established. [RULES]; [POLICY]

Article 8.59 permits the receiver's set-off and requires notification. Policy
limits/conditions also matter, including for disputed amounts during relief.
Do not silently net an expected refund against an unrelated bill. Match the
authority's actual allocation, period, reference and notice. [B1]; [POLICY, 8.57.2–8.57.3][POLICY]

Article 8.40 allocates insufficient payments in order: collection costs,
interest, administrative penalties, then the oldest unpaid assessments or
instalments. These fictional allocation cases stipulate an authority-reconciled
payment, costs USD 30, established interest USD 20, penalty USD 50, an older
principal USD 750 and newer principal USD 1,000, without another allocation
decision or dispute. Interest and penalty eligibility are stipulated, not
computed here. [B1]

| Component, USD | Payment 600 | Payment 1,350 |
|---|---:|---:|
| Collection costs allocated | 30 | 30 |
| Interest allocated | 20 | 20 |
| Penalty allocated | 50 | 50 |
| Older principal allocated | 500 | 750 |
| Newer principal allocated | 0 | 500 |
| Total allocated | 600 | 1,350 |
| Older principal remaining | 250 | 0 |
| Newer principal remaining | 1,000 | 500 |

A bank debit without the authority's allocation does not establish that the
oldest principal was fully discharged. Keep costs, interest, penalties and
principal visible and avoid recording the same settlement twice.

## Interest: current statute and older policy

Article 8.44 provides simple collection interest at **6% a year**, a USD 1
minimum and upward rounding to a multiple of USD 0.50. Its current period
starts when the assessment becomes collectible under article 8.43 and ends
the day before payment/set-off. The 2020 Tax Plan added the period sentence
from 1 January 2020. [B1]; [CHANGE, articles XXII and XXV][CHANGE]

The unchanged 2018 policy instead describes first-of-next-month to
payment-month-end, with a 30/360 calculation method. These pre-amendment
monthly boundaries must not silently replace the current statutory dates.
This guide holds actual day-count, partial-payment and statute/policy method
interaction until supported treatment is established. It does not approve
an operational interest calculator merely from the 6% rate. [POLICY, 8.44][POLICY]; [CHANGE]

For an **already established positive intermediate interest amount**, isolated
statutory amount controls give these conditional results: USD 0.42 becomes
USD 1; USD 1 remains USD 1; USD 1.01 becomes USD 1.50; USD 2.50 remains USD 2.50;
USD 2.51 becomes USD 3. These examples establish neither the underlying period
nor entitlement. No interest charge is invented for an unestablished liability
or a zero/no-interest case. [B1]

Refund interest is a separate branch. Article 8.44(3) has a delay threshold of
more than two months after the refund assessment date, but its defined
interest period starts the day after that assessment date and ends the day
before payment/set-off. Do not start the period only after the two-month
threshold or apply refund interest automatically where taxpayer-caused delay
is excluded by paragraph 4. Actual amounts retain the method/source hold above.
[B1]

## Completion conditions and self-checks

No missing-fact default is authorised. Unknown tax, decision, service event,
period, exception, source, eligibility, payment allocation or method remains
Needs Input or a hold. Follow every applicable refusal and preserve its
canonical message. A statutory maximum penalty or headline interest rate does
not establish the actual charge.

This reference does not complete special tax/transition returns, local-levy
procedure, every correction or limitation rule, actual payment-relief conflicts,
interest methods, remission, liability, civil enforcement, higher appeals,
penalties, portal mapping or a live engagement. Reconcile the chronology,
notices, decision/grant, filing receipt, ledger, authority allocation and
calendar with the applicable tax companion before any complete output.

Check distinct filing/payment/remedy triggers; applicable ATW scope and express
exclusions; continuing payment despite objection; relief conditions versus a
request; statutory rule versus older policy; one use of each credit/payment;
cost-to-oldest-principal allocation; no invented refunds; record duties; and
all universal/domain outputs. Obtain professional review. No real taxpayer,
court filing, payment, portal or engagement workbook was tested. This guide
does not establish comprehensive country coverage.

## Primary sources and read scope

Read on 17 October 2026. Fifty selected national-law articles were compared
across the [January][B-JAN], [February][B-FEB] and [April][B1] 2026 versions and
the fresh current capture; their text matches after explicit interface-label
and whitespace removal. That comparison does not imply every compared
provision was read or every procedural branch was completed. The cited general
filing, assessment, collection, records, objection and first-instance provisions
were read in context. The full Time Limits Act and extra-days order were read.

Implementing relief provisions, policy sections 8.40, 8.44 and 8.57, and the
2020 Tax Plan's interest amendment/commencement were examined. The policy's
entire 100,000-character document, all remission/enforcement branches and all
historical/court authorities were not reviewed. Current authority objection,
payment-relief and collection pages were read in full. Their stated conflicts
are retained; extraction or a citation alone does not establish applicability.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[B-JAN]: https://wetten.overheid.nl/BWBR0029244/2026-01-01
[B-FEB]: https://wetten.overheid.nl/BWBR0029244/2026-02-21
[RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[POLICY]: https://wetten.overheid.nl/BWBR0040762/2018-03-29
[ATW]: https://wetten.overheid.nl/BWBR0002448/2010-10-10
[EXTRA]: https://wetten.overheid.nl/BWBR0051300/2025-07-22
[CHANGE]: https://zoek.officielebekendmakingen.nl/stb-2019-510.html
[G-OBJECT]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/bezwaar-en-beroep-belastingdienst
[G-RELIEF]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-particulieren/invordering-particulieren/als-u-niet-kunt-betalen

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
