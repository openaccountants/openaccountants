# Svalbard 2026: independent whole-pack review

Review date: 24 October 2026. Initial candidate: `f4d7a970dbe0c50d9f4d664043e616d5dc83ec27`. Comparison base: `77dc50c0f1ff06898c7ffef4888a6fb6ec518821`.

## Initial verdict

**FAIL for independent merge closure on this candidate.** The a-melding penalty regime needs correction, two ordinary scope statements need tightening, and available official evidence should replace or narrow avoidable coverage gaps. **All twelve candidate examples recompute correctly under their stated assumptions.** This is a substantive source review, not accountant sign-off, a filing opinion, or a declaration that the pack is complete.

The reviewer started without writer research context. I read AGENTS.md, docs/skill-template.md, docs/pack-readme-template.md and LICENSING.md, then all six candidate country skills and README. The writer's research receipts and local downloaded sources were not used as independent legal evidence. Later author progress messages and working-tree corrections do not change this initial verdict, which is tied to the candidate above. Exact-source closure must identify the corrected commit and rehash all seven country files.

## Must-fix findings

### F1. PR and SC: distinguish a-melding penalties from annual-return penalties

The repeated ordinary-information paragraph gives 0.5 court-fee units per day and a 50-unit cap. Those are the Tax Administration Act/regulation rules. In payroll and social-contribution guides whose operative reporting obligation is a-melding, omitting the separate a-melding regime leaves a materially misleading penalty summary.

The [A-information Act §1](https://lovdata.no/dokument/NL/lov/2012-06-22-43/#%C2%A71) expressly applies to Svalbard. Under [§10](https://lovdata.no/dokument/NL/lov/2012-06-22-43/#%C2%A710) and [A-information regulation §§4-1–4-2](https://lovdata.no/dokument/SF/forskrift/2014-06-24-857/#%C2%A74-2), the ordinary coercive fine is **0.1 court-fee unit per day per income recipient** whose required information is missing, starting on the decision's date, with the Act's **1,000-unit maximum**. The separate late-report infringement fee under Act §11 is capped at **15 units**; regulation §§4-3–4-4 normally uses **0.25 unit per day**, and prohibits that fee where a coercive fine has accrued for the same delay. Do not invent a 2026 NOK court-fee amount merely to express these rules.

Required fix: add the payroll-specific regime in PR and SC. Retain the 0.5/50 annual-return information rule only with its proper scope. The additional-tax percentages and 2026 late-payment interest figures in the candidate are otherwise supported by the cited statutes and authority table.

### F2. PR: state the nonresident pension exclusion explicitly

The candidate joins pensions and listed benefits before saying that a nonresident benefit recipient must meet the local-stay and active-work-at-entitlement conditions. That wording can be read as admitting an ordinary pension after a 30-day stay.

[Svalbard Tax Act §2-2](https://lovdata.no/dokument/NL/lov/1996-11-29-68/#%C2%A72-2) imports only the replacement benefits in [Income Tax Act §5-10(c)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_5#%C2%A75-10), not ordinary pension/annuity income. The current [Skatte-ABC S-23-3.2 and S-23-7.15](https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-S-23) expressly confirms that temporary nonresidents' pensions are outside Svalbard liability, even after 30 days. The authority's [wage guidance](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/skatt-lonn/) also conditions pension inclusion on residence.

Required fix: separate ordinary resident pension liability from the nonresident replacement-benefit rule, including the requirement that the qualifying benefit be received during the local stay. The newcomer limitation also requires the §2-2 scope to be tested separately.

### F3. IT-IND: qualify the own-home letting exemption

The statement that ordinary long letting is exempt where the owner uses half by rental value needs the ordinary statutory exclusions beside it. [Income Tax Act §7-2(1)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_7#%C2%A77-2) defines the relevant letting as **at least 30 continuous days**. Subsection (3) excludes multi-unit properties, letting cabins and letting that is a business. Its NOK 20,000 receipts condition is correctly distinguished from the separate Svalbard ordinary-income allowance in the candidate.

Required fix: state the duration and subsection (3) exclusions. This is a scope correction, not a change to the examples or the rates.

### F4. TP: qualify the response clock for an early documentation request

The candidate twice states a 45-day response period from the authority request without its earliest-start qualification. [Administration regulation §8-11-15(1)](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/KAPITTEL_7#%C2%A78-11-15) says that this period cannot begin before expiry of the tax-return filing deadline. Add that qualification so an early request does not produce an incorrectly accelerated deadline. The ordinary 45-day figure itself is correct.

## Avoidable gaps and exact remaining limits

### G1. SC: first-krone salary contributions are established; annual assessed business interaction remains narrower

The candidate correctly withholds contributions from the first krone but treats final low-income Svalbard assessment too broadly as unresolved. The enacted [Svalbard regulation §5](https://lovdata.no/dokument/SF/forskrift/1997-12-15-1305/#%C2%A75) now expressly references §3-1 as well as chapter 5 and extends the youth refund. The Ministry's [20 June 2025 consultation, §3.5, pp.13–14](https://www.regjeringen.no/contentassets/337ef9a31fcc495bb63bb37166c52a1d/horingsnotat-fribelop-for-ungdom-pa-svalbard.pdf) explains that adding the §3-1 reference clarifies first-krone contribution liability in the withholding scheme. The authority's wage page describes withholding as the final settlement and confirms the special youth refund.

Correct proposition: covered salary/pension contributions within the gross withholding scheme are calculated from the first krone, subject to membership/class and the enacted youth refund. The general NOK 99,650/25% provision in [National Insurance Act §23-3](https://lovdata.no/dokument/NL/lov/1997-02-28-19/KAPITTEL_8#%C2%A723-3) is not a mainland tax-card exemption that can be imported into Svalbard payroll.

I did **not** locate equally explicit official treatment of that lower threshold/phase-in for separately assessed Svalbard sole-trader income, or its combination with gross-withheld income. The paragraph extending the middle rate to Svalbard business income and regulation §5 do not by themselves resolve that mixed-base administration beyond reasonable doubt. Preserve a **narrow SC partial entry for low-income annual assessed sole-trader/mixed-income cases** unless that treatment is established. Do not leave ordinary gross wage treatment unresolved.

### G2. XB: ordinary resident foreign-capital/wealth credits have available statutory mechanics

[Svalbard Tax Act §3-2](https://lovdata.no/dokument/NL/lov/1996-11-29-68/#%C2%A73-2) imports the Income Tax Act and does not exclude §§16-20–16-29. The candidate's blanket unresolved treatment of ordinary foreign capital/wealth credit mechanics can therefore be narrowed substantially.

For a fully liable resident, [Income Tax Act §§16-20–16-21](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_16#%C2%A716-20) permit a claim for final assessed, paid comparable foreign income/wealth tax on the same foreign-source income/wealth included in the Svalbard assessment. Source exclusions come first. Income and wealth credits have separate ceilings; income credit is also divided into the statutory categories. No credit is available merely because a foreign levy exists, on excluded income, or for the tax on §2-38(6)'s 3% dividend inclusion. Foreign tax and the attributable domestic tax both limit relief.

Section 16-22 permits unused income-tax credits to carry forward **five years**, subject to category capacity and ordering. Its **one-year carryback** requires the stated evidence that no corresponding foreign-source taxable income will arise in the next five years. Section 16-25 requires a claim by the return deadline, or, where it could not be substantiated earlier, within **six months after final foreign assessment**, with the **ten-year outer limit**. Do not describe wealth credits as automatically enjoying the income-credit carryforward.

[FSFIN §§16-29-1–9](https://lovdata.no/dokument/SF/forskrift/1999-11-19-1158/KAPITTEL_16#%C2%A716-29-1) supplies source/cost allocation, timing, foreign-exchange, payment/finality evidence and return allocation mechanics. Adapt those rules to the actual Svalbard ordinary-income assessment, including its separate salary/business buckets and the NOK 20,000 allowance. Do not manufacture a gross-income shortcut or apply a mainland uplift. A simple fully liable resident capital-income example can demonstrate the capped credit without claiming every mixed-base case is solved.

Required coverage improvement: include these established ordinary rules and evidence requirements. Keep any remaining special Svalbard allocation question specific. Treaty exclusion alone does not defeat domestic statutory credits.

### G3. PR: imported 2026 schedules and payment rounding can be checked

The candidate correctly flags its unverified communications and travel/car/snowmobile schedules, rather than inventing exempt figures. This is an avoidable research gap: [2026 Svalbard benefits regulation §§1–2](https://lovdata.no/dokument/SF/forskrift/2025-12-15-2559) expressly imports the mainland 2026 rules for those items. The author subsequently reported researching the 2026 rates regulation, FSFIN communications provisions and Payment regulation §10-4-4. Those subsequent additions are **not covered by this initial candidate verdict**; they need independent retrieval and checking during exact-source closure.

### G4. IT-IND: final 2026 Svalbard property assessment directions remain a genuine dated gap

The primary statute excludes the mainland automatic housing values. Current official sources confirm the special Svalbard treatment, but I did not find enacted **final 2026 discretionary property assessment directions** during this review. Search results surfaced the final 2025 directions and 2026 advance-tax guidance. Advance estimates and a prior-year discretionary direction are not proof of the final 2026 value.

Keep the partial entry narrowly tied to that final assessment question. Do not insert a mainland housing default or treat the lack of a completed assessment value for a particular taxpayer as a universal missing tax rule. Existing accepted values and relevant statutory caps still need to be considered.

### G5. XB: cross-border exit adaptation remains distinct from ordinary cessation

The candidate accurately identifies the mainland-to-Svalbard extension of §10-70 through §2-35(2)(b), the NOK 3m departure allowance, distinct NOK 100,000 transfer threshold, 12-year deferral choices and 70% distribution acceleration, subject to statutory conditions. The example does not compute exit tax and must not be represented as doing so.

For a departure **from Svalbard**, the detailed adaptations of [§9-14](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_9#%C2%A79-14), [§10-71](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_10#%C2%A710-71), territorial residence references and their payment exceptions remain unresolved here. Preserve that narrow cross-border limit.

Ordinary complete liquidation/cessation has more verified content available than the broad gap suggests. [§14-48(1)–(3)](https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_14#%C2%A714-48) settles specified negative balances and gain/loss accounts; subsections (4)–(5) have EEA/reorganisation exceptions. §§14-44–14-47 govern disposals/residual balances, while §14-7 governs qualifying final-loss carryback. Include ordinary final settlement without declaring cross-border adaptation solved.

## Rules checked and accepted, subject to findings above

- Resident/nonresident individual and company scope: retrospective 12 months; 30 continuous days, not more than 30; separate property rule; ten-year/five-year newcomer restriction and discretionary 12 G override; rolling **more than 183** outside days; whole/part-day counting and specific medical decision.
- Gross salary and separately assessed sole-trader income share one 12 G tax band. Last fixed 2026 G is NOK 136,549, so 12 G is NOK 1,638,588. The ordinary-income 16%/NOK 20,000 computation does not reduce gross salary or company profit. No mainland share uplift/shielding is imported.
- Personal wealth allowances/rates, listed/unlisted share valuation timing and debt-reduction rules; spouses are separate Svalbard taxpayers. The upper-band wealth example correctly starts the 1.1% rate above total wealth NOK 21.5m, not above allowance plus NOK 21.5m.
- Corporate 16%/22% formula uses the larger of NOK 15m and the payroll/physical-capital threshold. Ordinary deductions, balance depreciation rates, Svalbard building override, loss carryforward and qualified cessation carryback are supported. Interest-limitation figures and ten-year carryforward are correct; actual §6-41 exceptions, including subsection (9), still must be tested in a case computation.
- Membership is separate from tax residence and the 30-day rule. NAV supports retained membership, Norwegian-employer entry, employment-plus-one-month continuation and Nordic coordination. 7.6% ordinary wage/Svalbard business class, 5.1% low-rate classes and statutory zero employer cases are supported.
- Standard daily board/lodging, monthly housing/car and youth refund figures match enacted 2026 regulations. Fifth-of-next-month reporting and first-working-day remittance are separate obligations. Individual/company advance and residual payment figures match the Payment Act.
- Substantive arm's-length adjustment is not restricted by the 50% compliance definition. Strict NOK 10m/25m reporting exemption limits, small-group 250/400m/350m test, information-exchange exception, 45-day documentation response, ten-year retention and cited CbC headline figures are correct. The statutory documentation response cannot start before expiry of the return deadline under regulation §8-11-15(1); preserve that qualification when describing a request made early.
- The stated 20% foreign-shareholder dividend withholding is correct within its defined scope; mainland recipients and qualifying corporate exemptions require separate tests. Mainland exemption requires the item actually to be taxed to Svalbard. Norway's income-tax treaties do not extend to Svalbard.

## Independent recomputation of the twelve candidate examples

Each row below was checked against the underlying legal base/rate, not merely against the executable block. Stated valid costs, carried losses, membership, age, valuations and supported prices remain assumptions requiring case evidence.

| Candidate example | Independent computation | Result |
|---|---|---|
| IT-IND salary/business | 700,000 − 200,000 − 100,000 = 400,000 business; plus 1,200,000 salary = 1,600,000, below 1,638,588; ×8% | **128,000; pass** |
| IT-IND capital/wealth | 120,000 + 80,000 − 30,000 − 20,000 = 150,000; ×16% =24,000. Wealth: (21,500,000−1,900,000)×1% +1,500,000×1.1%=212,500 | **236,500 combined; pass** |
| IT-CORP ordinary | 12m−3m−0.4m−0.6m=8m; below 15m floor; ×16% | **1,280,000; pass** |
| IT-CORP higher slice | 10×2m+20%×10m=22m threshold; 30m−22m=8m higher slice; 22m×16%+8m×22% | **5,280,000; pass** |
| SC adult | 600,000×7.6%; zero employer rate on stated local employer/work facts | **45,600 / 0; pass** |
| SC over 69 | 400,000×5.1%=20,400; 400,000×7.6%=30,400 | **10,000 difference; pass** |
| PR ordinary cash | 50,000×8%=4,000; ×7.6%=3,800; cash less both | **42,200; pass** |
| PR car/band crossing | Gross62,850; low slice38,588×8%=3,087.04; high24,262×22%=5,337.64; insurance62,850×7.6%=4,776.60 | **Tax8,424.68; net46,798.72; pass before declared rounding** |
| TP service adjustment | 1.2m−1m=0.2m; 4m+0.2m=4.2m; ×16% | **672,000 tax /32,000 increase; pass** |
| TP higher-band correction | Substance=10×0.5m+20%×5m=6m, so15m floor; corrected17m:15m×16%+2m×22%=2.84m; less14m×16%=2.24m | **600,000 increase; pass** |
| XB exactly30 days | Stated countable30-day stay qualifies under statute; 90,000×8% | **7,200 tax /82,800 remainder; pass** |
| XB foreign dividend | Stated individual abroad/no exemption:500,000×20%; gross less withheld tax | **100,000 withholding /400,000 net; pass** |

## Repository, territory and trust checks

All three original country paths remain. Their platform-written `authored_by: Ryan Duguid`, `review_status: pending_review`, `trust_label: Accountant-authored` and literal `license` values match the base. The existing Ryan contribution line remains. Each original CTA suffix is byte-identical to base. New files do not add those platform keys or a manually authored CTA. All six skills use integer tax year 2026, tier 2, dated sources, the deep-tax section order and exactly two examples; no new `reviewed_by`/`reviewed_on` or professional approval claim was added. Original version/headings advance consistently.

The preserved platform license string is legacy platform metadata, not authority to override LICENSING.md's mixed-licence mapping. No generated packages/index files were edited by this review.

The boundary is **Svalbard only**, verified through Svalbard Tax Act §1-1 and Svalbard Act 1925 §1. The shared SJ identifier does not confer Jan Mayen coverage. The [VAT Act §1-2(2)](https://lovdata.no/dokument/NL/lov/2009-06-19-58/#%C2%A71-2) supports the local VAT absence. Mainland transactions remain separate.

Niche exclusions such as foreign research-group settlements, Barentsburg, specialist shipping/extractive/financial activity, large-group CbC territorial implementation, minimum tax and complex reorganisations do not themselves make ordinary coverage partial. The identified ordinary property, assessed low-income and exit-adaptation gaps do. Lack of professional sign-off is a separate trust limit, not an ordinary coverage gap and not a reason to invent a review attribution.

## Candidate country-file SHA256

Hashes are of committed candidate bytes, not subsequent working-tree revisions.

| File under skills/international/svalbard/ | SHA256 |
|---|---|
| README.md | `9f0be8f940ced7466713e55ddb2faf211051009e7bb34a33badbc86072065a90` |
| sj-svalbard-company-income-tax.md | `c520a1bbde766c80485c2b5714c09485d968b4c84f48f50ef6c61e942046a964` |
| sj-svalbard-income-tax.md | `d6d60aa9b311c565ad76aab07e987465e8fabf54cc4545435f77063d18e38dd8` |
| sj-svalbard-payroll-tax.md | `638d6091e24cdcf15991902af6d945538dc2dfb208c1cade467b7b757f746a03` |
| sj-svalbard-social-contributions.md | `83bcfac59e0f0c50fc4c31cdbfa4888aa7b32ad69ac5203456d7deccaac5fe0b` |
| sj-svalbard-tax-residence.md | `4e842f9b2ae6f51db7a4b34d435fdd42f1b65045e6c97593f078ea93de0e6f54` |
| sj-svalbard-transfer-pricing.md | `35a12a17ee3e26f99d87008b43160a388ec0ceacfb338effeb4013e3b9cea007` |

## Independent primary-source retrieval ledger

All sources below were retrieved independently in this review on **24 October 2026**. Hashes are SHA256 of original HTTP response-body bytes from ordinary HTTPS with a normal `Mozilla/5.0` user agent, unless explicitly labelled otherwise. HTML was stripped for reading; the hash remains of the unmodified fetched bytes. No writer download was used. Dynamic navigation/content means a later fetch need not have the same body hash. Read scope is stated precisely rather than claiming every chapter of a large statute was reviewed.

The web reader returned 405 for Lovdata; ordinary HTTPS succeeded without a challenge. Sandboxed DNS failed initially; the authorised network-enabled read succeeded. The Ministry PDF returned403 to ordinary HTTPS; a normal in-app browser was opened under template rule3 but provided no readable PDF content. The web PDF reader then supplied readable primary text. No CAPTCHA, human check, security interstitial, login or access-control bypass was attempted.

| Independently retrieved official URL | SHA256 | Read scope |
|---|---|---|
| https://lovdata.no/dokument/NL/lov/1996-11-29-68 | `9a0f0435d5bee5f12a011938e28ff8b5f352134cbf9f5c59a6a91bd3a847cf6f` | Entire operative Act, especially §§1–5 and transitional exclusions |
| https://lovdata.no/dokument/NL/lov/1925-07-17-11 | `04da35544186ab2b7e58bdae8f7cd4e7f736840673c442bb92a6fa413219a0cc` | §1 territorial definition |
| https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780 | `2743970b3bb96a956739282fcc44f1bc17f0315a11a2832780707d38a37546a4` | Entire2026 Svalbard decision §§1–7 |
| https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 | `43a2689294a3f4cc0b149ac824e677adbe3400fcf51cb447dc47e46ac3cfa99c` | Ch.2 wealth; current2026 consolidated decision and dates |
| https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 | `a8e5f37730e7363053685e4fa4b70634dad44fdaea64246c0056b6261fe7e4f0` | §§3,6–8, zero employer conditions and personal classes |
| https://lovdata.no/dokument/SF/forskrift/1997-12-15-1305 | `90458f5066a02aaaf65b8e47ea2be27962d56ab72b5d1df7b6606712339e791f` | §§3–6,8, including current2026 §5 amendment |
| https://lovdata.no/dokument/SF/forskrift/2025-12-15-2559 | `8ca80dcadbb1c6156898737c06ea980260abd82a136116adae654e6837a18ff9` | Entire2026 benefits regulation §§1–2 |
| https://www.nav.no/grunnbelopet | `e0f3bb56f323f712feef35d9df555a20724ac2d90d693f5136f7690430ea3a9b` | Current2026 G, average-G distinction, update date |
| https://www.nav.no/svalbard | `33466286eb193701fc56690da090a8b492079be6257056e898360774a482b52d` | Entire membership/coordination guidance,8 June2026 |
| https://lovdata.no/dokument/NL/lov/1997-02-28-19/KAPITTEL_1 | `6030318bad6be5dfbe9a5f5b36c1cb3800a9ba2883c1b857f516e12174ede298` | §2-3 membership |
| https://lovdata.no/dokument/NL/lov/1997-02-28-19/KAPITTEL_8 | `ce65357f6686e4d51957a8cd0cde883870b927ac041a162225b5eae3ae80bd68` | Entire §23-3, including low-income provision and Svalbard extension |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_2 | `297f74d88f3556ed86dcebca38180c21b40ee25db8a667bb6060cd5d7aa67769` | §§2-1,2-35,2-36,2-38 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_4 | `64afc8abdbbabb1c5cc77353200bfc0c36112c1ca5fc524ab72a065662089faf` | §§4-1,4-10,4-12,4-13,4-15,4-19,4-31 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_5 | `902965d7d3b082f536bf84c3274bdc964c84a5d7895cd6bcc1fdbd7228df25ab` | §§5-1,5-3,5-10,5-12,5-30 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_6 | `882f8db26d4bcd07c5d59f71defc0ebf709185b7a721c5c585decd3ed81209f8` | §§6-1–3,6-40,entire6-41,6-91 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_7 | `a411e85ee91f6c758863b1e3ed6ca2b657e7de75581cf1033e2c48d1373714fe` | §§7-1–2 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_9 | `ecf0a3c9213547da37775c8606ff669587b72611da7ba656617099c4ef4bed8d` | §§9-2–4,entire9-14 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_10 | `f2279bee3d17b174007b660c7258b8fe7ecbac382923bea5c1e277e0d16a81f0` | §§10-13,entire10-70,10-71 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_12 | `ef9cd88b71522a0b249c2faee19d6d185d043f883e98e0aec368a927cf903aa8` | §§12-2,12-12 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_13 | `6664d49d59c843b433d8c0fe1f9789e410f7766121af21582991e65cb44fe734` | Entire §13-1 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_14 | `043bb97a50c7a8c10464eae5b59fa5a6f3a54c4f26855391e48201f13f215c25` | §§14-2–3,14-6–7,14-40–48 |
| https://lovdata.no/dokument/NL/lov/1999-03-26-14/KAPITTEL_16 | `2c673d61f45614cd23d9e8c917bd3f1e03dc134d043e8654b469e2900a2218c6` | Entire §§16-20–29 |
| https://lovdata.no/dokument/SF/forskrift/1999-11-19-1158/KAPITTEL_16 | `13aea50186c291250bebfc7cd088e46f26f3f8ad42640d1b2aa24e5f296a434c` | Entire §§16-29-1–9 |
| https://lovdata.no/dokument/NL/lov/2016-05-27-14 | `c460a9e45b6196a203c85b1d7b7d1d837f95faab2cc96bf94dc9984dd0483b65` | §§8-2,8-11–12,14-1,14-3–6; §8-8 reporting relationship checked with Svalbard Act and handbook |
| https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/KAPITTEL_7 | `2f302336aea13089677573b7d1cfacc4e3379fed60ab2bcb97ab97d5398d70f0` | §§8-2-3,8-2-5,8-8-3,8-11-1–16,8-12-7 |
| https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/KAPITTEL_13 | `b9884b55a8acb602d17e0cad227ce5077385080e49662bfe33dd4db2be485dfc` | §14-1-1 |
| https://lovdata.no/dokument/NL/lov/2005-06-17-67 | `7eb689605b3dc5aebd1097a27530c58ee2276070d8aa66961e58fa8e886ad56c` | §§10-2,10-10–11,10-13,10-20–21,10-53,11-1,11-6 |
| https://www.skatteetaten.no/satser/forsinkelsesrenter/ | `c7e9a2422122ce59ae2e4f17f1d6952b338fbf10a14dd4b4a09c9495933fcd9d` |2026 half-year interest table |
| https://oppslag.rettskilder.skatteetaten.no/rettskilder2/type/handboker/skatte-abc/gjeldende/skatteabc-S-23 | `5df124347ea4a76707bbee7118c5e37ff31c45580c6874707cab909366a7b96d` | S-23-1–7.12,7.15–11; relevant sections read in bounded extracts; stale labels/numbering checked against law |
| https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/hvem-er-skattemessig-bosatt-pa-svalbard/ | `3e97352e5df16a0703dd7b8667cdac3bfda346c7d98d399fb81ebc55fcf0bc94` | Entire substantive residence/arrival/departure guidance and examples |
| https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/naring-pa-svalbard/ | `c860c8d79469c19c25bcc8aadfe9d61ce941d370ddd75ab96bc90f6ed1e21669` | Entire substantive business/allocation/return guidance |
| https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/skatt-lonn/ | `114f8a5e0d6e6f13e1c5681e2e3572012da28cba68e90401aa1e9055d7c6c75c` | Entire substantive wage, pension, youth, employer and reporting guidance |
| https://lovdata.no/dokument/NL/lov/2009-06-19-58 | `c7f80ed7105a70cccc153b135772ea2a19072b7677d2742e1219509497d7efa1` | §1-2 territorial VAT exclusion |
| https://lovdata.no/dokument/NL/lov/2012-06-22-43 | `1438a00e560d7d377e3d85cb43dc0eec4a635c4713b7ac25eab63f092f7d99cb` | §§1,10–11 |
| https://lovdata.no/dokument/SF/forskrift/2014-06-24-857 | `8cf2f61aae084056df74ea669f06b0932fc882e1af4a00c5f7c635b69b7956fe` | §§2-1,4-1–4-4 |
| https://www.regjeringen.no/contentassets/337ef9a31fcc495bb63bb37166c52a1d/horingsnotat-fribelop-for-ungdom-pa-svalbard.pdf | `8d9da566acb93971a0a9cb888a533ef64e6da546c5c05b9ebb03d17b29cece4a` | **Web-reader response JSON hash, not PDF-byte hash**; §§2.1,3.3–3.5,especially pp.13–14; underlying PDF403/browser unreadable |

Search-only leads concerning 2026 property advance values and source discovery are not represented as final assessment evidence. No country content was changed, no external message sent and no publication/push performed by this review. The only repository write is this receipt.

## Exact-source closure

Closure date: **24 October 2026**. Final reviewed country source commit: **`7ff2d2b2be80b24cf7a105b31de5c4aaaa8effc8`**. I reviewed the consolidated corrections in `b6c839d960d9bcc1a855f3852aa66a7ade3407f6`, the communications/pension wording correction in `9771cc9fef731a647140b57374c79c29961f0a33`, and the final isolated XB sentence change in `7ff2d2b2be80b24cf7a105b31de5c4aaaa8effc8`. The full initial country text plus all country diffs, the full corrected PR/XB text and all final file bytes were checked. All seven working-tree country files matched the final committed bytes when hashed.

**PASS: independent legal-source review of these exact seven files as a source-cited, explicitly partial tier-2 draft. No must-fix finding remains open in the stated covered scope.** This does **not** pass the pack as complete: the README still has genuine IT-IND, SC and XB partial entries, so issue #424 must remain open. Professional accountant review remains outstanding. A later evidence-only commit can retain this closure only if the seven country-file hashes below remain identical.

### Finding closure

| Item | Exact-source result |
|---|---|
| F1 a-melding sanctions | Closed. PR and SC now state the separate 0.1-unit/recipient/day coercive fine, 1,000-unit cap, separate 0.25-unit/day late fee and 15-unit cap, same-delay prohibition and notice/special-case conditions. Ordinary tax-return sanctions are separately scoped. |
| F2 pension/nonresident benefits | Closed. PR expressly excludes temporary nonresident pensions and distinguishes §5-10(c) replacement benefits and their entitlement/presence conditions. During closure, broad “maintenance payments” was replaced with contractual life-support payments (føderåd) and qualifying annuities. |
| F3 rental exemption | Closed. IT-IND states at least 30 continuous days and §7-2(3)'s multi-unit/letting-cabin/business exclusions. |
| F4 TP documentation clock | Closed. Table and filing prose state the earliest start at expiry of the return filing deadline; the separate 60–90-day supplementary comparability-analysis request also matches regulation §8-11-15(2). |
| G1 first-krone contributions | Closed for gross salary/pension withholding; SC's partial entry is now confined to low-income separately assessed sole-trader and mixed-income cases. No unverified annual business exemption is asserted. |
| G2 resident foreign credit | Closed for the ordinary capital/wealth rules stated. Included taxable bases, same-taxpayer final paid foreign tax, distinct income/wealth ceilings, categories, cost/interest allocation, current/prior credit ordering, five-year carryforward, conditional one-year carryback, claim deadlines and evidence/change duties match the statutes/regulation. The new example uses established net attributed bases after costs/allowance. |
| G3 imported payroll schedules and rounding | Closed. Newly cited primary provisions independently retrieved/read, with hashes below. Amounts and conditions match. The final text includes the work-related-need/private-availability condition in FSFIN §5-12-20. Raw payroll example arithmetic is expressly separated from downward whole-krone tax/contribution claim rounding. |
| G4 property directions | Remains a genuine, narrow IT-IND partial entry. The new advance-assessment paragraph accurately identifies nominal 2024-to-2026 continuation and the stated 30% documented-market-value cap as **advance** treatment. It does not promote this into final 2026 assessment directions or a mainland automatic housing value. |
| G5 cessation/exit | Ordinary disposals, tax balances, gain/loss accounts, sub-NOK 30,000 settlement and complete-liquidation rules are now covered accurately. The genuine XB partial entry is confined to territorial adaptation/computation/payment for cross-border unrealised-asset gains and company emigration. It does not conceal ordinary liquidation/final-loss rules. |

One stale reference to a foreign-dividend worked example remained after that example was replaced. The final isolated commit removes it and gives a standalone recipient-status instruction. No new tax proposition or arithmetic changed in that final correction.

### Final twelve examples: independent legal and numerical check

I rechecked the eleven unchanged examples against the same legal bases/rates and independently recomputed the new foreign-credit example under §§16-20–16-21. Taxable cost/loss/valuation/price/membership inputs remain explicit case assumptions, not proof supplied by the arithmetic. The executable check was then run with the six explicit skill paths: **6 files, 12 oa-check blocks, 0 failures, 0 missing**. That automated result corroborates, rather than replaces, the legal/base review.

| Final example | Independently recomputed result | Verdict |
|---|---|---|
| IT-IND salary and sole trader | Business 400,000; shared income 1,600,000; tax 128,000 | Pass |
| IT-IND capital and upper wealth band | Capital tax 24,000; wealth tax 212,500; total 236,500 | Pass |
| IT-CORP ordinary profit/loss | Taxable profit 8,000,000; tax 1,280,000 | Pass |
| IT-CORP higher slice | Threshold 22,000,000; high slice 8,000,000; tax 5,280,000 | Pass |
| SC ordinary adult | Employee 45,600; employer 0 on the stated facts | Pass |
| SC older member | Low-rate contribution 20,400; comparison difference 10,000 | Pass |
| PR ordinary cash | Tax 4,000; contribution 3,800; net cash 42,200 | Pass |
| PR car/band crossing | Raw tax 8,424.68; contribution 4,776.60; net cash 46,798.72 before the clearly identified claim-rounding stage | Pass |
| TP service correction | Adjustment 200,000; corrected tax 672,000; increase 32,000 | Pass |
| TP corporate band crossing | Corrected profit 17,000,000; threshold 15,000,000; tax 2,840,000; increase 600,000 | Pass |
| XB exactly 30 days | Tax 7,200; after-income-tax amount 82,800 | Pass |
| XB capital-income credit | 200,000×16%=32,000 before credit; 32,000×50,000/200,000=8,000 ceiling; min(10,000,8,000)=8,000 credit; 24,000 remaining Svalbard tax; 2,000 enters the statutory unused-credit test | Pass |

The final metadata/trust checks remain passed: all six tax years are 2026, all tiers are 2, no professional-review keys were added, the three original platform metadata blocks and Ryan contribution lines remain intact, and their platform CTA suffixes still match the base byte-for-byte. The final territory remains Svalbard and excludes Jan Mayen. Niche exclusions and the professional-review limit remain separate from the three ordinary partial domains.

### Final country-file SHA256 manifest

These hashes identify the **country content**, independently of later changes to review receipts, author evidence or generated assets.

| File under skills/international/svalbard/ | SHA256 at 7ff2d2b2be80b24cf7a105b31de5c4aaaa8effc8 |
|---|---|
| README.md | `4829c8b79636dca5e27cb06779a5fed8fe7e1afa15ebf0f6b01fd670e9835ff0` |
| sj-svalbard-company-income-tax.md | `3dde986717a5cde36f68be7bd6aad40a823b598f86dbfc8eccdbd541996bf27d` |
| sj-svalbard-income-tax.md | `ba393f34e4ec3ebcf945f77e6332d6977c7d30ca31708ecd9eb7be7867b36ef5` |
| sj-svalbard-payroll-tax.md | `184c3e06f3c4cef010cd2013b6d195dca3fcf2d45780116792d1678f54fbd9fe` |
| sj-svalbard-social-contributions.md | `1f5558c5b413594b222910db8414cc72aa3e42b91940242a9b5ac5dae7c4787e` |
| sj-svalbard-tax-residence.md | `1d64825274c647daed51cef5b51f74ff1812670081eea39eccabc0445fcf5c14` |
| sj-svalbard-transfer-pricing.md | `30d6fda025a1dd66360eb7de12b93b9d93d2182d70e27abc8c453c2365e28fd7` |

### Additional independently retrieved primary sources for closure

All retrieved on **24 October 2026**, with ordinary HTTPS and the same normal user agent. Hashes are original response-body bytes. Previously retrieved core statutes, Svalbard benefit regulation and a-melding law/regulation were reread against the corrections and are recorded in the initial ledger; the entries below cover newly relied-on official URLs and additional provisions.

| Official URL | SHA256 | Read scope and confirmed additions |
|---|---|---|
| https://lovdata.no/dokument/SF/forskrift/2025-11-07-2216 | `093b5a2dd39aad385ae559c8d0b08d408a1e2c928bf652b5a028a07c2079f465` | Entire §§2–4: 693/400/107 overnight rates and lodging conditions; actual extra costs; started extra day; meal reductions 20/30/50% and nearest-krone rounding; documented higher costs; conditional 452 night supplement; 15km and 6–12/>12-hour limits with 200/400 rates; 3.50/km car,10/km snowmobile/ATV, conditional1/km additions. |
| https://lovdata.no/dokument/SF/forskrift/1999-11-19-1158/KAPITTEL_5 | `e40d406060aaacd65bbdbdf777ea308b6aca30c0c1775bcee28c6b60dd012668` | Entire §§5-11-10,5-12-20–23: qualifying communications scope;4,392 annual amount;366 derived monthly; benefit/reimbursement ceiling; no employee-payment reduction; whole/started months;14-in-30 and30-in-year sporadic limits. |
| https://lovdata.no/dokument/SF/forskrift/2007-12-21-1766 | `5b4ab4def38552dd6d9b06d04efb4bae5323bee1116a074f8f270914c0d73a09` | Entire §5-6-12 documentation/allowance conditions and §10-4-4 downward whole-krone claim rounding. |
| https://lovdata.no/dokument/SF/forskrift/1999-11-19-1158/KAPITTEL_16-3-1-1 | `ed70e72e2a6a48c7061863982c29b6e23467caa3b5a728b59632f79d1f78a919` | §§16-29-10–11: possible notarised copy/authorised Norwegian translation demand; duty to disclose reduced foreign assessment. §§16-29-1–9 were independently read from the chapter URL already in the initial ledger. |
| https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ | `31baa3aff9ebf939437cef0231100b4ee2352fadcd8077b4f4cbef56c8fc527b` | “Fribeløpsordning for ungdom på Svalbard” and “Fritidseiendom”: current youth collection/refund statement; explicitly dated advance-property treatment and30% cap. Other mainland proposed/advance figures are not imported into the pack. |
| https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/andre-inntekter/ | `0f8fd719f6f2b106af56a665043d29e90baa414125bf73d32ee5b62a7ccdc877` | Entire substantive other-income page: ordinary assessed income/wealth is returned; gross salary withholding is a separate system and salary is not entered again in that return. |

No country skill/README was edited by the reviewer. This receipt is the reviewer's only repository mutation. No external communication, publication, push or new accountant-review attribution was performed by the reviewer.
