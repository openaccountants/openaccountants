"""Where things live under skills/. One place, so no script guesses.

skills/<country>/   one folder per country (skills/eu is the EU layer, same level)
skills/us/          federal/, states/<code>/ and a few national files at its top
skills/<topic>/     the shared folders named in TOPIC_DIRS
"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

TOPIC_DIRS = frozenset({
    "cross-border", "financial-reporting", "foundation", "integrations", "intelligence",
    "orchestrator", "patterns", "templates", "verticals",
})


def country_dirs(skills: Path = SKILLS) -> list[Path]:
    """Every country folder, skills/us and skills/eu included, sorted by name."""
    return sorted(p for p in skills.iterdir() if p.is_dir() and p.name not in TOPIC_DIRS)


def is_country_path(rel: str) -> bool:
    """True for a repo-relative file inside a country folder."""
    parts = rel.split("/")
    return len(parts) >= 3 and parts[0] == "skills" and parts[1] not in TOPIC_DIRS


def pure_moves(name_status: str) -> set[str]:
    """New paths of files moved with no change and the same filename, from
    `git diff --name-status -M100%`. Moving a file is not editing it, so the gates
    for changed skills skip these. A rename to a new filename changes the slug: it counts."""
    moved = set()
    for line in name_status.splitlines():
        fields = line.split("\t")
        if len(fields) == 3 and fields[0] == "R100" and os.path.basename(fields[1]) == os.path.basename(fields[2]):
            moved.add(fields[2])
    return moved
