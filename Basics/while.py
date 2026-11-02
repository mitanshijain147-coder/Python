"""
While Loop
Kaha se jana hai -> kab tak jana hai -> kaise jana hai
while jab tak yeh condition true hai:
    tab atk ye code chalega.
"""
# 1- 50 tak print krna hai using while loop.
"""
i = 1
while i<=50:
    print(i)
    i+=1
"""
# i = 10
# while i>=1:
#     print(i)
#     i-=1

# password=""
# while password!="Abhishek123":
#     password = input("Enter the password:")
# print("Access granted")

"""
n = int(input("Enter The number you want:"))
i = 1
while i<=10:
    print(i*n)
    i+=1
"""
"""
i=2
sum= 0
while i<=20:
    print(i)
    sum +=i
    i+=2
print(f"sum of even numbers from 2 to 20 is {sum}")
"""
# n = int(input("Enter The number"))
# a=0
# while n>0:
#     last=n%10
#     a =a*10 + last
#     n = n//10
# print(a)

# n = int(input("Enter The number"))
# a=0
# count=0
# while n>0:
#     last=n%10
#     count+=1
#     a =a*10 + last
#     n = n//10
    
# print(a)
# print(count)

#Number is Armstrong 
n = int(input("Enter the Number"))
length = len(str(n))
temp = n
sum = 0
while n > 0:
    last= n%10
    sum = sum + last**length
    n = n//10
if sum == temp:
    print("Armstrong number")
else :
    print("Not Armstrong")