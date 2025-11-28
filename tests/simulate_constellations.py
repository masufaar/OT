from tools.mock_network import MockNetwork
from agents.network_scanner import NetworkScanner
from rich.console import Console

if __name__ == "__main__":
    # Define Constellations
    empty_net = []
    
    small_net = [
        {"ip": "192.168.1.50", "mac": "AA:BB:CC:DD:EE:FF", "vendor": "Raspberry Pi", "type": "IoT"}
    ]
    
    large_net = [
        {"ip": f"192.168.1.{i}", "mac": f"00:00:00:00:00:{i:02x}", "vendor": "Generic", "type": "Node"}
        for i in range(10, 20)
    ]
    
    # Run Simulations
    constellations = {
        "Empty Network": empty_net,
        "Small IoT Network": small_net,
        "Large Office Network": large_net
    }
    
    for name, devices in constellations.items():
        print(f"\n--- Running Simulation: {name} ---")
        mock_net = MockNetwork(devices=devices)
        scanner = NetworkScanner(use_mock=True, mock_tool=mock_net)
        
        # Run Scan
        results = scanner.execute("192.168.1.0/24")
        print(f"Found {len(results)} devices.")
        for device in results:
            print(f" - {device['ip']} ({device['vendor']})")
            
        # Verify count
        assert len(results) == len(devices)
        print(f"✅ Simulation '{name}' Passed.")
