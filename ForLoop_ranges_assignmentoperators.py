"""Using addAND assignment operator in for loop"""
mysum = 0
for i in range (7,10):
	mysum += i
	print (mysum)
print ("END")
print ('')


mysum = 0
for i in range (7,10,2):
	mysum += i
	print (mysum)
print("END")
print('')

"""subtractAND operator in for loop with range"""
mysum = 100
for i in range (15,20):
	mysum -= i
	print (mysum)
print("END")
print ('')

""" modulus assignment operator"""
mysum = 24
for i in range (4,7):
	mysum %= i
	print (mysum)
print("END")
print ('')

""" multiplyAND assignment operator"""
mysum = 10
for i in range (4,7):
	mysum *= i
	print (mysum)
print("END")
print ('')


end = 6
n = 0
while n < end:
    n += 1
    print n
print ("END")
print ('')