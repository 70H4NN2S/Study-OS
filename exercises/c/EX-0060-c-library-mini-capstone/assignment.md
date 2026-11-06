# EX-0060 — C library mini-capstone

**Time:** ~55 min · **Skill:** `PROG-C-DESIGN`

**Task:** Read n (0..10) `(sensor_id value)` pairs with IDs 0..3; accumulate sums per ID and print four sums in ID order.

**Cases (stdin → stdout):** `"3 0 2 1 5 0 3\n"` → `"5 5 0 0\n"` · `"0\n"` → `"0 0 0 0\n"`

**Rules:** Put accumulation in a separate function, ideally a separate `.c/.h`. Inputs -100..100.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0060`.
