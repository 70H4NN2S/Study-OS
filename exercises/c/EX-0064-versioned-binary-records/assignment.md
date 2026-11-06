# EX-0064 — Versioned binary records

**Time:** ~25 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Use `fread` to read exactly 4 raw stdin bytes and print their unsigned decimal byte values.

**Cases (stdin → stdout):** `"ABCD"` → `"65 66 67 68\n"` · `"AB"` → `"short\n"`

**Rules:** If fewer than four bytes, print `short`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0064`.
