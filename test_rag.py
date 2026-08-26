import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from google import genai
import os
load_dotenv()
client_gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

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
prompt = f"""
You are an AI Resume Assistant.

Use ONLY the context below to answer the user's question.

Context:
{context}

Question:
{query}

If the answer is not present in the context, say:
"I don't have enough information."

Answer:
"""
response = client_gemini.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n===== AI ANSWER =====")
print(response.text)