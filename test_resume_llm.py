from src.pdf_reader import extract_text_from_pdf
from src.llm.gemini_client import analyze_resume
from src.prompts.resume_prompt import build_resume_prompt


# Chemin vers le CV
pdf_path = "data/cvs/cvPROF.pdf"


# 1. Extraire le texte du CV
cv_text = extract_text_from_pdf(pdf_path)

print("===== CV EXTRACTED =====")
print(cv_text[:500])


# 2. Construire le prompt
prompt = build_resume_prompt(cv_text)


# 3. Envoyer le CV à Gemini
analysis = analyze_resume(prompt)

# 4. Afficher le résumé
print("\n===== AI RESUME ANALYSIS =====")

print("\nSUMMARY:")
print(analysis.professional_summary)

print("\nSKILLS:")
print(analysis.skills)

print("\nPROJECTS:")
for project in analysis.projects:
    print("-", project.name)
    print("  Technologies:", project.technologies)

print("\nEDUCATION:")
for education in analysis.education:
    print("-", education.institution, education.period)

print("\nCERTIFICATIONS:")
print(analysis.certifications)