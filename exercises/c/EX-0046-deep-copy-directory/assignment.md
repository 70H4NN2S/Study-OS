# EX-0046 — Deep-copy directory

**Time:** ~35 min · **Skill:** `PROG-C-HEAP`

**Task:** Read one word (≤20 bytes). `malloc` and copy it, then replace the original buffer's first character with `X`. Print the copy.

**Cases (stdin → stdout):** `"hello\n"` → `"hello\n"` · `"test\n"` → `"test\n"`

**Rules:** Never make the copy point into original storage; free the copy.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0046`.
