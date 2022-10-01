
import sys

list_memory = [1,2,"ram","shyam",True,"sanyam"]
tuple_memory = (1,2,"ram","shyam",True,"sanyam")
print("size of list momory ",sys.getsizeof(list_memory))
print("size of tuple memory",sys.getsizeof(tuple_memory))






# tuple = ("apple","banana","cherry","kivi")
# print (tuple)



#tuple iteme data type


# tuple1 = ("apple","banana","cherry")
# tuple2 = (1,2,34,5,6,1.5)
# tuple3 = (True,False,False)
# print(tuple1)
# print(tuple2)
# print(tuple3)


# tuple4 = ("apple",1,23,4,True, False)
# print(tuple4)



#tuple type()



# tuple = ("apple","banana","cherry","kivi")
# print(type(tuple))



# THE TUPLE CONCSTRUCTOR



# tuple_con = (("apple","banana","cherry",1,2,3,4))
# print(tuple_con)



# #ACCESS TUPLE ITEME 

# tuple_access = ("apple","banana","cherry","kivi")
# print(tuple_access[1])





#NAGETIVE INDEXING




# tuple_access = ("apple","banana","cherry","kivi")
# print(tuple_access[-1])



#RANGE OF INDEXING 



# tuple_access = ("apple","banana","cherry","kivi")
# print(tuple_access[1:3])




# tuple_access = ("apple","banana","cherry","kivi")
# print(tuple_access[-3:-1])




# CHECK ITEM   EXIT



# tuple_check = ("appple","banana","cherry","kivi","mango",)
# if "kivi" in tuple_check:
#     print("yes, 'kivi' is  in the fruit tuple")



# CHANGE TUPLE VALUES 


# tuple1 = ("apple","banana","cherry")
# tuple2 = list(tuple1)
# tuple2[1] = "kivi"
# tuple3 = tuple(tuple2)
# print(tuple3)




#ADD TUPLE VALUE


# tuple1 = ("apple","banana","orenge",)
# y = list(tuple1 )
# y.append("kivi")
# tuple3 = tuple(y)
# print(tuple3)



# tuple_add = ("apple","banana","cherry","mango")
# y = ("lichi",)
# tuple_add+= y
# print(tuple_add)


#REMOVE ITEMES 




# tuple_add = ("apple","banana","cherry","mango")
# y = list(tuple_add)
# y . remove("apple")
# tuple3 = tuple(y)
# print(tuple3)




#UNPACKING A TUPLE


# fruits = ("apple","mango","banana")
# green, yellow, red = fruits

# print(green)
# print(yellow)
# print(red)



# fruits = ("apple","mango","banana","kivi","orenge","graps")
# green, yellow, *red = fruits

# print(green)
# print(yellow)
# print(red)


#LOOP IN TUPLE


# fruits = ("apple","mango","banana","kivi","orenge")
# for i in fruits:
#     print(i)
    
    
    
    
    

# fruits = ("apple","mango","banana","kivi","orenge")
# for i in range(len(fruits)):
#     print(fruits[i])
    
    
    
    
    
    

# fruits = ("apple","mango","banana","kivi","orenge")
# i = 0 
# while i < len(fruits):
#     print(fruits[i])
#     i = i +1



#JOIN TWO TUPLE


# tuple1 = ("sanyam","sachichidanad","sunil")
# tuple2 = (1,2,3,)
# tuple3 = tuple1 + tuple2 
# print(tuple3)




#MULTIPLY TUPLE



# tuple1 = ("sanyam","sachichidanad","sunil")
# tuple2 = tuple1 *2
# print(tuple2)



# tuple = (1,2,3,4,6,7,)
# tuple2 = tuple *3
# print (tuple2)

