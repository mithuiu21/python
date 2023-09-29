# Crate oop.py
#.....................
def Add(x, y):
    return x + y

pi = 3.1416


class A:
    def __init__(self):
        print("Object of class A")

#......................................


## Import Statement
import oop

print(oop.Add(2,3))

print(oop.pi)

obj = oop.A()

#............................................. 

## From Statement
print(dir(oop))

from oop import Add, pi, A
# for All
from oop import *

print(Add(20, 20))

#..........................
## Directory as Module
#myModule/mmOOP -> 
from myModule.mmOOP import sum

print(sum(1, 2))
#........................................
# For Module loaded we create __init__.py in myModule
# print("Module Loaded ...")



