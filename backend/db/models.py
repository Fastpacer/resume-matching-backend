from pydantic import BaseModel, Field

class Profile(BaseModel):
    name: str
    contact: str
    education: str
    experience: str

class JDAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str

class AnswerRequest(BaseModel):
    question: str
    profile: Profile
    job_description: str

class Application(BaseModel):
    title: str
    company: str
    status: str
    last_updated: str
