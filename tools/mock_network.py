"""
Mock Network Simulation Module
==============================

This module provides a realistic simulation of an Operational Technology (OT) network.
It allows the Multi-Agent System to be demonstrated safely without requiring access to real, physical hardware.

Simulated Environment:
-   **Subnet**: 192.168.1.0/24
-   **Assets**:
    1.  **Siemens S7-1500 PLC** (192.168.1.10): The "Brain" of the factory. Vulnerable to default creds.
    2.  **Schneider HMI** (192.168.1.20): The "Face" of the factory. Vulnerable to unauthenticated VNC/HTTP.
    3.  **Moxa Gateway** (192.168.1.30): Protocol converter. Vulnerable to SNMP info leakage.
    4.  **Workstation** (192.168.1.100): Generic PC.

Design Choices:
-   **Deterministic Behavior**: The simulation returns consistent results to ensure reproducible demos.
-   **Protocol Fidelity**: We simulate specific responses (e.g., S7Comm banners, Modbus outputs) to trick agents into thinking they are on a real network.
"""

from typing import List, Dict, Any

class MockNetwork:
    """
    Simulates an OT network for local testing.
    
    Attributes:
        devices (List[Dict]): The static list of simulated devices.
    """
    
    def __init__(self, devices: List[Dict[str, str]] = None):
        # Define the "Ground Truth" of our simulated network
        if devices is not None:
            self.devices = devices
        else:
            self.devices = [
                {"ip": "192.168.1.10", "mac": "00:1C:06:XX:XX:XX", "vendor": "Siemens", "type": "PLC"},
                {"ip": "192.168.1.20", "mac": "00:0C:29:XX:XX:XX", "vendor": "Schneider Electric", "type": "HMI"},
                {"ip": "192.168.1.30", "mac": "00:50:56:XX:XX:XX", "vendor": "Moxa", "type": "Gateway"},
                {"ip": "192.168.1.100", "mac": "00:00:00:00:00:00", "vendor": "Generic", "type": "Workstation"}
            ]

    def arp_scan(self, network_range: str, tool_context: Any = None) -> List[Dict[str, str]]:
        """
        Simulates an ARP scan (Layer 2 Discovery).
        
        Args:
            network_range (str): The target CIDR.
            tool_context (ToolContext, optional): Context for HITL requests.
            
        Returns:
            List[Dict]: Discovered devices if the range matches the mock subnet.
        """
        # HITL Check: If we have a context, use it to ask for permission
        if tool_context and not tool_context.tool_confirmation:
            tool_context.request_confirmation(
                hint=f"Starting active ARP scan on {network_range}. This may trigger IDS.",
                payload={"network": network_range}
            )
            # If denied (or just asked), we return empty or pending status. 
            # In a real async system, we'd pause. Here we just return empty if not confirmed.
            if not tool_context.tool_confirmation.confirmed:
                return []

        # Simple check to see if the agent is scanning the right network
        if "192.168.1" in network_range:
            # Simulate some randomness or latency if needed in future versions
            return self.devices
        return []

    def check_port(self, ip: str, port: int) -> bool:
        """
        Simulates checking if a TCP port is open (Port Scanning).
        
        This defines the "Attack Surface" of each device.
        """
        # Mock rules defining open ports per IP
        if ip == "192.168.1.10": # Siemens PLC
            # 102 (S7), 80/443 (Web), 502 (Modbus)
            return port in [102, 80, 443, 502]
        if ip == "192.168.1.20": # HMI
            # 80/443 (Web), 5900 (VNC)
            return port in [80, 443, 5900]
        if ip == "192.168.1.30": # Gateway
            # 22 (SSH), 80 (Web), 502 (Modbus)
            return port in [22, 80, 502]
        return False

    def get_service_banner(self, ip: str, port: int) -> Dict[str, str]:
        """
        Simulates service version detection (Banner Grabbing).
        
        Returns specific strings that look like real service banners.
        """
        if ip == "192.168.1.10": # Siemens PLC
            if port == 102: return {"service": "Siemens S7 Comm", "version": "S7-1500 v2.1"}
            if port == 80: return {"service": "HTTP", "version": "Siemens Web Server"}
            if port == 502: return {"service": "Modbus TCP", "version": "Simatic Modbus"}
            
        if ip == "192.168.1.20": # HMI
            if port == 5900: return {"service": "VNC", "version": "RealVNC 5.3"}
            if port == 80: return {"service": "HTTP", "version": "Apache 2.4"}

        if ip == "192.168.1.30": # Gateway
            if port == 22: return {"service": "SSH", "version": "OpenSSH 8.2"}
            if port == 502: return {"service": "Modbus TCP", "version": "Moxa Modbus Gateway"}
            
        return {"service": "unknown", "version": "unknown"}

    def check_snmp(self, ip: str) -> bool:
        """
        Simulates checking UDP 161 (SNMP).
        """
        # Only the Gateway and maybe the PLC have SNMP enabled
        return ip in ["192.168.1.10", "192.168.1.30"]

    def get_snmp_data(self, ip: str) -> Dict[str, str]:
        """
        Simulates SNMP enumeration.
        
        Returns OID-like values for system info.
        """
        if ip == "192.168.1.10":
            return {
                "community": "public",
                "sysName": "PLC_Main_Floor",
                "sysDescr": "Siemens S7-1500 FW:2.1",
                "sysContact": "admin@factory.local"
            }
        if ip == "192.168.1.30":
            return {
                "community": "public",
                "sysName": "GW_Area_1",
                "sysDescr": "Moxa MGate MB3180",
                "sysContact": "support@moxa.com"
            }
        return {}

    def check_web_auth(self, ip: str, port: int) -> bool:
        """
        Simulates checking if a web page requires login.
        """
        # Siemens PLC (192.168.1.10) requires login
        if ip == "192.168.1.10" and port == 80: return True
        # HMI (192.168.1.20) does NOT require login (misconfigured)
        if ip == "192.168.1.20" and port == 80: return False
        return False

    def web_login(self, ip: str, port: int, user: str, psw: str) -> bool:
        """
        Simulates login attempt.
        """
        if ip == "192.168.1.10" and user == "admin" and psw == "admin":
            return True
        return False

    def scrape_web(self, ip: str, port: int) -> Dict[str, str]:
        """
        Simulates scraping valuable info from a web page.
        """
        if ip == "192.168.1.10":
            return {"firmware": "v2.1", "serial": "S7-1500-XYZ-123", "mode": "RUN"}
        if ip == "192.168.1.20":
            return {"project": "Tank_Level_Monitor", "operator": "None", "status": "Active"}
        return {}

    def run_nse_script(self, ip: str, port: int, script_name: str) -> str:
        """
        Simulates Nmap Scripting Engine (NSE) output.
        """
        if script_name == "s7-info" and ip == "192.168.1.10":
            return "Module: 6ES7 511-1AK01-0AB0\nBasic Hardware: S7-1500\nVersion: 2.1.0"
        
        if script_name == "modbus-discover" and ip == "192.168.1.10":
            return "Sid: 1\nDevice: Simatic Modbus TCP"
            
        if script_name == "modbus-discover" and ip == "192.168.1.30":
            return "Sid: 1\nDevice: Moxa NPort"
            
        if script_name == "ssh-auth-methods" and ip == "192.168.1.30":
            return "Supported: publickey, password"
            
        return "No script output."

    def run_exploit(self, exploit_name: str, ip: str, port: int) -> Dict[str, Any]:
        """
        Simulates Metasploit exploit execution.
        """
        if exploit_name == "exploit/multi/http/default_creds_exec" and ip == "192.168.1.10":
            return {"success": True, "message": "Meterpreter session 1 opened. User: admin (uid=0)"}
            
        if exploit_name == "exploit/windows/scada/s7_1500_rce" and ip == "192.168.1.10":
            return {"success": False, "message": "Target is patched (Firmware v2.1)."}
            
        return {"success": False, "message": "Exploit failed or target not vulnerable."}

    def run_ics_command(self, command: str, ip: str, port: int) -> Dict[str, Any]:
        """
        Simulates ICS command execution (e.g., Stop CPU).
        """
        if command == "stop_cpu" and ip == "192.168.1.10":
            return {"success": True, "message": "PLC 192.168.1.10 switched to STOP mode. Process Halted."}
            
        if command == "write_coil" and ip == "192.168.1.30":
            return {"success": True, "message": "Coil 1 written successfully. Gateway configuration changed."}
            
        if command == "write_coil" and ip == "192.168.1.10":
            return {"success": True, "message": "Register written. Setpoint changed to 100."}

        return {"success": False, "message": "Command failed or access denied."}
