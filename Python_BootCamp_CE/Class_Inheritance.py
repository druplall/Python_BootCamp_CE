# What is inheritance ? 
# It is a way to form new classes using already defined classes
# What is the benefits ? We can reuse existing code and reduce complexity of a program 

## Base Class
class Animal():
    def __init__(self):
        print('Animal Created !')
    def who_am_i(self):
        print('I am an animal ')
    def eat(self):
        print('I am eating')

myanimal = Animal()

myanimal.eat()
myanimal.who_am_i()

## Derived class
class Dog(Animal): # Notice we are passing in the animal class in the Dog class, this will allow us to inhert from the Animal class
    def __init__(self):
        Animal.__init__(self) # Here we are creating an instance of the animal class which dog. 
        print('Dog Created')   
    
    # We can overwrite the base class functions -- Just use the same function name
    def who_am_i(self):
        print('I am dog now')

    def bark(self):
        print('Woof !')    

myDog = Dog()
myDog.eat()
myDog.who_am_i()
myDog.bark()