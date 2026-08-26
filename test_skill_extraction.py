from src.pdf_reader import extract_text_from_pdf
from src.preprocessing import preprocess_text
from src.skills_extractor import load_skills, extract_skills


pdf_path = "data/cvs/cvPROF.pdf"


# 1. Lire le CV
text = extract_text_from_pdf(pdf_path)


# 2. Prétraitement NLP
tokens = preprocess_text(text)


# Transformer tokens en texte
clean_text = " ".join(tokens)


# 3. Charger les compétences
skills = load_skills("data/skills.csv")


# 4. Extraction
found = extract_skills(clean_text, skills)


print("Compétences trouvées :\n")

categories = {}

for item in found:

    category = item["category"]

    if category not in categories:
        categories[category] = []

    categories[category].append(item["skill"])


for category, skills in categories.items():

    print("\n📌", category)

    for skill in skills:
        print("✅", skill)