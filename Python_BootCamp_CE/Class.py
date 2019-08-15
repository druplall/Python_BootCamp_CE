# Learn how to create class in python

class Dog():

    # Class Object Attribute
    # Same for any instance of a class so we dont use the self. keyword

    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


    # Methods are function that act on the object
    # What is the difference between a function and Method ?
        ## A method is a function within a class
    def bark(self, number):
        print('Woof My name is {} and the number is {}'.format(self.name, number))


my_dog = Dog('lab', 'sam')

# This is a method so we need to use ()
my_dog.bark(10)

# The species variable is an attribute so we dont use the () 

print(my_dog.species)

class Circle:
    # Class Object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2

# Note we are setting the default value as 1 in the constructor however if we pass in a value it will overwite the default
my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.get_circumference())
