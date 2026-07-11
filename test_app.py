from app import validate_email

def test_validate_email():
    """
    Exactly 1 unit test function using pytest to check email validation logic.
    """
    # Test valid email formats
    assert validate_email("user@example.com") is True
    assert validate_email("first.last@domain.co.uk") is True
    assert validate_email("user+tag@example-domain.org") is True
    
    # Test invalid email formats
    assert validate_email("invalid-email") is False
    assert validate_email("user@") is False
    assert validate_email("@domain.com") is False
    assert validate_email("user@domain..com") is False
