from Day9_art import logo

def new_bid():
    name = input("What is your name?:")
    bid =  input("What's your bid?: £")
    bids[name] = bid
    if input("Add bid?(y/n)") == "y":
        # clear()
        new_bid()

start_message = "Welcome to the secret auction program!"
print(logo)
print(start_message)
bids = {}
new_bid()
winning_bid = max(bids.values())
winning_name = [key for key, value in bids.items() if value == winning_bid]
print(f"The winner is {winning_name[0]} with a bid of £{winning_bid}.")