from Car import Car
cars = {}
id = 0
while True:
	print("Enter 1 to Add a Car")
	print("Enter 2 to Delete a Car")
	print("Enter 3 to Rent a Car")
	print("Enter 4 to Restore a Car")
	
	s = input()
	if (s == 1):
		print("Enter car type")
		t = raw_input()
		print("Enter car model")
		m = raw_input()
		print("Enter car year")
		y = input()
		cars[id] = Car(id,t,m,y)
		id += 1
		
	elif (s == 2):
		print("Enter car ID")
		i = input()
		del cars[i]
		
	elif (s == 3):
		print("Enter car ID")
		i = input()
		if (cars[i].rented()):
			print("This Car is already rented")
		else:
			cars[i].rent()
			print("The car is rented successfully")
			
	elif (s == 4):
		print("Enter car ID")
		i = input()
		if (cars[i].rented()):
			cars[i].restore()
			print("The Car is restored successfully")
		else:
			print("The car is already restored")
		
