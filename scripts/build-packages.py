#!/usr/bin/env python3
"""
Build per-jurisdiction packages from source skills.

Each package contains:
1. foundation.md — Universal execution framework (same for every country)
2. intake.md — Universal onboarding flow (same for every country)
3. [country]-[obligation].md — Country-specific content skills

US state packages (packages/us-[code]/) additionally include:
4. us-tax-workflow-base.md — US-specific workflow foundation
5. All federal skills from skills/federal/
6. Core US orchestrator files
7. State-specific skills from skills/us-states/[code]/

Usage:
    python3 scripts/build-packages.py           # rebuild all packages
    python3 scripts/build-packages.py --us-only # rebuild only US state packages

Output:
    packages/[country]/
        ├── README.md
        ├── foundation.md
        ├── intake.md
        ├── [country]-vat.md (or gst, iva, etc.)
        ├── [country]-income-tax.md (if available)
        └── [country]-ssc.md (if available)
    packages/us-[code]/
        ├── README.md
        ├── us-tax-workflow-base.md
        ├── us-*.md (federal skills)
        ├── us-federal-return-assembly.md
        └── [code]-*.md (state-specific skills)
"""

import os
import re
import shutil
import sys

from frontmatter_yaml import FrontmatterError, load_frontmatter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
PACKAGES_DIR = os.path.join(REPO_ROOT, "packages")

# ============================================================================
# HAND-AUTHORED PACKAGES — DO NOT WIPE, DO NOT REGENERATE.
#
# These directories under packages/ are maintained BY HAND (CPA-reviewed form
# guides, rates.*.json reference data, runbooks). They have NO builder in this
# script: if the packages/ wipe deletes them, the content is PERMANENTLY LOST.
# The rebuild in main() must always skip these directories, and no builder may
# ever write into them.
# ============================================================================
HAND_AUTHORED_PACKAGES = {"us-federal"}

# Country code → display name mapping
COUNTRY_NAMES = {
    "MT": "Malta", "GB": "United Kingdom", "DE": "Germany", "AU": "Australia",
    "CA": "Canada", "IN": "India", "ES": "Spain", "US-CA": "United States (California)",
    "FR": "France", "IT": "Italy", "NL": "Netherlands", "PT": "Portugal",
    "BE": "Belgium", "AT": "Austria", "CH": "Switzerland", "SE": "Sweden",
    "DK": "Denmark", "NO": "Norway", "PL": "Poland", "CZ": "Czech Republic",
    "RO": "Romania", "HU": "Hungary", "GR": "Greece", "IE": "Ireland",
    "FI": "Finland", "BG": "Bulgaria", "HR": "Croatia", "SK": "Slovakia",
    "SI": "Slovenia", "EE": "Estonia", "LV": "Latvia", "LT": "Lithuania",
    "LU": "Luxembourg", "CY": "Cyprus", "IS": "Iceland", "JP": "Japan",
    "SG": "Singapore", "KR": "South Korea", "NZ": "New Zealand",
    "BR": "Brazil", "MX": "Mexico", "AR": "Argentina", "CL": "Chile",
    "CO": "Colombia", "PE": "Peru", "AE": "UAE", "SA": "Saudi Arabia",
    "ZA": "South Africa", "KE": "Kenya", "NG": "Nigeria", "IL": "Israel",
    "EG": "Egypt", "TR": "Turkey", "UA": "Ukraine", "RU": "Russia",
    "TH": "Thailand", "VN": "Vietnam", "ID": "Indonesia", "PH": "Philippines",
    "MY": "Malaysia", "BD": "Bangladesh", "PK": "Pakistan", "LK": "Sri Lanka",
    "CN": "China", "TW": "Taiwan", "HK": "Hong Kong", "BH": "Bahrain",
    "OM": "Oman", "QA": "Qatar", "KW": "Kuwait", "JO": "Jordan",
    "GE": "Georgia", "AM": "Armenia", "AZ": "Azerbaijan", "KZ": "Kazakhstan",
    "RS": "Serbia", "BA": "Bosnia and Herzegovina", "ME": "Montenegro",
    "MK": "North Macedonia", "AL": "Albania", "XK": "Kosovo", "MD": "Moldova",
    "BY": "Belarus", "UZ": "Uzbekistan", "HN": "Honduras", "GT": "Guatemala",
    "SV": "El Salvador", "NI": "Nicaragua", "CR": "Costa Rica", "PA": "Panama",
    "DO": "Dominican Republic", "EC": "Ecuador", "PY": "Paraguay",
    "UY": "Uruguay", "BO": "Bolivia", "VE": "Venezuela", "JM": "Jamaica",
    "TT": "Trinidad and Tobago", "BB": "Barbados", "BS": "Bahamas",
    "GH": "Ghana", "TZ": "Tanzania", "UG": "Uganda", "RW": "Rwanda",
    "ET": "Ethiopia", "CM": "Cameroon", "CI": "Ivory Coast", "SN": "Senegal",
    "MZ": "Mozambique", "ZM": "Zambia", "ZW": "Zimbabwe", "TN": "Tunisia",
    "MA": "Morocco", "MU": "Mauritius", "IR": "Iran", "IQ": "Iraq",
    "LB": "Lebanon", "FJ": "Fiji", "PG": "Papua New Guinea", "MN": "Mongolia",
    "KH": "Cambodia", "LA": "Laos", "MV": "Maldives", "NP": "Nepal",
    "MM": "Myanmar", "BN": "Brunei", "AD": "Andorra", "LI": "Liechtenstein",
    "MC": "Monaco", "IM": "Isle of Man", "BM": "Bermuda", "VG": "BVI",
    "KY": "Cayman Islands",
}

# Practitioner titles by country
PRACTITIONER_TITLES = {
    "MT": "warranted accountant", "GB": "chartered accountant", "DE": "Steuerberater",
    "AU": "registered tax agent", "CA": "CPA", "IN": "Chartered Accountant (CA)",
    "ES": "asesor fiscal", "FR": "expert-comptable", "IT": "commercialista",
    "NL": "belastingadviseur", "PT": "contabilista certificado", "BE": "accountant",
    "AT": "Steuerberater", "CH": "Steuerberater/fiduciaire", "SE": "auktoriserad revisor",
    "JP": "税理士 (zeirishi)", "SG": "ISCA member", "KR": "세무사 (semusa)",
    "NZ": "chartered accountant", "BR": "contador", "MX": "contador público",
    "ZA": "SAIPA/SAICA member", "US-CA": "CPA or EA",
}

# Directory name → jurisdiction code mapping
DIR_TO_CODE = {
    "malta": "MT", "uk": "GB", "germany": "DE", "australia": "AU",
    "canada": "CA", "india": "IN", "spain": "ES", "france": "FR",
    "italy": "IT", "netherlands": "NL", "portugal": "PT", "belgium": "BE",
    "austria": "AT", "switzerland": "CH", "sweden": "SE", "denmark": "DK",
    "norway": "NO", "poland": "PL", "czech-republic": "CZ", "romania": "RO",
    "hungary": "HU", "greece": "GR", "ireland": "IE", "finland": "FI",
    "bulgaria": "BG", "croatia": "HR", "slovakia": "SK", "slovenia": "SI",
    "estonia": "EE", "latvia": "LV", "lithuania": "LT", "luxembourg": "LU",
    "cyprus": "CY", "iceland": "IS", "japan": "JP", "singapore": "SG",
    "south-korea": "KR", "new-zealand": "NZ", "brazil": "BR", "mexico": "MX",
    "argentina": "AR", "chile": "CL", "colombia": "CO", "peru": "PE",
    "uae": "AE", "saudi-arabia": "SA", "south-africa": "ZA", "kenya": "KE",
    "nigeria": "NG", "israel": "IL", "egypt": "EG", "turkey": "TR",
    "ukraine": "UA", "russia": "RU", "thailand": "TH", "vietnam": "VN",
    "indonesia": "ID", "philippines": "PH", "malaysia": "MY",
    "bangladesh": "BD", "pakistan": "PK", "sri-lanka": "LK", "china": "CN",
    "taiwan": "TW", "hong-kong": "HK", "bahrain": "BH", "oman": "OM",
    "qatar": "QA", "kuwait": "KW", "jordan": "JO", "georgia": "GE",
    "armenia": "AM", "azerbaijan": "AZ", "kazakhstan": "KZ", "serbia": "RS",
    "bosnia": "BA", "montenegro": "ME", "north-macedonia": "MK",
    "albania": "AL", "kosovo": "XK", "moldova": "MD", "belarus": "BY",
    "uzbekistan": "UZ", "honduras": "HN", "guatemala": "GT",
    "el-salvador": "SV", "nicaragua": "NI", "costa-rica": "CR",
    "panama": "PA", "dominican-republic": "DO", "ecuador": "EC",
    "paraguay": "PY", "uruguay": "UY", "bolivia": "BO", "venezuela": "VE",
    "jamaica": "JM", "trinidad-and-tobago": "TT", "barbados": "BB",
    "bahamas": "BS", "ghana": "GH", "tanzania": "TZ", "uganda": "UG",
    "rwanda": "RW", "ethiopia": "ET", "cameroon": "CM", "ivory-coast": "CI",
    "senegal": "SN", "mozambique": "MZ", "zambia": "ZM", "zimbabwe": "ZW",
    "tunisia": "TN", "morocco": "MA", "mauritius": "MU", "iran": "IR",
    "iraq": "IQ", "lebanon": "LB", "fiji": "FJ", "papua-new-guinea": "PG",
    "mongolia": "MN", "cambodia": "KH", "laos": "LA", "maldives": "MV",
    "nepal": "NP", "myanmar": "MM", "brunei": "BN", "andorra": "AD",
    "liechtenstein": "LI", "monaco": "MC", "isle-of-man": "IM",
    "bermuda": "BM", "bvi": "VG", "cayman-islands": "KY",
    "algeria": "DZ",
}

# EU member states (need eu-vat-base.md)
EU_MEMBERS = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR",
    "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL",
    "PL", "PT", "RO", "SK", "SI", "ES", "SE"
}

# Per-country metadata for keyword enrichment and discoverability.
# Keys are jurisdiction codes (matching COUNTRY_NAMES keys).
# tax_authority: official tax body name
# local_terms: local-language tax/accounting terms people search for
COUNTRY_METADATA = {
    "MT": {"tax_authority": "Commissioner for Revenue (CFR)", "local_terms": "perit tal-kontijiet, taxxa fuq id-dħul, VAT Malta, CfR"},
    "GB": {"tax_authority": "HM Revenue & Customs (HMRC)", "local_terms": "chartered accountant, self-assessment, SA100, SA103, NIC, PAYE, Making Tax Digital"},
    "DE": {"tax_authority": "Finanzamt / Bundeszentralamt für Steuern", "local_terms": "Steuerberater, Einkommensteuer, Umsatzsteuer, UStVA, Gewerbesteuer, EÜR"},
    "AU": {"tax_authority": "Australian Taxation Office (ATO)", "local_terms": "registered tax agent, BAS, ITR, superannuation, Medicare levy, ABN"},
    "CA": {"tax_authority": "Canada Revenue Agency (CRA)", "local_terms": "CPA, T1, T2125, GST/HST, CPP, EI, RRSP"},
    "IN": {"tax_authority": "Income Tax Department / CBDT / GSTN", "local_terms": "Chartered Accountant, ITR-3, ITR-4, GST, TDS, advance tax, PAN"},
    "ES": {"tax_authority": "Agencia Tributaria (AEAT)", "local_terms": "asesor fiscal, IRPF, IVA, modelo 303, modelo 130, RETA, autónomo"},
    "FR": {"tax_authority": "Direction générale des Finances publiques (DGFiP)", "local_terms": "expert-comptable, impôt sur le revenu, TVA, micro-entrepreneur, BNC, URSSAF, CFE"},
    "IT": {"tax_authority": "Agenzia delle Entrate", "local_terms": "commercialista, IRPEF, IVA, regime forfettario, partita IVA, INPS, F24"},
    "NL": {"tax_authority": "Belastingdienst", "local_terms": "belastingadviseur, inkomstenbelasting, BTW, ZZP, IB-aangifte, KvK"},
    "PT": {"tax_authority": "Autoridade Tributária e Aduaneira (AT)", "local_terms": "contabilista certificado, IRS, IVA, recibos verdes, trabalhador independente"},
    "BE": {"tax_authority": "SPF Finances / FOD Financiën", "local_terms": "comptable, impôt des personnes physiques, TVA/BTW, cotisations sociales, IPP"},
    "AT": {"tax_authority": "Bundesministerium für Finanzen / FinanzOnline", "local_terms": "Steuerberater, Einkommensteuer, Umsatzsteuer, SVS, EPU"},
    "CH": {"tax_authority": "Eidgenössische Steuerverwaltung (ESTV) / AFC", "local_terms": "Steuerberater, fiduciaire, Mehrwertsteuer, MWST, AHV/IV, direkte Bundessteuer"},
    "SE": {"tax_authority": "Skatteverket", "local_terms": "auktoriserad revisor, inkomstskatt, moms, F-skatt, egenavgifter, enskild firma"},
    "DK": {"tax_authority": "Skattestyrelsen", "local_terms": "revisor, indkomstskat, moms, B-skat, AM-bidrag"},
    "NO": {"tax_authority": "Skatteetaten", "local_terms": "regnskapsfører, inntektsskatt, merverdiavgift (MVA), forskuddsskatt, enkeltpersonforetak"},
    "PL": {"tax_authority": "Krajowa Administracja Skarbowa (KAS)", "local_terms": "księgowy, PIT, VAT, ZUS, JPK, działalność gospodarcza"},
    "CZ": {"tax_authority": "Finanční správa České republiky", "local_terms": "daňový poradce, daň z příjmů, DPH, OSVČ, sociální pojištění"},
    "RO": {"tax_authority": "ANAF (Agenția Națională de Administrare Fiscală)", "local_terms": "contabil, impozit pe venit, TVA, CAS, CASS, PFA"},
    "HU": {"tax_authority": "Nemzeti Adó- és Vámhivatal (NAV)", "local_terms": "könyvelő, személyi jövedelemadó, ÁFA, KATA, egyéni vállalkozó"},
    "GR": {"tax_authority": "AADE (Ανεξάρτητη Αρχή Δημοσίων Εσόδων)", "local_terms": "λογιστής, φόρος εισοδήματος, ΦΠΑ, ΕΦΚΑ, ελεύθερος επαγγελματίας"},
    "IE": {"tax_authority": "Revenue Commissioners", "local_terms": "chartered accountant, income tax, VAT, PRSI, USC, self-employed, Form 11"},
    "FI": {"tax_authority": "Verohallinto", "local_terms": "tilitoimisto, tulovero, arvonlisävero (ALV), YEL, toiminimi"},
    "JP": {"tax_authority": "National Tax Agency (国税庁)", "local_terms": "税理士 (zeirishi), 確定申告 (kakutei shinkoku), 消費税 (shōhizei), 所得税, 青色申告"},
    "SG": {"tax_authority": "Inland Revenue Authority of Singapore (IRAS)", "local_terms": "ISCA member, GST, income tax, CPF, sole proprietorship"},
    "KR": {"tax_authority": "National Tax Service (국세청)", "local_terms": "세무사 (semusa), 부가가치세, 종합소득세, 사업자등록"},
    "NZ": {"tax_authority": "Inland Revenue (IRD)", "local_terms": "chartered accountant, GST, income tax, ACC levy, sole trader"},
    "BR": {"tax_authority": "Receita Federal do Brasil", "local_terms": "contador, imposto de renda, IRPF, Simples Nacional, MEI, INSS, nota fiscal"},
    "MX": {"tax_authority": "Servicio de Administración Tributaria (SAT)", "local_terms": "contador público, ISR, IVA, CFDI, RIF, persona física con actividad empresarial"},
    "AR": {"tax_authority": "AFIP (Administración Federal de Ingresos Públicos)", "local_terms": "contador público, impuesto a las ganancias, IVA, monotributo, autónomo"},
    "CL": {"tax_authority": "Servicio de Impuestos Internos (SII)", "local_terms": "contador auditor, impuesto a la renta, IVA, boleta de honorarios, PPM"},
    "CO": {"tax_authority": "DIAN (Dirección de Impuestos y Aduanas Nacionales)", "local_terms": "contador público, impuesto de renta, IVA, régimen simple, RUT"},
    "ZA": {"tax_authority": "South African Revenue Service (SARS)", "local_terms": "SAIPA, SAICA, income tax, VAT, provisional tax, ITR12, sole proprietor"},
    "KE": {"tax_authority": "Kenya Revenue Authority (KRA)", "local_terms": "CPA, income tax, VAT, iTax, turnover tax, KRA PIN"},
    "NG": {"tax_authority": "Federal Inland Revenue Service (FIRS)", "local_terms": "chartered accountant, PAYE, VAT, CIT, TIN"},
    "IL": {"tax_authority": "Israel Tax Authority (רשות המסים)", "local_terms": "רואה חשבון (ro'e cheshbon), מס הכנסה, מע\"מ, עוסק מורשה, ביטוח לאומי"},
    "AE": {"tax_authority": "Federal Tax Authority (FTA)", "local_terms": "VAT, corporate tax, tax agent, TRN, free zone"},
    "SA": {"tax_authority": "Zakat, Tax and Customs Authority (ZATCA)", "local_terms": "VAT, zakat, e-invoicing, FATOORAH, محاسب قانوني"},
    "TH": {"tax_authority": "Revenue Department (กรมสรรพากร)", "local_terms": "ผู้สอบบัญชี, ภาษีเงินได้, VAT, PND.90, PND.91"},
    "VN": {"tax_authority": "General Department of Taxation", "local_terms": "kế toán, thuế thu nhập cá nhân, thuế GTGT, hóa đơn điện tử"},
    "ID": {"tax_authority": "Direktorat Jenderal Pajak (DJP)", "local_terms": "konsultan pajak, PPh, PPN, NPWP, SPT, e-Filing"},
    "PH": {"tax_authority": "Bureau of Internal Revenue (BIR)", "local_terms": "CPA, income tax, VAT, BIR Form 1701, TIN, percentage tax"},
    "MY": {"tax_authority": "Inland Revenue Board of Malaysia (LHDN)", "local_terms": "tax agent, income tax, SST, PCB, e-Filing, sole proprietor"},
    "CN": {"tax_authority": "State Taxation Administration (国家税务总局)", "local_terms": "注册会计师, 个人所得税, 增值税, 发票, 税务登记"},
    "TW": {"tax_authority": "National Taxation Bureau (國稅局)", "local_terms": "會計師, 所得稅, 營業稅, 統一發票, 執行業務所得"},
    "HK": {"tax_authority": "Inland Revenue Department (IRD)", "local_terms": "CPA, profits tax, salaries tax, MPF, sole proprietor"},
    "TR": {"tax_authority": "Gelir İdaresi Başkanlığı (GİB)", "local_terms": "mali müşavir, gelir vergisi, KDV, serbest meslek, e-fatura"},
    "RU": {"tax_authority": "Federal Tax Service (ФНС России)", "local_terms": "бухгалтер, НДФЛ, НДС, ИП, УСН, патент, самозанятый"},
}


def build_foundation():
    """Build compressed universal foundation."""
    return """# Foundation — How This System Works

> Upload this file alongside your country's skill files.
> This tells the AI HOW to work. The country files tell it WHAT the rules are.
> Covers all domains: tax, bookkeeping, payroll, e-invoicing, formation, financial statements, transfer pricing, and tax optimization.

## Conservative Defaults Principle

When uncertain about any position, choose the treatment that costs more or imposes stricter compliance, never less.
Your reviewer can correct an over-conservative position. They cannot easily recover from an aggressive one.

## Classification Contract

Every transaction or data point gets exactly one of three outcomes:

**Classified** — The documents carry enough info to apply the rule. No flag needed.

**Assumed** — A fact is missing. Conservative default applied. Disclosed to reviewer with the exact assumption and impact.

**Needs Input** — Cannot proceed without asking you. One targeted question, then classified.

## Domain-Specific Outputs

Depending on the domain, produce the relevant outputs:

### Tax
1. **Working paper** — Transaction-by-transaction classification with form line assignments
2. **Reviewer brief** — Every position cited to statute, every assumption disclosed, flags ranked by cash impact
3. **Action list** — What to do, when, how much to pay
4. **Review checklist** — Pre-populated sign-off document for your reviewer

### Bookkeeping
1. **Classified journal entries** — Double-entry postings with account codes
2. **Trial balance** — Debit/credit summary
3. **P&L and balance sheet** — In the country's required format

### Payroll
1. **Payslip** — Gross to net breakdown per employee
2. **Employer cost summary** — Total cost including employer contributions
3. **Filing summary** — What to report, when, to which authority

### Other domains
Each domain-specific workflow base defines its own output format. Load the relevant workflow base alongside country skills.

## Execution Rules

- Process ALL data before producing outputs. Do not output partial results.
- Every rate and threshold must cite the primary statute or authority.
- Never invent a classification code. Use only codes from the loaded country skill.
- When a transaction doesn't match the supplier pattern library, fall through to the general rules.
- Group related Assumed items (e.g., "5 entertainment expenses blocked, total EUR 340").
- Do not re-ask questions the documents already answered.
- When multiple domains apply (e.g., a payroll question that also affects income tax), address both.

## Reviewer Assumption

Everything you produce is addressed to a credentialed reviewer. You are not the preparer of record. The reviewer signs off. Your job is to make their review fast and accurate.

---

*OpenAccountants — openaccountants.com*
*This is not tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing or acting upon.*

## MANDATORY: Include in EVERY output you produce

At the TOP of every working paper, reviewer brief, and action list, include this notice:

> **Produced by OpenAccountants (openaccountants.com)**
>
> This output is for informational purposes only and does not constitute tax, legal, or financial advice.
> All positions must be reviewed and signed off by a qualified professional before filing or acting upon.
>
> Get this reviewed by a licensed accountant: **openaccountants.com**
>
> Found an error? Report it: **github.com/openaccountants/openaccountants/issues**

At the END of every output, include:

> ---
> OpenAccountants — open-source accounting skills for AI
> This output must be reviewed by a qualified professional before filing or acting upon.
> Latest verified skills: **openaccountants.com** | Report errors: **github.com/openaccountants/openaccountants**

**Do NOT skip these notices. They are mandatory on every output.**
"""


def build_intake(country_name, practitioner_title, jurisdiction_code):
    """Build universal intake with country-specific variables filled in."""
    return f"""# Intake — Onboarding for {country_name}

> This file guides the AI through the onboarding process.
> It runs BEFORE any classification begins.

## Opening statement

Say this FIRST, before any questions:

> "I'll help you with your {country_name} accounting and tax working papers. Everything I produce is for your {practitioner_title} to review — I won't file anything. Let me ask a few questions to make sure I can help."

## Step 1: Scope Check

Ask these questions as a batch. Do not explain the workflow. Just ask.

| # | Question |
|---|----------|
| 1 | Were you a full-year {country_name} resident in 2025? |
| 2 | What is your business structure? (Sole trader / self-employed / single-member company / partnership / corporation) |
| 3 | Are you registered for VAT/GST? If yes, what type/scheme? |
| 4 | Do you have employees? If yes, how many? |
| 5 | What industry/sector are you in? |
| 6 | Accounting method: cash basis or accrual? |
| 7 | What do you need help with? (tax return / bookkeeping / payroll / invoicing / annual accounts / company setup / all of the above) |

## Refusals (STOP if any trigger)

| Trigger | Response |
|---------|----------|
| Not full-year resident | "I'm set up for full-year {country_name} residents only. You need a {practitioner_title} who handles non-resident returns." |
| Partnership tax return | "Partnership tax returns file separately. You need a {practitioner_title} familiar with partnership returns." |
| Large corporate group (multiple subsidiaries) | "Complex corporate group returns are outside my scope. You need a {practitioner_title}." |

If all checks pass, continue.

## Step 2: Document Upload

Accept ANY documents the user provides — not just bank statements:
- Bank statements (CSV or PDF)
- Sales invoices / issued invoices
- Purchase invoices / received invoices
- Receipts
- Prior year return
- VAT/GST returns already filed
- Any other tax documents

Say: **"Drop all your documents here — bank statements, invoices, receipts, prior returns. Everything you have for 2025. I can read PDFs, CSVs, images, and spreadsheets."**

**Do NOT insist on bank statements.** If the user only has invoices, work with invoices. If they only have a bank statement, work with that. Use whatever documents are provided.

## Step 3: Inference

Read ALL provided documents and extract:
- Gross revenue / turnover (from invoices, bank credits, or both)
- Expenses by category (from purchase invoices, bank debits, or both)
- VAT/GST collected and paid (from invoices or returns)
- Tax payments already made (estimated/provisional)
- Client breakdown (domestic vs international)
- Capital items purchased
- Any prepayments or multi-year items (flag these for accounting method decision)

Present a summary and ask: **"Does this look right? Anything missing or wrong?"**

## Step 4: Gap Filling

Ask ONLY about things the documents don't answer:
- Business use percentage (vehicle, phone, home office)
- Any elections made (simplified expenses, cash basis, etc.)
- First year in business?
- Director's remuneration / salary drawn? (if company structure)

## Step 5: Decisions

After classification, present any decisions the user or their {practitioner_title} needs to make:

> **Decisions for you / your {practitioner_title}:**
> 1. [Decision] — [Option A: effect] vs [Option B: effect]
> 2. [Decision] — [Option A: effect] vs [Option B: effect]

These are items where the accounting treatment depends on a choice (cash vs accrual, simplified vs actual, capitalise vs expense). Present the options with the cash impact of each.

Then proceed to classification using the loaded country skills.

---

*OpenAccountants — openaccountants.com*
*All outputs must be reviewed by a {practitioner_title} before filing.*
"""


def build_readme(country_name, files, practitioner_title, jurisdiction_code):
    """Build per-jurisdiction README with keyword enrichment and accountant CTA."""
    file_list = "\n".join([f"{i+1}. `{f}`" for i, f in enumerate(files)])

    meta = COUNTRY_METADATA.get(jurisdiction_code, {})
    tax_authority = meta.get("tax_authority", "your national tax authority")
    local_terms = meta.get("local_terms", "")

    keywords_section = ""
    if local_terms:
        keywords_section = f"""
## Also known as

{local_terms}

Tax authority: **{tax_authority}**
"""
    elif tax_authority != "your national tax authority":
        keywords_section = f"""
## Tax authority

**{tax_authority}**
"""

    return f"""# {country_name} — AI Accounting Assistant | OpenAccountants

> Open-source accounting skills for {country_name}. Upload to Claude, ChatGPT, or any AI assistant.
> Tax, bookkeeping, payroll, formation, financial statements, and more. Free and open source.

## What's in this folder

{file_list}
{keywords_section}
## How to use

1. Upload ALL files in this folder to your AI assistant (Claude, ChatGPT, Gemini, etc.)
2. Attach your bank statement, invoices, or any financial documents (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my 2025 {country_name} taxes. Here's my bank statement."**
   - **"Classify my transactions and prepare my books."**
   - **"Run payroll for my employee."**
   - **"Help me set up a company in {country_name}."**
   - **"Prepare my annual accounts."**

The AI will:
- Ask onboarding questions to confirm your situation
- Load the right domain skills (tax, bookkeeping, payroll, etc.)
- Produce working papers for each obligation
- Flag anything that needs your {practitioner_title}'s attention

## Important

**This is not tax, legal, or financial advice.** Everything produced must be reviewed and signed off by a qualified {practitioner_title} before filing or acting upon.

The most up-to-date, verified version of these skills is maintained at [openaccountants.com](https://www.openaccountants.com).

---

## Are you a {practitioner_title}?

These {country_name} tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a human professional to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against {tax_authority}'s website
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source file under `skills/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*134 countries + 51 US states — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
"""


def _is_redirect(filepath):
    """Return True if a .md file is a redirect stub (not real content)."""
    with open(filepath, 'r', errors='ignore') as fh:
        lines = fh.readlines()
    if len(lines) <= 50:
        content = ''.join(lines[:20]).lower()
        if 'consolidated' in content or 'redirect' in content:
            return True
        # Short non-redirect files (like references.md) are kept
        return False
    return False


def find_country_skills(country_dir):
    """Find all content skill files for a country, including subdirectories."""
    skills = []
    if not os.path.isdir(country_dir):
        return skills

    for root, _dirs, files in os.walk(country_dir):
        for f in sorted(files):
            if not f.endswith('.md') or f.startswith('.'):
                continue
            filepath = os.path.join(root, f)
            if _is_redirect(filepath):
                continue
            with open(filepath, 'r', errors='ignore') as fh:
                line_count = sum(1 for _ in fh)
            if line_count < 5:
                continue  # skip near-empty stubs
            skills.append((f, filepath))

    return skills


def find_orchestrator_files(country_dir_name):
    """Find intake and assembly files for a country."""
    orch_dir = os.path.join(SKILLS_DIR, "orchestrator")
    prefix_map = {
        "malta": "mt-", "uk": "uk-", "germany": "de-", "australia": "au-",
        "canada": "ca-", "india": "in-", "spain": "es-",
        "france": "fr-", "japan": "jp-", "netherlands": "nl-",
        "brazil": "br-", "mexico": "mx-",
    }

    prefix = prefix_map.get(country_dir_name)
    if not prefix:
        return None, None

    intake = None
    assembly = None

    for f in os.listdir(orch_dir):
        if f.startswith(prefix) and 'intake' in f:
            intake = os.path.join(orch_dir, f)
        if f.startswith(prefix) and 'assembly' in f:
            assembly = os.path.join(orch_dir, f)

    return intake, assembly


def build_package(country_dir_name, country_dir):
    """Build a complete package for one jurisdiction."""
    code = DIR_TO_CODE.get(country_dir_name, country_dir_name.upper()[:2])
    name = COUNTRY_NAMES.get(code, country_dir_name.replace('-', ' ').title())
    practitioner = PRACTITIONER_TITLES.get(code, "qualified tax professional")

    # Find content skills
    content_skills = find_country_skills(country_dir)
    if not content_skills:
        return None

    # Create package directory
    pkg_dir = os.path.join(PACKAGES_DIR, country_dir_name)
    os.makedirs(pkg_dir, exist_ok=True)

    # Write foundation
    with open(os.path.join(pkg_dir, "foundation.md"), 'w') as f:
        f.write(build_foundation())

    # Write intake
    with open(os.path.join(pkg_dir, "intake.md"), 'w') as f:
        f.write(build_intake(name, practitioner, code))

    # Copy content skills
    copied_files = ["foundation.md", "intake.md"]
    for filename, filepath in content_skills:
        dest = os.path.join(pkg_dir, filename)
        shutil.copy2(filepath, dest)
        copied_files.append(filename)

    # Copy EU VAT base if EU member
    if code in EU_MEMBERS:
        eu_vat = os.path.join(SKILLS_DIR, "international", "eu", "eu-vat-base.md")
        if os.path.exists(eu_vat):
            shutil.copy2(eu_vat, os.path.join(pkg_dir, "eu-vat-directive.md"))
            copied_files.append("eu-vat-directive.md")

    # Copy domain-specific workflow bases when matching skills exist
    DOMAIN_BASES = {
        "bookkeeping": "bookkeeping-workflow-base.md",
        "einvoice": "einvoice-workflow-base.md",
        "payroll": "payroll-workflow-base.md",
        "formation": "company-formation-workflow-base.md",
        "financial-statements": "financial-statements-workflow-base.md",
        "transfer-pricing": "transfer-pricing-workflow-base.md",
        "tax-optimization": None,
        "crypto": "crypto-tax-workflow-base.md",
    }
    for keyword, base_file in DOMAIN_BASES.items():
        if base_file and any(keyword in f for f, _ in content_skills):
            base_path = os.path.join(SKILLS_DIR, "foundation", base_file)
            if os.path.exists(base_path):
                shutil.copy2(base_path, os.path.join(pkg_dir, base_file))
                copied_files.append(base_file)

    # Copy orchestrator files if they exist
    intake_file, assembly_file = find_orchestrator_files(country_dir_name)
    if intake_file and os.path.exists(intake_file):
        shutil.copy2(intake_file, os.path.join(pkg_dir, f"{country_dir_name}-guided-intake.md"))
        copied_files.append(f"{country_dir_name}-guided-intake.md")
    if assembly_file and os.path.exists(assembly_file):
        shutil.copy2(assembly_file, os.path.join(pkg_dir, f"{country_dir_name}-return-assembly.md"))
        copied_files.append(f"{country_dir_name}-return-assembly.md")

    # Write README
    with open(os.path.join(pkg_dir, "README.md"), 'w') as f:
        f.write(build_readme(name, copied_files, practitioner, code))

    # Count actual computation skills (not metadata like references.md)
    tax_skills = [s for s in content_skills if s[0] != "references.md"]
    skill_filenames = [s for s, _ in content_skills]
    has_bookkeeping = any("bookkeeping" in f for f in skill_filenames)
    has_einvoice = any("einvoice" in f for f in skill_filenames)
    has_payroll = any("payroll" in f for f in skill_filenames)
    has_formation = any("formation" in f for f in skill_filenames)
    has_fin_statements = any("financial-statements" in f for f in skill_filenames)
    has_tp = any("transfer-pricing" in f for f in skill_filenames)
    has_tax_opt = any("tax-optimization" in f for f in skill_filenames)
    has_crypto = any("crypto" in f for f in skill_filenames)

    return {
        "jurisdiction": code,
        "name": name,
        "files": copied_files,
        "has_orchestrator": intake_file is not None,
        "skill_count": len(tax_skills),
        "has_bookkeeping": has_bookkeeping,
        "has_einvoice": has_einvoice,
        "has_payroll": has_payroll,
        "has_formation": has_formation,
        "has_financial_statements": has_fin_statements,
        "has_transfer_pricing": has_tp,
        "has_tax_optimization": has_tax_opt,
        "has_crypto": has_crypto,
    }


# ---------------------------------------------------------------------------
# US state package generation
# ---------------------------------------------------------------------------

US_STATE_CODES = [
    "al", "ak", "az", "ar", "ca", "co", "ct", "dc", "de", "fl",
    "ga", "hi", "ia", "id", "il", "in", "ks", "ky", "la", "ma",
    "md", "me", "mi", "mn", "mo", "ms", "mt", "nc", "nd", "ne",
    "nh", "nj", "nm", "nv", "ny", "oh", "ok", "or", "pa", "ri",
    "sc", "sd", "tn", "tx", "ut", "va", "vt", "wa", "wi", "wv", "wy",
]

US_STATE_NAMES = {
    "al": "Alabama", "ak": "Alaska", "az": "Arizona", "ar": "Arkansas",
    "ca": "California", "co": "Colorado", "ct": "Connecticut",
    "dc": "District of Columbia", "de": "Delaware", "fl": "Florida",
    "ga": "Georgia", "hi": "Hawaii", "ia": "Iowa", "id": "Idaho",
    "il": "Illinois", "in": "Indiana", "ks": "Kansas", "ky": "Kentucky",
    "la": "Louisiana", "ma": "Massachusetts", "md": "Maryland",
    "me": "Maine", "mi": "Michigan", "mn": "Minnesota", "mo": "Missouri",
    "ms": "Mississippi", "mt": "Montana", "nc": "North Carolina",
    "nd": "North Dakota", "ne": "Nebraska", "nh": "New Hampshire",
    "nj": "New Jersey", "nm": "New Mexico", "nv": "Nevada",
    "ny": "New York", "oh": "Ohio", "ok": "Oklahoma", "or": "Oregon",
    "pa": "Pennsylvania", "ri": "Rhode Island", "sc": "South Carolina",
    "sd": "South Dakota", "tn": "Tennessee", "tx": "Texas", "ut": "Utah",
    "va": "Virginia", "vt": "Vermont", "wa": "Washington",
    "wi": "Wisconsin", "wv": "West Virginia", "wy": "Wyoming",
}


def build_us_state_readme(state_name, state_code, files):
    """Build README for a US state package with accountant CTA."""
    file_list = "\n".join([f"{i+1}. `{f}`" for i, f in enumerate(files)])
    return f"""# {state_name} ({state_code.upper()}) — AI Tax Assistant | OpenAccountants

> Open-source federal + {state_name} state tax skills for AI.
> Upload to Claude, ChatGPT, or any AI assistant. Verified by accountants.

## What's in this folder

This package contains **federal** tax skills (which apply to all US states) plus
**{state_name}-specific** state tax skills. Upload all files together.

{file_list}

## How to use

1. Upload ALL files in this folder to your AI assistant (Claude, ChatGPT, Gemini, etc.)
2. Attach your 2025 bank statement (CSV or PDF)
3. Say: **"Help me with my 2025 taxes. I'm based in {state_name}. Here's my bank statement."**

The AI will:
- Ask onboarding questions to confirm your situation
- Classify every transaction on your bank statement
- Produce federal AND {state_name} state working papers
- Flag anything that needs your CPA or EA's attention

## Important

**This is not tax advice.** Everything produced must be reviewed and signed off by a
qualified CPA, EA, or tax attorney before filing.

The most up-to-date, verified version of these skills is maintained at
[openaccountants.com](https://www.openaccountants.com).

---

## Are you a CPA, EA, or tax professional in {state_name}?

These {state_name} tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a human professional to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against your state tax authority's website and the IRS
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source under `skills/us-states/{state_code}/` or `skills/federal/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*134 countries + 51 US states — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
"""


def build_us_state_package(state_code):
    """Build a complete package for one US state.

    Copies federal foundation + federal skills + orchestrator files + state
    skills into packages/us-[code]/.
    """
    state_name = US_STATE_NAMES.get(state_code, state_code.upper())
    pkg_dir = os.path.join(PACKAGES_DIR, f"us-{state_code}")
    os.makedirs(pkg_dir, exist_ok=True)

    copied_files = []

    # 1. US workflow base (foundation equivalent)
    us_base = os.path.join(SKILLS_DIR, "foundation", "us-tax-workflow-base.md")
    if os.path.isfile(us_base):
        shutil.copy2(us_base, os.path.join(pkg_dir, "us-tax-workflow-base.md"))
        copied_files.append("us-tax-workflow-base.md")

    # 2. All federal skills
    federal_dir = os.path.join(SKILLS_DIR, "federal")
    if os.path.isdir(federal_dir):
        for f in sorted(os.listdir(federal_dir)):
            if f.endswith(".md"):
                shutil.copy2(os.path.join(federal_dir, f), os.path.join(pkg_dir, f))
                copied_files.append(f)

    # 3. Core US orchestrator files
    orch_dir = os.path.join(SKILLS_DIR, "orchestrator")
    core_orch = ["us-federal-return-assembly.md", "global-router.md"]
    for f in core_orch:
        src = os.path.join(orch_dir, f)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(pkg_dir, f))
            copied_files.append(f)

    # 4. State-specific orchestrator files (CA, NY, TX)
    state_orch_map = {
        "ca": ["us-ca-freelance-intake.md", "us-ca-return-assembly.md"],
        "ny": ["us-ny-freelance-intake.md", "us-ny-return-assembly.md"],
        "tx": ["us-tx-freelance-intake.md", "us-tx-return-assembly.md"],
    }
    for f in state_orch_map.get(state_code, []):
        src = os.path.join(orch_dir, f)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(pkg_dir, f))
            copied_files.append(f)

    # 5. State-specific skill files (everything except README.md)
    state_dir = os.path.join(SKILLS_DIR, "us-states", state_code)
    state_skill_count = 0
    if os.path.isdir(state_dir):
        for f in sorted(os.listdir(state_dir)):
            if f.endswith(".md") and f != "README.md":
                shutil.copy2(os.path.join(state_dir, f), os.path.join(pkg_dir, f))
                copied_files.append(f)
                state_skill_count += 1

    # 6. Generate README
    with open(os.path.join(pkg_dir, "README.md"), "w") as fh:
        fh.write(build_us_state_readme(state_name, state_code, copied_files))
    copied_files.append("README.md")

    return {
        "jurisdiction": f"US-{state_code.upper()}",
        "name": f"United States — {state_name}",
        "package_dir": f"us-{state_code}",
        "files": copied_files,
        "state_skills": state_skill_count,
        "has_orchestrator": state_code == "ca",
    }


def build_all_us_packages():
    """Build packages for all 51 US states + DC."""
    results = []
    for code in US_STATE_CODES:
        result = build_us_state_package(code)
        results.append(result)
    return results


# ---------------------------------------------------------------------------
# Canada province/territory package generation
# ---------------------------------------------------------------------------

CA_PROVINCE_CODES = [
    "ab", "bc", "mb", "nb", "nl", "ns", "nt", "nu",
    "on", "pe", "qc", "sk", "yt",
]

CA_PROVINCE_NAMES = {
    "ab": "Alberta", "bc": "British Columbia", "mb": "Manitoba",
    "nb": "New Brunswick", "nl": "Newfoundland and Labrador",
    "ns": "Nova Scotia", "nt": "Northwest Territories", "nu": "Nunavut",
    "on": "Ontario", "pe": "Prince Edward Island", "qc": "Quebec",
    "sk": "Saskatchewan", "yt": "Yukon",
}

# Source directory name under skills/international/canada/ for each province
CA_PROVINCE_DIRS = {
    "ab": "alberta", "bc": "british-columbia", "mb": "manitoba",
    "nb": "new-brunswick", "nl": "newfoundland", "ns": "nova-scotia",
    "nt": "northwest-territories", "nu": "nunavut", "on": "ontario",
    "pe": "pei", "qc": "quebec", "sk": "saskatchewan", "yt": "yukon",
}


def build_canada_province_readme(province_name, province_code, files):
    """Build README for a Canadian province/territory package."""
    file_list = "\n".join([f"{i+1}. `{f}`" for i, f in enumerate(files)])
    return f"""# {province_name} ({province_code.upper()}) — AI Tax Assistant | OpenAccountants

> Open-source federal + {province_name} provincial/territorial tax skills for AI.
> Upload to Claude, ChatGPT, or any AI assistant. Verified by accountants.

## What's in this folder

This package contains **federal Canadian** tax and accounting skills (T1, T2125,
CPP/EI, instalments, GST/HST, T1135, crypto, bookkeeping, payroll, formation,
financial statements, transfer pricing, tax optimization) plus
**{province_name}-specific** provincial/territorial tax skills. Upload all files together.

{file_list}

## How to use

1. Upload ALL files in this folder to your AI assistant (Claude, ChatGPT, Gemini, etc.)
2. Attach your 2025 bank statement (CSV or PDF)
3. Say: **"Help me with my 2025 taxes. I'm based in {province_name}. Here's my bank statement."**

The AI will:
- Ask onboarding questions to confirm your situation
- Classify every transaction on your bank statement
- Produce federal T1/T2125 AND {province_name} provincial working papers
- Flag anything that needs your CPA's attention

## Important

**This is not tax advice.** Everything produced must be reviewed and signed off by a
qualified Canadian CPA before filing.

The most up-to-date, verified version of these skills is maintained at
[openaccountants.com](https://www.openaccountants.com).

---

## Are you a CPA or tax professional in {province_name}?

These {province_name} tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a Canadian CPA to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against the CRA and your provincial/territorial finance department
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source under `skills/international/canada/{CA_PROVINCE_DIRS.get(province_code, province_code)}/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*134 countries + 51 US states + 13 Canadian provinces/territories — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
"""


def build_canada_province_package(province_code):
    """Build a complete package for one Canadian province or territory.

    Copies foundation + intake + Canadian federal skills + cross-border
    base + this province's skills into packages/ca-[code]/.
    """
    province_name = CA_PROVINCE_NAMES.get(province_code, province_code.upper())
    province_dir_name = CA_PROVINCE_DIRS.get(province_code, province_code)
    pkg_dir = os.path.join(PACKAGES_DIR, f"ca-{province_code}")
    os.makedirs(pkg_dir, exist_ok=True)

    copied_files = []

    # 1. Universal foundation
    with open(os.path.join(pkg_dir, "foundation.md"), "w") as fh:
        fh.write(build_foundation())
    copied_files.append("foundation.md")

    # 2. Canada-flavoured intake
    with open(os.path.join(pkg_dir, "intake.md"), "w") as fh:
        fh.write(build_intake("Canada", "CPA", "CA"))
    copied_files.append("intake.md")

    # 3. Federal Canadian skills (top-level .md files in skills/international/canada/)
    canada_root = os.path.join(SKILLS_DIR, "international", "canada")
    if os.path.isdir(canada_root):
        for f in sorted(os.listdir(canada_root)):
            full = os.path.join(canada_root, f)
            if os.path.isfile(full) and f.endswith(".md"):
                shutil.copy2(full, os.path.join(pkg_dir, f))
                copied_files.append(f)

    # 4. Domain workflow bases for any domains present in the federal pool
    DOMAIN_BASES = {
        "bookkeeping": "bookkeeping-workflow-base.md",
        "payroll": "payroll-workflow-base.md",
        "formation": "company-formation-workflow-base.md",
        "financial-statements": "financial-statements-workflow-base.md",
        "transfer-pricing": "transfer-pricing-workflow-base.md",
        "crypto": "crypto-tax-workflow-base.md",
    }
    for keyword, base_file in DOMAIN_BASES.items():
        if any(keyword in f for f in copied_files):
            base_path = os.path.join(SKILLS_DIR, "foundation", base_file)
            if os.path.isfile(base_path) and base_file not in copied_files:
                shutil.copy2(base_path, os.path.join(pkg_dir, base_file))
                copied_files.append(base_file)

    # 5. Province-specific skill files
    province_source = os.path.join(canada_root, province_dir_name)
    province_skill_count = 0
    if os.path.isdir(province_source):
        for f in sorted(os.listdir(province_source)):
            if f.endswith(".md") and f != "README.md":
                shutil.copy2(os.path.join(province_source, f), os.path.join(pkg_dir, f))
                copied_files.append(f)
                province_skill_count += 1

    # 6. Core orchestrator files (Canada freelance intake + return assembly, global router)
    orch_dir = os.path.join(SKILLS_DIR, "orchestrator")
    for orch_file in ("ca-freelance-intake.md", "ca-return-assembly.md", "global-router.md"):
        src = os.path.join(orch_dir, orch_file)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(pkg_dir, orch_file))
            copied_files.append(orch_file)

    # 7. Generate README
    with open(os.path.join(pkg_dir, "README.md"), "w") as fh:
        fh.write(build_canada_province_readme(province_name, province_code, copied_files))
    copied_files.append("README.md")

    return {
        "jurisdiction": f"CA-{province_code.upper()}",
        "name": f"Canada — {province_name}",
        "package_dir": f"ca-{province_code}",
        "files": copied_files,
        "province_skills": province_skill_count,
        "has_orchestrator": True,
    }


def build_all_canada_packages():
    """Build packages for all 13 Canadian provinces and territories."""
    results = []
    for code in CA_PROVINCE_CODES:
        result = build_canada_province_package(code)
        results.append(result)
    return results


# Mirrors scripts/build-index.py's extract_frontmatter so the generator judges
# its output by the same rule its consumers do.
_FM_END_RE = re.compile(r"^(---|\.\.\.)\s*$", re.MULTILINE)


def _frontmatter_block(text):
    """Return the raw frontmatter block, or None when the file has none."""
    if not text.startswith("---"):
        return None
    first_nl = text.find("\n")
    if first_nl == -1 or text[:first_nl].strip() != "---":
        return None
    end = _FM_END_RE.search(text[first_nl + 1:])
    if not end:
        return None
    return text[first_nl + 1: first_nl + 1 + end.start()]


def validate_generated_frontmatter():
    """Fail closed on our own output.

    Nothing downstream re-checks this tree before it ships: build-index.py
    walks skills/ and the hand-authored packages/us-federal only, and
    sync-mcp.yml mirrors packages/** to the MCP repo on every push to main. A
    malformed block written here used to travel the whole way unchecked.
    """
    failures = []
    for dirpath, dirnames, filenames in os.walk(PACKAGES_DIR):
        dirnames.sort()
        for filename in sorted(filenames):
            if not filename.endswith(".md"):
                continue
            if filename.lower().startswith("readme"):
                continue
            path = os.path.join(dirpath, filename)
            rel = os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            block = _frontmatter_block(text)
            if block is None:
                if text.startswith("---"):
                    failures.append(f"{rel}: frontmatter opens with --- but never closes")
                continue
            try:
                load_frontmatter(block)
            except FrontmatterError as exc:
                failures.append(f"{rel}: invalid YAML frontmatter: {exc}")
    return failures


def main():
    us_only = "--us-only" in sys.argv

    if not us_only:
        # Clean packages directory — but NEVER remove hand-authored packages
        # (see HAND_AUTHORED_PACKAGES at the top of this file). A whole-dir
        # rmtree here previously deleted packages/us-federal, which has no
        # builder and cannot be regenerated.
        os.makedirs(PACKAGES_DIR, exist_ok=True)
        for entry in sorted(os.listdir(PACKAGES_DIR)):
            if entry in HAND_AUTHORED_PACKAGES:
                continue
            path = os.path.join(PACKAGES_DIR, entry)
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
    else:
        # Only clean US state packages
        os.makedirs(PACKAGES_DIR, exist_ok=True)
        for code in US_STATE_CODES:
            assert f"us-{code}" not in HAND_AUTHORED_PACKAGES, f"us-{code} is hand-authored"
            pkg = os.path.join(PACKAGES_DIR, f"us-{code}")
            if os.path.isdir(pkg):
                shutil.rmtree(pkg)

    # ---- International packages ----
    intl_results = []
    if not us_only:
        intl_dir = os.path.join(SKILLS_DIR, "international")
        for country_dir_name in sorted(os.listdir(intl_dir)):
            country_dir = os.path.join(intl_dir, country_dir_name)
            if not os.path.isdir(country_dir):
                continue
            if country_dir_name == "eu":
                continue  # EU is a regional layer, not a jurisdiction
            if country_dir_name == "canada":
                continue  # Canada is split into per-province packages (ca-{code}/), see build_all_canada_packages()

            result = build_package(country_dir_name, country_dir)
            if result:
                intl_results.append(result)

        full = [r for r in intl_results if r["has_orchestrator"]]
        multi = [r for r in intl_results if r["skill_count"] >= 3 and not r["has_orchestrator"]]
        single = [r for r in intl_results if r["skill_count"] < 3]
        with_bookkeeping = [r for r in intl_results if r.get("has_bookkeeping")]
        with_einvoice = [r for r in intl_results if r.get("has_einvoice")]
        with_payroll = [r for r in intl_results if r.get("has_payroll")]
        with_formation = [r for r in intl_results if r.get("has_formation")]
        with_fin_stmts = [r for r in intl_results if r.get("has_financial_statements")]
        with_tp = [r for r in intl_results if r.get("has_transfer_pricing")]
        with_tax_opt = [r for r in intl_results if r.get("has_tax_optimization")]
        with_crypto = [r for r in intl_results if r.get("has_crypto")]

        print(f"\nInternational packages built: {len(intl_results)}")
        print(f"  Full (with orchestrator): {len(full)} — {', '.join(r['name'] for r in full)}")
        print(f"  Multi-skill (3+ skills): {len(multi)}")
        print(f"  Single-skill (1-2 skills): {len(single)}")
        print(f"  With bookkeeping: {len(with_bookkeeping)}")
        print(f"  With e-invoicing: {len(with_einvoice)}")
        print(f"  With payroll: {len(with_payroll)}")
        print(f"  With company formation: {len(with_formation)}")
        print(f"  With financial statements: {len(with_fin_stmts)}")
        print(f"  With transfer pricing: {len(with_tp)}")
        print(f"  With tax optimization: {len(with_tax_opt)}")
        print(f"  With crypto tax: {len(with_crypto)}")

    # ---- Cross-border package ----
    xb_result = None
    if not us_only:
        xb_dir = os.path.join(SKILLS_DIR, "cross-border")
        if os.path.isdir(xb_dir):
            xb_pkg = os.path.join(PACKAGES_DIR, "_cross-border")
            os.makedirs(xb_pkg, exist_ok=True)
            xb_files = []
            # Copy top-level cross-border skills
            for f in sorted(os.listdir(xb_dir)):
                if f.endswith(".md"):
                    shutil.copy2(os.path.join(xb_dir, f), os.path.join(xb_pkg, f))
                    xb_files.append(f)
            # Copy treaty corridor files from subdirectory
            corridors_dir = os.path.join(xb_dir, "treaty-corridors")
            if os.path.isdir(corridors_dir):
                for f in sorted(os.listdir(corridors_dir)):
                    if f.endswith(".md"):
                        shutil.copy2(os.path.join(corridors_dir, f), os.path.join(xb_pkg, f))
                        xb_files.append(f)
            # Copy cross-border workflow base from foundation
            xb_base = os.path.join(SKILLS_DIR, "foundation", "cross-border-workflow-base.md")
            if os.path.isfile(xb_base):
                shutil.copy2(xb_base, os.path.join(xb_pkg, "cross-border-workflow-base.md"))
                xb_files.append("cross-border-workflow-base.md")
            if xb_files:
                with open(os.path.join(xb_pkg, "README.md"), "w") as fh:
                    fh.write("# Cross-Border Accounting Skills\n\n"
                             "Multi-jurisdiction orchestrator for international transactions: "
                             "tax residency, VAT place of supply, withholding tax treaties, "
                             "social security coordination, PE risk, transfer pricing, "
                             "cross-border payroll, and e-invoicing compliance.\n\n"
                             "These skills supplement country packages when a taxpayer "
                             "has cross-border activity. Load alongside the relevant "
                             "country packages for each jurisdiction involved.\n")
                xb_files.append("README.md")
                xb_result = {
                    "jurisdiction": "CROSS-BORDER",
                    "name": "Cross-Border",
                    "files": xb_files,
                    "has_orchestrator": True,
                    "skill_count": len(xb_files) - 1,
                }
                print(f"\nCross-border package built: {len(xb_files) - 1} skills")

    # ---- Industry verticals package ----
    vert_result = None
    if not us_only:
        vert_dir = os.path.join(SKILLS_DIR, "verticals")
        if os.path.isdir(vert_dir):
            vert_pkg = os.path.join(PACKAGES_DIR, "_verticals")
            os.makedirs(vert_pkg, exist_ok=True)
            vert_files = []
            for f in sorted(os.listdir(vert_dir)):
                if f.endswith(".md"):
                    shutil.copy2(os.path.join(vert_dir, f), os.path.join(vert_pkg, f))
                    vert_files.append(f)
            if vert_files:
                with open(os.path.join(vert_pkg, "README.md"), "w") as fh:
                    fh.write("# Industry Vertical Skills\n\n"
                             "Industry-specific accounting patterns for freelancers and small businesses.\n"
                             "Load alongside your country package for industry-aware tax classification.\n\n"
                             "Available verticals: " + ", ".join(f.replace('.md', '').replace('-', ' ').title() for f in vert_files) + "\n")
                vert_files.append("README.md")
                vert_result = {
                    "jurisdiction": "VERTICALS",
                    "name": "Industry Verticals",
                    "files": vert_files,
                    "has_orchestrator": False,
                    "skill_count": len(vert_files) - 1,
                }
                print(f"\nIndustry verticals package built: {len(vert_files) - 1} skills")

    # ---- Integrations package ----
    integ_result = None
    if not us_only:
        integ_dir = os.path.join(SKILLS_DIR, "integrations")
        if os.path.isdir(integ_dir):
            integ_pkg = os.path.join(PACKAGES_DIR, "_integrations")
            os.makedirs(integ_pkg, exist_ok=True)
            integ_files = []
            for f in sorted(os.listdir(integ_dir)):
                if f.endswith(".md"):
                    shutil.copy2(os.path.join(integ_dir, f), os.path.join(integ_pkg, f))
                    integ_files.append(f)
            if integ_files:
                with open(os.path.join(integ_pkg, "README.md"), "w") as fh:
                    fh.write("# Software & Platform Integration Skills\n\n"
                             "Column mappings, export formats, and reconciliation guides for popular\n"
                             "accounting software and payment platforms.\n\n"
                             "Load alongside your country package so the AI knows how to read your\n"
                             "Stripe CSV, Xero export, PayPal download, or bank statement format.\n")
                integ_files.append("README.md")
                integ_result = {
                    "jurisdiction": "INTEGRATIONS",
                    "name": "Software Integrations",
                    "files": integ_files,
                    "has_orchestrator": False,
                    "skill_count": len(integ_files) - 1,
                }
                print(f"\nIntegrations package built: {len(integ_files) - 1} skills")

    # ---- US state packages ----
    us_results = build_all_us_packages()

    no_state_skills = [r for r in us_results if r["state_skills"] == 0]
    with_income = [r for r in us_results if any("income-tax" in f for f in r["files"])]
    print(f"\nUS state packages built: {len(us_results)}")
    print(f"  With state income tax: {len(with_income)}")
    print(f"  No state-specific skills (federal only): {len(no_state_skills)}")
    if no_state_skills:
        print(f"    {', '.join(r['jurisdiction'] for r in no_state_skills)}")

    # ---- Canada province/territory packages ----
    ca_results = build_all_canada_packages()
    no_prov_skills = [r for r in ca_results if r["province_skills"] == 0]
    print(f"\nCanada province/territory packages built: {len(ca_results)}")
    print(f"  With province-specific skills: {len(ca_results) - len(no_prov_skills)}")
    if no_prov_skills:
        print(f"  No province-specific skills (federal only): {', '.join(r['jurisdiction'] for r in no_prov_skills)}")

    # Regenerate Canada index (packages/canada/README.md)
    ca_index_dir = os.path.join(PACKAGES_DIR, "canada")
    os.makedirs(ca_index_dir, exist_ok=True)
    with open(os.path.join(ca_index_dir, "README.md"), "w") as fh:
        rows = "\n".join(
            f"| {CA_PROVINCE_NAMES[c]} | `{c.upper()}` | [`packages/ca-{c}/`](../ca-{c}/) |"
            for c in CA_PROVINCE_CODES
        )
        fh.write(
            "# Canada — Tax Skills Index\n\n"
            "Pick your province or territory package below. Each package contains the\n"
            "federal Canadian tax skills (T1, T2125, CPP/EI, GST/HST, T1135, instalments,\n"
            "crypto, bookkeeping, payroll, formation, financial statements, transfer pricing,\n"
            "tax optimization) plus the province/territory-specific tax skill.\n\n"
            "| Province / Territory | Code | Package |\n"
            "|---|---|---|\n"
            f"{rows}\n\n"
            "See the repo [README](../../README.md) for upload instructions.\n"
        )

    # Regenerate US index (packages/us/README.md)
    us_index_dir = os.path.join(PACKAGES_DIR, "us")
    os.makedirs(us_index_dir, exist_ok=True)
    us_index_src = os.path.join(PACKAGES_DIR, "us", "README.md")
    # Preserve the existing index if present; it's maintained in the repo
    if not os.path.isfile(us_index_src):
        with open(us_index_src, "w") as fh:
            fh.write("# United States — Tax Skills Index\n\n"
                     "Pick your state package under `packages/us-[code]/`.\n"
                     "See the repo README for details.\n")

    # ---- Summary ----
    # NOTE: packages/manifest.json is DEPRECATED and no longer written. The
    # canonical machine-readable inventory is index.json at the repo root
    # (scripts/build-index.py; freshness enforced in CI by
    # scripts/validate-guides.py). Nothing consumed packages/manifest.json —
    # the MCP server indexes packages/**/*.md frontmatter directly.
    special_pkgs = [xb_result, vert_result, integ_result]
    all_results = intl_results + [r for r in special_pkgs if r] + us_results + ca_results

    print(f"\nTotal packages: {len(all_results)}")
    print("packages/manifest.json is deprecated and not written — index.json is the canonical inventory.")

    failures = validate_generated_frontmatter()
    if failures:
        print(f"\nERROR: {len(failures)} generated file(s) have invalid frontmatter:",
              file=sys.stderr)
        for failure in failures[:20]:
            print(f"  {failure}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  ... and {len(failures) - 20} more", file=sys.stderr)
        sys.exit(1)
    print("generated frontmatter validated")


if __name__ == "__main__":
    main()
