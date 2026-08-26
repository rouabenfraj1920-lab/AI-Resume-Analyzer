from src.llm.gemini_client import generate_response

prompt = "Explain RAG in two simple sentences."

response = generate_response(prompt)

print("===== GEMINI =====")
print(response)