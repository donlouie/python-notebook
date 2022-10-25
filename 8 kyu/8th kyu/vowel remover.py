def shortcut(s):
    # ...
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for letter in s:
        if letter not in vowels:
            result.append(letter)
    return "".join(result)


shortcut("hello")
# hll

# Other Solution
# Solution #1


def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')

# Solution #2


def shortcut(s):
    return s.translate(None, 'aeiou')

# Solution #3


def shortcut(s):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s
