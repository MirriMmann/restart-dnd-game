# src\llm\illm_adapter.py

from abc import ABC, abstractmethod
from typing import Optional, Generator

class ILlm(ABC):
    """Абстракция LLM‑клиента (ядро зависит только от неё)."""

    @abstractmethod
    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
        model: Optional[str] = None,
        stream: bool = False,
        ) -> str | Generator[str, None, None]:
        """
        Основной метод общения с LLM. Возвращает либо строку, либо поток строк.
        """
        pass

    @abstractmethod
    def user_prompt_chat(
        self,
        user_prompt: str,
        model: Optional[str] = None,
        stream: bool = False,
    ) -> str | Generator[str, None, None]:
        """
        Упрощённый режим — только пользовательский prompt без системного.
        """
        pass

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """
        Возвращает вектор эмбеддинга для текста.
        Используется для памяти, поиска, индексации.
        """
        pass

    @abstractmethod
    def get_token_count(self, text: str) -> int:
        """
        Возвращает примерное количество токенов для строки текста.
        Нужно для контроля длины prompt.
        """
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """
        Возвращает имя модели, используемой в адаптере (например, gpt-4-1106-preview).
        """
        pass