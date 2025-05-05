# 📚 Kelime Öğretici Asistanı

İngilizce kelimeleri daha etkili öğrenmek için geliştirilen basit bir web uygulamasıdır. Yapay zeka desteklidir ve kullanıcıya:

- Kelimenin anlamını,
- Örnek bir cümle,
- Eşanlamlılar,
- Telaffuz sesi (TTS),
- Temsili bir görsel

sunmaktadır.

## 🚀 Kullanılan Teknolojiler

- FastAPI
- HTML & CSS
- gTTS
- Hugging Face (dil modeli)
- Unsplash API (görsel)

## ⚙️ Kurulum

### 1. Klonla ve Sanal Ortam Oluştur

```bash
git clone https://github.com/kullaniciadi/kelime-ogretici.git
cd kelime-ogretici
python -m venv .venv
```

### 2. Sanal Ortamı Aktifleştir

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 3. Gereksinimleri Kur ve Başlat

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Tarayıcıda `http://127.0.0.1:8000` adresine gidin.

## 📝 Notlar

- Görsel çekebilmek için [Unsplash API](https://unsplash.com/developers)'den ücretsiz bir API anahtarı almanız gereklidir.
- Ücretsiz modeller kullanıldığı için yanıtlar sade tutulmuştur.

## 📄 Lisans

MIT
