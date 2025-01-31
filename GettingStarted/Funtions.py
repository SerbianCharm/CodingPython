# you can add parameters to functions


def myFunc(userName):
    print("The name you wrote is " + userName)


myFunc("Boris")

# normaly a function takes and needs as many parameters as set, but if you dont know how many you need use *


def mySecFunc(*names):
    print("The oldest child is " + names[1])


mySecFunc("Boris", "Bojan", "Unknown")
