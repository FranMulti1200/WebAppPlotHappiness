"""
    Program that merges two lists into one and removes any common items between them.
"""


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

list1.extend(list2)
print(f"Lista Merge: {list1}")

def removeDuplicate(numbers):
    for number in numbers:
        #double = 0
        if (numbers.count(number) > 1):
            double = number
            index = numbers.index(number)
            numbers.pop(index)
            if (number == double):
                index = numbers.index(number)
                numbers.pop(index)
    return numbers

listClean = removeDuplicate(list1)
print(listClean)