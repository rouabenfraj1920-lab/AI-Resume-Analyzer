def build_resume_prompt(cv_text):
    prompt = f"""
You are an AI Resume Analyzer.

Analyze the CV provided below and create a professional, factual analysis.

IMPORTANT RULES:
1. Use ONLY information explicitly present in the CV.
2. Never invent information.
3. Never assume experience that is not stated.
4. Do not confuse an interest with professional experience.
5. Do not invent companies, universities, certifications, dates, skills, or achievements.
6. If information is not available, do not guess.
7. Keep technical skills exactly as they appear when possible.
8. Give more importance to concrete projects, education, skills, and certifications.
9. Write the final summary in English.
10. Keep the summary concise and professional.

Return the analysis using exactly this structure:

PROFESSIONAL SUMMARY:
Write a concise professional summary of the candidate.

KEY SKILLS:
List the technical skills explicitly found in the CV.

PROJECTS:
List the important projects explicitly mentioned in the CV.
For each project, include:
- Project name
- Short description
- Technologies used, if available

EDUCATION:
List the education information explicitly present in the CV.

CERTIFICATIONS:
List certifications explicitly present in the CV.
If there are no certifications, write:
None mentioned in the CV.

IMPORTANT:
Do not add information that is not present in the CV. And do not make it soo long

CV:
{cv_text}
"""

    return prompt