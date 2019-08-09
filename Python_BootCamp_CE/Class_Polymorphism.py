# What is Polymorphism ? Refers to the process in which different object classes can share the same method name. 

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' Say Woof'

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' Say Meow !'

niko = Dog('Niko')
flex = Cat('Felix')

print(niko.speak())
print(flex.speak())

# How to demonstate Polymorphism
for pet in [niko,flex]:
    print(type(pet))
    print(pet.speak())

# The best way is to use a function

def pet_speak(pet):
    print(pet.speak() + ' function test')

pet_speak(niko)

# What is an abstract class ? It is a class we will never expect to instantiate/create an instance of the abstract class
class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')



# This would fail as we are trying to instantiate an abstract class
#my_animal = Animal('Dog')
#my_animal.speak()