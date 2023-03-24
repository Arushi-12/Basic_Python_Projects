import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator")
l = int(input("Enter the number of letters to be used: "))
n = int(input("Enter the number of numbers to be used: "))
s = int(input("Enter the number of symbols to be used: "))
for i in range(l):
  password += random.choice(letters)
for j in range(n):
  password += random.choice(numbers)
for k in range(s):
  password += random.choice(symbols)
random.shuffle(password)
str1 = ''
for i in password :
  str1 += i
print(f"The password generated is: {str1}")
