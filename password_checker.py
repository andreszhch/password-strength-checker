def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&*)")

    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions:", ", ".join(feedback))

password = input("Enter a password to check: ")
check_password_strength(password)
