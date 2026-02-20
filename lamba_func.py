#lambda function adv pythn on elinear of python
# it is small anonyumus fun 
# used for short code
# def add(a,b,c):
#     return a+b+c
# print(add(4,5,6))

#using lambda
# x=lambda a,b,c : 10+20+30
# print (x(3,4,5))


# def check(num):
#     if num%2==0:
#        return "true"
#     else:
#         return "f"
# print(check(78))   

# check=lambda num:"even" if num%2==0 else "odd"
# print(check(45))

 
# check_1=lambda a,b: "greater" if a>b else "small"
# print(check_1(22,33))


# largest=lambda a,b:f"greater{}" if a>b else "smaller"
# print(largest(22,3))
# l = ["ww", 33, 4, "sadda"]

# def filter_text_num(l):
#     t = []
#     n = []
#     for i in l:
#         if type(i) == str:
#             if i.isalpha():
#                 t.append(i)
#         else:
#             n.append(i)
#     return t, n

# print(filter_text_num(l))

# store=(lambda a,b,: a+b)
# print(store(22,4))

# conv=lambda t : (t-32)*5/9
# print(conv(33))

check=lambda a: "postive" if a>0 else "negative"
print(check(-22))