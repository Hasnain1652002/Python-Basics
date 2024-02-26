def factorial (n):
    if n==0 :
        return (1)
    else:
        print (n,"-------------")
        return (n*factorial(n-1))
    print (n,"-------------")

a=factorial(3)
print(a)

def pwr (a,b):
    if b==0:
        return (1)
    else :
        return (a*pwr(a,b-1))



h=pwr(3,3)
print (h)



def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
##     else:
##         print("result is", result)
     finally:
         print("executing finally clause")
divide (40,4)         


try :
   z=int(input("numbers:"))
except ValueError:
    print("Input value is not no.")
else:
    print (z)















    
