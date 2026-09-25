# LLMOps Lab 02 — Building an LLM Application with a Provider Abstraction

This lab introduces the first real LLM application workflow in CSYE 7374 — Large Language Models Operations (LLMOps).

## Purpose

The purpose of this lab is to move students from a basic Python engineering workflow into the first software design problem of the semester:

- accept a prompt from a user
- validate the prompt
- load configuration from environment variables
- select a provider through an internal abstraction
- send the request to a provider
- normalize the provider response into a consistent application format
- handle errors cleanly

The main lesson of this lab is that an LLM application should be engineered as a software system, not as a single API call.

## Learning Objectives

By completing this lab, students should be able to:

1. Understand the basic request/response pattern of an LLM API.
2. Separate application logic from the LLM provider implementation.
3. Use environment variables for configuration.
4. Avoid hard-coding API credentials.
5. Design a small provider abstraction.
6. Validate user input.
7. Handle API and application errors.
8. Normalize an LLM response into a predictable application format.
9. Write tests using a mock LLM provider.
10. Use Make to run tests and the application.
11. Understand why production LLM applications should not tightly couple business logic to one model provider.
12. Use GitHub Actions to automatically test an LLM application without requiring a real API key.

## Prerequisites

Before starting this lab, make sure you have:

- Python 3.11 or newer installed
- `git` installed
- a terminal or command prompt
- a GitHub repository

## Repository Structure

```text
llmops-lab02/
├── README.md
├── Makefile
├── requirements.txt
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── main.py
│   ├── mock_provider.py
│   ├── models.py
│   ├── openai_provider.py
│   └── provider.py
├── tests/
│   ├── test_app.py
│   ├── test_config.py
│   ├── test_errors.py
│   └── test_provider.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Architecture

```text
User Input
    |
    v
Application
    |
    v
LLM Provider Interface
    |
    +----------------------+
    |                      |
    v                      v
Mock Provider         Real Provider
                       |
                       v
                    LLM API
```

## Installation

From the repository root, run:

```bash
make install
```

This creates a local Python virtual environment in `.venv` and installs the dependencies listed in `requirements.txt`.

## Running Tests

Run the test suite with:

```bash
make test
```

## Running Linting

Run linting with:

```bash
make lint
```

## Running the Application

Run the CLI with:

```bash
make run
```

This lab includes a small `main` entry point in `src/main.py`, so the CLI can be launched cleanly through `make run`.

The default provider is `mock`, so the application can run without an API key.

## Optional Real LLM

Students may optionally configure an OpenAI API key locally using `.env` or environment variables.

Example:

```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
```

Do not commit real credentials. The automated grading path must not depend on a real API key.

## What to Implement

This repository intentionally contains placeholder implementations only.

You must complete the TODOs in the following files:

- `src/config.py`
- `src/provider.py`
- `src/mock_provider.py`
- `src/openai_provider.py`
- `src/app.py`

Do not remove the TODO markers.

## Functional Specifications

### `src/config.py`

Implement configuration loading from environment variables.

Expected behavior:

- load `LLM_PROVIDER`
- load `OPENAI_API_KEY`
- load `OPENAI_MODEL`
- use sensible defaults where appropriate
- avoid hard-coded secrets

### `src/provider.py`

Implement or complete the provider abstraction.

Expected behavior:

- define an abstract provider contract
- require a `generate(prompt: str)` method
- use a consistent response type

### `src/mock_provider.py`

Implement the mock provider.

Expected behavior:

- return deterministic responses
- operate without an external API or secret
- produce predictable provider metadata
- support testing and local development

### `src/openai_provider.py`

Implement the optional real-provider integration.

Expected behavior:

- get the API key from configuration
- get the model from configuration
- send the prompt through the OpenAI SDK
- normalize the provider response into the application-level `LLMResponse`
- handle provider-side errors cleanly

### `src/app.py`

Implement the application logic.

Expected behavior:

- validate the user prompt
- select the configured provider
- call the provider abstraction
- return a normalized response dictionary
- preserve separation between application logic and provider-specific code

## Input Validation

The application should handle at least the following cases:

### Valid

```text
What is Kubernetes?
```

### Invalid

- empty strings
- whitespace-only strings
- non-string input
- oversized prompts

Use appropriate Python exceptions.

## Error Handling

The application should distinguish between at least:

1. invalid user input
2. configuration errors
3. provider errors

Error messages should never expose secrets such as API keys.

## Visible Tests

The visible tests are designed to validate observable behavior rather than a specific implementation.

They cover:

- configuration defaults and environment-variable overrides
- prompt validation
- mock provider deterministic output
- application response structure
- provider selection
- error handling
- safe error messages

## Hidden Tests

Instructor-only hidden tests will verify additional behavior such as:

- provider abstraction is respected
- mock mode does not require OpenAI
- invalid input is rejected
- whitespace-only input is rejected
- configuration is loaded dynamically
- API keys are not hard-coded
- provider errors are handled appropriately
- responses contain the required fields

## AI / Copilot Policy

GitHub Copilot and other AI coding assistants are permitted and encouraged for this lab. You are responsible for understanding, testing, and validating any code generated with AI assistance.

The goal is not to prevent AI use. The goal is to ensure that students still understand interfaces, configuration, validation, and testing.

Do not submit Copilot conversation history as part of the lab.

## Submission Requirements

Complete the required TODOs, run the tests, run linting, commit your changes, and push the repository to GitHub.

Students should also verify that:

- `make install` works
- `make test` passes
- `make lint` passes
- `make run` launches the application

## Expected Workflow

A reasonable workflow for this lab is:

1. Read the specification carefully.
2. Inspect the repository structure.
3. Review the TODOs in `src/config.py`, `src/provider.py`, `src/mock_provider.py`, `src/openai_provider.py`, and `src/app.py`.
4. Ask Copilot for help implementing the missing behavior.
5. Review any generated code for correctness.
6. Run `make test`.
7. Investigate any failing tests.
8. Update the implementation.
9. Run `make lint`.
10. Commit and push.

AI-generated code must still be tested and validated.

## Clean Up

When you are finished, you can remove local build artifacts with:

```bash
make clean
```
