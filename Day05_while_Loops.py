''' 
Basic Counting with while Loop:

Write a program that counts from 1 to 10 using a while loop.
'''

i=1
while i<=10:
    print(i,end=" ")
    i+=1

''' 
Odd Numbers Printer:

Create a program that prints all odd numbers between 1 and 20 using a while loop.

'''

i=1
while i<=20:
    if i%2==0:
        i+=1
        continue
        
    print(i,end=" ")
    i+=1

ticket=8
while ticket>0:
    print("a seat is booked")
    ticket-=1
    print(f"remaining tickets {ticket}")
print("all ticket are booked")    
