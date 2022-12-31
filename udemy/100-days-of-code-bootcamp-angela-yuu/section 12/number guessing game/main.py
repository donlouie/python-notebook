from random import *

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")
# ---Hard = 5 attempts; Easy = 10 attempts
attempts = 10 if difficulty == "easy" else 5

print(f"You have {attempts} remaining to guess the number.")

# Generate a random number between 1 and 100
random_number = randint(1, 100)

while attempts > 0:
    # print(f"RANDOM NUM = {random_number}")
    # Get a guess from user
    guess = int(input("Make a guess: "))
    hint = "Too high." if guess > random_number else "Too low."

    if guess == random_number:
        print("You guessed the number!")
        break
    else:
        attempts -= 1
        print(f"{hint}. \nGuess again.")
        if attempts == 0:
            print("You ran out of attempts. The number was", random_number)
            break
        else:
            print(
                f"You have {attempts} attempts remaining to guess the number.")
