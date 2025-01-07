thisdict = {"brand": "Ford",
          "model": "Mustang",
          "year": 1998}
print(thisdict)
#2
x = thisdict.get("model")
print(x)
print(thisdict.get("cost","Key not found"))
#3
x = thisdict["model"]
print(x)
#4
thisdict["year"] = 2018
print(thisdict)
#5
for x in thisdict:
    print(x)
#6
for x in thisdict:
    print(thisdict[x])
#7
for x in thisdict.values():
    print(x)
#8
for x, y in thisdict.items():
    print("The value at key x is: ", x, "is: ", y)
#iterate through keys
#iterate through values
#8
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
#9
print(len(thisdict))
#10
thisdict["color"] = "red"
print(thisdict)
#11
#thisdict.pop("model")
#print(thisdict)
#12
thisdict.popitem()
print(thisdict)
#13
del thisdict["model"]
print(thisdict)
#14
thisdict.clear()
print(thisdict)
#15
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
newdict = thisdict.copy()
print(newdict)
thisdict["year"] = 2024
newdictcopy = thisdict
thisdict["year"] = 2024
print(newdictcopy)
#16
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)

#17
#16
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)

#17
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}


myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}

print(myfamily)




    

