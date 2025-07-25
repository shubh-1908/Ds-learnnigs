  # functions

# syntax

# def function_name(parameter):
#     """"""docstring""""""
#     statement(s)
#     return expression




# 1

# def addnum(a,b):
#     c=a+b
#     print(c)
# addnum(2,3)    
# addnum(5,9 )    



# # 2

# def greet(name,age):
#     print(f"hi, I am {name},and I am {age} year old.")
# greet("shubham",24)    



# Local Scope Global Scope

# x=10
# def func():
#     x=5
#     print("local x:",x)
# func()
# print("Global x:",x)   



# Ananomous Function 

# square = lambda  x: x * x
# print(square(4))




# n = int(input("Enter the number: "))
# def fun(num):
     
#      n1,n2=0,1
#      print(n1,n2,end=" ")
#      for i in range(2,num):
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         print(n3, end= "  ")
# fun(10)


# def fun (n):
#    steps=0
#    while n > 0:
#       if n%2==0:
#           n=n//2
#       else:
#         n =n-1
#       steps +=1
#    print(steps)
# fun(15)   


def fun(n):
    steps = 0
    while n >= 10:
        temp = n
        sum_digit = 0 
        while temp > 0:
            sum_digit += temp % 10
            temp = temp // 10
        n = sum_digit    
        steps += 1
    print(steps)

fun(877)

