from src.config import load_config


def test_load_config_uses_environment_variables(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-4o-mini")

    config = load_config()

    assert config["LLM_PROVIDER"] == "mock"
    assert config["OPENAI_API_KEY"] == "test-key"
    assert config["OPENAI_MODEL"] == "gpt-4o-mini"


def test_load_config_uses_defaults(monkeypatch):
    monkeypatch.delenv("LLM_PROVIDER", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    config = load_config()

    assert config["LLM_PROVIDER"] == "mock"
    assert config["OPENAI_API_KEY"] == ""
    assert config["OPENAI_MODEL"] == ""
