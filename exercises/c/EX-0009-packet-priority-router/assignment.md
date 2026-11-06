# EX-0009 — Packet priority router

**Time:** ~8 min · **Skill:** `PROG-C-CONTROL`

**Task:** Read integer code 0..3; print `drop`, `bulk`, `normal`, or `urgent`.

**Cases (stdin → stdout):** `"3\n"` → `"urgent\n"` · `"0\n"` → `"drop\n"` · `"4\n"` → `""` (exit 2)

**Rules:** Use `switch`; invalid code prints no stdout and exits 2.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0009`.
