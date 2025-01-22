# get all fruits with "a" from one list to another

fruits = ["apple", "banana", "cherry", "watermelon", "mango"]
aList = []

for x in fruits:
    if "a" in x:
        aList.append(x)

print(aList)

# now with list comprehension
fruitsNew = ["apple", "banana", "cherry", "watermelon", "mango"]

newList = [x for x in fruitsNew if "a" in x]
print(newList)

randomList = [x for x in range(10)]
print(randomList)

# "Return the item if it is not banana, if it is banana return orange".
newlist = [x if x != "banana" else "orange" for x in fruits]
