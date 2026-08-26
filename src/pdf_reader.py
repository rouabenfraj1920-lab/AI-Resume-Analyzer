import pymupdf
import os


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str): Path of the PDF file.

    Returns:
        str: Extracted text.
    """

    # Vérifier si le fichier existe
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(
            f"Le fichier PDF n'existe pas : {pdf_path}"
        )

    try:
        document = pymupdf.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    except Exception as error:
        raise Exception(
            f"Erreur lors de la lecture du PDF : {error}"
        )