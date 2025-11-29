# OT Penetration Testing Multi-Agent System (MAS)

## 📌 Overview
The **OT Penetration Testing MAS** is an autonomous, multi-agent system designed to perform comprehensive security assessments of Operational Technology (OT) environments. It leverages a team of specialized AI agents to discover assets, identify vulnerabilities, and simulate exploitation in a controlled, safe manner.

[![Watch the Demo](https://img.youtube.com/vi/oFEb1cM6eIs/0.jpg)](https://www.youtube.com/watch?v=oFEb1cM6eIs)
[![Watch the Demo 2](https://img.youtube.com/vi/qYvpMzTdjEs/0.jpg)](https://www.youtube.com/watch?v=qYvpMzTdjEs)

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

## 🤖 Agent Roles & Workflow

The system operates in a **9-Phase Sequential Workflow**, orchestrated by the `RootAgent`. Each phase is handled by a specialized agent or a sub-loop of agents.

### 1. Network Discovery Phase
*   **Agent**: `NetworkScanner`
*   **Role**: Identifies active hosts on the target subnet using ARP scanning (Layer 2).
*   **Output**: List of live IP addresses, MAC addresses, and Vendor IDs.

### 2. Port Scanning Phase
*   **Agent**: `PortScanner`
*   **Role**: Scans identified hosts for open TCP ports.
*   **Interaction**: Consumes the list of IPs from Phase 1.

### 3. Service Scanning Phase
*   **Agent**: `ServiceScanner`
*   **Role**: Connects to open ports to grab banners and identify running services (e.g., Modbus, HTTP, SSH).
*   **Interaction**: Consumes open ports from Phase 2.

### 4. SNMP Scanning Phase
*   **Agent**: `SnmpScanner`
*   **Role**: Enumerates SNMP-enabled devices (UDP 161) to gather system information (OIDs, Community Strings).
*   **Interaction**: Targets devices identified in Phase 1.

### 5. Web Scanning Phase
*   **Agent**: `WebScanner`
*   **Role**: Inspects HTTP/HTTPS services for default credentials, directory listing, and specific vulnerabilities.
*   **Interaction**: Targets ports 80/443/8080 identified in Phase 2.

### 6. Nmap Scripting Phase
*   **Agent**: `NmapAgent`
*   **Role**: Runs specialized NSE scripts (e.g., `s7-info`, `modbus-discover`) for deep protocol enumeration.
*   **Interaction**: Refines data for specific services found in Phase 3.

### 7. Exploitation Phase (Autonomous with HITL)
*   **Agent**: `MetasploitAgent`
*   **Role**: Matches findings to known exploits and attempts to verify vulnerabilities.
*   **Safety**: **CRITICAL**. Requires Human-in-the-Loop (HITL) approval via `ToolContext` before executing any high-risk action.

### 8. ICS Security Phase
*   **Agent**: `IcsAgent`
*   **Role**: Interacts with OT protocols (S7Comm, Modbus) to test control logic safety (e.g., Stop CPU, Write Coil).
*   **Safety**: Strictly controlled via safety gates.

### 9. Reporting Phase
*   **Agents**: `WriterAgent`, `CriticAgent`
*   **Role**: Synthesizes all findings into two reports:
    *   **Assessment Report**: Technical findings and risk matrix.
    *   **Remediation Report**: Strategic mitigation plan.
*   **Quality Assurance**: The `CriticAgent` uses a **different LLM** (e.g., `gemini-1.5-pro`) to act as an independent "Editor-in-Chief", ensuring unbiased validation of the `WriterAgent`'s output.

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

## 📄 Documentation & Reports

### 1. Board of Management (Non-IT)
*   **[AS-IS Vulnerability Assessment Report](assessment_report.pdf)**: High-level risk assessment detailing existing vulnerabilities and operational risks (No remediation details).
*   **[TO-BE Remediation & Strategy Report](remediation_report.pdf)**: Strategic roadmap, cost estimates, and mitigation strategies for decision makers.

### 2. IT Management & Technical Team
*   **[Final Technical Report](final_report.pdf)**: Complete technical analysis, exploit logs, and detailed findings.
*   **[Board Quality Report](board_quality_report.md)**: System performance metrics, agent reliability, and quality assurance data.

### 3. Project Artifacts
*   [Requirements Analysis](requirements_gap_analysis.md): Feature gap tracking.
*   [Walkthrough](walkthrough.md): Implementation log (Dev only).
