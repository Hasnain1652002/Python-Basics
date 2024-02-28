from random import randint
from secrets import randbelow


for i in range (6):
    x = randint(5,9)
    print("Attempt",i+1,"hop width : ",x)
    if (x < 10 and i!=5):
        print("sorry you did not make it. Try again. You have ", 5-i," hops left")
    elif i==5 :
        print("You seem to have come down with Hopalittle. Please go home and try again tomorrow")
    else:
        print("You have crossed the river after ",i+1," hop attempts. Have a great day at work!")
        break


