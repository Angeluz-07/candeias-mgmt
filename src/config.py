import os

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "")
ALLOWED_ORIGINS = [origin.strip() for origin in ALLOWED_ORIGINS.split(",")]

CLERK_URI = os.getenv("CLERK_URI", "")
POSTGRES_URI = os.getenv("POSTGRES_URI", "")