#!/usr/bin/env python3
"""
Minimal smoke test for the OpenAccountants MCP server internals.

Run from the repo root (no extra dependencies needed beyond the package itself):

    python mcp/smoke_test.py

Exits 0 on success, 1 on failure.
"""

import sys
from pathlib import Path

# Ensure the package is importable when run from repo root without install
sys.path.insert(0, str(Path(__file__).resolve().parent))

from openaccountants_mcp.server import (
    PACKAGES_DIR,
    _safe_resolve,
    list_jurisdictions,
    list_files,
    get_file,
)

failures = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global failures
    status = "PASS" if condition else "FAIL"
    msg = f"  [{status}] {label}"
    if detail and not condition:
        msg += f"  -- {detail}"
    print(msg)
    if not condition:
        failures += 1


print(f"PACKAGES_DIR = {PACKAGES_DIR}\n")

# --- path safety ---------------------------------------------------------
print("Path safety:")
for bad in ["../../etc/passwd", "/etc/passwd", "../README.md"]:
    try:
        _safe_resolve(PACKAGES_DIR, bad)
        check(f"reject {bad!r}", False, "did NOT raise")
    except (ValueError, Exception):
        check(f"reject {bad!r}", True)

good = _safe_resolve(PACKAGES_DIR, "malta", "foundation.md")
check("accept malta/foundation.md", PACKAGES_DIR in good.parents or good == PACKAGES_DIR)

# --- list_jurisdictions ---------------------------------------------------
print("\nlist_jurisdictions:")
jurisdictions = list_jurisdictions()
check("returns a list", isinstance(jurisdictions, list))
check("contains 'malta'", "malta" in jurisdictions, f"got {jurisdictions[:5]}...")
check("contains 'uk'", "uk" in jurisdictions)
check(">100 jurisdictions", len(jurisdictions) > 100, f"got {len(jurisdictions)}")

# --- list_files -----------------------------------------------------------
print("\nlist_files('malta'):")
files = list_files("malta")
check("returns a list", isinstance(files, list))
check("contains foundation.md", "foundation.md" in files, f"got {files}")

try:
    list_files("../../../etc")
    check("reject traversal jurisdiction", False, "did NOT raise")
except (ValueError, Exception):
    check("reject traversal jurisdiction", True)

# --- get_file -------------------------------------------------------------
print("\nget_file('malta', 'foundation.md'):")
text = get_file("malta", "foundation.md")
check("returns a string", isinstance(text, str))
check("non-empty", len(text) > 100, f"length={len(text)}")

try:
    get_file("malta", "../../README.md")
    check("reject traversal filename", False, "did NOT raise")
except (ValueError, Exception):
    check("reject traversal filename", True)

# --- summary --------------------------------------------------------------
print()
if failures:
    print(f"FAILED — {failures} check(s) did not pass.")
    sys.exit(1)
else:
    print("ALL CHECKS PASSED.")
    sys.exit(0)
