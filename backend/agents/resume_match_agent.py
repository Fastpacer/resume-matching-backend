# ===== backend/agents/resume_match_agent.py =====
from backend.core.llm_client import call_llm
import json


def resume_matching_agent(resume_text, job_description):
    # Robust prompt ensuring only valid JSON is returned
    prompt = f"""
System: You are a specialized resume-screening AI. Your sole output must be a valid JSON object matching the exact schema below—no markdown, no commentary.

Schema:
{{
  "score": <integer 0-100>,
  "missing_skills": [<string>, ...],
  "suggestions": [<string>, ...]
}}

Steps:
1. Extract required skills and qualifications from the Job Description.
2. Compare those with the Resume Text to determine overlap.
3. Compute a match score (integer between 0 and 100).
4. Populate "missing_skills" with any JD skills not present in the resume.
5. Provide actionable, concise suggestions under "suggestions".

Respond with ONLY the JSON object.

Example Output:
{{
  "score": 85,
  "missing_skills": ["Kubernetes", "AWS CI/CD"],
  "suggestions": ["Add Kubernetes deployment experience", "Mention AWS CI/CD pipelines"]
}}

Resume Text:
{resume_text}

Job Description:
{job_description}
"""
    # Call the LLM
    raw = call_llm(prompt)
    print("🔍 Raw LLM output:", raw)

    # Safely parse JSON with fallback
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "score": 0,
            "missing_skills": [],
            "suggestions": [
                "Error: LLM output was not valid JSON.",
                f"Raw output: {raw}"
            ]
        }