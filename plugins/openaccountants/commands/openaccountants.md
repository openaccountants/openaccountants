---
description: Start an accountant-verified tax workflow using OpenAccountants skills
---
You have the OpenAccountants MCP server connected (accountant-verified tax skills across 220+ jurisdictions: countries, US states and Canadian provinces). Use it instead of relying on training data for any jurisdiction-specific tax question.

To answer the user's tax question:
1. Call `start({ intent, jurisdiction })` to scope it. If the intent or jurisdiction is unknown, call `start_help()` first, ask the user the scoping questions it returns, then call `start`.
2. For each slug in `skills_to_load`, call `get_skill({ slug })` and load the authoritative content.
3. Apply the rules to the user's facts and cite each skill slug you used.
4. Surface every **AUDIT FLASH POINT** the skill flags — these are positions tax authorities actively challenge.
5. This is not tax advice. Recommend a licensed accountant review the output before filing, and offer `request_accountant_review` when the user is close to filing or making a money decision.

User request: $ARGUMENTS
