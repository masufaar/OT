"""
Service Scanner Agent
=====================

This agent is responsible for **Phase 3: Service Scanning**.
It takes the open ports found in Phase 2 and interrogates them to identify the running application and version.

Capabilities:
-   **Banner Grabbing**: Connects to ports and reads the initial welcome message (banner).
-   **Version Detection**: Parses banners to identify software versions (e.g., "Apache 2.4.41", "Siemens S7-1500").
-   **Mock Integration**: Returns simulated banners for known mock devices.

Design Choices:
-   **Granularity**: Knowing the exact version is crucial for identifying CVEs (Common Vulnerabilities and Exposures).
-   **Refinement**: Updates the generic "tcp/open" status from Phase 2 with specific service names like "http", "modbus", "ssh".
"""

from typing import Dict, Any
from tools.mock_network import MockNetwork

class ServiceScanner:
    """
    Agent for identifying services and versions on open ports.
    
    Attributes:
        use_mock (bool): If True, uses the MockNetwork tool.
    """
    
    def __init__(self, use_mock: bool = True):
        self.name = "ServiceScanner"
        self.use_mock = use_mock
        self.mock_tool = MockNetwork()

    def scan(self, ip_address: str, port: int = 0, tool_context: Any = None) -> Dict[str, Any]:
        """
        Identifies the service running on a specific port.
        
        Args:
            ip_address (str): The target IP.
            port (int): The target port.
            tool_context (Any): HITL context.
            
        Returns:
            Dict[str, Any]: A dictionary with 'service', 'version', and 'banner'.
        """
        print(f"[{self.name}] Scanning service on {ip_address}:{port}...")
        
        result = {
            "service": "unknown",
            "version": "unknown",
            "banner": ""
        }
        
        if self.use_mock:
            # Simulate banner grabbing
            banner_info = self.mock_tool.get_service_banner(ip_address, port)
            if banner_info:
                result.update(banner_info)
        else:
            # TODO: Implement real banner grabbing / nmap -sV
            # Real implementation would use socket.recv() or nmap's service detection engine.
            pass
            
        print(f"[{self.name}] Identified: {result['service']} ({result['version']})")
        return result
