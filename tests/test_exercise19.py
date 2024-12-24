
from ppeg.exercise19 import generate_password

def test_password_length_at_least_12():
    assert len(generate_password(8)) == 12

def test_password_structure_correct():
    password = generate_password(14)
    assert len(password) == 14
    assert any(c.isdigit() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c in "~!@#$%^&*()_+" for c in password)