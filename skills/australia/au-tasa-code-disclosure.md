---
name: au-tasa-code-disclosure
description: "Scope-neutral conduct disclosure for the Australian guides in this library, on the law at 2 November 2026. States that the guides are reference material for a registered tax or BAS agent, not tax advice or a tax agent service; that the practitioner stays bound by the Code of Professional Conduct in section 30-10 of the Tax Agent Services Act 2009 and the Code Determination; how TPB(GS) 55/2026 applies to AI-assisted work; and, for members of the accounting bodies, APES 110 and APES 220. Carries no workflow, intake or tax rates. Trigger: 'TASA', 'Code of Professional Conduct', 'TPB', 'APES 110'."
version: 0.1
jurisdiction: AU
category: foundation
tax_year: 2026
tax_year_notes: "Law as at 2 November 2026"
last_updated: 2026-11-11
review_status: pending_review
tier: 2
verified_by: pending
license: FSL-1.1-ALv2
---

# Australian Tax Agent Services Act Disclosure

## What this file is

Load this file beside an Australian guide when output built on that guide may be used in a tax agent service or BAS service. It is deliberately narrow. It carries no workflow, no intake, no refusal catalogue and no tax rates, so it fits a guide on any Australian subject and any taxpayer. The only figures in it are the conduct rules' own periods and penalties.

The universal workflow (intake, working papers, refusals) lives in `workflow-base` and the domain bases in `skills/foundation/`. Penalty unit values live in `au-lodgment-deadlines-penalties`.

## The disclosure

> **Tax Agent Services Act disclosure.** The Australian guides in this library are reference material and drafting aids for a registered tax agent or BAS agent, or for staff working under one's supervision. They are not tax advice to any taxpayer, and the library does not provide a tax agent service: a service that ascertains or advises on liabilities, obligations or entitlements under a taxation law, or represents an entity before the Commissioner, where the entity can reasonably be expected to rely on it (*Tax Agent Services Act 2009* (TASA) s 90-5). A registered practitioner who uses a guide stays bound by the Code of Professional Conduct in TASA s 30-10 and the *Tax Agent Services (Code of Professional Conduct) Determination 2024*, including competence and reasonable care (Code items 7, 9 and 10), confidentiality (item 6), false or misleading statements (Determination s 15), client records (s 30), supervision (s 35) and quality management (s 40). When AI is used the practitioner remains responsible for the service, and AI output should be assessed, supplemented by professional judgement and verified before reliance (TPB(GS) 55/2026). The safe harbour in s 284-75(6) of Schedule 1 to the *Taxation Administration Act 1953*, from administrative penalties for false or misleading statements under s 284-75(1) or (4), depends on a registered tax or BAS agent, given all relevant taxation information, making the statement; a guide is not such an agent. A taxpayer must not use output built on a guide in place of a registered practitioner.

## How to use it

- **In output.** When output built on an Australian guide is addressed to a taxpayer, or may be used in a return, statement or advice, state the disclosure above or its substance in that output.
- **Code checks.** Apply the Code to the output as the table below indexes it. The table paraphrases TASA s 30-10; read the Act for the exact obligations.

| Code item | Obligation (paraphrased) | What output built on a guide must do |
| --- | --- | --- |
| 1 | Act honestly and with integrity | Invent no authority, evidence, review or certainty |
| 2 | Comply with the taxation laws in personal affairs | Flag for human review any practitioner compliance issue the task reveals |
| 3 | Account for client money or property held on trust | Direct no movement or use of trust money |
| 4 | Act lawfully in the client's best interests | Present only lawful options within the engagement |
| 5 | Keep adequate arrangements to manage conflicts of interest | Flag actual, potential or perceived conflicts |
| 6 | Disclose no client information to a third party without permission, unless legally required | Confirm permission before client information enters a third-party tool |
| 7, 8 | Provide services competently; keep knowledge and skills current | Use current law; flag where specialist input is needed |
| 9, 10 | Take reasonable care to ascertain the client's affairs and to apply the taxation laws correctly | Test facts; separate law, ATO view, judgement and uncertainty |
| 11 | Do not knowingly obstruct the proper administration of the taxation laws | Conceal nothing from the regulator |
| 12 | Advise the client of rights and obligations materially related to the service | State deadlines, choices and consequences within scope |
| 13 | Maintain professional indemnity insurance meeting the Board's requirements | Flag a service or tool use that may fall outside cover |
| 14 | Respond to the Board in a timely, responsible and reasonable manner | Escalate Tax Practitioners Board (TPB) correspondence at once |
| 15, 16 | Do not use an entity to provide services on the practitioner's behalf (without TPB approval), or provide services in connection with an arrangement with an entity, that the practitioner knows or ought reasonably to know is a disqualified entity | Allocate no work to, and support no arrangement with, a known or suspected disqualified entity |
| 17 | Comply with the Code Determination | Apply the sections below |

- **Code Determination.** Section 10 (uphold the profession's ethical standards); s 15 (no materially false or misleading statement to the Board or Commissioner, and the steps to take when a past statement is found to be wrong); ss 20 and 25 (conflicts and confidentiality in government work); s 30 (records showing the nature, scope and outcome of each service, the information considered, advice received and given and, for complex matters, the facts, assumptions and reasoning); s 35 (everyone providing services on the practitioner's behalf is competent and supervised); s 40 (a documented and enforced quality management system); s 45 (tell current and prospective clients about the TPB register, complaints, rights and obligations, specified adverse events in the last 5 years and current conditions or suspension). Amendments made from 1 October 2026 apply to events on or after that day (s 101); s 45 reaches only events on or after 1 July 2022 (s 151(1)).
- **AI-assisted work.** TPB(GS) 55/2026 (issued 22 July 2026): the practitioner remains responsible and should understand the tool's capabilities and limitations; AI output is assessed and supplemented by professional judgement before reliance, and verified and reviewed at each step of the workflow, with the steps documented; entering client information into an AI tool can be a disclosure to a third party, depending on how the tool is configured and used, so the client's permission must be obtained first, by a signed engagement letter, a signed consent or a fact-find and consent (a general authority may also be acceptable); and the practitioner performs due diligence so information stays secure and Privacy Act requirements are met.

**Time-critical clocks.** All read on 2 November 2026 in TASA compilation 27 and Code Determination compilation 4.

| Event | Period | Source |
| --- | --- | --- |
| Reasonable grounds to believe the practitioner's own breach is a significant breach | Notify the TPB in writing within 30 days of first having, or when the practitioner ought to have had, those grounds | TASA s 30-35(1)(ba), (4)(b) |
| Reasonable grounds to believe another agent's breach is a significant breach | Notify the TPB, and a TPB-accredited association if aware of the agent's membership, within 30 days | TASA s 30-40(1)-(3) |
| Other change of circumstances relevant to registration | Notify the TPB within 30 days of becoming, or when the practitioner ought to have become, aware | TASA s 30-35(4)(a) |
| Client records | Keep for at least 5 years after the service | Determination s 30(2)(b) |
| A specified adverse event, for an existing client not yet told | Within 30 days of the event | Determination s 45(2)(b)(ii) |
| Current registration conditions or suspension, for an existing client not yet told | As soon as reasonably practicable after the event | Determination s 45(2)(d)(ii) |

**Sanctions for conduct on or after 1 October 2026.** Schedule 1 to the *Treasury Laws Amendment (Strengthening Accountability for Tax Adviser Misconduct and Other Measures) Act 2026* commenced on 1 October 2026 and applies to conduct on or after that day (s 2 and Sch 1 item 70); earlier conduct stays under the earlier text.

- Failing to comply with the Code is a civil penalty provision: 2,500 penalty units for an individual and 50,000 for a body corporate (TASA s 50-31). The TPB may apply to the Federal Court within 4 years after the contravention, and only after an investigation under Subdivision 60-E (s 50-35(1), (4)).
- After an investigation the TPB may caution, make an order, suspend or terminate registration (s 30-15(2)). It may also suspend registration on an interim basis for up to 90 days without a natural justice hearing, extendable once an investigation has started (s 40-45(2)-(4)). The Act also provides for infringement notices (s 52-5) and enforceable undertakings (s 52-10).
- Providing a tax agent service (other than a BAS or tax (financial) advice service) for a fee whilst unregistered is an offence, subject to the section's other conditions: 200 penalty units or imprisonment for 40 months, or both (s 51-5(1)). Section 51-10 makes the matching offence for BAS services.

When a task discloses a possible Code failure, significant breach, suspension or unregistered service, flag it for the registered practitioner. Do not assess exposure, predict the TPB's response or notify anyone.

- **What this file does not do.** It does not decide whether a service is a tax agent service or BAS service, whether a breach is significant, or whether the s 284-75(6) safe harbour applies: the registered practitioner decides those. It does not refuse any engagement.

## APES 110 and APES 220

APES 110 *Code of Ethics for Professional Accountants (including Independence Standards)* binds Members of Chartered Accountants Australia and New Zealand, CPA Australia and the Institute of Public Accountants (APES 110 glossary, '[AUST] Member' and '[AUST] Professional Bodies'; paragraph R1.2). A registered agent who is not a Member is not bound by it unless law, regulation or the engagement terms incorporate it; the TASA applies either way. Each layer applies within its own scope, and meeting one does not meet another. This section paraphrases and cites APES 110; it does not reproduce it.

- **Fundamental principles.** Integrity, objectivity, professional competence and due care, confidentiality and professional behaviour (section 110, subsections 111 to 115), applied through the conceptual framework of identifying, evaluating and addressing threats (section 120).
- **Tax planning.** A Member may recommend or advise on a tax planning arrangement only after determining that it has a credible basis in laws and regulations (R280.12 for Members in business, R380.12 for Members in Public Practice). For Australian tax laws, the Australian application material equates a credible basis with a reasonably arguable position under s 284-15 of Schedule 1 to the *Taxation Administration Act 1953* (AUST 280.12 A1.1, AUST 380.12 A1.1). The work must be documented (AUST R280.23, AUST R380.26).
- **Non-compliance with laws and regulations.** Sections 260 (Members in business) and 360 (Members in Public Practice). Flag a suspected breach for the responsible Member; never warn, accuse or report anyone.
- **Technology and AI.** Under APESB's Technical Alert of 31 October 2025, a Member using AI keeps responsibility for the work, its professional judgements and its results. In summary, the Member should not depend unduly on AI, must test and verify AI output, and should say when AI tools were used and oversee their use. The alert notes that the Code's technology provisions have applied since 1 January 2025.
- **Taxation services.** APESB lists APES 220 *Taxation Services* (2025), effective from 1 July 2025, amongst its current pronouncements; a Member providing a taxation service checks it alongside APES 110.

The current compilation is 'Compilation of APES 110 Standard (Jul 2025)', listed under Standards & Guidance, Current Pronouncements at https://apesb.org.au/.

## Sources

All read on 2 November 2026.

| Source | URL | Read on |
| --- | --- | --- |
| *Tax Agent Services Act 2009*, compilation 27 (C2026C00441, from 1 October 2026): ss 30-5, 30-10, 30-15, 30-35, 30-40, 40-45, 50-31, 50-35, 51-5, 90-5 and the headings of ss 52-5 and 52-10 | https://www.legislation.gov.au/C2009A00013/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| *Tax Agent Services (Code of Professional Conduct) Determination 2024*, compilation 4 (F2026C00953, from 1 October 2026): ss 10 to 45, 100, 101, 151 | https://www.legislation.gov.au/F2024L00849/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| *Treasury Laws Amendment (Strengthening Accountability for Tax Adviser Misconduct and Other Measures) Act 2026* (No. 86, 2026), as made: s 2 and Sch 1 item 70 | https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| *Taxation Administration Act 1953*, compilation 227 (C2026C00468), Volume 2: Sch 1 s 284-75(1), (4)-(7) | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html | 2 November 2026 |
| TPB(GS) 55/2026, The use of artificial intelligence and the Code of Professional Conduct (issued 22 July 2026) | https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct | 2 November 2026 |
| TPB, Copyright notice (CC BY 3.0 AU; attribute as the Tax Practitioners Board) | https://www.tpb.gov.au/copyright-notice | 2 November 2026 |
| APESB: APES 110 Compilation (July 2025), paragraphs R1.2, R280.12, AUST 280.12 A1.1, AUST R280.23, R380.12, AUST 380.12 A1.1, AUST R380.26, sections 110 to 120, 260 and 360 and the glossary; Technical Alert, The ethical use of artificial intelligence by professional accountants (31 October 2025); current pronouncements list (APES 220) | https://apesb.org.au/ (Standards & Guidance, Current Pronouncements) | 2 November 2026 |

### Provenance and licence

Written on 2 November 2026 from the primary texts above. It has not been reviewed by a registered tax agent or a Member of an accounting body. Not yet confirmed: the full text of APES 220 was not read.

TPB material: the AI-specific obligations above adapt TPB(GS) 55/2026, which the TPB provides under the Creative Commons Attribution 3.0 Australia licence (the Commonwealth Coat of Arms, the TPB logo and material otherwise noted are excluded). Attribution: Tax Practitioners Board.

APES 110 is published under licence from the International Federation of Accountants by the Accounting Professional & Ethical Standards Board Limited, which reserves all rights. This file reproduces none of its text: it gives independently written summaries and paragraph references. Following the source repository's note on APESB's linking terms, it links only to APESB's main page.

Legislation is cited to the authorised Federal Register of Legislation versions; read the exact current law there.

Method adapted by its author from the TPB and APES 110 control sets (`src/guide/140-tpb-control-set.md`, `src/guide/150-apes-110-control-set.md`) and reference maps in ryanduguid/DrDebits, formerly ryanduguid/llm-tax-guardrails (commit 9daf087). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/DrDebits (formerly llm-tax-guardrails), FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

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
