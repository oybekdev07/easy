import cv2
import mediapipe as mp
from gtts import gTTS
import os

def recognize_sign_from_camera():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    cap = cv2.VideoCapture(0)

    print("✋ Imo-ishora tanlanmoqda...")
    result = ""

    while True:
        success, image = cap.read()
        if not success:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        if results.multi_hand_landmarks:
            # Hozircha test uchun doim "salom" deyamiz
            result = "salom"
            break

    cap.release()
    hands.close()
    print("✅ Tanlangan imo-ishora:", result)

    # Ruscha ovoz bilan o‘zbekcha matnni gapiradi
    tts = gTTS(result, lang='ru')
    tts.save("speech.mp3")
    os.system("mpg123 speech.mp3")

    return result