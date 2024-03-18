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
