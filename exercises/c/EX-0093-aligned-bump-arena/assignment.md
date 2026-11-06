# EX-0093 — Aligned bump arena

**Time:** ~45 min · **Skill:** `PROG-C-MEMORY-MODEL` · **Platform:** Linux/POSIX

**Task:** Use `unsigned char arena[64]` and a size_t offset. Read two sizes a,b (0..20); allocate first at offset 0 and second at next multiple of 4; print both offsets.

**Cases (stdin → stdout):** `"3 5"` → `"0 4\n"` · `"8 2"` → `"0 8\n"`

**Rules:** Bounds-check before reserving; no malloc necessary.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0093`.
