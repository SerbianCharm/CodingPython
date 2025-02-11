# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# try out an error and print the error message you want
try:
    print(x)
except:
    print("X is not defined")
# Standard error would be this:
# Traceback (most recent call last):
#  File "demo_try_except_error.py", line 3, in <module>
#    print(x)
# NameError: name 'x' is not defined


# you can throw -> raise an error
x = -1

if x < 0:
    raise Exception("No numbers below zero")
# output is:
# Traceback (most recent call last):
#  File "c:\Stuff\CodingPython\GettingStarted\TryExcept.py", line 23, in <module>
#    raise Exception("No numbers below zero")
# Exception: No numbers below zero
