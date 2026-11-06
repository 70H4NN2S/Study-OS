# EX-0008 — Checked addition

**Time:** ~20 min · **Skill:** `PROG-C-TYPES`

**Task:** Read two signed 32-bit integers; print sum, or `overflow` if unrepresentable.

**Cases (stdin → stdout):** `"-5 2\n"` → `"-3\n"` · `"2147483647 1\n"` → `"overflow\n"` (exit 1)

**Rules:** Prevent signed-overflow undefined behavior; overflow exits 1.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0008`.
