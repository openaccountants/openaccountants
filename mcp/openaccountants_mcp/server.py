"""
OpenAccountants MCP server.

Exposes read-only tools that let an MCP client (Claude Desktop, Cursor, etc.)
discover and fetch tax-skill markdown from the ``packages/`` tree.

Environment
-----------
OPENACCOUNTANTS_ROOT  Path to the repo checkout.  Defaults to two directories
                      above this file (i.e. the repo root when this package
                      lives at ``mcp/openaccountants_mcp/``).
"""

from __future__ import annotations

import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Resolve repo root + packages directory
# ---------------------------------------------------------------------------

_DEFAULT_ROOT = Path(__file__).resolve().parents[2]  # mcp/openaccountants_mcp/ -> mcp/ -> repo
REPO_ROOT = Path(os.environ.get("OPENACCOUNTANTS_ROOT", str(_DEFAULT_ROOT))).resolve()
PACKAGES_DIR = REPO_ROOT / "packages"

MAX_FILE_BYTES = 2 * 1024 * 1024  # 2 MB safety cap

# ---------------------------------------------------------------------------
# Path safety
# ---------------------------------------------------------------------------


def _safe_resolve(packages_dir: Path, *segments: str) -> Path:
    """Resolve *segments* under *packages_dir* and reject escapes."""
    joined = packages_dir.joinpath(*segments).resolve()
    # Python 3.9+ has is_relative_to; fall back for safety
    try:
        joined.relative_to(packages_dir)
    except ValueError:
        raise ValueError(f"Path escapes allowed root: {joined}")
    return joined


# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    "OpenAccountants",
    instructions=(
        "Read-only access to OpenAccountants tax-skill packages. "
        "Use list_jurisdictions to discover countries, list_files to see "
        "a country's skill files, and get_file to read one."
    ),
)


@mcp.tool()
def list_jurisdictions() -> list[str]:
    """List available country/jurisdiction slugs under packages/.

    Returns directory names that contain at least one .md file
    (i.e. look like a real skill package, not an empty placeholder).
    """
    if not PACKAGES_DIR.is_dir():
        return []
    return sorted(
        d.name
        for d in PACKAGES_DIR.iterdir()
        if d.is_dir() and any(d.glob("*.md"))
    )


@mcp.tool()
def list_files(jurisdiction: str) -> list[str]:
    """List .md (and .json) skill files for a jurisdiction.

    Args:
        jurisdiction: Country slug exactly as returned by list_jurisdictions
                      (e.g. "malta", "uk", "germany").

    Returns:
        Sorted list of filenames inside packages/<jurisdiction>/.
    """
    jdir = _safe_resolve(PACKAGES_DIR, jurisdiction)
    if not jdir.is_dir():
        raise ValueError(f"Unknown jurisdiction: {jurisdiction}")
    return sorted(
        f.name
        for f in jdir.iterdir()
        if f.is_file() and f.suffix in {".md", ".json"}
    )


@mcp.tool()
def get_file(jurisdiction: str, filename: str) -> str:
    """Read one skill file and return its UTF-8 text.

    Args:
        jurisdiction: Country slug (e.g. "malta").
        filename:     File inside that package (e.g. "foundation.md").

    Returns:
        The full file contents as a string (capped at 2 MB).
    """
    fpath = _safe_resolve(PACKAGES_DIR, jurisdiction, filename)
    if not fpath.is_file():
        raise ValueError(f"File not found: {jurisdiction}/{filename}")
    size = fpath.stat().st_size
    if size > MAX_FILE_BYTES:
        raise ValueError(
            f"File too large ({size:,} bytes, limit {MAX_FILE_BYTES:,})"
        )
    return fpath.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the stdio MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
