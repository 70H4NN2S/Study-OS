# EX-0050 — Ring queue with wraparound

**Time:** ~35 min · **Skill:** `PROG-C-ARRAYS`

**Task:** Implement an array queue capacity 3. Read four ints: enqueue first three, dequeue once, enqueue fourth; print remaining FIFO order.

**Cases (stdin → stdout):** `"1 2 3 4\n"` → `"2 3 4\n"` · `"0 7 0 8\n"` → `"7 0 8\n"`

**Rules:** Use head/count and modulo 3, not shifting elements.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0050`.
