---
jurisdiction: "NO"
version: 0.5
last_updated: 2026-10-30
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  XB: no-individual-residence
partial:
  IT-IND: "no-income-tax covers self-employed (enkeltpersonforetak) income only; employees, pensioners, investment income and wealth tax are not computed, and it is not yet in the deep-tax shape"
  SC: "no-social-contributions covers the self-employed rate; employee and employer contributions are in no-employer-payroll, and the skill is not yet in the deep-tax shape"
  VAT: "no-vat-return and norway-mva are duplicates in the older shape with no penalties or cross-border sections"
---

# Norway: tax pack

Calendar income year. Authority: Skatteetaten (skatteetaten.no); statutes on lovdata.no; yearly rates in the Storting's tax decision (Stortingets skattevedtak) and contribution decision. Currency: Norwegian kroner (NOK). Individuals pay 22% on ordinary income plus bracket tax and national insurance contribution on personal income, and wealth tax; companies pay 22%. VAT (merverdiavgift, MVA) is Norwegian law, not the EU directive.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | no-income-tax, no-capital-gains | sourced from the law |
| IT-CORP, corporate income tax | no-corporate-income-tax | checked against the law |
| VAT | no-vat-return, norway-mva (duplicates) | sourced from the law |
| SC, social contributions | no-social-contributions | sourced from the law |
| PR, payroll withholding | no-employer-payroll | checked against the law |
| TP, transfer pricing | no-transfer-pricing | checked against the law |
| XB, cross-border | no-individual-residence, norway-to-switzerland-wealth-tax-exit (tax year 2025) | checked against the law (no-individual-residence) |

Also in the pack: no-tax-overview and no-company-formation (both tax year 2025).

## Official sources

- Skatteloven (lov 1999-03-26-14): https://lovdata.no/dokument/NL/lov/1999-03-26-14 (read 2026-10-30)
- Skatteforvaltningsloven (lov 2016-05-27-14) and skatteforvaltningsforskriften (forskrift 2016-11-23-1360): https://lovdata.no/dokument/NL/lov/2016-05-27-14 (read 2026-10-30)
- Skattebetalingsloven (lov 2005-06-17-67) and skattebetalingsforskriften (forskrift 2007-12-21-1766): https://lovdata.no/dokument/NL/lov/2005-06-17-67 (read 2026-10-30)
- A-opplysningsloven (lov 2012-06-22-43) and a-opplysningsforskriften (forskrift 2014-06-24-857): https://lovdata.no/dokument/NL/lov/2012-06-22-43 (read 2026-10-30)
- Skatteetaten, Forskuddsutskrivingen 2026: https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ (read 2026-10-30)
- Skattedirektoratet, Arbeidsgiveravgift til folketrygden for 2026: https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/ (read 2026-10-30)
