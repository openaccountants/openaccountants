#!/usr/bin/env python3
"""
Pre-commit verification script for OpenAccountants contributors.

Runs the required repository checks locally before committing:
1. Guide frontmatter & quality tier validation (scripts/validate-guides.py --no-index-check)
2. Cross-guide contradiction scanner (scripts/detect-contradictions.py --all)
3. Full test suites (pytest tests/ and pytest mcp/tests)

Exit code:
  0 = All checks passed
  1 = One or more checks failed
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


# Ensure safe UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def run_step(description: str, cmd: list[str], env: dict[str, str] | None = None) -> bool:
    print(f"\n[CHECK] {description}...")
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    res = subprocess.run(cmd, cwd=str(REPO_ROOT), env=merged_env)
    if res.returncode != 0:
        print(f"  FAILED: {description} (exit code {res.returncode})")
        return False
    print(f"  PASSED: {description}")
    return True


def main() -> int:
    print("=" * 65)
    print("  OpenAccountants Pre-Commit Verification Pipeline")
    print("=" * 65)

    py_exe = sys.executable
    steps = [
        ("Validate Guide Metadata & Frontmatter", [py_exe, "scripts/validate-guides.py", "--no-index-check"], None),
        ("Cross-Guide Contradiction Detection", [py_exe, "scripts/detect-contradictions.py", "--all"], None),
        ("Core Test Suite", [py_exe, "-m", "pytest", "tests/"], None),
        ("MCP Server Test Suite", [py_exe, "-m", "pytest", "mcp/tests"], {"PYTHONPATH": "mcp"}),
    ]

    failed = 0
    for desc, cmd, env in steps:
        if not run_step(desc, cmd, env):
            failed += 1

    print("\n" + "=" * 65)
    if failed > 0:
        print(f"  ❌ Pre-commit checks FAILED ({failed} failed step(s)). Please fix before pushing.")
        print("=" * 65 + "\n")
        return 1

    print("  🎉 ALL PRE-COMMIT CHECKS PASSED!")
    print("=" * 65 + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
