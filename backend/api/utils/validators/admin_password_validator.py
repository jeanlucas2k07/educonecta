from os import getenv
from dotenv import  load_dotenv

load_dotenv()

def admin_password_validator(password: str) -> bool:
    return getenv("ADMIN_PASSWORD") == password