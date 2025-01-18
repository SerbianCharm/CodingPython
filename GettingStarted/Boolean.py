print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 100
b = 33

if b > a:
    print("B is greater than A!")
else:
    print("A ist greater than B!")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))  # Only empty strings are false
print(bool(y))  # Only 0 is false


def myFunction():
    return True


print(myFunction())

x = 200
print(isinstance(x, int))
