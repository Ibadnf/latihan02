def bilangan(angka):
	for x in range(angka):
		print(x)

bilangan(11)

def kenalan(nama, umur, posisi):
	print(f"Halo, nama saya {nama}, umur saya {umur}, saya memegang role {posisi}")

kenalan("ibad", "22", "graphic designer")

def sum_two_numbers(a, b):
	return a + b

a = sum_two_numbers("2", "3")
print(a)

# LATIHAN CLASS
class Siswa(object):
	name = "Luke Skywalker"
	umur = 14

	def alamat(self, almt):
		return almt

objectSiswa = Siswa()

print(objectSiswa.name)
print(objectSiswa.umur)
print(objectSiswa.alamat("Komplek Beruang"))