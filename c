def scan_message(text):
    """
    Checks SMS, WhatsApp, FB, TikTok, IG messages for scam patterns
    Returns: score, list_of_reasons
    """
    text = text.upper()
    
    # Keywords scammers use in Zim
    keywords = {
        "USD": 3, 
        "WIN": 3, 
        "WON": 3,
        "OTP": 4, 
        "ZESA": 2, 
        "ECOCASH": 2, 
        "ONE MONEY": 2,
        "URGENT": 2, 
        "LINK": 2, 
        "CLICK": 2,
        "ACCOUNT BLOCKED": 3,
        "100": 1,
        "HTTP": 2  # for links
    }
    
    score = 0
    reasons = []
    
    for word, points in keywords.items():
        if word in text:
            score += points
            reasons.append(word)
    
    # Extra: if it has a link + asks for money
    if "HTTP" in text and "USD" in text:
        score += 3
        reasons.append("LINK + USD")
        
    return score, reasons


def scan_number(num):
    """
    Checks if number is in blacklist numbers.txt
    """
    num = num.strip()
    try:
        with open("numbers.txt") as f:
            blacklist = f.read().splitlines()
    except:
        blacklist = []
    
    if num in blacklist:
        return 10, ["Number in blacklist"]
    if num.startswith("263100") or num.startswith("0770000"):
        return 8, ["Known scam prefix"]
        
    return 0, ["Number not found in blacklist"]
