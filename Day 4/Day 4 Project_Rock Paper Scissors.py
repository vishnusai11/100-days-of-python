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

#Write your code below this line 👇
import random
symbols=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer=random.randint(0,2)
if user<0 or user>2:
  print('You typed an invalid number, you lose!')
else:
  print(symbols[user])
  print('computer chose:')
  print(symbols[computer])
  if user==0:
    if computer==2:
      print('\n You win')
    elif computer==1:
      print('\n You lose')
    else:
      print('\n You draw')
  if user==1:
    print('Computer chose:')
    if computer==0:
      print('\n You win')
    elif computer==2:
      print('\n You lose')
    else:
      print('\n You draw')
  if user==2:
    print('Computer chose:')
    if computer==1:
      print('\n You win')
    elif computer==0:
      print('\n You lose')
    else:
      print('\n You draw')