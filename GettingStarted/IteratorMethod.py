# you can iterate through lists, tuples, dictionaries and sets with the method iter()

myTuple = ("apple", "banana", "cherry")
myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))
