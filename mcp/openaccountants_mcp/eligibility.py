"""Publication holds shared by repository builders and the installed MCP.

A source hold is not an unapproved-but-usable quality tier. Required companions
cannot be silently omitted: their dependents are held until the chain is usable.
This module has no SDK, YAML, filesystem or tax-domain dependencies.
"""

from collections.abc import Mapping
from typing import Any


def needs_sources(metadata: Mapping[str, Any]) -> bool:
    return str(metadata.get("status") or "").strip().lower() == "needs_sources"


def publication_holds(metadata: Mapping[str, Mapping[str, Any]]) -> dict[str, str]:
    """Return explicit reasons for direct holds and unavailable prerequisites."""
    held = {name: "status: needs_sources" for name, meta in metadata.items() if needs_sources(meta)}
    changed = True
    while changed:
        changed = False
        for name, meta in sorted(metadata.items()):
            if name in held:
                continue
            dependencies = meta.get("depends_on") or []
            if not isinstance(dependencies, list):
                held[name] = "depends_on is not a list"
                changed = True
                continue
            blocked = sorted(str(d) for d in dependencies if d not in metadata or d in held)
            if blocked:
                held[name] = "required companion unavailable: " + ", ".join(blocked)
                changed = True
    return dict(sorted(held.items()))
