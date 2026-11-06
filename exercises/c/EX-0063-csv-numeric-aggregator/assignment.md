# EX-0063 — CSV numeric aggregator

**Time:** ~30 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read two lines formatted `number,number`; parse each and print sum of all four integers.

**Cases (stdin → stdout):** `"1,2\n3,4\n"` → `"10\n"` · `"0,5\n5,0\n"` → `"10\n"`

**Rules:** Numbers 0..100; process using `fgets` and checked `sscanf`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0063`.
