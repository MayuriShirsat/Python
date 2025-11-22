# list->containers to store a set of values of nay datatype
# lists are mutable(orignal list is changed by opration)
l1=["apple","Orange",5,34.34,False,"Ram"]
print(l1[0])
l1[0]="grapes"# not possible in string
print(l1[0])
# indexing is same like string
print(l1[1:4])

# list methods
l1=[12,33,2,45,6,77]
l1.append(98)
print(l1)
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3,33333)# insert 33333 at index 3 ie.,after 2
print(l1)
l1.pop(3)
print(l1)
l1.remove(12)
print(l1)

# Tuple->imutable containers to store a set of values of nay datatype (list but imutable)
a=(1,2,57.8,45,"puja")#for tuple we use "()" and for list "[]"
print(type(a))
# a[0]=234  # can not change
# methods are same as list->.count,concatinate=a+b,repetation,membership(is member or not) ex.,->"hi" in a,len(),min(a),max(a),slicing, etc
