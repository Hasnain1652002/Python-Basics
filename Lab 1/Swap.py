def Swap(a,b,c,d):
    print("+++++ Before Swaping +++++")
    print(f"a={a},b={b},c={c},d={d}")
    
    a,b,c,d=d,c,b,a
    print()
    print("+++++ After Swaping +++++")
    print(f"a={a},b={b},c={c},d={d}")



if __name__ == "__main__":

    A=input("Enter value for a: ")
    B=input("Enter value for b: ")
    C=input("Enter value for c: ")
    D=input("Enter value for d: ")
    
    Swap(a=A,b=B,c=C,d=D)
