# 🏥 GenAI Healthcare Agent Orchestration Platform

## Overview

This project is an open-source, next-generation platform for orchestrating AI-powered agents to automate and streamline complex healthcare workflows. It enables seamless collaboration between specialized agents (Patient Intake, Medical Records, Diagnosis, Treatment Planning, Communication, etc.), external tools, and human-in-the-loop processes to deliver efficient, safe, and transparent healthcare solutions.

---

## Key Features

- **Multi-Agent Orchestration:** Coordinate multiple specialized agents in automated healthcare flows.
- **Agent Types Supported:**
  - **GenAI Agents:** Local Python agents for custom logic and LLM-powered reasoning.
  - **MCP Agents:** Integrate external tools/services (e.g., n8n, Claude Desktop) via the Multi-Component Protocol.
  - **A2A Agents:** Interoperate with other agent ecosystems using the Agent-to-Agent protocol.
- **Healthcare Workflow Automation:** Out-of-the-box flows for patient registration, triage, medical record retrieval, diagnosis, treatment planning, and patient/family communication.
- **External Tool Integration:** Easily connect to n8n for notifications, LLMs for advanced reasoning, and more.
- **Modern Tech Stack:** Python (FastAPI, SQLAlchemy, Celery), React, TypeScript, Tailwind CSS, PostgreSQL, Redis.
- **Explainability & Transparency:** All agent actions and reasoning are logged and visualized in the UI.
- **Extensible & Hackathon-Ready:** Modular design for rapid prototyping, easy addition of new agents, flows, or integrations.

---

## Example Use Case: Patient Care Flow

1. **Patient Intake Agent:** Registers a new patient, collects symptoms, and triages urgency.
2. **Medical Records Agent:** Retrieves and summarizes the patient’s medical history.
3. **Diagnostic Assistant Agent:** Suggests possible diagnoses and recommends tests.
4. **Treatment Plan Agent:** Proposes a treatment plan tailored to the diagnosis and patient context.
5. **Patient Communication Agent:** Notifies the patient’s emergency contact and provides updates.
6. **n8n Email Notification:** Sends a detailed email to the patient’s relative using an n8n workflow.

---

## Project Structure

- `backend/` — FastAPI backend, database, and core logic
- `frontend/` — React-based UI for healthcare professionals
- `cli/` — CLI for agent management, registration, and launching
  - `cli/agents/` — Directory for all agent implementations (e.g., patient_intake_agent, medical_records_agent, etc.)
- `master-agent/` — Orchestration logic for multi-agent flows
- `router/` — WebSocket and protocol routing
- `genai_agents_example/` — Example agents for reference

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/genai-works-org/genai-agentos.git
cd genai-agentos/
```

### 2. Environment Setup

Copy the example environment file and customize as needed:

```sh
cp .env-example .env
```

> Ensure Docker Desktop is running if using Docker.

### 3. Start the Infrastructure

```sh
make up
# or, alternatively
docker compose up
```

- Frontend UI: [http://localhost:3000/](http://localhost:3000/)
- API Docs: [http://localhost:8000/docs#/](http://localhost:8000/docs#/)

### 4. Register and Run Agents

#### Register a User and Login

```sh
cd cli/
python cli.py signup -u <username>
python cli.py login -u <username> -p <password>
```

#### Register an Agent

```sh
python cli.py register_agent --name <agent_name> --description <agent_description>
```

#### Install Agent Dependencies and Run

```sh
cd agents/<agent_name>
uv pip install .
python <agent_name>.py
```

---

## Integration with External Tools

- **n8n:** For automated email notifications and workflow automation.
- **Claude Desktop (Optional):** Route complex queries to external LLMs for advanced reasoning.

---

## Extending the Platform

- **Add New Agents:** Place new agent scripts in `cli/agents/` and register via the CLI.
- **Custom Flows:** Use the UI flow editor to design and visualize agent workflows.
- **External Integrations:** Register MCP or A2A agents to connect with external services.

---

## Why Use This Platform?

- **Automation:** Reduces manual work and speeds up patient processing.
- **Safety:** Ensures critical cases are triaged and escalated quickly.
- **Communication:** Keeps patients and families informed in real time.
- **Transparency:** Logs and visualizes every agent’s action for auditability.
- **Scalability:** Easily adapts to new use cases, agents, or integrations.

---

## Acknowledgements

Built with inspiration from the open-source GenAI, n8n, and agent orchestration communities.  
Special thanks to hackathon mentors, contributors, and testers.
