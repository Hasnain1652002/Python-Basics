def signup() :
    db = open("database.txt","r")
    fullname = input("Creat fullname : ")
    contact = input("Enter contact number : ")
    email = input("Enter your email id : ")
    dob = input("Enter date of birth  DD\MM\YYYY")
    password = input("Creat password : ")
    password1 = input("Confirm password : ")
    d = []
    f = []
    for i in db :
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d,f))
    if len(contact) != 10  and contact[0:1] != "0":
        print (" The mobile number should be 10 digit and starting from zero (For Example: 0XXXXXXXXX)")
    elif password[0:1]:


