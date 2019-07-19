# What is *args and *kwargs ? 
# *args is treated as a tuple of data and we can pass as many parameters within the function. 
# **kwargs will build a dictionary of values
def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(40,60))

def myfunctKwarg(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunctKwarg(fruit = 'apple', veggie = 'lettuce')