from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Database
from db import Base, engine

# Routers
from router.users import router as user_router
from router.translations import router as translation_router
from router.mix import mix_router

# FastAPI app
app = FastAPI(title="EasyTalk", docs_url='/docs')

# Static files (images)
app.mount("/images", StaticFiles(directory="images"), name="images")

# Static files (frontend v1 va v2)
app.mount("/frontend-v1", StaticFiles(directory="frontend/frontend-v1", html=True), name="frontend-v1")
app.mount("/frontend-v2", StaticFiles(directory="frontend/frontend-v2", html=True), name="frontend-v2")

# Create all database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(translation_router, prefix="/api/translations", tags=["Translations"])
app.include_router(mix_router, prefix="/api/mix", tags=["Mix"])

# CORS middleware (frontend uchun ruxsat)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "EasyTalk Backend is running!"}

