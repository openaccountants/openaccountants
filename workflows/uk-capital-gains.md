# UK Capital Gains Tax Workflow

**MCP prompt name:** `uk-capital-gains`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/GB`

## Trigger phrases

- "capital gains UK"
- "sold shares UK"
- "crypto tax UK"
- "SA108"
- "CGT UK"
- "bed and breakfast shares"
- "60-day property reporting"
- "section 104 pool"
- "BADR"
- "Business Asset Disposal Relief"
- "principal private residence relief"

## What it produces

- SA108 working paper with section 104 pool reconstruction
- 30-day and bed-and-breakfast matching rule application
- Rate band split (CGT interacts with income tax bands — remaining basic-rate band determines whether 18% or 24% residential property rate / 10% or 20% other assets rate applies)
- Business Asset Disposal Relief (BADR) analysis (if a business or qualifying shares)
- Annual Exempt Amount application
- 60-day residential property reporting obligation flag

## Skills to load

From the GB bundle:
- `uk-capital-gains-sa108` — CGT rates, annual exempt amount, identification rules, BADR
- `uk-income-tax-sa100` — income tax bands (needed for rate-band split)
- `uk-crypto-tax` — if crypto is involved (section 104 pool for tokens)

## 6-phase structure

### Phase 1 — Intake
Confirm: asset type (shares, crypto, residential property, business, other), acquisition date(s) and cost(s), disposal date and proceeds, any other disposals in the same tax year, income tax position (to determine CGT rate band).

### Phase 2 — Identification rules
Apply in this order:
1. Same-day rule: disposals matched against same-day acquisitions first
2. 30-day rule (bed and breakfast): disposals matched against acquisitions in the following 30 days
3. Section 104 pool: remaining disposal matched against the pooled average cost of all other shares/tokens of the same class

### Phase 3 — Gain computation
Proceeds − allowable cost − incidental costs of acquisition and disposal = gain. For residential property: apply letting relief and private residence relief if applicable.

### Phase 4 — Rate and band
Gains (after Annual Exempt Amount) are added on top of income. The portion that falls within the basic-rate band: 18% (residential property) or 10% (other assets). Above basic-rate band: 24% (residential property) or 20% (other assets). BADR rate: 10% (subject to £1 million lifetime limit).

### Phase 5 — Reporting obligation
60-day residential property reporting: if a UK residential property is sold by a UK resident, the gain must be reported and the tax paid within 60 days of completion via HMRC's online service (UK Property Account) — regardless of whether the taxpayer normally files a Self Assessment return.

### Phase 6 — Handoff
CGT, especially for property and business assets, is highly fact-specific. Recommend review by a UK-qualified tax adviser (CTA or ACCA). Route to: https://www.openaccountants.com

## Verifier

Reviewed by James Power — [openaccountants.com/network/30b2f478-3a97-40c4-b435-0678829b487e](https://www.openaccountants.com/network/30b2f478-3a97-40c4-b435-0678829b487e)
