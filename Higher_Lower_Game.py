logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    }]

import random
print(logo)
score = 0
def choose():
  return random.choice(data)

def compare(a,b,c):
  if a>b and c == 'A':
    return 1
  elif b>a and c == 'B':
    return 1
  else:
    return 0

answer_1 = choose()
answer_2 = choose()
while True:
  print(f"Compare A: {answer_1['name']}, a {answer_1['description']}, from {answer_1['country']}")
  print(vs)
  print(f"Compare B: {answer_2['name']}, a {answer_2['description']}, from {answer_2['country']}")
  user_answer = input("Who has more followers? A or B").upper()
  answer = compare(answer_1['follower_count'],answer_2['follower_count'],user_answer)
  if answer == 1:
    score += 1
    print(f"That is the correct option! Your score is: {score}")
    answer_1 = answer_2 
    answer_2 = choose()
  else:
    print(f"Incorrect option! Your final score is: {score}")
    break
