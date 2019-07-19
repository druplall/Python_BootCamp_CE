#Dictionaries is a key value pairs
my_dict = {'name':'Jose', 'age': 50,'grades':[12,45,66,90]}

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