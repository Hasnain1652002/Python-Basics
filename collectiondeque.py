from collections import deque
d = deque()
n = int(input())
for i in range(n):
    N = input().split()
    if len(N) == 2:
        eval("d.{}({})".format(N[0],N[1]))
    else:
        eval("d.{}()".format(N[0]))

print(*d , sep = " ")