def load_blacklist():
    with open("numbers.txt", "r") as f:
        return [line.strip().lower() for line in f]

def check_scam(message):
    blacklist = load_blacklist()
    message_lower = message.lower()
    for pattern in blacklist:
        if pattern in message_lower:
            return True
    return False

print("=== dzivisa-scam v1.0 ===")
user_input = input("Paste the suspicious SMS/WhatsApp message: ")
if check_scam(user_input):
    print("\n⚠️ WARNING: This looks like a scam!")
else:
    print("\n✅ No known scam patterns found.")
