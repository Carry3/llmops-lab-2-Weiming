from src.mock_provider import MockProvider
from src.models import LLMResponse


def test_mock_provider_returns_deterministic_response():
    provider = MockProvider()

    response = provider.generate("Explain virtualization.")

    assert isinstance(response, LLMResponse)
    assert response.provider == "mock"
    assert response.model == "mock-model"
    assert response.text
    assert response.text.lower().find("virtualization") >= 0


def test_mock_provider_response_structure_is_predictable():
    provider = MockProvider()

    response = provider.generate("Kubernetes")

    assert response.provider == "mock"
    assert response.model == "mock-model"
    assert isinstance(response.text, str)
    assert response.text
