# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    # TODO
    return "Yes" if boolean == True else "No"


print(bool_to_word(True))
print(bool_to_word(False))

# Other Solution
# Solution 1


def bool_to_word(bool):
    return "Yes" if bool else "No"
