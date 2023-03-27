from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid = {}
while True:
  name = input("Enter your name: ")
  bid_amount = int(input("Enter the bid amount: $"))
  bid[name] = bid_amount
  answer = input("Are there any more bidders? Type 'y' for yes and 'n' for no").lower()
  if answer == 'y':
    clear()
  elif answer == 'n':
    max_bid = 0
    for i in bid:
      if bid[i] > max_bid :
        max_bid = bid[i]
        max_name = i
    print (f"The highest bidder is {max_name} and the amount is ${max_bid}")
    break
