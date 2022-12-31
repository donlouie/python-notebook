# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def pizza_order():
    bill = 0

    size = input("What size pizza do you want? S, M, or L ")
    if (size.upper() == "S"):
        bill = 12
    elif (size.upper() == "M"):
        bill = 20
    elif (size.upper() == "L"):
        bill = 25

    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni.upper() == 'Y':
        bill += 2

    extra_cheese = input("Do you want extra cheese? Y or N ")
    if extra_cheese.upper() == 'Y':
        bill += 1

    print(f"Your final bill is: ${bill}")


pizza_order()
