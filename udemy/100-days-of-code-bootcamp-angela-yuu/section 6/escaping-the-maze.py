# Solution 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     while not wall_on_right():
#         turn_right()
#         move()
#     if wall_in_front() == False:
#         move()
#     elif wall_in_front() == True:
#         if right_is_clear() == True:
#             turn_right()
#             move()
#         elif wall_on_right() == True:
#             turn_left()
#             if front_is_clear() == True:
#                 move()
#             elif wall_on_right() == True:
#                 turn_left()
#                 move()

# Solution 2
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# Solution 2 Fixed
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
