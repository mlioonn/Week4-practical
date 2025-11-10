"""
def sum_digit(number):
    numSum = 0
    numList = str(number)
    for char in numList:
        numSum += int(char)
    return numSum

print(sum_digit(1234))
"""
"""
def pairwise_digits(number_a, number_b):
    listA = str(number_a)
    listB = str(number_b)
    diff = 0
    if len(listA) > len(listB):
        diff = len(listA) - len(listB)
    elif len(listB) > len(listA):
        diff = len(listB) - len(listA)
    finalList = []
    for x, y in zip(listA, listB):
        if x == y:
            finalList.append("1")
        else:
            finalList.append("0")
    #if len(listA) > le
    return "".join(finalList) + diff * "0"

print(pairwise_digits(1213, 121))
"""

"""
def to_base10(binary):
    number = 0
    binary = str(binary)
    for char in range(len(binary)): 
        number += int(binary[char]) * pow(2, len(binary) - 1 - char )
    return number
print(to_base10(11111111))
"""

"""
def triangle():
    output = ''
    add1 = True
    
    number = int(input("Enter a number"))
    for char in range(number):
        if char % 2 == 0:
            add1 = True
        else:
            add1 = False
        for i in range(char + 1):
            if add1: 
                output += "1"
            else:
                output += "0"
            add1 = not add1
        output += '\n'
    print(output)
        
triangle()
"""
"""
def sum_lists(list_2D):
    output =[]
    total = 0

    for row in list_2D:
        for val in row:
            total += val
        output.append(total)
        total = 0

    return output
print(sum_lists([[1,2,3], [2], [1, 2, 3, 4]]))
"""