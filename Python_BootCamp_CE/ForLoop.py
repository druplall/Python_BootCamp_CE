# For Loop

mylist = [1,2,3,4,5,6,7,8,9,10]

for i in mylist:
    if (i % 2 == 0):
        print(i)

x = 0
while x < 5:
    print(f'The Current value of x is {x}')
    x = x+1
else:
    print('X is not less than 5')


# What is the 'continue' statement ?
# Goes to the top of the closest enclosing loop
mystring = 'Deodat'
for i in mystring:
    if i == 'E':
        continue
    print(i)


