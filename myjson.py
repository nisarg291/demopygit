
# Python JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Parse JSON - Convert from JSON to Python

"""If you have a JSON string, you can parse it by using the json.loads() method.
The result will be a Python dictionary.
Example
Convert from JSON to Python:"""

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print(type(x))
# parse x:
y = json.loads(x)  # to convert form json to python json.loads() is use
# and we give the json object as parameter of an obj

# the result is a Python dictionary:
print(y["age"])
print(type(y))  # it is dictionary

# Convert from Python to JSON

"""If you have a Python object, 
you can convert it into a JSON string by using the json.dumps() method.
Example
# Convert from Python to JSON:"""
x ={
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(type(x))  # it is dictionary
y = json.dumps(x)  # convert python dictionary into json string
print(y)  # the result is a JSON string:

