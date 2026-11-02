#Data structures
"""
List
1. Square Brackets -> List[]
2. Heterogeneous Data structure(a list can store different data types together).
3. List allows storing duplicate values.
4. List are ordered - because they have indexing and indexing starts from 0.
5. List are mutable ( we can change any value anytime and anywhere).
"""
#marks = [] #Empty List
"""marks = [80,65,88,90,75, "Abhishek", 3.14, True, 2+1j]
print(marks)
print(marks[3])#65
print(marks[1:6])# goes from index 1 to 5
marks[3] = "Modiji"
"""
#Traversing 
# a = [10,20,30,40,50]
# for i in a :
#     print(i)

""" Agar kisi keyword ke aage "." nahi laga that is a function 
agar laga hai toh METHOD hai"""

#Methods in List
#1. .append() add the value at the last of list.
marks = [10,20,30,40,50]
marks.append(90)
print(marks)

#2. .extend()
marks2 = [60,70,80]
marks2.extend(marks)
print(marks2)

#3. .insert(index,value)
marks.insert(3,90)
print(marks)
marks.insert(6,100)
