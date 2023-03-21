n = input("Enter a string: ")
names = n.split(", ")
random = random.randint(0,len(n)-1)
print(f"{names[random]} will pay the bill")
