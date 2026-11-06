# EX-0055 — Error-aware parser library

**Time:** ~30 min · **Skill:** `PROG-C-ERROR`

**Task:** Read one token; use `strtol` and `errno` to parse signed decimal 0..65535, printing value or `invalid`.

**Cases (stdin → stdout):** `"8080\n"` → `"8080\n"` · `"80000\n"` → `"invalid\n"` · `"12x\n"` → `"invalid\n"`

**Rules:** Reject signs other than optional `+`, trailing text, empty and range errors.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0055`.
