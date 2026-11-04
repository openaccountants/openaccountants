# OpenAccountants for Hermes

The OpenAccountants tax library as a portable Agent Plugin (agent-plugins.org
v1), which Hermes loads natively: 2,100+ jurisdiction tax skills (countries,
US states, cross-border, verticals) register as plugin skills, and the hosted
OpenAccountants connector ships as the package's MCP server.

## What installs

- `skills/` — the full library, one folder per skill with a `SKILL.md`.
  Built from `skills/**` by `scripts/build-agent-skills.py`; never edit here.
- `mcp.json` — the connector at https://www.openaccountants.com/api/mcp
  (streamable-http). Hermes registers it as `openaccountants` when the plugin
  is enabled.

Skills register read-only as `openaccountants:<slug>`: listed by `skills_list`
and readable by `skill_view()`, not copied into `~/.hermes/skills/`.

## Disclosure

- Network calls: the OpenAccountants connector (hosted at
  https://www.openaccountants.com/api/mcp) when the plugin is enabled.
- Shell commands: none. Writes: none at runtime. Credentials: none required.

## Install (Hermes)

Copy this folder to `~/.hermes/plugins/openaccountants/`, then
`hermes plugins enable openaccountants`.
