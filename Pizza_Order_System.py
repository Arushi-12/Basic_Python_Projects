print("Welcome to python pizza deliveries")
size = input("What size pizza do you want? S M or L")
add_peperoni = input("Want to add peperoni? Y or N")
add_cheese = input("Want extra cheese? Y or N")
bill = 0
if size == 'S':
  print("Small pizza is for $20")
  bill = 20
  if add_peperoni == 'Y':
    bill += 2
elif size == 'M':
  print("Medium pizza is for $25")
  bill = 25
  if add_peperoni == 'Y':
    bill += 3
elif size == 'L':
  print("Large pizza is for $30")
  bill = 30
  if add_peperoni == 'Y':
    bill += 3
else:
  print("Wrong choice")
if add_cheese == 'Y':
  bill += 1
print(f"Your final bill is: ${bill}")
