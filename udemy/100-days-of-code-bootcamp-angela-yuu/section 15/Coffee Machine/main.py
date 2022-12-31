from data import MENU, resources
# Contains - MENU, resources

# Track profit
profit = 0


def display_report():
    # Display report and profit
    for item in resources:
        print(item, resources[item])
    print("Profit:", profit)


def resources_available(order_ingredients):
    # Check if resources are available
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            return False
    return True


def make_coffee(order_ingredients):
    # Deduct ingredients from resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


def get_sum(quarters, dimes, nickles, pennies):
    # Get sum of payment
    sum = (quarters * .25) + (dimes * .1) + \
        (nickles * .05) + (pennies * .01)
    return sum


def calculate_change(order_cost, total_payment):
    # Calculate change
    change = round(total_payment - order_cost, 2)
    return change


menu = 0
while menu < 3:
    print("1. Order\n2. Report\n3. Exit")
    menu = int(input("What would you like to do? "))
    if menu == 1:
      # Get order
        type_of_coffee = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        order_ingredients = MENU[type_of_coffee]["ingredients"]
        order_cost = MENU[type_of_coffee]["cost"]
        if resources_available(order_ingredients):

            # Get coins
            print("Please insert coins...")
            # Get payment
            quarters = int(input("How many quarters?:  "))
            dimes = int(input("How many dimes?:  "))
            nickles = int(input("How many nickles?:  "))
            pennies = int(input("How many pennies?:  "))
            # Get total payment
            total_payment = get_sum(quarters, dimes, nickles, pennies)

            if total_payment >= order_cost:
                # Add order cost to profit
                profit += order_cost
                # Calculate change
                change = calculate_change(order_cost, total_payment)
                print(f"Here is your change: ${change}")
                make_coffee(order_ingredients)
                print(f"Here is your {type_of_coffee} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Sorry there is not enough ingredients. Please try again later.")
            continue_order = False
    if menu == 2:
        display_report()
    if menu >= 3:
        print("Exiting...")
        break
