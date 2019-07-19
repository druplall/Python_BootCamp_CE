# Dictionaries are unordered mapping for sotring objects
# This key-value pair allows users to quickly grab objects without needing to know an index location
# Dictionaries will uses { } and colons to signify the keys and thier associated values. 
    # {'key1':'value1', 'key2':'value2'}

# When to use a dictionary verus a list ? 
    # Dictionaries: Objects retrieved by key name -- They are unordered and cannot be sorted (** You don't need the location for accessing**)
    # Lists: Objects retrieved by location.       -- Ordered sequence can be indexed or sliced.

my_dict = {'name':'Jose', 'age': 50,'grades':[12,45,66,90]}
# Use the [] brace for passing the key
print(my_dict['grades'])

# How to access value in a dictionary of dictionaries
d = {'k1':'Test', 'k2':1, 'k3':{'InsideKey':10000000}}
print(d['k3']['InsideKey'])

lottery_player = {
    'name': 'Deo',
    'number': (20,30,40)
}

universities = [
    {
        'name': 'Deo',
        'location': 'UK'
    },
    {
        'name': 'Haley',
        'location': 'usa'
    }
]

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]

    },
    {
        'name': 'Second Store',
        'items': [
            {
                'name': 'Second item',
                'price': 30.95
            }
        ]
    }

]

print(stores[1]['items'][0]['price'])