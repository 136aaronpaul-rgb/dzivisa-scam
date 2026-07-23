# dzivisa-scam 🇿🇼
Stop SMS/WhatsApp scams in Zimbabwe.

Scammers are sending fake "Your service could not be renewed" and "You WON USD 1000" messages to steal money and OTPs. 
dzivisa-scam is a simple offline tool that checks suspicious messages against a community blacklist and warns you instantly.

## Features
- **Detects Zim scam patterns**: `100`, `263100`, `SMS USD`, `WIN USD`, `OTP`
- **Works offline**: No internet needed after you clone it
- **Simple**: Just paste the message and get a warning
- **Community blacklist**: You can add new scam numbers to `numbers.txt`

## How to use
```bash
git clone https://github.com/136aaronpaul-rgb/dzivisa-scam.git
cd dzivisa-scam
python main.py
