names = []
count = 0

while count < 5: 
    newname = str(input("Please input a name: "))
    names.append(newname)
    count += 1

for name in names:
    print(f"{name} is awesome!")
