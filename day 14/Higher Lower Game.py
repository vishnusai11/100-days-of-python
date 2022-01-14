from art import logo
from art import vs
from game_data import data
from replit import clear
import random
#defining the functions
def generateA(data):
  selection=random.randint(0,49)
  selection_list=[]
  selection_list.append(data[selection]["name"])
  selection_list.append(data[selection]["follower_count"])
  selection_list.append(data[selection]["description"])
  selection_list.append(data[selection]["country"])
  return selection_list
def generateB(data):
  selection=random.randint(0,49)
  selection_list=[]
  selection_list.append(data[selection]["name"])
  selection_list.append(data[selection]["follower_count"])
  selection_list.append(data[selection]["description"])
  selection_list.append(data[selection]["country"])
  return selection_list
def printable(list1):
  name=list1[0]
  followers_count=list1[1]
  description=list1[2]
  country=list1[3]
  print(f"{name}, a {description}, from {country}.")
def compare(A,B,player_guess):
  follower_countA=A[1]
  follower_countB=B[1]
  #True_value=True
  #False_value=False
  cond=False
  winner=''
  maximum=max(follower_countA,follower_countB)
  if maximum==follower_countA:
    winner='A'
  elif maximum==follower_countB:
    winner='B'
  if player_guess==winner:
    cond=True
  else:
    cond=False
  return cond
#actual starting of the program xD
print(logo)
score=0
A=generateA(data)
printable(A)
print(vs)
B=generateB(data)
printable(B)
player_guess=(input('Guess who has the highest number of followers(A/B)'))
comp=compare(A,B,player_guess)
while comp:
  clear()
  score+=1
  print(logo)
  print(f"You're right! Current score: {score}")
  A=B
  printable(A)
  print(vs)
  B=generateB(data)
  printable(B)
  player_guess=(input('Guess who has the highest number of followers(A/B)'))
  comp=compare(A,B,player_guess)

if comp==False:
  print(f"Sorry, that's wrong. Final score: {score}")