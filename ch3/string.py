'''
string is a datatyoe in python 
it is imuteble(existing string can not be changed)
it is sequence of characters in quotes
way to write string->
'''

a="mayuri"
b='santosh'
c='''shirsat'''
# string slicing
# index start from "0" if form left and from "-1" if from right(negative slicing)
d=a[0:3]#from 0 to 1 less than 3(excluding 3)
print(d)
# -ve slicing
print(a[-4:-1])#simple way convert -ve indexing in +ve ex., -4:-1 become 2:5
# it print "yur"
print(a[:4])
print(a[2:])
print(a[0:6:2])#print from 'm' to 'r' but at a gap of 2
