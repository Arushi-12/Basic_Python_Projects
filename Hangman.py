import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
counter = 6
word_list = ["aardvark", "baboon", "camel",'abruptly','absurd','buffoon','crypt','embezzle','equip','espionage','euouae']
chosen_word = random.choice(word_list)
l = []
for i in range(len(chosen_word)):
  l.append("_ ")
print(l)
while True:
  f = False
  guess = input("Enter a letter: ").lower()
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      l[i] = guess
      f = True
  print(l)
  if f == False:
    counter -= 1
  if '_ ' not in l:
    print("you win")
    break
  print(stages[counter])
  if counter == 0:
    print("You lost")
    break
