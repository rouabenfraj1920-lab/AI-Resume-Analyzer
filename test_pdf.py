from src.pdf_reader import extract_text_from_pdf
from src.preprocessing import preprocess_text

pdf_path = "data/cvs/cvROUA.pdf"

try:
    text = extract_text_from_pdf(pdf_path)

    tokens = preprocess_text(text)

    print("Premiers tokens :")
    print(tokens[:50])

except Exception as error:
    print(error)