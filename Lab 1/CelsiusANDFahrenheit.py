def CelsiusANDFahrenheit(Temperature,Scale):
    if Scale == "C":
        F = (float(Temperature) * 9/5) + 32
        print(f"Temperature in Celsius    : {Temperature} ")
        print(f"Temperature in Fahrenheit : {F} ")
    elif Scale == "F":
        C = (float(Temperature) - 32) * 5/9
        print(f"Temperature in Fahrenheit  : {Temperature} ")
        print(f"Temperature in Celsius     : {C} ")
    else:
        print("Scale not found :(")

if __name__ == "__main__":

    Scale=input("Select a Scale (C/F)    : ")
    Temperature=input("Enter Temperature : ")
    CelsiusANDFahrenheit(Temperature=Temperature,Scale=Scale)
