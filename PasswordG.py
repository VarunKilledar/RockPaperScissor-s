import random
targetL = int(input("The Number of letters you want: \n"))
targetN = int(input("The Number of Number you want:\n"))
targetS = int(input("The Number of Symbols youo want:\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_lsit = []

for char in range(1, targetL+1):
    password_lsit .append(random.choice(letters)) 
for char in range(1, targetN+1):
    password_lsit .append(random.choice(numbers))
for char in range(1,targetS+1):
    password_lsit .append(random.choice(symbols)) 
random.shuffle(password_lsit)
password = ""
for char in password_lsit:
    password += char

print(f"The random Genetrated password is :{password}")



