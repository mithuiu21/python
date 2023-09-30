## JSON in Python

import json

x = '{"name":"BD", "age": 51}'
y = json.loads(x)

y = json.dumps(x)

# print(y)


####
# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "Peter",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Leroy","Kimberly"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

