"""Student-facing application logic for Lab 02."""

from __future__ import annotations

from src.config import load_config


def validate_prompt(prompt: str) -> str:
    """Validate and normalize a user prompt."""
    # TODO: implement this function.
    raise NotImplementedError("Implement validate_prompt().")


def create_provider(config: dict):
    """Select and instantiate the configured provider."""
    # TODO: implement this function.
    raise NotImplementedError("Implement create_provider().")


def generate_response(prompt: str) -> dict:
    """Generate a normalized response for a user prompt."""
    # TODO: implement this function.
    raise NotImplementedError("Implement generate_response().")


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
