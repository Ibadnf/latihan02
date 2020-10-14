numbers=[]
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings=["Halo"+" "+"Dunia"]


names=["Kim Namjoon","Kim Seokjin","Min Yoongi","Jung Hoseok","Park Jimin","Kim Taehyung","Jeon Jungkook"]

# write
second_name=1

print(numbers)
print(strings)
print("The second name on the names list is %s" % names[second_name])

# print variabel pake for
for x in names:
    print(x)

# print the list without Sabi
nama=["Abdi","Ibad","Dalbi","Sabi","Somi","Mimi","Papi"]
for x in nama:
    if x !="Sabi":
        print(x)