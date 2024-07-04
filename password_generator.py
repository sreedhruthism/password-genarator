import random
import string

def generate_password(length):
    """
    Generates a random password with the given length.
    The password will include uppercase, lowercase, digits, and special characters.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the remaining length with random choices from all sets
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to ensure random order
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

def generate_passwords(length, count):
    """
    Generates a specified number of random passwords with the given length.
    """
    return [generate_password(length) for _ in range(count)]

def main():
    # Instructions for the user
    print("Welcome to the Secure Password Generator!")
    print("You can specify the length and number of passwords to generate.")
    
    # Get user input for password length and number of passwords
    try:
        length = int(input("Enter the desired length of the passwords: "))
        count = int(input("Enter the number of passwords to generate: "))
        
        # Generate passwords
        passwords = generate_passwords(length, count)
        
        # Display the generated passwords
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"{i}. {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
print("Sree Dhruthi Mulakaledu Jain University")