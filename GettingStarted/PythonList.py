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
