#1(05-10 practice)
#  N = int(input("Enter the integer :"))
# count = 0
# for i in range (1, N+1):
#     if i%3==0 and i%5==0 :
#         count+=1
# print(f"count :{count}")

#2
# n = int(input("Enter the number:"))
# fact= 1
# for i in range(1,n+1):
#     fact*=i
# print(f"Factorial of {n} is {fact}")

#3 strong number
# n = int(input("Enter the number:"))
# temp = n
# sum = 0
# while n>0:
#     last = n%10
#     fact = 1
#     for i in range(1,last+1):
#         fact *= i
#     sum+=fact
#     n= n//10
# if sum == temp:
#     print("Strong number")
# else:
#     print("Not a strong")

#4
# n = int(input("Enter the number:"))
# sum = 0
# for i in range (1,n+1):
#     if i%2 != 0:
#         sum+=i
# print(sum)

#5 06-10
#Fibonacci series
# n = int(input("Enter the number:"))
# n1 = 0
# n2 = 1

# for i in range (n):
   
#     print(n1,end= " ")
#     num = n1 + n2
#     n1 = n2
#     n2 = num
    
#6
# n = input("Enter the string:")
# count=0
# for i in n:
#     if(i in "AEIOUaeiou"):
#         count+=1
# print(f"No. of Vowels present in the string :{count}")

#7
# s = input("Enter The String:")
# ch = input("Enter the character to search:")
# count=0
# for i in s:
#     if i == ch:
#         count+=1
# print(f"{ch} appears {count} times is {s}")

#08-10
# n= int(input("Enter the number:"))


# for digit in range(0,10):
#     count_digit = 0
#     temp = n
    
#     while temp>0 :
#         last_digit = temp%10
#         if last_digit == digit:
#             count_digit+=1
#         temp//=10
#     if count_digit>0:
#         print(f"For {digit} -> {count_digit}")

#9
n = int(input("Enter The number:"))
temp = n
s = 9
while temp>0:
    digit= temp%10
    if digit<s:
        s= digit
    temp//=10
print(f"chota digit in {n} is {s}")