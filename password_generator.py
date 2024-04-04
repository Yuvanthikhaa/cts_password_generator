import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    
def get_password_length():
    try:
        return int(input("Enter the length of the password: "))
    except ValueError:
        print("Error: Please enter a valid length.")

def get_password_characters():
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'

    characters = ''
    if symbols:
        characters += string.punctuation
    if numbers:
        characters += string.digits
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase

    if not any([symbols, numbers, uppercase, lowercase]):
        print("Error: Please select at least one character type.")
        return None
    return characters

def display_password(password):
    print("Generated Password:", password)
