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
