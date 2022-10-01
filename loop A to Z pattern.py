
# # (A)


# for row  in range(6):     
#     for col in range(5):
#         if (col == 0 or col == 4)and(row != 0)or(row==0 and col > 0 and col < 4)or(row == 3):
#             print ("*",end=" ")
#         else:
#             print (end="  ")
#     print()


#(B)

# for row  in range(7):
#     for col in range(5):
#         if (col ==0) or   (col == 4 and (row !=0 and row !=3 and row !=6)) or  ((row ==0 or  row ==3 or row ==6)) and (col>0 and col<3):
#             print ("*",end=" ")
#         else:
#             print (end=" ")
#     print()



#(C)

# for row  in range(7):
#     for col in range(5):
#         if (col == 0 and (row !=0 and row !=6)) or ((row ==0 or row == 6) and(col !=0)):
#             print ("*",end=" ")
#         else:
#             print (end=" ")
#     print ()


#(D)

# for row  in range(7):
#     for col in range(5):
#         if (col == 0) or (col == 4 and (row != 0 and row != 6)) or (row == 0 or row == 6) and (col>0 and col<4):
#             print ("*",end=" ")
#         else:
#             print (end="  ")
#     print ()




#(E)

# for row in range (5):
#     for col in range (4):
#         if (col==0) or (row== 0 or row ==2 or row == 4):
#             print ("*",end=" ")
#         else:
#             print (end=" ")
#     print(end=" ")


#(F)

# for row in range (5):
#     for col in range (3):
#         if (col==0) or (row== 0 or row ==2):
#             print ("*",end=" ")
#         else:
#             print (end=" ")
#     print()




#(G)

# for row in range (7):
#     for col in range (4):
#         if (col == 0 and (row !=0 and row !=6)) or (row ==0 or row ==6 and (col !=0 and col !=6)) or ((row == 4 and (col !=0 and col !=1)) or ((row ==5 )) and col > 2):
#                print ("*",end=" ")
#         else:
#             print (end="  ")
#     print()

#(K)

# i = 0
# j = 4 

# for row in range(7):
#     for col in range(5):
#         if col==0 or (row==col+2 and col>1):
#             print("*",end=" ")
#         elif ((row == i and col == j )and col >0):
#             print("*",end=" ")
#             i =1+1
#             j= j-1
#         else:
#             print(end="  ")

#     print()

#(M)

# for row in range(7):
#     for col in range(7):
#         if col== 0 or col == 6 or ((row == col) and (col>0 and col<4 )) or (row == 1 and col == 5) or (row ==2 and col ==4):
#             print ("*",end=" ")
#         else:
#             print(end='  ')
#     print()


# #(N)

# for row in range(7):
#     for col in range(7):
#         if (col== 0 or col == 6) or (row == col  and (col>0 and col<6)):
#              print ("*",end=" ")
#         else:
#             print(end='  ')
#     print()


#(O)

# for row in range(7):
#      for col in range(5):
#          if  ((col==0 or col ==4) and (row !=0 and row !=6)) or ((row==0 or row== 6) and (col>0 and col<4)):
#               print ("*",end=" ")
#          else:
#             print(end='  ')
#      print()

#(w)

# i = 0 
# j = 3

# for row in range(4):
#     for col in range(7):
#         if col == 0 or col == 6 or (col == 5 and row ==2) or (col ==4 and row==1):
#             print("*",end=' ')
#         elif row == i and col ==j :
#             print ("*",end=" ")
#             i = i +1
#             j  = j -1
#         else:
#             print(end="  ")
#     print()

#(y)
# for row in range(5):
#     for col in range(5):
#         if (col == 2 and row >1) or (row == col  and col<2) or (row == 0 and col == 4 ) or (row ==1 and col ==3):
#                print ("*",end=" ")
#         else:
#             print(end='  ')
#     print()


#(Z)


# for row in range(6):
#     for col in range(7):
#         if (row==0 or row == 5) or (row+col==5):
#                   print ("*",end=" ")
#         else:
#             print(end='  ')

#     print()




# (S)

# for row in range(7):
#     for col in range(5):
#         if ((row == 0 or row ==3 or row == 6) and (col>0  and col<4 )) or (col == 0 and (row>0 and row<3)) or (col ==4 and(row>3 and row<6)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()      
       
            






#(O)

# for row in range(7):
#      for col in range(5):
#          if  ((col==0 or col ==4) and (row !=0 and row !=6)) or ((row==0 or row== 6) and (col>0 and col<4)):
#               print ("*",end=" ")
#          else:
#             print(end='  ')
#      print()

      
      
     
     
      
      
# R    

# for row in range(7):
#     for col in range(5):
#         if col ==0 or (col == 4 and (row !=0 and row !=3 )) or ((row==0 or row==3 ) and (col>0 and col<4)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()      






# R


# for row in range(7):
#     for col in range(5):
#         if col ==0 or (col == 4 and (row !=0 and row !=3 )) or ((row==0 or row==3 ) and (col>0 and col<4)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()      




# Y

# for row in range(5):
#     for col in range(5):
#         if (col==2 and row>1) or (row==col and col<2 ) or (row==0 and col==4) or  (row==1 and col==3):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()      

    
         
# (H)
                                     

# for row in range(7):
#     for col in range(5):
#         if col == 0 or col == 4 or (row == 3 and (col>0 and col<4)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()      
       
    
    
    
    
    
       
       
# # # (I)

# for row in range(7):
#     for col in range(5):
#         if col == 2 or ((row == 0 or row == 6) and col!=2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()      
       






# # (V)

# i = 0 
# j = 6 
# for row in range(4):
#     for col in range(7):
#         if row == col:
#             print("*",end=" ")
#         elif row == i and col == j:
#             print("*",end="  ")
#             i =  i+1
#             j = j-1
#         else:
#             print(end="  ")
#     print()









# # (A)


# for row  in range(6):     
#     for col in range(5):
#         if (col == 0 or col == 4)and(row != 0)or(row==0 and col > 0 and col < 4)or(row == 3):
#             print ("*",end=" ")
#         else:
#             print (end="  ")
#     print()







# #(N)

# for row in range(7):
#     for col in range(7):
#         if (col== 0 or col == 6) or (row == col  and (col>0 and col<6)):
#              print ("*",end=" ")
#         else:
#             print(end=' ')
#     print()




# #(G)

# for row in range (7):
#     for col in range (4):
#         if (col == 0 and (row !=0 and row !=6)) or (row ==0 or row ==6 and (col !=0 and col !=6)) or ((row == 4 and (col !=0 and col !=1)) or ((row ==5 )) and col > 2):
#                print ("*",end=" ")
#         else:
#             print (end="  ")
#     print()




# # (I)

# for row in range(7):
#     for col in range(5):
#         if col == 2 or ((row == 0 or row == 6) and col!=2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()      






# hart pattern

# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or ( row-col==2) or (row+col==8):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()


    
  
    
# i=0
# while i<5:
#     j=0
#     while j<=i:
#         print("*",end='')
#         j+=1
#     i+=1
#     print('')
    
    

# n = 5 
# i = 0 
# while (i<=n ):
#     print("  "* (n-i)+"*" *i)
#     i+=1