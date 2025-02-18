thisList = ["apple", "banana", "cherry"]
print(thisList)

# lists allows duplicate items
anotherList = ["apple", "apple", "banana", "banana", "cherry"]
print(anotherList)

# to see how many items a list has use len()
print(len(anotherList))

# list items can be of any data type and have different data types in it
numberList = [1, 2, 3, 4, 5]
booleanList = [True, False, True]
difList = [1, True, "Hello"]

print(type(difList))

# you can construc lists with list()

testList = list(("apple", 1, True))
print(testList)

# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#   *Set items are unchangeable, but you can remove and/or add items whenever you like.
#   **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# to change a value just overwrite it
broList = [1, 2, 4, 4, 5]  # one 4 to much overwrite it
broList[2] = 3  # overwrite third position from 4 to 3
print(broList)  # new list is [1, 2, 3, 4, 5]

# you can use ranges too
testList[0:2] = [1, 2, 3]
print(testList)

# you can add items with the insert() method
insertList = [1, 2, 4, 5]
insertList.insert(2, 3)
print(insertList)

# to add an item to the end of the list use the apped() method
anotherTestList = [1, 2, 3, 4, 5]
anotherTestList.append(6)
print(anotherTestList)

# to add fusion lists together use extend() --> you can even add different arrays together like lists and tuples and so on
fullNumberList = [1, 2, 3, 4]
expandedNumberlist = [5, 6, 7, 8]
fullNumberList.extend(expandedNumberlist)
print(fullNumberList)

# to remove items use remove() method
# removes the actual number/string not the position --> removes the value only once if it is used more than once in the list, first appearance is removed
fullNumberList.remove(2)
print(fullNumberList)

# if you want to remove with the index number use pop() --> if not specified == no number written, it will remove the last item
thisList.pop(2)  # will remove 2 index == cherry
# thisList.del(2)    #does the same as pop() and can delete the whole list if not written with any number --> thisList.del()

print(thisList)

# to clear out the lists without deleting it completly you can use the clear() method
borisList = ["ABC", True, "Jawohl"]
print(borisList)
borisList.clear()
print(borisList)  # is empty

# how to loop through lists
for i in range(len(fullNumberList)):
    print(fullNumberList[i])

# or with while

i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1

# or with comprehension

[print(x) for x in thisList]

# sort list alphanumerical ascending
fruits = ["apple", "banana", "cherry", "watermelon", "mango"]
fruits.sort()
print(fruits)

# to sort it descending use reverse = True
fruits.sort(reverse=True)
print(fruits)


# sort the list to be as close to 50
def myfunc(n):
    return abs(n - 50)


numList = [2, 40, 50, 30, 65]
numList.sort(key=myfunc)
print(numList)

# sort is case sensitive so we will make it lower case
fruits.sort(key=str.lower)
print(fruits)

# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
