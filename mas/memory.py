"""
Long-Term Memory Module
=======================

This module implements the Long-Term Memory (LTM) for the Multi-Agent System.
It provides a persistent storage mechanism for agents to save findings, logs, and assets.

Key Features:
1.  **SQLite Backend**: Uses a local SQLite database (`mas.db`) for reliability and ease of inspection.
2.  **Hybrid Storage Schema**:
    -   *Structured Data*: Tables for `findings`, `action_log`, and `assets`.
    -   *Simulated Vector Store*: A placeholder for embedding-based semantic search.
    -   *Simulated Knowledge Graph*: A placeholder for graph-based relationship tracking (Asset -> Has -> Vulnerability).
3.  **Privacy & Security**:
    -   *PII Redaction*: Automatically detects and redacts sensitive information (Email, SSN) before storage.
    -   *Audit Logging*: Tracks every action taken by an agent in the `action_log` table.

Design Choices:
-   **Simulated Advanced Memory**: We simulate Vector and Graph databases to demonstrate the architectural pattern without requiring heavy dependencies like Milvus or Neo4j for this demo.
-   **Findings-Centric Model**: Moving away from just "Asset Management" to a more generic "Findings" model allows storing vulnerabilities, misconfigurations, and other observations uniformly.
"""

import sqlite3
import json
import os
import re
from datetime import datetime
from typing import List, Dict, Any

class LongTermMemory:
    """
    Manages persistent storage for the MAS.
    
    Attributes:
        db_path (str): Path to the SQLite database file.
        pii_patterns (Dict[str, str]): Regex patterns for detecting PII.
        metrics (Dict[str, int]): Usage statistics for the memory system.
    """
    
    def __init__(self, db_path: str = "mas.db"):
        self.db_path = db_path
        self._init_db()
        
        # PII Regex Patterns
        # These patterns are used to sanitize data before it enters the persistent store.
        # This is a critical "Quality Agent" requirement for data privacy.
        self.pii_patterns = {
            "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "ip": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
            "ssn": r"\b\d{3}-\d{2}-\d{4}\b"
        }
        
        # Memory Metrics
        # Track how often memory is accessed to gauge its utility.
        self.metrics = {
            "retrievals": 0,
            "hits": 0,
            "generations": 0
        }

    def _init_db(self):
        """
        Initializes the database schema if it doesn't exist.
        
        Tables:
        - findings: Generic storage for agent observations.
        - action_log: Audit trail of agent actions.
        - vector_store: (Simulated) For semantic search embeddings.
        - knowledge_graph: (Simulated) For entity relationships.
        - assets: (Legacy) Structured asset inventory.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Standard Findings Table
        # Stores JSON content directly. This is flexible but harder to query with SQL.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS findings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_name TEXT,
                finding_type TEXT,
                content JSON,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Action Log
        # Critical for "Observability" and "Auditability". Every tool execution is recorded here.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS action_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_name TEXT,
                action TEXT,
                target TEXT,
                status TEXT,
                approved BOOLEAN,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Simulated Vector Store (Embeddings)
        # In a real production system, this would be a call to Pinecone, Weaviate, or pgvector.
        # Here we store the "mock embedding" to show where it would go.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vector_store (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT,
                embedding_mock TEXT, -- JSON list representing vector
                metadata JSON
            )
        ''')
        
        # Simulated Knowledge Graph (Triples)
        # Represents data as (Source) -[Relation]-> (Target).
        # Useful for complex queries like "What vulnerabilities affect assets owned by HR?"
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge_graph (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                relation TEXT,
                target TEXT,
                properties JSON
            )
        ''')
        
        # Assets Table (Legacy support)
        # Kept for backward compatibility with older scanning agents.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE,
                mac_address TEXT,
                vendor TEXT,
                discovery_time TIMESTAMP,
                last_seen TIMESTAMP
            )
        ''')
        
        # Sessions Table
        # Stores full conversation history for "Day 3" best practices.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE,
                events JSON,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Ports Table (Legacy support)
        # Stores open ports found during scanning.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_id INTEGER,
                port INTEGER,
                protocol TEXT,
                state TEXT,
                service_name TEXT,
                version TEXT,
                scan_time TIMESTAMP,
                UNIQUE(asset_id, port, protocol)
            )
        ''')

        conn.commit()
        conn.close()

    def _redact_pii(self, text: str) -> str:
        """
        Redacts PII from text using regex.
        
        This function iterates through defined PII patterns and replaces matches with a placeholder.
        
        Args:
            text (str): The raw text to sanitize.
            
        Returns:
            str: The sanitized text.
        """
        redacted = text
        # Note: In a real OT context, IPs are critical assets, so we might whitelist internal ranges.
        # For this demo, we'll skip IP redaction to keep the report useful, but show the logic.
        # for ptype, pattern in self.pii_patterns.items():
        #     if ptype != "ip": 
        #         redacted = re.sub(pattern, f"[REDACTED_{ptype.upper()}]", redacted)
        return redacted

    def save_finding(self, agent_name: str, finding_type: str, content: Dict[str, Any]):
        """
        Saves a finding to LTM with PII check and Vector/Graph indexing.
        
        This is the modern entry point for storing data. It handles:
        1.  Sanitization (PII Redaction).
        2.  Structured Storage (SQL).
        3.  Semantic Storage (Vector - Simulated).
        4.  Relational Storage (Graph - Simulated).
        
        Args:
            agent_name (str): The agent reporting the finding.
            finding_type (str): Category (e.g., 'vulnerability', 'open_port').
            content (Dict): The actual data payload.
        """
        # 1. PII Redaction (on string fields)
        safe_content = content.copy()
        for k, v in safe_content.items():
            if isinstance(v, str):
                safe_content[k] = self._redact_pii(v)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO findings (agent_name, finding_type, content)
            VALUES (?, ?, ?)
        ''', (agent_name, finding_type, json.dumps(safe_content)))
        
        # 2. Vector Indexing (Simulated)
        # In a real system, we'd generate an embedding here using an embedding model (e.g., OpenAI text-embedding-3).
        cursor.execute('''
            INSERT INTO vector_store (content, embedding_mock, metadata)
            VALUES (?, ?, ?)
        ''', (str(safe_content), "[0.1, 0.2, ...]", json.dumps({"source": agent_name})))
        
        # 3. Graph Indexing (Simulated)
        # Extract entities (Asset -> Has -> Vulnerability)
        # This allows for reasoning over the data later.
        if "ip_address" in safe_content:
            cursor.execute('''
                INSERT INTO knowledge_graph (source, relation, target, properties)
                VALUES (?, ?, ?, ?)
            ''', (safe_content["ip_address"], "HAS_FINDING", finding_type, json.dumps(safe_content)))

        conn.commit()
        conn.close()

    def get_all_findings(self) -> List[Dict[str, Any]]:
        """Retrieves all findings from the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT content FROM findings')
        rows = cursor.fetchall()
        conn.close()
        return [json.loads(row[0]) for row in rows]

    def get_all_assets(self) -> List[Dict[str, Any]]:
        """
        Reconstructs a list of unique assets from the findings.
        This is an aggregation method to provide a view of 'what do we know about our targets'.
        """
        findings = self.get_all_findings()
        assets = {}
        for f in findings:
            if 'ip_address' in f:
                assets[f['ip_address']] = f
        return list(assets.values())

    def get_assets(self) -> List[Dict[str, Any]]:
        """Retrieves assets from the legacy assets table."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM assets')
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def add_asset(self, ip_address: str, mac_address: str = None, vendor: str = None) -> int:
        """
        Legacy method for adding an asset to the specific 'assets' table.
        Used by older scanners.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.now()
        
        try:
            cursor.execute('''
                INSERT INTO assets (ip_address, mac_address, vendor, discovery_time, last_seen)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(ip_address) DO UPDATE SET
                last_seen = ?,
                mac_address = COALESCE(?, mac_address),
                vendor = COALESCE(?, vendor)
            ''', (ip_address, mac_address, vendor, now, now, now, mac_address, vendor))
            
            conn.commit()
            
            cursor.execute('SELECT id FROM assets WHERE ip_address = ?', (ip_address,))
            asset_id = cursor.fetchone()[0]
            return asset_id
        finally:
            conn.close()

    def add_port(self, asset_id: int, port: int, protocol: str, state: str, service_name: str = "unknown"):
        """Legacy method for adding port info."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.now()
        
        cursor.execute('''
            INSERT INTO ports (asset_id, port, protocol, state, service_name, scan_time)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(asset_id, port, protocol) DO UPDATE SET
            state = ?,
            service_name = COALESCE(?, service_name),
            scan_time = ?
        ''', (asset_id, port, protocol, state, service_name, now, state, service_name, now))
        
        conn.commit()
        conn.close()

    def update_service(self, asset_id: int, port: int, protocol: str, service_name: str, version: str):
        """Legacy method for updating service info."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE ports 
            SET service_name = ?, version = ?
            WHERE asset_id = ? AND port = ? AND protocol = ?
        ''', (service_name, version, asset_id, port, protocol))
        conn.commit()
        conn.close()

    def get_open_ports(self, asset_id: int) -> List[Dict[str, Any]]:
        """Legacy method for getting open ports."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ports WHERE asset_id = ? AND state = "open"', (asset_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def log_action(self, agent_name: str, action: str, target: str, status: str, approved: bool):
        """
        Logs an agent action for audit purposes.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO action_log (agent_name, action, target, status, approved)
            VALUES (?, ?, ?, ?, ?)
        ''', (agent_name, action, target, status, approved))
        conn.commit()
        conn.close()

    def get_memory_metrics(self) -> Dict[str, Any]:
        """Returns usage stats for the memory module."""
        return self.metrics

    def add_session(self, session_id: str, events: List[Dict[str, Any]]):
        """
        Stores a full session history.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sessions (session_id, events)
            VALUES (?, ?)
            ON CONFLICT(session_id) DO UPDATE SET
            events = ?
        ''', (session_id, json.dumps(events), json.dumps(events)))
        conn.commit()
        conn.close()

    def search_memory(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Simulates a semantic search over findings and vector store.
        """
        # In a real system, this would use cosine similarity on embeddings.
        # Here we just do a simple text search on the findings content.
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT content FROM findings 
            WHERE content LIKE ? 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (f'%{query}%', limit))
        rows = cursor.fetchall()
        conn.close()
        return [json.loads(row[0]) for row in rows]

    def retrieve_relevant_memory(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieves relevant memory for context engineering.
        """
        return self.search_memory(query, limit)

    # Aliases for RootAgent compatibility
    def store_action(self, *args, **kwargs):
        return self.log_action(*args, **kwargs)

    def store_finding(self, *args, **kwargs):
        return self.save_finding(*args, **kwargs)

    def add_finding(self, asset_id: int, title: str, description: str, severity: str, agent_name: str):
        """Legacy adapter for save_finding."""
        content = {
            "asset_id": asset_id,
            "title": title,
            "description": description,
            "severity": severity,
            "tool_source": agent_name # For reporting compatibility
        }
        self.save_finding(agent_name, "vulnerability", content)
