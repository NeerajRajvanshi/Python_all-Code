# counter = 0 
# while counter < 5 :
#     print ("navgurukul")
#     counter = counter + 1




# counter = 20 
# while counter < 40:
#     a = counter - 19 
#     print (a)
#     counter = counter + 1


# counter = 1 
# sum = 0 
# while counter <= 100:
#     print (counter)
#     sum = sum + counter
#     counter = counter + 1
# print (sum)


# a = -1
# while a >= (-10):
#   print(-a)
#   a = a -1





# a =int(input("enter the first number"))
# b = int(input("enter the secound number"))
# n = 0 
# for i in range(1,b+1):
#     n = n + a 
# print (n)



 
# a =int(input("enter the first number"))
# b = int(input("enter the secound number"))
# n = 0 
# for i in range(1,a+1):
#     n = n + b 
# print (n)



# a=int(input("enter : -"))
# for i in range(a):
#     print(i)
#     v=i+(i+1)
#     print(v)


# from tokenize import Number


# amt = 0  
# num = int(input("enter the  unit bill number"))
# if num <= 100 :
#     amt = 0
# if num > 100 and num <=200:
#     amt = num - 100 * 5
# if num > 200: 
#     amt = 500 + num - 200 *10
# print ("amount to pay ",amt)
 


# x = 5
# while x < 15 :
#     if x % 2 ==0:
#         print ("even",x)
#         break
#     print (x)
#     x = x +1


# x = 5 
# while x < 15 :
#     if x % 2 ==0:
#         x = x + 1
#         continue
#     print ("odd",x)
#     x = x +1


# i =  0
# while i <= 3:
#     print ("outer code",i)
#     i = i + 1
#     j = 1 
#     while j <= 5:
#         print ("inner code",j)
#         j = j + 1
# print ("reast of  the code")


# st = "Geekyshows"
# for ch  in st:
#     print (ch,end=" ")
# print ("reast of the code")




# st = "Geekyshows"
# for ch  in st:
#     print (ch)
# print ("reast of the code")


# a = range (10, 0 , -1)
# for i in a :
#     print (i)



# counter = 0 
# string = "navgurukul"
# while counter < len(string):
#     if string [counter] == "g":
#         break 
#     print (string[counter])
#     counter= counter+1



# st =input("enter your name")
# n = len (st)
# for i in range (n):
#     print (i,"=",st[i])



# st =input("enter the number.")
# for i in st:
#     print (i)
# else:
#     print("Rest of the code.")



# for i in range(2):
#     print ("outer of code",i)
#     for i in range (3):
#         print ("inner of the code")
    

# i = 0 
# while i < 3 :
#     j = 0 
#     while j < 5 :
#         print ("outer",i)
#         i = i + 1
#         print ("inner",j)
#         j = j +1
    
# a = 0
# while(a<6):
#     b = 0
#     while(b<6):
#         if (a == b):
#             break
#         print ('*'),
#         b = b + 1
#     print ('')
#     a = a + 1


# i =  0 
# a = "geeksforgeeks"
# while i < len(a):
#     if a [i] == 'e' or a [i] == 's':
#         continue

#     print ("courent letter",a [i])
#     i = i +1

# a=int(input("enter : "))
# l=[]
# for Number in range (1, a):
#     count = 0
#     for i in range(2, (Number//2 + 1)):
#         if(Number % i == 0):
#             count = count + 1
#             break

#     if (count == 0 and Number != 1):
#         l.append(Number)
# print("neareast prime number is : - ",l[-1])


# secret_number = 9 
# chance = 3
# starting_chance = 1
# while starting_chance <= chance:
#     guess_number = int(input("guess numnber "))
#     if guess_number == secret_number:
#         print ('you win !!')
#     else:
#         print ("you lost chance")
#         print ("remind chance is ",chance-starting_chance)
#         starting_chance = starting_chance + 1
# else:
#     print ("you faield")





# n = int(input("inter the number"))
# num = 1
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(num,end=" ")
#         num = num + 1
#     print()



# for row in range(8):
#     for col in range(5):
#         if ((col == 0 or col == 4) and (row !=0)) or (row ==0 or row ==4) and (col>0 and col<4):
#             print ("*",end=" ")
#         else:
#             print (end="  ")
#     print()




# for row in range(7):
#         for col in range(5):
#             if (col== 0 or col == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 3 or row == 6 ) and (col >0 and col <4 )):
#                    print ("*",end=" ")
#             else:
#                 print (end="  ")
#         print()
        




# for row in range (6):
#     for col in range(4):
#         if  (col == 0 and (row !=0 and row !=5)) or ((row == 0 or row == 5) and(col !=0)):
#             print ("*",end=" ")
#         else:
#             print (end="  ")
#     print ()







# x=int(input("enter your number"))
# x1=x%1000
# x2=x1%100
# x3=x//1000*100
# x4=x3+x2
# print(x4)





# a=int(input("entet the number "))
# b=int(input("enter the number "))
# c=int(input("entet the number"))
# d=int(input("enter the number "))
# if a<b and a>c and a>d or a<c and a>d and a>a or a<d and a>b and a>c:
#     print(a)
# elif b<c and b>d and b>a:
#     print(b)          
# elif  b<d and b>a and b>c or  b<a and b>c and b>d:
#            print(b)
# elif  c<d and c>a and c>b  or  c<a and c>b and c>d:
#            print(c)
# elif  c<b and c>c and c>d or   d<a and  d>b and d>c:
#            print(d)
# elif  d<b and d>c and d>a or  d<c and  d>a and d>b:
#            print(d)







# a=int(input("entet the number "))
# b=int(input("enter the number "))
# c=int(input("entet the number"))
# if a>b and a>c:
# 		print(a)
# elif b>a and b>c:
# 		print(b)
# else:
# 		print(c)		
		




# for i in range(1,16):
#     for j in range(1,16):
#         print(i*j,end=" \t ")
#     print()





# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()





# a=int(input("enter number"))
# a= a%100
# a2= a%10
# a3=a%100
# a4= a3//1*10
# a5= a//1000*1000
# a6= a5+a4+a2






# a=int(input("enter number"))
# b=a//1000
# c=a%1000
# d=c%100
# b=a//1000*100
# g=b+d
# print(g)
# f=c//100
# g=g*10
# j= g+f
# print(j)




# for row in range(6):
#     for col in range(5):
#         if (col== 0 or col== 4) and (row !=0) or (row== 0 and col> 0 and col<4) or (row==3):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()



# num = int(input("enter the any number"))
# for i in range(num):
#     for j in range(i+1):
#         print(num-j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()


# a =1 
# b =0 
# while a <=100:
#     print(a)
#     b = a + b
#     a = a+1
# print(b)



# a = 1
# sum=0
# while a <=100  :
#     print (a)
#     sum=a+sum
#     a=a+1
# print(sum)



# a = int(input("enter the any  number"))
# for i in range(a):
#     for j in  range(i+1):
#         print(j+1,end=" ")
#     print()





# b = int(input("enter the any nubmer"))
# for i in range(b):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#    







# RAma = "\103"
# print(RAma)



# bak = "heelo\nhii"
# print(bak)




# aak = "ab\ba"
# print(aak)





# logic = "\101\109\111\114\120"
# print(logic)




#   this is my calculater
  
  
   

# first=input("enter the first number")
# operator=input("enter operator (+,-,/,*,%)")
# second=input("enter the second number ")
# first=int(first)
# second=int(second)
# if operator=="+":
# 	print(first+second)
# elif operator=="-":
# 	print(first-second)
# elif operator=="*":
# 	print(first*second)
# elif operator=="/":
# 	print(first/second)
# elif operator=="%":
# 	print(first%second)
	



# #   this is my calculater
  
  
  
# x = input("enter your math problme")
# print("your answer is :",eval(x))

# n = int(input("enter the number"))
# for i  in range(n):
#     if i==2 or i==3:
#         continue
#     print(i)






# a=[0,1,5,4,0,0,4,3,0]
# i=0
# sum=[]
# sum2=[]
# while i<len(a):
# 	if a[i] == 0:
# 		sum=sum+[a[i]]
# 	else:
# 		sum2=sum2+[a[i]]
# 	i=i+1
# print(sum2+sum)



# list2 = [20,30,40,]
# list3 =[]
# for i in list2:
#     list3.append(i)
# list2.clear()
# print(list2)
# print(list3)





# a=[0,1,5,4,0,0,4,3,0]
# i=0
# sum=[]
# sum2=[]
# while i<len(a):
# 	if a[i%2] == 0:
#          sum = sum +[a[i]]
#     else:
#      sum2=sum2+[a[i]]
# 	i=i+1
# print(sum2+sum)



# a = int(input("inter the first number"))
# b = int(input("enter the secund number"))
# c = int(input("enter the third number"))
# p = (a+b+c)
# s =  p/2
# area = (s*(s-a)*(s-b)*(s-c))
# print(area)
# print(p)
# print(s)



# car_game =  ("")
# while True:
#      car_game  = input(">>").lower()
#      if car_game  == "start":
#           print("Car started...")
#      elif car_game  == "stop":
#          print("game over")
#      elif car_game == "help":
#           print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#           """)
#      elif car_game == "start":
#          print("car alraedy started")
#      elif car_game == "stop":
#          print("car alraedy stoped")
#      elif car_game  == "quit":
#          print("game over")
#          break
#      else:
#                print("Sorry, I don't understand that")


            
            
# command=""
# is_car_started = False
# while True:
#     command=input('>').lower()
#     if command=='start':
#         if is_car_started == True:
#             print("Car started already")
#         else:
#             is_car_started = True
#             print("Car started")
#     elif command=='stop':
#          is_car_started = False
#          print("Car stopped already")
#     elif command=="help":
#         print('''
# start-to start the car
# stop-to stop the car
# quit-to exit
#         ''')
#     elif command=='quit':
#         break
#     else:
#         print("I don't understand that")
        
        



# a = 0 
# sum = 0 
# while a <=10 :
#     b = int(input("enter the number"))
#     sum = sum +1 
#     a = a + 1
#     print(sum)
     

