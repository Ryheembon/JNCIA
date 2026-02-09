# JNCIA-Junos (JNCIA-105) Study & Practice Exam

A **professional web-based study tool** to help you pass the **JNCIA-Junos** certification (JNCIA-105 / JN0-102). Includes **100+ multiple-choice questions** with explanations, aligned to the official exam blueprint.

## Goal: Pass by Saturday

Use the **Practice Quiz** and **Flashcards** daily. Aim for 70%+ on full quizzes (typical passing score). Focus on weak topics using the topic filter.

## Features

- **100+ questions** across 7+ exam topics
- **Practice quiz**: Choose number of questions (10–100 or All) and filter by topic
- **Immediate feedback**: Correct answer and explanation after each question
- **Flashcards**: Review by topic; flip to see answer and explanation
- **Exam topics**: Networking fundamentals, Junos OS, CLI, configuration, monitoring, routing, security

## Quick Start (Website)

1. Open `index.html` in a modern browser (Chrome, Firefox, Safari, Edge).
2. Click **Start Practice Quiz** or scroll to **Practice quiz**.
3. Select **Number of questions** and **Topic** (or "All topics").
4. Click **Start quiz**, answer each question, then **Submit answer** → read explanation → **Next question**.
5. Use **Flashcards** to review concepts by topic.

No server or install required—everything runs in the browser.

## Exam Topics Covered

- **Networking fundamentals** — Collision/broadcast domains, L2/L3, subnetting, longest match, routing tables (inet.0, inet6.0)
- **Junos OS fundamentals** — RE vs PFE, control vs forwarding plane, transit vs exception traffic
- **User interfaces** — CLI modes, active vs candidate config, load merge/override, J-Web
- **Configuration basics** — Users, login classes, NTP, SNMP, syslog, rescue config, commit confirmed
- **Operational monitoring** — show/monitor commands, ping, traceroute, upgrades, root recovery
- **Routing fundamentals** — Static, OSPF, BGP, route preference, routing policy, firewall filters
- **Security** — Zones, policies, NAT, IPsec, authentication

## CLI Quiz (Optional)

If you prefer the command line:

```bash
python3 cli_quiz.py
```

Choose 5–50 questions and answer by number. The CLI uses the same style of questions (multiple choice + explanations).

## Study Tips

1. **Practice daily** — Do at least one quiz (20–50 questions) each day.
2. **Read every explanation** — Even when you're right, the explanation reinforces the concept.
3. **Filter by topic** — Use the topic filter to drill weak areas (e.g. Security, Routing).
4. **Use flashcards** — Great for quick review without scoring pressure.
5. **Aim for 70%+** — Treat that as your minimum before exam day.

## Files

- `index.html` — Main study site (quiz + flashcards + exam topics)
- `questions.js` — 100+ JNCIA-Junos questions (multiple choice + explanations)
- `script.js` — Quiz and flashcard logic
- `styles.css` — Layout and theme
- `cli_quiz.py` — Optional command-line quiz (Python)
- `daily_guide.md` — Daily study plan
- `study_plan.md` — 30-day study plan

## Good Luck

Good luck on your JNCIA-Junos exam. Consistent practice with this site and the CLI quiz will help you pass by Saturday.
