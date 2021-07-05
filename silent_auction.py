from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

silent_auction = {}
end_of_auction = False

while not end_of_auction:
  print("Welcome to the silent_auction.")
  name = input("What is your name?\n")
  bid = input("How much would you like to bid?\n$")
  silent_auction[name] = int(bid)
  more_bids = input("Does anyone else want to bid? Type 'yes' or 'no'.\n")

  if more_bids == "yes":
    clear()
  elif more_bids == "no":
    end_of_auction = True
    silent_auction.values()
    highest_bid = max(silent_auction.values())
    highest_bidder = max(silent_auction, key=silent_auction.get)
    print(f"{highest_bidder} won the auction with a bid of ${highest_bid}")
