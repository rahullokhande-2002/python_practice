# # # # # # What will be the code if output if code is this ? Explain why.
# # # # # a = "5"
# # # # # b = 2
# # # # # print(a * b + str(b))
# # # # # #  Ans==> will be 552 bcz it follow bodmas rule and after that string multplication happen after that due string concation happens

# # # # # # Mutable vs Immutable:
# # # # # # Predict the output and explain the behavior

# # # # # x = [1, 2, 3]
# # # # # y = x
# # # # # y.append(4)
# # # # # print(x)
# # # # # o/p =[1,2,3,4]  bcz due  x value is assign to the y and y append the 4


# # # # # Write a program to count how many numbers are present in a given string without using any built-in count() 
# # # # # method. use user defined function

# # # # # def count_num(s):
# # # # #     digits=0
# # # # #     alph=0
# # # # #     strings=0
# # # # #     for i in s:
# # # # #         if i.isdigit():
# # # # #             digits=digits+1
# # # # #         elif i.isalpha():
# # # # #             alph=alph+1
# # # # #         else:
# # # # #             strings=strings+1
# # # # #     return digits,alph,strings
# # # # # text=input('enter the text: ')
# # # # # # result=count_num(text)
# # # # # d, a, s = count_num(text)

# # # # # print("Digits:", d)
# # # # # print("Alphabets:", a)
# # # # # print("Special characters:", s)


# # # # # Q4] Dictionary Logic:
# # # # # Given a dictionary of student names and marks, find and print the student(s) with the second highest marks.

# # # # # students={"rahul":70,"suyash":76,"kartik":90,"yk":78}
# # # # # store=(sorted(students.values()))
# # # # # print(store)
# # # # # second_highest=store[-2]

# # # # # for name,marks in students.items():
# # # # #     if marks==second_highest:
# # # # #         print(f"{name}:{marks}")

# # # # # Q6 . While Loop with Condition:
# # # # # Write a program using a while loop to find the sum of digits of a given integer.

# # # # # i=1
# # # # # count=0
# # # # # n=int(input("enter the value :  "))
# # # # # while i<=n:
# # # # #     count=count+i
# # # # #     i=i+1
# # # # # print(count)


# # # # #  Q7 Break and Continue Combo:
# # # # # Write a program that prints all numbers from 1 to 30 except multiples of 3.
# # # # # Stop the loop completely if a number is divisible by 13.

# # # # # n = 30

# # # # # for i in range(1, 31):
# # # # #     if i % 3 == 0:
# # # # #         continue        
    
# # # # #     if i % 13 == 0:
# # # # #         break       
    
# # # # #     print(i)
            
    
# # # # # For Loop Challenge:
# # # # # Q8] Using a for loop, calculate the sum of all prime numbers between 10 and 50  
# # # # # total = 0

# # # # # for i in range(10, 51):  
# # # # #     count = 0

# # # # #     for j in range(1, i + 1):   
# # # # #         if i % j == 0:
# # # # #             count += 1

# # # # #     if count == 2:  
# # # # #         total += i

# # # # # print(total)
# # # # # print(sum)


# # # # #9]
# # # # def add_item(item, items=None):
# # # #     if items is None:
# # # #         items = []
# # # #     items.append(item)
# # # #     return items
        
# # # #   10]      
# # # # words = ["apple", "cat", "banana", "dog" "sun"]

# # # # result = [word for word in words if len(word) > 4]

# # # # print(result)      

# # # Q 11
# # # result = [num**2 for num in range(1, 21) 
# # #           if num % 2 == 0 and num % 4 != 0]

# # # print(result)


# # # 12. List Flattening Challenge:
# # # Given a nested list like [[1,2], [3,4,5], [6]], flatten it into a single list using list comprehension only. E.g. [1,2, 
# # # 3,4,5, 6]

# # # nested = [[1, 2], [3, 4, 5], [6]]

# # # flat = [num for sublist in nested for num in sublist]

# # # print(flat)

# # # Remove duplicates from a list while maintaining order (no set()).

# # numbers = [1, 2, 2, 3, 4, 3, 5, 1]

# # unique_list = []

# # for num in numbers:
# #     if num not in unique_list:
# #         unique_list.append(num)

# # print(unique_list)


# # Merge two dictionaries without using the update() method
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# merged = {**dict1, **dict2}

# print(merged)

# 17
# def authenticate_user(stored_password):
#     def check_password(entered_password):
#         if entered_password == stored_password:
#             return "Access Granted"
#         else:
#             return "Access Denied"
    

#     entered = input("Enter your password: ")
#     return check_password(entered)

# result = authenticate_user("mySecret123")
# print(result)

#18
transactions = [100, -50, 200, -30, -20, 300]

# Total income
total_income = sum(t for t in transactions if t > 0)

# Total expense (make it positive for readability)
total_expense = sum(-t for t in transactions if t < 0)

# Net balance
net_balance = sum(transactions)

print("Total Income:", total_income)
print("Total Expense:", total_expense)
print("Net Balance:", net_balance)