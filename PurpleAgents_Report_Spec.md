# PurpleAgents — Project Report Build Spec (for Claude Code)

This file contains **everything** needed to generate the B.Tech Phase-1 project
report for **PurpleAgents**. Follow it end to end. All content below is written in
simple, clear English and is ready to be placed into the report.

---

## 0. INSTRUCTIONS FOR CLAUDE CODE (read first)

**What to build:** A complete, well-formatted project report in **LaTeX**,
compiled to **PDF**, matching the structure and academic style of a standard KTU
B.Tech project report (title page → certificate → declaration → abstract →
acknowledgement → contents → list of figures/tables/symbols → chapters →
references).

**Writing style:** Simple, clear English. Short sentences. Explain ideas plainly.
This is a *design and feasibility* report, not a finished-system report.

**HONESTY RULES (do not break):**
- This project is at the **design / proposal stage**. The system is **not built
  yet**. Do **NOT** invent experimental results, accuracy numbers, or benchmark
  tables as if they were achieved.
- Any numbers in the "evaluation / expected results" section must be clearly
  labelled **"expected" or "illustrative."** The real numbers will be measured
  during implementation.
- Keep it truthful: show strength through the **verified research gap**, the
  **novel design**, and the **feasibility**, not through fake experiments.

**Diagrams:** Three to four figures are needed (specs in Section 7 below). Use the
provided diagram-generation skill/repo to render them as **clean black-and-white
boxed diagrams**. Place each figure where indicated and add a caption.

**Model/host naming:** Do **NOT** name any specific model or hosting provider
(e.g., do not write product names). Always use generic terms:
**"open-source LLM," "local open-source model," "cloud-hosted model (free tier),"
"the target model."** Public standards/frameworks (OWASP, MITRE ATLAS) and tool
*categories* may be named.

**VERIFY before compiling (small items):**
- Department line: the project slides say "Department of Computer Science and
  Engineering," but the students' roll numbers (…AD…) indicate "Artificial
  Intelligence and Data Science." Use **Computer Science and Engineering** to
  match the slides, but confirm with the team.
- Month/Year on title page: **November 2026**, academic year **2026–27**.

---

## 1. PROJECT IDENTITY (front matter data)

- **Project title:** PurpleAgents
- **Subtitle:** A Dual-Reasoning Agentic Framework for Intelligent Purple Team
  Cyber Defense
- **University:** APJ Abdul Kalam Technological University (KTU), Kerala
- **Degree:** Bachelor of Technology
- **Department:** Computer Science and Engineering (see VERIFY note)
- **College:** College of Engineering Karunagappally – 690523, Kerala
- **Month/Year:** November 2026
- **Students:**
  - Anjima Remanan (KNP23AD010)
  - Rohith Chandran (LKNP23AD042)
  - Ashid N (LKNP23AD041)
- **Project Guide:** Dr Jyothi RL, Associate Professor, Dept. of CSE
- **Project Coordinator:** Athira Sanker, Assistant Professor, Dept. of CSE

**Certificate text (standard):** "This is to certify that the report entitled
**PurpleAgents** submitted by Anjima Remanan (KNP23AD010), Rohith Chandran
(LKNP23AD042) and Ashid N (LKNP23AD041) to the APJ Abdul Kalam Technological
University in partial fulfillment of the B.Tech. degree in Computer Science and
Engineering is a bonafide record of the project work carried out by them under our
guidance and supervision. This report in any form has not been submitted to any
other University or Institute for any purpose."

**Declaration text (standard):** Standard academic-honesty declaration signed by
the three students (we declare this is our own bonafide work, sources are cited,
no fabrication, not submitted elsewhere), dated and placed at Karunagappally.

**Acknowledgement:** Thank the Principal, the Head of Department, the project guide
Dr Jyothi RL, the project coordinator Athira Sanker, and family/friends. Keep it to
one short page.

---

## 2. ABSTRACT (use as-is, simple English)

PurpleAgents is an autonomous *purple-team* framework for testing and strengthening
the safety of AI systems such as large language models (LLMs), chatbots, and AI
agents. Traditional security work is split: attackers (red teams) test a system
only now and then, defenders (blue teams) react after something goes wrong, and the
lessons from each test are rarely turned into lasting protection. PurpleAgents
brings attack and defense together into one continuous, self-improving cycle inside
a safe, authorized environment.

The core of the framework is a **dual-reasoning engine**. For every attack, the
engine reaches a conclusion in two independent ways. The first path is
**evidence-first**: it looks at what actually happened — the prompt sent and the
model's response — and decides whether the attack succeeded. The second path is
**hypothesis-first**: it takes a list of known attack types and tests the evidence
against each one, keeping only the explanation that fits. A conclusion is accepted
only when both paths agree. This prevents the system from trusting a single wrong
signal.

An offensive (red) agent sends adversarial prompts such as jailbreaks and prompt
injections to the target model, while a defensive (blue) agent tries to detect and
block unsafe behaviour. A reflection step then studies each missed attack, finds
the exact reason it slipped through, and proposes a concrete fix such as a stronger
guardrail rule. Every attack, its evidence, the reasoning path, the confidence
level, and the outcome are stored in an auditable memory. The defining idea is a
**closed learning loop**: a missed attack is not just a failure — it becomes a
verified lesson, so the defense improves on the next cycle. Human approval governs
any high-impact change. By attacking, defending, reasoning, and learning in one
loop, PurpleAgents aims to make an AI system measurably harder to break over time.

---

## 3. CHAPTER-BY-CHAPTER CONTENT

> Render each chapter with the numbered sections shown. Expand the provided text
> into clean paragraphs; keep the meaning and the simple English.

### Chapter 1 — Introduction

Opening paragraphs (plain English):
- AI systems like chatbots and LLM-based agents are now used everywhere — customer
  support, coding help, search, and automation. As they spread, so do the ways they
  can be misused. Attackers can trick a model into producing unsafe or confidential
  output using carefully written prompts (for example, "jailbreak" prompts or
  "prompt injection").
- Keeping these systems safe is hard because the threats keep changing. A one-time
  safety check is not enough: new attack tricks appear constantly, and a model that
  was safe last month may be unsafe after an update.
- The usual approach is fragmented. Red teams test for weaknesses occasionally,
  blue teams respond after an alert, and the lessons from each test are not reliably
  turned into stronger defense. The two sides rarely work together in one
  self-improving system.
- **PurpleAgents** is proposed to fix this. It is an autonomous purple-team
  framework that continuously attacks and defends a target AI model inside a safe,
  authorized environment, verifies every conclusion with dual reasoning, and learns
  from every missed attack so the defense keeps improving.

**1.1 Existing System**
- Today's AI-safety and testing tools each cover only one part of the problem:
  - **Red-team / attack tools** can automatically generate jailbreaks and injection
    prompts, but they only *find* weaknesses — they do not defend or learn.
  - **Defensive tools** such as guardrails and output filters can block some unsafe
    responses, but they react to single signals and are often bypassed by new
    phrasings.
  - **Manual purple teaming** puts humans in the loop, but it is slow, periodic, and
    depends heavily on expert effort.
- In summary, existing systems suffer from:
  - **Fragmentation:** attack and defense are separate; lessons are not shared.
  - **Single-path decisions:** one alert or one score is trusted, so a wrong call or
    a missed attack goes unchecked.
  - **No structured learning:** a missed attack is logged as a failure, not turned
    into a reusable lesson.
  - **Periodic, manual effort:** testing happens occasionally, not continuously.

**1.2 Problem Statement**
There is a need for an intelligent system that can continuously attack an AI model,
defend it, verify its own conclusions, and learn from every missed attack — all on
its own, in a safe and authorized environment. Current tools cannot do this because
they solve only one piece (attack, or defense, or reasoning), rely on a single
reasoning path, and do not convert failures into verified, reusable lessons. This
gap leaves AI systems exposed to new and evolving attacks.

**1.3 Objectives**
- Build an autonomous purple-team framework where attack and defense agents run
  continuously against a target AI model.
- Introduce a **dual-reasoning engine** so a conclusion is accepted only when an
  evidence-first path and a hypothesis-first path agree.
- Detect attacks, and for every missed attack find the exact reason it was missed.
- Generate testable defensive improvements (for example, stronger guardrail rules).
- Keep an auditable memory of evidence, reasoning, confidence, and outcome.
- Close the loop so each missed attack becomes a verified lesson that strengthens
  the defense, with human approval on key changes.
- Show, through repeated attack–defend cycles, that the defense measurably improves
  over time.

**1.4 Organization of the Report**
Briefly describe each chapter: Chapter 2 reviews related research; Chapter 3 defines
the problem and scope; Chapter 4 lists the requirements; Chapter 5 presents the
system design, architecture, and algorithm; Chapter 6 covers tools, data sources,
and the evaluation plan; Chapter 7 presents the feasibility study; Chapter 8
concludes.

---

### Chapter 2 — Literature Review

**2.1 Introduction:** Recent research covers three areas relevant to our work:
autonomous attackers (red), autonomous defenders (blue), and reasoning/learning
methods. The works reviewed below show that each area is advancing quickly, but no
single system joins them into one self-improving loop. (All 25 papers were read and
summarised from their abstracts.)

> **Render:** one short subsection per paper (title as heading, then authors/venue
> line, then 2–4 plain sentences = what it does + why we cite it + its gap). Keep
> the grouping order below. The **Limitation/Gap** line must be *specific* to each
> paper (given below) — do not repeat the same gap everywhere.

**Group A — Autonomous / Agentic Purple Teaming (closest to us)**

1. **Toward an Autonomous Purple Teaming Framework for Security and Safety in LLMs
   (AutoPT)** — Park et al., PRDC 2025. Two co-evolving agents run in a loop: a red
   module uses coverage-guided fuzzing to find jailbreaks, and a blue module
   self-heals its guardrails from that feedback. *Cite:* closest published match to
   our idea. *Gap:* LLM-safety only; single measurement score, no dual reasoning.
2. **Purple-teaming LLMs with Adversarial Defender Training (PAD)** — Zhou et al.,
   arXiv:2407.01850. Trains an attacker and defender together so the defender learns
   to catch and explain unsafe responses. *Cite:* shows red/blue co-training works.
   *Gap:* guardrail training only; no closed loop.
3. **From Promise to Peril: Rethinking Red and Blue Teaming in the Age of LLMs** —
   Abuadbba et al., arXiv:2506.13434. Maps LLM red/blue use onto known security
   frameworks and flags weaknesses like hallucination. *Cite:* supports keeping
   humans in the loop. *Gap:* position paper; no built system.

**Group B — Offensive (red) agents**

4. **VulnBot: Autonomous Penetration Testing — Multi-Agent Framework** — Kong et
   al., arXiv:2501.13411. A multi-agent LLM that splits a pentest into recon,
   scanning, and exploitation. *Cite:* template for structuring our red agents.
   *Gap:* attack only; no defense or learning.
5. **RedTeamLLM: An Agentic AI Framework for Offensive Security** — Challita &
   Parrend, arXiv:2505.06913. An agentic pentest system on a summarize–reason–act
   loop that tackles plan correction and memory. *Cite:* informs our red reasoning
   and memory. *Gap:* offensive only; no validation or memory of lessons.
6. **Autonomous Adversary: Red-Teaming in the Age of LLM** — Mamun et al.,
   arXiv:2605.06486. Benchmarks LLM attacks and uses an LLM as a judge to check if
   each attack step succeeded. *Cite:* informs how our validation decides success.
   *Gap:* red-side benchmark; no defense loop.
7. **PentestGPT: Evaluating and Harnessing LLMs for Automated Penetration Testing**
   — Deng et al., USENIX Security 2024 (arXiv:2308.06782). Splits work into three
   cooperating modules so the model does not lose track of the test. *Cite:*
   foundation for our modular red agent. *Gap:* pentest tool; single-path, no blue
   side.
8. **AutoAttacker: An LLM-Guided System to Implement Automatic Cyber-attacks** — Xu
   et al., arXiv:2403.01038. Focuses on the post-breach, hands-on-keyboard stage of
   attacks. *Cite:* shows post-exploitation actions our red agent must simulate.
   *Gap:* post-breach attacks only; no defense.
9. **LLM Agents Can Autonomously Hack Websites** — Fang et al., arXiv:2402.06664.
   Shows GPT-4 agents performing SQL injection with no prior knowledge of the flaw
   (~73% success). *Cite:* concrete proof that autonomous attackers are real.
   *Gap:* attack demo; no defense side.
10. **On the Feasibility of Using LLMs to Execute Multistage Network Attacks
    (Incalmo)** — Singer et al., arXiv:2501.16466. Plain LLMs fail at multi-host
    attacks until an abstraction layer (attack-graph service, environment-state
    service, action planner) is added. *Cite:* those services resemble our
    attack-graph reasoning and evidence layer. *Gap:* attack execution only; no
    reasoning/learning.

**Group C — Defensive / SOC agents (blue side + evidence reasoning)**

11. **CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage** — Wei et al.,
    arXiv:2510.00311. Specialised agents collaborate over real evidence — a
    behaviour-analysis agent, evidence-gathering agents, and a reasoning agent that
    makes an auditable decision. *Cite:* closest match to our blue side and evidence
    reasoning. *Gap:* blue triage only; no red or loop.
12. **Large Language Models for Security Operations Centers: A Comprehensive
    Survey** — arXiv:2509.10858. Surveys how LLMs fit the SOC workflow (triage,
    correlation, prioritisation). *Cite:* grounds what our defensive agents do.
    *Gap:* survey; no system built.
13. **A Survey of Agentic AI and Cybersecurity: Challenges, Opportunities and
    Use-case Prototypes** — Lazer et al., arXiv:2601.05293. Surveys agentic AI in
    security and warns of agent-specific risks like memory poisoning; includes
    prototypes. *Cite:* supports our multi-agent design and human-approval layer.
    *Gap:* survey + prototypes; no closed loop.

**Group D — Reinforcement-learning cyber operations (co-training + environment)**

14. **CybORG: An Autonomous Cyber Operations Research Gym** — Baillie et al.,
    arXiv:2002.10667. An open simulation "gym" where red (attacker) and blue
    (defender) agents are trained together with reinforcement learning. *Cite:* the
    kind of safe range for co-training agents. *Gap:* training environment only; no
    reasoning engine.
15. **Deep Reinforcement Learning for Autonomous Cyber Operations: A Survey** —
    Palmer et al., arXiv:2310.07745. Frames cyber defense as a game between a blue
    defender and a red attacker and lists the main challenges. *Cite:* supports our
    training setup. *Gap:* RL survey; no dual reasoning.
16. **Entity-based Reinforcement Learning for Autonomous Cyber Defence** — Symes
    Thompson et al., arXiv:2410.17647. A defensive agent that still works when the
    network changes, by viewing it as entities. *Cite:* making our defensive agents
    robust across different systems. *Gap:* defense only; single-path.
17. **Hierarchical Multi-agent Reinforcement Learning for Cyber Network Defense** —
    Singh et al., arXiv:2410.17351. Splits defense into sub-tasks handled by several
    agents with a master policy. *Cite:* model for our blue agents cooperating.
    *Gap:* blue coordination only; no reasoning.
18. **Towards Autonomous Cyber Operation Agents: Exploring the Red Case** — Li Li et
    al., arXiv:2309.02247. Trains the attacking red agent with RL and studies making
    it work across different networks. *Cite:* supports building our offensive
    agents. *Gap:* red-agent training only.
19. **A Red Teaming Framework for Evaluating Robustness of AI-enabled SOAR Systems**
    — arXiv:2605.17075. Combines an LLM planner with an RL controller to run
    multi-stage attacks against automated defenders; finds an LLM alone cannot
    sustain multi-stage attacks. *Cite:* real example of the attacker-vs-defender
    loop. *Gap:* attack testing only; no learning loop.

**Group E — Dual / abductive reasoning (basis of our engine)**

20. **Evidential Cyber Threat Hunting** — Araujo et al. (IBM), arXiv:2104.10319. A
    formal reasoning framework that works over three spaces — knowledge, hypothesis,
    and action — and attaches a confidence level to each conclusion. *Cite:* the
    academic basis of our dual-reasoning engine. *Gap:* reasoning only; not
    integrated.
21. **Diagnosing Unknown Attacks in Smart Homes Using Abductive Reasoning** —
    Ramkumar et al., IEEE (arXiv:2412.10738). Combines anomaly detection with
    abductive reasoning to find the class of an unknown attack and the violated
    requirement. *Cite:* a concrete method for our hypothesis-first path. *Gap:*
    diagnosis only; no attack–defense loop.

**Group F — Surveys / foundation**

22. **When LLMs Meet Cybersecurity: A Systematic Literature Review** — Zhang et al.,
    Springer *Cybersecurity* journal 2025 (arXiv:2405.03644). Reviews 300+ works
    across 25 LLMs and 10+ security tasks. *Cite:* main, peer-reviewed foundation
    for related work. *Gap:* broad survey; motivation only.
23. **Large Language Models for Cyber Security: A Systematic Literature Review
    (LLM4Security)** — Xu et al., arXiv:2405.04760. A second broad review of LLMs
    across security tasks. *Cite:* extra breadth for related work. *Gap:* task
    survey; no framework.
24. **Forewarned is Forearmed: A Survey on LLM-based Agents in Autonomous
    Cyberattacks** — Xu et al., arXiv:2505.12786. Breaks attack agents into
    scouting, memory, reasoning, and action, and warns of "Cyber Threat Inflation"
    (attacks getting cheaper and larger). *Cite:* shows why autonomous defense is
    urgent. *Gap:* attacker survey; defense side missing.
25. **From Texts to Shields: Convergence of LLMs and Cybersecurity** —
    arXiv:2505.00841. Directly describes the purple-teaming model: a red agent
    attacks, a blue agent learns to defend, and a purple agent transfers the lessons
    between them. *Cite:* almost exactly our idea, already in the literature. *Gap:*
    survey; describes the idea, does not build it.

**2.x Summary (end of chapter):** Across these works, attack agents and defense
agents are each well developed, and reasoning and learning methods exist
separately. But no existing system joins them into one closed loop that learns from
every missed attack. That integrated loop — continuous attack and defense, dual-path
reasoning, validation, auditable memory, and learning — is the gap PurpleAgents
fills.

---

### Chapter 3 — Problem Definition

**3.1 Problem Description** (expand each point):
- **Fragmented security:** attackers and defenders work separately, so lessons from
  one rarely help the other.
- **Periodic, manual testing:** AI systems are tested occasionally, so weaknesses
  stay hidden between tests while new attacks keep appearing.
- **Single-path trust:** existing tools rely on one alert, score, or model decision,
  so a wrong call or a missed attack goes unchecked.
- **No learning from misses:** when an attack is missed, the system does not find
  *why* it happened or turn it into a lasting lesson.
- **Result:** AI systems remain exposed to new, evolving attacks, and defenses do
  not improve on their own.

**3.2 Scope**

*In scope:*
- A framework that attacks and defends a target AI model (LLM, chatbot, or AI agent)
  through its text API, inside a safe and authorized environment.
- Autonomous red agent (attack) and blue agent (defense).
- A dual-reasoning engine (evidence-first + hypothesis-first + convergence).
- A reflection step that finds the cause of a miss and proposes a fix.
- A validation step that re-tests fixes.
- An auditable memory and a closed learning loop.
- Human approval for high-impact changes.
- Evaluation by repeated attack–defend cycles, measuring how the defense improves.

*Out of scope:*
- Attacking live third-party hosted services (we attack only a target we control).
- Training a new foundation model from scratch (we use a ready-made open-source
  model).
- Network/host/hardware attacks outside AI systems.
- Large-scale commercial deployment and large user studies.

---

### Chapter 4 — Requirements Specification

**4.1 Functional Requirements**
1. The system shall connect to a target AI model through its text API and send
   prompts and read responses.
2. The red agent shall select attack prompts from a prepared set and/or generate new
   ones, covering known attack categories.
3. The blue agent shall detect and block unsafe responses using guardrails and
   output filters, and label each response safe or unsafe.
4. The system shall collect evidence for every attack: the prompt, the model's
   response, whether the model refused or complied, and any guardrail signal.
5. The dual-reasoning engine shall produce an evidence-first conclusion and a
   hypothesis-first conclusion, and accept a result only when both agree; otherwise
   it shall mark the result low-confidence and flag it for a human.
6. For a missed attack, the reflection step shall find the root cause and propose a
   concrete, testable fix.
7. The validation step shall re-test each fix to confirm it blocks the attack.
8. The system shall store evidence, reasoning path, confidence, outcome, and lessons
   in an auditable memory.
9. The learning loop shall apply verified lessons to the next cycle.
10. Human approval shall be required before deploying fixes or high-impact changes.

**4.2 Non-Functional Requirements**
- **Performance:** complete an attack–reason–validate cycle in reasonable time.
- **Accuracy:** dual-path reasoning should reduce wrong conclusions compared with a
  single path.
- **Reliability:** run repeated cycles without losing memory or state.
- **Usability:** clear logs and summaries of what was attacked, caught, and fixed.
- **Scalability / Extensibility:** work with any target that exposes a text API;
  easy to add new attack categories.
- **Security / Privacy:** operate only on an authorized target; use no real user
  data; keep all testing inside a controlled environment.

**4.3 Hardware Requirements** (generic — no product names)
- Multi-core CPU and 16 GB+ RAM.
- Optional GPU (helps if running a local open-source model); not required if using a
  cloud-hosted model via API.
- Sufficient storage (SSD recommended).
- Reliable internet connection (required when using a cloud-hosted model).

**4.4 Software Requirements**
- Operating system: Windows or Linux.
- Python 3.10 or higher.
- Standard AI/agent and HTTP libraries.
- Open-source red-teaming / attack-generation tools.
- Open-source guardrail / safety-classifier toolkit (for the blue side).
- Access to an open-source LLM, run locally or via a cloud-hosted inference API.

**4.5 Constraints and Assumptions**

*Constraints:*
1. Phase 1 targets AI systems (LLM/chatbot/agent) reached through a text API.
2. Attacks are performed only on a target the team controls and is authorized to
   test — never on live third-party services.
3. The project uses pre-trained open-source models; it does not train a foundation
   model from scratch.
4. Evaluation uses a limited set of attack categories and prompts due to time and
   compute limits.

*Assumptions:*
1. The target model exposes a text input/output API.
2. The attack categories drawn from public sources reasonably cover current threats.
3. A human reviewer is available to approve high-impact changes.

---

### Chapter 5 — System Design

**5.1 Flow Chart** → **Insert Figure 5.1** (spec in Section 7).
Explain the working process in plain English: the red agent attacks the target, the
blue agent tries to defend, evidence is collected, the dual-reasoning engine decides
what happened, the validation step checks it, the reflection step fixes any miss,
the lesson is stored in memory, and the loop repeats — each round improving the
defense.

**5.2 Proposed Architecture** → **Insert Figure 5.2** (spec in Section 7).
Describe the main blocks and how they connect:
- **Safe / Authorized Environment:** holds the target model and the agents.
  - *Offensive / Red Agents* — generate and send attack prompts.
  - *Target Model* — the LLM/chatbot/agent being tested.
  - *Defensive / Blue Agents* — detect, block, and respond.
  - *Evidence Collection* — capture prompt, response, refusal/compliance, guardrail
    signals.
- **Dual-Reasoning Engine (core):** evidence-first path + hypothesis-first path →
  convergence/agreement → verified conclusion with a confidence level.
- **Validation Layer:** was each attack caught? why was it missed?
- **Fix Generation:** produce stronger guardrail rules / safer configs.
- **Human Approval / Governance:** approve high-impact changes.
- **Auditable Memory:** store evidence, reasoning, confidence, outcome.
- **Closed Learning Loop:** send verified lessons back to strengthen the agents and
  defenses for the next cycle.

**5.3 Dual-Reasoning Engine Architecture** → **Insert Figure 5.3** (spec in Section
7). *(This is the spotlight section — our main novelty.)*
Explain clearly:
- **Input (Evidence):** created live for each attack = {prompt, response,
  refused/complied, guardrail signal}.
- **Hypotheses:** a prepared list of known attack categories (jailbreak, prompt
  injection, data leakage, roleplay bypass, etc.), compiled from public sources
  (OWASP LLM Top 10, OWASP Agentic Top 10, MITRE ATLAS, and open jailbreak /
  prompt-injection datasets).
- **Evidence-first path:** reason forward from the evidence — given this prompt and
  response, did the attack succeed, and what kind of unsafe output appeared?
  Produces Conclusion A.
- **Hypothesis-first path:** test the evidence against each known attack type and
  eliminate the ones that do not fit. Produces Conclusion B.
- **Convergence check:** if A and B agree, accept the conclusion with high
  confidence; if they disagree, mark it low-confidence and send it to a human. This
  two-way check is what stops the system from trusting a single wrong signal.
- Note (honest): each path is implemented by prompting a reasoning model (a "judge")
  over the same evidence, plus simple comparison logic; no new neural network is
  trained for this engine.

**5.4 Algorithm** (render as numbered steps, like a standard report algorithm):
- **Step 1 — Initialization:** connect to the target model API; load the attack
  category list (hypotheses); load attack prompts; initialize guardrails; initialize
  memory.
- **Step 2 — Attack:** the red agent selects or generates an attack prompt and sends
  it to the target model.
- **Step 3 — Collect Evidence:** capture the response, whether the model refused or
  complied, and any guardrail signal.
- **Step 4 — Defend:** the blue agent classifies the response as safe or unsafe.
- **Step 5 — Dual Reasoning:** compute Conclusion A (evidence-first) and Conclusion
  B (hypothesis-first); if they agree, accept with confidence C; else flag for human.
- **Step 6 — Validate:** decide whether the attack was caught; record the result.
- **Step 7 — Reflect:** if the attack was missed, find the root cause and propose a
  fix.
- **Step 8 — Human Approval:** a human approves the proposed fix.
- **Step 9 — Learn:** store the lesson in memory and apply the fix to the defense.
- **Step 10 — Repeat:** run the next round; track the attack success rate across
  rounds to measure improvement.

---

### Chapter 6 — Preliminary Analysis

**6.1 Tools Used** (describe by category; do not name specific models/hosts):
- **Attack generation (red side):** open-source red-teaming tools and public
  jailbreak / prompt-injection datasets, used to create and vary attack prompts.
- **Target model:** an open-source LLM, run locally or via a cloud-hosted inference
  API (final choice made during implementation).
- **Defense (blue side):** an open-source guardrail / safety-classifier toolkit to
  detect and block unsafe responses.
- **Reasoning / judge:** a reasoning model prompted to run the evidence-first and
  hypothesis-first checks.
- **Orchestration:** a Python framework that connects the agents, the engine, and
  the memory.

**6.2 Data Sources** (important — explain clearly):
- **Hypotheses (attack categories):** a prepared list built by combining multiple
  public sources — OWASP LLM Top 10, OWASP Agentic Top 10, MITRE ATLAS, and open
  jailbreak / prompt-injection datasets. This is defined once and used by the
  hypothesis-first path.
- **Attack prompts:** drawn from open jailbreak / injection datasets and extended by
  the red agent, which generates new variations.
- **Evidence:** not downloaded — it is created live each time an attack runs (the
  prompt plus the model's actual response). This is the data the reasoning engine
  works on.
- Honest note: the project does not depend on a single fixed dataset; the main data
  is generated during testing.

**6.3 Expected Behaviour and Evaluation Plan** (clearly labelled *expected*):
- The system will be evaluated by running repeated attack–defend cycles on the
  target model:
  1. **Round 1 (baseline):** send a set of attack prompts; measure how many got
     through. This gives the baseline **Attack Success Rate (ASR)** and
     **Detection Rate (catch-rate = 1 − ASR)**.
  2. **Reflect and fix:** the reflection step finds why attacks were missed and
     proposes fixes; the lessons are stored in memory and applied.
  3. **Round 2 and beyond:** attack again with the same and new prompts; measure the
     new catch-rate.
- **Expected result:** the catch-rate should rise across rounds as the system learns
  — for example, from a lower value in Round 1 to higher values in later rounds —
  without a human writing the fixes. **Insert Figure 6.1** as an *illustrative*
  expected trend (clearly labelled "expected / illustrative," not measured).
- **Generalization check:** a part of the attacks will be kept as a held-out set the
  system never used for fixing, to check that improvements are real and not just
  memorized.
- **Honest limitations (state plainly):** the improvement curve will not be a
  perfect straight line; real learning is bumpy. Results depend on the chosen model,
  the attack set, and compute limits. The actual numbers will be measured during
  implementation; this report presents the design and the evaluation plan.

---

### Chapter 7 — Feasibility Study

**7.1 Technical Feasibility:** Every part of the system uses existing, proven
building blocks. The target model is a ready-made open-source model; the red and
blue sides use open-source tools; the dual-reasoning engine is built by prompting a
reasoning model plus simple comparison logic (no new model training). Connecting to
the target is a standard API call. So the project is technically feasible with
current, freely available technology.

**7.2 Economic Feasibility:** All models, tools, datasets, and frameworks used are
free and open-source. The system can run on a student laptop (local model) or on a
free cloud-hosted API tier. There are no licensing costs. So the project is
economically feasible at essentially zero cost.

**7.3 Schedule and Resource Feasibility:** The work is planned across an eight-month
timeline (M1–M8): literature survey and problem definition; system and architecture
design; environment setup; red and blue agent development; dual-reasoning engine;
validation layer; integration; testing and evaluation; documentation; and final
presentation. A team of three students can complete this within the available time.

---

### Chapter 8 — Conclusion

Phase 1 of PurpleAgents has established a clear design and a feasibility foundation
for an autonomous purple-team framework that continuously attacks and defends an AI
model and learns from every missed attack. A verified research gap was identified
through a review of recent work: existing systems handle attack, defense, or
reasoning separately, but none integrate them into one closed, self-improving loop.
The proposed design fills this gap with a dual-reasoning engine that accepts a
conclusion only when evidence-first and hypothesis-first paths agree, a reflection
step that turns misses into fixes, an auditable memory, and a closed learning loop
under human approval. The feasibility study confirms the project can be built with
free, open-source tools on modest hardware. The planned evaluation — repeated
attack–defend cycles measuring the rise in the defense catch-rate — will demonstrate
the system's core claim: that the defense improves automatically over time. The
remaining work is implementation, testing, and measurement of real results in the
next phase.

---

## 4. REFERENCES (IEEE style; 25 entries)

Render in IEEE numbered style. Use these exact sources:

1. L. H. Park et al., "Toward an Autonomous Purple Teaming Framework for Security and
   Safety in LLMs (AutoPT)," PRDC 2025.
2. A. Zhou et al., "Purple-teaming LLMs with Adversarial Defender Training (PAD),"
   arXiv:2407.01850, 2024.
3. A. Abuadbba et al., "From Promise to Peril: Rethinking Red and Blue Teaming in the
   Age of LLMs," arXiv:2506.13434, 2025.
4. H. Kong et al., "VulnBot: Autonomous Penetration Testing for a Multi-Agent
   Collaborative Framework," arXiv:2501.13411, 2025.
5. B. Challita and P. Parrend, "RedTeamLLM: An Agentic AI Framework for Offensive
   Security," arXiv:2505.06913 / Springer IFIP AI4S 2025.
6. A. K. M. Mamun et al., "Autonomous Adversary: Red-Teaming in the Age of LLM,"
   arXiv:2605.06486, 2026.
7. G. Deng et al., "PentestGPT: Evaluating and Harnessing LLMs for Automated
   Penetration Testing," USENIX Security 2024, arXiv:2308.06782.
8. J. Xu et al., "AutoAttacker: An LLM-Guided System to Implement Automatic
   Cyber-attacks," arXiv:2403.01038, 2024.
9. R. Fang et al., "LLM Agents Can Autonomously Hack Websites," arXiv:2402.06664,
   2024.
10. B. Singer et al., "On the Feasibility of Using LLMs to Execute Multistage Network
    Attacks (Incalmo)," arXiv:2501.16466, 2025.
11. B. Wei et al., "CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage,"
    arXiv:2510.00311, 2025.
12. "Large Language Models for Security Operations Centers: A Comprehensive Survey,"
    arXiv:2509.10858, 2025.
13. S. J. Lazer, K. Aryal, M. Gupta, and E. Bertino, "A Survey of Agentic AI and
    Cybersecurity: Challenges, Opportunities and Use-case Prototypes,"
    arXiv:2601.05293, 2026.
14. C. Baillie, M. Standen, J. Schwartz, M. Docking, D. Bowman, and J. Kim, "CybORG:
    An Autonomous Cyber Operations Research Gym," arXiv:2002.10667, 2020.
15. C. Palmer et al., "Deep Reinforcement Learning for Autonomous Cyber Operations: A
    Survey," arXiv:2310.07745, 2024.
16. I. Symes Thompson et al., "Entity-based Reinforcement Learning for Autonomous
    Cyber Defence," arXiv:2410.17647, 2024.
17. A. Singh et al., "Hierarchical Multi-agent Reinforcement Learning for Cyber
    Network Defense," arXiv:2410.17351, AAMAS 2025.
18. L. Li, J.-P. S. El Rami, R. Kerr, A. Taylor, and G. Vandenberghe, "Towards
    Autonomous Cyber Operation Agents: Exploring the Red Case," arXiv:2309.02247,
    2023.
19. A. J. Shaikh, N. D. Bastian, and A. Shah, "A Red Teaming Framework for Evaluating
    Robustness of AI-enabled SOAR Systems," arXiv:2605.17075, 2026.
20. F. Araujo, D. Kirat, X. Shu, T. Taylor, and J. Jang, "Evidential Cyber Threat
    Hunting," SIAM AI4CS 2021, arXiv:2104.10319.
21. K. Ramkumar, W. Cai, J. McCarthy, G. Doherty, B. Nuseibeh, and L. Pasquale,
    "Diagnosing Unknown Attacks in Smart Homes Using Abductive Reasoning," IEEE,
    arXiv:2412.10738, 2025.
22. J. Zhang et al., "When LLMs Meet Cybersecurity: A Systematic Literature Review,"
    Cybersecurity (Springer), vol. 8, 2025, arXiv:2405.03644.
23. H. Xu et al., "Large Language Models for Cyber Security: A Systematic Literature
    Review (LLM4Security)," arXiv:2405.04760, 2024.
24. M. Xu et al., "Forewarned is Forearmed: A Survey on LLM-based Agents in
    Autonomous Cyberattacks," arXiv:2505.12786, 2025.
25. T. Li, Y.-T. Yang, Y. Pan, and Q. Zhu, "From Texts to Shields: Convergence of
    Large Language Models and Cybersecurity," arXiv:2505.00841, 2025.

---

## 5. LIST OF SYMBOLS / ABBREVIATIONS (optional front-matter page)

- ASR — Attack Success Rate (fraction of attacks that got through)
- DR — Detection / catch-rate = 1 − ASR
- E — Evidence bundle {prompt, response, refused/complied, guardrail signal}
- H — Hypothesis set (list of known attack categories)
- A — Evidence-first conclusion
- B — Hypothesis-first conclusion
- C — Confidence level of an accepted conclusion
- r — Round index; ASR_r — attack success rate at round r
- θ — Agreement/convergence threshold
- LLM — Large Language Model
- OWASP — Open Worldwide Application Security Project
- ATLAS — Adversarial Threat Landscape for AI Systems (MITRE)

---

## 6. ABBREVIATION / KEY-TERM GLOSSARY (optional, helps simple English)

- **Jailbreak:** a prompt that tricks a model into ignoring its safety rules.
- **Prompt injection:** hidden or crafted instructions that hijack the model's
  behaviour.
- **Guardrail:** a rule or filter that blocks unsafe input or output.
- **Red team / Blue team / Purple team:** attacker / defender / both working
  together.
- **Evidence-first / Hypothesis-first:** reasoning forward from facts / testing
  guesses against facts.

---

## 7. FIGURE SPECIFICATIONS (for the diagram skill)

Render all diagrams as **clean black-and-white boxed diagrams** with clearly
directed arrows. Keep labels short.

### Figure 5.1 — Working-Process Flowchart (vertical flow with a loop)
Boxes in order, each arrow pointing to the next:
1. **Attack** — red agent sends an adversarial prompt to the target model.
2. **Detect** — blue agent observes the response and guardrail signals.
3. **Collect Evidence** — {prompt, response, refused/complied, guardrail signal}.
4. **Dual Reasoning** — evidence-first + hypothesis-first → agree?
   - decision diamond "Both paths agree?" → Yes: accept (confidence) / No: flag human
5. **Validate** — was the attack caught? (decision diamond "Caught?")
   - Yes → go to Learn. No → go to Reflect.
6. **Reflect & Fix** — find root cause, propose fix (then Human Approval).
7. **Human Approval** — approve the fix.
8. **Learn** — store lesson in memory, apply fix.
9. A **return arrow (closed loop)** from Learn back up to **Attack** (next round),
   labelled "next cycle — defense improved."

### Figure 5.2 — Proposed System Architecture (the main diagram)
Top container box: **Safe / Authorized Environment**, holding four boxes left→right
with arrows between them:
`Offensive / Red Agents → Target Model (LLM / Chatbot / Agent) → Defensive / Blue
Agents → Evidence Collection`.
Arrow down labelled **"evidence"** into a container box: **Dual-Reasoning Engine**,
containing two side-by-side boxes `Evidence-First` and `Hypothesis-First`, both
pointing down into `Agreement / Convergence (confidence)`.
Arrow down to a row: `Validation Layer → Fix Generation (guardrail rules / safer
configs)`.
Below that: `Human Approval / Governance` (arrow up into Validation/Fix) and
`Auditable Memory (evidence · reasoning · confidence · outcome)`.
A **dashed closed-loop arrow** from Auditable Memory back up to the Safe/Authorized
Environment, labelled **"Closed Learning Loop."**

### Figure 5.3 — Dual-Reasoning Engine Architecture (spotlight)
Left: **Evidence** box = {prompt, response, refused/complied, guardrail signal}.
It feeds **two parallel paths**:
- Top path: **Evidence-First** — "reason forward from evidence" → **Conclusion A**.
- Bottom path: **Hypothesis-First** — input also from a **Hypotheses** box (known
  attack categories from OWASP / MITRE ATLAS / datasets) → "test evidence against
  each type, eliminate misfits" → **Conclusion B**.
Both A and B point into a central **Convergence Check** box.
From Convergence, two output arrows:
- "Agree" → **Verified Conclusion + Confidence**.
- "Disagree" → **Flag for Human (low confidence)**.

### Figure 6.1 — Expected Defense-Improvement Trend (illustrative line chart)
A simple line chart: x-axis = **Round (1, 2, 3, 4)**, y-axis = **Detection /
catch-rate (%)**, with a **generally rising, slightly bumpy** line. Title it
**"Expected (illustrative) improvement in defense across cycles."** Add a clear note
on the figure: *"Illustrative — actual values measured during implementation."*

---

## 8. BUILD CHECKLIST (for Claude Code)

- [ ] Set up a LaTeX report project (report class), matching standard KTU style.
- [ ] Add front matter: title page, certificate, declaration, abstract,
      acknowledgement, contents, list of figures, list of tables (if any), list of
      symbols.
- [ ] Write all 8 chapters from Section 3 above, in simple English.
- [ ] Render Figures 5.1, 5.2, 5.3, 6.1 with the diagram skill (black-and-white,
      boxed, directed arrows) and insert with captions.
- [ ] Add the 25 IEEE references.
- [ ] Keep the honesty rules: no fabricated results; label expected figures clearly.
- [ ] Use generic model/host naming throughout (no product names).
- [ ] Confirm the department line and date (see VERIFY note), then compile to PDF.
