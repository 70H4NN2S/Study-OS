# EX-0025 — Safe integer parser

**Time:** ~25 min · **Skill:** `PROG-C-ERROR`

**Task:** Read a token; parse it as signed 32-bit decimal using `strtol`; print its value or `invalid`.

**Cases (stdin → stdout):** `"+17\n"` → `"17\n"` · `"12x\n"` → `"invalid\n"` · `"2147483648\n"` → `"invalid\n"`

**Rules:** Check `errno`, consumed characters, and 32-bit range.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0025`.
