def build_resume_analysis_prompt(cv_text):

    prompt = f"""
You are an AI Resume Analyzer.

Analyze the following resume and extract information ONLY from the provided text.

IMPORTANT RULES:
- Do not invent information.
- Do not infer missing information.
- Do not add skills, projects, technologies, dates, or certifications that are not explicitly present.
- If a field is not present in the resume, return an empty list or an empty string.
- Keep the extracted information faithful to the resume.
- Write all extracted information in English.

Resume:
{cv_text}

Extract the following:

1. Professional summary
2. Skills
3. Projects
   - project name
   - description
   - technologies explicitly mentioned
4. Education
   - institution
   - field
   - period
5. Certifications

Return the information according to the required structured schema.
"""

    return prompt