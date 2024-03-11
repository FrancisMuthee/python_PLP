print("Hello world")

#This is a tuple, it has ordered elements. It's immutable, and cannot be modified.
tuple = ("Ramsdale", "Saliba", "Odeegard", "Martinelli")
print (tuple[2]) #Accessing the second indexed variable.

#Talk of a list, we use square brackets.
list = ["Lucy", "Dokta", "Scar", "Frank"]
print (list[3])

#And a Dictionary? For pair elemets ie Key and value.
Dictionary = {'Kenya': 'Nairobi', 'Djibouti': 'Djibouti', 'Tanzania': 'Dodoma'} 
print(Dictionary)

#Indexing starts from 0,1,2,3...

#string data types
message = 'How are you doing today?'

#Set , Sets are mutable.
student_id = {100,101,102,103}
print(student_id)

#CONVERSION
#Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.

#Commenting
#Always use comments to explain why we did something rather than how we did something. Comments shouldn't be a substitute to explain poorly written code.

#Types of operators
#Arithmetic, logical, Assignment, Bitwise,Special(is and is not), membership operators(in and not in)

#Syntax of print
#print(object= separator= end= file= flush=)
#end= is used to add a new line

print('Good mrng', end= ' ') #Like concatenation of two strings
print('It is a rainy day')

#Separator
print('New Year', 2023, 'See you soon!', sep= '.')

#Concatenation
print('Hello, '+'Njaramba')

#Output formatting
x=5
y=10
print('The value of x is {} and the value of y is {}'. format(x,y)) #The fullstop used used to close the statement.

#Input from the user
num = input('Enter a number') #input when requesting an output.
print('You entered:', num)

var_1 = 'El'
var_2 = 'GODFATHER'
print(f'My name is {var_1} and I am the {var_2}') # f' can be used to reference variable in as calling them.































