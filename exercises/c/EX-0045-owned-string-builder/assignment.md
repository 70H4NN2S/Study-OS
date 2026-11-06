# EX-0045 — Owned string builder

**Time:** ~30 min · **Skill:** `PROG-C-HEAP`

**Task:** Read two words (≤20 bytes each); allocate exactly enough bytes for `word1:word2` plus NUL and print the result.

**Cases (stdin → stdout):** `"cat dog\n"` → `"cat:dog\n"` · `"a b\n"` → `"a:b\n"`

**Rules:** Use `malloc`, `strlen`, `memcpy` or `snprintf`; free.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0045`.
