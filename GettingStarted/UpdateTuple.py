# tuples are unchangeable, but there are workarounds
# update items by changing to list and back

stdTuple = (1, 2, 3, 4, 5)
x = list(stdTuple)
x[1] = 7
stdTuple = tuple(x)

print(stdTuple)

# this goes with every operation like append(), remove(), and so on
