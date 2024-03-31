import re

def validate_password(password, username, last_three_passwords):
    # Check minimum length
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."
    
    # Check character variety
    if not (sum(1 for c in password if c.isupper()) >= 2 and
            sum(1 for c in password if c.islower()) >= 2 and
            sum(1 for c in password if c.isdigit()) >= 2 and
            sum(1 for c in password if c in '@#$%&*!') >= 2):
        return False, "Password must contain at least two uppercase letters, two lowercase letters, two digits, and two special characters."
    
    # Check sequence and repetition restrictions
    if username:
        if any(username[i:i+3] in password for i in range(len(username) - 2)):
            return False, "Password should not contain any sequence of three or more consecutive characters from the username."
    if re.search(r'(.)\1\1\1', password):
        return False, "No character should repeat more than three times in a row."
    
    # Historical password check
    if password in last_three_passwords:
        return False, "New password must not be the same as the last three passwords used."
    
    return True, "Password is valid."

def main():
    username = input("Enter username (leave blank if none): ")
    last_three_passwords = []

    while True:
        password = input("Enter new password: ")
        is_valid, message = validate_password(password, username, last_three_passwords)
        if is_valid:
            print("Password set successfully.")
            # Update last three passwords
            last_three_passwords.append(password)
            if len(last_three_passwords) > 3:
                last_three_passwords.pop(0)
            break
        else:
            print("Invalid password:", message)

if __name__ == "__main__":
    main()
