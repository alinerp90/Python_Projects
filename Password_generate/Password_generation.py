#Password Generator Project
import random

# list with database of the caracters of the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# input from the user regarding how many items the password needs:
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
pw_letters = " "
nr_symbols = int(input(f"How many symbols would you like?\n"))
pw_symbols = " "
nr_numbers = int(input(f"How many numbers would you like?\n"))
pw_numbers = " "


# selection of random items from the user input
if nr_letters > 0:
    pw_letters = random.choices(letters, k=nr_letters)


if nr_symbols > 0:
    pw_symbols = random.choices(symbols, k=nr_symbols)


if nr_numbers > 0:
    pw_numbers = random.choices(numbers, k=nr_numbers)

# final password in list format
password = pw_letters + pw_symbols + pw_numbers
print(password)


password_str = ""
# loop to convert the password from list to string
for item in range(len(password)):
    password_str += password[item]

# print the password selected in order: Letters, symbols and numbers.
print(password_str)

# randomization of the previous password
random.shuffle(password)
password_random = ""

# loop to convert the password from list to string
for item in range(len(password)):
    password_random += password[item]
# print password in random order:
print(password_random)
