#  Higher Lower Game Demo
# https://replit.com/@appbrewery/higher-lower-final?embed=1&output=1#main.py

from random import randint
from game_data import data
from art import logo, vs

score = 0
profile_A = data[randint(0, len(data) - 1)]
profile_B = data[randint(0, len(data) - 1)]


def compare_followers(profile_A, profile_B):
    if profile_A['follower_count'] > profile_B['follower_count']:
        return 'A'
    else:
        return 'B'


continue_game = True
while continue_game:
    print(logo)

    print(
        f"Compare A: {profile_A['name']}, a {profile_A['description']}, from {profile_A['country']}.")
    print(vs)
    print(
        f"Against B: {profile_B['name']}, a {profile_B['description']}, from {profile_B['country']}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_choice == compare_followers(profile_A, profile_B):
        score += 1
        profile_A = profile_B
        profile_B = data[randint(0, len(data) - 1)]
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}.")
