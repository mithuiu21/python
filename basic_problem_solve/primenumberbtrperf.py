import math

def is_primeOne(n=1013):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

def is_primeTwo(n=1013):
    if n == 2:
        return True # 2 is prime
    if n % 2 == 0:
        return False # all even numbers except 2 are not prime
    if n < 2:
        return False # numbers less than 2 are not prime
    prime = True
    for x in range(3, n, 2):
        if n % x == 0:
            prime = False
            return prime
    return prime


## timeit(): performance analysis

import timeit
t1 = timeit.timeit(is_primeTwo)
t2 = timeit.timeit(is_primeOne) # better performance

print(t1, t2, t1/t2)


