"""
Network Scanner Agent
=====================

This agent is responsible for **Phase 1: Network Discovery**.
Its primary goal is to identify active hosts on the target network range.

Capabilities:
-   **ARP Scanning**: Uses Address Resolution Protocol (Layer 2) to find live hosts on the local subnet.
-   **Mock Integration**: Supports a simulated mode for safe testing without generating real network traffic.

Design Choices:
-   **Layer 2 Focus**: ARP is preferred for local networks as it is less likely to be blocked by host firewalls than ICMP (Ping).
-   **Simplicity**: Returns a clean list of IP/MAC/Vendor tuples for downstream agents to consume.
"""

from typing import List, Dict, Any
from rich.console import Console
from mas.memory import LongTermMemory
from google_local.adk.agents import Agent
from tools.mock_network import MockNetwork

class NetworkScanner(Agent):
    """
    Agent for discovering devices on a network.
    """
    
    def __init__(self, console: Console = None, memory: LongTermMemory = None, use_mock: bool = True, mock_tool: Any = None):
        super().__init__(name="NetworkScanner", instruction="Scan network for assets.")
        self.console = console or Console()
        self.memory = memory
        self.use_mock = use_mock
        self.mock_tool = mock_tool if mock_tool else MockNetwork()

    def run(self, input_text: str, context: Dict[str, Any] = None, **kwargs) -> str:
        """
        ADK compliant run method.
        """
        # For NetworkScanner, input_text is the network range
        return self.execute(input_text)

    def execute(self, network_range: str) -> List[Dict[str, Any]]:
        """
        Executes the network scan.
        """
        self.console.print(f"[bold green][NetworkScanner] Scanning network: {network_range}...[/bold green]")
        
        if self.use_mock:
            # Use the injected mock tool directly
            assets = self.mock_tool.arp_scan(network_range)
        else:
            # Real implementation would go here
            assets = []
        
        # Save to Memory if available
        if self.memory:
            for asset in assets:
                self.memory.add_asset(
                    ip_address=asset['ip'], 
                    mac_address=asset['mac'], 
                    vendor=asset['vendor']
                )
            
        self.console.print(f"[bold green][NetworkScanner] Found {len(assets)} devices.[/bold green]")
        return assets
