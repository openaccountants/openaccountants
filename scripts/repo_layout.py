"""Where things live under skills/. One place, so no script guesses.

skills/<country>/   one folder per country (skills/eu is the EU layer, same level)
skills/us/          federal/, states/<code>/ and a few national files at its top
skills/<topic>/     the shared folders named in TOPIC_DIRS
"""

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
