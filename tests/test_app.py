import pytest

from src.app import generate_response, validate_prompt


def test_validate_prompt_accepts_valid_input():
    assert validate_prompt("What is Kubernetes?") == "What is Kubernetes?"


def test_validate_prompt_rejects_empty_input():
    with pytest.raises(ValueError):
        validate_prompt("")


def test_validate_prompt_rejects_whitespace_only_input():
    with pytest.raises(ValueError):
        validate_prompt("   \n\t  ")


def test_validate_prompt_rejects_non_string_input():
    with pytest.raises(TypeError):
        validate_prompt(123)


def test_generate_response_uses_mock_provider(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")

    response = generate_response("Explain virtualization.")

    assert response["provider"] == "mock"
    assert response["model"] == "mock-model"
    assert response["text"]


def test_generate_response_uses_normalized_structure():
    response = generate_response("Kubernetes")

    assert set(response) == {"text", "provider", "model"}
    assert response["text"]
