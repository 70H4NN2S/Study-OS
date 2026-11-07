# EX-0114 — Identify rules ER cannot encode

**Time:** ~25 min · **Skill:** `DB-ERM-INTEGRITY`

**Task:** Scooter rental tracks Rider(rider_id), Scooter(scooter_id, battery_percent), Reservation(reservation_id,start_time,end_time). Every Reservation has one Rider and one Scooter; either may have 0..* Reservations. Draw Chen. Then classify constraints: battery_percent 0..100; start_time < end_time; no overlapping reservations on one Scooter.

**Checks:** Which constraints are expressible via Chen min–max, and which require supplementary enforcement?

**Submit:** diagram + short constraint note. Send a clear photo/export in chat, or commit it in this exercise's `submission/` folder and link the exact GitHub commit/PR. See [track rules](../README.md); no mandatory reflection.
