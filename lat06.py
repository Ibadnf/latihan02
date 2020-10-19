def sapa(name):
	print(f"Hello, {name}")

sapa("Luke Skywalker")

def tanya(nama, hal):
	print(f"Hello, {nama}, anda sedang berada di halaman {hal}")

tanya("Luke","user admin")

def printNegative(index, length):
	if index == "" and length == "":
		return

	while index < length:
		if index %2 == 1:
			print(index)
		index += 1

printNegative(0,10)

def sum_two_numbers(a, b)
	return a + b

sum_two_numbers("2", "3")