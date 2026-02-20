year=int(input("enter the year:"))

if year%400==0:
    print('this is leap year',year)
    
elif year%4==0 and year % 100!=0:
   print('this is leap year',year)
else:
    print('year is not leap year')