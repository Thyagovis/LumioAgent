from pathlib import Path

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from Core.config import settings  # ajuste para o caminho real

BASE_DIR = Path(__file__).resolve().parent
PROMPT_PATH = BASE_DIR / "Input" / "system.md"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")

model = OpenAIChatModel(
    "gemini-3.1-flash-lite",
    provider=OpenAIProvider(
        base_url=settings.router_base_url,
        api_key=settings.router_api_key,
    ),
)

agent = Agent(
    model,
    system_prompt=SYSTEM_PROMPT,
)