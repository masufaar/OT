"""
Web Scanner Agent
=================

This agent is responsible for **Phase 5: Web Scanning**.
It targets HTTP/HTTPS services, which are common for Human-Machine Interfaces (HMIs) and PLC configuration pages.

Capabilities:
-   **Authentication Check**: Detects if the web interface requires a login.
-   **Default Credential Testing**: Attempts to log in using common default credentials (e.g., "admin/admin").
-   **Data Scraping**: Extracts useful information from the page if access is granted (e.g., "System Ready", "Tank Level").
-   **Mock Integration**: Simulates web login flows and page content.

Design Choices:
-   **Focus on Defaults**: In OT, default credentials are the #1 vulnerability. We prioritize this check.
-   **Information Leakage**: Even without login, some HMIs display sensitive operational data (scraped_data).
"""

from typing import Dict, Any, Optional
from tools.mock_network import MockNetwork

class WebScanner:
    """
    Agent for scanning web interfaces.
    
    Attributes:
        use_mock (bool): If True, uses the MockNetwork tool.
    """
    
    def __init__(self, use_mock: bool = True):
        self.name = "WebScanner"
        self.use_mock = use_mock
        self.mock_tool = MockNetwork()

    def scan(self, ip_address: str, port: int = 80, tool_context: Any = None) -> Dict[str, Any]:
        """
        Scans HTTP services for vulnerabilities and info.
        
        Args:
            ip_address (str): The target IP.
            port (int): The target port (usually 80, 443, 8080).
            tool_context (Any): HITL context.
            
        Returns:
            Dict[str, Any]: A dictionary containing auth status, login success, scraped data, and vulnerabilities.
        """
        print(f"[{self.name}] Scanning Web Service on {ip_address}:{port}...")
        
        result = {
            "auth_required": False,
            "login_success": False,
            "scraped_data": {},
            "vulnerabilities": []
        }
        
        if self.use_mock:
            # Check Authentication
            if self.mock_tool.check_web_auth(ip_address, port):
                print(f"[{self.name}] Authentication Required.")
                result["auth_required"] = True
                
                # Try Default Creds
                # This is a "noisy" but highly effective check.
                print(f"[{self.name}] Attempting default credentials (admin/admin)...")
                if self.mock_tool.web_login(ip_address, port, "admin", "admin"):
                    print(f"[{self.name}] Login SUCCESS!")
                    result["login_success"] = True
                    result["vulnerabilities"].append("Default Credentials (admin/admin)")
                else:
                    print(f"[{self.name}] Login Failed.")
            else:
                print(f"[{self.name}] No Authentication Required.")
            
            # Scrape Data (if no auth or login success)
            # If we are logged in OR if no auth is needed, we grab the page content.
            if not result["auth_required"] or result["login_success"]:
                data = self.mock_tool.scrape_web(ip_address, port)
                print(f"[{self.name}] Scraped Data: {data}")
                result["scraped_data"] = data
                
        else:
            # TODO: Implement requests/BeautifulSoup logic
            # Real implementation would use `requests.get()` and `BeautifulSoup` to parse HTML.
            pass
            
        return result
