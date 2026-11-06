# EX-0020 — Grid island perimeter

**Time:** ~30 min · **Skill:** `PROG-C-ARRAYS`

**Task:** Read rows r, columns c (1..5), then r*c entries 0/1; print total exposed edges of 1-cells.

**Cases (stdin → stdout):** `"1 1 1\n"` → `"4\n"` · `"1 2 1 1\n"` → `"6\n"` · `"2 2 0 0 0 0\n"` → `"0\n"`

**Rules:** Each 1 contributes four edges minus one per adjacent 1 side.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0020`.
