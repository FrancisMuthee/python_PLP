
#Built-in data structures; List,Tuple,Dictionary,Set.
#they are objects(nonprimitive data types)
#User-defined;Stack,Queue,Tree,Linked list,Graph, Hash map
#Indeximg strats from zero.
#Slicing operator(:),Start index is inclusive and last index is exclusive.
#
my_list = ["soko","uwezo", "dishi tamu","raha","Dola","Ndovu"]
print(my_list)
print(my_list[-1])
my_list.append('lowland') # adding a new item to the list.
print(my_list)
empty_list = []

list_2 = ['samaki', 'Sukuma', 'Spinach']

my_list.extend(list_2) # Combining two lists
print(my_list)

my_list[2]= 'Tupike' # Changing the values of my_list
print(my_list)

del my_list[2]
print(my_list)

for list in my_list: #Iterating through a loop
    print(list)

#List comprehension
nums= [num*num for num in range(1,6)]
print(nums)


#TUPLES
#Not immutable
my_tuple = ('Ginger','Vitamalt','happy happpy','Nuvita')
print(my_tuple)

#Dictionary
#ordered collection with key/value pairs
#Key is the unique identifier.

Dictionary = ['Kenya:' 'Nairobi','Rwanda:' 'Kagame']
print(Dictionary)

set_1 ={'even','prime','odd','complex','negative','positive'}
print(set_1)
set_1.add('decimals')
print(set_1)

# set_1.update(random)
# print(set_1)

#Question 1
#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
integers = input('List your random integers')
integers_1=[]
print(integers)

#Question 2
#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Books = ('Child of Two worlds','Thinking Fast and slow','The Davici code','Zero to One','Art of War')
for book in Books:
    print(book)


 #Question 3
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

#Question 4
# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
    
#Question 5
# Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.       

if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)


















































