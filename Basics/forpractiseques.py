#30-09
#1
# p = 0
# a = 0
# for i in range(1,8):
#     At = input(f"Enter the attendence of student for {i} day P or A:")
#     if At=='P':
#         p+=1
#     elif At=='A':
#         a+=1
# print(f"The student was present for {p} days")
# print(f"The student was absent for {a} days")

#2
# p = 0
# f = 0
# for i in range(1,11):
#     I = int(input(f"Tell Inspection for {i} product :"))
#     if I==1:
#         p+=1
#     elif I==0:
#         f+=1
# print(f"Number of products passed are {p}")
# print(f"Number of products failed are{f}")

#3
# total =0
# count=0
# for i in range(7):
#     s= int(input(f"Enter the savings for day{i+1}: "))
#     total+=s
#     if s> 500:
#         count+=1
# print(f"Total  savings is {total}")
# print(f"{count} days the savings were above 500")

#4
#Total Electricity Consumption
# total = 0
# count=0
# for i in  range (1,8):
#     E= int(input(f"Enter the Electricity Consumption of day {i}:"))
#     total+=E
#     if E>10 :
#         count+=1
# print("Total Units is ",total)
# print("Days the consumption was more than 10 is",count)

#5
# count = 0
# p = 0
# for i in range(10):
#     At = input(f"Enter the Attendence for day {i+1}:")
#     if At=='P'or At=='p':
#         count+=1
# p = (count/10)*100
# if p>75 :
#     print(f"Yes Students attendance is above 75%, total is {p}")
# else:
#     print(f"No students attendance is not 75%, total is{p}")


#01-10

#1
# count = 0
# N = int(input("Enter The Interger:"))
# for i in range (1,N+1):
#     if i%3 == 0:
#         count +=1
# print(f"Total numbers from 1 to {N} which are divisible by 3 are {count}")


#2
# n= int(input("How many numbers you want to compare:"))
# greatest = 0
# for i in range (1,n+1):
#     num= int(input("Enter the number"))
#     if num>greatest:
#         greatest = num
# print (f"Greatest number is{greatest}" )

#3
# N = int(input("How many numbers you want to enter:"))
# avg = 0
# sum = 0
# for i in range (N):
#     n=int(input("Enter the number :"))
#     sum+=n
# avg = sum/N
# print("Average is",avg)


#4
# N = int(input("Enter the number:"))
# fact= 0
# for i in range(1,N):
#     if N%i == 0:
#         fact+=i
# if fact == N:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

# #5
# N= int(input("Enter the number:"))
# for i in range (1, N+1):
#     if i%10 == 0:
#         print(i)

#02-10
#1
# n = int(input("Enter the number:"))
# esum=0
# osum =0
# diff = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         esum+=i
#     else:
#         osum+=i
# diff = esum - osum
# print(f"Difference between even and odd sum is {diff}")


#2
# n = int(input("How many numbers you want to enter:"))

# s = float("inf")  
# g= 0
# for i in range (1,n+1):
#     num= int(input(f"Enter the {i} number :"))
#     if num>g:
#         g = num
#     if num<s:
#         s= num
# print(g)
# print(s)

#3
# n = int(input("How many numbers you want to enter:"))
# s = float("inf")
# for i in range (1, n+1):
#     num= int(input(f"Enter th number {i}:"))
#     if num<s :
#         s = num
# print(f"Smallest number is{s}")
    
#4
# N = int(input("How many numbers yu want to enter:"))
# count = 0
# for i in range (N):
#     num = int(input(f"Enter th number {i+1}:"))
#     if num % 10 == 0:
#         count+=1
# print(f"{count} Digits contain zero")

#5
# N = int(input("Enter the number:"))
# count = 0
# for i in range (1,N+1):
#     last = i%10
#     if last == 5:
#         count+=1
# print (count)

#6
N = int(input("Enter the Number"))

