import chromadb
from src.rag.reranker import rerank
from sentence_transformers import SentenceTransformer
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
client = chromadb.PersistentClient(
    path="data/chroma"
)
def create_collection():

    collection = client.get_or_create_collection(
        name="resume_collection"
    )

    return collection

def add_chunks(collection, chunks):
    if not chunks:
        print("⚠️ No chunks to add.")
    embeddings = model.encode(chunks)
    ids = [
    f"chunk_{i}"
    for i in range(len(chunks))
]
    metadatas = [
    {
        "source": "cvPROF.pdf",
        "chunk_id": i,
    }
    for i, chunk in enumerate(chunks)
]
    collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist(),
    metadatas=metadatas
)

def search_chunks(collection, original_question, queries):

    all_documents = []

    for query in queries:

        print("\nSearching with:", query)

        query_embedding = model.encode(query)

        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=5,
            include=[
                "documents",
                "distances",
                "metadatas"
            ]
        )

        print("\n===== SEARCH SCORES =====")

        for doc, distance, metadata in zip(
            results["documents"][0],
            results["distances"][0],
            results["metadatas"][0]
        ):

            print("\n========================")
            print("Distance :", distance)
            print("Metadata :", metadata)
            print("------------------------")
            print(doc[:150])

            if distance <= 1.65:
                all_documents.append(doc)

    # Supprimer les doublons
    all_documents = list(
        dict.fromkeys(all_documents)
    )

    print("\n===== UNIQUE DOCUMENTS =====")
    print("Nombre :", len(all_documents))

    if len(all_documents) == 0:
        return "I don't have enough information."

    # Reranking avec la question originale
    ranked_docs = rerank(
        original_question,
        all_documents
    )

    print("\n===== RERANKING =====")

    for doc, score in ranked_docs:

        print("Score :", score)
        print(doc[:150])
        print("------------------------")

    context = "\n\n".join(
        doc for doc, score in ranked_docs
    )

    return context
    
def reset_collection():

    try:
        client.delete_collection("resume_collection")
        print("Collection supprimée.")
    except:
        print("Aucune ancienne collection.")
