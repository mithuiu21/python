# Function


def hello(fname, lname):
    print(f"Full Name: {fname} {lname}")
#Positional argument
#fname, lname -> parameter
# arguments -> K. , Mithu (Passed Value)
hello("K.", "Mithu")


# Arbitrary(Freedom) Arguments
# *args -> pack all and make a Tuple:
def funOne(*args):
    print(args)
    print(args[1]) # indexing

funOne("K.", "Mithu", 2022, False)


def funTwo(fname="K.", lname="Mithu"):
    print(f"Full Name: {fname} {lname}")

funTwo()
funTwo("Dhaka", "BD")

# Arbitrary Keyword Arguments
# **kwargs -> pack all and make a Dictionaries
def funThree(**kwargs):
    print(kwargs)
    print(kwargs['age']) # add key

funThree(fname="K.", lname="Mithu", age=25)


# *args and **kwargs 
def funFour(*args, **kwargs):
    print(args, kwargs)

funFour("K.", "Mithu", 2022, False, fname="K.", lname="Mithu", age=25)
funFour("K.", "Mithu", 2022) 
funFour() # pass empty Tuple & empty Dictinary


# Lambda function
# Anonymous function
# IIFE -> immediately invoked function expression 
def add(x,y):
    return x+y

addTwo = lambda x,y: x+y
print(addTwo(2,2))


############
################
#Built-in function

# map() function
def func(n):
    return n*n*n

l = [3, 4, 1, 0, 6]

# List/ Tuple/ Set
newL = list(map(func, l)) # function definition pass not call(func())
print(newL)

#//#comprehension
NewL = [n*n*n for n in l]
print(NewL)

# lambda function
lnewL = list(map(lambda n: n*n*n, l))
print(lnewL)
#//

L = ["k.", "Mithu", "UIU"]
L2 = list(map(list, L))
print(L2)

#######
# filter() function

fList = [1, 2, 3, 4, 5, 6, 7]

def funcFtr(n):
    return n%2 == 1

newfList = list(filter(funcFtr, fList))
print(newfList)

#lambda
newfListlbd = list(filter(lambda n: n%2==1, fList))
print(newfListlbd)

#########
# reduce() function
from functools import reduce
li = [1, 2, 3, 4, 5, 6]

def funcR(x, y):
    return x + y

sum = reduce(funcR, li)
print(sum)

# lambda
sum = reduce(lambda x, y: x+y, li)
print(sum)

#########
#######


