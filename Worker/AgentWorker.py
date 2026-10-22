from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from Core.config import settings

model = GoogleModel(
    "gemini-3.1-flash-lite",
    provider=GoogleProvider(api_key=settings.google_api_key)
)

agent = Agent(
    model = model,
    instructions= "você é um assistente de ia, sua função atual é auxiliar e servir o usuario com tudo que você tem alcance"
)


