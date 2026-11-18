from typing import Generator, Optional
from google import genai
from google.genai import types

from common import config
from common.config import (
    model_name,
    GEMINI_API_KEY,
    validate_env
)

_cached_client: Optional[genai.Client] = None


def gemini_client() -> genai.Client:
    global _cached_client
    if _cached_client is None:
        validate_env()
        _cached_client = genai.Client(api_key=GEMINI_API_KEY)
    return _cached_client

def generate_text(
        prompt: str,
        model: str = model_name,
        system_instruction: Optional[str] = None,
        client: Optional[genai.Client] = None,
) -> str:
    client = client or gemini_client()

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction
        ),
    )

    if response.usage_metadata:
        print(
            f"[Tokens: prompt={response.usage_metadata.prompt_token_count}, "
            f"candidates={response.usage_metadata.candidates_token_count}]"
        )
    return response.text or ""

def create_chat_session(
        model: str = model_name,
        system_instruction: Optional[str] = None,
        client: Optional[genai.Client] = None,
) -> genai.chats.Chat:

    client = client or gemini_client()

    config = (
        types.GenerateContentConfig(system_instruction=system_instruction)
        if system_instruction
        else None
    )
    chat = client.chats.create(model=model, config=config)
    chat._client = client
    return chat





