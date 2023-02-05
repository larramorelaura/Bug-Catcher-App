print ("Hello World")

x=5
if x > 50:
    pass
# This is a comment

"""
This is a comment that can 
be on multiple lines
"""

#variables
snake_case = "all loer case, separated by underscore"
GLOBAL_VAR = "All caps"
#class names will be pascal case ie HumanClass

#Datatypes
#primitive and composite
#primitive are the most basic building blocks
#boolean
bool = True
bool2 = False
    #boolean must be capitalized
#number
integer=8
float_num=8.6
#string
string="A collection of characters!"
format_string= f"We can inject variables using {integer}" #this will basically concat into a string
print(format_string)


#composite are collections of the primitive types

#tuples
#immutable list, cannot be changed
tup=(1, 2, 3, 4, 5)
print(tup[3])#indexed like lists

#lists--what we call arrays in js, zeor indexed
list =[1, 2, 3, 4, 5, 6, 7, 8]
val = list[7]
list[7]= 100 #changes the value
print(list)
len(list) #returns the length of a list
#list methods
list.append(2) #a method is a function that belongs to a class...this will add to a list
print(list)
list.pop(2) #pop will remove by index
list.remove(100) #remove takes in a value instead of an index
print(list)
list.sort(reverse= True) #alphabetically or numerically and reverses the list
print(list)

#dictionaries
#Dont Index Coupled Things
#Key Value Pairs
dog_dict={
    'name': 'Pebbles',
    'age': 3,
    'breed': 'Corgi'
}
print(dog_dict)
name=dog_dict['name'] #if you try to access a key that doesnt exist in the dict, you'll get a key error and crash the code
print(name)

if "name" in dog_dict:
    print(f"The dogs name is{dog_dict['name']}")
if "size" in dog_dict:
    print(f"The dog size is{dog_dict['size']}")
else:
    print("Size not found")

dog_dict['size'] ="big boi"
print(dog_dict)

#removing from a dict
del dog_dict['age'] #deletes it and it disappears
breed = dog_dict.pop('breed') #pop can return back the value
dog_dict.clear() #nuclear option removes every key value from the dictionary


#ctl shift l grabs all instances of a word ctrl d grabs the next one so you can change a few


"""
Py       Js
==       ===
none     null
not      !
or       ||

operators in conditionals
and     ==
or      <=
not     >=