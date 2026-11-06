# EX-0065 — Binary hexdump

**Time:** ~25 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read up to 4 stdin bytes with `fread` and print them as uppercase hexadecimal, two digits each.

**Cases (stdin → stdout):** `"AB"` → `"41 42\n"` · `"0"` → `"30\n"`

**Rules:** Separate bytes with one space; read binary data as `unsigned char`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0065`.
