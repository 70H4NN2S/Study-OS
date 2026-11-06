# EX-0043 — Vector insert and erase

**Time:** ~35 min · **Skill:** `PROG-C-HEAP`

**Task:** Read n (0..10) and n integers, then `index value`; use `realloc` to insert value at index and print new array.

**Cases (stdin → stdout):** `"3 1 3 4 1 2\n"` → `"1 2 3 4\n"` · `"0 0 9\n"` → `"9\n"`

**Rules:** Index 0..n; preserve existing order; free heap.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0043`.
