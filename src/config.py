"""Student-facing configuration helpers for Lab 02."""

from __future__ import annotations

import os


def load_config() -> dict:
    """
    Load configuration from environment variables.

    Expected keys:
    - LLM_PROVIDER
    - OPENAI_API_KEY
    - OPENAI_MODEL
    """
    return {
        "LLM_PROVIDER": os.getenv("LLM_PROVIDER", "mock").strip() or "mock",
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "") or "",
        "OPENAI_MODEL": os.getenv("OPENAI_MODEL", "") or "",
    }
