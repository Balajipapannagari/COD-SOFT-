import random
import string

print("Password Generator")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Ask user for complexity level
print("\nChoose complexity level:")
print("1. Letters only (a-z, A-Z)")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter choice (1/2/3): ")

# Define character sets
if choice == '1':
    characters = string.ascii_letters
elif choice == '2':
    characters = string.ascii_letters + string.digits
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Defaulting to Letters + Numbers + Symbols.")
    characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for i in range(length))

# Display password
print(f"\nGenerated Password: {password}")
