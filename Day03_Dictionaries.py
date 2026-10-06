''' 
Basic Dictionary Operations:

Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary.
'''

my_dict={"udupi":"dosa","mangalore":"buns","davanagere":"benne dosa","uttarkannada":"rotti"}

my_dict["bangalore"]="chai"

print(my_dict)

my_dict["bangalore"]="kebab"
print(my_dict)

my_dict.pop("davanagere")
print(my_dict)

print(my_dict.keys())
print(my_dict.values())



''' 
Nested Dictionary Practice (Simple for now):

Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
Access and print the favorite food of one friend.

'''


friends={
"friend_dict1":{
    "name":"sudeep",
    "fav_food":"Rice and dal",
    "fav_subject":"DL"
},
"friend_dict2":{
    "name":"bob",
    "fav_food":"biryani",
    "fav_subject":"maths"
}

}
print(friends["friend_dict1"]["fav_food"])
