"""Student-facing application logic for Lab 02."""

from __future__ import annotations

from src.config import load_config
from src.mock_provider import MockProvider
from src.openai_provider import OpenAIProvider


def validate_prompt(prompt: str) -> str:
    """Validate and normalize a user prompt."""
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a string")

    normalized = prompt.strip()
    if not normalized:
        raise ValueError("prompt must not be empty")
    if len(normalized) > 10000:
        raise ValueError("prompt is too long")

    return normalized


def create_provider(config: dict):
    """Select and instantiate the configured provider."""
    provider_name = (config.get("LLM_PROVIDER", "mock") or "mock").lower()

    if provider_name == "mock":
        return MockProvider()

    if provider_name == "openai":
        api_key = (config.get("OPENAI_API_KEY") or "").strip()
        model = (config.get("OPENAI_MODEL") or "").strip()
        if not api_key or not model:
            raise ValueError("OpenAI provider requires OPENAI_API_KEY and OPENAI_MODEL.")
        return OpenAIProvider(api_key=api_key, model=model)

    raise ValueError(f"Unsupported LLM provider: {provider_name}")


def generate_response(prompt: str) -> dict:
    """Generate a normalized response for a user prompt."""
    normalized_prompt = validate_prompt(prompt)
    config = load_config()
    provider = create_provider(config)
    response = provider.generate(normalized_prompt)

    return {
        "text": response.text,
        "provider": response.provider,
        "model": response.model,
    }


def main() -> None:
    """Simplified CLI entry point for the lab."""
    print("LLMOps Lab 02")

    try:
        config = load_config()
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("Provider:", config.get("LLM_PROVIDER", "mock"))

    prompt = input("\nEnter prompt:\n> ")

    try:
        response = generate_response(prompt)
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("\nResponse:")
    print(response["text"])


if __name__ == "__main__":
    main()
