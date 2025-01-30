#grade Calculator

#assign a letter grade based on student progrses  
#90-100 a grade
#80-89 b grde
#70-79 c grade 
#60-69 f grade

score = 90
if(score>=101):
    print("Please Verify grade again")
    exit()
if( score >=90):
    grade = "A"
elif(score>=80):
    grade = "B"
elif(score>=70):
    grade = "C"
elif(score>=60):
    grade = "D"
else:
    grade = "F"
print(grade)