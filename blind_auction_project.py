import art
print(art.logo)
print("Welcome to the Silent Auction Program.")


def choose_winner(bidding_dict):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner += bidder
    print(f"The winner is: {winner}\n"
          f"With a bid of ${highest_bid}")


details = {}
bid = True
while bid:
    name = input("What's your name? ")
    price = int(input("How much would you like to bid? $"))
    details[name] = price

    new_bids = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if new_bids == "yes":
        print("\n" * 20)
    else:
        print("\n" * 10)
        bid = False
        choose_winner(details)

