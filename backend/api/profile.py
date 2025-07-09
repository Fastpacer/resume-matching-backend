from fastapi import APIRouter
from backend.db.database import conn
from backend.db.models import Profile

router = APIRouter(prefix="/api/profile")

@router.post("/")
def save_profile(profile: Profile):
    conn.execute("INSERT INTO profiles (name, contact, education, experience) VALUES (?, ?, ?, ?)",
                 (profile.name, profile.contact, profile.education, profile.experience))
    conn.commit()
    return {"message": "Profile saved."}

@router.get("/")
def get_profile():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profiles ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        return {"name": row[1], "contact": row[2], "education": row[3], "experience": row[4]}
    return {"message": "No profile found."}
