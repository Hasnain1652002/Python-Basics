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
