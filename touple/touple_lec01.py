tea_types = ("Black","Green","Oolong")
print(tea_types)
print(tea_types[0])
print(tea_types[1])
print(tea_types[-1])


#this will show error becz touple is immutable
# tea_types[0]="Lemon"
# print(tea_types)

print(len(tea_types))
#touple is immutable but we can add more values into the touple

more_tea = ("Herbal","Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have a green tea")
#count the tea values in touple
print(more_tea.count("Herbal"))
print(more_tea.count("Herb"))

#touple unwrapped

# ('Black','Green','Oolong')=tea_types 
# print(tea_types )

print(type(tea_types))