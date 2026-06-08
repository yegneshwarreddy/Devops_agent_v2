# DevOps Agent V1 🚀

A local AI-powered DevOps assistant built using LangChain, Ollama, Docker, Kubernetes, and PostgreSQL memory.

---

## Overview

DevOps Agent V1 is a command-line AI agent that can perform Docker and Kubernetes operational tasks using tool calling.

The agent uses:

* LangChain Agents
* Ollama (Llama 3)
* Docker CLI
* Kubernetes CLI (kubectl)
* PostgreSQL for conversation persistence

This project was built primarily for learning:

* LangChain Fundamentals
* Tool Calling
* Agent Architectures
* PostgreSQL Memory
* Docker Automation
* Kubernetes Automation

---

## Features

### Docker Tools

#### Container Operations

* List running containers
* List all containers
* Start container
* Stop container
* Restart container
* Remove container
* Inspect container
* View container logs
* View container resource usage

#### Image Operations

* List images
* Pull images
* Inspect images
* Remove images

#### Network Operations

* List networks
* Inspect networks

#### Volume Operations

* List volumes
* Inspect volumes

#### System Operations

* Docker version
* Docker system information
* Docker disk usage

---

### Kubernetes Tools

#### Pod Operations

* List pods
* Describe pod
* View pod logs
* Delete pod

#### Deployment Operations

* List deployments
* Describe deployment
* Restart deployment

#### Service Operations

* List services
* Describe services

#### Node Operations

* List nodes
* Describe node

#### Cluster Operations

* List namespaces
* View cluster events
* Cluster information
* Cluster version

---

## Architecture

```text
User
  │
  ▼
main.py
  │
  ▼
LangChain Agent
  │
  ├──────────────► Docker Tools
  │
  ├──────────────► Kubernetes Tools
  │
  ▼
PostgreSQL Memory
```

---

## Project Structure

```text
Devops_agent/

├── agents/
│   └── devops_agent.py
│
├── database/
│   └── postgres.py
│
├── memory/
│   └── postgres_memory.py
│
├── tools/
│   ├── docker_tools.py
│   └── k8s_tools.py
│
├── utils/
│   ├── command_runner.py
│   └── memory_debugger.py
│
├── LLM/
│   └── ollama_llm.py
│
├── main.py
│
└── requirements.txt
```

---

## Memory Architecture

### Sessions Table

Stores conversations.

```sql
sessions
```

| Column     |
| ---------- |
| session_id |
| created_at |

---

### Chat Messages Table

Stores messages.

```sql
chat_messages
```

| Column     |
| ---------- |
| id         |
| session_id |
| role       |
| content    |
| created_at |

---

## Database Relationships

```text
sessions
---------
session_id (PK)

        │
        │
        ▼

chat_messages
---------
id (PK)
session_id (FK)
role
content
created_at
```

---

## Technologies Used

### AI

* LangChain
* Ollama
* Llama 3

### Infrastructure

* Docker
* Kubernetes

### Database

* PostgreSQL
* psycopg2

### Language

* Python 3.12+

---

## Running The Agent

### Start Ollama

```bash
ollama serve
```

---

### Pull Model

```bash
ollama pull llama3
```

---

### Run Agent

```bash
python main.py
```

---

## Example Prompts

### Docker

```text
List all running containers

Get logs of nginx

Show docker images

Inspect container nginx

Restart container nginx

Show docker system information
```

---

### Kubernetes

```text
List all pods

Describe pod nginx

Show pod logs

List deployments

Restart deployment frontend

Show cluster info
```

---

## Current Limitations

### V1 Limitations

* No confirmation workflow for destructive actions
* No workflow orchestration
* No multi-step planning
* No human approval node
* No structured outputs
* No RBAC controls
* No streaming responses
* No observability/tracing

---

## Lessons Learned

This project helped understand:

* LLMs
* Tool Calling
* LangChain Agents
* Agent Memory
* PostgreSQL Persistence
* Docker Automation
* Kubernetes Automation

---

# Version Roadmap

## V1 (Current)

✅ LangChain Agent

✅ Docker Tools

✅ Kubernetes Tools

✅ PostgreSQL Memory

✅ Session Management

---

## V2 (Next)

Planned migration to LangGraph.

Features:

* LangGraph Workflows
* Human Approval Nodes
* Safety Layer
* Multi-step Planning
* Structured Outputs
* Better Error Handling
* Agent State Management
* Tool Routing Logic

---

Built as a learning project to understand how real-world AI-powered DevOps agents are designed and implemented.
