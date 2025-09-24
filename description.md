# GenAI Agent Orchestration Platform for Healthcare

## Project Overview
This project is a next-generation, open-source agent orchestration platform designed to streamline and automate complex healthcare workflows using GenAI and multi-agent collaboration. The system enables seamless integration of AI-powered agents, external tools, and human-in-the-loop processes to deliver efficient, safe, and transparent healthcare solutions.

## Key Features
- **Multi-Agent Orchestration:** Coordinate multiple specialized agents (Patient Intake, Medical Records, Diagnostic Assistant, Treatment Planner, Communication, etc.) in a single, automated workflow.
- **Agent Types:**
  - **GenAI Agents:** Local Python agents for custom logic and LLM-powered reasoning.
  - **MCP Agents:** Integrate external tools/services (e.g., n8n, Claude Desktop) as callable agents via the Multi-Component Protocol.
  - **A2A Agents:** Support for Agent-to-Agent (A2A) protocol for interoperability with other agent ecosystems.
- **Healthcare Workflow Automation:** Out-of-the-box flows for patient registration, triage, medical record retrieval, diagnosis, treatment planning, and patient/family communication.
- **External Tool Integration:**
  - **n8n Integration:** Automatically send email notifications to patients or relatives using n8n workflows triggered by agent actions.
  - **LLM/Claude Desktop Ready:** Easily route complex queries to advanced LLMs or external reasoning engines.
- **Modern Tech Stack:**
  - **Backend:** Python, FastAPI, SQLAlchemy, Celery, WebSockets
  - **Frontend:** React, TypeScript, Tailwind CSS, Shadcn UI
  - **CLI:** Typer-based CLI for agent management and registration
- **Extensible & Hackathon-Ready:**
  - Easily add new agents, flows, or integrations
  - Modular design for rapid prototyping and experimentation
- **Explainability & Transparency:**
  - Each agent’s reasoning and actions are logged and can be visualized in the UI
- **Resilience & Error Handling:**
  - Graceful fallback and clear error messages for missing data or agent failures

## Example Use Case: Healthcare Patient Flow
1. **Patient Intake Agent:** Registers a new patient, collects symptoms, age, contact info, and triages urgency.
2. **Medical Records Agent:** Retrieves and summarizes the patient’s medical history.
3. **Diagnostic Assistant Agent:** Suggests possible diagnoses and recommends tests based on symptoms and history.
4. **Treatment Plan Agent:** Proposes a treatment plan tailored to the diagnosis and patient context.
5. **Patient Communication Agent:** Notifies the patient’s emergency contact and provides updates.
6. **n8n Email Notification:** Sends a detailed email to the patient’s relative using an n8n workflow triggered by the agent.

## Integration with External Tools
- **n8n:** Used for sending automated, customizable email notifications. The Patient Intake Agent triggers an n8n webhook with patient details, and n8n handles the email delivery.
- **Claude Desktop (Optional):** The system is designed to support routing complex queries to external LLMs like Claude Desktop via MCP, enabling advanced reasoning and second opinions.

## Technical Stack
- **Backend:** Python, FastAPI, SQLAlchemy, Celery, WebSockets
- **Frontend:** React, TypeScript, Tailwind CSS, Shadcn UI
- **CLI:** Typer
- **Database:** PostgreSQL
- **Task Queue:** Redis (for Celery)

## Extensibility & Hackathon Readiness
- **Add New Agents:** Create new agent scripts in the `cli/agents/` directory and register them via the CLI.
- **Custom Flows:** Use the flow editor to design and visualize custom agent workflows.
- **External Integrations:** Register MCP or A2A agents to connect with external services or agent networks.
- **Rapid Prototyping:** Modular architecture allows for quick iteration and experimentation.

## How This Improves Healthcare Workflows
- **Automation:** Reduces manual work and speeds up patient processing.
- **Safety:** Ensures critical cases are triaged and escalated quickly.
- **Communication:** Keeps patients and families informed in real time.
- **Transparency:** Logs and visualizes every agent’s action for auditability.
- **Scalability:** Easily adapts to new use cases, agents, or integrations.

## Unique & Innovative Aspects
- **Unified Multi-Agent Platform:** Supports GenAI, MCP, and A2A agents in a single orchestration engine.
- **Plug-and-Play Integrations:** Easily connect to tools like n8n, LLMs, or other agent networks.
- **Explainable AI:** Every agent’s reasoning is logged and can be reviewed.
- **Hackathon-Optimized:** Pre-configured for rapid setup, demo, and extension.

## Getting Started (High-Level)
1. **Clone the repository and install dependencies** (see README.md for details).
2. **Start backend, frontend, and required services** (PostgreSQL, Redis, n8n, etc.).
3. **Register and run agents** using the CLI.
4. **Design agent flows** in the UI and test with sample patient scenarios.
5. **(Optional) Integrate external tools** (e.g., n8n, Claude Desktop) as MCP agents.

## Acknowledgements
- Built with inspiration from the open-source GenAI, n8n, and agent orchestration communities.
- Special thanks to hackathon mentors, contributors, and testers.

---

For more details, see the project README and code documentation. 