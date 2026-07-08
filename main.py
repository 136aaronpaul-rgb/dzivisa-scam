print("=== DZIVISA-SCAM v1.0 ===")
print("Tool to detect scams in Zimbabwe\n")

scam_keywords = ["winner", "lottery", "ecocash pin", "bank verification", "agent fee", "click link", "free airtime", "low balance", "switch_currency", "sms usd to", "renewed", "urgent", "account blocked"]

msg = input("Paste the suspicious SMS/WhatsApp message: ")

if any(word in msg.lower() for word in scam_keywords):
    print("\n⚠️ WARNING: This looks like a scam! Do NOT send money or share codes.")
else:
    print("\n✅ No obvious scam keywords found. Still verify the sender.")
