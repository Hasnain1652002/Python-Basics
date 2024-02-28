import random

# select a random sample without replacement
from random import seed
from random import sample


#Generate 6 random numbers between 0 and 61
randomlist = random.sample(range(0, 61), 6)
print(randomlist)

# seed random number generator
seed(1)

# prepare a sequence
sequence = [i for i in range(1, 61)]
# print(sequence)
# select a subset without replacement
subset = sample(sequence, 6)
print(subset)

# most 4
mostShow4X = (10)

# most 3
mostShow3X = (3, 5, 20, 33, 36)

# most 2
mostShow2x = (11, 2, 17, 18, 33, 34, 35, 37, 38, 40, 41, 42, 51, 53, 56, 58)

# normal 1 time shown
normal = (31, 32, 36, 37, 43, 45, 46, 47, 49, 50, 52, 55, 57)

# normal 1 time shown 2
normaltwo = (1, 2, 4, 6, 11, 12, 14, 16, 17, 18)

# no aperance
seqNotepiked = (7, 8, 9, 13, 15, 19, 21, 23, 26, 28, 39, 44, 48, 54, 59, 60)

one = (10)

# Number 2
two = random.sample(mostShow3X, 1)
random.choices(mostShow3X)

# Number 3
three = random.sample(mostShow2x, 1)
random.choices(mostShow2x)

# Number 4
four = random.sample(normal, 1)
random.choices(normal)

# Number 5
five = random.sample(normaltwo, 1)
random.choices(normaltwo)

# Number 6
six = random.sample(seqNotepiked, 1)
random.choices(seqNotepiked)

print (one, two, three, four, five, six)


# not picked yet
# 07, 08, 09, 13, 15, 19, 21, 23, 26, 28, 39, 44, 48, 54, 59, 60

# most show sofar
# 4x
# 10

# 3x
# 03, 05, 20, 33, 36

# 2x
# 11, 02, 17, 18, 33, 34, 35, 37, 38, 40, 41, 42, 51, 53, 56, 58

# Normal
# 01, 02, 04, 06, 11, 12, 14, 16, 17, 18, 31, 32, 36, 37, 43, 45, 46, 47, 49, 50, 52, 55, 57