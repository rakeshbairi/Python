print("hello world");

#Concatenation
first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)

#A list stores a series of items in a particular order. You
#access items using an index, or within a loop.

#Make a list
bikes = ['trek', 'redline', 'giant']

#Get the first item in a list
first_bike = bikes[0]
print('First Bike:'+ first_bike)

#Get the last item in a list
last_bike = bikes[-1]
print('Last Bike:'+ last_bike)

#Looping through a list
print('Lopping Started:')
for bike in bikes:
 print(bike) 
print('Lopping End:')
 
#Adding items to a list
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

'''
Making numerical lists
range(start, stop, step)
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Optional. An integer number specifying at which position to end.
step	Optional. An integer number specifying the incrementation. Default is 1
'''

squares = []
for x in range(1, 11):
 #   print(x)
   squares.append(x**2) 

for item in squares:
  print(item)

squares = [x**2 for x in range(1, 11)]

#Slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]

for item in first_two:
  print(item)

#Copying a list
  copy_of_bikes = bikes[:]

#Tuples
#Tuples are similar to lists, but the items in a tuple can't be modified.
dimensions = (1920, 1080)

#Conditional test with lists
#equals x == 42 not equal x != 42 greater than x > 42 or equal to x >= 42 less than x < 42 or equal to x <= 42

#'trek' in bikes 
#'surly' not in bikes
age=20
if age >= 18: 
  print("You can vote!")

age=2
if age < 4: 
   ticket_price = 0 
elif age < 18:
   ticket_price = 10 
else: 
   ticket_price = 15
    
print(ticket_price)

#Dictionaries store connections between pieces of information. Each item in a dictionary is a key-value pair.
alien = {'color': 'green', 'points': 5}
print("The alien's color is " + alien['color'])

#Adding a new key-value pair
alien['x_position'] = 0
print("The alien's color is " + str(alien['x_position']))

#Looping through all key-value pairs
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items(): 
  print(name + ' loves ' + str(number))

  #Looping through all keys
  for number in fav_numbers.values(): 
    print(str(number) + ' is a favorite')

#USER INPUT Your programs can prompt the user for input. All input is stored as a string.
name = input("What's your name? ") 
print("Hello, " + name + "!")

#Prompting for numerical input
age = input("How old are you? ") 
age = int(age)
print("Age:"+str(age))
pi = input("What's the value of pi? ")
pi = float(pi)
print("PI:"+str(pi))
