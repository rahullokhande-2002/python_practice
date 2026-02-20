#set:A set is an unordered collection of unique elements
#{}
#does not allow duplicate elements
#unordered==>no index
#mutable: add, change remove elements
#How set is muatble?
#set methods
#add elements==>add(),update()
#remove elements==>remove(),discard(),pop()
#change:we cannot change (modify) an existing element coz set is an unordered: no indexing,No replacement
# l=[1,2,3,4]
# #add: append(),extend()
# #remove: remove(),pop()
# #change : using index
# l[0]=100
# print(l)
# s1={1,2,1,1,2,3,3,4,1,12,23,34,4,"chetana"}
# print(s1)
#add
# s1.add(500)
# print(s1)
# #update
# s1.update([200,"data"])
# print(s1)
# #remove()
# s1.remove("chetana")
# print(s1)
# #discard()
# s1.discard(200)
# print(s1)
# # s1.remove("z")  #error: if element not present
# s1.discard("z")   #no error: if element not present
# print(s1)
# #pop()
# #if we use pop() in list it will remove last element
# #if we use pop() in set it will remove any random element
# s1.pop()
# l.pop()
# print(s1)
# print(l)
# s2={"data","chetana","sceince"}
# s2.pop()
# print(s2)
# #pop fn can accept index num as a paramter
# l.pop(0)
# print(l)
# #type casting set to list
# s1_list=list(s1)
# print(s1_list)

# #clear(),copy()
# s2=s1.copy()
# print(s2)
# s1.clear()
# print(s1)
#empty list==>[]
#empty tuple==>()
#empty set==>set()
#empty dict={}

########################################################
#set mathemtical methods
#union()  or |   : combine ignoring duplicates
#intersection() or &  : common 
#difference()  or - : Elements in a but not in b
#symmetric_difference() or ^: uncommon elements
a={1,2,3,4,1,2}
b={3,4,5,6,7}
print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a&b)
print(a.difference(b))  #1,2
print(a-b)
print(a.symmetric_difference(b))  #1,2
print(a^b)
###############
#set relationship methods
#issubset(). issuperset(), isdisjoint()
c={2,3}
d={1,2,3,4}
print(c.issubset(d))
print(d.issubset(c))
print(c.issuperset(d))
print(d.issuperset(c))
#isdisjoint(): checks if sets have no common elements
print(c.isdisjoint(d))
x={1,2}
y={3,4}
print(x.isdisjoint(y))