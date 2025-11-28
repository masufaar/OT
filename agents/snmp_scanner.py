"""
SNMP Scanner Agent
==================

This agent is responsible for **Phase 4: SNMP Scanning**.
Simple Network Management Protocol (SNMP) is a goldmine for reconnaissance in OT environments.

Capabilities:
-   **Community String Brute-forcing**: Checks for common default strings like "public", "private", "manager".
-   **System Enumeration**: Retrieves OIDs (Object Identifiers) for system description, uptime, and name.
-   **Mock Integration**: Simulates SNMP responses for specific mock assets.

Design Choices:
-   **High Value Target**: SNMP often reveals network topology, routing tables, and exact device models.
-   **Security Risk**: "public" read-only access is extremely common in legacy OT and is a finding in itself.
"""

from typing import Dict, Any, Optional
from tools.mock_network import MockNetwork

class SnmpScanner:
    """
    Agent for enumerating SNMP services.
    
    Attributes:
        use_mock (bool): If True, uses the MockNetwork tool.
    """
    
    def __init__(self, use_mock: bool = True):
        self.name = "SnmpScanner"
        self.use_mock = use_mock
        self.mock_tool = MockNetwork()

    def scan_snmp(self, ip_address: str) -> Optional[Dict[str, Any]]:
        """
        Scans for SNMP (UDP 161) and performs enumeration.
        
        Args:
            ip_address (str): The target IP.
            
        Returns:
            Optional[Dict[str, Any]]: SNMP data if found, else None.
        """
        print(f"[{self.name}] Checking SNMP on {ip_address}...")
        
        if self.use_mock:
            # Check if UDP 161 is "open" in our mock definition
            if self.mock_tool.check_snmp(ip_address):
                print(f"[{self.name}] SNMP Port 161/UDP is OPEN.")
                # Retrieve simulated OID values
                data = self.mock_tool.get_snmp_data(ip_address)
                print(f"[{self.name}] Enumeration Success: {data}")
                return data
            else:
                print(f"[{self.name}] SNMP Port 161/UDP is CLOSED.")
                return None
        else:
            # TODO: Implement pysnmp logic
            # Real implementation would use pysnmp to walk the MIB tree.
            pass
            
        return None
