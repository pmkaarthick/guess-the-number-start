import random
from art import logo
print(logo)
print("Welcome to Number Guessing Game")
level=input("Enter the difficulty level")
if(level == "easy"):
  chances = 10
else:
  chances = 5

actual = random.randint(1,101)
gameover = False
while not gameover:
  guess = int(input("Enter any number between 1 to 100"))
  if(chances>0):
    if(guess == actual):
      print("You Won")
      gameover=True
    elif guess>actual:
      print("Too High")
      chances-=1
    else:
      print("Too Low")
      chances-=1
  else:
    print("Game Over")
    gameover=True