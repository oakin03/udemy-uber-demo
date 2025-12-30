from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json

router = APIRouter()

def simulate_payment(card_number: str) -> bool:
    # Kart numarasının son hanesi çift ise ödeme başarılı. Aksi takdirde başarısız.
    # If the last digit of card number is even, then payment will be successful. Otherwise payment will be failed.
    last_digit = int(card_number[-1])
    return last_digit % 2 == 0


class PurchaseRequest(BaseModel):
    user_id: int
    course_id: int
    card_number: str

@router.get("/courses")
def get_courses():
    with open("data/courses.json", "r", encoding="utf-8") as f:
        courses = json.load(f)
    return courses

@router.post("/purchase")
def purchase_course(request: PurchaseRequest):

    with open("data/courses.json", "r", encoding="utf-8") as f:
        courses = json.load(f)

    course = next((c for c in courses if c["id"] == request.course_id), None)
    if not course:
        raise HTTPException(status_code=404, detail="Course is not found / Kurs bulunamadı.")

    payment_success = simulate_payment(request.card_number)

    if not payment_success:
        raise HTTPException(
            status_code=400,
            detail="Payment failed / Ödeme başarısız."
        )

    # If payment is successful / Ödeme başarılıysa.
    with open("data/purchases.json", "r", encoding="utf-8") as f:
        purchases = json.load(f)

    purchases.append({
        "user_id": request.user_id,
        "course_id": request.course_id
    })

    with open("data/purchases.json", "w", encoding="utf-8") as f:
        json.dump(purchases, f, ensure_ascii=False, indent=2)

    return {"message": "Payment successful / Ödeme başarılı."}

@router.get("/my-courses/{user_id}")
def get_my_courses(user_id: int):
    with open("data/purchases.json", "r", encoding="utf-8") as f:
        purchases = json.load(f)

    with open("data/courses.json", "r", encoding="utf-8") as f:
        courses = json.load(f)

    user_course_ids = [
        p["course_id"] for p in purchases if p["user_id"] == user_id
    ]

    user_courses = [
        c for c in courses if c["id"] in user_course_ids
    ]

    return user_courses
