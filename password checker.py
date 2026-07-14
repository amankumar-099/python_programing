import re

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"


def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not any(char in SPECIAL_CHARACTERS for char in password):
        return False
    return True


def password_feedback(password: str) -> str:
    if is_strong_password(password):
        return "Password is strong."

    reasons = []
    if len(password) < 8:
        reasons.append("at least 8 characters")
    if not re.search(r"[A-Z]", password):
        reasons.append("an uppercase letter")
    if not re.search(r"[a-z]", password):
        reasons.append("a lowercase letter")
    if not re.search(r"\d", password):
        reasons.append("a digit")
    if not any(char in SPECIAL_CHARACTERS for char in password):
        reasons.append("a special character")

    return "Password should include " + ", ".join(reasons) + "."


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(password_feedback(pwd))
