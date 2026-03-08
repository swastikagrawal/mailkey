from dotenv import load_dotenv
import os

load_dotenv(".env")

API_USER         = os.getenv("SENDPULSE_API_USER")
API_SECRET       = os.getenv("SENDPULSE_API_SECRET")
SENDER_EMAIL     = os.getenv("SENDER_EMAIL")
SENDER_NAME      = os.getenv("SENDER_NAME")

ALLOWED_DOMAINS = os.getenv("ALLOWED_DOMAINS").split(",")

OTP_LENGTH       = int(os.getenv("OTP_LENGTH"))