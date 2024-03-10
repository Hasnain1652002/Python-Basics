import math
import numpy

# LOOP FOR PUTTING HAMMING BITS IN MESSAGE LIST

'''This loop will append "h(x)" bits according to the length of 
message and also print the message packet.'''

##message = [1, 0, 0, 1]
message = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]

# n = 0
for n in range(5):
    a = message.insert(int(math.pow(2, n) - 1), f"h{n}")
    if a is not None:
        message.append(a)
    # n += 1
print(f"Message packet: {message}")
'''This loop separates each list of "h" and print it on the terminal'''

print('========')

# LOOP FOR SEPARATING EACH "h(x)" LIST

n = 0
message_packet = []
for x in range(5):
    h = []
    del message[:n]
    for y in range(0, len(message), n + 2):
        h.append(message[y])
    n += 1
    message_packet.append(h)
    print(f"h{x} = {h} ")
# print(message_packet)

# LOOP FOR PUTTING ORIGINAL PARITY BITS
'''This loop counts the number of "1" in each list of "h(x)"
and add parity bit instead of "h(x)" element either "1"or"0".'''

for x in range(len(message_packet)):
    a = message_packet[x].count(1)
    if a % 2 == 0:
        message_packet[x].pop(0)
        message_packet[x].insert(0, 1)
    else:
        message_packet[x].pop(0)
        message_packet[x].insert(0, 1)
# print(message_packet)

# CHECKING CODE ALGORITHM
'''Product of odd numbers is always odd. So, the product of counts
of "1" from each "h" list will be odd and its definitely means the 
 message is sent without any error. '''

check_lis = []
for x in range(len(message_packet)):
    a = message_packet[x].count(1)
    check_lis.append(a)
print(check_lis)
check = numpy.prod(check_lis)
# print(check)
if check % 2 == 0:
    print("There is an error in the code")

else:
    print("Code is not changed!"
          "Your message is safe.")
