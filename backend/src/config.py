import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT")
FRONTEND_HOST = os.getenv("FRONTEND_HOST")
MONGODB_CONN_STR = os.getenv("MONGO_CONNECTION_STRING")
MONGODB_DB_NAME = os.getenv("MONGO_DATABASE_NAME")