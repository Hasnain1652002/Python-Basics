##=========================LAB-2 EXERCISES================================


##Exercise 1:
##(I)Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes inputs like height,
##width and depth from user and then calculate volume of the cube:
##volume = height ∗ width ∗ depth
##After calculating volume of cube, compare it with following ranges and print the relevant label:
##    Volume Range
##Label
##1 cm3 – 10 cm3
##Extra Small
##11 cm3 – 25 cm3
##Small
##26 cm3 – 75 cm3
##Medium
##76 cm3 – 100 cm3
##Large
##101 cm3 – 250 cm3
##Extra Large
##251 cm3 and above
##Extra-Extra Large

def cubeVolume(height,width,depth):
    volume = height*width*depth
    if volume >= 1 and volume <= 10:
        print(f"Volume={volume} cm^3 Extra Small !!!")
    elif volume >= 11 and volume <= 25:
        print(f"Volume={volume} cm^3 Small !!!")
    elif volume >= 26 and volume <= 75:
        print(f"Volume={volume} cm^3 Medium !!!")
    elif volume >= 76 and volume <= 100:
        print(f"Volume={volume} cm^3 Large !!!")
    elif volume >= 101 and volume <= 250:
        print(f"Volume={volume} cm^3 Extra Large !!!")
    elif volume >= 251:
        print(f"Volume={volume} cm^3 Extra-Extra Large !!!")
    else:
        print("Error :(")
    


if __name__ == "__main__":

    Height = float(input("Enter Height in cm  : "))
    Width  = float(input("Enter Width  in cm  : "))
    Depth  = float(input("Enter Depth  in cm  : "))
    cubeVolume(height=Height,width=Width,depth=Depth)


##(II)In a company ,worker efficiency is determined on the basis of the time required for a worker to complete a particular job.
##If the time taken by the worker is between 2-3 hours then the worker is said to be highly efficient. If the time required by the
##worker is between 3-4hours,then the worker is ordered to improve speed. If the time taken is between 4-5 hours ,
##the worker is given training to improve his speed ,and if the time taken by the worker is more than 5 hours ,
##then the worker haas to leave the company, If the time taken by the worker is input through the keyboard,find the efficiency of the worker.

def workerEfficiency(Time):
    
    if Time <= 3:
        print(f"Time={Time} hour/'s  Good Job Keep up the good work :)")
    elif Time > 3 and Time <= 4:
        print(f"Time={Time} hour/'s  You need to improve your speed ...")
    elif Time > 4 and Time <= 5:
        print(f"Time={Time} hour/'s  You will have to go through the training to improve your speed ...")
    elif Time > 5:
        print(f"Time={Time} hour/'s  You are Fired :(")
    else:
        print("Error :(")
    


if __name__ == "__main__":

    Time = float(input("Enter Time in hours  : "))
    workerEfficiency(Time=Time)


##(iii)The program must prompt the user for a username and password. The program should compare the password given by the user to a known password.
##If the password matches, the program should display “Welcome!” If it doesn’t match, the program should display “I don’t know you.
##Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123


def Login(Username,Password):
    savedPassword="abc$123"
    
    if Password.lower() == savedPassword.lower():
        print(f"Welcome {Username} :)")
    else:
        print("I don't know you :(")



if __name__ == "__main__":

    Username = input("Enter Your Username  : ")
    Password = input("Enter Your Password  : ")
    Login(Username=Username,Password=Password)


##Exercise 2:
##(i)What Would Python Print?
##>>> n = 3
##>>> while n >= 0:
##... n -= 1
##... print(n)

n = 3
while n >= 0:
     n -= 1
print(n)







##The code block will continue to run until n becomes < 0, since 0 is not greater than or equal to 0.
##(ii): What Would Python Print?
##>>> # typing Ctrl-C will stop infinite loops
##>>> n = 4
##>>> while n > 0:
##... n += 1
##... print(n)


n = 4
while n > 0:
    n += 1
print(n)






##(ii)Try the scenrio below:

##Make a program that lists the countries in the set clist = ['Canada','USA','Mexico','Australia']

def LoopList(List):
    for i in List:
        print(i)
 

if __name__ == "__main__":

    List = ['Canada','USA','Mexico','Australia'] 
    LoopList(List=List)

##1. Create a loop that counts from 0 to 100

def Count():
    for i in range(1,101):
        print(i,end=" ")
 

if __name__ == "__main__":
 
    Count()

##2. Make a multiplication table using a loop

def Table(Number):
    for i in range(1,11):
        print(f"{Number} x {i} = {Number*i}")
 

if __name__ == "__main__":
 
    Table(Number=9)

##3. Output the numbers 1 to 10 backwards using a loop

def CountBackward():
    for i in range(10,0,-1):
        print(i,end=" ")
 

if __name__ == "__main__":
 
    CountBackward()
##4. Create a loop that counts all even numbers to 10

def CountEven():
    for i in range(0,11,2):
        print(i,end=" ")
 

if __name__ == "__main__":
 
    CountEven()

##5. Create a loop that sums the numbers from 100 to 200

def Sum():
    sum = 0
    for i in range(100,201):
        sum+=i
    
    print(s)

if __name__ == "__main__":
 
    Sum()

##(iii) Try the exercise below:

##1. Make a program that lists the countries in the set below using a while loop. clist = ["Canada","USA","Mexico"]

def WhileLoopList(List):
    count=0
    while count<len(List):
        print(List[count])
        count+=1
 

if __name__ == "__main__":

    List = ["Canada","USA","Mexico"] 
    WhileLoopList(List=List)











    
