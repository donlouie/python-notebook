# https://replit.com/@appbrewery/blackjack-final
# file:///C:/Users/User/Downloads/Blackjack_Flowchart.pdf

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards, computer_cards = [], []
user_score, computer_score = 0, 0

game_start = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if game_start == 'y':
    def deal_card():
        return random.choice(cards)

    while len(user_cards) < 2:
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(list):
        sum = 0
        for card in list:
            sum += card
        return sum

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(
        f"Computer's first card: {computer_cards[0]}")

    if user_score == 21:
        print("Blackjack! You win!")
        should_continue = False
    elif computer_score == 21:
        print("Blackjack! Computer wins!")
        should_continue = False
    else:
        should_continue = True
        while should_continue:
            user_action = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_action == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)

                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)

                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")

                if should_continue == False:
                    print(
                        f"Your final hand: {user_cards}, final score: {user_score}")
                    print(
                        f"Computer's final hand: {computer_cards}, final score: {computer_score}")

                if user_score > 21:
                    print("You bust! Computer wins!")
                    should_continue = False
                elif computer_score > 21:
                    print("Computer busts! You win!")
                    should_continue = False
                elif user_score > computer_score:
                    print("You win!")
                    should_continue = False
                elif user_score < computer_score:
                    print("Computer wins!")
                    should_continue = False

            elif user_action == 'n':
                should_continue = False

                user_score = calculate_score(user_cards)
                computer_score = calculate_score(computer_cards)

                if computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)

                print(
                    f"Your final hand: {user_cards}, final score: {user_score}")
                print(
                    f"Computer's final hand: {computer_cards}, final score: {computer_score}")

                if computer_score > 21:
                    print("Computer busted! You win!")
                elif user_score > computer_score:
                    print("You win!")
                elif user_score < computer_score:
                    print("Computer wins!")
                else:
                    print("It's a tie!")
