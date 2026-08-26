from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(question, documents, top_k=3):

    pairs = []

    for doc in documents:
        pairs.append([question, doc])

    scores = reranker.predict(pairs)

    ranked = list(zip(documents, scores))

    ranked.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]