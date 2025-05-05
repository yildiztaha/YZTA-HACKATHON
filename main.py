import requests
import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import pipeline
from gtts import gTTS

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Unsplash API Key
UNSPLASH_API_KEY = "yl_fvFXsm8a40Uqw3eEsU7AYl96ao7pHqr8dDpWkjZQ"  # Unsplash API anahtarınızı buraya ekleyin

# Daha büyük model
generator = pipeline("text2text-generation", model="google/flan-t5-base")


# Sesli telaffuz için gTTS fonksiyonu
def create_pronunciation(word: str):
    audio_dir = "static/audio"
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)  # Eğer yoksa oluştur

    tts = gTTS(text=word, lang='en')
    filename = f"{audio_dir}/{word}.mp3"
    tts.save(filename)
    return "/" + filename  # Tarayıcıdan erişilebilir yol


# Unsplash API ile resim çekme fonksiyonu
def fetch_image(word: str):
    url = f"https://api.unsplash.com/photos/random?query={word}&client_id={UNSPLASH_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['urls']['regular']
    return None


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/", response_class=HTMLResponse)
async def explain_word(request: Request, word: str = Form(...)):
    word_cleaned = word.strip().lower()

    # Kelimenin anlamı ve örnek cümlesi
    prompt = (
        f"Word: {word}\n"
        "Explain the meaning of the word in simple English.\n"
        "Give a natural example sentence using the word.\n"
        "List 1 or 2 common synonyms."
    )
    result = generator(prompt, max_length=128)[0]["generated_text"]

    # Telaffuz oluştur
    pronunciation_path = create_pronunciation(word_cleaned)

    # Görsel çek
    image_url = fetch_image(word_cleaned)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "word": word_cleaned,
        "pronunciation": pronunciation_path,
        "image_url": image_url  # Görseli HTML'ye ekleyeceğiz
    })
