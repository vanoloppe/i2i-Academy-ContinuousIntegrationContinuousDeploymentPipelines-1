import re

def validate_email(email: str) -> bool:
    """
    Validates if the provided string is a valid email format.
    
    Args:
        email (str): The email string to validate.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))
