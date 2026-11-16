---
name: japan-formation
description: "Use this skill whenever asked about forming, incorporating, or registering a company in Japan. Trigger on phrases like \"set up a company in Japan\", \"KK formation\", \"GK formation\", \"kabushiki kaisha\", \"godo kaisha\", \"法務局\", \"Legal Affairs Bureau\", \"Japanese company formation\", \"register a business Japan\", \"会社設立\", \"定款\", \"登録免許税\", or any question about starting a business entity in Japan. Covers entity types (KK, GK, branch office), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Japanese company formation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/japan-formation"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan Formation

> **General reference only.** This skill produces working papers for professional review. It has not been approved by an accountant for any particular person, entity, election or filing. Confirm the applicable facts and official forms before filing, paying or taking a position.

## Scope

2026 legal incorporation workflow for a Japanese KK (株式会社), GK (合同会社), individual business and foreign-parent branch. The output is a registration and post-registration checklist with fee calculations. `jp-incorporation` handles the separate financial decision whether a sole proprietor should incorporate. A branch is part of its foreign parent; it is not a separate Japanese limited-liability company. Industry permits, immigration permission and a bank account are separate tasks.

Quick reference: KK articles require notarisation; GK articles do not. Registration tax is capital-based with a minimum. Incorporation does not itself grant a right to live or work in Japan. Sources are Companies Act arts. 30, 49, 575-579 and the official fee/ISA pages below.

## Ask the client first

- Owners, beneficial owners, residence, nationality, corporate versus individual founders, and intended representative.
- KK/GK/branch, proposed name and exact registered address, business purpose and regulated activity.
- Cash and in-kind contributions, capital, financing requirements and foreign documents.
- Immigration status and whether Business Manager permission is needed.
- First year-end, anticipated payroll, employees and consumption-tax/invoice status.
- Who will prepare the Japanese application, translations, proof of payment and post-registration notices.

## The method, step by step

### Choose the form and name

An individual business has no separate corporate personality and the proprietor bears business liabilities. KK shareholders and GK limited-liability members have limited liability subject to the Companies Act. KK governance separates shareholders and directors; GK members manage by default unless articles provide otherwise. Transfer of GK interests normally needs other members' consent, with statutory exceptions and freedom to vary by articles. Decide funding, voting, exit, profit distribution and customer requirements before choosing. Do not describe perceived prestige as law. Sources: Companies Act arts. 104, 576, 580, 585, 590, 599 and 622, https://laws.e-gov.go.jp/law/417AC0000000086.

JETRO’s official comparison lists capital of JPY 1 or more and at least 1 investor for KK/GK. This nominal capital is separate from viable working capital or immigration eligibility. KK/GK representatives need not satisfy the former Japan-domicile requirement (removed from 16 March 2015), while a branch needs at least 1 representative resident in Japan. Source: JETRO section1.2 and notes, https://www.jetro.go.jp/en/invest/setting_up/section1/page2.html.

Use the entity characters in the trade name. The registration refusal is an identical name at an identical head-office location, not a ban on every similar name in a municipality. A registration search does not clear trademarks or misleading use. Sources: Companies Act arts. 6 and 8, https://laws.e-gov.go.jp/law/417AC0000000086; Commercial Registration Act art. 27, https://laws.e-gov.go.jp/law/338AC0000000125.

### Articles, capital, notarisation and registration

Prepare KK articles showing purpose, name, head-office location, contributed value/minimum and incorporators; decide share structure, officers and year-end. Notarise KK articles before filing. For a GK, all intended members sign or seal articles specifying their liability and contributions; notarisation is not the KK requirement. Pay contributions before incorporation; document the bank, payer, amount and payment date. In-kind KK contributions require the art. 33 examination analysis, including its exemptions. Do not substitute an unsupported banking-capital recommendation for a legal requirement. Sources: Companies Act arts. 27, 30, 33-34 and 575-578, https://laws.e-gov.go.jp/law/417AC0000000086.

| Fee or boundary | Complete condition | Official source |
|---|---|---|
| KK registration tax | Capital × 0.7%, minimum JPY 150,000; ordinary incorporation, before any separately verified relief ; monetary amounts derived from Japanese 万/億 units and 0.7% = 7/1,000 | Registration and License Tax Act, Appended Table 1; NTA No.7191, https://www.nta.go.jp/taxes/shiraberu/taxanswer/inshi/7191.htm |
| GK registration tax | Capital × 0.7%, minimum JPY 60,000; ordinary incorporation ; monetary amounts derived from Japanese 万/億 units and 0.7% = 7/1,000 | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/inshi/7191.htm |
| KK notary fee JPY 15,000 | Capital/contributed amount below JPY 1,000,000; all founders natural persons, no more than 3 founders, all initial shares subscribed by founders, no board ; monetary amounts derived from Japanese 万/億 units | Notary Fee Order art.35 proviso; https://www.koshonin.gr.jp/notary/ow12/12-q7 |
| KK notary fee JPY 30,000 | Below JPY 1,000,000 and reduced-fee conditions above not all met ; monetary amounts derived from Japanese 万/億 units | same, https://www.koshonin.gr.jp/notary/ow12/12-q7 |
| KK notary fee JPY 40,000 | JPY 1,000,000 to below JPY 3,000,000 ; monetary amounts derived from Japanese 万/億 units | same, https://www.koshonin.gr.jp/notary/ow12/12-q7 |
| KK notary fee JPY 50,000 | Other cases; articles giving only a minimum contributed amount can fall here ; monetary amounts derived from Japanese 万/億 units | same, https://www.koshonin.gr.jp/notary/ow12/12-q7 |
| Paper KK articles stamp JPY 40,000 | Electronic articles do not require this stamp; copies/certification are separate costs ; monetary amounts derived from Japanese 万/億 units | Stamp Tax Act Schedule 1 document 6; https://www.koshonin.gr.jp/notary/ow12/12-q7 |
| In-kind KK inspection exception | Aggregate specified in-kind/property-acquisition values no more than JPY 5,000,000; other art.33(10) exemptions also exist | Companies Act art.33(10), https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |

Use the Legal Affairs Bureau's application for the chosen entity and method. Assemble articles, payment evidence, resolutions/consents, identity/signature evidence and required attachments. Decide electronic signatures versus paper seals under the applicable registration procedure; a purchased set of seals is not itself incorporation. Submit at the bureau for the head office through the commercial-registration online system, by post or the supported counter process. Pay registration tax and retain the application receipt and correction requests. Legal existence follows registration. Obtain the registered-matters certificate and establish statutory/accounting records. Companies Act arts. 49, 579 and 911-914, https://laws.e-gov.go.jp/law/417AC0000000086.

### Business Manager immigration boundary

For applications under the amended criteria from 16 October 2025, test all criteria together. The new standards include JPY 30,000,000 capital/contributions for a corporate business, at least 1 eligible full-time employee, appropriate Japanese premises, Japanese-language capacity, and the applicant's qualification or experience. Capital alone does not qualify. The employee for the employment criterion must be Japanese, a special permanent resident or hold an eligible Appended Table II residence status; an Appended Table I work-status employee does not satisfy that employment criterion. The language criterion has a broader employee definition. Sources: ISA guideline, https://www.moj.go.jp/isa/content/001448070.pdf.

Language must be B2 equivalent or higher for the applicant or a full-time employee; the guideline accepts JLPT N2, BJT 400 or higher, qualifying long residence or Japanese education. The applicant needs a relevant doctoral, master's or professional degree (including equivalent foreign degree), or at least 3 years' management experience, including qualifying startup preparation. The business plan needs expert confirmation of specificity, reasonableness and feasibility under the applicable application category. Premises must support real management; combining the home and business office is generally disallowed under the guideline. Check business permits, labour/social insurance and tax payments. Do not promise permission for a paper company or prolonged unexplained absence. Source: ISA guideline, https://www.moj.go.jp/isa/content/001448070.pdf.

Pre-commencement pending applications use the former criteria. Existing holders applying during the transition to 16 October 2028 receive consideration of business circumstances and prospects of meeting the new criteria; after that date the guideline still requires a contextual assessment where the new criteria are not met, including tax compliance and prospects by the next renewal. Startup-status transitions have separate grandfathering conditions. Refer immigration cases for the applicable category, documents and transition rule; do not assume the new capital criterion automatically forces departure. Source: ISA guideline, https://www.moj.go.jp/isa/content/001448070.pdf.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| A very small registered capital | Separate lawful registration from working capital, creditor risk, visa eligibility and each bank's KYC; do not guarantee account opening |
| Foreign founder/nonresident representative | Check representative appointment, payment-account evidence, signature certification, translation/legalisation and investment restrictions for the actual documents; no blanket apostille rule |
| Branch | Assess parent liability, Japanese representative, foreign-company registration and PE tax; obtain the branch-specific filing/fee before budgeting |
| Regulated activity | Obtain the relevant permit separately; registration is not a licence to trade |
| Officer/address/capital change | Register the relevant registered matter within 2 weeks, subject to art.915 exceptions; not an accounts-filing deadline. Companies Act art.915, https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |
| Failure to register or give required notice | Up to JPY 1,000,000 administrative fine under Companies Act art.976; not an automatic fixed fine, https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |

## Worked cases

Hypothetical electronic KK with JPY 500,000 capital, 1 natural-person founder, founder subscription and no board qualifies for the reduced notary fee. Registration tax is JPY 150,000, plus notary fee JPY 15,000, giving JPY 165,000 before copies, professional services and other costs. A GK with the same capital has registration tax JPY 60,000 and no KK notary fee. The difference is JPY 105,000. This compares official fee components, not total market setup costs.

```oa-check
name: Small electronic KK versus GK official fee components
inputs:
  capital: 500000
steps:
  - kk_registration: max(capital * 0.007, 150000)
  - gk_registration: max(capital * 0.007, 60000)
  - kk_components: kk_registration + 15000
  - difference: kk_components - gk_registration
expected:
  kk_components: 165000
  gk_registration: 60000
  difference: 105000
```

At JPY 30,000,000 capital, registration tax is JPY 210,000 for either form. Electronic KK notary fee adds JPY 50,000, so those components total JPY 260,000. Paper KK articles add JPY 40,000 to reach JPY 300,000. The Business Manager test still needs the non-capital criteria.

```oa-check
name: Capital-based registration tax overrides both minima
inputs:
  capital: 30000000
steps:
  - registration: max(capital * 0.007, 150000)
  - electronic_kk_components: registration + 50000
  - paper_kk_components: electronic_kk_components + 40000
expected:
  registration: 210000
  electronic_kk_components: 260000
  paper_kk_components: 300000
```

## When to refuse or refer

Never promise a bank account or visa on the strength of registration or capital alone. Never recommend a nominee deposit without evidence and professional review. Do not miss compulsory insurance or registry-change notices. Do not describe paper articles as necessary when electronic articles are available. Refer in-kind contributions, branches, restricted investment, permits, uncertain foreign signature evidence and immigration to the relevant specialist.

## Filing and payment

| Filing | Deadline and action | Official source |
|---|---|---|
| National corporate establishment notice | Within 2 months after establishment; file 法人設立届出書 in e-Tax or paper with articles copy; obtain user identification before first e-Tax filing and retain receipt | Corporate Tax Act art.148; NTA C1-4, https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/hojin/annai/1554_2.htm |
| Corporate blue-return application | Before the earlier of the date 3 months after establishment and the end of the first business year; do not turn this into an unconditional 3-month deadline | Corporate Tax Act art.122(2), https://laws.e-gov.go.jp/law/340AC0000000034 (in words on the page) |
| Payroll-office opening notice | Within 1 month after opening the paying office; statutory withholding generally due on the 10th of the next month; special approval must be separately established | Income Tax Act arts.183,230; NTA No.2502, https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2502.htm |
| Social insurance new workplace | Within 5 days when compulsory coverage conditions are met; corporate workplaces employing an insured person, including a remunerated owner alone, can be compulsory | Japan Pension Service, https://www.nenkin.go.jp/service/kounen/tekiyo/jigyosho/20150311.html |
| Corporation tax return | Normally within 2 months after year-end; apply for an available extension separately | Corporate Tax Act art.74, https://laws.e-gov.go.jp/law/340AC0000000034 (in words on the page) |

Check prefectural/municipal establishment notices locally; they do not share a single national deadline. When hiring, prepare labour insurance and Hello Work registrations with the employment specialist. For banking, gather registry/seal or signature evidence, articles, representative identification, beneficial ownership, office and business plan; request the bank's current checklist. MUFG (三菱UFJ), SMBC (三井住友), Mizuho (みずほ), Resona, Shinsei, PayPay Bank and GMO Aozora Net Bank remain possible research targets, not an endorsement or account-opening promise.

## Completion checklist

Record entity decision, name/address clearance, articles, cash/in-kind proof, fee calculation, filed documents, registration certificate, tax/insurance notices, permits, visa boundary and bank follow-up. Record exact local deadlines and retain confirmations. Prepare bookkeeping and annual accounts with `japan-bookkeeping` and `japan-financial-statements`.

## Sources

| Source | URL | Read on |
|---|---|---|
| JETRO; Read for section1.2 capital/investor table, branch liability and representative-residence notes | https://www.jetro.go.jp/en/invest/setting_up/section1/page2.html | 2026-11-14 |
| Companies Act; Read for arts.6,8,27,30,33-34,49,104,575-599,622,911-915,976 | https://laws.e-gov.go.jp/law/417AC0000000086 | 2026-11-14 |
| Commercial Registration Act; Read for art.27 identical-name/location test | https://laws.e-gov.go.jp/law/338AC0000000125 | 2026-11-14 |
| NTA No.7191; Read for commercial-registration fee table and rate/minimum | https://www.nta.go.jp/taxes/shiraberu/taxanswer/inshi/7191.htm | 2026-11-14 |
| Japan National Notaries Association; Read for Notary Fee Order art.35 bands, reduced-fee proviso and electronic-article stamp exception | https://www.koshonin.gr.jp/notary/ow12/12-q7 | 2026-11-14 |
| ISA amended criteria guideline; Read for all amended criteria, evidence, application treatment and transitional exceptions | https://www.moj.go.jp/isa/content/001448070.pdf | 2026-11-14 |
| NTA C1-4; Read for scope, submission time, attachments and filing method | https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/hojin/annai/1554_2.htm | 2026-11-14 |
| Corporate Tax Act; Read for arts.74,122 first-year deadline exceptions | https://laws.e-gov.go.jp/law/340AC0000000034 | 2026-11-14 |
| NTA No.2502; Read for payroll opening and withholding deadline | https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2502.htm | 2026-11-14 |
| Japan Pension Service; Read for compulsory workplace scope and new-application deadline | https://www.nenkin.go.jp/service/kounen/tekiyo/jigyosho/20150311.html | 2026-11-14 |

Not yet confirmed: Legacy market timing estimates (formation 1-3 weeks, step durations, overall 3-6 weeks, bank 1-8 weeks), seal/copy/scrivener/accountant fee ranges and total fee packages; universal JPY 1,000,000-5,000,000 banking recommendation; nationwide local-notice deadlines; universal JPY 70,000 inhabitant-tax floor and fixed social-insurance percentage; blanket apostille, physical-presence, residence-account and mandatory-seal statements; branch JPY 60,000 formation fee. These are excluded from usable advice pending the relevant official procedure, bank or locality confirmation. Legal capital and immigration capital are separate; do not reuse the old simplified visa-only-capital statement.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `japan-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/japan-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
