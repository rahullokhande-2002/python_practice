number=[22,33,44,5,22,4,224,4]
largest_num=second_larg=float('-inf')
for num in number:
    if num > largest_num:
        second_larg=largest_num
        largest_num=num
    elif num>second_larg and num !=largest_num:
        second_larg=num
print(second_larg)