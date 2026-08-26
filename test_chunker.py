from src.pdf_reader import extract_text_from_pdf
from src.rag.chunker import chunk_text

# Lire le CV
pdf_path = "data/cvs/cvPROF.pdf"

text = extract_text_from_pdf(pdf_path)

# Découper en chunks
chunks = chunk_text(text)

print("Nombre de chunks :", len(chunks))

print("\n===== CHUNKS =====\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"----- Chunk {i} -----")
    print(chunk)
    print()
    