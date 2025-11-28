from typing import Dict, Any
import sqlite3
import json
import os

class InMemorySessionService:
    """
    Google ADK Session Service (In-Memory).
    """
    def __init__(self):
        self._sessions: Dict[str, Any] = {}

    def get_session(self, session_id: str) -> Dict[str, Any]:
        return self._sessions.get(session_id, {})

    def update_session(self, session_id: str, data: Dict[str, Any]):
        if session_id not in self._sessions:
            self._sessions[session_id] = {}
        self._sessions[session_id].update(data)

class DatabaseSessionService:
    """
    Google ADK Session Service (SQLite).
    """
    def __init__(self, db_url: str = "sqlite:///sessions.db"):
        self.db_path = db_url.replace("sqlite:///", "")
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                data TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def get_session(self, session_id: str) -> Dict[str, Any]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT data FROM sessions WHERE session_id = ?', (session_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return json.loads(row[0])
        return {}

    def update_session(self, session_id: str, data: Dict[str, Any]):
        current_data = self.get_session(session_id)
        current_data.update(data)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO sessions (session_id, data)
            VALUES (?, ?)
        ''', (session_id, json.dumps(current_data)))
        conn.commit()
        conn.close()
