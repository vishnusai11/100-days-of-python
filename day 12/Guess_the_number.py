#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def easy(correct_answer):
  chance=10
  print("You have 10 attempts to guess the number.")
  chance_count=10
  for chance1 in range(1,chance+1):
    guess=int(input("Make a guess:"))
    if chance1<10:
      if guess==correct_answer:
        print(f"You got it! The answer was {guess}.")
        break
      elif guess>correct_answer:
        print("Too high.\nGuess again.\n")
        print(f"You have {chance_count-1} attempts remaining to guess the number.")
      elif guess<correct_answer:
        print("Too low.\nGuess again.\n")
        print(f"You have {chance_count-1} attempts remaining to guess the number.")
    chance_count=chance_count-1
    if chance1==10:
      if guess==correct_answer:
        print(f"You got it! The answer was {guess}.")
      elif guess>correct_answer:
        print("Too high.\n")
        print('Oops you have run out of chances')
      elif guess<correct_answer:
        print("Too low.\n")
        print('Oops you have run out of chances')
def hard(correct_answer):
    chance=5
    print("You have 5 attempts to guess the number.")
    chance_count=5
    for chance1 in range(1,chance+1):
      guess=int(input("Make a guess:"))
      if chance1<5:
        if guess==correct_answer:
          print(f"You got it! The answer was {guess}.")
          break
        elif guess>correct_answer:
          print("Too high.\nGuess again.\n")
          print(f"You have {chance_count-1} attempts remaining to guess the number.")
        elif guess<correct_answer:
          print("Too low.\nGuess again.\n")
          print(f"You have {chance_count-1} attempts remaining to guess the number.")
      chance_count=chance_count-1
      if chance1==5:
        if guess==correct_answer:
          print(f"You got it! The answer was {guess}.")
        elif guess>correct_answer:
          print("Too high.\n")
          print('Oops you have run out of chances')
      elif guess<correct_answer:
          print("Too low.\n")
          print('Oops you have run out of chances')
from art import logo
from random import *
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
correct_answer=randint(1,100)
print(correct_answer)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=='easy':
  easy(correct_answer)
if difficulty=='hard':
  hard(correct_answer)