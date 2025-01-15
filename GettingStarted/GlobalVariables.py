# global variables can be used in the whole program, which means in and outside of a function

x = 5


def myfunc():  # inits a function
    print("The global variable x = ", x)


myfunc()

# if you create a variable inside of the funtion with the same name as the global variable, the variable within the function will be used
y = 3


def myfunc2():
    y = 4
    print("This should be 4: ", y)


myfunc2()

print("This should be 3: ", y)


# you can make a variable inside of a function global with the keyword global
def myfunc3():
    global b
    b = 3


myfunc3()

print("This should write 3 only if the function is called in the code: ", b)

# you can edit global variables which are outside of a variable within the function itself with the keyword global
g = 5


def myfunc4():
    global g
    g = 11


myfunc4()
print(
    "If the function was called the value of g should be 11, lets see if its true: ", g
)
