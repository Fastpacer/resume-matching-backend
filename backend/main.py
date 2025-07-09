 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import profile, scoring, answer, applications

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router)
app.include_router(scoring.router)
app.include_router(answer.router)
app.include_router(applications.router)