# Dictionaries
# Key -> value


myDict = {
    'key1': "K. Mithu",
    'key2': 2021
}

print(myDict)

# Empty Dictionaries
myDict2 = {}
print(myDict2)

myDict2['key1'] = "Paul"
print(myDict2)
myDict2['key2'] = "Petar"
print(myDict2)


## dict() function

a = dict(key1 = 'K. Mithu', key2 = 'UIU', key3 = 2022)
print(a)

b = {'key1': 'K. Mithu', 'key2': 'UIU', 'Key3': 2022 }
print(b)

# zip() function

c = dict(zip(['key1','key2','key3'], ['K. Mithu', 'UIU', 2022]))
print(c)

# Tuple in Dictionaries

d = dict([('key1','K. Mituy'), ('key2', 'UIU')])
print(d)

##
e = dict({'key1': 'K. Mithu', 'key2': 'UIU', 'key3': 2022})
print(e)

f = dict({'key':'K. Mithu', 'key2': 'UIU'}, key3 = 2022)
print(f)

#pop
print(e.pop('key1'))

## Pass dictionaries in list and access list key

x = list(f)
print(x)


## https://docs.python.org/3/library/stdtypes.html

