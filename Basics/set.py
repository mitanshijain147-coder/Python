"""
SETS
1. Sets are annoted by {} or set().
2. Stores only unique elements and removes duplicate ones.
3. Sets are unordered that means there is no indexing in sets.
4. Sets are Hetrogeneous.
5. Sets are Semi-Mutable.
"""

#s = set() #Empty set
# s = {1,2,3,4,5,2}
# print(type(s))
# print(s)

# #List to SET
# L= [1,1,2,3,4,5]
# print(set(L))

"""
SET METHODS 
"""
# s = {1,2,3,4}
# #1. .add() -> adds an element to set.
# s.add(5)

# #2. .remove -> remove an element if the element didn't exists we will get an KEYERROR
# s.remove(3)
# print(s)

# #3. .discard() -> will not show  any erreo if the element is not present in set.
# s.discard(100)
# print(s)

""" SET Operations """
s1 = {1,2,3,4}
s2 = {4,5,6,7,8}

#1. .union() -> Merge both the sets.
print(f"UNION -> {s1.union(s2)}")
print(f"UNION -> {s1|s2}")

#2. .intersection() -> Common elements.
print(f"INTERSECTION -> {s1.intersection(s2)}")
print(f"INTERSECtTION -> {s1 & s2}")

#3. .difference() -> Elements present in one set but not in another.
print(f"DIFFERENCE == -> {s1.difference(s2)}")
print(f"DIFFERENCE == -> {s2.difference(s1)}")
print(f"DIFFERENCE -> {s1 - s2}")

#4. .symmetric_difference -> all elements except the common one.
print(f"SYMMETRIC -> {s1.symmetric_difference(s2)}")
print(f"SYMMETRIC -> {s1 ^ s2}")


#FROZENSET makes any set with of fixed elements we cannot add element and cannot remove one.
s = frozenset([1,2,3,4,5])
s.add(6)
print(s)