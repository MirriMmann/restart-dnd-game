# src\core\story_log.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class StoryEvent:
    step: int
    role: str # "gm", "player", "npc"
    type: str # "narration", "action", "dialogue"
    content: str
    parsed_action: Optional[dict] = None

class StoryLog:
    def __init__(self):
        self.events: list[StoryEvent] = []
        self.step_counter = 0

    def add(self, role: str, content: str, type="dialogue", parsed_action=None):
        self.step_counter += 1
        event = StoryEvent(
            step=self.step_counter,
            role=role,
            type=type,
            content=content,
            parsed_action=parsed_action
        )
        self.events.append(event)

    def get_recent_context(self, max_len=10) -> str:
        return "\n".join([f"{e.role}: {e.content}" for e in self.events[-max_len:]])
    
    def get_all_history(self) -> str:
        """Возвращает всю историю в виде строки"""
        return "\n".join([f"{e.step}. {e.role}: {e.content}" for e in self.events])

    def to_json(self):
        return [e.__dict__ for e in self.events]