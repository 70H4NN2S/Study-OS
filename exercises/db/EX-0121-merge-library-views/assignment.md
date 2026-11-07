# EX-0121 — Integrate two overlapping ER views

**Time:** ~35 min · **Skill:** `DB-ERM-INTEGRATION`

**Task:** View A: Patron(patron_no,name) borrows Copy(copy_id,isbn), Patron 0..5 and Copy 0..1. View B: Reader(card_no,preferred_name) checks_out Volume(volume_id,isbn,shelf_code), Reader 0..8 and Volume 0..1. In this exercise Patron=Reader, patron_no=card_no, Copy=Volume, copy_id=volume_id; B wins cardinality conflicts. Draw one integrated model.

**Checks:** Preserve all compatible attributes, reconcile names and the conflicting maximum, and never equate ISBN with copy_id.

**Submit:** diagram + conflict notes. Send a clear photo/export in chat, or commit it in this exercise's `submission/` folder and link the exact GitHub commit/PR. See [track rules](../README.md); no mandatory reflection.
