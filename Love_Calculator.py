print("Welcome to Love Calculator")
name1 = input("Enter the 1st name: ")
name2 = input("Enter the 2nd name: ")
name = name1.lower() + name2.lower()
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t+r+u+e
love = l+o+v+e
true = str(true)
love = str(love)
score = true + love
if int(score) <10 or int(score) >90:
  print(f"Your score is : {score}, You go together like coke and mentos")
elif int(score) > 40 and int(score) < 50:
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score is: {score}")
