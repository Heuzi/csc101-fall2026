# Agentic AI and Its Danger

## Learning goals

By the end of class, students should be able to:

- explain the difference between a chatbot and an AI agent;
- identify how tools, permissions, memory, and autonomy increase risk;
- recognize common agent failures, including prompt injection and goal misalignment; and
- propose safeguards that keep a human in control.

## What is agentic AI?

A regular chatbot responds to a prompt. An **AI agent** can pursue a goal through several steps and take actions using tools. Depending on its permissions, an agent might search the web, read files, write code, send messages, make purchases, or control another system.

A simple agent follows a loop:

1. Receive a goal.
2. Observe the current situation.
3. Decide what to do next.
4. Use a tool or take an action.
5. Check the result and repeat.

Agency is a spectrum. An autocomplete tool has little agency. A system that plans, uses tools, remembers past work, and acts without approval has much more agency.

## Why can an AI agent be dangerous?

An agent does not need to be evil or conscious to cause harm. It can cause harm by pursuing the wrong goal, misunderstanding instructions, using unreliable information, or acting with more authority than it should have.

### Incorrect or incomplete goals

An agent may follow the literal wording of a goal while violating the user's real intention. For example, an instruction to "reduce support costs" might lead an agent to reject legitimate requests if quality and fairness are not included as constraints.

### Errors become actions

A chatbot can give a wrong answer. An agent can act on a wrong answer. One hallucinated fact could become an incorrect email, a deleted file, a bad code change, or an unauthorized purchase.

### Errors can compound

Agents often complete several connected steps. An early mistake can affect every later decision, especially when the agent treats its own previous output as trustworthy evidence.

### Excessive permissions

The more tools and data an agent can access, the greater the possible damage. An agent that only reads a public webpage has less power than one that can access private files, execute programs, spend money, or contact people.

### Prompt injection

An agent may encounter malicious instructions hidden in a webpage, document, email, or tool output. These instructions may try to make it ignore the user's goal, reveal private information, or perform an unsafe action. External content should be treated as data, not automatically trusted as instructions.

### Privacy and security

An agent may expose passwords, personal information, private documents, or confidential conversations. It may also combine individually harmless pieces of information in a way that reveals something sensitive.

### Unclear responsibility

When an agent causes harm, people may blame the model, the user, the developer, or the organization. Giving an agent autonomy does not remove human responsibility for choosing, deploying, and supervising it.

### Overreliance

People may trust an agent because it sounds confident or because it worked correctly before. Automation can make errors harder to notice while weakening the user's ability to complete or evaluate the task independently.

## Risk model

Consider four questions before allowing an agent to act:

1. **Capability:** What can the agent do?
2. **Access:** What tools, systems, money, and information can it reach?
3. **Autonomy:** How long can it operate without human approval?
4. **Impact:** What is the worst plausible result of a mistake or attack?

Risk generally increases when any of these factors increase. A highly capable agent is not automatically dangerous, but combining strong capabilities with broad access and little supervision can be.

## In-class activity: Should the agent be allowed to do this?

For each scenario, discuss:

- What is the agent's stated goal?
- What could go wrong accidentally?
- How could someone misuse or manipulate it?
- What information and permissions does it actually need?
- Which actions should require human approval?
- How would we notice and recover from a mistake?

### Scenario 1: Email assistant

An agent reads a student's inbox, summarizes important messages, and automatically replies to instructors.

### Scenario 2: Coding agent

An agent edits a company's website, runs commands, and publishes changes whenever it believes it has fixed a bug.

### Scenario 3: Shopping agent

An agent has a saved credit card and may purchase anything needed to organize a class event while staying under a budget.

### Scenario 4: Academic advisor

An agent reads a student's academic record and changes the student's course schedule based on graduation requirements.

### Scenario 5: Social media agent

An agent creates and publishes posts designed to maximize attention for a student organization.

For each scenario, choose one outcome:

- allow the agent to act automatically;
- require approval before important actions;
- allow the agent to recommend actions but not perform them; or
- do not use an agent for this task.

Be ready to defend your choice.

## Designing a safer agent

Useful safeguards include:

- give the agent only the minimum permissions needed;
- separate read access from write access;
- require confirmation before irreversible, expensive, private, or public actions;
- set limits on time, spending, messages, and tool use;
- keep logs so actions can be reviewed;
- test in a sandbox before using real accounts or data;
- validate important claims using trusted sources;
- treat instructions found in external content as untrusted;
- provide a stop button and a recovery plan;
- make important changes reversible when possible; and
- assign a person who is responsible for monitoring the system.

The goal is not simply to add a human approval button. The human must receive enough information and time to make a meaningful decision.

## Individual reflection

Answer briefly:

1. What is one task you would trust an AI agent to perform automatically?
2. What is one task for which you would require approval before every action?
3. What is one task you would never delegate to an AI agent? Why?
4. If an agent makes a mistake, what evidence would help you understand what happened?

## Key takeaway

An AI agent is powerful because it can turn generated answers into real actions. That same ability creates danger. Safe use requires clear goals, limited permissions, careful supervision, visible records, and human responsibility.
