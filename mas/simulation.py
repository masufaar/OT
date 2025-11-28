from typing import Dict, List, Any
import random

class SimulationManager:
    """
    Manages different network constellations for simulation/testing.
    """
    
    CONSTELLATIONS = {
        "standard_office": {
            "192.168.1.1": {"mac": "AA:BB:CC:DD:EE:01", "vendor": "Cisco", "ports": {80: "http", 443: "https", 53: "dns"}},
            "192.168.1.10": {"mac": "AA:BB:CC:DD:EE:10", "vendor": "Dell", "ports": {3389: "rdp", 445: "smb"}},
            "192.168.1.15": {"mac": "AA:BB:CC:DD:EE:15", "vendor": "HP", "ports": {631: "ipp"}},
            "192.168.1.20": {"mac": "AA:BB:CC:DD:EE:20", "vendor": "Apple", "ports": {5000: "airplay"}}
        },
        "ics_plant": {
            "192.168.1.1": {"mac": "00:11:22:33:44:01", "vendor": "Siemens", "ports": {102: "s7comm", 80: "http"}},
            "192.168.1.50": {"mac": "00:11:22:33:44:50", "vendor": "Rockwell", "ports": {44818: "ethernet-ip", 80: "http"}},
            "192.168.1.51": {"mac": "00:11:22:33:44:51", "vendor": "Schneider", "ports": {502: "modbus", 80: "http"}},
            "192.168.1.100": {"mac": "00:11:22:33:44:AA", "vendor": "Generic HMI", "ports": {5900: "vnc", 80: "http"}}
        },
        "air_gapped": {
            "10.0.0.1": {"mac": "FF:EE:DD:CC:BB:01", "vendor": "Proprietary Gateway", "ports": {}} 
        }
    }

    def __init__(self, mode: str = "ics_plant"):
        self.mode = mode
        self.current_topology = self.CONSTELLATIONS.get(mode, self.CONSTELLATIONS["ics_plant"])

    def set_mode(self, mode: str):
        if mode in self.CONSTELLATIONS:
            self.mode = mode
            self.current_topology = self.CONSTELLATIONS[mode]
        else:
            raise ValueError(f"Unknown constellation: {mode}")

    def discover_assets(self, subnet: str) -> List[Dict[str, str]]:
        """
        Simulates ARP scan. Returns list of {ip, mac, vendor}.
        """
        assets = []
        for ip, details in self.current_topology.items():
            # In a real sim we'd check if IP is in subnet, but for now we assume simple match
            assets.append({
                "ip": ip,
                "mac": details["mac"],
                "vendor": details["vendor"]
            })
        return assets

    def scan_ports(self, ip: str) -> List[Dict[str, Any]]:
        """
        Simulates Port scan. Returns list of open ports.
        """
        if ip not in self.current_topology:
            return []
        
        ports = []
        for port, service in self.current_topology[ip]["ports"].items():
            ports.append({
                "port": port,
                "protocol": "tcp",
                "state": "open",
                "service": service
            })
        return ports
