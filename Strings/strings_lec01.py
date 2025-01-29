# """"""
# ''''''
# """"
chai = "lemon chai"
print(chai)
chai2 = "masala chai"
print(chai2)
first_char=chai[2] 
print(first_char)
slice_chai2 = chai2[0:6]
print(slice_chai2)

slice_chai = chai[0:6]
print(slice_chai)

num_list = "0123456789"
num_list[:]
print(num_list)
num_list2 = "0123456789"
num_list2[:7]
print(num_list2)
num_list3 = "0123456789"
num_list3[3:]
print(num_list3)
num_list4 = "0123456789"
num_list4[0:7:2]
print(num_list4)


user = "Masala Chai"
print(user.lower())

chai = "      Maslala Chai           "
print(chai.strip())
chai1 = "Lemon Chai"
print(chai1.replace("Lemon","Ginger"))
chai2 ="Lemon , Ginger , Masala ,Mint"
print(chai2.split(" , "))
chai3 = "Masala Chai"
print(chai3.find("Chai"))
chai4 = "Masala Chai Chai Chai"
print(chai4.count("Chai"))
Chai_type = "Masala"
quantity = 2
order  = "I Ordered {} cups of {} chai"
print(order.format(quantity , Chai_type))

chai_variety = ["lemon","masala","ginger"]
print(chai_variety)
print(" , ".join(chai_variety))

chai = "Masala chai"
print(len(chai))
# for i in chai:
#     print(i)
chai="He said, \"Masala chai is awsome\" "
print(chai)
chai = "Masala\nChai"
print(chai)
chai = r"Masala\nChai"
print(chai)
chai = r"c:\user\pwd" 
print(chai)
