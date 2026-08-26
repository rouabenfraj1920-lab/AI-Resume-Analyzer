import chromadb
from sentence_transformers import SentenceTransformer

# Charger le modèle
model = SentenceTransformer("all-MiniLM-L6-v2")

# Créer le client Chroma
client = chromadb.PersistentClient(path="data/chroma")

# Créer la collection
collection = client.get_or_create_collection(
    name="resume_test"
)

print("Collection créée !")

# -----------------------
# Documents de test
# -----------------------
documents = [
    "DELORA utilise un système multi-agents décentralisé et du Federated Learning.",
    "RailMind utilise des vector embeddings et Qdrant pour identifier des incidents ferroviaires similaires.",
    "CharthaVoyage est un site web responsive développé avec HTML, CSS et JavaScript."
]

embeddings = model.encode(documents)

print("Nombre de documents :", len(documents))
print("Dimension :", len(embeddings[0]))

# Ajouter dans ChromaDB
collection.add(
    ids=[
        "project_delora",
        "project_railmind",
        "project_charthavoyage"
    ],
    documents=documents,
    embeddings=embeddings.tolist()
)

print("Documents ajoutés !")

print("Nombre dans la collection :", collection.count())

# =========================
# RECHERCHE
# =========================

query = "Which project uses Artificial Intelligence?"

query_embedding = model.encode(query)

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)
context = "\n\n".join(results["documents"][0])

print("\n===== SEARCH RESULTS =====")

for doc in results["documents"][0]:
    print(doc)