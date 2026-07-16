#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
dzivisa-scam v10 - The Offline Guardian
A Termux/Python game to teach Zimbabwean students how to spot scams.

__author__ = "Aaron"
__email__ = "136aaronpaul@gmail.com"
__copyright__ = "Copyright 2026, Aaron (Bone.torun)"
__version__ = "10.0.0"
"""

import re
import time

def analyze_message(msg):
    """Analyzes a message for scam indicators."""
    score = 0
    flags = []
    
    # 1. Urgency Detection (Psychological Triggers)
    urgency_words = ["urgent", "immediately", "blocked", "suspended", "win", "claim", "now", "final warning", "act now"]
    if any(word in msg.lower() for word in urgency_words):
        score += 25
        flags.append("⚠️  HIGH URGENCY: Scammers want you to panic!")
        
    # 2. Financial Keywords
    money_words = ["ecocash", "onemoney", "wallet", "pin", "send money", "deposit", "cash"]
    if any(word in msg.lower() for word in money_words):
        score += 25
        flags.append("💰  FINANCIAL REQUEST: Never share PINs!")
        
    # 3. Suspicious Links
    if re.search(r'http[s]?://\S+', msg):
        score += 30
        flags.append("🔗  LINK DETECTED: Check the domain carefully!")
        
    # 4. Impersonation Attempts
    brand_words = ["econet", "netone", "bank", "police", "support team", "admin"]
    if any(word in msg.lower() for word in brand_words):
        score += 20
        flags.append("🎭  IMPERSONATION: Official bodies don't ask for PINs via SMS.")

    return score, flags

def main():
    print("=" * 40)
    print("🛡️  dzivisa-scam v10: The Offline Guardian")
    print("   Built by Aaron (@136aaronpaul)")
    print("=" * 40)
    print("\nPaste a suspicious SMS/WhatsApp message below:")
    print("(Type 'quit' to exit)\n")

    while True:
        msg = input("📩  Message: ")
        
        if msg.lower() == 'quit':
            print("\n👋 Stay safe! Remember: If it feels wrong, it IS wrong.")
            break
            
        if not msg.strip():
            continue

        risk, warnings = analyze_message(msg)
        
        print("\n--- 🛡️  AARON'S ANALYSIS ---")
        print(f"Risk Score: {risk}/100")
        
        for w in warnings:
            print(w)
            
        if risk >= 70:
            print("\n🚨  STOP! This is almost certainly a SCAM.")
            print("   ❌ Do NOT reply. ❌ Do NOT click links. ❌ Do NOT share PINs.")
        elif risk >= 40:
            print("\n⚠️  CAUTION: This looks suspicious.")
            print("   Verify with the official company directly before acting.")
        else:
            print("\n✅  Low risk detected, but always stay vigilant.")
        
        print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑  Interrupted by user. Exiting...")   
