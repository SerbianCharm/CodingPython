# you can add number variables into strings with f-format
int = 26
str = f"Ich bin so alt: {int}"
print(str)

# the placeholder can also have a modifier
int = 26
str = f"Um genau zu sein bin ich {int:.2f} Jahre alt"
print(str)

# you can also perform math function in the placeholder
str = f"Ich bin {13 + 13} Jahre alt"
print(str)
