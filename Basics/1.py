# #name = "Harsh"
# #age =24
# #two ways of using variables inside print statement
# print("Hello your name is",name,"and your age is",age)
# print(f"hello your name is {name} and your age is {age}")
# a = int(input("Enter The first Number"))
# b = int(input("Enter The Second number"))
# print("Addition is :",a+b)
# print("Substraction is:".a-b)
# print("Multiplication is :",a*b)
# print("Division is:",a/b)
# #Take input of three numbers P,R,T and calculate simple interest
# P= int(input("Enter The Amount"))
# R=float(input ("Enter the Interest"))
# T=int(input("Enter The Time"))
# I=(P*R*T)/100
# print("Simple Interest Is:",I)
# #Now calculate compound interest 
# ci= P*()
# #Assignment operator
# count = 0
# count += 1
# #Comparison
# a= 12
# b = 12
# #(==, !=, <, >, >=, <=)
# print(a>b)#False
# print(a==b)#True
# print(a>=b)#True
# print(ord("A"))
# print("5">"4")#True
# #Logical operators
# #(and, or , not)
# #and operator demand only one thing that all the comparisons must be true than only i will
# #provide the result as true
# print(12==12 and 34!=35)
# #or operator demands anyone comparison must be true then only i will provide true
# print( 12==13 or 45!=45 or 5==5)
# #not operator it converts true to false and false to true
# print(not 12==12)#False

# #Control statement
# age = int(input("tell your age"))
# if age>=18 :
#     print("You can vote")
# else:
#     print("You cannot vote")
# #if elif ladder
# money =int(input("Whats the value:"))
# if money ==100:
#     print("Sandwitch")
# elif money ==200:
#     print("Chole kulche")
# elif money ==500:
#     print("Full coarse meal")
# elif money ==50:
#     print("Panipuri")
# else:
#     print("Lays")

# #Accept two numbers and print the greatest among them
# num1 = int(input("Enter The first number"))
# num2 = int(input("Enter The second number"))
# if num1>num2 :
#     print("The Greatest of two numbers is",num1)
# elif num1==num2 :b

#     print("Both are Equal")
# else :
#     print("The Greatest of two numbers is ",num2)

#age = int(input("Enter the age:"))
#if age<5:
#   print("Ticket is free")
#elif age>=5 and age<=17 :
#   print("Ticket is 100")
#elif age>18 and age<=59:
#    print("Ticket is 200")
#else :
#   print("ticket is 120")
n =int(input("Enter The Number"))
if n>0 :
    if n%2 ==0:
        print("Positive and even")
    else:
        print("positive and odd")
elif n<0 :
    if n%2 ==0:
            print("Negative and even")
    else:
         print("Negative and odd")
else:
     print("Zero")