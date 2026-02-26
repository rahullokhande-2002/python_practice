
# # print(a)
# # print(b)


# # try:
# #      a=123
# #      b=int(input("enter the number: "))
# #      print(a/b)
# # except ZeroDivisionError :
# #       print("something wrong happen")


# # print(a)
# # print(b)


# # try:
# #      a=123
# #      b=int(input("enter the number: "))
# #      print(a/b)
# # except ZeroDivisionError :
# #       print(ZeroDivisionError)


# # print(a)
# # print(b)



# #  whenthe try correct then only else excute
# try:
#      a=123
#      b=int(input("enter the number: "))
#      print(a/b)
# except  :
#       print("error")



# else:
#   print(a)
#   print(b)


# catching multile exception
# try:
#     a=eval(input("enter the no1:"))
#     b=eval(input("enter the no2"))
#     print(a/b)
# except ZeroDivisionError:
#     print("plz enter non zero denominator")
# except NameError:
#      print("plz enter the numeric value")
# except TypeError:
#     print("dont  enter string value")
# except Exception as e:
#     print("error from exception class")
#     print(e)



#try and exception 
# this clause 

try:
    a=2
    b=80
    c=a/b
except:
    print("cant divide by zero")

else:
    print(a)
    print(b)
    print(c)
    
finally:
    print("code is fine")