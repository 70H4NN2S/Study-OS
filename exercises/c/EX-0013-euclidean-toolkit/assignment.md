# EX-0013 — Euclidean toolkit

**Time:** ~25 min · **Skill:** `PROG-C-FUNCTIONS`

**Task:** Write `unsigned gcd(unsigned a,unsigned b)` and use it to print gcd and lcm of two numbers.

**Cases (stdin → stdout):** `"12 18\n"` → `"6 36\n"` · `"0 5\n"` → `"5 0\n"`

**Rules:** Inputs 0..1000; `gcd(0,0)=0`, `lcm(0,x)=0`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0013`.
