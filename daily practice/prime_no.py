# num=int(input("enter the number "))
# prime=[]

# if num<=1:
#         print('number is  not prime')
# else:
#     for i in range (2,num):
#         if num%i==0:
#             print('number is not prime')
#             break
#     else:
#         print("number is prime")

num=int(input("enter the number "))


if  num<=1:
    print('number is not prime')
    
else:
    for i in range(2,int(num**0.5) + 1):
        if num%i==0:
            print("number is not prime")
            break
    else:
            print("niumber is prime")
        
    
        