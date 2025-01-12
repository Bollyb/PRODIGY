import re

def password_strength(password):
    Length = len(password)
    Uppercase = any(c.isupper() for c in password)
    Lowercase = any(c.islower() for c in password)
    Digit = any(c.isdigit() for c in password)
    Special_C = bool(re.match(r'[!@#$%^&*().,?;:"{}[]\/]', password))

    score = 0
    feedback = []

    if Length >= 12:
        score += 1
    elif Length >= 8:
        feedback.append("Consider using more stronger password for security Purpose")

    if Uppercase and Lowercase:
        score += 1
    else:
        feedback.append("Uppercase and Lowercase are Mixing, consider adding it for security")

    if Digit:
        score += 1
    else:
        feedback.append("Need to include number for the password complexity")

    if Special_C:
        score += 1
    else:
        feedback.append("Adding special character can be another strong security layer for security")


    if score >= 3:
        
        return "This is a strong password! keep it safe."
    else:
        return "Weak password. "+" ".join(feedback)

if __name__ == "__main__":
    print("You are welcome to password Complexity Checker")
    print("Enter your password blow")

    while True:
        password = input("> ")
        if password.lower() == 'exit':
            print("Exting...")
            break
        str_feedback = password_strength(password)
        print(str_feedback)
