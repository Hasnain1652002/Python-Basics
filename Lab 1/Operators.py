# a=9
# b=5
# a//=3
# b**=5

# # Output:

# print("floor divide=",a)
# print("exponent=",b)


# floor divide= 3
# exponent= 3125



# ****************************************************


# Identity Operators in Python
# x=6
# if (type(x) is int):
#     print ("true")
# else:
#     print ("false")

# true

# ****************************************************


# x = 7.2
# if (type(x) is not int):
#     print ("true")
# else:
#     print ("false")

# true


# ****************************************************

# # Membership operator:

# list1=[1,2,3,4,5]
# list2=[6,7,8,9]
# for item in list1:
#     if item in list2:
#         print("overlapping")
#     else:
#         print("not overlapping")

# not overlapping
# not overlapping
# not overlapping
# not overlapping
# not overlapping

# ****************************************************


# # Bitwise Operaotors:
# a = 60 # 60 = 0011 1100 
# b = 13 # 13 = 0000 1101 
# c = 0

# c=a&b # 12 = 0000 1100
# print("Line 1", c )

# c=a|b # 61 = 0011 1101 
# print("Line 2", c )

# c=a^b # 49 = 0011 0001 
# print("Line 3", c )

# c = ~a # -61 = 1100 0011 
# print("Line 4", c )

# c = a << 2 # 240 = 1111 0000 
# print("Line 5", c )

# c = a >> 2 # 15 = 0000 1111 
# print("Line 6", c )



# Line 1 12
# Line 2 61
# Line 3 49
# Line 4 -61
# Line 5 240
# Line 6 15