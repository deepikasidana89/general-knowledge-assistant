from __future__ import annotations

import os
import sys

from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def answer_general_knowledge_question(question: str) -> str:
    """Answer one general knowledge question."""
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=(
            "You are a helpful general knowledge assistant. "
            "Answer clearly and mention uncertainty when a fact may be disputed."
        ),
        input=question,
    )
    return response.output_text


def main() -> None:
    question = " ".join(sys.argv[1:]).strip()
    if not question:
        question = input("Ask a general knowledge question: ").strip()

    if not question:
        raise SystemExit("Please provide a question.")

    print(answer_general_knowledge_question(question))


if __name__ == "__main__":
    main()
