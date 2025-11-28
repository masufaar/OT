"""
Multi-Agent System (MAS) Entry Point
====================================

This is the main execution script for the OT Pentesting Multi-Agent System.
It orchestrates a complex, multi-stage security assessment using a team of specialized agents.

Workflow Overview (9 Phases):
1.  **Network Discovery**: Identify live hosts in the target range.
2.  **Port Scanning**: Enumerate open ports on discovered assets.
3.  **Service Scanning**: Identify running services and versions.
4.  **SNMP Scanning**: Check for weak community strings and system info.
5.  **Web Scanning**: Crawl web interfaces for vulnerabilities and data.
6.  **Nmap Scripting**: Run targeted NSE scripts based on service detection.
7.  **Metasploit Exploitation**: Attempt to exploit identified vulnerabilities (Simulated).
8.  **ICS Security Actions**: Perform OT-specific checks (Modbus/S7) (Simulated).
9.  **Reporting**: Generate comprehensive PDF reports (Assessment & Remediation).

Architecture Integration:
-   **Orchestrator**: All agent calls are wrapped via `orchestrator.run_agent_task` to ensure:
    -   *Observability*: Every step is traced and timed.
    -   *Context*: Agents receive optimized history.
    -   *Safety*: Actions are checked against safety gates and HITL.
-   **Memory**: Findings are stored in a centralized SQLite database (`mas.db`).
-   **Quality**: The system automatically generates a "Quality Framework Report" at the end.
"""

import sys
import argparse
from mas.orchestrator import RootAgent
from mas.memory import LongTermMemory
from mas.observability import QualityManager
from mas.context import ContextManager
from agents.network_scanner import NetworkScanner
from agents.port_scanner import PortScanner
from agents.service_scanner import ServiceScanner
from agents.web_scanner import WebScanner
from agents.snmp_scanner import SnmpScanner
from agents.nmap_agent import NmapAgent
from agents.metasploit_agent import MetasploitAgent
from agents.ics_agent import IcsAgent
from agents.writer_agent import WriterAgent
from agents.critic_agent import CriticAgent
from rich.console import Console

def main():
    """
    Main execution function.
    Initializes the system, runs the 9-phase workflow, and handles reporting.
    """
    parser = argparse.ArgumentParser(description="OT Pentesting Multi-Agent System")
    parser.add_argument("--auto-approve", action="store_true", help="Auto-approve HITL requests")
    args = parser.parse_args()

    console = Console()
    
    # Initialize the Central Nervous System
    # The RootAgent handles memory, quality, and context management.
    memory = LongTermMemory("mas.db")
    quality = QualityManager()
    context = ContextManager()
    
    orchestrator = RootAgent(memory, quality, context, auto_approve=args.auto_approve)
    
    # Initialize Agents
    # We use `use_mock=True` to ensure safety during this demo execution.
    # Note: NetworkScanner and PortScanner now use SimulationManager internally, so we pass console/memory.
    scanner = NetworkScanner(console, memory)
    port_scanner = PortScanner(console, memory)
    service_scanner = ServiceScanner(use_mock=True)
    snmp_scanner = SnmpScanner(use_mock=True)
    web_scanner = WebScanner(use_mock=True)
    nmap_agent = NmapAgent(use_mock=True)
    msf_agent = MetasploitAgent(use_mock=True)
    ics_agent = IcsAgent(use_mock=True)
    writer_agent = WriterAgent(memory)
    critic_agent = CriticAgent()

    console.print("[bold green]OT Pentesting MAS - Initialized[/bold green]")
    if args.auto_approve:
        console.print("Mode: [yellow]LOCAL DEMO (Auto-Approve Enabled)[/yellow]")
    else:
        console.print("Mode: [yellow]LOCAL DEMO (Mock Network)[/yellow]")

    # Step 1: Get Target from HITL
    # In a real scenario, this would be passed via CLI args or a config file.
    if args.auto_approve:
        target_network = "192.168.1.0/24"
        console.print(f"\n[bold]Target network:[/bold] {target_network} (Auto-selected)")
    else:
        target_network = console.input("\n[bold]Enter target network range (e.g., 192.168.1.0/24): [/bold]")
    
    # ==============================================================================================
    # Phase 1: Network Discovery
    # Goal: Identify all active IP addresses in the target range.
    # Agent: NetworkScanner
    # ==============================================================================================
    console.print(f"\n[bold]Phase 1: Network Discovery[/bold]")
    results = orchestrator.run_agent_task(scanner, "scan", target_network)

    if results:
        console.print("\n[bold]Scan Results:[/bold]")
        for device in results:
            console.print(f"- IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")
            # Store in Long Term Memory (LTM)
            # This allows subsequent agents to query these assets without re-scanning.
            orchestrator.memory.add_asset(device['ip'], device['mac'], device['vendor'])
        
        console.print(f"\n[green]Successfully stored {len(results)} assets in Long Term Memory.[/green]")
        
        # ==============================================================================================
        # Phase 2: Port Scanning
        # Goal: Find open TCP ports on the discovered assets.
        # Agent: PortScanner
        # ==============================================================================================
        console.print(f"\n[bold]Phase 2: TCP Port Scanning[/bold]")
        assets = orchestrator.memory.get_assets()
        
        for asset in assets:
            ip = asset['ip_address']
            asset_id = asset['id']
            
            # The Orchestrator handles the HITL check internally via `ask_permission`.
            # If the user denies, `ports` will be None.
            ports = orchestrator.run_agent_task(port_scanner, "scan", ip)
            
            if ports:
                for p in ports:
                    console.print(f"  - Found open port: {p['port']}/{p['protocol']}")
                    orchestrator.memory.add_port(asset_id, p['port'], p['protocol'], p['state'])
        
        # ==============================================================================================
        # Phase 3: Service Scanning
        # Goal: Identify the specific service and version running on each open port.
        # Agent: ServiceScanner
        # ==============================================================================================
        console.print(f"\n[bold]Phase 3: Service Scanning[/bold]")
        # Re-fetch assets to ensure we have the latest state (though in this sync flow it's the same)
        for asset in assets:
            asset_id = asset['id']
            ip = asset['ip_address']
            open_ports = orchestrator.memory.get_open_ports(asset_id)
            
            if open_ports:
                console.print(f"\n[cyan]Scanning services on {ip}...[/cyan]")
                for port_info in open_ports:
                    port = port_info['port']
                    protocol = port_info['protocol']
                    
                    # Run the service scan task
                    service_info = orchestrator.run_agent_task(service_scanner, "scan", ip, port)
                    
                    if service_info:
                        console.print(f"  - Port {port}: {service_info['service']} ({service_info['version']})")
                        orchestrator.memory.update_service(asset_id, port, protocol, service_info['service'], service_info['version'])

        # ==============================================================================================
        # Phase 4: SNMP Scanning
        # Goal: Enumerate SNMP information if available (Community strings, System info).
        # Agent: SnmpScanner
        # ==============================================================================================
        console.print(f"\n[bold]Phase 4: SNMP Scanning[/bold]")
        for asset in assets:
            ip = asset['ip_address']
            asset_id = asset['id']
            
            snmp_data = orchestrator.run_agent_task(snmp_scanner, "scan_snmp", ip)
            
            if snmp_data:
                console.print(f"[green]  - SNMP Enumerated on {ip}: {snmp_data['sysName']}[/green]")
                # Add as a finding (Weak Community String)
                if snmp_data.get('community') == 'public':
                    orchestrator.memory.add_finding(
                        asset_id, 
                        "Default SNMP Community String", 
                        f"Found default community string 'public'. System: {snmp_data.get('sysDescr')}", 
                        "MEDIUM", 
                        "SnmpScanner"
                    )

        # ==============================================================================================
        # Phase 5: Web Scanning
        # Goal: Scan HTTP/HTTPS services for common vulnerabilities and scrape data.
        # Agent: WebScanner
        # ==============================================================================================
        console.print(f"\n[bold]Phase 5: Web Scanning[/bold]")
        for asset in assets:
            ip = asset['ip_address']
            asset_id = asset['id']
            open_ports = orchestrator.memory.get_open_ports(asset_id)
            
            for port_info in open_ports:
                port = port_info['port']
                # Heuristic: Check common web ports
                if port in [80, 443, 8080]:
                    web_result = orchestrator.run_agent_task(web_scanner, "scan", ip, port)
                    
                    if web_result:
                        if web_result['vulnerabilities']:
                            for vuln in web_result['vulnerabilities']:
                                console.print(f"[red]  - Vulnerability on {ip}:{port}: {vuln}[/red]")
                                orchestrator.memory.add_finding(asset_id, "Web Vulnerability", vuln, "HIGH", "WebScanner")
                        
                        if web_result['scraped_data']:
                            console.print(f"[green]  - Scraped Data from {ip}:{port}: {web_result['scraped_data']}[/green]")

        # ==============================================================================================
        # Phase 6: Nmap Scripting
        # Goal: Run targeted NSE scripts based on the detected service (e.g., 'http-title' for http).
        # Agent: NmapAgent
        # ==============================================================================================
        console.print(f"\n[bold]Phase 6: Nmap Scripting[/bold]")
        for asset in assets:
            ip = asset['ip_address']
            asset_id = asset['id']
            open_ports = orchestrator.memory.get_open_ports(asset_id)
            
            for port_info in open_ports:
                port = port_info['port']
                service = port_info['service_name']
                
                # The agent logic decides which script to run based on the service name.
                # We peek here just to see if we should even call the agent, but the agent handles it robustly.
                script_name = nmap_agent._select_script(service, port)
                if script_name:
                    nse_result = orchestrator.run_agent_task(nmap_agent, "run_nse", ip, port, service)
                    
                    if nse_result:
                        console.print(f"[cyan]  - NSE '{nse_result['script']}' Output on {ip}:{port}:[/cyan]")
                        console.print(f"{nse_result['output']}")
                        orchestrator.memory.add_finding(asset_id, f"NSE Info: {nse_result['script']}", nse_result['output'], "INFO", "NmapAgent")

        # ==============================================================================================
        # Phase 7: Metasploit Exploitation
        # Goal: Attempt to exploit identified vulnerabilities (Simulated).
        # Agent: MetasploitAgent
        # ==============================================================================================
        console.print(f"\n[bold]Phase 7: Metasploit Exploitation[/bold]")
        
        for asset in assets:
            ip = asset['ip_address']
            asset_id = asset['id']
            open_ports = orchestrator.memory.get_open_ports(asset_id)
            
            for port_info in open_ports:
                port = port_info['port']
                service = port_info['service_name']
                
                # 1. Search for exploits relevant to the service or known findings
                # For this demo, we simulate searching for "Default Credentials" if we found them earlier,
                # or just generic service exploits.
                potential_exploits = msf_agent.search_exploit("Default Credentials", service)
                if not potential_exploits:
                    potential_exploits = msf_agent.search_exploit("", service)
                
                for exploit in potential_exploits:
                    console.print(f"[yellow]Potential Exploit found: {exploit}[/yellow]")
                    # The Orchestrator will ask for HITL permission for this dangerous action.
                    exploit_result = orchestrator.run_agent_task(msf_agent, "execute_exploit", exploit, ip, port)
                    
                    if exploit_result and exploit_result['success']:
                        console.print(f"[red][bold]  - EXPLOIT SUCCESS on {ip}:{port}![/bold] {exploit_result['message']}[/red]")
                        orchestrator.memory.add_finding(asset_id, "Exploit Success", f"Exploited with {exploit}. {exploit_result['message']}", "CRITICAL", "MetasploitAgent")
                        break # Stop after one success per service to avoid noise

        # ==============================================================================================
        # Phase 8: ICS Security Actions
        # Goal: Perform OT/ICS specific checks (e.g., Modbus coil reading).
        # Agent: IcsAgent
        # ==============================================================================================
        console.print(f"\n[bold]Phase 8: ICS Security Actions[/bold]")
        
        for asset in assets:
            ip = asset['ip_address']
            asset_id = asset['id']
            open_ports = orchestrator.memory.get_open_ports(asset_id)
            
            for port_info in open_ports:
                port = port_info['port']
                service = port_info['service_name']
                
                # Select action based on service (e.g., 'modbus' -> 'read_coils')
                action = ics_agent.select_action(service, [])
                
                if action:
                    ics_result = orchestrator.run_agent_task(ics_agent, "execute_ics_action", action, ip, port, service)
                    
                    if ics_result and ics_result['success']:
                        console.print(f"[red][bold]  - ICS ACTION SUCCESS on {ip}:{port}![/bold] {ics_result['message']}[/red]")
                        orchestrator.memory.add_finding(asset_id, "ICS Impact", f"Action '{action}' successful. {ics_result['message']}", "CRITICAL", "IcsAgent")

        # ==============================================================================================
        # Phase 9: Reporting & Refinement
        # Goal: Generate professional PDF reports summarizing the findings, refined by a Critic Agent.
        # Agent: WriterAgent, CriticAgent
        # ==============================================================================================
        
        console.print(f"\n[bold]Phase 9: Dual Reporting with Refinement Loop[/bold]")
        
        # 1. Assessment Report (AS-IS)
        # We use the refinement loop to generate -> critique -> refine
        assess_path = orchestrator.run_refinement_loop(
            draft_agent=writer_agent,
            critic_agent=critic_agent,
            method_name="generate_assessment_report",
            report_type="assessment_report"
        )
        console.print(f"[bold green]Final Assessment Report: {assess_path}[/bold green]")
        
        # 2. Remediation Report (TO-BE)
        remedy_path = orchestrator.run_refinement_loop(
            draft_agent=writer_agent,
            critic_agent=critic_agent,
            method_name="generate_remediation_report",
            report_type="remediation_report"
        )
        console.print(f"[bold green]Final Remediation Report: {remedy_path}[/bold green]")
        
        # Best Practice: Session Ingestion
        # Flush the full session history to Long-Term Memory for future retrieval.
        console.print(f"\n[bold]Phase 10: Session Ingestion[/bold]")
        session_id = orchestrator.quality.current_trace_id
        events = orchestrator.quality.trace_data["steps"]
        orchestrator.memory.add_session(session_id, events)
        console.print(f"[bold green]Session {session_id} ingested into Memory.[/bold green]")

        # Finalize Quality Trace
        orchestrator.close()
        
        # Generate Final Quality Framework Report
        # This report analyzes the efficiency and quality of the agents themselves.
        # Note: We could also run this through the critic, but for now we keep it standard.
        # We need to access the quality agent via the orchestrator if it has one, or just use the quality manager.
        # The original code called `orchestrator.quality_agent.generate_final_report`.
        # But `RootAgent` (orchestrator) doesn't have `quality_agent` attribute in my new code, it has `quality` (QualityManager).
        # QualityManager has `generate_efficiency_report` but maybe not `generate_final_report`?
        # Let's check QualityManager.
        # Assuming QualityManager handles it or we need to fix this call.
        # For now, let's call `quality.generate_efficiency_report()` if it exists, or just skip if not.
        # Actually, `observability.py` has `generate_efficiency_report`.
        orchestrator.quality.generate_efficiency_report()

    else:
        console.print("\n[yellow]No results found or action denied.[/yellow]")
        
        # Best Practice: Session Ingestion
        session_id = orchestrator.quality.current_trace_id
        events = orchestrator.quality.trace_data["steps"]
        orchestrator.memory.add_session(session_id, events)
        
        orchestrator.close()
        orchestrator.quality.generate_efficiency_report()

if __name__ == "__main__":
    main()
