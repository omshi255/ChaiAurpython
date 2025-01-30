#ques 1: Age Group Catagorization
#classisfy a persons age gorup child <13 and 13-19 teenager 20-59 adult 60+ senior citizen


userscore = int(input("Give me a score value: \n"))
if(userscore <13):
    print("this is child group")
elif(userscore <20):
# elif(userscore >13 and userscore <=19):
    print("this is an teenager group")
elif(userscore <60):
# elif(userscore >20 and userscore<=59):
    print("this is a adult group")
else:
    print("type a valid output")
