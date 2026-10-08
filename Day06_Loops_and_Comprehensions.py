''' 
Multiples of 3:

Write a for loop that prints all multiples of 3 between 1 and 30.
'''
i=3
print("Multiples of 3")
for j in range(1,11):
    print(i*j)


''' 
Sum of First 10 Numbers:

Write a program using a for loop that calculates the sum of numbers from 1 to 10.

'''

total=0
for i in range(1,11):
    total+=i
print(f"sum of first 10 numbers is >>>{total}")    

'''  
Print Your Name Letter by Letter:

Write a program that takes your name as input and prints each letter of your name using a for loop.
'''

name="Rakshan"
for letters in name:
    print(letters,end=" ")


'''  
Count Vowels in a String:

Write a program that counts how many vowels are in a given string using a for loop.
'''

name="Rakshan Suvarna"
count=0
for letters in name:
    if letters.lower() in "aeiou":
        count+=1
print(f"Number of vowels {count}")  


''' 
List Manipulation:

Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

'''
kannada_foods=["Buns","Neer dosa","Masala dosa","Ragi dosa"]
capitalized_foods=[food.upper() for food in kannada_foods]
print(capitalized_foods)

'''  
Sum of Prices:

Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

'''
my_dict={"soap":150,"shampoo":100,"body sparay":225,"hair jel":140,"hair oil":200}
total=0

for num in my_dict.values():
    total+=num
print(f"Total price of all items {total}")    

'''  
List of Squares:

Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
'''
l=[i for i in range (1,11)]
dl= [x**2 for x in l]
print(l)
print(dl)


''' 
Student Data Task:

Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student.
 Loop through the list and print each student's information.
'''

students=[
    {
        "name":"rakshan",
        "age":21,
        "marks":25
    },
    {
      "name":"sudeep",
              "age":18,
              "marks":95  
    },
    {
        "name":"rakshith",
                "age":21,
                "marks":75
    }
]
for student in students:
    print(f"Name:{student['name']} Age:{student['age']}, Marks:{student['marks']}")

'''  
Dictionary Comprehension:

Create a dictionary where the keys are Kannada cities, and the values are their populations.
 Use dictionary comprehension to filter out cities with populations below 10 lakhs
'''

cities={"udupi":9,"mangalore":11,"bengaluru":80,"dharwad":15,"hubbali":7}
pop_cities={city:pop for city,pop in cities.items() if pop>10 }
print(pop_cities)

'''  
Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

Prints the entire matrix row by row.
Prints the sum of each row in the matrix.
'''
matrix=[
    [1,2,3],
    [4,5,6],
    [8,9,10]
]
for row in matrix:
    print(row)

for index,row in enumerate(matrix,start=1):
    row_sum=sum(row)
    print(f"sum of {index}st row  is {row_sum}")
