# Study OS

A lightweight, GitHub-centered, ChatGPT-assisted learning system. **GitHub is the durable record; ChatGPT chats are the interface.** No Anki or dedicated application.

## Quick start
In any ChatGPT chat with GitHub access: **"Study OS: read STUDY_OS.md and state/, then create an exercise on [topic] as a PR."** For grading: **"Study OS: review my submission in PR/commit [link], grade it using the rubric, and propose state updates."** On weekends: **"Study OS: create my weekly exam from recent and overdue skills."**

## Structure
- [STUDY_OS.md](STUDY_OS.md): authoritative operating rules
- [AGENTS.md](AGENTS.md): entry point for future chats/agents
- [goals/](goals/README.md): learning objectives
- [curriculum/](curriculum/README.md): subjects and stable skill identifiers
- [exercises/](exercises/README.md): one folder per exercise, canonical assignment.md
- [projects/](projects/README.md): multi-topic projects
- [exams/](exams/README.md): weekly and cumulative assessments
- [state/](state/README.md): durable evidence, reviews, decisions and continuity
- [templates/](templates/exercise.md): exercise/exam/evaluation templates
- [tools/validate.py](tools/validate.py): simple data consistency check

## Workflow
Discuss topic and time → ChatGPT opens assignment PR → learner solves and submits code/docs/diagrams/PDF/configs → ChatGPT verifies artifacts and reasoning, grades against rubric → review and mastery state updated through a PR → later independent retrieval and weekend exams.

No exercises, exam results, mastery levels or previous progress are assumed at initialization. All generation and assessments are triggered by the user. This repo is **public** by choice: do not commit private, restricted, secret or copyrighted content without appropriate rights.
