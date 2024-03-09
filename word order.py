# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
n = int(input())
l = [ ]
for i in range(n):
    l.append(input())

x = Counter(l)

print ( len(x))
print (*x.values())