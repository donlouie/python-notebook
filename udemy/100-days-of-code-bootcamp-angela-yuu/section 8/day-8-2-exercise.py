# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

# My solution
# def prime_checker(number):
#     if number > 1:
#         for i in range(2, number):
#             if(number % i) == 0:
#                 print(number, "It's not a prime number.")
#                 break
#         else:
#             print(number, "It's a prime number")
#     else:
#         print(number, "It's a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
