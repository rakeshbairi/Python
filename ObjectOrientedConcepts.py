'''A class defines the behavior of an object and the kind of
information an object can store. The information in a class
is stored in attributes, and functions that belong to a class
are called methods. A child class inherits the attributes and
methods from its parent class.'''
class Dog():
    '''Represent a dog.'''
    def __init__(self,name):
        '''Initialize dog object '''
        super().__init__(name)

    def search(self):
        #Simulate Searching
        print(self.name + " is sitting.")
    
my_dog = Dog('Pesco')
print(my_dog.name + " is a great thing!")

        