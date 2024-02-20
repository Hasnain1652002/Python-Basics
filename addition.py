print("For 1st Matrix")
nC1 = int(input("Enter no. of Columns: "))
nR1 = int(input("Enter no. of Rows: "))
a = 0
m = []    # FINAL MATRIX
while a < nR1:
    i = 0
    k = []
    a += 1
    while i < nC1:
        b1 = float(input("Enter a number: "))
        k.append(b1)
        i += 1
    m.append(k)
print(m)

print("For 2nd Matrix")
nC2 = int(input("Enter no. of Columns: "))
nR2 = int(input("Enter no. of Rows: "))
a = 0
n = []    # FINAL MATRIX
while a < nR2:
    i = 0
    k = []
    a += 1
    while i < nC2:
        b2 = float(input("Enter a number: "))
        k.append(b2)
        i += 1
    n.append(k)
print(n)
print("Result")
result = []
if nR1 == nR2 and nC1 == nC2:
    i = 0
    while i < nR1:
        r = []
        i += 1
        j = 0
        while j < nC1:
            r.append(m[i][j])
            r.append(n[i][j])
            print(r.append(m[i][j]))
            r.append(n[i][j])
            j=j+1
        result.append(r)
    print(result)
else:
    print("Addition is not possible")
