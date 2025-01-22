# if you want to copy a list dont just use "=" use copy()
fruits = ["apple", "banana", "cherry", "watermelon", "mango"]
newList = fruits.copy()
print(newList)

# or use list()
anotherList = list(fruits)
print(anotherList)

# or use the slice operator ":"
sliceList = fruits[:]
print(sliceList)
