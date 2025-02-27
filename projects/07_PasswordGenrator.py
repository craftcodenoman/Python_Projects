import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


try:
    length = int(input("Enter the desired password length (min 6): "))
    password = generate_password(length)
    
    if password:
        print(f"Your generated password: {password}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
