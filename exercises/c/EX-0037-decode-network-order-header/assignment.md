# EX-0037 — Decode network-order header

**Time:** ~20 min · **Skill:** `PROG-C-TYPES`

**Task:** Read four hexadecimal bytes (0..FF); combine as a 32-bit big-endian unsigned number and print decimal.

**Cases (stdin → stdout):** `"00 00 01 00\n"` → `"256\n"` · `"00 00 00 2A\n"` → `"42\n"`

**Rules:** Use shifting of `uint32_t`, not struct casting.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0037`.
