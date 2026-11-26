---
name: mt-corporate-tax
description: "Malta corporate income tax for basis year 2026 (year of assessment 2027): companies resident in Malta and Malta permanent establishments of foreign companies. Covers the 35% company rate, the full imputation system and the five tax accounts, shareholder refunds (six-sevenths, five-sevenths, two-thirds, full), the elective 15% final tax without imputation (LN 188 of 2025), the taxable base, loss carry-forward, group loss relief (51%) and fiscal units (95%), notional interest deduction, provisional tax, the company return and its deadline, interest and additional tax, outbound withholding, and Pillar Two status. Trigger on: Malta corporate tax, Malta company tax rate, 35% Malta, six-sevenths refund, Malta tax accounts, Malta fiscal unit, Malta group relief, Malta provisional tax company, Malta 15% final tax election. Out of scope: participation exemption detail (mt-holding-company-participation-exemption), company residence, CFC and exit tax (mt-company-residence-and-substance), transfer pricing (malta-transfer-pricing), individuals (malta-income-tax)."
version: 0.6
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 1
domain: corporate-tax
type: computation
reviewed_by: "Michael Cutajar"
reviewed_on: 2026-11-17
---


# Malta corporate income tax: ordinary tax, refunds and filing (basis year 2026)

Malta's ordinary company rate is 35% of chargeable income. A qualifying shareholder refund follows a distribution and satisfaction of its conditions; it is not a 5% company rate. The elective 15% final regime has a statutory floor and restrictions. For a calendar year ending 31 December 2026, the year of assessment is 2027 (Cap. 123 arts. 10–11).

See also: `mt-holding-company-participation-exemption` for participating holdings and refund detail; `mt-company-residence-and-substance` for residence, remittance basis and ATAD; `malta-transfer-pricing`; `selling-a-company-in-malta`; `mt-capital-gains`; and `malta-financial-statements` for the accounts filing/audit documents.

## Who this applies to

A Malta-incorporated company is resident in Malta; a foreign-incorporated body is resident when control and management of its business are exercised here (Cap. 123 art. 2). MTCA describes Maltese companies as taxed on worldwide income and gains and foreign companies carrying on Malta business as taxed on Malta-source income. Residence, domicile, remittance basis, treaty permanent establishment and attribution require the companion Guide; foreign incorporation does not by itself establish worldwide taxation.

Article 56(6) charges 35% on each euro of chargeable income of a company, a body corporate established by law and an article 30(7)(d) separate undertaking. The company definition includes qualifying partnerships/EEIGs that elect under Cap. 372 art. 27(6), while the election remains effective. **Not yet confirmed:** the election procedure for a particular partnership. Check this point with one of our partner accountants. Individuals/self-employed, unelected partnerships, trusts/foundations and insurance, shipping, funds and securitisation regimes need their own treatment. Article 56(13) is the petroleum-contractor/subcontractor provision, not the ordinary company rate.

**Not yet confirmed:** a conclusion that no other minimum, sector or local levy can apply to a particular business. Check this point with one of our partner accountants. This Guide establishes the ordinary income tax charge, not absence of every other tax.

## Rates, bands and thresholds

These figures apply only with the conditions in the corresponding sections below.

| Item | Figure | Period / qualification | Source |
|---|---|---|---|
| Ordinary company income tax | 35% | YA 2027; subject to applicable special provisions | https://legislation.mt/eli/cap/123/eng/pdf |
| Elective final tax | 15%, subject to statutory floor | YA 2025 onward; no credit or refund | https://legislation.mt/eli/sl/123.217/eng/pdf |
| Registered-shareholder refund | 6/7 or 5/7 of eligible ACIT | Actual distribution, category, registration, payment and compliance conditions | https://legislation.mt/eli/cap/372/eng/pdf |
| Separate foreign-account refund | 2/3; eligible participating profits full | Base, tax-paid cap and shareholder/holding conditions | https://legislation.mt/eli/cap/372/eng/pdf |
| Group loss relief | More than 50% in all specified rights | Both companies Malta-only tax residence; other group conditions | https://legislation.mt/eli/cap/123/eng/pdf |
| Fiscal unit | At least 95% of any two specified rights | Eligible bodies, periods, consent and election conditions | https://legislation.mt/eli/sl/123.189/eng/pdf |
| NID limit | 90% of eligible pre-NID income | Relevant accounts; exceptions and carry-forward conditions | https://legislation.mt/eli/sl/123.176/eng/pdf |
| Interest limitation | 30% tax EBITDA; €3m alternative | Group amount and exclusions apply | https://legislation.mt/eli/sl/123.187/eng/pdf |

## 15% final income tax without imputation

S.L. 123.217 (LN 188/2025, 2 September 2025), regulations 2–3, permits an entity to elect 15% on chargeable income determined under the Act in place of article 56(6), for income of the fiscal year preceding YA 2025 and later. Entity includes a company, a body treated/deemed as a company and a trust applying article 27D(1). Excluded from that chargeable income are dividends received from profits **not** allocated to the final tax account of another company registered in Malta, and income already finally taxed and allocated to that account under another provision.

The tax cannot be lower than ordinary tax reduced by refunds **claimed or claimable** by all shareholders under Cap. 372 art. 48(4)/(4A), applying Cap. 123 art. 43(6) where applicable (reg. 3(4)(a)). It is final, unavailable as anyone's credit, set-off or refund; the relevant profits are reallocated to the final tax account. Do not replace that floor with an automatic 15%, or assume a shareholder can lower it merely by choosing not to claim a refund.

The election applies from the YA in which it is made until valid notice to return to normal taxation. That notice cannot be made before the end of five years starting at the beginning of the first elected YA; the return to ordinary taxation then lasts at least five consecutive YAs (reg. 3(3)). MTCA's 27 March 2026 notice requires election through the relevant income tax return questions, by the applicable online filing deadline. It does not supply future YA 2027 form fields.

**Not yet confirmed:** how the floor applies to unregistered shareholders and resident individuals under article 43(6), or whether brought-forward losses/group relief can reduce the elected base notwithstanding article 14(1)(g)'s final-tax-account restriction. Check this point with one of our partner accountants. The second example below remains a conditional arithmetic comparison, not advice to elect.

## The base

MTCA starts with accounting profit before tax adjusted for tax purposes. Article 14(1) requires expenses to be **wholly and exclusively** incurred in producing income; a bookkeeping entry alone is insufficient.

- Add back accounting depreciation; claim statutory wear and tear only for qualifying property used in producing income (art. 14(1)(f)). Unused wear and tear has its own source-specific carry-forward and cost limit. **Not yet confirmed:** asset classification, rates, industrial-building rules under S.L. 123.173 and initial allowances for a real asset. Check this point with one of our partner accountants. The EUR 24,000 allowance below is an assumed allowable input.
- Rent for income-producing premises, qualifying repairs and trade/business promotion and market research fall within arts. 14(1)(b), (c), (l), subject to their terms and the general test. A repair is not automatically every capital improvement.
- A trade/business/profession/vocation bad debt must be proved to the Commissioner's satisfaction to have become bad during the basis year (art. 14(1)(d)). A general doubtful-debt provision does not establish that test. Recoveries of previously written-off/allowed amounts are receipts in the recovery year.
- Scientific research under art. 14(1)(h) must be proved for the use and benefit of the trade/business/profession/vocation. Qualifying capital expenditure is spread equally over the expenditure year and five succeeding years, except qualifying wear-and-tear/initial-allowance expenditure; no duplicate deduction under (h) for plant/premises already allowed under (f)/(j).
- Article 14(1)(ha), marked applicable from YA 2027, provides 175% for qualifying research/development/innovation, but expressly depends on a Ministerial Gazette commencement notice and permits defining rules/conditions. **Not yet confirmed:** operative commencement and conditions for a 175% claim. Check this point with one of our partner accountants. A budget announcement alone is insufficient; the ordinary (h) test above still needs its own proof.
- Capital intellectual-property expenditure under art. 14(1)(m) requires proved income-producing use. The ordinary spread is equal over at least three consecutive years, starting with expenditure or first use. The alternative immediate deduction is subject to prescribed conditions. A tax-neutral article 5(9) transfer has the lower-of-cost/market-value limit less the transferor's prior deductions. **Not yet confirmed:** the immediate-deduction conditions and a client's transferred-IP claim. Check this point with one of our partner accountants.
- Participation exemption and transfer-pricing adjustments require `mt-holding-company-participation-exemption` and `malta-transfer-pricing`; an accounting dividend/gain is not automatically exempt.

### Notional interest deduction (NID)

S.L. 123.176 rules 1–6 apply from YA 2018. Eligible undertakings are resident companies/partnerships and nonresident companies/partnerships deriving income effectively connected to a Malta PE. Nonresident risk capital is limited to the PE-attributable part. The reference rate is the yield to maturity on Malta Government Stocks with approximately 20 years remaining plus 5 percentage points, applied to qualifying **period-end** risk capital: capital, premium, positive retained earnings, non-interest-bearing debt and qualifying reserves/equity balances.

Elect in the return with demonstrated approval of **all shareholders/partners for that YA**. It applies only against income standing to the foreign income or Maltese taxed account (or equivalent for another undertaking). The 90% cap uses that eligible income **before NID**, not all income regardless of account. Excess may optionally be carried forward; rule 4(2)(a) also contains a prescribed uplift and a deemed-interest recipient exception. Do not double deduct the same risk capital under different provisions (rule 4(2)(b)).

Exclude the rule 4 invested-risk-capital amounts producing exempt income, or not producing income where that income could have been exempt. Rule 5 deems interest received in the basis year by period-end holders; multiple holders share it by nominal risk-capital proportions unless the Commissioner directs an alternative basis. Investment-income articles 32–42 do not apply to that deemed interest. Rule 6 counters undue tax advantage. TP applies first where relevant. **Not yet confirmed:** a client's NID amount, applicable annual stock yield/uplift, detailed tracing, deemed-interest tax and the associated S.L. 123.101 rule 3(2) final-account reallocations. Check this point with one of our partner accountants.

### Interest limitation

S.L. 123.187 reg. 4 limits exceeding borrowing costs by 30% tax EBITDA, with the EUR 3m alternative applying to the entire group where treated as one taxpayer. Standalone relief requires no financial-accounting consolidated group, associated enterprise **or PE**. These are not unconditional borrowing deductions. Other exclusions, group equity escape, carry-forwards, ATAD CFC, hybrids and exit tax are dealt with in `mt-company-residence-and-substance`.

## Tax accounts and shareholder refunds

Article 2 of Cap. 123 separates distributable profits (including the relevant Malta-activity profits of a registered nonresident company) into five accounts. The table is an orientation; allocations must follow S.L. 123.101 and statutory definitions.

| Account | Main character and consequence |
|---|---|
| Final tax account | Allocated first. Includes qualifying final-tax profits, but also specified exempt profits; the 15% election reallocates its profits here. Distribution bears no further tax or credit/refund (art. 68(1)(c)). |
| Immovable property account | Statutory property-related and other specified allocations after the final account; not solely rent. No article 48(4A) refund. Article 68(3) requires distribution before Maltese taxed account profits. |
| Foreign income account | Taxable specified foreign investment/foreign PE profits and relevant onward foreign-account dividends; not every foreign receipt regardless of character. Refund route depends on the conditions below. |
| Maltese taxed account | Other qualifying taxed profits after other account allocations; ordinary Malta trading profit is the simple example. |
| Untaxed account | Residual distributable profits or accumulated losses after the other accounts, not a synonym for every exempt profit. No company-tax refund; art. 62 normally deducts 15% on untaxed dividends to a statutory recipient, except exempt payees. |

**Refund fractions (Cap. 372 art. 48).** A registered shareholder receiving a dividend from Maltese taxed/foreign income account profits may claim six-sevenths of the associated **Advance Company Income Tax**, capped at actual company tax paid. Five-sevenths replaces it for statutory passive interest/royalties or participating-holding dividends failing the specified conditions. Passive interest/royalties means non-trade/business interest/royalties suffering no foreign tax or foreign tax below 5% (Cap. 123 art. 2); not all interest is passive. Article 48(4A) is unavailable for foreign-account profits on which double-tax relief was claimed.

The separate art. 48(4)(a) route is two-thirds on eligible foreign-account dividends; its shareholder residence/ownership conditions are disapplied for appropriately registered shareholders. For FIA profits brought to charge from YA 2008, its base can add back double-tax relief under articles 74(a)–(c), but its refund remains capped at **actual Malta tax paid** (48(4)(c)). Do not simply apply two-thirds to the cash tax without checking the relief. Full refund on participating-holding profits under 48(4)(b) has the dividend anti-abuse conditions and dates; see the holding-company Guide. Historical international-trading-company distributions need separate review.

A claim is due within four years from eligibility (48(5)); the Commissioner must be satisfied and receive the article 59(5) dividend certificate. Investment-income tax on specified distributed amounts must also be paid (48(6)). No double refund is allowed and subsequent dividend credits are restricted by 48(7). Article 48(1A)/(1B) also blocks refunds pending the required income-tax, FSS and VAT filings; 48(2) addresses missing/incorrect returns. **Not yet confirmed:** registration steps, eligibility date, payment timing and all compliance facts for a particular claimant. Check this point with one of our partner accountants. A 5% combined burden follows only if 35% tax and an available six-sevenths refund on the same base actually apply.

**Resident individuals.** Article 43(6)(a) can deem the net profits to be received as dividends on the earlier actual distribution or first day of the next accounting period for a resident individual registered for refunds or indirectly beneficially entitled through a registered person/entity. The in-year distribution exception and related indirect-interest rules matter. Exempt taxed-account dividends under art. 12(1)(c)(iii) engage the art. 48(1) refund bar. **Not yet confirmed:** the individual's threshold, deemed-distribution calculation and withholding/refund interaction. Check this point with one of our partner accountants.

## Losses, group relief and fiscal units

Article 51(1) disregards artificial, fictitious or unimplemented tax-reducing schemes; 51(2) counters sole/main-purpose tax/refund advantages and non-genuine Directive arrangements. Article 51(4) can deny current and carried losses and unused wear-and-tear/initial allowances where income follows a scheme/shareholding change, unless the required proof shows it was not solely/mainly to exploit those losses/allowances to avoid tax. Check ownership changes and commercial evidence before using a carry-forward.

**Own trading losses - art. 14(1)(g).** Only a trade/business/profession/vocation loss whose profit would have been assessable qualifies; calculate it excluding wear-and-tear and initial allowances under (f)/(j). Set against the basis-year income/gains then carry unused losses through subsequent years in succession, with no stated time limit or carry-back in this provision. Exclude foreign losses whose retained-abroad profits would not have been taxable, final-account activities, and set-off against final-account income. Another person's loss is unavailable outside group relief; a bona fide merger/division requires the Commissioner's permission and conditions for transferred losses/allowances.

**Group loss relief - arts. 16–22.** Both companies must be Malta resident and not tax resident elsewhere. One must directly/indirectly own **more than 50%** of the other's ordinary share capital **and votes**, and be beneficially entitled to more than 50% of distributable ordinary-shareholder profits and winding-up assets; or both must be such subsidiaries of a Malta-resident parent. The label “51% subsidiary” is not an exact 51% cutoff.

- Membership throughout the loss basis year; matching accounting starts/ends. Article 18(2) permits a newly incorporated member with matching end date/all-period membership, or a wound-up member with matching start date/membership until winding up.
- Only current-year allowable losses, never brought-forward losses, are surrendered. Cross-currency losses use the specified Central Bank mean rates at the loss-period end (18(1)(a)).
- Match MTA/immovable-account losses to either of those accounts; foreign-account losses only to foreign-account income, including subsequent carry-forward. Ignore S.L. 123.101 rule 9(a) elections for this matching (18(1)(c)–(e)). Excess surrendered loss may be carried forward by the claimant as its own under 14(1)(g).
- Claim with required-form surrendering-company consent by the later of the claimant's return date and twelve months after its accounting period end. No double relief (art. 20). Article 19 denies membership where the specified tax-reduction arrangements would cause a company to cease membership.

**Fiscal units - S.L. 123.189.** From YA 2020 for periods commencing 2019 onward, eligible parents/subsidiaries can elect with at least 95% of **any two** of votes, beneficial ordinary-shareholder profits and winding-up assets. The principal taxpayer must satisfy the statutory “company registered in Malta” definition, which can include a qualifying registered nonresident, and not be a transparent subsidiary. Some bodies are excluded by rule 2. Match period start/end dates throughout membership, with the article 18(2) qualification; obtain minority equity-holder approval where not 100%. No company belongs to two units. The election's YA effect also depends on the subsidiary's return date (rule 3).

The unit's income is computed in the principal's name. Internal transactions are generally ignored **except article 5A transactions, property-company share transfers and specified pre-entry taxed dividends** (rule 6(1)(a)). External income retains character/source/country/account. Rule 6(2)'s reduced rate depends on actual hypothetical article 48 entitlement and specific consolidation empowerment; 6(3) bars a second refund on the same profits. It is not a universal 5% regime. Transparent subsidiaries' distributable profits go to their untaxed account; the principal allocates its attributed profits normally (rule 8). FSS and other statutory obligations do not simply disappear. Rule 11 requires unit consolidated accounts and audit notwithstanding general exemptions; rule 12 gives conditional subsidiary return relief, while the principal files the unit return. 100% transparent subsidiaries and principal have joint/several payment liability (12(3)).

Rule 13 tests unit tax after credits/refunds against **95%** of separate-company tax after credits/refunds. If triggered, the deemed advance is the **full difference between separate-company tax and unit tax**, divided by 35%, not just the gap below the 95% threshold. Look-through beneficial-owner/trust rules apply. It becomes an untaxed dividend on the stated tax return date; where taxable, the deduction is 35%, not ordinary untaxed-dividend 15%. General anti-abuse also applies.

**Not yet confirmed:** a client's fiscal-unit registration/composition timetable and clean-filing/payment eligibility, “specifically empowered” application, entry/exit balances, substance/foreign attribution, exact reduced rate and rule 13 computation/payment. Check this point with one of our partner accountants. MTCA's unit guidelines must be applied with the statutory rules; this summary is not a registration or rate-computation instruction.

## Deadlines and filing

| Item | Operative rule |
|---|---|
| Company return | For article 11(2) persons, later of the last day of month nine after the accounts month and 31 March of the YA (S.L. 372.16 rule 2(c)(i)); 31 December 2026 → 30 September 2027. |
| Ordinary tax settlement | Normally that statutory return date (rule 5(b)); FIA deferral, valid duty determinations and distribution/ACIT rules can alter payment timing. Do not treat the return date as every tax payment's due date. |
| Provisional tax | 30 April, 31 August, 21 December falling in the basis period; first date in that period is instalment one. Minimum 20%, further 30%, further 50% of benchmark, subject to adjustments under S.L. 372.18. Non-December periods may reorder those dates. |
| Benchmark | Normally last YA whose return was due before the calendar year of instalment one, self-assessed tax plus PT added back. Rules 6–9 cover changed assessments/Commissioner benchmarks, missing returns and mergers. First YA of a nonindividual: nil; second: first-YA computation from records. |
| PT reduction | Rule 10 prescribed form, estimate at least current-year liability, not unilateral withholding of an instalment. Later payments use the lower rule 5 amount or current-year liability less prior PT. Revision under rules 11–12 can create additional tax. |
| Foreign income account | Cap. 372 art. 42(9) defers tax until not before the earlier distribution or 18 months after period end; read alongside the actual ordinary payment and ACIT rules. |
| Advance Company Income Tax | Art. 42B: compute the dividend-related tax/credits and subtract applicable double-tax relief and tax paid; payment within the statutory sixty-day period following the end of the month after the dividend. Current-period profits distributed during that period are deemed paid on period-end for this rule. Paid ACIT (excluding additional tax) credits later payments on the same profits. |

MTCA's Income Tax page requires a registered tax practitioner and signed MTCA02 authority retained by the practitioner. Cap. 372 arts. 10(4)–(5), 19(4) require the relevant statements/documents and a materially complete return; statutory audit/waiver conditions are in `malta-financial-statements`. **Not yet confirmed:** current spreadsheet/TIFD/TRA attachments, portal fields and online extension for YA 2027. Check this point with one of our partner accountants. MTCA currently lists 27 November 2026 online filing for December 2025 accounts; its extensions expressly concern electronic filing, not tax payment. Do not project that date into YA 2027.

## Penalties and interest

| Default | Consequence and qualification |
|---|---|
| Nonindividual late return | Cap. 123 Schedule item 3 Table B: within 6 months €50; over 6–12 €200; over 12–18 €400; over 18–24 €600; over 24–36 €800; over 36–48 €1,000; over 48–60 €1,200; over 60 €1,500. |
| Return omission | Items 5–7: 1.5% endangered tax per month/part from the due/payable month through correction/assessment month. Correct by article 13 further return before written enquiry: fully remitted if within 12 months of return date, otherwise 0.1%; after written enquiry but before notification of assessment charging that omission: 0.75%. Maximum 60 times applicable monthly rate; endangered tax and special item 12 rules must be determined. |
| Late tax | Art. 44(2A), S.L. 372.28: where due 31 August 2022 onward, 0.6% per month/part, capped at tax. Start depends on the applicable payment/settlement provisions. |
| Late PT | Rule 14: 0.6% per calendar month/part for periods from 1 June 2022; 90% reduction of additional tax on the benchmark/current-self-assessed-tax difference. No further charge for months commencing after tax settlement date. Payments first discharge PT additional tax before the available PT credit. |
| Unentitled shareholder refund | Art. 48(10): penalty equal to refund claimed; if paid, repayment plus 7% per month/part from payment month through repayment month, with payment appropriation to additional tax first. Exception where claimant proves neither actual nor reasonably possible knowledge of non-entitlement. Art. 48(9) separately requires repayment within 30 days of receiving an undue refund, with interest if unpaid. |

Late-return reasonable-excuse remission is discretionary; insufficient funds and reliance on another person are excluded (Schedule item 4). Omission remission and other conditional powers exist under items 8/13; advice is not itself binding and complexity alone insufficient. Interest remission under S.L. 372.26 is discretionary for reasonable cause, excludes reliance on others, may impose forfeitable conditions, and does not entitle repayment of interest already paid. **Not yet confirmed:** a client's endangered tax, default/correction dates, remission, payment-plan treatment or overlapping charges. Check this point with one of our partner accountants. The old PT form's printed 1% does not displace current rule 14.

## Cross-border points

- **Dividends abroad:** taxed-account dividends ordinarily have no further tax for nonresidents under art. 68. Untaxed-account treatment depends on art. 61 recipient status: resident noncompanies, qualifying nonresident persons controlled by/acting for ordinarily resident and domiciled individuals, relevant trusts, and qualifying EU/EEA individuals/spouses. Art. 62 normally deducts 15%, except exempt payees, payable by day 14 after the payment month; art. 66 protects nonrecipients. Do not assert no withholding for every foreign shareholder. Actual recipient/treaty/refund status needs the holding-company Guide.
- **Interest/royalties abroad:** art. 12(1)(c)(i) exemption requires nonresidence, beneficial-owner conditions (including no ownership/control by or acting for ordinarily resident/domiciled individuals) and no effectively connected Malta PE debt claim/royalty. An ordinary exempt payment gives no domestic income-tax withholding; do not apply that result before those facts are established.
- **EU anti-hybrid participation condition:** the Parent-Subsidiary Directive-linked deduction condition needs the holding-company Guide. ATAD interest, CFC, hybrids and exit tax need `mt-company-residence-and-substance`; exit tax is not triggered by every outbound transfer irrespective of Malta losing taxing rights.
- **Pillar Two:** S.L. 123.212 regs. 1–2 apply from fiscal years beginning 31 December 2023; Malta's article 50 election limits the regime to Directive Chapters I, VIII, IX, X for a maximum six consecutive fiscal years, not an unconditional calendar “2024–2029” promise. The €750m test uses at least two of four preceding years, includes excluded-entity revenue, adjusts non-12-month years and has excluded-entity rules. Reg. 11, as amended by LN 48/2026, requires a Malta MNE ultimate parent to designate the specified eligible foreign filer; Malta entities supply required information and reg. 11(2) grants its stated filing/notification exemption. Malta's UTPR percentage is zero during the election. **Not yet confirmed:** the group's actual filing/notification duties, foreign IIR/UTPR exposure, domestic top-up position outside this source, and GloBE effective-rate computation. Check this point with one of our partner accountants. Do not substitute the simple post-refund 5% illustration for a GloBE rate.
- **Article 22B:** the Act authorises regulations for a higher elective tax. **Not yet confirmed:** an operative election and regulations applicable to this company. Check this point with one of our partner accountants.

## Worked examples

All companies and figures are invented. The executable blocks preserve the original inputs and arithmetic. They do not establish eligibility for a relief or election.

### Example 1: a Malta trading company, profits paid out to a foreign parent

Harbour Trading Ltd is incorporated in Malta, calendar year end, basis year 2026 (YA 2027). Its accounts show profit before tax of EUR 250,000. It booked depreciation of EUR 30,000; tax wear and tear allowances are EUR 24,000. It also booked a general provision for doubtful debts of EUR 5,000, which is not a deduction under art. 14(1)(d). All profit is Malta trading profit, so it goes to the Maltese taxed account.

Chargeable income is 250,000 + 30,000 - 24,000 + 5,000 = EUR 261,000. Tax at 35% is EUR 91,350.

Its YA 2025 self-assessment (basis year 2024, the last return due before 1 January 2026) showed tax of EUR 80,000, so provisional tax in 2026 is EUR 16,000 on 30 April, EUR 24,000 on 31 August and EUR 40,000 on 21 December. Assuming the benchmark is unchanged, no earlier distribution creates an additional payment and no other special payment rule applies, the balance of EUR 11,350 is due by 30 September 2027. This is the statutory return date; a future electronic filing extension does not extend payment.

Harbour pays all its 2026 profit as a dividend to its sole shareholder, a German company not owned or controlled by anyone ordinarily resident and domiciled in Malta, and registered for refunds. Assume the dividend certificate, actual tax payment, registration, compliance gates and other refund conditions below are satisfied. The shareholder claims six-sevenths of the tax: EUR 78,300. Malta tax left is EUR 13,050, which is 5% of chargeable income. No tax is withheld on the dividend.

```oa-check
name: Malta trading company, basis year 2026, six-sevenths refund
inputs:
  profit_before_tax: 250000
  depreciation_booked: 30000
  wear_and_tear: 24000
  general_provision: 5000
  pt_benchmark: 80000
steps:
  - chargeable: profit_before_tax + depreciation_booked - wear_and_tear + general_provision
  - tax: chargeable * 0.35
  - pt_april: pt_benchmark * 0.20
  - pt_august: pt_benchmark * 0.30
  - pt_december: pt_benchmark * 0.50
  - balance_due: tax - pt_april - pt_august - pt_december
  - refund_fraction: 6 / 7
  - refund: tax * refund_fraction
  - malta_tax_after_refund: tax - refund
  - effective_rate_pct: malta_tax_after_refund / chargeable * 100
expected:
  chargeable: 261000
  tax: 91350
  pt_april: 16000
  pt_august: 24000
  pt_december: 40000
  balance_due: 11350
  refund: 78300
  malta_tax_after_refund: 13050
  effective_rate_pct: 5.00
```

### Example 2: losses brought forward and group relief, and the 15% election compared

Gozo Logistics Ltd has chargeable income of EUR 300,000 for basis year 2026, all for its Maltese taxed account, before losses. It has its own unrelieved trading losses brought forward of EUR 80,000. Its sister company, Gozo Fleet Ltd, made a 2026 trading loss of EUR 60,000 that would have gone to its Maltese taxed account. A Malta parent owns 100% of both; both are resident only in Malta, were in the group all year, and have 31 December year ends. Fleet consents in the required form and Gozo Logistics claims the whole loss by 30 September 2027, before the later statutory limit of 31 December 2027. Assume the losses satisfy article 14(1)(g), there is no double relief or article 19 arrangement and article 51 does not deny the losses, and both companies have matching tax currency (otherwise apply article 18(1)(a) conversion).

Chargeable income is 300,000 - 80,000 - 60,000 = EUR 160,000. Tax at 35% is EUR 56,000. If the profits are paid out and six-sevenths is claimed, Malta tax left is EUR 8,000.

**15% comparison - arithmetic only; not usable as an election computation.** The original inputs remain EUR 300,000 income, EUR 80,000 own losses and EUR 60,000 surrendered losses. If EUR 160,000 were the eligible elected chargeable income and EUR 8,000 the correctly determined regulation 3(4)(a) floor, then 15% is EUR 24,000, EUR 16,000 above the assumed refund route. The block below computes precisely those assumptions. It does not decide whether losses/group relief reduce income reallocated to the final tax account, the shareholders' actual claimable refunds, or article 43(6). **Not yet confirmed:** the client-specific election base and floor. Check this point with one of our partner accountants. Retaining profits, delaying dividends or deciding not to claim a refund does not by itself prove a saving.
```oa-check
name: Losses brought forward plus group relief, and the 15% election compared
inputs:
  chargeable_before_losses: 300000
  own_losses_bf: 80000
  group_loss_surrendered: 60000
steps:
  - own_used: min(own_losses_bf, chargeable_before_losses)
  - group_used: min(group_loss_surrendered, chargeable_before_losses - own_used)
  - chargeable: chargeable_before_losses - own_used - group_used
  - losses_carried_forward: own_losses_bf - own_used
  - tax: chargeable * 0.35
  - refund_fraction: 6 / 7
  - refund_route_net: tax - tax * refund_fraction
  - elective_tax: chargeable * 0.15
  - elective_payable: max(elective_tax, refund_route_net)
  - election_extra_cost: elective_payable - refund_route_net
expected:
  chargeable: 160000
  losses_carried_forward: 0
  tax: 56000
  refund_route_net: 8000
  elective_payable: 24000
  election_extra_cost: 16000
```

## Ask the client first

Obtain ownership/residence/domicile and refund registration, each income source and tax account, actual dividend plans, election history, period-end dates and tax currency, loss provenance, group rights and consolidation records, benchmark self-assessments/payments, filing/VAT/FSS compliance, and group revenue over the relevant years. These are evidence requests; none establishes eligibility by itself.

## Sources

| Official provision / guidance | URL | Read on | Scope |
|---|---|---|---|
| Cap. 123 | https://legislation.mt/eli/cap/123/eng/pdf | 2026-11-26 | Read for art.2 company/residence/accounts/passive-interest definitions; arts.10–11,12(1)(c) and12(1)(u)(1) relevant clauses,14(1)(b)–(m),16–22B,43(6)(a)/(b)/(d),51(1)–(2)/(4),56(6)/(12),59–68 and Schedule items1–9,12–13; only relevant provisions, not whole Act. |
| Cap. 372 | https://legislation.mt/eli/cap/372/eng/pdf | 2026-11-26 | Read for arts.10(1)–(5),19(4) reused same-day financial-statements proof;42(9),42B,44(2A),48(1)–(7),(9)–(10); historical transitional refunds not usable instructions. |
| Final tax without imputation | https://legislation.mt/eli/sl/123.217/eng/pdf | 2026-11-26 | Read for all regulations1–3. |
| Fiscal units | https://legislation.mt/eli/sl/123.189/eng/pdf | 2026-11-26 | Read for rules1–3,4(1)–(2),6–13; specific entry/exit operations referred. |
| MTCA fiscal-unit guidance | https://mtca.gov.mt/docs/default-source/documents/guidelines-in-relation-to-the-consolidated-group-(income-tax)-rules.pdf | 2026-11-26 | Read for paragraphs(i)–(ii),(xv)–(xvi),(xix), showing additional registration and empowerment conditions; actual client registration/computation referred. |
| NID | https://legislation.mt/eli/sl/123.176/eng/pdf | 2026-11-26 | Read for all rules1–6. |
| Tax accounts | https://legislation.mt/eli/sl/123.101/eng/pdf | 2026-11-26 | Read for rules2–5(3)(b), including NID final-account reallocation; detailed client allocation referred. |
| ATAD | https://legislation.mt/eli/sl/123.187/eng/pdf | 2026-11-26 | Read for reg4(1)–(3); detailed exclusions/CFC/exit/hybrids routed to residence Guide. |
| Pillar Two | https://legislation.mt/eli/sl/123.212/eng/pdf | 2026-11-26 | Read for regs1–2 and11, amendment list; actual group calculation and other-country law referred. |
| Statutory dates | https://legislation.mt/eli/sl/372.16/eng/pdf | 2026-11-26 | Read for rules2–5; same-day transfer-pricing evidence reused for unchanged return-date rule. |
| Provisional tax | https://legislation.mt/eli/sl/372.18/eng/pdf | 2026-11-26 | Read for rules1–14 and prescribed reduction form; rule10 estimate and rule12 revision conditions included. |
| Interest rate | https://legislation.mt/eli/sl/372.28/eng/pdf | 2026-11-26 | Read for all rules1–2. |
| Remission of interest | https://legislation.mt/eli/sl/372.26/eng/pdf | 2026-11-26 | Read for all rules1–6; actual payment-plan effect referred. |
| MTCA corporate tax | https://mtca.gov.mt/business-tax/corporate/corporate_tax | 2026-11-26 | Read for scope/ordinary-rate summary; statutory conditions control. |
| MTCA Income Tax | https://mtca.gov.mt/business-tax/corporate/Income_Tax | 2026-11-26 | Read for practitioner/MTCA02, accounting-profit adjustments and current extension table; reused same-day formation read once. |
| MTCA final-tax election notice | https://mtca.gov.mt/news-results-page/2026/03/27/election-for-final-income-tax-without-imputation | 2026-11-26 | Read for election through return, five-YA commitment and applicable online filing deadline. |

Not yet confirmed: every explicitly referred client-specific computation, future form/extension, commencement and specialist topic above supplies no usable operative conclusion. Check this point with one of our partner accountants.
