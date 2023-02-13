import openai

from app.constants import settings

openai.api_key = settings.OPENAI_API_KEY
