# 🚨 Don't change the code below 👇
from html.entities import name2codepoint


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def love_calculator(name1, name2):
    combined_name = name1 + name2
    true_score = str(
        sum(map(combined_name.lower().count, ['t', 'r', 'u', 'e'])))
    love_score = str(
        sum(map(combined_name.lower().count, ['l', 'o', 'v', 'e'])))
    print(true_score + love_score)


love_calculator("Angela Yu", "Jack Bauer")
love_calculator("Kanye West", "Kim Kardashian")
love_calculator("Brad Pitt", "Jennifer Aniston")

# Other Solution
# Solution #1
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = str(true) + str(love)

print(love_score)
