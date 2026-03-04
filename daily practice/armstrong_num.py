num=int(input("enter the number: "))
temp=num
sum=0

length= len(str(num))

while temp> 0:
    digit=temp%10
    sum=sum+digit**length
    temp=temp//10

if sum==num:
    print("yes")
else:
    print("its not")