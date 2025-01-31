# while can have break statements

i = 1
while i < 6:
    print("This is loop number", [i])
    if i == 4:
        break
    i += 1

# same goes with continue

x = 1
while x < 6:
    x += 1
    if x == 4:
        continue
    print("This is loop", x)
