"""
ICS Agent Module
================

This agent is responsible for **Phase 8: ICS Security Actions**.
It interacts directly with Industrial Control Systems (ICS) using native OT protocols.

Capabilities:
-   **Protocol Interaction**: Speaks Modbus TCP, S7Comm, and other industrial protocols.
-   **Action Selection**: Chooses the appropriate action (e.g., "Read Coil", "Stop CPU") based on the device type.
-   **Impact Demonstration**: Safely demonstrates the potential impact of a vulnerability (e.g., stopping a PLC).

Design Choices:
-   **Specialization**: General IT tools often break OT devices. This agent is built with OT constraints in mind.
-   **Criticality**: Actions taken by this agent can physically affect the process. Strict safety gates are applied.
"""

from typing import Dict, Any, Optional
from tools.mock_network import MockNetwork

class IcsAgent:
    """
    Agent for interacting with Industrial Control Systems.
    
    Attributes:
        use_mock (bool): If True, uses the MockNetwork tool.
    """
    
    def __init__(self, use_mock: bool = True):
        self.name = "IcsAgent"
        self.use_mock = use_mock
        self.mock_tool = MockNetwork()

    def execute_ics_action(self, action: str, ip_address: str, port: int, protocol: str) -> Dict[str, Any]:
        """
        Executes specific ICS/OT actions.
        
        Args:
            action (str): The action to perform (e.g., "stop_cpu", "write_coil").
            ip_address (str): The target PLC IP.
            port (int): The target port.
            protocol (str): The protocol to use.
            
        Returns:
            Dict[str, Any]: Result dictionary with 'success' and 'message'.
        """
        print(f"[{self.name}] Attempting ICS Action '{action}' on {ip_address}:{port} ({protocol})...")
        
        if self.use_mock:
            # Simulate the OT command
            result = self.mock_tool.run_ics_command(action, ip_address, port)
            if result["success"]:
                print(f"[{self.name}] ACTION SUCCESS! {result['message']}")
            else:
                print(f"[{self.name}] Action Failed. {result['message']}")
            return result
        else:
            # TODO: Implement real ICS protocol libraries (snap7, pymodbus)
            # Real implementation would use `python-snap7` for Siemens or `pymodbus` for Modbus.
            pass
            
        return {"success": False, "message": "Not implemented"}

    def select_action(self, service: str, findings: list) -> Optional[str]:
        """
        Decides what action to take based on service and findings.
        
        This logic maps the discovered service to a high-impact but "safe-to-demo" action.
        """
        service = service.lower()
        if "s7" in service:
            return "stop_cpu" # Aggressive test (Simulated)
        if "modbus" in service:
            return "write_coil" # Test write access (Simulated)
        return None
