# Malta property, succession and residence audit

Read date: 4 November 2026. Read-only audit of public repository head `ab692cc2ef1c6306de9435b63448294d30fc4052`. No Guide, metadata, attribution, Git branch or PR changed. Ten assigned Guides read. This is an audit with findings and explicitly bounded checks, not an attestation or a statement that every possible issue is excluded.

## Confirmed findings requiring correction

### PR-01 [P1] Trading rental receipts are wrongly denied the 15% option

File `skills/malta/how-to-account-for-rental-income-in-malta.md`, lines23 and69. Line69: “A client presenting as a landlord but providing cleaning, linen, and guest turnover is running a trade ... no 15% option.” Line23 excludes short-stay operations constituting a trade. The categorical tax consequence is wrong. MTCA's specific Guidance Note on Article31D paragraph(b) expressly permits the15% rental-receipt option for both trading and passive rental income. Service provision also needs a facts-based classification, not an automatic trade conclusion from cleaning/linen alone. The other rental Guide line192 allows the option for shortlets, so these Guides directly conflict.

Primary authority: https://mtca.gov.mt/docs/default-source/documents/mtca-guidance-note-art31d.pdf paragraph(b), page2. Exact short quote: “chargeable to tax either under Article 4(1)(a) ... or Article 4(1)(e)”. Read4Nov2026. Also Income Tax Act art31D(1)-(2): https://legislation.mt/eli/cap/123/eng/pdf. Fix the exclusion and consequence, preserving the separate VAT/MTA and non-rent-service questions.

### PR-02 [P1] Historical restoration transfer rate presented as current

File `skills/malta/mt-property-transfer-tax-the-sale-immovable.md`, line37. The table states transfers in art31C(1) circumstances bear7% without a deed-period restriction. The current Income Tax Act art5A(5)(d) has10%; its7% proviso is restricted to specified2015 deeds. Exact decisive quote: “before the 1st January 2016”. The Guide lifted the stale MTCA FAQ Q16 wording into a2026 table. `mt-capital-gains.md` correctly gives10% for this limb. Other reliefs can apply, so this is not a recommendation to automatically charge10% without the complete gate.

Primary law: https://legislation.mt/eli/cap/123/eng/pdf art5A(5)(d), PDFpage54, fetched4Nov2026. Conflicting official guidance: https://mtca.gov.mt/personal-tax/property-taxes/faqs/new-property-tax-system---faq Q16. Treat law as controlling and scope/remove the obsolete row.

### PR-03 [P1] Ordinary garages/stores incorrectly classified automatically taxable18%

File `skills/malta/mt-rental-income.md`, line223: “Parking sites, garages, stores, installed equipment and machinery, safes | Taxable at18%”. Garages/stores are not an automatic taxable class. The VAT Act FifthSchedule PartTwo item1(1)(e)(iv) excepts these from the short-period exclusion; another limb can still tax a particular letting. Parking likewise carries statutory designated-parking conditions omitted here. Applying the table literally causes VAT to be charged on exempt supplies.

Primary source: https://legislation.mt/eli/cap/406/eng/pdf FifthSchedule PartTwo item1(1)(b)-(e), PDFpage88, fetched4Nov2026. Exact quote: “except for ... the letting of premises used or intended to be used as garages, stores or similar uses”. Repair by separating conditional parking, ordinary garages/stores, and the equipment/safes classes.

### PR-04 [P2] Wrong denominator in valuation tolerance

File `skills/malta/how-to-submit-capital-gain-taxes-in-malta.md`, line68: market value exceeding declared price by more than15% is said to trigger assessment. That is not equivalent to declared value being below85% of market. Example: declared100,000, market116,000: the Guide triggers, but100,000/116,000=86.2069%, above85%. The Guide's line102 is similarly too loose. `mt-capital-gains.md` line105 correctly gives the statutory relationship.

Primary law: https://legislation.mt/eli/cap/123/eng/pdf art5A(12)(d), and https://legislation.mt/eli/cap/364/eng/pdf arts10(2),52(1),(4), fetched4Nov2026. Short exact quote from Cap364 art52: “less than eighty-five per centum (85%) of the real value”. Rewrite the formula explicitly. This does not alter tax on an actual higher consideration or other assessment powers.

### PR-05 [P1 retrieval metadata] Capital-gains description says no gains tax on securities

File `skills/malta/mt-capital-gains.md`, line3: description promises “absence of CGT on securities”. Its own opening body, prohibition list and share example expressly establish the opposite. Retrieval reads descriptions before the full Guide, making this materially misleading even though the body is much better.

Primary law: https://legislation.mt/eli/cap/123/eng/pdf art5(1)(a)(ii), fetched4Nov2026. The positive listing includes securities. Replace the description with conditional taxation and reliefs; do not erase the substantive body.

## Scope limitations and lower-priority defects

- `mt-capital-gains.md` lines117-119 use “under” at16,000 and60,000, leaving exact boundary incomes unmapped. Current MTCA2026 table includes16,000 and60,000 in their respective lower bands. Source: https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026, fetched4Nov2026. At the boundaries the continuous formulas agree, so this is a mapping gap, not an identified euro miscalculation.
- `mt-capital-gains.md` line108 simplifies the duty property-company test without excluding current assets other than immovable property. The succession Guide gives the full exclusion. Use Cap364 art42(2)(a), https://legislation.mt/eli/cap/364/eng/pdf. The simplified test can misclassify a company with substantial current assets.
- The “verbatim”15% quotations in `mt-global-residence-programme.md` lines24,42 and `mt-residence-programmes-for-wealthy-families.md` lines61,76 splice a PDF margin heading into the statutory sentence: “(0.15) on every15% rate.” The rate is correct; the quote is not a proper substantive sentence. Replace with “rate of fifteen cents (0.15) on every euro”. The ResidenceProgramme PDF extraction itself injects its marginal heading after “every”; check visible page, not OCR alone. Sources S.L.123.148 and123.160 rule5(1).
- The capital-gain method lines50,54,96 equate the inherited acquisition base directly with the denunzja value. Other assigned Guides explicitly reserve the prescribed acquisition-value rules. This audit did not independently establish every adjustment under those subsidiary rules. Keep as an unresolved computation gate, not a confirmed wrong figure.
- No assumption that an uninspected permit-page figure is false: the nomad Guide deliberately withholds income threshold, immigration fees, permit duration and renewal conditions. Live https://nomad.residencymalta.gov.mt/faqs/ was inaccessible via browsing on4Nov2026. This remains missing coverage, not a numerical error. Tax-only publication can be retained with its narrower title/scope.
- MPRP brochure URL https://residencymalta.gov.mt/wp-content/uploads/2026/08/MPRP-Brochure-English.pdf failed the browser fetch because content length10,823,911 exceeded its limit. Therefore this pass does NOT independently accept the EUR500 card fee or brochure-only subletting/travel wording. The Guides label these brochure-only and reserve the property-use conditions. No evidence found here that these figures are wrong.
- LN158/2026 appears in the fetched S.L.364.06 amendment header; it amends company-share valuation rules11/12. The separately requested amendment PDF failed retrieval. The consolidated rules4,5,7 used for succession deadlines and rebate were readable and matched. Do not represent share valuation as comprehensively audited solely from nominal duty percentages.
- Budget2027 announcements are not enacted2026 rules. This pass did not certify all future changes or delegated notifications/portal practice. Dates described as2027 return dates are ordinary statutory dates, not an independently confirmed online-filing extension.

## Per-file disposition

| Guide | Scope checked | Disposition / remaining limits |
|---|---|---|
| how-to-account-for-rental-income-in-malta | Election, gross base, related-commercial test, ordinary deductions, TA24 deadline and interest guidance, rebate table, trade gate | PR-01 confirmed. Rebate amounts checked to official manual, not separate rebate instrument. Registration penalties explicitly held in Guide. |
| how-to-submit-capital-gain-taxes-in-malta | Rate-date gates, residence gate, inherited/donated bases, nonresident route, brokerage guidance, notarial handoff, valuation threshold | PR-04 confirmed; inherited acquisition-value subsidiary computation remains unresolved. Do not certify all temporary buyer-side reliefs from this short method. |
| mt-capital-gains | Asset taxonomy; ordinary share-gain example; property rate priority; own-home, inheritance, donation, listed/nonresident/non-dom/participation gates; provisional/final filing text | PR-05 confirmed plus boundary and stamp-duty-definition simplifications. No full treaty, trust, corporate reconstruction, project or prescribed-basis calculation signoff. |
| mt-inheritance-and-succession | Cap364 rates, exemptions/reliefs, familybusiness thresholds, valuation/assessment text; S.L.364.06 rules4/5/7; CivilCode reserved portions; examples | Core quoted figures and basic examples matched. No cross-border succession/foreign estate-law review or prescribed inherited acquisition-base certification. |
| mt-property-transfer-tax-the-sale-immovable | Current-vs-legacy seller rates, notarial steps, buyer provisional stage, stale scheme labels | PR-02 confirmed. Second-buyer2024 table is explicitly historical, not a falsely claimed2026 relief. General rate is deliberately withheld here and supplied elsewhere; omission isn't false law. |
| mt-rental-income | FWS/ordinary deductions and examples; related-commercial gate; VAT exemption exceptions; sources | PR-03 confirmed. Shortlet MTA scope, gross platform fees and treaty credit remain limited/unverified as labelled. The15% gross-base main rule matches authority. |
| mt-global-residence-programme | Both statutory programme tables, nationality/dependant limits, property, minimum/paymentyear, status-ending rules, examples | Core figures/gates matched S.L.123.148/123.160. Malformed quote is editorial. Interaction with other final taxes explicitly reserved. |
| mt-nomad-residence-permit | All four pages S.L.123.210: authorisedwork definition,10%, first12months, foreigntax proof, registration/return exceptions, regainedpermit, employer presence, antiabuse; example | Tax-rule core matched. Immigration conditions withheld/inaccessible; no full immigration eligibility signoff. |
| mt-permanent-residence-programme | Consolidated S.L.217.26 plus LN146/2025: fee, dependent exclusions, property/capital, payment/holdingperiods, ownervsrenter replacement, eligibility and cancellation | Current principal monetary figures and five-year conditions matched. Cardfee/brochure claims not reaccepted due fetchlimit. Immigration/citizenship/tax statuses appropriately distinguished. |
| mt-residence-programmes-for-wealthy-families | Cross-guide comparison, statutory programme figures, family tax example, non-dom holds, taxvsimmigration distinction | Core programme figures matched. MPRP “Nothing” cell should say “No special tax treatment” for clarity; following sentence already avoids claimingtaxfree status. Non-dom disputed trigger remains explicitly unresolved. |

## Specific residence-currentness acceptance

Fetched S.L.217.26 includes LN57/2024,310/2024 and146/2025. Current tables in both MPRPGuides match: mainfee60,000 split15,000/45,000;7,500 dependent administrationfee subject to spouse/minor/disability exclusions; contribution37,000 for both property routes; donation2,000; property375,000 or annualrent14,000; capital500,000 with150,000 financial OR650,000 with75,000financial. Timing1month/2months/8months and capital/property5years match. LN146/2025 reg16 expressly reaches post1Jan2025 pending applications. No obsolete south/Gozo price discount found in MPRP tables. Sources: https://legislation.mt/eli/sl/217.26/eng/pdf and https://legislation.mt/eli/ln/2025/146/eng/pdf, fetched4Nov2026.

For GRP/TRP, tables matched statutory property275,000/220,000, annualrent9,600/8,750, application6,000 or5,500 for qualifying owned southernMalta property,15% foreign remittances,15,000minimum and35% other chargeableincome. Family-membership restrictions matter and are included. Sources: https://legislation.mt/eli/sl/123.148/eng/pdf and https://legislation.mt/eli/sl/123.160/eng/pdf, fetched4Nov2026. The unusual minimum-tax due date preceding YA is actually in rule5(3); do NOT “correct” it to the following April merely because TA24 works that way.

## Arithmetic and executable checks

Ran `python3 scripts/check-examples.py` on all10 assigned files: checked10files,3oa-checkblocks,0failures,0missing. This is not evidence that all prose examples are machine-tested. Manual recomputation:

- Rental15%×12,000=1,800. Ordinaryroute12,000−3,000−2,400=6,600;36,600×25%−3,400=5,750;30,000×25%−3,400=4,100;increment1,650;saving150. Nonresident18,000×15%=2,700. Relatedoffice6,000−1,200=4,800;25%=1,200. These arithmetic results match stated assumptions.
- Rental platform example: stated rounded gross20,619 gives VAT1,348.9065,net19,270.0935,tax2,890.5140,roundingto2,891. Exact20,000netafter3% would imply gross20,618.5567, so input rounding should be explicit. Not a material discrepancy in roundedillustration.
- Capitalcases:320,000×8%=25,600;250,000×5%=12,500 or8%=20,000;150,000gain×12%=18,000 vs300,000×8%=24,000;400,000×10%=40,000;50,000×25%−3,400=9,100;7%×70,000=4,900;balance4,200;15,000−10,000loss=5,000;35%×200,000=70,000. Arithmetic matches, not independent verification of every entitlement assumption.
- Succession:400,000×5%=20,000each;300,000×2%=6,000each;propertyincrease3%=9,000each;eachcombined15,000. Latergain100,000×12%=12,000each,24,000total. The2032 illustration uses stated2026 rules hypothetically; it cannot guarantee2032 legislation.
- GRP:60,000×15%=9,000 raisedto15,000minimum;4,000×35%=1,400;total16,400.120,000×15%=18,000. Familycomparison80,000×15%=12,000 raisedto15,000;10,000×35%=3,500;total18,500.150,000×15%=22,500.90,000×35%−10,550=20,950. Ordinarymarriedtable independently matched current MTCA2026table (https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026).
- Nomad5,000×9=45,000;5,000×3=15,000;postperiod45,000×10%=4,500. Under stated assumptions the timeline matches S.L.123.210. MPRP example deliberately supplies no aggregate; no total mistakenly includesrecoverableassets.

## Attribution and reduction recommendation

Metadata observed, not a verified history of real human review: MichaelCutajar at lines10-11 in both methods and lines8-9 in succession and wealthyfamilies; MichaelSpiteriStaines at lines8-9 in GRP,nomad,MPRP. Capitalgains and propertytransfer have tier2 without reviewed_by; rental body explicitly says source-citeddraft. A reviewed_by string is NOT proof that the named person checked these rules or approved the presentbody. Parent should reconcile actual review records before retaining public attribution.

User is willing to reduce and invite other Maltese accountants. Sensible candidate consolidation is one rental authorityGuide plus a short method routed to it; one property/capital core plus a notarialmethod; and one residencecomparison routing to separately maintained programmeGuides. Retain research and history; leave genuinely unchecked specialist areas openly unclaimed. Do not remove MichaelSpiteriStaines's or MichaelCutajar's name silently or convert unknown authorship into attestation. This report changes none of them.
