# EX-0003 — Clock formatter

**Time:** ~10 min · **Skill:** `PROG-C-TYPES`

**Task:** Read nonnegative total seconds; print `HH:MM:SS`.

**Cases (stdin → stdout):** `"3661\n"` → `"01:01:01\n"` · `"90061\n"` → `"25:01:01\n"`

**Rules:** Hours may exceed 24; minutes/seconds are two digits.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0003`.
