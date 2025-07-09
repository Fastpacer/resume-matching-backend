# 🤖 Job Assistant AI Agent

A backend-only AI-powered tool that analyzes resumes against job descriptions using an LLM (via Groq API) and returns structured JSON feedback. Designed as a modular, extensible foundation for resume screening tools, this project showcases how to make LLM output safe, reliable, and developer-friendly — all while preparing for a more agentic, scalable future.

---

## 🧠 Overview

This project is a backend implementation of a resume–job description matching system powered by **LLMs via Groq API**. It’s built with **FastAPI**, uses structured prompting, and ensures clean JSON output with fallback handling.

---

## 🧰 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Groq API (for LLM calls)**
- **Structured Prompt Engineering**
- **Uvicorn for dev server**

---

## 💼 What It Does

Given:
- A resume (plain text)
- A job description (plain text)

It returns:

```json
{
  "score": 80,
  "missing_skills": [
    "ML Engineer",
    "Zapier",
    "data transformation workflows"
  ],
  "suggestions": [
    "Highlight experience with ML engineering",
    "Mention proficiency with Zapier or similar automation tools",
    "Emphasize experience with data transformation workflows"
  ]
}
✨ Features
✅ Clean JSON output schema

✅ Controlled prompt with fixed structure

✅ Automatic error fallback if LLM output is malformed

✅ Modular agent callable from any backend service

✅ Easily extendable for new agent types

🗂 Project Structure
graphql
Copy
Edit
Job_Assistant_AI_Agent/
├── backend/
│   ├── agents/
│   │   └── resume_match_agent.py      # LLM-powered resume scoring logic
│   ├── api/
│   │   └── scoring.py                 # FastAPI POST endpoint
│   └── core/
│       └── llm_client.py             # Groq API call abstraction
├── requirements.txt
└── README.md
⚙️ How to Run
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/<your-username>/job-assistant-agent.git
cd job-assistant-agent
2. Set up the environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Add your Groq API key
Create a .env file:

env
Copy
Edit
GROQ_API_KEY=your-groq-key-here
4. Run the server
bash
Copy
Edit
uvicorn backend.api.scoring:app --reload
Visit: http://localhost:8000/docs

🧪 Sample Request
POST /api/resume/score

Payload:

json

{
  "resume_text": "Data scientist with strong experience in Python and ML...",
  "job_description": "Looking for an ML Engineer with skills in Zapier and orchestration workflows..."
}

📈 Future Scope
If time had permitted, I would have loved to extend this project in the following directions:

🧠 Agentic Capabilities
Integrate LangChain for memory, tool use, and dynamic reasoning

Use LangSmith for traceability, versioning, and performance debugging

Expand agents to multi-turn workflows (e.g., auto-apply or resume rewriting)

🎯 Frontend Development
Build a Streamlit or Next.js frontend for uploading resumes and displaying score reports interactively

Add login and profile dashboards for job seekers or recruiters

✅ Testing & Evaluation
Add unit tests using pytest

Incorporate mock API tests for robustness

Add a resume parsing pipeline for handling raw .pdf or .docx

😓 Challenges Faced
Getting Groq LLMs to strictly follow JSON schema

Catching malformed responses and handling them gracefully

Staying backend-focused due to limited time while juggling multiple workflows

🙋‍♂️ Author
Atharva Salpekar

💼 www.linkedin.com/in/atharva-salpekar-084019215
