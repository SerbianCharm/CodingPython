# get the characters from position 2 to position 5(will not be included)
b = "Hello, World!"
print(b[2:5])  # will print 2,3,4 --> llo

# get all letters before position 5 --> 0,1,2,3,4
b = "BorisAna"
print(b[:5])  # by not typing the first number its starts with 0

# get all letters until end with a starting point of 2
b = "BorisAna"
print(b[5:])

# there is also negativ slicing
b = "Hello World"
print(b[-4:-1])  # get "orl"
