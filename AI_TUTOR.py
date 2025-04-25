import pyttsx3
import google.generativeai as genai
from gtts import gTTS 
import os 


API_KEY = "AIzaSyDKCl0dIoS7P2wZJohOCTaZomBkHEIiGT0" 
genai.configure(api_key=API_KEY)
engine = pyttsx3.init()
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
model_config = {
    "temperature": 1,
    "top_p": 0.99,
    "top_k": 0,
    "max_output_tokens": 4096,
}

while True:
    query = input("ASK QUESTIONS TO ME ")
    if query.lower() == "exit":
        break
    response = model.generate_content([f"Imagine yourself as a tutor named MR. Noodel. Your goal is to explain the concept of {query} in an easy-to-understand and engaging way. Keep it simple and clear."])
    clean_response = response.text.replace("*", "") 
    print(clean_response)
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 1.0)
    engine.say(clean_response)
    engine.runAndWait()
