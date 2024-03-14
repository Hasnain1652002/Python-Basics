a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

print("Before swapping")
print("a =", a, "b =", b, "c =", c, "d =", d)

# swapping a and d variables
a = a + d
d = a - d
a = a - d

# swapping b and c variables
b = b + c
c = b - c
b = b - c

print("After swapping")
print("a =", a, "b =", b, "c =", c, "d =", d)