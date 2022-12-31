from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(logo)

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    print(num1)
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

# My Solution
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# should_continue = True
# running_total = 0
# previous_number = 0

# first_number = int(input("What's the first number?: "))
# running_total += first_number
# previous_number = first_number

# for symbol in operations:
#     print(symbol)

# while should_continue:
#     operation_symbol = input("Pick an operation from the line above: ")
#     next_number = int(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     previous_number = running_total
#     running_total = calculation_function(running_total, next_number)

#     print(f"{previous_number} {operation_symbol} {next_number} = {running_total}")
#     result = input(
#         f"Types 'y' to continue calculating with {running_total}, or type 'n' to exit.: ")
#     if result == "n":
#         print("Goodbye")
