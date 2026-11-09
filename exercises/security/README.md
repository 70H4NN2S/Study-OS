# Symmetric cryptography: short challenges

Original practice aligned conceptually to the TU Braunschweig **Symmetric-Key Cryptography** unit (sec-02-crypto.pdf, pages 3–34). The university slides and original university exercises are **not** copied into this public repository.

Start with EX-0125. Each assignment is independently completable and uses the shared [Study OS contract](../../STUDY_OS.md). **No solutions are supplied.**

| ID | Concept | Expected time |
|---|---|---|
| [EX-0125](EX-0125-caesar-shift/assignment.md) | Caesar encrypt/decrypt | 15 min |
| [EX-0126](EX-0126-monoalphabetic-substitution/assignment.md) | Monoalphabetic substitution | 25 min |
| [EX-0127](EX-0127-crack-caesar/assignment.md) | Caesar ciphertext-only cryptanalysis | 30 min |
| [EX-0128](EX-0128-vigenere-cipher/assignment.md) | Vigenère encrypt/decrypt | 25 min |
| [EX-0129](EX-0129-break-vigenere/assignment.md) | Vigenère known-period key recovery | 45 min |
| [EX-0130](EX-0130-xor-pad-reuse/assignment.md) | XOR and the reused-pad failure | 20 min |
| [EX-0131](EX-0131-aes-ecb-vector/assignment.md) | AES-ECB known-answer tests | 25 min |
| [EX-0132](EX-0132-aes-cbc-vector/assignment.md) | AES-CBC chaining and IV | 30 min |
| [EX-0133](EX-0133-aes-ctr-counter/assignment.md) | AES-CTR counter-mode experiment | 30 min |
| [EX-0134](EX-0134-aes-gcm-integrity/assignment.md) | AES-GCM authenticated encryption | 40 min |

## Workflow

1. Read one assignment. Implement its specified functions in that assignment's `src/main.py`.
2. Run `python3 tools/check_crypto.py EX-0125` (replace the ID). Run `python3 tools/check_crypto.py all` to test all submitted solutions.
3. Submit the code or a commit/PR. The reviewer applies novel cases and assesses your explanation separately from public test results. No skills or completions are recorded until review.

**Environment:** Python 3.12+. EX-0131 to EX-0134 require `python3 -m pip install pycryptodome` (prefer a virtual environment). All other exercises use the Python standard library. Test vectors for AES are standard published known-answer vectors, not secret answers.

**Security:** Classical ciphers, ECB, and bare CBC/CTR are exercises, not recipes for production encryption. Never invent encryption for real secrets. Prefer reviewed authenticated encryption such as AES-GCM, with unique nonces per key, in real software. The provided fixed test keys/nonces are for reproducible tests only.
