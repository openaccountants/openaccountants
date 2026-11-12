# Skill names and required companions

`depends_on` is a YAML list of exact frontmatter `name` values. Each target must
be a source skill in `skills/` or the hand-authored `packages/us-federal/` set.
The name is what `get_skill` loads. A similar filename or a matching country is
not proof that the required instructions exist or have the same scope.

`scripts/validate-guides.py` checks the whole source graph on every run, including
a PR that only deletes a parent. Missing or ambiguous names fail validation.
The test uses the source files, so a stale generated index cannot hide a break.
Documentation such as `README.md` and `references.md`, and authoring files in
`templates/` or `_templates/`, are not dependency targets or downloadable MCP
skill entries. They remain available as repository documents.

Two different documents cannot claim one name. Aliases must match both guidance
and parsed source metadata, including prerequisites, period, shape and approval.
The documented federal exception remains: a
hand-authored `packages/us-federal/` skill takes precedence over its matching
`skills/us/federal/` copy. Another country's skill cannot use that exception.

The package builder includes each declared dependency and its own dependencies
in the country, state, province or special bundle. The files retain the source
bytes. An occupied output filename is an error, not permission to overwrite
other guidance. The generated `foundation.md` is a compressed package helper;
declare `workflow-base` when a loadable universal method is required.

Source skills outside the historical bundle list are copied byte for byte into
`packages/_supplemental/`, with their own jurisdictions, scopes and approval
states. This includes global standards and methods and deeper treaty corridors.
The build fails if a named packaged copy does not match its source guidance and
jurisdiction. A reference to a consolidated Act is not a redirect instruction.

The income-tax and social-contributions method names are routing contracts.
They were once empty stubs removed in April 2026, while many country files kept
their dependencies. The restored routers load the universal method and require
the applicable country content. They contain no national tax values and claim
no professional approval.

Dependencies are prerequisites and cannot form a cycle. Intake comes before
return assembly; an intake's later handoff to assembly belongs in its body,
not as a backwards prerequisite. Validation rejects both self-dependencies and
loops through several skills.

Gabon income tax is `gabon-income-tax`; `ga-income-tax` remains US Georgia.
There is no global redirect between those names: an old Gabon request must be
updated with its known country and source path, never guessed from `ga`.

This check establishes that named instructions can be loaded. It does not
establish that a country's legal rules are complete or current, or that an
accountant has approved them. Those remain separate source and approval checks.
