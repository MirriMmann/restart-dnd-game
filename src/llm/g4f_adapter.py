# src\llm\g4f_adapter.py

from typing import List, Dict
import g4f
from g4f.client import Client
from g4f.Provider import RetryProvider, LMArena, PollinationsAI, OpenaiChat
from .illm_adapter import ILlm
import g4f.debug

class G4fClient(ILlm):
    def __init__(self):
        self._client = Client()
        g4f.debug.version_check = True
        g4f.debug.logging = True

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
        model: str = "openai-large",
        stream: bool = False,
    ):
        messages: List[Dict] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        resp = self._client.chat.completions.create(
            model=model,
            messages=messages,
            provider=RetryProvider([PollinationsAI], shuffle=False),
            stream=stream,
        )
        if stream:
            return (ch.choices[0].delta.content or "" for ch in resp)
        return resp.choices[0].message.content


    def user_prompt_chat(
        self,
        user_prompt: str,
        model="openai-large",
        stream=False
    ):
        messages: List[Dict] = [
            {"role": "user", "content": user_prompt},
        ]
        resp = self._client.chat.completions.create(
            model=model,
            messages=messages,
            # provider=RetryProvider([OpenaiChat, PollinationsAI], shuffle=False),
            stream=stream,
        )
        if stream:
            return (ch.choices[0].delta.content or "" for ch in resp)
        return resp.choices[0].message.content

    def embed(self, text: str):
        # если G4F не поддерживает — заглушка
        return []

    def get_token_count(self, text: str):
        return len(text.split())  # приближённо

    def get_model_name(self):
        return "openai-large"