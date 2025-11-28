from google_local.adk.tools.openapi import OpenApiTool
import os

def test_openapi_tool():
    """
    Verifies the OpenAPI Tool functionality.
    """
    spec_path = "tests/mock_openapi.json"
    tool = OpenApiTool(spec_path=spec_path, base_url="http://api.example.com")
    
    print(f"Loaded OpenAPI Spec with endpoints: {tool.endpoints}")
    
    # Test valid endpoint
    result = tool.call_endpoint("/users", "get")
    print(f"Result for /users: {result}")
    assert result["status"] == "success"
    
    # Test invalid endpoint
    result = tool.call_endpoint("/invalid", "get")
    print(f"Result for /invalid: {result}")
    assert "error" in result

if __name__ == "__main__":
    test_openapi_tool()
