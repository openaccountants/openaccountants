---
name: france-references
jurisdiction: FR
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# France — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## OpenFisca France

- Repository: [openfisca/openfisca-france](https://github.com/openfisca/openfisca-france)
- License: AGPL-3.0
- Language: French
- Stars: 296
- Scope: Complete model of the French tax and benefit system — income tax, social contributions, housing benefits, family benefits, and more. Encodes French fiscal law as executable Python code with a web API.
- Why it matters: This is the gold standard for rules-as-code in France. Maintained by a dedicated organisation, used by French government services, and covers far more than just income tax.
- Integration: Same license (AGPL-3.0). Content, formulas, parameter values, and test cases can be directly referenced or adapted with attribution.

## Calculette Impôts (DGFiP source code)

- Repository: [GouvernementFR/calculette-impots-m-source-code](https://github.com/GouvernementFR/calculette-impots-m-source-code)
- License: CeCILL 2.1 (GPL-compatible)
- Language: French (M language — DGFiP internal)
- Stars: ~58
- Scope: The actual source code used by the French tax authority (DGFiP) to compute income tax. Written in a custom "M" language.
- Why it matters: This is literally the government's own tax engine source code, published under an open license. It is the ultimate source of truth for how French income tax is actually calculated.
- Integration: CeCILL 2.1 is explicitly GPL-compatible, which flows into AGPL. Logic can be adapted with attribution.

## Calculette Impôts Python

- Repository: [openfisca/calculette-impots-python](https://github.com/openfisca/calculette-impots-python)
- License: AGPL-3.0
- Language: French / Python
- Stars: 9
- Scope: Python translation of the DGFiP M-language tax calculator.
- Why it matters: More readable than the raw M source. Useful as a bridge between the official logic and OpenAccountants skill format.
- Integration: AGPL-3.0. Directly compatible.
