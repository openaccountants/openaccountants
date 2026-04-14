# Changelog

All notable changes to OpenAccountants will be documented in this file.

## [1.0.0] — 2026-04-14

### The initial release

**371 tax skills across 134 countries.** Upload to any LLM with your bank statement.

#### Skills
- 185 consumption tax skills (VAT/GST/sales tax) — verified against tax authority websites
- 45 income tax skills — brackets, deductions, transaction pattern libraries
- 50 social contribution skills — SSC/NIC/pension/health with payment pattern libraries
- 14 estimated tax skills — advance payments, provisional tax, quarterly instalments
- 5 cross-border skills — reverse charge, withholding tax matrix, PE risk, OSS, exports
- 5 transaction pattern files — 120+ global vendor patterns for instant classification
- 3 intelligence skills — deadline engine, threshold alerts, optimisation advisor

#### End-to-end jurisdictions
Complete guided experience (intake → classification → computation → assembly → review):
Malta, United Kingdom, Germany, Australia, Canada, India, Spain, United States (California)

#### Architecture
- Per-jurisdiction packages in `packages/` — self-contained, upload to any LLM
- Universal foundation + intake (same for every country)
- Country-specific content skills with local supplier/transaction pattern libraries
- Malta v2.0 structure: tiers as sections (Classified/Assumed/Needs Input), not inline tags
- Build script generates packages from source skills

#### Quality
- Q1 (battle-tested): Malta VAT/IT/SSC, Germany VAT, US federal bookkeeping/SE
- Q2 (research-verified): ~200 skills verified against tax authority websites
- Deep research caught 200+ errors across 100+ countries during verification
