# General Knowledge Assistant

A small command-line assistant that answers general knowledge questions.

The application accepts a question, sends it to a language model, and prints the answer. It is intentionally simple so it can be used as a realistic example repository for evaluating implementation evidence with EARF.

## Example

```bash
python assistant.py "Why do eclipses happen?"
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your-key"
python assistant.py "What is the largest planet in our solar system?"
```

Never commit API keys or `.env` files.

## EARF evaluation expectation

The `uses_llm` capability should be assessed as `VERIFIED` because this repository contains:

- A model client import
- Client construction
- A real completion request
- A user-facing function connected to that request
