import secrets
import requests
from load import *

def generate_otp():
    return str(secrets.SystemRandom().randint(10**(OTP_LENGTH-1), (10**OTP_LENGTH)-1))

def is_valid_email(email):
    if not email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_.-"
    for char in local:
        if char not in allowed_chars:
            return False
    return domain in ALLOWED_DOMAINS

def get_token():
    url = "https://api.sendpulse.com/oauth/access_token"
    data = {
        "grant_type": "client_credentials",
        "client_id": API_USER,
        "client_secret": API_SECRET
    }
    response = requests.post(url, json=data)
    return response.json()["access_token"]

def send_otp(email, otp):
    token = get_token()
    url = "https://api.sendpulse.com/smtp/emails"
    data = {
        "email": {
            "subject": "Your OTP",
            "from": {"name": SENDER_NAME, "email": SENDER_EMAIL},
            "to": [{"email": email}],
            "text": f"Your OTP is: {otp}"
        }
    }
    response = requests.post(url, json=data, headers={"Authorization": f"Bearer {token}"})
    return response.json()

def verify_otp(user_otp, actual_otp):
    if user_otp == actual_otp:
        return True
    return False

while True:
    email = input("Enter your email: ")
    if not is_valid_email(email):
        print("Invalid email or domain not supported")
    else:
        otp = generate_otp()
        send_otp(email, otp)
        user_otp = input("Enter OTP: ")
        if verify_otp(user_otp, otp):
            print("OTP Verified Successfully!")
            break
        else:
            print("Invalid OTP, try again")