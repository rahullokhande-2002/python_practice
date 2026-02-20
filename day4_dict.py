# student={'name':'rahul','city':'kolhapur','roll':33}
# print(student.keys()) 
# print(student.values())
# print(student.items())

students={'name':['rahul','shivaji','lokhande'],'marks':(22,33,22),'city':{'pune','kolhapur','goa'}}
# print(students['city'])
# l1=[2,4,5,6]
# print(l1[-1])
# print(students.get('name',2))

# students['std_id']=[1,2,3]
# print(students)

students['name']=['omkar','sayali','dhanu']
# print(students) # updating the value

students.pop('city')
# print(students)

students.popitem()
# print(students)


#fromkeys
subjects=['maths','science','gk']
marks=dict.fromkeys(subjects,1000)
# print(students)
print(marks)
