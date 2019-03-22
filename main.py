from Car import Car
cars = []
id = 0
while True:
	print("Enter 1 to Add a Car")
	
	s = input()
	if (s == 1):
		print("Enter car type")
		t = raw_input()
		print("Enter car model")
		m = raw_input()
		print("Enter car year")
		y = input()
		cars.append(Car(++id,t,m,y))
