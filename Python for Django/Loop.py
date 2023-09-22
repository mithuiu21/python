# looping
# for i in tuple, range, dictionary, list

# Tuple
myTuple = ("a", "b", "c", "d")

for x in myTuple:
    print(x)

# List
myList = [("a", 1, "BDT"), ("b", 2, "USD"), ("c", 3, "CAD")]
for a, b, c in myList:
    print(f"{a}, {b}, {c}")

# Dictionaries
myDict = {
    'name': 'K. Mithu',
    'age': 25,
    'uni': "UIU"
}

for key, value in myDict.items():
    print(f"{key} => {value}")


# String

myStr = "Bangladesh"
for a in myStr:
    print(a)

# Sets
mySet = {"BDT", "USD", "CAD"}
for currency in mySet:
    print(currency)


#########
#########
# Loop with range() function
myListRange = list(range(1,10))
print(myListRange)

for i in range(1, 10):
    print(i)

## 2 to 100 Even number:
for even in range(0, 51, 2):
    print(even)

## 
myLangList = ["Bangla","English", "Irish", "Chinese"]

for l in range(len(myLangList)):
    print(f"Languages: {myLangList[l]}")

print("...........")

# Different Loop technique

myFruitList = ['orange', 'apple', 'banana', 'apple']
for fruit in myFruitList:
    print(fruit)

# sorted
for s in sorted(myFruitList):
    print(s)

print("..........")

# reversed
for r in reversed(sorted(myFruitList)):
    print(r)

print("..........")

# enumerate:

for f, fruit in enumerate(myFruitList):
    print(f"{f} index of {fruit}")


# zip
myList1 = ["a","b","c","d","e"]
myList2 = [1,2,3,4,5]

for p, q in zip(myList1, myList2):
    print(p, q)

