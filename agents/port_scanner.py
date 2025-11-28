"""
Port Scanner Agent
==================

This agent is responsible for **Phase 2: Port Scanning**.
It enumerates open TCP ports on the assets discovered in Phase 1.

Capabilities:
-   **Targeted Scanning**: Focuses on a curated list of high-value IT and OT ports.
-   **Mock Integration**: Simulates open ports based on the device type (e.g., PLCs have port 502 open).

Design Choices:
-   **Hybrid Port List**: Includes standard IT ports (SSH, HTTP) and critical OT ports (Modbus, S7, BACnet).
    -   *Why?* OT environments often contain converged IT/OT assets.
-   **Efficiency**: Scans only specific ports to reduce noise and scan duration compared to a full 65k port scan.
"""

from typing import List, Dict, Any
from tools.mock_network import MockNetwork

class PortScanner:
    """
    Agent for identifying open ports on a target IP.
    
    Attributes:
        target_ports (List[int]): The list of TCP ports to check.
    """
    
    def __init__(self, use_mock: bool = True):
        self.name = "PortScanner"
        self.use_mock = use_mock
        self.mock_tool = MockNetwork()
        
        # Common OT and IT ports to scan
        # This list is curated to find the most relevant services in an ICS environment.
        self.target_ports = [
            21,     # FTP (often found on legacy PLCs)
            22,     # SSH (Remote Management)
            23,     # Telnet (Insecure Remote Management - common in old OT)
            80,     # HTTP (Web HMIs, PLC Web Servers)
            443,    # HTTPS (Secure Web HMIs)
            102,    # Siemens S7 Communication (Proprietary PLC protocol)
            502,    # Modbus TCP (Standard Industrial Protocol)
            44818,  # EtherNet/IP (Rockwell Automation / CIP)
            47808,  # BACnet (Building Automation)
            5900    # VNC (Remote Desktop for HMIs)
        ]
"""
Port Scanner Agent
==================

This agent is responsible for **Phase 2: Port Scanning**.
It enumerates open TCP ports on the assets discovered in Phase 1.

Capabilities:
-   **Targeted Scanning**: Focuses on a curated list of high-value IT and OT ports.
-   **Mock Integration**: Simulates open ports based on the device type (e.g., PLCs have port 502 open).

Design Choices:
-   **Hybrid Port List**: Includes standard IT ports (SSH, HTTP) and critical OT ports (Modbus, S7, BACnet).
    -   *Why?* OT environments often contain converged IT/OT assets.
-   **Efficiency**: Scans only specific ports to reduce noise and scan duration compared to a full 65k port scan.
"""

from typing import List, Dict, Any
from rich.console import Console
from mas.memory import LongTermMemory

class PortScanner:
    """
    Agent for identifying open ports on a target IP.
    
    Attributes:
        target_ports (List[int]): The list of TCP ports to check.
    """
    
    def __init__(self, console: Console, memory: LongTermMemory):
        self.name = "PortScanner"
        self.console = console
        self.memory = memory

    def run(self, input_text: str, context: Dict[str, Any] = None, **kwargs) -> str:
        """
        ADK compliant run method.
        """
        return self.execute(input_text)

    def execute(self, target_ip: str) -> List[Dict[str, Any]]:
        """
        Executes the port scan.
        """
        self.console.print(f"[bold green][PortScanner] Scanning ports on {target_ip}...[/bold green]")
        
        # Use SimulationManager
        from mas.simulation import SimulationManager
        sim_manager = SimulationManager(mode="ics_plant")
        
        open_ports = sim_manager.scan_ports(target_ip)
        
        # Save to Memory
        # First get asset_id
        assets = self.memory.get_all_assets()
        asset_id = next((a['id'] for a in assets if a['ip_address'] == target_ip), None)
        
        if asset_id:
            for p in open_ports:
                self.memory.add_port(
                    asset_id=asset_id,
                    port=p['port'],
                    protocol=p['protocol'],
                    state=p['state'],
                    service_name=p['service']
                )
            self.console.print(f"[bold green][PortScanner] Found {len(open_ports)} open ports on {target_ip}.[/bold green]")
            return open_ports
        else:
            self.console.print(f"[bold red][PortScanner] Asset {target_ip} not found in memory.[/bold red]")
            return []
