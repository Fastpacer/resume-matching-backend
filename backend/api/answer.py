from fastapi import APIRouter
from backend.db.models import AnswerRequest
from backend.core.llm_client import call_llm

router = APIRouter(prefix="/api/answer")

@router.post("")
def generate_answer(req: AnswerRequest):
    prompt = f"""
    You are an AI that helps answer job application questions.
    Based on the profile and job description below, answer:
    '{req.question}'

    Profile:
    Name: {req.profile.name}
    Contact: {req.profile.contact}
    Education: {req.profile.education}
    Experience: {req.profile.experience}

    JD:
    {req.job_description}
    """
    response = call_llm(prompt)
    return {"answer": response}

