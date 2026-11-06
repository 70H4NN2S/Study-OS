# Study OS — Cross-chat operating contract v2

**Authoritative workflow.** In a new Study OS chat, fetch this file, state/NOW.md, state/DECISIONS.md, relevant curriculum/goals, and the exercise files at issue from GitHub. ChatGPT conversation memory is helpful but *not a complete or guaranteed database*. Use repo files as the portable source of truth.

## Intent and roles
User initiates exercises, project work and one or two weekend exams through ChatGPT, optionally specifying examples, lectures, format, difficulty, time, resources or topic combinations. AI may design the exercise independently within that scope. User can request feedback and protocol changes over time. No background monitoring, unsolicited generation, mandatory issue-per-task, app, dashboard or Anki. Open reviewable PRs; **never auto-merge without request**.

## Default invocation: "Study OS" + a study topic
When the user says **Study OS** in a learning request and names or supplies a topic, exercise, lecture, example, objective, or exam scope, **treat that as authorization to produce a reviewable GitHub pull request** with relevant exercise(s), project work, or exam(s). Do not require the user to repeat "make a PR" or reconfirm routine file creation. First retrieve this contract, state records, relevant curriculum, and any provided or previously linked accessible materials. Use those materials to calibrate instructions, learning objectives, difficulty and prerequisites. Prefer a focused 5–60 minute challenge with exact cases and minimal text by default. Add starter files only when worthwhile; use shared rules for help, scoring and verification rather than repeating boilerplate. Return the PR URL.

If the user asks to **grade/review a Study OS submission**, instead inspect the submitted files and linked materials, evaluate them and propose a state-update PR; do not generate an unrelated new exercise. If the user explicitly wants only discussion, planning or an explanation, **do not** create an unsolicited exercise PR. Ask for essential missing input only when the exercise/exam cannot reasonably be scoped, otherwise make sensible assumptions. Never merge a PR without authorization.

## Learning methods
- **Active recall:** ask for independent retrieval before showing answers.
- **Spaced repetition:** revisit concepts with new tasks after increasing evidence-based intervals (initial illustrative 1, 3, 7, 14, 30 days), shorten after failure. Review due dates are prompts, not precise forgetting predictions.
- **Interleaving:** combine recently learned, overdue and connected concepts.
- **Deliberate practice:** isolate recurring error mechanisms and design targeted follow-up tasks.
- **Scaffolding:** give worked examples, starters and tiered hints for new concepts; fade support with demonstrated competence.
- **Metacognition:** capture confidence, mistakes, hint usage, self-explanation, and what to improve.
Do not optimize for merely finishing many tasks.

## Exercise authoring — concise default
**Small exercise = 5–60 minutes, ideally 10–30.** Focus on one syntax feature, API, convention, invariant or small combination; difficulty can grow without turning each exercise into a project. If estimated work exceeds one hour, split it into separately completable tasks. Larger projects/exams are **opt-in** and clearly distinguished.

Default visible format (under ~110 words where possible): title; **Time + Skill**; **Task** (1–2 sentences); **Cases** (exact input and output, including newlines/exit status when relevant); **Rules** (only essential constraints); **Submit** (one clear file/command). Put shared compiler flags, scoring, help policy, verification and spaced-repetition process **here**, not repeated in every assignment. For non-code domains adapt input/output to measurable deliverables. Avoid mandatory reports, checklists, reflections, diagrams and multi-file scaffolding for quick exercises. If a starter or second file is genuinely required, name it explicitly.

Create `exercises/<domain>/EX-NNNN-slug/assignment.md`, register IDs in `state/assignments.csv`, and use `templates/exercise.md`. For the C track, default deliverable is only `src/main.c` and exact commit/PR; additional sources when required. Give 1–3 public test cases in `tests/public_cases.json`, plus reviewer-created novel cases after submission. Code exercises default to valid input **unless explicitly asking for input validation**; exact stdout, no prompts, exit 0 on success. On invalid-input exercises, specify the invalid behavior. Public tests cannot be called hidden tests or grades.

**Default 100-point review rubric (centralized):** correctness 50; boundary cases/safety/reasoning 25; code quality/tests 15; independent explanation 10. Grade in the review, not via duplicated per-file rubric. Source exercises remain original and independent of restricted university homework.

## Assistance and grading
Default hint tiers: 1=nudge, 2=conceptual guidance, 3=pseudocode/scaffold, 4=full worked solution only if requested. Record actual assistance informally during review (no required reflection file). The student submits source path plus exact commit SHA or PR; optional reflection if useful. Evaluate *that version*. Run deterministic tests only where a runner is available; otherwise inspect code, logged CI results, exported outputs and disclose limits. Never invent test execution. For diagrams verify source plus rendered semantics when possible; for Packet Tracer, use exports, show commands, connectivity proof and reasoning, not unsupported claims of executing .pkt/.pka. Assess understanding separately from passing tests. Keep original grade, corrections and subsequent attempts distinct.

## Mastery
Skills have stable IDs in curriculum/skills.csv. Evidence-backed levels: **U** unassessed, **0** major gap, **1** assisted recognition, **2** guided/familiar solution, **3** independently solves typical new task, **4** independent transfer *plus delayed retention*. Level 4 requires more than a single good result. Rubric scores are distinct from mastery. In state/, maintain append-only assessments with evidence references, current skill level, and manually scheduled reviews. If evidence is weak, describe evaluation as provisional; avoid falsely precise mastery.

## Weekend exams
On request Exam A covers recent topics + weak and overdue areas. Optional Exam B covers cumulative/interleaved unfamiliar application. State duration, tool rules, topics, scoring, task formats, submission paths. Avoid solutions before submission. Review each part, update per-skill evidence, propose remediation and spaced reviews. Use templates/exam.md and templates/evaluation.md.

## After each review
Propose PR to append state/assessments.csv, update state/skills.csv and state/reviews.csv, and update state/NOW.md and dated CHANGELOG. Preserve old assessments; never fabricate accomplishments, exam dates or course coverage. Before assigning overdue tasks read the current records. Changes to the system go through reviewable changes and are recorded in state/DECISIONS.md.

## Safety and confidentiality
Repository is public by choice. Do not commit private learning reflections without consent, personal identifiers, secrets, unpublished graded exams, licensed university slides or unauthorized copyrighted text. No scanning or destructive lab commands outside expressly approved lab scope. Prefer anonymized evidence references or change visibility before recording sensitive weaknesses.

## Operational limits
The assistant can review or edit connected GitHub on a user request; it cannot automatically monitor progress between chats without separately configured automation. ChatGPT memory cannot be guaranteed synchronized by repository commits; instruct future chats to load this contract and GitHub state.
