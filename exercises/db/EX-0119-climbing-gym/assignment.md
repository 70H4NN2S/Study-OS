# EX-0119 — Design a complete ER diagram

**Time:** ~35 min · **Skill:** `DB-ER-CHEN`

**Task:** ClimbingGym tracks Member(member_id,name,one or more emergency_phones), Route(route_id,grade), Coach(coach_id,name), and Session(session_id,date,completion_status), where every stated ID is unique. Each Session has exactly one Member, Route and Coach. Members, Routes and Coaches may participate in 0..* Sessions. Draw a complete Chen model with keys and cardinalities.

**Checks:** Explain where completion_status belongs and why extra relationships are unnecessary.

**Submit:** diagram + one sentence. Send a clear photo/export in chat, or commit it in this exercise's `submission/` folder and link the exact GitHub commit/PR. See [track rules](../README.md); no mandatory reflection.
