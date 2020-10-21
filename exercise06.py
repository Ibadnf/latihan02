class Car:
	title = "Honda"
	kind = "Matic"
	color = "Black"

	def setTitle(self, title):
		print(title)

	def setColor(self, color):
		print(color)

theCar = Car()
theCar.setColor("White")


class ComplexNumber(object):

	glbl = "Hello"

	# class constructor
	def __init__(self, r=0, i=0):
		self.real = r
		self.img = i

	def get_data(self):
		print(f"{self.real} + {self.img}")		# jadi string
		print(self.real + self.img)				# jadi int

num = ComplexNumber(2, 3)
num.get_data()

		