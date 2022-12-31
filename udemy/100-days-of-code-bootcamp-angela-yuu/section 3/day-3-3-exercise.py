# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def identify_leap_year(year):
    if (year % 4 == 0) and (year % 400 == 0):
        print("leap")
    else:
        print("not leap")


identify_leap_year(2100)

# Other Solution
# Solution 1
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
