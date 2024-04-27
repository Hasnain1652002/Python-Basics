# import re

# # Define a regular expression pattern for a digit
# pattern = r'\d+'

# # Test the pattern using the re module
# text = input("enter : ")
# match = re.search(pattern, text)

# if match:
#     print(f"Found a digit: {match.group()}")
# else:
#     print("No digit found.")

import re

# Define a regular expression pattern for a digit
pattern = "[0-9]+"

# Test the pattern using the re module
text = "The number 7 is a digit. The number 3 is also a dig2901901290 1919 1919 1091it."
matches = re.finditer(pattern, text)

for match in matches:
    print(f"Found a digit: {match.group()}")

