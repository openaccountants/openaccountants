# Liechtenstein independent whole-pack source review

Review date: 24 October 2026. Reviewer: fresh independent AI agent, separate from the country writer. This is a source and calculation review, not a credentialed accountant sign-off, certified translation, complete legal audit or comprehensive-coverage determination.

## Decision at original checkpoint

Two actionable P2 findings require correction before country publication. All 24 original calculation controls independently recompute. No further confirmed substantive error was found within the legal and administrative passages inspected below. This limited result does not remove the seven partial-domain flags or any professional-review gate. Corrected blobs have not yet been closed by this report.

## Exact scope and independence

Source checkpoint: `d1faf74d0b9f0e07cf5a9374a231451e3cfd8f4c`. Initial checkout HEAD `27f191c0db87904b54e7ccd4bdedbb59872b5f8e` added the review brief only. The writer subsequently merged published OWNERS workflow updates while keeping these country blobs frozen. I read all eight Guides and README in full, including descriptions/frontmatter, bodies, calculations, sources, referral boundaries and CTAs; I did not restrict review to changed paragraphs. All nine hashes were independently matched to the brief before corrections began.

All paths below are relative to `skills/international/liechtenstein/`:

| File | Reviewed Git blob | Controls |
|---|---|---:|
| README.md | 110f20262410faacde01f4d2fdafd3fd699a16cb | 0 |
| li-company-formation.md | 0ba77b0b61f38b07e30a38a048e918fbd112c098 | 2 |
| li-corporate-income-tax.md | cda610045cf4201532c085de5d943ced2c2b05c6 | 4 |
| li-cross-border.md | b0d8614498184c5e68c02ef6dd1d9d2dad36c517 | 3 |
| li-income-tax.md | f2d1f9bba7c6cf23857404c2395f31b3a39cf9fb | 4 |
| li-payroll-social.md | 9f9de83278f1a32a467c69b49c915d58602fc2be | 4 |
| li-tax-overview.md | 36cd761e0574c6320c221f0941150c45634c8073 | 0 |
| li-transfer-pricing.md | 591dae8e9f13e62222acfc2eb4e62c761dee0024 | 3 |
| liechtenstein-vat.md | e1f1e91cc3f8fc7d52028891649ed7635b9920ba | 4 |

Read applicable supplied firm/engineering instructions, local CLAUDE.md, GOAL.md, OWNERS country-batch requirements, docs/skill-template.md, the country review brief, reconciliation, source-retrieval and transport records. Existing unrelated untracked files were left untouched. I did not edit any repository file, commit, push, merge, file a return or make a payment. This report is my only written output file. Writer evidence was used to locate material, not accepted as independent verification.

## Findings requiring correction

### F1, P2: apply the separate resident subsistence exemption before the tariff

Location: li-income-tax.md, original lines 31–41 and the three tariff tables, particularly the sentence that basic exemptions apply through the zero band.

SteG article 19(1) expressly reserves article 15(2)(i), which exempts qualifying unlimited taxpayers whose relevant total income does not exceed the Existenzminimum. SteV article 8 specifies the monthly gross amounts: CHF 2,100 single; CHF 2,600 single parent; CHF 3,200 joint spouses/registered partners; CHF 1,600 each for separately assessed spouses/registered partners sharing a household and de facto partners; additional CHF 300/450/600 per child aged up to 5 / 6–11 / at least 12. Article 15(2)(i) contains total-income and part-year annualisation gates. These are separate from article 19’s zero bands and fixed subtractions.

Impact: the printed positive bands can produce tax for a qualifying low-income resident if a reader follows the ordinary method without this screen. A generic reference to exclusions/deductions does not explain the material difference between the subsistence exemption and the basic tariff allowance.

Correction: add the complete article 15(2)(i)/SteV 8 screen before tariff selection, include category/child/time gates, and say it is an eligibility exemption, not a second amount to subtract from taxable income. Keep taxable-income and relevant gross/total-income tests distinct. Add a focused threshold control or explicit low-income illustration. Sources: [SteG](https://www.gesetze.li/konso/pdf/2010340000), [SteV](https://www.gesetze.li/konso/pdf/2010437000), both consolidated 1 July 2026, independently read.

### F2, P2: inherited CTA contradicts firm identity and review status

Locations: end blocks in li-company-formation.md, li-corporate-income-tax.md, li-income-tax.md, li-payroll-social.md, li-tax-overview.md and liechtenstein-vat.md.

These six blocks describe an OpenAccountants “network” and assert a live, always-current version with a professional behind it. The supplied firm rule says one company, never a network; the same country pack expressly has tier-2 sources, no named Liechtenstein review and incomplete coverage. No evidence in this review establishes the CTA’s implied country-specific professional/currentness promise.

Correction: use the neutral CTA already present in TP/XB, linking to current Guide and professional-review status. Retain the CTA marker. Do not change tier or professional review_status to suggest this AI review is professional approval. Source: supplied firm instructions; the pack’s own metadata, README and scope text; docs/skill-template.md platform-key definition.

### Workflow reconciliation, P3

README’s Bosnia primary-chat reference became stale when published OWNERS moved the primary chat to Montenegro during this review. Reconcile it and date the independent-review result after closure. Preserve the separate named local accountant gate. This is workflow text, not a tax-law defect.

## Primary material independently accessed and read

Read on 24 October 2026. For statutory PDFs I reused writer-provided `pdftotext -layout` extracts for navigation and passage comparison, explicitly disclosed here. I independently opened the cited official sources through the web reader; for MWSTG/PGR, where that reader failed, I independently retrieved the public official bytes directly and matched them to the local PDFs. Network DNS failed in the sandbox first; approved read-only network execution succeeded. Matching bytes prove identity, not correctness of every provision.

| Primary source | Version/access | Provisions or content actually inspected |
|---|---|---|
| [SteG](https://www.gesetze.li/konso/pdf/2010340000) | 1 July 2026; official web reader plus local extract | Articles 1–2, 5–12, 14–16, 18–19, 21–29, 44–47, 49, 51, 54, 57, 61–63a, 75, 94–95, 113–114, 124a, 127, 135; selected adjacent context only |
| [SteV](https://www.gesetze.li/konso/pdf/2010437000) | 1 July 2026; official web reader plus local extract | Articles 4, 6, 8, 18a–18c, 19, 31a–31b in full, 32–32a, 41–42a, 45, 47; selected adjacent context |
| [MWSTG](https://www.gesetze.li/konso/pdf/2009330000) | 1 January 2026; official direct retrieval, 434,519 bytes, SHA256 8ea497ccf56427cb13631b9f695f6ac770568f43524c7ebf41f7c97bbd92bcef; matches writer PDF | Articles 7–8, 10–14, 25–31, 35–38, 45–48, 53–54, 58–59, 76–77, 86. Complete exemptions/options/import chain not audited |
| [PGR](https://www.gesetze.li/konso/pdf/1926004000) | 1 September 2026; official direct retrieval, 4,735,428 bytes, SHA256 5851b543646ab11f235bd220478f60f06a90c6fa6c3795e7eb1af27ab46ebdcc; matches writer PDF | Articles 122, 180a, 261, 284, 390–391, 394, 552 §13, 1058a, 1064, 1122; selected adjacent context |
| [Act 2024/483](https://www.gesetze.li/chrono/pdf/2024483000) | Official web reader and local extract | Selected amended text and commencement II(1)–(2), independently checked the separate article-5 2026 start against general 2025 application |
| [2026 AHV-IV-FAK-ALV bulletin](https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf) | Effective 1 January 2026; official web reader and full local extract | Sections 1–17, concentrating on age/status, wage inclusion/exclusion, rates, ALV cap and 254-day example; no independent complete insurance-act review |
| [Wage-withholding bulletin](https://www.llv.li/servicekonto/steuerverwaltung/quellensteuer-lohnsteuer-unselbstaendige-taetigkeit-und-ersatzeinkuenfte-merkblatt.pdf) | February 2026; January 2026 annex; web reader | All substantive bulletin sections I–III and annex screening/footnotes. No treaty entitlement independently adjudicated |
| [GmbH fact sheet](https://www.llv.li/serviceportal2/amtsstellen/amt-fuer-justiz/handelsregister/merkblaetter/007_merkblatt_zur_gmbh.pdf) | July 2025; web reader | Sections 1–12, capital, governance, simplified formation, review and disclosure; compared with current PGR |
| [eMWST](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/e-mwst) | Current authority web content | Mandatory January 2025 channel, old lilog/authorisation replacement, representation and acquisition-tax registration instructions |
| [Registration/allocation](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/wer-ist-mwst-steuerpflichtig) | Current authority web content | Actual substantive section, foreign-enterprise Swiss/LI authority allocation, thresholds and acquisition screening |
| [Rates](https://www.llv.li/de/unternehmen/steuern-abgaben-versicherung/mehrwertsteuer/mwst-steuersaetze) | Current authority web content | Rate/date table and supply-period gate |
| [Swiss practice by analogy](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/publikationen-zur-mehrwertsteuerpraxis) | Current authority web content | Explicit analogy/local-deviations passage |
| [2025 VAT changes](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/aenderungen-ab-01012025) | Current authority web content | Substantive changes, including emissions, digital services/platforms and net-tax method; specialist methods remain referred |
| [Health contributions](https://www.llv.li/de/privatpersonen/gesundheit-vorsorge-und-pflege/krankenversicherung/praemien-beitraege) | Current authority web content | Distinct 2026 versus 2027 employer amounts, youth age group, part-time and age-change provisions |
| [Corporate authority summary](https://www.llv.li/de/landesverwaltung/steuerverwaltung/steuern-juristische-personen/ertragssteuer) | Current web content | Actual headline rate/minimum and links, not every linked document |
| [Provisional corporate leaflet](https://www.llv.li/servicekonto/steuerverwaltung/provisorischer-bezug-der-ertragssteuer-merkblatt.pdf) | March 2012, official web reader | Both pages. Historical date/calendar treatment in Guide is accurate; not established as a 2027 deadline source |

The general tax-authority/treaty/register URLs are navigation references, not proof of an exhaustive underlying-source review. I did not use them to certify treaties. No hash is invented for reader-only authority content. I did not re-run the writer’s 23-URL transport audit; its 403/200 classification is separate evidence from my content review. PDF retrieval and a navigation-only page are not treated as substantive legal verification.

## Independent 24-control results

I used a separate inline Python parser/evaluator, not the repository’s checker, recalculated every expected field, and manually compared formulas/bases/gates with narrative and inspected provisions. Floating-point tails were checked within 1e-7 absolute / 1e-9 relative tolerance; all printed currency amounts and the recurring TP percentage match. Existing controls are conditional arithmetic examples, not evidence of taxpayer eligibility.

| Guide/control | Independently recomputed material results | Result |
|---|---|---|
| Formation: GmbH contributions | 4,000 + 3,000 + 3,000 = 10,000; shortfall 0 | Pass |
| Formation: AG funding | 100,000 × 25% = 25,000; minimum screen 50,000; unpaid 50,000 | Pass |
| Corporate: bridge | 105,000 before equity; equity 20,000; pre-loss 85,000; losses 59,500; taxable 25,500; tax 3,187.50; closing loss 500 | Pass |
| Corporate: minimum | ordinary 1,250; result 1,800; increase 550 | Pass |
| Corporate: no new loss | raw equity 20,000; allowed 10,000; remaining profit 0 | Pass |
| Corporate: three-year average | (400,000 + 500,000 + 600,000) / 3 = 500,000; remaining limit 0 | Pass |
| XB: credit | credit 1,200; uncredited 400 | Pass |
| XB: board payment | tax 1,200; cash 8,800 | Pass |
| XB: exit | uplift 40,000; isolated tax 5,000 | Pass |
| Individual: wealth yield/ordinary | yield 20,000; income 100,000; state 3,256; municipality 4,884; combined 8,140 | Pass |
| Individual: joint | state 6,512; municipality 11,721.60; combined 18,233.60 | Pass |
| Individual: single parent | state 4,884; municipality 9,768; combined 14,652 | Pass |
| Individual: loss cap | limit/use 70,000; income after loss 30,000; unused 20,000 | Pass |
| Payroll: employee | AHV/IV/FAK 2,940; ALV 300; specified total 3,240 | Pass |
| Payroll: employer | AHV/IV/FAK/VK 11,077.50; capped ALV 630; total 11,707.50 | Pass |
| Payroll: part year | cap 254 × 350 = 88,900; each side 444.50; combined 889 | Pass |
| Payroll: withholding | 7,500 × 9% = 675 | Pass |
| TP: group goods | 1,100,000; excess 100,000 | Pass |
| TP: separate-size services | 140,000; excess 15,000 | Pass |
| TP: denominator | profit 8,000; revenue 108,000; profit/sales 7.407407407407407% | Pass |
| VAT: inclusive | net 10,000; output 810 | Pass |
| VAT: reduced/accommodation | 26 + 7.60 = 33.60 | Pass |
| VAT: acquisition/partial input | 81 output; 56.70 input; net 24.30 | Pass |
| VAT: food classification | 13 versus 40.50; difference 27.50 | Pass |

## Cross-file and applicability checks

- Payroll’s 2026 employee/employer totals, annual cap, per-employment/part-year distinction and institution example match the bulletin. Resident withholding, maximum whole-base schedule, field-8-less-field-6 base, authority instructions, training threshold and remittance versus reporting are distinguished. Health costs are separate.
- VAT uses Liechtenstein’s own statute numbering and actual authority/portal. Rates, restaurant separation, recipient/supplier/acquisition gates, input evidence, mixed use, annual reporting and instalments, corrections and sanctions were compared. CHF 5,005,000 annual reporting is not substituted for the separate CHF 5,024,000/108,000 net-tax-method gate.
- Individual tariff entries were checked row by row; state/municipality basis and 4% wealth yield are consistent with corporate references. The material missing subsistence screen is F1. Actual municipality rates and full deductions remain unverified case inputs.
- Corporate examples use modified equity, not paid capital; no-new-loss, ordinary loss ceiling, minimum versus additive tax, three-year balance gate, short-period distinction and 2026 commencement are preserved. Groups/exemptions/GloBE remain separately scoped.
- TP’s greater-than group/transaction thresholds, specified relationship gate, all-criteria PGR cross-reference, residual evidence, 60-day/language rule and denominator example match inspected text. No benchmark/CbCR safe harbour is inferred.
- XB keeps domestic and treaty tests separate, identifies specified source categories, uses the correct treaty-refund clock and nonbusiness credit gate/ceiling/claim period, and distinguishes exit valuation from deferral/security. Corresponding-adjustment finality is conditional, not a generic reopening entitlement.
- Formation’s currency minima, GmbH payment, AG per-share/overall minimum, simplified route and disclosure/review distinction match the inspected provisions. This remains a secondary topic.
- README maps seven domains to the eight Guides with all partial flags. Overview routes without its own tax formula. Six inherited CTA blocks conflict with this status (F2). Original platform attribution and review status are preserved; there is no tier-1 or local-professional sign-off.

## Limits and next gate

I did not establish every within-year amendment’s application to every transaction date, all personal deductions/valuations, actual municipal rates or 2027 calendars, specialist corporate exemptions/groups/PVS/GloBE, full social insurance statutes/benefit/plan terms, all VAT special transactions/ordinances, benchmarks/CbCR, any concrete treaty entitlement, complete filing-field workflows or production ingestion. The existing explicit partial/referral boundaries must stay. I did not re-run the writer’s 129 unit tests or full repository metadata audit; those are writer/CI evidence and must be rerun as appropriate after fixes.

Writer has received F1/F2 promptly and reports working-tree corrections, but no corrected exact checkpoint has yet been provided. This original-checkpoint review is complete; finding closure remains pending exact replacement source blobs and focused recheck. Neither source review nor publication is professional accountant approval.


## Corrected-checkpoint closure, 24 October 2026

**Closed for the documented independent source/editorial review scope at exact corrective checkpoint `ede184f9d5b0ba4fdd35e8178d49e30df377d95d`.** This closure supersedes the original-checkpoint “pending correction” decision above. F1 and F2 are corrected; the P3 workflow reconciliation is corrected. No correction regression or additional actionable finding was identified in the final country text/diff. This does not certify comprehensive coverage, a professional accountant review, publication, CI, filing readiness or a client-specific position.

I reviewed the final nine-file country scope against the original `d1faf74d0b9f0e07cf5a9374a231451e3cfd8f4c`, including the complete diff, final source text, descriptions, source/CTA/status changes and version headings. Final source identity was read from Git objects, not inferred from working-tree timestamps.

| Final file, relative to skills/international/liechtenstein/ | Final Git blob | Version | Controls |
|---|---|---:|---:|
| README.md | 7fc941d25bd531e3706ddf5ffcf988ce8e490c84 | 0.2 | 0 |
| li-company-formation.md | 7d6f387930eb334e4ffd5f3ecd57dc15c2748a0c | 0.2 | 2 |
| li-corporate-income-tax.md | c2cb0b168275ba43af4b318c8af82f66be93099a | 0.2 | 4 |
| li-cross-border.md | 99bd1caabcda1f4baa3b1582384aabc8e51aa276 | 0.3 | 3 |
| li-income-tax.md | f01ba16199825646d1362b5acfe91c1a0d8a8748 | 0.2 | 5 |
| li-payroll-social.md | a995419b98bcba5cb6d2c7521291a33f4be5d297 | 0.2 | 4 |
| li-tax-overview.md | 610495ca94efe39cf51eed7207c1e0fe8b292366 | 0.2 | 0 |
| li-transfer-pricing.md | f4cbc65e3e45b0e8c926971a9dddfe3a61589981 | 0.2 | 3 |
| liechtenstein-vat.md | bb604e41015f8a83aaeecac0294fa2d49cc0b02b | 2.2 | 4 |

F1 closure: re-read SteG 15(2)(i), article 19’s express reservation, SteV 8’s full category/child text and amendment notes 14–17 in the same current primary-source extracts independently accessed during the original review. The correction places the exemption before tariff selection, retains the unlimited-liability, total-income and part-year annualisation gates, distinguishes gross/total income from post-deduction taxable income and says the exemption is not another deduction. All four adult-category rows and three child-age rows match the inspected law. Their twelve-month arithmetic is correct. The stated amended adult-base first application in tax year 2025 matches notes 14–17. Changing-family/disputed-attribution cases remain separately scoped rather than decided by the illustration.

The new control independently recomputes CHF 2,100 × 12 = CHF 25,200 and CHF 25,200 − CHF 24,000 = CHF 1,200. Its wording assumes a full-year unlimited-liability single resident, no child addition and established total article-14 income including relevant deemed wealth yield; under those express assumptions, its exemption conclusion matches the inspected gate. It does not call the CHF 1,200 headroom a deduction or a tax saving.

I also reran the separate evaluator on **all 25 final controls: all expected fields pass** at the original independent tolerance. All **24 original calculation blocks are byte-identical** to the original reviewed checkpoint, so their original narrative/legal-assumption review remains applicable; the new exemption control is the only added block. This recomputation is independent of the repository checker. The overview and README correctly have no controls; README’s 25-control total matches the final files.

F2 closure: all six inherited CTA blocks now use the neutral current-Guide/professional-review-status wording already used by TP/XB. All eight final Guides have exactly one CTA marker and neutral CTA. The unsupported network/currentness/professional promise is removed. Each Guide keeps tier 2; existing platform professional `review_status: pending_review` fields are preserved. Version headings match frontmatter, including XB 0.3 and VAT 2.2. Review-status prose directs the reader to the exact-revision/scope record and expressly preserves named Liechtenstein accountant review. README retains all seven partial flags and the separate live-filing/professional gates. Montenegro/Bosnia workflow wording now matches the writer’s published assignment reconciliation.

The refreshed `country_source_sha256` maps in both retrieval/transport JSON records independently match all nine final Git-object byte streams. Transport timestamps remain historical evidence, not a fresh source-content/HTTP audit. This closure does not renew or extend the original source-access and substantive-law scope limits.

The linked repository copy `docs/research/2026-10-24-liechtenstein-pack-review.md` is to be populated by the writer from this final report before publication. It was not yet present at this source checkpoint, so its existence/content and the eventual published head are procedural publication checks, not facts certified here. Copying this report and adding research/status evidence can preserve this closure if all nine final country blobs above remain identical. Any subsequent country-source edit requires a focused review of that change; any tax-rule or example change requires appropriate legal/arithmetic recheck.

All limitations in the original review remain. Only `/private/tmp/oa-li-independent-review.md` was appended by this reviewer; no country/repository files, commits, remotes, returns, messages to clients or payments were changed by this reviewer.
