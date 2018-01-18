
varA = (input("enter something here "))
print ('')
varB = (input("enter something here "))
print ('')

if (type (varA)== str) or (type (varB)== str):
	print ("string involved")
else:
	if varA > varB:
		print ("bigger")
	elif varA == varB:
		print ("equal")
	elif varA < varB:
		print ("smaller")

