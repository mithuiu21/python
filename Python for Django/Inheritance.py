# Object Oriented Programming
# Inheritance

class A:
    def __init__(self, name): 
        self.name = name

    def hello(self):
        print("Hello from class A")    


obj = A("K. ")
obj.hello()


class B(A):
    def hello(self):
        print("Hello from class B")
    pass

objTwo = B("Mithu")
objTwo.hello()

###########
#############
# Overriding
class x():
    def __init__(self, name): #constructors
        self.name = name
       
    
    def skill(self):
        print("Python")

class y(x):
    def __init__(self, name, job):
        x.__init__(self,name)
        self.job = job

    def activity(self):
        print(f"{self.name} is a {self.job}")


myObj = y("K. Mithu", "Engineer")
myObj.activity()


## super() method

class z(x):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

    def activity(self):
        print(f"{self.name} is a {self.job}")


mySuperObject = z("K. Mithu", "Engineer")
mySuperObject.activity()


###########
###########
#Multiple Inheritance and Multilevel Inheritance in python

class K:
    def __init__(self, city):
        self.city=city
    
    def cityName(self):
        print(f"{self.city} is my home town")

class N(K):
    def __init__(self, city, cname):
        super().__init__(self)
        self.cname = cname

    def cityName(self):
        print(f"{self.cname} is in {self.city} division")


class D(N):
    pass

mycObj = D("Khulna", "Narail")
mycObj.cityName()
#print(dir(mycObj))

##############
###################
# Method Resolution Order (MRO)  
class P:
    def __init__(self, cname):
        self.cname=cname
    
    def cityName(self):
        print("Hello from P")

class Q:
    def __init__(self, area):
        self.area = area

    def cityName(self):
        print("Hello from Q")


class R(P, Q):
    def __init__(self):
        pass

    def cityName(self):
        print("Hello from R")

myMRO = R()
print(R.__mro__)
myMRO.cityName()


# Constructor in Multiple Inheritance
class P:
    def __init__(self, cname):
        self.cname=cname
    
    def cityName(self):
        print("Hello from P")

class Q:
    def __init__(self, area):
        self.area = area

    def cityName(self):
        print("Hello from P")
class R(P, Q):
    def __init__(self, cname, area):
        P.__init__(self, cname)
        Q.__init__(self, area)
        
    def hello(self):
        P.cityName(self)
        Q.cityName(self)
        print(f"{self.cname} and {self.area}")


myCMI = R("Khulna", "Narail")
myCMI.cityName()

###############
###################

# Meta Class => Class of Class
# Everything is object


myStr = "Dhaka"
myNum = 20
myDict = {'name': "KMithu"}
myList = [1, 2, 3]

print(type(myStr))
print(type(myNum))
print(type(myDict))
print(type(myList))


# type is a metaclass
class A:
    pass

metaObj = A()
print(type(metaObj))
print(type(A))



# https://www.datacamp.com/community/tutorials/python-metaclasses




