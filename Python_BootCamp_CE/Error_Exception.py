# The following are the 3 keywords for the exception handling
# try: This is the block of code to be attempted 
# except: Block of code will execute in case there is an error in try block
# finally: A final block of code to be exected, regardless of an error (ALWAYS Executed)

def add(n1,n2):
    print(n1+n2)

add(10,20)

# To get user input we use input()
number2 = input('Please enter a number: ')
# Note input will return the data in string format

#add(10,number2)

try:
    #want to attemp this code
    add(10,number2)
except:
    print('failed')
else:
    print('Add went well')


try:
    f = open('testfile', 'w')
    f.write('Write to the test line')
except TypeError:
    print('There was an error')


def ask_for_int():
    try:
        result = int(input('Please provide an input: '))
    except:
        print("Whoops this is not a number")
    finally:
        print('Final ')