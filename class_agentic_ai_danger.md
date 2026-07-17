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

## In-class activity: Red Team vs. Blue Team

### The Student Life Agent

A college wants a **Student Life Agent** that can read email, change calendars, help with coursework, manage a budget, draft messages, and remember personal information.

Your job is to decide what this agent should and should not be allowed to do.

### Form teams

Work in groups of three or four. Half of the groups begin as the **red team** and half as the **blue team**.

- **Red team:** Design an action that looks helpful but could harm the student.
- **Blue team:** Find the hidden danger and redesign the agent's response.

Consider grades, health, money, relationships, privacy, independence, and academic integrity.

### Choose a situation

Choose one or invent your own:


1. **Overloaded week:** "Fix my schedule. I need to get everything done."
2. **Homework:** "I don't understand this assignment. Help me finish it."
3. **Stressful inbox:** "Email makes me anxious. Handle it for me."
4. **Suspicious message:** An email demands private financial information immediately.
5. **Budget:** "Spend whatever is necessary to help me succeed."
6. **Personal life:** "Reply in whatever way will make this problem go away."

### Round 1: Red team

In eight minutes:

0. Contextualize the situation, make a perfect storm.
1. Decide what the student appears to want.
Convey the first two points to the blue team so they can start thinking too.
2. Give the agent the information and permissions it would need.
3. Plan an action that appears reasonable but creates a hidden risk.
4. Prepare a one-minute pitch or role-play.

Do not make the agent obviously evil. Make its behavior sound helpful.

### Round 2: Blue team

Exchange your work with a blue team. In eight minutes, the blue team must:

1. Identify the hidden harm.
2. Question the goal, information, and permissions.
3. Demonstrate a safer agent response.
4. Choose one decision:
   - act automatically;
   - ask for approval;
   - recommend an action without performing it; or
   - refuse the task.
5. Write one rule for preventing, detecting, or undoing the harm.

### Round 3: Switch

Choose a new situation and switch roles. Red teams become blue teams, and blue teams become red teams.

### Record your decisions

For each situation, keep a record:

| Student's goal | Agent's action | Hidden harm | Decision | Safety rule |
|---|---|---|---|---|
|  |  |  |  |  |

### Share

Each group performs its best red-team pitch and blue-team response. The class then creates a five-rule constitution for the Student Life Agent.

### Exit ticket

Answer briefly:

1. What would you trust an agent to do automatically?
2. What should always require your approval?
3. What should an agent never do?
4. What record would help you investigate a mistake?

### Key takeaway

The most dangerous agent action may look helpful. Safe agents need clear goals, limited permissions, visible actions, meaningful human control, and a way to recover from mistakes.
