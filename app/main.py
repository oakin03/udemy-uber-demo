from fastapi import FastAPI
from app.auth import router as auth_router
from app.courses import router as courses_router
from app.matching import router as matching_router

app = FastAPI(title="Udemy & Uber Demo")
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(courses_router, tags=["Courses"])
app.include_router(matching_router, tags=["Matching"])