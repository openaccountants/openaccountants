# Foundation Workflow Bases

Tier-1 workflow architectures. Every domain has a base that explains *how* the work is done. Country-specific content skills load on top and provide the *what* (rates, thresholds, forms).

## Tax domain bases

| File | What it covers |
|---|---|
| [`workflow-base.md`](workflow-base.md) | Universal cross-domain workflow contract — output format, classification contract, conservative defaults |
| [`us-tax-workflow-base.md`](us-tax-workflow-base.md) | US federal tax workflow — IRC navigation, federal/state interaction, OBBBA coverage |
| [`income-tax-workflow-base.md`](income-tax-workflow-base.md) | Route country income-tax work through the universal contract, keeping individuals and companies separate |
| [`social-contributions-workflow-base.md`](social-contributions-workflow-base.md) | Route employee, employer and self-employed contributions to the applicable country rules |
| [`vat-workflow-base.md`](vat-workflow-base.md) | VAT return preparation lifecycle for any country |
| [`corporate-income-tax-workflow-base.md`](corporate-income-tax-workflow-base.md) | Corporate income tax computation lifecycle |
| [`crypto-tax-workflow-base.md`](crypto-tax-workflow-base.md) | Crypto-asset taxation lifecycle |
| [`wealth-estate-tax-workflow-base.md`](wealth-estate-tax-workflow-base.md) | Wealth / estate / IHT / gift / property transfer tax |
| [`customs-duties-workflow-base.md`](customs-duties-workflow-base.md) | Customs declaration lifecycle |
| [`excise-tax-workflow-base.md`](excise-tax-workflow-base.md) | Excise duty on alcohol, tobacco, fuel, plastic, sugar |

## Accounting domain bases

| File | What it covers |
|---|---|
| [`bookkeeping-workflow-base.md`](bookkeeping-workflow-base.md) | Chart of accounts, double-entry posting, P&L / balance sheet |
| [`financial-statements-workflow-base.md`](financial-statements-workflow-base.md) | Annual accounts preparation under IFRS / local GAAP |
| [`statutory-audit-workflow-base.md`](../audit/statutory-audit-workflow-base.md) | ISA-aligned audit lifecycle (engagement → reporting) |
| [`payroll-workflow-base.md`](payroll-workflow-base.md) | PAYE withholding, social security, payslip generation |
| [`einvoice-workflow-base.md`](einvoice-workflow-base.md) | Structured invoice issuance under EN 16931, Peppol BIS, country mandates |
| [`company-formation-workflow-base.md`](company-formation-workflow-base.md) | Entity formation lifecycle |
| [`transfer-pricing-workflow-base.md`](transfer-pricing-workflow-base.md) | Master file / local file / CbCR / arm's length analysis |
| [`cross-border-workflow-base.md`](cross-border-workflow-base.md) | Multi-jurisdiction transaction orchestration |

---

## How to use

You generally don't load these directly — they're loaded automatically by the country / state content skills that depend on them. If you're building a new country skill, load the relevant workflow base first; it gives you the contract every country skill must fulfill.

See [docs/skill-template.md](../../../docs/skill-template.md) for the slot contract that every content skill must populate.
