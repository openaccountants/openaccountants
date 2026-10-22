#!/usr/bin/env python3
"""
Recompute the worked examples in skills.

A worked example that can be checked is written as a fenced block:

    ```oa-check
    name: Sole trader, profit EUR 40,000 (2026)
    inputs:
      profit: 40000
    steps:
      - band_15: (min(profit, 14500) - 9100) * 0.15
      - band_25: (min(profit, 19500) - 14500) * 0.25
      - band_35: (profit - 19500) * 0.35
      - tax: band_15 + band_25 + band_35
    expected:
      tax: 9235.00
    ```

Arithmetic only. Every step is `name: expression`; expressions may use the
inputs, earlier steps, numbers, + - * / ( ), unary minus, and the functions
min, max, round, abs, floor, ceil, pct (pct(x, 15) == x * 15 / 100) and
clamp(x, lo, hi). Decimal arithmetic; a result matches when it is within the
tolerance (default 0.01, override with `tolerance: 1` on the block).

Exit 1 if any expected value does not match or a block cannot be read.
A skill with no oa-check block passes; `--require` makes that a failure for
the tax domains listed in GOAL.md (files under skills/ whose slug contains a
tax token).

Usage:
    python3 scripts/check-examples.py                  # every skill
    python3 scripts/check-examples.py --changed-only   # files changed vs the base branch (CI)
    python3 scripts/check-examples.py path/to/skill.md
"""

import argparse
import ast
import math
import os
import re
import subprocess
import sys
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK_RE = re.compile(r"^```oa-check[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
TAX_TOKENS = ("income-tax", "corporate", "vat", "gst", "sales-tax", "payroll", "social", "ssc", "withholding", "transfer-pricing", "exit")


class CheckError(Exception):
    pass


def d(value):
    try:
        return Decimal(str(value))
    except InvalidOperation:
        raise CheckError(f"not a number: {value!r}")


FUNCS = {
    "min": lambda *a: min(a),
    "max": lambda *a: max(a),
    "abs": lambda a: abs(a),
    "round": lambda a, n=0: a.quantize(Decimal(1).scaleb(-int(n)), rounding=ROUND_HALF_UP),
    "floor": lambda a: Decimal(math.floor(a)),
    "ceil": lambda a: Decimal(math.ceil(a)),
    "pct": lambda a, p: a * d(p) / Decimal(100),
    "clamp": lambda a, lo, hi: max(lo, min(a, hi)),
}


def evaluate(expr, names):
    """Evaluate an arithmetic expression with Decimal, allowing only safe nodes."""
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        raise CheckError(f"cannot parse {expr!r}: {exc.msg}")

    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return d(node.value)
        if isinstance(node, ast.Name):
            if node.id not in names:
                raise CheckError(f"unknown name {node.id!r} in {expr!r}")
            return names[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            v = ev(node.operand)
            return -v if isinstance(node.op, ast.USub) else v
        if isinstance(node, ast.BinOp):
            left, right = ev(node.left), ev(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                if right == 0:
                    raise CheckError(f"division by zero in {expr!r}")
                return left / right
            raise CheckError(f"operator not allowed in {expr!r}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FUNCS:
            if node.keywords:
                raise CheckError(f"keyword arguments not allowed in {expr!r}")
            return FUNCS[node.func.id](*[ev(a) for a in node.args])
        raise CheckError(f"not allowed in {expr!r}: {type(node).__name__}")

    return ev(tree)


def parse_block(text):
    """Parse the tiny YAML subset used by oa-check blocks."""
    block = {"name": None, "inputs": {}, "steps": [], "expected": {}, "tolerance": Decimal("0.01")}
    section = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if not line.startswith((" ", "\t", "-")):
            key, _, value = line.partition(":")
            key, value = key.strip(), value.strip()
            if key in ("inputs", "steps", "expected"):
                section = key
            elif key == "name":
                block["name"] = value
                section = None
            elif key == "tolerance":
                block["tolerance"] = d(value)
                section = None
            else:
                raise CheckError(f"unknown key {key!r}")
            continue
        item = line.strip()
        if item.startswith("- "):
            item = item[2:]
        key, sep, value = item.partition(":")
        if not sep:
            raise CheckError(f"expected 'name: value', got {item!r}")
        key, value = key.strip(), value.strip()
        if section == "inputs":
            block["inputs"][key] = d(value.replace(",", ""))
        elif section == "steps":
            block["steps"].append((key, value))
        elif section == "expected":
            block["expected"][key] = d(value.replace(",", ""))
        else:
            raise CheckError(f"line outside a section: {item!r}")
    if not block["steps"] and not block["expected"]:
        raise CheckError("block has no steps or expected values")
    return block


def run_block(block):
    """Return a list of (name, expected, actual) mismatches; empty means pass."""
    names = dict(block["inputs"])
    for key, expr in block["steps"]:
        names[key] = evaluate(expr, names)
    mismatches = []
    for key, expected in block["expected"].items():
        if key not in names:
            raise CheckError(f"expected value {key!r} is not an input or step")
        actual = names[key]
        if abs(actual - expected) > block["tolerance"]:
            mismatches.append((key, expected, actual))
    return mismatches


def check_file(path):
    """Return (blocks_found, failures) for one file."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    failures = []
    found = 0
    for match in BLOCK_RE.finditer(text):
        found += 1
        label = f"{os.path.relpath(path, REPO_ROOT)} block {found}"
        try:
            block = parse_block(match.group(1))
            if block["name"]:
                label += f" ({block['name']})"
            for key, expected, actual in run_block(block):
                failures.append(f"{label}: {key} expected {expected} got {actual.quantize(Decimal('0.01'))}")
        except CheckError as exc:
            failures.append(f"{label}: {exc}")
    return found, failures


def changed_files():
    base = os.environ.get("BASE_REF", "main")
    out = subprocess.run(["git", "diff", "--name-only", f"origin/{base}...HEAD"], capture_output=True, text=True, cwd=REPO_ROOT)
    if out.returncode != 0:
        out = subprocess.run(["git", "diff", "--name-only", "HEAD~1"], capture_output=True, text=True, cwd=REPO_ROOT)
    return [os.path.join(REPO_ROOT, p) for p in out.stdout.split() if p.endswith(".md") and os.path.isfile(os.path.join(REPO_ROOT, p))]


def all_skill_files():
    paths = []
    for tree in ("skills", os.path.join("packages", "us-federal")):
        for dirpath, _dirs, files in os.walk(os.path.join(REPO_ROOT, tree)):
            for f in files:
                if f.endswith(".md") and not f.lower().startswith("readme"):
                    paths.append(os.path.join(dirpath, f))
    return sorted(paths)


def is_tax_skill(path):
    slug = os.path.splitext(os.path.basename(path))[0].lower()
    return path.replace(os.sep, "/").find("/skills/") != -1 and any(t in slug for t in TAX_TOKENS)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--changed-only", action="store_true")
    ap.add_argument("--require", action="store_true", help="fail tax skills that have no oa-check block")
    args = ap.parse_args(argv)

    if args.paths:
        files = [os.path.abspath(p) for p in args.paths]
    elif args.changed_only:
        files = changed_files()
    else:
        files = all_skill_files()

    total_blocks = 0
    failures = []
    missing = []
    for path in files:
        found, fails = check_file(path)
        total_blocks += found
        failures.extend(fails)
        if args.require and found == 0 and is_tax_skill(path):
            missing.append(os.path.relpath(path, REPO_ROOT))

    for line in failures:
        print("FAIL", line)
    for path in missing:
        print("MISSING", path, "(tax skill with no oa-check block)")
    print(f"checked {len(files)} files, {total_blocks} oa-check blocks, {len(failures)} failures, {len(missing)} missing")
    return 1 if failures or missing else 0


if __name__ == "__main__":
    sys.exit(main())
