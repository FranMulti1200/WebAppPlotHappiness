numbers = [3, 1, 2, 3, 4, 1, 5, 2]

for number in numbers:
    if (numbers.count(number) > 1):
        index = numbers.index(number)
        numbers.pop(index)

print(f"List without duplicates: {numbers}")