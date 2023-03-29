import random
from replit import clear
logo = logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(list):
  sum_1 = sum(list)
  if sum_1 == 21 and len(list) == 2:
    return 0 
  if sum_1 > 21 and 11 in list:
      list.remove(11)
      list.append(1)
  return sum_1

def compare(user_score , computer_score):
  if computer_score == user_score:
    return "It's a Draw"
  elif user_score == 0:
    return "You have a Blackjack. You win!"
  elif computer_score == 0:
    return "Computer has a Blackjack.You lose!"
  elif computer_score > 21:
    return "Opponent went over! You win!"
  elif user_score > 21 :
    return "You went over! You lose!"
  elif computer_score > user_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  print(logo)
  user_card = []
  computer_card = []
  for i in range(2):
    new_card = deal_card()
    user_card.append(new_card)
    new_card_1 = deal_card()
    computer_card.append(new_card_1)
  
  
  while True:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"Your cards: {user_card} and the score: {user_score}")
    print(f"Computers first card: {computer_card[0]}")
    if user_score == 0 or computer_score > 21:
      print("You win")
      break
    elif computer_score == 0 or user_score > 21:
      print("You loose")
      break
    else:
      answer = input("want to draw another card? (y/n)")
      if answer in 'Yy':
        new_card = deal_card()
        user_card.append(new_card)
      else:
        break
  while  computer_score < 17 and computer_score != 0 :
    new_card = deal_card()
    computer_card.append(new_card)
    computer_score = calculate_score(computer_card)
  print(f"Your final hand {user_card} and final score: {user_score}")
  print(f"Coputers final hand: {computer_card} and final score: {computer_score}")
  print(compare(user_score,computer_score))      
while input("Do you want to play a game of BlackJack? Type 'y' or 'n'") in 'Yy':
  clear()
  play_game()
