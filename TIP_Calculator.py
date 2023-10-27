
print("Welcome to the Tip Calculator")
# prints the message between ""
total = float(input("What was the total bill?  "))
# creates a variable float that receives input from the user  regarding the total of the bill
tip_YN = input("Would you like to leave a tip? Type Y or N :  ")
# create a variable that receives input from the user regarding 
if tip_YN == 'N' :    
# create an if statement that will do something if variable 'tip_YN' is equal to 'N' 
    people = int(input("How many people to spill the bill?  "))
# the variable people is an int and receives input from the user  
    total_w = total / people 
# create a var that will contain the result between 'total and people' 
    print(f"Each person should pay : {round(total_w,2)}")
#print the result rounding the number to two digits after the comma
else:
#the else means that the input from the user 'tip_YN ' is equal to 'N'   
    percent = int(input("What percentage would you like to give? 10 , 12 or 15 ?    "))
# create a var that receive the input from the user regarding the percent for the tip 
    people = int(input("How many people to spill the bill?  "))
#create a var that will ask the user for input regarding the number of people that will split the bill
    total_p = (total * percent) / 100
# create a var that will represent the result of the (percent from the total)
    total_f = (total + total_p) / people
# create a var that holds the final result from the total and people 
    print(f"Each person should pay: {round(total_f,2)}")
# print the result, rounding the float to two digits after the comma

