
# indexing
myList = ["Bhutan", "Nepal", "France", "Italy", "Brazil", "dubai", "Germany", "USA","AU"]

# positive indexing
print(myList[1]) # Bhutan

# negative indexing
print(myList[-1]) #AU


#slicing and create a new list with positive index
newList = myList[3:5] # upto
print(newList)

##slicing and create a new list with negative index
newList = myList[-5:-1]
print(newList)

# Starting index 1 and Ending index 5 and skip one member
newList2 = myList[1:5:2]# skip 2
print(newList2)


# list Methods
#myList.append("Bangladesh")
#myList.append(2)
#myList.append(["Palistan", "India"])
#myList.extend(["Palistan", "India"])
#myList.insert(3,"Bangladesh")
#myList.remove("Italy")
#country = myList.pop(3)
#print(country)

#myList.clear()
print(myList)


# List Sorting

myList.sort()
print(myList)

#ASCII Table
# https://www.rapidtables.com/code/text/ascii-table.html
myList.sort(key=str.lower, reverse=True)
print(myList)

# reverse sorting
myList.reverse()
print(myList)

#Py built-in datastructures
#https://docs.python.org/3/tutorial/datastructures.html

#Py built-in functions
# https://docs.python.org/3/library/functions.html
