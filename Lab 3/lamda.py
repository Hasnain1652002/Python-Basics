numbers = [0, 1, 2, 3, 4, 5]

# Square every number in the list using lambda
squared_numbers = list(map(lambda x: x**2, numbers))

# Cube every number in the list using lambda
cubed_numbers = list(map(lambda x: x**3, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Cubed numbers:", cubed_numbers)