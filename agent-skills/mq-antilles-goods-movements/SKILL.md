---
name: mq-antilles-goods-movements
description: "Martinique goods movements with Guadeloupe inside the single Antilles market (marche unique antillais) for octroi de mer, 2026. Covers which goods move without fresh customs clearance (locally produced or already released for consumption), the exclusion of goods under a suspensive regime, the accompanying document deposited on arrival, the monthly periodic declaration at the departure island's customs office by the tenth working day after the movement month and its contents, sales versus own-stock transfers, temporary round trips and the records to reconcile. Product rates and Guyane trade are out of scope. Trigger phrases include marche unique antillais, octroi de mer Martinique Guadeloupe, declaration periodique d'expedition, DEB octroi de mer, livraison Martinique Guadeloupe."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mq-antilles-goods-movements"
  jurisdiction: "MQ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Martinique: goods movements with Guadeloupe v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Year: 2026. Law: Loi n. 2004-639 on octroi de mer, art. 1 II ([Loi 2004-639, Legifrance](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/)); decree 2015-1077 art. 15 and the customs circular of 10 July 2025, chapter IX ([Circulaire octroi de mer](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf)).

## Scope

Guadeloupe and Martinique form the single Antilles territory for octroi under **article 1(II) of Law 2004-639**. This does not extend the same treatment to every Caribbean or overseas territory. [Law](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/).

The July 2025 customs circular, chapter IX, covers goods produced locally or already imported and released for consumption in one island, then sent to the other. These movements do not require fresh customs clearance. Goods remaining under a customs or fiscal suspensive regime are excluded from this treatment. Paragraph 110 nevertheless requires an accompanying document and a periodic declaration. [Circular paragraphs 108–110, printed page 47](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

## Ask the client first

1. Were the goods produced locally or imported and released for consumption in Martinique, or are they still under a suspensive regime?
2. Is the movement a sale, a transfer of own stock, or a temporary round trip?
3. Which month did the goods leave, and to whom (recipient SIRET)?
4. Commodity codes, origin, net mass, value and transport mode for each line.
5. Is a representative filing for the operator?

## The method, step by step

1. **Check the route qualifies.** Only goods produced locally or already released for consumption use the single-market route; goods under customs or fiscal suspension follow their own regime (paragraph 109) ([Circulaire, paras. 108 to 110](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf)).
2. **Prepare the accompanying document** and deposit it with the competent customs office on arrival in the destination DROM: for a sale, the prescribed invoice; without a sale, a copy of the import declaration or the invoice stamped by customs on import, the supplier's invoice, the excise accompanying document, or another document customs accepts (paragraph 112) ([Circulaire, para. 112](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf)).
3. **Link each dispatch** to its goods list, origin evidence, invoice or own-stock document, transport record and arrival record. A commercial invoice alone does not prove that goods still in a warehouse suspension have been released for consumption.
4. **File the monthly periodic declaration** at the departure island's customs office by the tenth working day after the movement month ([Circulaire, para. 113 and decree 2015-1077 art. 15 II](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf)).
5. **Reconcile** imported goods later dispatched separately from locally produced goods, and keep the filed declaration and arrival evidence.

### Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Single Antilles market | Martinique and Guadeloupe treated as one territory for octroi | Art. 1 II of the law | 2026 | [Loi 2004-639, art. 1](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/) |
| Periodic declaration | monthly, by the tenth working day after the movement month | Filed at the departure island's customs office | 2026 | [Circulaire, para. 113; decree 2015-1077 art. 15 II](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |
| Accompanying document | deposited on arrival in the destination DROM | Para. 112 | 2026 | same |
| Temporary round trip | value field optional | Simple round trips not treated as deliveries, marked as temporary on departure and return | 2026 | [Circulaire, para. 113 continuation](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Sale from Martinique to Guadeloupe | Single-market route; sale invoice as accompanying document; include in the monthly declaration. No fresh clearance does not mean no declaration | [Circulaire, paras. 109, 112 to 113](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |
| Transfer of own stock without a sale | Use the permitted no-sale evidence and include the dispatch; shipment versus delivery depends on whether ownership passes before entry | same |
| Temporary movement and return | Mark as temporary on departure and return; value optional; not for an actual sale | [Circulaire, para. 113](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |
| Goods still under suspension | Not the ordinary route; determine the governing customs or fiscal regime | [Circulaire, para. 109](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf) |
| Trade with Guyane | Outside the single market; the law has separate Guyane provisions | [Loi 2004-639](https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/) |

## Worked cases

**Case: October 2026 dispatches from Fort-de-France to Pointe-a-Pitre.** A wholesaler sends goods sold to a Guadeloupe customer (value 12,000 euros), transfers own stock to its Guadeloupe branch (value 3,500) and sends a display unit on a temporary round trip (value 800, optional on the declaration). The October declaration carries 12,000 + 3,500 = 15,500 of value lines, plus the temporary line. Due by the tenth working day of November 2026: counting Monday 2 November and skipping weekends and 11 November (Armistice Day), that is Monday 16 November 2026; check the local holiday calendar.

```oa-check
name: Martinique October 2026 dispatch declaration values
inputs:
  sale_value: 12000
  own_stock_value: 3500
  temporary_value: 800
steps:
  - declared_value: sale_value + own_stock_value
  - value_if_temporary_included: declared_value + temporary_value
expected:
  declared_value: 15500
  value_if_temporary_included: 16300
```

## When to refuse or refer

- Goods under a customs or fiscal suspensive regime: refer to customs.
- Excise goods, product rates and the annual payment under art. 39 of the law on imported goods dispatched: outside this skill.
- Trade with Guyane or other territories: refer.

## Filing and payment

Paragraph 113 requires the declaration at the **departure island's competent customs office by the tenth working day after the movement month**. The responsible economic operator, qualifying public entity or authorized representative dates and signs it. It records operator and representative identity, period, commodity code, origin, net mass and supplementary units where relevant, transport mode, recipient SIRET, value and signatory details. [Circular paragraph 113, page 48](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

Reconcile imported goods subsequently dispatched separately from locally produced goods as the paragraph requires. The circular's narrative calls the model annex VI, while its contents list calls the periodic declaration annex V. Locate the form by its title and confirm the current version with customs; do not rely on the inconsistent annex number. [Circular contents and paragraph 113](https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf).

## Completion checklist

- [ ] Route qualifies (local production or released for consumption).
- [ ] Accompanying document deposited on arrival.
- [ ] Monthly declaration filed at the departure office by the tenth working day.
- [ ] Sale, own-stock and temporary lines separated; imported and local goods reconciled.
- [ ] Arrival evidence, filed declaration and transport records kept.

## Sources

| Source | URL | Read on |
|---|---|---|
| Loi n. 2004-639 relative a l'octroi de mer, Legifrance, version in force on 14 November 2026: read for art. 1 II (marche unique antillais) and the Guyane provisions | https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000253374/LEGISCTA000006099294/ | 2026-11-14 |
| Direction generale des douanes, circulaire octroi de mer of 10 July 2025: read for chapter IX paras. 108 to 113 and decree 2015-1077 art. 15 II (monthly declaration, tenth working day, accompanying documents) | https://www.douane.gouv.fr/sites/default/files/2025-07/16/Circulaire-octroi-de-mer10072025.pdf | 2026-11-14 |

Not yet confirmed: the current version and annex number of the periodic declaration form (the circular calls it annex VI in the text and annex V in the contents); the submission channel; penalties; the exact working-day calendar customs applies.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mq-antilles-goods-movements` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mq-antilles-goods-movements. If neither is available, confirm every figure against the official source pages cited above before relying on it.
