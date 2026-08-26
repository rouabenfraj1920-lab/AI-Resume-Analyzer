from src.rag.reranker import rerank

question = "What certifications does the candidate have?"

documents = [
    "Cisco CCNA 1 and Cisco CCNA 2 certifications.",
    "Chair IEEE ENICarthage Student Branch.",
    "DELORA uses Federated Learning."
]

results = rerank(question, documents)

for doc, score in results:
    print(score)
    print(doc)
    print()