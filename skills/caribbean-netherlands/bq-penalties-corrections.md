---
name: bq-penalties-corrections
description: >
  Analyse selected 2026 BES administrative tax and customs penalties,
  voluntary corrections and ex officio reductions. Use to separate a
  statutory ceiling from policy, filing from payment, default from intent
  or gross negligence, and general tax from customs. Includes primary law,
  current penalty policy, notice and evidence safeguards, limitation rules
  and fictional monetary components. This source-cited draft holds actual
  culpability, disputed policy mapping, mandatory correction delegation,
  criminal proceedings and live submissions. Load with the universal workflow
  base and BES compliance references; professional review remains required.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Selected administrative penalties and correction controls checked on 17 October 2026; actual conduct, decision and applicable period required"
tier: 2
last_updated: 2026-10-17
version: 0.2
review_status: pending_review
depends_on:
  - workflow-base
  - bq-tax-system
  - bq-tax-compliance
  - bq-customs-debt-remedies
---

# Bonaire, Sint Eustatius and Saba: penalties and corrections

Establish the tax, obligation, period, person, conduct, amount, actual
notification, correction and prior decisions. Keep tax, interest, costs
and penalties separate. A missed return, unpaid tax and an inaccurate
declaration have different tests; a statutory maximum is not an amount
automatically imposed on a taxpayer. Obtain professional determination
of culpability, defences and contested legal application.

Load `workflow-base` and applicable domain/BES references. Preserve source
gates, profile confirmation, refusals, four universal outputs and every
domain output/check. Unknown mandatory conditions hold the complete
financial output package. This Tier 2 reference supplies selected controls
and conditional components, not a complete controversy strategy or country
pack.

## Statute, policy and the actual decision

The current penalty policy defines its scope by administrative fines the
inspector can impose under Belastingwet BES chapter VIII for the specified
BES taxes. Its 2023 amendment expanded the scope beyond title 4 and updated
the annual-accounts reference, effective 1 January 2024. That does not
automatically extend its percentages to penalties imposed under the
separate customs Act. [POLICY, article 1][POLICY]; [CHANGE]

Policy article 2 directs use of its stated percentages/amounts and allows
reduction in its disproportionate or beyond-the-person's-control cases
through an objection. Establish actual applicability, statutory limits,
rights and the authority's decision. Neither this reference nor a ledger
calculation imposes a fine. Use `bq-tax-compliance` and
`bq-customs-debt-remedies` for the appropriate remedy/payment branch.
[POLICY]; [B1]; [DAB]

Article 8.6a permits delegated mandatory disclosure cases, timing and
methods, with a separate intent/gross-negligence penalty power. The actual
delegated case must be established before inferring that duty or fine.
A voluntary-correction policy is not proof that every error has the same
mandatory supplement deadline or form. That mapping remains held here. [B1]

## General tax defaults

| Obligation and statute | Statutory control | Current policy, subject to its conditions |
|---|---|---|
| Assessment-based return, 8.22(1) | Maximum USD 1,400; the statutory reminder/return term matters. | Article 3 ordinarily specifies USD 140 only where the set term and reminder were not complied with. Exceptional systematic default can attract the statutory maximum. Its article-41B nil/negative-assessment exception must itself be established. |
| Payment/remittance-on-return filing, 8.22(2)–(3) | Maximum USD 1,400; filing penalty power expires one year after the relevant filing term. | Article 4: no fine for the first default; USD 100 for a second/further default within 24 months after the preceding one. Exceptional systematic default is a separate maximum case. |
| Unpaid, partly unpaid or late remittance, 8.23 | Maximum USD 5,600, with the specified assessment and five-year calendar-year-end power rules. | Article 5 ordinarily uses 5% of the relevant unpaid/late-paid amount, minimum USD 100, capped by the statute. Article 6 instead uses 15%, minimum USD 200, where payment default results from under-declaration. |
| Employee/non-employee information, 8.24 | Maximum USD 2,800; power expires one year after the required information term. | Article 6a: first default is 10% of that maximum; second/further default may reach the statutory maximum. |
| Required annual accounts, 8.24a | Maximum USD 14,000; power expires one year after the required submission term. | Article 6b: first default is 10% of that maximum; second/further default may reach the statutory maximum. |

[B1]; [POLICY]

Article 8.22(3)'s one-year-after-filing-term limit applies to both filing
branches. Separate filing and payment defaults even for the same return.
An accepted filing does not establish payment, and paying the
principal does not erase an already established filing default. Retain
reminders, granted extensions, due dates, receipts, allocation and the
authority's separate penalty decision. Special tax periods, exceptions
and statutory cross-references require their actual branch. [B1]

## Intent, gross negligence and repeated conduct

B1 8.24b concerns specified assessment-return failures attributable to
intent or gross negligence, 8.25 concerns under-assessment, and 8.26
concerns payment/remittance taxes. Each has its own base, assessment
timing, loss and limitation provisions. The listed offence ceilings are
100% of the **defined attributable base**, not necessarily the entire
turnover, unpaid account or reported loss. A loss preventing an assessment
does not itself eliminate the statutory penalty power. [B1]

Policy 7 expressly maps its ordinary 25% gross-negligence and 50% intent
rates to the 8.25/8.26 bases. Serious intent, including the described
serious and relatively extensive fraud, has its 100% case. Its recidivism
rule uses the **same tax** and the five years before the proposed offence
fine, with specified earlier fine, settlement or criminal punishment;
rates become 50% for gross negligence and 100% for intent. Do not borrow
the remittance-filing default's 24-month clock. [POLICY]

For a connected factual complex in a tax year involving several taxes
whose offence fines ultimately fall on one person, policy 7(5) retains
the highest fine and halves each other fine. This is conditional, not
a general right to halve every second notice. The policy's express
8.25/8.26 mapping does not settle the rate for a new 8.24b or 8.6a case;
actual mapping remains held rather than inferred from the shared word
“intent”. [POLICY]; [B1]

Article 8.27a allows a later offence fine for the same act only on its
specified new objections/evidence conditions, with reasons identifying
them and credit for the earlier default fine. Do not simply add both
amounts without the required credit. Article 8.34 separately governs
criminal-judgment concurrence, absence of attributable intent/gross
negligence and substitution by a lower default fine. [B1]

## Voluntary correction and other reduction routes

Article 8.33 requires correct, complete disclosure before the person knows
or should reasonably suspect that the inspector knows or will know of
the error. It provides a **default fine replacing an offence fine**, capped
at 15% of its defined tax amount. This is not automatic immunity and does
not cancel the tax, interest, filing obligations or another offence. [B1]

Policy article 8 addresses undercalculated, underdeclared and underpaid
remittance tax corrected with complete payment. It requires an express,
separate statement allowing a correct assessment without further inquiry;
merely showing an ABB balance in annual accounts, even with explanation,
is insufficient. An announced books inspection or relevant announced/ongoing
industry/fraud inquiry can defeat its voluntary condition as specified.
Record the actual awareness and disclosure chronology. [POLICY]

For a qualifying **remittance-tax** correction, policy 8(6) uses 10% of the
penalty base. Paragraph 7 omits that default fine if the corrected payment
is **USD 3,000 or less**, or **strictly less than 10%** of the relevant
previous net paid/refunded tax for the corresponding period(s). Establish
the correct period, denominator, signs, completeness and payment; do not
assume a nil or net-refund denominator works like a stipulated positive
previous payment. [POLICY]

Policy 8(8) extends specified correction provisions to assessment taxes
but describes reduction of an offence fine. Article 8.33 instead describes
replacement by a default fine. The 2015 publication contains that wording,
and the 2023 amendment changes articles 1 and 6b, not this paragraph.
Actual assessment-correction classification and interactions remain held
for professional resolution; this guide does not silently relabel either
text or certify an actual fine from that disputed mapping.
[B1]; [POLICY]; [ORIGINAL]; [CHANGE]

Ex officio reduction under 8.20 is a separate route. Its five-year cut-off
uses the assessment/calendar, differing financial/tax period or point-in-time
event as specified; the remittance branch uses the end of its relevant
tax year. Paragraph 4 has a specified evidential burden where the return
or named information duties were not fulfilled. Do not replace a timely
objection or a customs refund request with this longer route. [B1]

## Notice, evidence and safeguards

For a general tax offence fine, 8.27 requires advance grounds and at least
two weeks to contest them; its paragraph 3 addresses the effect of failure
to follow that procedure. Article 8.28 requires an objection-eligible
decision, reasons, the stated language assistance and separate notice of
a fine assessed with tax. Applicable collection rules follow the tax.
Retain the actual notice and service evidence. [B1]

Articles 8.29–8.32 distinguish record/access duties from statements about
the penalised conduct, the right not to answer in the stated circumstances,
assistance/interpreting at interview and access/copies of the supporting
material. Preserve these safeguards and refer contested rights to the
practitioner. A tax information duty is not authority for this agent to
collect identities, tax identifiers or bank details. [B1]

Article 8.35 prevents a new fine after death and provides for requested
annulment of a non-final fine; it does not state the same rule as the
customs provision below. Article 8.36 proportionally reduces a tax-based
fine where its own underlying taxed amount is reduced/refunded/remitted.
Article 8.37 extends the section to other legally liable persons. Keep
actual decisions and credits distinct from calculating a possible reduction.
[B1]

## Customs administrative penalties

DAB 2.107–2.112 prescribe separate defaults for entry, temporary storage,
temporary/transit completion, shortages, outgoing formalities and specified
incorrect declarations, each with a USD 140 ceiling and its own responsible
persons. Nil duty does not remove every formal-declaration default. [DAB]

| DAB branch | Stated ceiling/floor controls; actual conditions still required |
|---|---|
| 2.113(1), incorrect declaration reducing duty | Up to 25% of the duty/additional duty, increasing by 25 percentage points on each repetition, up to 100%. Do not invent a repetition period from another paragraph or tax policy. |
| 2.113(2), culpable conduct leading to the specified post-assessed debt | Up to 100% of that debt, capped at USD 5,600. |
| 2.113(3), specified debt attributable to intent/gross negligence | Up to 200% of the debt, minimum USD 140, subject to paragraph 5's USD 14,000 ceiling. |
| 2.113(4)–(5), fraudulent acts or the specified previous paragraph-3 fine less than two years earlier | Percentage increases to 300%, minimum USD 560, maximum USD 14,000. |
| 2.114, specified information, assistance, identification, permission and other duties | Default ceiling USD 140; intent/gross-negligence offence ceiling USD 2,800. |

[DAB]

DAB 2.115 permits delegated defaults with stated ceilings. Customs
regulation 2.76–2.80 names particular notice, permission and other failures
with USD 140 ceilings; identify the exact underlying obligation rather
than fining every procedural irregularity under every row. Decree
2.47–2.49 separately provide USD 2,800 ceilings for their specified
origin-data and warehouse-prohibition defaults. The first two concern
incorrect/incomplete origin information for the named certificates under
decree 2.15(5) and 2.17(3). The third concerns decree 2.43(1)'s prohibited
warehouse storage/possession: specified public-order, safety, environmental,
health, veterinary/phytosanitary and intellectual-property risks.

Decree 2.53 also designates breach of that **decree's warehouse rule** a
criminal offence. It does not refer to the customs Act's identically
numbered document provision. Preserve the administrative/criminal
concurrence rules and hold the actual charging decision; criminal liability
is outside these administrative amount components.
[DAB]; [RULES]; [DECREE]

Article 2.116 gives a three-year penalty-power term after the default or
offence, distinct from the customs debt's post-assessment term. Articles
2.117–2.125 cover the decision, language help, proportional duty-based
reduction, death, advance offence notice, contesting grounds, interview
assistance/interpreter, inspection/copies, criminal-proceeding concurrence,
other persons and ministerial remission. The customs advance-notice
provision sets an inspector's term; do not automatically import B1 8.27's
two-week minimum. [DAB]

Customs 2.119 also covers a final but not fully paid fine at death: reduction
to the amount then paid, by request or official action. Its specified
requests have a five-year-from-death term. Preserve this separate rule;
do not apply it automatically to a general tax fine. A request for remission
under 2.125 is not a grant. Remedies and collection follow the actual branch
in `bq-customs-debt-remedies`. [DAB]

## Fictional monetary components

These cases stipulate a valid applicable branch, positive established base,
the required conduct/culpability and remaining facts, with no exceptional
adjustment or unresolved source issue. They test amount components, not
the existence of an actual offence, an imposed fine or a full tax bill:

| Stipulated branch and facts | Conditional component |
|---|---|
| Ordinary policy-5 payment default, base 1,000 | 5% is 50; policy minimum makes the component **100**. |
| Same policy branch, base 200,000 | 5% is 10,000; statutory cap makes the component **5,600**. |
| Policy-6 under-declaration payment default, base 900 | 15% is 135; policy minimum makes the component **200**. |
| First qualifying employee information default | **2,800 × 10% = 280**. |
| First qualifying accounts default | **14,000 × 10% = 1,400**. |
| Policy-7 ordinary gross negligence versus intent, base 10,000 | **2,500** versus **5,000**, before any applicable distinct adjustment. |
| Two qualifying connected-complex offence fines, 2,000 and 1,000 | Highest 2,000 remains; other becomes 500; combined component **2,500**. |
| Qualifying remittance voluntary correction of 3,000 | Meets policy 8(7)'s inclusive payment threshold. Tax itself remains payable. |
| Qualifying correction 4,000; corresponding previous positive net payment 50,000 | 4,000 is below 5,000, so the strict percentage threshold is met. |
| Qualifying correction 4,000; corresponding previous positive net payment 40,000 | Exactly 10%, not less; neither stated exemption threshold is met. Under the stipulated ordinary policy-8(6) branch, 10% component is **400**. |
| DAB 2.113(3), base 50, stated upper-rate component | 200% gives 100; minimum makes that component **140**, within the 14,000 cap. This does not direct the inspector to impose the upper rate. |
| DAB 2.113(4), base 50, stated upper-rate component | 300% gives 150; minimum makes that component **560**, within the cap. |
| DAB 2.113(3), base 10,000, stated upper-rate component | 200% gives 20,000; ceiling makes that component **14,000**. |

## Verification and limits

Check the specific obligation, person and conduct; source hierarchy and
tax/customs branch; reminders and service; actual base and culpability;
prior-decision tax/type/date; separate filing/payment/correction events;
notice and interview rights; limitation; reductions, credits and imposed
decision. Unknown facts, actual rounding or mandatory legal mapping remain
Needs Input or holds with every workflow output and reviewer question.
The practitioner retains original private records and identifiers.

Read on 17 October 2026: B1 8.6a and 8.19–8.37 including inserted articles;
DAB 2.107–2.125; customs regulation 2.76–2.80; decree 2.15, 2.17, 2.43,
2.47–2.49 and 2.53; all operative
current policy articles 1–11 including 6a/6b; and the complete 2015 and
2023 policy publications in HTML. Authentic PDFs were not examined.

Actual culpability/defences, new statutory-branch policy rates, assessment
correction classification, mandatory disclosure delegation, special minimum-tax
penalties, tax-specific correspondence, criminal procedure, disputed service,
rounding, full collection methods, external forms and live submissions are
not completed. No private case, identity/tax identifier or bank submission,
correction filing, payment, engagement workbook or practitioner sign-off
was used. No comprehensive-area credit is claimed.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[DAB]: https://wetten.overheid.nl/BWBR0029236/2025-01-01
[RULES]: https://wetten.overheid.nl/BWBR0029309/2025-01-01
[DECREE]: https://wetten.overheid.nl/BWBR0029262/2025-01-01
[POLICY]: https://wetten.overheid.nl/BWBR0037210/2024-01-01
[ORIGINAL]: https://zoek.officielebekendmakingen.nl/stcrt-2015-41005.html
[CHANGE]: https://zoek.officielebekendmakingen.nl/stcrt-2023-32017.html

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
