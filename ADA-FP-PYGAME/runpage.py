from gui import mainpage

while(True):
    print("Write exit to exit the program!")
    a = input("Enter your username: ")
    
    if (a == "Admin"):
        b = input("Enter your password: ")
        if(b == "password"):
            mainpage()
        else:
            print("Wrong password")
    elif (a == "exit"):
        break
    else:
        print("Wrong username")
