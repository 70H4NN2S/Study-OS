# EX-0068 — Sparse file inspector

**Time:** ~30 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read a word (1..20 bytes); write to `tmpfile`, seek to its final byte with `fseek`, then print that byte.

**Cases (stdin → stdout):** `"abcd"` → `"d\n"` · `"Z"` → `"Z\n"`

**Rules:** Use `ftell` to find length; close file.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0068`.
