---
name: nz-company-capital-records-core
description: "Use for selected New Zealand ordinary company share issues, share and accounting records, annual meetings and written shareholder resolutions. Trigger on initial share consideration, later share issues, pre-emption, director certificates, company record retention or shareholder decision thresholds. Requires independently confirmed company status, constitution, rights, transaction authority and reporting classification. Prepares bounded working papers for qualified review; it cannot approve a special capital transaction, determine audit eligibility, complete formation or submit a filing."
jurisdiction: NZ
category: formation
tier: 2
review_status: pending_review
tax_year: 2026
tax_year_notes: "Company-law controls checked on 14 November 2026; revalidate the address-information transition from 18 November 2026. This is not an income-tax year."
last_updated: 2026-11-14
version: 0.1
depends_on:
  - workflow-base
  - company-formation-workflow-base
  - nz-company-register-core
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand company capital, records and shareholder decisions v0.1

## Scope and source period

Prepare selected working papers for an already selected ordinary domestic company limited by shares. Load workflow-base, company-formation-workflow-base and nz-company-register-core. Retain their confirmation sequence, entity-choice gates, mandatory country slots, required outputs, refusals and qualified-review controls. This guide adds selected capital, records and shareholder-decision rules; it does not complete the formation or financial-reporting topic.

Confirm that the company and transaction fall within the ordinary scope. Listed companies, public offers, financial markets participants, co-operatives, overseas companies, amalgamations, buy-backs, redemptions, distributions, financial assistance, insolvency, restructurings and disputed rights require their own source chain. Options and convertible instruments also require separate work. An ordinary share issue can still trigger class-rights or major-transaction controls. Never classify it as unrestricted merely because the company has few shareholders.

The Companies Act consolidation reviewed is dated 1 July 2025 and the Companies Act 1993 Regulations 1994 consolidation is dated 1 July 2023. Checked on 14 November 2026, the live Act warning list still identifies Deposit Takers Act 2023, Employment Leave Act 2026 and Companies (Address Information) Amendment Act 2025. The selected Deposit Takers and Employment Leave amendment items do not directly amend the capital, record or meeting provisions used here. This is a scoped review, not whole-Act assurance. It does not describe the entire Deposit Takers Act as uncommenced. [Version warnings][V1], [Deposit Takers amendments][V5], [commencement][V3], [Employment Leave amendments][V6], [commencement][V4].

At the check date the Address Information Amendment Act remains labelled 'Not yet in force'. Its section 2 provides a single commencement date by Order in Council, with 18 November 2026 as the backstop. Its section 6 adds alternative-address wording to section 189(1)(f); section 7 inserts conditional replacements for director and shareholder addresses in the section 215 inspection records. The address-information regulations commence on 18 November 2026. Recheck commencement, consolidation and applicable protection before work on or after that date. The rules below describe the checked pre-commencement position; they cannot approve a new alternative-address application or post-transition disclosure. [Address Act, ss2/6/7][V2], [address regulations][V7].

Use redacted summaries and synthetic labels in these working papers. The professional retains personal addresses, identity documents, tax identifiers, bank details, authentication and signing credentials, and performs any authorised submission or payment. Public-inspection duties below do not authorise this workflow to collect or publish private records.

## Engagement and formation completion gates

Obtain the actual constitution and issue terms, current share register, class rights, existing offers and agreements, proposed consideration, board/shareholder authority, transaction date, balance date, meeting history and record locations. Establish voting eligibility for each resolution, rather than equating issued shares, shareholders, voting rights and votes actually cast. Record missing or conflicting evidence as Needs Input, with the affected output and next evidence required.

| Mandatory country slot | Contribution and remaining gate |
| --- | --- |
| Entity catalogue and comparison | Only the independently selected ordinary domestic company is addressed. The complete catalogue, comparison and recommendation remain open |
| Authorities and registration streams | Use nz-company-register-core for incorporation and the separate register annual return. Licensing, regulated activity, banking and other registration applicability remain separate |
| Statutory and annual costs | The register core supplies selected online fees only. No share-issue filing fee or complete professional, office, licence or audit cost is established here |
| Founding documents | The register core covers selected application and consent requirements. This guide adds capital terms, authority and record controls; special execution and transaction documents remain for separate review |
| Capital rules | Selected initial and ordinary later issues below. No monetary minimum, special transaction or valuation approval is inferred from a share count or no-par-value rule |
| Ongoing compliance | Selected records and shareholder decisions below. Register, tax, payroll, GST, financial statements, annual reports, audit, director duties and event-driven changes still need their own applicability and calendars |
| Directors and officers | Retain the register core's eligibility/residence checks. Board authority, interests, duties and the constitution must be independently established; this is not a complete officer regime |
| Ownership disclosures | Reconcile the share register and required ultimate holding company information separately. They do not constitute a complete beneficial-owner assessment |
| GST registration | Route to new-zealand-gst and current IRD authority. A share issue or incorporation does not establish a GST registration decision |
| Audit thresholds | Unverified here. A resolution threshold below does not establish eligibility for an audit or reporting opt-out |

For a formation advisory engagement retain all 5 mandatory outputs: entity comparison, registration checklist, cost breakdown, first-year compliance calendar and reviewer brief. Retain the universal outputs as well. Put these selected facts into the relevant outputs without marking a whole output complete whilst a mandatory slot is unresolved. A standalone existing-company capital, records or decision engagement may prepare its scoped working papers once its applicable facts and sources are verified; it does not thereby complete formation or reporting. Keep evidence, calculations, unresolved facts and qualified-review status consistent.

## Share rights and initial capital

Section 36 supplies default rights to one vote per share on a poll on any company resolution, an equal share of authorised dividends and an equal share of surplus assets. Under section 36(2), those rights may be negated, altered or added to by the constitution or the terms of issue under sections 41(b), 42, 44 or 107(2), subject to section 53. Section 37 permits different classes and rights, including limited or no voting rights, subject to the constitution. Establish actual rights before any proportional or voting calculation. Section 38 says shares have no nominal or par value. It does not establish a NZ$1 minimum, an obligation to pay NZ$1 per share, a solvency conclusion or exemption from a special regime. [Sections 36/37/38][S36], [section 37][S37], [section 38][S38].

Under section 41(a), forthwith after registration the company must issue to each named application shareholder the number of shares stated for that person. Section 51 treats a share as issued when the holder's name is entered on the share register. Cash receipt, a draft subscription document or a Companies Register notification alone does not substitute for that entry. [Section 41][S41], [section 51][S51].

For section 41(a) initial shares, section 46A says the shareholder is not liable to pay consideration unless the constitution specifies it or a pre- or post-incorporation contract provides for it. Read the actual constitution and contract. Do not infer either a free issue or an unpaid capital liability from the number of shares alone. Section 97 limits a shareholder's liability for company obligations solely by reason of being a shareholder, but preserves specified company liabilities and independent contractual, tortious or other liability. Do not describe limited liability as universal personal immunity. [Section 46A][S46A], [section 97][S97].

## Ordinary later share issue working papers

Keep the legal route, authority and each filing clock distinct. The professional must verify all applicable requirements before issue.

1. **Classify the issue and authority.** Section 42 permits the board to issue shares subject to the Act and constitution. Section 44 addresses a constitutional limitation or restriction: approval must be obtained in the manner required for a constitutional alteration that would permit the issue. Record the actual approval and its terms. Its notice must be delivered in the prescribed form within 10 working days of approval. This does not displace section 117 interest-group approval. [Section 42][S42], [section 44][S44].
2. **Resolve pre-emption and affected rights.** Section 45 requires an offer to existing holders where new shares rank equally with or before existing shares for voting or distribution rights, on terms which would maintain existing rights if accepted, and open for a reasonable time. The constitution may negate, limit or modify that requirement. Verify the actual rights and constitution; do not use a simple ownership ratio across unequal classes or silently round fractional entitlements. Under sections 116/117, identify every affected interest group and its required special resolution. An equal or prior-ranking issue is deemed to affect rights unless the constitution expressly permits it or the issue accords with section 45 or the constitution's pre-emption provisions. One class can contain more than one affected interest group. Section 118 may give dissenting holders purchase rights; refer the notices and buy-out procedure for separate qualified review. [Section 45][S45], [sections 116/117][S116], [section 117][S117], [section 118][S118].
3. **Check the wider transaction.** Section 129 requires a major transaction to be approved by special resolution or contingent on that approval. Its definitions include specified acquisitions, dispositions and rights or obligations exceeding half the value of the company's pre-transaction assets, with stated exclusions and contingent-liability rules. Classify the actual transaction and valuation before concluding whether it applies. Do not assume every issue is a major transaction or that an issue can never be one. Board duties, interests, financial markets and any other applicable law require separate clearance. [Section 129][S129].
4. **Set consideration and terms before issue.** Section 46 permits cash, promissory notes, future services, property and other financial products. For a section 42 or 44 issue, section 47 requires the board to decide the consideration and terms and resolve that they are fair and reasonable to the company and all existing shareholders. Where consideration is not cash, determine its reasonable present cash value and resolve that it is not less than the amount credited for the shares. Obtain support for that value; this workflow does not appraise property or future services. [Section 46][S46], [section 47(1)][S47].
5. **Prepare and file the director certificate.** Directors voting in favour must sign the section 47 certificate describing the consideration and terms, the required non-cash value and basis where applicable, fairness and the non-cash floor. A copy must be delivered to the Registrar within 10 working days after the certificate is given. Sections 47(3)/(4) separately address later non-cash crediting of already issued shares. Section 47(6) treats the specified arrangements for exchanging property or services for cash as non-cash to that extent; routing funds through cash does not necessarily change the classification. Section 48 has specific exceptions; do not invoke them without verifying every condition. [Section 47][S47], [section 48][S48].
6. **Obtain any new-liability consent.** Under section 50 an issue increasing a person's liability to the company or imposing a new liability to the company is void without that person's prior written consent, or consent by an agent authorised in writing. A board vote, a capital certificate or another shareholder's signature is not that consent. Retain the distinct authority and consent evidence. [Section 50][S50].
7. **Enter the issue and deliver the applicable notice.** Record the issue on the company's share register. Section 43 requires prescribed notice within 10 working days of issue for section 41(b), 42 or 107(2) issues. Section 41(a) initial incorporation shares are not in that section 43 list. Do not impose or remove a statutory filing merely by applying simplified agency wording to all issues. The section 43 issue clock, section 44 approval clock and section 47 certificate clock have different triggers. [Sections 43/51][S43], [section 51][S51].
8. **Reconcile the prescribed document and actual channel.** Regulation 4 prescribes the Schedule 1 forms and particulars. Form 7 covers the section 43 issue notice and section 44 approval notice: company name/number, prior shares, issue date and number, issue total, total shares after issue, and, where applicable, number, terms and date of approval. It includes director/authorised-person signature, date, full legal name and completer details, with additional sheets where needed. Regulation 7 requires legible documents and the specified signature/name requirements. Establish the applicable filing channel and execution rules; no authenticated portal or blanket electronic-signature conclusion is established here. Do not substitute Form 12, a share certificate or the annual return for an event notice. [Regulation 4][R4], [Form 7][F7], [regulation 7][R7].

Section 47(8) excludes issue on conversion or exercise of an option from section 47, but section 49 separately addresses consideration, board findings, certificates and filing when convertible financial products or options are granted. Do not treat the conversion exclusion as permission to omit the grant-stage requirements. Keep those instruments outside this ordinary issue workflow until separately reviewed. Section 107 also permits specified unanimous written assent routes, with their own conditions and notice requirements; a 75% written resolution is not unanimous assent and is not a blanket waiver of capital rules. [Sections 47/49][S47], [section 49][S49], [section 107][S107].

## Share register, transfers and certificates

The company's own share register is distinct from information filed with the Registrar. Under section 87, record issued shares and transfer restrictions, including where a restriction document can be inspected. For each class keep an alphabetical record of current holders and those who held shares within the last 10 years, their latest known addresses, holdings and the required dated issue, repurchase, redemption and transfer entries and counterparties. Directors must take reasonable steps to supervise maintenance and prompt transfer entry under section 90. Section 89 makes registration prima facie evidence of legal title, subject to rectification, and section 91 provides court remedies. Record disputes as unresolved rather than deciding ownership from a spreadsheet alone. Section 92 prohibits entering notice of a trust; personal-representative and bankruptcy cases in sections 93/94 have their own rules. [Section 87][S87], [sections 89/90][S89], [section 90][S90], [section 91][S91], [sections 92–94][S92], [section 93][S93], [section 94][S94].

Section 88 permits division into registers at different places only if the constitution expressly permits it. Keep the principal register in New Zealand. Within 10 working days after division or a register-location change, deliver notice of each location to the Registrar. Keep a copy of every register with the principal register; an entry in another register must be reflected in its copy there within 10 working days. Do not replace 'working days' with calendar days. [Section 88][S88].

For a section 84 transfer, obtain the transfer signed by the current holder or personal representative and, if registration imposes liability to the company, the transferee. Enter the transferee forthwith unless all refusal/delay conditions are met: a reasoned board resolution within 30 working days of receipt, notice including those reasons to both transferor and transferee within 5 working days of that resolution, and an express Act or constitution basis for the stated reasons. The 30-day condition is not general permission to wait before registering every transfer. [Section 84][S84].

For an ordinary unlisted company outside section 95(1)/(2), a shareholder may request a certificate for some or all shares. Within 20 working days after receipt, send the certificate showing company name, class and number, separating parcels in the register if the request covers only some shares. Do not apply the listed-company automatic certificate rule to every ordinary company. Where a certificate has been issued, section 95(5) requires it with the transfer, or evidence of loss/destruction and any indemnity required by the board, subject to the statutory exceptions. Cancel a surrendered certificate; under the ordinary route issue a replacement to the transferee only on request. [Section 95][S95].

## Company and accounting records

Section 189 is subject to the separate share-register and accounting-location rules. Keep a record inventory and the legal basis for each period rather than labelling every item '7 years'. [Section 189][S189].

| Section 189 category | Period or content to establish |
| --- | --- |
| Constitution, interests register, current directors' full names and addresses, share register | Required records; do not invent a 7-year deletion date for these categories. Apply the share register's own 10-year history requirements |
| Shareholder, director and committee meeting minutes/resolutions; director certificates | Last 7 years under section 189, subject to the separate inspection and other applicable requirements |
| Written communications to all shareholders or all holders of a class, including annual reports | Last 7 years under section 189; section 216 separately requires access to specified communications during the preceding 10 years. The 7-year rule is not authority to destroy records still needed for that duty |
| Financial/group statements required by the Act or another enactment | Last 7 completed accounting periods |
| Accounting records required by section 194 | Current accounting period and last 7 completed accounting periods |

A shorter period needs the Registrar's written approval under section 189(2); it is not assumed. Records in paragraphs (a)–(i) may be kept elsewhere in New Zealand with notice to the Registrar within 10 working days of first being kept elsewhere or moved. Share-register arrangements follow section 88. Accounting records may be overseas under section 195, but sufficient accounts and returns must be sent to and kept at a New Zealand place to enable the required financial/group statements and other Act documents. Notify the Registrar of both the overseas accounting-record location and the New Zealand accounts/returns location. Section 195 itself does not specify a separate notice deadline; classify any independently applicable section 189 trigger rather than inventing a universal 10-day section 195 clock. [Sections 189/195][S189], [section 195][S195].

Section 190 permits written records or an easily accessible form convertible into writing. The board must have adequate measures both to prevent and to detect falsification. Section 194 requires correct transaction records at all times and a satisfactory accounting-record control system. The records must be in written English or easily accessible and convertible into written English. GAAP and audit capability in section 194(1)(b)/(c) are conditional on the company's applicable statement and audit requirements. They do not establish that every ordinary company requires an audit, or that no-audit status removes transaction-record duties. Section 194(1A) expressly includes transactions of the type described in Crimes Act section 105C(3); keeping a record does not approve the underlying conduct. No criminal-law defence is assessed here. [Section 190][S190], [section 194][S194].

## Inspection and copies

Before responding, the professional must classify the request, actual entitlement, service date, records and applicable address protection. Keep personal data outside this workflow. Under section 215, a person serving written notice may inspect the incorporation certificate, any constitution, share register, ultimate holding company information, directors' full names/residential addresses and office/service addresses in the prescribed manner. Section 216 gives shareholders and their written authorised representatives additional access on written notice to shareholder minutes/resolutions, specified communications during the preceding 10 years, director certificates and the interests register. Its minutes/resolutions and certificate categories do not repeat section 189's 7-year limit; do not import that limit automatically. Revalidate the address transition described above. [Section 215][S215], [section 216][S216], [Address Act][V2].

Section 217 requires availability at the records location from 9 am to 5 pm on each working day in the period starting on the third working day after the day of service and ending on the eighth working day after it. For copies or extracts of a document the requester may inspect, section 218 provides 5 working days after a written request, conditional on payment of the company's reasonable copying and administration fee. Establish the actual fee/request facts, calendar and delivery; these are separate from the inspection window. [Sections 217/218][S217], [section 218][S218].

Section 191 separately permits a director, on reasonable notice, to inspect company records in writing without charge at a reasonable time specified by the director. Restriction under that section is a court order on the company's application and stated grounds, not an unrestricted board power to deny access. [Section 191][S191].

## Annual meetings and shareholder resolutions

The register annual return is separate from the annual shareholder meeting, statutory statements, annual reports and income-tax return. Track each stream independently. Section 120(1) requires an annual meeting both within 6 months after balance date and within 15 months after the previous annual meeting. Section 120(2) says the first annual meeting need not be held in the registration calendar year but must be held within 18 months after registration. Preserve that distinction; do not use one deadline as a general replacement for another. Hold a calculated date until the actual dates, applicable exception and calendar are verified. [Section 120][S120].

Section 120(5) dispenses with calling/holding the annual meeting only if all 3 conditions are satisfied: nothing is required to be done at it; the board resolves that relying on the exception serves the company's interests, having regard to shareholders' opportunity to discuss, comment or ask questions; and the constitution does not require it. Separately, section 122(4) dispenses with an annual meeting if everything required there, by resolution or otherwise, is done through resolutions complying with section 122(2)/(3). Section 120(5) does not limit that route. One signed resolution does not prove all required annual business has been completed. [Section 120][S120], [section 122][S122].

For an actual meeting, section 124 applies Schedule 1, except matters the Schedule expressly lets the constitution regulate. Clause 2 requires written notice at least 10 working days beforehand to every shareholder entitled to notice, every director and an auditor. Include sufficiently detailed business, the special-resolution text, any sections 207I/207J resolution text and applicable section 110 rights. The Schedule also governs waiver/irregularity, quorum, proxies, polls, postal votes, electronic participation and minutes. Verify those provisions and the constitution before counting a meeting result. Subject to its exceptions and the constitution, clause 4 requires a quorum able to exercise a majority of votes on the business; clause 12, subject to the constitution, removes the voting right on a share where a sum due to the company in respect of that share remains unpaid, at a shareholder meeting other than an interest-group meeting. Consideration payable later does not remove that right merely because the share is not fully paid. Do not infer eligibility from the total share count alone. [Section 124][S124], [Schedule 1][SCH1].

| Decision route | Threshold and denominator |
| --- | --- |
| Ordinary resolution at a meeting | Section 105: simple majority of votes of those entitled to vote and voting, unless the Act or constitution requires otherwise |
| Special resolution at a meeting | Section 2: at least 75% of votes of those entitled to vote and voting, or the constitution's higher majority |
| General section 122 written resolution | At least 75%, or the constitution's higher special-resolution percentage, of eligible shareholders, together holding at least that percentage of all votes entitled to be cast. Both headcount and voting tests apply |
| Section 122(2)/(3)(a) written resolution for sections 207I/207J | At least 95% of all votes entitled to be cast on the resolution, subject to the underlying section's eligibility, constitution and timing requirements. It is not the general written-resolution test |

A meeting's votes actually cast and a written resolution's all-eligible-votes denominator are different. Verify polls, proxies, joint holders, unpaid amounts and the actual constitution before using those thresholds. Sections 207I/207J also have distinct meeting opt-out rules, and section 207H defines the opting period. This guide does not classify a company as eligible, large, public, subject to section 207E or exempt from statements/audit/annual reports. Obtain that separate reporting chain before using either opt-out. [Sections 105/2][S105], [special-resolution definition][S2], [section 122][S122], [sections 207H/207I/207J][S207H], [section 207I][S207I], [section 207J][S207J].

Section 122(3A) permits similar-form documents, including electronic communications, signed or assented to by or for the relevant shareholders. No prior notice is required under section 122(6), but within 5 working days after passing send a copy to every shareholder who did not sign personally or have it signed on their behalf. For a special resolution required by section 106(1)(a) or (b), also send the section 110 rights statement. Actual purchase rights are conditional, including the relevant activity-restricting constitutional alteration or major transaction and the shareholder's position; not every constitutional change automatically grants a buy-out. Resolve the full procedure separately. [Section 122][S122], [section 106][S106], [section 110][S110].

## Worked controls

All cases are synthetic. The numeric checks test stated arithmetic only. Legal eligibility, actual values, authority, calendars and professional conclusions remain independent inputs. Do not use a passing block as a certificate, filing or approval.

### Case 1: contractual initial consideration

The application allocates 60 initial ordinary shares to A and 40 to B. A verified subscription contract requires $2 per share; the shares are already validly entered in the share register. A paid $120 and B paid $50. The contract establishes the consideration duty in this case: total agreed consideration is $200 and B's shortfall is $30. Do not invent that duty merely from section 38 or a share count; collection and voting consequences need their actual terms and law. [Sections 41/46A][S41], [section 46A][S46A], [section 51][S51].

```oa-check
name: nz-capital-initial-contract
inputs:
  a_shares: 60
  b_shares: 40
  contractual_price: 2
  a_paid: 120
  b_paid: 50
steps:
  agreed_total: (a_shares + b_shares) * contractual_price
  b_shortfall: b_shares * contractual_price - b_paid
  total_unpaid: agreed_total - a_paid - b_paid
expected:
  agreed_total: 200
  b_shortfall: 30
  total_unpaid: 30
tolerance: 0
```

### Case 2: no verified initial payment term

An application specifies 100 initial shares. The constitution and contracts have not been supplied. Do not enter $100 unpaid capital, zero consideration or a payment deadline by assumption. Mark the consideration basis Needs Input. If the professional establishes that neither the constitution nor a relevant contract imposes consideration for section 41(a) shares, apply section 46A's rule on that established basis. [Section 46A][S46A].

### Case 3: single-class pre-emption and Form 7 totals

A and B hold 60 and 40 shares of one verified class with equal rights. Section 45 applies without constitutional modification. A proposed issue of 50 equally ranking shares is offered on otherwise verified terms preserving those rights, with a reasonable offer period. The offer allocation is 30 to A and 20 to B; if both accept and all other authority/consent conditions are met, holdings become 90 and 60, still 60%/40%. Form 7's share total is 150. This arithmetic does not itself satisfy sections 44/47/50/117/129, prove acceptance or authorise issue. [Section 45][S45], [section 117][S117], [Form 7][F7].

```oa-check
name: nz-capital-proportionate-offer
inputs:
  a_old: 60
  b_old: 40
  new_shares: 50
steps:
  old_total: a_old + b_old
  a_offer: new_shares * a_old / old_total
  b_offer: new_shares * b_old / old_total
  a_after: a_old + a_offer
  b_after: b_old + b_offer
  total_after: old_total + new_shares
  a_after_percent: a_after / total_after * 100
expected:
  a_offer: 30
  b_offer: 20
  a_after: 90
  b_after: 60
  total_after: 150
  a_after_percent: 60
tolerance: 0
```

### Case 4: non-cash value below the credit

The board's independently supported reasonable present cash value is $950 for consideration proposed to be credited as $1,000. The $50 shortfall fails the section 47 non-cash floor. Hold the proposed terms for professional correction; do not cure the shortfall with an unsupported fairness assertion or treat the example as a valuation method. [Section 47][S47].

```oa-check
name: nz-capital-noncash-floor
inputs:
  supported_present_value: 950
  proposed_credit: 1000
steps:
  value_shortfall: proposed_credit - supported_present_value
expected:
  value_shortfall: 50
tolerance: 0
```

### Case 5: separate issue, approval and certificate clocks

The professional has already verified actual trigger dates and working-day calculations. There are 2 working days remaining for a required section 43 issue notice, 4 for a section 44 approval notice and 1 for the section 47 certificate copy. The earliest current constraint is 1 working day. Track and satisfy every applicable notice; completing one does not discharge the others. This case does not derive dates from an unverified calendar. [Sections 43/44/47][S43], [section 44][S44], [section 47][S47].

```oa-check
name: nz-capital-independent-notice-clocks
inputs:
  issue_remaining: 2
  approval_remaining: 4
  certificate_remaining: 1
steps:
  earliest_constraint: min(issue_remaining, approval_remaining, certificate_remaining)
expected:
  earliest_constraint: 1
tolerance: 0
```

### Case 6: missing new-liability consent

A proposed issue imposes a new liability on A. The board has approved it, but neither A's prior written consent nor a written-authorised agent's consent exists. Hold issue: section 50 makes the issue void without that consent. Neither the 75% written-resolution route nor another holder's consent substitutes for it. [Section 50][S50], [section 122][S122].

### Case 7: transfer and certificate controls

A valid ordinary transfer is delivered with an existing share certificate missing. Before registration resolve the section 95(5) loss/destruction evidence and any board-required indemnity. A board also wants to delay registration for a reason its constitution does not expressly permit and the Act does not supply. A resolution within 30 working days would not cure that missing legal basis; all section 84 refusal conditions are cumulative. Refer the actual facts promptly. Do not turn either clock into a routine waiting period. [Sections 84/95][S84], [section 95][S95].

### Case 8: accounting periods are not years

An established company has the current accounting period and 7 completed periods, some shorter than 12 months. Section 189 requires accounting records for all 8 periods, while the required financial-statement category covers the last 7 completed periods. Do not convert this to an automatic 8-year rule or a deletion date. A shareholder communication from 9 years ago may still be within section 216's preceding-10-year access duty, notwithstanding section 189's 7-year communication category. [Section 189][S189], [section 216][S216].

```oa-check
name: nz-records-accounting-periods
inputs:
  current_periods: 1
  completed_periods: 7
steps:
  accounting_record_periods: current_periods + completed_periods
expected:
  accounting_record_periods: 8
tolerance: 0
```

### Case 9: overseas ledger and divided share register

The accounting ledger is overseas but no sufficient accounts/returns are kept in New Zealand and neither location has been notified. Section 195's overseas permission does not clear those omissions. Separately, a proposal to divide the share register lacks express constitutional permission. Hold that arrangement under section 88 even if the cloud system can technically provide copies. Verify section 189's separately applicable location notices; do not invent a standalone section 195 deadline. [Sections 88/195][S88], [section 195][S195], [section 189][S189].

### Case 10: written resolution passes heads but fails votes

There are 4 eligible shareholders and 100 eligible votes. Three sign, holding 60 votes; no higher constitutional percentage applies. The headcount is 75%, but eligible votes are only 60%. The general section 122 written resolution fails the voting test. Do not use the signers' votes alone as the denominator. [Section 122][S122].

```oa-check
name: nz-resolution-heads-versus-votes
inputs:
  eligible_heads: 4
  signing_heads: 3
  eligible_votes: 100
  signing_votes: 60
steps:
  heads_percent: signing_heads / eligible_heads * 100
  votes_percent: signing_votes / eligible_votes * 100
  votes_shortfall: 75 - votes_percent
expected:
  heads_percent: 75
  votes_percent: 60
  votes_shortfall: 15
tolerance: 0
```

### Case 11: high votes do not clear the ordinary headcount

Two of 4 eligible shareholders sign with 96 of 100 eligible votes. The 50% headcount fails the general section 122 route despite 96% voting support. The special sections 207I/207J written mechanism uses the 95% eligible-votes test, but only if that particular statutory resolution and all its underlying company, constitution and timing conditions are independently established. They are unresolved in this case; do not infer an audit opt-out. [Section 122][S122], [sections 207I/207J][S207I], [section 207J][S207J].


A higher constitutional percentage also applies to both general written-resolution tests. In a separate verified case, 4 of 5 eligible holders sign with 90 of 100 eligible votes, but the constitution requires 90%. Voting support meets that percentage; headcount is only 80%, a 10-percentage-point shortfall, so the general written resolution fails. Do not apply the default 75% headcount to this constitution. [Section 122][S122].

```oa-check
name: nz-resolution-higher-constitution
inputs:
  eligible_heads: 5
  signing_heads: 4
  eligible_votes: 100
  signing_votes: 90
  constitutional_percent: 90
steps:
  heads_percent: signing_heads / eligible_heads * 100
  votes_percent: signing_votes / eligible_votes * 100
  heads_shortfall: constitutional_percent - heads_percent
expected:
  heads_percent: 80
  votes_percent: 90
  heads_shortfall: 10
tolerance: 0
```

### Case 12: meeting votes cast use another denominator

For a professionally verified quorate meeting and valid poll, an ordinary resolution has 45 votes for and 35 against; another 20 eligible votes are not cast. The 45/80 majority is 56.25%, so the stated ordinary threshold is met, subject to the Act and constitution. It is not 45/100 and this result cannot be imported into a section 122 written resolution. The case assumes notice, quorum, eligibility, proxy/poll rules and any higher applicable approval have already been cleared. [Section 105][S105], [Schedule 1][SCH1].

```oa-check
name: nz-resolution-meeting-votes-cast
inputs:
  for_votes: 45
  against_votes: 35
  not_cast: 20
steps:
  cast_votes: for_votes + against_votes
  for_percent_cast: for_votes / cast_votes * 100
  total_eligible: cast_votes + not_cast
expected:
  cast_votes: 80
  for_percent_cast: 56.25
  total_eligible: 100
tolerance: 0
```

### Case 13: annual meeting exception is incomplete

All holders sign one ordinary written resolution. The team has not established every item required at the annual meeting, or the constitution's meeting requirements. Do not mark the meeting dispensed with. Establish all annual business for section 122(4), or separately every condition of section 120(5). Filing the register annual return would not cure this missing evidence. [Sections 120/122][S120], [section 122][S122].

### Case 14: inspection window and requested certificate

A professionally validated calendar labels the working days after service as 1 through 8. The section 217 inspection window is days 3 through 8 inclusive: 6 working days, each 9 am to 5 pm. A copy request has its own section 218 conditions and 5-working-day rule. Separately, an ordinary unlisted shareholder requests a certificate for 30 of 100 shares. Section 95 requires separate parcels of 30 and 70 and delivery within 20 working days of that request, not automatic delivery for every issue. [Sections 217/218][S217], [section 218][S218], [section 95][S95].

```oa-check
name: nz-records-inspection-and-parcels
inputs:
  first_inspection_day: 3
  last_inspection_day: 8
  shares_held: 100
  certificate_requested: 30
steps:
  inspection_working_days: last_inspection_day - first_inspection_day + 1
  remaining_parcel: shares_held - certificate_requested
expected:
  inspection_working_days: 6
  remaining_parcel: 70
tolerance: 0
```

### Case 15: consideration not yet due leaves the holder eligible

Five otherwise eligible shareholders each hold one voting share. One shareholder's consideration is contractually payable later and no sum due to the company in respect of that share remains unpaid. The constitution does not remove the right. Three other holders sign a general written resolution and no higher constitutional percentage applies. All 5 shareholders and votes remain eligible: both tests are 3/5, or 60%, so the resolution fails. The share being not fully paid is insufficient to exclude its holder. Incorrectly excluding that holder would produce 3/4, or 75%, on both tests and a false pass. This is a comparison of the stated populations, not an independent validation of an actual contract or eligibility decision. [Schedule 1, clause 12][SCH1], [section 122][S122].

```oa-check
name: nz-resolution-consideration-not-yet-due
inputs:
  eligible_heads: 5
  eligible_votes: 5
  signing_heads: 3
  signing_votes: 3
  wrongly_excluded_heads: 1
  wrongly_excluded_votes: 1
steps:
  correct_heads_percent: signing_heads / eligible_heads * 100
  correct_votes_percent: signing_votes / eligible_votes * 100
  wrong_heads_percent: signing_heads / (eligible_heads - wrongly_excluded_heads) * 100
  wrong_votes_percent: signing_votes / (eligible_votes - wrongly_excluded_votes) * 100
expected:
  correct_heads_percent: 60
  correct_votes_percent: 60
  wrong_heads_percent: 75
  wrong_votes_percent: 75
tolerance: 0
```

## Delivery and self-check

For a formation advisory engagement deliver the inherited mandatory outputs together. For a standalone existing-company engagement deliver the agreed scoped working papers and universal outputs. Attach the redacted capital/authority schedule, separate notice calendar, register reconciliation, record inventory/location map and decision-status evidence where relevant. Show sources and check date, actual terms, calculations, missing evidence, professional decisions and completion limits. Do not mark a filing, meeting exemption or transaction approved without its actual result and qualified review.

Before delivery verify: scope and date; current amendments; complete inherited country slots; issue route and actual rights; constitution/pre-emption/interest groups/major transaction; supported consideration and certificates; new-liability consents; share-register entry and separate statutory clocks; prescribed form and channel; transfer/certificate conditions; each retention unit and independent access duty; locations and notices; accessible English accounting records and prevention/detection controls; actual decision eligibility, denominators, meeting procedure, annual business and non-signer notices; separate reporting, audit, tax and register-return statuses. Reject malformed, negative or duplicate counts, zero eligible denominators and signing counts exceeding the verified eligible population. Joint holders and class entitlements require their actual statutory treatment. A passing arithmetic block cannot validate those inputs.

## Primary sources and revision

Checked 14 November 2026. Selected Act provisions use the 1 July 2025 consolidation, regulations use 1 July 2023 and the scoped amendment/currentness review is described above. Refresh affected provisions for later work, especially the 18 November 2026 address transition. No complete financial-reporting, audit, beneficial-ownership or special-capital regime is claimed.

[V1]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320614/?active_tab=version "Fresh Companies Act version warnings"
[V5]: https://www.legislation.govt.nz/act/public/2023/35/en/latest/sections/LMS469579/ "Deposit Takers Act 2023, Schedule 3"
[V3]: https://www.legislation.govt.nz/act/public/2023/35/en/latest/sections/LMS469452/ "Fresh Deposit Takers commencement"
[V6]: https://www.legislation.govt.nz/act/public/2026/48/en/latest/sections/LMS1506038/ "Employment Leave Act 2026, Schedule 2"
[V4]: https://www.legislation.govt.nz/act/public/2026/48/en/latest/sections/LMS737990/ "Fresh Employment Leave commencement"
[V2]: https://www.legislation.govt.nz/act/public/2025/67/en/latest/ "Fresh Address Information Amendment Act"
[V7]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2026/319/en/latest/ "Companies Act 1993 (Address Information) Amendment Regulations 2026 address-regulations-2026.txt"
[S36]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320143/ "Companies Act s36"
[S37]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320147/ "Companies Act s37"
[S38]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320149/ "Companies Act s38"
[S41]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320154/ "Companies Act s41"
[S51]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320168/ "Companies Act s51"
[S46A]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320162/ "Companies Act s46A"
[S97]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320464/ "Companies Act s97"
[S42]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320156/ "Companies Act s42"
[S44]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320159/ "Companies Act s44"
[S45]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320160/ "Companies Act s45"
[S116]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320603/ "Companies Act s116"
[S117]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320609/ "Companies Act s117"
[S118]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320611/ "Companies Act s118"
[S129]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320644/ "Companies Act s129"
[S46]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320161/ "Companies Act s46"
[S47]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320164/ "Companies Act s47"
[S48]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320165/ "Companies Act s48"
[S50]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320167/ "Companies Act s50"
[S43]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320157/ "Companies Act s43"
[R4]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/1994/118/en/latest/sections/DLM190588/ "Companies Act Regulations reg4"
[F7]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/1994/118/en/latest/sections/DLM190829/ "Regulations Schedule1 Form7"
[R7]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/1994/118/en/latest/sections/DLM190596/ "Companies Act Regulations reg7"
[S49]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320166/ "Companies Act s49"
[S107]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320484/ "Companies Act s107"
[S87]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320447/ "Companies Act s87"
[S89]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320450/ "Companies Act s89"
[S90]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320451/ "Companies Act s90"
[S91]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320452/ "Companies Act s91"
[S92]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320453/ "Companies Act s92"
[S93]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320454/ "Companies Act s93"
[S94]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320455/ "Companies Act s94"
[S88]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320448/ "Companies Act s88"
[S84]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320442/ "Companies Act s84"
[S95]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320457/ "Companies Act s95"
[S189]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320862/ "Companies Act s189"
[S195]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320875/ "Companies Act s195"
[S190]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320865/ "Companies Act s190"
[S194]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320874/ "Companies Act s194"
[S215]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321136/ "Companies Act s215"
[S216]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321137/ "Companies Act s216"
[S217]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321139/ "Companies Act s217"
[S218]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321141/ "Companies Act s218"
[S191]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320866/ "Companies Act s191"
[S120]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320614/ "Companies Act s120"
[S122]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320619/ "Companies Act s122"
[S124]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320624/ "Companies Act s124"
[SCH1]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM323288/ "Companies Act Schedule1"
[S105]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320482/ "Companies Act s105"
[S2]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM319576/ "Companies Act s2"
[S207H]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041581/ "Companies Act s207H"
[S207I]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041583/ "Companies Act s207I"
[S207J]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041584/ "Companies Act s207J"
[S106]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320483/ "Companies Act s106"
[S110]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320496/ "Companies Act s110"

## Disclaimer

This is a source-cited draft for a qualified New Zealand professional's review. It does not establish complete formation, reporting, audit or tax compliance. Verify actual facts, operative law, authority, notices and filing requirements before acting.

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
