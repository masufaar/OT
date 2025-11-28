"""
Template Manager Tool
=====================

This tool manages professional templates for various report types.
It ensures that all generated reports follow a consistent, high-quality structure.
"""

from typing import Dict

class TemplateManager:
    """
    Manages report templates.
    """
    
    def __init__(self):
        self.templates = {
            "quality_report": self._get_quality_template(),
            "assessment_report": self._get_assessment_template(),
            "remediation_report": self._get_remediation_template(),
            "final_project_report": self._get_final_project_template()
        }

    def get_template(self, report_type: str) -> str:
        """
        Retrieves the requested template.
        """
        return self.templates.get(report_type, "Template not found.")

    def _get_quality_template(self) -> str:
        return """
# Quality Assurance Report

**Date:** {date}
**Auditor:** QualityAgent

## 1. Executive Summary
Provide a high-level overview of the agent performance. Mention the overall success rate and any critical safety violations.

## 2. Performance Metrics
| Metric | Value | Status |
| :--- | :--- | :--- |
| **Total Steps** | {total_steps} | - |
| **Success Rate** | {success_rate}% | - |
| **Avg Latency** | {avg_latency}ms | - |
| **Total Tokens** | {total_tokens} | - |

## 3. Safety & Compliance
- **Safety Gates Triggered:** {safety_violations}
- **Context Rot Risk:** {rot_risk}

## 4. Detailed Observations
For each agent, provide a brief analysis of their effectiveness and efficiency.
"""

    def _get_assessment_template(self) -> str:
        return """
# Vulnerability Assessment Report (AS-IS)

**Date:** {date}
**Scope:** OT Network (192.168.1.0/24)

## 1. Executive Summary
Summarize the security posture of the environment. Highlight the most critical risks that require immediate attention.

## 2. Methodology
Briefly describe the phases of the assessment (Discovery, Enumeration, Exploitation).

## 3. Critical Findings
List the top vulnerabilities discovered.
- **Finding Title**: [Name]
- **Severity**: [Critical/High/Medium]
- **Impact**: [Business Impact]
- **Evidence**: [Proof of Concept]

## 4. Asset Inventory
List all discovered assets with their identified vendors and roles.

## 5. Compliance Gaps
Map findings to ISO 27001 and IEC 62443 controls.
"""

    def _get_remediation_template(self) -> str:
        return """
# Strategic Remediation Plan (TO-BE)

**Date:** {date}
**Reference:** Assessment Report

## 1. Strategic Roadmap
Outline the high-level strategy for improving the security posture. Focus on "Quick Wins" vs "Long-Term Strategic Initiatives".

## 2. Prioritized Action Plan
Group remediations by priority.

### Priority 1: Critical & Immediate
- **Action**: [Action Name]
- **Rationale**: [Why this is urgent]
- **Estimated Cost**: [$$$]
- **Effort**: [Low/Medium/High]

### Priority 2: High Impact
...

## 3. Budgetary Estimates
Provide a rough order of magnitude (ROM) for the total remediation cost.
"""

    def _get_final_project_template(self) -> str:
        return """
# Final Project Report: OT Pentesting Multi-Agent System

**Date:** {date}
**Prepared For:** Executive Board

## 1. Executive Summary
A concise overview of the project, its goals, and the value delivered.

## 2. Architecture Overview
Explain the Multi-Agent System design, the Orchestrator, and the specialized agents.

## 3. Technical Implementation
Detail the technology stack, the "Agentic AI" approach, and the Quality Framework.

## 4. Risk & Safety Controls
Describe how the system ensures safety in OT environments (HITL, Safety Gates).

## 5. Conclusion & Recommendations
Final thoughts on the viability and future of this technology.
"""
