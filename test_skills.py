from src.skills_extractor import load_skills


skills = load_skills("data/skills.csv")


print("Nombre de compétences :", len(skills))

print("\nPremières compétences :")

print(skills[:10])