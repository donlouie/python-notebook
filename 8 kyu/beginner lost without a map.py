# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]


def maps(a):
    double_a = []
    for number in a:
        x = number * 2
        double_a.append(x)
    return double_a


print(maps([1, 2, 3]))

# Other Solution
# Solution 1


def maps(a):
    return [2 * x for x in a]
