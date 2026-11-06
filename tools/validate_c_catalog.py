#!/usr/bin/env python3
"""Check the proposed 100-exercise C catalog for structural completeness."""
import csv
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = root / "exercises" / "c"
assignments = list(catalog.glob("EX-*/assignment.md"))
expected = {f"EX-{n:04d}" for n in range(1, 101)}
found = {p.parent.name[:7] for p in assignments}
errors = []
if len(assignments) != 100 or found != expected:
    errors.append(f"Expected EX-0001..EX-0100 exactly once, got {len(assignments)} files.")
with (root / "curriculum" / "skills.csv").open(encoding="utf-8", newline="") as f:
    skill_ids = {row["skill_id"] for row in csv.DictReader(f)}
with (root / "state" / "assignments.csv").open(encoding="utf-8", newline="") as f:
    rows = [row for row in csv.DictReader(f) if row["topic"] == "C programming"]
if len(rows) != 100:
    errors.append(f"Expected 100 registered C assignments, got {len(rows)}.")
registered = {row["assignment_id"]: row["path"] for row in rows}
if set(registered) != expected:
    errors.append("Registered IDs differ from EX-0001..EX-0100.")
for p in assignments:
    identifier = p.parent.name[:7]
    relative = p.relative_to(root).as_posix()
    if registered.get(identifier) != relative:
        errors.append(f"{identifier}: registry path mismatch.")
    body = p.read_text(encoding="utf-8")
    for heading in ("## Assignment", "## Deliverables", "## Allowed help", "## Acceptance criteria", "## Verification"):
        if heading not in body:
            errors.append(f"{identifier}: missing {heading}")
    if not re.search(r"Rubric[^\n]*100", body):
        errors.append(f"{identifier}: missing 100-point rubric")
    skill_line = next((line for line in body.splitlines() if "**Target skills:**" in line), "")
    task_skills = set(re.findall(r"PROG-C-[A-Z-]+", skill_line))
    if not task_skills:
        errors.append(f"{identifier}: missing skill IDs")
    if not task_skills.issubset(skill_ids):
        errors.append(f"{identifier}: unknown skill IDs {task_skills - skill_ids}")
if errors:
    raise SystemExit("\n".join(errors))
print("C catalog: 100 assignments, registration, skills and required sections validated.")

if __name__ == "__main__":
    pass
