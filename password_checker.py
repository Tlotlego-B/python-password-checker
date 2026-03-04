import re

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 4:
        return "Strong password"
    elif score >= 2:
        return "Medium password"
    else:
        return "Weak password"


password = input("Enter your password: ")
result = check_password_strength(password)

print(result)