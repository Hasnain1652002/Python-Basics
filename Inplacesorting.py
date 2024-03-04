####-----for acsending order------####
a=[61,32,54,22,91,100,36,48,50,1,44]
b=0
while b<len(a):
    s=a[b]
    i=0
    while i<len(a) :
        if a[i]>s :
            t=a[i]
            a[i]=a[b]
            a[b]=t
        i+=1   
    b+=1
print (a)

####-----for decending order-----####
a=[61,32,54,22,91,100,36,48,50,1,44]
b=0
while b<len(a):
    s=a[b]
    i=0
    while i<len(a) :
        if a[i]<s :
            t=a[i]
            a[i]=a[b]
            a[b]=t
        i+=1   
    b+=1
print (a)

####-----experiment for single inplacement---------####
##s=a[0]
##while i<len(a) :
##    if a[i]<s :
##        j=i
##        s=a[j]
##    i+=1
##
##
##t=a[j]
##a[j]=a[0]
##a[0]=t
##
##
##print (a)
