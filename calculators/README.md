# Calculators

Small, open decision checks built on the skills in this repository. A skill is written for an AI; a calculator takes a person's own numbers and answers one question. The hosted versions live at openaccountants.com/tools; the logic lives here so anyone can read it, test it or embed it.

Each calculator is a folder with:

- `rules.json`: the figures it uses, each with its legal basis, its official source and the date they were checked (`as_of`).
- `index.mjs`: one pure function. No network, no clock, no tracking. Node 20+ (JSON import attributes).
- `index.test.mjs`: `node --test calculators/<name>/`.
- `README.md`: the question, the inputs, the outputs, what it does not cover.

| Calculator | Question | Skills behind it |
|---|---|---|
| [`eu-vat-registration`](eu-vat-registration/) | I sell to customers in other EU countries. Do I have to register for VAT elsewhere, and whose VAT do I charge? | `eu-oss-digital`, `cross-border-vat-gst`, `eu-reverse-charge` |

Results are estimates from the rules in `rules.json`, not advice on anyone's situation. The nightly source watch on openaccountants.com checks the official pages each calculator cites; when a figure moves, `rules.json` is updated here and the hosted page follows.

Licence: the code is AGPL-3.0-or-later; the figures and wording in `rules.json` are under the OpenAccountants Guide License v1.0, like the skills.
