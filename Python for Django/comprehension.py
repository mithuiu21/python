# Comprehension
# iterable -> List, tuple, Dictionary, Set, Range
# create -> List, Dictionary, Set 


myList = [1,5,6,7,2,3]
newList = []

for i in myList:
    newList.append(i*i)

print("Old List: ", myList)
print("New List: ", newList)


comList = [i*i for i in myList]
print("Compreshension List: ", comList)

# List of the squares of the odd numbers
newList2 = []
for i in myList:
    if i%2 == 1:
        newList2.append(i*i)
print(newList2)

comList2 = [i**3 for i in myList if i%2==0]
print(comList2)

#####
#######
# From List
myList2 = [1,2,3,4,5,6]
newList2 = [i+1 for i in myList2]

print(newList2)

# Create Dictionaries
newDict = {i: i*i for i in myList2}
print(newDict)

#  Create set
newSet = {i**3 for i in myList2}
print(newSet)

# Create Tuple
newTuple = tuple(i**4 for i in myList2)
print(newTuple)

# Create Tuple List
newTList = [(i, i**2) for i in myList2]
print(newTList)


## From Dictionary

myDictionary = {'name':"K. Mithu", "Uni": "UIU", 'Year': 2022}

newDList = [value for key, value in myDictionary.items()]
#newDList = [key for key, value in myDictionary.items()] # get the key/ values for Dictionary
print(newDList)

# Tuple
newTList2 = [(key, value) for key, value in myDictionary.items()]
print(newTList2)

# New Dictionaries
newDict2 = {key + "key": value for key, value in myDictionary.items()}
print(newDict2)



# String comprehension
mySList = [ letter.upper() for letter in 'Bohubrihi']
print(mySList)


##########
########
# Nested Loop

# 0 1 2 3
# 0 1 2 3
# 0 1 2 3

myMatrix = [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
print(myMatrix[0][2])

matrix = []

for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)

print(matrix)

# Matrix with Comprehension 
myComMatrix = [[j for j in range(4)] for i in range(3)]
print(myComMatrix)

# flat
flatList = [i[0] for i in myComMatrix]
print(flatList)


# https://docs.python.org/3/tutorial/datastructures.html
