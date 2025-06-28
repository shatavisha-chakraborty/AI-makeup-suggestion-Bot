import gradio as gr
import numpy as np
from sklearn.cluster import KMeans
import cv2

def get_suggestions_html(tone, suggestion):
    return """
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px;">
    """ + "".join([
        f"""
        <div style='background: linear-gradient(135deg, #f5e1ff, #fceaff); padding: 20px; border-radius: 15px; width: 230px;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.15); text-align: center;'>
            <h3 style='color: #6a0dad; font-family: Poppins;'>💜 {item}</h3>
            <p style='font-weight: bold;'>{suggestion[item.lower()]["name"]}</p>
            <a href='{suggestion[item.lower()]["link"]}' target='_blank' style='color: #d63384;'>🛍 Buy Now</a>
        </div>
        """ for item in ['Foundation', 'Lipstick', 'Blush', 'Highlighter']
    ]) + "</div>"



def get_skin_tone_and_suggestions(image):
    img = np.array(image)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([25, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(img_hsv, lower_skin, upper_skin)
    skin = cv2.bitwise_and(img, img, mask=mask)

    pixels = skin.reshape(-1, 3)
    pixels = pixels[~np.all(pixels == 0, axis=1)]
    if len(pixels) == 0:
        return "<h3 style='color:red;'>🚫 No skin tone detected. Please upload a clearer image.</h3>"

    kmeans = KMeans(n_clusters=1, random_state=42).fit(pixels)
    r, g, b = kmeans.cluster_centers_[0].astype(int)
    avg = (r + g + b) // 3

    if avg >= 230:
        tone = "Porcelain"
    elif avg >= 210:
        tone = "Ivory Fair"
    elif avg >= 185:
        tone = "Beige"
    elif avg >= 160:
        tone = "Warm Medium"
    elif avg >= 135:
        tone = "Olive Wheatish"
    elif avg >= 110:
        tone = "Golden Tan"
    elif avg >= 85:
        tone = "Rich Dusky"
    else:
        tone = "Deep Brown"

    suggestions = {
        "Ivory Fair": {
            "foundation": {"name": "Lakmé 9to5 Ivory Cream", "link": "https://www.nykaa.com/lakme-9to5/p/234567"},
            "lipstick": {"name": "Maybelline Peach Coral", "link": "https://www.amazon.in/dp/B07ZRYC3HG"},
            "blush": {"name": "Sugar Mini Blush Pink", "link": "https://www.nykaa.com/sugar-mini-blush/p/980231"},
            "highlighter": {"name": "Maybelline Master Chrome", "link": "https://www.amazon.com/dp/B074G57W4J"}
        },
        "Beige": {
            "foundation": {"name": "Maybelline Fit Me 115", "link": "https://www.nykaa.com/maybelline-fit-me/p/14523"},
            "lipstick": {"name": "Lakmé Rosewood", "link": "https://www.amazon.in/dp/B0789F8HYT"},
            "blush": {"name": "Swiss Beauty Coral", "link": "https://www.nykaa.com/swiss-beauty-blush/p/109234"},
            "highlighter": {"name": "Wet n Wild MegaGlo", "link": "https://www.amazon.com/dp/B01M0H4Y6F"}
        },
        "Warm Medium": {
            "foundation": {"name": "Lakmé Natural Sand", "link": "https://www.amazon.in/dp/B08HJWNFVK"},
            "lipstick": {"name": "Maybelline Brick Red", "link": "https://www.amazon.com/dp/B00XRDONDU"},
            "blush": {"name": "Colorbar Cheekillusion Rose", "link": "https://www.nykaa.com/colorbar-blush/p/98765"},
            "highlighter": {"name": "NYX Born to Glow", "link": "https://www.amazon.in/dp/B0853GFB9X"}
        },
        "Olive Wheatish": {
            "foundation": {"name": "Maybelline 228 Soft Tan", "link": "https://www.nykaa.com/maybelline-228/p/106107"},
            "lipstick": {"name": "Sugar Terracotta Nude", "link": "https://www.nykaa.com/sugar-lipstick/p/127312"},
            "blush": {"name": "Insight Peach Glow", "link": "https://www.amazon.in/dp/B0B4KH6JPN"},
            "highlighter": {"name": "L.A. Girl Strobe Lite", "link": "https://www.amazon.com/dp/B01MQTS20P"}
        },
        "Golden Tan": {
            "foundation": {"name": "L’Oréal Golden Cappuccino", "link": "https://www.amazon.in/dp/B07GRM9RWY"},
            "lipstick": {"name": "Lakmé Brick Orange", "link": "https://www.nykaa.com/lakme-lipstick/p/456712"},
            "blush": {"name": "Kiro Cinnamon Coral", "link": "https://www.nykaa.com/kiro-blush/p/108203"},
            "highlighter": {"name": "Fenty Beauty Trophy Wife", "link": "https://www.sephora.com/product/trophy-wife-P679900"}
        },
        "Rich Dusky": {
            "foundation": {"name": "Huda Beauty Toffee", "link": "https://www.nykaa.com/huda-toffee/p/98721"},
            "lipstick": {"name": "MAC Plum Diva", "link": "https://www.nykaa.com/mac-lipstick/p/12345"},
            "blush": {"name": "Maybelline Terracotta", "link": "https://www.amazon.in/dp/B07B9G7QF1"},
            "highlighter": {"name": "MAC Gold Deposit", "link": "https://www.amazon.com/dp/B001FB5GR8"}
        },
        "Deep Brown": {
            "foundation": {"name": "MAC NW50", "link": "https://www.nykaa.com/mac-nw50/p/653215"},
            "lipstick": {"name": "Nykaa Mocha Shot", "link": "https://www.nykaa.com/nykaa-lipstick/p/679823"},
            "blush": {"name": "SUGAR Berry Bold", "link": "https://www.nykaa.com/sugar-berry-blush/p/109876"},
            "highlighter": {"name": "Bobbi Brown Bronze Glow", "link": "https://www.sephora.com/product/bronze-glow-P123456"}
        },
        "Porcelain": {
            "foundation": {"name": "L’Oreal Porcelain", "link": "https://www.amazon.com/dp/B01ID4KJS2"},
            "lipstick": {"name": "Nude Pink", "link": "https://www.amazon.com/dp/B07J6J8VYG"},
            "blush": {"name": "Tarte Rosy Blush", "link": "https://www.sephora.com/product/tarte-blush-P112323"},
            "highlighter": {"name": "Becca Pearl", "link": "https://www.sephora.com/product/becca-pearl-P412"}
        }
    }

    s = suggestions.get(tone, None)
    if not s:
        return "<h3 style='color:red;'>⚠️ No suggestions for this tone.</h3>"

    return f"<h2 style='color: violet;'>💫 Skin Tone Detected: {tone}</h2>" + get_suggestions_html(tone, s)

with gr.Blocks(css="""
.gradio-container {
    background-image: url('https://shatavisha-drdz03.hf.space/file/girly.jpeg');
    background-size: cover;
    font-family: 'Poppins', sans-serif;
}
""") as demo:
    gr.Markdown("""
        <h1 style="color: #ff66cc; text-align: center;">💄 AI Makeup Suggestion Bot</h1>
        <p style="text-align: center; color: white;">Upload your selfie to get your personalized glam look 🌟</p>
    """)
    with gr.Row():
        image = gr.Image(type="pil", label="📸 Upload your image")

    result = gr.HTML()
    submit_btn = gr.Button("✨ Get My Glam Look")
    submit_btn.click(fn=get_skin_tone_and_suggestions, inputs=image, outputs=result)

demo.launch()
