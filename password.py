import secrets
import string

def generate_strong_password(length=12):
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars

    while True:
    
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        
        if (any(char in special_chars for char in password) and
            sum(char in digits for char in password) >= 2):
            return password

password = generate_strong_password(16)
print("Generated Strong Password:", password)
