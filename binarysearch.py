a=[10,15,20,25,30,35,40,45,50,55]
i=0
s=i
e=int(len(a)-1)
l=int((s+e)/2)
m=a[l]
n=int(input("enter no. :"))
while s<e :
     if n>m :
        s=l+1
        l=int((s+e)/2)
        m=a[l]
     if n<m :
        e=l-1
        l=int((s+e)/2)
        m=a[l]
     if n==m :
        print (n," is found at position ",l+1)     
        break
else :
     print (n," is not found ")
