# num=int(input("enter the number : "))
# n1,n2=0,1
# sum=0
# if num<0:
#     print("enter the number greater than 0 ")

# else:
#    for i in range(0,num):
#        print(sum,end=" ")
#        n1=n2
#        n2=sum
#        sum=n1+n2

# 0,1==>n1,n2
# n1,n2,sum  ,sum


num=int(input("enter the number"))
n1,n2=0,1
sum=0

for i in range(0,num):
 if num<0:
    print("enter the +ve number")
    
 else:
    n1=n2
    n2=sum
    sum=n1+n2
print(sum)