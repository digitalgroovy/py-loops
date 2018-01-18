"""This while loop will add all numbers in a range starting from zero to the number you specify at input"""

end = int(input("Enter an integer range here>>> "))
totalOfCollection  = 0
incrementCounter = 1
while incrementCounter <= end:
        totalOfCollection = totalOfCollection + incrementCounter
        incrementCounter = incrementCounter + 1

print totalOfCollection

