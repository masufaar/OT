import json
from typing import Dict, Any, List, Optional
from .__init__ import Tool

class OpenApiTool(Tool):
    """
    A tool that dynamically generates functions from an OpenAPI specification.
    """
    def __init__(self, spec_path: str, base_url: str):
        self.spec_path = spec_path
        self.base_url = base_url
        self.spec = self._load_spec()
        self.endpoints = self._parse_endpoints()
        
        # In a real implementation, we would register each endpoint as a separate tool
        # or have a single 'call_api' tool. For this shim, we'll use a single tool.
        super().__init__(
            name="call_openapi_endpoint",
            func=self.call_endpoint,
            description="Calls an API endpoint defined in the OpenAPI spec."
        )

    def _load_spec(self) -> Dict[str, Any]:
        with open(self.spec_path, 'r') as f:
            return json.load(f)

    def _parse_endpoints(self) -> List[str]:
        return list(self.spec.get("paths", {}).keys())

    def call_endpoint(self, path: str, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Simulates calling an API endpoint.
        """
        print(f"DEBUG: OpenApiTool calling {method.upper()} {self.base_url}{path} with params {params}")
        
        if path not in self.endpoints:
            return {"error": f"Endpoint {path} not found in spec."}
            
        # Mock response based on path
        return {
            "status": "success",
            "data": f"Mock response from {path}",
            "params_received": params
        }
