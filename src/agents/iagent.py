# agent.py
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
# from game_models import GameState, Action, ActionResult, Observation # Предполагаемые классы

class IAgent(ABC):
    @abstractmethod
    def get_id(self) -> str:
        """
        Уникальный ID агента (например, 'npc_1' или 'elmar_the_wise').
        """
        pass

    @abstractmethod
    def get_type(self) -> str:
        """
        Тип агента: "human", "llm", "random", "rule_based" и т.п.
        """
        pass

    @abstractmethod
    def observe(self, observation) -> None:
        """
        Получает событие/наблюдение: может быть обновление поля боя, речи другого агента и т.п.
        observation может включать: окружение, действия других персонажей, системные события.
        """
        pass

    @abstractmethod
    def decide(self, game_state):
        """
        Возвращает следующее действие агента в виде экземпляра Action (не просто dict).
        """
        pass

    @abstractmethod
    def apply_result(self, result) -> None:
        """
        Получает исход последнего действия (результат броска, последствия, урон и т.п.)
        """
        pass

    @abstractmethod
    def serialize(self) -> Dict[str, Any]:
        """
        Сохранение состояния (статы, память, цели, истории и т.п.)
        """
        pass

    @abstractmethod
    def restore(self, data: Dict[str, Any]) -> None:
        """
        Восстановление из сохранения
        """
        pass

    @abstractmethod
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