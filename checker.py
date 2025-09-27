from zxcvbn import zxcvbn

def check_password_strength(password):
    result = zxcvbn(password)
    score = result['score']  # 0 to 4
    feedback = result['feedback']

    print(f"Password: {password}")
    print(f"Score (0-4): {score}")
    if feedback['warning']:
        print(f"Warning: {feedback['warning']}")
    if feedback['suggestions']:
        print("Suggestions:")
        for suggestion in feedback['suggestions']:
            print(f" - {suggestion}")

if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    check_password_strength(pwd)