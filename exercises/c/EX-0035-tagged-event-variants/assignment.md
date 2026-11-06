# EX-0035 — Tagged event variants

**Time:** ~25 min · **Skill:** `PROG-C-STRUCTS`

**Task:** Use `enum`, `union`, and `struct` for one event: `TEMP x` or `ALARM x`. Print normalized event.

**Cases (stdin → stdout):** `"TEMP 20\n"` → `"temperature=20\n"` · `"ALARM 3\n"` → `"alarm=3\n"`

**Rules:** `TEMP x` → `temperature=x`; `ALARM x` → `alarm=x`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0035`.
