def matrixinput ():
   m=[]
   i=0
   while i<nr1 :
       a=[]
       r=0
       while r<nc1 :
           h=float(input("enter a value for matrix :"))
           a.append(h)
           r+=1
       m.append(a)
       i+=1
   return(m)
#----------------------------------------------------------------------------#

print("for first matrix")
nr1=float(input("enter no. of rows :"))
nc1=float(input("enter no. of columns :"))

print("for second matrix")
nr2=float(input("enter no. of rows :"))
nc2=float(input("enter no. of columns :"))

p=matrixinput ()
print(p)
l=matrixinput ()
print(l)
if nc1!=nc2 :
   print (" Adition is not possible ")
else:
   v=0
   u=[]
   while v<nc2 :
       c=[]
       o=0
       while o<nc1 :
           j=l[v][o]+p[v][0]
           
           o+=1
           c.append(j)
       u.append(c)
       v+=1
    
   print(u) 



































