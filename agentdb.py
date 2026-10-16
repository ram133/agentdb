import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

class AgentMemory:
    def __init__(self, filepath: str = ".agent_context.json") -> None:
        self.filepath = filepath

    def save_context(self, branch_name: str, code_snippets: List[Dict[str, Any]]) -> None:
        context_data = {
            "branch": branch_name,
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "snippets": code_snippets
        }
        with open(self.filepath, 'w') as f:
            json.dump(context_data, f, indent=4)

    def load_context(self) -> Optional[Dict[str, Any]]:
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                return json.load(f)
        return None

    def clear_context(self) -> None:
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

