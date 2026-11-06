# EX-0070 — Journal replay

**Time:** ~45 min · **Skill:** `PROG-C-DESIGN` · **Platform:** C11

**Task:** Read n (1..5) operations: `SET a value`, `SET b value`, `DEL a`, or `DEL b`; output final stored keys in a,b order.

**Cases (stdin → stdout):** `"3 SET a 2 SET b 9 DEL a"` → `"b=9\n"` · `"2 SET a 4 DEL a"` → `"empty\n"`

**Rules:** Values 0..100. Output `a=value` / `b=value` each on separate line; empty state prints `empty`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0070`.
