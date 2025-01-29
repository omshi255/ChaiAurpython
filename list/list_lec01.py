tea_varieties = ["Black","Green","Oolong","White"]
print(tea_varieties)
print(tea_varieties[0])
print(tea_varieties[1])
print(tea_varieties[-1])
print(tea_varieties[:2])
print(tea_varieties[0:2])
print(tea_varieties[2:])
tea_varieties[3]="Herbal"
print(tea_varieties)
tea_varieties[1:3] = ["lemon"]
print(tea_varieties)
print(tea_varieties[1:3])
tea_varieties[1:3]=["green","Masala"]
print(tea_varieties)
print(tea_varieties[1:1])
tea_varieties[1:1]=["test","test"]
print(tea_varieties)
tea_varieties[1:3]=[]
print(tea_varieties)
tea_varieties = ["Black","Green","Oolong","White"]

for tea in tea_varieties:
    print(tea,end=" ")
for tea in tea_varieties:
    print(tea)
for tea in tea_varieties:
    print(tea,end="-\n")
if "Oolong" in tea_varieties:
    print(" YES ,i have Oolong Tea")
#append method
tea_varieties.append("herbal")
print(tea_varieties)
if "blue" in tea_varieties:
    print(tea_varieties)
else:
    print("not having")
#pop method
print(tea_varieties.pop())
print(tea_varieties)
#remove value method
tea_varieties.remove("Green")
print(tea_varieties)
#insert value method
tea_varieties.insert(0,"green")
print(tea_varieties)
#copy mehtod
tea_varieties_copy = tea_varieties.copy()
print(tea_varieties_copy)

print(tea_varieties_copy.append("Lemon"))
print(tea_varieties_copy)
print(tea_varieties)

#squared numbers----------------list comprehension

squared_nums = [X**2 for X in range(11)]
print(squared_nums)
y = range(0,10)
print(y)

cube_num = [i**3 for i in range(10)]
print(cube_num)