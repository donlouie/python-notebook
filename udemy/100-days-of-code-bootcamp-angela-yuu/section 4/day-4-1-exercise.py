import random

def coin_toss():
    n = random.randint(0, 1)
    if(n == 1):
        print("Heads")
    else:
        print("Tails")


coin_toss()
