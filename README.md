# Mailkey
Mailkey is a terminal-based email OTP authentication system built with Python and SendPulse API.
It validates the user's email, sends a one-time password, and verifies it — all from the terminal.

---

## Features
- Email validation with allowed domain whitelist
- OTP generation using Python's `secrets` module
- OTP delivery via SendPulse Email API
- Simple terminal-based verification flow

---

## Tech Stack
- Python
- SendPulse API

---

## How it Works
1. User enters their email address
2. Email is validated for format and allowed domain
3. OTP is generated and sent via SendPulse
4. User enters OTP in the terminal
5. If correct → `OTP Verified Successfully!`

---

## Setup
Install dependencies:
```bash
pip install -r requirements.txt
```
Fill in your credentials in `.env`:
```bash
SENDPULSE_API_USER=<YOUR_SENDPULSE_API_USER>
SENDPULSE_API_SECRET=<YOUR_SENDPULSE_API_SECRET>
SENDER_EMAIL=<YOUR_SENDER_EMAIL>
SENDER_NAME=<YOUR_SENDER_NAME>
ALLOWED_DOMAINS=<COMMA_SEPARATED_DOMAINS>
OTP_LENGTH=<OTP_LENGTH>
OTP_EXPIRY_SEC=<OTP_EXPIRY_IN_SECONDS>
```
Run:
```bash
python main.py
```
