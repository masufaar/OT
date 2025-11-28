from typing import Dict, Any
from .__init__ import Tool
import sys
import io
import contextlib

class CodeExecutionTool(Tool):
    """
    Simulates a secure Code Execution Environment (Sandbox).
    """
    def __init__(self):
        super().__init__(
            name="execute_python",
            func=self.execute_code,
            description="Executes Python code in a sandboxed environment."
        )

    def execute_code(self, code: str) -> Dict[str, Any]:
        """
        Executes the provided Python code and returns stdout/stderr.
        WARNING: In this shim, it runs locally. In production, use a real sandbox.
        """
        print(f"DEBUG: Executing Code:\n{code}")
        
        # Capture stdout
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                exec(code, {"__builtins__": {}}) # Minimal sandbox for demo
            
            return {
                "status": "success",
                "stdout": stdout_capture.getvalue(),
                "stderr": stderr_capture.getvalue()
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
