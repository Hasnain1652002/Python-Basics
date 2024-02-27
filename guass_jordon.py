def guass_jordon():
    import numpy as np
    n=int(input("Enter The No. Of Variables : "))
    rows=n
    columns=n+1
    a=np.zeros((rows,columns))
    x=np.zeros(n)
    print ("Enter The Coefficient Of Augmented Matrix : ")
    for i in range (rows):
        for j in range (columns):
            a[i][j]=float(input('a['+str(i)+']['+str(j)+']='))
    print (a)
    for i in range (rows):
        if a[i][i]==0.0:
            
            break
        else :
            for j in range (rows):
                if i!=j :
                    r=a[j][i]/a[i][i]
                    for k in range (columns):
                        a[j][k]=a[j][k]-r*a[i][k]
    if a[i][i]==0.0:
        h="Not Possible By Guass Jordon Method!"
        print(h)
    else:
        print ("The Diagonal Matrix Is : ")
        print (a)
        print ("\nThe Values Of Variables Are : ")
        for i in range (n):
            x[i]=a[i][n]/a[i][i]
        for i in range (n):
            print("x%d=%0.2f" %(i+1,x[i]), end='\n')
            

guass_jordon()
