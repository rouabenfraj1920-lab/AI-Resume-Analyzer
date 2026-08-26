import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(
    name="test_resume",
    embedding_function=embedding_function
)

# Ajouter quelques documents
collection.add(
    ids=["doc1", "doc2", "doc3"],
    documents=[
        "Python is a programming language used for AI and data science.",
        "Federated Learning allows machine learning models to learn from distributed data.",
        "HTML and CSS are used to build web interfaces."
    ]
)


print("Documents added successfully!")