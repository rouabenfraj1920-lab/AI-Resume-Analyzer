import pandas as pd
import re


def load_skills(csv_path):
    """
    Load skills from CSV file.
    """

    skills_df = pd.read_csv(csv_path)

    return skills_df



def extract_skills(text, skills_df):

    found_skills = []

    text = text.lower()

    for _, row in skills_df.iterrows():

        skill = row["skill"].lower()

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append({
                "skill": row["skill"],
                "category": row["category"]
            })

    return found_skills