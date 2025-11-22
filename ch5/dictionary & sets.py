# dictionary-->is print collection of keys-value pairs
a={
   "key":"value",
   "mayuri":"code",
   "marks":"98",
   "list":[1,4,6],
   0:"sun"
   }

print(a,type(a))
print(a["key"]) #prints curresponding value
print(a["list"]) #print [1,4,6]

# it is unorderd
# it is mutable
# it is indexed
# it can not contain duplicate keys

# dictionary methodes
print(a.items())
print(a.keys())
print(a.values())
a.update({"sandhya":99,"marks":100})
print(a)
print(a.get("mayuri")) # this do same wark as "a["mayuri"]" as above but note following
print(a.get("shiv")) # it give output as NONE as shiv is not in a
print(a["shiv"]) # but this give ERROR as shiv is not in a


# set->collection of non-repetitive element of any datatypes
a={1,2,3,3,3,3,7,5,8} #this is a set if in this repetative values are present then it take that value only once in output
print(a)
b={} #this is a empty DICTIONARY
print(type(b))
c=set() # this is a empty SET
print(type(c))

# sets are not ordered ie., in o/p we get the elements in any random order
# sets are unindexed
# we can not change exesting items in sets(immutable)

# set methods
a.add(345)
print(a)
print(len(a))
a.remove(1)
print(a)
print(a.pop())
print(a) # remove any random element
a.clear()
print(a) # cleare the whole set
s1={1,2,5,76,54,3,8}
s2={454,2,3,76,8,53}
print(s1.union(s2)) # return all values in both sets without repetation
print(s1.intersection(s2)) # return values same in both sets without repetation
print({1,2}.issubset(s1))
