# 🐍 GenAI Agents Infrastructure

![Build Status](https://img.shields.io/github/workflow/status/genai-works-org/genai-agentos/CI?label=Build&style=flat-square)
![License](https://img.shields.io/github/license/genai-works-org/genai-agentos?label=License&style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)
![Docker](https://img.shields.io/badge/docker-supported-blue?style=flat-square)

This repository provides a comprehensive infrastructure for running **GenAI Agents**, designed to streamline the development and deployment of AI-powered agents. The infrastructure includes:

- **Backend**: FastAPI-based backend for handling API requests.
- **Router**: WebSocket-based routing for agent communication.
- **Master Agents**: Core agents managing system workflows.
- **PostgreSQL Database**: Persistent storage for agent data and configurations.
- **Frontend**: React-based UI for interacting with the system.
- **CLI**: Command-line interface for managing agents and configurations.
- **Redis**: In-memory data store for caching and task queuing.
- **Celery**: Distributed task queue for asynchronous processing.

## 📎 Repository Link

👉 [GitHub Repository](https://github.com/genai-works-org/genai-agentos)

## 📚 Table of Contents

- [Repository Structure](#-repository-structure)
- [Supported Agent Types](#-supported-agent-types)
- [Prerequisites](#-prerequisites)
- [Local Setup](#-local-setup)
- [Supported Providers and Models](#-supported-providers-and-models)
- [Ngrok Setup (Optional)](#-ngrok-setup-optional)
- [GenAI Agent Registration](#-genai-agent-registration)
- [Environment Variables](#-environment-variables)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#%EF%B8%8F-license)

## 📂 Repository Structure

Explore the detailed README files for each component:

- [CLI](cli/README.md): Command-line interface for managing agents.
- [Backend](backend/README.md): API server for agent interactions.
- [Master Agents](master-agent/README.md): Core agents for system orchestration.
- [Router](router/README.md): WebSocket routing for agent communication.
- [Frontend](frontend/README.md): User interface for interacting with the system.

## 🧠 Supported Agent Types

The system supports multiple types of agents, each with specific integration protocols:

| Agent Type       | Description                                                                                   | Integration Method                                      |
|------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **GenAI Agents** | Agents connected via the [`genai-protocol`](https://pypi.org/project/genai-protocol/) library. | Configured through the CLI or UI.                      |
| **MCP Servers**  | Model Context Protocol servers for model interactions.                                        | Add via URL in the UI (e.g., `http://host.docker.internal:8000/mcp`). |
| **A2A Servers**  | Agent-to-Agent Protocol servers for inter-agent communication.                                | Add via URL in the UI (e.g., `http://host.docker.internal:10002`).    |

## 📦 Prerequisites

Ensure the following tools are installed before setting up the project:

- **[Docker](https://www.docker.com/)**: Containerization platform for running services.
- **[Docker Compose](https://docs.docker.com/compose/)**: Tool for defining and running multi-container Docker applications.
- **[`make`](https://www.gnu.org/software/make/)** (optional):
  - macOS: Install via `brew install make`
  - Linux: Install via `sudo apt-get install make`
- **Python 3.8+**: Required for running the CLI and agent scripts.
- **Git**: For cloning the repository.

## 🚀 Local Setup

Follow these steps to set up the infrastructure locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/genai-works-org/genai-agentos.git
   cd genai-agentම

2. **Configure Environment Variables**:

Copy the example .env file and customize it as needed:

   ```bash
   cp .env-example .env
   ```

   - A .env file is required for configuration.
   - Variables in .env-example are commented. Uncomment and modify the relevant lines to customize settings (e.g., database credentials, ports).

3. **Start Docker Desktop**:

Ensure Docker Desktop is running on your machine.

4. **Launch the Infrastructure**:

Use either of the following commands to start all services:

   ```bash
   make up
   ```

or

   ```bash
   docker compose up
   ```

5. **Access the Application**:

Once the services are running, access the following endpoints:

- **Frontend UI**: http://localhost:3000/
- **Swagger API Docs**: http://localhost:8000/docs#/

## 👾 Supported Providers and Models

The system currently supports the following AI providers and models:

- **OpenAI**: gpt-4o

Additional providers and models can be integrated by extending the genai-protocol library.

## 🌐 Ngrok Setup (Optional)

Ngrok allows you to expose your local WebSocket endpoint to the internet for testing or remote access.

### Install Ngrok

```bash
# macOS (Homebrew)
brew install ngrok/ngrok/ngrok

# Linux
sudo snap install ngrok
```

### Authenticate Ngrok

1. Sign up or log in at the [Ngrok Dashboard](https://dashboard.ngrok.com/)
2. Copy your authtoken from the "Your Authtoken" section
3. Configure Ngrok with the token:

```bash
ngrok config add-authtoken <YOUR_AUTH_TOKEN>
```

### Start a Tunnel

Expose the local WebSocket server running on port 8080:

```bash
ngrok http 8080
```

### Update WebSocket URL

Copy the generated WebSocket URL (e.g., `wss://<ngrok-id>.ngrok.io`) and update the ws_url field in:

```text
genai_session.session.GenAISession
```

## 🤖 GenAI Agent Registration

Quickly register and run a GenAI agent using the CLI. For detailed instructions, see CLI README.

### Navigate to the CLI Directory

```bash
cd cli/
```

### Register a New User

```bash
python cli.py signup -u <username>
```

Alternatively, register via the UI at http://localhost:3000/.

### Log In

```bash
python cli.py login -u <username> -p <password>
```

This returns a JWT token for authentication.

### Register an Agent

```bash
python cli.py register_agent --name <agent_name> --description <agent_description>
```

### Run the Agent

Navigate to the agents directory and run the agent script:

```bash
cd agents/
uvicorn run python <agent_name>.py
```

or

```bash
python <agent_name>.py
```

## 💎 Environment Variables

The following environment variables can be configured in the .env file:

| Variable | Description | Example / Default |
|----------|-------------|-------------------|
| FRONTEND_PORT | Port for the frontend service | 3000 |
| ROUTER_WS_URL | WebSocket URL for the router container | ws://genai-router:8080/ws |
| SECRET_KEY | Secret key for JWT and LLM config encryption | $(openssl rand -hex 32) |
| POSTGRES_HOST | PostgreSQL host | genai-postgres |
| POSTGRES_USER | PostgreSQL username | postgres |
| POSTGRES_PASSWORD | PostgreSQL password | postgres |
| POSTGRES_DB | PostgreSQL database name | postgres |
| POSTGRES_PORT | PostgreSQL port | 5432 |
| DEBUG | Enable/disable debug mode for server/ORM logging | True / False |
| MASTER_AGENT_API_KEY | API key for the Master Agent | e1adc3d8-fca1-40b2-b90a-7b48290f2d6a::master_server_ml |
| MASTER_BE_API_KEY | API key for the Master Backend | 7a3fd399-3e48-46a0-ab7c-0eaf38020283::master_server_be |
| BACKEND_CORS_ORIGINS | Allowed CORS origins for the backend | ["*"], ["http://localhost"] |
| DEFAULT_FILES_FOLDER_NAME | Default folder for file storage (Docker volume path) | /files |
| CLI_BACKEND_ORIGIN_URL | Backend URL for CLI access | http://localhost:8000 |

To override the default FRONTEND_PORT, run:

```bash
source FRONTEND_PORT=<your_port>
```

## 🛠️ Troubleshooting

### ❓ MCP Server or A2A Card URL Not Accessible by genai-backend

**✅ Solution**: If your MCP server or A2A card is hosted locally, replace `http://localhost:<your_port>` with `http://host.docker.internal:<your_port>` in the URL.

**🔎 Example:**
- MCP: `http://host.docker.internal:8000/mcp`
- A2A: `http://host.docker.internal:10002`

**⚠️ Note**: Do not append `/.well-known/agent.json` for A2A cards; the genai-backend handles this automatically.

### ❓ MCP Server with Valid Host Not Accessible

**✅ Solution:**
1. Ensure the MCP server supports the streamable-http protocol and is remotely accessible.
2. Verify the full URL is specified (e.g., `http://host.docker.internal:8000/mcp`).

**⚠️ Note**: The sse protocol is deprecated, and stdio is not yet supported. Stay tuned for updates.

## 🤝 Contributing

We welcome contributions to improve the GenAI Agents Infrastructure! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes appropriate tests.

## 📄️ License

This project is licensed under the MIT License.
