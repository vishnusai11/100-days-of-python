from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bidding={}
choice=False
def find_biggest(bidding_record):
  winning_bid=0
  winning_name=""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > winning_bid: 
      winning_bid = bid_amount
      winning_name = bidder
  print(f"The winner is {winning_name} with a bid of ${winning_bid}")

while not choice :
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bidding[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    choice=True
    find_biggest(bidding)
  elif should_continue == "yes":
    clear()