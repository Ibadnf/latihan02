for x in range(1,11):		# Bisa dibikin simple lagi sebenernya gausah ada continue
	if x % 2 == 1:
		continue
	print(x)

for i in range(1,11):
	if i % 2 == 0:
		continue
	print(i)

lst = [1,5,6,10,2]
index = 0
while index < len(lst):
	print(lst[index])
	index += 1


def bagiTiga(parameter = None):
	if parameter == None or parameter <3:
		return
	for b in range(parameter):
		if b == 0:
			continue
		if b % 3 == 0:
			print(b)

bagiTiga(16)

# bisa pake return
#	if parameter == "" or parameter == "0"
#		return


def bagiEmpat(num = None):
	if num == None or num <3:
		return

	index = 1

	while index < num:
		if index == 0:
			continue
		if index % 4 == 0:
			print(index)
		index += 1

bagiEmpat(17)