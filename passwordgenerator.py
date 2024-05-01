#This is a random password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input Questions
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Letters, Special characters, Numbers
password_easy = ""
for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password_easy += random_char
    
for spl in range(1,nr_symbols + 1):
    random_sym = random.choice(symbols)
    password_easy += random_sym

for int in range(1,nr_numbers + 1):
    random_int = random.choice(numbers)
    password_easy += random_int
print(f"Generated password (Easy Level): {password_easy}")

#Shuffle method
password_list = []
for char in range(1,nr_letters + 1):
    password_list.append(random.choice(letters)) 

for spl in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)
    
for int in range(1,nr_numbers + 1):
    password_list += random.choice(numbers)

#Shuffling my list
random.shuffle(password_list)

#Creating a string and printing the password
password = ""
for letter in password_list:
    password += letter
print(f"Generated password (Hard Level): {password}")
