from flask import Flask, render_template, request

app = Flask(__name__)

scam_words = ["won", "congratulations", "claim", "otp", "pin", "password", "ecocash", "oneshot", "lottery", "agent", "free money"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    input_type = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        check_type = request.form["check_type"]
        
        found = [word for word in scam_words if word in user_input.lower()]
        
        if found:
            result = f"⚠️ SCAM DETECTED in {check_type}! Found: {', '.join(found)}"
        else:
            result = f"✅ {check_type} looks safe. But always verify!"
    
    return render_template("index.html", result=result, input_type=input_type)

if __name__ == "__main__":
    app.run(debug=True)
