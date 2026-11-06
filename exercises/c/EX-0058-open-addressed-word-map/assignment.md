# EX-0058 — Open-addressed word map

**Time:** ~45 min · **Skill:** `PROG-C-ALGORITHMS`

**Task:** Build a 7-slot open-addressed integer set. Read n (0..5), n distinct integers 0..99 and one query; print the query's stored slot or `-1`.

**Cases (stdin → stdout):** `"3 1 8 15 8\n"` → `"2\n"` · `"2 7 14 21\n"` → `"-1\n"`

**Rules:** Hash = key % 7; linear probe; empty slots marked -1; no removal.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0058`.
