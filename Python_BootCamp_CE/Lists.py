# Testing List
my_list = [1,2,3,4]
my_name = ['Deodat', 'Ruplall']

test = my_list + my_name

# Append will add new item to the back of the list
my_list.append('New')

print(my_list)

# Pop will remove the last element from the list
my_list.pop()
print(my_list)

# You can save the popped item to a variable
popvalue = my_list.pop()
print('This is the popped item: ' + str(popvalue))

# You can pass in the index position to pop to remove a specific value
my_list.pop(1)
print(my_list)

# You can sort list by the .sort() function
new_list = ['a','e','x','b','c']
new_list.sort()
# Sorting is done in place so you dont need to return a value which would be the sorted amount. 
print(new_list)

# None type is a common value returned for a default value.