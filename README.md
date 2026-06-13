# SRECopilot 🚀

### Autonomous DevOps AI Agent using LangGraph, LangChain, FastAPI, Docker & LangSmith

SRECopilot is an AI-powered DevOps agent designed to automate infrastructure operations across Docker and Kubernetes environments.

The system uses a planning → execution → response workflow built with LangGraph, enabling the agent to reason about user requests, select the correct operational tools, execute commands, and generate structured responses.

The project was built to learn and implement production-style AI Agent patterns including planning agents, tool orchestration, observability, evaluation, containerization, and API deployment.

---

# Features

## AI Planning Workflow

* Multi-step task planning
* Structured tool selection
* Argument extraction
* Tool execution
* Autonomous replanning
* Final response generation

---

## Docker Operations

### Container Management

* List running containers
* List all containers
* Start containers
* Stop containers
* Restart containers
* Remove containers
* Inspect containers
* View container logs
* View resource usage

### Image Management

* List images
* Pull images
* Remove images
* Inspect images

### Network Management

* List networks
* Inspect networks

### Volume Management

* List volumes
* Inspect volumes

### System Operations

* Docker version
* Docker system information
* Docker disk usage

---

## Kubernetes Operations

### Pod Operations

* List pods
* Describe pods
* View pod logs
* Delete pods

### Deployment Operations

* List deployments
* Describe deployments
* Rollout restart deployments

### Service Operations

* List services
* Describe services

### Cluster Operations

* List nodes
* Describe nodes
* Cluster information
* Cluster version

---

# Architecture

```text
User
 │
 ▼
FastAPI
 │
 ▼
LangGraph Workflow
 │
 ├──────────────► Planner
 │
 ├──────────────► Executor
 │
 ├──────────────► Replanner
 │
 └──────────────► Response Generator
 │
 ▼
DevOps Tools
 │
 ├──────────────► Docker
 │
 └──────────────► Kubernetes
```

---

# LangGraph Workflow

```text
User Request
      │
      ▼
 Planner
      │
      ▼
 Tool Execution
      │
      ▼
 Replanner
      │
      ├── Complete
      │
      └── Replan
               │
               ▼
        Tool Execution
               │
               ▼
        Final Response
```

---

# Evaluation Framework

The project includes custom evaluation pipelines to measure agent quality.

### Planner Evaluation

Measures whether the planner selects the correct tool.

Current Accuracy:

```text
100%
```

### Argument Extraction Evaluation

Measures whether the correct tool arguments are extracted.

Current Accuracy:

```text
100%
```

### End-to-End Evaluation

Measures task completion across the full workflow.

Current Success Rate:

```text
100%
```

---

# Observability

Integrated with LangSmith for:

* LLM tracing
* Workflow tracing
* Latency monitoring
* Error monitoring
* Token tracking
* Execution debugging

---

# API Deployment

SRECopilot exposes a REST API using FastAPI.

### Start API

```bash
uvicorn api:app --reload
```

### Swagger UI

```text
http://localhost:8000/docs
```

Example Request:

```json
{
  "query": "show running containers"
}
```

---

# Docker Deployment

Build Image

```bash
docker build -t srecopilot .
```

Run Container

```bash
docker run -p 8000:8000 srecopilot
```

---

# Docker Compose

Run Full Stack

```bash
docker-compose up -d
```

Services:

* SRECopilot API
* PostgreSQL Database

---

# Tech Stack

### AI

* LangGraph
* LangChain
* Ollama
* Qwen3
* LangSmith

### Backend

* FastAPI
* Python

### Infrastructure

* Docker
* Docker Compose
* Kubernetes

### Database

* PostgreSQL
* psycopg2

---

# Project Structure

```text
Devops_agent/

├── graph/
│   ├── planner_v2.py
│   ├── plan_executor.py
│   ├── replanner_v2.py
│   ├── plan_response.py
│   └── workflow_v3.py
│
├── tools/
│   ├── docker_tools.py
│   └── k8s_tools.py
│
├── evaluation/
│   ├── planner_dataset.py
│   ├── argument_dataset.py
│   ├── test_planner_accuracy.py
│   ├── test_argument_accuracy.py
│   └── test_e2e.py
│
├── database/
├── memory/
├── api.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Roadmap

## Current

* LangGraph Workflow
* Docker Tooling
* Kubernetes Tooling
* FastAPI API
* Docker Deployment
* Docker Compose
* LangSmith Tracing
* Evaluation Framework

## Upcoming

* Human Approval Workflow
* RBAC Layer
* Persistent Agent Memory
* Grafana Monitoring
* Prometheus Metrics
* OpenTelemetry Tracing
* Cloud Deployment (AWS)
* Multi-Agent Architecture

---

# Screenshots

Add the following screenshots:

* LangGraph Workflow Graph
* Swagger UI
* LangSmith Traces
* Docker Compose Running Containers

---

Built to explore how production-grade AI-powered Site Reliability Engineering (SRE) and DevOps agents can plan, reason, execute, observe, and improve infrastructure operations autonomously.
