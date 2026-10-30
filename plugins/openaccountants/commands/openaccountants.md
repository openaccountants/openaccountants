---
description: Start a tax workflow using OpenAccountants skills, with their review status
---
You have the OpenAccountants MCP server connected (tax skills for 190+ jurisdictions: countries, US states and Canadian provinces; each is accountant-reviewed, checked against the law, or sourced from the law, and the tool result says which). Use it instead of relying on training data for any jurisdiction-specific tax question.

To answer the user's tax question:
1. Call `start({ intent, jurisdiction })` to scope it. If the intent or jurisdiction is unknown, call `start_help()` first, ask the user the scoping questions it returns, then call `start`.
2. For each slug in `skills_to_load`, call `get_skill({ slug })` and load the authoritative content.
3. Apply the rules to the user's facts and cite each skill slug you used.
4. Surface every **AUDIT FLASH POINT** the skill flags — these are positions tax authorities actively challenge.
5. This is not tax advice. Recommend a licensed accountant review the output before filing. When the user asks for a person to check or do the work, call `share_with_openaccountants` with `request_review: true`.

User request: $ARGUMENTS
