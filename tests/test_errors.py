import pytest

from src.app import generate_response


def test_generate_response_handles_provider_failure(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")

    class BrokenProvider:
        def generate(self, prompt: str):
            raise RuntimeError("provider failed")

    monkeypatch.setattr("src.app.MockProvider", BrokenProvider)

    with pytest.raises(RuntimeError):
        generate_response("Hello")


def test_generate_response_handles_invalid_configuration(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    with pytest.raises(ValueError):
        generate_response("Hello")


def test_errors_do_not_expose_secrets(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "super-secret")
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    with pytest.raises(ValueError):
        generate_response("Hello")
