class Car:
	def __init__(self, id, type, model, year):
		self.Id = id
		self.Type = type
		self.Model = model
		self.Year = year
		self.Rented = False
		
	def rent(self):
		self.Rented = True
		
	def rented(self):
		return self.Rented
	
	def restore(self):
		self.Rented = False
