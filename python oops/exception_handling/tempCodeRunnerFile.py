

# try:
#      a=123
#      b=int(input("enter the number: "))
#      print(a/b)
# except ZeroDivisionError :
#       print("something wrong happen")


# print(a)
# print(b)


# try:
#     print("card inserted")
#     balance=5000
#     with_draw=int(input("enter amount : "))
    
#     if with_draw>balance:
#         raise Exception
#     else:
#         print("successfully")
# except Exception as e:
#     print("transcation failed",e)
# else:
#     print("Remaining - ",balance- with_draw)
# finally:
#     print("thankyou for visiting ")
    
    
    
# try:
#     a=90
#     b=int(input("enter the value"))
#     c=a/b
# except Exception as e:
#     print("error is ",e)
    
        
# try:
#     my_list=[22,3,4,55]
#     index_list=int(input("enter the value"))
#     store=my_list[index_list]
#     print(store)
# except Exception as e:
#     print("error is due to ",e)
    
# finally:
#     print("this is printed in every condition")

li=eval(input("enter the value"))
li=list(li)
index_no=int(input("enter the index you want"))
print(li[index_no])