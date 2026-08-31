"""
Password Strength Checker
--------------------------
A simple helpdesk tool to evaluate password strength based on
length, character variety, and common weak-password patterns.

Usage:
    python password_checker.py
"""

import re
import string

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "letmein", "admin", "welcome", "monkey", "iloveyou",
    "password1", "123456789", "football", "dragon", "sunshine"
}


def check_length(password: str) -> tuple[int, str]:
    length = len(password)
    if length < 8:
        return 0, "Too short (minimum 8 characters recommended)"
    elif length < 12:
        return 1, "Acceptable length"
    else:
        return 2, "Strong length"


def check_character_variety(password: str) -> tuple[int, list[str]]:
    score = 0
    missing = []

    if any(c in string.ascii_lowercase for c in password):
        score += 1
    else:
        missing.append("lowercase letter")

    if any(c in string.ascii_uppercase for c in password):
        score += 1
    else:
        missing.append("uppercase letter")

    if any(c in string.digits for c in password):
        score += 1
    else:
        missing.append("number")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        missing.append("special character")

    return score, missing


def check_common_patterns(password: str) -> list[str]:
    warnings = []
    lowered = password.lower()

    if lowered in COMMON_PASSWORDS:
        warnings.append("This is a commonly used password — avoid it")

    if re.search(r'(.)\1{2,}', password):
        warnings.append("Contains repeated characters (e.g. 'aaa')")

    if re.search(r'(0123|1234|2345|3456|4567|5678|6789|abcd|bcde|cdef)', lowered):
        warnings.append("Contains a sequential pattern (e.g. '1234' or 'abcd')")

    if re.fullmatch(r'[A-Za-z]+', password):
        warnings.append("Contains only letters — add numbers/symbols")

    if re.fullmatch(r'[0-9]+', password):
        warnings.append("Contains only numbers — add letters/symbols")

    return warnings


def rate_password(password: str) -> dict:
    length_score, length_msg = check_length(password)
    variety_score, missing = check_character_variety(password)
    warnings = check_common_patterns(password)

    total_score = length_score + variety_score  # max 6

    if warnings or total_score <= 2:
        rating = "Weak"
    elif total_score <= 4:
        rating = "Moderate"
    elif total_score <= 5:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {
        "rating": rating,
        "score": f"{total_score}/6",
        "length_feedback": length_msg,
        "missing_character_types": missing,
        "warnings": warnings,
    }


def print_report(password: str) -> None:
    result = rate_password(password)
    print("\n" + "=" * 40)
    print(f" PASSWORD STRENGTH REPORT")
    print("=" * 40)
    print(f"Rating       : {result['rating']}")
    print(f"Score        : {result['score']}")
    print(f"Length check : {result['length_feedback']}")

    if result["missing_character_types"]:
        print(f"Missing      : {', '.join(result['missing_character_types'])}")
    else:
        print("Missing      : none — good variety")

    if result["warnings"]:
        print("Warnings:")
        for w in result["warnings"]:
            print(f"  - {w}")
    else:
        print("Warnings     : none")
    print("=" * 40 + "\n")


def main():
    print("Password Strength Checker")
    print("Type 'quit' to exit.\n")

    while True:
        pwd = input("Enter a password to check: ")
        if pwd.lower() == "quit":
            print("Goodbye!")
            break
        if not pwd:
            print("Please enter a non-empty password.\n")
            continue
        print_report(pwd)


if __name__ == "__main__":
    main()