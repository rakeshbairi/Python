print("hello world");

#Concatenation
first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)


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

#Making numerical lists
#range(start, stop, step)
#start	Optional. An integer number specifying at which position to start. Default is 0
#stop	Optional. An integer number specifying at which position to end.
#step	Optional. An integer number specifying the incrementation. Default is 1

squares = []
for x in range(1, 11):
    print(x)
    squares.append(x**2) 

for item in squares:
  print(item)

squares = [x**2 for x in range(1, 11)]

#Slicing a list
