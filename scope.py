
# Scope
# A Variable is only available from inside the region it is created. This is called scope.

# function inside function
def myfunc():
    x = 20
    def myinnerfunc():
        print(x)
    
    myinnerfunc()

myfunc()

####
#####
# variable created outside of a function is global and can be used by anyone:
x = 10

def myfunc():
    print(x)
myfunc()

print(x)

####
# Global keyword

def myfunc():
    global x
    x = 20

myfunc()

print(x)

