# # 1  Write a program to input exactly five student names, store them in a list, and then print the names in uppercase. 
# students = []

# for i in range (5):
#     name=input('enter the name : ')
#     students.append(name)
    
# for name in students:
#     print(name.upper())
    
# 2    Convert a list of integers to a set to remove duplicates, then convert it back to a sorted list.
# l1=[22,33,44,55,55,66,77,88,88]
# print(l1)

# conv_list=set(l1)
# print(conv_list)

# f_list=list(conv_list)
# print(f_list)



#  3 Write a program to check whether a list contains any duplicate elements (return True/False).

# l1=[22,33,44,22,44,676,89]
# l1=[2,3,4,5,6,5]

# if(len(l1)== len(set(l1))):
#         print('true')
# else:
#      print('false')  
     
# 4    Remove all vowels (a, e, i, o, u) from every string in a list and print the resulting list.

# words = ["rahul", "shivaji", "lokhande"]

# vowels = "aeiou"
# result = []

# for word in words:
#     new_word = ""
#     for ch in word:
#         if ch not in vowels:
#             new_word += ch
#     result.append(new_word)

# print(result)

############################################
# 12    Read three numbers and use if‑elif‑else to print the largest of the three.
     
# a,b,c = 10, 5, 7

# if a>b and a>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)
    
# 13 Check whether a given string is a palindrome (reads the same forward and backward) by using slicing

# s = input("Enter a string: ")

# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 11    Determine whether a single input character is a vowel or consonant with an if‑else statement.

# ch = input("Enter a character: ")

# if ch in "aeiouAEIOU":
#     print("Vowel")
# else:
#     print("Consonant")


# 10    Swap the values of two variables without using a third variable and print the swapped values.
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))

# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)


# 6    Ask the user for a number and check whether it is divisible by both 3 and 5.

# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by both 3 and 5")
# else:
#     print("The number is not divisible by both 3 and 5")


# 5    Take a user’s age as input and determine the movie‑ticket price using if‑elif‑else logic:

# < 5 → “Free”, 5–18 → “₹50”, 18–60 → “₹100”, ≥ 60 → “₹70”

# age = int(input("Enter your age: "))

# if age < 5:
#     print("Free")
# elif age >= 5 and age < 18:
#     print("₹50")
# elif age >= 18 and age < 60:
#     print("₹100")
# else:
#     print("₹70")



