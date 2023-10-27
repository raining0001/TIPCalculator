
print("Welcome to the Tip Calculator")
total = float(input("What was the total bill?  "))
tip_YN = input("Would you like to leave a tip? Type Y or N :  ")

if tip_YN == 'N' :
    people = int(input("How many people to spill the bill?  "))
    total_w = total / people 
    print(f"Each person should pay : {round(total_w,2)}")
else:
    precent = int(input("What percentage would you like to give? 10 , 12 or 15 ?    "))
    people = int(input("How many people to spill the bill?  "))
    total_p = (total * precent) / 100
    total_f = (total + total_p) / people
    print(f"Each person should pay: {round(total_f,2)}")


