from fastapi import APIRouter
from backend.db.database import conn
from backend.db.models import Application

router = APIRouter(prefix="/api/applications")

@router.post("")
def add_application(app: Application):
    conn.execute("INSERT INTO applications (title, company, status, last_updated) VALUES (?, ?, ?, ?)",
                 (app.title, app.company, app.status, app.last_updated))
    conn.commit()
    return {"message": "Application saved."}

@router.get("")
def list_applications():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications")
    rows = cursor.fetchall()
    return [{"title": row[1], "company": row[2], "status": row[3], "last_updated": row[4]} for row in rows]


