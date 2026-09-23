'''List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.'''

my_list=["apple","banana","mango","Orange","chikku"]

my_list.append("pomogranate")
print(my_list) #appended new item to the end of the list

my_list.insert(1,"pears") #added new item at the second position
print(my_list)

my_list.pop(2) #removed the third item from the list
print(my_list)



#2
'''Reverse and Sort a List: Create a list of numbers and:

Sort it in descending order.
Reverse the sorted list and print it.'''

num=[10,30,-5,15,25,35,50]
num.sort()
print(num) #sorted the list in ascending order

num.sort(reverse=True)
print(num) #sorted the list in descending order

num.reverse()
print(num) #reversed the sorted list    
