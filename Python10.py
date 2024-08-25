"""
#
# Part: Python JSON
# API = Application Programming Interface
#
"""
import json

# make a json (Dictionary string)
x = '{"name": "John", "age": 20, "city": "Phuket"}'
print(x)

# pardr
y = json.loads(x)

# python dictionary
print(y)
print(type(y))
print(y["city"])

# python dictionary
a = {
    "name": "Noa",
    "age": 20,
    "city": "Phuket"
}

# convert to JSON (string)
b = json.dumps(a)

# JSON String
print(b)