from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os

MODEL_PATH = "model/vosk-model-small-uz-0.22"
model = Model(MODEL_PATH)

def recognize_from_microphone():
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    print("🎤 Mikrofondan gapiring...")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result).get("text", "")
            print("✅ Tanildi:", text)
            return text