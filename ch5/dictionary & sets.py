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
