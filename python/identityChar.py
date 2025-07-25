# # char = input("Enter the char: ")

# # if char.isalpha():
# #     if char.lower() in 'aeiou':
# #         print("vowel")
# #     else:
# #         print("consonant")
# # elif char.isdigit():
# #     print("digit")
# # else:
# #     print("special char")



# # while loop  

# # sum of natural numbers


# n = int(input("enter the number:"))
# sum_ =0
# i=1
# while i <= n:
#     sum_=sum_ + i
#     i =i + 1
#     print("sum:",sum_)
# Sum of natural numbers up to n

# n = int(input("Enter the number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print(" sum ", sum)






# # Continue Statement

# x = 0
# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x)



# # Break Statement

# x = 1
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1


# # Print numbers from 10 to 1 using a while loop
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1



# # even numbers
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1






# # simple password checker

# correct_password = "0010"
# password = input("Enter password: ")
# while password != correct_password:
#     password = input("Incorrect. Try again: ")
# print("Access granted")        



# fibonacci series

# n = int(input("Enter the number: "))
# n1,n2=0,1
# print(n1,n2,end="")
# for i in range(2,n):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3, end="")

# n = 14
# steps=0
# while n > 0:
#     if n%2==0:
#         n=n//2
#     else:
#         n =n-1
#     steps +=1
# print(steps)


# num=877
# steps=0
# while num>=10:
#     temp=num
#     sum_digit=0 
#     while temp > 0:
#         sum_digit +=temp%10
#         temp=temp//10
#     num=sum_digit
#     steps +=1
# print(steps)        




    