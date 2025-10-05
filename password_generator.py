import random

letter = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '!', '$', '%', '^', '&', '*', ',', '.', '/']

print("welcome to pypassword generator")
in_letter = int (input(f"how many letters do you want?"))
in_numbers = int (input(f"how many numbers do you want?"))
in_symbols = int (input(f"how many symbols do you want?"))

password = []

for letters in range(0, in_letter):
    random_char = (random.choice(letter))
    password.append (random_char)

for number in range(0, in_numbers):
        random_number = (random.choice(numbers))
        password.append (random_number)

for symbol in range (0, in_symbols):
        random_symbol = (random.choice(symbols))
        password.append(random_symbol)


print((password))
random.shuffle(password)
print(password)

password_new = ""
for char in password:
  password_new += char

print(f"Your password is: {password_new}")


