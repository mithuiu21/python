#Sets

mySet = {"K. Mithu", 2, 3, True, False}
print(mySet)

# Set is using for revoming duplicate entry 
setOne = {20, 20, 20}
print(setOne)

# Empty set{}
setTwo = set()
print(setTwo)
setTwo = set("abcdef")
print(setTwo)


# Set Operations
set1 = set("abcd")
set2 = set("adpq")

# Intersection
is_set =  set1 & set2
print(is_set)

# Union
u_set = set1 | set2
print(u_set)

# - 
min_set = set1 - set2
print(min_set)

# But Not : common element won't come
bn_set = set1 ^ set2
print(bn_set)
