def structure_cv(text):

    sections = {
        "education": "",
        "skills": "",
        "experience": "",
        "projects": ""
    }


    lines = text.split("\n")


    current_section = None


    for line in lines:

        line_clean = line.lower().strip()


        if "education" in line_clean:
            current_section = "education"

        elif "skills" in line_clean:
            current_section = "skills"

        elif "experience" in line_clean:
            current_section = "experience"

        elif "project" in line_clean:
            current_section = "projects"


        elif current_section:
            sections[current_section] += line + " "


    return sections