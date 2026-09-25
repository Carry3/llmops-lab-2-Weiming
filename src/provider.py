"""Provider abstraction for Lab 02."""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.models import LLMResponse


class BaseProvider(ABC):
    """Abstract provider interface."""

    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response for the given prompt."""
        raise NotImplementedError("Implement BaseProvider.generate().")
