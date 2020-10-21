"""
class MyClass(object):
	variable = "blah"

	def function(self):
		print("This is message inside the class")

myObjectx = MyClass()
print(myObjectx.variable)
"""

"""
class MyClass(object):
	variable = "blah"

	def function(self):
		print("This is message inside the class")

myObjectx = MyClass()
myObjecty = MyClass()

myObjecty.variable = "Hello"

print(myObjectx.variable)
print(myObjecty.variable)
"""
"""
class MyClass(object):
	variable = "blah"

	def function(self):
		print("This is message inside the class")

myObjectx = MyClass()
myObjectx.function()
"""

class Vehicle(object):

	classified = "car"
	
	def __init__(self, name, color, value):
		self.name = name
		self.color = color
		self.value = value

car1 = Vehicle("kijang", "red", "16,000,000")
car2 = Vehicle("Lamborghini", "yellow", "200,000,000")

print(f"kijang is a {car1.__class__.classified} ")
print(f"Lamborghini is also a {car2.__class__.classified} ")

print(f"{car1.name} is a car which has {car1.color} color and worth {car1.value}")
print(f"{car2.name} is also a car which has {car2.color} color and worth {car2.value}")


class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def swimming_test(bird):
    bird.swim()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
swimming_test(blu)
swimming_test(peggy)


class KaryawanSatu:
	"""docstring for GajiKaryawan"""
	def __init__(self):
		print("Karyawan pertama namanya Ibad")

	def gaji(self):
		print("Gajinya 24 Juta")

class KaryawanDua(KaryawanSatu):
	"""docstring for GajiDua"""
	def __init__(self):
		super().__init__()
		print("Karyawan kedua namanya Naning")

	def gaji(self):
		print("Gajinya 5 Juta")

naning = KaryawanDua()
ibad = KaryawanSatu()
ibad.gaji()
naning.gaji()


class Employee:

	empCount = 0

	"""docstring for EmployeeSalary"""
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayEmployee(self):
		print("Name : ", self.name,  ", Salary: ", self.salary)

	def totalEmployee(self):
		print("Total employee %d" % Employee.empCount)


emp1 = Employee("Ibaddilah", "24.000.000")
emp2 = Employee("Luke Skywalker", "15.000.000")
emp3 = Employee("Anna padma", "10.000.000")
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print("Total employee %d" % Employee.empCount)
print(emp1.salary + emp2.salary + emp3.salary)