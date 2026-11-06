# EX-0038 — Function pointer calculator

**Time:** ~30 min · **Skill:** `PROG-C-POINTERS`

**Task:** Dispatch `add`, `min`, `max`, `xor` through function pointers on two nonnegative integers (0..1000).

**Cases (stdin → stdout):** `"xor 5 3\n"` → `"6\n"` · `"max 5 3\n"` → `"5\n"` · `"add 2 9\n"` → `"11\n"`

**Rules:** Print decimal result; define compatible callback types.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0038`.
