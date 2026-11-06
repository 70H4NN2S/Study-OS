# EX-0010 — Interactive safe menu

**Time:** ~20 min · **Skill:** `PROG-C-CONTROL`

**Task:** Read command integers until `0`: `1` increments counter, `2` decrements, `3` prints counter.

**Cases (stdin → stdout):** `"1 1 3 2 3 0\n"` → `"2\n1\n"` · `"2 3 0\n"` → `"error\n0\n"`

**Rules:** Initial counter = 0; only allow values 0..100. Invalid operation prints `error`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0010`.
