# Flask tutorial
# The request is what your browser is doing, searching the internet is a request.. The Response is what you get back.
# Whenever we go to google the request is the following
# GET / HTTP/1.1
# GET IS THE VERB, THE / is the path and the HTTP is the protocol
# HOST: www.google.com
# The get is the verb that tells the server what we think it will return (Protocol)
# Example: GET /download/mac HTTP/1.1
# https:/git-sccm

# What are the main verbs ? GET, POST, PUT and Delete
# Get will retrieve something
# POST will receive data, and use it
# PUT Make sure something is there
# DELETE will remove something

# What is the principle of REST API? Its a way of thinking about how a web server responds to your request
# It will response with resources (aka data)
# Is is stateless -- This means one request cannot depend on any other request,
# the server will only know about the current request and not any of the previous requests

from flask import Flask, jsonify, request
# Always us upper case for the first letter for the Class, Lower letter is usually the package

# __ is a special variable that gives each file a unique name
app = Flask(__name__)

# Creating a list of stores
# JSON is basically a key value pair (dictionary ), very usefully for sending data from one application to another
# JSON is a long string (A dictionary is not a JSON)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }

]


# Important to know, from the server point of view: GET is used to send back data only and POST is used to receive data
# We will create some end points
# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
# 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    # iterate over stores
    # IF the store names matches, return it
    # if none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
    # this will return a string from the list of store


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>/item
@app.route('/store/<string:name>')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Item is not found'})


# What is the port ? Is an area of the computer where you will receive a response
app.run(port=5000)