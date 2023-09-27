# Higher Order Function
# HOF -> Accepts function as argument or returns function

def hof(fn):
    print(fn.__name__)
    fn()

def greet():
    print("Hello World!")

def hello():
    print("Hello Bangladesh!")

#hof("K. Mithu") # Error

# hof(hello)
# hof(greet)

##

li = [1, 2, 3, 4, 5, 6]
newList =  list(filter(lambda x: x%2==1, li))
print(newList)


## Modified Higher Order Function
def myFilter(fn, l):
    newL = []
    for i in l:
        if fn(i):
            newL.append(i)
    return newL

newList = myFilter(lambda x: x%2==1, li)
print(newList)

#########
#########

def myFunc():
    def hello():
        print("Hello World!")
    
    return hello

f = myFunc()
print(f)
f()


########
# Wrapper Function
def myWrapper(fn):
    def test():
        print("I am from test! Before")
        fn()
        print("I am from test! After")
   
    return test


def greeTwo():
    print("Hello World!")

def wrapperUses():
    print()
    print("Wrapper function uses")
    print()

greeTwo = myWrapper(greet)
greeTwo()
print("........")
wrapUses = myWrapper(wrapperUses)
wrapUses()

#####
#######
# Decorators

# greeTwo = myWrapper(greet)
# greeTwo()

@myWrapper
def greeTest():
    print("Hello Decorators")

greeTest()

@myWrapper
def wrapTest():
    print("Test")

wrapTest()



