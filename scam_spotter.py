import random
import json
import os
from datetime import datetime

SCORES_FILE = "scores.json"

SCAMS = [
    {"text": "You've won $1000 EcoCash! Send $5 processing fee to claim.", "answer": "scam", "tip": "Real companies never ask you to pay to receive money."},
    {"text": "EcoCash: Your account will be blocked. Dial *150# to verify now.", "answer": "scam", "tip": "EcoCash never asks for PINs or codes via SMS."},
    {"text": "OneMoney: You received $20 from John. Check balance.", "answer": "legit", "tip": "Check your real balance with *303#"},
    {"text": "WhatsApp: Hello mum, I lost my phone. Send me airtime please.", "answer": "scam", "tip": "Call the person first to confirm."},
    {"text": "FREE BUNDLES! Click this link to claim your 10GB", "answer": "scam", "tip": "Fake links steal your login and money."}
]

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return {"played": 0, "correct": 0}

def save_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f)

def play_game():
    print("="*50)
    print(" DZIVISA SCAM - Spot the Zimbabwe Scam!")
    print(" Learn to protect yourself on EcoCash, OneMoney, WhatsApp")
    print("="*50)
    
    scores = load_scores()
    scam = random.choice(SCAMS)
    
    print(f"\nMessage: {scam['text']}")
    answer = input("\nIs this a SCAM or LEGIT? ").lower().strip()
    
    if answer == scam['answer']:
        print("\n✅ CORRECT! Well done!")
        scores["correct"] += 1
    else:
        print(f"\n❌ WRONG! This was a {scam['answer'].upper()}")
    
    print(f"Tip: {scam['tip']}")
    
    scores["played"] += 1
    save_scores(scores)
    print(f"\nYour Score: {scores['correct']}/{scores['played']}")

if __name__ == "__main__":
    play_game()
