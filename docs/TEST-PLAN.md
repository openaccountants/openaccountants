# OpenAccountants — Test Plan

15 real-world test cases across different countries, business types, and complexity levels. Each simulates a real user who cloned the repo into Claude Code and starts a conversation.

---

## How to run each test

1. Clone the repo: `git clone https://github.com/openaccountants/openaccountants.git ~/.claude/skills/openaccountants`
2. Open Claude Code
3. Paste the user message exactly as written
4. Observe: Does the right skill load? Does the flow work? Where does it break?

---

## Test 1 — UK Sole Trader, First Year

**User message:**
> "I started freelancing as a graphic designer in London in June 2025. I've never done a tax return before. I have my Starling Bank statements. Can you help me figure out what I owe?"

**Expected flow:**
- Router detects: GB, sole trader, first year
- Routes to `uk-freelance-intake`
- Intake asks: UK resident? Sole trader? VAT registered? Scottish taxpayer?
- First-year flags: cash basis default, simplified expenses option, no payments on account in year 1
- Loads: uk-self-employment-sa103 → uk-income-tax-sa100 → uk-national-insurance
- Output: SA103 trading profit, SA100 tax computation, Class 4 NIC

**What to check:**
- [ ] Does the router detect "London" → GB?
- [ ] Does the intake flag first-year reliefs?
- [ ] Does SA103 offer simplified expenses (flat rates for mileage, use of home)?
- [ ] Does SA100 correctly apply the full personal allowance (£12,570)?
- [ ] Is Class 2 NIC flagged as voluntary (post-April 2024)?
- [ ] Are payments on account correctly NOT calculated for year 1?

---

## Test 2 — Australian Sole Trader with GST

**User message:**
> "I'm a freelance web developer in Melbourne. I'm GST registered, turnover about $120K. I've got my CBA bank statements and all my invoices for the year. Need to do my BAS and tax return."

**Expected flow:**
- Router detects: AU, sole trader, full return
- Routes to `au-freelance-intake`
- Intake asks: ABN? GST registered? Simpler BAS? Home office method? HELP debt?
- Loads: australia-gst → au-individual-return → au-super-guarantee → au-medicare-levy
- Assembly cross-checks: BAS G1 = ITR business income

**What to check:**
- [ ] Does BAS correctly separate GST-free food from taxable supplies?
- [ ] Is home office at 70c/hour (not the old 67c)?
- [ ] Is motor vehicle at 88c/km (not the old 85c)?
- [ ] Is instant asset write-off at $20K per asset?
- [ ] Does Medicare levy apply at 2% with correct low-income threshold ($27,222)?
- [ ] Is super contribution voluntary (sole traders don't pay SG to themselves)?

---

## Test 3 — Canadian Freelancer in Ontario

**User message:**
> "I'm a self-employed software consultant in Toronto. Made about $95K CAD this year. I'm registered for HST. Have my TD bank statements ready."

**Expected flow:**
- Router detects: CA (Ontario), sole trader, full return
- Routes to `ca-freelance-intake`
- Loads: canada-gst-hst → ca-fed-t2125 → ca-fed-t1-return → ca-fed-cpp-ei

**What to check:**
- [ ] Is HST at 13% for Ontario (not 5% GST)?
- [ ] Does T2125 correctly compute net business income?
- [ ] Is CPP self-employed at 11.90% (double rate)?
- [ ] Is CPP2 at 8% on YAMPE-YMPE band?
- [ ] Does T1 use the blended 14.5% lowest bracket (not 15%)?
- [ ] Is basic personal amount $16,129?
- [ ] Does the system flag that Ontario provincial return is Q4 stub?

---

## Test 4 — Indian Freelancer, Presumptive Taxation

**User message:**
> "I'm a freelance UI/UX designer in Bangalore. All my clients pay via bank transfer and I invoice digitally. Gross receipts about ₹45 lakh. Should I use 44ADA?"

**Expected flow:**
- Router detects: IN, self-employed, income tax question
- Routes to `in-freelance-intake`
- Intake detects: digital receipts < ₹75L → 44ADA eligible
- Loads: india-gst → in-income-tax → in-advance-tax

**What to check:**
- [ ] Does the system correctly identify ₹75L threshold for digital receipts (not ₹50L)?
- [ ] Is 44ADA deemed profit 50% of gross receipts?
- [ ] Does it flag: no expense deductions allowed under 44ADA?
- [ ] Is advance tax single instalment by March 15 (not quarterly)?
- [ ] Does it ask about new vs old tax regime?
- [ ] Are GST 2.0 rates correct (5/18/40%, not old 5/12/18/28%)?

---

## Test 5 — Spanish Autónomo, First Year

**User message:**
> "Acabo de darme de alta como autónomo en Barcelona. Soy desarrollador web. ¿Me puedes ayudar con mis impuestos? Tengo mis extractos de CaixaBank."

**Expected flow:**
- Router detects: ES (Barcelona), autónomo, Spanish language
- Routes to `es-freelance-intake`
- Responds in Spanish
- Intake flags: first year → tarifa plana (€80/month RETA), 7% retención (not 15%)

**What to check:**
- [ ] Does the router detect Spanish language and respond in Spanish?
- [ ] Does it flag tarifa plana eligibility?
- [ ] Is retención at 7% for first 3 years (not 15%)?
- [ ] Does Modelo 130 use 20% cumulative method?
- [ ] Is estimación directa simplificada offered (with 5% hard-to-justify deduction)?
- [ ] Does the RETA skill show 2025 income-based tranche system?

---

## Test 6 — Netherlands ZZP'er

**User message:**
> "I'm a zzp'er in Amsterdam, working as a management consultant. About €85K revenue. I need to do my belastingaangifte and BTW-aangifte."

**Expected flow:**
- Router detects: NL, zzp'er, full return
- Content skills: netherlands-vat-return, nl-income-tax, nl-zzp-deductions

**What to check:**
- [ ] Is zelfstandigenaftrek €2,470 for 2025?
- [ ] Is urencriterium 1,225 hours flagged as a question?
- [ ] Is MKB-winstvrijstelling at 12.7%?
- [ ] Is BTW at 21% standard?
- [ ] Does Box 1 use correct brackets (35.82% / 37.48% / 49.50%)?
- [ ] Is FOR correctly flagged as abolished from 2023?

---

## Test 7 — Singapore Freelancer

**User message:**
> "I'm a freelance data scientist in Singapore. Income about SGD 150K. I need to file my Form B and also handle my GST since I just hit the $1M threshold."

**Expected flow:**
- Router detects: SG, self-employed, GST registration threshold hit
- Content skills: singapore-gst, sg-income-tax, sg-cpf-medisave

**What to check:**
- [ ] Is GST at 9% (not 8%)?
- [ ] Are GST F5 box numbers correct (the entire box structure was rewritten)?
- [ ] Does income tax use progressive rates through 22%?
- [ ] Is CPF MediSave mandatory for NTI > $6,000?
- [ ] Is NOR scheme correctly flagged as abolished from YA 2025?
- [ ] Does the system flag InvoiceNow requirements?

---

## Test 8 — South African Provisional Taxpayer

**User message:**
> "I'm a freelance marketing consultant in Johannesburg. Revenue about R650K. Need to sort out my provisional tax and annual return. Have my FNB statements."

**Expected flow:**
- Router detects: ZA, self-employed, full return
- Content skills: south-africa-vat (if registered), za-income-tax, za-provisional-tax

**What to check:**
- [ ] Are tax brackets correct (18-45% across 7 bands)?
- [ ] Is primary rebate R17,235?
- [ ] Is VAT at 15% (not 15.5% — the increase was reversed)?
- [ ] Does provisional tax show 3 periods (Aug 31, Feb 28, Sep 30 voluntary)?
- [ ] Is turnover tax option flagged for businesses under R1M?
- [ ] Is medical tax credit R364/month for first 2 members?

---

## Test 9 — Brazilian MEI / Simples Nacional

**User message:**
> "Sou desenvolvedor freelancer em São Paulo. Faturamento de R$60.000 por ano. Preciso de ajuda com IRPF e ISS."

**Expected flow:**
- Router detects: BR (São Paulo), self-employed, Portuguese language
- Content skills: brazil-vat (indirect tax), br-income-tax, br-inss

**What to check:**
- [ ] Does it respond in Portuguese?
- [ ] Does it flag MEI option (if under R$81K)?
- [ ] Is Carnê-Leão monthly computation correct?
- [ ] Are IRPF brackets correct for 2025?
- [ ] Is INSS at 20% (normal plan) or 11% (simplified)?
- [ ] Does the system explain ISS vs ICMS distinction for services?

---

## Test 10 — Japanese Freelancer, Blue Return

**User message:**
> "東京でフリーランスのエンジニアをしています。青色申告で確定申告をしたいです。銀行の明細があります。"

**Expected flow:**
- Router detects: JP (Tokyo), self-employed, Japanese language
- Content skills: japan-consumption-tax, jp-income-tax, jp-social-insurance

**What to check:**
- [ ] Does it respond in Japanese?
- [ ] Is blue return special deduction ¥650,000 (with e-Tax + double-entry)?
- [ ] Is basic deduction ¥580,000 for 2025 (increased from ¥480,000)?
- [ ] Is consumption tax at 10%/8% with qualified invoice system?
- [ ] Is National Pension ¥16,980/month?
- [ ] Does it flag the ¥10M threshold for consumption tax registration?

---

## Test 11 — UAE Freelancer, Corporate Tax

**User message:**
> "I'm a freelance software engineer in Dubai. Revenue about AED 500K. I know there's the new corporate tax — do I need to pay it? Also need help with VAT."

**Expected flow:**
- Router detects: AE (Dubai), self-employed, corporate tax + VAT
- Content skills: uae-vat, ae-corporate-tax

**What to check:**
- [ ] Is VAT at 5%?
- [ ] Is corporate tax 0% on first AED 375K, 9% above?
- [ ] Does it flag small business relief (AED 3M revenue, must elect)?
- [ ] Does it correctly state: no personal income tax in UAE?
- [ ] Is natural person threshold AED 1M flagged?
- [ ] Are e-invoicing Phase 2 waves documented?

---

## Test 12 — New Zealand Sole Trader

**User message:**
> "I'm a freelance photographer in Auckland. About NZD 90K revenue. Registered for GST. Need to sort my GST return and income tax."

**Expected flow:**
- Router detects: NZ, sole trader, full return
- Content skills: new-zealand-gst, nz-income-tax-ir3, nz-acc-levies, nz-provisional-tax

**What to check:**
- [ ] Is GST at 15%?
- [ ] Is registration threshold NZD 60K?
- [ ] Does IR3 use correct brackets (10.5% through 39%)?
- [ ] Is IETC $520 with expanded $70K upper threshold?
- [ ] Is ACC earner levy 1.67%?
- [ ] Is provisional tax flagged if RIT > $5,000?

---

## Test 13 — Irish Sole Trader

**User message:**
> "I'm a self-employed copywriter in Dublin. About €55K income. Need to do my Form 11 and sort my preliminary tax."

**Expected flow:**
- Router detects: IE (Dublin), self-employed, full return
- Content skills: ireland-vat-return (if registered), ie-income-tax-form11, ie-prsi-class-s, ie-usc, ie-preliminary-tax

**What to check:**
- [ ] Is income tax 20% standard / 40% higher (€44K single band)?
- [ ] Is USC correctly computed (0.5%/2%/3%/8% bands)?
- [ ] Is PRSI Class S at blended 4.125% for 2025?
- [ ] Is preliminary tax 100% current year or 90% prior year?
- [ ] Does it flag earned income credit (€2,000)?
- [ ] Is VAT registration threshold flagged if approaching €40K services?

---

## Test 14 — South Korean Freelancer

**User message:**
> "서울에서 프리랜서 개발자로 일하고 있습니다. 연수입 약 8천만원. 종합소득세 신고를 도와주세요."

**Expected flow:**
- Router detects: KR (Seoul), self-employed, Korean language
- Content skills: south-korea-vat, kr-income-tax, kr-social-insurance

**What to check:**
- [ ] Does it respond in Korean?
- [ ] Is 3.3% withholding on freelance income handled?
- [ ] Are 8 progressive brackets correct (6% through 45%)?
- [ ] Is local income tax 10% surtax?
- [ ] Is NPS at 9% (ceiling KRW 6,370,000/month from Jul 2025)?
- [ ] Is NHIS point-based for self-employed?

---

## Test 15 — Mexican Freelancer

**User message:**
> "Soy freelancer de diseño gráfico en Ciudad de México. Facturo como persona física con actividad profesional. Necesito ayuda con mi declaración anual de ISR y mis pagos provisionales."

**Expected flow:**
- Router detects: MX (CDMX), self-employed, Spanish language
- Routes to `es-freelance-intake` — WAIT, this should route to Mexico, not Spain
- Content skills: mexico-iva, mx-income-tax, mx-estimated-tax

**What to check:**
- [ ] Does the router correctly distinguish Mexico from Spain (both Spanish-speaking)?
- [ ] Is IVA at 16% (not Spain's 21%)?
- [ ] Is ISR computed with 11-tier annual tariff?
- [ ] Are pagos provisionales monthly (not quarterly like Spain)?
- [ ] Is retención 10% on professional services from personas morales?
- [ ] Is CFDI 4.0 requirement flagged?
- [ ] Is UMA 2025 value correct?

---

## Scoring

For each test, score:

| Criteria | Pass/Fail |
|----------|-----------|
| Router detects correct jurisdiction | |
| Router detects correct business type | |
| Router routes to correct skill(s) | |
| Language detection works (tests 5, 9, 10, 14, 15) | |
| Key rates/thresholds are correct | |
| First-year reliefs flagged (tests 1, 5) | |
| Cross-checks pass (where assembly exists) | |
| Output format correct (4 outputs) | |
| Conservative defaults applied correctly | |
| Reviewer flags are appropriate | |

**Target: 90%+ pass rate across all 15 tests before launch.**
