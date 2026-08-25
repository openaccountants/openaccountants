---
name: italy-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Italy. Trigger on phrases like "set up a company in Italy", "SRL formation", "SRLS", "Camera di Commercio", "Italian company formation", "register a business Italy", "società a responsabilità limitata", "Registro delle Imprese", "partita IVA", "Italian notary", or any question about starting a business entity in Italy. Covers entity types (SRL, SRLS, SPA, SNC, SAS), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Italian company formation.
version: 1.0
jurisdiction: IT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy Formation

## Italy Company Formation Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Italy (Italian Republic) |
| Currency | EUR |
| Company registrar | Camera di Commercio / Registro delle Imprese |
| Key legislation | Codice Civile (Art. 2462--2483 for SRL); D.Lgs. 123/2025 |
| Typical formation time | 1--3 weeks |
| Corporate tax rate | 24% IRES + 3.9% IRAP = ~27.9% effective |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Ditta Individuale (Sole Trader) | S.r.l. (Standard) | S.r.l.s. (Simplified) | S.n.c. / S.a.s. (Partnerships) | S.p.A. (Public Company) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | Yes | Yes | S.n.c.: No / S.a.s.: Yes | Yes |
| Liability | Unlimited | Limited | Limited | S.n.c.: Unlimited / S.a.s.: Limited for accomandanti | Limited |
| Min. founders | 1 | 1 | 1 (natural persons only) | 2 | 1 |
| Min. share capital | N/A | €10,000 | €1--€9,999 | N/A | €50,000 |
| Min. paid-up at formation | N/A | 25% (multi-shareholder) or 100% (single) | 100% (cash only) | N/A | 25% |
| Governance flexibility | N/A | High (customisable statuto) | Low (standard statuto) | Low | Medium |
| Tax treatment | IRPEF (personal) | IRES + IRAP | IRES + IRAP | Partners taxed via IRPEF | IRES + IRAP |
| Notary required | No | Yes | Yes (reduced fees) | No (deed required) | Yes |
| Admin burden | Low | High | Medium | Low--Medium | Very High |

**Recommended default:** Standard S.r.l. for most commercial purposes. S.r.l.s. for bootstrapped micro-businesses run by individuals.

## Section 3 -- Registration Process

### Step 1: Choose Company Name (Denominazione Sociale)

- **Company name requirements** — Check availability at local Camera di Commercio. Must include "Società a responsabilità limitata" or "S.r.l." in the name. S.r.l.s. must include "Società a responsabilità limitata semplificata"

### Step 2: Draft Atto Costitutivo and Statuto

- **Atto costitutivo and statuto requirements** — Atto costitutivo (deed of incorporation) and statuto (articles of association). S.r.l.s. must use the standard-form statuto (not customisable). Standard S.r.l. allows fully customisable statuto

### Step 3: Notary Appointment

- **Notary appointment requirements** — Both S.r.l. and S.r.l.s. require notarisation. S.r.l.s. notary fees are waived or significantly reduced by law. Notary verifies identity, capacity, and capital deposit

### Step 4: Deposit Share Capital

- **Deposit share capital requirements** — S.r.l. (multi-shareholder): deposit min. 25% (€2,500 of €10,000) with a bank. S.r.l. (single shareholder): deposit 100% of capital. S.r.l.s.: deposit 100% (€1--€9,999, cash only). S.p.A.: deposit min. 25% of €50,000

### Step 5: Register with Registro delle Imprese

- **Registration with Registro delle Imprese** — Notary files the deed within 20 days of signing. Electronic filing with Camera di Commercio. Registration fees: ~€120--€200 (Chamber of Commerce) + €200 (registration tax for cash contributions) + €156 stamp duty

### Step 6: Obtain PEC and Codice Fiscale / Partita IVA

- **PEC and Codice Fiscale / Partita IVA** — PEC (Posta Elettronica Certificata) is mandatory for all companies. Codice fiscale and Partita IVA assigned by Agenzia delle Entrate. File via ComUnica (single communication to INPS, INAIL, Camera di Commercio, Agenzia delle Entrate)

### Step 7: INPS and INAIL Registration

- **INPS and INAIL Registration** — INPS: social security registration for directors and employees. INAIL: workplace insurance registration. Both handled via ComUnica

### Step 8: Tassa di Concessione Governativa

- **Tassa di Concessione Governativa** — Annual government concession tax for company books: €309.87. Payable for vidimazione of libro giornale, inventari, and verbali assemblee

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| S.r.l. (multi-shareholder) | €10,000 | 25% (€2,500) | At deed of incorporation | Permitted (expert appraisal or director's valuation for < €10,000) |
| S.r.l. (single shareholder) | €10,000 | 100% | At deed of incorporation | Permitted |
| S.r.l.s. | €1--€9,999 | 100% | At deed (cash only) | NOT permitted |
| S.p.A. | €50,000 | 25% (€12,500) | At deed of incorporation | Permitted (court-appointed expert required) |

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | S.r.l. Standard (EUR) | S.r.l.s. (EUR) | Notes |
| --- | --- | --- | --- |
| Notary fees | €800--€1,500 | €0--€400 | S.r.l.s. reduced/waived by law |
| Registration tax (imposta di registro) | €200 | €200 | Fixed for cash contributions |
| Stamp duty (bolli) | ~€156 | Exempt | S.r.l.s. exemption |
| Camera di Commercio (diritti camerali) | ~€120 | ~€120 | Initial registration |
| Tassa concessione governativa | €309.87 | €309.87 | Annual book-vidimation tax |
| PEC setup | €10--€50 | €10--€50 | Mandatory certified email |
| **Total initial (excl. capital)** | **€1,600--€2,500** | **€640--€1,100** |  |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (EUR) |
| --- | --- |
| Diritto annuale (Camera di Commercio) | €120 (base for società di capitali) |
| Tassa concessione governativa | €309.87 |
| Commercialista (accountant) fees | €2,000--€6,000/year |
| Bilancio deposito (annual accounts filing) | ~€60--€120 |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Bilancio (annual accounts) | Approve within 120 days of year-end; file within 30 days of approval | Registro delle Imprese |
| IRES/IRAP return (Modello Redditi SC) | By 30 November of following year | Agenzia delle Entrate |
| IVA declarations | Monthly or quarterly | Agenzia delle Entrate |
| Diritto annuale | 30 June (with tax return deadline) | Camera di Commercio |
| Titolare effettivo (UBO register) | Within 30 days of any change | Camera di Commercio |
| Libro soci updates | On any share transfer | Internal (notarised) |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Documents required for bank account** — Visura camerale (Chamber of Commerce extract); Atto costitutivo and statuto; ID and codice fiscale of all directors and shareholders; PEC address; Description of business activity

### Typical Timeline

- **Bank account opening timeline** — 1--3 weeks (Italian banks are typically thorough with KYC)

### Common Banks

- **Common banks** — Intesa Sanpaolo, UniCredit, BNL (BNP Paribas) (traditional); Banca Sella, Qonto Italy, Finom (digital)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes -- codice fiscale required (obtainable from Italian consulate or Agenzia delle Entrate) |
| Physical presence required? | Yes for notary deed (power of attorney possible but must itself be notarised and apostilled) |
| Apostille requirements | Foreign documents require apostille + sworn Italian translation |
| Foreign ownership restrictions | None for standard S.r.l.; regulated sectors may require authorisations |
| Codice fiscale for foreigners | Obtainable via Italian consulate abroad or Agenzia delle Entrate |

## Section 9 -- Common Mistakes and Refusals

- **R-IT-F1 -- Choosing S.r.l.s. for a growing business** — The S.r.l.s. has a rigid, non-customisable statuto and a capital ceiling of €9,999. It cannot accommodate investor-friendly provisions. Advise standard S.r.l. for any business expecting growth or external investment.  _(R-IT-F1)_
- **R-IT-F2 -- Failing to set up PEC** — PEC is legally mandatory. Failure to have an active PEC address can result in fines and makes the company unreachable for official communications.  _(R-IT-F2)_
- **R-IT-F3 -- Ignoring tassa concessione governativa** — The €309.87 annual government concession tax for company books is often overlooked by founders. It is mandatory regardless of turnover.  _(R-IT-F3)_
- **R-IT-F4 -- Single-shareholder S.r.l. with only 25% paid up** — For single-shareholder S.r.l., the law requires 100% of capital to be paid up at formation. The 25% minimum applies only to multi-shareholder S.r.l.  _(R-IT-F4)_
- **R-IT-F5 -- In-kind contributions in S.r.l.s.** — The S.r.l.s. only permits cash contributions. In-kind contributions are prohibited. Use a standard S.r.l. if non-cash contributions are needed.  _(R-IT-F5)_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Name check and document preparation | 2--5 days | Day 2--5 |
| Notary appointment | 1--5 days | Day 3--10 |
| Capital deposit | 1--5 days | Day 4--15 |
| Notary files with Registro delle Imprese | 1--3 days | Day 5--18 |
| Camera di Commercio registration complete | 3--7 days | Day 8--25 |
| Partita IVA and codice fiscale (via ComUnica) | 1--3 days | Day 9--28 |
| INPS/INAIL registration | Simultaneous with ComUnica | Day 9--28 |
| Bank account fully operational | 1--3 weeks | Day 16--49 |
| **Ready to trade** |  | **~2--5 weeks** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
