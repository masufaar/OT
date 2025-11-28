"""
Nmap Agent Module
=================

This agent is responsible for **Phase 6: Nmap Scripting**.
It leverages the Nmap Scripting Engine (NSE) to perform advanced enumeration and vulnerability scanning.

Capabilities:
-   **Targeted Scripting**: Automatically selects the correct NSE script based on the service (e.g., `s7-info` for Siemens S7).
-   **Deep Enumeration**: Extracts detailed information that standard banner grabbing misses (e.g., PLC module types, firmware versions).
-   **Mock Integration**: Simulates NSE output for specific scripts and targets.

Design Choices:
-   **Service-Aware**: The agent is "smart" enough to know which script applies to which port/service.
-   **Safety First**: We only run "safe" and "discovery" category scripts by default to avoid crashing sensitive OT equipment.
"""

from typing import Dict, Any, Optional
from tools.mock_network import MockNetwork

class NmapAgent:
    """
    Agent for running Nmap NSE scripts.
    
    Attributes:
        use_mock (bool): If True, uses the MockNetwork tool.
    """
    
    def __init__(self, use_mock: bool = True):
        self.name = "NmapAgent"
        self.use_mock = use_mock
        self.mock_tool = MockNetwork()

    def run_nse(self, ip_address: str, port: int, service: str) -> Optional[Dict[str, Any]]:
        """
        Runs Nmap Scripting Engine (NSE) scripts based on the service.
        
        Args:
            ip_address (str): The target IP.
            port (int): The target port.
            service (str): The service name (e.g., "s7", "modbus", "ssh").
            
        Returns:
            Optional[Dict[str, Any]]: Script name and output if successful, else None.
        """
        script_name = self._select_script(service, port)
        if not script_name:
            return None

        print(f"[{self.name}] Selected script '{script_name}' for {service} on {ip_address}:{port}...")
        
        if self.use_mock:
            # Simulate NSE execution
            output = self.mock_tool.run_nse_script(ip_address, port, script_name)
            if output:
                print(f"[{self.name}] Script Execution Success.")
                return {"script": script_name, "output": output}
        else:
            # TODO: Implement python-nmap script execution
            # Real implementation: nm.scan(ip, arguments=f'-p {port} --script {script_name}')
            pass
            
        return None

    def _select_script(self, service: str, port: int) -> Optional[str]:
        """
        Selects the appropriate NSE script based on service name or port.
        
        This mapping ensures we only run relevant scripts.
        """
        service = service.lower()
        if "s7" in service or port == 102:
            return "s7-info"
        if "modbus" in service or port == 502:
            return "modbus-discover"
        if "ssh" in service or port == 22:
            return "ssh-auth-methods"
        if "bacnet" in service or port == 47808:
            return "bacnet-info"
        return None
