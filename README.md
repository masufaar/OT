# OT Penetration Testing Multi-Agent System (MAS)

## 📌 Overview
The **OT Penetration Testing MAS** is an autonomous, multi-agent system designed to perform comprehensive security assessments of Operational Technology (OT) environments. It leverages a team of specialized AI agents to discover assets, identify vulnerabilities, and simulate exploitation in a controlled, safe manner.

## 🚀 Key Features
*   **Multi-Agent Architecture**: Orchestrated team of specialized agents (Network, Port, Service, Web, SNMP, Nmap, Metasploit, ICS, Writer, Critic).
*   **Advanced Tooling**:
    *   **OpenAPI Support**: Dynamic ingestion of API specifications.
    *   **MCP Integration**: Compatible with Model Context Protocol.
    *   **Code Execution**: Sandboxed Python execution for complex calculations.
    *   **Custom Tools**: Specialized scanners for OT protocols (Modbus, S7).
*   **Safety First**:
    *   **Human-in-the-Loop (HITL)**: Critical actions (exploits, active scans) require explicit user approval.
    *   **State Serialization**: Robust Pause/Resume capabilities for long-running operations.
*   **Production Ready**:
    *   **Persistence**: SQLite-backed session and memory management.
    *   **Observability**: Structured logging, tracing, and metrics.
    *   **Deployment**: Dockerized and Kubernetes-ready (GKE).
    *   **A2A Protocol**: Exposes the system as a service to other agents.

## 🏗️ Architecture
The system follows a **Hub-and-Spoke** architecture:
*   **Orchestrator (RootAgent)**: The central brain that manages the workflow, context, and safety gates.
*   **Agents**: Specialized workers (e.g., `NetworkScanner`, `MetasploitAgent`) treated as tools.
*   **Memory**: Centralized Long-Term Memory (SQLite) for sharing findings.
*   **Quality Manager**: Monitors agent performance and ensures output quality.

## 🛠️ Setup & Usage

### Prerequisites
*   Python 3.11+
*   Docker (optional)

### Local Installation
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the simulation:
    ```bash
    python main.py --auto-approve
    ```

### Docker Deployment
1.  Build the image:
    ```bash
    docker build -t mas-agent .
    ```
2.  Run with Docker Compose:
    ```bash
    docker-compose up
    ```

### Kubernetes Deployment
1.  Apply manifests:
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

## 🧪 Verification
Run the comprehensive test suite:
```bash
# Run Unit Tests
pytest tests/

# Run Network Simulations
python tests/simulate_constellations.py
```

## 📄 Documentation
*   [Walkthrough](walkthrough.md): Detailed implementation log.
*   [Board Quality Report](board_quality_report.md): Executive summary.
*   [Requirements Analysis](requirements_gap_analysis.md): Feature gap tracking.
