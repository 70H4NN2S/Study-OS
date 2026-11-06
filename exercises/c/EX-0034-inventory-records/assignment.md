# EX-0034 — Inventory records

**Time:** ~25 min · **Skill:** `PROG-C-STRUCTS`

**Task:** Declare `struct item {int id,quantity,price;}`; read two items and print total `quantity*price` in cents.

**Cases (stdin → stdout):** `"1 2 50 2 1 70\n"` → `"170\n"` · `"3 0 99 4 2 7\n"` → `"14\n"`

**Rules:** All fields 0..100; use struct members rather than parallel arrays.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0034`.
