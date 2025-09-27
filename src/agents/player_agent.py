# player_agent.py

from typing import Any, Dict
from src.prompts.prompts import build_npc_prompt
from src.agents.iagent import IAgent
from src.core.story_log import StoryLog
from src.llm.g4f_adapter import G4fClient

class PlayerAgent(IAgent):
    def __init__(self, character, client=None):
        super().__init__()
        self.character = character
        self.client = client or G4fClient()
        self.story_log = StoryLog()
    
    def get_id(self) -> str:
        """
        Уникальный ID агента (например, 'npc_1' или 'elmar_the_wise').
        """
        pass

    def get_type(self) -> str:
        """
        Тип агента: "human", "llm", "random", "rule_based" и т.п.
        """
        pass

    def observe(self, observation) -> None:
        """
        Получает событие/наблюдение: может быть обновление поля боя, речи другого агента и т.п.
        observation может включать: окружение, действия других персонажей, системные события.
        """
        pass

    def decide(self, game_history):
        print("Игроку нужно принять решение вручную.")
        response = input(">>> ")
        # self.story_log.add(role=self.character['name'], content=response, type="narration")
        return response

    def apply_result(self, result) -> None:
        """
        Получает исход последнего действия (результат броска, последствия, урон и т.п.)
        """
        pass

    def serialize(self) -> Dict[str, Any]:
        """
        Сохранение состояния (статы, память, цели, истории и т.п.)
        """
        pass

    def restore(self, data: Dict[str, Any]) -> None:
        """
        Восстановление из сохранения
        """
        pass

    def get_character_summary(self) -> str:
        """
        Краткое текстовое описание персонажа — используется при генерации LLM-подсказок.
        """
        pass

    def is_human_controlled(self) -> bool:
        """
        Возвращает True, если агент — человек, False — LLM/бот.
        Удобно для UI.
        """
        return self.get_type() == "human"