from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json

router = APIRouter()

class LiveLessonRequest(BaseModel):
    user_id: int
    course_id: int

@router.post("/live-request")
def create_live_request(request: LiveLessonRequest):
    with open("data/users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    instructors = [u for u in users if u["role"] == "instructor"]

    if not instructors:
        raise HTTPException(status_code=404, detail="No instructor found / Eğitmen bulunamadı.")

    assigned_instructor = instructors[0]

    # talebi kaydet
    with open("data/live_requests.json", "r", encoding="utf-8") as f:
        live_requests = json.load(f)

    live_requests.append({
        "user_id": request.user_id,
        "course_id": request.course_id,
        "instructor_id": assigned_instructor["id"],
        "status": "assigned"
    })

    with open("data/live_requests.json", "w", encoding="utf-8") as f:
        json.dump(live_requests, f, ensure_ascii=False, indent=2)

    print(
        f"Notification: A new live lesson request has been sent to {assigned_instructor['name']}.\n"
        f"Bildirim: {assigned_instructor['name']}'e yeni bir canlı ders talebi iletildi."
    )
    return {
        "message": "A request for a live lesson has been created. / Canlı ders talebi oluşturuldu.",
        "assigned_instructor": assigned_instructor["name"]
    }
