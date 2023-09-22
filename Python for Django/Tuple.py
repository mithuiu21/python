# Tuples -> Sequence Data Type
# Immutable
# homogeneous => List (Data type same)
myList = [1, 2, 3, 4 ]
# heterogeneous => Tuple (Different data type)
myTuple = ("Dhaka", 2, True)

#######################

tp = "K. Mithu", 25, "Dhaka"
print(tp)

# Nested tuples
tpTwo = ((1,2), "K. Mithu")
print(tpTwo[1])
 
# Get an error / Tuble is Immutable
#tpTwo[1] = "Dhaka" 

#List in tuple and list is changeable
tpThree = ([1,2,3], [4,5,6])
print(tpThree)

tpThree[0][0] = "Dhaka"
print(tpThree)


# Empty Tuple
tpFour = ()
print(tpFour)

# Tuple with a single element ** must use a comma after element
tpFive = "Dhaka",
print(tpFive)


