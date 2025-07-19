from email_validator import validate_email, EmailNotValidError

def email_validator(email: str) -> bool:
    try:
        validate_email(email)
        return True
    
    except EmailNotValidError as e:
        return False