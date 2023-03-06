#read marks fot five subjects
math = int(input("Enter marks for math:"))
english = int(input("Enter marks for English:"))
physics = int(input("Enter marks for Physics:"))
chemistry = int(input("Enter marks for Chemistry:"))
history = int(input("Enter marks for History:"))

#sum of the subjects
Sum = (math + english + physics + chemistry + history)

#finding the average
avg = Sum / 5

#printing the sum and average 
print("You have an total of",Sum, "and an average of",avg,)

#find if the user has passed or failed
if avg >20 :
    print("You have succesfully passed the test ;)")
else :
    print("You have not passed the test :()")

