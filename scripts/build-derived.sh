#!/usr/bin/env bash
# Rebuild every derived tree from skills/**, in the order the builders need.
#
# One list, two callers:
#   .github/workflows/rebuild-derived.yml  runs it on main and opens the bot PR
#   .github/workflows/validate.yml         runs it on that PR to prove the files
#                                          are exactly what this script produces
#
# Writes: packages/** (not us-federal), index.json, llms.txt (counts line),
# llms-full.txt, agent-skills/**, plugins/openaccountants/skills/**, skills/COUNTRIES.md.
# Under skills/, writes only the generated COUNTRIES.md, never Guide sources.
#
# Usage: scripts/build-derived.sh [REF...]
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/build-country-index.py
python3 scripts/build-packages.py
python3 scripts/build-index.py
python3 scripts/build-llms-full.py
python3 scripts/build-agent-skills.py --plugin MT,NL,DE,IE,GB

# index.json carries a build timestamp. If nothing else in it changed, keep a
# committed copy (HEAD's, or that of any REF given, such as the bot branch), so
# a rebuild of unchanged skills is no change at all.
python3 - HEAD "$@" <<'PY'
import json, subprocess, sys

def without_stamp(text):
    data = json.loads(text)
    data.pop("generated_at", None)
    return data

new = without_stamp(open("index.json", encoding="utf-8").read())
for ref in sys.argv[1:]:
    old = subprocess.run(["git", "show", f"{ref}:index.json"], capture_output=True, text=True)
    if old.returncode == 0 and without_stamp(old.stdout) == new:
        with open("index.json", "w", encoding="utf-8") as fh:
            fh.write(old.stdout)
        break
PY

if [ -n "$(git status --porcelain -- skills/ ':(exclude)skills/COUNTRIES.md')" ]; then
  echo "::error::Hand-authored skills/ changed during the build. Only generated COUNTRIES.md may change." >&2
  git status --porcelain -- skills/ ':(exclude)skills/COUNTRIES.md' | head -20 >&2
  exit 1
fi
