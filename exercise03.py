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

for x in lst:
	print(x)

def bagiTiga(parameter):
	for b in range(parameter):
		if b == 0:
			continue
		if b % 3 == 0:
			print(b)

bagiTiga(15)

# bisa pake return
#	if parameter == "" or parameter == "0"
#		return