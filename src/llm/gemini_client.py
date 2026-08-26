from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        import traceback
        traceback.print_exc()
        return str(e)
from src.models.resume_models import ResumeAnalysis


def analyze_resume(prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": ResumeAnalysis,
        },
    )

    return response.parsed