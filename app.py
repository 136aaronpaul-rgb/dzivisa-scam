from flask import Flask, request
import scam_spotter
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    result = "Welcome! Paste a message to check."
    css_class = ""
    if request.method == "POST":
        user_input = request.form["input"]
        score, reasons = scam_spotter.scan_message(user_input)
        if score > 4:
            result = f"SCAM DETECTED! Reasons: {', '.join(reasons)}"
            css_class = "scam"
        else:
            result = "SAFE. No scam patterns found."
            css_class = "safe"
            
    year = datetime.datetime.now().year
    return f'''
    <style>
    body{{font-family:Arial; max-width:700px; margin:20px auto; padding:10px; background:#f0f2f5}}
    .header{{background:#004d00; color:white; padding:20px; text-align:center; border-radius:10px}}
    .header h2{{margin:0}} .header p{{margin:5px 0}}
    .result{{padding:15px; margin-top:10px; border-radius:8px; font-weight:bold}}
    .safe{{background:#d4edda; color:#155724; border:1px solid #c3e6cb}} 
    .scam{{background:#f8d7da; color:#721c24; border:1px solid #f5c6cb}}
    textarea{{width:100%; padding:10px; border-radius:5px; border:1px solid #ccc; box-sizing:border-box}} 
    button{{padding:10px 20px; background:#004d00; color:white; border:none; border-radius:5px; cursor:pointer; margin-top:10px}}
    button:hover{{background:#003300}}
    .footer{{text-align:center; margin-top:20px; font-size:12px; color:gray}}
    </style>
    
    <div class="header">
        <h2>dzivisa-scam v11 🇿🇼</h2>
        <p><b>Built by Aaron Paul</b></p>
        <small>Protecting Zimbabweans from SMS & WhatsApp Scams</small>
    </div>
    
    <form method="post">
    <textarea name="input" rows="4" placeholder="Paste SMS/WhatsApp message here"></textarea><br>
    <button>Scan Message</button>
    </form>
    
    <div class="result {css_class}">{result}</div>
    
    <div class="footer">
        © {year} Aaron Paul | If you sent money to a scammer, call 111
    </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
