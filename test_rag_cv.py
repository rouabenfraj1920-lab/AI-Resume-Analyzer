from src.pdf_reader import extract_text_from_pdf
from src.rag.chunker import chunk_text
from src.rag.vector_store import reset_collection
from src.llm.gemini_client import generate_response
from src.rag.query_expansion import expand_query
from src.rag.vector_store import create_collection, add_chunks, search_chunks
pdf_path = "data/cvs/cvPROF.pdf"
cv_text = extract_text_from_pdf(pdf_path)
chunks = chunk_text(cv_text)
print("\n===== CHUNKS =====")

for i, chunk in enumerate(chunks):
    print(f"\n----- Chunk {i+1} -----")
    print(chunk)
print("Nombre de chunks :", len(chunks))
reset_collection()
collection = create_collection()
print(collection.count())
add_chunks(collection, chunks)
while True:    

    question = input("\nAsk your question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break
    queries = expand_query(question)

    print("\n===== EXPANDED QUERIES =====")

    for q in queries:
        print("-", q)

    context = search_chunks(
    collection,
    question,
    queries
)

    print("\n===== RETRIEVED CONTEXT =====")
    print(context)
    

    prompt = f"""
You are an AI Resume Assistant.

Your task is to answer ONLY using the retrieved context.

Rules:
- Never invent information.
- Never guess dates or names.
- If information is incomplete, explicitly say it is incomplete.
- If the answer is not present in the context, reply:
"I don't have enough information."

Context:
{context}

Question:
{question}
"""

    answer = generate_response(prompt)

    print("\n===== AI ANSWER =====")
    print(answer)