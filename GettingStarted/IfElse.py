# if then elif and everything other else

a = 33
b = 32

if a < b:
    print("A is smaller than B.")
elif a == b:
    print("A equals B.")
else:
    print("A is bigger than B.")

# or you can write it in one line

print("A") if a > b else print("==") if a == b else print("B")

# normally if statements cant be empty, there is one exception "pass"

x = 10
y = 20

if x < y:
    pass
