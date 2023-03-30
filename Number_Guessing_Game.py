logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
import random
def guess(guesses,number):
  while guesses > 0:
    print(f"You have {guesses} guesses")
    guess_1 = int(input("Enter your guess: "))
    if guess_1 > number:
      print("Too High")
    elif guess_1 < number:
      print("Too Low")
    else:
      print("You have guessed the number!You win!")
      return
    guesses -= 1
    print("Guess again")
  print("You lose!")
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
number = random.randint(1,100)
type = input("Choose a  difficulty: Type 'e' for easy and 'h' for hard: ").lower()
if type == 'e':
  guesses = 10
  guess(guesses,number)
elif type == 'h':
  guesses = 5
  guess(guesses,number)
else:
  print("Wrong Choice")
