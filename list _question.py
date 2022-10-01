

#LIST APPEND()


# months = ['January', 'February', 'March'] 
# months.append('April') 
# print(months)



#LIST INSERT()

# list = [1, 2, 3,4] 
# list.insert(2,40) 
# print(list)



#LIST EXTEND()

# list1 = ["hello","neeraj","kumar"]
# list2 = [1,2,3,4,5,6,7,8,]
# list1.extend(list2)
# print(list1)


#LIST INDEX

# months = ['January', 'February', 'March', 'April', 'May'] 
# b = months.index('March')
# print(b)



# LIST RECERESED



# prices = [589.36, 237.81, 230.87, 463.98, 453.42] 
# price_max = max(prices) 
# print(price_max)



#LIST LENGHT


# list_1 = [50.29] 
# list_2 = [76.14, 89.64, 167.28] 
# print('list_1 length is ', len(list_1)) 
# print('list_2 length is ', len(list_2))





#LIST COUNT



# fruits = ['cherry', 'apple', 'cherry', 'banana', 'cherry'] 
# x = fruits.count("cherry")
# print(x)




#LIST POP


# fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple']
# fruits.pop(2)
# print(fruits)





#LIST REMOVE




# fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple']
# fruits.remove("banana")
# print(fruits)





#LIST REVERS


# fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple']
# fruits.reverse()
# print(fruits)



#LIST COPY


# fruits = ['apple', 'banana', 'cherry', 'orange']
# x = fruits.copy()
# print(x)




#LIST EXTEND


# hello = [1,2,3,4,5,6,7,8,9,]
# hello.extend([10,11,12,])
# print(hello)





#LIST SORT


# fruits = ['cpple', 'yanana', 'cherry', 'orange', 'aineapple']
# fruits.sort()
# print(fruits)




#LIST CLEAR


# fruits = ['cpple', 'yanana', 'cherry', 'orange', 'aineapple']
# fruits.clear()
# print(fruits)



#LIST INDEXING


# thislist = ["apple","banana","chery",]
# raj = (thislist[-1])
# print(raj)






# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)

# print(thislist)


#LIST FOR LOOP 


# this= ["hello","ram","how","are"]
# for  i in range(len(this)):
#     print(this[i])




# fruits = ["hello","apple","nanana"]
# newlist =[]
# for x in fruits:
#     if "a" in x:
#         newlist . append (x)
#     print(newlist)



# list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# new_list1= []
# for i in list1:
#     new_list1 .append(i+1)
# print(new_list1)





#LIST COMREHENSION



# list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# new_list2 = [i+1 for i in list2 ]
# print(new_list2)

# st = [i + 1 for i in range(20)]
# print(st)





# list = []
# for i in range(20):
#     if i%2 == 0 :
#         if i%3 == 0:
#             list.append(i)
# print(list)
# print()


# list=[i for i in (20) if i%2==0 if i%3==0]
# print("new list",list)

# list = [i if i%2==0 else "neeraj" for in range(10)]
# print(list)


# a = [1,2,3,4,5,6,7]
# print([i for i in a if i % 2 == 0])




# a = [1,2,3,4,5,6,7]
# li1= []
# for j in a:
#     if j%2 == 0:
#         li1.append(j)
# print(li1)
    




#LIST SORT ()


# list1= [1,2,3,4,5,5,6,7,8,9,10]
# list2= list(set(list1))
# list2.sort()
# print(list2[-2])


#LIST SAM()


# list1 = [1,3,4,5,6,7,8,9,]
# print (sum(list1))



#LIST MIN()


# list = [1,2,3,4,55,6,78,8,]
# print (min(list))



#
#LIST MAX ()

# list = [1,2,3,4,55,6,78,8,]
# print (max(list))



#LIST DEL()


# list = [1,2,3,4,5,6,7,8,9,]
# del list [2]
# print(list)





# num = [i for i in range(1,10,2)]
# print(num)




#CONORT LIST []

# str = "hi,hello , ABC, DEF"
# rosted = str. split(", ")
# print (rosted)



#INT CONORT LIST


# int = 12345
# str = [i for i in str(int)]
# print(str)





# list = ["got","cot","dog"]
# for i in range(len(list)):
#  print("banshi","=",list[i])



#COMPREHENSION LIST


# List = [[10,20],[25,30]]
# flat = []
# for i in List:
#     for item in i:
#         flat.append(item)
# print(flat)




#LIST JOIN



# st = ["hello","word", "python","is","awesom"]
# st3 = " " . join(st)
# print(st3)





# my_dict = {"a,":1,"b":2,"c":3,"d":4}
# print(my_dict)

# key_list = list(my_dict.keys())
# print(key_list)

# value_list = list(my_dict.values())
# print(value_list)




# num = list(range(8))
# print(num)




#SAB LIST KA SUM

# List = [[10,20],[25,30],[5,3,7]]
# flat = []
# for i in List:
#     for j in i:
#         flat.append(j)
# print(flat)
# print(sum(flat))




#LIST ADD 


# a = [1,2,3,] ,[4,5]
# print(a)
# b = list(a)
# print(b)
# a[0][0]=35
# print(a)





# grocery_list = ['flour','cheese','carrots']
# for i in grocery_list:
#     print(i)
    
    
    
    
    
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# n . insert(0,[])
# print(n)







# List = [[10,20],[25,30],2,3,[5,3,7]]
# flat = []
# for i in List:
#     if i == int():
#         flat.append(i)
#     else:
#         for  j in i:
#             flat.append(j)
# print(flat)

 
 
 
# even_nums = []
# for x in range(21):
#     if x%2 == 0:
#         even_nums.append(x)
# print(even_nums)

 
 


# list = [ "hello","riya singh","how are you"]
# list2= [n for n in list if "a" in n]
# print(list2)
 
 



# list3 = [chr(i) for i in range(65,91)]
# print(list3)




# list_NR = {1:"one",2:"two",3:"three",4:"four"}
# for N,R in list_NR . items():
#     print("key =",N , "value=",R)


# list4 = {1:"one",2:"tow",3:"three",4:"four"}
# for i  in list4 . items():
#     print(i)

 
 
 
 
 


# x = [ x ** 2 % 5 for x in range(1,100)]
# print (x)
 



# movis  = ["star wars","Ghandhi","casablance","shawshank",
#           "gonewith the winth","to kill a mockingbil","killer"]
# gmovies = []
# for title in movis:
#     if title.startswith("s"):
#           gmovies.append(title)
# print (gmovies)
 
 

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list.append("dhruv")
# print("length of the list is ", len(names_list))
# print(names_list)



 
 
 
 
 
#  list = [i for i in range(1,11)]
# # print(list)

 
 


# list = [i for  i in range(21) if i%2==0 ]
# print(list)

 
 
 
 

# from turtle import title


# movies = [("Minions thed Rise of Gru ",2022),("Elivi",2021),
#           ("The black phone",2021),("kGF",2022),("Dangal",2019)]
# pre2k = [title for (title,year)in movies if year<2022 ]
# print(pre2k)

 


# list4 = [ 10,20,30,10,40,20,50,60]
# result = []
# for i in list4:
#     if i not in result:
#         result. append(i)
# print (result)



# l = []
# if not l:
#     print("list is empty",l)



# original_list = [10,20,30,40,50]
# new_list = list(original_list)
# print (original_list)
# print (new_list)



# color = ["red","green","block","white","yellow"]
# color = [ x for (i,x) in enumerate (color) if i not in (0,4,5) ]
# print(color)



# color = ["red","green","block","white","yellow"]
# del color[0]
# print(color)


