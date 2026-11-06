# EX-0039 — Recursion and stack limits

**Time:** ~20 min · **Skill:** `PROG-C-FUNCTIONS`

**Task:** Write a recursive `unsigned factorial(unsigned n)`; read n (0..12) and print n!.

**Cases (stdin → stdout):** `"0\n"` → `"1\n"` · `"5\n"` → `"120\n"`

**Rules:** Handle 0!=1; stay within unsigned 32-bit range.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0039`.
