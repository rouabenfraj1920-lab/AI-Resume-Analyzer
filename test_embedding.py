from sentence_transformers import SentenceTransformer

print("Chargement du modèle...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Modèle chargé !")

text = "Python is a programming language."

embedding = model.encode(text)

print("Embedding généré !")
print("Dimension :", len(embedding))
print("Premiers nombres :", embedding[:5])