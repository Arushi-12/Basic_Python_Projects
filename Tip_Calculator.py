print("Welcome to Tip Calculator")
bill = float(input("Your total bill is? $"))
percent = int(input("What percentage tip? (10/12/15) "))
people = int(input("How many people to split the bil? "))
total = (bill + ((bill*percent) /100))/people
total = round(total,2)
print(f"Each person has to pay: ${total}")
