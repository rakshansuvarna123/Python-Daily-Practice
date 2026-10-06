''' 
Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. 
If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price
'''

gender=input("enter your gender:    ")



if gender=="female":
    print("free ticket")
else:
    age=int(input("enter your age:  "))
    if(age<=5):
        print("free ticket")
    elif(5<age<=12):
        print("half ticket")
    elif(age>=60):
        friend=input("are you friend of conductor?(y/n)")
        if friend=="y":
            print("free ticket")
        else:
            print("senior citizen discount")    
    else:
        print("pay full for ticket")    
        




# library membership proble, using If statements

age=int(input("enter your age:"))
if age<=18:
    print("student membership")
elif age>=60:
    print("senior citizen membership")
else:
    print("regular membership")        

# meal time program using If

time=int(input("enter time of the day(24 hours cycle)"))
if time==8:
    print("breakfast")
elif time==13:
    print("lunch time")
elif time==20:
    print("dinner time")
else:
    print("not meal time")        
