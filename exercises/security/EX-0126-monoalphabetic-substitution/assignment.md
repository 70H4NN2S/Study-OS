# EX-0126 — Monoalphabetic substitution

**Time:** ~25 min · **Skill:** `SEC-CRYPTO-CLASSICAL`

**Task:** Implement `encrypt(text: str, key: str) -> str` and `decrypt(text: str, key: str) -> str`. `key` is a 26-letter uppercase permutation mapping A..Z to the key alphabet.

**Cases:** Key `QWERTYUIOPASDFGHJKLZXCVBNM`: `encrypt("ABC xyz!", key)` → `"QWE bnm!"`; `decrypt("QWE bnm!", key)` → `"ABC xyz!"`.

**Rules:** Assume a valid permutation; preserve case and non-letters. Do not use an encryption library.

**Submit:** `exercises/security/EX-0126-monoalphabetic-substitution/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0126`.
