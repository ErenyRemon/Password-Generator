import random
import string
print("Welcome to the Password Generator!")
num_characters = int(input("Enter the total number of characters in the password: "))
num_letters = int(input("Enter the number of letters in the password: "))
num_numbers = int(input("Enter the number of numbers in the password: "))
num_symbols = int(input("Enter the number of symbols in the password: "))
sum_numbers = num_letters + num_numbers + num_symbols
if num_characters == sum_numbers:
    password_chars =( 
    random.choices(string.ascii_letters, k = num_letters) +
    random.choices(string.digits, k = num_numbers) +
    random.choices(string.punctuation, k = num_symbols)
    )

    rand_shuffled = random.shuffle(password_chars)
    password = "".join(password_chars)
    print(f"Generated Password: {password}")

else: 
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password")

