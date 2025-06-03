import random

letters = list("qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM")
numbers = list("0123456789")
symbols = ['!', '#', '$', '%', '&', '+', '-']

print("🔐 Welcome to the Password Generator!\n")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Damit nicht überall 0 eingegeben wird
if nr_letters + nr_symbols + nr_numbers == 0:
    print("Password can't be empty. Please try again.")
    exit()

# Passwort-Liste zusammenstellen
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Zeichen mischen
random.shuffle(password_list)

# Liste zu String
password = "".join(password_list)

print(f"\n✅ Your generated password is: {password}")
