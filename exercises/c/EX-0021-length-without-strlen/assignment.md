# EX-0021 — Length without strlen

**Time:** ~10 min · **Skill:** `PROG-C-STRINGS`

**Task:** Read one line; print its byte length excluding the newline.

**Cases (stdin → stdout):** `"hello\n"` → `"5\n"` · `"\n"` → `"0\n"`

**Rules:** Implement `size_t my_strlen(const char *s)`; no `strlen`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0021`.
