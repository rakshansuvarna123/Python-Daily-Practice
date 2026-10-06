''' 
Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.
'''

fruits=("apple","banana","mango","Orange","chikku") #creation

#fruits.append("tomato") #error because immutable

print(fruits[1:3]) #slicing

fruits1=("pears",)
fruits2=fruits+fruits1 #conctenation
print(fruits2)


''' 
Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?

'''


fruits1={"mosambi","orange","banana"}
fruits2={"banana","papaya","seethapala"}
print(fruits1 &  fruits2)
print(fruits1 | fruits2)
print(fruits1-fruits2)
fruits1.add("mango")

fruits1.remove("mosambi")
fruits1.discard("banana")
print(fruits1)


'''  
Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?
'''


l=[1,2,3,4,5]

s=set(l)
print(s) #converted list to set 

t=tuple(l) 
print(t) 

#t.add(7)   error
s.add(7)
print(s)  
