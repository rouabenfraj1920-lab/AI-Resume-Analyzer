from src.pdf_reader import extract_text_from_pdf
from src.summarizer import summarize_cv

pdf_path = "data/cvs/cvPROF.pdf"

text = extract_text_from_pdf(pdf_path)

from src.cv_parser import structure_cv


cv_data = structure_cv(text)


structured_text = f"""
Education:
{cv_data['education']}

Skills:
{cv_data['skills']}

Experience:
{cv_data['experience']}

Projects:
{cv_data['projects']}
"""


summary = summarize_cv(structured_text)
print("\n===== RÉSUMÉ =====\n")
print(summary)