"""Mock provider for Lab 02."""

from __future__ import annotations

from src.models import LLMResponse
from src.provider import BaseProvider


class MockProvider(BaseProvider):
    """Deterministic provider used for testing and local development."""

    def generate(self, prompt: str) -> LLMResponse:
        """Return a deterministic mock response."""
        prompt_text = str(prompt).strip()
        if not prompt_text:
            raise ValueError("prompt must not be empty")

        response_text = (
            f"Mock response for: {prompt_text}. "
            "This deterministic output is returned by the mock provider "
            "to support local testing and validation."
        )
        return LLMResponse(
            text=response_text,
            provider="mock",
            model="mock-model",
            usage={"tokens": 0},
        )
