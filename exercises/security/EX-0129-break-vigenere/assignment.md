# EX-0129 — Vigenère known-period key recovery

**Time:** ~45 min · **Skill:** `SEC-CRYPTO-ANALYSIS`

**Task:** Implement `recover_key(ciphertext: str, key_length: int) -> str`. Split letters by index modulo key length and use frequency analysis to recover each Caesar shift.

**Cases:** The public ciphertext is English text encrypted under a 5-letter key; return that uppercase key.

**Rules:** Key length is given; do not assume plaintext, dictionary lists, or internet services. Sufficient ciphertext is provided.

**Submit:** `exercises/security/EX-0129-break-vigenere/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0129`.
