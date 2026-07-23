import re
COUNTRIES = {
    "ZW": {"name": "Zimbabwe", "money": ["ecocash"], "official": ["ecocash.co.zw"]},
}
def analyze_message(msg):
    l=msg.lower(); s=0; f=[]
    if any(x in l for x in ["urgent","blocked","5 minutes"]): s+=30; f.append("URGENCY")
    if "http" in l: s+=30; f.append("LINK")
    if "ecocash" in l and "ecocash.co.zw" not in l and "http" in l: s+=40; f.append("FAKE DOMAIN")
    if "*150#" in msg: s+=25; f.append("USSD scam")
    if s>100: s=100
    return s,f,"ZW"
def main():
    print("🛡️ dzivisa-scam v11.1 - 12 Country")
    while True:
        m=input("\nPaste msg (quit to exit): ")
        if m=="quit": break
        s,f,c=analyze_message(m)
        print(f"Score {s}/100 - {f}")
main()
