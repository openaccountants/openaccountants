# Australia Small Company & Trust Tax Workflow

**MCP prompt name:** `australia-company-trust`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/AU`

## Trigger phrases

- "my company's tax return Australia"
- "Pty Ltd tax"
- "base rate entity"
- "franking my dividend"
- "family trust distribution"
- "trustee resolution"
- "bucket company"
- "Div 7A loan"
- "selling my business CGT concessions"
- "PSI company"

## What it produces

- Company taxable-income reconciliation working paper (add-backs, timing differences)
- BRE rate determination (25% vs 30%) with the two-limb test evidenced
- Franking account rollforward and maximum-frankable-distribution check
- Trust distribution package: s 95 net income, resolution checklist (30 June deadline), streaming schedule, s 100A risk-zone screen
- Div 7A loan register: benchmark interest, minimum yearly repayments, deemed-dividend exposure
- PSI screen for service entities (attribution risk and PCG 2025/5 zones)
- Division 152 eligibility map when a business sale is in scope
- Reviewer brief with escalation list

## Skills to load

From the AU bundle:
- `au-rates-2026-27` — current-year figures used throughout
- `au-company-tax` — BRE tests, franking, losses, lodgment program
- `au-trust-distributions` — Div 6, resolutions, streaming, s 100A, FTE/FTDT
- `au-div7a` — shareholder loans, UPEs post-Bendel, MYR arithmetic
- `au-psi` — personal services income attribution and Part IVA zones
- `au-small-business-cgt` — Div 152 concessions when a sale/restructure is live
- `au-fbt` — employee benefits picked up in the company ledger
- `australia-gst` — BAS reconciliation for the entity
- `au-return-assembly` — final assembly and reviewer brief

## 6-phase structure

### Phase 1 — Entity intake
Establish: entity type (company / discretionary trust / unit trust / company-as-trustee), income year, aggregated turnover (grouping connected entities and affiliates), shareholder/beneficiary map with associate relationships, prior-year returns, franking account balance brought forward, existing Div 7A loan agreements, FTE status. Upload-first: ASIC extract, prior return, trust deed, loan agreements, trial balance. A trust return without the deed and any FTE/IEE history is an automatic reviewer flag.

### Phase 2 — Ledger sweep
Run the GL sweep tables from `au-company-tax` (companies) or `au-trust-distributions` (trusts). Highest-risk patterns: debit loans to shareholders or beneficiaries (route to `au-div7a`), partner/director "salary" that is really a distribution, GIC/SIC in the interest expense account (not deductible from 1 July 2025), one individual generating the revenue of a service entity (route to `au-psi`), trust distribution journals without a matching signed resolution.

### Phase 3 — Entity tax computation
**Companies:** reconcile accounting profit to taxable income; determine BRE status on the two-limb test (watch bucket companies: trust distributions are usually base rate entity passive income); apply 25%/30%; compute franking for any distributions paid and check the account never goes into deficit at 30 June. **Trusts:** compute s 95 net income vs distributable income; confirm present entitlement by 30 June via signed resolutions; apply streaming where the deed permits; screen every arrangement against the PCG 2022/2 s 100A zones; s 99A exposure for any undistributed income.

### Phase 4 — Cross-entity flows
Trace every dollar crossing entity lines: dividends carry franking (gross-up and offset in the recipient), trust distributions carry character (BREPI in a bucket company), UPEs to corporate beneficiaries follow Bendel (not Div 7A loans while passive, but s 100A and Subdiv EA still bite), loans and payments to shareholders/associates go through the Div 7A register with complying-agreement deadlines diarised to lodgment day.

### Phase 5 — Positions and elections
Confirm before lodgment: loss utilisation (COT/similar business test evidence for companies; Schedule 2F escalation for trusts), FTE make/keep/revoke analysis where franking credits or losses flow through the trust, Div 152 concession stack if a CGT event occurred (gateways first, then concession order), instant asset write-off claims against the current threshold, PAYG instalment variation risk (GIC on shortfalls below 85%, and GIC is no longer deductible).

### Phase 6 — Handoff
Run `au-return-assembly` for the reviewer brief. The brief must list: BRE determination basis, franking account closing balance, resolution dates sighted, s 100A zone conclusions, Div 7A register with next MYR dates, and every escalation triggered from refusal catalogues. Recommend review by a registered tax agent or CA/CPA. Lodgment dates follow the agent program (`au-company-tax` Rule 9). Route to: https://www.openaccountants.com

## Escalation boundaries

This workflow stops and refers when it hits: consolidation/MEC groups, trust loss recoupment, Everett assignments, s 100A red-zone arrangements, restructures and rollovers, international dealings, R&D claims, or any dispute already on foot. The refusal catalogues in the loaded skills are binding.

## Verifier

Pending. Australian CPA/CA sign-off required; drafted from primary sources (ATO, legislation.gov.au) and awaiting Partner review.
