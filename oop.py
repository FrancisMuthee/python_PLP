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
#This a python function in a class
#They are defined using def keyword.
#Has a self parameter which refers to calling the instance.

class prof:
    def displayInfo(self): #class method
        print('personal information')

p3=prof()
p3.displayInfo()

class rep:
    def __init__(self, name, age):
        self.name = name
        self.age= age

    def displayInfo(self): #class method
        print('rep Name:',self.name,'Age:', self.age)

p4 = rep('Mzandu', 24)
p4.displayInfo()

#deleting attribute, class, object use del followed by its name.


#Inheritance

#process of inheriting properties from parent class to child class
#It promotes code reusability.
#Types
#Single,multiple,multilevel,hierarchical,hybrid.

#Single
#Base/parent class
class vehicle:
    def vehicle_info(self):
        print("Inside parent(vehicle) class") 
#child class
class car(vehicle):
    def car_info(self):

        print("inside child(car) class")

#Create object of a car
car = car()

#Access vehicle's info using car object

car.vehicle_info()
car.car_info()

#Multiple
#One child class inherits from multiple parent classes

#Parent class 1

class father:
    def father_info(self, name, age):
        print('Inside fathers class')
        print('Name:', name, 'Age:', age)

#Parent class 2
class mother:
    def mother_info(self, company_name, location):
        print("Inside mothers info")
        print('Name:', company_name, 'location:', location)

#Childs class
class student(father, mother):
    def student_info(self, grade, sport):
        print('Inside student class')
        print('grade', grade, "sport", sport)

#create an object of student
pupil= student()

#Access data
pupil.father_info('Robert', 50)
pupil.mother_info('SSA', 'Nyeri')
pupil.student_info(71, 'Football')


#Multilevel inheritance
#Chain of classes

#base class
class motors:
    def motors_info(self):
        print('inside motors class')

#Child class
class car(motors):
    def car_info(self):
        print('inside car class')

#Child class
class sportscar(car):
    def sportscar_info(self):
        print('Inside sportscar info')


#Create object for sportscar
s_car = sportscar()
#Access vehicles and car info using sportcar object
s_car.motors_info()
s_car.car_info()
s_car.sportscar_info()

#Hierarchical
class shop:
    def budgetry(self):
        print('This is a shop')

class retail(shop):
    def shop_info(self, name):
        print("Shop name is:", name)

class items(shop):
    def items_info(self, name):
        print("fresh products located in:", name)

obj1= retail()
obj1.budgetry()
obj1.shop_info('Budgetry')

obj2 =items()
obj2.budgetry()
obj2.items_info('this shop')


#python super() function
#makes the child class inherit all method and properties from its parent.

class company:
    def company_name(self):
        return 'Google'
    
class employee (company):
    def info(self):
        #calling the super class method using super() function
        c_name = super().company_name()
        print('This guy works at', c_name)

#Creating object of childs class
emp = employee()
emp.info()

'''
Kindly go through the assignment, and submit the GitHub repo


Create a Python class named Person.
The Person class should have the following attributes:
name: representing the person's name.
age: representing the person's age.
gender: representing the person's gender.
Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
Create an instance of the Person class and call the introduce method to display the person's information.
Create a GitHub repository for your assignment and submit the link.
'''

