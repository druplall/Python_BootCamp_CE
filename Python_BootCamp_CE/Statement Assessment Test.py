st = 'Print only the words that start with s in this sentence'
st = str.upper(st)

for i in st.split():
    if i[0] == 'S':
        print(i)

print('All Even number 0 - 10 code')
for i in range(0,10):
    if (i % 2) == 0:
        print(i)

print('List Comprehesion code here !')

print('Go through the string below and if the length of a word is even print EVEN!')
st2 = 'Print every word in this sentence that has an even number of letters'
print(st2)

for i in st2.split():
    if (len(i) % 2) == 0:
        print(i)

print('Write a program that prints the integers from 1 to 100. But for multiples of three print FIZZ')
for i in range(1,101):
    if(i % 3) == 0:
        print( str(i) + ' Fizz')
    elif (i % 5) == 0:
        print(str(i) + 'Buzz')
    elif