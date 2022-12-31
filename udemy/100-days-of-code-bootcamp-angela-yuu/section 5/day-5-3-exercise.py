total_even_number = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_even_number += number

print(total_even_number)

# Other solution
total = 0
for number in range(2, 101, 2):
    total += number
print(total)
