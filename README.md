# 🖼️ Image to Speech AI

An AI-powered web app that **describes images** and **reads them aloud** using Hugging Face Transformers and Gradio.  
Just upload an image — the model will generate a caption and convert it into speech!

---

## 🚀 Features

- 🧠 Automatic image captioning using `Salesforce/blip-image-captioning-base`
- 🔊 Text-to-speech synthesis using `facebook/fastspeech2-en-ljspeech`
- 💻 Simple Gradio interface for real-time interaction
- ⚡ Runs locally — no external API calls needed once models are cached

---

## 🧱 Project Structure

image-to-speech/
│
├── app.py # Main app file
├── requirements.txt # Dependencies
└── README.md # Project documentation


## ⚙️ Installation
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
Install dependencies


pip install -r requirements.txt
Run the app


python app.py
🧠 How It Works
Upload an image in the web app.

The BLIP model generates a caption describing the image.

The FastSpeech2 model converts the caption into audio speech.

You can read and listen to the result instantly!

🧩 Models Used
🏞️ Salesforce/blip-image-captioning-base
Generates captions from images.

🎙️ facebook/fastspeech2-en-ljspeech
Converts text into realistic human-like speech.


🧾 License
This project is open-source and available under the MIT License.

✨ Author
Khushi Chauhan







