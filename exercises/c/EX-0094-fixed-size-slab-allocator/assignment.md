# EX-0094 — Fixed-size slab allocator

**Time:** ~35 min · **Skill:** `PROG-C-MEMORY-MODEL` · **Platform:** Linux/POSIX

**Task:** Implement a 4-slot array pool with a free-index stack. Allocate slots 0,1,2; release slot 1; allocate once more and print reused index.

**Cases (stdin → stdout):** `""` → `"1\n"`

**Rules:** Do not allocate outside the pool.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0094`.
