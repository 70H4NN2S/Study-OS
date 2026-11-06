#!/usr/bin/env python3
"""Compile a learner's C solution and run public examples. Not a grading or mastery tool."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISES = ROOT / "exercises" / "c"

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exercise", help="Exercise ID such as EX-0001")
    parser.add_argument("--cc", default=None, help="Compiler executable (default: cc)")
    parser.add_argument("--sanitize", action="store_true", help="Enable ASan/UBSan if compiler supports them")
    args = parser.parse_args()
    if not args.exercise.startswith("EX-") or not args.exercise[3:].isdigit():
        parser.error("exercise must look like EX-0001")
    number = int(args.exercise[3:])
    if number < 1 or number > 100:
        parser.error("exercise number must be between 1 and 100")
    matches = list(EXERCISES.glob(f"EX-{number:04d}-*"))
    if len(matches) != 1:
        print("Exercise directory not found or ambiguous.", file=sys.stderr)
        return 2
    work = matches[0]
    sources = sorted((work / "src").glob("*.c"))
    if not sources:
        print(f"No learner source under {work / 'src'}. Create it first.", file=sys.stderr)
        return 2
    compiler = args.cc or shutil.which("cc")
    if compiler is None:
        print("C compiler not installed.", file=sys.stderr)
        return 2
    flags = ["-std=c11", "-pedantic", "-D_XOPEN_SOURCE=700", "-Wall", "-Wextra", "-Werror", "-g", "-I" + str(work / "include")]
    if number >= 81:
        flags.append("-pthread")
    if args.sanitize:
        flags += ["-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
    cases_path = work / "tests" / "public_cases.json"
    with tempfile.TemporaryDirectory(prefix="study-os-c-") as tmp:
        exe = Path(tmp) / "app"
        build = subprocess.run([compiler, *flags, *map(str, sources), "-o", str(exe)], capture_output=True, text=True, timeout=60)
        if build.returncode != 0:
            print(build.stdout + build.stderr, file=sys.stderr)
            print("Compilation failed; not assessed.", file=sys.stderr)
            return 1
        print(f"Build successful: {args.exercise}")
        if not cases_path.is_file():
            print("No public executable cases: consult assignment tests.md requirements. Build success is not an exercise pass.")
            return 0
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
        failures = 0
        for i, case in enumerate(cases, 1):
            try:
                process = subprocess.run([str(exe)], input=case["stdin"], text=True, capture_output=True, timeout=5)
            except subprocess.TimeoutExpired:
                print(f"FAIL {i}: {case['name']} (timeout)")
                failures += 1
                continue
            ok = process.returncode == case["exit"] and process.stdout == case["stdout"]
            if ok:
                print(f"PASS {i}: {case['name']}")
            else:
                failures += 1
                print(f"FAIL {i}: {case['name']} -> exit={process.returncode}, stdout={process.stdout!r}")
                print(f"         expected exit={case['exit']}, stdout={case['stdout']!r}")
        print(f"Public examples: {len(cases)-failures}/{len(cases)} passed; independent review and novel tests still required.")
        return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
