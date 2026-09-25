"""Mock provider for Lab 02."""

from __future__ import annotations

from src.models import LLMResponse
from src.provider import BaseProvider


class MockProvider(BaseProvider):
    """Deterministic provider used for testing and local development."""

    def generate(self, prompt: str) -> LLMResponse:
        """Return a deterministic mock response."""
        # TODO: implement this method.
        raise NotImplementedError("Implement MockProvider.generate().")
