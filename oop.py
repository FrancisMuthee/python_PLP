'''
Mini Project

In this project, you are tasked to create a program that automates searching for a word definition in a dictionary. Follow the instructions to implement



Dictionary Project is provided here: 



We should have a data source (Download from the link above)
Learn how to load json data into a python dictionary
Create a function that returns a definition of a word
Consider a condition that the entered word is not in a dictionary
Consider input from user having different cases – upper/ lower case or mixed eg: RAIN/rain/RaIN
Make your dictionary program more intelligent incase users input a word with wrong spelling the program should be able to suggest the word that might be intended.
eg . pott instead of pot or rainn instead of rain. Tip: use difflib library here
'''


'''
OOP is a paradigm in CS that relies on the concept of classes and objects.
The building blocks are Classes, Objects, Methods, Attributes.
The four pillars of OOP are; Inheriatnce, Encapsulation, Methods, Attributes.

Python classes and Objects
A class is an object constructor or a blueprint for creating objects.
'''

#You can retrieve the class name of vriables using the type() method.
# A class is defined using a class keyword.
#class members; Class attributes, constructor, instance attributes, properties, class methods.

 #Class attributes are the variables defined directly in the class that are shared by all objects of the class

from mimetypes import init


class person:
    name='Frank' #class attribute
    
print(person.name)

details = person()
print(details.name)
 
#Constructor
#Constructor must have a special name __init__() and a special paramete called self.
#All classes have a function called __init__(), which is always executed when the class is initiated.
#Constructor defines attributes of an instance and assigns values to them.
#The first parameter must be the self which refers to calling the object.

class student:
    def __init__(self): #constructor method
        print("Constructor invoked")

details1 = student()
details2 =student()


#Instance attributes
#They are properties attached to an instance ofa class.They are defined in the constructor.

class alumni:
    nationality = 'Kenyan' # Class attribute
    def __init__(self): #Constructor
        self.name = 'Muthee' # Instance attribute
        self.age = 23 #Instance attribute
P1= alumni()
print(P1.name)
print(P1.age)


#Setting attribute values
class lec:
    def __init__(self, name, age):
        self.name = name
        self.age = age

lec1 = lec("Lucy", 30)
print(lec1.name)

#Also you can set default values.

class Mut:
    def __init__(self, name='Mkuu', age=101):
        self.name=name
        self.age=age

p2=Mut()
print(p2.name)

#Class methods.

#They are defined using def keyword.












