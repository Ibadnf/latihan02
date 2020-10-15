astring="Hello World, my name is ibadnf"
alist=astring.split(" ")

print(astring.index("l"))
print(astring.count("l"))
print(astring[3:8:2]) # start:stop:step
print(astring[::-1]) # dibalikin dari belakang
print(astring.upper()) # case nya
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("bchjdsbvjs"))
print(astring.split(" "))
print(astring.split("--"))


myList=["ibad","Abdi","Dabi"]
print(len(myList)) # ngitung berapa di list


# condition
x = 2

if x == 2:
    print(x)

if "Hello" in alist:
    print("Yes I have")

x = [1,2,3]
y = [1,2,3]
print(x==y) # True karena nilainya sama
print(x is y) # False karena yang dibandingkan variabelnya
print(not False)
print((not False) == (False))


