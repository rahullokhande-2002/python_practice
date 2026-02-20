# mcount=0
# acount=0
# vote=0

# while vote!="stop":
#       vote=input("enter the vote for Manu M and Adu A: ")
#       if vote=="M":
#           mcount=mcount+1
#       elif vote=="A":
#           acount=acount+1
#       else:
#           print("enter the valid vote")
# print(acount)
# print(mcount)      
      
# check the prime number div by 1 and itself

# number=int(input("enter the number :"))
# if number<=1:
#      print("not a prime number")
# else:
#     for i in range(2,number):
#      if i % i==0:
#              print(f"number is prime number {i}")
#              break
#     else:
#       print(" a prime number")
 
number=int(input("enter the value"))
if number<=1:
     print("not prime number")
else :
     for i in range(2,number):
          if number % i==0:
               print("number is  prime ",i)
          else:
               print("number is not prime",i)
               
               