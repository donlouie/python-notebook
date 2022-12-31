from art import logo
# HINT: You can call clear() to clear the output in the console.

print(logo)

bid_log = []


def add_new_bid(name, bid):
    new_bid = {}
    new_bid["name"] = name
    new_bid["bid"] = int(bid)
    bid_log.append(new_bid)


should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    add_new_bid(name, bid)
    result = input("Are there any other bidders? Type 'yes' or 'no': ")
    if result == "no":
        should_continue = False
        max_key = max(bid_log, key=lambda x: x["bid"])
        print("The winner is: " + max_key["name"] +
              "with a bid of: $" + str(max_key["bid"]))
