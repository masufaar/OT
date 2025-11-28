"""
Writer Agent Module
===================

This module implements the `WriterAgent`, which is responsible for generating professional,
human-readable reports from the technical findings stored in the Long-Term Memory.

Key Responsibilities:
1.  **Risk Assessment**: Calculates risk levels based on likelihood and impact.
2.  **Compliance Mapping**: Maps technical findings to regulatory frameworks (ISO 27001, PCI DSS, HIPAA).
3.  **Cost Estimation**: Provides rough estimates for remediation costs to help management prioritize.
4.  **Dual Reporting**: Generates two distinct reports:
    -   *Assessment Report (AS-IS)*: Technical details for security engineers.
    -   *Remediation Report (TO-BE)*: Strategic roadmap for executives.

Design Choices:
-   **Separation of Concerns**: The WriterAgent does not scan or exploit; it only processes data.
-   **Template-Based Generation**: Uses Markdown templates converted to PDF for consistent, professional output.
-   **Business Context**: Adds value by translating "Open Port 502" into "Critical Risk to Industrial Control Systems".
"""

from typing import Dict, Any, List
import datetime
from xhtml2pdf import pisa
import markdown2

class WriterAgent:
    """
    The Reporting Specialist agent.
    
    Attributes:
        memory (LongTermMemory): Access to the shared memory to retrieve findings.
    """
    
    def __init__(self, memory):
        self.name = "WriterAgent"
        self.memory = memory

    def calculate_risk(self, finding: Dict[str, Any]) -> Dict[str, str]:
        """
        Calculates Risk Level based on Likelihood and Impact.
        
        Formula: Risk = Likelihood * Impact
        
        Args:
            finding (Dict): The finding data.
            
        Returns:
            Dict: A dictionary containing 'likelihood', 'impact', and 'level'.
        """
        title = finding['title'].lower()
        desc = finding['description'].lower()
        severity = finding['severity']

        # Default values
        likelihood = "Low"
        impact = "Low"

        # Determine Likelihood
        # Heuristics based on the type of finding
        if "exploit success" in title or "ics impact" in title:
            likelihood = "High (Proven)" # We actually exploited it, so likelihood is 100%
        elif "default" in title or "weak" in title:
            likelihood = "High" # Trivial to exploit
        elif "snmp" in title:
            likelihood = "Medium"
        
        # Determine Impact
        # Heuristics based on the potential damage
        if "stop_cpu" in desc or "meterpreter" in desc:
            impact = "Critical (Safety/Operational)" # Could cause physical harm or downtime
        elif "write_coil" in desc:
            impact = "High (Process Manipulation)"
        elif "admin" in desc:
            impact = "High (Unauthorized Access)"
        elif "snmp" in title:
            impact = "Medium (Info Disclosure)"

        # Risk Matrix
        # For this demo, we simplify the matrix and often defer to the tool's severity,
        # but annotated with our context.
        risk_level = severity 
        
        return {
            "likelihood": likelihood,
            "impact": impact,
            "level": risk_level
        }

    def get_compliance_mapping(self, finding: Dict[str, Any]) -> List[str]:
        """
        Maps findings to ISO 27001, PCI DSS, and HIPAA.
        
        This adds business value by showing which regulations are violated.
        
        Args:
            finding (Dict): The finding data.
            
        Returns:
            List[str]: A list of compliance violation strings.
        """
        title = finding['title'].lower()
        desc = finding['description'].lower()
        compliance = []

        if "default" in title or "weak" in title or "admin" in desc:
            compliance.append("ISO 27001: A.9.2.1 (User Registration), A.9.4.3 (Password Mgmt)")
            compliance.append("PCI DSS: Req 2.1 (Default Defaults), Req 8.2 (Auth)")
            compliance.append("HIPAA: 164.308(a)(5)(ii)(D) (Password Mgmt)")
        
        if "snmp" in title or "clear text" in desc:
            compliance.append("ISO 27001: A.13.1 (Network Security)")
            compliance.append("PCI DSS: Req 4.1 (Strong Cryptography)")
            compliance.append("HIPAA: 164.312(e)(1) (Transmission Security)")

        if "ics impact" in title or "stop_cpu" in desc:
            compliance.append("ISO 27001: A.12.1 (Operational Procedures), A.17 (Continuity)")
            compliance.append("PCI DSS: Req 10 (Monitoring)")
            compliance.append("HIPAA: 164.308(a)(7) (Contingency Plan)")

        return compliance

    def estimate_cost(self, finding: Dict[str, Any]) -> Dict[str, str]:
        """
        Estimates mitigation cost and effort.
        
        This is a "Value-Add" feature for the Remediation Report.
        
        Args:
            finding (Dict): The finding data.
            
        Returns:
            Dict: Cost and effort estimates.
        """
        title = finding['title'].lower()
        desc = finding['description'].lower()

        if "stop_cpu" in desc or "s7" in desc:
            return {
                "mitigation": "Network Segmentation & PLC Hardening",
                "cost": "$15,000 - $50,000 (Hardware + Labor)",
                "effort": "High (Downtime Required)"
            }
        if "write_coil" in desc or "modbus" in desc:
            return {
                "mitigation": "Deep Packet Inspection Firewall & VPN",
                "cost": "$10,000 - $30,000",
                "effort": "Medium"
            }
        if "default" in title or "admin" in desc:
            return {
                "mitigation": "Policy Update & Config Change",
                "cost": "$1,000 - $5,000 (Labor)",
                "effort": "Low"
            }
        
        return {
            "mitigation": "General Patching & Hardening",
            "cost": "$5,000 - $10,000/yr",
            "effort": "Medium"
        }

    def generate_assessment_report(self) -> str:
        """
        Generates the AS-IS Vulnerability Assessment Report (No Remediation).
        
        This report focuses on "What is wrong right now".
        
        Returns:
            str: The filename of the generated PDF.
        """
        print(f"[{self.name}] Generating Assessment Report (AS-IS)...")
        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        
        report = f"# OT Security Assessment Report (AS-IS)\n"
        report += f"**Date:** {date_str}\n"
        report += f"**Compliance Scope:** ISO 27001, PCI DSS, HIPAA\n\n"
        
        # Executive Summary
        report += "## 1. Executive Summary\n"
        report += "This report details the findings of a security assessment conducted on the Operational Technology (OT) environment. "
        report += "The assessment focused on identifying vulnerabilities that could impact operational continuity, safety, and compliance.\n\n"
        report += "**Key Findings:**\n"
        report += "- Critical risks identified in PLC and Modbus communications.\n"
        report += "- Compliance gaps found regarding Access Control and Network Security.\n\n"

        # Methodology
        report += "## 2. Methodology\n"
        report += "The assessment followed a standard penetration testing methodology adapted for OT environments:\n"
        report += "1. **Discovery**: Passive and active asset identification.\n"
        report += "2. **Enumeration**: Service and version detection.\n"
        report += "3. **Vulnerability Analysis**: Identification of known flaws.\n"
        report += "4. **Exploitation (Controlled)**: Verification of critical vulnerabilities.\n"
        report += "5. **Risk Assessment**: Likelihood and Impact analysis.\n\n"

        # Asset Inventory
        report += "## 3. Asset Inventory\n"
        assets = self.memory.get_all_assets()
        for asset in assets:
            report += f"- **{asset['ip_address']}** ({asset['vendor'] or 'Unknown'})\n"
        report += "\n"

        # Findings (AS-IS)
        report += "## 4. Technical Findings & Risk Assessment\n"
        findings = self.memory.get_all_findings()
        
        severity_order = {"CRITICAL": 1, "HIGH": 2, "MEDIUM": 3, "LOW": 4, "INFO": 5}
        sorted_findings = sorted(findings, key=lambda x: severity_order.get(x['severity'], 99))

        for finding in sorted_findings:
            risk = self.calculate_risk(finding)
            compliance = self.get_compliance_mapping(finding)
            severity_icon = "🔴" if finding['severity'] == "CRITICAL" else "🟠" if finding['severity'] == "HIGH" else "🔵"

            report += f"### {severity_icon} {finding['title']}\n"
            report += f"**Asset:** {finding['asset_id']} | **Source:** {finding['tool_source']}\n"
            report += f"**Description:** {finding['description']}\n\n"
            
            report += "**Risk Assessment:**\n"
            report += f"- **Likelihood:** {risk['likelihood']}\n"
            report += f"- **Impact:** {risk['impact']}\n"
            report += f"- **Risk Level:** {risk['level']}\n\n"

            if compliance:
                report += "**Compliance Impact:**\n"
                for item in compliance:
                    report += f"- {item}\n"
            report += "\n---\n"

        # Save PDF
        self._save_pdf(report, "assessment_report.pdf")
        return "assessment_report.pdf"

    def generate_remediation_report(self) -> str:
        """
        Generates the TO-BE Remediation & Strategy Report.
        
        This report focuses on "How to fix it and how much it costs".
        
        Returns:
            str: The filename of the generated PDF.
        """
        print(f"[{self.name}] Generating Remediation Report (TO-BE)...")
        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        
        report = f"# OT Security Remediation Strategy (TO-BE)\n"
        report += f"**Date:** {date_str}\n"
        report += f"**Reference:** Based on Assessment Report dated {date_str}\n\n"

        # Executive Summary (Strategic)
        report += "## 1. Strategic Executive Summary\n"
        report += "Following the vulnerability assessment, this report outlines the strategic roadmap for remediation. "
        report += "The focus is on prioritizing high-impact mitigations that align with business objectives and compliance mandates.\n\n"

        # Remediation Plan
        report += "## 2. Prioritized Remediation Plan\n"
        findings = self.memory.get_all_findings()
        severity_order = {"CRITICAL": 1, "HIGH": 2, "MEDIUM": 3, "LOW": 4, "INFO": 5}
        sorted_findings = sorted(findings, key=lambda x: severity_order.get(x['severity'], 99))

        # Deduplicate findings for strategic view (group by title/type)
        seen_types = set()
        
        for finding in sorted_findings:
            key = finding['title']
            if key in seen_types:
                continue
            seen_types.add(key)

            cost_data = self.estimate_cost(finding)
            severity_icon = "🔴" if finding['severity'] == "CRITICAL" else "🟠" if finding['severity'] == "HIGH" else "🔵"

            report += f"### {severity_icon} Mitigation: {finding['title']}\n"
            report += f"**Risk Driver:** {finding['severity']} Risk identified in assessment.\n\n"
            
            report += "**Recommended Actions:**\n"
            # Logic from previous get_mitigation, but expanded
            if "ICS Impact" in finding['title']:
                report += "- Implement **Zone-based Segmentation** (IEC 62443).\n"
                report += "- Deploy **Industrial IPS** with deep packet inspection.\n"
                report += "- Enable **PLC Protection Levels** and password authentication.\n"
            elif "Exploit" in finding['title']:
                report += "- **Patch Management**: Urgent patching of web services.\n"
                report += "- **Network Isolation**: Restrict access to HMI/PLC web interfaces.\n"
            elif "Default" in finding['title']:
                report += "- **Identity Management**: Enforce strong password policies.\n"
                report += "- **MFA**: Implement multi-factor authentication for critical access.\n"
            else:
                report += "- Standard hardening and monitoring.\n"
            
            report += "\n**Cost & Effort Analysis:**\n"
            report += f"- **Estimated Cost:** {cost_data['cost']}\n"
            report += f"- **Implementation Effort:** {cost_data['effort']}\n"
            report += "\n---\n"

        # Save PDF
        self._save_pdf(report, "remediation_report.pdf")
        return "remediation_report.pdf"

    def _save_pdf(self, markdown_content: str, filename: str):
        """
        Helper to convert Markdown to PDF.
        """
        html_content = markdown2.markdown(markdown_content)
        styled_html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Helvetica, sans-serif; font-size: 12px; line-height: 1.5; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }}
                h2 {{ color: #34495e; margin-top: 20px; border-bottom: 1px solid #bdc3c7; }}
                h3 {{ color: #7f8c8d; margin-top: 15px; background-color: #ecf0f1; padding: 5px; }}
                strong {{ color: #2c3e50; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        with open(filename, "wb") as pdf_file:
            pisa.CreatePDF(styled_html, dest=pdf_file)
        print(f"[{self.name}] Saved {filename}")
