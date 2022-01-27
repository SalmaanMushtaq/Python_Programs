# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters you want in your password\n"))
no_numbers = int(input("How many numbers you want in your password\n"))
no_symbols = int(input("How many symbols you want in your password\n"))

# Below code generates the password in a sequence manner like leeters + numbers+ symbol
#password = ""

# for char in range(1, no_letters + 1):
#     password += random.choice(letters)
# #print(password)
# for char in range(1, no_numbers+1):
#     password += random.choice(numbers)
# #print(password
#
# for char in range(1, no_symbols +1):
#      password += random.choice(symbols)
# print(password)
password_list = []
for char in range(1, no_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, no_numbers + 1):
    password_list.append(random.choice(numbers))
for char in range(no_symbols + 1):
    password_list.append(random.choice(symbols))

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is : {password}")