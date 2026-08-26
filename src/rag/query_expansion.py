from src.llm.gemini_client import generate_response


def expand_query(question):

    prompt = f"""
You are an AI assistant.

Generate 3 different search queries
that have the same meaning.

Return ONLY one query per line.

Question:
{question}
"""

    response = generate_response(prompt)

    queries = response.split("\n")

    queries = [q.strip() for q in queries if q.strip()]

    queries.insert(0, question)

    return queries