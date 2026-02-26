def count_down(num):
    if num==0:
        print("times up")
    else:
        print(num)
        return count_down(num-1)
count_down(5)    