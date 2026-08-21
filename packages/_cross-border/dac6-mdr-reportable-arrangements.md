---
name: dac6-mdr-reportable-arrangements
description: "Use this skill whenever an intermediary (tax adviser, lawyer, accountant, bank, trust company) or a relevant taxpayer asks about mandatory disclosure of cross-border tax arrangements. Trigger on phrases like \"DAC6\", \"MDR\", \"mandatory disclosure rules\", \"reportable cross-border arrangement\", \"hallmark A1\", \"hallmark E3\", \"main benefit test\", \"MBT\", \"legal professional privilege\", \"DAC6 notification\", \"BZSt reporting\", \"arrangement reference number\", \"ARN\", \"OECD model MDR\", \"CRS avoidance arrangement\", or any request to determine whether an arrangement must be reported under DAC6 (EU Directive 2018/822) or equivalent OECD MDR rules in non-EU jurisdictions. Covers EU Member States, UK MDR (the post-Brexit OECD-aligned regime in SI 2023/38), and the OECD Model Mandatory Disclosure Rules on CRS Avoidance Arrangements and Opaque Offshore Structures (2018). Does NOT cover: domestic-only tax shelter disclosure regimes (e.g., US §6111 reportable transactions, UK DOTAS, Canada §237.3), country-by-country reporting (BEPS Action 13), or FATCA/CRS automatic exchange (see fatca-crs-automatic-exchange). ALWAYS read this skill before advising on whether a cross-border arrangement triggers reporting."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DAC6 MDR Reportable Arrangements

## DAC6 / MDR — Mandatory Disclosure of Reportable Cross-Border Arrangements v0.1

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It implements:

- **EU Council Directive 2018/822 (DAC6)** as transposed into the 27 EU Member States (in force from 1 July 2020 for reporting; reportable arrangements with first step from 25 June 2018 onwards).
- **UK MDR (Mandatory Disclosure Rules)** under the International Tax Enforcement (Disclosable Arrangements) Regulations 2023 (SI 2023/38), in force from 28 March 2023.
- **OECD Model Mandatory Disclosure Rules on CRS Avoidance Arrangements and Opaque Offshore Structures** (2018) as adopted by various non-EU jurisdictions.

**Tax year coverage.** Current for **arrangements with a first step on or after 1 January 2025**. The historical DAC6 backlog (June 2018 → June 2020) is addressed in Section 5.

**The reviewer is the customer of this output.** DAC6 / MDR analysis turns on legal classification, intent, and privilege. Outputs must be reviewed by a credentialed practitioner (typically a tax lawyer or Big 4 specialist) before any filing or refusal-to-file decision.

## Section 1 — Scope statement

This skill covers:

- **Hallmark classification** (Categories A, B, C, D, E under DAC6; equivalent hallmarks under UK MDR and OECD model).
- **Main Benefit Test (MBT)** application to Category A, B, and certain C hallmarks.
- **Reporting obligations**: who reports (intermediary or relevant taxpayer), where (jurisdiction priority rules), when (30-day window), what (the eleven data points in Article 8ab(14)).
- **Legal professional privilege (LPP) carve-outs** by Member State.
- **Penalty regimes** by Member State and the UK.
- **Interaction with DAC7 (digital platforms)** and **DAC8 (crypto-assets)** — out of scope for content but cross-referenced.

This skill does NOT cover:

- **Domestic-only tax shelter disclosure** — US §6011/§6111/§6112 reportable transactions, UK DOTAS, Australian PCG 2024 reportable arrangements, Canadian §237.3 reportable transactions.
- **Country-by-country reporting** under BEPS Action 13 — see `cbcr-beps-13.md` (forthcoming).
- **FATCA/CRS automatic exchange** — see `fatca-crs-automatic-exchange.md`.
- **State aid recovery and EU anti-abuse rules** — see `eu-state-aid-tax-rulings.md` (forthcoming).
- **Pillar Two anti-abuse rules** — see `pillar-two-globe-minimum-tax.md`.

## Section 2 — Filing requirements

### Who is the reporter

- **Reporter priority order** — 1. **Intermediary** — any person that designs, markets, organises, makes available for implementation, or manages the implementation of a reportable cross-border arrangement. Includes service intermediaries (those who provide aid, assistance, or advice with respect to the foregoing). 2. **Relevant taxpayer** — the person to whom the reportable cross-border arrangement is made available, or who is ready to implement, or who has implemented the first step. Reports only where no intermediary is reportable in the EU/UK, or where all relevant intermediaries claim privilege.  _([T1] Article 8ab DAC6)_

### Who is an intermediary

**Two tests for intermediary status**  _([T1] Article 3(21) DAC6)_

| Test | Trigger |
| --- | --- |
| Promoter test | The person designs, markets, organises, makes available, or manages implementation |
| Service-provider test | The person provides aid, assistance, or advice with respect to the design/marketing/organising/availability/implementation, *and* a reasonable person in the same position would have known the arrangement is reportable |

- **Connecting nexus to the EU** — At least one of: Tax resident in a Member State; Permanent establishment in a Member State through which services are provided; Incorporated/governed by laws of a Member State; Registered with a professional association related to legal, taxation or consultancy services in a Member State  _(Article 3(21) DAC6)_

### Reporting jurisdiction priority

- **Priority order if multiple intermediaries / multiple Member States could claim reporting** — 1. Member State where the intermediary is **tax resident**. 2. Otherwise: Member State where the intermediary has a **PE** through which the services were provided. 3. Otherwise: Member State where the intermediary is **incorporated** or **governed**. 4. Otherwise: Member State where the intermediary is **registered with the professional association**. An intermediary is exempt where it can prove the arrangement has already been reported by another intermediary in a Member State or by the taxpayer.  _([T1] Article 8ab(3))_

### When to report

- **30-day reporting window trigger events** — The clock starts on the EARLIEST of: The day after the arrangement is made available for implementation; The day after the arrangement is ready for implementation; The day after the first step of implementation has been taken. For service intermediaries the clock starts the day after they provide aid, assistance or advice. For marketable arrangements, the intermediary must file a quarterly update.  _([T1] Article 8ab(1); Article 8ab(2))_

### What to report

- **The eleven data points** — 1. Identification of intermediaries and relevant taxpayers (name, DoB/incorporation, tax residence, TIN) 2. Details of the hallmarks that make the arrangement reportable 3. Summary of the arrangement (commercial name; abstract description; no LPP-protected detail required) 4. Date on which the first step has been or will be taken 5. Details of national tax provisions concerned 6. Value of the reportable cross-border arrangement 7. Identification of the Member State of the relevant taxpayer(s) and of any other Member States likely to be concerned 8. Identification of any other persons in a Member State likely to be affected 9. Identification of associated enterprises 10. The arrangement reference number (ARN) — issued by the receiving Member State and reused across all Member States 11. Updated data points where there is a change  _([T1] Article 8ab(14))_

## Section 3 — The five hallmark categories

Each Member State transposed DAC6 substantially uniformly; UK MDR substantially mirrors hallmarks A, B, certain C, D, and E but uses different drafting.

### Category A — Generic hallmarks (MBT required)

**Category A hallmarks**

| Hallmark | Description |
| --- | --- |
| **A.1** | Arrangement where the relevant taxpayer / participant undertakes to comply with a confidentiality condition that may require them not to disclose how the arrangement could secure a tax advantage. |
| **A.2** | The intermediary is entitled to a fee fixed by reference to (a) the tax advantage derived OR (b) whether a tax advantage is actually derived (e.g., contingency fee). |
| **A.3** | The arrangement has substantially standardised documentation or structure, available to more than one taxpayer, without need for substantial customisation. |

### Category B — Specific hallmarks (MBT required)

**Category B hallmarks**

| Hallmark | Description |
| --- | --- |
| **B.1** | A participant takes contrived steps consisting in acquiring a loss-making company, discontinuing its main activity, and using the losses in order to reduce its tax liability. |
| **B.2** | Conversion of income into capital, gifts, or other categories of revenue taxed at a lower level or exempt. |
| **B.3** | Circular transactions resulting in the round-tripping of funds through entities without primary commercial function or transactions that offset / cancel each other. |

### Category C — Cross-border deductible payments

**Category C hallmarks**

| Hallmark | MBT? | Description |
| --- | --- | --- |
| **C.1(a)** | No | Cross-border deductible payments where the recipient is not resident in any tax jurisdiction. |
| **C.1(b)(i)** | No | Cross-border deductible payments where the recipient is resident in a jurisdiction that levies no corporate tax or a corporate tax rate of zero or almost zero. |
| **C.1(b)(ii)** | **Yes** | Cross-border deductible payments where the recipient is resident in a jurisdiction included on the EU list of non-cooperative jurisdictions. |
| **C.1(c)** | **Yes** | The payment benefits from a full exemption in the jurisdiction of the recipient. |
| **C.1(d)** | **Yes** | The payment benefits from a preferential tax regime in the jurisdiction of the recipient. |
| **C.2** | No | Deductions for the same depreciation on the same asset are claimed in more than one jurisdiction. |
| **C.3** | No | Relief from double taxation in respect of the same item of income or capital is claimed in more than one jurisdiction. |
| **C.4** | No | Arrangements that include transfers of assets where there is a material difference in the amount being treated as payable in consideration for the assets in those jurisdictions. |

### Category D — CRS/transparency hallmarks (no MBT)

**Category D hallmarks**

| Hallmark | Description |
| --- | --- |
| **D.1** | An arrangement that may have the effect of undermining the reporting obligation under the laws implementing the EU automatic exchange of information legislation (CRS / DAC2) or that takes advantage of the absence of such legislation. Covers eight specific sub-features (D.1(a)–(g)) reflecting the OECD Model MDR on CRS Avoidance Arrangements. |
| **D.2** | An arrangement involving a non-transparent legal or beneficial ownership chain with the use of persons, legal arrangements or structures (a) that do not carry on substantive economic activity supported by adequate staff, equipment, assets and premises; (b) that are incorporated, managed, resident, controlled or established in any jurisdiction other than the jurisdiction of residence of one or more of the beneficial owners of the assets held; and (c) where the beneficial owners are made unidentifiable. |

### Category E — Transfer pricing (no MBT)

**Category E hallmarks**

| Hallmark | Description |
| --- | --- |
| **E.1** | An arrangement that involves the use of unilateral safe harbour rules. |
| **E.2** | An arrangement involving the transfer of hard-to-value intangibles for which no reliable comparables exist at the time of transfer and projections of future cash flows / income are uncertain. |
| **E.3** | An arrangement involving an intragroup cross-border transfer of functions, risks or assets if the projected annual EBIT, during the three-year period after the transfer, of the transferor(s) is less than 50% of the projected annual EBIT of such transferor(s) if the transfer had not been made. |

## Section 4 — Computation rules

### Step 1 — Identify whether the arrangement is "cross-border"

- **Cross-border test** — An arrangement that concerns more than one Member State, or a Member State and a third country, where at least one of the following: Not all participants are tax resident in the same jurisdiction; One or more participants are simultaneously tax resident in more than one jurisdiction; One or more participants carry on business in another jurisdiction through a PE there, and the arrangement forms part or whole of the business of that PE; One or more participants carry on activity in another jurisdiction without being resident or creating a PE there; The arrangement has a possible impact on the automatic exchange of information or the identification of beneficial ownership. If purely domestic → not in scope.  _([T1] Article 3(18) DAC6)_

### Step 2 — Test each hallmark

- **Hallmark testing procedure** — For each potential hallmark, walk the definition mechanically. Document: Which factual elements of the arrangement meet which sub-element of the hallmark; Where the evidence sits.

### Step 3 — Apply the Main Benefit Test where required (Article 3(19))

- **MBT definition** — the main benefit, or one of the main benefits, that a person may reasonably expect to derive from an arrangement, having regard to all relevant facts and circumstances, is the obtaining of a tax advantage.  _([T1] Article 3(19))_
- **MBT applies to** — all Category A hallmarks, all Category B hallmarks, hallmarks C.1(b)(ii), C.1(c), C.1(d).
- **MBT does not apply to** — C.1(a), C.1(b)(i), C.2, C.3, C.4, Category D (all), Category E (all). These hallmarks make an arrangement reportable irrespective of tax-advantage intent.

**[T2] MBT analysis is judgement-heavy.** Document:
- The tax advantage hypothesised
- The non-tax commercial benefits
- A comparative ranking
- The reviewer's conclusion

### Step 4 — Determine the reporter and reporting jurisdiction

- **Reporter determination procedure** — Apply Section 2 priority rules. Document: Whether the user is acting as intermediary or relevant taxpayer; Which Member State has primary reporting right; Whether other intermediaries are also reportable and whether they have filed.

### Step 5 — Assemble the 30-day timeline

- **Timeline assembly procedure** — Identify each of the three trigger events (made available / ready / first step). Pick the earliest. Plot a 30-day countdown.

### Step 6 — Prepare the eleven data points

- **Portal schema by jurisdiction** — Use the receiving Member State's portal schema (e.g., DAC6XML 4.0 in Germany; "DAC6 manager" in Italy; "DECLOYER" in France; UK HMRC's DAC6/MDR submission portal).

### Step 7 — Confirm legal professional privilege if relied upon

LPP carve-outs vary materially:

**LPP scope by jurisdiction**

| Jurisdiction | LPP scope |
| --- | --- |
| **Germany** | Rechtsanwälte, Steuerberater, Wirtschaftsprüfer have LPP for advice-only; design/marketing falls outside |
| **France** | Avocats are exempt for promotor and service-provider activities — full LPP carve-out post-Cour de cassation 2022 |
| **Ireland** | Solicitors and barristers — privilege carve-out for legal advice |
| **Netherlands** | Advocaten — LPP carve-out; tax advisers without legal qualification do NOT have LPP |
| **Luxembourg** | Avocats — LPP carve-out |
| **Belgium** | Avocats — LPP carve-out, but the Constitutional Court (judgment 167/2020) found the LPP notification requirement (informing the next intermediary or taxpayer) incompatible with privilege; CJEU 8 Dec 2022 (C-694/20) confirmed |
| **Italy** | Avvocati — LPP carve-out; commercialisti do NOT |
| **Spain** | Abogados — LPP carve-out; asesores fiscales do NOT |
| **UK** | LPP for legal advice from solicitors and barristers; the rest must report |

**[T2] Where the user claims LPP:**
- They must still notify any other intermediary (or, in the absence of intermediaries, the relevant taxpayer) of the reporting obligation, except where that notification itself is impermissible under national LPP (e.g., Belgium post-CJEU C-694/20).
- The receiving Member State should be informed of the LPP claim.

### Step 8 — Track the Arrangement Reference Number (ARN)

- **ARN tracking** — The receiving Member State issues an ARN at first filing. All subsequent reports for the same arrangement (by other intermediaries, by the taxpayer, or updated returns) reference the ARN.

### Step 9 — Annual taxpayer disclosure (Article 8ab(11))

- **Annual disclosure obligation** — Each relevant taxpayer must, in their annual tax return, disclose the use of any reportable cross-border arrangement in which they are involved. This is independent of the 30-day intermediary report.  _(Article 8ab(11))_

## Section 5 — Edge cases and special rules

### 5.1 The June 2018 → June 2020 backlog

- **Backlog filing deadline** — Arrangements where the first step was implemented between 25 June 2018 and 30 June 2020 were reportable by 28 February 2021 (extended from 31 August 2020 by Council Directive (EU) 2020/876). New filings in this window today should be rare but may still arise on discovery.  _(Council Directive (EU) 2020/876)_

### 5.2 Marketable arrangements (Article 3(24))

- **Marketable arrangement definition and quarterly update rule** — A reportable cross-border arrangement that is designed, marketed, ready for implementation or made available for implementation without a need to be substantially customised. Quarterly updates required: by 30 April, 31 July, 31 October, 31 January, the intermediary must update the receiving Member State with the new relevant taxpayers identified in the prior quarter.  _(Article 3(24))_

### 5.3 Hallmark D.1 — CRS avoidance sub-features

- **D.1 eight sub-features** — D.1 captures eight specific patterns from the OECD Model MDR on CRS Avoidance: - D.1(a) — use of an account, product or investment that is not, or purports not to be, a Financial Account - D.1(b) — transfer of accounts to jurisdictions not bound by automatic exchange of Financial Account information with the Member State of the taxpayer - D.1(c) — reclassification of income and capital into products / payments not subject to automatic exchange - D.1(d) — transfer or conversion of a Financial Institution or Financial Account into a Financial Institution or Financial Account not subject to CRS reporting - D.1(e) — use of legal entities, arrangements or structures that eliminate or purport to eliminate reporting of one or more Account Holders or Controlling Persons under CRS - D.1(f) — undermining or exploiting weaknesses in due diligence procedures used by Financial Institutions to identify Account Holders or Controlling Persons - D.1(g) — arrangements involving the transformation of a Reportable Account into a non-reportable account  _(OECD Model MDR on CRS Avoidance Arrangements)_

### 5.4 UK MDR specifics (SI 2023/38)

The UK exited DAC6 reporting on 28 March 2023. The new UK MDR captures only **Category D** hallmarks (CRS avoidance and opaque ownership) as adopted from the OECD Model MDR. Hallmarks A, B, C and E that were reportable under UK-DAC6 are NO LONGER reportable under UK MDR.

**UK MDR summary table**  _(SI 2023/38)_

| Item | UK MDR |
| --- | --- |
| In-force date | 28 March 2023 |
| Hallmark scope | Category D only (CRS avoidance and opaque structures) |
| Reporter | "Intermediary" (promoter or service provider) or "Reportable Taxpayer" |
| Window | 30 days |
| Reference number | URN issued by HMRC |
| Penalties | Up to £600/day for late filing; higher penalties for deliberate failure |
| Privilege | LPP for legal advice; tax advice not privileged |

### 5.5 Penalties — illustrative

**Penalties by jurisdiction**

| Jurisdiction | Penalty |
| --- | --- |
| **Germany** | Up to €25,000 per failure (§ 379 Abgabenordnung) |
| **France** | Up to €10,000 per failure, capped at €100,000 per year (CGI art. 1729 C ter) |
| **Italy** | €3,000 to €31,500 per failure (D.Lgs. 100/2020 art. 12) |
| **Netherlands** | Up to €870,000 per failure for deliberate non-disclosure (AWR art. 10h) |
| **Spain** | €1,000 to €600,000 depending on data points missing (Ley 10/2020 DT 4) |
| **Ireland** | €500/day; €4,000 fixed for late filing; criminal sanctions for fraudulent failure |
| **Luxembourg** | Up to €250,000 per failure |
| **UK MDR** | £5,000 standard, up to £600/day continuation, higher for deliberate failures |

### 5.6 Interaction with DAC7 (digital platforms) and DAC8 (crypto-assets)

DAC7 (digital platform reporting) and DAC8 (crypto-assets) are separate exchange regimes. An arrangement that has a possible impact on DAC7 or DAC8 reporting can engage hallmark D.1 (CRS-style avoidance). See `dac7-platform-reporting.md` (forthcoming) and the EU crypto-tax skills.

### 5.7 Cross-EU coordination of ARNs

- **ARN cross-referencing across Member States** — Following Council Implementing Regulation (EU) 2020/1132, each Member State issues an ARN at first filing and all other Member States accept it for cross-references. The reporting intermediary in Member State A informs the taxpayer of the ARN, and the taxpayer or other intermediaries reference the same ARN when filing in Member State B.  _(Council Implementing Regulation (EU) 2020/1132)_

### 5.8 OECD Model MDR adoption outside the EU

**OECD Model MDR adoption status by jurisdiction**

| Jurisdiction | Status |
| --- | --- |
| **UK** | Adopted (Category D only) — SI 2023/38 |
| **Mexico** | Adopted (Ley del ISR Art. 197–202) — covers CRS avoidance hallmarks; broader hallmarks than D.1 |
| **Argentina** | Adopted in respect of certain offshore structures (Resolución General 4838/2020) |
| **Australia** | Not adopted as MDR; reportable arrangements regime under PCG 2024 covers a different scope |
| **Canada** | Reportable Transactions and Notifiable Transactions under §237.3 / §237.4 — domestic regime, broader than OECD MDR but different drafting |
| **South Africa** | Section 80M Income Tax Act — domestic-leaning regime |
| **New Zealand** | Disclosure of foreign trusts; no formal adoption of OECD MDR Category D |
| **Switzerland** | No DAC6/MDR adoption; SBA AML and tax-evasion-as-predicate-offence provisions apply |

## Section 6 — Output specification

The reviewer brief must include:

1. **Arrangement summary** — anonymised description of the arrangement, parties, jurisdictions, value.
2. **Cross-border test** — confirmation that Article 3(18) is met (or not).
3. **Hallmark matrix** — for each potential hallmark A.1 through E.3, classify Yes / No / Indeterminate with reasoning.
4. **MBT analysis** where any A, B, or C.1(b)(ii)/C.1(c)/C.1(d) hallmark is potentially in play.
5. **Reporter analysis** — who reports, in which jurisdiction, by when.
6. **LPP analysis** if applicable.
7. **Data points draft** — eleven Article 8ab(14) data points filled in, ready for portal submission.
8. **Penalty exposure** — estimated penalty if missed, by reporter and jurisdiction.
9. **Reviewer questions** — open items at [T2]/[T3] flagged for sign-off.

## Section 7 — Self-checks

Before delivering output, verify:

- [ ] The arrangement is cross-border per Article 3(18). Domestic arrangements are not reportable under DAC6.
- [ ] Each hallmark walked sub-element by sub-element; no narrative shortcuts.
- [ ] MBT applied only to A, B, and C.1(b)(ii)/(c)/(d).
- [ ] D and E hallmarks treated as no-MBT — reportable irrespective of tax intent.
- [ ] Reporter priority applied — intermediary first, taxpayer only if no intermediary OR all claim privilege.
- [ ] 30-day window counted from earliest of the three triggers (made available / ready / first step).
- [ ] LPP carve-out applied per the Member State of the intermediary, not the taxpayer.
- [ ] CJEU C-694/20 considered for any LPP notification cascade.
- [ ] Receiving Member State portal schema matched (DAC6XML 4.0 or local equivalent).
- [ ] ARN registered and cross-referenced for any second filing.
- [ ] Annual taxpayer disclosure obligation (Article 8ab(11)) noted on tax return checklist.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 8 — Prohibitions

- **Do not** advise on whether an arrangement is or is not "abusive". DAC6 is reporting, not anti-avoidance.
- **Do not** treat absence of MBT as conclusive. Category C.1(a)/(b)(i)/(2)/(3)/(4) and all of D and E are reportable without MBT.
- **Do not** rely on LPP without confirming the user is qualified for it in the relevant Member State and that the arrangement is genuinely legal advice (not design/marketing).
- **Do not** refuse to file based on LPP without also serving the notification on the next intermediary or relevant taxpayer where the Member State requires it.
- **Do not** apply UK MDR hallmark scope (Category D only) to arrangements with EU intermediaries — the EU intermediary remains subject to the full DAC6 hallmark list.

## Section 9 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. DAC6 / MDR involves classification under hallmarks whose interpretation is contested in the courts and varies materially by Member State. Every output must be reviewed and signed off by a credentialed tax lawyer or equivalent in the reporting jurisdiction before filing or refusing to file.

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
