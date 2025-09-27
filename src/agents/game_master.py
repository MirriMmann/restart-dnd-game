# src\agents\game_master.py

from src.core.story_log import StoryLog
from src.llm.g4f_adapter import G4fClient
from src.prompts.prompts import INITIAL_PROMPT, GAME_MASTER_PROMPT

class GameMaster:
    def __init__(self, client=None):
        self.client = client or G4fClient()
        self.story_log = StoryLog()

    def begin_adventure(self):
        response = self.client.chat(
            system_prompt=INITIAL_PROMPT,
            user_prompt='Теперь создай новую сцену.')
        # self.story_log.add(role="Гейммастер", content=response, type="narration")
        return response

    def add_agent_action(self, role, content):
        self.story_log.add(role=role, content=content, type="action")

    def get_context_for_prompt(self):
        return self.story_log.get_recent_context(max_len=10)
    
    def continue_adventure(self):
        # Создаём промпт для гейммастера с учётом истории игры
        game_history = self.get_context_for_prompt()
        
        game_master_prompt = GAME_MASTER_PROMPT.format(game_history=game_history)
        
        # Получаем ответ от модели, продолжая историю
        response = self.client.chat(
            system_prompt=game_master_prompt,  # Начальный контекст (если нужно)
            user_prompt='Создай новое описание, которое поможет игрокам продолжить приключение.'  # Промпт для продолжения истории
        )

        # Добавляем новый элемент в историю
        # self.story_log.add(role="Гейммастер", content=response, type="narration")
        return response
