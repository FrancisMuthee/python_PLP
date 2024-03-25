marks = 80
result = ""
if marks < 30:
    result = 'failed'
elif marks > 75:
    result= "passed with distinction"
else:
    result = "passed"

print('He ' + result)


#Match statements
def checkvowel(n):
   match n:
       case 'a': return "vowel alphabet"
       case 'e': return "vowel alphabet"
       case 'i': return "vowel alphabet"
       case 'o': return "vowel alphabet"
       case 'u': return "vowel alphabet"
       case _: return "simple alphabet"
print(checkvowel('a'))
print(checkvowel('m'))
print(checkvowel('u'))

# bike = 'Yamaha'
# if bike == 'Suzuki':
# print('the bike is ')
# print()

#LOOPS
#for loop.
cars = ['mercedes', 'bmw', 'caldina', 'Premio']
for car in cars:
    print(car)

#while
i = 1
while i < 6:
    print(i)
    i += 1


#Jump statements.
    #breaking
x = 0
while x < 10:
    print('x:', x)
    if x ==5:
        print("Breaking ...")
        break
    x += 1

print('end')

#Continue
for letter in "python":
    if letter == "h": continue
print("Current letter :", letter)


#Conditional statements.
grade = 83
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print('F')


#While loop
count = 0
while count <= 2:
      count += 1
      print(count)
    
#Using break statement.

colors = ['blue','green','white','yellow','brown','cream']
my_want = 'yellow'

for color in colors:
    if color == my_want:
        print('They have my want')
        break
    print(color)

#Continue
ages = [13,24,17,36]

for age in ages:
    if age <21:
        continue
    print(age)


 #Nested loops
    
groups = [['paul', 'Frank', 'Swazzer', 'Messi'], ['Arsenal', 'Barca', 'MNC','Wolves']]  
for group in groups:
    # print(group)
    for name in group:
        print(name)    


#List comprehensions
nums = [4,-11,69,53,-65]
doubled = [num * 2 for num in nums]
print(doubled)


#Function elements/parameters
def add_nums(a,b):
    answer = a+ b
    return answer
total = add_nums(2,13)
print("The total is: ", total)

#Arbtrary arguments
def add_nams(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print("Total ", add_nams(2,3,5,7,9,11,13,17,19,23,29,31,37))

#Kwargs, Keyword Arguments
def add_ages(**ages):
    sum = 0
    for k, v in ages.items():
        sum += v
    return sum
print('Total:', add_ages(Mutemi=23, skiloo=22, Adams=25))

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

for num in range(1, 5):
    print(num)
































