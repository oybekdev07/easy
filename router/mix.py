from fastapi import APIRouter

from router.sign_recognizer import recognize_sign_from_camera
from router.speech_recognizer import recognize_from_microphone

mix_router = APIRouter()

@mix_router.get("/")
def mix_endpoint():
    return {"message": "Mix API"}

@mix_router.get("/recognize/speech")
def recognize_speech():
    result = recognize_from_microphone()
    return {"recognized_text": result}

@mix_router.get("/recognize/sign")
def recognize_sign():
    result = recognize_sign_from_camera()
    return {"recognized_sign": result}

