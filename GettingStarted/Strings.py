# Strings in python can either be casted with single or double quotes

x = "Hello World"
# same as
y = "Hello World"

print(x)
print(y)

a = """Das ist ein Test von
Multiline Strings und wie der output ist"""

# Multiline strings will be printed out as written in the code (with spaces and enter)
print(a)

# If you want to print out a specific character out of a string you do as followed
t = "Hello World"
print(t[2])  # prints "l"

# you can loop through strings because they are basically arrays in python
for x in "banana":
    print(x)  # will print out each letter --> for x(letters) in banana print out

# if you want to have the length of a string you use len
k = "Hello Boris!!"
print(len(k))  # solution is 13 with space included

# you can check if something is present in a string with "in"
txt = "Das ist ein Test von in!"
print("Test" in txt)  # will output true if it is in the string

# Another usage of "in"
test = "Das ist ein Test von in Statements in if Schleifen"
if "Statements" in test:
    # This text only shows if the search word is in the txt variable
    print("Statement ist vorhanden")

# you can do the same with "not in"
test2 = "Das ist Boris"
if "Ana" not in test2:
    print("Boris ist drinnen nicht Ana!")
