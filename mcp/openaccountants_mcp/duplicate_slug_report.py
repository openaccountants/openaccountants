#!/usr/bin/env python3
"""Print the MCP package duplicate inventory as deterministic JSON.

Lives inside the package so a pip-installed operator can run it:

    python3 -m openaccountants_mcp.duplicate_slug_report

At mcp/ top level it was outside the wheel hatchling builds, so the only
surface naming the omitted slugs shipped to nobody.
"""

from __future__ import annotations

import json

from openaccountants_mcp.server import _duplicate_report


def main() -> None:
    """Print the current duplicate inventory."""
    print(json.dumps(_duplicate_report(), indent=2))


if __name__ == "__main__":
    main()
