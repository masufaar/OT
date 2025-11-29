"""
Critic Agent Module
===================

This module implements the `CriticAgent`, responsible for reviewing and refining reports.
It acts as an "Editor-in-Chief", ensuring that all outputs meet professional standards
and adhere to the defined templates.

Capabilities:
-   **Template Verification**: Checks if the report follows the required structure.
-   **Style Improvement**: Enhances the tone, clarity, and professionalism of the text.
-   **Refinement Loop**: Generates a critique and a refined version of the report.

Design Choices:
-   **Model Agnostic**: Designed to support OpenAI, Anthropic, or Mistral (simulated for local demo).
-   **Constructive Feedback**: Provides actionable advice ("Add more detail to section 2") rather than just "Bad report".
"""

from typing import Dict, Any, Optional
from tools.template_manager import TemplateManager

class CriticAgent:
    """
    The Editor/Critic agent.
    
    Attributes:
        model_provider (str): The LLM provider to use (default: "local").
        template_manager (TemplateManager): Tool to fetch report templates.
    """
    
    def __init__(self, model_provider: str = "local"):
        self.name = "CriticAgent"
        self.model_provider = model_provider
        self.template_manager = TemplateManager()

    def review_report(self, draft_content: str, report_type: str) -> Dict[str, Any]:
        """
        Reviews a draft report against the standard template.
        
        Args:
            draft_content (str): The raw markdown content of the draft.
            report_type (str): The type of report (e.g., 'assessment_report').
            
        Returns:
            Dict[str, Any]: Contains 'critique' (str) and 'refined_content' (str).
        """
        print(f"[{self.name}] Reviewing '{report_type}' using provider '{self.model_provider}'...")
        
        template = self.template_manager.get_template(report_type)
        
        # In a real scenario with an API key, we would call the LLM here.
        # For this local demo, we simulate the critique and refinement process.
        
        critique = self._generate_simulated_critique(draft_content, template)
        refined_content = self._generate_simulated_refinement(draft_content, template)
        
        print(f"[{self.name}] Critique generated. Refinement complete.")
        
        return {
            "critique": critique,
            "refined_content": refined_content
        }

    def _generate_simulated_critique(self, draft: str, template: str) -> str:
        """
        Simulates the LLM's critique logic.
        """
        critique = f"## Critic's Feedback (Model: {self.model_provider})\n"
        critique += "1. **Structure**: The draft mostly follows the template, but some sections could be more detailed.\n"
        critique += "2. **Tone**: The tone is generally professional, but avoid using passive voice in the Executive Summary.\n"
        critique += "3. **Completeness**: Ensure all placeholders (like {date}) are filled.\n"
        critique += "4. **Safety Check**: Verified no PII or sensitive internal IPs are exposed in plain text.\n"
        return critique

    def _generate_simulated_refinement(self, draft: str, template: str) -> str:
        """
        Simulates the LLM's rewriting logic.
        It appends a 'Refined by CriticAgent' badge and ensures the header is correct.
        """
        # Simple simulation: We take the draft and prepend a professional header if missing,
        # or just tag it to show it passed through the critic.
        
        refined = draft
        if "Refined by CriticAgent" not in refined:
            refined += "\n\n---\n*Refined by CriticAgent (Model: " + self.model_provider + ")*"
            
        # In a real implementation, this would be a full rewrite.
        # Here we just ensure the title matches the template for demonstration.
        if "# " not in refined[:10]:
            # If draft is missing a title, grab it from the template
            title_line = template.split('\n')[1] # Assuming line 1 is the title in template
            refined = title_line + "\n\n" + refined
            
        return refined
