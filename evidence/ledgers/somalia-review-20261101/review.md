# Independent Somalia statutory-baseline review, 1 November 2026

Reviewed freeze: `3fc0d47e51a7f337732c9744a7abe04fbc4799d5`, branch `codex/somalia-tax-2026`. Comparison base: `db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6`. Fresh reviewer read the candidate, ledgers, manifest, old-topic map, source-read record, writer receipt, `CLAUDE.md` and `docs/skill-template.md`. This record belongs to that exact freeze, not an eventual edited version.

**Result: revise one ledger quotation.** All 46 substantive ledger rules are supported as descriptions of the opened statutory baseline. Of 46 short quotations checked visually, 45 pass and residence row 15 needs the correction below. No other substantive correction was identified within this bounded scope. The two Guides are expressly provisional working papers. This review does **not** approve operative 2026 law, current-year coverage, country completion, filing readiness or accountant attestation.

## Required correction

`evidence/ledgers/so-cross-border-residence.md`, row 15, line 21: the purported exact quote begins `gacan-ka-saaridda`. The relevant sentence on Act 37 PDF page 93, article 78(3), begins **`Gacan-ka-saarista`**. Correct that word, or quote the narrower exact fragment `laguma dabaqaayo hantida maxalliga ah`. This is an evidence-transcription defect, not a change to the supported rule summary. A new render from the independently downloaded PDF confirmed the distinction. [Official Act 37 PDF](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

The reviewer did not edit the frozen Guide, ledger, manifest or initial receipts. The writer must make the correction and bind the changed ledger/manifest to a new freeze; the corrected row then needs a targeted recheck. Initial review evidence must be preserved.

## Independently opened sources and actual scope

Ordinary direct `curl -L --fail` downloads of the three official PDFs succeeded on 2026-11-01. SHA256 was recomputed independently, not copied from the writer. All match the supplied private files and recorded manifest. `pdfinfo` confirmed page counts. Full PDFs and PNGs remain outside Git.

| Official source | SHA256 and pages | Actual reviewer reading |
|---|---|---|
| [Act 37/2025](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) | `ee02cdda1b14270ac385469f2db90c3cc8c233b3b08c62f49e96180a4beaf85a`, 135 pages | Visual pages 1–3, 14, 25, 36–37, 48, 56–57, 91–93, 124–125. This includes every ledger clause, relevant adjacent clauses and exceptions, and the document identity/commencement chain. Existing private rendered scans were inspected; fresh renders from the independent download of pages 92 and 93 resolved detail checks. OCR served only as a locator/cross-check, never as the exact-quote authority. |
| [Revenue Authority Law 56/2026](https://sag.gov.so/media/documents/bulletins-contents/legislation/2026/Sharci_Lr_56_Hayadda_Dakhliga_Qaranka.pdf) | `a83fe74d9119c53144c9aa076b3a67bd3e8f2728030e1fbc2cdb37bc9e14c80b`, 21 pages | Visual enactment page 2 and pages 19–21, articles 22–27. Supports existing federal revenue-law administration and institutional transfer. Does not establish a live portal, submission address or acknowledgement workflow. |
| [2026 budget Law 44](https://sag.gov.so/media/documents/bulletins-contents/budget/2025/SHARCIGA_MIISAANIYADDA_SANADKA_2026.pdf) | `dbd8759b9a080e5056fe9a6155157eeb719c8be215977711cdd3d25b9e703d57`, 143 pages | Visual enactment page 2 and operative closing page 13; extracted operative appropriation text from title/contents through printed page 10 read. No specific TP/residence amendment was identified in that bounded text. Annex forecasts/tables were not researched as tax law. This does not certify that no amendment exists elsewhere. |
| [Ministry English Income Tax Manual, November 2025](https://mof.gov.so/sites/default/files/Publications/Somalia%20Income%20Tax%20Manual_English%20Version.pdf) | Web reader opened 25-page PDF; no local hash claimed | Contents, introduction/disclaimer, section III assessable-income scope and section VI residence tests read. Used as a reading aid for the Somali provisions, not as legislation or a substitute for unread regulations. The introduction states the Act/regulations prevail. No whole-manual or regulations read is claimed by this reviewer. |

The web PDF reader failed to open Act 37; direct official download then worked. Initial `git fetch origin` failed with DNS resolution of github.com. Local HEAD and the pinned base were verified, but this review does not represent a successful remote refresh. No access control was bypassed.

## Identity, applicability and stop gates

The official Act 37 file is an Attorney General gazette wrapper dated 17 August 2025, followed by the presidential Act 37 enactment dated 11 May 2025 and the enclosed statute. The enclosure retains its `HINDISE-SHARCIYEEDKA` heading. Reading that heading alone would miss the signed enactment immediately before it. The draft correctly discloses the mismatch and excludes an exact 2025 first-application conclusion. The signature-based wording on enactment page 2 and article 106's publication wording were both checked. The manual's general commencement statement does not remove this bounded uncertainty. [Act 37, PDF 1–3 and 125](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

Article 37(3) leaves exceptions/alternative standards and international-guideline choices to regulations. Article 105(7) permits transitional measures delaying or modifying operation, subject to its statutory limit. Regulations 0141/2025 and applicable transitional directions remain unread in this review. Therefore a general manual, the budget search and Law 56 cannot establish operative 2026 conditions. The frontmatter descriptions, body opening gates, Sources caveats and README partial entries consistently require a stop before final treatment. The task is evidence organisation and provisional reconciliation, not a completed return, certificate or current-year tax opinion. [Act 37, PDF 57 and 125](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

No tax rate, TP safe harbour, mandatory documentation threshold, prescribed method, penalty, treaty entitlement or live filing process is inferred from an omission. Recommendations for evidence schedules are identified as recommendations. This limited historical-baseline finding must not be used as an operative-2026 approval.

## Row-by-row source check

`Pass` means the substantive rule, its conditions, article/page reference and short quotation were checked against the visual source, allowing the declared line-break and typographic-apostrophe normalisation. It does not mean operative 2026 applicability. Repeated rules in the two ledgers were each checked in their own context.

| Pricing row | Source page / provision | Result and condition checked |
|---|---|---|
| 1 | 56–57, art.37(1) | Pass: resident dealing with associated non-resident; not all domestic transactions. |
| 2 | 56–57, art.37(1) | Pass: resident income and tax under independent-party standard. |
| 3 | 57, art.37(2) | Pass: calculation, characterisation and allocation as independent persons. |
| 4 | 25, art.4(1)(b) | Pass: relative/dependant association. |
| 5 | 25, art.4(1)(t) | Pass: partners within the same partnership. |
| 6 | 25, art.4(1)(x) | Pass: specified instruction relationship; ordinary employment exclusion belongs to that limb. |
| 7 | 25, art.4(2)(b) | Pass: control is an alternative to numerical rights. |
| 8 | 25, art.4(2)(b) | Pass: 50% or more income, capital or voting rights, not only share capital. |
| 9 | 25, art.4(2)(b)(i) | Pass: alone or aggregated with associated persons. |
| 10 | 25, art.4(2)(b)(ii) | Pass: direct/indirect rights through other entities. |
| 11 | 25, art.4(2)(t) | Pass: association with a qualifying person under the preceding limb. |
| 12 | 57, art.37(3)(b) | Pass: regulations determine exceptions/alternative standards; no absence inferred. |
| 13 | 57, art.37(3)(t) | Pass: regulations determine international guidance and modifications. |
| 14 | 57, art.37(4)(b) | Pass: noncompliance condition and transaction recharacterisation power. |
| 15 | 57, art.37(4)(t) | Pass: source/nature of income, loss, amount or payment covered. |
| 16 | 57, art.37(4)(j) | Pass: expense allocation by turnover. |
| 17 | 48, art.25(1)–(3) | Pass: default calendar year; corporation/trust application and approval conditions. |
| 18 | 125, art.105(7) | Pass: regulation/transition gate, not a claimed delay actually made. |
| 19 | 2, signed enactment | Pass: stated 11 May 2025 date; exact first application excluded. |
| 20 | 125, art.106 | Pass: publication is in the commencement wording. |
| 21 | 124, art.105(1),(3) | Pass: earlier-period saving; no mixed-period conclusion invented. |
| 22 | Law 56 p.19, art.23 | Pass: existing income-tax law within administration; not fresh substantive tax rules. |
| 23 | Law 56 p.21, art.26(2) | Pass: institutional transfer, not operational portal verification. |

| Residence row | Source page / provision | Result and condition checked |
|---|---|---|
| 1 | 14, art.2(7) | Pass: definition refers to article 77. |
| 2 | 91, art.77(1)(b) | Pass: permanent home in Somalia is a separate ground. |
| 3 | 92, art.77(1)(t) | Pass: citizenship and foreign permanent-home availability for whole-year exception. |
| 4 | 92, art.77(1)(j) | Pass: 183 days or more in aggregate, not necessarily continuous. |
| 5 | 92, art.77(1)(j) | Pass: any relevant 12-month period commencing/ending during year, plus presence during year. |
| 6 | 92, art.77(1) posting limb | Pass: federal/state employee or official posted abroad during year. |
| 7 | 92, art.77(2) | Pass: any partner resident at any time during year. |
| 8 | 92, art.77(3)(b),(t) | Pass: local settlement/establishment or any-time resident trustee. |
| 9 | 92, art.77(3)(j) | Pass: resident control/power to control; sole/joint and direct/interposed alternatives. |
| 10 | 92, art.77(4)(b) | Pass: local incorporation/formation/organisation/establishment. |
| 11 | 92, art.77(4)(t) | Pass: effective management locally at any time during year. |
| 12 | 91–92, art.77(1) | Pass: alternative tests; 182 days does not override home ground. |
| 13 | 48, art.25(1)–(3) | Pass: 1 January–31 December, with approved alternative for corporation/trust. |
| 14 | 93, art.78(1) | Pass: sole day-count ground and no preceding-year residence; period-start distinction preserved. |
| 15 | 93, art.78(2),(3) | Rule passes: entry cost/departure deemed disposal and domestic-asset exceptions. Exact quotation fails: `saaridda` substituted for `saarista` in quoted sentence. Required correction above. |
| 16 | 36–37, art.11(b) | Pass: resident worldwide employment/business/investment assessable scope, not final tax. |
| 17 | 37, art.11(t) | Pass: Somali-PE worldwide income plus other Somali-source income outside that limb; no PE attribution computed. |
| 18 | 125, art.105(7) | Pass: regulatory/transition gate; operative conditions not certified. |
| 19 | 2, signed enactment | Pass: stated enactment date; first application excluded. |
| 20 | 125, art.106 | Pass: publication wording checked. |
| 21 | 124, art.105(1),(3) | Pass: earlier-period saving; no transition outcome claimed. |
| 22 | Law 56 p.19, art.23 | Pass: administration of existing federal income-tax law. |
| 23 | Law 56 p.21, art.26(2) | Pass: transfer, not proof of current submission workflow. |

## Examples, preservation and mechanical checks

The four examples were recomputed independently: sale 1,000 × 80 = 80,000 and 1,000 × 100 = 100,000, difference +20,000; associated rights 49 + 1 = 50 and purchase 500 × 120 = 60,000 versus 500 × 100 = 50,000, income difference +10,000; presence 90 + 70 + 23 = 183; alternative presence 90 + 70 + 22 = 182, one day short. The home-test distinction remains separate from the last arithmetic. Hypothetical evidence and resolved-regulation assumptions are explicit. Arithmetic does not prove any real client's facts or final tax.

All seven manifest content hashes match. All six legacy files are byte-identical to the pinned base and manifest, including frontmatter and complete platform CTA blocks. All 71 pre-CTA headings/bold topic labels have entries in the 71-row old-topic map, with no missing labels. Byte equality also preserves every narrative paragraph, beyond those labels. Manual spot checks included legacy residence, non-residents, corporate/withholding topics, payroll/social claims, sales-tax reverse charge/input credit and company formation. Their retention is not recertification. **Lost content restored: 0; no source Guide was rewritten, merged, renamed or deleted.**

The reviewer reran changed-only validation (2 Guides, zero warning groups), all 15 skill checks for both Guides, 4 required executable examples, pinned-base strict sync integrity (2 Guides, zero errors/warnings/notices) and `git diff --check`; all passed. Exact command output, all hashes, old-topic/CTA results and arithmetic are in [mechanical-checks.json](mechanical-checks.json).

Setup failures are disclosed: initial invocation without the supplied PYTHONPATH failed on missing `yaml`; after setting PYTHONPATH the intended checks passed. An attempted `validate-guides.py --help` is unsupported by that script and instead ran full-tree validation: six legacy Guides generated warning groups and stale generated index/LLM inventory caused two errors. An attempted `skill_checks.py --help` treated it as a filename and failed. These probes changed no content. The intended bounded validations above, with exact outputs, are the acceptance evidence; no generator was run to silence the unrelated full-tree results.

## Items still not confirmed and work deliberately not done

Regulations 0141/2025, transitional directions and their operative 2026 effect; exact 2025 first application; TP methods/exceptions/documentation, thresholds and procedures; present portal/forms/payment and acknowledgement path; penalties/interest/appeals; territorial administration; treaty/PE/source/withholding/foreign-credit outcomes; part-day/transit rules; client permanent-home/effective-management facts; part-year and entry/exit asset computations. The reviewer did not claim to read all 135 Act pages or budget annexes, did not rebuild the six retained Guides, and did not research every acknowledged gap.

No Guide or initial evidence file was edited. No commit, push, PR, public comment, publication, attestation or completion action was performed. Only this review directory was added. Mechanical success does not close any legal or operative coverage gate.
