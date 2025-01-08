numbers = [3, 1, 2, 3, 4, 1, 5, 2]
numbers_cp = numbers.copy()

for number_cp in numbers_cp:
    for number in numbers:
        if(number_cp == number and numbers.count(number) > 1):
            index = numbers.index(number)
            numbers.pop(index)


print(f"List without duplicates: {numbers}")