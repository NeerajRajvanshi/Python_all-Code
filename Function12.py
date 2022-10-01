
# Creating a Function 




# def name ():
#     print("welcome mr. Neeraj Ranjvanshi ")
    
    
# # Calling a Function 



# def name ():
#     print("welcome mr. Neeraj Ranjvanshi ")
# name ()




# LENTH OF F STRING FUNCTION



# def a_lenth_of(string):
#     return len(string)
# x = a_lenth_of("function")
# y = a_lenth_of("python")
# print("lenth of the string function",x)
# print("lenth of the string python is", y)


# def len_a(string):
#     return len(string)
# print("lenth of the string is punction", len_a("function"))
# print("lenth of string of python is ",len_a("python"))





# # Arguments 


# def My_Function (fname): 
#     print(fname+ " " + "kumar")
# My_Function("neeraj")
# My_Function("sanyam")
# My_Function("sachcchida")



# # Number of Argument 

# def my_number (fname , lname):
#     print(fname+ " " +lname)
# my_number("sanyam","srivasta")



# # Arbirraoy Argument Arye

# def my_function (*kids): 
#     print("the yougest child is "+ kids[3])
# my_function("Neeraj", "Rajvanshi", "softwere", "Devloper")



# # Keyword Argument

# def my_function (child3,child2, child1):
#     print("The yonyest child is " + child2)
# my_function(child1 = "Neeraj", child2 = "sanyam", child3 = "sachchidanad")




# # Arbitrary Keyword Arguments, **kwargs


# def my_function (**kid):
#     print("His last name is " +  kid["lname"])
# my_function ( fname = "shikha", lname = "singh ")




# # Default Parameter Value


# def my_function (country=  "India"): 
#     print( "I am from "  + country)
# my_function ( "America")
# my_function( "canada")
# my_function()
# my_function("rush")



# # passing a List Arument


# def my_function (food):
#     for x in food:
#         print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function ( fruits)
    
    
    


# # Return Values


# def my_function (x):
#     return 5 * x 
# print(my_function(3))
# print(my_function(5))
# print(my_function(7))
    
    
    


# # add two numbers


# def add( a,b):
#     c = a+b
#     return c

# result = add (5,7)
#h print(result)



# def fun_name(name,age):
#     print(name , age)
# fun_name('neeraj',19)



# def fun(*num):
#     for i in num:
#         print(i)
# fun("neeraj","kumar", "rajvanshi")
        
    
    
    


# words = ("hello","welcome","to", "N,R website")
# my_lisr = []
# for i in words:
#     my_lisr.append(len(i))
# print(my_lisr)



# def add(a,b):
#     c = a+b
#     return c 
# a = int(input("Enter the first number "))
# b = int(input("enter the second number"))
# z = add(a,b)
# print("additions",z)



# def evenOdd(x):
#     if (x%2==0):
#         print("even")
#     else:
#         print("odd")
# A = int(input("Enter the number"))
# evenOdd(A)




# def my_function(*raj):
#     for i in raj:
#         print(i)
# my_function("hollo", "mr.", "my name is neeraj ")




# def myFunction(**kwarge):
#     for key,value in kwarge.items():
#         print("%s==%s" % (key,value))
# myFunction(first= "geeks",mid= "for",last="geeks")





# def squre_value(num):
#     return num**2
# print(squre_value(5))
# print(squre_value(-5))





# def my_function(name,age):
#     print(name,age)
# my_function('neeraj', 20)



# def func1(*args):
#     for i in args:
# h        print(i)
# func1(20,40,60)
# print("printing valus")
# func1(80,100)



# def multiple(a,b):
#     additions = a+b
#     subtriction = a-b
#     return additions,subtriction
# result = multiple(40,10)
# print(result)


# # FUNCTION ARGUMENTS PARAMETER 


# # POSITIONL ARGUMENT 



# def add(a,b,c): 
#     d = a+b+c
#     print(d)
# add(10,30,40)


# def add(a,b,c):
#     d = a*b*c
#     print(d)
# add(30,40,50)



# def simpal(p,r,t):
#h     print("prinsiple", p)
#     print("rate", r)
#     print("time", t)
#     si = (p*r*t)//100
#     return si
# Result = simpal(20,40,50)
# print(Result)



# # DEFOULT ARGUMENT

# def add(a,b=40 ,c=30):
#     d = a+b+c
#     print(d)
# add(10,20,)


# def even(x):
#     if (x%2==0):
#         print("even")
#     else:
#         print("odd")
# A = int(input("enter the number"))
# even(A)
        


    
# num = int(input("enter the odd even number"))
# def odd_even(num):
#     if num%2== 0:
#         print("even")
#     else:
#         print("odd")
# odd_even(num)



# def simaple(a, b, c):
#     print("apple",a)
#     print("banana",b)
#     print("cherry",c)
#     d = a+b+c
#     return d
# s

 


# def fun(number):
#     if(number%2==0):
#         print(number)
#         return fun(number+1)
#     if(number>100):
#         return
#     else:
#         return fun(number+1)
# c=fun(1)
# print(c)




# def max_of_two (x,y):
#     if x>y:
#         return x
#     return y
# def max_of_three(x,y,z):
#     return max_of_two(x,max_of_two(y,z))
# print(max_of_three(3,6,-5))



# def sam(numbers):
#     total = 0
#     for i in numbers:
#         total = total+i
#     return total
# print(sum((8,2,3,0,7)))
        
        
        

# def multipaly(numbers):
#     total = 1 
#     for i in numbers:
#         total=total*i
#     return total 
# print(multipaly((8,2,-1,3,7)))



# def string_reverse(str1):
#     rstr1 = ''
#     index = len(str1)
#     while index>0:
#         rstr1+=str1[index -1]
#         index = index -1 
#     return rstr1
# print(string_reverse("1234abcd"))



# def factorial(n):
#     if n == 0:
#         return 1 
#     else:
#    h     return n* factorial(n-1)
# n = int(input("Enter a number to compute the factiorial:-"))
# print(factorial(n))




# def test_range(n):
#     if n in range(3,9):
#         print("%s is in the range"%str(n))
#     else:
#         print("the number is outside the given range")
# test_range(5)




# def unique_list(l):
#     x = []
#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x 
# print(unique_list([1,2,3,3,3,3,3,4,5,]))




# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True     
#     else:
#         for x in range(2,n):
#             if (n%x==0):
#               return False
#         return True
# print(test_prime(9))
        
    


# def is_even_num(l):
#     enum = []
#     for n in l:
#         if n%2==0:
#             enum.append(n)
#     return enum 
# print(is_even_num([1,2,3,4,5,6,7,8,9,]))




# def perfect_number (n):
#     sum = 0 
#     for x in range(1,n):
#         if n%x == 0 :
#             sum+=x
#     return sum==n
# print(perfect_number(6))



# def pascal_triangle(n):
#     trow = [1]
#     y = [0]
#     for x in range(max(n,0)):
#         print(trow)
#         trow=[l+r for l,r in zip(trow+y,y+trow)]
#     return n>1
#  pascal_triangle(6)
        
# input = ()
# items = [n for n in input().split("-")]
# items.sort()
# print("-".join(items))





# def printValues():
#     l = list()
#     for i in range(1,21):
#         l.append(i**2)
#     print(l)
# printValues()




# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn()+"/b>"
#     return wrapped
# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "/i"
#     return wrapped
# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
#h fgefff hello():
#     return l;fa"hello word"
# sint(hello())## returns "<b><i><u>hello world</u></i></b>       

# mycode = 'print ("hello")'
# code = """
# def mutiply(x,y):
#     return x*y
    
# print('multiply of 2 and 3 is: ',mutiply(2,3))
# """
# exec (mycode)
# exec (code)
        



# def test(a):
#     def add(b):
#         nonlocal a 
#         a+=1
#         return a+b
#     return add 
# func = test(4)
# print(func(4))



# def abc ():
#     x=1 
#     y=2 
#     str1= "w3resource"
#     print("python Exercises")
# print(abc.__code__.co_nlo





# L = 10
# def fun(n):
#     L = 5
#     print(L)
#     print(n,"I have printed")
# fun("This is me")
# print(L)
  
  

# L = 10 
# def fun(n):
#     m = 8
#     global L 
#     L = L+45
#     print(L,m)
#     print(n,"I have printed")
# fun("thi is me")




# def harry():
#     x = 20
#     def rohan():
#         global x 
#         x = 88 
#     print("before caling rohan", x)
#     rohan()
#     print("after calling rohan",x)
# harry()




# def a_len(string):
#     return len(string)
# x = a_len("javaTpoint")
# y = a_len("python")
# print("lenth of stirng javaTpoint :",x)
# print("lenth of stiring python :",y)





# def fun():
#     a = "javaTpoint "
#     b = "python "
#     c = a+b
#     return c
# x = fun()
# print(x,len(x))
# print(x)

    


# def fun(a):
#     while a<=5:
#         print(a)
#         a= a+1
      
# fun(1)





# def fun(a):
#     while a<100:
#         a = a+1
#         if a%2==0:
#             print(a,'even')
#         else:
#             print(a,'odd')
# fun(1)




# def fun():
#     for n in range(1,101):
#         count = 0 
#         a = n//2 
#         for i in range(2,(a+1)):
#             if n%2==0:
#                 count+=1
#                 break
#         if (count==0 and n>1):
#             print("%i" %n ,end=' ')
# fun()

     
     
                
                
# def fun(a):
#     while a<40:
#         b = a-6
#         if b%3==0:
#          print(b)
#         a = a+1
# fun(31)
    






# num = 1 
# odd_num = []
# while num:
#     if num%2!=0:
#         odd_num.append(num)
#     if num>=20:
#         break
#     num = num +1
# print("odd numbers", odd_num)







# def fun(num):
#     odd_num = []
#     while num<21:
#         if num%2!=0:
#             odd_num.append(num)
#         num = num+1
#     print("odd numbers",odd_num)
# fun(1)
        
        
        
        


# def guess_number(secret_no,chance,starting_chance):
#     while starting_chance <=chance:
#         guess_no = int(input("guess numbers"))
#         if guess_no == secret_no:
#             print("you win..!!!")
#             break
#         else:
#             print("you lost chance")
#             print("remaind chance is ",chance -starting_chance)
#         starting_chance+=1
#     else:
#         print("you failed")
# guess_number(7,3,1)







# n = int(input("enter the value of 'n' : " ))
# def fibonacci(a,b,sum,count):
#     print("fibooynacci series :", end=' ')
#     while count <=n:
#         print(sum,end=' ')
#         count+=1
#         a = b
#         b = sum
#         sum = a+b
# fibonacci(0,1,0,1)






# def square(num):
#     empty = []
#     for i in num:
#         empty.append(i**2)
#     return empty
# list = [45,52,13]
# result = square(list)
# print(result)



# def function(*num):
#     res = []
#     for i in num:
#         res.append(i.upper())
#     return res
# a_variable = "python is a most importend language"
# result = function(a_variable)
# print(result)



# def function(**my_square):
#     res = []
#     for key,value in my_square.items():
#         res.append([key,value])
#     return res
# result = function(first= 'python' ,secund='javascript', third='HTML')
# print(result)

