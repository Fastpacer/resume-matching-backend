from fastapi import APIRouter
from backend.db.models import JDAnalysisRequest
from backend.agents.resume_match_agent import resume_matching_agent

router = APIRouter(prefix="/api/resume")

@router.post("/score")
def score_resume(data: JDAnalysisRequest):
    return resume_matching_agent(data.resume_text, data.job_description)
