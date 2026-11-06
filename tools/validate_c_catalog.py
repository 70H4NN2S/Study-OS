#!/usr/bin/env python3
"""Validate the 100 short C challenges and their public test contracts."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "exercises" / "c"
expected = {f"EX-{n:04d}" for n in range(1, 101)}
files = sorted(CATALOG.glob("EX-*/assignment.md"))
errors = []

with (ROOT / "curriculum/skills.csv").open(encoding="utf-8", newline="") as handle:
    known_skills = {row["skill_id"] for row in csv.DictReader(handle)}

with (ROOT / "state/assignments.csv").open(encoding="utf-8", newline="") as handle:
    rows = [row for row in csv.DictReader(handle) if row["topic"] == "C programming"]

registered = {row["assignment_id"]: row["path"] for row in rows}
if len(files) != 100 or {p.parent.name[:7] for p in files} != expected:
    errors.append("Exercise catalog must contain exactly EX-0001..EX-0100")
if len(rows) != 100 or len(registered) != 100 or set(registered) != expected:
    errors.append("Study OS registry must contain 100 unique C assignments")

for path in files:
    exercise_id = path.parent.name[:7]
    if registered.get(exercise_id) != path.relative_to(ROOT).as_posix():
        errors.append(f"{exercise_id}: registry path mismatch")
    body = path.read_text(encoding="utf-8")
    for marker in ("**Time:**", "**Skill:**", "**Task:**", "**Cases (stdin → stdout):**", "**Rules:**", "**Submit:**"):
        if marker not in body:
            errors.append(f"{exercise_id}: missing {marker}")
    t = re.search(r"\*\*Time:\*\* ~([0-9]+) min", body)
    if not t or not 5 <= int(t.group(1)) <= 60:
        errors.append(f"{exercise_id}: time outside 5–60 minutes")
    skill = re.search(r"\*\*Skill:\*\* `(PROG-C-[A-Z-]+)`", body)
    if not skill or skill.group(1) not in known_skills:
        errors.append(f"{exercise_id}: missing or unregistered skill")
    if len(body.split()) > 180:
        errors.append(f"{exercise_id}: description too long for microchallenge")
    cases_file = path.parent / "tests" / "public_cases.json"
    if not cases_file.is_file():
        errors.append(f"{exercise_id}: public cases missing")
        continue
    try:
        cases = json.loads(cases_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as err:
        errors.append(f"{exercise_id}: invalid JSON: {err}")
        continue
    if not isinstance(cases, list) or not (1 <= len(cases) <= 3):
        errors.append(f"{exercise_id}: expected 1–3 concrete public cases")
        continue
    for i, case in enumerate(cases, 1):
        if not isinstance(case, dict):
            errors.append(f"{exercise_id} case {i}: invalid object")
            continue
        if not isinstance(case.get("stdin"), str) or not isinstance(case.get("stdout"), str) or type(case.get("exit")) is not int:
            errors.append(f"{exercise_id} case {i}: expected exact stdin/stdout strings and integer exit code")
            continue
        # Ensure the prose example matches the executable test case.
        shown = "`" + json.dumps(case["stdin"], ensure_ascii=False) + "` → `" + json.dumps(case["stdout"], ensure_ascii=False) + "`"
        if shown not in body:
            errors.append(f"{exercise_id} case {i}: assignment and public case differ")

if errors:
    raise SystemExit("\n".join(errors))
print("C microchallenges validated: 100 registered tasks, 5–60 min, each with exact public cases.")
