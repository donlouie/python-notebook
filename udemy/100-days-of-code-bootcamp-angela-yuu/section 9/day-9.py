# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                           "Loop": "The action of doing something over and over again."}

# print(programming_dictionary["Bug"])

# Add a new key-value pair to the dictionary
# programming_dictionary["Variable"] = "A name that you can use to store a value."
# print(programming_dictionary)

# programming_dictionary = {}
# print(programming_dictionary)

# programming_dictionary["Bug"] = "Modified"
# print(programming_dictionary)

# for key, value in programming_dictionary.items():
#     print(key, value)

# * Nesting
from multiprocessing.sharedctypes import Value


capitals = {
    "Alabama": "Montgomery",
    "Germany": "Berlin",
}

# * Nesting a list in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lyon", "Marseille"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Frankfurt"], "total_visits": 8},
}

# * Nesting dictionary in a list
travel_log = {
    {
        "country": "France",
        "cities_visited": ["Paris", "Lyon", "Marseille"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Frankfurt"],
        "total_visits": 8
    },
}
