""" 
Dictionary
1. Dictionary annoted by {curly brackets}.
2. Dictionary are combination of multiple Keys:Values.
3. Dict are mutable.
4. Dictionary are heterogeneous.
5. Dictionary are ordered.
"""
"""
d = {1:10, 2:20, 3:30}
d[3] = 100
d[4] = 100 #Creatimg a new key value

print(d)

#Methods in dict
#1. .keys()
d = {"Ravi" : 80, "Rohan": 23, "Devraj" : 88}
print(d.keys())

#2. .values()
print(d.values())

#3. .items() -> both keys and values
print(d.items())

#4. .pop() -> Key and remove both key and values
d.pop("Rohan")
print(d)

#5. .get() -> agar key present hai in dictionary so we will get value  for that key either wise None or ANY MESSAGE.
print(d.get(5, "Not Found"))

#6. .update() -> merge two dictionaries.
a= {1:10, 2:20 ,3:30}
b= {4:40, 5:50, 6:60}
a.update(b)
print(a)
"""

d = {"Ravi": 70, "Abhishek": 88, "Rohan": 12}

# print(d.keys())

# sum = 0
# for key, value in d.items():
#     print(key)
#     sum+=value
# print(sum)



#Print student who scored more than 50
# for key, value in d.items():
#     if value >=50:
#         print(key)


# Find the student with the highest marks.
# highest = 0
# top = 0
# for name, marks in d.items():
    
#     if marks> highest:
#         highest = marks
#         top = name
# print(highest,top)

# Add bonus marks to every student.
for i in d:
    d[i] = d[i]+5
print(d)
