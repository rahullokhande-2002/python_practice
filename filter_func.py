l=[3,4,5,5,4,5,6,7,84,"rahul"]
# even=list(filter (lambda x: x%2==0,l))
# print(even)

# def even_fn(a):
#      if a%2==0:
#          return a
# print(even_fn(23))

# l=[1,2,3]
# even=list(filter(lambda x:x%2==0,l))
# print(even)

# text1=["rahul","lokhande",33]
# store=set(filter(lambda x:type(x)==str,text1))
# print(store)

# def check2(word):
#     return len(word)
# x=list(map(check2,l))
# x=list(map)


# l = [2, 5, 8, 1, 10]
# store=list(filter(lambda a: a>5,l))
# print(store)


# l = [10, 5, 20, 8, 15]
# n = int(input("Enter number: "))

# greater=list(filter(lambda x : x>n ,l))
# smaller=list(filter(lambda x : x<n ,l))

# print("greater",greater)
# print("smaller",smaller)




# def domain(emails):
#     store = []
#     for i in emails:
#         store.append(i.split("@")[1])
#     return store

# print(domain(emails))
emails = ["rahul@gmail.com", "omkar@speedup.com", "vinod@info.com"]
store=[]
for i in emails:
     store.append(i.split("@")[1])
print(store)

