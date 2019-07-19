# How to define functions
## def name_of_function():
## Docsting explain function.
## print('Hello')
### Call function by name, example name_of_function

def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input..
    OUTPUT: Hello..
    :return:
    '''
    print('Hello')

name_function()

# Find out of the word dog is in a string ?
def dog_check(mystring):
    return 'dog' in mystring.lower()

print(dog_check('MY DOG is great !'))

# Pig Latin code
def pig_latin (s):
    mylist = ['a','e','i','o','u']
    for i in mylist:
        if s[0].lower() == i:
            return (s + 'ay')
        else:
            return (s[1:] + s[0] + 'ay')

test = pig_latin('apple')
print(test)

def pig_latin_two (word):
    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin_two('a'))