from flask import Flask, render_template, request
import re

app = Flask(__name__)

scam_words = ["won", "congratulations", "claim", "otp", "pin", "password", "ecocash", "oneshot", "lottery", "agent", "free money", "click link"]

tips = {
    "Message": "Tip: Real companies never ask for OTP/PIN. Report to 111.",
    "WhatsApp": "Tip: Scammers use new +263 78 numbers. Don't send money to strangers.",
    "Call": "Tip: Banks never ask for Ecocash PIN on call. Hang up.",
    "Facebook": "Tip: Fake FB pages have no blue tick and few followers.",
    "Instagram": "Tip: 'You won' DMs on IG are 99% scams. Check for verified badge.",
    "TikTok": "Tip: 'Send money to get money' on TikTok is always a scam."
}

def scan_text(text, check_type):
    found = [word for word in scam_words if word in text.lower()]
    is_number = re.search(r'\+?263[0-9]{9}', text)
    is_link = "http" in text or "facebook.com" in text or "instagram.com" in text or "tiktok.com" in text
    
    if found or (check_type in ["WhatsApp", "Call"] and is_number) or (check_type in ["Facebook", "Instagram", "TikTok"] and is_link):
        return f"⚠️ POSSIBLE SCAM in {check_type}!", tips[check_type]
    else:
        return f"✅ {check_type} looks okay.", tips[check_type]

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    user_input = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        types = ["Message", "WhatsApp", "Call", "Facebook", "Instagram", "TikTok"]
        for t in types:
            res, tip = scan_text(user_input, t)
            results.append({"type": t, "result": res, "tip": tip})
    
    return render_template("index.html", results=results, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
