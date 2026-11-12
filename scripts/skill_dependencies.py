"""Resolve source-owned skill names and dependencies before publication.

The source inventory is independent of stale generated packages/index.json.
The one precedence rule matches the Python MCP: hand-authored us-federal wins.
Every other repeated name must carry the same guidance and jurisdiction.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re

from frontmatter_yaml import FrontmatterError, load_frontmatter

FRONTMATTER = re.compile(r"\A---[ \t]*\n(.*?)^(?:---|\.\.\.)[ \t]*\n?(.*)\Z", re.M | re.S)
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


@dataclass(frozen=True)
class Skill:
    path: Path
    name: str
    jurisdiction: str
    body: str
    dependencies: tuple[str, ...]


def read_skill(path: Path) -> Skill | None:
    if path.name.lower().startswith("readme") or path.name.lower() == "references.md":
        return None  # package documentation, never an executable dependency
    if {"templates", "_templates"}.intersection(path.parts):
        return None  # authoring templates are not usable country guidance
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return None
    fm = load_frontmatter(match[1])
    if not fm.get("name"):
        return None  # documentation is not a dependency target
    name = fm["name"]
    if not isinstance(name, str) or not SLUG.fullmatch(name):
        raise ValueError(f"{path}: skill name must be a lowercase slug")
    deps = fm.get("depends_on") or []
    if not isinstance(deps, list) or any(not isinstance(d, str) or not SLUG.fullmatch(d) for d in deps):
        raise ValueError(f"{path}: depends_on must be a list of skill slugs")
    return Skill(path, name, str(fm.get("jurisdiction") or "").upper(), match[2], tuple(deps))


def select_target(name: str, candidates: list[Skill], root: Path) -> Skill:
    unique = {s.path: s for s in candidates}
    group = list(unique.values())
    if not group:
        raise ValueError(f"missing dependency `{name}`: no source skill has that name")
    federal = [s for s in group if s.path.is_relative_to(root / "packages/us-federal")]
    # Only the documented source/manual federal pair has this precedence.
    # Another country's document may not borrow a federal name to hide itself.
    if len(federal) == 1 and all(
        s is federal[0] or s.path.is_relative_to(root / "skills/us/federal") for s in group
    ):
        return federal[0]
    if len({(s.body, s.jurisdiction) for s in group}) == 1:
        return min(group, key=lambda s: s.path.as_posix())
    paths = ", ".join(str(s.path.relative_to(root)) for s in group)
    raise ValueError(f"ambiguous skill name `{name}`: different guidance or jurisdictions in {paths}")


def catalogue(root: Path) -> tuple[list[Skill], dict[str, Skill], list[str]]:
    skills, errors = [], []
    for tree in (root / "skills", root / "packages/us-federal"):
        for path in sorted(tree.rglob("*.md")):
            if path.name.lower().startswith("readme"):
                continue
            try:
                if skill := read_skill(path):
                    skills.append(skill)
            except (FrontmatterError, ValueError) as exc:
                errors.append(str(exc))
    names: dict[str, list[Skill]] = defaultdict(list)
    for skill in skills:
        names[skill.name].append(skill)
    resolved = {}
    for name, candidates in sorted(names.items()):
        try:
            resolved[name] = select_target(name, candidates, root)
        except ValueError as exc:
            errors.append(str(exc))
    for skill in skills:
        for dependency in skill.dependencies:
            if dependency not in resolved:
                errors.append(f"{skill.path.relative_to(root)}: missing or ambiguous dependency `{dependency}`")
    return skills, resolved, errors


def add_package_dependencies(package: Path, files: list[str], targets: dict[str, Skill]) -> None:
    """Copy the declared transitive closure into a generated package.

    Copy by the canonical skill name, so callers can load exactly depends_on.
    Existing files are retained; an occupied filename with other guidance fails.
    """
    queue = list(files)
    present = {}
    for filename in files:
        if skill := read_skill(package / filename):
            previous = present.get(skill.name)
            if previous and (previous.body, previous.jurisdiction) != (skill.body, skill.jurisdiction):
                raise ValueError(f"{package}: ambiguous skill name `{skill.name}`")
            present[skill.name] = skill
    visited = set()
    while queue:
        filename = queue.pop(0)
        skill = read_skill(package / filename)
        if not skill or skill.name in visited:
            continue
        visited.add(skill.name)
        for dependency in skill.dependencies:
            target = targets.get(dependency)
            if target is None:
                raise ValueError(f"{package / filename}: missing or ambiguous dependency `{dependency}`")
            if dependency in present:
                continue
            destination = package / f"{dependency}.md"
            if destination.exists():
                raise ValueError(f"{destination}: dependency would overwrite an existing file")
            destination.write_bytes(target.path.read_bytes())
            files.append(destination.name)
            queue.append(destination.name)
            present[dependency] = target
