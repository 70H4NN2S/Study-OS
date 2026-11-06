# EX-0029 — IPv4 text validator

**Time:** ~35 min · **Skill:** `PROG-C-STRINGS`

**Task:** Read a dotted IPv4 token; print `valid` only for four decimal octets 0..255.

**Cases (stdin → stdout):** `"192.168.1.10\n"` → `"valid\n"` · `"256.1.2.3\n"` → `"invalid\n"` · `"01.2.3.4\n"` → `"invalid\n"`

**Rules:** No empty component, signs, leading zeroes or trailing junk.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0029`.
