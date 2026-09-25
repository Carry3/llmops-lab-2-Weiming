"""Application-level data models for Lab 02."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LLMRequest:
    """Represents a request sent to an LLM provider."""

    prompt: str
    model: str | None = None
    temperature: float | None = None


@dataclass
class LLMResponse:
    """Represents a normalized response returned to the application."""

    text: str
    provider: str
    model: str
    usage: dict | None = None
