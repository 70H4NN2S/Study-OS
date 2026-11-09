#!/usr/bin/env python3
"""Run published deterministic function cases for Study OS symmetric-crypto drills.

No student solutions are distributed in this repository. Each assignment supplies
its own src/main.py after the learner has implemented the stated functions.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "exercises" / "security"


def check_folder(folder: Path) -> tuple[int, int]:
    source = folder / "src" / "main.py"
    cases_file = folder / "tests" / "public_cases.json"
    if not source.is_file():
        print(f"{folder.name}: no submitted src/main.py (not tested)")
        return 0, 0
    spec = importlib.util.spec_from_file_location(
        f"crypto_{folder.name.replace('-', '_')}", source
    )
    if spec is None or spec.loader is None:
        print(f"{folder.name}: unable to import source")
        return 0, 1
    try:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cases = json.loads(cases_file.read_text(encoding="utf-8"))
    except Exception as error:
        print(f"{folder.name}: setup error: {type(error).__name__}: {error}")
        return 0, 1
    passed = failed = 0
    for index, case in enumerate(cases, 1):
        try:
            function = getattr(module, case["function"])
            actual = function(*case.get("args", []), **case.get("kwargs", {}))
            if "raises" in case:
                raise AssertionError(f"expected {case['raises']}, returned {actual!r}")
            if actual != case["expected"]:
                raise AssertionError(f"expected {case['expected']!r}, got {actual!r}")
        except Exception as error:
            if "raises" in case and type(error).__name__ == case["raises"]:
                passed += 1
                continue
            failed += 1
            print(f"FAIL {folder.name} #{index}: {type(error).__name__}: {error}")
        else:
            passed += 1
    print(f"{folder.name}: {passed} passed, {failed} failed")
    return passed, failed


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 tools/check_crypto.py EX-0125|all")
        return 2
    target = argv[1]
    folders = sorted(
        folder for folder in CATALOG.iterdir()
        if folder.is_dir() and (folder / "assignment.md").is_file()
    )
    if target != "all":
        folders = [folder for folder in folders if folder.name.startswith(target + "-")]
        if len(folders) != 1:
            print(f"Unknown or ambiguous exercise: {target}")
            return 2
    n_pass = n_fail = 0
    for folder in folders:
        passed, failed = check_folder(folder)
        n_pass += passed
        n_fail += failed
    print(f"Public cases: {n_pass} passed, {n_fail} failed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
