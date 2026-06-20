from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Optional
import os
import anthropic


def get_claude_client() -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


@dataclass
class AgentResult:
    agent: str
    content: str
    actions: list[dict] = field(default_factory=list)
    data: dict = field(default_factory=dict)
    success: bool = True
    error: Optional[str] = None


class BaseAgent(ABC):
    NAME: str = ""
    DESCRIPTION: str = ""
    SYSTEM_PROMPT: str = ""

    def __init__(self, db=None):
        self.db = db
        self._client: Optional[anthropic.Anthropic] = None

    @property
    def client(self) -> anthropic.Anthropic:
        if self._client is None:
            self._client = get_claude_client()
        return self._client

    def call_llm(self, user_message: str, system_override: str = None, model: str = "claude-haiku-4-5-20251001") -> str:
        system = system_override or self.SYSTEM_PROMPT
        response = self.client.messages.create(
            model=model,
            max_tokens=1024,
            system=system,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text

    @abstractmethod
    def process(self, payload: dict, context: dict) -> AgentResult:
        pass
