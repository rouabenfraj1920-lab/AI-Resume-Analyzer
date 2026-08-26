from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]
class Education(BaseModel):
    institution: str
    field: str | None
    period: str | None
class ResumeAnalysis(BaseModel):
    professional_summary: str
    skills: list[str]
    projects: list[Project]
    education: list[Education]
    certifications: list[str]