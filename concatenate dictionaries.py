# d1={1:10, 2:20}
# d2={3:30, 4:40}
# d3={5:50, 6:60}

# d4 = {**d1, **d2, **d3}
# print(d4)

# ## Or 

# D5={}
# for d in (d1, d2, d3):
#     d4.update(d)

nums = [1,2,3,4,5,6]
plusOneNums = [x+1 for x in nums]
print(plusOneNums)
oddNums = [x for x in nums if x % 2 == 1] 
print(oddNums) 
# oddNumsPlusOne = [x+1 for x in nums if x % 2 ==1]
# print(oddNumsPlusOne)
# for x in range(len(nums)):
#     if nums[x]%2 == 1:
#         pass
#     else:
#         nums[x].remove()
