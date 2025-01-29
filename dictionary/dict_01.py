chai_types = {"Masala":"Spicy" , "Ginger":"Zesty" , "Green":"mild"}
print(chai_types)
#printing dict
print(chai_types["Masala"])
#printing particular chai_types
print(chai_types["Ginger"])
# print(chai_types["Gingeryy"])
chai_types["Green"] = "Fresh"
print(chai_types)
for chai in chai_types:
    print(chai,chai_types[chai])

#print through loop
for key,values in chai_types.items():
    print(key,":",values)
if "Masala" in chai_types:
    print("I have Masala Chai")
else:
    print("I do not have")
#finding length
print(len(chai_types))
#adding new key and values
chai_types["Earl Grey"] = "Citrus"
print(chai_types)

#pop chai_types
chai_types.pop("Ginger")
print(chai_types)

#pop items
chai_types.popitem()
print(chai_types)

#del keyword ---delete dict from the memory reference

del chai_types["Green"]
print(chai_types)

#copy key word

chai_types_copy = chai_types.copy()
print(chai_types_copy)

#nesting dictionary

tea_shop = {
    "chai":{"Masala" : "Spicy" , "Ginger" : "Zesty"},
    "Tea": {"Green":"Mild", "black" : "Strong"}
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])
print(tea_shop["Tea"])

#square method

squared_num = {x:x**2 for x in range(11)}
print(squared_num)

#clear method

squared_num.clear()
print(squared_num)

#convert list to dictonary

Keys = ["Masala","Ginger","Lemon"]
print(Keys)
default_value = "delecious"
new_dict = dict.fromkeys(Keys , default_value)
print(new_dict)

print(Keys)
default_value = "delecious"
new_dict = dict.fromkeys(Keys , Keys)
print(new_dict)

