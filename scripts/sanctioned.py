"""The countries this repository does not cover, read from scripts/data/sanctioned.yml.

One reader for every script that needs the list: validate-guides.py (the guard),
coverage-report.py and build-country-index.py (shown as "Not covered (sanctioned)").
"""

import json
import os
import re

import yaml

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPTS_DIR, "data", "sanctioned.yml")

#: Top-level folders a sanctioned country may not appear under.
GUARDED_ROOTS = ("skills/", "library/", "evidence/")

_JURISDICTION_LINE = re.compile(r"^jurisdiction:[ \t]*[\"']?([^\"'\n#]*)", re.MULTILINE)
_cache = None


def load(path=DATA_PATH):
    """The parsed data file: ``decided_on``, ``decided_by``, ``countries``, ``stay_live``."""
    global _cache
    if path == DATA_PATH and _cache is not None:
        return _cache
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    countries = data.get("countries") if isinstance(data, dict) else None
    if not countries or not all(isinstance(c, dict) and c.get("code") and c.get("folder") for c in countries):
        raise ValueError(f"{path}: every entry under countries needs a code and a folder")
    if path == DATA_PATH:
        _cache = data
    return data


def countries():
    return load()["countries"]


def codes():
    return {c["code"].upper() for c in countries()}


def folders():
    return {c["folder"].lower(): c for c in countries()}


def by_code():
    return {c["code"].upper(): c for c in countries()}


def label(country):
    return f"{country['name']} ({country['code']})"


def country_for_path(rel):
    """The sanctioned country a repository path sits in, or None.

    A path counts when any folder under skills/, library/ or evidence/ is the
    country's folder (skills/iran/x.md, library/iran/figures.json), and under
    evidence/ also when a folder starts with it (evidence/research/belarus-2026/).
    Case-insensitive, so skills/Iran/ is caught too.
    """
    rel = rel.replace("\\", "/").lstrip("./")
    if not rel.lower().startswith(GUARDED_ROOTS):
        return None
    table = folders()
    parts = [p.lower() for p in rel.split("/")[1:-1]]
    for part in parts:
        if part in table:
            return table[part]
        if rel.lower().startswith("evidence/"):
            for folder, country in table.items():
                if part.startswith(folder + "-"):
                    return country
    return None


def _jurisdiction_values(value):
    if isinstance(value, (list, tuple)):
        out = []
        for item in value:
            out.extend(_jurisdiction_values(item))
        return out
    if value is None:
        return []
    return [str(value)]


def country_for_jurisdiction(value):
    """The sanctioned country a ``jurisdiction`` value names (RU, ru, RU-MOW, [DE, IR]), or None."""
    table = by_code()
    for raw in _jurisdiction_values(value):
        for token in re.split(r"[^A-Za-z0-9-]+", raw):
            base = token.split("-")[0].upper()
            if base in table:
                return table[base]
    return None


def jurisdiction_in_text(rel, text):
    """The ``jurisdiction`` a skill or library file declares, or None.

    Markdown: the frontmatter key (the strict reader first, then the plain line, so
    a malformed block cannot hide it). JSON: a top-level ``jurisdiction`` key.
    """
    if rel.endswith(".json"):
        try:
            data = json.loads(text)
        except ValueError:
            return None
        return data.get("jurisdiction") if isinstance(data, dict) else None
    if not rel.endswith(".md"):
        return None
    import skill_checks  # loaded here: it pulls in build-index.py

    value = skill_checks.read_frontmatter(text).get("jurisdiction")
    if value is None:
        match = _JURISDICTION_LINE.search(text[:5000])
        value = match.group(1).strip() if match else None
    return value


def problem(rel, text):
    """A plain message when ``rel`` is a sanctioned-country file, else None."""
    country = country_for_path(rel)
    reason = "its folder"
    if country is None and rel.startswith(("skills/", "library/")) and text is not None:
        country = country_for_jurisdiction(jurisdiction_in_text(rel, text))
        reason = "its jurisdiction"
    if country is None:
        return None
    data = load()
    return (
        f"{rel}: {label(country)} is a sanctioned country ({reason}). This repository does not "
        f"cover it: no skill, library or evidence file is accepted for "
        f"{', '.join(c['name'] for c in countries())}. Remove this file from the pull request. "
        f"List: scripts/data/sanctioned.yml ({data.get('decided_by')})."
    )
