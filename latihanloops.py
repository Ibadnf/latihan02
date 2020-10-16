# Loops for
primes = [2,3,5,7]
for prime in primes:
	print(prime)


# Prints out the numbers 0,1,2,3,4
for x in range(5):
	print(x)

for x in range(3,6):
	print(x)

# Loops while

# baris 0,1,2,3,4
count = 0
while count < 5:
	print(count)
	count += 1 	# This is the same as count = count + 1 ini tuh maksudnya loncatan step ya kalo nilainya 2 loncatnya 2 kali

# break
while True:
	print(count)
	count += 1
	if count >= 5:
		break	# Ini sama kaya count atas

# continue
for x in range(10):
	if x % 2 == 0:	# Pembagi (mod)
		continue
	print(x)

