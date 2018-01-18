
""" While loop game example"""
print ("Instructions. Enter either right or left in quotatoins at prompt. All lower case")
print ("")

n = input ("You are in the lost forest. Go left or go right? ")
while n == "right":
	n = input ("You are in the lost forest. Go left or go right? ")

print ("You got out of the lost forest!")

"""While loop prints 0,1,2,3,4"""
print ('')
print ('')

n = 0
while n < 5:
     print n
     n = n + 1
print ('')

n = 0
while n <= 5:
     print n
     n += 2
print ("Outside of loop")
print (n)
print ("END")
print ('')

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops += 1
print("Number of apples: " + str(numberOfApples))
print ("END")
print ('')

num = 10
while num > 3:
    num -= 1
    print(num) 
print ("END")
print ('')

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
print('')

"""For-loop version of above example"""
print ('')
print ('')

for n in range (7):
	print (n)
print ('')
print("END")

n = 2
while n <= 10:
     print n
     n += 2
print ("Goodbye")
print ("END")
print ('')

print ("Hello")
n = 10
while n >= 2:
     print n
     n -= 2
print("END")
print ('')





