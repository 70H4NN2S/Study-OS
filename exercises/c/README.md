# Progressive C mastery — 100 original exercises

**Scope:** beginner C11 → defensive programming → memory ownership → modular C → files → POSIX → threads/IPC → advanced systems. Exercises are independent and deliberately **not** copies of TU Braunschweig homework.

## How to use
Start at EX-0001 unless an independent diagnostic demonstrates prerequisite mastery. Within a module, attempt tasks in order. One completed task ≠ skill mastery: submit exact commit, tests and explanation, then request review. Schedule retrieval from evidence after each review; do not blindly mark 100 tasks complete.

- No solution keys or pre-filled implementations; public example tests are transparent, not hidden grades.
- Strict compile flags: `-std=c11 -pedantic -D_XOPEN_SOURCE=700 -Wall -Wextra -Werror`. Later tasks require POSIX/Linux and sometimes `-pthread`.
- Help: attempt independently first; ask for tier 1/2 hints, escalate to pseudocode only with an identified blocker; record help used.
- University homework PDFs informed topic selection only. The course prohibits AI for graded homework: never submit AI-generated Study OS code as a university answer.
- Run `python3 tools/validate.py` for registries, `python3 tools/validate_c_catalog.py` for this catalog, and `python3 tools/check_c.py EX-0001` after writing source.

## Exercises

### Module 1: C tooling and numerical foundations (EX-0001–EX-0010)
_Program structure, safe I/O, types, casting, branching, flags and overflow_

- [EX-0001 — hello toolchain](EX-0001-hello-toolchain/assignment.md)
- [EX-0002 — temperature station](EX-0002-temperature-station/assignment.md)
- [EX-0003 — clock formatter](EX-0003-clock-formatter/assignment.md)
- [EX-0004 — signed number inspector](EX-0004-signed-number-inspector/assignment.md)
- [EX-0005 — tiered bandwidth billing](EX-0005-tiered-bandwidth-billing/assignment.md)
- [EX-0006 — cross midnight timer](EX-0006-cross-midnight-timer/assignment.md)
- [EX-0007 — permission bit decoder](EX-0007-permission-bit-decoder/assignment.md)
- [EX-0008 — checked addition](EX-0008-checked-addition/assignment.md)
- [EX-0009 — packet priority router](EX-0009-packet-priority-router/assignment.md)
- [EX-0010 — interactive safe menu](EX-0010-interactive-safe-menu/assignment.md)

### Module 2: Loops, arrays and search (EX-0011–EX-0020)
_Divisibility, numeric algorithms, histograms, arrays, sorting, searching and matrix locality_

- [EX-0011 — range labeling](EX-0011-range-labeling/assignment.md)
- [EX-0012 — prime detector](EX-0012-prime-detector/assignment.md)
- [EX-0013 — euclidean toolkit](EX-0013-euclidean-toolkit/assignment.md)
- [EX-0014 — small histogram](EX-0014-small-histogram/assignment.md)
- [EX-0015 — streaming extremes](EX-0015-streaming-extremes/assignment.md)
- [EX-0016 — stable unique values](EX-0016-stable-unique-values/assignment.md)
- [EX-0017 — insertion sort trace](EX-0017-insertion-sort-trace/assignment.md)
- [EX-0018 — binary search contract](EX-0018-binary-search-contract/assignment.md)
- [EX-0019 — matrix scanner](EX-0019-matrix-scanner/assignment.md)
- [EX-0020 — grid island perimeter](EX-0020-grid-island-perimeter/assignment.md)

### Module 3: Strings and robust parsing (EX-0021–EX-0030)
_NUL termination, bytes vs characters, safe parsing, CSV/command grammars and IPv4 input_

- [EX-0021 — length without strlen](EX-0021-length-without-strlen/assignment.md)
- [EX-0022 — in place whitespace trimmer](EX-0022-in-place-whitespace-trimmer/assignment.md)
- [EX-0023 — case insensitive frequency](EX-0023-case-insensitive-frequency/assignment.md)
- [EX-0024 — palindrome normalizer](EX-0024-palindrome-normalizer/assignment.md)
- [EX-0025 — safe integer parser](EX-0025-safe-integer-parser/assignment.md)
- [EX-0026 — manual substring search](EX-0026-manual-substring-search/assignment.md)
- [EX-0027 — text word wrapper](EX-0027-text-word-wrapper/assignment.md)
- [EX-0028 — csv two field reader](EX-0028-csv-two-field-reader/assignment.md)
- [EX-0029 — ipv4 text validator](EX-0029-ipv4-text-validator/assignment.md)
- [EX-0030 — tiny command tokenizer](EX-0030-tiny-command-tokenizer/assignment.md)

### Module 4: Pointers, structs and undefined behavior (EX-0031–EX-0040)
_Aliasing, lifetime, typed views, tagged unions, callbacks, byte order and debugging_

- [EX-0031 — pointer swap laboratory](EX-0031-pointer-swap-laboratory/assignment.md)
- [EX-0032 — reverse a span](EX-0032-reverse-a-span/assignment.md)
- [EX-0033 — readonly view versus owner](EX-0033-readonly-view-versus-owner/assignment.md)
- [EX-0034 — inventory records](EX-0034-inventory-records/assignment.md)
- [EX-0035 — tagged event variants](EX-0035-tagged-event-variants/assignment.md)
- [EX-0036 — comparator clinic](EX-0036-comparator-clinic/assignment.md)
- [EX-0037 — decode network order header](EX-0037-decode-network-order-header/assignment.md)
- [EX-0038 — function pointer calculator](EX-0038-function-pointer-calculator/assignment.md)
- [EX-0039 — recursion and stack limits](EX-0039-recursion-and-stack-limits/assignment.md)
- [EX-0040 — undefined behavior audit](EX-0040-undefined-behavior-audit/assignment.md)

### Module 5: Dynamic memory and containers (EX-0041–EX-0050)
_malloc/calloc/realloc/free, failure safety, ownership, lists, queues and amortized analysis_

- [EX-0041 — allocation failure discipline](EX-0041-allocation-failure-discipline/assignment.md)
- [EX-0042 — dynamic vector i](EX-0042-dynamic-vector-i/assignment.md)
- [EX-0043 — vector insert and erase](EX-0043-vector-insert-and-erase/assignment.md)
- [EX-0044 — amortized growth experiment](EX-0044-amortized-growth-experiment/assignment.md)
- [EX-0045 — owned string builder](EX-0045-owned-string-builder/assignment.md)
- [EX-0046 — deep copy directory](EX-0046-deep-copy-directory/assignment.md)
- [EX-0047 — ownership graph challenge](EX-0047-ownership-graph-challenge/assignment.md)
- [EX-0048 — sorted linked set](EX-0048-sorted-linked-set/assignment.md)
- [EX-0049 — doubly linked playlist](EX-0049-doubly-linked-playlist/assignment.md)
- [EX-0050 — ring queue with wraparound](EX-0050-ring-queue-with-wraparound/assignment.md)

### Module 6: Modules, Make and generic components (EX-0051–EX-0060)
_Header interfaces, preprocessor, makefiles, errno, generic callbacks, hash maps and capstone_

- [EX-0051 — multi file library boundary](EX-0051-multi-file-library-boundary/assignment.md)
- [EX-0052 — make rebuild rules](EX-0052-make-rebuild-rules/assignment.md)
- [EX-0053 — build time feature switches](EX-0053-build-time-feature-switches/assignment.md)
- [EX-0054 — macro side effect trap](EX-0054-macro-side-effect-trap/assignment.md)
- [EX-0055 — error aware parser library](EX-0055-error-aware-parser-library/assignment.md)
- [EX-0056 — generic filtered fold](EX-0056-generic-filtered-fold/assignment.md)
- [EX-0057 — undoable text editor](EX-0057-undoable-text-editor/assignment.md)
- [EX-0058 — open addressed word map](EX-0058-open-addressed-word-map/assignment.md)
- [EX-0059 — binary search tree index](EX-0059-binary-search-tree-index/assignment.md)
- [EX-0060 — c library mini capstone](EX-0060-c-library-mini-capstone/assignment.md)

### Module 7: Streams, formats and persistence (EX-0061–EX-0070)
_Standard C/POSIX file I/O, long lines, binary serialization, durable saves, logs and journaling_

- [EX-0061 — file line counter](EX-0061-file-line-counter/assignment.md)
- [EX-0062 — arbitrarily long line reader](EX-0062-arbitrarily-long-line-reader/assignment.md)
- [EX-0063 — csv numeric aggregator](EX-0063-csv-numeric-aggregator/assignment.md)
- [EX-0064 — versioned binary records](EX-0064-versioned-binary-records/assignment.md)
- [EX-0065 — binary hexdump](EX-0065-binary-hexdump/assignment.md)
- [EX-0066 — safe atomic configuration save](EX-0066-safe-atomic-configuration-save/assignment.md)
- [EX-0067 — bytewise file comparator](EX-0067-bytewise-file-comparator/assignment.md)
- [EX-0068 — sparse file inspector](EX-0068-sparse-file-inspector/assignment.md)
- [EX-0069 — streaming log tail](EX-0069-streaming-log-tail/assignment.md)
- [EX-0070 — journal replay](EX-0070-journal-replay/assignment.md)

### Module 8: POSIX files, processes and IPC (EX-0071–EX-0080)
_File descriptors, EINTR, directories, fork/exec/wait, pipes, signal lifecycles and CLOEXEC_

- [EX-0071 — descriptor based copier](EX-0071-descriptor-based-copier/assignment.md)
- [EX-0072 — robust write all api](EX-0072-robust-write-all-api/assignment.md)
- [EX-0073 — directory snapshot](EX-0073-directory-snapshot/assignment.md)
- [EX-0074 — symlink safe tree walker](EX-0074-symlink-safe-tree-walker/assignment.md)
- [EX-0075 — fork and wait timeline](EX-0075-fork-and-wait-timeline/assignment.md)
- [EX-0076 — exec argument runner](EX-0076-exec-argument-runner/assignment.md)
- [EX-0077 — parent child result pipe](EX-0077-parent-child-result-pipe/assignment.md)
- [EX-0078 — two stage pipeline](EX-0078-two-stage-pipeline/assignment.md)
- [EX-0079 — timed child supervisor](EX-0079-timed-child-supervisor/assignment.md)
- [EX-0080 — descriptor leak audit](EX-0080-descriptor-leak-audit/assignment.md)

### Module 9: Synchronization, atomics and network foundations (EX-0081–EX-0090)
_Signals, shared memory, semaphores, pthreads, locks, atomics and loopback TCP_

- [EX-0081 — async signal safe shutdown](EX-0081-async-signal-safe-shutdown/assignment.md)
- [EX-0082 — posix shared memory scoreboard](EX-0082-posix-shared-memory-scoreboard/assignment.md)
- [EX-0083 — semaphore gate](EX-0083-semaphore-gate/assignment.md)
- [EX-0084 — thread safe counter](EX-0084-thread-safe-counter/assignment.md)
- [EX-0085 — producer consumer ring](EX-0085-producer-consumer-ring/assignment.md)
- [EX-0086 — deadlock avoidance lab](EX-0086-deadlock-avoidance-lab/assignment.md)
- [EX-0087 — read mostly cache](EX-0087-read-mostly-cache/assignment.md)
- [EX-0088 — c11 atomic flags](EX-0088-c11-atomic-flags/assignment.md)
- [EX-0089 — loopback tcp client](EX-0089-loopback-tcp-client/assignment.md)
- [EX-0090 — single client tcp echo server](EX-0090-single-client-tcp-echo-server/assignment.md)

### Module 10: Advanced systems engineering (EX-0091–EX-0100)
_poll, framed protocols, arenas, slab allocation, memory mapping, journaling, thread pools, benchmarking, fuzzing and final capstone_

- [EX-0091 — poll based chat relay](EX-0091-poll-based-chat-relay/assignment.md)
- [EX-0092 — streaming framed message parser](EX-0092-streaming-framed-message-parser/assignment.md)
- [EX-0093 — aligned bump arena](EX-0093-aligned-bump-arena/assignment.md)
- [EX-0094 — fixed size slab allocator](EX-0094-fixed-size-slab-allocator/assignment.md)
- [EX-0095 — memory mapping explorer](EX-0095-memory-mapping-explorer/assignment.md)
- [EX-0096 — checksummed event journal](EX-0096-checksummed-event-journal/assignment.md)
- [EX-0097 — small worker thread pool](EX-0097-small-worker-thread-pool/assignment.md)
- [EX-0098 — cache locality benchmark](EX-0098-cache-locality-benchmark/assignment.md)
- [EX-0099 — input fuzzing and invariant campaign](EX-0099-input-fuzzing-and-invariant-campaign/assignment.md)
- [EX-0100 — capstone local telemetry service](EX-0100-capstone-local-telemetry-service/assignment.md)
