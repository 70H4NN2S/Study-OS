# Decisions

## 2026-11-06
- Lite/Core hybrid: ChatGPT as tutor/evaluator, GitHub as versioned memory.
- Six methods: active recall, spaced repetition, interleaving, deliberate practice, scaffolding, metacognition.
- User triggers exercise creation and 1–2 weekend exams; tutor has freedom to design exercises and combine subjects.
- **Default trigger:** When a learning request invokes **Study OS** alongside a topic, example exercise, lecture material or exam scope, proactively read relevant GitHub state and supplied materials and **open a reviewable PR with the corresponding exercises or exams** without asking again. A submission review should produce grading/state updates instead; explicit discussion-only requests do not trigger exercise generation.
- PRs preferred; one Markdown assignment per exercise, optional PDF/starter code/tests/project artifacts; specify allowed help, deliverables and verification.
- Strict rubric-based correction, feedback-led improvements, stateful mastery/review tracking based only on actual evidence.
- No Anki; avoid separate application, excessive ceremony and speculative scores.
- Public repository for now by user choice; handle personal and restricted materials carefully.
