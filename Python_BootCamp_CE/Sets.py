# Sets are unordered collections of unique elements
# Meaning there can only be one represenatative of the same object.
# Aka - Only one unique value

myset = set()
print(type(myset))
myset.add(1)
print(myset)

# Note 1 already exist and will not show two 1's
myset.add(1)

# You can cast a list to a set to get only the unique values
mylist = [1,1,1,1,3,3,3]
print(set(mylist))

