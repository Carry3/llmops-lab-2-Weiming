"""Optional OpenAI provider implementation for Lab 02."""

from __future__ import annotations

from openai import OpenAI

from src.models import LLMResponse
from src.provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """Provider implementation backed by the OpenAI Python SDK."""

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response using the OpenAI SDK."""
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is required for the OpenAI provider.")
        if not self.model:
            raise ValueError("OPENAI_MODEL is required for the OpenAI provider.")

        client = OpenAI(api_key=self.api_key)

        response = client.responses.create(model=self.model, input=prompt)
        text = getattr(response, "output_text", None)
        if text is None:
            try:
                text = response.output[0].content[0].text
            except (AttributeError, IndexError, TypeError):
                text = ""

        usage = getattr(response, "usage", None)
        if usage is not None and hasattr(usage, "model_dump"):
            usage = usage.model_dump()
        elif usage is None:
            usage = {"tokens": 0}

        return LLMResponse(
            text=str(text) if text is not None else "",
            provider="openai",
            model=self.model,
            usage=usage,
        )
