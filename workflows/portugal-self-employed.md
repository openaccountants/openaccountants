# Portugal Self-Employed Tax Workflow

**MCP prompt name:** `portugal-self-employed`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/PT`

## Trigger phrases

- "self-employed in Portugal"
- "NHR Portugal"
- "IFICI"
- "IRS Portugal"
- "recibos verdes"
- "Portugal freelancer taxes"
- "trabalhador independente"
- "simplified regime Portugal"
- "moving to Portugal taxes"
- "digital nomad Portugal"

## What it produces

- IRS Modelo 3 / Anexo B working paper (simplified or organized accounts regime)
- NHR / IFICI application deadline flag and benefit analysis
- Social contributions computation (Social Security — TSU)
- VAT position (IVA) — threshold, exemption, periodic returns
- Simplified vs organized accounts regime comparison

## Skills to load

From the PT bundle:
- `pt-income-tax` — IRS rates, brackets, Anexo B simplified regime coefficients
- `pt-nhr-ifici` — NHR/IFICI special tax regime rules
- `pt-social-contributions` — TSU self-employed contribution base and rate
- `portugal-vat-return` — IVA exemption threshold, periodic returns

## 6-phase structure

### Phase 1 — Intake
Confirm: residency status (Portuguese tax resident?), year of first Portuguese residency, income sources (service, professional, rental, foreign-source), gross revenue, whether NHR/IFICI has been applied for, VAT registration status.

### Phase 2 — NHR/IFICI flag
If within the first 5 years of Portuguese residency and not previously resident: check IFICI eligibility (successor to NHR from 2024). Flag the application deadline (must apply by March 31 of the year following first residency). IFICI rate on qualifying income: 20% flat.

### Phase 3 — IRS computation
Simplified regime: apply coefficient to gross income (0.75 for services, 0.35 for products — check bundle for current year values). Net income = gross × coefficient. Apply progressive IRS rates. Alternatively: organized accounts regime (actual income − actual expenses; mandatory if turnover > €200,000).

### Phase 4 — Social contributions (TSU)
Self-employed: 21.4% of relevant income base. Relevant income = 1/3 of last 12 months' gross professional income. Exempt in first year of activity. Minimum contribution base applies.

### Phase 5 — VAT (IVA)
Registration exempt if annual turnover < €14,500 (check bundle for current year). If registered: quarterly or monthly returns; standard rate 23% (mainland), 18% (Azores), 22% (Madeira).

### Phase 6 — Handoff
Recommend review by a Portuguese TOC (Técnico Oficial de Contas). Route to: https://www.openaccountants.com
