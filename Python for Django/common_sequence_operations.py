# Common Sequence Operation
# list, tuple, range
# List -> mutable
# tuple -> immutable
# in

myTuple = ("K. Mithu", "UIU", 2022)
myList = ["K. Mithu", "UIU", 2022]
myRange = range(0, 51)

result = "K. Mithu" in myTuple # myList / myRange
print(result)

result2 = "UIU" in myList
print(result2)

result3 = 2022 in myRange
print(result3)

# concat
myTuple1 = ("K.",)
myTuple2 = ("Mithu",)
myFullname = myTuple1 + myTuple2
print(myFullname)


# Len()
print(len(myFullname))


## https://docs.python.org/3/library/stdtypes.html


############
############

# Sequence Unpacking

myTupleSU = ("Bangladesh", "India", "Pakistan")
c1, c2, c3 = myTupleSU
print(c1)
print(c2)
print(c3)

# same goes for List and Nested List
myListSU = ["Bangladesh", "India", "Pakistan", [1, 2, 3]]
p1, p2, p3, [p4, p5, p6] = myListSU
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)

## use * for assigned rest of element and '*' is used one time only
myListSUstar = ["Bangladesh", "India", "Pakistan", "USA"]
p1, p2, *p3 = myListSUstar
print(p1)
print(p2)
print(p3)

