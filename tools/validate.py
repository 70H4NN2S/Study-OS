#!/usr/bin/env python3
"""Basic dependency-free Study OS registry checks."""
from pathlib import Path
import csv
import sys

root = Path(__file__).resolve().parents[1]
columns = {
 "curriculum/skills.csv": ["skill_id","domain","topic","skill","prerequisites","status"],
 "state/skills.csv": ["skill_id","mastery","last_assessed","confidence","evidence_ref","notes"],
 "state/assessments.csv": ["assessment_id","date","assignment_id","skill_id","score_percent","mastery_observation","help_level","evidence_ref","feedback_ref","notes"],
 "state/reviews.csv": ["review_id","skill_id","last_attempt","next_due","interval_days","reason","status","evidence_ref"],
 "state/assignments.csv": ["assignment_id","path","kind","topic","created_date","status","submission_ref"],
}
errors = []
data = {}
for name, headers in columns.items():
    with (root / name).open(encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != headers:
            errors.append(f"{name}: unexpected CSV headers")
        data[name] = list(reader)
ids = [r["skill_id"] for r in data["curriculum/skills.csv"]]
if len(ids) != len(set(ids)): errors.append("Duplicate skill IDs")
known = set(ids)
for name in ("state/skills.csv","state/assessments.csv","state/reviews.csv"):
    for row in data[name]:
        if row["skill_id"] not in known: errors.append(f"{name}: unknown skill {row['skill_id']}")
for row in data["state/skills.csv"]:
    if row["mastery"] not in ("U","0","1","2","3","4"):
        errors.append(f"Invalid mastery for {row['skill_id']}")
assignments = data["state/assignments.csv"]
if len({r["assignment_id"] for r in assignments}) != len(assignments): errors.append("Duplicate assignment IDs")
for row in assignments:
    if not (root / row["path"]).is_file(): errors.append(f"Missing assignment {row['path']}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("Study OS validation passed")
