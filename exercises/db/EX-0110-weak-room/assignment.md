# EX-0110 — Identify a weak entity

**Time:** ~20 min · **Skill:** `DB-ERM-WEAK`

**Task:** CampusBuilding has unique building_id and may have zero Rooms. Every Room belongs to one building; room_no is unique only inside its building. Room also has seats. Model weak identity and the identifying relationship in Chen.

**Checks:** Specify how a single room is identified campus-wide; explain why room_no alone fails.

**Submit:** diagram + key expression. Send a clear photo/export in chat, or commit it in this exercise's `submission/` folder and link the exact GitHub commit/PR. See [track rules](../README.md); no mandatory reflection.
