rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ans = int(input("Choose rock , paper or scissors (0,1,2)"))
random = random.randint(0,2)
list = [rock, paper, scissors]
if ans < 0 or ans >= 3:
  print("Invalid Output")
else:
  print("You chose:")
  print(list[ans])
  print("Computer chose:")
  print(list[random])
  if ans == 0 and random == 2:
    print("You win")
  elif ans == 1 and random == 0:
    print("You win")
  elif ans == 2 and random == 1:
    print("You win")
  else:
    print("You lose")
