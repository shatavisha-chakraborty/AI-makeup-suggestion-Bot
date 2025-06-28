
# AI Makeup Suggestion Bot

Welcome to the **AI Makeup Suggestion Bot** — an intelligent beauty assistant that suggests the perfect foundation, lipstick, blush, and highlighter based on your skin tone using AI and computer vision. Upload your selfie and get personalized product recommendations in seconds. ✨

---

## 🌈 Features

- 📸 Upload your own selfie (JPG or PNG)
- 🧠 AI detects your **skin tone** using KMeans clustering
- 💄 Suggests:
  - Foundation
  - Lipstick
  - Blush
  - Highlighter
- 🇮🇳 Focus on Indian skin tones, with optional international tones
- 🎨 Stylish violet-pink themed layout
- 🛍 Product links from Nykaa, Amazon India, Sephora

---

## 🧠 How It Works

1. The user uploads a selfie.
2. The app isolates skin regions using OpenCV and HSV skin color masking.
3. KMeans clustering finds the dominant skin tone.
4. Based on the tone, the app selects the best matching makeup products from a curated database.
5. Results are displayed as aesthetic, colorful boxes with shopping links.

---

## 💻 Tech Stack

| Tool       | Purpose |
|----------- |---------|
| **Python** | Core programming |
| **Gradio** | Web UI for image upload and results |
| **OpenCV** | Image processing and skin detection |
| **NumPy**  | Pixel and array operations |
| **Scikit-learn (KMeans)** | Dominant color detection (clustering) |
| **HTML/CSS** | Styling of output and background |
| **Hugging Face Spaces** | Hosting the app online

---

## 🖼 Background Styling

The app uses a soft glam **background image** (`girly.jpeg`) hosted on Hugging Face, with pastel and violet tones to enhance visual appeal.

---

## 📦 WORKING PROTOTYPE

### 🔧 Option 1: Running on Hugging Face Spaces
> This project is live! Just click this link to try it out.
> https://huggingface.co/spaces/shatavisha-drdz03/makeupsuggestion


### 🧑‍💻 Option 2: Run Locally
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/makeup_suggestion
cd makeup_suggestion
pip install -r requirements.txt
python app.py
