# EX-0127 — Caesar ciphertext-only cryptanalysis

**Time:** ~30 min · **Skill:** `SEC-CRYPTO-ANALYSIS`

**Task:** Implement `recover_shift(ciphertext: str) -> int` for longer English text without knowing the key. Rank all 26 candidate shifts using an English-letter frequency score (e.g. chi-square).

**Cases:** The included public case is original English prose encrypted with shift 7; the function should return `7`.

**Rules:** Ciphertext is ASCII English with enough letters for statistics. Return the encryption shift (0..25), not the decryption shift.

**Submit:** `exercises/security/EX-0127-crack-caesar/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0127`.
